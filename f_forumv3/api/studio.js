import { createClient } from "@supabase/supabase-js";
import { cleanPage, looksSensitive, MAX_HTML } from "../server/output.js";
const LIMIT = 15;
class RequestError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}
const err = (status, message) => new RequestError(status, message);
function client(url, key) {
  return createClient(url, key, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
}
async function read(req) {
  if (req.body && typeof req.body === "object" && !Buffer.isBuffer(req.body)) {
    if (JSON.stringify(req.body).length > 100000)
      throw err(413, "Yêu cầu quá lớn.");
    return req.body;
  }
  let raw = typeof req.body === "string" ? req.body : "";
  if (!raw)
    for await (const chunk of req) {
      raw += chunk;
      if (raw.length > 100000) throw err(413, "Yêu cầu quá lớn.");
    }
  if (raw.length > 100000) throw err(413, "Yêu cầu quá lớn.");
  try {
    return JSON.parse(raw || "{}");
  } catch {
    throw err(400, "Dữ liệu không hợp lệ.");
  }
}
export default async function handler(req, res) {
  const send = (status, data) => {
    res.statusCode = status;
    res.setHeader("Content-Type", "application/json; charset=UTF-8");
    res.setHeader("Cache-Control", "no-store");
    res.end(JSON.stringify(data));
  };
  try {
    const {
      SUPABASE_URL: url,
      SUPABASE_ANON_KEY: anon,
      SUPABASE_SERVICE_ROLE_KEY: service,
      AI_BASE_URL: base,
      AI_API_KEY: key,
      AI_MODEL: model,
      ADMIN_USER_IDS: admins = "",
    } = process.env;
    const params = new URL(req.url, "http://studio.internal").searchParams;
    const action = params.get("action");
    const configured = Boolean(url && anon && service),
      ai = Boolean(configured && base && key && model);
    if (req.method === "GET" && action === "config")
      return send(200, {
        url: configured ? url : null,
        anon: configured ? anon : null,
        ai,
        limit: LIMIT,
      });
    if (!configured)
      throw err(
        503,
        "Máy chủ chưa được cấu hình. Bạn vẫn có thể dùng bản thử trên thiết bị.",
      );
    const db = client(url, service);
    const uuid = (s) =>
      typeof s === "string" &&
      /^[\da-f]{8}(-[\da-f]{4}){3}-[\da-f]{12}$/i.test(s);
    if (req.method === "GET" && action === "replies") {
      const post = params.get("post");
      if (!uuid(post)) throw err(400, "Bài viết không hợp lệ.");
      const { data, error } = await db
        .from("studio_replies")
        .select("id,author,body,created_at,studio_posts!inner(hidden)")
        .eq("post_id", post)
        .eq("studio_posts.hidden", false)
        .order("created_at")
        .limit(100);
      if (error) throw err(503, "Chưa tải được phản hồi.");
      return send(200, { replies: data.map(({ studio_posts, ...x }) => x) });
    }
    if (req.method === "GET" && action === "feed") {
      const { data, error } = await db
        .from("studio_posts")
        .select("id,category,title,body,author,created_at")
        .eq("hidden", false)
        .order("created_at", { ascending: false })
        .limit(60);
      if (error) throw err(503, "Chưa tải được thảo luận.");
      return send(200, { posts: data });
    }
    const token = (req.headers.authorization || "").match(
      /^Bearer (\S+)$/i,
    )?.[1];
    if (!token) throw err(401, "Đăng nhập để tiếp tục.");
    const {
      data: { user },
      error: authError,
    } = await client(url, anon).auth.getUser(token);
    if (authError || !user) throw err(401, "Phiên đăng nhập đã hết hạn.");
    if (!user.email_confirmed_at)
      throw err(403, "Xác nhận email trước khi tiếp tục.");
    const admin = admins
      .split(",")
      .map((s) => s.trim())
      .includes(user.id);
    const today = new Date().toISOString().slice(0, 10);
    if (req.method === "GET" && action === "me") {
      const { data, error } = await db
        .from("studio_usage")
        .select("used")
        .eq("user_id", user.id)
        .eq("day", today)
        .maybeSingle();
      if (error) throw err(503, "Chưa đọc được số lượt.");
      return send(200, {
        admin,
        used: data?.used || 0,
        limit: admin ? null : LIMIT,
      });
    }
    if (req.method === "GET" && action === "admin") {
      if (!admin) throw err(403, "Tài khoản này không có quyền quản trị.");
      const { data, error } = await db
        .from("studio_reports")
        .select("id,post_id,reason,created_at,studio_posts(title,hidden)")
        .order("created_at", { ascending: false })
        .limit(60);
      if (error) throw err(503, "Chưa tải được báo cáo.");
      return send(200, { reports: data });
    }
    if (req.method !== "POST") throw err(405, "Phương thức không hợp lệ.");
    const body = await read(req);
    if (action === "reply") {
      if (
        !uuid(body.post) ||
        typeof body.author !== "string" ||
        body.author.length > 40 ||
        typeof body.body !== "string" ||
        body.body.trim().length < 5 ||
        body.body.length > 2000 ||
        looksSensitive(body.body)
      )
        throw err(400, "Phản hồi không hợp lệ.");
      const { error } = await db.rpc("studio_add_reply", {
        p_user: user.id,
        p_post: body.post,
        p_body: body.body.trim(),
        p_author: body.author.trim() || "Thành viên",
      });
      if (error)
        throw err(
          error.code === "P0001" ? 429 : 503,
          "Chưa gửi được phản hồi; hãy kiểm tra bài viết và hạn mức.",
        );
      return send(201, { ok: true });
    }
    if (action === "post") {
      const { title, category, author, body: text } = body;
      if (
        !["Dev Q&A", "Showcase", "Drops", "Club Hub"].includes(category) ||
        typeof title !== "string" ||
        title.trim().length < 5 ||
        title.length > 120 ||
        typeof text !== "string" ||
        text.trim().length < 10 ||
        text.length > 3000 ||
        typeof author !== "string" ||
        author.length > 40 ||
        looksSensitive(`${title}\n${text}\n${author}`)
      )
        throw err(
          400,
          "Kiểm tra tiêu đề và nội dung. Không đăng khóa hoặc mật khẩu.",
        );
      const { error } = await db.rpc("studio_add_post", {
        p_user: user.id,
        p_title: title.trim(),
        p_body: text.trim(),
        p_category: category,
        p_author: author.trim() || "Thành viên",
      });
      if (error)
        throw err(
          error.code === "P0001" ? 429 : 503,
          error.code === "P0001"
            ? "Bạn đã đăng đủ số bài trong ngày."
            : "Chưa đăng được bài.",
        );
      return send(201, { ok: true });
    }
    if (action === "report") {
      if (
        !uuid(body.post) ||
        !["Spam", "Quấy rối", "Thông tin cá nhân", "Khác"].includes(body.reason)
      )
        throw err(400, "Báo cáo không hợp lệ.");
      const { error } = await db.rpc("studio_add_report", {
        p_user: user.id,
        p_post: body.post,
        p_reason: body.reason,
      });
      if (error)
        throw err(
          error.code === "23505" ? 409 : error.code === "P0001" ? 429 : 503,
          error.code === "23505"
            ? "Bạn đã báo cáo bài này."
            : error.code === "P0001"
              ? "Bạn đã gửi đủ số báo cáo trong ngày."
              : "Chưa gửi được báo cáo.",
        );
      return send(201, { ok: true });
    }
    if (action === "moderate") {
      if (!admin) throw err(403, "Tài khoản này không có quyền quản trị.");
      if (!uuid(body.post) || typeof body.hidden !== "boolean")
        throw err(400, "Thao tác không hợp lệ.");
      const { error } = await db
        .from("studio_posts")
        .update({ hidden: body.hidden })
        .eq("id", body.post);
      if (error) throw err(503, "Chưa cập nhật được bài.");
      return send(200, { ok: true });
    }
    if (action !== "generate") throw err(404, "Không tìm thấy thao tác.");
    if (!ai)
      throw err(503, "AI chưa được cấu hình. Có thể tạo từ mẫu trên thiết bị.");
    const { prompt, previous = "", context = "" } = body;
    if (
      typeof prompt !== "string" ||
      !prompt.trim() ||
      prompt.length > 6500 ||
      typeof previous !== "string" ||
      previous.length > MAX_HTML ||
      typeof context !== "string" ||
      context.length > 3000
    )
      throw err(400, "Nội dung trống hoặc vượt giới hạn.");
    if (looksSensitive(`${prompt}\n${previous}\n${context}`))
      throw err(400, "Hãy bỏ khóa hoặc mật khẩu trước khi gửi.");
    const endpoint = new URL(`${base.replace(/\/$/, "")}/chat/completions`);
    if (
      endpoint.protocol !== "https:" ||
      endpoint.username ||
      endpoint.password
    )
      throw err(503, "Máy chủ AI chưa được cấu hình đúng.");
    const { data: used, error } = await db.rpc("studio_reserve", {
      p_user: user.id,
      p_day: today,
      p_limit: admin ? null : LIMIT,
    });
    if (error) throw err(503, "Chưa kiểm tra được hạn mức.");
    if (used === -1)
      throw err(
        429,
        "Đã dùng 15 lượt AI hôm nay. Hạn mức đặt lại lúc 00:00 UTC.",
      );
    try {
      const upstream = await fetch(endpoint, {
        method: "POST",
        redirect: "error",
        signal: AbortSignal.timeout(47000),
        headers: {
          authorization: `Bearer ${key}`,
          "content-type": "application/json",
        },
        body: JSON.stringify({
          model,
          max_tokens: 5200,
          messages: [
            {
              role: "system",
              content:
                "Return only a complete single-file HTML/CSS static website, in Vietnamese unless requested otherwise. No scripts, forms, remote assets, iframes, credentials or external links. Put all CSS in one style element inside head, use responsive layouts, semantic HTML, visible focus and accessible contrast. Preserve requested sections from the previous version. Do not claim features that do not run. If a requested feature is dynamic, show a static layout and label it a prototype.",
            },
            {
              role: "user",
              content: JSON.stringify({
                request: prompt,
                reference: context,
                previous,
              }),
            },
          ],
        }),
      });
      if (!upstream.ok) throw Error("provider");
      const out = (await upstream.json()).choices?.[0]?.message?.content;
      if (typeof out !== "string" || !/<(?:html|main|body)\b/i.test(out))
        throw Error("invalid");
      return send(200, {
        html: cleanPage(out.replace(/^\s*```(?:html)?\s*|\s*```\s*$/gi, "")),
        used,
        limit: admin ? null : LIMIT,
      });
    } catch {
      const refund = await db.rpc("studio_refund", {
        p_user: user.id,
        p_day: today,
      });
      throw err(
        502,
        refund.error
          ? "Chưa tạo được bản xem. Trạng thái hạn mức chưa được xác nhận."
          : "Chưa tạo được bản xem. Lượt thử này đã được hoàn lại.",
      );
    }
  } catch (e) {
    return send(e instanceof RequestError ? e.status : 500, {
      error:
        e instanceof RequestError ? e.message : "Không xử lý được yêu cầu.",
    });
  }
}

import { looksSensitive } from "./sensitive.js";
export const makeProject = (prompt = "", context = "") => ({
  id: crypto.randomUUID(),
  name: prompt.trim().slice(0, 52) || "Dự án chưa đặt tên",
  created: new Date().toISOString(),
  updated: new Date().toISOString(),
  draft: prompt,
  context,
  html: "",
  previous: "",
  messages: [],
  pinned: false,
  archived: false,
  process: null,
});
const escape = (v) =>
  v.replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ],
  );
export function buildStarter(prompt) {
  if (looksSensitive(prompt))
    throw Error("Hãy bỏ khóa hoặc mật khẩu trước khi tạo bản mẫu.");
  const title = escape(
    prompt.trim().split("\n")[0].replace(/^Tạo /i, "").slice(0, 90) ||
      "Website đầu tiên",
  );
  return `<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>${title}</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#faf8ff;color:#241b3d;font-family:system-ui,sans-serif}header,main,footer{width:min(920px,calc(100% - 42px));margin:auto}header{display:flex;justify-content:space-between;align-items:center;padding:22px 0;border-bottom:1px solid #ded6f2}a{color:#4e2bb1}a:focus-visible{outline:2px solid #4e2bb1;outline-offset:4px}.hero{padding:clamp(52px,12vw,112px) 0 60px}.tag{font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:#4e2bb1}h1{font-size:clamp(2rem,7vw,4.8rem);letter-spacing:-.055em;line-height:1.03;margin:.24em 0 .4em;overflow-wrap:anywhere}p{line-height:1.65;max-width:58ch}.cta{display:inline-block;padding:12px 20px;border-radius:10px;background:#4e2bb1;color:white;text-decoration:none}article{border-top:1px solid #ded6f2;padding:30px 0}footer{padding:20px 0;border-top:1px solid #ded6f2;font-size:.875rem}
</style>
</head>
<body>
<header><strong>Website của bạn</strong><a href="#noi-dung">Nội dung</a></header>
<main><section class="hero"><p class="tag">Bản mẫu tĩnh</p><h1>${title}</h1><p>Đây là điểm bắt đầu. Hãy thử thay tiêu đề, chỉnh nội dung hoặc dùng bản mẫu để mô tả phiên bản tiếp theo.</p><a href="#noi-dung" class="cta">Xem nội dung</a></section><article id="noi-dung"><h2>Giới thiệu</h2><p>Viết ở đây điều bạn muốn người ghé thăm biết hoặc thực hiện đầu tiên.</p></article></main>
<footer>Website mẫu tạo bằng F‑FORUM</footer>
</body>
</html>`;
}
export function checkDocument(html) {
  const doc = new DOMParser().parseFromString(html, "text/html");
  const heading = Boolean(doc.querySelector("h1"));
  const title = Boolean(doc.title.trim());
  const viewport = Boolean(doc.querySelector('meta[name="viewport"]'));
  const targets = [...doc.querySelectorAll('a[href^="#"]')].every((a) =>
    doc.getElementById(a.getAttribute("href").slice(1)),
  );
  const active =
    Boolean(doc.querySelector("script,iframe,form,object,embed,link,base")) ||
    [...doc.querySelectorAll("*")].some((el) =>
      [...el.attributes].some(
        (a) =>
          a.name.startsWith("on") ||
          ["src", "srcset", "action"].includes(a.name) ||
          (a.name === "href" && a.value && !a.value.startsWith("#")),
      ),
    );
  return [
    [
      "Tiêu đề & heading",
      title && heading,
      "Có tiêu đề trang và một heading cấp một.",
    ],
    [
      "Viewport",
      viewport,
      "Kiểm tra có thẻ viewport; không thay thế kiểm thử nhiều thiết bị.",
    ],
    [
      "Liên kết nội bộ",
      targets,
      "Các anchor trỏ tới ID có thật trong tài liệu.",
    ],
    [
      "Nội dung chủ động",
      !active,
      "Không tìm thấy thẻ hoặc thuộc tính chủ động trong bản xem.",
    ],
  ];
}

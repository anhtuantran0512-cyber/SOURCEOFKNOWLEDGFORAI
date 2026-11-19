import React, { useEffect, useState } from "react";
import {
  ArrowUpRight,
  Flag,
  MessageSquare,
  Plus,
  Search,
  Shield,
} from "lucide-react";
import { communityCategories, demoPosts } from "./data.js";
import { Empty, PageTitle } from "./ui.jsx";
export default function Community({
  admin,
  config,
  call,
  user,
  setAuthOpen,
  notify,
  add,
}) {
  const [posts, setPosts] = useState([]),
    [selected, setSelected] = useState(null),
    [cat, setCat] = useState("Tất cả"),
    [query, setQuery] = useState(""),
    [error, setError] = useState(""),
    [compose, setCompose] = useState(false),
    [title, setTitle] = useState(""),
    [content, setContent] = useState(""),
    [category, setCategory] = useState("Dev Q&A"),
    [report, setReport] = useState(""),
    [sending, setSending] = useState(false),
    [reports, setReports] = useState([]),
    [reply, setReply] = useState(""),
    [replies, setReplies] = useState([]),
    [liked, setLiked] = useState(() => {
      try {
        return JSON.parse(localStorage.getItem("ff3-saved-posts")) || [];
      } catch {
        return [];
      }
    });
  const live = Boolean(config.url);
  const initialPost = new URLSearchParams(location.search).get("post");
  const load = () =>
    call("feed")
      .then((x) => setPosts(x.posts))
      .catch((e) => setError(e.message));
  useEffect(() => {
    if (initialPost)
      setSelected(
        (live ? posts : demoPosts).find((p) => p.id === initialPost) || null,
      );
  }, [initialPost, live, posts]);
  const loadReports = () =>
    call("admin")
      .then((x) => setReports(x.reports))
      .catch((e) => setError(e.message));
  useEffect(() => {
    if (admin) {
      if (user.admin) loadReports();
    } else if (live) load();
  }, [admin, live, user.admin, call]);
  useEffect(() => {
    let liveReply = true;
    setReplies([]);
    setReply("");
    if (live && selected)
      call(`replies&post=${selected.id}`)
        .then((x) => {
          if (liveReply) setReplies(x.replies);
        })
        .catch((e) => {
          if (liveReply) setError(e.message);
        });
    return () => {
      liveReply = false;
    };
  }, [live, selected?.id, call]);
  const authorized = (f) => (user.signed ? f() : setAuthOpen(true));
  const perform = async (f) => {
    setSending(true);
    setError("");
    try {
      await f();
    } catch (e) {
      setError(e.message);
    } finally {
      setSending(false);
    }
  };
  if (admin)
    return (
      <div className="container page">
        <PageTitle n="05" label="ADMIN" title="Quản trị cộng đồng">
          Xử lý báo cáo và ẩn bài vi phạm. Hạn mức AI thông thường không áp dụng
          cho tài khoản quản trị.
        </PageTitle>
        {!user.admin ? (
          <>
            <Empty icon={Shield} title="Yêu cầu tài khoản quản trị" />
            <button className="btn" onClick={() => setAuthOpen(true)}>
              Đăng nhập
            </button>
          </>
        ) : (
          <div className="resource-list">
            {reports.map((r) => (
              <article className="resource-row" key={r.id}>
                <Flag size={18} />
                <div>
                  <h2>
                    {r.studio_posts?.title || "Bài viết không còn tồn tại"}
                  </h2>
                  <p>
                    {r.reason} ·{" "}
                    {new Date(r.created_at).toLocaleDateString("vi")}
                  </p>
                </div>
                <button
                  className="btn"
                  disabled={sending}
                  onClick={() =>
                    perform(async () => {
                      await call("moderate", {
                        post: r.post_id,
                        hidden: !r.studio_posts?.hidden,
                      });
                      await loadReports();
                      notify("Đã cập nhật hiển thị.");
                    })
                  }
                >
                  {r.studio_posts?.hidden ? "Hiện lại" : "Ẩn bài"}
                </button>
              </article>
            ))}
            {!reports.length && !error && (
              <Empty icon={Flag} title="Chưa có báo cáo hiển thị" />
            )}
          </div>
        )}
        {error && (
          <p className="inline-error" role="alert">
            {error}
          </p>
        )}
      </div>
    );
  const filtered = (live ? posts : demoPosts).filter(
    (p) =>
      (cat === "Tất cả" || p.category === cat) &&
      (!query ||
        `${p.title} ${p.body}`.toLowerCase().includes(query.toLowerCase())),
  );
  const savePost = () => {
    const next = liked.includes(selected.id)
      ? liked.filter((id) => id !== selected.id)
      : [...liked, selected.id];
    setLiked(next);
    try {
      localStorage.setItem("ff3-saved-posts", JSON.stringify(next));
    } catch {}
    notify(
      next.includes(selected.id)
        ? "Đã lưu bài trên thiết bị."
        : "Đã bỏ lưu bài.",
    );
  };
  return (
    <div className="container page community">
      <PageTitle
        n="04"
        label="SOURCE OF KNOWLEDGE"
        title="Hỏi thật. Chia sẻ thật."
      >
        Thảo luận về code, xin góp ý cho dự án và ghi lại những gì nhóm sau cần
        biết.
      </PageTitle>
      <div className="community-tools">
        <label className="search-box">
          <Search size={16} />
          <input
            placeholder="Tìm thảo luận"
            aria-label="Tìm thảo luận"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </label>
        <button
          className="btn primary"
          onClick={() =>
            live
              ? authorized(() => setCompose(!compose))
              : notify("Diễn đàn chưa kết nối máy chủ.")
          }
        >
          <Plus size={16} /> Viết bài
        </button>
      </div>
      <div className="category-row community-filters">
        {["Tất cả", ...communityCategories].map((c) => (
          <button
            className={c === cat ? "active" : ""}
            key={c}
            onClick={() => {
              setCat(c);
              setSelected(null);
            }}
          >
            {c}
          </button>
        ))}
      </div>
      {!live && (
        <p className="context-note">
          Đây là bài minh họa, không phải hoạt động của thành viên. Đăng bài và
          báo cáo cần máy chủ.
        </p>
      )}
      {error && (
        <p role="alert" className="inline-error">
          {error}
        </p>
      )}
      {compose && (
        <form
          className="community-form"
          onSubmit={(e) => {
            e.preventDefault();
            perform(async () => {
              await call("post", {
                title,
                category,
                body: content,
                author: user.name.slice(0, 40),
              });
              setCompose(false);
              setTitle("");
              setContent("");
              await load();
              notify("Đã đăng bài.");
            });
          }}
        >
          <label>
            Chủ đề
            <select
              value={category}
              onChange={(e) => setCategory(e.target.value)}
            >
              {communityCategories.map((c) => (
                <option key={c}>{c}</option>
              ))}
            </select>
          </label>
          <label>
            Tiêu đề
            <input
              minLength={5}
              maxLength={120}
              required
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </label>
          <label>
            Nội dung
            <textarea
              minLength={10}
              maxLength={3000}
              rows={5}
              required
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder="Không đăng email cá nhân, lịch học hoặc khóa API."
            />
          </label>
          <button className="btn primary" disabled={sending}>
            Đăng công khai
          </button>
        </form>
      )}
      <div className="community-stage">
        <div className="topic-list">
          {filtered.map((p, i) => (
            <button
              key={p.id}
              className={selected?.id === p.id ? "active" : ""}
              onClick={() => {
                setSelected(p);
                setReport("");
                setError("");
              }}
            >
              <span className="eyebrow">
                {String(i + 1).padStart(2, "0")} / {p.category}
              </span>
              <strong>{p.title}</strong>
              <small>
                {p.author}
                {p.created_at
                  ? " · " + new Date(p.created_at).toLocaleDateString("vi")
                  : ""}
              </small>
              <ArrowUpRight size={17} />
            </button>
          ))}
          {!filtered.length && (
            <Empty icon={MessageSquare} title="Chưa có thảo luận phù hợp" />
          )}
        </div>
        <aside className="topic-detail">
          {selected ? (
            <>
              <span className="eyebrow">{selected.category}</span>
              <h2>{selected.title}</h2>
              <p className="topic-body">{selected.body}</p>
              <div className="topic-actions">
                <button className="btn" onClick={savePost}>
                  {liked.includes(selected.id) ? "Bỏ lưu" : "Lưu trên thiết bị"}
                </button>
                {["Drops", "Showcase", "Club Hub"].includes(
                  selected.category,
                ) && (
                  <button
                    className="btn"
                    onClick={() =>
                      add(
                        "",
                        `${selected.title}\nTham chiếu từ ${selected.category}. Tóm tắt: ${selected.body.slice(0, 1000)}`,
                      )
                    }
                  >
                    Dùng làm ngữ cảnh
                  </button>
                )}
                {live && (
                  <button
                    className="btn"
                    onClick={() =>
                      authorized(() => setReport(report ? "" : "Spam"))
                    }
                  >
                    <Flag size={14} /> Báo cáo
                  </button>
                )}
              </div>
              {report && (
                <form
                  className="report-form"
                  onSubmit={(e) => {
                    e.preventDefault();
                    perform(async () => {
                      await call("report", {
                        post: selected.id,
                        reason: report,
                      });
                      setReport("");
                      notify("Đã gửi báo cáo.");
                    });
                  }}
                >
                  <label className="sr-only" htmlFor="reason">
                    Lý do
                  </label>
                  <select
                    id="reason"
                    value={report}
                    onChange={(e) => setReport(e.target.value)}
                  >
                    {["Spam", "Quấy rối", "Thông tin cá nhân", "Khác"].map(
                      (r) => (
                        <option key={r}>{r}</option>
                      ),
                    )}
                  </select>
                  <button className="btn" disabled={sending}>
                    Gửi báo cáo
                  </button>
                </form>
              )}
              {live && (
                <div className="replies">
                  <h3>Phản hồi</h3>
                  {replies.map((r) => (
                    <div key={r.id}>
                      <b>{r.author}</b>
                      <p>{r.body}</p>
                    </div>
                  ))}
                  {!replies.length && <p>Chưa có phản hồi.</p>}
                  {user.signed ? (
                    <form
                      onSubmit={(e) => {
                        e.preventDefault();
                        perform(async () => {
                          await call("reply", {
                            post: selected.id,
                            body: reply,
                            author: user.name.slice(0, 40),
                          });
                          setReply("");
                          setReplies(
                            (await call(`replies&post=${selected.id}`)).replies,
                          );
                        });
                      }}
                    >
                      <label>
                        Viết phản hồi
                        <textarea
                          required
                          minLength={5}
                          maxLength={2000}
                          rows={3}
                          value={reply}
                          onChange={(e) => setReply(e.target.value)}
                        />
                      </label>
                      <button className="btn" disabled={sending}>
                        Gửi phản hồi
                      </button>
                    </form>
                  ) : (
                    <button className="btn" onClick={() => setAuthOpen(true)}>
                      Đăng nhập để trả lời
                    </button>
                  )}
                </div>
              )}
            </>
          ) : (
            <Empty icon={MessageSquare} title="Chọn một thảo luận">
              Nội dung sẽ mở ở đây để bạn đọc mà không mất vị trí trong danh
              sách.
            </Empty>
          )}
        </aside>
      </div>
    </div>
  );
}

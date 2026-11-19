import React, { useEffect, useRef, useState } from "react";
import { diffLines } from "diff";
import { strToU8, zipSync } from "fflate";
import {
  Archive,
  ArrowDownToLine,
  Check,
  Code2,
  ExternalLink,
  FileCode2,
  FolderOpen,
  Maximize2,
  Monitor,
  PanelRight,
  Pin,
  Plus,
  Search,
  Smartphone,
  SquareTerminal,
  X,
} from "lucide-react";
import { buildStarter, checkDocument } from "./project.js";
import { Composer, Empty, Mark } from "./ui.jsx";
function download(data, name, type) {
  const url = URL.createObjectURL(new Blob([data], { type }));
  const a = document.createElement("a");
  a.href = url;
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
export default function Workspace({
  projects,
  setProjects,
  project,
  select,
  update,
  add,
  config,
  session,
  user,
  setAuthOpen,
  call,
  notify,
  profile,
  me,
  pending,
  setPending,
  setMe,
}) {
  const [search, setSearch] = useState(""),
    [archived, setArchived] = useState(false),
    [view, setView] = useState("Chat"),
    [panel, setPanel] = useState("Diff"),
    [device, setDevice] = useState("Desktop"),
    [size, setSize] = useState(false),
    [rename, setRename] = useState(false),
    [name, setName] = useState(""),
    [split, setSplit] = useState(profile.diff === "Split"),
    [error, setError] = useState(""),
    [mobilePanel, setMobilePanel] = useState("Chat");
  const frame = useRef(null);
  const busyRef = useRef(false);
  useEffect(() => {
    setView(project?.html ? "Preview" : "Chat");
    setError("");
    setRename(false);
    setMobilePanel("Chat");
  }, [project?.id]);
  useEffect(() => {
    if (!size) return;
    const cb = (e) => {
      if (e.key === "Escape") setSize(false);
    };
    window.addEventListener("keydown", cb);
    return () => window.removeEventListener("keydown", cb);
  }, [size]);
  const diff = project?.html
    ? diffLines(project.previous || "", project.html)
    : [];
  const added = diff.reduce((n, x) => n + (x.added ? x.count : 0), 0),
    removed = diff.reduce((n, x) => n + (x.removed ? x.count : 0), 0);
  const list = projects
    .filter(
      (p) =>
        p.archived === archived &&
        p.name.toLowerCase().includes(search.toLowerCase()),
    )
    .sort(
      (a, b) =>
        Number(b.pinned) - Number(a.pinned) ||
        b.updated.localeCompare(a.updated),
    );
  const run = async (local) => {
    if (!project || !project.draft.trim() || pending || busyRef.current) return;
    if (!local && !session) {
      setAuthOpen(true);
      return;
    }
    const p = project;
    const prompt = p.draft.trim();
    setError("");
    busyRef.current = true;
    setPending(true);
    try {
      const result = local
        ? { html: buildStarter(prompt) }
        : await call("generate", {
            prompt,
            previous: p.html,
            context: p.context,
          });
      setProjects((items) =>
        items.map((item) =>
          item.id === p.id
            ? {
                ...item,
                draft: item.draft === p.draft ? "" : item.draft,
                html: result.html,
                previous: p.html,
                messages: [
                  ...p.messages,
                  {
                    prompt,
                    reply: local
                      ? "Đã dựng bản mẫu tĩnh. Bản này chỉ dùng nội dung đầu tiên làm tiêu đề; các phần còn lại là nội dung mẫu."
                      : "Đã tạo bản HTML/CSS. Mở Diff để xem các dòng thay đổi.",
                  },
                ].slice(-20),
                process: {
                  text: local
                    ? "Tạo bản mẫu trên thiết bị"
                    : "Tạo bản tĩnh qua AI",
                  status: "Hoàn tất",
                },
                updated: new Date().toISOString(),
              }
            : item,
        ),
      );
      if (!local)
        setMe((m) => ({ ...m, used: result.used, limit: result.limit }));
      setView("Preview");
    } catch (e) {
      setError(e.message);
      update(p.id, {
        process: { text: "Tạo bản tĩnh qua AI", status: "Thất bại" },
      });
    } finally {
      busyRef.current = false;
      setPending(false);
    }
  };
  const exportZip = () => {
    if (!project?.html) return;
    download(
      zipSync({
        "index.html": strToU8(project.html),
        "README.md": strToU8(
          "# F‑FORUM\n\nMở index.html bằng trình duyệt. Đây là website HTML/CSS tĩnh, không có máy chủ.\n",
        ),
      }),
      "f-forum-project.zip",
      "application/zip",
    );
    notify("Đã chuẩn bị tệp ZIP.");
  };
  const exportSetup = () => {
    download(
      zipSync({
        "README.md": strToU8("# Website\n\nMở index.html để xem dự án tĩnh.\n"),
        "PROJECT_CONTEXT.md": strToU8(
          "# Bối cảnh\n\nMục tiêu:\n\nĐối tượng:\n\nQuyết định kỹ thuật:\n",
        ),
        "TASKS.md": strToU8(
          "# Công việc\n\n- [ ] Kiểm tra link nội bộ\n- [ ] Xem trên điện thoại\n- [ ] Kiểm tra độ tương phản\n",
        ),
        ".cursor/rules/project.mdc": strToU8(
          "---\nalwaysApply: true\n---\nGiữ HTML có ngữ nghĩa. Không đưa khóa vào mã nguồn.\n",
        ),
      }),
      "f-forum-setup.zip",
      "application/zip",
    );
  };
  return (
    <div className="container workspace">
      <div className="work-top">
        <div>
          <span className="eyebrow">
            <span className="route-led" /> 03 / WORK SPACE
          </span>
          <h1>Work space</h1>
        </div>
        <div className="work-actions">
          <span className="local-label">
            <i /> {session ? "Dự án trên thiết bị" : "Phiên khách"}
          </span>
          <button onClick={exportSetup} className="btn setup-btn">
            Project setup
          </button>
          <button
            onClick={exportZip}
            disabled={!project?.html}
            className="btn primary"
          >
            <ArrowDownToLine size={16} /> Export ZIP
          </button>
        </div>
      </div>
      <div className="mobile-work-tabs tab-row">
        {["Lịch sử", "Chat", "Kiểm tra"].map((t) => (
          <button
            key={t}
            className={mobilePanel === t ? "active" : ""}
            onClick={() => setMobilePanel(t)}
          >
            {t}
          </button>
        ))}
      </div>
      <div className="work-grid" data-mobile={mobilePanel}>
        <aside className="work-history">
          <div className="work-pane-head">
            <strong>Phiên làm việc</strong>
            <button
              className="icon-button"
              onClick={() => add()}
              aria-label="Phiên mới"
            >
              <Plus size={18} />
            </button>
          </div>
          <div className="history-filter">
            <Search size={15} />
            <input
              aria-label="Tìm dự án"
              placeholder="Tìm dự án"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
          </div>
          <div className="history-toggle">
            <button
              className={!archived ? "active" : ""}
              onClick={() => setArchived(false)}
            >
              Gần đây
            </button>
            <button
              className={archived ? "active" : ""}
              onClick={() => setArchived(true)}
            >
              Lưu trữ
            </button>
          </div>
          {list.map((p) => (
            <button
              key={p.id}
              className={
                "history-item " + (p.id === project?.id ? "active" : "")
              }
              onClick={() => {
                select(p.id);
                setMobilePanel("Chat");
              }}
            >
              {p.pinned ? <Pin size={14} /> : <FolderOpen size={14} />}
              <span>
                {p.name}
                <small>{p.html ? "Có bản xem" : "Bản nháp"}</small>
              </span>
            </button>
          ))}
          {!list.length && (
            <p className="pane-note">
              {archived ? "Chưa có dự án lưu trữ." : "Không có dự án phù hợp."}
            </p>
          )}
        </aside>
        <section className="work-center">
          <div className="work-pane-head center-head">
            {project ? (
              rename ? (
                <form
                  className="rename"
                  onSubmit={(e) => {
                    e.preventDefault();
                    if (name.trim()) update(project.id, { name: name.trim() });
                    setRename(false);
                  }}
                >
                  <input
                    aria-label="Tên dự án"
                    maxLength={60}
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    autoFocus
                  />
                  <button className="icon-button" aria-label="Lưu tên">
                    <Check size={16} />
                  </button>
                </form>
              ) : (
                <button
                  className="project-name"
                  onClick={() => {
                    setName(project.name);
                    setRename(true);
                  }}
                  title="Đổi tên"
                >
                  {project.name}
                </button>
              )
            ) : (
              <strong>Dự án mới</strong>
            )}
            {project && (
              <details className="project-menu">
                <summary aria-label="Thao tác dự án">•••</summary>
                <div className="account-menu">
                  <button
                    onClick={() => {
                      update(project.id, { pinned: !project.pinned });
                    }}
                  >
                    <Pin size={14} />
                    {project.pinned ? "Bỏ ghim" : "Ghim"}
                  </button>
                  <button
                    onClick={() => {
                      update(project.id, { archived: !project.archived });
                    }}
                  >
                    <Archive size={14} />
                    {project.archived ? "Khôi phục" : "Lưu trữ"}
                  </button>
                  <button
                    onClick={() => {
                      if (confirm("Xóa dự án khỏi thiết bị này?"))
                        setProjects((p) =>
                          p.filter((x) => x.id !== project.id),
                        );
                    }}
                  >
                    <X size={14} /> Xóa
                  </button>
                </div>
              </details>
            )}
          </div>
          {!project ? (
            <div className="new-work">
              <Empty icon={SquareTerminal} title="Chưa chọn dự án">
                Tạo phiên mới hoặc mở lại dự án trong lịch sử.
              </Empty>
              <button className="btn primary" onClick={() => add()}>
                <Plus size={16} /> Tạo dự án
              </button>
            </div>
          ) : (
            <>
              <div className="tab-row work-view">
                {["Chat", "Preview", "Code"].map((v) => (
                  <button
                    className={view === v ? "active" : ""}
                    key={v}
                    onClick={() => setView(v)}
                  >
                    {v}
                  </button>
                ))}
                {profile.autoPreview === false && project.html && (
                  <small>Bản lưu trên thiết bị</small>
                )}
              </div>
              {view === "Chat" ? (
                <div className="work-thread">
                  <div className="intro-message">
                    <Mark size={28} busy={pending} />
                    <div>
                      <strong>Trợ lý tạo web</strong>
                      <p>
                        {config.ai
                          ? "Mô tả một website HTML/CSS. Đừng gửi khóa, thông tin học sinh hay dữ liệu riêng tư."
                          : "Bạn có thể dựng bản mẫu HTML/CSS ngay trên thiết bị. AI chưa được kết nối."}
                      </p>
                    </div>
                  </div>
                  {project.context && (
                    <div className="context-note">
                      Ngữ cảnh: {project.context}
                    </div>
                  )}
                  {project.messages.map((m, i) => (
                    <div className="exchange" key={i}>
                      <p>{m.prompt}</p>
                      <p>{m.reply}</p>
                    </div>
                  ))}
                  {pending && <p role="status">Đang tạo bản xem…</p>}
                </div>
              ) : view === "Code" ? (
                <div className="code-area">
                  {project.html ? (
                    <pre style={{ fontSize: profile.font }}>{project.html}</pre>
                  ) : (
                    <Empty icon={Code2} title="Chưa có mã nguồn" />
                  )}
                </div>
              ) : (
                <div className={size ? "preview preview-full" : "preview"}>
                  <div className="preview-toolbar">
                    <button
                      className={
                        "icon-button " + (device === "Desktop" ? "active" : "")
                      }
                      aria-label="Xem desktop"
                      onClick={() => setDevice("Desktop")}
                    >
                      <Monitor size={16} />
                    </button>
                    <button
                      className={
                        "icon-button " + (device === "Mobile" ? "active" : "")
                      }
                      aria-label="Xem điện thoại"
                      onClick={() => setDevice("Mobile")}
                    >
                      <Smartphone size={16} />
                    </button>
                    <button
                      className="icon-button expand"
                      aria-label={
                        size ? "Đóng toàn màn hình" : "Xem toàn màn hình"
                      }
                      onClick={() => setSize(!size)}
                    >
                      {size ? <X size={16} /> : <Maximize2 size={16} />}
                    </button>
                  </div>
                  {project.html ? (
                    <iframe
                      ref={frame}
                      sandbox=""
                      title="Bản xem website tĩnh"
                      className={device.toLowerCase()}
                      srcDoc={project.html}
                    />
                  ) : (
                    <Empty icon={Monitor} title="Chưa có bản xem" />
                  )}
                </div>
              )}
              <div className="work-composer">
                {error && (
                  <p role="alert" className="inline-error">
                    {error}
                  </p>
                )}
                <Composer
                  value={project.draft}
                  onChange={(draft) => update(project.id, { draft })}
                  onSubmit={() => run(!config.ai)}
                  busy={pending}
                  foot={
                    <>
                      <FileCode2 size={14} />{" "}
                      {config.ai ? "AI · HTML/CSS" : "Mẫu cục bộ · HTML/CSS"}
                    </>
                  }
                />
                <div className="composer-bottom">
                  <button
                    className="link-button"
                    disabled={!project.draft.trim() || pending}
                    onClick={() => run(true)}
                  >
                    Tạo từ mẫu cục bộ
                  </button>
                  <span>
                    {me?.admin
                      ? "Admin · không giới hạn lượt tài khoản"
                      : me
                        ? `${me.used}/${me.limit} lượt hôm nay`
                        : config.ai
                          ? "AI cần đăng nhập"
                          : "Không gọi API"}
                  </span>
                </div>
              </div>
            </>
          )}
        </section>
        <aside className="work-inspector">
          <div className="work-pane-head">
            <strong>Kiểm tra dự án</strong>
            <PanelRight size={16} />
          </div>
          <div className="tab-row">
            {["Diff", "Checks"].map((t) => (
              <button
                className={panel === t ? "active" : ""}
                key={t}
                onClick={() => setPanel(t)}
              >
                {t}
              </button>
            ))}
          </div>
          {panel === "Diff" ? (
            project?.html ? (
              <>
                <div className="diff-summary">
                  <FileCode2 size={15} /> index.html{" "}
                  <span>
                    <b>+{added}</b> <i>−{removed}</i>
                  </span>
                </div>
                <button
                  className="btn diff-mode"
                  onClick={() => setSplit(!split)}
                >
                  {split ? "Split" : "Unified"}
                </button>
                {split ? (
                  <div
                    className="split-diff"
                    style={{ fontSize: profile.font }}
                  >
                    <pre>{project.previous || "Chưa có bản trước"}</pre>
                    <pre>{project.html}</pre>
                  </div>
                ) : (
                  <pre className="diff-code" style={{ fontSize: profile.font }}>
                    {diff.map((d, i) => (
                      <span
                        className={d.added ? "plus" : d.removed ? "minus" : ""}
                        key={i}
                      >
                        {d.value
                          .split(/(?<=\n)/)
                          .map(
                            (l) =>
                              `${d.added ? "+" : d.removed ? "−" : " "} ${l}`,
                          )
                          .join("")}
                      </span>
                    ))}
                  </pre>
                )}
              </>
            ) : (
              <p className="pane-note">Tạo bản đầu tiên để xem thay đổi.</p>
            )
          ) : project?.html ? (
            <>
              <ul className="check-list">
                {checkDocument(project.html).map(([name, pass, desc]) => (
                  <li key={name}>
                    <span className={pass ? "check-pass" : "check-fail"}>
                      {pass ? <Check size={14} /> : <X size={14} />}
                    </span>
                    <div>
                      <b>{name}</b>
                      <small>{desc}</small>
                    </div>
                  </li>
                ))}
              </ul>
              <p className="pane-note">
                Không chạy Build, Lint hoặc Unit tests cho HTML tĩnh. Không xác
                nhận đã quét bí mật.
              </p>
            </>
          ) : (
            <p className="pane-note">Chưa có tài liệu để kiểm tra.</p>
          )}
          <div className="inspector-foot">
            <strong>Processes</strong>
            <p role="status">
              {pending
                ? "Đang chạy yêu cầu tạo bản xem…"
                : project?.process
                  ? `${project.process.status} · ${project.process.text}`
                  : "Chưa có tiến trình."}
            </p>
            <strong>Connectors</strong>
            <p>GitHub chưa kết nối.</p>
          </div>
        </aside>
      </div>
    </div>
  );
}

import React, { lazy, Suspense, useCallback, useEffect, useState } from "react";
import {
  ArrowDown,
  ArrowRight,
  ArrowUpRight,
  BookOpen,
  Braces,
  ChevronDown,
  Code2,
  Compass,
  FolderOpen,
  Gamepad2,
  Globe,
  LayoutDashboard,
  LogIn,
  LogOut,
  Moon,
  Plus,
  Settings,
  Shield,
  ShoppingBag,
  Sparkles,
  Sun,
  Users,
} from "lucide-react";
import {
  Art,
  Composer,
  Empty,
  Mark,
  Reveal,
  featureItems,
  navItems,
} from "./ui.jsx";
import { demoPosts, quick, templates } from "./data.js";
import { makeProject } from "./project.js";
import "./studio.css";
const Workspace = lazy(() => import("./Workspace.jsx"));
const Explore = lazy(() => import("./Explore.jsx"));
const Community = lazy(() => import("./Community.jsx"));
const SettingsPage = lazy(() => import("./Settings.jsx"));
const read = (key, initial) => {
  try {
    return JSON.parse(localStorage.getItem(key)) ?? initial;
  } catch {
    return initial;
  }
};
function useLocal(key, initial) {
  const [value, put] = useState(() => read(key, initial));
  useEffect(() => {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch {
      /* quota can be reached */
    }
  }, [key, value]);
  return [value, put];
}
const quickIcons = [
  Globe,
  LayoutDashboard,
  Users,
  BookOpen,
  Gamepad2,
  Code2,
  Braces,
  ShoppingBag,
];
export default function Studio() {
  const [route, setRoute] = useState(location.pathname),
    [theme, setTheme] = useLocal("ff3-theme", "light"),
    [profile, setProfile] = useLocal("ff3-profile", {
      name: "",
      handle: "",
      bio: "",
      club: "",
      github: "",
      diff: "Unified",
      font: 13,
    }),
    [projects, setProjects] = useLocal("ff3-projects", []),
    [saved, setSaved] = useLocal("ff3-saved", []),
    [active, setActive] = useLocal("ff3-active", null);
  const [pending, setPending] = useState(false),
    [authOpen, setAuthOpen] = useState(
      new URLSearchParams(location.search).has("auth"),
    ),
    [config, setConfig] = useState({ ai: false, limit: 15 }),
    [auth, setAuth] = useState(null),
    [session, setSession] = useState(null),
    [me, setMe] = useState(null),
    [notice, setNotice] = useState("");
  const go = useCallback((path) => {
    const change = () => {
      history.pushState({}, "", path);
      setRoute(path.split("?")[0]);
      window.scrollTo({ top: 0, behavior: "instant" });
    };
    if (
      document.startViewTransition &&
      !matchMedia("(prefers-reduced-motion: reduce)").matches
    )
      document.startViewTransition(change);
    else change();
  }, []);
  useEffect(() => {
    const back = () => {
      setRoute(location.pathname);
      window.scrollTo(0, 0);
    };
    window.addEventListener("popstate", back);
    return () => window.removeEventListener("popstate", back);
  }, []);
  useEffect(() => {
    document.documentElement.dataset.studioTheme = theme;
    return () => delete document.documentElement.dataset.studioTheme;
  }, [theme]);
  useEffect(() => {
    document.title = `${navItems.find(([, path]) => path === route)?.[0] || { "/settings": "Cài đặt", "/admin": "Quản trị" }[route] || "Trang không tồn tại"} · F‑FORUM`;
  }, [route]);
  useEffect(() => {
    let sub,
      live = true;
    fetch("/api/studio?action=config")
      .then((r) => r.json())
      .then(async (c) => {
        if (!live) return;
        setConfig(c);
        if (c.url && c.anon) {
          const { createClient } = await import("@supabase/supabase-js");
          if (!live) return;
          const a = createClient(c.url, c.anon);
          setAuth(a);
          sub = a.auth.onAuthStateChange((_, s) => setSession(s)).data
            .subscription;
        }
      })
      .catch(() => {});
    return () => {
      live = false;
      sub?.unsubscribe();
    };
  }, []);
  const call = useCallback(
    async (action, body) => {
      const response = await fetch(`/api/studio?action=${action}`, {
        method: body ? "POST" : "GET",
        headers: {
          ...(body ? { "Content-Type": "application/json" } : {}),
          ...(session
            ? { Authorization: `Bearer ${session.access_token}` }
            : {}),
        },
        ...(body ? { body: JSON.stringify(body) } : {}),
      });
      const data = await response.json();
      if (!response.ok) throw Error(data.error || "Yêu cầu thất bại.");
      return data;
    },
    [session],
  );
  useEffect(() => {
    let live = true;
    setMe(null);
    if (session)
      call("me")
        .then((m) => {
          if (live) setMe(m);
        })
        .catch(() => {});
    return () => {
      live = false;
    };
  }, [session, call]);
  useEffect(() => {
    if (!notice) return;
    const id = setTimeout(() => setNotice(""), 4200);
    return () => clearTimeout(id);
  }, [notice]);
  const add = (prompt = "", context = "") => {
    const project = makeProject(prompt, context);
    setProjects((p) => [project, ...p]);
    setActive(project.id);
    go("/workspace");
    return project;
  };
  const update = (id, patch) =>
    setProjects((p) =>
      p.map((x) =>
        x.id === id ? { ...x, ...patch, updated: new Date().toISOString() } : x,
      ),
    );
  const select = (id) => {
    setActive(id);
    if (route != "/workspace") go("/workspace");
  };
  const toggleSave = (id) =>
    setSaved((s) => (s.includes(id) ? s.filter((x) => x !== id) : [...s, id]));
  const user = {
    name:
      profile.name ||
      session?.user?.user_metadata?.name ||
      (session ? "Thành viên" : "Khách"),
    signed: !!session,
    admin: me?.admin === true,
  };
  const shared = {
    go,
    config,
    call,
    session,
    user,
    me,
    setAuthOpen,
    theme,
    notify: setNotice,
    profile,
    setProfile,
    add,
    saved,
    toggleSave,
  };
  return (
    <div className="studio">
      <a href="#studio-main" className="skip">
        Chuyển đến nội dung chính
      </a>
      <header className="navbar">
        <div className="nav-inner">
          <a className="logo" href="/" aria-label="F‑FORUM — Landing page">
            <Mark busy={pending} />
          </a>
          <nav aria-label="Chính" className="primary-nav">
            {navItems.map(([label, path]) => (
              <a
                key={path}
                className={route === path ? "current" : ""}
                aria-current={route === path ? "page" : undefined}
                href={path}
                onClick={(e) => {
                  if (!e.metaKey && !e.ctrlKey && !e.shiftKey && !e.altKey) {
                    e.preventDefault();
                    go(path);
                  }
                }}
              >
                {label}
              </a>
            ))}
          </nav>
          <div className="nav-end">
            <button
              className="icon-button theme-toggle"
              aria-label={theme === "dark" ? "Giao diện sáng" : "Giao diện tối"}
              onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
            >
              {theme === "dark" ? <Sun size={17} /> : <Moon size={17} />}
            </button>
            <details className="account">
              <summary aria-label={`Tài khoản: ${user.name}`}>
                <span className="avatar">{user.name[0]?.toUpperCase()}</span>
                <span className="account-name">{user.name}</span>
                <ChevronDown size={13} />
              </summary>
              <div
                className="account-menu"
                onClick={(e) => {
                  if (e.target.closest("button"))
                    e.currentTarget.parentElement.open = false;
                }}
              >
                <b>{user.name}</b>
                <button onClick={() => go("/settings")}>
                  <Settings size={16} /> Cài đặt & hồ sơ
                </button>
                <button onClick={() => go("/saved")}>
                  <BookOpen size={16} /> Tài nguyên đã lưu
                </button>
                {user.admin && (
                  <button onClick={() => go("/admin")}>
                    <Shield size={16} /> Quản trị
                  </button>
                )}
                {session ? (
                  <button onClick={() => auth?.auth.signOut()}>
                    <LogOut size={16} /> Đăng xuất
                  </button>
                ) : (
                  <button onClick={() => setAuthOpen(true)}>
                    <LogIn size={16} /> Đăng nhập
                  </button>
                )}
              </div>
            </details>
          </div>
        </div>
      </header>
      <main id="studio-main" tabIndex={-1}>
        <Suspense
          fallback={
            <div className="loading" role="status">
              Đang mở trang…
            </div>
          }
        >
          {route === "/home" ? (
            <Home
              projects={projects}
              select={select}
              go={go}
              add={add}
              call={call}
              live={!!config.url}
            />
          ) : route === "/workspace" ? (
            <Workspace
              {...shared}
              projects={projects}
              setProjects={setProjects}
              project={projects.find((x) => x.id === active)}
              select={select}
              update={update}
              pending={pending}
              setPending={setPending}
              setMe={setMe}
            />
          ) : route === "/explore" || route === "/saved" ? (
            <Explore {...shared} key={route} savedOnly={route === "/saved"} />
          ) : route === "/community" || route === "/admin" ? (
            <Community {...shared} key={route} admin={route === "/admin"} />
          ) : route === "/settings" ? (
            <SettingsPage
              {...shared}
              setTheme={setTheme}
              projects={projects}
              clearLocal={() => {
                setProjects([]);
                setActive(null);
                setSaved([]);
                setProfile({
                  name: "",
                  handle: "",
                  bio: "",
                  club: "",
                  github: "",
                  diff: "Unified",
                  font: 13,
                });
              }}
            />
          ) : (
            <div className="container">
              <Empty title="Không tìm thấy trang" />
              <button className="btn" onClick={() => go("/home")}>
                Về Home
              </button>
            </div>
          )}
        </Suspense>
      </main>
      {authOpen && <AuthDialog auth={auth} close={() => setAuthOpen(false)} />}
      <div className={notice ? "toast" : "sr-only"} role="status">
        {notice}
      </div>
    </div>
  );
}
function AuthDialog({ auth, close }) {
  const [email, setEmail] = useState(""),
    [message, setMessage] = useState(""),
    [sending, setSending] = useState(false);
  useEffect(() => {
    const f = (e) => {
      if (e.key === "Escape") close();
    };
    window.addEventListener("keydown", f);
    return () => window.removeEventListener("keydown", f);
  }, [close]);
  return (
    <div className="overlay">
      <section
        role="dialog"
        aria-modal="true"
        aria-labelledby="auth-title"
        className="dialog"
      >
        <Mark />
        <h2 id="auth-title">Đăng nhập F‑FORUM</h2>
        <p>
          {auth
            ? "Nhận liên kết đăng nhập qua email. Không cần đặt mật khẩu."
            : "Chưa có dịch vụ đăng nhập trong bản xem này. Bạn vẫn có thể xem mẫu và tạo dự án cục bộ."}
        </p>
        {auth && (
          <form
            onSubmit={async (e) => {
              e.preventDefault();
              setSending(true);
              try {
                const { error } = await auth.auth.signInWithOtp({
                  email,
                  options: { emailRedirectTo: location.origin + "/home" },
                });
                setMessage(
                  error
                    ? "Không gửi được liên kết. Hãy thử lại sau."
                    : "Kiểm tra email để tiếp tục.",
                );
              } catch {
                setMessage("Không gửi được liên kết.");
              } finally {
                setSending(false);
              }
            }}
          >
            <label>
              Email
              <input
                autoFocus
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </label>
            <button className="btn primary" disabled={sending}>
              {sending ? "Đang gửi…" : "Gửi liên kết"}
            </button>
          </form>
        )}
        <p role="status">{message}</p>
        <button className="btn" onClick={close} autoFocus={!auth}>
          Đóng
        </button>
      </section>
    </div>
  );
}
function Home({ projects, select, go, add, call, live }) {
  const [briefs, setBriefs] = useState([]);
  useEffect(() => {
    let mounted = true;
    if (live)
      call("feed")
        .then((data) => {
          if (mounted) setBriefs(data.posts.slice(0, 2));
        })
        .catch(() => {});
    return () => {
      mounted = false;
    };
  }, [live, call]);
  const [draft, setDraft] = useState("");
  const [blueprint, setBlueprint] = useState(null);
  const [purpose, setPurpose] = useState("");
  const [audience, setAudience] = useState("");
  const recent = projects
    .filter((x) => !x.archived)
    .sort((a, b) => b.updated.localeCompare(a.updated))
    .slice(0, 5);
  return (
    <div className="container home">
      <div className="home-top">
        <div className="eyebrow">
          <span className="route-led" /> 01 / HOME LAUNCHPAD
        </div>
        <a href="#discover" className="minor-link">
          Khám phá F‑FORUM <ArrowDown size={13} />
        </a>
      </div>
      <section className="hero">
        <div className="hero-content">
          <div className="hero-tag">
            <Sparkles size={13} /> KHÔNG GIAN TẠO WEB
          </div>
          <h1>
            Từ ý tưởng,
            <br />
            <span>thành website.</span>
          </h1>
          <p>
            Viết vài dòng để bắt đầu. Xem thử, chỉnh sửa và mang mã nguồn theo
            khi bạn muốn.
          </p>
          <Composer
            home
            value={draft}
            onChange={setDraft}
            onSubmit={() => add(draft)}
            foot={
              <>
                <Braces size={14} /> Bản nháp của bạn
              </>
            }
          />
          <div className="hero-hint">
            Không gửi AI cho đến khi bạn xác nhận trong Work space.
          </div>
        </div>
        <Art />
      </section>
      <section className="quick-block">
        <div className="eyebrow">BẮT ĐẦU NHANH</div>
        <div className="quick-rail">
          {quick.map(([label, type], i) => {
            const Icon = quickIcons[i];
            return (
              <button
                className={blueprint?.[0] === label ? "selected" : ""}
                key={label}
                onClick={() => {
                  setBlueprint([label, type]);
                  setPurpose("");
                  setAudience("");
                  if (!draft.trim()) setDraft(`Tạo ${type}.`);
                }}
              >
                <Icon size={15} />
                {label}
              </button>
            );
          })}
        </div>
        {blueprint && (
          <form
            className="blueprint"
            onSubmit={(e) => {
              e.preventDefault();
              setDraft(
                `Tạo ${blueprint[1]}.\nMục đích: ${purpose.trim()}.\nĐối tượng: ${audience.trim()}.\nƯu tiên bố cục dễ đọc, dùng tốt trên điện thoại.`,
              );
              setBlueprint(null);
              document.getElementById("home-prompt")?.focus();
            }}
          >
            <label>
              Mục đích
              <input
                required
                maxLength={250}
                value={purpose}
                onChange={(e) => setPurpose(e.target.value)}
                placeholder="Ví dụ: tuyển thành viên mới"
              />
            </label>
            <label>
              Ai sẽ sử dụng?
              <input
                required
                maxLength={250}
                value={audience}
                onChange={(e) => setAudience(e.target.value)}
                placeholder="Ví dụ: học sinh trong trường"
              />
            </label>
            <button className="btn primary">Điền prompt</button>
            <button
              className="btn"
              type="button"
              onClick={() => setBlueprint(null)}
            >
              Đóng
            </button>
          </form>
        )}
      </section>
      <section className="recent-section">
        <div className="section-heading">
          <div>
            <span className="eyebrow">TIẾP TỤC LÀM VIỆC</span>
            <h2>Dự án gần đây</h2>
          </div>
          <button className="link-button" onClick={() => go("/workspace")}>
            Mở Work space <ArrowUpRight size={15} />
          </button>
        </div>
        <div className="recent-rail">
          {recent.map((p) => (
            <button
              className="project-tile"
              key={p.id}
              onClick={() => select(p.id)}
            >
              <span className="tile-icon">
                <FolderOpen size={18} />
              </span>
              <strong>{p.name}</strong>
              <small>
                {p.html ? "Có bản xem" : "Bản nháp"} ·{" "}
                {new Date(p.updated).toLocaleDateString("vi")}
              </small>
              <ArrowUpRight size={15} className="tile-arrow" />
            </button>
          ))}
          <button className="project-tile new-tile" onClick={() => add()}>
            <span className="tile-icon">
              <Plus size={18} />
            </span>
            <strong>Tạo dự án</strong>
            <small>
              {recent.length
                ? "Bắt đầu một phiên mới"
                : "Dự án trên thiết bị này sẽ xuất hiện ở đây."}
            </small>
          </button>
        </div>
      </section>
      <section id="discover" className="discover">
        <Reveal>
          <div className="section-heading">
            <div>
              <span className="eyebrow">BÊN TRONG F‑FORUM</span>
              <h2>Từ mẫu đến sản phẩm.</h2>
            </div>
          </div>
        </Reveal>
        {featureItems.map(([n, title, desc, Icon, path]) => (
          <Reveal key={path}>
            <button className="feature-row" onClick={() => go(path)}>
              <span className="eyebrow">{n}</span>
              <Icon size={23} />
              <strong>{title}</strong>
              <span>{desc}</span>
              <ArrowUpRight size={20} />
            </button>
          </Reveal>
        ))}
      </section>
      <section className="home-briefs">
        <div>
          <span className="eyebrow">TỪ THƯ VIỆN</span>
          <h2>Mẫu trong kho</h2>
          {templates.slice(0, 2).map((t) => (
            <a
              key={t.id}
              href={`/explore?template=${t.id}`}
              onClick={(e) => {
                e.preventDefault();
                go(`/explore?template=${t.id}`);
              }}
            >
              {t.title}
              <ArrowUpRight size={14} />
            </a>
          ))}
        </div>
        <div>
          <span className="eyebrow">
            {live ? "CỘNG ĐỒNG" : "THẢO LUẬN MINH HỌA"}
          </span>
          <h2>Đọc và trao đổi</h2>
          {(live ? briefs : demoPosts.slice(0, 2)).map((p) => (
            <a
              key={p.id}
              href={`/community?post=${p.id}`}
              onClick={(e) => {
                e.preventDefault();
                go(`/community?post=${p.id}`);
              }}
            >
              {p.title}
              <ArrowUpRight size={14} />
            </a>
          ))}
          {live && !briefs.length && <p>Chưa có bài để hiển thị.</p>}
        </div>
      </section>
      <footer className="studio-footer">
        <a href="/" aria-label="Về landing">
          <Mark size={28} />
        </a>
        <span>F‑FORUM / Studio</span>
        <a
          href="/settings"
          onClick={(e) => {
            e.preventDefault();
            go("/settings");
          }}
        >
          Dữ liệu & quyền riêng tư
        </a>
      </footer>
    </div>
  );
}

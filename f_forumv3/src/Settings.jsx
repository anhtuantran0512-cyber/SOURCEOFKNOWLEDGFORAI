import React, { useState } from "react";
import {
  ArrowDownToLine,
  Brain,
  Database,
  Github,
  Layout,
  UserRound,
} from "lucide-react";
import { PageTitle } from "./ui.jsx";
const sections = [
  ["Hồ sơ & tài khoản", UserRound],
  ["AI & mô hình", Brain],
  ["Tùy chọn Work space", Layout],
  ["Kết nối", Github],
  ["Dữ liệu & quyền riêng tư", Database],
];
export default function SettingsPage({
  profile,
  setProfile,
  config,
  user,
  me,
  theme,
  setTheme,
  setAuthOpen,
  projects,
  saved,
  clearLocal,
  notify,
}) {
  const [tab, setTab] = useState(0);
  const patch = (k, v) => setProfile((p) => ({ ...p, [k]: v }));
  const text = (key, label, max) => (
    <label>
      {label}
      <input
        value={profile[key] || ""}
        maxLength={max}
        onChange={(e) => patch(key, e.target.value)}
      />
    </label>
  );
  const exportData = () => {
    const url = URL.createObjectURL(
      new Blob([JSON.stringify({ profile, projects, saved }, null, 2)], {
        type: "application/json",
      }),
    );
    const a = document.createElement("a");
    a.href = url;
    a.download = "fforum-local-data.json";
    a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return (
    <div className="container page">
      <PageTitle n="05" label="SETTINGS" title="Cài đặt">
        Tùy chỉnh hồ sơ, công cụ và dữ liệu trên thiết bị này.
      </PageTitle>
      <div className="settings-grid">
        <nav aria-label="Cài đặt">
          {sections.map(([label, Icon], i) => (
            <button
              key={label}
              className={tab === i ? "active" : ""}
              onClick={() => setTab(i)}
            >
              <Icon size={18} /> {label}
            </button>
          ))}
        </nav>
        <section className="settings-pane">
          <h2>{sections[tab][0]}</h2>
          {tab === 0 ? (
            <>
              <p>
                {user.signed
                  ? "Đang đăng nhập. Hồ sơ bên dưới chỉ lưu trên thiết bị."
                  : "Bạn đang dùng phiên khách."}
              </p>
              {!user.signed && (
                <button className="btn" onClick={() => setAuthOpen(true)}>
                  Đăng nhập
                </button>
              )}
              {text("name", "Tên hiển thị", 40)}
              {text("handle", "Handle", 32)}
              {text("club", "Trường hoặc CLB (không bắt buộc)", 60)}
              {text("github", "Trang GitHub", 120)}
              <label>
                Giới thiệu
                <textarea
                  value={profile.bio || ""}
                  maxLength={240}
                  rows={3}
                  onChange={(e) => patch("bio", e.target.value)}
                />
              </label>
            </>
          ) : tab === 1 ? (
            <>
              <p>
                {config.ai
                  ? "AI đã cấu hình phía máy chủ."
                  : "AI chưa được cấu hình ở môi trường này."}
              </p>
              <p>
                Model do máy chủ chọn. Khóa cá nhân chưa được hỗ trợ; không dán
                khóa vào prompt hoặc hồ sơ.
              </p>
            </>
          ) : tab === 2 ? (
            <>
              <label>
                Diff mặc định
                <select
                  value={profile.diff}
                  onChange={(e) => patch("diff", e.target.value)}
                >
                  <option>Unified</option>
                  <option>Split</option>
                </select>
              </label>
              <label>
                Cỡ chữ mã nguồn
                <input
                  type="range"
                  min="11"
                  max="20"
                  value={profile.font}
                  onChange={(e) => patch("font", Number(e.target.value))}
                />
                <span>{profile.font}px</span>
              </label>
              <label>
                Giao diện
                <select
                  value={theme}
                  onChange={(e) => setTheme(e.target.value)}
                >
                  <option value="light">Sáng</option>
                  <option value="dark">Tối</option>
                </select>
              </label>
            </>
          ) : tab === 3 ? (
            <>
              <p>
                Connector GitHub chưa được bật. Bạn có thể tải ZIP và đưa mã vào
                repo của mình.
              </p>
              <a
                className="btn"
                href="https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI"
                target="_blank"
                rel="noreferrer"
              >
                Kho tài nguyên
              </a>
            </>
          ) : (
            <>
              <p>
                Dự án lưu trong trình duyệt, không đồng bộ giữa các máy. Nếu
                chọn tạo với AI, prompt, mã trước đó và nguồn bạn chọn được
                chuyển đến nhà cung cấp. Bài đăng công khai được lưu trên máy
                chủ.
              </p>
              <p>
                {me?.admin
                  ? "Tài khoản quản trị không có hạn mức ngày."
                  : me
                    ? `Đã dùng ${me.used}/${me.limit} lượt AI hôm nay (UTC).`
                    : "Đăng nhập để xem hạn mức AI."}
              </p>
              <div className="settings-actions">
                <button className="btn" onClick={exportData}>
                  <ArrowDownToLine size={16} /> Xuất dữ liệu trên thiết bị
                </button>
                <button
                  className="btn danger"
                  onClick={() => {
                    if (
                      confirm(
                        "Xóa dự án, hồ sơ và tài nguyên lưu trên thiết bị này?",
                      )
                    ) {
                      clearLocal();
                      try {
                        localStorage.removeItem("ff3-saved-posts");
                      } catch {}
                      notify("Đã xóa dữ liệu trên thiết bị.");
                    }
                  }}
                >
                  Xóa dữ liệu trên thiết bị
                </button>
              </div>
              <p>Thao tác này không xóa tài khoản hoặc bài đã đăng.</p>
            </>
          )}
        </section>
      </div>
    </div>
  );
}

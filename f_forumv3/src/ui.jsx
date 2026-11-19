import React, { useEffect, useRef, useState } from "react";
import {
  ArrowUp,
  ArrowUpRight,
  Box,
  Braces,
  Code2,
  Command,
  Layers3,
  LayoutTemplate,
  PanelsTopLeft,
  Play,
  Plus,
  Sparkles,
} from "lucide-react";
import "./pinui/prompt-composer.css";
export function Mark({ busy = false, size = 35 }) {
  return (
    <svg
      className={busy ? "kinetic" : ""}
      viewBox="0 0 40 40"
      width={size}
      height={size}
      aria-hidden="true"
    >
      <rect width="40" height="40" rx="11" fill="var(--brand-solid,#6748e8)" />
      <g fill="white">
        <path d="M10 10h8v8h-8zm0 12h8v8h-8z" />
        <path d="M22 10a8 8 0 0 1 8 8h-8zm0 12h8a8 8 0 0 1-8 8z" />
      </g>
    </svg>
  );
}
export function Composer({
  value,
  onChange,
  onSubmit,
  placeholder = "Mô tả website bạn muốn tạo…",
  busy = false,
  foot,
  home = false,
}) {
  const ref = useRef(null);
  return (
    <form
      className={`pcmp studio-composer ${home ? "home-composer" : ""}`}
      onSubmit={(e) => {
        e.preventDefault();
        if (value.trim() && !busy) onSubmit();
      }}
    >
      <label className="sr-only" htmlFor={home ? "home-prompt" : "work-prompt"}>
        Mô tả yêu cầu
      </label>
      <textarea
        ref={ref}
        id={home ? "home-prompt" : "work-prompt"}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
            e.preventDefault();
            if (value.trim() && !busy) onSubmit();
          }
        }}
        placeholder={placeholder}
        maxLength={6500}
        rows={2}
      />
      <div className="composer-tools">
        <span className="composer-label">
          {foot || (
            <>
              <Sparkles size={13} /> Prompt Blueprint
            </>
          )}
        </span>
        <button
          className="send-btn"
          type="submit"
          disabled={busy || !value.trim()}
          aria-label={home ? "Mở Work space" : "Gửi yêu cầu"}
          title={home ? "Mở Work space" : "Gửi yêu cầu"}
        >
          <ArrowUp size={19} />
        </button>
      </div>
    </form>
  );
}
export function Reveal({ children, className = "" }) {
  const el = useRef(null);
  useEffect(() => {
    const node = el.current;
    if (
      !node ||
      !("IntersectionObserver" in window) ||
      matchMedia("(prefers-reduced-motion: reduce)").matches
    )
      return;
    const ob = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          node.dataset.entered = "true";
          ob.disconnect();
        }
      },
      { threshold: 0.12 },
    );
    ob.observe(node);
    return () => ob.disconnect();
  }, []);
  return (
    <div className={"reveal " + className} ref={el}>
      {children}
    </div>
  );
}
export function Empty({ icon: Icon = Box, title, children }) {
  return (
    <div className="empty">
      <span>
        <Icon size={22} />
      </span>
      <strong>{title}</strong>
      {children && <p>{children}</p>}
    </div>
  );
}
export function PageTitle({ n, label, title, children }) {
  return (
    <div className="page-title">
      <div className="eyebrow">
        <span className="route-led" />
        {n} / {label}
      </div>
      <h1>{title}</h1>
      {children && <p>{children}</p>}
    </div>
  );
}
export function Art() {
  return (
    <div className="hero-art" aria-hidden="true">
      <div className="art-grid" />
      <div className="art-orbit a" />
      <div className="art-orbit b" />
      <span className="art-coordinate top-left">
        FIG. 01 <i /> WEB CANVAS
      </span>
      <span className="art-coordinate bottom-right">01 / 04</span>
      <div className="art-window">
        <div className="art-titlebar">
          <span className="dots">
            <i />
            <i />
            <i />
          </span>
          <span>index.html</span>
          <Code2 size={13} />
        </div>
        <div className="art-editor">
          <div className="art-lines">
            01
            <br />
            02
            <br />
            03
            <br />
            04
            <br />
            05
          </div>
          <div>
            <b>&lt;main&gt;</b>
            <br />
            &nbsp;&nbsp;<em>&lt;h1&gt;</em>Ý tưởng<em>&lt;/h1&gt;</em>
            <br />
            &nbsp;&nbsp;<span>/* bắt đầu ở đây */</span>
            <br />
            &nbsp;&nbsp;<em>&lt;canvas /&gt;</em>
            <br />
            <b>&lt;/main&gt;</b>
          </div>
        </div>
        <div className="art-window-bottom">
          <span>
            <i /> Preview
          </span>
          <Play size={12} />
        </div>
      </div>
      <svg className="hero-iso" viewBox="0 0 315 250" fill="none">
        <defs>
          <linearGradient id="iso-top" x1="0" x2="1" y1="0" y2="1">
            <stop stopColor="#f3ebff" />
            <stop offset="1" stopColor="#c6a7ff" />
          </linearGradient>
          <linearGradient id="iso-left" x2="0" y2="1">
            <stop stopColor="#b497ff" />
            <stop offset="1" stopColor="#7046eb" />
          </linearGradient>
          <linearGradient id="iso-right" x2="0" y2="1">
            <stop stopColor="#8559f7" />
            <stop offset="1" stopColor="#48249e" />
          </linearGradient>
        </defs>
        <path
          d="M26 163 157 92 289 163 157 235z"
          fill="#724bdd"
          fillOpacity=".19"
        />
        <path
          d="M44 157l113-62 114 62-114 61z"
          fill="#ded1ff"
          stroke="#f7edff"
        />
        <path
          d="M44 157v13l113 63v-15zm113 61 114-61v13l-114 63z"
          fill="#ae95ed"
        />
        <path
          d="M74 129l83-45 84 45-84 46z"
          fill="url(#iso-top)"
          stroke="#f7edff"
        />
        <path d="M74 129v21l83 47v-22z" fill="url(#iso-left)" />
        <path d="M157 175l84-46v21l-84 47z" fill="url(#iso-right)" />
        <g className="iso-float">
          <path
            d="M105 79l52-28 53 28-53 29z"
            fill="url(#iso-top)"
            stroke="#fff4ff"
          />
          <path d="M105 79v49l52 30v-50z" fill="url(#iso-left)" />
          <path d="M157 108l53-29v49l-53 30z" fill="url(#iso-right)" />
          <path d="m140 81 17-10 19 10-19 10z" fill="#fff" fillOpacity=".88" />
          <path
            d="M118 107l15 8m-15 0 15 8m39 5 17-9m-17 17 17-9"
            stroke="#e6d6ff"
            strokeLinecap="round"
            strokeWidth="2"
          />
        </g>
        <path
          d="M238 109h14m-7-7v14M67 89h12m-6-6v12M219 57h10m-5-5v10"
          stroke="#8f69e9"
          strokeLinecap="round"
          strokeWidth="1.5"
        />
      </svg>
      <div className="art-tag">
        <Braces size={13} /> HTML / CSS
      </div>
    </div>
  );
}
export const navItems = [
  ["Home", "/home"],
  ["Explore", "/explore"],
  ["Work space", "/workspace"],
  ["Source of Knowledge", "/community"],
];
export const featureItems = [
  [
    "01",
    "Explore",
    "Tìm thành phần, mẫu giao diện và tài liệu trước khi bắt tay làm.",
    LayoutTemplate,
    "/explore",
  ],
  [
    "02",
    "Work space",
    "Xem thử trang, đối chiếu thay đổi và xuất mã nguồn.",
    PanelsTopLeft,
    "/workspace",
  ],
  [
    "03",
    "Source of Knowledge",
    "Hỏi khi mắc kẹt, chia sẻ dự án hoặc bàn giao cho nhóm.",
    Layers3,
    "/community",
  ],
];

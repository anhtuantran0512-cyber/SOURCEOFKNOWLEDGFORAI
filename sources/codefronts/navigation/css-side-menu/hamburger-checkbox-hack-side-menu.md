---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/hamburger-checkbox-hack-side-menu/"
title: "Hamburger Checkbox-Hack Side Menu"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A classic pure-CSS interaction using a hidden checkbox input and the :checked general sibling combinator to toggle menu visibility and animate the burger…"
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hamburger Checkbox-Hack Side Menu
Source: https://codefronts.com/navigation/css-side-menu/hamburger-checkbox-hack-side-menu/

A classic pure-CSS interaction using a hidden checkbox input and the :checked general sibling combinator to toggle menu visibility and animate the burger icon into an X.
## HTML
```html
<div class="sm-13">
  <input type="checkbox" id="sm-13-chk">
  <label class="sm-13__burger" for="sm-13-chk" aria-label="Toggle menu">
    <span></span><span></span><span></span>
  </label>
  <!-- Clicking overlay also closes the menu -->
  <label class="sm-13__overlay" for="sm-13-chk"></label>
  <nav class="sm-13__nav">
    <div class="sm-13__links">
      <a class="sm-13__link sm-13__link--active" href="#"><span class="sm-13__link-chip"></span> Dashboard</a>
      <a class="sm-13__link" href="#"><span class="sm-13__link-chip"></span> Analytics</a>
      <a class="sm-13__link" href="#"><span class="sm-13__link-chip"></span> Content</a>
      <a class="sm-13__link" href="#"><span class="sm-13__link-chip"></span> Audience</a>
      <div class="sm-13__divider"></div>
      <a class="sm-13__link" href="#"><span class="sm-13__link-chip"></span> Help</a>
      <a class="sm-13__link" href="#"><span class="sm-13__link-chip"></span> Settings</a>
    </div>
    <div class="sm-13__user">
      <div class="sm-13__avatar">CK</div>
      <div>
        <div class="sm-13__uname">C. Kim</div>
        <div class="sm-13__urole">Publisher</div>
      </div>
    </div>
  </nav>
  <div class="sm-13__content">
    <div class="sm-13__heading">Checkbox Hack Menu</div>
    <div class="sm-13__sub">Uses a hidden <code>&lt;input type="checkbox"&gt;</code> and the CSS sibling combinator. No JavaScript at all.</div>
    <div class="sm-13__code-card">
      <span class="sel">#chk:checked ~ .nav</span> {<br>
      &nbsp;&nbsp;<span class="kw">transform</span>: translateX(0);<br>
      }<br>
      <span class="sel">#chk:checked ~ .burger span:nth-child(1)</span> {<br>
      &nbsp;&nbsp;<span class="kw">transform</span>: translateY(8px) rotate(45deg);<br>
      }
    </div>
    <div class="sm-13__grid">
      <div class="sm-13__card"><div class="sm-13__card-val">0 JS</div><div class="sm-13__card-lbl">Lines of JS</div></div>
      <div class="sm-13__card"><div class="sm-13__card-val">100%</div><div class="sm-13__card-lbl">Pure CSS</div></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-13,
.sm-13 *,
.sm-13 *::before,
.sm-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-13 ::selection {
  background: #f97316;
  color: #fff;
}

.sm-13 {
  --bg: #111113;
  --surface: #1c1c1f;
  --nav-bg: #18181b;
  --accent: #f97316;
  --accent2: #fb923c;
  --text: #f4f4f5;
  --muted: #71717a;
  --border: rgba(249,115,22,0.15);
  --font: 'Rubik', system-ui, sans-serif;
  --w: 270px;
  --dur: 0.38s;
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
}
/* Hidden checkbox — the :checked hack engine */

#sm-13-chk {
  display: none;
}
/* ======== BURGER LABEL ======== */

.sm-13__burger {
  position: absolute;
  top: 18px;
  left: 18px;
  z-index: 100;
  width: 44px;
  height: 44px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
  border-radius: 10px;
  background: var(--surface);
  border: 1px solid var(--border);
  transition: background 0.2s;
}

.sm-13__burger:hover {
  background: rgba(249,115,22,0.15);
}
/* Three bars — animated via :checked ~ sibling combinator */

.sm-13__burger span {
  width: 20px;
  height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform var(--dur) cubic-bezier(0.4,0,0.2,1), opacity var(--dur), width var(--dur);
  transform-origin: center;
  display: block;
}
/* :checked ~ .burger targets the burger because both are children of .sm-13 */

#sm-13-chk:checked ~ .sm-13__burger span:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}

#sm-13-chk:checked ~ .sm-13__burger span:nth-child(2) {
  opacity: 0;
  width: 0;
}

#sm-13-chk:checked ~ .sm-13__burger span:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}
/* ======== OVERLAY (backdrop close area) ======== */

.sm-13__overlay {
  position: absolute;
  inset: 0;
  z-index: 40;
  pointer-events: none;
  transition: background var(--dur);
}

#sm-13-chk:checked ~ .sm-13__overlay {
  background: rgba(0,0,0,0.5);
  pointer-events: all;
}
/* ======== DRAWER ======== */

.sm-13__nav {
  position: absolute;
  top: 0;
  left: 0;
  width: var(--w);
  height: 100%;
  background: var(--nav-bg);
  border-right: 1px solid var(--border);
  z-index: 50;
  transform: translateX(calc(-1 * var(--w)));
  transition: transform var(--dur) cubic-bezier(0.4,0,0.2,1);
  display: flex;
  flex-direction: column;
  padding: 74px 0 20px;
}

#sm-13-chk:checked ~ .sm-13__nav {
  transform: translateX(0);
  box-shadow: 8px 0 32px rgba(0,0,0,0.5);
}
/* Orange top accent line */

.sm-13__nav::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--accent), var(--accent2), transparent);
}

.sm-13__links {
  flex: 1;
  padding: 0 10px;
}

.sm-13__link {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 12px 14px;
  border-radius: 9px;
  color: var(--muted);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.18s;
  margin-bottom: 4px;
}

.sm-13__link:hover {
  color: var(--text);
  background: rgba(249,115,22,0.1);
}

.sm-13__link--active {
  color: var(--accent2);
  background: rgba(249,115,22,0.12);
}

.sm-13__link-chip {
  width: 8px;
  height: 8px;
  background: var(--muted);
  border-radius: 2px;
  transition: background 0.18s;
  transform: rotate(45deg);
  flex-shrink: 0;
}

.sm-13__link:hover .sm-13__link-chip {
  background: var(--accent2);
}

.sm-13__link--active .sm-13__link-chip {
  background: var(--accent);
  box-shadow: 0 0 6px var(--accent);
}

.sm-13__divider {
  height: 1px;
  background: var(--border);
  margin: 8px 14px;
}

.sm-13__user {
  padding: 16px 18px 0;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}

.sm-13__avatar {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: linear-gradient(135deg, var(--accent), #ef4444);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
}

.sm-13__uname {
  font-size: 13px;
  font-weight: 700;
}

.sm-13__urole {
  font-size: 10px;
  color: var(--muted);
}
/* ======== MAIN CONTENT ======== */

.sm-13__content {
  padding: 80px 22px 22px;
}

.sm-13__heading {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 6px;
}

.sm-13__sub {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 22px;
}
/* Explain the checkbox hack technique */

.sm-13__code-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px 16px;
  font-size: 12px;
  font-family: monospace;
  color: #a1a1aa;
  line-height: 1.8;
  margin-bottom: 14px;
}

.sm-13__code-card .kw {
  color: var(--accent);
}

.sm-13__code-card .sel {
  color: #60a5fa;
}

.sm-13__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.sm-13__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 9px;
  padding: 13px;
}

.sm-13__card-val {
  font-size: 20px;
  font-weight: 700;
  color: var(--accent2);
}

.sm-13__card-lbl {
  font-size: 11px;
  color: var(--muted);
  margin-top: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-13__nav,
    .sm-13__overlay,
    .sm-13__burger span {
    transition: none;
  }
}
```

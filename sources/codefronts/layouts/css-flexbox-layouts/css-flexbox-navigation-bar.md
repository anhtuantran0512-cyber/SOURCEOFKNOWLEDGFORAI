---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-navigation-bar/"
title: "CSS Flexbox Navigation Bar"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "Three navigation bar variants — space-between spread, absolutely centered links with flex spacers, and a pill-style active-highlight nav — all built with…"
has_js: "false"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Navigation Bar
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-navigation-bar/

Three navigation bar variants — space-between spread, absolutely centered links with flex spacers, and a pill-style active-highlight nav — all built with flex alignment tricks.
## HTML
```html
<div class="fl-03">

  <!-- Variant 1: classic space-between -->
  <div class="fl-03__nav-row">
    <span class="fl-03__nav-tag">space-between</span>
    <nav class="fl-03__nav">
      <div class="fl-03__logo">Flex<em>Nav</em></div>
      <div class="fl-03__spacer"></div>
      <ul class="fl-03__links">
        <li class="fl-03__link is-active">Home</li>
        <li class="fl-03__link">Products <span class="fl-03__link-badge">3</span></li>
        <li class="fl-03__link">Blog</li>
        <li class="fl-03__link">Pricing</li>
      </ul>
      <div class="fl-03__spacer"></div>
      <div class="fl-03__actions">
        <div class="fl-03__icon-btn">🔔</div>
        <button class="fl-03__btn fl-03__btn--ghost">Log in</button>
        <button class="fl-03__btn fl-03__btn--primary">Sign up</button>
        <div class="fl-03__avatar">AK</div>
      </div>
    </nav>
  </div>

  <!-- Variant 2: centered links -->
  <div class="fl-03__nav-row">
    <span class="fl-03__nav-tag fl-03__nav-tag--pink">centered links</span>
    <nav class="fl-03__nav fl-03__nav--centered">
      <div class="fl-03__logo">A<em>.</em></div>
      <ul class="fl-03__links">
        <li class="fl-03__link is-active">Work</li>
        <li class="fl-03__link">About</li>
        <li class="fl-03__link">Journal</li>
        <li class="fl-03__link">Contact</li>
      </ul>
      <div class="fl-03__spacer"></div>
      <div class="fl-03__actions">
        <button class="fl-03__btn fl-03__btn--primary">Hire me</button>
      </div>
    </nav>
  </div>

  <!-- Variant 3: pill nav -->
  <div class="fl-03__nav-row">
    <span class="fl-03__nav-tag">pill nav</span>
    <div class="fl-03__nav--pill">
      <div class="fl-03__pill-wrap">
        <div class="fl-03__pill-logo">Pill<em>UI</em></div>
        <ul class="fl-03__pill-links">
          <li class="fl-03__pill-link is-active">Home</li>
          <li class="fl-03__pill-link">Features</li>
          <li class="fl-03__pill-link">Docs</li>
          <li class="fl-03__pill-link">Community</li>
        </ul>
        <div class="fl-03__spacer"></div>
        <div class="fl-03__pill-cta">Get started →</div>
      </div>
    </div>
  </div>

  <!-- Variant cards -->
  <div class="fl-03__variants">
    <div class="fl-03__variant-card">
      <div class="fl-03__variant-title">Logo Left · Links Center</div>
      <div class="fl-03__variant-code">justify-content: space-between<br>flex: 1 spacers push links</div>
      <div class="fl-03__variant-desc">Two invisible <code>flex: 1</code> spacers flank the link list, centering it between logo and actions.</div>
    </div>
    <div class="fl-03__variant-card">
      <div class="fl-03__variant-title">Absolute Center Trick</div>
      <div class="fl-03__variant-code">position: absolute<br>left: 50%; translateX(-50%)</div>
      <div class="fl-03__variant-desc">Links use absolute positioning on the nav container to achieve pixel-perfect centering independent of logo width.</div>
    </div>
    <div class="fl-03__variant-card">
      <div class="fl-03__variant-title">Pill Nav Pattern</div>
      <div class="fl-03__variant-code">border-radius: 40px<br>align-items: center</div>
      <div class="fl-03__variant-desc">Wrapping the entire flex row in a pill border-radius creates a floating nav aesthetic popular in SaaS landing pages.</div>
    </div>
  </div>

</div>
```
## CSS
```css
.fl-03,
.fl-03 *,
.fl-03 *::before,
.fl-03 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-03 ::selection {
  background: #00f5c4;
  color: #000;
}

.fl-03 {
  --bg: #0b0c10;
  --surface: #13151a;
  --border: rgba(255,255,255,0.08);
  --accent: #00f5c4;
  --accent2: #ff5c87;
  --muted: rgba(255,255,255,0.45);
  --text: #fff;
  font-family: 'Syne', sans-serif;
  background: var(--bg);
  padding: 12px 0 20px;
  min-height: 500px;
  border-radius: 16px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
/* Variant row — wraps the variant tag + the nav itself.
   Tag sits ABOVE the nav as a non-overlapping caption so it never
   conflicts with the actions group on narrow viewports. */

.fl-03__nav-row {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 12px 24px 0;
}

.fl-03__nav-tag {
  align-self: flex-start;
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  opacity: 0.75;
  padding: 2px 8px;
  background: rgba(0,245,196,0.08);
  border: 1px solid rgba(0,245,196,0.2);
  border-radius: 4px;
}

.fl-03__nav-tag--pink {
  color: var(--accent2);
  background: rgba(255,92,135,0.08);
  border-color: rgba(255,92,135,0.2);
}
/* ── Navbar 1: Space-between classic ── */

.fl-03__nav {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 0 16px;
  height: 56px;
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}
/* Logo */

.fl-03__logo {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -0.03em;
  flex-shrink: 0;
}

.fl-03__logo em {
  color: var(--accent);
  font-style: normal;
}
/* Nav links group (center or left) */

.fl-03__links {
  display: flex;
  align-items: center;
  gap: 2px;
  list-style: none;
}

.fl-03__link {
  padding: 7px 14px;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  position: relative;
  transition: color 0.2s, background 0.2s;
}

.fl-03__link:hover {
  color: var(--text);
  background: rgba(255,255,255,0.06);
}

.fl-03__link.is-active {
  color: var(--text);
}

.fl-03__link.is-active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 50%;
  transform: translateX(-50%);
  width: 20px;
  height: 2px;
  background: var(--accent);
  border-radius: 2px;
}

.fl-03__link-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--accent2);
  color: #fff;
  font-size: 0.6rem;
  font-weight: 800;
  margin-left: 4px;
}
/* Actions group */

.fl-03__actions {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.fl-03__btn {
  padding: 6px 16px;
  border-radius: 8px;
  font-size: 0.78rem;
  font-weight: 700;
  font-family: 'Syne', sans-serif;
  cursor: pointer;
  border: none;
  transition: opacity 0.2s, transform 0.15s;
}

.fl-03__btn:hover {
  opacity: 0.85;
  transform: translateY(-1px);
}

.fl-03__btn--ghost {
  background: transparent;
  color: var(--muted);
  border: 1px solid var(--border);
}

.fl-03__btn--ghost:hover {
  color: var(--text);
}

.fl-03__btn--primary {
  background: var(--accent);
  color: #000;
}

.fl-03__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ff5c87, #6c63ff);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 800;
  color: #fff;
  cursor: pointer;
  flex-shrink: 0;
}

.fl-03__icon-btn {
  width: 34px;
  height: 34px;
  border-radius: 8px;
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--muted);
  font-size: 0.9rem;
  transition: background 0.2s, color 0.2s;
}

.fl-03__icon-btn:hover {
  background: rgba(255,255,255,0.1);
  color: var(--text);
}
/* Spacer utility */

.fl-03__spacer {
  flex: 1;
}
/* ── Variant descriptor cards ── */

.fl-03__variants {
  display: flex;
  flex: 1;
  padding: 20px 24px;
  gap: 14px;
  flex-wrap: wrap;
  align-content: flex-start;
}

.fl-03__variant-card {
  flex: 1 1 200px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.fl-03__variant-title {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.05em;
}

.fl-03__variant-code {
  font-family: 'Courier New', monospace;
  font-size: 0.72rem;
  color: rgba(255,255,255,0.5);
  background: rgba(255,255,255,0.04);
  padding: 6px 10px;
  border-radius: 6px;
  line-height: 1.7;
}

.fl-03__variant-desc {
  font-size: 0.75rem;
  color: var(--muted);
  line-height: 1.6;
}
/* Nav variant 2: centered links */

.fl-03__nav--centered .fl-03__links {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
/* Nav variant 3: pill style */

.fl-03__nav--pill {
  background: transparent;
  height: auto;
}

.fl-03__pill-wrap {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 40px;
  padding: 6px 8px 6px 16px;
  display: flex;
  align-items: center;
  gap: 8px;
  width: 100%;
  min-width: 0;
}

.fl-03__pill-logo {
  font-size: 0.9rem;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -0.03em;
  margin-right: 8px;
}

.fl-03__pill-logo em {
  color: var(--accent2);
  font-style: normal;
}

.fl-03__pill-links {
  display: flex;
  align-items: center;
  gap: 2px;
  list-style: none;
  flex: 1;
}

.fl-03__pill-link {
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 0.76rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  transition: all 0.2s;
}

.fl-03__pill-link:hover {
  color: var(--text);
  background: rgba(255,255,255,0.06);
}

.fl-03__pill-link.is-active {
  background: var(--accent2);
  color: #fff;
}

.fl-03__pill-cta {
  padding: 7px 16px;
  border-radius: 20px;
  background: var(--accent);
  color: #000;
  font-size: 0.76rem;
  font-weight: 800;
  cursor: pointer;
  flex-shrink: 0;
  transition: opacity 0.2s;
}

.fl-03__pill-cta:hover {
  opacity: 0.85;
}
/* Responsive defenses: hide low-priority items so the actions group
   fits and nothing overflows. The "centered links" trick relies on the
   absolutely-positioned link group — on narrow viewports it would
   collide with the logo, so re-anchor it inline. */

@media (max-width: 640px) {
  .fl-03__nav-row {
    padding: 10px 12px 0;
  }

  .fl-03__nav {
    padding: 0 10px;
  }

  .fl-03__icon-btn,
    .fl-03__avatar {
    display: none;
  }

  .fl-03__link[data-priority="low"] {
    display: none;
  }

  .fl-03__nav--centered .fl-03__links {
    position: static;
    transform: none;
  }

  .fl-03__pill-logo {
    font-size: 0.8rem;
  }

  .fl-03__pill-link {
    padding: 5px 8px;
    font-size: 0.7rem;
  }
}

@media (max-width: 480px) {
  .fl-03__btn--ghost {
    display: none;
  }

  .fl-03__links .fl-03__link:nth-child(n+3) {
    display: none;
  }

  .fl-03__pill-links .fl-03__pill-link:nth-child(n+3) {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fl-03__btn,
    .fl-03__icon-btn {
    transition: none;
  }
}
```

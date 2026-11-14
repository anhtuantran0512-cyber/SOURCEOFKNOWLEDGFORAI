---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-landing-page-hero-title/"
title: "CSS Text Gradient Landing Page Hero Title"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A sophisticated dark-mode hero section demonstrating the core background-clip text gradient technique for high-impact H1 headlines."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Gradient Landing Page Hero Title
Source: https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-landing-page-hero-title/

A sophisticated dark-mode hero section demonstrating the core background-clip text gradient technique for high-impact H1 headlines.
## HTML
```html
<div class="tg-01">
  <div class="tg-01__hero">
    <div class="tg-01__badge">NOW AVAILABLE</div>
    <h1 class="tg-01__title">Build Products<br><span class="tg-01__grad">Users Love</span></h1>
    <p class="tg-01__sub">Design systems, prototypes, and production-grade components—all in one collaborative workspace.</p>
    <div class="tg-01__cta-row">
      <button class="tg-01__btn tg-01__btn--primary">Start for free</button>
      <button class="tg-01__btn tg-01__btn--ghost">View demo →</button>
    </div>
    <div class="tg-01__stats">
      <div class="tg-01__stat"><strong>50K+</strong><span>Developers</span></div>
      <div class="tg-01__stat"><strong>4.9★</strong><span>Rating</span></div>
      <div class="tg-01__stat"><strong>99.9%</strong><span>Uptime</span></div>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-01,
.tg-01 *,
.tg-01 *::before,
.tg-01 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-01 ::selection {
  background: #6c3fe4;
  color: #fff;
}

.tg-01 {
  --g-from: #a855f7;
  --g-via: #6366f1;
  --g-to: #06b6d4;
  --bg: #080b14;
  --text: #e2e8f0;
  --muted: #94a3b8;
  --border: rgba(255,255,255,.08);
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tg-01__hero {
  max-width: 680px;
  text-align: center;
}

.tg-01__badge {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  color: var(--g-from);
  border: 1px solid rgba(168,85,247,.35);
  background: rgba(168,85,247,.08);
  border-radius: 99px;
  padding: 4px 14px;
  margin-bottom: 24px;
}

.tg-01__title {
  font-size: clamp(2.4rem, 6vw, 4rem);
  font-weight: 800;
  line-height: 1.1;
  color: var(--text);
  margin-bottom: 20px;
  letter-spacing: -.03em;
}
/* The gradient text technique: background-clip + transparent text */

.tg-01__grad {
  background: linear-gradient(135deg, var(--g-from) 0%, var(--g-via) 50%, var(--g-to) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-01__sub {
  font-size: 1.0625rem;
  color: var(--muted);
  line-height: 1.7;
  max-width: 520px;
  margin: 0 auto 32px;
}

.tg-01__cta-row {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 40px;
}

.tg-01__btn {
  cursor: pointer;
  font-size: .9375rem;
  font-weight: 600;
  border-radius: 8px;
  padding: 12px 28px;
  border: none;
  transition: opacity .2s, transform .15s;
}

.tg-01__btn:hover {
  opacity: .85;
  transform: translateY(-1px);
}

.tg-01__btn--primary {
  background: linear-gradient(135deg, var(--g-from), var(--g-via));
  color: #fff;
}

.tg-01__btn--ghost {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text);
}

.tg-01__stats {
  display: flex;
  gap: 40px;
  justify-content: center;
  border-top: 1px solid var(--border);
  padding-top: 28px;
}

.tg-01__stat {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.tg-01__stat strong {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--text);
}

.tg-01__stat span {
  font-size: .8125rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .tg-01__btn {
    transition: none;
  }
}
```

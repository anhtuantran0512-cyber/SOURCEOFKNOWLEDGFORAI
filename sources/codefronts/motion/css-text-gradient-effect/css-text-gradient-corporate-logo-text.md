---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-corporate-logo-text/"
title: "CSS Text Gradient Corporate Logo Text"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "An image-free corporate navbar logo using gradient text that scales infinitely at any DPI with zero HTTP requests."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Gradient Corporate Logo Text
Source: https://codefronts.com/motion/css-text-gradient-effect/css-text-gradient-corporate-logo-text/

An image-free corporate navbar logo using gradient text that scales infinitely at any DPI with zero HTTP requests.
## HTML
```html
<div class="tg-03">
  <div class="tg-03__wrapper">
    <nav class="tg-03__nav">
      <div class="tg-03__logo">
        <span class="tg-03__logo-icon">◈</span>
        <span class="tg-03__logo-text">Spectr<span class="tg-03__grad">um</span></span>
      </div>
      <div class="tg-03__nav-links">
        <a href="#" class="tg-03__link">Product</a>
        <a href="#" class="tg-03__link">Pricing</a>
        <a href="#" class="tg-03__link">About</a>
      </div>
      <button class="tg-03__cta">Get started</button>
    </nav>
    <div class="tg-03__showcase">
      <p class="tg-03__label">LOGO SIZES</p>
      <div class="tg-03__size-row">
        <span class="tg-03__logo-display tg-03__logo-display--sm">Spectr<span class="tg-03__grad">um</span></span>
        <span class="tg-03__logo-display tg-03__logo-display--md">Spectr<span class="tg-03__grad">um</span></span>
        <span class="tg-03__logo-display tg-03__logo-display--lg">Spectr<span class="tg-03__grad">um</span></span>
      </div>
      <p class="tg-03__note">Gradient text is image-free — scales infinitely, renders crisply on all DPI screens, and requires zero HTTP requests.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-03,
.tg-03 *,
.tg-03 *::before,
.tg-03 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-03 ::selection {
  background: #6366f1;
  color: #fff;
}

.tg-03 {
  --g-a: #6366f1;
  --g-b: #a855f7;
  --bg: #f8fafc;
  --surface: #ffffff;
  --text: #0f172a;
  --muted: #64748b;
  --border: #e2e8f0;
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 0;
}
/* Gradient reusable */

.tg-03__grad {
  background: linear-gradient(120deg, var(--g-a) 0%, var(--g-b) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.tg-03__nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 32px;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  gap: 24px;
}

.tg-03__logo {
  display: flex;
  align-items: center;
  gap: 8px;
}

.tg-03__logo-icon {
  background: linear-gradient(120deg, var(--g-a), var(--g-b));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 1.4rem;
}

.tg-03__logo-text {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -.03em;
}

.tg-03__nav-links {
  display: flex;
  gap: 24px;
}

.tg-03__link {
  text-decoration: none;
  font-size: .9rem;
  font-weight: 500;
  color: var(--muted);
  transition: color .2s;
}

.tg-03__link:hover {
  color: var(--text);
}

.tg-03__cta {
  font-size: .875rem;
  font-weight: 600;
  padding: 8px 20px;
  border-radius: 7px;
  border: none;
  background: linear-gradient(120deg, var(--g-a), var(--g-b));
  color: #fff;
  cursor: pointer;
}

.tg-03__showcase {
  padding: 40px 32px;
  max-width: 700px;
  margin: 0 auto;
}

.tg-03__label {
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .1em;
  color: var(--muted);
  margin-bottom: 24px;
}

.tg-03__size-row {
  display: flex;
  align-items: center;
  gap: 32px;
  flex-wrap: wrap;
  margin-bottom: 32px;
}

.tg-03__logo-display {
  font-weight: 800;
  letter-spacing: -.03em;
  color: var(--text);
}

.tg-03__logo-display--sm {
  font-size: 1.25rem;
}

.tg-03__logo-display--md {
  font-size: 2rem;
}

.tg-03__logo-display--lg {
  font-size: 3.25rem;
}

.tg-03__note {
  font-size: .9rem;
  color: var(--muted);
  line-height: 1.65;
  max-width: 560px;
  border-left: 3px solid;
  border-image: linear-gradient(to bottom, var(--g-a), var(--g-b)) 1;
  padding-left: 16px;
}

@media (prefers-reduced-motion: reduce) {
  .tg-03__cta,
    .tg-03__link {
    transition: none;
  }
}
```

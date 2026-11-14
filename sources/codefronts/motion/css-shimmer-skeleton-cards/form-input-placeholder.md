---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/form-input-placeholder/"
title: "Form Input Placeholder"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A form skeleton for auth screens, checkout flows and settings pages: label lines followed by 42px input bars whose left edge carries a focus-ring-tinted…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Form Input Placeholder
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/form-input-placeholder/

A form skeleton for auth screens, checkout flows and settings pages: label lines followed by 42px input bars whose left edge carries a focus-ring-tinted accent, a taller textarea block and a gradient submit pill. The 42px height matches standard input controls exactly, so when the real form hydrates — or autofill fires — nothing moves a pixel.
## HTML
```html
<section class="ssc-10" aria-label="Form input skeleton demo">
  <div class="ssc-10__form" role="status" aria-busy="true">
    <span class="ssc-sr">Loading form…</span>
    <div aria-hidden="true">
      <div class="ssc-10__field">
        <div class="ssc-sk ssc-10__label" style="width:28%"></div>
        <div class="ssc-sk ssc-10__input"></div>
      </div>
      <div class="ssc-10__field">
        <div class="ssc-sk ssc-10__label" style="width:34%"></div>
        <div class="ssc-sk ssc-10__input"></div>
      </div>
      <div class="ssc-10__field">
        <div class="ssc-sk ssc-10__label" style="width:24%"></div>
        <div class="ssc-sk ssc-10__textarea"></div>
      </div>
      <div class="ssc-sk ssc-10__submit"></div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-10,
.ssc-10 *,
.ssc-10 *::before,
.ssc-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-10 {
  --accent: oklch(0.65 0.15 165);
  --sk-bg: oklch(0.93 0.012 165);
  --sk-shine: rgba(255,255,255,.85);
  --field-h: 42px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(165deg,oklch(0.97 0.008 165),oklch(0.94 0.015 180));
}

.ssc-10 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 9px;
}

.ssc-10 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-10-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-10-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-10 .ssc-sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.ssc-10 .ssc-10__form {
  position: relative;
  width: min(380px,100%);
  background: #fff;
  border: 1px solid oklch(0.9 0.02 170);
  border-radius: 20px;
  padding: 26px;
  box-shadow: 0 20px 44px -30px oklch(0.45 0.1 170 / .5);
}

.ssc-10 .ssc-10__form>div[aria-hidden] {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ssc-10 .ssc-10__field {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ssc-10 .ssc-10__label {
  height: 9px;
  border-radius: 999px;
}

.ssc-10 .ssc-10__input {
  height: var(--field-h);
  width: 100%;
  background: linear-gradient(90deg,color-mix(in oklab,var(--accent) 45%,var(--sk-bg)) 0 3px,var(--sk-bg) 3px);
  box-shadow: inset 0 0 0 1px oklch(0.88 0.02 170);
}

.ssc-10 .ssc-10__textarea {
  height: 96px;
  width: 100%;
  box-shadow: inset 0 0 0 1px oklch(0.88 0.02 170);
}

.ssc-10 .ssc-10__submit {
  height: 44px;
  width: 140px;
  border-radius: 999px;
  margin-top: 2px;
  background: color-mix(in oklab,var(--accent) 30%,var(--sk-bg));
}

@media (prefers-reduced-motion: reduce) {
  .ssc-10 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — the 42px height contract keeps CLS at zero; a hard-stop gradient paints the focus-edge accent. */
```

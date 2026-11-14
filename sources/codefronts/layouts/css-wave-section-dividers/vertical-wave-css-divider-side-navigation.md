---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/vertical-wave-css-divider-side-navigation/"
title: "Vertical wave CSS divider side navigation"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "The wave rotated 90°: a curved vertical seam between a sidebar and the content column, for split-screen layouts and creative sidebars."
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical wave CSS divider side navigation
Source: https://codefronts.com/layouts/css-wave-section-dividers/vertical-wave-css-divider-side-navigation/

The wave rotated 90°: a curved vertical seam between a sidebar and the content column, for split-screen layouts and creative sidebars. Includes the container-query-driven collapse so the vertical wave becomes a horizontal one when the layout stacks on mobile.
## HTML
```html
<div class="wsd-14-group">
<section class="wsd-14a">
  <div class="wsd-14a__shell">
    <aside class="wsd-14a__side">
      <p class="wsd-14a__brand">codefronts</p>
      <nav class="wsd-14a__nav" aria-label="Section navigation">
        <ul>
          <li><a href="#0" aria-current="page">Overview</a></li>
          <li><a href="#0">Dividers</a></li>
          <li><a href="#0">Gradients</a></li>
          <li><a href="#0">Masks</a></li>
        </ul>
      </nav>
      <svg class="wsd-14a__wave" viewBox="0 0 120 800" preserveAspectRatio="none" aria-hidden="true" focusable="false">
        <path d="M64,0 C104,140 24,260 60,400 C96,540 20,660 56,800 L120,800 L120,0 Z"></path>
      </svg>
    </aside>
    <main class="wsd-14a__main">
      <h2 class="wsd-14a__title">Vertical seam, authored portrait</h2>
      <p class="wsd-14a__copy">The wave runs down the grid instead of across it — for split-screen and creative sidebar layouts.</p>
    </main>
  </div>
</section>
<section class="wsd-14b">
  <div class="wsd-14b__left">
    <h2 class="wsd-14b__title">Split screen</h2>
    <p class="wsd-14b__copy">Masked edge, no SVG node.</p>
  </div>
  <div class="wsd-14b__right">
    <p class="wsd-14b__copy">The right panel carries a vertical wave mask on its left edge, so the two halves interlock.</p>
  </div>
</section>
</div>
```
## CSS
```css
.wsd-14-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-14-group > section {
  width: 100%;
}

.wsd-14a,
.wsd-14a *,
.wsd-14a *::before,
.wsd-14a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-14a {
  --side: oklch(0.24 0.06 280);
  --main: oklch(0.96 0.01 280);
  --accent: oklch(0.8 0.15 100);
  font-family: 'Segoe UI',system-ui,sans-serif;
  container-type: inline-size;
}

.wsd-14a__shell {
  display: grid;
  grid-template-columns: minmax(190px,28%) 1fr;
  min-height: 320px;
  background: var(--main);
}

.wsd-14a__side {
  position: relative;
  background: var(--side);
  color: #fff;
  padding: 30px 22px 30px 26px;
}

.wsd-14a__brand {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -.01em;
  margin-bottom: 22px;
}

.wsd-14a__nav ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding-right: 34px;
}

.wsd-14a__nav a {
  display: block;
  font-size: 14.5px;
  color: rgba(255,255,255,.82);
  text-decoration: none;
  padding: 8px 10px;
  border-radius: 8px;
}

.wsd-14a__nav a:hover {
  background: rgba(255,255,255,.1);
  color: #fff;
}

.wsd-14a__nav a[aria-current="page"] {
  background: color-mix(in oklab,var(--accent) 22%,transparent);
  color: #fff;
  box-shadow: inset 2px 0 0 var(--accent);
}

.wsd-14a__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.wsd-14a__wave {
  position: absolute;
  top: 0;
  bottom: 0;
  right: -1px;
  display: block;
  width: clamp(26px,4vw,58px);
  height: 100%;
  color: var(--main);
  pointer-events: none;
}

.wsd-14a__wave path {
  fill: currentColor;
}

.wsd-14a__main {
  padding: 34px 30px 40px;
  color: oklch(0.28 0.04 280);
}

.wsd-14a__title {
  font-size: clamp(21px,3vw,30px);
  margin-bottom: 10px;
}

.wsd-14a__copy {
  font-size: 15px;
  opacity: .74;
  max-width: 48ch;
}

@container (max-width: 560px) {
  .wsd-14a__shell {
    grid-template-columns: 1fr;
  }

  .wsd-14a__wave {
    top: auto;
    bottom: -1px;
    right: 0;
    left: 0;
    width: 100%;
    height: 34px;
    transform: rotate(0);
  }

  .wsd-14a__side {
    padding-bottom: 54px;
  }

  .wsd-14a__nav ul {
    padding-right: 0;
  }
}

.wsd-14b,
.wsd-14b *,
.wsd-14b *::before,
.wsd-14b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-14b {
  --left: oklch(0.3 0.1 20);
  --right: oklch(0.95 0.03 60);
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 300px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--left);
}

.wsd-14b__left {
  color: oklch(0.96 0.03 60);
  padding: 38px 26px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 8px;
}

.wsd-14b__title {
  font-size: clamp(22px,3.2vw,32px);
}

.wsd-14b__copy {
  font-size: 15px;
  opacity: .8;
  max-width: 36ch;
}

.wsd-14b__right {
  background: var(--right);
  color: oklch(0.3 0.07 30);
  padding: 38px 26px 38px 90px;
  display: flex;
  align-items: center;
  margin-left: -30px;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 800' preserveAspectRatio='none'%3E%3Cpath d='M60,0 C110,160 20,300 66,440 C104,556 26,660 62,800 L200,800 L200,0 Z' fill='%23000'/%3E%3C/svg%3E") no-repeat center/100% 100%;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 800' preserveAspectRatio='none'%3E%3Cpath d='M60,0 C110,160 20,300 66,440 C104,556 26,660 62,800 L200,800 L200,0 Z' fill='%23000'/%3E%3C/svg%3E") no-repeat center/100% 100%;
}

.wsd-14b__right .wsd-14b__copy {
  opacity: .95;
}

@media (max-width: 620px) {
  .wsd-14b {
    grid-template-columns: 1fr;
  }

  .wsd-14b__right {
    margin-left: 0;
    -webkit-mask: none;
    mask: none;
    border-top: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — a portrait viewBox stretched down the seam; a container query collapses the layout and re-orients the wave on narrow cards. */

/* No JavaScript — a portrait data-URI mask on the right panel's left edge interlocks the two halves; the mask is dropped when the layout stacks. */
```

---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/glass-floating-sidebar/"
title: "Frosted Glass Floating Sidebar Layout with Backdrop Blur"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The showpiece: a floating frosted-glass sidebar over a slowly-drifting aurora, with heavy blur + saturation, a light-catching gradient hairline, glass nav…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Floating Sidebar Layout with Backdrop Blur
Source: https://codefronts.com/layouts/css-sidebar-layouts/glass-floating-sidebar/

The showpiece: a floating frosted-glass sidebar over a slowly-drifting aurora, with heavy blur + saturation, a light-catching gradient hairline, glass nav pills, and a glowing gradient CTA — the portfolio/creative-landing treatment pushed to full art direction while staying readable, keyboard-navigable and reduced-motion-safe.
## HTML
```html
<section class="sbl-30">
  <aside class="sbl-30__glass" aria-label="Portfolio">
    <div class="sbl-30__brand"><span aria-hidden="true"></span>Aurora Studio</div>
    <nav class="sbl-30__nav">
      <a href="#" aria-current="page">Work</a><a href="#">About</a><a href="#">Journal</a><a href="#">Contact</a>
    </nav>
    <a class="sbl-30__cta" href="#">Start a project<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></a>
  </aside>
  <main class="sbl-30__stage">
    <h1>Design that<br>holds light.</h1>
    <p>A brand &amp; digital studio. The sidebar is one pane of frosted glass over a living aurora — blur, saturation and a light-catching hairline.</p>
  </main>
</section>
```
## CSS
```css
.sbl-30,
.sbl-30 *,
.sbl-30 *::before,
.sbl-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-30 {
  --ink: oklch(0.97 0.005 300);
  --mut: oklch(0.85 0.02 300);
  position: relative;
  isolation: isolate;
  display: grid;
  grid-template-columns: auto 1fr;
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  font-family: system-ui,'Segoe UI',sans-serif;
  color: var(--ink);
  background: oklch(0.15 0.03 290);
}

.sbl-30::before {
  content: "";
  position: absolute;
  inset: -30%;
  z-index: -1;
  pointer-events: none;
  background: radial-gradient(38% 42% at 30% 30%,oklch(0.55 0.22 310 / .8),transparent 70%),radial-gradient(34% 38% at 72% 62%,oklch(0.6 0.18 230 / .7),transparent 70%),radial-gradient(30% 34% at 50% 85%,oklch(0.65 0.16 180 / .5),transparent 70%);
  animation: sbl30-drift 24s ease-in-out infinite alternate;
}

@keyframes sbl30-drift {
  from {
    transform: translate3d(-3%,-2%,0) rotate(0deg) scale(1);
  }

  to {
    transform: translate3d(3%,2%,0) rotate(4deg) scale(1.08);
  }
}

.sbl-30__glass {
  width: 256px;
  margin: 20px;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  border-radius: 22px;
  border: 1px solid transparent;
  background: linear-gradient(rgba(255,255,255,.1),rgba(255,255,255,.08)) padding-box,linear-gradient(155deg,rgba(255,255,255,.6),rgba(255,255,255,.15) 35%,rgba(255,255,255,.04)) border-box;
  -webkit-backdrop-filter: blur(22px) saturate(1.8);
  backdrop-filter: blur(22px) saturate(1.8);
  box-shadow: 0 12px 40px oklch(0 0 0 / .35),inset 0 1px 0 rgba(255,255,255,.2);
}

.sbl-30__brand {
  display: flex;
  align-items: center;
  gap: 11px;
  font: 700 16px/1 system-ui,sans-serif;
  padding: 2px 10px 24px;
  letter-spacing: .01em;
}

.sbl-30__brand span {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: conic-gradient(oklch(0.75 0.16 310),oklch(0.75 0.14 230),oklch(0.78 0.14 180),oklch(0.75 0.16 310));
  box-shadow: 0 0 16px oklch(0.7 0.18 290 / .6);
}

.sbl-30__nav {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.sbl-30__nav a {
  padding: 12px 14px;
  border-radius: 12px;
  font: 500 14.5px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .2s ease,color .2s ease;
}

.sbl-30__nav a:hover {
  color: var(--ink);
  background: rgba(255,255,255,.1);
}

.sbl-30__nav a[aria-current="page"] {
  color: var(--ink);
  background: rgba(255,255,255,.16);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.18);
}

.sbl-30__nav a:focus-visible,
.sbl-30__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.sbl-30__cta {
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  padding: 14px;
  border-radius: 14px;
  font: 650 14px/1 system-ui,sans-serif;
  color: oklch(0.2 0.04 300);
  text-decoration: none;
  background: linear-gradient(120deg,oklch(0.85 0.1 310),oklch(0.87 0.09 220));
  box-shadow: 0 6px 24px oklch(0.7 0.18 290 / .45);
  transition: transform .2s ease,box-shadow .2s ease;
}

.sbl-30__cta svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: translate .2s ease;
}

.sbl-30__cta:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 32px oklch(0.7 0.18 290 / .6);
}

.sbl-30__cta:hover svg {
  translate: 3px 0;
}

.sbl-30__stage {
  display: grid;
  align-content: center;
  gap: 18px;
  padding: 48px 56px;
}

.sbl-30__stage h1 {
  font: 750 clamp(34px,5vw,54px)/1.08 system-ui,sans-serif;
  letter-spacing: -.02em;
  text-shadow: 0 2px 24px oklch(0 0 0 / .3);
}

.sbl-30__stage p {
  font: 400 15px/1.7 system-ui,sans-serif;
  color: var(--mut);
  max-width: 46ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-30::before {
    animation: none;
  }

  .sbl-30__cta {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — blur(22px) saturate(1.8) frost over a transform-only drifting aurora; gradient hairline + inner sheen make the glass read as lit. */
```

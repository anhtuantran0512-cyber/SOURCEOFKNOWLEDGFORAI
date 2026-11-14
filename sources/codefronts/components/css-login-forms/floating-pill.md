---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/floating-pill/"
title: "Floating Pill"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "An ultra-compact login widget that floats above app content like a modular control card — fully pill-shaped, docked to the bottom-centre of the viewport,…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Pill
Source: https://codefronts.com/components/css-login-forms/floating-pill/

An ultra-compact login widget that floats above app content like a modular control card — fully pill-shaped, docked to the bottom-centre of the viewport, ideal for mobile web overlays.
## HTML
```html
<section class="lf-13">
  <div class="lf-13__app" aria-hidden="true"><span>your app content</span></div>
  <form class="lf-13__pill" novalidate>
    <span class="lf-13__badge" aria-hidden="true">◐</span>
    <label class="lf-13__field"><span class="lf-13__vh">Email</span>
      <input type="email" autocomplete="email" placeholder="Email" required></label>
    <label class="lf-13__field"><span class="lf-13__vh">Password</span>
      <input type="password" autocomplete="current-password" placeholder="Password" required></label>
    <button class="lf-13__go" type="submit" aria-label="Sign in">→</button>
  </form>
</section>
```
## CSS
```css
.lf-13,
.lf-13 *,
.lf-13 *::before,
.lf-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-13 {
  --accent: oklch(0.6 0.18 285);
  position: relative;
  overflow: hidden;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #eceaf5;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-13__app {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  color: #c3bfd6;
  font-size: 38px;
  font-weight: 800;
  letter-spacing: .05em;
  background: repeating-linear-gradient(45deg,#e6e3f2 0 24px,#ecebf6 24px 48px);
}

.lf-13__pill {
  position: absolute;
  left: 50%;
  bottom: calc(2rem + env(safe-area-inset-bottom,0px));
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 8px;
  width: min(460px,calc(100% - 32px));
  padding: 8px 8px 8px 16px;
  background: rgba(255,255,255,.82);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,.7);
  border-radius: 9999px;
  box-shadow: 0 20px 50px -18px rgba(40,20,80,.45);
}

.lf-13__badge {
  flex: none;
  font-size: 20px;
  color: var(--accent);
}

.lf-13__field {
  flex: 1;
  min-width: 0;
}

.lf-13__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.lf-13__field input {
  width: 100%;
  height: 44px;
  border: 0;
  background: transparent;
  font-size: 14.5px;
  color: #241b3a;
  padding: 0 6px;
  border-radius: 9999px;
  transition: box-shadow .16s;
}

.lf-13__field input::placeholder {
  color: #9a92b4;
}

.lf-13__field input:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px oklch(0.6 0.18 285/.28);
}

.lf-13__field:first-of-type {
  border-right: 1px solid #ddd7ec;
  padding-right: 6px;
}

.lf-13__go {
  flex: none;
  width: 44px;
  height: 44px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 19px;
  transition: filter .16s,transform .12s;
}

.lf-13__go:hover {
  filter: brightness(1.08);
}

.lf-13__go:active {
  transform: scale(.94);
}

.lf-13__go:focus-visible {
  outline: 3px solid oklch(0.6 0.18 285/.55);
  outline-offset: 2px;
}

@media (max-width: 520px) {
  .lf-13__pill {
    flex-wrap: wrap;
    border-radius: 26px;
    padding: 12px;
  }

  .lf-13__field {
    flex: 1 1 100%;
  }

  .lf-13__field:first-of-type {
    border-right: 0;
    border-bottom: 1px solid #ddd7ec;
    padding-bottom: 4px;
  }

  .lf-13__go {
    margin-left: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-13 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — a fixed-centre pill (translateX -50%) with a 9999px radius and blur backdrop. */
```

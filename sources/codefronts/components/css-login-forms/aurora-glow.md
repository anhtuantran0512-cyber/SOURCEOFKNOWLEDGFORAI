---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/aurora-glow/"
title: "Aurora Glow"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The indie-startup landing look: colourful, blurred atmospheric shapes drift behind a clean login card like a soft aurora."
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Glow
Source: https://codefronts.com/components/css-login-forms/aurora-glow/

The indie-startup landing look: colourful, blurred atmospheric shapes drift behind a clean login card like a soft aurora. High aesthetic impact, engineered to stay smooth on mobile.
## HTML
```html
<section class="lf-08">
  <div class="lf-08__bg" aria-hidden="true"></div>
  <form class="lf-08__card" novalidate>
    <h1 class="lf-08__h">Welcome back</h1>
    <p class="lf-08__sub">Sign in to keep building.</p>
    <label class="lf-08__field"><span class="lf-08__label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required></label>
    <label class="lf-08__field"><span class="lf-08__label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
    <button class="lf-08__submit" type="submit">Sign in</button>
    <p class="lf-08__foot"><a href="#">Forgot password?</a></p>
  </form>
</section>
```
## CSS
```css
.lf-08,
.lf-08 *,
.lf-08 *::before,
.lf-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-08 {
  --accent: oklch(0.65 0.2 300);
  --radius: 14px;
  --field-h: 48px;
  position: relative;
  overflow: hidden;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #0a0a14;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-08__bg {
  position: absolute;
  inset: -20%;
  z-index: 0;
}

.lf-08__bg::before,
.lf-08__bg::after {
  content: "";
  position: absolute;
  width: 60%;
  height: 60%;
  border-radius: 50%;
  filter: blur(90px);
  will-change: transform;
  opacity: .85;
}

.lf-08__bg::before {
  left: 2%;
  top: 5%;
  background: radial-gradient(circle,oklch(0.7 0.2 300),transparent 70%);
  animation: lf-08-a 16s ease-in-out infinite;
}

.lf-08__bg::after {
  right: 0%;
  bottom: 0%;
  background: radial-gradient(circle,oklch(0.72 0.19 210),transparent 70%);
  animation: lf-08-b 20s ease-in-out infinite;
}

.lf-08__card {
  position: relative;
  z-index: 1;
  width: min(360px,100%);
  background: rgba(18,18,30,.72);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(255,255,255,.09);
  border-radius: 20px;
  padding: 34px 30px;
  display: flex;
  flex-direction: column;
  gap: 15px;
  box-shadow: 0 30px 80px -40px #000;
  color: #eef0fa;
}

.lf-08__h {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.lf-08__sub {
  font-size: 14px;
  color: #a9adc4;
  margin-top: -6px;
  margin-bottom: 6px;
}

.lf-08__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-08__label {
  font-size: 13px;
  font-weight: 600;
  color: #c3c7dd;
}

.lf-08__field input {
  height: var(--field-h);
  border: 1.5px solid rgba(255,255,255,.14);
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 15px;
  color: #eef0fa;
  background: rgba(255,255,255,.04);
  transition: border-color .18s,box-shadow .18s;
}

.lf-08__field input::placeholder {
  color: #7f849e;
}

.lf-08__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.65 0.2 300/.28);
}

.lf-08__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: linear-gradient(90deg,oklch(0.65 0.2 300),oklch(0.66 0.19 250));
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  transition: filter .18s,transform .12s;
}

.lf-08__submit:hover {
  filter: brightness(1.08);
}

.lf-08__submit:active {
  transform: scale(.985);
}

.lf-08__submit:focus-visible {
  outline: 3px solid oklch(0.65 0.2 300/.6);
  outline-offset: 3px;
}

.lf-08__foot {
  text-align: center;
  font-size: 13px;
}

.lf-08__foot a {
  color: #c9bdf5;
  text-decoration: none;
}

.lf-08__foot a:hover {
  text-decoration: underline;
}

@keyframes lf-08-a {
  0%,
    100% {
    transform: translate(0,0) rotate(0);
  }

  50% {
    transform: translate(30%,20%) rotate(40deg);
  }
}

@keyframes lf-08-b {
  0%,
    100% {
    transform: translate(0,0) rotate(0);
  }

  50% {
    transform: translate(-25%,-15%) rotate(-30deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-08__bg::before,
    .lf-08__bg::after {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two blurred gradient blobs drift on the compositor via transform-only keyframes. */
```

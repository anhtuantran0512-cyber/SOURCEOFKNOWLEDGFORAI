---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-login-card/"
title: "Liquid Glass Login Card"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "An ultra-premium auth screen: a floating glass login card over a slowly drifting mesh-gradient background, so the refraction and blur visibly shift in real…"
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Login Card
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-login-card/

An ultra-premium auth screen: a floating glass login card over a slowly drifting mesh-gradient background, so the refraction and blur visibly shift in real time behind the card. High-converting, calm, and pure CSS — the animated backdrop is what shows off the glass.
## HTML
```html
<section class="lg-17" aria-label="Liquid glass login card">
  <div class="lg-17__mesh" aria-hidden="true"></div>
  <form class="lg-17__card" novalidate>
    <h3 class="lg-17__title">Welcome back</h3>
    <p class="lg-17__sub">Sign in to your Lumen workspace</p>
    <div class="lg-17__field"><label class="lg-17__label" for="lg-17-email">Email</label><input class="lg-17__input" id="lg-17-email" type="email" placeholder="[email protected]" autocomplete="email"></div>
    <div class="lg-17__field"><label class="lg-17__label" for="lg-17-pass">Password</label><input class="lg-17__input" id="lg-17-pass" type="password" placeholder="••••••••" autocomplete="current-password"></div>
    <div class="lg-17__row"><label class="lg-17__remember"><input type="checkbox"> Remember me</label><a class="lg-17__forgot" href="#lg-17">Forgot?</a></div>
    <button class="lg-17__submit" type="submit">Sign in</button>
    <p class="lg-17__alt">New here? <a href="#lg-17">Create an account</a></p>
  </form>
</section>
```
## CSS
```css
.lg-17,
.lg-17 *,
.lg-17 *::before,
.lg-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-17 {
  --accent: oklch(0.66 0.19 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 60px 20px;
  background: #0c0a18;
}

.lg-17__mesh {
  position: absolute;
  inset: -20%;
  background: radial-gradient(40% 40% at 20% 30%,oklch(0.6 0.22 300),transparent 70%),radial-gradient(40% 40% at 80% 20%,oklch(0.62 0.2 210),transparent 70%),radial-gradient(45% 45% at 70% 80%,oklch(0.64 0.2 340),transparent 70%),radial-gradient(40% 40% at 25% 85%,oklch(0.6 0.2 40),transparent 70%);
  filter: saturate(140%);
  animation: lg-17-drift 20s ease-in-out infinite alternate;
}

.lg-17__card {
  position: relative;
  z-index: 2;
  width: min(380px,92vw);
  padding: 34px;
  border-radius: 26px;
  color: #fff;
  background: color-mix(in oklab,white 12%,transparent);
  border: 1px solid rgba(255,255,255,.32);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 40px 80px -34px rgba(0,0,0,.7);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
}

.lg-17__title {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -.02em;
}

.lg-17__sub {
  font-size: 14px;
  color: rgba(255,255,255,.75);
  margin: 6px 0 24px;
}

.lg-17__field {
  margin-bottom: 16px;
}

.lg-17__label {
  display: block;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
  margin-bottom: 7px;
}

.lg-17__input {
  width: 100%;
  font-size: 15px;
  color: #fff;
  padding: 13px 15px;
  border-radius: 13px;
  border: 1px solid rgba(255,255,255,.25);
  background: color-mix(in oklab,white 8%,transparent);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.3);
  outline: none;
  transition: border-color .2s,box-shadow .2s,background .2s;
}

.lg-17__input::placeholder {
  color: rgba(255,255,255,.5);
}

.lg-17__field:focus-within .lg-17__input {
  border-color: color-mix(in oklab,var(--accent) 70%,white);
  background: color-mix(in oklab,white 14%,transparent);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 0 0 3px color-mix(in oklab,var(--accent) 40%,transparent);
}

.lg-17__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 13px;
  margin: 4px 0 20px;
}

.lg-17__remember {
  display: flex;
  align-items: center;
  gap: 7px;
  color: rgba(255,255,255,.8);
  cursor: pointer;
}

.lg-17__forgot,
.lg-17__alt a {
  color: oklch(0.82 0.12 285);
  text-decoration: none;
  font-weight: 600;
}

.lg-17__forgot:hover,
.lg-17__alt a:hover {
  text-decoration: underline;
}

.lg-17__submit {
  position: relative;
  overflow: hidden;
  width: 100%;
  font-size: 16px;
  font-weight: 700;
  color: #fff;
  padding: 14px;
  border-radius: 13px;
  cursor: pointer;
  border: 1px solid color-mix(in oklab,var(--accent) 40%,white);
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 85%,white),var(--accent));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 14px 30px -16px rgba(0,0,0,.6);
  transition: transform .15s;
}

.lg-17__submit::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 50%;
  height: 100%;
  background: linear-gradient(105deg,transparent,rgba(255,255,255,.5),transparent);
  transform: translateX(-200%) skewX(-14deg);
  transition: transform .7s;
}

.lg-17__submit:hover {
  transform: translateY(-2px);
}

.lg-17__submit:hover::after {
  transform: translateX(320%) skewX(-14deg);
}

.lg-17__submit:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-17__alt {
  text-align: center;
  font-size: 13px;
  color: rgba(255,255,255,.75);
  margin-top: 18px;
}

@keyframes lg-17-drift {
  from {
    transform: translate(-4%,-3%) scale(1.05);
  }

  to {
    transform: translate(4%,4%) scale(1.15);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-17__mesh {
    animation: none;
  }

  .lg-17__submit::after {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — an animated pure-CSS mesh-gradient backdrop drifts behind the card so the backdrop-filter glass visibly refracts shifting colour; inputs glow via :focus-within. */
```

---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/secure-glass-login-form-card/"
title: "Secure Glass Login Form Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A floating authentication card in Liquid Glass whose input fields have subtle inset glass borders that bloom with a soft accent glow the moment they receive…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Secure Glass Login Form Card
Source: https://codefronts.com/components/css-liquid-glass-cards/secure-glass-login-form-card/

A floating authentication card in Liquid Glass whose input fields have subtle inset glass borders that bloom with a soft accent glow the moment they receive focus — the 'secure and premium' entry point web-app teams want. Real form semantics, visible focus, no JS required.
## HTML
```html
<section class="lg-09" aria-label="Secure glass login form card demo">
  <form class="lg-09__card" aria-labelledby="lg-09-h">
    <h3 class="lg-09__h" id="lg-09-h">Welcome back</h3>
    <p class="lg-09__sub">Sign in to your CodeFronts account</p>
    <div class="lg-09__field"><input class="lg-09__in" id="lg-09-email" type="email" autocomplete="email" placeholder=" " required><label class="lg-09__lb" for="lg-09-email">Email</label></div>
    <div class="lg-09__field"><input class="lg-09__in" id="lg-09-pass" type="password" autocomplete="current-password" placeholder=" " required><label class="lg-09__lb" for="lg-09-pass">Password</label></div>
    <button class="lg-09__submit" type="submit">Sign in</button>
    <p class="lg-09__foot">No account? <a href="#lg-09">Create one</a></p>
  </form>
</section>
```
## CSS
```css
.lg-09,
.lg-09 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-09 {
  --accent: oklch(0.68 0.17 250);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 160deg at 30% 20%,#1e3a8a,#3730a3,#5b21b6,#1e3a8a);
  background-size: 200% 200%;
  animation: lg-09-bg 22s ease-in-out infinite;
}

@keyframes lg-09-bg {
  50% {
    background-position: 100% 100%;
  }
}

.lg-09__card {
  width: min(320px,100%);
  padding: 28px 26px;
  border-radius: 24px;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 11%,transparent);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 30px 64px -30px rgba(0,0,0,.75);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
}

.lg-09__h {
  font-size: 22px;
  font-weight: 800;
}

.lg-09__sub {
  font-size: 13px;
  color: rgba(255,255,255,.75);
  margin: 5px 0 22px;
}

.lg-09__field {
  position: relative;
  margin-bottom: 16px;
}

.lg-09__in {
  width: 100%;
  min-height: 50px;
  padding: 18px 14px 6px;
  border-radius: 13px;
  border: 1px solid rgba(255,255,255,.28);
  background: rgba(255,255,255,.08);
  color: #fff;
  font-size: 15px;
  box-shadow: inset 0 2px 6px rgba(0,0,0,.25);
  transition: box-shadow .3s,border-color .3s,background .3s;
}

.lg-09__in:focus {
  outline: none;
  border-color: color-mix(in oklab,var(--accent) 80%,white);
  background: rgba(255,255,255,.12);
  box-shadow: inset 0 2px 6px rgba(0,0,0,.2),0 0 0 3px color-mix(in oklab,var(--accent) 45%,transparent),0 0 22px -2px color-mix(in oklab,var(--accent) 70%,transparent);
}

.lg-09__lb {
  position: absolute;
  left: 14px;
  top: 15px;
  font-size: 15px;
  color: rgba(255,255,255,.7);
  pointer-events: none;
  transition: transform .2s,font-size .2s,color .2s;
  transform-origin: left;
}

.lg-09__in:focus+.lg-09__lb,
.lg-09__in:not(:placeholder-shown)+.lg-09__lb {
  transform: translateY(-9px);
  font-size: 11px;
  color: color-mix(in oklab,var(--accent) 60%,white);
}

.lg-09__submit {
  width: 100%;
  min-height: 48px;
  margin-top: 6px;
  border: 0;
  border-radius: 13px;
  cursor: pointer;
  font-weight: 700;
  font-size: 15px;
  color: #fff;
  background: rgba(255,255,255,.2);
  border: 1px solid rgba(255,255,255,.3);
  transition: background .3s,box-shadow .3s;
}

.lg-09__card:has(.lg-09__in:not(:placeholder-shown)) .lg-09__submit {
  background: var(--accent);
  border-color: transparent;
  box-shadow: 0 12px 28px -10px var(--accent);
}

.lg-09__submit:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-09__foot {
  text-align: center;
  font-size: 13px;
  color: rgba(255,255,255,.75);
  margin-top: 16px;
}

.lg-09__foot a {
  color: #fff;
  font-weight: 700;
}

@media (prefers-reduced-motion: reduce) {
  .lg-09 {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — fields bloom a glowing inset accent ring on :focus, floating labels ride :placeholder-shown, and :has() brightens the submit only once inputs are filled. */
```

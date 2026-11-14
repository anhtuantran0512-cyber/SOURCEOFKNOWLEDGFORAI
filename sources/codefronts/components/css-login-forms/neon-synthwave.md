---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/neon-synthwave/"
title: "Neon Synthwave"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A dark-mode-first, retro-gaming login glowing with disciplined neon: multi-layered text shadows and a tight box glow that says arcade without wrecking…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Synthwave
Source: https://codefronts.com/components/css-login-forms/neon-synthwave/

A dark-mode-first, retro-gaming login glowing with disciplined neon: multi-layered text shadows and a tight box glow that says arcade without wrecking contrast or legibility.
## HTML
```html
<section class="lf-09">
  <div class="lf-09__grid" aria-hidden="true"></div>
  <form class="lf-09__card" novalidate>
    <h1 class="lf-09__h">PLAYER LOGIN</h1>
    <label class="lf-09__field"><span class="lf-09__label">Username</span>
      <input type="text" autocomplete="username" placeholder="neo_runner" required></label>
    <label class="lf-09__field"><span class="lf-09__label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="••••••••" required></label>
    <button class="lf-09__submit" type="submit">ENTER</button>
    <p class="lf-09__foot"><a href="#">Insert coin — sign up</a></p>
  </form>
</section>
```
## CSS
```css
.lf-09,
.lf-09 *,
.lf-09 *::before,
.lf-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-09 {
  --neon: oklch(0.72 0.2 330);
  --neon2: oklch(0.78 0.16 200);
  --radius: 6px;
  --field-h: 48px;
  position: relative;
  overflow: hidden;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #0a0713;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-09__grid {
  position: absolute;
  left: -50%;
  right: -50%;
  bottom: -10%;
  height: 70%;
  background-image: linear-gradient(oklch(0.72 0.16 330/.35) 1px,transparent 1px),linear-gradient(90deg,oklch(0.72 0.16 330/.35) 1px,transparent 1px);
  background-size: 44px 44px;
  transform: perspective(300px) rotateX(62deg);
  mask-image: linear-gradient(#000,transparent);
}

.lf-09__card {
  position: relative;
  z-index: 1;
  width: min(360px,100%);
  background: #120b22;
  border: 1.5px solid var(--neon);
  border-radius: 16px;
  padding: 34px 30px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 0 18px oklch(0.72 0.2 330/.5),inset 0 0 22px oklch(0.72 0.2 330/.12);
  color: #eee;
}

.lf-09__h {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: .08em;
  text-align: center;
  color: #fff;
  text-shadow: 0 0 5px var(--neon),0 0 16px var(--neon);
}

.lf-09__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.lf-09__label {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--neon2);
  text-shadow: 0 0 8px oklch(0.78 0.16 200/.6);
}

.lf-09__field input {
  height: var(--field-h);
  border: 1.5px solid oklch(0.5 0.08 320);
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 15px;
  color: #fff;
  background: #0c0718;
  transition: border-color .18s,box-shadow .18s;
}

.lf-09__field input::placeholder {
  color: #6a5f85;
}

.lf-09__field input:focus-visible {
  outline: none;
  border-color: var(--neon);
  box-shadow: 0 0 0 3px oklch(0.72 0.2 330/.35),0 0 14px oklch(0.72 0.2 330/.5);
}

.lf-09__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 1.5px solid var(--neon);
  border-radius: var(--radius);
  cursor: pointer;
  background: transparent;
  color: #fff;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .1em;
  text-shadow: 0 0 8px var(--neon);
  box-shadow: 0 0 12px oklch(0.72 0.2 330/.4);
  transition: background .18s,box-shadow .18s,transform .12s;
}

.lf-09__submit:hover {
  background: oklch(0.72 0.2 330/.16);
  box-shadow: 0 0 22px oklch(0.72 0.2 330/.6);
}

.lf-09__submit:active {
  transform: scale(.985);
}

.lf-09__submit:focus-visible {
  outline: 3px solid oklch(0.72 0.2 330/.6);
  outline-offset: 3px;
}

.lf-09__foot {
  text-align: center;
  font-size: 12.5px;
}

.lf-09__foot a {
  color: var(--neon2);
  text-decoration: none;
  text-shadow: 0 0 8px oklch(0.78 0.16 200/.5);
}

.lf-09__foot a:hover {
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .lf-09 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — layered text/box shadows create the neon; glow lives on borders, not input text. */
```

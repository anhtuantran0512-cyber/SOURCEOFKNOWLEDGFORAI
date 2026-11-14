---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/glassmorphism-card-over-gradient/"
title: "Glassmorphism Card over Gradient"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A frosted-glass sign-in card and two glass stat chips floating over a living aurora — real backdrop-filter blur, a mask-composite glass edge, inner…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Card over Gradient
Source: https://codefronts.com/design-styles/css-gradient-ui/glassmorphism-card-over-gradient/

A frosted-glass sign-in card and two glass stat chips floating over a living aurora — real backdrop-filter blur, a mask-composite glass edge, inner highlight, and inputs that stay readable through the glass.
## HTML
```html
<div class="cgu-08-group">
<section class="cgu-08" aria-label="Glassmorphism card over gradient demo">
  <div class="cgu-08__sky" aria-hidden="true"></div>
  <div class="cgu-08__layout">
    <div class="cgu-08__intro">
      <p class="cgu-08__eyebrow">08 · Glassmorphism</p>
      <h2 class="cgu-08__title">Glass that earns its blur</h2>
      <p class="cgu-08__sub">Four layers make believable glass: backdrop blur + saturation, a white gradient film, an inset edge highlight, and a light-aware gradient border.</p>
      <div class="cgu-08__chips">
        <div class="cgu-08__chip"><strong>4,218</strong><span>teams signed in today</span></div>
        <div class="cgu-08__chip"><strong>99.98%</strong><span>uptime this quarter</span></div>
      </div>
    </div>
    <form class="cgu-08__card" aria-label="Sign in">
      <h3 class="cgu-08__cardtitle">Welcome back</h3>
      <p class="cgu-08__cardsub">Sign in to your workspace</p>
      <label class="cgu-08__label" for="cgu-08-email">Email</label>
      <input class="cgu-08__input" id="cgu-08-email" type="email" placeholder="[email protected]" autocomplete="email">
      <label class="cgu-08__label" for="cgu-08-pass">Password</label>
      <input class="cgu-08__input" id="cgu-08-pass" type="password" placeholder="••••••••••" autocomplete="current-password">
      <button class="cgu-08__submit" type="button">Sign in</button>
      <p class="cgu-08__alt">No account? <a class="cgu-08__link" href="#signup">Start free</a></p>
    </form>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-08-group {
  display: block;
  width: 100%;
}

.cgu-08,
.cgu-08 *,
.cgu-08 *::before,
.cgu-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-08 {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f4f3ff;
  background: #0a0714;
}

.cgu-08__sky {
  position: absolute;
  inset: -22%;
  z-index: -1;
  background: radial-gradient(36% 40% at 22% 28%,oklch(0.62 0.23 290 / .9),transparent 66%),radial-gradient(32% 36% at 76% 24%,oklch(0.7 0.18 210 / .85),transparent 64%),radial-gradient(38% 42% at 68% 76%,oklch(0.66 0.22 350 / .75),transparent 68%),#0a0714;
  filter: blur(38px) saturate(1.2);
  animation: cgu08-drift 50s ease-in-out infinite alternate;
}

.cgu-08__layout {
  width: min(980px,100%);
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 56px;
  align-items: center;
}

.cgu-08__intro {
  display: grid;
  gap: 18px;
}

.cgu-08__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: rgba(244,243,255,.7);
}

.cgu-08__title {
  font-size: clamp(32px,4.6vw,56px);
  font-weight: 850;
  letter-spacing: -.025em;
  line-height: 1.04;
  text-wrap: balance;
  text-shadow: 0 2px 30px rgba(0,0,0,.4);
}

.cgu-08__sub {
  max-width: 46ch;
  font-size: 15.5px;
  line-height: 1.65;
  color: rgba(244,243,255,.82);
  text-wrap: pretty;
}

.cgu-08__chips {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  margin-top: 8px;
}

.cgu-08__chip {
  display: grid;
  gap: 2px;
  padding: 14px 20px;
  border-radius: 16px;
  background: linear-gradient(150deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(18px) saturate(1.4);
  -webkit-backdrop-filter: blur(18px) saturate(1.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.25);
}

.cgu-08__chip strong {
  font-size: 20px;
  font-weight: 800;
}

.cgu-08__chip span {
  font-size: 12px;
  color: rgba(244,243,255,.7);
}

.cgu-08__card {
  position: relative;
  isolation: isolate;
  display: grid;
  gap: 10px;
  padding: 36px 34px;
  border-radius: 24px;
  background: linear-gradient(150deg,rgba(255,255,255,.14),rgba(255,255,255,.05));
  backdrop-filter: blur(22px) saturate(1.4);
  -webkit-backdrop-filter: blur(22px) saturate(1.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.28),0 24px 60px -30px rgba(0,0,0,.6);
}

.cgu-08__card::before {
  content: "";
  position: absolute;
  inset: 0;
  padding: 1px;
  border-radius: inherit;
  background: linear-gradient(160deg,rgba(255,255,255,.55),rgba(255,255,255,.06) 45%,rgba(255,255,255,.2));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.cgu-08__cardtitle {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cgu-08__cardsub {
  font-size: 13.5px;
  color: rgba(244,243,255,.72);
  margin-bottom: 10px;
}

.cgu-08__label {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(244,243,255,.75);
  margin-top: 6px;
}

.cgu-08__input {
  font: inherit;
  font-size: 15px;
  color: #fff;
  padding: 13px 16px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,.22);
  background: rgba(10,7,20,.35);
  outline: none;
  transition: border-color .25s,box-shadow .25s;
}

.cgu-08__input::placeholder {
  color: rgba(244,243,255,.5);
}

.cgu-08__input:focus-visible {
  border-color: rgba(255,255,255,.65);
  box-shadow: 0 0 0 4px rgba(255,255,255,.14);
}

.cgu-08__submit {
  margin-top: 14px;
  font: inherit;
  font-size: 15.5px;
  font-weight: 750;
  color: #170b2b;
  padding: 14px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: linear-gradient(120deg,#f4f0ff,#d9ccff);
  transition: transform .25s,box-shadow .25s;
  box-shadow: 0 14px 30px -14px rgba(217,204,255,.55);
}

.cgu-08__submit:hover,
.cgu-08__submit:focus-visible {
  transform: translateY(-2px);
  box-shadow: 0 20px 38px -14px rgba(217,204,255,.7);
}

.cgu-08__submit:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.cgu-08__alt {
  font-size: 13px;
  text-align: center;
  color: rgba(244,243,255,.7);
  margin-top: 4px;
}

.cgu-08__link {
  color: #fff;
  font-weight: 700;
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cgu-08__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
  border-radius: 4px;
}

@supports not (backdrop-filter: blur(1px)) {
  .cgu-08__card,
    .cgu-08__chip {
    background: rgba(16,10,32,.92);
  }
}

@keyframes cgu08-drift {
  0% {
    transform: translate(0,0) scale(1);
  }

  100% {
    transform: translate(-3%,2.5%) scale(1.07);
  }
}

@media (max-width: 760px) {
  .cgu-08__layout {
    grid-template-columns: 1fr;
    gap: 36px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-08__sky {
    animation: none;
  }

  .cgu-08__submit {
    transition: box-shadow .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — backdrop-filter blur + saturate, white gradient film, inset edge highlight, and a mask-composite gradient border make the glass. */
```

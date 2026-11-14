---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-shake-button-on-hover/"
title: "CSS Shake Button on Hover"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Hover-shake with two opposite intents: an eager gift-claim CTA that wiggles happily for as long as you hover (rotation, soft, inviting), and a destructive…"
has_js: "false"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shake Button on Hover
Source: https://codefronts.com/motion/css-shake-animation/css-shake-button-on-hover/

Hover-shake with two opposite intents: an eager gift-claim CTA that wiggles happily for as long as you hover (rotation, soft, inviting), and a destructive 'Delete forever' button that buzzes with a hard steps() vibration — the same trigger reading as 'yes please' in one and 'are you sure?' in the other.
## HTML
```html
<div class="shk-09-group">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400..800&display=swap" rel="stylesheet">
<section class="shk-09a" aria-label="Gift button that wiggles on hover">
  <div class="shk-09a__stage">
    <p class="shk-09a__eyebrow">Year-one anniversary</p>
    <h2 class="shk-09a__title">There's a gift<br>waiting for you</h2>
    <button class="shk-09a__btn" type="button"><span class="shk-09a__inner"><svg class="shk-09a__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="8" width="18" height="4"></rect><path d="M5 12v8a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-8"></path><path d="M12 8v13M12 8s-2.5-5-5-3.5S9 8 12 8zm0 0s2.5-5 5-3.5S15 8 12 8z"></path></svg>Claim your gift</span></button>
    <p class="shk-09a__hint" aria-hidden="true">hover — it can barely contain itself</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-09b" aria-label="Destructive button that buzzes on hover">
  <div class="shk-09b__modal" role="presentation">
    <h2 class="shk-09b__title">Delete project “aurora-v2”?</h2>
    <p class="shk-09b__sub">42 files, 9 collaborators, 14 months of history. This cannot be undone.</p>
    <div class="shk-09b__row">
      <button class="shk-09b__keep" type="button">Keep project</button>
      <button class="shk-09b__del" type="button"><span class="shk-09b__delin">Delete forever</span></button>
    </div>
    <p class="shk-09b__hint" aria-hidden="true">hover Delete — steps(2) turns a wiggle into a warning</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-09-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-09-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-09a,
.shk-09a *,
.shk-09a *::before,
.shk-09a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-09a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(170deg,#fdf3e7,#f9e2cf);
  font-family: 'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;
}

.shk-09a__stage {
  text-align: center;
}

.shk-09a__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.6 0.15 45);
}

.shk-09a__title {
  margin-top: 12px;
  font-size: clamp(32px,5vw,50px);
  line-height: 1.06;
  font-weight: 800;
  letter-spacing: -.025em;
  color: #2c1f14;
}

.shk-09a__btn {
  margin-top: 30px;
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
}

.shk-09a__inner {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 17px 32px;
  border-radius: 999px;
  font: inherit;
  font-size: 17px;
  font-weight: 700;
  color: #fff8f0;
  background: linear-gradient(180deg,oklch(0.68 0.19 40),oklch(0.58 0.19 35));
  box-shadow: 0 14px 30px -12px oklch(0.58 0.19 35 / .65),inset 0 1px 0 rgba(255,255,255,.25);
  transition: box-shadow .25s,filter .25s;
}

.shk-09a__ico {
  width: 20px;
  height: 20px;
}

.shk-09a__btn:hover .shk-09a__inner {
  animation: shk-09a-wiggle .45s ease-in-out .12s infinite;
  filter: brightness(1.05);
  box-shadow: 0 20px 40px -14px oklch(0.58 0.19 35 / .75),inset 0 1px 0 rgba(255,255,255,.25);
}

.shk-09a__btn:focus-visible {
  outline: none;
}

.shk-09a__btn:focus-visible .shk-09a__inner {
  outline: 3px solid #2c1f14;
  outline-offset: 3px;
  animation: shk-09a-wiggle .45s ease-in-out infinite;
}

.shk-09a__btn:active .shk-09a__inner {
  animation: none;
  scale: .96;
}

.shk-09a__hint {
  margin-top: 20px;
  font-size: 12px;
  color: rgba(44,31,20,.45);
}

@keyframes shk-09a-wiggle {
  0%,
    100% {
    rotate: 0deg;
  }

  25% {
    rotate: 3.5deg;
  }

  75% {
    rotate: -3.5deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-09a__btn:hover .shk-09a__inner,
    .shk-09a__btn:focus-visible .shk-09a__inner {
    animation: none;
  }
}

.shk-09b,
.shk-09b *,
.shk-09b *::before,
.shk-09b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-09b {
  --err: oklch(0.62 0.22 26);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101115;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-09b__modal {
  width: min(430px,100%);
  padding: 32px;
  border-radius: 18px;
  background: #181a20;
  border: 1px solid rgba(190,200,225,.13);
  box-shadow: 0 50px 100px -50px rgba(0,0,0,1);
}

.shk-09b__title {
  font-size: 19px;
  font-weight: 700;
  color: #edeff6;
  letter-spacing: -.01em;
}

.shk-09b__sub {
  margin-top: 9px;
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(225,230,245,.55);
}

.shk-09b__row {
  margin-top: 24px;
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

.shk-09b__keep {
  padding: 11px 18px;
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  color: #edeff6;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(190,200,225,.16);
  border-radius: 10px;
  cursor: pointer;
  transition: background .15s;
}

.shk-09b__keep:hover {
  background: rgba(255,255,255,.12);
}

.shk-09b__del {
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
}

.shk-09b__delin {
  display: inline-block;
  padding: 11px 18px;
  font: inherit;
  font-size: 14px;
  font-weight: 700;
  color: oklch(0.8 0.14 25);
  background: oklch(0.62 0.22 26 / .12);
  border: 1px solid oklch(0.62 0.22 26 / .4);
  border-radius: 10px;
  transition: background .15s,color .15s,border-color .15s;
}

.shk-09b__del:hover .shk-09b__delin {
  animation: shk-09b-buzz .12s steps(2,jump-none) infinite;
  background: oklch(0.62 0.22 26 / .2);
  border-color: var(--err);
  color: #ffd9d4;
}

.shk-09b__del:focus-visible {
  outline: none;
}

.shk-09b__del:focus-visible .shk-09b__delin {
  outline: 2px solid var(--err);
  outline-offset: 3px;
}

.shk-09b__del:active .shk-09b__delin {
  animation: none;
  scale: .96;
}

.shk-09b__hint {
  margin-top: 18px;
  font-size: 11.5px;
  color: rgba(225,230,245,.35);
  text-align: right;
}

@keyframes shk-09b-buzz {
  0% {
    translate: -1.5px 0;
  }

  100% {
    translate: 1.5px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-09b__del:hover .shk-09b__delin {
    animation: none;
    background: oklch(0.62 0.22 26 / .28);
  }
}
```

## JavaScript
```js
/* No JavaScript — an inner span carries the infinite ±3.5° wiggle (with a .12s delay so drive-by cursors don't flash it); the outer button keeps its own shadow/press transitions, so the two transforms never collide. */

/* No JavaScript — the exact same infinite-loop trigger as a friendly wiggle, but steps(2, jump-none) at 120ms with a 1.5px throw reads as an electric 'are you sure?'. Easing IS the emotion. */
```

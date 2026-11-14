---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/paywall-content-lock-blur/"
title: "Paywall / Content Lock Blur"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A subscribe wall that blurs the article behind a strong ::backdrop filter and fades the copy into a lock, prompting the reader to subscribe or log in — the…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Paywall / Content Lock Blur
Source: https://codefronts.com/components/css-modals/paywall-content-lock-blur/

A subscribe wall that blurs the article behind a strong ::backdrop filter and fades the copy into a lock, prompting the reader to subscribe or log in — the metered-content gate news and SaaS docs sites reach for.
## HTML
```html
<div class="cm-04">
  <article class="cm-04__article">
    <p class="cm-04__kicker">MEMBERS · MARKETS</p>
    <h1 class="cm-04__head">The quiet reshaping of global supply chains</h1>
    <p class="cm-04__by">By A. Okafor · 6 min read</p>
    <p class="cm-04__p">For three decades the logistics map optimised relentlessly for a single variable: cost. Factories clustered wherever labour was cheapest, and inventory was pared to the hour.</p>
    <p class="cm-04__p">Then the shocks arrived in sequence — a pandemic, a canal, a war — and the calculus inverted almost overnight. Resilience, not efficiency, became the word every operations chief…</p>
  </article>
  <div class="cm-04__lock">
    <button class="cm-04__open" type="button">Subscribe to keep reading</button>
  </div>

  <dialog class="cm-04__dlg" aria-labelledby="cm-04-title">
    <div class="cm-04__card">
      <button class="cm-04__x" type="button" aria-label="Close">&times;</button>
      <p class="cm-04__eyebrow">Unlimited access</p>
      <h2 id="cm-04-title" class="cm-04__title">Keep reading — join today</h2>
      <ul class="cm-04__list">
        <li>Every members-only report &amp; analysis</li>
        <li>Ad-free reading across all devices</li>
        <li>Cancel anytime, no questions asked</li>
      </ul>
      <div class="cm-04__price"><b>$8</b><span>/ month</span></div>
      <button type="button" class="cm-04__cta">Subscribe now</button>
      <p class="cm-04__login">Already a member? <a href="#login">Log in</a></p>
      <button type="button" class="cm-04__later">Maybe later</button>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-04,
.cm-04 *,
.cm-04 *::before,
.cm-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-04 {
  --accent: oklch(0.68 0.2 300);
  position: relative;
  font-family: Georgia,'Times New Roman',serif;
  min-height: 100dvh;
  padding: 44px 28px 0;
  background: #0c0d12;
  color: #e8e9f0;
}

.cm-04__article {
  max-width: 600px;
  margin: 0 auto;
  -webkit-mask-image: linear-gradient(#000 55%,transparent);
  mask-image: linear-gradient(#000 55%,transparent);
}

.cm-04__kicker {
  font-family: system-ui,sans-serif;
  font-size: 11px;
  letter-spacing: .22em;
  color: var(--accent);
  margin-bottom: 14px;
}

.cm-04__head {
  font-size: clamp(28px,5vw,40px);
  line-height: 1.15;
  font-weight: 700;
  color: #f3f4fa;
  margin-bottom: 14px;
}

.cm-04__by {
  font-family: system-ui,sans-serif;
  font-size: 13px;
  color: #8b8ea0;
  margin-bottom: 26px;
}

.cm-04__p {
  font-size: 18px;
  line-height: 1.75;
  color: #c3c6d4;
  margin-bottom: 18px;
}

.cm-04__lock {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 220px;
  display: grid;
  place-items: end center;
  padding-bottom: 40px;
  background: linear-gradient(transparent,#0c0d12 62%);
}

.cm-04__open {
  font-family: system-ui,sans-serif;
  cursor: pointer;
  padding: 15px 30px;
  border-radius: 12px;
  border: none;
  background: var(--accent);
  color: #120820;
  font: 700 15px system-ui;
  box-shadow: 0 14px 40px -12px var(--accent);
  transition: filter .2s,transform .1s;
}

.cm-04__open:hover {
  filter: brightness(1.08);
}

.cm-04__open:active {
  transform: translateY(1px);
}

.cm-04__open:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.cm-04__dlg {
  margin: auto;
  width: min(420px,94vw);
  padding: 0;
  border: none;
  border-radius: 20px;
  font-family: system-ui,sans-serif;
  color: #eceef6;
  background: linear-gradient(180deg,#181a26,#111219);
  box-shadow: 0 40px 90px -30px #000,0 0 0 1px #262a3a;
  opacity: 0;
  transform: translateY(14px) scale(.97);
  transition: opacity .3s,transform .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-04__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-04__dlg[open] {
    opacity: 0;
    transform: translateY(14px) scale(.97);
  }
}

.cm-04__dlg::backdrop {
  background: rgba(8,9,14,0);
  backdrop-filter: blur(0);
  transition: background .35s,backdrop-filter .35s,overlay .35s allow-discrete,display .35s allow-discrete;
}

.cm-04__dlg[open]::backdrop {
  background: rgba(8,9,14,.5);
  backdrop-filter: blur(9px);
}

@starting-style {
  .cm-04__dlg[open]::backdrop {
    background: rgba(8,9,14,0);
    backdrop-filter: blur(0);
  }
}

.cm-04__card {
  position: relative;
  padding: 34px 32px 26px;
}

.cm-04__x {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #8b8ea0;
  font-size: 22px;
  cursor: pointer;
}

.cm-04__x:hover {
  background: #212436;
  color: #fff;
}

.cm-04__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-04__eyebrow {
  font-size: 11px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 10px;
}

.cm-04__title {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: #f5f6fc;
  margin-bottom: 20px;
}

.cm-04__list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 22px;
}

.cm-04__list li {
  position: relative;
  padding-left: 28px;
  font-size: 14.5px;
  color: #c6c9d6;
}

.cm-04__list li::before {
  content: "✓";
  position: absolute;
  left: 0;
  top: 0;
  color: var(--accent);
  font-weight: 800;
}

.cm-04__price {
  display: flex;
  align-items: baseline;
  gap: 6px;
  margin-bottom: 18px;
}

.cm-04__price b {
  font-size: 34px;
  color: #fff;
}

.cm-04__price span {
  font-size: 14px;
  color: #9599aa;
}

.cm-04__cta {
  width: 100%;
  padding: 15px;
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #120820;
  font: 700 15px system-ui;
  cursor: pointer;
  transition: filter .2s,transform .1s;
}

.cm-04__cta:hover {
  filter: brightness(1.08);
}

.cm-04__cta:active {
  transform: translateY(1px);
}

.cm-04__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.cm-04__login {
  text-align: center;
  font-size: 13px;
  color: #9599aa;
  margin-top: 16px;
}

.cm-04__login a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
}

.cm-04__login a:hover {
  text-decoration: underline;
}

.cm-04__later {
  display: block;
  margin: 12px auto 0;
  background: none;
  border: none;
  color: #70748a;
  font: 13px system-ui;
  cursor: pointer;
  padding: 6px;
}

.cm-04__later:hover {
  color: #a0a3b6;
}

.cm-04__later:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .cm-04__dlg,
    .cm-04__dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-04');
  var dlg = root.querySelector('.cm-04__dlg');
  root.querySelector('.cm-04__open').addEventListener('click', function(){ dlg.showModal(); });
  root.querySelector('.cm-04__x').addEventListener('click', function(){ dlg.close(); });
  root.querySelector('.cm-04__later').addEventListener('click', function(){ dlg.close(); });
})();
```

---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/minimalist-floating-hamburger-button/"
title: "Minimalist Floating Hamburger Button CSS"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Navigation reduced to a single floating disc: a 56px FAB parked bottom-right over the page, opening a vertical speed-dial of three pill links that spring…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Floating Hamburger Button CSS
Source: https://codefronts.com/navigation/css-hamburger-menus/minimalist-floating-hamburger-button/

Navigation reduced to a single floating disc: a 56px FAB parked bottom-right over the page, opening a vertical speed-dial of three pill links that spring upward with staggered, slightly-overshooting motion. The restraint is the design — no bar, no chrome, just content and one affordance. The technique to study is the spring stagger: pure transition-delay choreography with an overshoot cubic-bezier, no keyframes, fully reversible mid-flight.
## HTML
```html
<section class="chm-14" aria-label="Floating hamburger button demo">
  <div class="chm-14__stage">
    <div class="chm-14__page" aria-hidden="true">
      <h2>Notes on less</h2>
      <p>A reading page with no header at all — navigation lives in one floating disc, bottom-right.</p>
      <div class="chm-14__ln" style="--w:100%"></div>
      <div class="chm-14__ln" style="--w:92%"></div>
      <div class="chm-14__ln" style="--w:97%"></div>
      <div class="chm-14__ln" style="--w:64%"></div>
      <div class="chm-14__ln" style="--w:88%"></div>
      <div class="chm-14__ln" style="--w:71%"></div>
    </div>
    <nav class="chm-14__dial" id="chm14-dial" aria-label="Site">
      <a href="#writing" class="chm-14__item" style="--i:2"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h11l3 3v13H5Z"/><path d="M15.5 4v3.5H19M8.5 12h7M8.5 16h5"/></svg>Writing</a>
      <a href="#about" class="chm-14__item" style="--i:1"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8.5" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/></svg>About</a>
      <a href="#contact" class="chm-14__item" style="--i:0"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5.5" width="17" height="13" rx="2.5"/><path d="m4.5 7 7.5 6L19.5 7"/></svg>Contact</a>
    </nav>
    <button class="chm-14__fab" type="button" aria-expanded="false" aria-controls="chm14-dial" aria-label="Open menu">
      <span aria-hidden="true"><i></i><i></i><i></i></span>
    </button>
  </div>
</section>
```
## CSS
```css
.chm-14,
.chm-14 *,
.chm-14 *::before,
.chm-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-14 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.985 0.002 90);
  --ink: oklch(0.22 0.008 90);
  --mut: oklch(0.55 0.008 90);
  --fab: oklch(0.22 0.008 90);
  --fab-ink: oklch(0.985 0.002 90);
  --acc: oklch(0.62 0.15 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-14__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid oklch(0.9 0.004 90);
}

.chm-14__page {
  padding: 40px 30px;
  display: grid;
  gap: 15px;
  align-content: start;
}

.chm-14__page h2 {
  font-size: 26px;
  letter-spacing: -.02em;
}

.chm-14__page p {
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--mut);
  max-width: 34ch;
  margin-bottom: 10px;
  text-wrap: pretty;
}

.chm-14__ln {
  height: 10px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.93 0.003 90);
}

.chm-14__dial {
  position: absolute;
  right: 18px;
  bottom: 86px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 10px;
}

.chm-14__item {
  display: flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 18px 0 14px;
  border-radius: 99px;
  background: oklch(1 0 0);
  border: 1px solid oklch(0.9 0.004 90);
  box-shadow: 0 10px 24px -14px oklch(0.2 0.01 90/.5);
  font-size: 13.5px;
  font-weight: 600;
  color: var(--ink);
  text-decoration: none;
  opacity: 0;
  translate: 0 14px;
  scale: .6;
  pointer-events: none;
  transition: opacity .25s,translate .45s cubic-bezier(.2,1.4,.35,1),scale .45s cubic-bezier(.2,1.4,.35,1),border-color .2s,color .2s;
}

.chm-14__item svg {
  width: 17px;
  height: 17px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

[data-open] .chm-14__item {
  opacity: 1;
  translate: 0 0;
  scale: 1;
  pointer-events: auto;
  transition-delay: calc(var(--i)*.05s);
}

.chm-14__item:hover,
.chm-14__item:focus-visible {
  border-color: var(--acc);
  color: var(--acc);
}

.chm-14__item:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-14__fab {
  position: absolute;
  right: 18px;
  bottom: 18px;
  width: 56px;
  height: 56px;
  border: none;
  border-radius: 50%;
  background: var(--fab);
  color: var(--fab-ink);
  cursor: pointer;
  display: grid;
  place-items: center;
  box-shadow: 0 14px 30px -12px color-mix(in oklch,var(--fab) 70%,transparent);
  transition: translate .2s,scale .15s,box-shadow .25s,background .3s;
}

.chm-14__fab:hover {
  translate: 0 -2px;
  box-shadow: 0 20px 36px -12px color-mix(in oklch,var(--fab) 65%,transparent);
}

.chm-14__fab:active {
  scale: .92;
}

.chm-14__fab:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-14__fab span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-14__fab i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-14__fab i:nth-child(1) {
  top: 0;
}

.chm-14__fab i:nth-child(2) {
  top: 5px;
}

.chm-14__fab i:nth-child(3) {
  top: 10px;
}

[data-open] .chm-14__fab i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

[data-open] .chm-14__fab i:nth-child(2) {
  opacity: 0;
}

[data-open] .chm-14__fab i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

@media (prefers-reduced-motion: reduce) {
  .chm-14 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-14__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('.chm-14__fab');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
  });
})();
```

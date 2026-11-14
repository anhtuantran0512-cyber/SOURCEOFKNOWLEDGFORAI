---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/full-screen-blur-overlay-hamburger-menu/"
title: "Full Screen Blur Overlay Hamburger Menu CSS"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The cinematic takeover: open the menu and the article behind stays visible but slips out of focus — a full-viewport backdrop-filter sheet blurs and darkens…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full Screen Blur Overlay Hamburger Menu CSS
Source: https://codefronts.com/navigation/css-hamburger-menus/full-screen-blur-overlay-hamburger-menu/

The cinematic takeover: open the menu and the article behind stays visible but slips out of focus — a full-viewport backdrop-filter sheet blurs and darkens the page like a camera pulling focus, while the menu links themselves arrive through a blur-to-sharp animation (filter: blur(14px) → 0 with letter-spacing settling). Depth-of-field as navigation. Where demo 07 is a glass panel OVER a page, this is the whole viewport becoming the lens.
## HTML
```html
<section class="chm-20" aria-label="Fullscreen blur overlay menu demo">
  <div class="chm-20__stage">
    <article class="chm-20__page" aria-hidden="true">
      <span class="chm-20__kicker">Field Notes · 07</span>
      <h2>The city at f/1.4</h2>
      <p>Night photography is an argument between what the eye saw and what the sensor kept. The lens holds one plane in confidence and lets the rest dissolve into rumor —</p>
      <p>streetlights become coins of light, faces become suggestions. Depth of field is an editor: it decides, frame by frame, what the story is about.</p>
      <p>The same is true of interfaces. Focus is a resource you spend.</p>
    </article>
    <nav class="chm-20__sheet" id="chm20-sheet" aria-label="Site">
      <a href="#stories" style="--i:0">Stories</a>
      <a href="#prints" style="--i:1">Prints</a>
      <a href="#workshops" style="--i:2">Workshops</a>
      <a href="#about" style="--i:3">About</a>
      <span class="chm-20__dof" style="--i:4" aria-hidden="true">ƒ/1.4 · everything else can wait</span>
    </nav>
    <header class="chm-20__bar">
      <span class="chm-20__brand">APERTURE&amp;CO</span>
      <button class="chm-20__btn" type="button" aria-expanded="false" aria-controls="chm20-sheet" aria-label="Open menu"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
    </header>
  </div>
</section>
```
## CSS
```css
.chm-20,
.chm-20 *,
.chm-20 *::before,
.chm-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-20 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.2 0.025 280);
  --ink: oklch(0.93 0.01 280);
  --mut: oklch(0.68 0.02 280);
  --acc: oklch(0.8 0.13 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-20__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 560px;
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid oklch(0.32 0.03 280);
  background: radial-gradient(130% 90% at 80% -10%,oklch(0.34 0.08 300/.8),transparent 55%),radial-gradient(100% 80% at 0% 110%,oklch(0.3 0.07 220/.7),transparent 50%),var(--bg);
}

.chm-20__page {
  padding: 96px 28px 28px;
  display: grid;
  gap: 14px;
  align-content: start;
  transition: scale .5s cubic-bezier(.2,.7,.2,1);
}

.chm-20__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--acc);
}

.chm-20__page h2 {
  font-size: 30px;
  letter-spacing: -.02em;
  line-height: 1.06;
}

.chm-20__page p {
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--mut);
  text-wrap: pretty;
}

.chm-20__sheet {
  position: absolute;
  inset: 0;
  z-index: 2;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 4px;
  padding: 0 34px;
  background: oklch(0.15 0.02 280/.55);
  -webkit-backdrop-filter: blur(18px) saturate(120%);
  backdrop-filter: blur(18px) saturate(120%);
  opacity: 0;
  visibility: hidden;
  transition: opacity .45s,visibility 0s .45s;
}

[data-open] .chm-20__sheet {
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}

@supports not (backdrop-filter: blur(1px)) {
  .chm-20__sheet {
    background: oklch(0.17 0.025 280/.93);
  }

  [data-open] .chm-20__page {
    scale: .96;
  }
}

.chm-20__sheet a {
  padding: 13px 0;
  font-size: 34px;
  font-weight: 700;
  letter-spacing: .12em;
  color: var(--ink);
  text-decoration: none;
  opacity: 0;
  filter: blur(14px);
  transition: opacity .4s,filter .5s,letter-spacing .6s cubic-bezier(.2,.7,.2,1),color .2s;
}

[data-open] .chm-20__sheet a {
  opacity: 1;
  filter: blur(0);
  letter-spacing: 0;
  transition-delay: calc(.15s + var(--i)*.07s),calc(.15s + var(--i)*.07s),calc(.15s + var(--i)*.07s),0s;
}

.chm-20__sheet a:hover,
.chm-20__sheet a:focus-visible {
  color: var(--acc);
}

.chm-20__sheet a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 5px;
  border-radius: 6px;
}

.chm-20__dof {
  margin-top: 26px;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--mut);
  opacity: 0;
  filter: blur(10px);
  transition: opacity .4s,filter .5s;
}

[data-open] .chm-20__dof {
  opacity: 1;
  filter: blur(0);
  transition-delay: calc(.15s + var(--i)*.07s);
}

.chm-20__bar {
  position: absolute;
  inset: 0 0 auto 0;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 76px;
  padding: 0 20px 0 26px;
}

.chm-20__brand {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .3em;
}

.chm-20__btn {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border: 1px solid oklch(1 0 0/.22);
  border-radius: 50%;
  background: oklch(1 0 0/.06);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  color: var(--ink);
  cursor: pointer;
  transition: background .25s,scale .2s;
}

.chm-20__btn:hover {
  background: oklch(1 0 0/.14);
  scale: 1.05;
}

.chm-20__btn:active {
  scale: .94;
}

.chm-20__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-20__btn span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-20__btn i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-20__btn i:nth-child(1) {
  top: 0;
}

.chm-20__btn i:nth-child(2) {
  top: 5px;
}

.chm-20__btn i:nth-child(3) {
  top: 10px;
}

[data-open] .chm-20__btn i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

[data-open] .chm-20__btn i:nth-child(2) {
  opacity: 0;
}

[data-open] .chm-20__btn i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

@media (prefers-reduced-motion: reduce) {
  .chm-20 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }

  .chm-20 .chm-20__sheet a,
    .chm-20 .chm-20__dof {
    filter: none;
    letter-spacing: 0;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-20__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('.chm-20__btn');
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

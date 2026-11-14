---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/claymorphism-card-component/"
title: "Claymorphism Card Component"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "The workhorse: a clay content card with a real photo, nested concentric radii, a clay avatar row, and a hover lift that promotes the card exactly one depth…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Claymorphism Card Component
Source: https://codefronts.com/design-styles/css-claymorphism/claymorphism-card-component/

The workhorse: a clay content card with a real photo, nested concentric radii, a clay avatar row, and a hover lift that promotes the card exactly one depth tier. It is also container-query driven — the same card switches from stacked to side-by-side based on its own width, not the viewport, so it drops into a sidebar or a full-width grid unchanged.
## HTML
```html
<section class="cl-13" aria-label="Claymorphism card component demo">
  <div class="cl-13__stage">
    <article class="cl-13__card">
      <figure class="cl-13__media">
        <img class="cl-13__img" width="640" height="640" loading="lazy" alt="Terracotta pottery bowls on a soft neutral background"
          src="https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?q=80&w=800&auto=format&fit=crop">
        <figcaption class="cl-13__tag">Module 04</figcaption>
      </figure>
      <div class="cl-13__body">
        <p class="cl-13__kicker">Interactive course</p>
        <h2 class="cl-13__h">Sculpting depth with CSS shadows</h2>
        <p class="cl-13__text">Six lessons on layered shadows, light discipline and the elevation scale — with every example built as one copyable snippet.</p>
        <div class="cl-13__meta">
          <ul class="cl-13__avatars">
            <li class="cl-13__av cl-13__av--a" aria-hidden="true"></li>
            <li class="cl-13__av cl-13__av--b" aria-hidden="true"></li>
            <li class="cl-13__av cl-13__av--c" aria-hidden="true"></li>
          </ul>
          <span class="cl-13__count">1,204 learners</span>
        </div>
        <div class="cl-13__foot">
          <button class="cl-13__btn" type="button">Start module</button>
          <button class="cl-13__save" type="button" aria-label="Save for later">
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M7 4h10a1 1 0 011 1v15l-6-3.6L6 20V5a1 1 0 011-1z" fill="currentColor"/></svg>
          </button>
        </div>
      </div>
    </article>
    <p class="cl-13__chip" aria-hidden="true">concentric radii · image in a clay well · @container layout switch</p>
  </div>
</section>
```
## CSS
```css
.cl-13,
.cl-13 *,
.cl-13 *::before,
.cl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-13-bg);
  --cl-13-bg: oklch(0.94 0.03 55);
  --cl-13-clay: oklch(0.9 0.05 55);
  --cl-13-accent: oklch(0.8 0.13 45);
  --cl-13-shade: oklch(0.56 0.09 50/.55);
  --cl-13-light: oklch(1 0.015 60/.95);
  --cl-13-ink: oklch(0.28 0.05 50);
  --cl-13-mut: oklch(0.5 0.04 50);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-13-ink);
}

.cl-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 30% 0%,oklch(0.97 0.035 70),transparent 66%);
}

.cl-13__card {
  --cl-13-r: 40px;
  --cl-13-p: 14px;
  container-type: inline-size;
  display: grid;
  gap: clamp(14px,2.4vw,18px);
  width: min(100%,560px);
  padding: var(--cl-13-p);
  border-radius: var(--cl-13-r);
  background: var(--cl-13-clay);
  box-shadow: 0 26px 46px -16px var(--cl-13-shade),inset 0 -16px 26px -12px var(--cl-13-shade),inset 0 18px 26px -8px var(--cl-13-light);
  transition: translate .4s cubic-bezier(.34,1.3,.5,1),box-shadow .4s;
}

.cl-13__card:hover {
  translate: 0 -8px;
  box-shadow: 0 40px 66px -20px var(--cl-13-shade),inset 0 -16px 26px -12px var(--cl-13-shade),inset 0 20px 28px -8px var(--cl-13-light);
}

@container (min-width: 430px) {
  .cl-13__card {
    grid-template-columns: 172px 1fr;
    align-items: stretch;
  }
}

.cl-13__media {
  position: relative;
  overflow: hidden;
  border-radius: calc(var(--cl-13-r) - var(--cl-13-p));
  background: linear-gradient(145deg,oklch(0.86 0.07 55),oklch(0.75 0.09 40));
}

.cl-13__media::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  box-shadow: inset 0 12px 22px -10px var(--cl-13-shade),inset 0 -10px 20px -12px oklch(0 0 0/.35);
  pointer-events: none;
}

.cl-13__img {
  display: block;
  width: 100%;
  height: 100%;
  min-height: 172px;
  object-fit: cover;
  transition: scale .5s cubic-bezier(.2,.7,.3,1);
}

.cl-13__card:hover .cl-13__img {
  scale: 1.04;
}

.cl-13__tag {
  position: absolute;
  left: 12px;
  top: 12px;
  padding: 6px 12px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--cl-13-ink);
  background: oklch(1 0 0/.82);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  box-shadow: 0 6px 12px -6px var(--cl-13-shade),inset 0 5px 8px -5px oklch(1 0 0);
}

.cl-13__body {
  display: grid;
  gap: 9px;
  align-content: center;
  padding: clamp(8px,2vw,14px) clamp(10px,2.4vw,18px) clamp(10px,2vw,14px);
}

.cl-13__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--cl-13-ink) 62%,transparent);
}

.cl-13__h {
  font-size: clamp(20px,3vw,25px);
  font-weight: 770;
  line-height: 1.2;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.cl-13__text {
  font-size: 13.5px;
  line-height: 1.6;
  color: color-mix(in oklch,var(--cl-13-ink) 80%,transparent);
  text-wrap: pretty;
}

.cl-13__meta {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 2px;
}

.cl-13__avatars {
  list-style: none;
  display: flex;
}

.cl-13__av {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-inline-start: -9px;
  box-shadow: 0 0 0 3px var(--cl-13-clay),inset 0 -5px 8px -6px var(--cl-13-shade),inset 0 6px 8px -5px var(--cl-13-light);
}

.cl-13__av:first-child {
  margin-inline-start: 0;
}

.cl-13__av--a {
  background: oklch(0.84 0.1 30);
}

.cl-13__av--b {
  background: oklch(0.84 0.09 190);
}

.cl-13__av--c {
  background: oklch(0.85 0.1 290);
}

.cl-13__count {
  font-size: 12.5px;
  color: var(--cl-13-mut);
  font-variant-numeric: tabular-nums;
}

.cl-13__foot {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 8px;
}

.cl-13__btn {
  flex: 1;
  min-height: 50px;
  padding: 0 22px;
  border: 0;
  border-radius: 22px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 680;
  color: oklch(0.25 0.06 45);
  cursor: pointer;
  background: var(--cl-13-accent);
  box-shadow: 0 14px 24px -10px var(--cl-13-shade),inset 0 -10px 16px -9px var(--cl-13-shade),inset 0 12px 16px -7px var(--cl-13-light);
  transition: translate .2s,box-shadow .2s,scale .2s cubic-bezier(.2,.8,.3,1.4);
}

.cl-13__btn:hover {
  translate: 0 -3px;
}

.cl-13__btn:active {
  scale: 1 .94;
  translate: 0 3px;
  box-shadow: inset 0 12px 18px -8px var(--cl-13-shade);
}

.cl-13__save {
  display: grid;
  place-items: center;
  width: 50px;
  height: 50px;
  flex: none;
  border: 0;
  border-radius: 20px;
  color: var(--cl-13-mut);
  cursor: pointer;
  background: color-mix(in oklch,var(--cl-13-clay) 62%,white);
  box-shadow: 0 10px 18px -10px var(--cl-13-shade),inset 0 -8px 13px -8px var(--cl-13-shade),inset 0 10px 13px -6px var(--cl-13-light);
  transition: color .25s,translate .2s;
}

.cl-13__save:hover {
  color: var(--cl-13-ink);
  translate: 0 -3px;
}

.cl-13__save:active {
  translate: 0 3px;
  box-shadow: inset 0 10px 16px -7px var(--cl-13-shade);
}

.cl-13__btn:focus-visible,
.cl-13__save:focus-visible {
  outline: 3px solid var(--cl-13-ink);
  outline-offset: 3px;
}

.cl-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-13-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-13-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-13 * {
    transition-duration: .01ms !important;
  }
}
```

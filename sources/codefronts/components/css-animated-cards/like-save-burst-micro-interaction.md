---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/like-save-burst-micro-interaction/"
title: "Like/Save Burst Micro-Interaction"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "The like that feels good to press: an overshooting heart, twelve particles thrown out on trigonometric angles, an expanding ring, and a count that rolls over…"
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Like/Save Burst Micro-Interaction
Source: https://codefronts.com/components/css-animated-cards/like-save-burst-micro-interaction/

The like that feels good to press: an overshooting heart, twelve particles thrown out on trigonometric angles, an expanding ring, and a count that rolls over — all CSS keyframes fired by a single class toggle. The particles are pure CSS (no canvas, no library), positioned with a rotate-then-translate trick so twelve elements need one keyframe between them.
## HTML
```html
<section class="ac-08" aria-label="Like and save burst micro-interaction demo">
  <div class="ac-08__stage">
    <header class="ac-08__head">
      <p class="ac-08__eyebrow">Micro-interaction</p>
      <h2 class="ac-08__title">A like worth pressing twice</h2>
    </header>
    <ul class="ac-08__grid" role="list">
      <li class="ac-08__card">
        <span class="ac-08__media"><img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=700&auto=format&fit=crop" alt="Portrait of a woman in warm light" loading="lazy" decoding="async" width="700" height="560"></span>
        <div class="ac-08__body">
          <div class="ac-08__meta"><h3 class="ac-08__name">Golden hour, no filter</h3><p class="ac-08__by">@rennadavis</p></div>
          <div class="ac-08__acts">
            <button class="ac-08__like" type="button" data-like aria-pressed="false">
              <span class="ac-08__ring" aria-hidden="true"></span>
              <span class="ac-08__burst" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>
              <svg class="ac-08__heart" viewBox="0 0 24 24" width="21" height="21" aria-hidden="true"><path d="M12 20.4l-1.5-1.36C5.4 14.4 2.4 11.7 2.4 8.4 2.4 5.9 4.4 4 6.9 4c1.5 0 2.9.7 3.8 1.8l1.3 1.5 1.3-1.5C14.2 4.7 15.6 4 17.1 4c2.5 0 4.5 1.9 4.5 4.4 0 3.3-3 6-8.1 10.66L12 20.4z"/></svg>
              <b class="ac-08__count" data-count>1,204</b>
              <span class="ac-08__sr" data-likesr>Like this post</span>
            </button>
            <button class="ac-08__save" type="button" data-save aria-pressed="false">
              <svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round" aria-hidden="true"><path d="M6 4h12v16l-6-4.2L6 20V4z"/></svg>
              <span class="ac-08__sr">Save this post</span>
            </button>
          </div>
        </div>
      </li>
      <li class="ac-08__card">
        <span class="ac-08__media"><img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=700&auto=format&fit=crop" alt="Blue abstract data light streaks" loading="lazy" decoding="async" width="700" height="560"></span>
        <div class="ac-08__body">
          <div class="ac-08__meta"><h3 class="ac-08__name">Signal, long exposure</h3><p class="ac-08__by">@kojiwrites</p></div>
          <div class="ac-08__acts">
            <button class="ac-08__like" type="button" data-like aria-pressed="false">
              <span class="ac-08__ring" aria-hidden="true"></span>
              <span class="ac-08__burst" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>
              <svg class="ac-08__heart" viewBox="0 0 24 24" width="21" height="21" aria-hidden="true"><path d="M12 20.4l-1.5-1.36C5.4 14.4 2.4 11.7 2.4 8.4 2.4 5.9 4.4 4 6.9 4c1.5 0 2.9.7 3.8 1.8l1.3 1.5 1.3-1.5C14.2 4.7 15.6 4 17.1 4c2.5 0 4.5 1.9 4.5 4.4 0 3.3-3 6-8.1 10.66L12 20.4z"/></svg>
              <b class="ac-08__count" data-count>318</b>
              <span class="ac-08__sr" data-likesr>Like this post</span>
            </button>
            <button class="ac-08__save" type="button" data-save aria-pressed="false">
              <svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round" aria-hidden="true"><path d="M6 4h12v16l-6-4.2L6 20V4z"/></svg>
              <span class="ac-08__sr">Save this post</span>
            </button>
          </div>
        </div>
      </li>
    </ul>
    <p class="ac-08__sr" role="status" aria-live="polite" data-status></p>
    <p class="ac-08__chip" aria-hidden="true">rotate() then translateY() particle fan · scale overshoot 1.35 → .92 → 1 · aria-pressed toggle · CSS-only burst</p>
  </div>
</section>
```
## CSS
```css
.ac-08,
.ac-08 *,
.ac-08 *::before,
.ac-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-08-bg: oklch(0.15 0.015 320);
  --ac-08-card: oklch(0.20 0.018 320);
  --ac-08-ink: oklch(0.97 0.004 300);
  --ac-08-mut: oklch(0.69 0.02 320);
  --ac-08-acc: oklch(0.66 0.23 12);
  --ac-08-line: oklch(1 0 0/.11);
  background: var(--ac-08-bg);
  color: var(--ac-08-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.6vw,26px);
  padding: clamp(20px,5vw,58px);
  background: radial-gradient(90% 60% at 50% 0%,color-mix(in oklch,var(--ac-08-acc) 12%,transparent),transparent 62%);
}

.ac-08__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
}

.ac-08__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-08-acc);
}

.ac-08__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-08__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(258px,1fr));
  gap: 14px;
  width: min(100%,700px);
  list-style: none;
}

.ac-08__card {
  display: grid;
  border: 1px solid var(--ac-08-line);
  border-radius: 20px;
  overflow: hidden;
  background: var(--ac-08-card);
}

.ac-08__media {
  display: block;
  aspect-ratio: 5/4;
  background: linear-gradient(135deg,oklch(0.36 0.08 340),oklch(0.26 0.05 300));
}

.ac-08__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.ac-08__body {
  display: grid;
  gap: 12px;
  padding: 14px 14px 12px;
}

.ac-08__meta {
  display: grid;
  gap: 3px;
}

.ac-08__name {
  font-size: 15px;
  font-weight: 640;
  letter-spacing: -.02em;
}

.ac-08__by {
  font-size: 12.5px;
  color: var(--ac-08-mut);
}

.ac-08__acts {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ac-08__like {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 16px;
  border: 1px solid var(--ac-08-line);
  border-radius: 99px;
  background: transparent;
  color: var(--ac-08-mut);
  font-family: inherit;
  cursor: pointer;
  transition: background .2s,color .2s,border-color .2s;
}

.ac-08__like:hover {
  background: oklch(1 0 0/.05);
  color: var(--ac-08-ink);
}

.ac-08__like:focus-visible {
  outline: 2px solid var(--ac-08-acc);
  outline-offset: 3px;
}

.ac-08__like[aria-pressed="true"] {
  color: var(--ac-08-acc);
  border-color: color-mix(in oklch,var(--ac-08-acc) 45%,transparent);
  background: color-mix(in oklch,var(--ac-08-acc) 12%,transparent);
}

.ac-08__heart {
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  flex: none;
  transition: fill .2s;
}

.ac-08__like[aria-pressed="true"] .ac-08__heart {
  fill: var(--ac-08-acc);
  stroke: var(--ac-08-acc);
}

.ac-08__like[data-burst] .ac-08__heart {
  animation: ac-08-pop .55s cubic-bezier(.2,.7,.3,1);
}

@keyframes ac-08-pop {
  0% {
    scale: .2;
  }

  45% {
    scale: 1.35;
  }

  70% {
    scale: .92;
  }

  100% {
    scale: 1;
  }
}

.ac-08__count {
  font-size: 13.5px;
  font-weight: 650;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.01em;
}

.ac-08__ring {
  position: absolute;
  left: 16px;
  top: 50%;
  width: 21px;
  height: 21px;
  margin-top: -10.5px;
  border-radius: 50%;
  border: 2px solid var(--ac-08-acc);
  opacity: 0;
  pointer-events: none;
}

.ac-08__like[data-burst] .ac-08__ring {
  animation: ac-08-ring .6s cubic-bezier(.2,.7,.3,1);
}

@keyframes ac-08-ring {
  0% {
    opacity: .9;
    scale: .3;
  }

  70% {
    opacity: .25;
  }

  100% {
    opacity: 0;
    scale: 2.6;
  }
}

.ac-08__burst {
  position: absolute;
  left: 26.5px;
  top: 50%;
  width: 0;
  height: 0;
  pointer-events: none;
}

.ac-08__burst i {
  position: absolute;
  left: -3px;
  top: -3px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--ac-08-acc);
  opacity: 0;
  transform: rotate(var(--ac-08-a)) translateY(0) scale(0);
}

.ac-08__burst i:nth-child(2) {
  --ac-08-a: 30deg;
  background: oklch(0.80 0.18 60);
}

.ac-08__burst i:nth-child(3) {
  --ac-08-a: 60deg;
}

.ac-08__burst i:nth-child(4) {
  --ac-08-a: 90deg;
  background: oklch(0.75 0.19 330);
}

.ac-08__burst i:nth-child(5) {
  --ac-08-a: 120deg;
}

.ac-08__burst i:nth-child(6) {
  --ac-08-a: 150deg;
  background: oklch(0.80 0.18 60);
}

.ac-08__burst i:nth-child(7) {
  --ac-08-a: 180deg;
}

.ac-08__burst i:nth-child(8) {
  --ac-08-a: 210deg;
  background: oklch(0.75 0.19 330);
}

.ac-08__burst i:nth-child(9) {
  --ac-08-a: 240deg;
}

.ac-08__burst i:nth-child(10) {
  --ac-08-a: 270deg;
  background: oklch(0.80 0.18 60);
}

.ac-08__burst i:nth-child(11) {
  --ac-08-a: 300deg;
}

.ac-08__burst i:nth-child(12) {
  --ac-08-a: 330deg;
  background: oklch(0.75 0.19 330);
}

.ac-08__burst i:nth-child(1) {
  --ac-08-a: 0deg;
}

.ac-08__like[data-burst] .ac-08__burst i {
  animation: ac-08-fly .62s cubic-bezier(.2,.7,.3,1) forwards;
}

.ac-08__like[data-burst] .ac-08__burst i:nth-child(even) {
  animation-duration: .72s;
  animation-delay: .04s;
}

@keyframes ac-08-fly {
  0% {
    opacity: 1;
    transform: rotate(var(--ac-08-a)) translateY(-4px) scale(0);
  }

  35% {
    opacity: 1;
    transform: rotate(var(--ac-08-a)) translateY(-24px) scale(1);
  }

  100% {
    opacity: 0;
    transform: rotate(var(--ac-08-a)) translateY(-38px) scale(0);
  }
}

.ac-08__save {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border: 1px solid var(--ac-08-line);
  border-radius: 99px;
  background: transparent;
  color: var(--ac-08-mut);
  cursor: pointer;
  transition: background .2s,color .2s,border-color .2s;
}

.ac-08__save:hover {
  background: oklch(1 0 0/.05);
  color: var(--ac-08-ink);
}

.ac-08__save:focus-visible {
  outline: 2px solid var(--ac-08-acc);
  outline-offset: 3px;
}

.ac-08__save[aria-pressed="true"] {
  color: oklch(0.85 0.16 88);
  border-color: color-mix(in oklch,oklch(0.85 0.16 88) 45%,transparent);
}

.ac-08__save[aria-pressed="true"] svg {
  fill: oklch(0.85 0.16 88);
  animation: ac-08-tuck .45s cubic-bezier(.2,.7,.3,1);
}

@keyframes ac-08-tuck {
  0% {
    translate: 0 -6px;
    scale: .8;
  }

  60% {
    translate: 0 2px;
  }

  100% {
    translate: 0 0;
    scale: 1;
  }
}

.ac-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ac-08__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-08-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-08-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,700px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-08__burst,
    .ac-08__ring {
    display: none;
  }

  .ac-08__like[data-burst] .ac-08__heart {
    animation: none;
  }

  .ac-08__save[aria-pressed="true"] svg {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const nf = new Intl.NumberFormat('en-US');
  document.querySelectorAll('.ac-08').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const status = root.querySelector('[data-status]');

    root.querySelectorAll('[data-like]').forEach((btn) => {
      const out = btn.querySelector('[data-count]');
      const sr = btn.querySelector('[data-likesr]');
      let n = +out.textContent.replace(/,/g, '');
      btn.addEventListener('click', () => {
        const on = btn.getAttribute('aria-pressed') !== 'true';
        btn.setAttribute('aria-pressed', String(on));
        n += on ? 1 : -1;
        out.textContent = nf.format(n);
        sr.textContent = on ? 'Unlike this post' : 'Like this post';
        if (on) {
          btn.removeAttribute('data-burst');
          void btn.offsetWidth;                 // reflow so the keyframes restart on re-like
          btn.dataset.burst = '';
        } else {
          btn.removeAttribute('data-burst');    // undo gets no celebration
        }
        status.textContent = (on ? 'Liked. ' : 'Like removed. ') + nf.format(n) + ' likes.';
      });
    });

    root.querySelectorAll('[data-save]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const on = btn.getAttribute('aria-pressed') !== 'true';
        btn.setAttribute('aria-pressed', String(on));
        status.textContent = on ? 'Saved to your collection.' : 'Removed from your collection.';
      });
    });
  });
})();
```

---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/blur-to-sharp-lazy-image-card/"
title: "Blur-to-Sharp Lazy Image Card"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "The blur-up every image-heavy card grid should ship: a tiny gradient or LQIP renders instantly, the real photo decodes off-thread, then unblurs and settles…"
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blur-to-Sharp Lazy Image Card
Source: https://codefronts.com/components/css-animated-cards/blur-to-sharp-lazy-image-card/

The blur-up every image-heavy card grid should ship: a tiny gradient or LQIP renders instantly, the real photo decodes off-thread, then unblurs and settles into place. Zero layout shift because the aspect-ratio is reserved up front, and the whole reveal is four CSS declarations plus img.decode(). Press Reload images to watch it again with a simulated slow connection.
## HTML
```html
<section class="ac-05" aria-label="Blur to sharp lazy image card demo">
  <div class="ac-05__stage">
    <header class="ac-05__head">
      <p class="ac-05__eyebrow">Progressive imagery</p>
      <h2 class="ac-05__title">Blur-up cards with zero layout shift</h2>
      <button class="ac-05__btn" type="button" data-reload>
        <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>
        Reload images
      </button>
    </header>
    <ul class="ac-05__grid" role="list">
      <li class="ac-05__card" style="--ac-05-a:oklch(0.55 0.13 235);--ac-05-b:oklch(0.30 0.08 265)">
        <span class="ac-05__media"><img class="ac-05__img" data-img data-src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=800&auto=format&fit=crop" alt="Mist between tall conifers at dawn" width="800" height="533" loading="lazy" decoding="async"></span>
        <div class="ac-05__body"><h3 class="ac-05__name">Cascade Ridge</h3><p class="ac-05__meta">Oregon · 4.8 MB source</p></div>
      </li>
      <li class="ac-05__card" style="--ac-05-a:oklch(0.62 0.14 55);--ac-05-b:oklch(0.34 0.09 30)">
        <span class="ac-05__media"><img class="ac-05__img" data-img data-src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?q=80&w=800&auto=format&fit=crop" alt="Sunrise light across a mountain range" width="800" height="533" loading="lazy" decoding="async"></span>
        <div class="ac-05__body"><h3 class="ac-05__name">Golden Hour Pass</h3><p class="ac-05__meta">Dolomites · 6.1 MB source</p></div>
      </li>
      <li class="ac-05__card" style="--ac-05-a:oklch(0.58 0.10 165);--ac-05-b:oklch(0.30 0.06 195)">
        <span class="ac-05__media"><img class="ac-05__img" data-img data-src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=800&auto=format&fit=crop" alt="Sunbeams through a green forest canopy" width="800" height="533" loading="lazy" decoding="async"></span>
        <div class="ac-05__body"><h3 class="ac-05__name">Understory</h3><p class="ac-05__meta">Vancouver Island · 5.2 MB source</p></div>
      </li>
    </ul>
    <p class="ac-05__status" role="status" aria-live="polite" data-status>Ready</p>
    <p class="ac-05__chip" aria-hidden="true">aspect-ratio reservation · gradient LQIP · img.decode() · blur(18px) → 0 with 6% overscale</p>
  </div>
</section>
```
## CSS
```css
.ac-05,
.ac-05 *,
.ac-05 *::before,
.ac-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-05-bg: oklch(0.17 0.014 255);
  --ac-05-card: oklch(0.22 0.016 255);
  --ac-05-ink: oklch(0.97 0.004 260);
  --ac-05-mut: oklch(0.70 0.02 260);
  --ac-05-acc: oklch(0.83 0.14 195);
  --ac-05-line: oklch(1 0 0/.11);
  background: var(--ac-05-bg);
  color: var(--ac-05-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.6vw,28px);
  padding: clamp(20px,5vw,58px);
  background: radial-gradient(100% 70% at 50% 0%,color-mix(in oklch,var(--ac-05-acc) 10%,transparent),transparent 62%);
}

.ac-05__head {
  display: grid;
  justify-items: center;
  gap: 11px;
  text-align: center;
}

.ac-05__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-05-acc);
}

.ac-05__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-05__btn {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 20px;
  margin-top: 4px;
  border: 1px solid var(--ac-05-line);
  border-radius: 99px;
  background: oklch(1 0 0/.05);
  color: var(--ac-05-ink);
  font-size: 14px;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: background .2s,transform .2s;
}

.ac-05__btn:hover {
  background: oklch(1 0 0/.1);
  transform: translateY(-1px);
}

.ac-05__btn:focus-visible {
  outline: 2px solid var(--ac-05-acc);
  outline-offset: 3px;
}

.ac-05__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(240px,1fr));
  gap: clamp(13px,1.8vw,18px);
  width: min(100%,940px);
  list-style: none;
}

.ac-05__card {
  display: grid;
  gap: 0;
  border: 1px solid var(--ac-05-line);
  border-radius: 20px;
  overflow: hidden;
  background: var(--ac-05-card);
}

.ac-05__media {
  position: relative;
  display: block;
  aspect-ratio: 3/2;
  overflow: clip;
  background: linear-gradient(135deg,var(--ac-05-a),var(--ac-05-b));
}

.ac-05__media::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(115deg,transparent 30%,oklch(1 0 0/.10) 50%,transparent 70%);
  background-size: 220% 100%;
  animation: ac-05-sweep 1.5s linear infinite;
  opacity: 1;
  transition: opacity .4s;
}

.ac-05__media:has(.ac-05__img[data-loaded])::after {
  opacity: 0;
  animation: none;
}

.ac-05__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: 0;
  filter: blur(18px) saturate(1.4);
  scale: 1.06;
  transition: opacity .55s ease-out,filter .7s cubic-bezier(.16,1,.3,1),scale .7s cubic-bezier(.16,1,.3,1);
}

.ac-05__img[data-loaded] {
  opacity: 1;
  filter: blur(0) saturate(1);
  scale: 1;
}

.ac-05__body {
  display: grid;
  gap: 4px;
  padding: 15px 16px 18px;
}

.ac-05__name {
  font-size: 15.5px;
  font-weight: 640;
  letter-spacing: -.02em;
}

.ac-05__meta {
  font-size: 12.5px;
  color: var(--ac-05-mut);
  font-variant-numeric: tabular-nums;
}

.ac-05__status {
  font-size: 12.5px;
  color: var(--ac-05-mut);
  font-variant-numeric: tabular-nums;
}

.ac-05__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-05-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-05-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,680px);
}

@keyframes ac-05-sweep {
  from {
    background-position: 120% 0;
  }

  to {
    background-position: -120% 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ac-05__img {
    transition-duration: .01ms;
  }

  .ac-05__media::after {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.ac-05').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const imgs = [...root.querySelectorAll('[data-img]')];
    const status = root.querySelector('[data-status]');

    const load = (img, delay) => new Promise((done) => setTimeout(() => {
      img.removeAttribute('data-loaded');
      img.src = img.dataset.src + '&cb=' + Date.now();
      const reveal = () => { img.dataset.loaded = ''; done(); };
      // decode() resolves when the frame is paint-ready — load fires before rasterisation finishes
      if (img.decode) img.decode().then(reveal, reveal); else img.addEventListener('load', reveal, { once: true });
    }, delay));

    const run = () => {
      status.textContent = 'Decoding ' + imgs.length + ' images…';
      Promise.all(imgs.map((img, i) => load(img, 180 + i * 260)))
        .then(() => { status.textContent = 'All images decoded and revealed.'; });
    };

    root.querySelector('[data-reload]').addEventListener('click', run);
    run();
  });
})();
```

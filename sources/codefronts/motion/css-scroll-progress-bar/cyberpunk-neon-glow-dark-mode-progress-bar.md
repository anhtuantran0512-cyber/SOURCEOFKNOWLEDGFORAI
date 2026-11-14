---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/cyberpunk-neon-glow-dark-mode-progress-bar/"
title: "Cyberpunk / Neon Glow Dark-Mode Progress Bar"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "A neon tube rather than a rectangle: three stacked shadows produce a real bloom, a brighter nib burns at the leading edge, and a faint scanline layer sits…"
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk / Neon Glow Dark-Mode Progress Bar
Source: https://codefronts.com/motion/css-scroll-progress-bar/cyberpunk-neon-glow-dark-mode-progress-bar/

A neon tube rather than a rectangle: three stacked shadows produce a real bloom, a brighter nib burns at the leading edge, and a faint scanline layer sits over the whole page. It is the maximalist end of this collection — and it is built from four declarations, not a canvas.
## HTML
```html
<section class="sp-17" aria-label="Cyberpunk neon glow scroll progress bar demo">
  <div class="sp-17__scan" aria-hidden="true"></div>
  <div class="sp-17__rail" role="progressbar" aria-label="Reading progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="sp-17-rail"><i class="sp-17__fill"><b class="sp-17__nib"></b></i></div>
  <header class="sp-17__bar">
    <a class="sp-17__brand" href="#sp-17-s1"><span class="sp-17__logo" aria-hidden="true"></span>NEON<span class="sp-17__brandthin">//grid</span></a>
    <p class="sp-17__meta" id="sp-17-pct">00%</p>
  </header>
  <div class="sp-17__intro">
    <p class="sp-17__intro-eyebrow">three shadows, one tube</p>
    <h2 class="sp-17__intro-title">Light, not blur</h2>
    <p class="sp-17__intro-sub">Scroll. The rail burns brighter at its leading edge, the scanlines sit over everything, and none of it costs a frame.</p>
  </div>
  <main class="sp-17__main">
    <section class="sp-17__sec" id="sp-17-s1">
      <p class="sp-17__kicker">// 01 bloom</p>
      <h3 class="sp-17__h">Stack the falloff</h3>
      <p class="sp-17__p sp-17__p--lede">Real light fades in layers. Three shadows at 4px, 12px and 34px with decreasing opacity produce a tube; one 30px shadow produces a smudge.</p>
    </section>
    <section class="sp-17__sec" id="sp-17-s2">
      <p class="sp-17__kicker">// 02 nib</p>
      <h3 class="sp-17__h">drop-shadow follows the alpha</h3>
      <p class="sp-17__p">A <code>box-shadow</code> glows in the shape of the box. A <code>drop-shadow</code> filter glows in the shape of what is actually painted — which is why the rounded nib has a rounded halo.</p>
      <figure class="sp-17__fig">
        <img class="sp-17__img" src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&amp;fit=crop&amp;w=1400&amp;q=70" alt="Green digital code cascading down a dark screen" loading="lazy" decoding="async">
        <figcaption class="sp-17__cap">Atmosphere is paint. Two gradients and a vignette, no elements.</figcaption>
      </figure>
    </section>
    <section class="sp-17__sec" id="sp-17-s3">
      <p class="sp-17__kicker">// 03 legibility</p>
      <h3 class="sp-17__h">Only the accents glow</h3>
      <p class="sp-17__p">Body copy stays a low-chroma near-white. Glowing paragraphs are the fastest way to make a beautiful dark theme unusable — and neon on black often fails contrast even when it looks bright.</p>
    </section>
    <section class="sp-17__sec" id="sp-17-s4">
      <p class="sp-17__kicker">// 04 respect</p>
      <h3 class="sp-17__h">Let the system win</h3>
      <p class="sp-17__p">Under <code>forced-colors</code> every glow is dropped so the OS high-contrast palette renders cleanly. Under <code>prefers-reduced-motion</code> the bar stops pulsing and simply fills.</p>
      <p class="sp-17__chip">3 shadows · 1 filter · 0 canvas</p>
    </section>
  </main>
  <footer class="sp-17__pagefoot"><p class="sp-17__pagefootin">Scroll progress pattern 17 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-17 {
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --sp-17-neon: oklch(0.78 0.19 195);
  --sp-17-neon2: oklch(0.68 0.25 330);
  --sp-17-bg: oklch(0.13 0.02 275);
  --sp-17-ink: oklch(0.94 0.01 220);
  --sp-17-mut: oklch(0.68 0.02 230);
  --sp-17-line: oklch(0.78 0.19 195/.22);
  --sp-17-p: 0;
  background: radial-gradient(120% 70% at 50% -10%,oklch(0.2 0.07 280),transparent),var(--sp-17-bg);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-17-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-17 *,
.sp-17 *::before,
.sp-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-17__scan {
  position: fixed;
  inset: 0;
  z-index: 58;
  pointer-events: none;
  background: repeating-linear-gradient(180deg,oklch(1 0 0/.035) 0 1px,transparent 1px 3px);
  mix-blend-mode: screen;
  opacity: .7;
}

.sp-17__rail {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 4px;
  z-index: 60;
  background: oklch(0.78 0.19 195/.1);
  pointer-events: none;
}

.sp-17__fill {
  position: relative;
  display: block;
  block-size: 100%;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-17-p));
  background: linear-gradient(90deg,var(--sp-17-neon2),var(--sp-17-neon));
  box-shadow: 0 0 4px var(--sp-17-neon),0 0 12px color-mix(in oklch,var(--sp-17-neon) 70%,transparent),0 0 34px color-mix(in oklch,var(--sp-17-neon) 40%,transparent);
}

.sp-17__nib {
  position: absolute;
  inset-block: -3px;
  inset-inline-end: -1px;
  inline-size: 3px;
  border-radius: 99px;
  background: oklch(0.99 0.02 195);
  filter: drop-shadow(0 0 6px var(--sp-17-neon)) drop-shadow(0 0 14px var(--sp-17-neon));
}

@supports (animation-timeline: scroll()) {
  .sp-17__fill {
    transform: scaleX(0);
    animation: sp-17-fill linear both;
    animation-timeline: scroll(root block);
  }
}

@keyframes sp-17-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-17__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 58px;
  padding-block-start: 4px;
  background: color-mix(in oklch,var(--sp-17-bg) 74%,transparent);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-block-end: 1px solid var(--sp-17-line);
}

.sp-17__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  color: var(--sp-17-neon);
  text-decoration: none;
  text-shadow: 0 0 10px color-mix(in oklch,var(--sp-17-neon) 60%,transparent);
}

.sp-17__brandthin {
  color: var(--sp-17-mut);
  text-shadow: none;
  font-weight: 400;
}

.sp-17__brand:focus-visible {
  outline: 2px solid var(--sp-17-neon);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-17__logo {
  inline-size: 14px;
  block-size: 14px;
  background: var(--sp-17-neon);
  clip-path: polygon(50% 0,100% 50%,50% 100%,0 50%);
  box-shadow: 0 0 12px var(--sp-17-neon);
}

.sp-17__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  font-variant-numeric: tabular-nums;
  letter-spacing: .14em;
  color: var(--sp-17-neon2);
  text-shadow: 0 0 10px color-mix(in oklch,var(--sp-17-neon2) 55%,transparent);
}

.sp-17__intro {
  display: grid;
  gap: 16px;
  padding-block: clamp(50px,11vh,124px) clamp(26px,6vh,58px);
}

.sp-17__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--sp-17-neon);
}

.sp-17__intro-title {
  font-size: clamp(42px,8vw,96px);
  line-height: .94;
  letter-spacing: -.045em;
  font-weight: 760;
  max-inline-size: 12ch;
  text-wrap: balance;
  text-shadow: 0 0 24px color-mix(in oklch,var(--sp-17-neon) 45%,transparent),2px 0 0 color-mix(in oklch,var(--sp-17-neon2) 55%,transparent);
}

.sp-17__intro-sub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: var(--sp-17-mut);
  max-inline-size: 52ch;
  text-wrap: pretty;
}

.sp-17__sec {
  scroll-margin-top: 74px;
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 76svh;
  padding-block: clamp(26px,5vw,52px);
  border-block-end: 1px solid oklch(1 0 0/.08);
}

.sp-17__sec:last-child {
  border-block-end: 0;
}

.sp-17__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--sp-17-neon);
}

.sp-17__h {
  font-size: clamp(23px,3.3vw,36px);
  line-height: 1.08;
  letter-spacing: -.034em;
  font-weight: 730;
  text-wrap: balance;
}

.sp-17__p {
  max-inline-size: 60ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-17-mut);
  text-wrap: pretty;
}

.sp-17__p--lede {
  font-size: 17.8px;
  color: var(--sp-17-ink);
}

.sp-17__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.78 0.19 195/.14);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--sp-17-neon);
}

.sp-17__fig {
  display: grid;
  gap: 9px;
  max-inline-size: 68ch;
}

.sp-17__img {
  inline-size: 100%;
  aspect-ratio: 16/7;
  object-fit: cover;
  display: block;
  border-radius: 14px;
  border: 1px solid var(--sp-17-line);
  background: linear-gradient(135deg,oklch(0.32 0.1 200),oklch(0.2 0.08 300));
  filter: saturate(1.15);
}

.sp-17__cap {
  font-size: 12.6px;
  color: var(--sp-17-mut);
}

.sp-17__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-17-neon);
  padding: 7px 13px;
  border-radius: 99px;
  background: oklch(0.78 0.19 195/.1);
  border: 1px solid var(--sp-17-line);
  box-shadow: 0 0 18px -6px var(--sp-17-neon);
}

.sp-17__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(40px,8vh,100px) 24px;
  border-block-start: 1px solid var(--sp-17-line);
}

.sp-17__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .1em;
  color: var(--sp-17-mut);
  text-align: center;
}

.sp-17__bar,
.sp-17__intro,
.sp-17__sec {
  padding-inline: max(clamp(18px,4vw,36px),calc((100% - 900px)/2));
}

:root:has(.sp-17) {
  scroll-behavior: smooth;
  scroll-padding-top: 74px;
}

@media (max-width: 600px) {
  .sp-17__sec {
    min-block-size: auto;
  }

  .sp-17__scan {
    opacity: .45;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-17) {
    scroll-behavior: auto;
  }

  .sp-17 * {
    transition-duration: .01ms !important;
  }
}

@media (forced-colors: active) {
  .sp-17__fill,
    .sp-17__nib,
    .sp-17__chip,
    .sp-17__brand,
    .sp-17__meta,
    .sp-17__intro-title {
    box-shadow: none;
    filter: none;
    text-shadow: none;
  }

  .sp-17__scan {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-17');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const rail = root.querySelector('#sp-17-rail');
  const pct = root.querySelector('#sp-17-pct');
  const native = CSS.supports('animation-timeline', 'scroll()');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    if (!native) root.style.setProperty('--sp-17-p', p.toFixed(4));
    const n = Math.round(p * 100);
    pct.textContent = String(n).padStart(2, '0') + '%';
    rail.setAttribute('aria-valuenow', String(n));
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
})();
```

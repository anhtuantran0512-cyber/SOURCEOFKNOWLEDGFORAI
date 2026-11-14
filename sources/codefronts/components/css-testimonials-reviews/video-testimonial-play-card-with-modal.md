---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/video-testimonial-play-card-with-modal/"
title: "Video Testimonial Play Card with Modal"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Video social proof converts harder than text for high-ticket SaaS and services — this is the grid of play cards plus the lightbox that opens them."
has_js: "true"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Testimonial Play Card with Modal
Source: https://codefronts.com/components/css-testimonials-reviews/video-testimonial-play-card-with-modal/

Video social proof converts harder than text for high-ticket SaaS and services — this is the grid of play cards plus the lightbox that opens them. The modal is a native <dialog> animated in and out with @starting-style and transition-behavior: allow-discrete, which means a real fade-and-lift on both open and close with no JS timers and no setTimeout before close().
## HTML
```html
<section class="tr-05" aria-label="Video testimonial play card with modal demo">
  <div class="tr-05__stage">
    <header class="tr-05__head">
      <p class="tr-05__eyebrow">Video stories</p>
      <h2 class="tr-05__title">Two minutes each. Straight from the people who run it.</h2>
    </header>

    <div class="tr-05__grid">
      <article class="tr-05__card">
        <button class="tr-05__play" type="button" data-video="https://www.youtube-nocookie.com/embed/aqz-KE-bpKQ" aria-label="Play video testimonial from Ines Bakker, 2 minutes 14 seconds">
          <img src="https://images.unsplash.com/photo-1573496799652-408c2ac9fe98?q=80&w=800&auto=format&fit=crop" alt="Ines Bakker speaking to camera in a bright office" width="640" height="360" loading="lazy" decoding="async">
          <span class="tr-05__scrim"></span>
          <span class="tr-05__btn" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.2l11 6.8-11 6.8z" fill="currentColor"/></svg></span>
          <span class="tr-05__len" aria-hidden="true">2:14</span>
        </button>
        <div class="tr-05__body">
          <blockquote>“We stopped guessing which accounts were at risk.”</blockquote>
          <p class="tr-05__who"><b>Ines Bakker</b> · VP Customer Success, Kettleworth</p>
        </div>
      </article>

      <article class="tr-05__card">
        <button class="tr-05__play" type="button" data-video="https://www.youtube-nocookie.com/embed/aqz-KE-bpKQ" aria-label="Play video testimonial from Devon Clarke, 1 minute 48 seconds">
          <img src="https://images.unsplash.com/photo-1580894742597-87bc8789db3d?q=80&w=800&auto=format&fit=crop" alt="Devon Clarke on a video call at a desk" width="640" height="360" loading="lazy" decoding="async">
          <span class="tr-05__scrim"></span>
          <span class="tr-05__btn" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.2l11 6.8-11 6.8z" fill="currentColor"/></svg></span>
          <span class="tr-05__len" aria-hidden="true">1:48</span>
        </button>
        <div class="tr-05__body">
          <blockquote>“Payback was eleven weeks. I showed the board the same dashboard.”</blockquote>
          <p class="tr-05__who"><b>Devon Clarke</b> · CFO, Harrow &amp; Bell</p>
        </div>
      </article>

      <article class="tr-05__card">
        <button class="tr-05__play" type="button" data-video="https://www.youtube-nocookie.com/embed/aqz-KE-bpKQ" aria-label="Play video testimonial from Amara Diallo, 3 minutes 6 seconds">
          <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800&auto=format&fit=crop" alt="Amara Diallo with her team around a meeting table" width="640" height="360" loading="lazy" decoding="async">
          <span class="tr-05__scrim"></span>
          <span class="tr-05__btn" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.2l11 6.8-11 6.8z" fill="currentColor"/></svg></span>
          <span class="tr-05__len" aria-hidden="true">3:06</span>
        </button>
        <div class="tr-05__body">
          <blockquote>“Forty-one people onboarded in a day, with no training budget.”</blockquote>
          <p class="tr-05__who"><b>Amara Diallo</b> · Director of Ops, Fernbrook</p>
        </div>
      </article>
    </div>

    <dialog class="tr-05__dlg" aria-label="Video testimonial player">
      <div class="tr-05__player">
        <iframe class="tr-05__frame" title="Customer video testimonial" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>
      </div>
      <button class="tr-05__close" type="button" aria-label="Close video">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </dialog>

    <p class="tr-05__chip" aria-hidden="true">&lt;dialog&gt; showModal · @starting-style · transition-behavior:allow-discrete · lazy iframe src</p>
  </div>
</section>
```
## CSS
```css
.tr-05,
.tr-05 *,
.tr-05 *::before,
.tr-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-05-bg: oklch(0.16 0.018 275);
  --tr-05-card: oklch(0.22 0.024 275);
  --tr-05-ink: oklch(0.97 0.005 275);
  --tr-05-mut: oklch(0.71 0.02 275);
  --tr-05-acc: oklch(0.72 0.19 22);
  background: var(--tr-05-bg);
  color: var(--tr-05-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,34px);
  padding: clamp(20px,5vw,60px);
}

.tr-05__head {
  text-align: center;
  display: grid;
  gap: 10px;
  max-width: 22ch;
}

.tr-05__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tr-05-acc);
}

.tr-05__title {
  font-size: clamp(24px,4vw,42px);
  font-weight: 670;
  letter-spacing: -.035em;
  line-height: 1.1;
  text-wrap: balance;
}

.tr-05__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,272px),1fr));
  gap: clamp(14px,2vw,22px);
  width: min(100%,1060px);
}

.tr-05__card {
  display: grid;
  grid-template-rows: auto 1fr;
  border-radius: 18px;
  overflow: hidden;
  background: var(--tr-05-card);
  border: 1px solid oklch(1 0 0/.09);
  box-shadow: 0 24px 50px -32px oklch(0 0 0/.95);
  animation: tr-05-in .7s cubic-bezier(.16,1,.3,1) both;
}

.tr-05__card:nth-child(2) {
  animation-delay: .09s;
}

.tr-05__card:nth-child(3) {
  animation-delay: .18s;
}

@keyframes tr-05-in {
  from {
    opacity: 0;
    translate: 0 18px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-05__play {
  position: relative;
  display: block;
  width: 100%;
  aspect-ratio: 16/9;
  padding: 0;
  border: 0;
  background: linear-gradient(140deg,oklch(0.4 0.06 275),oklch(0.3 0.05 300));
  cursor: pointer;
  overflow: hidden;
}

.tr-05__play img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: scale .6s cubic-bezier(.16,1,.3,1),filter .4s;
}

.tr-05__play:hover img,
.tr-05__play:focus-visible img {
  scale: 1.06;
  filter: saturate(1.08);
}

.tr-05__play:focus-visible {
  outline: 3px solid var(--tr-05-acc);
  outline-offset: -3px;
}

.tr-05__scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,oklch(0 0 0/.05),oklch(0 0 0/.55));
  transition: opacity .4s;
}

.tr-05__btn {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  translate: -50% -50%;
  display: grid;
  place-items: center;
  width: 62px;
  height: 62px;
  border-radius: 50%;
  background: oklch(1 0 0/.14);
  color: oklch(0.99 0 0);
  border: 1px solid oklch(1 0 0/.4);
  backdrop-filter: blur(8px);
  transition: scale .35s cubic-bezier(.16,1,.3,1),background .35s;
}

.tr-05__btn svg {
  width: 26px;
  height: 26px;
  margin-inline-start: 3px;
}

.tr-05__btn::after {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: 50%;
  border: 1px solid color-mix(in oklch,var(--tr-05-acc) 70%,transparent);
  animation: tr-05-ping 2.6s cubic-bezier(.16,1,.3,1) infinite;
}

@keyframes tr-05-ping {
  0% {
    scale: 1;
    opacity: .85;
  }

  70%,
    100% {
    scale: 1.7;
    opacity: 0;
  }
}

.tr-05__play:hover .tr-05__btn {
  scale: 1.1;
  background: var(--tr-05-acc);
  color: oklch(0.15 0.02 22);
}

.tr-05__len {
  position: absolute;
  inset-block-end: 11px;
  inset-inline-end: 11px;
  padding: 3px 8px;
  border-radius: 6px;
  background: oklch(0 0 0/.6);
  color: oklch(0.98 0 0);
  font-size: 11.5px;
  font-weight: 620;
  font-variant-numeric: tabular-nums;
  backdrop-filter: blur(4px);
}

.tr-05__body {
  padding: 18px 20px 20px;
  display: grid;
  align-content: start;
  gap: 10px;
}

.tr-05__body blockquote {
  font-size: 16px;
  line-height: 1.42;
  font-weight: 560;
  letter-spacing: -.02em;
  text-wrap: pretty;
}

.tr-05__who {
  font-size: 12.5px;
  color: var(--tr-05-mut);
}

.tr-05__who b {
  color: var(--tr-05-ink);
  font-weight: 640;
}

.tr-05__dlg {
  width: min(94vw,980px);
  max-width: none;
  padding: 0;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 18px;
  background: oklch(0.12 0.015 275);
  color: var(--tr-05-ink);
  overflow: visible;
  opacity: 0;
  translate: 0 16px;
  scale: .98;
  transition: opacity .32s cubic-bezier(.16,1,.3,1),translate .32s cubic-bezier(.16,1,.3,1),scale .32s cubic-bezier(.16,1,.3,1),overlay .32s allow-discrete,display .32s allow-discrete;
}

.tr-05__dlg[open] {
  opacity: 1;
  translate: 0 0;
  scale: 1;
}

@starting-style {
  .tr-05__dlg[open] {
    opacity: 0;
    translate: 0 16px;
    scale: .98;
  }
}

.tr-05__dlg::backdrop {
  background: oklch(0.08 0.01 275/.72);
  backdrop-filter: blur(0px);
  transition: backdrop-filter .32s,background .32s,overlay .32s allow-discrete,display .32s allow-discrete;
}

.tr-05__dlg[open]::backdrop {
  backdrop-filter: blur(10px);
}

@starting-style {
  .tr-05__dlg[open]::backdrop {
    background: oklch(0.08 0.01 275/0);
    backdrop-filter: blur(0px);
  }
}

.tr-05__player {
  aspect-ratio: 16/9;
  border-radius: 17px;
  overflow: hidden;
  background: #000;
}

.tr-05__frame {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
}

.tr-05__close {
  position: absolute;
  inset-block-start: -16px;
  inset-inline-end: -16px;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 1px solid oklch(1 0 0/.2);
  background: oklch(0.2 0.02 275);
  color: var(--tr-05-ink);
  cursor: pointer;
  transition: background .2s,rotate .3s cubic-bezier(.16,1,.3,1);
}

.tr-05__close svg {
  width: 20px;
  height: 20px;
}

.tr-05__close:hover {
  background: var(--tr-05-acc);
  color: oklch(0.15 0.02 22);
  rotate: 90deg;
}

.tr-05__close:focus-visible {
  outline: 3px solid var(--tr-05-acc);
  outline-offset: 3px;
}

.tr-05__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-05-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (max-width: 560px) {
  .tr-05__close {
    inset-block-start: auto;
    inset-block-end: -58px;
    inset-inline-end: calc(50% - 22px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .tr-05__card {
    animation: none;
  }

  .tr-05__btn::after {
    animation: none;
  }

  .tr-05__play img {
    transition: none;
  }

  .tr-05__dlg,
    .tr-05__dlg::backdrop {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tr-05').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const dlg = root.querySelector('.tr-05__dlg');
    const frame = root.querySelector('.tr-05__frame');
    root.querySelectorAll('.tr-05__play').forEach((btn) => {
      btn.addEventListener('click', () => {
        frame.src = btn.dataset.video + '?autoplay=1&rel=0';
        if (typeof dlg.showModal === 'function') dlg.showModal(); else dlg.setAttribute('open', '');
      });
    });
    root.querySelector('.tr-05__close').addEventListener('click', () => dlg.close());
    dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener('close', () => { frame.src = ''; });
  });
})();
```

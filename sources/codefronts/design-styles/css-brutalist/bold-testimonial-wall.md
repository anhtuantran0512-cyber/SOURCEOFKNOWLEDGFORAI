---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/bold-testimonial-wall/"
title: "Bold Testimonial Wall"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A wall of quote cards in mixed pastel fills, laid out with CSS columns so the heights stagger naturally by quote length — real masonry without a script or a…"
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bold Testimonial Wall
Source: https://codefronts.com/design-styles/css-brutalist/bold-testimonial-wall/

A wall of quote cards in mixed pastel fills, laid out with CSS columns so the heights stagger naturally by quote length — real masonry without a script or a library. Each card is semantic <blockquote> plus <figcaption>, with an oversized quote mark drawn as a ::before that bleeds past the card edge.
## HTML
```html
<div class="brt-08">
  <input class="brt-08__sr" type="checkbox" id="brt-08-dark">
  <label class="brt-08__theme" for="brt-08-dark">
    <svg class="brt-08__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-08__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-08__vh">Dark theme</span>
  </label>

  <div class="brt-08__stage">
    <section class="brt-08__wrap" aria-labelledby="brt-08-h">
      <header class="brt-08__head">
        <p class="brt-08__eyebrow">4.9 average · 1,284 teams</p>
        <h2 class="brt-08__h" id="brt-08-h">People who ship on it</h2>
      </header>

      <div class="brt-08__wall">
        <figure class="brt-08__item">
          <blockquote class="brt-08__quote">We replaced four internal tools with this in a fortnight. The migration was boring, which is the highest compliment I can pay a piece of software.</blockquote>
          <figcaption class="brt-08__by">
            <img class="brt-08__avatar" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=160&amp;h=160&amp;fit=crop&amp;auto=format" width="160" height="160" alt="Priya Sharma, head of platform, smiling in an office" loading="lazy" decoding="async">
            <span class="brt-08__who"><cite class="brt-08__name">Priya Sharma</cite><span class="brt-08__role">Head of Platform, Northwind</span></span>
          </figcaption>
          <p class="brt-08__stars"><span class="brt-08__vh">5 out of 5</span><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 4.5l2.4 4.9 5.4.8-3.9 3.8.9 5.4-4.8-2.6-4.8 2.6.9-5.4L4.2 10.2l5.4-.8z" fill="currentColor"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 4.5l2.4 4.9 5.4.8-3.9 3.8.9 5.4-4.8-2.6-4.8 2.6.9-5.4L4.2 10.2l5.4-.8z" fill="currentColor"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 4.5l2.4 4.9 5.4.8-3.9 3.8.9 5.4-4.8-2.6-4.8 2.6.9-5.4L4.2 10.2l5.4-.8z" fill="currentColor"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 4.5l2.4 4.9 5.4.8-3.9 3.8.9 5.4-4.8-2.6-4.8 2.6.9-5.4L4.2 10.2l5.4-.8z" fill="currentColor"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 4.5l2.4 4.9 5.4.8-3.9 3.8.9 5.4-4.8-2.6-4.8 2.6.9-5.4L4.2 10.2l5.4-.8z" fill="currentColor"/></svg></p>
        </figure>

        <figure class="brt-08__item">
          <blockquote class="brt-08__quote">Our first release cut deploy time from 22 minutes to 40 seconds.</blockquote>
          <figcaption class="brt-08__by">
            <img class="brt-08__avatar" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=160&amp;h=160&amp;fit=crop&amp;auto=format" width="160" height="160" alt="Jordan Lee, staff engineer, in a bright studio" loading="lazy" decoding="async">
            <span class="brt-08__who"><cite class="brt-08__name">Jordan Lee</cite><span class="brt-08__role">Staff Engineer, Peartree Labs</span></span>
          </figcaption>
        </figure>

        <figure class="brt-08__item">
          <blockquote class="brt-08__quote">I run design and support with no engineers on staff. This is the first stack where I have never had to file a ticket to change a page. The audit log alone won over our compliance lead.</blockquote>
          <figcaption class="brt-08__by">
            <img class="brt-08__avatar" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=160&amp;h=160&amp;fit=crop&amp;auto=format" width="160" height="160" alt="Sam Rivera, founder, standing by a window" loading="lazy" decoding="async">
            <span class="brt-08__who"><cite class="brt-08__name">Sam Rivera</cite><span class="brt-08__role">Founder, Ellis &amp; Fern</span></span>
          </figcaption>
        </figure>

        <figure class="brt-08__item">
          <blockquote class="brt-08__quote">The pricing page is honest, the docs are honest, and the invoice matched the estimate to the cent. Rare.</blockquote>
          <figcaption class="brt-08__by">
            <img class="brt-08__avatar" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=160&amp;h=160&amp;fit=crop&amp;auto=format" width="160" height="160" alt="Alex Chen, operations lead, in a dark shirt" loading="lazy" decoding="async">
            <span class="brt-08__who"><cite class="brt-08__name">Alex Chen</cite><span class="brt-08__role">Operations, Kettle Row</span></span>
          </figcaption>
        </figure>

        <figure class="brt-08__item">
          <blockquote class="brt-08__quote">Onboarded 25 people in a morning. Nobody asked me how anything worked, which has never once happened before.</blockquote>
          <figcaption class="brt-08__by">
            <img class="brt-08__avatar" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=160&amp;h=160&amp;fit=crop&amp;auto=format" width="160" height="160" alt="Mara Devlin, engineering manager, outdoors" loading="lazy" decoding="async">
            <span class="brt-08__who"><cite class="brt-08__name">Mara Devlin</cite><span class="brt-08__role">Engineering Manager, Tilt</span></span>
          </figcaption>
        </figure>

        <figure class="brt-08__item">
          <blockquote class="brt-08__quote">Support replied in nine minutes on a Sunday with a patch, not an apology.</blockquote>
          <figcaption class="brt-08__by">
            <img class="brt-08__avatar" src="https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?w=160&amp;h=160&amp;fit=crop&amp;auto=format" width="160" height="160" alt="Tobias Nkemi, CTO, in a grey jumper" loading="lazy" decoding="async">
            <span class="brt-08__who"><cite class="brt-08__name">Tobias Nkemi</cite><span class="brt-08__role">CTO, Harborline</span></span>
          </figcaption>
        </figure>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-08 {
  --page: #faf6ee;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 14px;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Space Grotesk','Sora',ui-sans-serif,system-ui,sans-serif;
}

.brt-08 *,
.brt-08 *::before,
.brt-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-08 {
    --page: oklch(0.974 0.016 86);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
  }
}

.brt-08__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-08__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-08__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-08__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-08__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-08__sr:focus-visible + .brt-08__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-08__sun {
  display: none;
}

.brt-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,4.5vw,3.5rem);
}

.brt-08__wrap {
  inline-size: min(74rem,100%);
}

.brt-08__head {
  margin-block-end: clamp(1.75rem,4vw,2.5rem);
  padding-inline-end: 3rem;
}

.brt-08__eyebrow {
  display: inline-block;
  margin: 0 0 .7rem;
  padding: .35rem .7rem;
  background: var(--mint);
  color: var(--on);
  border: 2px solid var(--edge);
  border-radius: 8px;
  box-shadow: 3px 3px 0 var(--sh);
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.brt-08__h {
  margin: 0;
  font-size: clamp(2rem,5.4vw,3.2rem);
  font-weight: 700;
  letter-spacing: -.03em;
  line-height: 1.02;
  text-wrap: balance;
}

.brt-08__wall {
  columns: 19rem 3;
  column-gap: clamp(1rem,2.2vw,1.6rem);
}

.brt-08__item {
  break-inside: avoid;
  margin: 0 0 clamp(1rem,2.2vw,1.6rem);
  padding: clamp(1.15rem,2.2vw,1.6rem);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 6px 6px 0 var(--sh);
  color: var(--on);
}

.brt-08__item:nth-child(5n+1) {
  background: var(--butter);
}

.brt-08__item:nth-child(5n+2) {
  background: var(--panel);
  color: var(--ink);
}

.brt-08__item:nth-child(5n+3) {
  background: var(--lilac);
}

.brt-08__item:nth-child(5n+4) {
  background: var(--mint);
}

.brt-08__item:nth-child(5n+5) {
  background: var(--sky);
}

.brt-08__quote {
  position: relative;
  margin: 0 0 1.1rem;
  padding-block-start: 1.4rem;
  font-size: clamp(1.02rem,1.6vw,1.15rem);
  font-weight: 600;
  line-height: 1.45;
  letter-spacing: -.01em;
  text-wrap: pretty;
}

.brt-08__quote::before {
  content: '\201C';
  position: absolute;
  inset-block-start: -.28em;
  inset-inline-start: -.06em;
  font-size: 5.5rem;
  font-weight: 700;
  line-height: 1;
  opacity: .32;
}

.brt-08__by {
  display: flex;
  align-items: center;
  gap: .7rem;
  padding-block-start: .9rem;
  border-block-start: 2px solid var(--edge);
}

.brt-08__avatar {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  flex: none;
  object-fit: cover;
  aspect-ratio: 1;
  background: var(--page);
  border: var(--bw) solid var(--edge);
  border-radius: 50%;
}

.brt-08__who {
  display: grid;
  gap: .1rem;
}

.brt-08__name {
  font-style: normal;
  font-size: .88rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.brt-08__role {
  font-size: .82rem;
  opacity: .72;
}

.brt-08__stars {
  display: flex;
  gap: .15rem;
  margin: .9rem 0 0;
}

.brt-08__stars svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.brt-08:has(#brt-08-dark:checked) {
  --page: #14131a;
  --panel: #221f2b;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-08:has(#brt-08-dark:checked) .brt-08__moon {
  display: none;
}

.brt-08:has(#brt-08-dark:checked) .brt-08__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-08:not(:has(#brt-08-dark:checked)) {
    --page: #14131a;
    --panel: #221f2b;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-08:not(:has(#brt-08-dark:checked)) .brt-08__moon {
    display: none;
  }

  .brt-08:not(:has(#brt-08-dark:checked)) .brt-08__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-08 *,
    .brt-08 *::before,
    .brt-08 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-08__item,
    .brt-08__avatar,
    .brt-08__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-08__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```

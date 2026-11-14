---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/blossom-bento/"
title: "Bento Box Testimonial Grid Layout"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "The bento grid is the dominant landing-page layout of the decade because it lets one section carry several kinds of proof at once — a marquee quote, a hard…"
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Box Testimonial Grid Layout
Source: https://codefronts.com/components/css-testimonials-reviews/blossom-bento/

The bento grid is the dominant landing-page layout of the decade because it lets one section carry several kinds of proof at once — a marquee quote, a hard metric, a logo wall, a rating and a photo, each sized to its own importance. This build uses explicit grid-template-areas so the composition is readable in the CSS and re-flows to a single column with one rewritten area map.
## HTML
```html
<section class="tr-13" aria-label="Bento box testimonial grid layout demo">
  <div class="tr-13__stage">
    <header class="tr-13__head">
      <p class="tr-13__eyebrow">Social proof, all of it</p>
      <h2 class="tr-13__title">One section. Five kinds of evidence.</h2>
    </header>

    <div class="tr-13__bento">
      <figure class="tr-13__tile tr-13__hero">
        <span class="tr-13__mark" aria-hidden="true">“</span>
        <blockquote>We benchmarked four vendors for six weeks. This one won on the boring things — audit logs, permissions, an API that behaved exactly like its docs said it would.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Alessandra Rossi" width="48" height="48" loading="lazy" decoding="async">
          <span><b>Alessandra Rossi</b>CTO · Vaultline Financial</span>
        </figcaption>
      </figure>

      <div class="tr-13__tile tr-13__stat">
        <b class="tr-13__big"><span class="tr-13__n" aria-hidden="true"></span><span>%</span></b>
        <span class="tr-13__sr">98 percent</span>
        <p>renew after year one</p>
      </div>

      <div class="tr-13__tile tr-13__rate">
        <span class="tr-13__stars" style="--tr-13-pct:96%" role="img" aria-label="Rated 4.8 out of 5 across 3,912 reviews"></span>
        <b>4.8</b>
        <p>3,912 reviews across four platforms</p>
      </div>

      <figure class="tr-13__tile tr-13__photo">
        <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=700&auto=format&fit=crop" alt="A product team reviewing work together at a table" width="520" height="600" loading="lazy" decoding="async">
        <figcaption><b>Fernbrook</b> onboarded 41 people in a day</figcaption>
      </figure>

      <div class="tr-13__tile tr-13__logos" aria-hidden="true">
        <p>Trusted by</p>
        <div>
          <span>NORTHWIND</span><span>MERIDIAN</span><span>AURYN</span><span>PORTSIDE</span><span>BLOMST</span><span>HALDEN</span>
        </div>
      </div>

      <figure class="tr-13__tile tr-13__quote">
        <blockquote>“Support answered a Sev-2 in nine minutes. At 4am.”</blockquote>
        <figcaption><b>Callum Doyle</b> · Head of Platform, Meridian</figcaption>
      </figure>

      <div class="tr-13__tile tr-13__cta">
        <p>Read 40+ full customer stories</p>
        <a class="tr-13__btn" href="#tr-13-stories">Browse case studies <span aria-hidden="true">→</span></a>
      </div>
    </div>
    <p class="tr-13__chip" aria-hidden="true">grid-template-areas · area remap at breakpoint · minmax auto rows · @property counter tile</p>
  </div>
</section>
```
## CSS
```css
@property --tr-13-n {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.tr-13,
.tr-13 *,
.tr-13 *::before,
.tr-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-13-bg: oklch(0.16 0.016 265);
  --tr-13-tile: oklch(0.21 0.02 265);
  --tr-13-ink: oklch(0.97 0.006 265);
  --tr-13-mut: oklch(0.71 0.018 265);
  --tr-13-acc: oklch(0.8 0.15 165);
  --tr-13-star: oklch(0.83 0.15 88);
  background: var(--tr-13-bg);
  color: var(--tr-13-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(18px,3vw,28px);
  padding: clamp(18px,4vw,48px);
}

.tr-13__head {
  text-align: center;
  display: grid;
  gap: 9px;
}

.tr-13__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tr-13-acc);
}

.tr-13__title {
  font-size: clamp(23px,3.6vw,38px);
  font-weight: 670;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.tr-13__bento {
  display: grid;
  width: min(100%,1120px);
  grid-template-columns: repeat(4,1fr);
  grid-auto-rows: minmax(132px,auto);
  gap: clamp(10px,1.3vw,15px);
  grid-template-areas: 'hero hero stat logos' 'hero hero photo logos' 'quote rate photo cta';
}

.tr-13__tile {
  position: relative;
  padding: clamp(16px,2vw,22px);
  border-radius: 18px;
  background: var(--tr-13-tile);
  border: 1px solid oklch(1 0 0/.08);
  overflow: hidden;
  animation: tr-13-in .7s cubic-bezier(.16,1,.3,1) both;
  transition: translate .3s cubic-bezier(.16,1,.3,1),border-color .3s;
}

.tr-13__tile:hover {
  translate: 0 -2px;
  border-color: color-mix(in oklch,var(--tr-13-acc) 38%,transparent);
}

@keyframes tr-13-in {
  from {
    opacity: 0;
    translate: 0 14px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-13__hero {
  grid-area: hero;
  display: grid;
  align-content: space-between;
  gap: 20px;
  padding: clamp(22px,2.8vw,32px);
  background: linear-gradient(160deg,color-mix(in oklch,var(--tr-13-acc) 14%,var(--tr-13-tile)),var(--tr-13-tile) 65%);
  animation-delay: 0s;
}

.tr-13__mark {
  position: absolute;
  inset-block-start: 2px;
  inset-inline-end: 18px;
  font-family: Georgia,serif;
  font-size: 120px;
  line-height: 1;
  color: color-mix(in oklch,var(--tr-13-acc) 18%,transparent);
}

.tr-13__hero blockquote {
  position: relative;
  font-size: clamp(17px,2.1vw,23px);
  line-height: 1.45;
  letter-spacing: -.024em;
  text-wrap: pretty;
}

.tr-13__hero figcaption,
.tr-13__photo figcaption {
  display: flex;
  align-items: center;
  gap: 11px;
}

.tr-13__hero figcaption img {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
}

.tr-13__hero figcaption span {
  display: grid;
  font-size: 12px;
  line-height: 1.35;
  color: var(--tr-13-mut);
}

.tr-13__hero figcaption b {
  font-size: 14.5px;
  font-weight: 640;
  color: var(--tr-13-ink);
  letter-spacing: -.014em;
}

.tr-13__stat {
  grid-area: stat;
  display: grid;
  align-content: center;
  gap: 2px;
  animation-delay: .06s;
}

.tr-13__big {
  display: flex;
  align-items: baseline;
  font-size: clamp(34px,4.4vw,50px);
  font-weight: 720;
  letter-spacing: -.05em;
  line-height: 1;
  color: var(--tr-13-acc);
  font-variant-numeric: tabular-nums;
}

.tr-13__big span:last-child {
  font-size: .5em;
  margin-inline-start: 2px;
}

.tr-13__n {
  counter-reset: tr-13-c var(--tr-13-n);
  animation: tr-13-run 2.2s cubic-bezier(.16,1,.3,1) .3s both;
}

.tr-13__n::after {
  content: counter(tr-13-c);
}

@keyframes tr-13-run {
  from {
    --tr-13-n: 0;
  }

  to {
    --tr-13-n: 98;
  }
}

.tr-13__stat p {
  font-size: 12.5px;
  color: var(--tr-13-mut);
  line-height: 1.4;
  text-wrap: balance;
}

.tr-13__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.tr-13__rate {
  grid-area: rate;
  display: grid;
  align-content: center;
  gap: 5px;
  animation-delay: .12s;
}

.tr-13__stars {
  position: relative;
  display: inline-block;
  font-size: 19px;
  line-height: 1;
  letter-spacing: 1.5px;
  width: fit-content;
}

.tr-13__stars::before {
  content: '★★★★★';
  color: oklch(1 0 0/.16);
}

.tr-13__stars::after {
  content: '★★★★★';
  color: var(--tr-13-star);
  position: absolute;
  inset: 0;
  clip-path: inset(0 calc(100% - var(--tr-13-pct,100%)) 0 0);
}

.tr-13__rate b {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
}

.tr-13__rate p {
  font-size: 12px;
  color: var(--tr-13-mut);
  line-height: 1.4;
}

.tr-13__photo {
  grid-area: photo;
  padding: 0;
  animation-delay: .18s;
}

.tr-13__photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  min-height: 180px;
  background: linear-gradient(140deg,oklch(0.4 0.05 265),oklch(0.3 0.04 300));
  transition: scale .6s cubic-bezier(.16,1,.3,1);
}

.tr-13__photo:hover img {
  scale: 1.05;
}

.tr-13__photo figcaption {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  padding: 16px;
  font-size: 12px;
  color: oklch(0.97 0 0);
  background: linear-gradient(transparent,oklch(0.12 0.01 265/.92));
}

.tr-13__photo figcaption b {
  font-weight: 660;
}

.tr-13__logos {
  grid-area: logos;
  display: grid;
  align-content: center;
  gap: 12px;
  animation-delay: .24s;
}

.tr-13__logos p {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--tr-13-mut);
}

.tr-13__logos div {
  display: grid;
  gap: 10px;
}

.tr-13__logos span {
  font-size: 13px;
  font-weight: 720;
  letter-spacing: .06em;
  color: oklch(1 0 0/.42);
  transition: color .25s;
}

.tr-13__logos:hover span {
  color: oklch(1 0 0/.7);
}

.tr-13__quote {
  grid-area: quote;
  display: grid;
  align-content: center;
  gap: 10px;
  animation-delay: .3s;
}

.tr-13__quote blockquote {
  font-size: 15px;
  line-height: 1.42;
  letter-spacing: -.016em;
  text-wrap: pretty;
}

.tr-13__quote figcaption {
  font-size: 11.5px;
  color: var(--tr-13-mut);
}

.tr-13__quote figcaption b {
  color: var(--tr-13-ink);
  font-weight: 620;
}

.tr-13__cta {
  grid-area: cta;
  display: grid;
  align-content: center;
  gap: 12px;
  background: linear-gradient(150deg,color-mix(in oklch,var(--tr-13-acc) 20%,var(--tr-13-tile)),var(--tr-13-tile));
  animation-delay: .36s;
}

.tr-13__cta p {
  font-size: 13.5px;
  line-height: 1.4;
  font-weight: 560;
  text-wrap: balance;
}

.tr-13__btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 16px;
  width: fit-content;
  border-radius: 10px;
  background: var(--tr-13-acc);
  color: oklch(0.18 0.03 165);
  font-size: 13px;
  font-weight: 660;
  text-decoration: none;
  transition: gap .25s cubic-bezier(.16,1,.3,1),background .25s;
}

.tr-13__btn:hover {
  gap: 12px;
  background: color-mix(in oklch,var(--tr-13-acc) 82%,white);
}

.tr-13__btn:focus-visible {
  outline: 3px solid var(--tr-13-acc);
  outline-offset: 3px;
}

.tr-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-13-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (max-width: 860px) {
  .tr-13__bento {
    grid-template-columns: repeat(2,1fr);
    grid-template-areas: 'hero hero' 'stat rate' 'photo photo' 'quote logos' 'cta cta';
  }
}

@media (max-width: 520px) {
  .tr-13__bento {
    grid-template-columns: 1fr;
    grid-template-areas: 'hero' 'stat' 'rate' 'photo' 'quote' 'logos' 'cta';
  }
}

@media (prefers-reduced-motion: reduce) {
  .tr-13__tile {
    animation: none;
  }

  .tr-13__n {
    animation-duration: 1ms;
  }

  .tr-13__photo:hover img {
    scale: 1;
  }
}
```

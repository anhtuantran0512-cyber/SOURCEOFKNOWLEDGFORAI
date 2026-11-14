---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/high-fashion/"
title: "High Fashion Editorial Quote Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Magazine layout logic applied to a customer quote: a full-bleed portrait, an oversized serif pull-quote that overlaps the image, hairline rules that run edge…"
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: High Fashion Editorial Quote Card
Source: https://codefronts.com/components/css-testimonials-reviews/high-fashion/

Magazine layout logic applied to a customer quote: a full-bleed portrait, an oversized serif pull-quote that overlaps the image, hairline rules that run edge to edge, and letter-spaced small caps for every piece of metadata. Nothing is centred, nothing is boxed, and the type sizes are two steps further apart than a web designer would instinctively choose.
## HTML
```html
<section class="tr-21" aria-label="High fashion editorial quote card demo">
  <div class="tr-21__stage">
    <div class="tr-21__spread">
      <p class="tr-21__issue">Studio Journal — Nº 14 · Autumn / Winter 26</p>

      <figure class="tr-21__portrait">
        <img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=900&auto=format&fit=crop" alt="Model in an oversized wool coat photographed against a plain wall" width="720" height="900" loading="lazy" decoding="async">
        <figcaption>Photographed in Antwerp, March 2026</figcaption>
      </figure>

      <blockquote class="tr-21__pull">
        <p>I have worn the same coat for four winters. It is the only thing in my wardrobe that has never once been the wrong decision.</p>
      </blockquote>

      <div class="tr-21__attr">
        <p class="tr-21__name">Margaux Vandenberghe</p>
        <p class="tr-21__role">Creative Director, Maison Ferrand · Client since 2022</p>
      </div>

      <p class="tr-21__rule" aria-hidden="true"></p>

      <ul class="tr-21__facts">
        <li><span>Piece</span>The Long Wool Coat, Nº 004</li>
        <li><span>Worn</span>Four seasons, unaltered</li>
        <li><span>Origin</span>Milled in Biella, made in Porto</li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
.tr-21,
.tr-21 *,
.tr-21 *::before,
.tr-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-21-bg: oklch(0.955 0.006 75);
  --tr-21-ink: oklch(0.17 0.008 60);
  --tr-21-mut: oklch(0.5 0.008 60);
  --tr-21-panel: oklch(0.99 0.004 75);
  --tr-21-line: color-mix(in oklch,var(--tr-21-ink) 22%,transparent);
  background: var(--tr-21-bg);
  color: var(--tr-21-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(20px,5vw,72px);
}

.tr-21__spread {
  width: min(100%,1120px);
  display: grid;
  grid-template-columns: repeat(12,1fr);
  column-gap: clamp(12px,2vw,26px);
  row-gap: clamp(18px,2.6vw,30px);
  animation: tr-21-in 1s cubic-bezier(.16,1,.3,1) both;
}

@keyframes tr-21-in {
  from {
    opacity: 0;
    translate: 0 16px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-21__issue {
  grid-column: 1/-1;
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .34em;
  text-transform: uppercase;
  color: var(--tr-21-mut);
  padding-bottom: clamp(14px,2.4vw,24px);
  border-block-end: 1px solid var(--tr-21-line);
}

.tr-21__portrait {
  grid-column: 1/8;
  grid-row: 2;
  position: relative;
}

.tr-21__portrait img {
  width: 100%;
  height: auto;
  aspect-ratio: 4/5;
  object-fit: cover;
  display: block;
  background: linear-gradient(150deg,oklch(0.86 0.01 70),oklch(0.72 0.02 60));
  filter: grayscale(1) contrast(1.04);
  transition: filter 1.2s cubic-bezier(.16,1,.3,1);
}

.tr-21__portrait:hover img {
  filter: grayscale(0) contrast(1);
}

.tr-21__portrait figcaption {
  margin-top: 10px;
  font-size: 10px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--tr-21-mut);
}

.tr-21__pull {
  grid-column: 6/13;
  grid-row: 2;
  align-self: end;
  position: relative;
  z-index: 1;
  background: var(--tr-21-panel);
  padding: clamp(24px,3.4vw,46px) clamp(20px,3vw,40px) clamp(20px,3vw,36px);
  margin-block-end: clamp(24px,5vw,74px);
}

.tr-21__pull::before {
  content: '“';
  position: absolute;
  inset-block-start: -.36em;
  inset-inline-start: .1em;
  font-family: Georgia,'Times New Roman',serif;
  font-size: clamp(140px,20vw,300px);
  line-height: 1;
  color: color-mix(in oklch,var(--tr-21-ink) 9%,transparent);
  pointer-events: none;
}

.tr-21__pull p {
  position: relative;
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
  font-size: clamp(24px,4.4vw,54px);
  font-weight: 400;
  line-height: 1.04;
  letter-spacing: -.032em;
  text-wrap: balance;
}

.tr-21__attr {
  grid-column: 6/13;
  grid-row: 3;
  display: grid;
  gap: 6px;
}

.tr-21__name {
  font-family: Georgia,'Times New Roman',serif;
  font-size: clamp(17px,2vw,21px);
  letter-spacing: -.01em;
}

.tr-21__role {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--tr-21-mut);
  text-wrap: balance;
}

.tr-21__rule {
  grid-column: 1/-1;
  grid-row: 4;
  block-size: 1px;
  background: var(--tr-21-line);
}

.tr-21__facts {
  grid-column: 1/-1;
  grid-row: 5;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,220px),1fr));
  gap: clamp(14px,2.4vw,30px);
}

.tr-21__facts li {
  display: grid;
  gap: 7px;
  font-family: Georgia,'Times New Roman',serif;
  font-size: 15px;
  line-height: 1.45;
  letter-spacing: -.008em;
}

.tr-21__facts span {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 9.5px;
  font-weight: 640;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: var(--tr-21-mut);
}

@media (max-width: 820px) {
  .tr-21__portrait {
    grid-column: 1/-1;
  }

  .tr-21__pull {
    grid-column: 1/-1;
    grid-row: 3;
    margin-block: -60px 0;
    margin-inline: clamp(12px,4vw,40px) 0;
  }

  .tr-21__attr {
    grid-column: 1/-1;
    grid-row: 4;
  }

  .tr-21__rule {
    grid-row: 5;
  }

  .tr-21__facts {
    grid-row: 6;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tr-21__spread {
    animation: none;
  }

  .tr-21__portrait img {
    transition: none;
  }
}
```

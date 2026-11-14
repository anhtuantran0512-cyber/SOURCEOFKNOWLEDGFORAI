---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/luxury-real-estate/"
title: "Real Estate Client Testimonial Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Real-estate proof has to carry the transaction, not just the sentiment: the property, the suburb, days on market and the outcome against asking price."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Real Estate Client Testimonial Card
Source: https://codefronts.com/components/css-testimonials-reviews/luxury-real-estate/

Real-estate proof has to carry the transaction, not just the sentiment: the property, the suburb, days on market and the outcome against asking price. This split card puts the sold listing beside the client's words with a restrained neutral-and-brass palette, the visual language North American and Australian premium agencies actually use.
## HTML
```html
<section class="tr-19" aria-label="Premium real estate client review card demo">
  <div class="tr-19__stage">
    <article class="tr-19__card">
      <div class="tr-19__media">
        <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=900&auto=format&fit=crop" alt="Exterior of a renovated two-storey weatherboard home with a paved driveway" width="620" height="720" loading="lazy" decoding="async">
        <span class="tr-19__ribbon">Sold</span>
        <div class="tr-19__addr">
          <b>14 Wentworth Terrace</b>
          <span>Hawthorn East, VIC 3123 · 4 bed · 2 bath · 620 m²</span>
        </div>
      </div>

      <div class="tr-19__body">
        <p class="tr-19__kicker">Client testimonial</p>
        <blockquote>We had already been to market once with another agency and withdrawn. Marguerite re-photographed the house, moved the campaign to a Wednesday and told us plainly which of our expectations were wrong. It sold in nineteen days, eight per cent above the revised guide, to the second couple through the door.</blockquote>

        <figcaption class="tr-19__who">
          <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Erin and James McAllister" width="52" height="52" loading="lazy" decoding="async">
          <span><b>Erin &amp; James McAllister</b>Vendors · Sold July 2026</span>
          <span class="tr-19__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</span>
        </figcaption>

        <dl class="tr-19__out">
          <div><dt>Days on market</dt><dd>19</dd></div>
          <div><dt>Result vs. guide</dt><dd class="tr-19__up">+8.0%</dd></div>
          <div><dt>Method</dt><dd>Private treaty</dd></div>
          <div><dt>Inspections</dt><dd>64 groups</dd></div>
        </dl>

        <p class="tr-19__note">Figures supplied by the selling agency and reflect the July 2026 campaign. Past results are not an indication of future outcomes.</p>
      </div>
    </article>
    <p class="tr-19__chip" aria-hidden="true">container query split · logical inset properties (RTL-safe) · aspect-ratio media · dl outcome pairs</p>
  </div>
</section>
```
## CSS
```css
.tr-19,
.tr-19 *,
.tr-19 *::before,
.tr-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-19-bg: oklch(0.94 0.008 85);
  --tr-19-card: oklch(0.995 0.004 85);
  --tr-19-ink: oklch(0.22 0.012 70);
  --tr-19-mut: oklch(0.52 0.012 70);
  --tr-19-acc: oklch(0.68 0.1 78);
  --tr-19-up: oklch(0.55 0.14 155);
  background: var(--tr-19-bg);
  color: var(--tr-19-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,54px);
}

.tr-19__card {
  container-type: inline-size;
  width: min(100%,940px);
  display: grid;
  background: var(--tr-19-card);
  border: 1px solid oklch(0 0 0/.07);
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 34px 70px -44px oklch(0.28 0.03 70/.75);
  animation: tr-19-in .8s cubic-bezier(.16,1,.3,1) both;
}

@keyframes tr-19-in {
  from {
    opacity: 0;
    translate: 0 20px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

@container (min-width: 640px) {
  .tr-19__card {
    grid-template-columns: 44% 1fr;
  }
}

.tr-19__media {
  position: relative;
  min-block-size: 260px;
  overflow: hidden;
  background: linear-gradient(150deg,oklch(0.82 0.03 80),oklch(0.7 0.04 60));
}

.tr-19__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 55%;
  display: block;
  transition: scale .8s cubic-bezier(.16,1,.3,1);
}

.tr-19__card:hover .tr-19__media img {
  scale: 1.05;
}

.tr-19__ribbon {
  position: absolute;
  inset-block-start: 16px;
  inset-inline-start: 16px;
  padding: 6px 14px;
  background: var(--tr-19-ink);
  color: oklch(0.97 0.02 85);
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.tr-19__addr {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  display: grid;
  gap: 3px;
  padding: 18px;
  background: linear-gradient(transparent,oklch(0.16 0.01 70/.88));
  color: oklch(0.98 0.004 85);
}

.tr-19__addr b {
  font-family: Georgia,'Times New Roman',serif;
  font-size: 18px;
  font-weight: 600;
  letter-spacing: -.015em;
}

.tr-19__addr span {
  font-size: 11.5px;
  letter-spacing: .03em;
  color: oklch(0.9 0.006 85);
}

.tr-19__body {
  padding: clamp(24px,3.4cqi,38px);
  display: grid;
  align-content: center;
  gap: 18px;
}

.tr-19__kicker {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--tr-19-acc) 82%,black);
}

.tr-19__body blockquote {
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
  font-size: clamp(16px,2.1cqi,19px);
  line-height: 1.62;
  letter-spacing: -.006em;
  color: color-mix(in oklch,var(--tr-19-ink) 94%,transparent);
  text-wrap: pretty;
}

.tr-19__body blockquote::before {
  content: '“';
}

.tr-19__body blockquote::after {
  content: '”';
}

.tr-19__who {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  padding-block: 16px;
  border-block: 1px solid oklch(0 0 0/.09);
}

.tr-19__who img {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
}

.tr-19__who span:not(.tr-19__stars) {
  display: grid;
  gap: 2px;
  font-size: 12px;
  color: var(--tr-19-mut);
}

.tr-19__who b {
  font-size: 14.5px;
  font-weight: 640;
  color: var(--tr-19-ink);
  letter-spacing: -.014em;
}

.tr-19__stars {
  margin-inline-start: auto;
  font-size: 14px;
  letter-spacing: 2px;
  color: var(--tr-19-acc);
}

.tr-19__out {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 14px 22px;
}

.tr-19__out>div {
  display: grid;
  gap: 3px;
}

.tr-19__out dt {
  font-size: 10.5px;
  font-weight: 640;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--tr-19-mut);
}

.tr-19__out dd {
  font-size: 20px;
  font-weight: 650;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.tr-19__up {
  color: var(--tr-19-up);
}

.tr-19__note {
  font-size: 11px;
  line-height: 1.5;
  color: color-mix(in oklch,var(--tr-19-mut) 85%,transparent);
  max-width: 52ch;
}

.tr-19__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-19-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.5);
}

@media (prefers-reduced-motion: reduce) {
  .tr-19__card {
    animation: none;
  }

  .tr-19__card:hover .tr-19__media img {
    scale: 1;
  }
}
```

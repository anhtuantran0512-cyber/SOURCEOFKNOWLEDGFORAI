---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/neon-glass-saas/"
title: "Glassmorphism SaaS Testimonial Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Frosted glass done properly — which mostly means doing less of it."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism SaaS Testimonial Card
Source: https://codefronts.com/components/css-testimonials-reviews/neon-glass-saas/

Frosted glass done properly — which mostly means doing less of it. Real glass needs three things working together: a backdrop that is actually worth blurring, a backdrop-filter that saturates as well as blurs, and an edge that catches light on one side only. The floating aurora behind the cards is pure CSS, animated on the compositor, and the cards refract it as they sit.
## HTML
```html
<section class="tr-14" aria-label="Glassmorphism SaaS testimonial card demo">
  <div class="tr-14__stage">
    <div class="tr-14__aurora" aria-hidden="true"><i></i><i></i><i></i></div>

    <header class="tr-14__head">
      <p class="tr-14__eyebrow">Customer voices</p>
      <h2 class="tr-14__title">Frosted, not foggy</h2>
    </header>

    <div class="tr-14__row">
      <figure class="tr-14__card">
        <div class="tr-14__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
        <blockquote>The onboarding flow they built for us converted 34% better than the one we spent two quarters on. I stopped defending the old one after week two.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Jessa Moreau" width="46" height="46" loading="lazy" decoding="async">
          <span><b>Jessa Moreau</b>Growth Lead · Tidewell</span>
        </figcaption>
      </figure>

      <figure class="tr-14__card tr-14__card--lift">
        <div class="tr-14__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
        <blockquote>Every integration we asked about already existed. The one that did not shipped six weeks later, and they emailed to tell us.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Marcus Yeung" width="46" height="46" loading="lazy" decoding="async">
          <span><b>Marcus Yeung</b>Director of Risk · Halden</span>
        </figcaption>
      </figure>

      <figure class="tr-14__card">
        <div class="tr-14__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
        <blockquote>Our security review is famously unpleasant. They cleared it in nine days without a single exception request.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Erin McAllister" width="46" height="46" loading="lazy" decoding="async">
          <span><b>Erin McAllister</b>COO · Larkfield Health</span>
        </figcaption>
      </figure>
    </div>
    <p class="tr-14__chip" aria-hidden="true">backdrop-filter: blur() saturate() · masked gradient edge · compositor-only aurora drift</p>
  </div>
</section>
```
## CSS
```css
.tr-14,
.tr-14 *,
.tr-14 *::before,
.tr-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-14-bg: oklch(0.19 0.04 290);
  --tr-14-ink: oklch(0.98 0.005 290);
  --tr-14-mut: oklch(0.8 0.02 290);
  --tr-14-acc: oklch(0.82 0.15 200);
  --tr-14-star: oklch(0.87 0.13 92);
  background: var(--tr-14-bg);
  color: var(--tr-14-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-14__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,34px);
  padding: clamp(20px,4vw,56px);
  overflow: hidden;
  isolation: isolate;
}

.tr-14__aurora {
  position: absolute;
  inset: -10%;
  z-index: -1;
}

.tr-14__aurora i {
  position: absolute;
  border-radius: 50%;
  filter: blur(70px);
  opacity: .85;
  animation: tr-14-drift 24s ease-in-out infinite alternate;
}

.tr-14__aurora i:nth-child(1) {
  inline-size: 46vmax;
  block-size: 46vmax;
  inset-block-start: -8%;
  inset-inline-start: -6%;
  background: radial-gradient(circle,oklch(0.62 0.22 300),transparent 68%);
}

.tr-14__aurora i:nth-child(2) {
  inline-size: 40vmax;
  block-size: 40vmax;
  inset-block-start: 12%;
  inset-inline-end: -8%;
  background: radial-gradient(circle,oklch(0.7 0.2 200),transparent 68%);
  animation-delay: -8s;
}

.tr-14__aurora i:nth-child(3) {
  inline-size: 44vmax;
  block-size: 44vmax;
  inset-block-end: -14%;
  inset-inline-start: 26%;
  background: radial-gradient(circle,oklch(0.66 0.21 340),transparent 68%);
  animation-delay: -15s;
}

@keyframes tr-14-drift {
  to {
    translate: 6% -5%;
    scale: 1.14;
  }
}

.tr-14__head {
  text-align: center;
  display: grid;
  gap: 9px;
}

.tr-14__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--tr-14-acc);
}

.tr-14__title {
  font-size: clamp(26px,4.4vw,46px);
  font-weight: 660;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.tr-14__row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,272px),1fr));
  gap: clamp(14px,2vw,20px);
  width: min(100%,1060px);
  align-items: start;
}

.tr-14__card {
  position: relative;
  display: grid;
  gap: 16px;
  padding: clamp(22px,2.6vw,28px);
  border-radius: 20px;
  background: oklch(1 0 0/.07);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
  backdrop-filter: blur(22px) saturate(180%);
  border: 1px solid oklch(1 0 0/.15);
  box-shadow: 0 30px 60px -34px oklch(0.1 0.05 290/.85),inset 0 1px 0 oklch(1 0 0/.14);
  animation: tr-14-in .8s cubic-bezier(.16,1,.3,1) both;
  transition: translate .4s cubic-bezier(.16,1,.3,1),background .4s;
}

.tr-14__card:nth-child(2) {
  animation-delay: .1s;
}

.tr-14__card:nth-child(3) {
  animation-delay: .2s;
}

@keyframes tr-14-in {
  from {
    opacity: 0;
    translate: 0 20px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-14__card--lift {
  translate: 0 -18px;
}

.tr-14__card:hover {
  translate: 0 -8px;
  background: oklch(1 0 0/.11);
}

.tr-14__card--lift:hover {
  translate: 0 -26px;
}

.tr-14__card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(140deg,oklch(1 0 0/.55),transparent 42%,transparent 62%,oklch(1 0 0/.14));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.tr-14__stars {
  font-size: 15px;
  letter-spacing: 2.5px;
  color: var(--tr-14-star);
  text-shadow: 0 1px 6px oklch(0.7 0.15 92/.5);
}

.tr-14__card blockquote {
  font-size: 15.5px;
  line-height: 1.56;
  letter-spacing: -.016em;
  text-wrap: pretty;
  text-shadow: 0 1px 2px oklch(0 0 0/.3);
}

.tr-14__card figcaption {
  display: flex;
  align-items: center;
  gap: 11px;
  padding-top: 16px;
  border-top: 1px solid oklch(1 0 0/.13);
}

.tr-14__card figcaption img {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  box-shadow: 0 0 0 1px oklch(1 0 0/.28);
}

.tr-14__card figcaption span {
  display: grid;
  font-size: 12px;
  line-height: 1.35;
  color: var(--tr-14-mut);
}

.tr-14__card figcaption b {
  font-size: 14.5px;
  font-weight: 640;
  color: var(--tr-14-ink);
  letter-spacing: -.014em;
}

.tr-14__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-14-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.18);
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.06);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .tr-14__card {
    background: oklch(0.28 0.05 290/.88);
  }
}

@media (max-width: 760px) {
  .tr-14__card--lift {
    translate: 0 0;
  }

  .tr-14__card--lift:hover {
    translate: 0 -8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tr-14__aurora i,
    .tr-14__card {
    animation: none;
  }

  .tr-14__card,
    .tr-14__card--lift {
    transition: none;
  }
}
```

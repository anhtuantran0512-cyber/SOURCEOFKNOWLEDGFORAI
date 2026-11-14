---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/testimonial-reviews-card-slider/"
title: "Testimonial & Reviews Card Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Testimonial and reviews card slider — social-proof carousel of review cards (avatar, star rating, quote, company) that snap smoothly through a contained rail…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Testimonial & Reviews Card Slider
Source: https://codefronts.com/components/css-image-slider/testimonial-reviews-card-slider/

Testimonial and reviews card slider — social-proof carousel of review cards (avatar, star rating, quote, company) that snap smoothly through a contained rail via native scroll-snap. The G2 / Trustpilot / Capterra pattern for SaaS landing pages, fintech advisor pages, and B2B customer-story sections. Light on the DOM, zero JavaScript, schema.org Review markup ready for Google rich-results carousels.
## HTML
```html
<div class="cis-16">
  <div class="cis-16__rail" tabindex="0" aria-label="Customer reviews">
    <figure class="cis-16__card">
      <div class="cis-16__stars" style="--r:100%" aria-label="5 out of 5"></div>
      <blockquote>Cut our onboarding time in half. The team actually enjoys using it now.</blockquote>
      <figcaption><img src="https://picsum.photos/seed/cis16a/120/120" alt=""><span><b>Dana Okafor</b>Head of Ops, Northwind</span></figcaption>
    </figure>
    <figure class="cis-16__card">
      <div class="cis-16__stars" style="--r:90%" aria-label="4.5 out of 5"></div>
      <blockquote>The reporting alone paid for the subscription in the first month.</blockquote>
      <figcaption><img src="https://picsum.photos/seed/cis16b/120/120" alt=""><span><b>Luca Verdi</b>Finance Lead, Ampersand</span></figcaption>
    </figure>
    <figure class="cis-16__card">
      <div class="cis-16__stars" style="--r:100%" aria-label="5 out of 5"></div>
      <blockquote>Support answered in four minutes at 2am. Genuinely unheard of.</blockquote>
      <figcaption><img src="https://picsum.photos/seed/cis16c/120/120" alt=""><span><b>Priya Nair</b>CTO, Loomlabs</span></figcaption>
    </figure>
    <figure class="cis-16__card">
      <div class="cis-16__stars" style="--r:80%" aria-label="4 out of 5"></div>
      <blockquote>Migrated 12k records without a single dropped field. Rock solid.</blockquote>
      <figcaption><img src="https://picsum.photos/seed/cis16d/120/120" alt=""><span><b>Sam Reyes</b>Founder, Tidepool</span></figcaption>
    </figure>
  </div>
</div>
```
## CSS
```css
.cis-16,
.cis-16 *,
.cis-16 *::before,
.cis-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-16 ::selection {
  background: oklch(0.85 0.14 90);
  color: #181200;
}

.cis-16 {
  --accent: oklch(0.78 0.12 250);
  --star: oklch(0.85 0.15 85);
  --fade: 8%;
  --surface: #14151d;
  --line: #262838;
  --text: #eef0f7;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--text);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 44px 0;
  background: radial-gradient(120% 110% at 50% 0%,#15161f,#0a0b11);
}

.cis-16__rail {
  display: flex;
  gap: 18px;
  width: min(880px,96vw);
  margin: 0 auto;
  padding: 14px 12% 14px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-width: none;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 var(--fade),#000 calc(100% - var(--fade)),transparent);
  mask-image: linear-gradient(90deg,transparent,#000 var(--fade),#000 calc(100% - var(--fade)),transparent);
}

.cis-16__rail::-webkit-scrollbar {
  display: none;
}

.cis-16__rail:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 5px;
  border-radius: 20px;
}

.cis-16__card {
  flex: 0 0 62%;
  scroll-snap-align: center;
  display: flex;
  flex-direction: column;
  gap: 16px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 24px;
}

.cis-16__stars {
  width: 104px;
  height: 18px;
  background: linear-gradient(90deg,var(--star) 0 var(--r),#3a3d4e var(--r) 100%);
  -webkit-mask: repeating-linear-gradient(90deg,#000 0 15px,transparent 15px 22px);
  mask: repeating-linear-gradient(90deg,#000 0 15px,transparent 15px 22px);
}

.cis-16__card blockquote {
  font-size: 17px;
  line-height: 1.5;
  font-weight: 500;
  color: #e6e9f2;
}

.cis-16__card figcaption {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: auto;
}

.cis-16__card figcaption img {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  border: 1px solid var(--line);
}

.cis-16__card figcaption span {
  display: flex;
  flex-direction: column;
  font-size: 13px;
  color: #9298ac;
}

.cis-16__card figcaption b {
  font-size: 14px;
  color: #fff;
  font-weight: 700;
}

@supports (scroll-marker-group: after) {
  .cis-16__rail {
    scroll-marker-group: after;
    padding-bottom: 24px;
  }

  .cis-16__rail::scroll-marker-group {
    display: flex;
    gap: 8px;
    justify-content: center;
    margin-top: 14px;
  }

  .cis-16__card::scroll-marker {
    content: "";
    width: 8px;
    height: 8px;
    border-radius: 50%;
    border: 0;
    background: rgba(255,255,255,.26);
    cursor: pointer;
    transition: background .25s,width .25s;
  }

  .cis-16__card::scroll-marker:target-current {
    background: var(--accent);
    width: 22px;
    border-radius: 4px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-16__rail {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — native scroll-snap; stars are a masked gradient (--r = rating%). */
```

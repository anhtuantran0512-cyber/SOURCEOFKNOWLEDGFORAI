---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/testimonial-card-rail-marquee/"
title: "Auto-Sliding Testimonial Marquee — Card Rail with Focus-Safe Pause"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "The modern replacement for testimonial carousels: customer quote cards drift by slowly enough to read, freeze the moment a cursor or keyboard focus enters…"
has_js: "false"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Auto-Sliding Testimonial Marquee — Card Rail with Focus-Safe Pause
Source: https://codefronts.com/motion/css-infinite-marquee/testimonial-card-rail-marquee/

The modern replacement for testimonial carousels: customer quote cards drift by slowly enough to read, freeze the moment a cursor or keyboard focus enters the rail, and lift softly on hover — no dots, no arrows, no slider library, and every quote remains real selectable text a visitor can copy.
## HTML
```html
<section class="mqs-07" aria-label="Testimonial marquee demo">
  <div class="mqs-07__inner">
    <h3 class="mqs-07__title">Loved by teams everywhere</h3>
    <p class="mqs-07__sub">Hover or focus to pause and read</p>
    <div class="mqs-07__rail">
      <div class="mqs-07__group">
        <figure class="mqs-07__card">
          <p class="mqs-07__stars" aria-hidden="true">★★★★★</p><span class="mqs-07__sr">Rated 5 out of 5</span>
          <blockquote class="mqs-07__quote">“Cut our onboarding time in half. The team actually enjoys using it.”</blockquote>
          <figcaption class="mqs-07__who"><span class="mqs-07__avatar" style="--a:#7c3aed" aria-hidden="true">MK</span><span><b>Mara Kent</b><br>Ops lead, Fernwork</span></figcaption>
        </figure>
        <figure class="mqs-07__card">
          <p class="mqs-07__stars" aria-hidden="true">★★★★★</p><span class="mqs-07__sr">Rated 5 out of 5</span>
          <blockquote class="mqs-07__quote">“The first tool our engineers and our accountants both said yes to.”</blockquote>
          <figcaption class="mqs-07__who"><span class="mqs-07__avatar" style="--a:#0891b2" aria-hidden="true">DA</span><span><b>Dev Anand</b><br>CTO, Baseline</span></figcaption>
        </figure>
        <figure class="mqs-07__card">
          <p class="mqs-07__stars" aria-hidden="true">★★★★★</p><span class="mqs-07__sr">Rated 5 out of 5</span>
          <blockquote class="mqs-07__quote">“Support answered in four minutes. On a Sunday. We're not leaving.”</blockquote>
          <figcaption class="mqs-07__who"><span class="mqs-07__avatar" style="--a:#dc2626" aria-hidden="true">JW</span><span><b>Jess Whitfield</b><br>Founder, Quill &amp; Co</span></figcaption>
        </figure>
        <figure class="mqs-07__card">
          <p class="mqs-07__stars" aria-hidden="true">★★★★★</p><span class="mqs-07__sr">Rated 5 out of 5</span>
          <blockquote class="mqs-07__quote">“Migrated 40k records on day one without a single support ticket.”</blockquote>
          <figcaption class="mqs-07__who"><span class="mqs-07__avatar" style="--a:#059669" aria-hidden="true">TO</span><span><b>Tom Okafor</b><br>Data lead, Harbourly</span></figcaption>
        </figure>
      </div>
      <div class="mqs-07__group" aria-hidden="true">
        <figure class="mqs-07__card">
          <p class="mqs-07__stars">★★★★★</p>
          <blockquote class="mqs-07__quote">“Cut our onboarding time in half. The team actually enjoys using it.”</blockquote>
          <figcaption class="mqs-07__who"><span class="mqs-07__avatar" style="--a:#7c3aed">MK</span><span><b>Mara Kent</b><br>Ops lead, Fernwork</span></figcaption>
        </figure>
        <figure class="mqs-07__card">
          <p class="mqs-07__stars">★★★★★</p>
          <blockquote class="mqs-07__quote">“The first tool our engineers and our accountants both said yes to.”</blockquote>
          <figcaption class="mqs-07__who"><span class="mqs-07__avatar" style="--a:#0891b2">DA</span><span><b>Dev Anand</b><br>CTO, Baseline</span></figcaption>
        </figure>
        <figure class="mqs-07__card">
          <p class="mqs-07__stars">★★★★★</p>
          <blockquote class="mqs-07__quote">“Support answered in four minutes. On a Sunday. We're not leaving.”</blockquote>
          <figcaption class="mqs-07__who"><span class="mqs-07__avatar" style="--a:#dc2626">JW</span><span><b>Jess Whitfield</b><br>Founder, Quill &amp; Co</span></figcaption>
        </figure>
        <figure class="mqs-07__card">
          <p class="mqs-07__stars">★★★★★</p>
          <blockquote class="mqs-07__quote">“Migrated 40k records on day one without a single support ticket.”</blockquote>
          <figcaption class="mqs-07__who"><span class="mqs-07__avatar" style="--a:#059669">TO</span><span><b>Tom Okafor</b><br>Data lead, Harbourly</span></figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mqs-07,
.mqs-07 *,
.mqs-07 *::before,
.mqs-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-07 {
  min-height: 100vh;
  width: 100%;
  --gap: 22px;
  --speed: 45s;
  --accent: #b45309;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fffbf5;
  padding: 64px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow-x: clip;
}

.mqs-07__inner {
  width: min(1000px,100%);
}

.mqs-07__title {
  font-size: clamp(20px,3vw,26px);
  font-weight: 800;
  color: #292524;
  text-align: center;
  letter-spacing: -.02em;
}

.mqs-07__sub {
  font-size: 13px;
  color: #a8a29e;
  text-align: center;
  margin: 6px 0 30px;
}

.mqs-07__rail {
  display: flex;
  gap: var(--gap);
  overflow: hidden;
  padding-block: 10px;
  mask-image: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
}

.mqs-07__group {
  flex: none;
  display: flex;
  align-items: stretch;
  gap: var(--gap);
  animation: mqs-07-scroll var(--speed) linear infinite;
  will-change: transform;
}

@keyframes mqs-07-scroll {
  to {
    transform: translateX(calc(-100% - var(--gap)));
  }
}

.mqs-07__rail:hover .mqs-07__group,
.mqs-07__rail:focus-within .mqs-07__group {
  animation-play-state: paused;
}

.mqs-07__card {
  flex: none;
  width: 300px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #fff;
  border: 1px solid #f0e4d3;
  border-radius: 16px;
  padding: 22px;
  box-shadow: 0 2px 10px -6px rgba(120,80,20,.18);
  transition: transform .2s,box-shadow .2s;
  user-select: text;
}

.mqs-07__card:hover {
  transform: translateY(-4px);
  box-shadow: 0 14px 28px -14px rgba(120,80,20,.28);
}

.mqs-07__stars {
  font-size: 13px;
  letter-spacing: 2px;
  color: var(--accent);
}

.mqs-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.mqs-07__quote {
  font-size: 14.5px;
  line-height: 1.55;
  color: #44403c;
  text-wrap: pretty;
}

.mqs-07__who {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 12px;
  line-height: 1.35;
  color: #78716c;
  margin-top: auto;
}

.mqs-07__who b {
  color: #292524;
  font-size: 13px;
}

.mqs-07__avatar {
  flex: none;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 11px;
  font-weight: 800;
  color: #fff;
  background: var(--a,#78716c);
}

@media (prefers-reduced-motion: reduce) {
  .mqs-07__group {
    animation: none;
  }

  .mqs-07__rail {
    overflow-x: auto;
    mask-image: none;
    -webkit-mask-image: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the reading contract is CSS: 45s loop, pause on :hover AND :focus-within, fixed 300px cards so loop math never depends on quote length. */
```

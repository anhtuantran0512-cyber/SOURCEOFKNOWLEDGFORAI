---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/trustpilot-and-google-style-review-card/"
title: "Trustpilot & Google Style Review Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "The third-party review widget pattern: a source-branded header with an aggregate score, then individual reviews carrying the platform's visual signature —…"
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Trustpilot & Google Style Review Card
Source: https://codefronts.com/components/css-testimonials-reviews/trustpilot-and-google-style-review-card/

The third-party review widget pattern: a source-branded header with an aggregate score, then individual reviews carrying the platform's visual signature — square filled rating blocks for the review-platform style, round monogram avatars and a relative timestamp for the search-engine style. Both cards are drawn entirely with CSS shapes and inline SVG, so nothing here depends on a vendor script or an iframe.
## HTML
```html
<section class="tr-06" aria-label="Third-party review platform style cards demo">
  <div class="tr-06__stage">
    <div class="tr-06__grid">

      <article class="tr-06__card" data-plat="trust">
        <header class="tr-06__ph">
          <span class="tr-06__logo" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 2.4l2.9 6 6.6.9-4.8 4.6 1.2 6.6L12 17.4 6.1 20.5l1.2-6.6L2.5 9.3l6.6-.9z" fill="currentColor"/></svg><b>Reviewly</b></span>
          <span class="tr-06__ver"><svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.4"/><path d="M6.4 10.2l2.4 2.4 4.8-5" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Verified company</span>
        </header>

        <div class="tr-06__agg">
          <div class="tr-06__blocks" data-score="5" role="img" aria-label="Rated excellent, 4.7 out of 5"><i></i><i></i><i></i><i></i><i></i></div>
          <p><b>4.7</b> Excellent · <span>3,912 reviews</span></p>
        </div>

        <figure class="tr-06__rev">
          <header>
            <span class="tr-06__mono" aria-hidden="true">HB</span>
            <div>
              <b>Hollie Bennett</b>
              <span class="tr-06__meta">2 reviews · <span aria-hidden="true">🇬🇧</span> United Kingdom</span>
            </div>
          </header>
          <div class="tr-06__blocks tr-06__blocks--sm" data-score="5" role="img" aria-label="Rated 5 out of 5"><i></i><i></i><i></i><i></i><i></i></div>
          <h3>Delivered a week early and under quote</h3>
          <blockquote>Booked on a Tuesday, installed the following Monday. The engineer sent a photo of the meter reading before he left — I have never had a trade do that.</blockquote>
          <footer><time datetime="2026-07-12">12 July 2026</time> · Experience: 8 July 2026</footer>
        </figure>
      </article>

      <article class="tr-06__card" data-plat="search">
        <header class="tr-06__ph">
          <span class="tr-06__logo" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 3v18M3 12h18" fill="none" stroke="currentColor" stroke-width="1.4" opacity=".55"/></svg><b>Search Business Profile</b></span>
          <span class="tr-06__pin">Local · Manchester</span>
        </header>

        <div class="tr-06__agg">
          <span class="tr-06__stars" style="--tr-06-pct:96%" role="img" aria-label="Rated 4.8 out of 5"></span>
          <p><b>4.8</b> · <span>612 Google-style reviews</span></p>
        </div>

        <figure class="tr-06__rev">
          <header>
            <img class="tr-06__ava" src="https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Sofia Marchetti" width="40" height="40" loading="lazy" decoding="async">
            <div>
              <b>Sofia Marchetti</b>
              <span class="tr-06__meta">Local Guide · 84 reviews · 12 photos</span>
            </div>
          </header>
          <span class="tr-06__stars tr-06__stars--sm" style="--tr-06-pct:100%" role="img" aria-label="Rated 5 out of 5"></span>
          <blockquote>Third year in a row we have used them for the office fit-out. They quote in plain English, they turn up when they say, and when a panel arrived damaged they replaced it before we noticed.</blockquote>
          <div class="tr-06__shots" aria-hidden="true">
            <img src="https://images.unsplash.com/photo-1524758631624-e2822e304c36?q=80&w=240&h=240&fit=crop&auto=format" alt="" width="62" height="62" loading="lazy" decoding="async">
            <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=240&h=240&fit=crop&auto=format" alt="" width="62" height="62" loading="lazy" decoding="async">
            <span>+10</span>
          </div>
          <footer><time datetime="2026-06-28">3 weeks ago</time> · <b>Owner replied</b></footer>
        </figure>
      </article>

    </div>
    <p class="tr-06__chip" aria-hidden="true">data-score rating blocks · clip-path stars · &lt;time datetime&gt; · pair with JSON-LD AggregateRating</p>
  </div>
</section>
```
## CSS
```css
.tr-06,
.tr-06 *,
.tr-06 *::before,
.tr-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-06-bg: oklch(0.95 0.008 230);
  --tr-06-card: oklch(1 0 0);
  --tr-06-ink: oklch(0.23 0.015 250);
  --tr-06-mut: oklch(0.55 0.015 250);
  --tr-06-trust: oklch(0.66 0.17 155);
  --tr-06-search: oklch(0.6 0.18 255);
  --tr-06-star: oklch(0.78 0.16 76);
  --tr-06-off: oklch(0.9 0.008 250);
  background: var(--tr-06-bg);
  color: var(--tr-06-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(18px,4vw,52px);
}

.tr-06__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,330px),1fr));
  gap: clamp(14px,2vw,22px);
  width: min(100%,880px);
}

.tr-06__card {
  --tr-06-on: var(--tr-06-trust);
  display: grid;
  align-content: start;
  gap: 16px;
  padding: clamp(18px,2.6vw,24px);
  background: var(--tr-06-card);
  border: 1px solid oklch(0 0 0/.08);
  border-radius: 16px;
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 20px 44px -30px oklch(0.3 0.04 250/.7);
  animation: tr-06-in .7s cubic-bezier(.16,1,.3,1) both;
}

.tr-06__card[data-plat='search'] {
  --tr-06-on: var(--tr-06-search);
  animation-delay: .1s;
}

@keyframes tr-06-in {
  from {
    opacity: 0;
    translate: 0 16px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-06__ph {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  flex-wrap: wrap;
  padding-bottom: 14px;
  border-bottom: 1px solid oklch(0 0 0/.07);
}

.tr-06__logo {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  color: var(--tr-06-on);
  font-size: 14px;
  letter-spacing: -.015em;
}

.tr-06__logo svg {
  width: 19px;
  height: 19px;
}

.tr-06__logo b {
  font-weight: 700;
  color: var(--tr-06-ink);
}

.tr-06__ver {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 11.5px;
  font-weight: 620;
  color: var(--tr-06-trust);
}

.tr-06__ver svg {
  width: 14px;
  height: 14px;
  fill: var(--tr-06-trust);
}

.tr-06__pin {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--tr-06-mut);
  padding: 4px 9px;
  border-radius: 99px;
  background: oklch(0 0 0/.05);
}

.tr-06__agg {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.tr-06__agg p {
  font-size: 13px;
  color: var(--tr-06-mut);
}

.tr-06__agg b {
  font-size: 16px;
  font-weight: 700;
  color: var(--tr-06-ink);
  font-variant-numeric: tabular-nums;
}

.tr-06__blocks {
  display: flex;
  gap: 3px;
}

.tr-06__blocks i {
  inline-size: 24px;
  aspect-ratio: 1;
  border-radius: 4px;
  background: var(--tr-06-off);
}

.tr-06__blocks--sm i {
  inline-size: 17px;
  border-radius: 3px;
}

.tr-06__blocks[data-score='5'] i:nth-child(-n+5),
.tr-06__blocks[data-score='4'] i:nth-child(-n+4),
.tr-06__blocks[data-score='3'] i:nth-child(-n+3),
.tr-06__blocks[data-score='2'] i:nth-child(-n+2),
.tr-06__blocks[data-score='1'] i:nth-child(-n+1) {
  background: var(--tr-06-on);
  animation: tr-06-pop .5s cubic-bezier(.16,1,.3,1) both;
}

.tr-06__blocks i:nth-child(2) {
  animation-delay: .05s;
}

.tr-06__blocks i:nth-child(3) {
  animation-delay: .1s;
}

.tr-06__blocks i:nth-child(4) {
  animation-delay: .15s;
}

.tr-06__blocks i:nth-child(5) {
  animation-delay: .2s;
}

@keyframes tr-06-pop {
  from {
    scale: .4;
    opacity: 0;
  }

  to {
    scale: 1;
    opacity: 1;
  }
}

.tr-06__stars {
  position: relative;
  display: inline-block;
  font-size: 19px;
  line-height: 1;
  letter-spacing: 1px;
}

.tr-06__stars::before {
  content: '★★★★★';
  color: var(--tr-06-off);
}

.tr-06__stars::after {
  content: '★★★★★';
  color: var(--tr-06-star);
  position: absolute;
  inset: 0;
  clip-path: inset(0 calc(100% - var(--tr-06-pct,100%)) 0 0);
}

.tr-06__stars--sm {
  font-size: 15px;
}

.tr-06__rev {
  display: grid;
  gap: 11px;
}

.tr-06__rev>header {
  display: flex;
  align-items: center;
  gap: 11px;
}

.tr-06__rev header div {
  display: grid;
  gap: 2px;
}

.tr-06__rev header b {
  font-size: 14.5px;
  font-weight: 640;
  letter-spacing: -.012em;
}

.tr-06__meta {
  font-size: 11.5px;
  color: var(--tr-06-mut);
}

.tr-06__mono {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--tr-06-on) 20%,var(--tr-06-card));
  color: color-mix(in oklch,var(--tr-06-on) 75%,black);
  font-size: 14px;
  font-weight: 700;
  flex: none;
}

.tr-06__ava {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: var(--tr-06-off);
}

.tr-06__rev h3 {
  font-size: 15.5px;
  font-weight: 660;
  letter-spacing: -.02em;
  line-height: 1.3;
}

.tr-06__rev blockquote {
  font-size: 14px;
  line-height: 1.6;
  color: color-mix(in oklch,var(--tr-06-ink) 88%,transparent);
  text-wrap: pretty;
}

.tr-06__shots {
  display: flex;
  align-items: center;
  gap: 6px;
}

.tr-06__shots img {
  width: 62px;
  height: 62px;
  border-radius: 9px;
  object-fit: cover;
  background: var(--tr-06-off);
}

.tr-06__shots span {
  display: grid;
  place-items: center;
  width: 62px;
  height: 62px;
  border-radius: 9px;
  background: oklch(0 0 0/.05);
  font-size: 12px;
  font-weight: 640;
  color: var(--tr-06-mut);
}

.tr-06__rev footer {
  font-size: 11.5px;
  color: var(--tr-06-mut);
  padding-top: 11px;
  border-top: 1px solid oklch(0 0 0/.06);
}

.tr-06__rev footer b {
  color: var(--tr-06-on);
  font-weight: 640;
}

.tr-06__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-06-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.11);
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
}

@media (prefers-reduced-motion: reduce) {
  .tr-06__card,
    .tr-06__blocks i {
    animation: none;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/e-commerce-product-review-card-with-star-ratings/"
title: "E-Commerce Product Review Card with Star Ratings"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "The full product-page review block: aggregate score, a five-row rating histogram, verified-purchase reviews with size and fit metadata, and working \"helpful\"…"
has_js: "true"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Product Review Card with Star Ratings
Source: https://codefronts.com/components/css-testimonials-reviews/e-commerce-product-review-card-with-star-ratings/

The full product-page review block: aggregate score, a five-row rating histogram, verified-purchase reviews with size and fit metadata, and working "helpful" votes. The star rows use one gradient-masked SVG per rating, so 4.3 stars renders as exactly 4.3 stars — no half-star sprite, no rounding lie.
## HTML
```html
<section class="tr-03" aria-label="E-commerce product review card with star ratings demo">
  <div class="tr-03__stage">
    <article class="tr-03__card">
      <div class="tr-03__top">
        <div class="tr-03__media">
          <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=700&auto=format&fit=crop" alt="Charcoal running shoe photographed on a neutral background" width="320" height="320" loading="lazy" decoding="async">
          <span class="tr-03__flag">Best seller</span>
        </div>

        <div class="tr-03__summary">
          <p class="tr-03__brand">Meridian Athletic</p>
          <h2 class="tr-03__name">Trailform GTX — Trail Running Shoe</h2>
          <div class="tr-03__agg">
            <b class="tr-03__score">4.3</b>
            <div>
              <span class="tr-03__stars" style="--tr-03-pct:86%" role="img" aria-label="Rated 4.3 out of 5"></span>
              <p class="tr-03__count">1,284 reviews · 92% would buy again</p>
            </div>
          </div>

          <ul class="tr-03__hist">
            <li style="--tr-03-pct:68%"><span>5★</span><span class="tr-03__bar" aria-hidden="true"><i></i></span><span class="tr-03__n">873</span></li>
            <li style="--tr-03-pct:19%"><span>4★</span><span class="tr-03__bar" aria-hidden="true"><i></i></span><span class="tr-03__n">244</span></li>
            <li style="--tr-03-pct:7%"><span>3★</span><span class="tr-03__bar" aria-hidden="true"><i></i></span><span class="tr-03__n">89</span></li>
            <li style="--tr-03-pct:4%"><span>2★</span><span class="tr-03__bar" aria-hidden="true"><i></i></span><span class="tr-03__n">51</span></li>
            <li style="--tr-03-pct:2%"><span>1★</span><span class="tr-03__bar" aria-hidden="true"><i></i></span><span class="tr-03__n">27</span></li>
          </ul>
        </div>
      </div>

      <div class="tr-03__reviews">
        <figure class="tr-03__rev">
          <header class="tr-03__rh">
            <img class="tr-03__ava" src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Jessa M." width="38" height="38" loading="lazy" decoding="async">
            <div>
              <b>Jessa M.</b>
              <span class="tr-03__ver"><svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.4"/><path d="M6.4 10.2l2.4 2.4 4.8-5" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Verified purchase</span>
            </div>
            <span class="tr-03__stars tr-03__stars--sm" style="--tr-03-pct:100%" role="img" aria-label="Rated 5 out of 5"></span>
          </header>
          <blockquote><b>Held up over 340 km of wet limestone.</b> I sized up half and that was right — the toe box runs narrow out of the box but relaxes after a week. Grip on wet rock is the reason I'll rebuy.</blockquote>
          <ul class="tr-03__meta"><li>Size: <b>UK 7.5</b></li><li>Fit: <b>Runs small</b></li><li>Width: <b>Narrow</b></li><li>Owned: <b>4 months</b></li></ul>
          <footer class="tr-03__rf">
            <time datetime="2026-06-14">14 June 2026</time>
            <button class="tr-03__help" type="button" aria-pressed="false" data-base="38">
              <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M6 17V8.6l3.6-5.2c.9-1.3 2.9-.6 2.9 1V8h3.3c1 0 1.8.9 1.6 1.9l-1.1 5.6c-.2.9-1 1.5-1.9 1.5H6z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><rect x="2" y="8.4" width="3.2" height="8.6" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
              Helpful <span class="tr-03__hn" aria-live="polite">38</span>
            </button>
          </footer>
        </figure>

        <figure class="tr-03__rev">
          <header class="tr-03__rh">
            <img class="tr-03__ava" src="https://images.unsplash.com/photo-1546525848-3ce03ca516f6?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Andrew T." width="38" height="38" loading="lazy" decoding="async">
            <div>
              <b>Andrew T.</b>
              <span class="tr-03__ver"><svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.4"/><path d="M6.4 10.2l2.4 2.4 4.8-5" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Verified purchase</span>
            </div>
            <span class="tr-03__stars tr-03__stars--sm" style="--tr-03-pct:80%" role="img" aria-label="Rated 4 out of 5"></span>
          </header>
          <blockquote><b>Brilliant shoe, average laces.</b> Everything above the eyelets is superb. The stock laces slacken on long descents — swapped them in week two and it's been faultless since.</blockquote>
          <ul class="tr-03__meta"><li>Size: <b>US 11</b></li><li>Fit: <b>True to size</b></li><li>Width: <b>Regular</b></li><li>Owned: <b>7 weeks</b></li></ul>
          <footer class="tr-03__rf">
            <time datetime="2026-05-02">2 May 2026</time>
            <button class="tr-03__help" type="button" aria-pressed="false" data-base="21">
              <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M6 17V8.6l3.6-5.2c.9-1.3 2.9-.6 2.9 1V8h3.3c1 0 1.8.9 1.6 1.9l-1.1 5.6c-.2.9-1 1.5-1.9 1.5H6z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><rect x="2" y="8.4" width="3.2" height="8.6" rx="1" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
              Helpful <span class="tr-03__hn" aria-live="polite">21</span>
            </button>
          </footer>
        </figure>
      </div>
      <p class="tr-03__chip" aria-hidden="true">clip-path fractional stars · container query card · aria-pressed vote · tabular-nums</p>
    </article>
  </div>
</section>
```
## CSS
```css
.tr-03,
.tr-03 *,
.tr-03 *::before,
.tr-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-03-bg: oklch(0.96 0.006 250);
  --tr-03-card: oklch(1 0 0);
  --tr-03-ink: oklch(0.24 0.015 260);
  --tr-03-mut: oklch(0.55 0.015 260);
  --tr-03-acc: oklch(0.55 0.16 250);
  --tr-03-star: oklch(0.78 0.16 76);
  --tr-03-ok: oklch(0.6 0.15 152);
  background: var(--tr-03-bg);
  color: var(--tr-03-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(16px,4vw,48px);
}

.tr-03__card {
  container-type: inline-size;
  width: min(100%,880px);
  background: var(--tr-03-card);
  border: 1px solid oklch(0 0 0/.07);
  border-radius: 22px;
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 30px 60px -34px oklch(0.3 0.04 260/.6);
  overflow: hidden;
  animation: tr-03-in .75s cubic-bezier(.16,1,.3,1) both;
}

@keyframes tr-03-in {
  from {
    opacity: 0;
    translate: 0 20px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-03__top {
  display: grid;
  gap: clamp(18px,3cqi,28px);
  padding: clamp(18px,3cqi,28px);
}

@container (min-width: 620px) {
  .tr-03__top {
    grid-template-columns: 280px 1fr;
  }
}

.tr-03__media {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  background: linear-gradient(140deg,oklch(0.9 0.02 250),oklch(0.82 0.03 260));
  aspect-ratio: 1;
}

.tr-03__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: scale .5s cubic-bezier(.16,1,.3,1);
}

.tr-03__card:hover .tr-03__media img {
  scale: 1.04;
}

.tr-03__flag {
  position: absolute;
  inset-block-start: 12px;
  inset-inline-start: 12px;
  padding: 5px 10px;
  border-radius: 8px;
  background: oklch(0.22 0.02 260/.86);
  color: oklch(0.99 0 0);
  font-size: 11px;
  font-weight: 650;
  letter-spacing: .02em;
  backdrop-filter: blur(6px);
}

.tr-03__brand {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--tr-03-acc);
}

.tr-03__name {
  margin-top: 6px;
  font-size: clamp(19px,2.6cqi,25px);
  font-weight: 660;
  letter-spacing: -.028em;
  line-height: 1.2;
  text-wrap: balance;
}

.tr-03__agg {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 16px;
}

.tr-03__score {
  font-size: 44px;
  font-weight: 700;
  letter-spacing: -.045em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.tr-03__stars {
  position: relative;
  display: inline-block;
  font-size: 17px;
  line-height: 1;
  letter-spacing: 2px;
}

.tr-03__stars::before {
  content: '★★★★★';
  color: oklch(0 0 0/.14);
}

.tr-03__stars::after {
  content: '★★★★★';
  color: var(--tr-03-star);
  position: absolute;
  inset: 0;
  clip-path: inset(0 calc(100% - var(--tr-03-pct,100%)) 0 0);
  overflow: hidden;
}

.tr-03__stars--sm {
  font-size: 14px;
  margin-inline-start: auto;
}

.tr-03__count {
  margin-top: 5px;
  font-size: 12.5px;
  color: var(--tr-03-mut);
}

.tr-03__hist {
  list-style: none;
  margin-top: 18px;
  display: grid;
  gap: 7px;
}

.tr-03__hist li {
  display: grid;
  grid-template-columns: 26px 1fr 44px;
  align-items: center;
  gap: 10px;
  font-size: 12px;
  color: var(--tr-03-mut);
  font-variant-numeric: tabular-nums;
}

.tr-03__bar {
  block-size: 7px;
  border-radius: 99px;
  background: oklch(0 0 0/.07);
  overflow: hidden;
}

.tr-03__bar i {
  display: block;
  block-size: 100%;
  inline-size: var(--tr-03-pct);
  border-radius: 99px;
  background: linear-gradient(90deg,var(--tr-03-star),color-mix(in oklch,var(--tr-03-star) 60%,var(--tr-03-acc)));
  animation: tr-03-grow 1s cubic-bezier(.16,1,.3,1) both;
  animation-delay: .2s;
}

@keyframes tr-03-grow {
  from {
    inline-size: 0;
  }
}

.tr-03__n {
  text-align: end;
}

.tr-03__reviews {
  border-top: 1px solid oklch(0 0 0/.07);
  background: color-mix(in oklch,var(--tr-03-acc) 3.5%,var(--tr-03-card));
}

.tr-03__rev {
  padding: clamp(18px,3cqi,26px);
  border-bottom: 1px solid oklch(0 0 0/.06);
}

.tr-03__rh {
  display: flex;
  align-items: center;
  gap: 11px;
}

.tr-03__ava {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: oklch(0.88 0.02 250);
}

.tr-03__rh div {
  display: grid;
  gap: 2px;
}

.tr-03__rh b {
  font-size: 14px;
  font-weight: 640;
  letter-spacing: -.01em;
}

.tr-03__ver {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--tr-03-ok);
}

.tr-03__ver svg {
  width: 14px;
  height: 14px;
  fill: var(--tr-03-ok);
}

.tr-03__rev blockquote {
  margin-top: 13px;
  font-size: 14.5px;
  line-height: 1.6;
  color: color-mix(in oklch,var(--tr-03-ink) 90%,transparent);
  text-wrap: pretty;
}

.tr-03__rev blockquote b {
  font-weight: 660;
  color: var(--tr-03-ink);
}

.tr-03__meta {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 13px;
}

.tr-03__meta li {
  padding: 5px 10px;
  border-radius: 8px;
  background: oklch(0 0 0/.045);
  border: 1px solid oklch(0 0 0/.05);
  font-size: 11.5px;
  color: var(--tr-03-mut);
}

.tr-03__meta b {
  color: var(--tr-03-ink);
  font-weight: 620;
}

.tr-03__rf {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-top: 15px;
  font-size: 12px;
  color: var(--tr-03-mut);
}

.tr-03__help {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 99px;
  border: 1px solid oklch(0 0 0/.13);
  background: var(--tr-03-card);
  color: var(--tr-03-mut);
  font: inherit;
  font-size: 13px;
  font-weight: 560;
  cursor: pointer;
  transition: background .22s,color .22s,border-color .22s,scale .22s cubic-bezier(.16,1,.3,1);
}

.tr-03__help svg {
  width: 17px;
  height: 17px;
  transition: rotate .3s cubic-bezier(.16,1,.3,1),translate .3s;
}

.tr-03__help:hover {
  border-color: var(--tr-03-acc);
  color: var(--tr-03-acc);
}

.tr-03__help:focus-visible {
  outline: 3px solid var(--tr-03-acc);
  outline-offset: 2px;
}

.tr-03__help[aria-pressed='true'] {
  background: color-mix(in oklch,var(--tr-03-acc) 12%,transparent);
  border-color: var(--tr-03-acc);
  color: var(--tr-03-acc);
}

.tr-03__help[aria-pressed='true'] svg {
  rotate: -8deg;
  translate: 0 -1px;
}

.tr-03__help[aria-pressed='true'] {
  animation: tr-03-pop .34s cubic-bezier(.16,1,.3,1);
}

@keyframes tr-03-pop {
  40% {
    scale: 1.06;
  }
}

.tr-03__hn {
  font-variant-numeric: tabular-nums;
  font-weight: 660;
}

.tr-03__chip {
  padding: 14px 20px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-03-mut);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .tr-03__card,
    .tr-03__bar i,
    .tr-03__help[aria-pressed='true'] {
    animation: none;
  }

  .tr-03__card:hover .tr-03__media img {
    scale: 1;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tr-03 .tr-03__help').forEach((btn) => {
    if (btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const out = btn.querySelector('.tr-03__hn');
    const base = Number(btn.dataset.base || 0);
    btn.addEventListener('click', () => {
      const on = btn.getAttribute('aria-pressed') !== 'true';
      btn.setAttribute('aria-pressed', String(on));
      out.textContent = String(base + (on ? 1 : 0));
    });
  });
})();
```

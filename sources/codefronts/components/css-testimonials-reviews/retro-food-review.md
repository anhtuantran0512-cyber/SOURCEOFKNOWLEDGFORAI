---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/retro-food-review/"
title: "Retro Food & Restaurant Review Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Warm, printed-menu energy for hospitality and food-delivery products: cream stock, a mustard-and-tomato palette, dish tag pills, a reviewer level badge and…"
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Food & Restaurant Review Card
Source: https://codefronts.com/components/css-testimonials-reviews/retro-food-review/

Warm, printed-menu energy for hospitality and food-delivery products: cream stock, a mustard-and-tomato palette, dish tag pills, a reviewer level badge and the dish photo strip that makes a food review actually useful. The card is textured with a repeating conic "paper" pattern and a torn-edge mask — both pure CSS, both free.
## HTML
```html
<section class="tr-15" aria-label="Retro food and restaurant review card demo">
  <div class="tr-15__stage">
    <article class="tr-15__card">
      <header class="tr-15__top">
        <div class="tr-15__place">
          <p class="tr-15__kicker">Reviewed · Neighbourhood bistro</p>
          <h2 class="tr-15__name">The Copper Larder</h2>
          <p class="tr-15__where">Fitzroy North, Melbourne · Modern Australian · $$</p>
        </div>
        <div class="tr-15__score">
          <b>4.6</b>
          <span class="tr-15__stars" role="img" aria-label="Rated 4.6 out of 5">★★★★<i>★</i></span>
          <span>412 reviews</span>
        </div>
      </header>

      <figure class="tr-15__rev">
        <div class="tr-15__who">
          <img src="https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Sofia Marchetti" width="48" height="48" loading="lazy" decoding="async">
          <div>
            <b>Sofia Marchetti</b>
            <span class="tr-15__lvl">Local Guide · Level 6 · 84 reviews</span>
          </div>
          <span class="tr-15__visit">Dined in · Dinner</span>
        </div>

        <blockquote>Booked on a whim at 6pm on a Tuesday and got the last table by the window. The lamb is the reason to come — thirty-six hours in the oven and it does not need a knife. Service was quick without ever feeling like they wanted the table back.</blockquote>

        <ul class="tr-15__tags">
          <li class="tr-15__tag" style="--tr-15-h:35">Slow-cooked lamb</li>
          <li class="tr-15__tag" style="--tr-15-h:120">Charred greens</li>
          <li class="tr-15__tag" style="--tr-15-h:75">Burnt honey tart</li>
          <li class="tr-15__tag" style="--tr-15-h:265">Natural wine list</li>
        </ul>

        <div class="tr-15__shots">
          <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=400&h=400&fit=crop&auto=format" alt="Plated lamb dish with jus" width="96" height="96" loading="lazy" decoding="async">
          <img src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=400&h=400&fit=crop&auto=format" alt="Bowl of charred greens" width="96" height="96" loading="lazy" decoding="async">
          <img src="https://images.unsplash.com/photo-1552566626-52f8b828add9?q=80&w=400&h=400&fit=crop&auto=format" alt="Warm interior of the dining room" width="96" height="96" loading="lazy" decoding="async">
          <span class="tr-15__count">+6</span>
        </div>

        <footer class="tr-15__f">
          <time datetime="2026-07-21">21 July 2026</time>
          <span class="tr-15__helpful">Helpful · 64</span>
        </footer>
      </figure>
    </article>
    <p class="tr-15__chip" aria-hidden="true">radial-gradient mask scallops · hue-token dish pills · aspect-ratio photo strip · zero CLS</p>
  </div>
</section>
```
## CSS
```css
.tr-15,
.tr-15 *,
.tr-15 *::before,
.tr-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-15-bg: oklch(0.9 0.05 70);
  --tr-15-paper: oklch(0.975 0.02 85);
  --tr-15-ink: oklch(0.25 0.04 45);
  --tr-15-mut: oklch(0.5 0.04 45);
  --tr-15-acc: oklch(0.58 0.19 32);
  --tr-15-star: oklch(0.72 0.16 62);
  background: var(--tr-15-bg);
  color: var(--tr-15-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
  background-image: repeating-linear-gradient(45deg,oklch(0.25 0.04 45/.045) 0 2px,transparent 2px 11px);
}

.tr-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,52px);
}

.tr-15__card {
  --tr-15-s: 13px;
  width: min(100%,660px);
  background: var(--tr-15-paper);
  border-radius: 18px 18px 4px 4px;
  padding: clamp(22px,3.4vw,32px) clamp(20px,3.4vw,30px) calc(clamp(20px,3.4vw,30px) + var(--tr-15-s));
  box-shadow: 0 28px 56px -34px oklch(0.3 0.06 45/.8);
  -webkit-mask: radial-gradient(var(--tr-15-s) at 50% 0,transparent 97%,#000) 50% 100%/calc(2*var(--tr-15-s)) var(--tr-15-s) repeat-x,linear-gradient(#000 0 0) 0 0/100% calc(100% - var(--tr-15-s)) no-repeat;
  mask: radial-gradient(var(--tr-15-s) at 50% 0,transparent 97%,#000) 50% 100%/calc(2*var(--tr-15-s)) var(--tr-15-s) repeat-x,linear-gradient(#000 0 0) 0 0/100% calc(100% - var(--tr-15-s)) no-repeat;
  animation: tr-15-in .75s cubic-bezier(.16,1,.3,1) both;
}

@keyframes tr-15-in {
  from {
    opacity: 0;
    translate: 0 18px;
    rotate: -.6deg;
  }

  to {
    opacity: 1;
    translate: 0 0;
    rotate: 0deg;
  }
}

.tr-15__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 18px;
  flex-wrap: wrap;
  padding-bottom: 18px;
  border-bottom: 2px dashed color-mix(in oklch,var(--tr-15-ink) 22%,transparent);
}

.tr-15__kicker {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--tr-15-acc);
}

.tr-15__name {
  margin-top: 5px;
  font-family: Georgia,'Times New Roman',serif;
  font-size: clamp(26px,4vw,36px);
  font-weight: 700;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.tr-15__where {
  margin-top: 6px;
  font-size: 12.5px;
  color: var(--tr-15-mut);
}

.tr-15__score {
  display: grid;
  justify-items: end;
  gap: 3px;
  text-align: end;
}

.tr-15__score b {
  font-size: 34px;
  font-weight: 750;
  line-height: 1;
  letter-spacing: -.04em;
  color: var(--tr-15-acc);
  font-variant-numeric: tabular-nums;
}

.tr-15__stars {
  font-size: 15px;
  letter-spacing: 1.5px;
  color: var(--tr-15-star);
}

.tr-15__stars i {
  opacity: .28;
  font-style: normal;
}

.tr-15__score span:last-child {
  font-size: 11.5px;
  color: var(--tr-15-mut);
}

.tr-15__rev {
  display: grid;
  gap: 16px;
  padding-top: 20px;
}

.tr-15__who {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.tr-15__who img {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  box-shadow: 0 0 0 2px var(--tr-15-paper),0 0 0 4px color-mix(in oklch,var(--tr-15-acc) 55%,transparent);
}

.tr-15__who div {
  display: grid;
  gap: 2px;
}

.tr-15__who b {
  font-size: 15px;
  font-weight: 660;
  letter-spacing: -.014em;
}

.tr-15__lvl {
  font-size: 11px;
  font-weight: 640;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--tr-15-acc);
}

.tr-15__visit {
  margin-inline-start: auto;
  padding: 6px 12px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--tr-15-acc) 12%,transparent);
  border: 1px solid color-mix(in oklch,var(--tr-15-acc) 26%,transparent);
  font-size: 11.5px;
  font-weight: 600;
  color: color-mix(in oklch,var(--tr-15-acc) 85%,black);
}

.tr-15__rev blockquote {
  font-size: 15.5px;
  line-height: 1.62;
  color: color-mix(in oklch,var(--tr-15-ink) 92%,transparent);
  text-wrap: pretty;
}

.tr-15__tags {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tr-15__tag {
  padding: 6px 13px;
  border-radius: 99px;
  background: oklch(0.94 0.07 var(--tr-15-h,35));
  border: 1px solid oklch(0.72 0.12 var(--tr-15-h,35)/.55);
  font-size: 12.5px;
  font-weight: 580;
  color: oklch(0.32 0.09 var(--tr-15-h,35));
  transition: translate .25s cubic-bezier(.16,1,.3,1);
}

.tr-15__tag:hover {
  translate: 0 -2px;
}

.tr-15__shots {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.tr-15__shots img {
  width: 96px;
  aspect-ratio: 1;
  height: auto;
  border-radius: 12px;
  object-fit: cover;
  background: oklch(0.88 0.04 60);
  filter: saturate(1.05) contrast(1.02);
  transition: scale .35s cubic-bezier(.16,1,.3,1);
}

.tr-15__shots img:hover {
  scale: 1.05;
}

.tr-15__count {
  display: grid;
  place-items: center;
  width: 96px;
  aspect-ratio: 1;
  border-radius: 12px;
  background: color-mix(in oklch,var(--tr-15-ink) 8%,transparent);
  border: 1px dashed color-mix(in oklch,var(--tr-15-ink) 26%,transparent);
  font-size: 14px;
  font-weight: 660;
  color: var(--tr-15-mut);
}

.tr-15__f {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-top: 14px;
  border-top: 2px dashed color-mix(in oklch,var(--tr-15-ink) 22%,transparent);
  font-size: 11.5px;
  color: var(--tr-15-mut);
}

.tr-15__helpful {
  font-weight: 620;
  color: var(--tr-15-acc);
}

.tr-15__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-15-mut);
  padding: 8px 15px;
  border: 1px solid color-mix(in oklch,var(--tr-15-ink) 22%,transparent);
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.4);
}

@media (prefers-reduced-motion: reduce) {
  .tr-15__card {
    animation: none;
  }

  .tr-15__shots img,
    .tr-15__tag {
    transition: none;
  }
}
```

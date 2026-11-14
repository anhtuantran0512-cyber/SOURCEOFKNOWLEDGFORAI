---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/trust-badge-footer/"
title: "Footer with Trust Badges & Guarantee Icons"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "Trust badges that a sceptical buyer can verify: each guarantee pairs an icon with a specific, checkable claim and the small print underneath."
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Footer with Trust Badges & Guarantee Icons
Source: https://codefronts.com/layouts/css-footer-designs/trust-badge-footer/

Trust badges that a sceptical buyer can verify: each guarantee pairs an icon with a specific, checkable claim and the small print underneath. Plus an accessible star rating (a real number, not six unlabelled glyphs) and a die-cut seal drawn entirely with clip-path.
## HTML
```html
<section class="ft-21" aria-label="Footer with trust badges and guarantee icons demo">
  <main class="ft-21__main">
    <p class="ft-21__eyebrow">Claim + proof · accessible ratings</p>
    <h1 class="ft-21__title">Badges people can check</h1>
    <p class="ft-21__sub">Every guarantee below states a number, a period and a condition. That is what turns a sticker into a reason to buy.</p>
  </main>
  <footer class="ft-21__foot">
    <section class="ft-21__trust" aria-labelledby="ft-21-th">
      <div class="ft-21__thead">
        <h2 class="ft-21__h" id="ft-21-th">Our guarantees</h2>
        <div class="ft-21__seal" aria-hidden="true"><span>12<small>yr</small></span></div>
      </div>
      <ul class="ft-21__badges">
        <li class="ft-21__badge">
          <span class="ft-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M12 3l8 3.4v6.1c0 4.9-3.3 8.6-8 10.5-4.7-1.9-8-5.6-8-10.5V6.4z"/><path d="M8.6 12.2l2.6 2.6 4.6-4.8"/></svg></span>
          <span class="ft-21__claim">12-year structural warranty</span>
          <span class="ft-21__proof">Frames and joints, transferable if you sell it. <a class="ft-21__inline" href="#ft-21-a">Full terms</a></span>
        </li>
        <li class="ft-21__badge">
          <span class="ft-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M3 12a9 9 0 1 0 3.2-6.9"/><path d="M3 3.5V9h5.5"/><path d="M12 8v4.4l3 1.8"/></svg></span>
          <span class="ft-21__claim">100 nights to change your mind</span>
          <span class="ft-21__proof">Free collection from your door, refunded in 5 working days.</span>
        </li>
        <li class="ft-21__badge">
          <span class="ft-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M4 9.5L12 5l8 4.5-8 4.5z"/><path d="M4 14.5L12 19l8-4.5"/></svg></span>
          <span class="ft-21__claim">Repair, not replace</span>
          <span class="ft-21__proof">Spare parts stocked for 15 years. 2,140 repairs completed in 2025.</span>
        </li>
        <li class="ft-21__badge">
          <span class="ft-21__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><path d="M9.4 10.2l1.9 1.9 3.4-3.6"/></svg></span>
          <span class="ft-21__claim">Made in Leicestershire</span>
          <span class="ft-21__proof">One workshop, 38 people, every order traceable to its maker.</span>
        </li>
      </ul>
      <div class="ft-21__reviews">
        <p class="ft-21__rating"><span class="ft-21__stars" style="--ft-21-pct:96%" aria-hidden="true">★★★★★</span><span class="ft-21__rtext"><strong>4.8 out of 5</strong> from 21,904 verified reviews on an independent platform</span></p>
        <a class="ft-21__rlink" href="#ft-21-a">Read the one-star reviews too<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6"/></svg></a>
      </div>
    </section>
    <div class="ft-21__cols">
      <div class="ft-21__brandcol">
        <div class="ft-21__brand"><span class="ft-21__mark" aria-hidden="true"></span>Rushmere</div>
        <p class="ft-21__blurb">Furniture built to be handed down, not thrown away.</p>
      </div>
      <nav class="ft-21__col" aria-labelledby="ft-21-c1"><h2 class="ft-21__ch" id="ft-21-c1">Shop</h2><ul class="ft-21__list"><li><a class="ft-21__link" href="#ft-21-a">Beds</a></li><li><a class="ft-21__link" href="#ft-21-a">Sofas</a></li><li><a class="ft-21__link" href="#ft-21-a">Tables</a></li><li><a class="ft-21__link" href="#ft-21-a">Spare parts</a></li></ul></nav>
      <nav class="ft-21__col" aria-labelledby="ft-21-c2"><h2 class="ft-21__ch" id="ft-21-c2">Promises</h2><ul class="ft-21__list"><li><a class="ft-21__link" href="#ft-21-a">Warranty terms</a></li><li><a class="ft-21__link" href="#ft-21-a">Returns</a></li><li><a class="ft-21__link" href="#ft-21-a">Delivery</a></li><li><a class="ft-21__link" href="#ft-21-a">Repairs</a></li></ul></nav>
      <nav class="ft-21__col" aria-labelledby="ft-21-c3"><h2 class="ft-21__ch" id="ft-21-c3">Workshop</h2><ul class="ft-21__list"><li><a class="ft-21__link" href="#ft-21-a">Our makers</a></li><li><a class="ft-21__link" href="#ft-21-a">Timber sourcing</a></li><li><a class="ft-21__link" href="#ft-21-a">Visit us</a></li></ul></nav>
    </div>
    <p class="ft-21__copy">© <time datetime="2026">2026</time> Rushmere Workshop Ltd · FSC C014047 · Registered in England 07711204</p>
  </footer>
</section>
```
## CSS
```css
.ft-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-21-bg);
  --ft-21-bg: oklch(0.96 0.014 75);
  --ft-21-foot: oklch(0.985 0.01 75);
  --ft-21-ink: oklch(0.25 0.03 55);
  --ft-21-mut: oklch(0.52 0.02 55);
  --ft-21-acc: oklch(0.48 0.11 45);
  --ft-21-gold: oklch(0.78 0.14 80);
  --ft-21-line: oklch(0.25 0.03 55/.13);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-21-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-21 *,
.ft-21 *::before,
.ft-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-21 ul {
  list-style: none;
}

.ft-21__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(36px,7vh,80px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1160px)/2));
}

.ft-21__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-21-acc);
}

.ft-21__title {
  font-size: clamp(30px,5.4vw,58px);
  line-height: 1.02;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 13ch;
  text-wrap: balance;
}

.ft-21__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-21-mut);
  max-width: 54ch;
  text-wrap: pretty;
}

.ft-21__foot {
  background: var(--ft-21-foot);
  border-top: 1px solid var(--ft-21-line);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1160px)/2));
}

.ft-21__trust {
  display: grid;
  gap: 18px;
  padding-block: clamp(28px,4vw,48px);
}

.ft-21__thead {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px;
}

.ft-21__h {
  font-size: clamp(19px,2.3vw,25px);
  font-weight: 690;
  letter-spacing: -.025em;
}

.ft-21__seal {
  position: relative;
  display: grid;
  place-items: center;
  width: 78px;
  height: 78px;
  margin-inline-start: auto;
  border-radius: 50%;
  background: conic-gradient(from 0deg,var(--ft-21-acc) 0 6deg,transparent 6deg 12deg),radial-gradient(circle,var(--ft-21-acc) 68%,transparent 68%);
  color: oklch(0.98 0.01 75);
  font-weight: 800;
  flex: none;
}

.ft-21__seal::after {
  content: '';
  position: absolute;
  inset: 14%;
  border-radius: 50%;
  border: 1.5px dashed oklch(0.98 0.01 75/.5);
}

.ft-21__seal span {
  position: relative;
  font-size: 21px;
  line-height: 1;
  letter-spacing: -.03em;
}

.ft-21__seal small {
  font-size: 10px;
  letter-spacing: .06em;
  margin-inline-start: 1px;
}

.ft-21__badges {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(15rem,100%),1fr));
  gap: clamp(14px,2vw,24px);
}

.ft-21__badge {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 3px 14px;
  align-items: start;
  padding: 16px;
  border-radius: 16px;
  background: oklch(1 0 0);
  border: 1px solid var(--ft-21-line);
  transition: transform .25s ease,box-shadow .25s ease,border-color .25s ease;
}

.ft-21__badge:hover {
  transform: translateY(-2px);
  border-color: color-mix(in oklch,var(--ft-21-acc) 40%,transparent);
  box-shadow: 0 18px 34px -26px oklch(0.25 0.03 55/.9);
}

.ft-21__ico {
  grid-row: span 2;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 13px;
  background: color-mix(in oklch,var(--ft-21-acc) 12%,transparent);
  color: var(--ft-21-acc);
}

.ft-21__claim {
  font-size: 14.8px;
  font-weight: 680;
  letter-spacing: -.015em;
  text-wrap: balance;
}

.ft-21__proof {
  font-size: 12.8px;
  line-height: 1.5;
  color: var(--ft-21-mut);
  text-wrap: pretty;
}

.ft-21__inline {
  color: var(--ft-21-acc);
  text-decoration: underline;
  text-underline-offset: .22em;
}

.ft-21__reviews {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 22px;
  padding: 16px 18px;
  border-radius: 16px;
  background: color-mix(in oklch,var(--ft-21-gold) 13%,transparent);
  border: 1px solid color-mix(in oklch,var(--ft-21-gold) 34%,transparent);
}

.ft-21__rating {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
}

.ft-21__stars {
  font-size: 19px;
  letter-spacing: .1em;
  background: linear-gradient(90deg,var(--ft-21-gold) var(--ft-21-pct),oklch(0.25 0.03 55/.2) var(--ft-21-pct));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.ft-21__rtext {
  font-size: 13.6px;
  color: var(--ft-21-mut);
}

.ft-21__rtext strong {
  color: var(--ft-21-ink);
  font-weight: 700;
}

.ft-21__rlink {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 40px;
  margin-inline-start: auto;
  font-size: 13.4px;
  font-weight: 650;
  color: var(--ft-21-acc);
  text-decoration: none;
}

.ft-21__rlink:hover {
  text-decoration: underline;
  text-underline-offset: .25em;
}

.ft-21__rlink:hover svg {
  translate: 3px 0;
}

.ft-21__rlink svg {
  transition: translate .2s ease;
}

.ft-21__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: clamp(22px,3vw,36px) clamp(16px,2.2vw,28px);
  padding-block: clamp(24px,3.4vw,40px);
  border-top: 1px solid var(--ft-21-line);
}

.ft-21__brandcol {
  display: grid;
  align-content: start;
  gap: 10px;
  min-width: 0;
}

.ft-21__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ft-21__mark {
  width: 24px;
  height: 24px;
  border-radius: 8px;
  background: linear-gradient(150deg,var(--ft-21-acc),var(--ft-21-gold));
}

.ft-21__blurb {
  font-size: 14px;
  line-height: 1.55;
  color: var(--ft-21-mut);
  max-width: 28ch;
}

.ft-21__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-21__ch {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  margin-block-end: 8px;
}

.ft-21__list {
  display: grid;
  gap: 1px;
}

.ft-21__link {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  font-size: 14.2px;
  color: var(--ft-21-mut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease;
}

.ft-21__link:hover {
  color: var(--ft-21-acc);
  text-decoration: underline;
  text-underline-offset: .25em;
}

.ft-21__link:focus-visible,
.ft-21__inline:focus-visible,
.ft-21__rlink:focus-visible {
  outline: 2px solid var(--ft-21-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.ft-21__copy {
  padding-block: 18px;
  padding-bottom: calc(18px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-21-line);
  font-size: 12.6px;
  color: var(--ft-21-mut);
}

@media (prefers-contrast: more) {
  .ft-21__badge,
    .ft-21__reviews {
    border-width: 2px;
    border-color: currentColor;
  }

  .ft-21__proof,
    .ft-21__rtext,
    .ft-21__copy,
    .ft-21__blurb {
    color: var(--ft-21-ink);
  }
}

@media (max-width: 620px) {
  .ft-21__seal {
    margin-inline-start: 0;
  }

  .ft-21__rlink {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-21 * {
    transition-duration: .01ms !important;
  }
}
```

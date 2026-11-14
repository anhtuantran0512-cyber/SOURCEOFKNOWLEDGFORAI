---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/minimal-white-cards/"
title: "Clean White Quote Card Grid"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "The universal one — the card grid that drops into any light-mode site without a fight."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clean White Quote Card Grid
Source: https://codefronts.com/components/css-testimonials-reviews/minimal-white-cards/

The universal one — the card grid that drops into any light-mode site without a fight. Its value is entirely in the details most implementations get wrong: a layered two-part shadow instead of a single blur, equal-height cards with bottom-pinned attribution, an auto-fit grid with no media queries, and a hover that changes elevation rather than colour.
## HTML
```html
<section class="tr-23" aria-label="Clean white quote card grid demo">
  <div class="tr-23__stage">
    <header class="tr-23__head">
      <p class="tr-23__eyebrow">Customer feedback</p>
      <h2 class="tr-23__title">The one you will actually reuse</h2>
      <p class="tr-23__sub">Six cards, one grid declaration, no media queries and no framework.</p>
    </header>

    <div class="tr-23__grid">
      <figure class="tr-23__card">
        <div class="tr-23__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
        <blockquote>Setup took twenty minutes and the first report was useful immediately. I keep waiting for the catch.</blockquote>
        <figcaption class="tr-23__who">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Priya Raghunathan" width="42" height="42" loading="lazy" decoding="async">
          <span><b>Priya Raghunathan</b>Staff Engineer, Northwind</span>
        </figcaption>
      </figure>

      <figure class="tr-23__card">
        <div class="tr-23__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
        <blockquote>We compared four vendors on a spreadsheet with eighty rows. This one won on the eleven rows that turned out to matter.</blockquote>
        <figcaption class="tr-23__who">
          <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Marcus Yeung" width="42" height="42" loading="lazy" decoding="async">
          <span><b>Marcus Yeung</b>Director of Risk, Halden</span>
        </figcaption>
      </figure>

      <figure class="tr-23__card tr-23__card--feature">
        <div class="tr-23__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
        <blockquote>Six months in, the thing I would tell another buyer is that nothing broke. That is a boring sentence and it is the entire reason we renewed.</blockquote>
        <figcaption class="tr-23__who">
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Grace Whitlock" width="42" height="42" loading="lazy" decoding="async">
          <span><b>Grace Whitlock</b>Design Systems Lead, Auryn</span>
        </figcaption>
      </figure>

      <figure class="tr-23__card">
        <div class="tr-23__stars" role="img" aria-label="Rated 4 out of 5">★★★★<span>★</span></div>
        <blockquote>The mobile app trails the web app by a release or two. Everything else has been exactly as promised.</blockquote>
        <figcaption class="tr-23__who">
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Dan Reyes" width="42" height="42" loading="lazy" decoding="async">
          <span><b>Dan Reyes</b>VP Infrastructure, Portside</span>
        </figcaption>
      </figure>

      <figure class="tr-23__card">
        <div class="tr-23__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
        <blockquote>Our finance team asked for one export format. It shipped in the next release with a changelog entry crediting them by name.</blockquote>
        <figcaption class="tr-23__who">
          <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Hana Sørensen" width="42" height="42" loading="lazy" decoding="async">
          <span><b>Hana Sørensen</b>Product Manager, Blomst</span>
        </figcaption>
      </figure>

      <figure class="tr-23__card">
        <div class="tr-23__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</div>
        <blockquote>I have onboarded three teams onto it now and have never once had to write a how-to document.</blockquote>
        <figcaption class="tr-23__who">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Nia Osei" width="42" height="42" loading="lazy" decoding="async">
          <span><b>Nia Osei</b>Ops Lead, Fieldwork</span>
        </figcaption>
      </figure>
    </div>
    <p class="tr-23__chip" aria-hidden="true">auto-fit minmax(min(100%,290px),1fr) · layered contact + ambient shadow · margin-block-start:auto footer</p>
  </div>
</section>
```
## CSS
```css
.tr-23,
.tr-23 *,
.tr-23 *::before,
.tr-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-23-bg: oklch(0.973 0.004 250);
  --tr-23-card: oklch(1 0 0);
  --tr-23-ink: oklch(0.22 0.015 255);
  --tr-23-mut: oklch(0.54 0.015 255);
  --tr-23-acc: oklch(0.55 0.17 260);
  --tr-23-star: oklch(0.77 0.16 74);
  background: var(--tr-23-bg);
  color: var(--tr-23-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-23__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,34px);
  padding: clamp(20px,4vw,58px);
}

.tr-23__head {
  text-align: center;
  display: grid;
  gap: 9px;
  max-width: 52ch;
}

.tr-23__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tr-23-acc);
}

.tr-23__title {
  font-size: clamp(25px,4vw,42px);
  font-weight: 670;
  letter-spacing: -.038em;
  line-height: 1.1;
  text-wrap: balance;
}

.tr-23__sub {
  font-size: 14.5px;
  line-height: 1.55;
  color: var(--tr-23-mut);
  text-wrap: pretty;
}

.tr-23__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,290px),1fr));
  gap: clamp(14px,2vw,20px);
  width: min(100%,1120px);
}

.tr-23__card {
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: clamp(20px,2.4vw,26px);
  background: var(--tr-23-card);
  border: 1px solid oklch(0 0 0/.06);
  border-radius: 16px;
  box-shadow: 0 1px 2px oklch(0.3 0.03 255/.06),0 12px 28px -16px oklch(0.3 0.05 255/.35);
  animation: tr-23-in .65s cubic-bezier(.16,1,.3,1) both;
  transition: box-shadow .3s,translate .3s cubic-bezier(.16,1,.3,1);
}

.tr-23__card:nth-child(2) {
  animation-delay: .06s;
}

.tr-23__card:nth-child(3) {
  animation-delay: .12s;
}

.tr-23__card:nth-child(4) {
  animation-delay: .18s;
}

.tr-23__card:nth-child(5) {
  animation-delay: .24s;
}

.tr-23__card:nth-child(6) {
  animation-delay: .3s;
}

@keyframes tr-23-in {
  from {
    opacity: 0;
    translate: 0 14px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-23__card:hover {
  translate: 0 -3px;
  box-shadow: 0 2px 4px oklch(0.3 0.03 255/.07),0 24px 46px -20px oklch(0.3 0.05 255/.4);
}

.tr-23__card--feature {
  background: linear-gradient(165deg,color-mix(in oklch,var(--tr-23-acc) 7%,var(--tr-23-card)),var(--tr-23-card) 72%);
  border-color: color-mix(in oklch,var(--tr-23-acc) 22%,transparent);
}

.tr-23__stars {
  font-size: 14px;
  letter-spacing: 2px;
  color: var(--tr-23-star);
}

.tr-23__stars span {
  color: oklch(0 0 0/.14);
}

.tr-23__card blockquote {
  font-size: 15px;
  line-height: 1.6;
  letter-spacing: -.012em;
  color: color-mix(in oklch,var(--tr-23-ink) 90%,transparent);
  text-wrap: pretty;
}

.tr-23__who {
  display: flex;
  align-items: center;
  gap: 11px;
  margin-block-start: auto;
  padding-top: 15px;
  border-top: 1px solid oklch(0 0 0/.07);
}

.tr-23__who img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: oklch(0.9 0.015 255);
}

.tr-23__who span {
  display: grid;
  font-size: 11.5px;
  line-height: 1.35;
  color: var(--tr-23-mut);
}

.tr-23__who b {
  font-size: 13.5px;
  font-weight: 640;
  color: var(--tr-23-ink);
  letter-spacing: -.012em;
}

.tr-23__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-23-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.11);
  border-radius: 99px;
  text-align: center;
  background: var(--tr-23-card);
}

@media (prefers-reduced-motion: reduce) {
  .tr-23__card {
    animation: none;
    transition: none;
  }
}
```

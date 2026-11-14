---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/wall-of-love-testimonial-grid-css-columns/"
title: "Wall of Love Testimonial Grid (CSS Columns)"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "The high-density \"wall of love\" every indie SaaS ships once it has more praise than a carousel can hold — variable-height quote cards packed into a true…"
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Wall of Love Testimonial Grid (CSS Columns)
Source: https://codefronts.com/components/css-testimonials-reviews/wall-of-love-testimonial-grid-css-columns/

The high-density "wall of love" every indie SaaS ships once it has more praise than a carousel can hold — variable-height quote cards packed into a true masonry rhythm by column-count, with zero JavaScript and zero layout shift. The filter chips are pure CSS too: radio inputs plus a :has() rule on the root, so switching between Product, Support and Migration quotes never touches the main thread.
## HTML
```html
<section class="tr-01" aria-label="Wall of love testimonial grid demo">
  <div class="tr-01__stage">
    <header class="tr-01__head">
      <p class="tr-01__eyebrow">Wall of love</p>
      <h2 class="tr-01__title">4,180 teams have said it better than we could</h2>
      <div class="tr-01__filters" role="group" aria-label="Filter testimonials by topic">
        <input class="tr-01__sr" type="radio" name="tr-01-f" id="tr-01-all" checked>
        <label class="tr-01__chip" for="tr-01-all">Everything <span>9</span></label>
        <input class="tr-01__sr" type="radio" name="tr-01-f" id="tr-01-product">
        <label class="tr-01__chip" for="tr-01-product">Product <span>4</span></label>
        <input class="tr-01__sr" type="radio" name="tr-01-f" id="tr-01-support">
        <label class="tr-01__chip" for="tr-01-support">Support <span>3</span></label>
        <input class="tr-01__sr" type="radio" name="tr-01-f" id="tr-01-migration">
        <label class="tr-01__chip" for="tr-01-migration">Migration <span>2</span></label>
      </div>
    </header>

    <div class="tr-01__wall">
      <figure class="tr-01__card" data-src="product" style="--tr-01-i:0">
        <div class="tr-01__stars" role="img" aria-label="Rated 5 out of 5">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
        </div>
        <blockquote class="tr-01__quote"><p>We replaced three internal dashboards with one board and the weekly status meeting just… stopped happening. Nobody misses it.</p></blockquote>
        <figcaption class="tr-01__who">
          <img class="tr-01__ava" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Priya Raghunathan" width="40" height="40" loading="lazy" decoding="async">
          <span><b>Priya Raghunathan</b>Staff Engineer, Northwind</span>
        </figcaption>
      </figure>

      <figure class="tr-01__card" data-src="support" style="--tr-01-i:1">
        <div class="tr-01__stars" role="img" aria-label="Rated 5 out of 5">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
        </div>
        <blockquote class="tr-01__quote"><p>Raised a Sev-2 at 04:10 GMT. A human answered in nine minutes with a patch branch attached. That is not a support team, that is insurance.</p></blockquote>
        <figcaption class="tr-01__who">
          <img class="tr-01__ava" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Callum Doyle" width="40" height="40" loading="lazy" decoding="async">
          <span><b>Callum Doyle</b>Head of Platform, Meridian</span>
        </figcaption>
      </figure>

      <figure class="tr-01__card tr-01__card--accent" data-src="migration" style="--tr-01-i:2">
        <div class="tr-01__stars" role="img" aria-label="Rated 5 out of 5">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
        </div>
        <blockquote class="tr-01__quote"><p>Nineteen years of legacy records moved in a weekend. Monday morning nobody in the building could tell anything had changed — which was exactly the brief.</p></blockquote>
        <figcaption class="tr-01__who">
          <img class="tr-01__ava" src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Alessandra Rossi" width="40" height="40" loading="lazy" decoding="async">
          <span><b>Alessandra Rossi</b>CTO, Vaultline Financial</span>
        </figcaption>
      </figure>

      <figure class="tr-01__card" data-src="product" style="--tr-01-i:3">
        <div class="tr-01__stars" role="img" aria-label="Rated 4 out of 5">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg class="tr-01__off" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
        </div>
        <blockquote class="tr-01__quote"><p>The audit trail alone justified the line item. Compliance stopped filing tickets and started filing praise.</p></blockquote>
        <figcaption class="tr-01__who">
          <img class="tr-01__ava" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Marcus Yeung" width="40" height="40" loading="lazy" decoding="async">
          <span><b>Marcus Yeung</b>Director of Risk, Halden Group</span>
        </figcaption>
      </figure>

      <figure class="tr-01__card" data-src="support" style="--tr-01-i:4">
        <div class="tr-01__stars" role="img" aria-label="Rated 5 out of 5">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
        </div>
        <blockquote class="tr-01__quote"><p>Onboarding took an afternoon, not a quarter.</p></blockquote>
        <figcaption class="tr-01__who">
          <img class="tr-01__ava" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Nia Osei" width="40" height="40" loading="lazy" decoding="async">
          <span><b>Nia Osei</b>Ops Lead, Fieldwork</span>
        </figcaption>
      </figure>

      <figure class="tr-01__card" data-src="product" style="--tr-01-i:5">
        <div class="tr-01__stars" role="img" aria-label="Rated 5 out of 5">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
        </div>
        <blockquote class="tr-01__quote"><p>Our design system finally has a home that engineers actually open. Adoption went from polite nodding to 94% of merged PRs referencing a token.</p></blockquote>
        <figcaption class="tr-01__who">
          <img class="tr-01__ava" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Grace Whitlock" width="40" height="40" loading="lazy" decoding="async">
          <span><b>Grace Whitlock</b>Design Systems Lead, Auryn</span>
        </figcaption>
      </figure>

      <figure class="tr-01__card" data-src="migration" style="--tr-01-i:6">
        <div class="tr-01__stars" role="img" aria-label="Rated 4 out of 5">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg class="tr-01__off" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
        </div>
        <blockquote class="tr-01__quote"><p>Two data centres, four time zones, one rollback plan we never had to use.</p></blockquote>
        <figcaption class="tr-01__who">
          <img class="tr-01__ava" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Dan Reyes" width="40" height="40" loading="lazy" decoding="async">
          <span><b>Dan Reyes</b>VP Infrastructure, Portside</span>
        </figcaption>
      </figure>

      <figure class="tr-01__card" data-src="support" style="--tr-01-i:7">
        <div class="tr-01__stars" role="img" aria-label="Rated 5 out of 5">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
        </div>
        <blockquote class="tr-01__quote"><p>They shipped the feature I asked for in a Friday email. On Tuesday. With docs.</p></blockquote>
        <figcaption class="tr-01__who">
          <img class="tr-01__ava" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Hana Sørensen" width="40" height="40" loading="lazy" decoding="async">
          <span><b>Hana Sørensen</b>Product Manager, Blomst</span>
        </figcaption>
      </figure>

      <figure class="tr-01__card" data-src="product" style="--tr-01-i:8">
        <div class="tr-01__stars" role="img" aria-label="Rated 5 out of 5">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg>
        </div>
        <blockquote class="tr-01__quote"><p>Renewal was a fifteen-minute conversation because the usage report argued for itself. Our CFO has never approved anything that fast.</p></blockquote>
        <figcaption class="tr-01__who">
          <img class="tr-01__ava" src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=120&h=120&fit=crop&auto=format" alt="Portrait of Erin McAllister" width="40" height="40" loading="lazy" decoding="async">
          <span><b>Erin McAllister</b>COO, Larkfield Health</span>
        </figcaption>
      </figure>
    </div>

    <p class="tr-01__chip" aria-hidden="true">column-count · break-inside:avoid · :has() filtering · figure/blockquote semantics</p>
  </div>
</section>
```
## CSS
```css
.tr-01,
.tr-01 *,
.tr-01 *::before,
.tr-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-01-bg: oklch(0.97 0.012 85);
  --tr-01-card: oklch(1 0 0);
  --tr-01-ink: oklch(0.24 0.02 60);
  --tr-01-mut: oklch(0.55 0.02 60);
  --tr-01-acc: oklch(0.62 0.19 28);
  --tr-01-star: oklch(0.76 0.16 72);
  background: var(--tr-01-bg);
  color: var(--tr-01-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,30px);
  padding: clamp(22px,5vw,64px);
  background: radial-gradient(120% 60% at 50% -10%,color-mix(in oklch,var(--tr-01-acc) 12%,transparent),transparent 60%);
}

.tr-01__head {
  width: min(100%,1120px);
  display: grid;
  justify-items: center;
  gap: 14px;
  text-align: center;
}

.tr-01__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tr-01-acc);
}

.tr-01__title {
  font-size: clamp(25px,4vw,44px);
  font-weight: 670;
  line-height: 1.08;
  letter-spacing: -.035em;
  text-wrap: balance;
  max-width: 20ch;
}

.tr-01__filters {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
  margin-top: 4px;
}

.tr-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.tr-01__chip:is(label) {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 99px;
  border: 1px solid oklch(0 0 0/.12);
  background: var(--tr-01-card);
  font-size: 13.5px;
  font-weight: 560;
  cursor: pointer;
  user-select: none;
  transition: background .22s,color .22s,border-color .22s,transform .22s cubic-bezier(.16,1,.3,1);
}

.tr-01__chip span {
  font-size: 11px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 99px;
  background: oklch(0 0 0/.06);
  color: var(--tr-01-mut);
}

.tr-01__chip:hover {
  transform: translateY(-1px);
  border-color: color-mix(in oklch,var(--tr-01-acc) 45%,transparent);
}

.tr-01__sr:checked+.tr-01__chip {
  background: var(--tr-01-ink);
  color: oklch(0.99 0 0);
  border-color: var(--tr-01-ink);
}

.tr-01__sr:checked+.tr-01__chip span {
  background: oklch(1 0 0/.18);
  color: oklch(1 0 0/.85);
}

.tr-01__sr:focus-visible+.tr-01__chip {
  outline: 3px solid var(--tr-01-acc);
  outline-offset: 3px;
}

.tr-01__wall {
  width: min(100%,1120px);
  column-count: 3;
  column-gap: 18px;
}

@media (max-width: 900px) {
  .tr-01__wall {
    column-count: 2;
  }
}

@media (max-width: 620px) {
  .tr-01__wall {
    column-count: 1;
  }
}

.tr-01__card {
  break-inside: avoid;
  -webkit-column-break-inside: avoid;
  margin-bottom: 18px;
  padding: 22px 22px 20px;
  border-radius: 18px;
  background: var(--tr-01-card);
  border: 1px solid oklch(0 0 0/.07);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 12px 28px -18px oklch(0.3 0.06 60/.5);
  animation: tr-01-in .7s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(var(--tr-01-i,0)*70ms);
  transition: box-shadow .3s,translate .3s cubic-bezier(.16,1,.3,1),border-color .3s;
}

.tr-01__card:hover {
  translate: 0 -3px;
  border-color: color-mix(in oklch,var(--tr-01-acc) 35%,transparent);
  box-shadow: 0 2px 4px oklch(0 0 0/.05),0 22px 44px -22px oklch(0.3 0.06 60/.6);
}

.tr-01__card--accent {
  background: linear-gradient(165deg,color-mix(in oklch,var(--tr-01-acc) 13%,var(--tr-01-card)),var(--tr-01-card) 70%);
  border-color: color-mix(in oklch,var(--tr-01-acc) 30%,transparent);
}

@keyframes tr-01-in {
  from {
    opacity: 0;
    translate: 0 16px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-01__stars {
  display: flex;
  gap: 2px;
  margin-bottom: 12px;
}

.tr-01__stars svg {
  width: 15px;
  height: 15px;
  fill: var(--tr-01-star);
}

.tr-01__off {
  fill: oklch(0 0 0/.13);
}

.tr-01__quote p {
  font-size: 15.5px;
  line-height: 1.55;
  letter-spacing: -.012em;
  text-wrap: pretty;
  color: color-mix(in oklch,var(--tr-01-ink) 92%,transparent);
}

.tr-01__who {
  display: flex;
  align-items: center;
  gap: 11px;
  margin-top: 18px;
  padding-top: 15px;
  border-top: 1px solid oklch(0 0 0/.07);
}

.tr-01__ava {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  background: linear-gradient(135deg,oklch(0.85 0.05 60),oklch(0.75 0.08 28));
  flex: none;
}

.tr-01__who span {
  display: grid;
  font-size: 12.5px;
  line-height: 1.35;
  color: var(--tr-01-mut);
}

.tr-01__who b {
  font-size: 14px;
  font-weight: 640;
  color: var(--tr-01-ink);
  letter-spacing: -.01em;
}

.tr-01:has(#tr-01-product:checked) .tr-01__card:not([data-src='product']),
.tr-01:has(#tr-01-support:checked) .tr-01__card:not([data-src='support']),
.tr-01:has(#tr-01-migration:checked) .tr-01__card:not([data-src='migration']) {
  display: none;
}

.tr-01__chip:not(label) {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-01-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.11);
  border-radius: 99px;
  background: color-mix(in oklch,var(--tr-01-card) 60%,transparent);
}

@media (prefers-reduced-motion: reduce) {
  .tr-01__card {
    animation: none;
  }

  .tr-01__card:hover {
    translate: none;
  }
}
```

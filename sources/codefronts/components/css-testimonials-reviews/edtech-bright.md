---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/edtech-bright/"
title: "Student Course Review Card with Rating"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Built for EdTech, where a review is only credible if you can see how much of the course the reviewer actually finished."
has_js: "true"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Student Course Review Card with Rating
Source: https://codefronts.com/components/css-testimonials-reviews/edtech-bright/

Built for EdTech, where a review is only credible if you can see how much of the course the reviewer actually finished. This card pairs the rating with a completion ring, a cohort tag, an instructor reply thread and a working star-rating input — the interactive kind students use to leave the review in the first place.
## HTML
```html
<section class="tr-18" aria-label="Student course review card with rating demo">
  <div class="tr-18__stage">
    <article class="tr-18__card">
      <header class="tr-18__top">
        <div class="tr-18__course">
          <p class="tr-18__kicker">Course review</p>
          <h2>Systems Design for Working Engineers</h2>
          <p class="tr-18__meta">14 modules · 26 hours · Cohort AU-Autumn 26</p>
        </div>
        <div class="tr-18__ring" style="--tr-18-p:96" role="img" aria-label="96 percent of the course completed">
          <span><b>96</b>%</span>
        </div>
      </header>

      <figure class="tr-18__rev">
        <div class="tr-18__who">
          <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Hana Sørensen" width="46" height="46" loading="lazy" decoding="async">
          <div>
            <b>Hana Sørensen</b>
            <span>Backend engineer · 4 years experience</span>
          </div>
          <span class="tr-18__stars" role="img" aria-label="Rated 5 out of 5">★★★★★</span>
        </div>
        <blockquote>Module 9 alone was worth the fee. I had been hand-waving through consistency models for years and it took ninety minutes of this to fix that. The exercises are hard in the right way — you cannot pass them by watching.</blockquote>
        <ul class="tr-18__pills">
          <li>Pace: <b>Just right</b></li>
          <li>Difficulty: <b>Challenging</b></li>
          <li>Would recommend: <b>Yes</b></li>
        </ul>

        <figure class="tr-18__reply">
          <p class="tr-18__rlabel"><b>Reply from the instructor</b> · Dr. Aoife Brennan</p>
          <blockquote>Thank you Hana — module 9 gets rewritten every intake and this cohort got the version with the failure-injection lab. Glad it landed.</blockquote>
        </figure>

        <footer class="tr-18__f"><time datetime="2026-06-30">30 June 2026</time> · Verified enrolment · Completed 96%</footer>
      </figure>

      <div class="tr-18__rateblock">
        <p class="tr-18__rtitle">Finished the course? Leave your rating</p>
        <div class="tr-18__rate" role="radiogroup" aria-label="Rate this course from 1 to 5 stars">
          <input type="radio" name="tr-18-r" id="tr-18-r5" value="5"><label for="tr-18-r5"><span class="tr-18__sr">Rate 5 out of 5</span><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg></label>
          <input type="radio" name="tr-18-r" id="tr-18-r4" value="4"><label for="tr-18-r4"><span class="tr-18__sr">Rate 4 out of 5</span><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg></label>
          <input type="radio" name="tr-18-r" id="tr-18-r3" value="3"><label for="tr-18-r3"><span class="tr-18__sr">Rate 3 out of 5</span><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg></label>
          <input type="radio" name="tr-18-r" id="tr-18-r2" value="2"><label for="tr-18-r2"><span class="tr-18__sr">Rate 2 out of 5</span><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg></label>
          <input type="radio" name="tr-18-r" id="tr-18-r1" value="1"><label for="tr-18-r1"><span class="tr-18__sr">Rate 1 out of 5</span><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.6l2.6 5.3 5.8.8-4.2 4.1 1 5.8L10 14.9 4.8 17.6l1-5.8L1.6 7.7l5.8-.8z"/></svg></label>
        </div>
        <p class="tr-18__out" aria-live="polite">No rating selected yet</p>
      </div>
    </article>
    <p class="tr-18__chip" aria-hidden="true">conic-gradient + radial mask ring · reversed radio star input · role=radiogroup · aria-live summary</p>
  </div>
</section>
```
## CSS
```css
.tr-18,
.tr-18 *,
.tr-18 *::before,
.tr-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-18-bg: oklch(0.96 0.014 270);
  --tr-18-card: oklch(1 0 0);
  --tr-18-ink: oklch(0.23 0.02 270);
  --tr-18-mut: oklch(0.54 0.02 270);
  --tr-18-acc: oklch(0.55 0.2 285);
  --tr-18-star: oklch(0.76 0.16 72);
  --tr-18-track: oklch(0.9 0.015 270);
  background: var(--tr-18-bg);
  color: var(--tr-18-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,52px);
}

.tr-18__card {
  width: min(100%,720px);
  background: var(--tr-18-card);
  border: 1px solid oklch(0 0 0/.07);
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 30px 60px -36px oklch(0.3 0.06 270/.7);
  animation: tr-18-in .75s cubic-bezier(.16,1,.3,1) both;
}

@keyframes tr-18-in {
  from {
    opacity: 0;
    translate: 0 18px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-18__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
  padding: clamp(20px,3vw,28px);
  background: linear-gradient(150deg,color-mix(in oklch,var(--tr-18-acc) 12%,var(--tr-18-card)),var(--tr-18-card) 70%);
  border-bottom: 1px solid oklch(0 0 0/.07);
}

.tr-18__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tr-18-acc);
}

.tr-18__course h2 {
  margin-top: 6px;
  font-size: clamp(19px,2.6vw,25px);
  font-weight: 670;
  letter-spacing: -.03em;
  line-height: 1.2;
  text-wrap: balance;
}

.tr-18__meta {
  margin-top: 6px;
  font-size: 12.5px;
  color: var(--tr-18-mut);
}

.tr-18__ring {
  position: relative;
  inline-size: 86px;
  block-size: 86px;
  flex: none;
  border-radius: 50%;
  background: conic-gradient(var(--tr-18-acc) calc(var(--tr-18-p,0)*1%),var(--tr-18-track) 0);
  -webkit-mask: radial-gradient(farthest-side,transparent 68%,#000 69%);
  mask: radial-gradient(farthest-side,transparent 68%,#000 69%);
  animation: tr-18-fill 1.4s cubic-bezier(.16,1,.3,1) both;
  animation-delay: .25s;
}

@keyframes tr-18-fill {
  from {
    background: conic-gradient(var(--tr-18-acc) 0%,var(--tr-18-track) 0);
  }
}

.tr-18__ring span {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  -webkit-mask: none;
  mask: none;
  font-size: 11px;
  color: var(--tr-18-mut);
  font-variant-numeric: tabular-nums;
}

.tr-18__ring b {
  font-size: 20px;
  font-weight: 720;
  letter-spacing: -.035em;
  color: var(--tr-18-ink);
}

.tr-18__rev {
  padding: clamp(20px,3vw,28px);
  display: grid;
  gap: 15px;
}

.tr-18__who {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.tr-18__who img {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  box-shadow: 0 0 0 2px var(--tr-18-card),0 0 0 4px color-mix(in oklch,var(--tr-18-acc) 45%,transparent);
}

.tr-18__who div {
  display: grid;
  gap: 2px;
}

.tr-18__who b {
  font-size: 15px;
  font-weight: 650;
  letter-spacing: -.015em;
}

.tr-18__who span {
  font-size: 12px;
  color: var(--tr-18-mut);
}

.tr-18__stars {
  margin-inline-start: auto;
  font-size: 16px;
  letter-spacing: 2px;
  color: var(--tr-18-star);
}

.tr-18__rev>blockquote {
  font-size: 15.5px;
  line-height: 1.62;
  color: color-mix(in oklch,var(--tr-18-ink) 91%,transparent);
  text-wrap: pretty;
}

.tr-18__pills {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tr-18__pills li {
  padding: 6px 12px;
  border-radius: 9px;
  background: oklch(0 0 0/.045);
  border: 1px solid oklch(0 0 0/.05);
  font-size: 12px;
  color: var(--tr-18-mut);
}

.tr-18__pills b {
  color: var(--tr-18-ink);
  font-weight: 640;
}

.tr-18__reply {
  padding: 16px 18px;
  border-radius: 14px;
  border-inline-start: 3px solid var(--tr-18-acc);
  background: color-mix(in oklch,var(--tr-18-acc) 7%,transparent);
}

.tr-18__rlabel {
  font-size: 12px;
  color: var(--tr-18-mut);
}

.tr-18__rlabel b {
  color: color-mix(in oklch,var(--tr-18-acc) 80%,black);
  font-weight: 680;
}

.tr-18__reply blockquote {
  margin-top: 8px;
  font-size: 14px;
  line-height: 1.55;
  color: color-mix(in oklch,var(--tr-18-ink) 88%,transparent);
  text-wrap: pretty;
}

.tr-18__f {
  font-size: 11.5px;
  color: var(--tr-18-mut);
  padding-top: 6px;
}

.tr-18__rateblock {
  padding: clamp(18px,3vw,24px) clamp(20px,3vw,28px);
  border-top: 1px solid oklch(0 0 0/.07);
  background: color-mix(in oklch,var(--tr-18-acc) 4%,var(--tr-18-card));
  display: grid;
  gap: 10px;
  justify-items: start;
}

.tr-18__rtitle {
  font-size: 13.5px;
  font-weight: 620;
  letter-spacing: -.01em;
}

.tr-18__rate {
  display: flex;
  flex-direction: row-reverse;
  justify-content: flex-end;
  gap: 2px;
}

.tr-18__rate input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.tr-18__rate label {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  cursor: pointer;
  color: var(--tr-18-track);
  transition: color .18s,scale .18s cubic-bezier(.16,1,.3,1);
}

.tr-18__rate label svg {
  width: 28px;
  height: 28px;
  fill: currentColor;
}

.tr-18__rate input:checked~label,
.tr-18__rate label:hover,
.tr-18__rate label:hover~label {
  color: var(--tr-18-star);
}

.tr-18__rate label:hover {
  scale: 1.14;
}

.tr-18__rate input:focus-visible+label {
  outline: 3px solid var(--tr-18-acc);
  outline-offset: -2px;
  border-radius: 10px;
}

.tr-18__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.tr-18__out {
  font-size: 12.5px;
  color: var(--tr-18-mut);
  font-variant-numeric: tabular-nums;
}

.tr-18__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-18-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.6);
}

@media (prefers-reduced-motion: reduce) {
  .tr-18__card,
    .tr-18__ring {
    animation: none;
  }

  .tr-18__rate label {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tr-18 .tr-18__rate').forEach((group) => {
    if (group.dataset.wired) return;
    group.dataset.wired = '1';
    const out = group.parentElement.querySelector('.tr-18__out');
    const words = { 1: 'Not for me', 2: 'Mixed', 3: 'Solid', 4: 'Really good', 5: 'Excellent' };
    group.addEventListener('change', (e) => {
      const v = e.target.value;
      out.textContent = 'You rated this ' + v + ' out of 5 — ' + words[v] + '.';
    });
  });
})();
```

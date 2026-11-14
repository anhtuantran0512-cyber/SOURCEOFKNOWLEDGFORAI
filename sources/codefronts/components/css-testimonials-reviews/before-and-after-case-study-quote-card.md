---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/before-and-after-case-study-quote-card/"
title: "Before & After Case Study Quote Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "The layout agencies and B2B consultancies convert on: a client quote sitting shoulder to shoulder with the numbers that back it up."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Before & After Case Study Quote Card
Source: https://codefronts.com/components/css-testimonials-reviews/before-and-after-case-study-quote-card/

The layout agencies and B2B consultancies convert on: a client quote sitting shoulder to shoulder with the numbers that back it up. The delta figures count up on load using @property plus counter() — genuine style-engine interpolation, no JavaScript — and the before/after rows use a diagonal strike so the improvement is legible in one glance.
## HTML
```html
<section class="tr-07" aria-label="Before and after case study quote card demo">
  <div class="tr-07__stage">
    <article class="tr-07__card">
      <div class="tr-07__quote">
        <p class="tr-07__tag">Case study · D2C retail</p>
        <span class="tr-07__mark" aria-hidden="true">“</span>
        <blockquote>
          <p>We had eleven tools and no answers. Nine weeks later we had one pipeline, and the forecast was accurate enough that we stopped hedging inventory. That is the whole story — the rest is arithmetic.</p>
        </blockquote>
        <figcaption class="tr-07__who">
          <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Nathan Boateng" width="52" height="52" loading="lazy" decoding="async">
          <span><b>Nathan Boateng</b>Chief Revenue Officer · Coplandt &amp; Sons</span>
        </figcaption>
        <p class="tr-07__foot">Measured Jan–Sep 2026 against the preceding nine months. Methodology in the full case study.</p>
      </div>

      <div class="tr-07__stats">
        <div class="tr-07__stat">
          <b class="tr-07__big" data-k="a"><span class="tr-07__pre">+</span><span class="tr-07__n" aria-hidden="true"></span><span class="tr-07__suf">%</span></b>
          <span class="tr-07__sr">Plus 310 percent</span>
          <p>Monthly recurring revenue</p>
        </div>
        <div class="tr-07__stat">
          <b class="tr-07__big" data-k="b"><span class="tr-07__pre">−</span><span class="tr-07__n" aria-hidden="true"></span><span class="tr-07__suf">%</span></b>
          <span class="tr-07__sr">Minus 64 percent</span>
          <p>Cost per acquisition</p>
        </div>

        <dl class="tr-07__rows">
          <div>
            <dt>Time to forecast</dt>
            <dd class="tr-07__old">9 days</dd>
            <dd class="tr-07__new">40 min</dd>
          </div>
          <div>
            <dt>Tools in the stack</dt>
            <dd class="tr-07__old">11</dd>
            <dd class="tr-07__new">3</dd>
          </div>
          <div>
            <dt>Stockouts per quarter</dt>
            <dd class="tr-07__old">27</dd>
            <dd class="tr-07__new">2</dd>
          </div>
          <div>
            <dt>Analyst hours / week</dt>
            <dd class="tr-07__old">62</dd>
            <dd class="tr-07__new">9</dd>
          </div>
        </dl>
      </div>
    </article>
    <p class="tr-07__chip" aria-hidden="true">@property &lt;integer&gt; · counter-reset var() · content:counter() · grid rails · tabular-nums</p>
  </div>
</section>
```
## CSS
```css
@property --tr-07-a {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@property --tr-07-b {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.tr-07,
.tr-07 *,
.tr-07 *::before,
.tr-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-07-bg: oklch(0.21 0.032 268);
  --tr-07-card: oklch(0.98 0.006 250);
  --tr-07-ink: oklch(0.22 0.02 265);
  --tr-07-mut: oklch(0.54 0.02 265);
  --tr-07-acc: oklch(0.68 0.17 155);
  background: var(--tr-07-bg);
  color: var(--tr-07-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(18px,4vw,54px);
  background: radial-gradient(85% 60% at 20% 0%,color-mix(in oklch,var(--tr-07-acc) 16%,transparent),transparent 62%);
}

.tr-07__card {
  container-type: inline-size;
  width: min(100%,1020px);
  display: grid;
  background: var(--tr-07-card);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 40px 90px -50px oklch(0 0 0/.85);
  animation: tr-07-in .8s cubic-bezier(.16,1,.3,1) both;
}

@keyframes tr-07-in {
  from {
    opacity: 0;
    translate: 0 22px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

@container (min-width: 760px) {
  .tr-07__card {
    grid-template-columns: 1.15fr .85fr;
  }
}

.tr-07__quote {
  position: relative;
  padding: clamp(26px,4cqi,44px);
  display: grid;
  align-content: center;
  gap: 20px;
}

.tr-07__tag {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--tr-07-acc) 72%,black);
}

.tr-07__mark {
  position: absolute;
  inset-block-start: clamp(6px,2cqi,18px);
  inset-inline-end: clamp(14px,3cqi,34px);
  font-family: Georgia,'Times New Roman',serif;
  font-size: clamp(120px,18cqi,190px);
  line-height: 1;
  color: color-mix(in oklch,var(--tr-07-acc) 16%,transparent);
  pointer-events: none;
}

.tr-07__quote blockquote p {
  font-size: clamp(18px,2.5cqi,25px);
  line-height: 1.42;
  letter-spacing: -.028em;
  font-weight: 520;
  text-wrap: pretty;
  position: relative;
}

.tr-07__who {
  display: flex;
  align-items: center;
  gap: 13px;
}

.tr-07__who img {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: oklch(0.86 0.02 250);
}

.tr-07__who span {
  display: grid;
  font-size: 13px;
  line-height: 1.4;
  color: var(--tr-07-mut);
}

.tr-07__who b {
  font-size: 15.5px;
  font-weight: 660;
  color: var(--tr-07-ink);
  letter-spacing: -.018em;
}

.tr-07__foot {
  font-size: 11.5px;
  line-height: 1.5;
  color: color-mix(in oklch,var(--tr-07-mut) 85%,transparent);
  max-width: 46ch;
}

.tr-07__stats {
  padding: clamp(24px,4cqi,40px);
  display: grid;
  align-content: center;
  gap: clamp(16px,2.4cqi,24px);
  background: linear-gradient(170deg,color-mix(in oklch,var(--tr-07-acc) 13%,var(--tr-07-card)),color-mix(in oklch,var(--tr-07-acc) 4%,var(--tr-07-card)));
  border-inline-start: 1px solid oklch(0 0 0/.07);
}

.tr-07__stat p {
  font-size: 12.5px;
  color: var(--tr-07-mut);
  margin-top: 2px;
  letter-spacing: -.005em;
}

.tr-07__big {
  display: flex;
  align-items: baseline;
  font-size: clamp(40px,7cqi,60px);
  font-weight: 720;
  line-height: 1;
  letter-spacing: -.05em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
  color: color-mix(in oklch,var(--tr-07-acc) 80%,black);
}

.tr-07__suf,
.tr-07__pre {
  font-size: .55em;
  font-weight: 640;
  color: color-mix(in oklch,var(--tr-07-acc) 70%,black);
}

.tr-07__n::after {
  content: counter(tr-07-c);
}

.tr-07__big[data-k='a'] .tr-07__n {
  counter-reset: tr-07-c var(--tr-07-a);
  animation: tr-07-run-a 2.1s cubic-bezier(.16,1,.3,1) .15s both;
}

.tr-07__big[data-k='b'] .tr-07__n {
  counter-reset: tr-07-c var(--tr-07-b);
  animation: tr-07-run-b 2.1s cubic-bezier(.16,1,.3,1) .3s both;
}

@keyframes tr-07-run-a {
  from {
    --tr-07-a: 0;
  }

  to {
    --tr-07-a: 310;
  }
}

@keyframes tr-07-run-b {
  from {
    --tr-07-b: 0;
  }

  to {
    --tr-07-b: 64;
  }
}

.tr-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.tr-07__rows {
  display: grid;
  gap: 1px;
  margin-top: 6px;
  background: oklch(0 0 0/.08);
  border: 1px solid oklch(0 0 0/.08);
  border-radius: 12px;
  overflow: hidden;
}

.tr-07__rows>div {
  display: grid;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: 12px;
  padding: 11px 14px;
  background: var(--tr-07-card);
}

.tr-07__rows dt {
  font-size: 12.5px;
  color: var(--tr-07-mut);
}

.tr-07__rows dd {
  font-size: 13.5px;
  font-weight: 620;
  font-variant-numeric: tabular-nums;
}

.tr-07__old {
  color: color-mix(in oklch,var(--tr-07-mut) 90%,transparent);
  text-decoration: line-through 2px;
  text-decoration-color: oklch(0.6 0.19 25/.75);
}

.tr-07__new {
  position: relative;
  padding-inline-start: 20px;
  color: color-mix(in oklch,var(--tr-07-acc) 78%,black);
}

.tr-07__new::before {
  content: '→';
  position: absolute;
  inset-inline-start: 0;
  color: var(--tr-07-mut);
  font-weight: 500;
}

.tr-07__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: oklch(0.78 0.02 265);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@supports not (background: paint(x)) {
  .tr-07__n::after {
    content: counter(tr-07-c);
  }
}

@media (prefers-reduced-motion: reduce) {
  .tr-07__card {
    animation: none;
  }

  .tr-07__n {
    animation-duration: 1ms;
  }
}
```

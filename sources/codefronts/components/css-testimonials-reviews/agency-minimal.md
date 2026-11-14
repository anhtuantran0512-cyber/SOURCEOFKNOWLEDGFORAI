---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/agency-minimal/"
title: "Minimalist Agency Client Testimonial"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "What high-end studios actually ship: no cards, no shadows, no icons."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Agency Client Testimonial
Source: https://codefronts.com/components/css-testimonials-reviews/agency-minimal/

What high-end studios actually ship: no cards, no shadows, no icons. A hairline rule, a 12-column rhythm, one enormous quote and a client index that switches the quote on hover — the layout does the work that decoration would otherwise have to. Every visual decision here is a subtraction.
## HTML
```html
<section class="tr-16" aria-label="Minimalist agency client testimonial demo">
  <div class="tr-16__stage">
    <div class="tr-16__wrap">
      <p class="tr-16__eyebrow">Selected clients — 2024 / 2026</p>

      <div class="tr-16__index" role="group" aria-label="Choose a client testimonial">
        <input class="tr-16__sr" type="radio" name="tr-16-c" id="tr-16-c1" checked>
        <label for="tr-16-c1"><span>01</span>Ashcombe Labs<em>Brand system</em></label>
        <input class="tr-16__sr" type="radio" name="tr-16-c" id="tr-16-c2">
        <label for="tr-16-c2"><span>02</span>Halyard Ventures<em>Identity &amp; site</em></label>
        <input class="tr-16__sr" type="radio" name="tr-16-c" id="tr-16-c3">
        <label for="tr-16-c3"><span>03</span>Coplandt &amp; Sons<em>Retail rollout</em></label>
        <input class="tr-16__sr" type="radio" name="tr-16-c" id="tr-16-c4">
        <label for="tr-16-c4"><span>04</span>Larkfield Health<em>Product design</em></label>
      </div>

      <div class="tr-16__quotes">
        <figure class="tr-16__q" data-c="1">
          <blockquote><p>They deleted more than they added, and the thing that came back was unmistakably ours. Six months later our recruiters are quoting the brand guide in job ads.</p></blockquote>
          <figcaption><b>Samuel Idris</b><span>Principal Engineer, Ashcombe Labs</span></figcaption>
        </figure>
        <figure class="tr-16__q" data-c="2">
          <blockquote><p>The pitch deck template alone has been used in every raise since. Two of our portfolio companies asked who made it before we told them.</p></blockquote>
          <figcaption><b>Vivienne Adeyemi</b><span>General Partner, Halyard Ventures</span></figcaption>
        </figure>
        <figure class="tr-16__q" data-c="3">
          <blockquote><p>Eleven stores, one system, no arguments. The first rollout took a week; the eleventh took an afternoon and a phone call.</p></blockquote>
          <figcaption><b>Nathan Boateng</b><span>Chief Revenue Officer, Coplandt &amp; Sons</span></figcaption>
        </figure>
        <figure class="tr-16__q" data-c="4">
          <blockquote><p>Our clinicians stopped filing complaints about the software. In this sector that is the highest praise that exists.</p></blockquote>
          <figcaption><b>Erin McAllister</b><span>Chief Operating Officer, Larkfield Health</span></figcaption>
        </figure>
      </div>

      <p class="tr-16__foot"><span>Studio Aubain</span><span>Melbourne · London</span><span>Selected work available on request</span></p>
    </div>
  </div>
</section>
```
## CSS
```css
.tr-16,
.tr-16 *,
.tr-16 *::before,
.tr-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-16-bg: oklch(0.965 0.002 90);
  --tr-16-ink: oklch(0.18 0.005 90);
  --tr-16-mut: oklch(0.52 0.005 90);
  --tr-16-line: color-mix(in oklch,var(--tr-16-ink) 15%,transparent);
  background: var(--tr-16-bg);
  color: var(--tr-16-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(24px,6vw,80px);
}

.tr-16__wrap {
  width: min(100%,1180px);
  display: grid;
  grid-template-columns: repeat(12,1fr);
  column-gap: clamp(16px,2.4vw,28px);
  row-gap: clamp(26px,4vw,52px);
  animation: tr-16-in .9s cubic-bezier(.16,1,.3,1) both;
}

@keyframes tr-16-in {
  from {
    opacity: 0;
    translate: 0 14px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-16__eyebrow {
  grid-column: 1/-1;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--tr-16-mut);
  padding-bottom: clamp(18px,3vw,34px);
  border-block-end: 1px solid var(--tr-16-line);
}

.tr-16__index {
  grid-column: 1/5;
  display: grid;
  align-content: start;
  gap: 0;
}

.tr-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.tr-16__index label {
  display: grid;
  grid-template-columns: 34px 1fr;
  align-items: baseline;
  column-gap: 10px;
  padding: 15px 0;
  border-block-end: 1px solid var(--tr-16-line);
  font-size: 15.5px;
  font-weight: 560;
  letter-spacing: -.016em;
  color: var(--tr-16-mut);
  cursor: pointer;
  transition: color .3s,padding-inline-start .35s cubic-bezier(.16,1,.3,1);
  min-height: 44px;
}

.tr-16__index label span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .14em;
  color: color-mix(in oklch,var(--tr-16-mut) 70%,transparent);
}

.tr-16__index label em {
  grid-column: 2;
  display: block;
  font-style: normal;
  font-size: 11.5px;
  letter-spacing: .02em;
  color: color-mix(in oklch,var(--tr-16-mut) 78%,transparent);
  margin-top: 3px;
}

.tr-16__index label:hover {
  color: var(--tr-16-ink);
  padding-inline-start: 6px;
}

.tr-16__sr:checked+label {
  color: var(--tr-16-ink);
}

.tr-16__sr:checked+label span {
  color: var(--tr-16-ink);
}

.tr-16__sr:focus-visible+label {
  outline: 2px solid var(--tr-16-ink);
  outline-offset: 4px;
}

.tr-16__quotes {
  grid-column: 6/13;
  display: grid;
  align-content: center;
  min-block-size: clamp(220px,32vw,320px);
}

.tr-16__q {
  grid-area: 1/1;
  display: grid;
  gap: clamp(20px,3vw,34px);
  align-content: center;
  opacity: 0;
  visibility: hidden;
  translate: 0 10px;
  transition: opacity .5s cubic-bezier(.16,1,.3,1),translate .5s cubic-bezier(.16,1,.3,1),visibility .5s;
}

.tr-16:has(#tr-16-c1:checked) .tr-16__q[data-c='1'],
.tr-16:has(#tr-16-c2:checked) .tr-16__q[data-c='2'],
.tr-16:has(#tr-16-c3:checked) .tr-16__q[data-c='3'],
.tr-16:has(#tr-16-c4:checked) .tr-16__q[data-c='4'] {
  opacity: 1;
  visibility: visible;
  translate: 0 0;
}

.tr-16__q blockquote p {
  font-size: clamp(23px,3.4vw,49px);
  font-weight: 480;
  line-height: 1.16;
  letter-spacing: -.035em;
  text-wrap: balance;
  text-indent: -.42em;
  hanging-punctuation: first;
}

.tr-16__q blockquote p::before {
  content: '“';
}

.tr-16__q blockquote p::after {
  content: '”';
}

.tr-16__q figcaption {
  display: grid;
  gap: 3px;
  padding-block-start: clamp(16px,2vw,24px);
  border-block-start: 1px solid var(--tr-16-line);
}

.tr-16__q figcaption b {
  font-size: 14.5px;
  font-weight: 620;
  letter-spacing: -.012em;
}

.tr-16__q figcaption span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--tr-16-mut);
}

.tr-16__foot {
  grid-column: 1/-1;
  display: flex;
  flex-wrap: wrap;
  gap: clamp(14px,3vw,42px);
  padding-block-start: clamp(18px,3vw,30px);
  border-block-start: 1px solid var(--tr-16-line);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--tr-16-mut);
}

.tr-16__foot span:first-child {
  color: var(--tr-16-ink);
}

@media (max-width: 840px) {
  .tr-16__index {
    grid-column: 1/-1;
  }

  .tr-16__quotes {
    grid-column: 1/-1;
    min-block-size: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tr-16__wrap {
    animation: none;
  }

  .tr-16__q {
    transition: opacity .01s,visibility .01s;
  }
}
```

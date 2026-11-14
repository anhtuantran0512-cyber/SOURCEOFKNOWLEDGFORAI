---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/fintech-trust/"
title: "Fintech Security Trust Review Badge"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "In financial services the testimonial is only half the asset — the other half is who said it and what they are certified against."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fintech Security Trust Review Badge
Source: https://codefronts.com/components/css-testimonials-reviews/fintech-trust/

In financial services the testimonial is only half the asset — the other half is who said it and what they are certified against. This card pairs a named, titled reviewer from a regulated institution with a compliance strip (SOC 2, PCI DSS, ISO 27001, FCA reference), a lock-marked verification line and a tamper-evident "attested" timestamp.
## HTML
```html
<section class="tr-22" aria-label="Fintech security trust review badge demo">
  <div class="tr-22__stage">
    <article class="tr-22__card">
      <header class="tr-22__top">
        <span class="tr-22__seal">
          <svg viewBox="0 0 20 20" aria-hidden="true"><path d="M5.5 9V7a4.5 4.5 0 0 1 9 0v2" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><rect x="3.6" y="9" width="12.8" height="8.4" rx="2.2" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="10" cy="13.2" r="1.5" fill="currentColor"/></svg>
          Identity &amp; employment verified
        </span>
        <span class="tr-22__ref">REF · TR-22-4C9F17</span>
      </header>

      <figure class="tr-22__rev">
        <blockquote>Reconciliation used to close on the fourth business day. It now closes overnight, and the exception queue went from three hundred items to eleven. Our external auditors asked which system we had moved to before we mentioned it.</blockquote>
        <figcaption class="tr-22__who">
          <img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?q=80&w=160&h=160&fit=crop&auto=format" alt="Portrait of Alessandra Rossi" width="58" height="58" loading="lazy" decoding="async">
          <div>
            <b>Alessandra Rossi <span class="tr-22__chk"><svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.4"/><path d="M6.4 10.2l2.4 2.4 4.8-5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Verified</span></b>
            <span class="tr-22__title">Group Chief Technology Officer</span>
            <span class="tr-22__org">Vaultline Financial · FCA FRN 574 118 · London</span>
          </div>
        </figcaption>
      </figure>

      <div class="tr-22__certs">
        <p class="tr-22__clabel">Platform attestations current at time of review</p>
        <ul>
          <li class="tr-22__badge">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l7 3v5.6c0 4.5-2.9 8.6-7 10-4.1-1.4-7-5.5-7-10V5.6z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M8.6 12.2l2.3 2.3 4.5-4.7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <b>SOC 2 Type II</b><span>Audited Mar 2026 · Deloitte</span>
          </li>
          <li class="tr-22__badge">
            <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.4" y="6" width="17.2" height="12" rx="2.4" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3.4 10h17.2" stroke="currentColor" stroke-width="1.6"/><path d="M6.8 14.4h3.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <b>PCI DSS v4.0</b><span>Level 1 service provider</span>
          </li>
          <li class="tr-22__badge">
            <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 6.6v5.6l3.6 2.1" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <b>ISO/IEC 27001</b><span>Certified · expires 2028</span>
          </li>
          <li class="tr-22__badge">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19.4V9.2L12 4l8 5.2v10.2z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9.4 19.4v-5.6h5.2v5.6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>
            <b>Open Banking</b><span>FCA-registered AISP</span>
          </li>
        </ul>
      </div>

      <footer class="tr-22__f">
        <span>Attested <time datetime="2026-07-09T09:14:00Z">9 July 2026, 09:14 UTC</time></span>
        <span>Collected by an independent review partner · unedited</span>
      </footer>
    </article>
    <p class="tr-22__chip" aria-hidden="true">icon spanning two grid rows · gradient hairline seal · tabular-nums references · never colour-only state</p>
  </div>
</section>
```
## CSS
```css
.tr-22,
.tr-22 *,
.tr-22 *::before,
.tr-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-22-bg: oklch(0.2 0.026 260);
  --tr-22-card: oklch(0.985 0.004 250);
  --tr-22-ink: oklch(0.21 0.018 258);
  --tr-22-mut: oklch(0.52 0.018 258);
  --tr-22-acc: oklch(0.48 0.13 258);
  --tr-22-ok: oklch(0.56 0.15 155);
  background: var(--tr-22-bg);
  color: var(--tr-22-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,54px);
  background: radial-gradient(75% 55% at 50% 0%,oklch(0.32 0.06 258/.7),transparent 62%);
}

.tr-22__card {
  width: min(100%,780px);
  background: var(--tr-22-card);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 40px 80px -46px oklch(0 0 0/.8);
  animation: tr-22-in .8s cubic-bezier(.16,1,.3,1) both;
}

@keyframes tr-22-in {
  from {
    opacity: 0;
    translate: 0 18px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-22__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
  padding: 14px clamp(20px,3vw,30px);
  background: color-mix(in oklch,var(--tr-22-ok) 10%,var(--tr-22-card));
  border-bottom: 1px solid oklch(0 0 0/.07);
}

.tr-22__seal {
  display: flex;
  align-items: center;
  gap: 9px;
  flex: 1 1 240px;
  font-size: 12.5px;
  font-weight: 640;
  letter-spacing: -.005em;
  color: color-mix(in oklch,var(--tr-22-ok) 80%,black);
}

.tr-22__seal svg {
  width: 19px;
  height: 19px;
  flex: none;
}

.tr-22__seal::after {
  content: '';
  flex: 1;
  block-size: 1px;
  background: linear-gradient(90deg,currentColor,transparent);
  opacity: .45;
}

.tr-22__ref {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .06em;
  color: var(--tr-22-mut);
  font-variant-numeric: tabular-nums;
}

.tr-22__rev {
  padding: clamp(24px,3.4vw,34px) clamp(20px,3vw,30px);
  display: grid;
  gap: 22px;
}

.tr-22__rev blockquote {
  font-size: clamp(16px,2.2vw,19.5px);
  line-height: 1.6;
  letter-spacing: -.016em;
  color: color-mix(in oklch,var(--tr-22-ink) 94%,transparent);
  text-wrap: pretty;
}

.tr-22__rev blockquote::before {
  content: '“';
}

.tr-22__rev blockquote::after {
  content: '”';
}

.tr-22__who {
  display: flex;
  align-items: center;
  gap: 14px;
}

.tr-22__who img {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  box-shadow: 0 0 0 2px var(--tr-22-card),0 0 0 4px color-mix(in oklch,var(--tr-22-acc) 30%,transparent);
}

.tr-22__who div {
  display: grid;
  gap: 3px;
  min-width: 0;
}

.tr-22__who b {
  display: flex;
  align-items: center;
  gap: 9px;
  flex-wrap: wrap;
  font-size: 16px;
  font-weight: 660;
  letter-spacing: -.018em;
}

.tr-22__chk {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 2px 9px 2px 5px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--tr-22-ok) 14%,transparent);
  color: color-mix(in oklch,var(--tr-22-ok) 80%,black);
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .04em;
}

.tr-22__chk svg {
  width: 13px;
  height: 13px;
  fill: var(--tr-22-ok);
}

.tr-22__title {
  font-size: 13px;
  font-weight: 580;
  color: var(--tr-22-ink);
}

.tr-22__org {
  font-size: 11.5px;
  color: var(--tr-22-mut);
  font-variant-numeric: tabular-nums;
}

.tr-22__certs {
  padding: clamp(18px,2.6vw,24px) clamp(20px,3vw,30px);
  border-top: 1px solid oklch(0 0 0/.07);
  background: color-mix(in oklch,var(--tr-22-acc) 4%,var(--tr-22-card));
}

.tr-22__clabel {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tr-22-mut);
  margin-bottom: 14px;
}

.tr-22__certs ul {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,178px),1fr));
  gap: 12px;
}

.tr-22__badge {
  display: grid;
  grid-template-columns: auto 1fr;
  column-gap: 11px;
  align-items: center;
  padding: 12px 14px;
  border-radius: 11px;
  background: var(--tr-22-card);
  border: 1px solid oklch(0 0 0/.08);
  transition: border-color .25s,translate .25s cubic-bezier(.16,1,.3,1);
}

.tr-22__badge:hover {
  border-color: color-mix(in oklch,var(--tr-22-acc) 45%,transparent);
  translate: 0 -2px;
}

.tr-22__badge svg {
  grid-row: 1/3;
  width: 26px;
  height: 26px;
  color: var(--tr-22-acc);
}

.tr-22__badge b {
  font-size: 13px;
  font-weight: 660;
  letter-spacing: -.012em;
}

.tr-22__badge span {
  font-size: 11px;
  color: var(--tr-22-mut);
  line-height: 1.35;
}

.tr-22__f {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 20px;
  justify-content: space-between;
  padding: 14px clamp(20px,3vw,30px);
  border-top: 1px solid oklch(0 0 0/.07);
  font-size: 11px;
  color: var(--tr-22-mut);
  font-variant-numeric: tabular-nums;
}

.tr-22__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: oklch(0.78 0.02 258);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.15);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .tr-22__card {
    animation: none;
  }

  .tr-22__badge {
    transition: none;
  }
}
```

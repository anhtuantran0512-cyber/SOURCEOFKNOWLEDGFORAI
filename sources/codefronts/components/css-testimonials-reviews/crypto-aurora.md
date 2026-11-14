---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/crypto-aurora/"
title: "Web3 Gradient Glow Review Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "The animated conic border every AI, fintech and Web3 product wants — and the correct way to build it."
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Web3 Gradient Glow Review Card
Source: https://codefronts.com/components/css-testimonials-reviews/crypto-aurora/

The animated conic border every AI, fintech and Web3 product wants — and the correct way to build it. A registered @property angle is animated so the gradient genuinely rotates (unanimatable as a plain custom property), the glow is a blurred copy of the same gradient behind the card, and the whole thing runs on one composited element instead of a stack of hacks.
## HTML
```html
<section class="tr-17" aria-label="Web3 gradient glow review card demo">
  <div class="tr-17__stage">
    <header class="tr-17__head">
      <p class="tr-17__eyebrow">Builder feedback</p>
      <h2 class="tr-17__title">Signed by the people running it in production</h2>
    </header>

    <div class="tr-17__row">
      <figure class="tr-17__card">
        <div class="tr-17__chain"><span class="tr-17__dot" aria-hidden="true"></span>Verified on-chain · 0x7f…c41a</div>
        <blockquote>Settlement dropped from four minutes to under two seconds and the fee variance basically disappeared. We rewrote our treasury logic around it.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Ethan Park" width="44" height="44" loading="lazy" decoding="async">
          <span><b>Ethan Park</b>Protocol Lead · Northgate</span>
        </figcaption>
      </figure>

      <figure class="tr-17__card tr-17__card--glow">
        <div class="tr-17__chain"><span class="tr-17__dot" aria-hidden="true"></span>Verified on-chain · 0x2b…9e04</div>
        <blockquote>We audited six SDKs. This was the only one where the docs, the types and the actual behaviour agreed with each other on the first try.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Farah Haddad" width="44" height="44" loading="lazy" decoding="async">
          <span><b>Farah Haddad</b>Head of Engineering · Kestrel</span>
        </figcaption>
        <span class="tr-17__ribbon">Featured</span>
      </figure>

      <figure class="tr-17__card">
        <div class="tr-17__chain"><span class="tr-17__dot" aria-hidden="true"></span>Verified on-chain · 0x9a…7d13</div>
        <blockquote>Two million events a day, no dropped webhooks, no pager at 3am for eleven straight months. That is the whole review.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1546525848-3ce03ca516f6?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Andrew Tulloch" width="44" height="44" loading="lazy" decoding="async">
          <span><b>Andrew Tulloch</b>SRE · Vantage Rails</span>
        </figcaption>
      </figure>
    </div>
    <p class="tr-17__chip" aria-hidden="true">@property &lt;angle&gt; · animated conic-gradient border · mask-composite · phase-locked blur bloom</p>
  </div>
</section>
```
## CSS
```css
@property --tr-17-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.tr-17,
.tr-17 *,
.tr-17 *::before,
.tr-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-17-bg: oklch(0.145 0.02 285);
  --tr-17-card: oklch(0.2 0.024 285);
  --tr-17-ink: oklch(0.97 0.006 285);
  --tr-17-mut: oklch(0.71 0.02 285);
  --tr-17-c1: oklch(0.72 0.19 300);
  --tr-17-c2: oklch(0.78 0.16 200);
  --tr-17-c3: oklch(0.8 0.17 145);
  background: var(--tr-17-bg);
  color: var(--tr-17-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.tr-17__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,34px);
  padding: clamp(20px,4vw,58px);
  isolation: isolate;
  background: radial-gradient(70% 50% at 50% 0%,oklch(0.35 0.09 300/.4),transparent 62%);
}

.tr-17__head {
  text-align: center;
  display: grid;
  gap: 9px;
  max-width: 24ch;
}

.tr-17__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  background: linear-gradient(90deg,var(--tr-17-c1),var(--tr-17-c2));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.tr-17__title {
  font-size: clamp(24px,4vw,40px);
  font-weight: 670;
  letter-spacing: -.038em;
  line-height: 1.1;
  text-wrap: balance;
}

.tr-17__row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,268px),1fr));
  gap: clamp(16px,2.2vw,24px);
  width: min(100%,1080px);
  align-items: center;
}

.tr-17__card {
  position: relative;
  display: grid;
  gap: 16px;
  padding: clamp(22px,2.6vw,28px);
  border-radius: 20px;
  background: linear-gradient(165deg,color-mix(in oklch,var(--tr-17-c1) 7%,var(--tr-17-card)),var(--tr-17-card) 65%);
  border: 1px solid oklch(1 0 0/.09);
  animation: tr-17-in .8s cubic-bezier(.16,1,.3,1) both;
  transition: translate .35s cubic-bezier(.16,1,.3,1);
}

.tr-17__card:nth-child(2) {
  animation-delay: .1s;
}

.tr-17__card:nth-child(3) {
  animation-delay: .2s;
}

@keyframes tr-17-in {
  from {
    opacity: 0;
    translate: 0 18px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.tr-17__card:hover {
  translate: 0 -4px;
}

.tr-17__card--glow {
  border-color: transparent;
  background: linear-gradient(165deg,color-mix(in oklch,var(--tr-17-c1) 12%,var(--tr-17-card)),var(--tr-17-card) 62%);
  padding-block: clamp(28px,3.2vw,36px);
}

.tr-17__card--glow::before,
.tr-17__card--glow::after {
  content: '';
  position: absolute;
  inset: -1.5px;
  border-radius: inherit;
  background: conic-gradient(from var(--tr-17-a),var(--tr-17-c1),var(--tr-17-c2),var(--tr-17-c3),var(--tr-17-c1));
  animation: tr-17-spin 7s linear infinite;
}

.tr-17__card--glow::before {
  padding: 1.5px;
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
  z-index: 1;
}

.tr-17__card--glow::after {
  z-index: -1;
  filter: blur(26px);
  opacity: .5;
}

@keyframes tr-17-spin {
  to {
    --tr-17-a: 360deg;
  }
}

.tr-17__chain {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  width: fit-content;
  padding: 5px 11px;
  border-radius: 99px;
  background: oklch(1 0 0/.06);
  border: 1px solid oklch(1 0 0/.11);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .02em;
  color: var(--tr-17-mut);
}

.tr-17__dot {
  inline-size: 7px;
  block-size: 7px;
  border-radius: 50%;
  background: var(--tr-17-c3);
  box-shadow: 0 0 0 0 color-mix(in oklch,var(--tr-17-c3) 70%,transparent);
  animation: tr-17-pulse 2.4s cubic-bezier(.16,1,.3,1) infinite;
}

@keyframes tr-17-pulse {
  0% {
    box-shadow: 0 0 0 0 color-mix(in oklch,var(--tr-17-c3) 65%,transparent);
  }

  70%,
    100% {
    box-shadow: 0 0 0 8px transparent;
  }
}

.tr-17__card blockquote {
  font-size: 15.5px;
  line-height: 1.55;
  letter-spacing: -.016em;
  text-wrap: pretty;
}

.tr-17__card figcaption {
  display: flex;
  align-items: center;
  gap: 11px;
  padding-top: 16px;
  border-top: 1px solid oklch(1 0 0/.1);
}

.tr-17__card figcaption img {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  box-shadow: 0 0 0 1px oklch(1 0 0/.18);
}

.tr-17__card figcaption span {
  display: grid;
  font-size: 12px;
  line-height: 1.35;
  color: var(--tr-17-mut);
}

.tr-17__card figcaption b {
  font-size: 14.5px;
  font-weight: 640;
  color: var(--tr-17-ink);
  letter-spacing: -.014em;
}

.tr-17__ribbon {
  position: absolute;
  inset-block-start: -11px;
  inset-inline-start: clamp(22px,2.6vw,28px);
  padding: 4px 12px;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--tr-17-c1),var(--tr-17-c2));
  color: oklch(0.15 0.02 285);
  font-size: 10.5px;
  font-weight: 750;
  letter-spacing: .1em;
  text-transform: uppercase;
  z-index: 2;
}

.tr-17__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-17-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .tr-17__card {
    animation: none;
  }

  .tr-17__card--glow::before,
    .tr-17__card--glow::after,
    .tr-17__dot {
    animation: none;
  }
}
```

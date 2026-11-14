---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/certificate-seal-ribbon-rosette/"
title: "Certificate Seal Ribbon Rosette"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "The foil seal that makes a certificate feel issued rather than printed."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Certificate Seal Ribbon Rosette
Source: https://codefronts.com/snippets/css-ribbons/certificate-seal-ribbon-rosette/

The foil seal that makes a certificate feel issued rather than printed. A registered @property <angle> rotates a multi-stop conic gradient so the gold genuinely catches light as it turns — an effect that is impossible with an unregistered custom property, because gradients cannot be transitioned but their angle variable can. Sits on a real certificate layout with an engraved guilloche border.
## HTML
```html
<section class="rib-13" aria-label="Certificate diploma ribbon rosette trust seal demo">
  <div class="rib-13__stage">
    <article class="rib-13__cert">
      <div class="rib-13__frame">
        <p class="rib-13__issuer">Institute of Interface Engineering</p>
        <p class="rib-13__pre">This is to certify that</p>
        <h2 class="rib-13__name">Amelia R. Whitcombe</h2>
        <p class="rib-13__for">has completed the advanced programme in</p>
        <p class="rib-13__course">Modern CSS Architecture &amp; Accessible Interface Systems</p>
        <div class="rib-13__seal-wrap">
          <div class="rib-13__seal" role="img" aria-label="Official completion seal of the Institute of Interface Engineering">
            <span class="rib-13__tail rib-13__tail--l"></span>
            <span class="rib-13__tail rib-13__tail--r"></span>
            <span class="rib-13__disc"><span class="rib-13__face"><span class="rib-13__mark">IIE</span><span class="rib-13__small">Certified</span></span></span>
          </div>
        </div>
        <dl class="rib-13__meta">
          <div><dt>Certificate ID</dt><dd>IIE-2026-0714-9C42</dd></div>
          <div><dt>Issued</dt><dd><time datetime="2026-07-14">14 July 2026</time></dd></div>
          <div><dt>Verify at</dt><dd><a class="rib-13__link" href="#rib-13-verify">iie.edu/verify</a></dd></div>
        </dl>
      </div>
    </article>
    <p class="rib-13__chip" aria-hidden="true">@property &lt;angle&gt; conic foil · inset emboss shadows · guilloche gradients</p>
  </div>
</section>
```
## CSS
```css
@property --rib-13-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.rib-13,
.rib-13 *,
.rib-13 *::before,
.rib-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-13-bg: #2a2723;
  --rib-13-bg: oklch(0.28 0.012 80);
  --rib-13-paper: #fbf7ee;
  --rib-13-paper: oklch(0.98 0.014 88);
  --rib-13-ink: #2a2318;
  --rib-13-ink: oklch(0.28 0.02 70);
  --rib-13-mut: #6f6455;
  --rib-13-mut: oklch(0.53 0.024 78);
  --rib-13-hue: 86;
  --rib-13-hi: #f4dfa0;
  --rib-13-hi: oklch(0.92 0.1 var(--rib-13-hue));
  --rib-13-lo: #b48a34;
  --rib-13-lo: oklch(0.68 0.13 var(--rib-13-hue));
  --rib-13-deep: #7a5a19;
  --rib-13-deep: oklch(0.5 0.11 var(--rib-13-hue));
  --rib-13-seal: clamp(94px,17vw,124px);
  background: var(--rib-13-bg);
  color: var(--rib-13-ink);
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
}

.rib-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(14px,3vw,24px);
  padding: clamp(16px,4vw,52px);
  background: radial-gradient(80% 70% at 50% 0%,oklch(0.36 0.02 80),transparent 70%);
}

.rib-13__cert {
  width: min(100%,700px);
  padding: clamp(10px,2vw,16px);
  background: var(--rib-13-paper);
  border-radius: 6px;
  box-shadow: 0 2px 3px oklch(0 0 0/.3),0 40px 80px -40px oklch(0 0 0/.9);
}

.rib-13__frame {
  position: relative;
  display: grid;
  justify-items: center;
  gap: clamp(7px,1.5vw,11px);
  padding: clamp(26px,5vw,48px) clamp(20px,4vw,44px);
  text-align: center;
  border: 2px solid color-mix(in oklch,var(--rib-13-lo) 55%,transparent);
  outline: 1px solid color-mix(in oklch,var(--rib-13-lo) 30%,transparent);
  outline-offset: 5px;
  background-image: repeating-conic-gradient(from 0deg,color-mix(in oklch,var(--rib-13-lo) 5%,transparent) 0deg 4deg,transparent 4deg 8deg),repeating-linear-gradient(45deg,color-mix(in oklch,var(--rib-13-lo) 5%,transparent) 0 1px,transparent 1px 7px);
  background-size: auto,auto;
}

.rib-13__issuer {
  font-size: clamp(11px,2.2vw,13px);
  font-weight: 700;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--rib-13-lo);
}

.rib-13__pre,
.rib-13__for {
  font-size: 13.5px;
  font-style: italic;
  color: var(--rib-13-mut);
}

.rib-13__name {
  font-size: clamp(28px,6vw,44px);
  font-weight: 400;
  letter-spacing: -.01em;
  line-height: 1.1;
  text-wrap: balance;
  border-block-end: 1px solid color-mix(in oklch,var(--rib-13-lo) 45%,transparent);
  padding-block-end: 8px;
  margin-block-start: 2px;
}

.rib-13__course {
  max-width: 34ch;
  font-size: clamp(15px,3vw,18px);
  line-height: 1.45;
  font-weight: 700;
  text-wrap: balance;
}

.rib-13__seal-wrap {
  margin-block: clamp(10px,2.4vw,18px) clamp(30px,6vw,44px);
}

.rib-13__seal {
  position: relative;
  inline-size: var(--rib-13-seal);
  display: grid;
  place-items: center;
  filter: drop-shadow(0 10px 14px oklch(0.4 0.06 80/.4));
}

.rib-13__tail {
  position: absolute;
  inset-block-start: 58%;
  inline-size: calc(var(--rib-13-seal) * .3);
  block-size: calc(var(--rib-13-seal) * .62);
  background: #b48a34;
  background: linear-gradient(100deg,var(--rib-13-deep),var(--rib-13-lo) 48%,var(--rib-13-deep));
  clip-path: polygon(0 0,100% 0,100% 100%,50% 72%,0 100%);
  z-index: 0;
  transform-origin: top center;
}

.rib-13__tail--l {
  inset-inline-start: calc(50% - var(--rib-13-seal) * .3);
  rotate: 13deg;
}

.rib-13__tail--r {
  inset-inline-start: 50%;
  rotate: -13deg;
}

.rib-13__disc {
  position: relative;
  z-index: 1;
  inline-size: var(--rib-13-seal);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: #b48a34;
  background: conic-gradient(from var(--rib-13-a),var(--rib-13-deep),var(--rib-13-hi) 14%,var(--rib-13-lo) 30%,color-mix(in oklch,var(--rib-13-hi) 100%,white 20%) 48%,var(--rib-13-lo) 66%,var(--rib-13-hi) 84%,var(--rib-13-deep));
  box-shadow: inset 0 2px 3px oklch(1 0 0/.5),inset 0 -3px 7px oklch(0 0 0/.35),0 0 0 4px color-mix(in oklch,var(--rib-13-deep) 65%,transparent);
  animation: rib-13-turn 9s linear infinite;
}

@keyframes rib-13-turn {
  to {
    --rib-13-a: 360deg;
  }
}

.rib-13__face {
  inline-size: 72%;
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 1px;
  border-radius: 50%;
  background: radial-gradient(circle at 36% 30%,color-mix(in oklch,var(--rib-13-hi) 100%,white 26%),var(--rib-13-lo) 70%);
  box-shadow: inset 0 1px 2px oklch(1 0 0/.55),inset 0 -2px 5px oklch(0 0 0/.3);
  color: oklch(0.3 0.06 var(--rib-13-hue));
}

.rib-13__mark {
  font-size: clamp(19px,4vw,25px);
  font-weight: 700;
  letter-spacing: .04em;
  line-height: 1;
  text-shadow: 0 1px 0 oklch(1 0 0/.45);
}

.rib-13__small {
  font-family: system-ui,sans-serif;
  font-size: 8px;
  font-weight: 800;
  letter-spacing: .22em;
  text-transform: uppercase;
  opacity: .85;
}

.rib-13__meta {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(14px,4vw,34px);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  padding-block-start: clamp(12px,2.4vw,18px);
  border-block-start: 1px solid color-mix(in oklch,var(--rib-13-lo) 30%,transparent);
  width: 100%;
}

.rib-13__meta div {
  display: grid;
  gap: 3px;
}

.rib-13__meta dt {
  font-size: 9.5px;
  font-weight: 750;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--rib-13-mut);
}

.rib-13__meta dd {
  font-size: 13px;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.rib-13__link {
  color: color-mix(in oklch,var(--rib-13-lo) 85%,black);
  text-underline-offset: 3px;
}

.rib-13__link:hover {
  color: var(--rib-13-ink);
}

.rib-13__link:focus-visible {
  outline: 3px solid var(--rib-13-lo);
  outline-offset: 3px;
  border-radius: 2px;
}

.rib-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: oklch(0.78 0.02 85);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
  text-align: center;
}

@media print {
  .rib-13__disc {
    animation: none;
  }

  .rib-13__chip {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rib-13 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

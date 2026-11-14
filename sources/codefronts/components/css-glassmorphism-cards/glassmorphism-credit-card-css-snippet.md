---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-credit-card-css-snippet/"
title: "Glassmorphism Credit Card CSS Snippet"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "The canonical frosted bank card, two ways: an aurora-lit dark card with a gold chip, embossed number and a hover light-sweep + 3D tilt, and a light-theme…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Credit Card CSS Snippet
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-credit-card-css-snippet/

The canonical frosted bank card, two ways: an aurora-lit dark card with a gold chip, embossed number and a hover light-sweep + 3D tilt, and a light-theme fanned stack where the glass card visibly blurs a vivid card behind it — the clearest possible proof of what backdrop-filter does.
## HTML
```html
<div class="glz-01-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-01a" aria-label="Glassmorphism credit card demo">
  <div class="glz-01a__card" tabindex="0" role="img" aria-label="Nova Infinite virtual card ending 4467, expires September 2029">
    <div class="glz-01a__top"><span class="glz-01a__bank">NOVA<em>∞</em></span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 8.6a6.4 6.4 0 0 1 0 6.8M9.6 6.4a10.4 10.4 0 0 1 0 11.2M13.2 4.2a14.6 14.6 0 0 1 0 15.6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></div>
    <div class="glz-01a__chip" aria-hidden="true"></div>
    <p class="glz-01a__num" aria-hidden="true">5389&#8194;1201&#8194;8890&#8194;4467</p>
    <div class="glz-01a__meta"><span><em>Card holder</em>AVA REYNOLDS</span><span><em>Expires</em>09/29</span><span class="glz-01a__brand" aria-hidden="true"><i></i><i></i></span></div>
  </div>
  <p class="glz-01a__hint" aria-hidden="true">blur(24px) saturate(180%) · hover / focus to tilt</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-01b" aria-label="Stacked glassmorphism credit cards demo">
  <div class="glz-01b__stack">
    <div class="glz-01b__back" aria-hidden="true"><span>debit</span><b>ivy • studio</b></div>
    <div class="glz-01b__front" tabindex="0" role="img" aria-label="Ivy Studio glass card ending 2210">
      <div class="glz-01b__row"><b>ivy</b><span class="glz-01b__tag">virtual</span></div>
      <p class="glz-01b__num" aria-hidden="true">••••&#8194;••••&#8194;••••&#8194;2210</p>
      <div class="glz-01b__foot"><span>MILA CHEN</span><span>11/28</span></div>
    </div>
  </div>
  <p class="glz-01b__hint" aria-hidden="true">hover the stack — the frost blurs the card behind it, live</p>
</section>
</div>
```
## CSS
```css
.glz-01-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-01-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-01a,
.glz-01a *,
.glz-01a *::before,
.glz-01a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-01a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: 48px 24px;
  background: #080b14;
  font-family: 'Space Grotesk',system-ui,sans-serif;
}

.glz-01a::before,
.glz-01a::after {
  content: "";
  position: absolute;
  width: 46vmin;
  height: 46vmin;
  border-radius: 50%;
  filter: blur(72px);
  opacity: .8;
  animation: glz-01a-drift 14s ease-in-out infinite alternate;
}

.glz-01a::before {
  background: oklch(0.62 0.26 285);
  top: 4%;
  left: 14%;
}

.glz-01a::after {
  background: oklch(0.75 0.17 195);
  bottom: 2%;
  right: 12%;
  animation-delay: -7s;
}

.glz-01a__card {
  position: relative;
  z-index: 1;
  width: min(400px,100%);
  aspect-ratio: 8/5;
  border-radius: 24px;
  padding: 24px 28px;
  display: flex;
  flex-direction: column;
  color: #f2f5ff;
  background: linear-gradient(135deg,rgba(255,255,255,.16),rgba(255,255,255,.05));
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255,255,255,.24);
  box-shadow: 0 30px 60px -20px rgba(0,0,0,.65),inset 0 1px 0 rgba(255,255,255,.28);
  overflow: hidden;
  transition: transform .5s cubic-bezier(.2,.8,.25,1.1);
}

.glz-01a__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(115deg,transparent 32%,rgba(255,255,255,.3) 47%,rgba(160,220,255,.16) 53%,transparent 68%);
  transform: translateX(-130%) skewX(-8deg);
  transition: transform .9s ease;
}

.glz-01a__card:hover,
.glz-01a__card:focus-visible {
  transform: perspective(900px) rotateX(7deg) rotateY(-9deg) translateY(-8px);
}

.glz-01a__card:hover::before,
.glz-01a__card:focus-visible::before {
  transform: translateX(130%) skewX(-8deg);
}

.glz-01a__card:focus-visible {
  outline: 2px solid oklch(0.8 0.14 210);
  outline-offset: 5px;
}

.glz-01a__top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 700;
  letter-spacing: .3em;
  font-size: 15px;
}

.glz-01a__top em {
  font-style: normal;
  color: oklch(0.8 0.15 195);
  margin-left: 4px;
}

.glz-01a__top svg {
  width: 23px;
  height: 23px;
  color: rgba(255,255,255,.7);
}

.glz-01a__chip {
  width: 46px;
  height: 34px;
  margin-top: 22px;
  border-radius: 8px;
  background: linear-gradient(135deg,#f6d67f,#c9973f 55%,#eec168);
  box-shadow: inset 0 0 0 1px rgba(110,72,8,.4),0 2px 6px rgba(0,0,0,.35);
  position: relative;
}

.glz-01a__chip::before {
  content: "";
  position: absolute;
  inset: 7px 5px;
  border: 1px solid rgba(110,72,8,.5);
  border-radius: 4px;
  background: linear-gradient(90deg,transparent 44%,rgba(110,72,8,.5) 44% 56%,transparent 56%);
}

.glz-01a__num {
  margin-top: auto;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: clamp(16px,4.2vw,20px);
  letter-spacing: .05em;
  text-shadow: 0 1px 1px rgba(0,0,0,.6),0 -1px 1px rgba(255,255,255,.2);
}

.glz-01a__meta {
  display: flex;
  align-items: flex-end;
  gap: 26px;
  margin-top: 14px;
  font-size: 12.5px;
  letter-spacing: .05em;
}

.glz-01a__meta em {
  display: block;
  font-style: normal;
  font-size: 8.5px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: rgba(235,242,255,.55);
  margin-bottom: 3px;
}

.glz-01a__brand {
  margin-left: auto;
  display: flex;
}

.glz-01a__brand i {
  width: 27px;
  height: 27px;
  border-radius: 50%;
  background: rgba(255,86,58,.9);
}

.glz-01a__brand i+i {
  margin-left: -11px;
  background: rgba(255,190,60,.85);
  mix-blend-mode: screen;
}

.glz-01a__hint {
  position: relative;
  z-index: 1;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 11px;
  letter-spacing: .14em;
  color: rgba(198,214,245,.45);
}

@keyframes glz-01a-drift {
  to {
    transform: translate(9vmin,-7vmin) scale(1.18);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-01a__card {
    background: rgba(20,26,44,.92);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-01a::before,
    .glz-01a::after {
    animation: none;
  }

  .glz-01a__card,
    .glz-01a__card::before {
    transition: none;
  }
}

.glz-01b,
.glz-01b *,
.glz-01b *::before,
.glz-01b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-01b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 34px;
  padding: 48px 24px;
  background: linear-gradient(160deg,#eef1f8,#e9e4f2 55%,#f4e9e2);
  font-family: 'Space Grotesk',system-ui,sans-serif;
}

.glz-01b__stack {
  position: relative;
  width: min(380px,86vw);
  aspect-ratio: 8/5;
}

.glz-01b__back {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  background: linear-gradient(130deg,oklch(0.62 0.23 300),oklch(0.68 0.2 20) 60%,oklch(0.8 0.15 70));
  transform: rotate(-7deg) translate(-9%,-13%);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 22px 24px;
  color: rgba(255,255,255,.92);
  font-size: 13px;
  letter-spacing: .18em;
  text-transform: uppercase;
  box-shadow: 0 18px 40px -14px rgba(90,50,120,.55);
  transition: transform .55s cubic-bezier(.2,.8,.25,1.15);
}

.glz-01b__back b {
  font-size: 15px;
  letter-spacing: .04em;
  text-transform: none;
}

.glz-01b__front {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  padding: 24px 26px;
  display: flex;
  flex-direction: column;
  color: #241d33;
  background: linear-gradient(135deg,rgba(255,255,255,.55),rgba(255,255,255,.22));
  backdrop-filter: blur(18px) saturate(160%);
  -webkit-backdrop-filter: blur(18px) saturate(160%);
  border: 1px solid rgba(255,255,255,.75);
  box-shadow: 0 24px 50px -18px rgba(60,45,110,.4),inset 0 1px 0 rgba(255,255,255,.9);
  transition: transform .55s cubic-bezier(.2,.8,.25,1.15);
}

.glz-01b__stack:hover .glz-01b__back,
.glz-01b__front:focus-visible~.glz-01b__back {
  transform: rotate(-13deg) translate(-16%,-24%);
}

.glz-01b__stack:hover .glz-01b__front {
  transform: rotate(2deg) translateY(4%);
}

.glz-01b__front:focus-visible {
  outline: 2px solid oklch(0.55 0.2 300);
  outline-offset: 4px;
}

.glz-01b__row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.glz-01b__tag {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: .22em;
  text-transform: uppercase;
  padding: 5px 10px;
  border-radius: 99px;
  background: rgba(255,255,255,.5);
  border: 1px solid rgba(255,255,255,.8);
  color: #4c3f6d;
}

.glz-01b__num {
  margin-top: auto;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 19px;
  letter-spacing: .08em;
  color: #33284d;
}

.glz-01b__foot {
  display: flex;
  justify-content: space-between;
  margin-top: 12px;
  font-size: 12px;
  letter-spacing: .14em;
  color: rgba(36,29,51,.65);
}

.glz-01b__hint {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  color: rgba(60,50,90,.5);
  text-align: center;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-01b__front {
    background: rgba(255,255,255,.9);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-01b__back,
    .glz-01b__front {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the tilt is a hover/focus transform, the sheen is a translated gradient on ::before, and the aurora is two blurred, animated pseudo-elements. */

/* No JavaScript — hovering the stack re-transforms both absolutely-stacked cards; the frosted front card blurs the vivid back card through backdrop-filter in real time. */
```

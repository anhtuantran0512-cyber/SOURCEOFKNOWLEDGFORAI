---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/card-lift/"
title: "Card Lift Accordion — Elevation & Scale on Open (Material-Style Depth)"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Depth as state: closed items are flat, flush cards; the open item lifts toward you — scaling to 102%, growing a layered soft shadow and pushing neighbors…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Card Lift Accordion — Elevation & Scale on Open (Material-Style Depth)
Source: https://codefronts.com/navigation/css-accordions/card-lift/

Depth as state: closed items are flat, flush cards; the open item lifts toward you — scaling to 102%, growing a layered soft shadow and pushing neighbors away with extra margin. The material-design 'picked up paper' metaphor, tuned so elevation alone tells you what's active from across the room.
## HTML
```html
<section class="acc-14" aria-label="Card lift elevation accordion demo">
  <div class="acc-14__wrap">
    <h3 class="acc-14__title">Choose your plan</h3>
    <details class="acc-14__item" name="acc-14-plans" open>
      <summary class="acc-14__sum"><span class="acc-14__plan">Starter<small>For solo builders</small></span><span class="acc-14__price">$0</span></summary>
      <div class="acc-14__body"><p>3 projects · community support · 1GB storage. Everything you need to ship a side project tonight.</p></div>
    </details>
    <details class="acc-14__item" name="acc-14-plans">
      <summary class="acc-14__sum"><span class="acc-14__plan">Pro<small>For growing teams</small></span><span class="acc-14__price">$24<em>/mo</em></span></summary>
      <div class="acc-14__body"><p>Unlimited projects · priority support · 100GB storage · staging environments and preview deploys for every branch.</p></div>
    </details>
    <details class="acc-14__item" name="acc-14-plans">
      <summary class="acc-14__sum"><span class="acc-14__plan">Scale<small>For companies</small></span><span class="acc-14__price">Custom</span></summary>
      <div class="acc-14__body"><p>SSO/SAML · audit logs · dedicated support with a 4-hour SLA · invoicing and procurement-friendly paperwork.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-14,
.acc-14 *,
.acc-14 *::before,
.acc-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-14 {
  --accent: oklch(0.6 0.17 45);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3f1ee;
  padding: 44px 24px;
}

.acc-14__wrap {
  width: min(540px,100%);
}

.acc-14__title {
  font-size: 25px;
  font-weight: 800;
  color: #241f19;
  letter-spacing: -.02em;
  margin-bottom: 18px;
}

.acc-14__item {
  background: #fbfaf8;
  border: 1px solid #e7e2da;
  border-radius: 16px;
  margin: 0 0 8px;
  border-top: 3px solid transparent;
  transition: scale .35s cubic-bezier(.3,1.2,.4,1),box-shadow .35s,margin .35s,background .25s,border-color .25s;
}

.acc-14__item[open] {
  background: #fff;
  scale: 1.02;
  margin: 14px 0;
  border-top-color: var(--accent);
  box-shadow: 0 2px 6px -2px rgba(40,30,15,.18),0 24px 50px -20px rgba(40,30,15,.28);
}

.acc-14__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 66px;
  padding: 10px 22px;
  cursor: pointer;
}

.acc-14__sum::-webkit-details-marker {
  display: none;
}

.acc-14__sum::marker {
  content: "";
}

.acc-14__plan {
  display: flex;
  flex-direction: column;
  gap: 2px;
  font-size: 17px;
  font-weight: 750;
  color: #241f19;
}

.acc-14__plan small {
  font-size: 12.5px;
  font-weight: 500;
  color: #8b8172;
}

.acc-14__price {
  margin-left: auto;
  font-size: 20px;
  font-weight: 800;
  color: #241f19;
}

.acc-14__price em {
  font-style: normal;
  font-size: 12.5px;
  font-weight: 600;
  color: #8b8172;
}

.acc-14__item[open] .acc-14__price {
  color: var(--accent);
}

.acc-14__body {
  padding: 0 22px 20px;
  font-size: 14.5px;
  line-height: 1.65;
  color: #57503f;
}

.acc-14__item[open] .acc-14__body {
  animation: acc-14-in .4s cubic-bezier(.2,.7,.3,1);
}

@keyframes acc-14-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-14__sum:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-14__item {
    transition: background .25s;
  }

  .acc-14__item[open] {
    scale: 1;
    margin: 0 0 8px;
  }

  .acc-14__item[open] .acc-14__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — details[open] applies scale:1.02, a two-layer contact+ambient shadow and clearance margins; closed cards stay deliberately flat so elevation alone marks the active item. */
```

---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/order-tracking-timeline-delivery-progress-stepper/"
title: "Order Tracking Timeline — Delivery Progress Stepper"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The e-commerce essential: Placed → Packed → Shipped → Out for delivery → Delivered as a horizontal stepper whose connector fills to the current stage with…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Order Tracking Timeline — Delivery Progress Stepper
Source: https://codefronts.com/layouts/css-timelines/order-tracking-timeline-delivery-progress-stepper/

The e-commerce essential: Placed → Packed → Shipped → Out for delivery → Delivered as a horizontal stepper whose connector fills to the current stage with one custom property, an animated pulse on the live step, ETA copy, and a container-query flip to the vertical mobile layout — the exact component order-status emails link to.
## HTML
```html
<section class="tls-04" aria-label="Order tracking timeline demo">
  <div class="tls-04__card" style="--tl-progress:2.5;--tl-steps:5">
    <header class="tls-04__head">
      <div><p class="tls-04__no">Order #48-2214</p><p class="tls-04__eta">Arriving <time datetime="2026-07-21">Tue, Jul 21</time> by 8pm</p></div>
      <span class="tls-04__badge">In transit</span>
    </header>
    <div class="tls-04__wrap">
      <div class="tls-04__track" aria-hidden="true"><span class="tls-04__fill"></span></div>
      <ol class="tls-04__steps" role="list">
        <li class="tls-04__step" data-state="done"><span class="tls-04__dot" aria-hidden="true"></span><span class="tls-04__lab">Placed<span class="tls-04__sr">, completed</span></span><time class="tls-04__t" datetime="2026-07-17T10:12">Jul 17</time></li>
        <li class="tls-04__step" data-state="done"><span class="tls-04__dot" aria-hidden="true"></span><span class="tls-04__lab">Packed<span class="tls-04__sr">, completed</span></span><time class="tls-04__t" datetime="2026-07-18T08:30">Jul 18</time></li>
        <li class="tls-04__step" data-state="current" aria-current="step"><span class="tls-04__dot" aria-hidden="true"></span><span class="tls-04__lab">Shipped<span class="tls-04__sr">, current step</span></span><time class="tls-04__t" datetime="2026-07-19T06:15">Jul 19</time></li>
        <li class="tls-04__step"><span class="tls-04__dot" aria-hidden="true"></span><span class="tls-04__lab">Out for delivery</span><span class="tls-04__t">—</span></li>
        <li class="tls-04__step"><span class="tls-04__dot" aria-hidden="true"></span><span class="tls-04__lab">Delivered</span><span class="tls-04__t">—</span></li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-04,
.tls-04 *,
.tls-04 *::before,
.tls-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-04 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #0972d3;
  --tl-ok: #037f4c;
  --tl-line: #e4e7eb;
  --tl-ink: #16191f;
  --tl-mut: #5f6b7a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f4f6f8;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-04__card {
  width: min(720px,100%);
  container-type: inline-size;
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 16px;
  padding: 26px 30px 30px;
  box-shadow: 0 1px 4px rgba(15,25,40,.06);
}

.tls-04__head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 30px;
}

.tls-04__no {
  font-size: 13px;
  font-weight: 600;
  color: var(--tl-mut);
}

.tls-04__eta {
  font-size: 17px;
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.01em;
  margin-top: 3px;
}

.tls-04__badge {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--tl-accent);
  background: #e8f2fc;
  border-radius: 999px;
  padding: 5px 12px;
}

.tls-04__wrap {
  position: relative;
}

.tls-04__track {
  position: absolute;
  left: calc(10% );
  right: 10%;
  top: 13px;
  height: 4px;
  border-radius: 2px;
  background: var(--tl-line);
  overflow: hidden;
}

.tls-04__fill {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,var(--tl-ok),var(--tl-accent));
  transform-origin: left;
  transform: scaleX(calc(var(--tl-progress) / (var(--tl-steps) - 1)));
  transition: transform .6s cubic-bezier(.3,.7,.3,1);
}

.tls-04__steps {
  list-style: none;
  display: flex;
  position: relative;
}

.tls-04__step {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  text-align: center;
}

.tls-04__dot {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid var(--tl-line);
  position: relative;
  z-index: 1;
}

.tls-04__step[data-state="done"] .tls-04__dot {
  background: var(--tl-ok);
  border-color: var(--tl-ok);
}

.tls-04__step[data-state="done"] .tls-04__dot::after {
  content: '';
  position: absolute;
  left: 9px;
  top: 6px;
  width: 6px;
  height: 11px;
  border-right: 2.5px solid #fff;
  border-bottom: 2.5px solid #fff;
  rotate: 45deg;
}

.tls-04__step[data-state="current"] .tls-04__dot {
  border-color: var(--tl-accent);
  border-width: 4px;
}

.tls-04__step[data-state="current"] .tls-04__dot::before {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 2px solid var(--tl-accent);
  animation: tls-04-pulse 1.8s ease-out infinite;
}

@keyframes tls-04-pulse {
  0% {
    transform: scale(1);
    opacity: .7;
  }

  100% {
    transform: scale(1.9);
    opacity: 0;
  }
}

.tls-04__lab {
  font-size: 12.5px;
  font-weight: 700;
  color: var(--tl-mut);
  max-width: 11ch;
  text-wrap: balance;
}

.tls-04__step[data-state] .tls-04__lab {
  color: var(--tl-ink);
}

.tls-04__t {
  font-size: 11px;
  color: var(--tl-mut);
}

.tls-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@container (max-width: 440px) {
  .tls-04__track {
    left: 14px;
    right: auto;
    top: 8px;
    bottom: 8px;
    width: 4px;
    height: auto;
  }

  .tls-04__fill {
    transform-origin: top;
    transform: scaleY(calc(var(--tl-progress) / (var(--tl-steps) - 1)));
  }

  .tls-04__steps {
    flex-direction: column;
    gap: 22px;
  }

  .tls-04__step {
    flex-direction: row;
    text-align: left;
    gap: 14px;
  }

  .tls-04__lab {
    max-width: none;
  }

  .tls-04__t {
    margin-left: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tls-04__step[data-state="current"] .tls-04__dot::before {
    animation: none;
    opacity: .5;
  }

  .tls-04__fill {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — progress is one custom property (--tl-progress) on the card; the fill derives via scaleX(calc(progress / (steps − 1))), so a backend renders a single inline style. */
```

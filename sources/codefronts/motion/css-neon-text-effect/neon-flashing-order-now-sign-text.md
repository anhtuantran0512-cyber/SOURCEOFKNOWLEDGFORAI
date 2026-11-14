---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/neon-flashing-order-now-sign-text/"
title: "Neon Flashing \"Order Now\" Sign Text"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "An attention-grabbing storefront-style banner where the offer copy flashes like a live retail neon sign — built for checkout urgency, flash sales and 'Live…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Flashing "Order Now" Sign Text
Source: https://codefronts.com/motion/css-neon-text-effect/neon-flashing-order-now-sign-text/

An attention-grabbing storefront-style banner where the offer copy flashes like a live retail neon sign — built for checkout urgency, flash sales and 'Live Offer' bars. The exact 'active storefront' look conversion pages reach for.
## HTML
```html
<div class="cnt-02">
  <div class="cnt-02__plate">
    <p class="cnt-02__kicker">Kitchen closes at midnight</p>
    <h2 class="cnt-02__sign"><span class="cnt-02__word">ORDER</span> <span class="cnt-02__now">NOW</span></h2>
    <p class="cnt-02__sub">free delivery over $30 — tonight only</p>
  </div>
</div>
```
## CSS
```css
.cnt-02,
.cnt-02 *,
.cnt-02 *::before,
.cnt-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-02 ::selection {
  background: oklch(0.72 0.22 5);
  color: #fff;
}

.cnt-02 {
  --accent: oklch(0.72 0.24 8);
  --accent2: oklch(0.82 0.17 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: radial-gradient(130% 120% at 50% 15%,#161014,#0a0708 70%);
}

.cnt-02__plate {
  position: relative;
  text-align: center;
  padding: 44px 52px;
  border-radius: 16px;
  background: #0c0809;
  border: 1px solid #241519;
  box-shadow: 0 0 60px -10px color-mix(in oklch,var(--accent) 30%,transparent),0 40px 80px -40px #000;
}

.cnt-02__plate::before {
  content: "";
  position: absolute;
  inset: 10px;
  border-radius: 10px;
  border: 2px dashed color-mix(in oklch,var(--accent) 45%,#3a2a2e);
  pointer-events: none;
}

.cnt-02__kicker {
  font: 12px ui-monospace,Menlo,monospace;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--accent2) 60%,#6b5a3e);
  margin-bottom: 14px;
}

.cnt-02__sign {
  font-size: clamp(46px,10vw,88px);
  font-weight: 800;
  line-height: .92;
  letter-spacing: .04em;
  color: #fff5f6;
  display: flex;
  gap: .22em;
  justify-content: center;
}

.cnt-02__word {
  color: var(--accent);
  animation: cnt-02-flash 2.6s steps(1,end) infinite;
  text-shadow: 0 0 6px #fff,0 0 14px var(--accent),0 0 30px var(--accent),0 0 60px var(--accent);
}

.cnt-02__now {
  color: var(--accent2);
  animation: cnt-02-blink 1.3s steps(1,end) infinite .2s;
  text-shadow: 0 0 6px #fff,0 0 14px var(--accent2),0 0 32px var(--accent2),0 0 62px var(--accent2);
}

.cnt-02__sub {
  margin-top: 18px;
  font-size: 14px;
  letter-spacing: .04em;
  color: #a98d92;
}

@keyframes cnt-02-flash {
  0%,
    88%,
    100% {
    opacity: 1;
  }

  90%,
    94% {
    opacity: .28;
  }

  92% {
    opacity: 1;
  }
}

@keyframes cnt-02-blink {
  0%,
    55%,
    100% {
    opacity: 1;
  }

  60%,
    70% {
    opacity: .22;
  }

  65% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-02__word,
    .cnt-02__now {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two offset @keyframes create the live-storefront flicker. */
```

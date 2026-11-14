---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/insurance-quote-form-slide-in/"
title: "Insurance Quote Form Slide-In"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "An auto insurance quote widget where the form fields slide in sequentially from the left, then reveal an estimated monthly premium with a trust-signal strip…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Insurance Quote Form Slide-In
Source: https://codefronts.com/motion/css-slide-in-animation/insurance-quote-form-slide-in/

An auto insurance quote widget where the form fields slide in sequentially from the left, then reveal an estimated monthly premium with a trust-signal strip — the pattern used by Geico, Progressive, Lemonade, and modern insurtech landing pages.
## HTML
```html
<div class="sl-04">
  <div class="sl-04__card">
    <div class="sl-04__form">
      <span class="sl-04__eyebrow">Auto insurance quote</span>
      <h2>See your rate in 60 seconds</h2>
      <div class="sl-04__field">
        <label>ZIP code</label>
        <input type="text" value="90210" readonly>
      </div>
      <div class="sl-04__field">
        <label>Vehicle year</label>
        <select disabled><option>2022 Tesla Model Y</option></select>
      </div>
      <div class="sl-04__field">
        <label>Coverage level</label>
        <select disabled><option>Comprehensive + Collision</option></select>
      </div>
      <button class="sl-04__cta">Get my quote →</button>
      <div class="sl-04__trust">
        <span>★★★★★</span>
        <small>4.9/5 · 240K+ customers · A+ BBB rated</small>
      </div>
    </div>
    <div class="sl-04__result">
      <p class="sl-04__label">Estimated monthly premium</p>
      <div class="sl-04__amount">$127<small>/mo</small></div>
      <div class="sl-04__save">Save $54/mo vs your current provider</div>
      <ul class="sl-04__benefits">
        <li>✓ Same-day binding</li>
        <li>✓ 30-day money back</li>
        <li>✓ 24/7 claims support</li>
      </ul>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-04 {
  --bg: #f5f7fa;
  --card: #fff;
  --navy: #0a2540;
  --accent: #22c55e;
  --ink: #1a2540;
  --sub: #5c6b80;
  --line: #e5eaf0;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(70% 90% at 20% 0%, rgba(10,37,64,.06) 0%, transparent 55%), var(--bg);
  color: var(--ink);
}

.sl-04 *,
.sl-04 *::before,
.sl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-04 ::selection {
  background: var(--navy);
  color: #fff;
}

.sl-04__card {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 0;
  width: 100%;
  max-width: 820px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 24px 48px -20px rgba(10,37,64,.2);
}

.sl-04__form {
  padding: 32px 30px;
}

.sl-04__eyebrow {
  display: inline-block;
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--navy);
  margin-bottom: 8px;
  opacity: 0;
  animation: sl-04-in .55s cubic-bezier(.22,1,.36,1) .1s forwards;
}

.sl-04__form h2 {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 20px;
  opacity: 0;
  transform: translateX(-30px);
  animation: sl-04-slide .55s cubic-bezier(.22,1,.36,1) .2s forwards;
}

.sl-04__field {
  margin-bottom: 14px;
  opacity: 0;
  transform: translateX(-30px);
  animation: sl-04-slide .55s cubic-bezier(.22,1,.36,1) forwards;
}

.sl-04__field:nth-of-type(1) {
  animation-delay: .3s;
}

.sl-04__field:nth-of-type(2) {
  animation-delay: .4s;
}

.sl-04__field:nth-of-type(3) {
  animation-delay: .5s;
}

.sl-04__field label {
  display: block;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 4px;
}

.sl-04__field input,
.sl-04__field select {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fafbfc;
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  font-weight: 500;
}

.sl-04__cta {
  width: 100%;
  padding: 12px 22px;
  border: none;
  border-radius: 9px;
  background: var(--navy);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 700;
  cursor: pointer;
  margin-top: 12px;
  margin-bottom: 14px;
  opacity: 0;
  transform: translateX(-30px);
  animation: sl-04-slide .55s cubic-bezier(.22,1,.36,1) .6s forwards;
  transition: background .18s ease,transform .12s ease;
}

.sl-04__cta:hover {
  background: #0f3660;
}

.sl-04__trust {
  display: flex;
  align-items: center;
  gap: 8px;
  opacity: 0;
  animation: sl-04-in .55s cubic-bezier(.22,1,.36,1) .7s forwards;
}

.sl-04__trust span {
  color: #f59e0b;
  font-size: .85rem;
  letter-spacing: 1px;
}

.sl-04__trust small {
  font-size: .7rem;
  color: var(--sub);
  font-weight: 500;
}

.sl-04__result {
  padding: 32px 30px;
  background: linear-gradient(135deg,#0a2540,#0f3660);
  color: #fff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  opacity: 0;
  transform: translateX(30px);
  animation: sl-04-slide-right .6s cubic-bezier(.22,1,.36,1) .7s forwards;
}

.sl-04__label {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(255,255,255,.65);
  margin-bottom: 10px;
}

.sl-04__amount {
  font-size: 2.6rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1;
  margin-bottom: 6px;
  font-variant-numeric: tabular-nums;
}

.sl-04__amount small {
  font-size: .85rem;
  font-weight: 500;
  opacity: .7;
  margin-left: 4px;
}

.sl-04__save {
  display: inline-block;
  padding: 5px 12px;
  border-radius: 6px;
  background: rgba(34,197,94,.2);
  color: #a7f3d0;
  font-size: .72rem;
  font-weight: 700;
  margin-bottom: 20px;
  align-self: flex-start;
}

.sl-04__benefits {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sl-04__benefits li {
  font-size: .82rem;
  color: rgba(255,255,255,.85);
}

@keyframes sl-04-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes sl-04-slide {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes sl-04-slide-right {
  from {
    opacity: 0;
    transform: translateX(30px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-04 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 720px) {
  .sl-04__card {
    grid-template-columns: 1fr;
  }
}
```

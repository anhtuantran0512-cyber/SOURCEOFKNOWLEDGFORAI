---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/pure-css-stacked-card-testimonial-slider/"
title: "Pure CSS Stacked Card Testimonial Slider"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A compact social-proof widget built entirely with hidden radio inputs and the :checked selector — zero JavaScript and no heavy slider libraries."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Stacked Card Testimonial Slider
Source: https://codefronts.com/components/css-stacked-cards/pure-css-stacked-card-testimonial-slider/

A compact social-proof widget built entirely with hidden radio inputs and the :checked selector — zero JavaScript and no heavy slider libraries. The top review sits crisp while the next two peek behind it; clicking the dots cycles a card to the front. Perfect for landing-page testimonial sections where space is at a premium.
## HTML
```html
<div class="scd-30">
  <div class="scd-30__stage">
    <input type="radio" name="scd-30-t" id="scd-30-t1" class="scd-30__radio scd-30__radio--r1" checked>
    <input type="radio" name="scd-30-t" id="scd-30-t2" class="scd-30__radio scd-30__radio--r2">
    <input type="radio" name="scd-30-t" id="scd-30-t3" class="scd-30__radio scd-30__radio--r3">
    <div class="scd-30__slider">
      <div class="scd-30__quote scd-30__quote--q1"><p>&ldquo;This completely changed how our team ships. We cut launch time in half.&rdquo;</p><div class="scd-30__who"><span class="scd-30__av" style="background:linear-gradient(135deg,#ff9a3c,#ff5e62)"></span><div><h4>Maya Chen</h4><span>Head of Product, Loop</span></div></div></div>
      <div class="scd-30__quote scd-30__quote--q2"><p>&ldquo;Beautiful, fast, and genuinely a joy to use every single day.&rdquo;</p><div class="scd-30__who"><span class="scd-30__av" style="background:linear-gradient(135deg,#43cea2,#185a9d)"></span><div><h4>Theo Marsh</h4><span>Founder, Northbeam</span></div></div></div>
      <div class="scd-30__quote scd-30__quote--q3"><p>&ldquo;The support alone is worth it. Best decision we made this year.&rdquo;</p><div class="scd-30__who"><span class="scd-30__av" style="background:linear-gradient(135deg,#c471f5,#7f53ac)"></span><div><h4>Lena Ortiz</h4><span>CTO, Brightside</span></div></div></div>
    </div>
    <div class="scd-30__dots">
      <label for="scd-30-t1"></label><label for="scd-30-t2"></label><label for="scd-30-t3"></label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,500;1,6..72,400&family=Geist:wght@400;500;600&display=swap');

.scd-30,
.scd-30 *,
.scd-30 *::before,
.scd-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-30 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: linear-gradient(160deg,#fef6ee,#f4e4d4);
  font-family: 'Geist', sans-serif;
}

.scd-30__stage {
  position: relative;
}

.scd-30__radio {
  position: absolute;
  opacity: 0;
  pointer-events: none;
  width: 0;
  height: 0;
}

.scd-30__slider {
  position: relative;
  width: 330px;
  height: 300px;
}

.scd-30__quote {
  position: absolute;
  inset: 0;
  background: #fffdfa;
  border-radius: 22px;
  padding: 30px;
  box-shadow: 0 18px 40px rgba(120,80,50,.18);
  border: 1px solid #f0e2d2;
  transition: transform .6s cubic-bezier(.3,.9,.3,1), opacity .6s;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transform: translateY(28px) scale(.88);
  opacity: 0;
  z-index: 1;
}

.scd-30__quote p {
  font-family: 'Newsreader', serif;
  font-style: italic;
  font-size: 1.25rem;
  line-height: 1.45;
  color: #3a2e24;
}

.scd-30__who {
  display: flex;
  align-items: center;
  gap: 12px;
}

.scd-30__av {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  flex-shrink: 0;
  display: block;
}

.scd-30__who h4 {
  font-size: .9rem;
  font-weight: 600;
  color: #2a201a;
}

.scd-30__who span {
  font-size: .78rem;
  color: #9b7d5f;
}

.scd-30__radio--r1:checked ~ .scd-30__slider .scd-30__quote--q1,
.scd-30__radio--r2:checked ~ .scd-30__slider .scd-30__quote--q2,
.scd-30__radio--r3:checked ~ .scd-30__slider .scd-30__quote--q3 {
  transform: translateY(0) scale(1);
  opacity: 1;
  z-index: 4;
}

.scd-30__radio--r1:checked ~ .scd-30__slider .scd-30__quote--q2,
.scd-30__radio--r2:checked ~ .scd-30__slider .scd-30__quote--q3,
.scd-30__radio--r3:checked ~ .scd-30__slider .scd-30__quote--q1 {
  transform: translateY(14px) scale(.94);
  opacity: .55;
  z-index: 3;
}

.scd-30__radio--r1:checked ~ .scd-30__slider .scd-30__quote--q3,
.scd-30__radio--r2:checked ~ .scd-30__slider .scd-30__quote--q1,
.scd-30__radio--r3:checked ~ .scd-30__slider .scd-30__quote--q2 {
  transform: translateY(28px) scale(.88);
  opacity: .3;
  z-index: 2;
}

.scd-30__dots {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-top: 30px;
}

.scd-30__dots label {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: #d8c3aa;
  cursor: pointer;
  transition: background .3s, transform .3s;
}

.scd-30__dots label:hover {
  background: #c9a98a;
}

.scd-30__radio--r1:checked ~ .scd-30__dots label[for="scd-30-t1"],
.scd-30__radio--r2:checked ~ .scd-30__dots label[for="scd-30-t2"],
.scd-30__radio--r3:checked ~ .scd-30__dots label[for="scd-30-t3"] {
  background: #b8553f;
  transform: scale(1.3);
}

@media (prefers-reduced-motion: reduce) {
  .scd-30__quote,
    .scd-30__dots label {
    transition: none !important;
  }
}
```

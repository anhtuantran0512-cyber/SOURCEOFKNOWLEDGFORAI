---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/testimonial-customer-review-profile-card/"
title: "Testimonial Customer Review Profile Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A review card pairing a large quotation mark, an italic serif testimonial, a five-star rating and a reviewer row with circular avatar and company logo."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Testimonial Customer Review Profile Card
Source: https://codefronts.com/components/css-profile-cards/testimonial-customer-review-profile-card/

A review card pairing a large quotation mark, an italic serif testimonial, a five-star rating and a reviewer row with circular avatar and company logo.
## HTML
```html
<div class="pc-17">
  <div class="pc-17__card">
    <span class="pc-17__quote">&ldquo;</span>
    <p class="pc-17__text">The onboarding flow they designed cut our drop-off by 40%. Genuinely the best design partner we've worked with.</p>
    <div class="pc-17__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
    <div class="pc-17__person">
      <div class="pc-17__pfp">HP</div>
      <div class="pc-17__meta">
        <h4>Hannah Park</h4>
        <p>VP Product · Northwind</p>
      </div>
      <div class="pc-17__logo">N</div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-17,
.pc-17 *,
.pc-17 *::before,
.pc-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-17 ::selection {
  background: #ffb703;
  color: #111;
}

.pc-17 {
  font-family: 'Georgia',serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: radial-gradient(700px 500px at 50% -10%,#1a1d2e,#0b0d16);
  color: #f5f3ee;
}

.pc-17__card {
  position: relative;
  width: 100%;
  max-width: 400px;
  border-radius: 24px;
  padding: 38px 32px;
  background: linear-gradient(160deg,#151827,#10121d);
  border: 1px solid #23273a;
  box-shadow: 0 30px 70px -28px rgba(0,0,0,.85);
}

.pc-17__quote {
  position: absolute;
  top: 8px;
  left: 24px;
  font-size: 5rem;
  line-height: 1;
  color: #2a3050;
  font-family: Georgia,serif;
}

.pc-17__text {
  position: relative;
  font-size: 1.12rem;
  line-height: 1.6;
  font-style: italic;
  color: #e6e3db;
  margin-top: 26px;
  text-wrap: balance;
}

.pc-17__stars {
  color: #ffb703;
  font-size: 1.05rem;
  letter-spacing: 3px;
  margin-top: 20px;
  font-family: sans-serif;
}

.pc-17__person {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 24px;
  padding-top: 22px;
  border-top: 1px solid #23273a;
}

.pc-17__pfp {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  flex-shrink: 0;
  display: grid;
  place-items: center;
  font-family: sans-serif;
  font-weight: 800;
  font-size: 1.05rem;
  color: #111;
  background: linear-gradient(145deg,#ffb703,#fb8500);
}

.pc-17__meta {
  flex: 1;
  font-family: sans-serif;
}

.pc-17__meta h4 {
  font-size: 1rem;
  font-weight: 800;
}

.pc-17__meta p {
  font-size: .78rem;
  color: #9096ad;
  margin-top: 2px;
  font-style: normal;
}

.pc-17__logo {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-family: sans-serif;
  font-weight: 800;
  color: #8b93b5;
  background: #1c2033;
  border: 1px solid #2a3050;
}

@media (prefers-reduced-motion: reduce) {
  .pc-17 * {
    animation: none!important;
  }
}
```

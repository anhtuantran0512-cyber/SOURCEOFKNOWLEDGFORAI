---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/flexbox-e-commerce-hire-me-badge-card/"
title: "Flexbox E-commerce Hire-Me Badge Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A freelancer marketplace card with a landscape flex layout, live online-status dot, hourly-rate chip, rating tags and a prominent Hire Me action."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flexbox E-commerce Hire-Me Badge Card
Source: https://codefronts.com/components/css-profile-cards/flexbox-e-commerce-hire-me-badge-card/

A freelancer marketplace card with a landscape flex layout, live online-status dot, hourly-rate chip, rating tags and a prominent Hire Me action.
## HTML
```html
<div class="pc-16">
  <div class="pc-16__card">
    <div class="pc-16__left">
      <div class="pc-16__pfp">FA</div>
      <span class="pc-16__status"><i></i>Online</span>
    </div>
    <div class="pc-16__right">
      <div class="pc-16__top">
        <div>
          <h3>Farah Aziz</h3>
          <p>Brand & Motion Designer</p>
        </div>
        <span class="pc-16__rate">$85<small>/hr</small></span>
      </div>
      <p class="pc-16__bio">7+ years crafting identities for startups. Available for select freelance projects this quarter.</p>
      <div class="pc-16__tags"><span>&#9733; 4.96</span><span>142 jobs</span><span>Top Rated</span></div>
      <div class="pc-16__actions">
        <button class="pc-16__hire">Hire Me</button>
        <button class="pc-16__save" aria-label="Save">&#9829;</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-16,
.pc-16 *,
.pc-16 *::before,
.pc-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-16 ::selection {
  background: #14a800;
  color: #fff;
}

.pc-16 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #0d1310;
  color: #e8f0ea;
}

.pc-16__card {
  display: flex;
  gap: 22px;
  width: 100%;
  max-width: 480px;
  border-radius: 22px;
  padding: 26px;
  background: #131a15;
  border: 1px solid #1f2c22;
  box-shadow: 0 24px 60px -26px rgba(0,0,0,.8);
}

.pc-16__left {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.pc-16__pfp {
  width: 92px;
  height: 92px;
  border-radius: 24px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.7rem;
  color: #fff;
  background: linear-gradient(145deg,#14a800,#4fd35b);
  box-shadow: 0 12px 28px -10px #14a800;
}

.pc-16__status {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: .74rem;
  color: #8fb89a;
}

.pc-16__status i {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #4fd35b;
  box-shadow: 0 0 8px #4fd35b;
  animation: pc-16-blink 2s ease-in-out infinite;
}

@keyframes pc-16-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .35;
  }
}

.pc-16__right {
  flex: 1;
  min-width: 0;
}

.pc-16__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.pc-16__top h3 {
  font-size: 1.3rem;
  font-weight: 800;
}

.pc-16__top p {
  color: #8fb89a;
  font-size: .84rem;
  margin-top: 2px;
}

.pc-16__rate {
  font-size: 1.35rem;
  font-weight: 800;
  color: #4fd35b;
  white-space: nowrap;
}

.pc-16__rate small {
  font-size: .7rem;
  color: #8fb89a;
  font-weight: 600;
}

.pc-16__bio {
  font-size: .84rem;
  line-height: 1.5;
  color: #c3d6c9;
  margin-top: 12px;
  text-wrap: balance;
}

.pc-16__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}

.pc-16__tags span {
  font-size: .72rem;
  padding: 5px 11px;
  border-radius: 20px;
  background: #1a271e;
  border: 1px solid #26382c;
  color: #a9c9b2;
}

.pc-16__actions {
  display: flex;
  gap: 10px;
  margin-top: 18px;
}

.pc-16__hire {
  flex: 1;
  padding: 12px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  font-size: .88rem;
  color: #fff;
  background: #14a800;
  transition: background .25s,transform .2s;
}

.pc-16__hire:hover {
  background: #108500;
}

.pc-16__hire:active {
  transform: scale(.98);
}

.pc-16__save {
  width: 46px;
  border: 1px solid #26382c;
  border-radius: 12px;
  cursor: pointer;
  background: #1a271e;
  color: #4fd35b;
  font-size: 1rem;
  transition: background .25s;
}

.pc-16__save:hover {
  background: #22352a;
}

@media (max-width: 440px) {
  .pc-16__card {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .pc-16__top {
    flex-direction: column;
    align-items: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pc-16 * {
    animation: none!important;
    transition: none!important;
  }
}
```

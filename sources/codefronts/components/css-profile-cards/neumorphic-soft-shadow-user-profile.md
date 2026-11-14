---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/neumorphic-soft-shadow-user-profile/"
title: "Neumorphic Soft-Shadow User Profile"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A soft-UI profile card built entirely from dual light/dark box-shadows, with an extruded avatar, inset stat wells and a button that presses inward on click."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft-Shadow User Profile
Source: https://codefronts.com/components/css-profile-cards/neumorphic-soft-shadow-user-profile/

A soft-UI profile card built entirely from dual light/dark box-shadows, with an extruded avatar, inset stat wells and a button that presses inward on click.
## HTML
```html
<div class="pc-12">
  <div class="pc-12__card">
    <div class="pc-12__pfp">GS</div>
    <h3>Grace Sullivan</h3>
    <p class="pc-12__role">UX Researcher</p>
    <p class="pc-12__bio">Turning user interviews into product clarity for fintech teams.</p>
    <div class="pc-12__row">
      <div class="pc-12__stat"><b>84</b><span>Studies</span></div>
      <div class="pc-12__stat"><b>15</b><span>Years</span></div>
    </div>
    <button class="pc-12__cta">Get in touch</button>
  </div>
</div>
```
## CSS
```css
.pc-12,
.pc-12 *,
.pc-12 *::before,
.pc-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-12 ::selection {
  background: #a3b1c6;
  color: #fff;
}

.pc-12 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #e0e5ec;
  color: #3a4256;
}

.pc-12__card {
  width: 300px;
  padding: 34px 28px;
  text-align: center;
  border-radius: 28px;
  background: #e0e5ec;
  box-shadow: 12px 12px 24px #b8bec9,-12px -12px 24px #ffffff;
}

.pc-12__pfp {
  width: 96px;
  height: 96px;
  border-radius: 50%;
  margin: 0 auto 20px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.7rem;
  color: #5b6478;
  background: #e0e5ec;
  box-shadow: inset 6px 6px 12px #b8bec9,inset -6px -6px 12px #ffffff;
}

.pc-12__card h3 {
  font-size: 1.4rem;
  font-weight: 800;
  color: #2e3546;
}

.pc-12__role {
  font-size: .86rem;
  color: #8992a5;
  margin-top: 3px;
}

.pc-12__bio {
  font-size: .84rem;
  line-height: 1.5;
  color: #6b7488;
  margin-top: 14px;
  text-wrap: balance;
}

.pc-12__row {
  display: flex;
  gap: 14px;
  margin: 22px 0;
}

.pc-12__stat {
  flex: 1;
  padding: 14px 8px;
  border-radius: 16px;
  background: #e0e5ec;
  box-shadow: inset 4px 4px 8px #b8bec9,inset -4px -4px 8px #ffffff;
}

.pc-12__stat b {
  display: block;
  font-size: 1.25rem;
  font-weight: 800;
  color: #2e3546;
}

.pc-12__stat span {
  font-size: .68rem;
  color: #8992a5;
}

.pc-12__cta {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 16px;
  cursor: pointer;
  font-weight: 700;
  font-size: .88rem;
  color: #5b6478;
  background: #e0e5ec;
  box-shadow: 6px 6px 12px #b8bec9,-6px -6px 12px #ffffff;
  transition: box-shadow .2s,color .2s;
}

.pc-12__cta:hover {
  color: #4a7cff;
}

.pc-12__cta:active {
  box-shadow: inset 5px 5px 10px #b8bec9,inset -5px -5px 10px #ffffff;
}

@media (prefers-reduced-motion: reduce) {
  .pc-12 * {
    transition: none!important;
  }
}
```

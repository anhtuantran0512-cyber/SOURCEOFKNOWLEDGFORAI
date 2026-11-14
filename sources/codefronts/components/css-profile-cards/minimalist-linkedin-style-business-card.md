---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/minimalist-linkedin-style-business-card/"
title: "Minimalist LinkedIn-style Business Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A flat, high-contrast professional card with a gradient header strip, verified badge, overlapping connection avatars and pill action buttons."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist LinkedIn-style Business Card
Source: https://codefronts.com/components/css-profile-cards/minimalist-linkedin-style-business-card/

A flat, high-contrast professional card with a gradient header strip, verified badge, overlapping connection avatars and pill action buttons.
## HTML
```html
<div class="pc-10">
  <div class="pc-10__card">
    <div class="pc-10__pfp">RM</div>
    <div class="pc-10__body">
      <div class="pc-10__namerow">
        <h3>Robin Mercer</h3>
        <span class="pc-10__verified" title="Verified">&#10004;</span>
      </div>
      <p class="pc-10__role">Senior Staff Engineer at Vertex</p>
      <p class="pc-10__loc">&#128205; San Francisco Bay Area</p>
      <div class="pc-10__conn"><span></span><span></span><span></span><p>500+ connections</p></div>
      <div class="pc-10__actions">
        <button class="pc-10__primary">Connect</button>
        <button class="pc-10__secondary">Message</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-10,
.pc-10 *,
.pc-10 *::before,
.pc-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-10 ::selection {
  background: #0a66c2;
  color: #fff;
}

.pc-10 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #eef3f8;
  color: #1d2226;
}

.pc-10__card {
  width: 340px;
  border-radius: 16px;
  overflow: hidden;
  background: #fff;
  border: 1px solid #dce3ea;
  box-shadow: 0 10px 30px -12px rgba(0,40,80,.2);
  transition: box-shadow .3s;
}

.pc-10__card:hover {
  box-shadow: 0 18px 44px -14px rgba(0,40,80,.3);
}

.pc-10__pfp {
  height: 88px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.5rem;
  color: #fff;
  background: linear-gradient(120deg,#0a66c2,#3f9cff);
  position: relative;
}

.pc-10__pfp::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(120deg,transparent 40%,rgba(255,255,255,.15));
}

.pc-10__body {
  padding: 22px;
}

.pc-10__namerow {
  display: flex;
  align-items: center;
  gap: 7px;
}

.pc-10__namerow h3 {
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -.01em;
}

.pc-10__verified {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #0a66c2;
  color: #fff;
  font-size: .6rem;
  display: grid;
  place-items: center;
}

.pc-10__role {
  font-size: .9rem;
  color: #3d4b57;
  margin-top: 5px;
  line-height: 1.4;
}

.pc-10__loc {
  font-size: .8rem;
  color: #8a97a3;
  margin-top: 6px;
}

.pc-10__conn {
  display: flex;
  align-items: center;
  gap: 0;
  margin-top: 16px;
}

.pc-10__conn span {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 2px solid #fff;
  margin-left: -6px;
}

.pc-10__conn span:nth-child(1) {
  background: #f4a261;
  margin-left: 0;
}

.pc-10__conn span:nth-child(2) {
  background: #2a9d8f;
}

.pc-10__conn span:nth-child(3) {
  background: #e76f51;
}

.pc-10__conn p {
  font-size: .78rem;
  color: #0a66c2;
  font-weight: 600;
  margin-left: 10px;
}

.pc-10__actions {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.pc-10__primary {
  flex: 1;
  padding: 10px;
  border-radius: 22px;
  border: none;
  cursor: pointer;
  font-weight: 700;
  font-size: .86rem;
  color: #fff;
  background: #0a66c2;
  transition: background .25s;
}

.pc-10__primary:hover {
  background: #084c92;
}

.pc-10__secondary {
  flex: 1;
  padding: 10px;
  border-radius: 22px;
  cursor: pointer;
  font-weight: 700;
  font-size: .86rem;
  color: #0a66c2;
  background: #fff;
  border: 1.5px solid #0a66c2;
  transition: background .25s;
}

.pc-10__secondary:hover {
  background: #eaf3fb;
}

@media (prefers-reduced-motion: reduce) {
  .pc-10 * {
    transition: none!important;
  }
}
```

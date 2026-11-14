---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/saas-user-dropdown-profile-card/"
title: "SaaS User Dropdown Profile Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "The avatar-triggered account menu from a dashboard navbar: a glassy dropdown with profile summary, plan badge and menu items that springs open on hover or…"
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS User Dropdown Profile Card
Source: https://codefronts.com/components/css-profile-cards/saas-user-dropdown-profile-card/

The avatar-triggered account menu from a dashboard navbar: a glassy dropdown with profile summary, plan badge and menu items that springs open on hover or focus.
## HTML
```html
<div class="pc-20">
  <div class="pc-20__nav">
    <div class="pc-20__brand"><span class="pc-20__logo">V</span>Vertex</div>
    <div class="pc-20__menu" tabindex="0">
      <button class="pc-20__trigger" aria-label="Account menu">
        <span class="pc-20__mini">DP</span>
        <span class="pc-20__caret">&#9662;</span>
      </button>
      <div class="pc-20__dropdown">
        <div class="pc-20__profile">
          <div class="pc-20__pfp">DP</div>
          <div>
            <h4>Dana Prescott</h4>
            <p>[email protected]</p>
          </div>
        </div>
        <div class="pc-20__plan"><span>Pro plan</span><em>Active</em></div>
        <nav class="pc-20__items">
          <a><span>&#9881;</span>Settings</a>
          <a><span>&#9993;</span>Notifications</a>
          <a><span>&#128179;</span>Billing</a>
          <a><span>&#63;</span>Help &amp; Support</a>
        </nav>
        <a class="pc-20__signout"><span>&#8592;</span>Sign out</a>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-20,
.pc-20 *,
.pc-20 *::before,
.pc-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-20 ::selection {
  background: #6366f1;
  color: #fff;
}

.pc-20 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 40px 20px;
  background: #0b0d18;
  color: #e7e9f5;
}

.pc-20__nav {
  width: 100%;
  max-width: 520px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 18px;
  border-radius: 16px;
  background: #12142280;
  border: 1px solid #22263c;
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.pc-20__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 800;
  font-size: 1.05rem;
}

.pc-20__logo {
  width: 30px;
  height: 30px;
  border-radius: 9px;
  display: grid;
  place-items: center;
  color: #fff;
  background: linear-gradient(145deg,#6366f1,#a855f7);
}

.pc-20__menu {
  position: relative;
}

.pc-20__trigger {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  padding: 6px 10px 6px 6px;
  border-radius: 30px;
  background: #1a1d30;
  border: 1px solid #2a2e47;
  color: inherit;
  transition: background .25s;
}

.pc-20__trigger:hover {
  background: #22263c;
}

.pc-20__mini {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: .78rem;
  color: #fff;
  background: linear-gradient(145deg,#6366f1,#ec4899);
}

.pc-20__caret {
  font-size: .7rem;
  color: #9aa0c0;
  transition: transform .3s;
}

.pc-20__menu:hover .pc-20__caret,
.pc-20__menu:focus-within .pc-20__caret {
  transform: rotate(180deg);
}

.pc-20__dropdown {
  position: absolute;
  top: calc(100% + 12px);
  right: 0;
  width: 280px;
  padding: 16px;
  border-radius: 18px;
  z-index: 10;
  background: #141728;
  border: 1px solid #262a42;
  box-shadow: 0 24px 60px -20px rgba(0,0,0,.85);
  opacity: 0;
  transform: translateY(-8px) scale(.97);
  transform-origin: top right;
  pointer-events: none;
  transition: opacity .28s cubic-bezier(.2,.8,.2,1),transform .28s cubic-bezier(.2,.8,.2,1);
}

.pc-20__menu:hover .pc-20__dropdown,
.pc-20__menu:focus-within .pc-20__dropdown {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}

.pc-20__profile {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-bottom: 14px;
  border-bottom: 1px solid #262a42;
}

.pc-20__pfp {
  width: 46px;
  height: 46px;
  border-radius: 14px;
  display: grid;
  place-items: center;
  font-weight: 800;
  color: #fff;
  background: linear-gradient(145deg,#6366f1,#ec4899);
}

.pc-20__profile h4 {
  font-size: .95rem;
  font-weight: 800;
}

.pc-20__profile p {
  font-size: .76rem;
  color: #9aa0c0;
  margin-top: 1px;
}

.pc-20__plan {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 12px 0;
  padding: 9px 12px;
  border-radius: 11px;
  background: #1a1d30;
  font-size: .8rem;
}

.pc-20__plan em {
  font-style: normal;
  font-size: .7rem;
  color: #34d399;
  background: #0e3226;
  padding: 3px 9px;
  border-radius: 20px;
}

.pc-20__items {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.pc-20__items a,
.pc-20__signout {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 10px 12px;
  border-radius: 10px;
  font-size: .85rem;
  color: #c4c8dd;
  cursor: pointer;
  transition: background .2s,color .2s;
}

.pc-20__items a span,
.pc-20__signout span {
  width: 18px;
  text-align: center;
  opacity: .8;
}

.pc-20__items a:hover {
  background: #1e2136;
  color: #fff;
}

.pc-20__signout {
  margin-top: 8px;
  padding-top: 12px;
  border-top: 1px solid #262a42;
  color: #f87171;
  border-radius: 0 0 10px 10px;
}

.pc-20__signout:hover {
  color: #fca5a5;
}

@media (prefers-reduced-motion: reduce) {
  .pc-20 * {
    transition: none!important;
  }
}
```

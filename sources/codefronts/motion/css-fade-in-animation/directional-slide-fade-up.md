---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/directional-slide-fade-up/"
title: "Directional Slide-Fade Up"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "A two-column feature section where the text block slides up from below while card items follow with sequential translateY(30px → 0) + opacity delays for a…"
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Directional Slide-Fade Up
Source: https://codefronts.com/motion/css-fade-in-animation/directional-slide-fade-up/

A two-column feature section where the text block slides up from below while card items follow with sequential translateY(30px → 0) + opacity delays for a rising-content effect.
## HTML
```html
<div class="fi-06">
  <div class="fi-06__left">
    <div class="fi-06__eyebrow">Premium Features</div>
    <h2 class="fi-06__heading">Everything you need to ship faster</h2>
    <p class="fi-06__body">Components slide into view from below as the page loads, creating a sense of content rising to meet the reader — directional fade with translateY.</p>
    <a href="#" class="fi-06__link">Explore features →</a>
  </div>
  <div class="fi-06__right">
    <div class="fi-06__card">
      <div class="fi-06__icon">⚡</div>
      <div><div class="fi-06__cname">Lightning Build</div><div class="fi-06__cmeta">Zero-config bundling</div></div>
    </div>
    <div class="fi-06__card">
      <div class="fi-06__icon">🎨</div>
      <div><div class="fi-06__cname">Design Tokens</div><div class="fi-06__cmeta">CSS custom properties</div></div>
    </div>
    <div class="fi-06__card">
      <div class="fi-06__icon">🔒</div>
      <div><div class="fi-06__cname">Auth Built-in</div><div class="fi-06__cmeta">JWT + OAuth 2.0</div></div>
    </div>
  </div>
</div>
```
## CSS
```css
.fi-06 {
  --bg: #0e0a1a;
  --violet: #7c3aed;
  --indigo: #4f46e5;
  --text: #ede9fe;
  font-family: 'DM Sans',sans-serif;
  min-height: 340px;
  border-radius: 20px;
  padding: 40px;
  overflow: hidden;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  align-items: center;
}

.fi-06 *,
.fi-06 *::before,
.fi-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-06 ::selection {
  background: var(--violet);
  color: #fff;
}
/* slide-fade from below: translateY(40px) opacity:0 → Y(0) opacity:1 */

.fi-06__left {
  opacity: 0;
  transform: translateY(40px);
  animation: fi-06-up .8s cubic-bezier(.16,1,.3,1) .1s forwards;
}

.fi-06__eyebrow {
  font-size: .7rem;
  font-weight: 500;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--violet);
  margin-bottom: 14px;
}

.fi-06__heading {
  font-family: 'Syne',sans-serif;
  font-size: clamp(1.6rem,3vw,2.4rem);
  font-weight: 800;
  color: var(--text);
  line-height: 1.15;
  margin-bottom: 14px;
}

.fi-06__body {
  font-size: .9rem;
  color: rgba(237,233,254,.5);
  line-height: 1.7;
  margin-bottom: 20px;
}

.fi-06__link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: .85rem;
  font-weight: 600;
  color: var(--violet);
  text-decoration: none;
  border-bottom: 1px solid rgba(124,58,237,.3);
  padding-bottom: 2px;
  transition: border-color .2s;
}

.fi-06__link:hover {
  border-color: var(--violet);
}

.fi-06__right {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.fi-06__card {
  background: linear-gradient(135deg,rgba(124,58,237,.1),rgba(79,70,229,.06));
  border: 1px solid rgba(124,58,237,.2);
  border-radius: 12px;
  padding: 16px 20px;
  display: flex;
  gap: 14px;
  align-items: center;
  opacity: 0;
  transform: translateY(30px);
}

.fi-06__card:nth-child(1) {
  animation: fi-06-up .7s cubic-bezier(.16,1,.3,1) .3s forwards;
}

.fi-06__card:nth-child(2) {
  animation: fi-06-up .7s cubic-bezier(.16,1,.3,1) .45s forwards;
}

.fi-06__card:nth-child(3) {
  animation: fi-06-up .7s cubic-bezier(.16,1,.3,1) .6s forwards;
}

.fi-06__icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: rgba(124,58,237,.2);
  display: grid;
  place-items: center;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.fi-06__cname {
  font-size: .88rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 2px;
}

.fi-06__cmeta {
  font-size: .72rem;
  color: rgba(237,233,254,.4);
}

@keyframes fi-06-up {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-06 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```

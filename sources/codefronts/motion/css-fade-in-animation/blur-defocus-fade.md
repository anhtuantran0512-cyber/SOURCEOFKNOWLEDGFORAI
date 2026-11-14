---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/blur-defocus-fade/"
title: "Blur Defocus Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "A feature card that emerges from a dreamlike haze using filter: blur(20px) combined with opacity: 0, animating to sharp focus — the cinematographic…"
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blur Defocus Fade
Source: https://codefronts.com/motion/css-fade-in-animation/blur-defocus-fade/

A feature card that emerges from a dreamlike haze using filter: blur(20px) combined with opacity: 0, animating to sharp focus — the cinematographic rack-focus in pure CSS.
## HTML
```html
<div class="fi-03">
  <div class="fi-03__card">
    <div class="fi-03__icon">✦</div>
    <h2 class="fi-03__title">Blur-to-Focus Reveal</h2>
    <p class="fi-03__sub">Elements emerge from a dreamlike haze into sharp clarity using CSS <code>filter: blur()</code> combined with opacity — the cinematographic focus pull, in pure CSS.</p>
    <div class="fi-03__tags">
      <span class="fi-03__tag">filter: blur()</span>
      <span class="fi-03__tag">opacity fade</span>
      <span class="fi-03__tag">Pure CSS</span>
    </div>
  </div>
</div>
```
## CSS
```css
.fi-03 {
  --bg: #0d0f1a;
  --purple: #a855f7;
  --pink: #ec4899;
  --text: #f8f0ff;
  font-family: 'Plus Jakarta Sans',sans-serif;
  min-height: 320px;
  border-radius: 20px;
  display: grid;
  place-items: center;
  padding: 40px;
  overflow: hidden;
}

.fi-03 *,
.fi-03 *::before,
.fi-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-03 ::selection {
  background: var(--purple);
  color: #fff;
}
/* blur fade: filter:blur(20px) opacity:0 → blur(0) opacity:1 */

.fi-03__card {
  background: linear-gradient(135deg,rgba(168,85,247,.1),rgba(236,72,153,.08));
  border: 1px solid rgba(168,85,247,.25);
  border-radius: 20px;
  padding: 36px;
  max-width: 480px;
  text-align: center;
  opacity: 0;
  filter: blur(20px);
  animation: fi-03-blur-in 1s cubic-bezier(.4,0,.2,1) .15s forwards;
}

.fi-03__icon {
  width: 64px;
  height: 64px;
  border-radius: 18px;
  background: linear-gradient(135deg,var(--purple),var(--pink));
  display: grid;
  place-items: center;
  font-size: 1.8rem;
  margin: 0 auto 20px;
  box-shadow: 0 8px 32px rgba(168,85,247,.4);
}

.fi-03__title {
  font-size: clamp(1.4rem,3vw,2rem);
  font-weight: 800;
  color: var(--text);
  margin-bottom: 10px;
}

.fi-03__sub {
  font-size: .9rem;
  color: rgba(248,240,255,.55);
  line-height: 1.6;
  margin-bottom: 24px;
}

.fi-03__tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  justify-content: center;
}

.fi-03__tag {
  padding: 5px 14px;
  border-radius: 20px;
  font-size: .75rem;
  font-weight: 700;
  background: rgba(168,85,247,.15);
  color: var(--purple);
  border: 1px solid rgba(168,85,247,.2);
}

.fi-03__tag:nth-child(2) {
  background: rgba(236,72,153,.15);
  color: var(--pink);
  border-color: rgba(236,72,153,.2);
}

.fi-03__tag:nth-child(3) {
  background: rgba(168,85,247,.1);
  color: rgba(248,240,255,.7);
  border-color: rgba(255,255,255,.1);
}

@keyframes fi-03-blur-in {
  to {
    opacity: 1;
    filter: blur(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-03__card {
    animation: none;
    opacity: 1;
    filter: none;
  }
}
```

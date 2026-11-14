---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/layered-glass-profile-card/"
title: "Layered Glass Profile Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A bio / profile card with skeuomorphic depth: the circular avatar breaks out and overlaps the top rim of the frosted glass panel, casting a soft shadow onto…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Layered Glass Profile Card
Source: https://codefronts.com/components/css-liquid-glass-cards/layered-glass-profile-card/

A bio / profile card with skeuomorphic depth: the circular avatar breaks out and overlaps the top rim of the frosted glass panel, casting a soft shadow onto the glass so the two layers read as physically stacked. A subtle tilt-on-hover adds parallax between the avatar and the pane.
## HTML
```html
<section class="lg-05" aria-label="Layered glass profile card demo">
  <article class="lg-05__card">
    <div class="lg-05__avatar" role="img" aria-label="Avatar of Mara Vance">MV</div>
    <div class="lg-05__panel">
      <h3 class="lg-05__name">Mara Vance <span class="lg-05__verified" aria-label="Verified">✓</span></h3>
      <p class="lg-05__role">Product Designer · Auckland</p>
      <div class="lg-05__stats"><span><b>248</b> posts</span><span><b>18.2k</b> followers</span><span><b>412</b> following</span></div>
      <button class="lg-05__follow" type="button">Follow</button>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-05,
.lg-05 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-05 {
  --accent: oklch(0.66 0.19 250);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  perspective: 1000px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 20% 0%,#22d3ee,#3b82f6 45%,#1e1b4b);
}

.lg-05__card {
  position: relative;
  width: min(300px,100%);
  margin-top: 52px;
  transform-style: preserve-3d;
  transition: transform .5s ease;
}

.lg-05__card:hover {
  transform: rotateX(6deg) rotateY(-6deg);
}

.lg-05__avatar {
  position: absolute;
  top: -46px;
  left: 50%;
  transform: translateX(-50%) translateZ(50px);
  width: 92px;
  height: 92px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 30px;
  font-weight: 800;
  color: #fff;
  background: repeating-linear-gradient(45deg,#334155,#334155 8px,#475569 8px,#475569 16px);
  border: 3px solid rgba(255,255,255,.7);
  box-shadow: 0 16px 30px -10px rgba(0,0,0,.7);
}

.lg-05__panel {
  padding: 60px 24px 24px;
  border-radius: 24px;
  text-align: center;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 13%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),0 30px 60px -30px rgba(0,0,0,.75);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
}

.lg-05__name {
  font-size: 20px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
}

.lg-05__verified {
  width: 20px;
  height: 20px;
  font-size: 12px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
}

.lg-05__role {
  font-size: 13px;
  color: rgba(255,255,255,.8);
  margin-top: 5px;
}

.lg-05__stats {
  display: flex;
  justify-content: space-between;
  gap: 6px;
  margin: 18px 0;
  padding: 12px;
  border-radius: 14px;
  background: rgba(255,255,255,.12);
  font-size: 12px;
  color: rgba(255,255,255,.85);
}

.lg-05__stats b {
  display: block;
  font-size: 16px;
  color: #fff;
}

.lg-05__follow {
  width: 100%;
  min-height: 44px;
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  font-size: 15px;
  color: #fff;
  background: var(--accent);
  box-shadow: 0 10px 24px -10px var(--accent);
}

.lg-05__follow:hover {
  filter: brightness(1.08);
}

.lg-05__follow:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-05__card {
    transition: none;
  }

  .lg-05__card:hover {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the avatar is a sibling that straddles the panel's top edge with a shadow cast onto the glass, and the hover tilt is a CSS perspective transform with preserve-3d parallax. */
```

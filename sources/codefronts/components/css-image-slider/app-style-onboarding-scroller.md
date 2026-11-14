---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/app-style-onboarding-scroller/"
title: "App-Style Onboarding Scroller"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "App-style onboarding scroller — viewport-locked onboarding flow styled like a native iOS/Android intro with full-bleed screens, imagery, welcome copy, and…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: App-Style Onboarding Scroller
Source: https://codefronts.com/components/css-image-slider/app-style-onboarding-scroller/

App-style onboarding scroller — viewport-locked onboarding flow styled like a native iOS/Android intro with full-bleed screens, imagery, welcome copy, and Skip / Next actions, swiped through with scroll-snap inside a phone frame. The exact pattern Notion, Linear, Superhuman, and Stripe Atlas ship on their /welcome and product-tour routes to drive trial-to-paid activation. No JavaScript, no react-onboarding-flow (18KB) or intro.js (32KB) dependency.
## HTML
```html
<div class="cis-17">
  <div class="cis-17__phone">
    <div class="cis-17__notch"></div>
    <div class="cis-17__track">
      <section class="cis-17__screen" id="cis-17-1">
        <div class="cis-17__art"><img src="https://picsum.photos/seed/cis17a/700/900" alt="Welcome illustration"></div>
        <div class="cis-17__body"><h2>Welcome to Drift</h2><p>Plan trips, split costs and keep everyone in the loop.</p>
          <div class="cis-17__row"><a class="cis-17__skip" href="#cis-17-3">Skip</a><a class="cis-17__next" href="#cis-17-2">Next</a></div></div>
      </section>
      <section class="cis-17__screen" id="cis-17-2">
        <div class="cis-17__art"><img src="https://picsum.photos/seed/cis17b/700/900" alt="Sync illustration"></div>
        <div class="cis-17__body"><h2>Everything syncs</h2><p>Changes show up instantly for every traveller on the trip.</p>
          <div class="cis-17__row"><a class="cis-17__skip" href="#cis-17-3">Skip</a><a class="cis-17__next" href="#cis-17-3">Next</a></div></div>
      </section>
      <section class="cis-17__screen" id="cis-17-3">
        <div class="cis-17__art"><img src="https://picsum.photos/seed/cis17c/700/900" alt="Ready illustration"></div>
        <div class="cis-17__body"><h2>You're all set</h2><p>Create your first trip and invite the crew.</p>
          <div class="cis-17__row"><a class="cis-17__start" href="#cis-17-1">Get started</a></div></div>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
.cis-17,
.cis-17 *,
.cis-17 *::before,
.cis-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-17 ::selection {
  background: oklch(0.8 0.15 285);
  color: #0c0620;
}

.cis-17 {
  --accent: oklch(0.7 0.16 285);
  --w: 300px;
  --h: 600px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f3f1fa;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background: radial-gradient(120% 120% at 50% 0%,#120e22,#08060f);
}

.cis-17__phone {
  position: relative;
  width: var(--w);
  height: var(--h);
  border-radius: 44px;
  padding: 10px;
  background: #0b0910;
  border: 1px solid #2a2440;
  box-shadow: 0 40px 90px -40px #000,inset 0 0 0 2px #16122a;
}

.cis-17__notch {
  position: absolute;
  top: 16px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 5;
  width: 110px;
  height: 26px;
  border-radius: 0 0 16px 16px;
  background: #0b0910;
}

.cis-17__track {
  display: flex;
  width: 100%;
  height: 100%;
  border-radius: 36px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-width: none;
}

.cis-17__track::-webkit-scrollbar {
  display: none;
}

.cis-17__screen {
  position: relative;
  flex: 0 0 100%;
  scroll-snap-align: center;
  display: flex;
  flex-direction: column;
}

.cis-17__art {
  flex: 1;
  overflow: hidden;
}

.cis-17__art img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-17__body {
  padding: 24px 22px 30px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  background: linear-gradient(180deg,transparent,#0b0910 22%);
  margin-top: -60px;
  position: relative;
}

.cis-17__body h2 {
  font-size: 23px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cis-17__body p {
  font-size: 14px;
  line-height: 1.5;
  color: #b3accb;
}

.cis-17__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 14px;
}

.cis-17__skip {
  font-size: 14px;
  font-weight: 600;
  color: #8f88a8;
  text-decoration: none;
}

.cis-17__next,
.cis-17__start {
  text-decoration: none;
  font-size: 14px;
  font-weight: 700;
  color: #0c0620;
  background: var(--accent);
  padding: 11px 22px;
  border-radius: 12px;
  transition: filter .2s;
}

.cis-17__start {
  width: 100%;
  text-align: center;
}

.cis-17__next:hover,
.cis-17__start:hover {
  filter: brightness(1.1);
}

@supports (scroll-marker-group: after) {
  .cis-17__track {
    scroll-marker-group: after;
  }

  .cis-17__track::scroll-marker-group {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 88px;
    display: flex;
    gap: 7px;
    justify-content: center;
  }

  .cis-17__screen::scroll-marker {
    content: "";
    width: 7px;
    height: 7px;
    border-radius: 50%;
    border: 0;
    background: rgba(255,255,255,.3);
    transition: width .25s,background .25s;
  }

  .cis-17__screen::scroll-marker:target-current {
    background: var(--accent);
    width: 20px;
    border-radius: 4px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-17__track {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — scroll-snap track with anchor-link Next/Skip navigation. */
```

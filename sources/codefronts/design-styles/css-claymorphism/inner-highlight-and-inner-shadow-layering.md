---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/inner-highlight-and-inner-shadow-layering/"
title: "Inner Highlight and Inner Shadow Layering"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Isolate the two inset layers and the material becomes obvious: highlight alone looks inflated, shade alone looks hollow, together they look like clay you…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inner Highlight and Inner Shadow Layering
Source: https://codefronts.com/design-styles/css-claymorphism/inner-highlight-and-inner-shadow-layering/

Isolate the two inset layers and the material becomes obvious: highlight alone looks inflated, shade alone looks hollow, together they look like clay you could press a thumb into. Three spheres show each state, and the hero sphere animates its light around the object using @property-registered lengths — a genuinely animatable inset shadow, not a cross-fade.
## HTML
```html
<section class="cl-02" aria-label="Inner highlight and inner shadow layering demo">
  <div class="cl-02__stage">
    <div class="cl-02__hero">
      <div class="cl-02__sphere" aria-hidden="true"></div>
      <div class="cl-02__note">
        <h2 class="cl-02__h">Two insets make the material</h2>
        <p class="cl-02__lede">The highlight is the lit face, the shade is the far wall. Keep them diametrically opposed and the object holds one light source — even while the light orbits.</p>
        <p class="cl-02__pill"><code>@property</code> registered lengths → animatable inset offsets</p>
      </div>
    </div>
    <ul class="cl-02__set">
      <li class="cl-02__item">
        <span class="cl-02__ball cl-02__ball--light" aria-hidden="true"></span>
        <b class="cl-02__cap">Highlight only</b>
        <span class="cl-02__sub">inflated · no thickness</span>
      </li>
      <li class="cl-02__item">
        <span class="cl-02__ball cl-02__ball--dark" aria-hidden="true"></span>
        <b class="cl-02__cap">Shade only</b>
        <span class="cl-02__sub">hollow · reads as a bowl</span>
      </li>
      <li class="cl-02__item">
        <span class="cl-02__ball cl-02__ball--both" aria-hidden="true"></span>
        <b class="cl-02__cap">Both layers</b>
        <span class="cl-02__sub">clay · pressable mass</span>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
@property --cl-02-lx {
  syntax: '<length>';
  inherits: false;
  initial-value: 0px;
}

@property --cl-02-ly {
  syntax: '<length>';
  inherits: false;
  initial-value: 20px;
}

.cl-02,
.cl-02 *,
.cl-02 *::before,
.cl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-02-bg);
  --cl-02-bg: oklch(0.94 0.03 285);
  --cl-02-clay: oklch(0.8 0.1 292);
  --cl-02-shade: color-mix(in oklch,var(--cl-02-clay) 45%,oklch(0.38 0.13 290));
  --cl-02-light: oklch(0.99 0.02 300/.95);
  --cl-02-ink: oklch(0.3 0.06 292);
  --cl-02-mut: oklch(0.52 0.05 292);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-02-ink);
}

.cl-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(30px,5vw,52px);
  padding: clamp(22px,5vw,60px);
  background: radial-gradient(80% 60% at 78% 4%,oklch(0.97 0.04 300),transparent 62%);
}

.cl-02__hero {
  display: grid;
  gap: clamp(24px,4vw,44px);
  grid-template-columns: 1fr;
  justify-items: center;
  align-items: center;
  width: min(100%,860px);
  text-align: center;
}

@media (min-width: 820px) {
  .cl-02__hero {
    grid-template-columns: auto 1fr;
    text-align: left;
  }
}

.cl-02__sphere {
  width: clamp(168px,24vw,206px);
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--cl-02-clay);
  box-shadow: 0 26px 44px -14px var(--cl-02-shade),inset var(--cl-02-lx) var(--cl-02-ly) 30px -8px var(--cl-02-light),inset calc(var(--cl-02-lx) * -1) calc(var(--cl-02-ly) * -1) 30px -8px var(--cl-02-shade);
  animation: cl-02-orbit 9s linear infinite;
}

@keyframes cl-02-orbit {
  0% {
    --cl-02-lx: 0px;
    --cl-02-ly: 20px;
  }

  25% {
    --cl-02-lx: 20px;
    --cl-02-ly: 0px;
  }

  50% {
    --cl-02-lx: 0px;
    --cl-02-ly: -20px;
  }

  75% {
    --cl-02-lx: -20px;
    --cl-02-ly: 0px;
  }

  100% {
    --cl-02-lx: 0px;
    --cl-02-ly: 20px;
  }
}

.cl-02__note {
  display: grid;
  gap: 12px;
  max-width: 46ch;
}

.cl-02__h {
  font-size: clamp(23px,3.4vw,33px);
  font-weight: 780;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.cl-02__lede {
  font-size: 15px;
  line-height: 1.65;
  color: var(--cl-02-mut);
  text-wrap: pretty;
}

.cl-02__pill {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-02-ink);
  padding: 9px 16px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cl-02-bg) 80%,white);
  box-shadow: inset 0 -6px 12px -8px var(--cl-02-shade),inset 0 8px 12px -6px var(--cl-02-light);
}

.cl-02__set {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(150px,1fr));
  gap: clamp(16px,3vw,28px);
  width: min(100%,760px);
}

.cl-02__item {
  display: grid;
  justify-items: center;
  gap: 8px;
  padding: 26px 18px 22px;
  border-radius: 34px;
  text-align: center;
  background: color-mix(in oklch,var(--cl-02-bg) 86%,white);
  box-shadow: 0 18px 34px -18px var(--cl-02-shade),inset 0 -10px 18px -12px var(--cl-02-shade),inset 0 12px 18px -10px var(--cl-02-light);
  transition: translate .35s cubic-bezier(.34,1.3,.5,1);
}

.cl-02__item:hover {
  translate: 0 -6px;
}

.cl-02__ball {
  width: 82px;
  height: 82px;
  border-radius: 50%;
  background: var(--cl-02-clay);
  margin-bottom: 8px;
}

.cl-02__ball--light {
  box-shadow: inset 0 20px 28px -8px var(--cl-02-light);
}

.cl-02__ball--dark {
  box-shadow: inset 0 -20px 28px -8px var(--cl-02-shade);
}

.cl-02__ball--both {
  box-shadow: inset 0 20px 28px -8px var(--cl-02-light),inset 0 -20px 28px -8px var(--cl-02-shade),0 12px 20px -10px var(--cl-02-shade);
}

.cl-02__cap {
  font-size: 14.5px;
  font-weight: 680;
  letter-spacing: -.01em;
}

.cl-02__sub {
  font-size: 12.5px;
  color: var(--cl-02-mut);
}

@media (prefers-reduced-motion: reduce) {
  .cl-02__sphere {
    animation: none;
    --cl-02-lx: 0px;
    --cl-02-ly: 20px;
  }

  .cl-02 * {
    transition-duration: .01ms !important;
  }
}
```

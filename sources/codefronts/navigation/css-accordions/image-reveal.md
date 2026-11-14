---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/image-reveal/"
title: "Horizontal Image Reveal Accordion — Expanding Photo Gallery Panels"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "The portfolio showstopper: full-bleed image columns (rich CSS gradient scenes stand in for photos) that expand on selection to reveal a caption rising from a…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Image Reveal Accordion — Expanding Photo Gallery Panels
Source: https://codefronts.com/navigation/css-accordions/image-reveal/

The portfolio showstopper: full-bleed image columns (rich CSS gradient scenes stand in for photos) that expand on selection to reveal a caption rising from a gradient scrim — grayscale-and-dim when collapsed, full color when active. The 'expanding image gallery' effect usually sold as a JS plugin, in ~40 lines of CSS.
## HTML
```html
<section class="acc-16" aria-label="Horizontal image reveal gallery accordion demo">
  <div class="acc-16__row" role="group" aria-label="Expedition gallery">
    <div class="acc-16__panel" style="--scene:radial-gradient(420px 300px at 30% 20%,#ffd9a0 0%,transparent 60%),linear-gradient(165deg,#e8734a 0%,#8e3b5c 55%,#2c1e4a 100%)">
      <input type="radio" name="acc-16" id="acc-16-a" checked>
      <label class="acc-16__face" for="acc-16-a"><span class="acc-16__chip">01</span>
        <span class="acc-16__cap"><b>Desert dawn</b><p>First light on the dune sea — 41°C by nine, silence you can hear.</p></span>
      </label>
    </div>
    <div class="acc-16__panel" style="--scene:radial-gradient(400px 280px at 70% 15%,#bfe8ff 0%,transparent 55%),linear-gradient(180deg,#4a7fa8 0%,#274a66 60%,#12222f 100%)">
      <input type="radio" name="acc-16" id="acc-16-b">
      <label class="acc-16__face" for="acc-16-b"><span class="acc-16__chip">02</span>
        <span class="acc-16__cap"><b>Fjord crossing</b><p>Six hours by open boat between walls of thousand-metre granite.</p></span>
      </label>
    </div>
    <div class="acc-16__panel" style="--scene:radial-gradient(380px 300px at 50% 10%,#d9ffe0 0%,transparent 55%),linear-gradient(175deg,#3f7d52 0%,#1f4a33 55%,#0d1f16 100%)">
      <input type="radio" name="acc-16" id="acc-16-c">
      <label class="acc-16__face" for="acc-16-c"><span class="acc-16__chip">03</span>
        <span class="acc-16__cap"><b>Cloud forest</b><p>Every surface grows something. GPS useless under the canopy; we navigated by river sound.</p></span>
      </label>
    </div>
    <div class="acc-16__panel" style="--scene:radial-gradient(400px 280px at 40% 20%,#e8ecff 0%,transparent 50%),linear-gradient(170deg,#8b96c9 0%,#3d4670 55%,#151a30 100%)">
      <input type="radio" name="acc-16" id="acc-16-d">
      <label class="acc-16__face" for="acc-16-d"><span class="acc-16__chip">04</span>
        <span class="acc-16__cap"><b>High pass</b><p>5,200 metres. The tea froze before we finished pouring it.</p></span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-16,
.acc-16 *,
.acc-16 *::before,
.acc-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-16 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #101318;
  padding: 44px 24px;
}

.acc-16__row {
  display: flex;
  gap: 8px;
  width: min(840px,100%);
  height: 440px;
}

.acc-16__panel {
  display: flex;
  flex-grow: 1;
  flex-basis: 0;
  min-width: 56px;
  transition: flex-grow .55s cubic-bezier(.4,0,.2,1);
}

.acc-16__panel:has(input:checked) {
  flex-grow: 7;
}

.acc-16__panel input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-16__face {
  position: relative;
  flex: 1;
  display: block;
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
  background: var(--scene);
  background-size: cover;
  filter: grayscale(.7) brightness(.72);
  transition: filter .45s;
}

.acc-16__panel:has(input:checked) .acc-16__face {
  filter: none;
}

.acc-16__face:hover {
  filter: grayscale(.3) brightness(.85);
}

.acc-16__panel:has(input:checked) .acc-16__face:hover {
  filter: none;
}

.acc-16__chip {
  position: absolute;
  top: 14px;
  left: 50%;
  translate: -50% 0;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
  background: rgba(0,0,0,.45);
  padding: 5px 9px;
  border-radius: 99px;
  backdrop-filter: blur(4px);
}

.acc-16__panel:has(input:checked) .acc-16__chip {
  left: 18px;
  translate: 0 0;
  transition: left .4s,translate .4s;
}

.acc-16__cap {
  position: absolute;
  inset: auto 0 0 0;
  padding: 70px 24px 22px;
  background: linear-gradient(transparent,rgba(0,0,0,.72));
  display: flex;
  flex-direction: column;
  gap: 6px;
  opacity: 0;
  translate: 0 12px;
  transition: opacity .35s .2s,translate .35s .2s;
}

.acc-16__panel:has(input:checked) .acc-16__cap {
  opacity: 1;
  translate: 0 0;
}

.acc-16__cap b {
  font-size: 23px;
  font-weight: 800;
  color: #fff;
  letter-spacing: -.01em;
}

.acc-16__cap p {
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(255,255,255,.85);
  max-width: 46ch;
}

.acc-16__panel:has(input:focus-visible) .acc-16__face {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (max-width: 600px) {
  .acc-16__row {
    flex-direction: column;
    height: auto;
  }

  .acc-16__panel {
    min-height: 60px;
  }

  .acc-16__panel:has(input:checked) {
    min-height: 280px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-16__panel,
    .acc-16__face,
    .acc-16__cap {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — radio-driven flex-grow expansion; collapsed panels are dimmed with filter:grayscale() brightness(), and captions rise over a scrim gradient once the panel is wide. Swap each --scene for url(photo.jpg) to use real images. */
```

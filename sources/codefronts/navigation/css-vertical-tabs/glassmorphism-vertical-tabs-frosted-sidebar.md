---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/glassmorphism-vertical-tabs-frosted-sidebar/"
title: "Glassmorphism Vertical Tabs (Frosted Sidebar)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "Frosted glass that holds up to scrutiny: a real backdrop-filter stack with saturation boost, a hairline light border, an inner highlight along the top edge,…"
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Vertical Tabs (Frosted Sidebar)
Source: https://codefronts.com/navigation/css-vertical-tabs/glassmorphism-vertical-tabs-frosted-sidebar/

Frosted glass that holds up to scrutiny: a real backdrop-filter stack with saturation boost, a hairline light border, an inner highlight along the top edge, and — the part most tutorials skip — a contrast floor so the text stays legible no matter what photo scrolls behind it.
## HTML
```html
<section class="vt-17" aria-label="Glassmorphism vertical tabs demo">
  <div class="vt-17__bg" aria-hidden="true"></div>
  <div class="vt-17__stage">
    <div class="vt-17__card" role="radiogroup" aria-label="Frosted panels">
      <div class="vt-17__rail">
        <p class="vt-17__brand">Aurora <span>OS</span></p>
        <input class="vt-17__radio" type="radio" name="vt-17" id="vt-17-t1" checked>
        <label class="vt-17__tab" for="vt-17-t1">Four layers</label>
        <input class="vt-17__radio" type="radio" name="vt-17" id="vt-17-t2">
        <label class="vt-17__tab" for="vt-17-t2">Saturation</label>
        <input class="vt-17__radio" type="radio" name="vt-17" id="vt-17-t3">
        <label class="vt-17__tab" for="vt-17-t3">Legibility</label>
        <input class="vt-17__radio" type="radio" name="vt-17" id="vt-17-t4">
        <label class="vt-17__tab" for="vt-17-t4">Performance</label>
      </div>
      <div class="vt-17__panels">
        <article class="vt-17__panel" id="vt-17-p1"><h3 class="vt-17__h">Tint, frost, edge, highlight</h3><p class="vt-17__p">Glass is four layers. The <code>inset 0 1px 0</code> top highlight does more for the illusion than another ten pixels of blur ever will.</p></article>
        <article class="vt-17__panel" id="vt-17-p2"><h3 class="vt-17__h">saturate(180%) or grey plastic</h3><p class="vt-17__p">Blurring drains colour out of the backdrop. Pushing saturation back up is how real frosted surfaces behave optically.</p></article>
        <article class="vt-17__panel" id="vt-17-p3"><h3 class="vt-17__h">Test the worst image</h3><p class="vt-17__p">A translucent panel over an arbitrary photo can land anywhere from 1.2:1 to 12:1. A dark-biased tint plus a scrim keeps the floor safe.</p></article>
        <article class="vt-17__panel" id="vt-17-p4"><h3 class="vt-17__h">Few and large</h3><p class="vt-17__p">Every glass surface re-blurs what moves behind it. Keep them few, keep them big, and never animate the blur radius.</p></article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-17 {
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-17-bg);
  --vt-17-bg: oklch(0.22 0.06 285);
  --vt-17-ink: oklch(0.99 0.004 285);
  --vt-17-mut: oklch(0.88 0.014 285);
  --vt-17-acc: oklch(0.86 0.13 195);
  --vt-17-glass: oklch(1 0 0/.1);
  --vt-17-edge: oklch(1 0 0/.18);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-17-ink);
  overflow: hidden;
  isolation: isolate;
}

.vt-17 *,
.vt-17 *::before,
.vt-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-17__bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  background: linear-gradient(140deg,oklch(0.42 0.16 300),oklch(0.32 0.13 230) 45%,oklch(0.5 0.15 25)),url("https://images.unsplash.com/photo-1620121692029-d088224ddc74?q=80&w=1800&auto=format&fit=crop") center/cover no-repeat;
  background-blend-mode: overlay,normal;
  animation: vt-17-drift 26s ease-in-out infinite alternate;
}

@keyframes vt-17-drift {
  from {
    transform: scale(1.06) translate3d(-1.5%,-1%,0);
  }

  to {
    transform: scale(1.12) translate3d(1.5%,1%,0);
  }
}

.vt-17__stage {
  position: relative;
  z-index: 1;
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: clamp(18px,4vw,60px);
}

.vt-17__card {
  width: min(94vw,860px);
  display: grid;
  grid-template-columns: minmax(150px,224px) minmax(0,1fr);
  border-radius: 24px;
  background: var(--vt-17-glass);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
  backdrop-filter: blur(22px) saturate(180%);
  border: 1px solid var(--vt-17-edge);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.3),0 30px 70px -34px oklch(0 0 0/.7);
  overflow: hidden;
}

.vt-17__rail {
  display: grid;
  align-content: start;
  gap: 4px;
  padding: 16px 12px;
  background: linear-gradient(180deg,oklch(1 0 0/.08),oklch(0 0 0/.06));
  border-right: 1px solid oklch(1 0 0/.14);
}

.vt-17__brand {
  display: flex;
  align-items: baseline;
  gap: 6px;
  padding: 4px 12px 14px;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -.015em;
  text-shadow: 0 1px 8px oklch(0 0 0/.4);
}

.vt-17__brand span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  font-weight: 600;
  color: var(--vt-17-acc);
}

.vt-17__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-17__tab {
  display: flex;
  align-items: center;
  min-height: 46px;
  padding: 0 14px;
  border-radius: 13px;
  border: 1px solid transparent;
  font-size: 14.2px;
  font-weight: 640;
  color: var(--vt-17-mut);
  cursor: pointer;
  text-shadow: 0 1px 6px oklch(0 0 0/.35);
  transition: color .22s ease,background .22s ease,border-color .22s ease,box-shadow .22s ease;
}

.vt-17__tab:hover {
  color: var(--vt-17-ink);
  background: oklch(1 0 0/.1);
}

.vt-17__radio:checked+.vt-17__tab {
  color: oklch(0.2 0.04 250);
  background: oklch(1 0 0/.82);
  border-color: oklch(1 0 0/.6);
  box-shadow: 0 6px 20px -8px oklch(0 0 0/.55);
  text-shadow: none;
}

.vt-17__radio:focus-visible+.vt-17__tab {
  outline: 2px solid var(--vt-17-acc);
  outline-offset: 2px;
}

.vt-17__panels {
  position: relative;
  display: grid;
  min-height: clamp(240px,30vw,286px);
  padding: clamp(22px,3.4vw,40px);
}

.vt-17__panels::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg,oklch(0 0 0/.22),transparent 70%);
  pointer-events: none;
}

.vt-17__panel {
  position: relative;
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 12px;
  justify-items: start;
  opacity: 0;
  visibility: hidden;
  transform: translateY(9px) scale(.99);
  transition: opacity .3s ease,transform .38s cubic-bezier(.32,.72,.3,1),visibility 0s .38s;
}

.vt-17__card:has(#vt-17-t1:checked) #vt-17-p1,
.vt-17__card:has(#vt-17-t2:checked) #vt-17-p2,
.vt-17__card:has(#vt-17-t3:checked) #vt-17-p3,
.vt-17__card:has(#vt-17-t4:checked) #vt-17-p4 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s;
}

.vt-17__h {
  font-size: clamp(20px,2.5vw,27px);
  line-height: 1.16;
  letter-spacing: -.026em;
  font-weight: 700;
  text-wrap: balance;
  text-shadow: 0 2px 14px oklch(0 0 0/.45);
}

.vt-17__p {
  max-width: 44ch;
  font-size: 15px;
  line-height: 1.62;
  font-weight: 500;
  color: var(--vt-17-mut);
  text-wrap: pretty;
  text-shadow: 0 1px 10px oklch(0 0 0/.45);
}

.vt-17__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.16);
  padding: 2px 6px;
  border-radius: 5px;
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .vt-17__card {
    background: oklch(0.24 0.05 285/.94);
  }
}

@media (max-width: 680px) {
  .vt-17__card {
    grid-template-columns: 1fr;
  }

  .vt-17__rail {
    border-right: 0;
    border-bottom: 1px solid oklch(1 0 0/.14);
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-17 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/crosshair-brackets/"
title: "CSS Crosshair / Bracket Link Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Target acquired: HUD-grade link states for dashboards, dev tools and sci-fi-adjacent brands."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Crosshair / Bracket Link Hover Effect
Source: https://codefronts.com/motion/css-link-effects/crosshair-brackets/

Target acquired: HUD-grade link states for dashboards, dev tools and sci-fi-adjacent brands. Four corner marks that snap outward to frame the link (the four-pseudo-element trick — two from the anchor, two from an inner span), typographic square brackets that slide in as the tracking widens, and a hairline crosshair that extends through the target from its center.
## HTML
```html
<section class="cle-19" aria-label="Bracket and crosshair hover demo">
  <div class="cle-19__stage">
    <div class="cle-19__var"><a href="#a" class="cle-19__lock"><span class="cle-19__in">Deploy sequence</span></a><small class="cle-19__cap">A · corner lock</small></div>
    <div class="cle-19__var"><a href="#b" class="cle-19__brackets">Telemetry feed</a><small class="cle-19__cap">B · typographic brackets</small></div>
    <div class="cle-19__var"><a href="#c" class="cle-19__scope"><span class="cle-19__in">Orbital map</span></a><small class="cle-19__cap">C · hairline crosshair</small></div>
  </div>
</section>
```
## CSS
```css
.cle-19,
.cle-19 *,
.cle-19 *::before,
.cle-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-19 {
  width: 100%;
  min-height: 100vh;
  --cy: oklch(0.85 0.13 195);
  --dim: oklch(0.65 0.06 210);
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
}

.cle-19__stage {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 52px 72px;
  background: radial-gradient(110% 140% at 50% -10%,oklch(0.25 0.04 230),oklch(0.16 0.025 235) 62%);
  padding: 44px 36px;
}

.cle-19__var {
  display: grid;
  gap: 16px;
  justify-items: center;
}

.cle-19__cap {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--dim);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-19 a {
  position: relative;
  color: oklch(0.88 0.04 210);
  text-decoration: none;
  font-size: 17px;
  letter-spacing: .06em;
  padding: 12px 16px;
  transition: color .3s,text-shadow .3s;
}

.cle-19 a:hover,
.cle-19 a:focus-visible {
  color: var(--cy);
}

.cle-19 a:focus-visible {
  outline: 1.5px solid var(--cy);
  outline-offset: 6px;
}

.cle-19__lock::before,
.cle-19__lock::after,
.cle-19__lock .cle-19__in::before,
.cle-19__lock .cle-19__in::after {
  content: "";
  position: absolute;
  width: 10px;
  height: 10px;
  border: 0 solid var(--cy);
  opacity: 0;
  transition: translate .3s cubic-bezier(.3,1.2,.4,1),opacity .25s;
}

.cle-19__lock::before {
  top: 0;
  left: 0;
  border-top-width: 2px;
  border-left-width: 2px;
  translate: 7px 7px;
}

.cle-19__lock::after {
  bottom: 0;
  right: 0;
  border-bottom-width: 2px;
  border-right-width: 2px;
  translate: -7px -7px;
}

.cle-19__lock .cle-19__in::before {
  top: 0;
  right: 0;
  border-top-width: 2px;
  border-right-width: 2px;
  translate: -7px 7px;
}

.cle-19__lock .cle-19__in::after {
  bottom: 0;
  left: 0;
  border-bottom-width: 2px;
  border-left-width: 2px;
  translate: 7px -7px;
}

.cle-19__lock .cle-19__in::before,
.cle-19__lock .cle-19__in::after {
  content: "";
}

.cle-19__lock:hover ::before,
.cle-19__lock:hover ::after,
.cle-19__lock:hover::before,
.cle-19__lock:hover::after,
.cle-19__lock:focus-visible ::before,
.cle-19__lock:focus-visible ::after,
.cle-19__lock:focus-visible::before,
.cle-19__lock:focus-visible::after {
  opacity: 1;
  translate: 0 0;
}

.cle-19__brackets {
  transition: color .3s,letter-spacing .35s cubic-bezier(.3,.9,.3,1);
}

.cle-19__brackets::before,
.cle-19__brackets::after {
  position: absolute;
  top: 50%;
  translate: 0 -50%;
  opacity: 0;
  color: var(--cy);
  transition: translate .3s cubic-bezier(.3,1.2,.4,1),opacity .25s;
}

.cle-19__brackets::before {
  content: "[" / "";
  left: -4px;
  translate: 8px -50%;
}

.cle-19__brackets::after {
  content: "]" / "";
  right: -4px;
  translate: -8px -50%;
}

.cle-19__brackets:hover,
.cle-19__brackets:focus-visible {
  letter-spacing: .12em;
}

.cle-19__brackets:hover::before,
.cle-19__brackets:hover::after,
.cle-19__brackets:focus-visible::before,
.cle-19__brackets:focus-visible::after {
  opacity: 1;
  translate: 0 -50%;
}

.cle-19__scope::before,
.cle-19__scope::after {
  content: "";
  position: absolute;
  background: color-mix(in oklch,var(--cy),transparent 35%);
  opacity: 0;
  transition: scale .35s cubic-bezier(.3,.9,.3,1),opacity .25s;
}

.cle-19__scope::before {
  left: -14px;
  right: -14px;
  top: 50%;
  height: 1px;
  scale: 0 1;
}

.cle-19__scope::after {
  top: -14px;
  bottom: -14px;
  left: 50%;
  width: 1px;
  scale: 1 0;
}

.cle-19__scope:hover::before,
.cle-19__scope:focus-visible::before {
  scale: 1 1;
  opacity: 1;
}

.cle-19__scope:hover::after,
.cle-19__scope:focus-visible::after {
  scale: 1 1;
  opacity: 1;
}

.cle-19__scope:hover,
.cle-19__scope:focus-visible {
  text-shadow: 0 0 14px color-mix(in oklch,var(--cy),transparent 40%);
}

@media (prefers-reduced-motion: reduce) {
  .cle-19 * {
    transition-duration: .01s !important;
  }
}
```

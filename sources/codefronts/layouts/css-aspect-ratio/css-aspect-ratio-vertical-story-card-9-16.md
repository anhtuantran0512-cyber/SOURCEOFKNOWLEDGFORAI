---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-vertical-story-card-9-16/"
title: "CSS Aspect Ratio Vertical Story Card 9 16"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "A Stories/Shorts rail where the ratio runs the other direction: each card declares a height (clamped to the viewport) and aspect-ratio: 9/16 derives the width."
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Vertical Story Card 9 16
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-vertical-story-card-9-16/

A Stories/Shorts rail where the ratio runs the other direction: each card declares a height (clamped to the viewport) and aspect-ratio: 9/16 derives the width. That reversal — ratio solves for whichever axis you leave auto — is the most under-taught fact about the property. Scroll-snap paddles the rail, segment bars and conic-gradient avatar rings sell the Stories grammar, edge masks fade the overflow, and every card is a real focusable link.
## HTML
```html
<section class="car-05" aria-label="Vertical 9:16 story cards demo">
  <div class="car-05__stage" id="car05-top">
    <header class="car-05__bar">
      <a class="car-05__brand" href="#car05-top"><i aria-hidden="true"></i>Shortloop</a>
      <p class="car-05__hint"><code>height: clamp(340px, 56svh, 540px)</code> · <code>aspect-ratio: 9/16</code> — width is derived</p>
      <a class="car-05__all" href="#car05-top">See all</a>
    </header>
    <div class="car-05__railwrap">
      <ul class="car-05__rail" aria-label="Stories">
        <li><a class="car-05__story car-05__story--new" href="#car05-top"><span class="car-05__plus" aria-hidden="true">+</span><b>Your story</b><small>9:16, like all the others</small></a></li>
        <li><a class="car-05__story" href="#car05-top" style="--img:url('https://images.unsplash.com/photo-1529139574466-a303027c1d8b?q=80&w=700&h=1244&auto=format&fit=crop')"><span class="car-05__segs" aria-hidden="true"><i class="is-seen"></i><i class="is-seen"></i><i></i></span><span class="car-05__head"><img src="https://images.unsplash.com/photo-1529139574466-a303027c1d8b?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt=""><b>mira.k</b><time>2h</time></span><span class="car-05__cap">Fitting the fold on every phone since 2026</span><span class="car-05__eye" aria-hidden="true">▶ 12.4k</span></a></li>
        <li><a class="car-05__story" href="#car05-top" style="--img:url('https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=700&h=1244&auto=format&fit=crop')"><span class="car-05__segs" aria-hidden="true"><i class="is-seen"></i><i></i><i></i><i></i></span><span class="car-05__head"><img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt=""><b>june.ro</b><time>4h</time></span><span class="car-05__cap">The width of this card is height × 0.5625</span><span class="car-05__eye" aria-hidden="true">▶ 8.1k</span></a></li>
        <li><a class="car-05__story" href="#car05-top" style="--img:url('https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=700&h=1244&auto=format&fit=crop')"><span class="car-05__segs" aria-hidden="true"><i></i><i></i></span><span class="car-05__head"><img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt=""><b>theo.v</b><time>6h</time></span><span class="car-05__cap">flex:none is load-bearing here</span><span class="car-05__eye" aria-hidden="true">▶ 5.7k</span></a></li>
        <li><a class="car-05__story" href="#car05-top" style="--img:url('https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=700&h=1244&auto=format&fit=crop')"><span class="car-05__segs" aria-hidden="true"><i class="is-seen"></i><i class="is-seen"></i><i class="is-seen"></i></span><span class="car-05__head"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt=""><b>amara</b><time>9h</time></span><span class="car-05__cap">Scroll-snap lands every card on the gutter</span><span class="car-05__eye" aria-hidden="true">▶ 21k</span></a></li>
        <li><a class="car-05__story" href="#car05-top" style="--img:url('https://images.unsplash.com/photo-1502823403499-6ccfcf4fb453?q=80&w=700&h=1244&auto=format&fit=crop')"><span class="car-05__segs" aria-hidden="true"><i></i><i></i><i></i></span><span class="car-05__head"><img src="https://images.unsplash.com/photo-1502823403499-6ccfcf4fb453?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt=""><b>sol.ie</b><time>11h</time></span><span class="car-05__cap">Edge fade is mask-image, not a gradient div</span><span class="car-05__eye" aria-hidden="true">▶ 3.3k</span></a></li>
        <li><a class="car-05__story" href="#car05-top" style="--img:url('https://images.unsplash.com/photo-1509631179647-0177331693ae?q=80&w=700&h=1244&auto=format&fit=crop')"><span class="car-05__segs" aria-hidden="true"><i class="is-seen"></i><i></i></span><span class="car-05__head"><img src="https://images.unsplash.com/photo-1509631179647-0177331693ae?q=80&w=96&h=96&auto=format&fit=crop" width="96" height="96" loading="lazy" alt=""><b>nadia</b><time>14h</time></span><span class="car-05__cap">Tab through — every card is a real link</span><span class="car-05__eye" aria-hidden="true">▶ 9.8k</span></a></li>
      </ul>
    </div>
    <footer class="car-05__foot">Rotate or resize the pane: card heights re-clamp to <code>56svh</code> and every width re-derives from <code>aspect-ratio: 9/16</code>. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-05,
.car-05 *,
.car-05 *::before,
.car-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-05 {
  --bg: oklch(0.15 0.02 300);
  --ink: oklch(0.96 0.005 300);
  --mut: oklch(0.68 0.02 300);
  --line: oklch(0.3 0.03 300);
  --acc: oklch(0.7 0.19 340);
  --acc2: oklch(0.78 0.15 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-05__stage {
  width: 100%;
  container: car05/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  background: radial-gradient(120cqi 80cqi at 80% -20%,oklch(0.28 0.06 340/.5),transparent 60%),var(--bg);
}

.car-05__bar {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 18px clamp(16px,4cqi,40px) 10px;
  flex-wrap: wrap;
}

.car-05__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.car-05__brand i {
  width: 13px;
  height: 22px;
  border-radius: 4px;
  background: linear-gradient(160deg,var(--acc),var(--acc2));
}

.car-05__hint {
  font-size: 11.5px;
  color: var(--mut);
  margin-inline: auto;
}

.car-05__hint code,
.car-05__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .95em;
  background: oklch(0.24 0.03 300);
  padding: 2px 6px;
  border-radius: 5px;
  color: oklch(0.85 0.08 340);
}

.car-05__all {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  border: 1px solid var(--line);
  transition: border-color .2s,background .2s;
}

.car-05__all:hover,
.car-05__all:focus-visible {
  border-color: var(--acc);
  background: oklch(0.22 0.03 320);
}

.car-05__all:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.car-05__railwrap {
  flex: 1;
  display: grid;
  align-content: center;
  min-height: 0;
}

.car-05__rail {
  list-style: none;
  display: flex;
  gap: 14px;
  overflow-x: auto;
  padding: 18px clamp(16px,4cqi,40px) 22px;
  scroll-snap-type: x mandatory;
  scroll-padding-inline: clamp(16px,4cqi,40px);
  -webkit-mask-image: linear-gradient(to right,transparent,black 26px,black calc(100% - 26px),transparent);
  mask-image: linear-gradient(to right,transparent,black 26px,black calc(100% - 26px),transparent);
  scrollbar-width: thin;
  scrollbar-color: oklch(0.4 0.04 320) transparent;
}

.car-05__rail::-webkit-scrollbar {
  height: 8px;
}

.car-05__rail::-webkit-scrollbar-thumb {
  background: oklch(0.4 0.04 320);
  border-radius: 99px;
}

.car-05__story {
  position: relative;
  flex: none;
  height: clamp(340px,56svh,540px);
  aspect-ratio: 9/16;
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 14px;
  border-radius: 20px;
  overflow: hidden;
  text-decoration: none;
  color: oklch(0.98 0 0);
  isolation: isolate;
  background-color: oklch(0.3 0.05 320);
  background-image: linear-gradient(to bottom,oklch(0.2 0.03 320/.05) 40%,oklch(0.12 0.03 320/.82)),var(--img);
  background-size: cover;
  background-position: center;
  transition: translate .3s cubic-bezier(.2,.7,.2,1),box-shadow .3s;
}

.car-05__story:hover,
.car-05__story:focus-visible {
  translate: 0 -6px;
  box-shadow: 0 22px 50px oklch(0.05 0.03 320/.6);
}

.car-05__story:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.car-05__segs {
  position: absolute;
  left: 12px;
  right: 12px;
  top: 10px;
  display: flex;
  gap: 5px;
}

.car-05__segs i {
  flex: 1;
  height: 3px;
  border-radius: 99px;
  background: oklch(0.95 0.01 320/.35);
}

.car-05__segs i.is-seen {
  background: oklch(0.98 0 0/.95);
}

.car-05__head {
  display: flex;
  align-items: center;
  gap: 8px;
  position: absolute;
  left: 12px;
  right: 12px;
  top: 22px;
}

.car-05__head img {
  width: 34px;
  height: auto;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid transparent;
  background: linear-gradient(oklch(0.2 0.03 320),oklch(0.2 0.03 320)) padding-box,conic-gradient(var(--acc),var(--acc2),var(--acc)) border-box;
}

.car-05__head b {
  font-size: 13px;
  font-weight: 700;
  text-shadow: 0 1px 8px oklch(0.1 0.03 320/.8);
}

.car-05__head time {
  font-size: 11px;
  color: oklch(0.85 0.02 320/.85);
}

.car-05__cap {
  font-size: 13.5px;
  line-height: 1.4;
  font-weight: 600;
  text-shadow: 0 1px 10px oklch(0.1 0.03 320/.9);
  text-wrap: pretty;
}

.car-05__eye {
  margin-top: 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .04em;
  color: oklch(0.9 0.02 320/.9);
}

.car-05__story--new {
  align-items: center;
  justify-content: center;
  gap: 6px;
  background: oklch(0.2 0.03 320/.55);
  border: 1.5px dashed oklch(0.5 0.05 320);
}

.car-05__plus {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  font-size: 26px;
  font-weight: 600;
  background: linear-gradient(160deg,var(--acc),var(--acc2));
  color: oklch(0.15 0.03 320);
  transition: scale .25s cubic-bezier(.34,1.56,.64,1);
}

.car-05__story--new:hover .car-05__plus,
.car-05__story--new:focus-visible .car-05__plus {
  scale: 1.1;
}

.car-05__story--new b {
  font-size: 13.5px;
}

.car-05__story--new small {
  font-size: 11px;
  color: var(--mut);
}

.car-05__foot {
  padding: 0 clamp(16px,4cqi,40px) 22px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .car-05 * {
    transition-duration: .01ms !important;
  }
}
```

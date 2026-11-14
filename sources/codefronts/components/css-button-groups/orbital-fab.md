---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/orbital-fab/"
title: "CSS Floating Action Button with Radial Sub-Button Menu (Arc Fan-Out, Pure CSS)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A floating action button that fans a ring of sub-actions out along an arc when tapped — each satellite springs to its own orbital position on a staggered…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Floating Action Button with Radial Sub-Button Menu (Arc Fan-Out, Pure CSS)
Source: https://codefronts.com/components/css-button-groups/orbital-fab/

A floating action button that fans a ring of sub-actions out along an arc when tapped — each satellite springs to its own orbital position on a staggered delay, and the FAB icon rotates into a close cross. The delightful 'CSS floating action button radial menu' (speed-dial) built with a checkbox toggle, no JavaScript.
## HTML
```html
<section class="btn-21" aria-label="Orbital floating action button demo">
  <div class="btn-21__fab" role="group" aria-label="Quick create">
    <button type="button" class="btn-21__sat" style="--x:0px;--y:-96px" aria-label="New note"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 4h12l4 4v12H4zM16 4v4h4"/></svg></button>
    <button type="button" class="btn-21__sat" style="--x:-84px;--y:-48px" aria-label="New task"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 12l5 5L20 6"/></svg></button>
    <button type="button" class="btn-21__sat" style="--x:-96px;--y:44px" aria-label="Upload"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 16V5M7 10l5-5 5 5M5 19h14"/></svg></button>
    <button type="button" class="btn-21__sat" style="--x:-40px;--y:88px" aria-label="Invite"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="9" cy="8" r="3.2"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0M17 8v6M14 11h6"/></svg></button>
    <input type="checkbox" id="btn-21-t" class="btn-21__in">
    <label for="btn-21-t" class="btn-21__main" aria-label="Open quick create menu"><span class="btn-21__plus"></span></label>
  </div>
</section>
```
## CSS
```css
.btn-21,
.btn-21 *,
.btn-21 *::before,
.btn-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-21 {
  --accent: oklch(0.6 0.24 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 70% 70%,#221338,#0c0716);
  padding: 44px 20px;
}

.btn-21__fab {
  position: relative;
  width: 64px;
  height: 64px;
}

.btn-21__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-21__main {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: var(--accent);
  cursor: pointer;
  box-shadow: 0 12px 30px -8px var(--accent),0 0 0 0 rgba(255,255,255,.2);
  z-index: 3;
  transition: transform .3s,box-shadow .3s;
}

.btn-21__main:hover {
  transform: scale(1.05);
}

.btn-21__plus {
  position: relative;
  width: 22px;
  height: 22px;
}

.btn-21__plus::before,
.btn-21__plus::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  background: #fff;
  border-radius: 2px;
  translate: -50% -50%;
  transition: transform .35s cubic-bezier(.34,1.4,.4,1);
}

.btn-21__plus::before {
  width: 22px;
  height: 3px;
}

.btn-21__plus::after {
  width: 3px;
  height: 22px;
}

.btn-21__fab:has(.btn-21__in:checked) .btn-21__plus::before {
  transform: rotate(135deg);
}

.btn-21__fab:has(.btn-21__in:checked) .btn-21__plus::after {
  transform: rotate(135deg);
}

.btn-21__sat {
  position: absolute;
  left: 11px;
  top: 11px;
  width: 42px;
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 50%;
  background: #2a1f45;
  color: #e6d8ff;
  cursor: pointer;
  z-index: 2;
  scale: 0;
  translate: 0 0;
  box-shadow: 0 8px 20px -8px #000;
  transition: translate .4s cubic-bezier(.34,1.5,.5,1),scale .35s cubic-bezier(.34,1.5,.5,1),background .18s;
}

.btn-21__sat:hover {
  background: var(--accent);
  color: #fff;
}

.btn-21__fab:has(.btn-21__in:checked) .btn-21__sat {
  translate: var(--x) var(--y);
  scale: 1;
}

.btn-21__fab:has(.btn-21__in:checked) .btn-21__sat:nth-child(1) {
  transition-delay: .02s;
}

.btn-21__fab:has(.btn-21__in:checked) .btn-21__sat:nth-child(2) {
  transition-delay: .07s;
}

.btn-21__fab:has(.btn-21__in:checked) .btn-21__sat:nth-child(3) {
  transition-delay: .12s;
}

.btn-21__fab:has(.btn-21__in:checked) .btn-21__sat:nth-child(4) {
  transition-delay: .17s;
}

.btn-21__in:focus-visible + .btn-21__main {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.btn-21__sat:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-21__sat,
    .btn-21__plus::before,
    .btn-21__plus::after {
    transition: scale .2s,translate .2s;
  }

  .btn-21__fab:has(.btn-21__in:checked) .btn-21__sat {
    transition-delay: 0s;
  }
}
```

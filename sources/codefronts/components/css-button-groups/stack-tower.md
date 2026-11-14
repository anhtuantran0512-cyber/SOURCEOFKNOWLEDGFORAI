---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/stack-tower/"
title: "CSS Vertical Button Stack with 3D Hover Depth (Tilting Card Buttons)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A vertical stack of big button-cards that live in real 3D space: the tower tilts under a shared perspective, and hovering any button lifts it toward you on…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Vertical Button Stack with 3D Hover Depth (Tilting Card Buttons)
Source: https://codefronts.com/components/css-button-groups/stack-tower/

A vertical stack of big button-cards that live in real 3D space: the tower tilts under a shared perspective, and hovering any button lifts it toward you on the Z axis while its neighbors recede. A tactile 'CSS vertical button stack 3D hover depth' for nav menus, plan pickers and app launchers.
## HTML
```html
<section class="btn-20" aria-label="3D hover depth vertical button stack demo">
  <div class="btn-20__scene">
    <div class="btn-20__stack" role="group" aria-label="Workspace">
      <button type="button" class="btn-20__btn" style="--c:#ff8a4c"><span class="btn-20__k">Dashboard</span><span class="btn-20__s">Overview & metrics</span></button>
      <button type="button" class="btn-20__btn" style="--c:#ffd24c"><span class="btn-20__k">Projects</span><span class="btn-20__s">12 active</span></button>
      <button type="button" class="btn-20__btn" style="--c:#6ee7a8"><span class="btn-20__k">Team</span><span class="btn-20__s">8 members</span></button>
      <button type="button" class="btn-20__btn" style="--c:#5cc8ff"><span class="btn-20__k">Settings</span><span class="btn-20__s">Workspace config</span></button>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-20,
.btn-20 *,
.btn-20 *::before,
.btn-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-20 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(165deg,#2a1c14,#160f0a);
  padding: 44px 20px;
}

.btn-20__scene {
  perspective: 760px;
  perspective-origin: 50% 42%;
}

.btn-20__stack {
  display: flex;
  flex-direction: column;
  gap: 18px;
  width: min(340px,86vw);
  transform: rotateX(34deg) rotateZ(-1deg);
  transform-style: preserve-3d;
}

.btn-20__btn {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 4px;
  padding: 18px 22px;
  border: none;
  border-radius: 16px;
  background: linear-gradient(180deg,#33271c,#241a12);
  color: #f3e6d6;
  cursor: pointer;
  text-align: left;
  transform: translateZ(0);
  transform-style: preserve-3d;
  transition: transform .4s cubic-bezier(.34,1.4,.4,1),box-shadow .4s,opacity .4s,filter .4s;
  box-shadow: 0 16px 30px -14px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.08);
  border-left: 4px solid var(--c);
}

.btn-20__k {
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.btn-20__s {
  font-size: 13px;
  color: #b39a83;
}

.btn-20__stack:has(.btn-20__btn:hover) .btn-20__btn:not(:hover),
.btn-20__stack:has(.btn-20__btn:focus-visible) .btn-20__btn:not(:focus-visible) {
  transform: translateZ(-55px);
  opacity: .5;
  filter: brightness(.72);
}

.btn-20__btn:hover,
.btn-20__btn:focus-visible {
  transform: translateZ(70px) rotateX(-14deg);
  box-shadow: 0 40px 60px -24px rgba(0,0,0,.9),0 0 0 1px var(--c),inset 0 1px 0 rgba(255,255,255,.12);
  outline: none;
}

.btn-20__btn:focus-visible {
  box-shadow: 0 40px 60px -24px rgba(0,0,0,.9),0 0 0 3px var(--c);
}

@media (prefers-reduced-motion: reduce) {
  .btn-20__stack {
    transform: none;
  }

  .btn-20__btn {
    transition: opacity .2s,box-shadow .2s;
  }

  .btn-20__btn:hover,
    .btn-20__btn:focus-visible {
    transform: none;
  }

  .btn-20__stack:has(.btn-20__btn:hover) .btn-20__btn:not(:hover) {
    transform: none;
  }
}
```

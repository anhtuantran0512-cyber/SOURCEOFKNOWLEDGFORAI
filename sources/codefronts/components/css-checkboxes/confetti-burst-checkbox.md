---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/confetti-burst-checkbox/"
title: "Confetti Burst Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A moment of celebration: checking the box fires a short burst of tiny coloured squares outward from its edges."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Confetti Burst Checkbox
Source: https://codefronts.com/components/css-checkboxes/confetti-burst-checkbox/

A moment of celebration: checking the box fires a short burst of tiny coloured squares outward from its edges. The reward interaction for finishing onboarding, completing a goal or hitting 'I'm done' — pure CSS, no confetti library.
## HTML
```html
<section class="cb-27" aria-label="Confetti burst checkboxes">
  <div class="cb-27__panel">
    <label class="cb-27__row"><input type="checkbox" class="cb-27__input" checked><span class="cb-27__box" aria-hidden="true"><span class="cb-27__burst"><i style="--tx:-16px;--ty:-14px;--rot:120deg;background:#ff5d73"></i><i style="--tx:15px;--ty:-16px;--rot:-90deg;background:#ffd23f"></i><i style="--tx:-18px;--ty:10px;--rot:60deg;background:#3ddc97"></i><i style="--tx:17px;--ty:12px;--rot:-140deg;background:#4d7fff"></i><i style="--tx:0px;--ty:-20px;--rot:200deg;background:#c04cff"></i><i style="--tx:2px;--ty:19px;--rot:-40deg;background:#ff9a3d"></i></span></span><span class="cb-27__label">Finish onboarding</span></label>
    <label class="cb-27__row"><input type="checkbox" class="cb-27__input"><span class="cb-27__box" aria-hidden="true"><span class="cb-27__burst"><i style="--tx:-16px;--ty:-14px;--rot:120deg;background:#ff5d73"></i><i style="--tx:15px;--ty:-16px;--rot:-90deg;background:#ffd23f"></i><i style="--tx:-18px;--ty:10px;--rot:60deg;background:#3ddc97"></i><i style="--tx:17px;--ty:12px;--rot:-140deg;background:#4d7fff"></i><i style="--tx:0px;--ty:-20px;--rot:200deg;background:#c04cff"></i><i style="--tx:2px;--ty:19px;--rot:-40deg;background:#ff9a3d"></i></span></span><span class="cb-27__label">Claim your reward</span></label>
    <label class="cb-27__row"><input type="checkbox" class="cb-27__input"><span class="cb-27__box" aria-hidden="true"><span class="cb-27__burst"><i style="--tx:-16px;--ty:-14px;--rot:120deg;background:#ff5d73"></i><i style="--tx:15px;--ty:-16px;--rot:-90deg;background:#ffd23f"></i><i style="--tx:-18px;--ty:10px;--rot:60deg;background:#3ddc97"></i><i style="--tx:17px;--ty:12px;--rot:-140deg;background:#4d7fff"></i><i style="--tx:0px;--ty:-20px;--rot:200deg;background:#c04cff"></i><i style="--tx:2px;--ty:19px;--rot:-40deg;background:#ff9a3d"></i></span></span><span class="cb-27__label">Hit the goal</span></label>
  </div>
</section>
```
## CSS
```css
.cb-27,
.cb-27 *,
.cb-27 *::before,
.cb-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-27 ::selection {
  background: oklch(0.62 0.18 300);
  color: #fff;
}

.cb-27 {
  --accent: oklch(0.56 0.16 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f6f4fb;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-27__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #e9e5f3;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-27__row {
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  padding: 15px 8px;
}

.cb-27__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.cb-27__box {
  position: relative;
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 8px;
  border: 2px solid #c9c2dd;
  background: #fff;
  transition: background .2s,border-color .2s;
}

.cb-27__box::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 2;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .2s,transform .2s cubic-bezier(.2,.9,.3,1.3);
  -webkit-mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-27__burst {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.cb-27__burst i {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 6px;
  height: 6px;
  border-radius: 1px;
  transform: translate(-50%,-50%) scale(0);
  opacity: 0;
}

.cb-27__input:checked ~ .cb-27__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-27__input:checked ~ .cb-27__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-27__input:checked ~ .cb-27__box .cb-27__burst i {
  animation: cb-27-pop .6s ease-out;
}

.cb-27__input:focus-visible ~ .cb-27__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cb-27__label {
  font-size: 14.5px;
  color: #2f2a3d;
}

@keyframes cb-27-pop {
  0% {
    transform: translate(-50%,-50%) scale(0) rotate(0);
    opacity: 0;
  }

  15% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(1) rotate(0);
  }

  100% {
    transform: translate(calc(-50% + var(--tx)),calc(-50% + var(--ty))) scale(.4) rotate(var(--rot));
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-27__box,
    .cb-27__box::after {
    transition: none;
  }

  .cb-27__burst {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — per-particle --tx/--ty/--rot vectors drive a one-shot CSS burst. */
```

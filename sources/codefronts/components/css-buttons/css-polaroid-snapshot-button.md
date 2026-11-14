---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-polaroid-snapshot-button/"
title: "CSS Polaroid Snapshot Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "An instant photo mid-development: the image starts dark, flat and green-shifted, then blooms to full colour and contrast as you hover — a pure filter…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Polaroid Snapshot Button
Source: https://codefronts.com/components/css-buttons/css-polaroid-snapshot-button/

An instant photo mid-development: the image starts dark, flat and green-shifted, then blooms to full colour and contrast as you hover — a pure filter transition, exactly how the chemistry actually behaves. The frame tilts, lifts off the table, and the caption is hand-written on the wide bottom border.
## HTML
```html
<div class="cb-40">
  <div class="cb-40__stage">
    <button class="cb-40__btn" type="button">
      <span class="cb-40__frame">
        <span class="cb-40__win">
          <img class="cb-40__img" src="https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="800" height="800" loading="lazy" decoding="async">
          <span class="cb-40__vignette" aria-hidden="true"></span>
        </span>
        <span class="cb-40__caption">shake it once — open album</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&display=swap');

.cb-40 {
  --bg: #2a2723;
  --card: #fbfaf5;
  --card-lo: #e8e5dc;
  --ink: #2a2520;
  --accent: #3b7ea1;
  --hand: "Caveat",ui-rounded,cursive;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(34rem 22rem at 50% 40%, rgba(255,255,255,.06), transparent 72%), repeating-linear-gradient(94deg, rgba(0,0,0,.04) 0 2px, transparent 2px 12px), var(--bg);
  font-family: var(--hand);
}

@media (prefers-color-scheme: light) {
  .cb-40:not([data-theme="dark"]) {
    --bg: #3b3833;
  }
}

.cb-40[data-theme="light"] {
  --bg: #3b3833;
}

.cb-40,
.cb-40 *,
.cb-40 *::before,
.cb-40 *::after {
  box-sizing: border-box;
}

.cb-40__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-40__btn {
  cursor: pointer;
  border: 0;
  background: transparent;
  padding: 0;
  font: inherit;
  -webkit-tap-highlight-color: transparent;
}

.cb-40__frame {
  display: grid;
  gap: .55rem;
  width: 14rem;
  padding: .75rem .75rem .35rem;
  border-radius: .15rem;
  background: linear-gradient(170deg, var(--card), var(--card-lo));
  box-shadow: 0 14px 24px -14px rgba(0,0,0,.7), inset 0 0 0 1px rgba(0,0,0,.06);
  rotate: -2.2deg;
  transition: rotate .45s cubic-bezier(.16,1,.3,1), translate .45s cubic-bezier(.16,1,.3,1), box-shadow .4s ease;
}

.cb-40__win {
  position: relative;
  display: block;
  aspect-ratio: 1;
  overflow: hidden;
  background: #14161a;
}

.cb-40__img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(.34) contrast(.7) saturate(.32) hue-rotate(28deg) blur(1.2px);
  scale: 1.06;
  transition: filter 1.6s cubic-bezier(.3,.7,.3,1), scale 1.3s cubic-bezier(.16,1,.3,1);
}

.cb-40__vignette {
  position: absolute;
  inset: 0;
  pointer-events: none;
  box-shadow: inset 0 0 2.2rem rgba(0,0,0,.45), inset 0 0 .3rem rgba(255,255,255,.15);
}

.cb-40__caption {
  padding: .1rem .25rem .35rem;
  font-size: 1.25rem;
  color: var(--ink);
  text-align: center;
  line-height: 1.15;
}

.cb-40__btn:is(:hover,:focus-visible) .cb-40__frame {
  rotate: -.5deg;
  translate: 0 -4px;
  box-shadow: 0 22px 34px -14px rgba(0,0,0,.75);
}

.cb-40__btn:is(:hover,:focus-visible) .cb-40__img {
  filter: brightness(1) contrast(1.04) saturate(1.06) hue-rotate(0deg) blur(0);
  scale: 1;
}

.cb-40__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 6px;
}

.cb-40__btn:active .cb-40__frame {
  rotate: -1.6deg;
  translate: 0 1px;
  box-shadow: 0 6px 12px -8px rgba(0,0,0,.7);
}

.cb-40__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.6);
}

@media (prefers-reduced-motion: reduce) {
  .cb-40__frame,
    .cb-40__img {
    transition: none;
  }

  .cb-40__img {
    filter: none;
    scale: 1;
  }
}

@media (forced-colors: active) {
  .cb-40__frame {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
    rotate: 0deg;
  }

  .cb-40__caption {
    color: ButtonText;
  }

  .cb-40__vignette {
    display: none;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-origami-fortune-cookie-button/"
title: "CSS Origami Fortune Cookie Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Press the cookie and it cracks: two clipped halves rotate apart, a paper slip slides out from the fracture, and a fortune is written into it — a real…"
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Origami Fortune Cookie Button
Source: https://codefronts.com/components/css-buttons/css-origami-fortune-cookie-button/

Press the cookie and it cracks: two clipped halves rotate apart, a paper slip slides out from the fracture, and a fortune is written into it — a real aria-live region, so the message is announced rather than merely displayed. Press again to reset.
## HTML
```html
<div class="cb-28">
  <div class="cb-28__stage">
    <div class="cb-28__wrap">
      <p class="cb-28__slip" role="status" aria-live="polite"></p>
      <button class="cb-28__btn" type="button" aria-expanded="false">
        <span class="cb-28__half cb-28__half--l" aria-hidden="true"></span>
        <span class="cb-28__half cb-28__half--r" aria-hidden="true"></span>
        <span class="cb-28__label">Open your fortune</span>
      </button>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=DM+Sans:wght@600;700&display=swap');

.cb-28 {
  --bg: #2a1a1c;
  --cookie: #e8b874;
  --cookie-lo: #b8843f;
  --ink: #4a2a10;
  --label: #f2ddb9;
  --slip: #fdfaf3;
  --slip-ink: #3b2b22;
  --sans: "DM Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Cormorant Garamond",ui-serif,Georgia,serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(34rem 22rem at 50% 46%, color-mix(in oklab,var(--cookie) 18%,transparent), transparent 72%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-28 {
    --cookie: oklch(82% .1 76);
    --cookie-lo: oklch(65% .11 66);
    --bg: oklch(24% .03 25);
  }
}

@media (prefers-color-scheme: light) {
  .cb-28:not([data-theme="dark"]) {
    --bg: #3a2528;
  }
}

.cb-28[data-theme="light"] {
  --bg: #3a2528;
}

.cb-28,
.cb-28 *,
.cb-28 *::before,
.cb-28 *::after {
  box-sizing: border-box;
}

.cb-28__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-28__wrap {
  display: grid;
  justify-items: center;
  gap: .9rem;
}

.cb-28__slip {
  margin: 0;
  max-width: 22rem;
  min-height: 0;
  padding: 0 1.1rem;
  border-radius: .2rem;
  font-family: var(--serif);
  font-size: 1.0625rem;
  font-style: italic;
  line-height: 1.5;
  text-align: center;
  color: var(--slip-ink);
  background: var(--slip);
  box-shadow: 0 8px 18px -12px rgba(0,0,0,.7);
  scale: .72;
  opacity: 0;
  height: 0;
  overflow: hidden;
  transition: scale .5s cubic-bezier(.16,1,.3,1), opacity .35s ease, height .45s cubic-bezier(.16,1,.3,1), padding .45s ease;
}

.cb-28.is-open .cb-28__slip {
  scale: 1;
  opacity: 1;
  height: auto;
  padding: .85rem 1.1rem;
}

.cb-28__btn {
  position: relative;
  cursor: pointer;
  border: 0;
  background: transparent;
  padding: 4.9rem 0 0;
  min-width: 13rem;
  font: inherit;
  font-size: .9375rem;
  font-weight: 700;
  color: var(--ink);
  -webkit-tap-highlight-color: transparent;
}
/* The label lives BELOW the cookie, never inside the fracture — otherwise the
   crack opens straight through the middle of the word. */

.cb-28__label {
  display: block;
  position: relative;
  z-index: 3;
  font-size: .9375rem;
  font-weight: 700;
  letter-spacing: .01em;
  color: var(--label);
  transition: color .3s ease;
}

.cb-28__half {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: 4.25rem;
  z-index: 1;
  background: radial-gradient(120% 90% at 30% 20%, color-mix(in oklab,var(--cookie) 70%,white), transparent 60%), linear-gradient(160deg, var(--cookie), var(--cookie-lo));
  box-shadow: inset 0 -2px 4px rgba(0,0,0,.25), 0 12px 22px -12px rgba(0,0,0,.7);
  transition: rotate .55s cubic-bezier(.16,1,.3,1), translate .55s cubic-bezier(.16,1,.3,1), filter .4s ease;
}

.cb-28__half--l {
  clip-path: polygon(0 0,52% 0,45% 50%,52% 100%,0 100%);
  border-radius: 2.2rem 0 0 2.2rem;
  transform-origin: 0% 50%;
}

.cb-28__half--r {
  clip-path: polygon(52% 0,100% 0,100% 100%,52% 100%,45% 50%);
  border-radius: 0 2.2rem 2.2rem 0;
  transform-origin: 100% 50%;
}

.cb-28__btn:hover .cb-28__half {
  filter: brightness(1.05);
}

.cb-28__btn:hover .cb-28__half--l {
  rotate: -2deg;
}

.cb-28__btn:hover .cb-28__half--r {
  rotate: 2deg;
}

.cb-28__btn:focus-visible {
  outline: 2px solid var(--cookie);
  outline-offset: 4px;
  border-radius: 1rem;
}

.cb-28.is-open .cb-28__half--l {
  rotate: -9deg;
  translate: -1.1rem .2rem;
}

.cb-28.is-open .cb-28__half--r {
  rotate: 9deg;
  translate: 1.1rem .2rem;
}

.cb-28.is-open .cb-28__label {
  color: color-mix(in oklab,var(--label) 72%,var(--cookie-lo));
}

.cb-28__btn:active .cb-28__half {
  scale: .98;
}

@media (prefers-reduced-motion: reduce) {
  .cb-28__half,
    .cb-28__slip {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-28__half {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-28__label {
    color: CanvasText;
  }

  .cb-28__slip {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-28');
  const btn = root && root.querySelector('.cb-28__btn');
  const slip = root && root.querySelector('.cb-28__slip');
  if (!btn) return;
  const fortunes = [
    'The bug you fear is a typo you already fixed.',
    'Ship the small thing today; the big thing will follow.',
    'A stranger will use your CSS at 3am and be grateful.',
    'Delete one thing before you add three.',
    'Your next idea arrives while you are away from the keyboard.',
  ];
  let open = false;
  let last = -1;
  const pick = () => {
    let i = last;
    while (i === last) i = Math.floor(Math.random() * fortunes.length);
    last = i;
    return fortunes[i];
  };
  btn.addEventListener('click', () => {
    open = !open;
    root.classList.toggle('is-open', open);
    btn.setAttribute('aria-expanded', String(open));
    slip.textContent = open ? pick() : '';
  });
})();
```

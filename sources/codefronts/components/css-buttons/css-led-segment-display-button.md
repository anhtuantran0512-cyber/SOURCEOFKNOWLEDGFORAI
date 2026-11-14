---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-led-segment-display-button/"
title: "CSS LED Segment Display Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A machined instrument panel with a real seven-segment readout: every digit is seven CSS bars, lit from a bitmask lookup table, glowing with a layered shadow…"
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS LED Segment Display Button
Source: https://codefronts.com/components/css-buttons/css-led-segment-display-button/

A machined instrument panel with a real seven-segment readout: every digit is seven CSS bars, lit from a bitmask lookup table, glowing with a layered shadow bloom against a smoked lens. Press the button and the counter ticks up with the correct segment-by-segment switching.
## HTML
```html
<div class="cb-36">
  <div class="cb-36__stage">
    <button class="cb-36__btn" type="button" aria-label="Increment the counter">
      <span class="cb-36__lens" aria-hidden="true">
        <span class="cb-36__digit" data-i="0">
          <i class="cb-36__seg cb-36__seg--a" data-s="a"></i><i class="cb-36__seg cb-36__seg--b" data-s="b"></i><i class="cb-36__seg cb-36__seg--c" data-s="c"></i><i class="cb-36__seg cb-36__seg--d" data-s="d"></i><i class="cb-36__seg cb-36__seg--e" data-s="e"></i><i class="cb-36__seg cb-36__seg--f" data-s="f"></i><i class="cb-36__seg cb-36__seg--g" data-s="g"></i>
        </span>
        <span class="cb-36__digit" data-i="1">
          <i class="cb-36__seg cb-36__seg--a" data-s="a"></i><i class="cb-36__seg cb-36__seg--b" data-s="b"></i><i class="cb-36__seg cb-36__seg--c" data-s="c"></i><i class="cb-36__seg cb-36__seg--d" data-s="d"></i><i class="cb-36__seg cb-36__seg--e" data-s="e"></i><i class="cb-36__seg cb-36__seg--f" data-s="f"></i><i class="cb-36__seg cb-36__seg--g" data-s="g"></i>
        </span>
        <span class="cb-36__digit" data-i="2">
          <i class="cb-36__seg cb-36__seg--a" data-s="a"></i><i class="cb-36__seg cb-36__seg--b" data-s="b"></i><i class="cb-36__seg cb-36__seg--c" data-s="c"></i><i class="cb-36__seg cb-36__seg--d" data-s="d"></i><i class="cb-36__seg cb-36__seg--e" data-s="e"></i><i class="cb-36__seg cb-36__seg--f" data-s="f"></i><i class="cb-36__seg cb-36__seg--g" data-s="g"></i>
        </span>
      </span>
      <span class="cb-36__sr" role="status" aria-live="polite">0</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&display=swap');

.cb-36 {
  --bg: #0b0d0c;
  --panel: #1c211f;
  --panel-hi: #2c3331;
  --lens: #0a0f0d;
  --on: #5ef08a;
  --off: #1f2b24;
  --radius: .8rem;
  --sans: "Chakra Petch",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(34rem 20rem at 50% 44%, #17201c, transparent 74%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-36 {
    --on: oklch(84% .2 148);
    --off: oklch(28% .03 150);
  }
}

@media (prefers-color-scheme: light) {
  .cb-36:not([data-theme="dark"]) {
    --bg: #151a18;
  }
}

.cb-36[data-theme="light"] {
  --bg: #151a18;
}

.cb-36,
.cb-36 *,
.cb-36 *::before,
.cb-36 *::after {
  box-sizing: border-box;
}

.cb-36__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-36__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cb-36__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  place-items: center;
  padding: .9rem;
  border: 1px solid #0a0d0c;
  border-radius: var(--radius);
  background: linear-gradient(180deg, var(--panel-hi), var(--panel));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.14), inset 0 -2px 4px rgba(0,0,0,.5), 0 14px 26px -12px rgba(0,0,0,.8);
  transition: translate .16s ease, box-shadow .2s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-36__lens {
  display: flex;
  gap: .5rem;
  padding: .75rem 1rem;
  border-radius: .45rem;
  background: radial-gradient(120% 140% at 50% 0%, rgba(255,255,255,.06), transparent 60%), var(--lens);
  box-shadow: inset 0 2px 8px rgba(0,0,0,.85), inset 0 0 0 1px rgba(255,255,255,.05);
}

.cb-36__digit {
  position: relative;
  display: block;
  width: 1.6rem;
  height: 2.9rem;
}

.cb-36__seg {
  position: absolute;
  display: block;
  background: var(--off);
  border-radius: .06rem;
  transition: background-color .09s linear, box-shadow .09s linear;
}

.cb-36__seg--a,
.cb-36__seg--d,
.cb-36__seg--g {
  left: 14%;
  width: 72%;
  height: .28rem;
  clip-path: polygon(.18rem 0,calc(100% - .18rem) 0,100% 50%,calc(100% - .18rem) 100%,.18rem 100%,0 50%);
}

.cb-36__seg--a {
  top: 0;
}

.cb-36__seg--g {
  top: calc(50% - .14rem);
}

.cb-36__seg--d {
  bottom: 0;
}

.cb-36__seg--b,
.cb-36__seg--c,
.cb-36__seg--e,
.cb-36__seg--f {
  width: .28rem;
  height: calc(50% - .34rem);
  clip-path: polygon(0 .18rem,50% 0,100% .18rem,100% calc(100% - .18rem),50% 100%,0 calc(100% - .18rem));
}

.cb-36__seg--f {
  left: 0;
  top: .34rem;
}

.cb-36__seg--b {
  right: 0;
  top: .34rem;
}

.cb-36__seg--e {
  left: 0;
  bottom: .34rem;
}

.cb-36__seg--c {
  right: 0;
  bottom: .34rem;
}

.cb-36__seg.is-on {
  background: var(--on);
  box-shadow: 0 0 4px var(--on), 0 0 12px color-mix(in oklab,var(--on) 55%,transparent), 0 0 22px color-mix(in oklab,var(--on) 28%,transparent);
}

.cb-36__btn:hover {
  translate: 0 -1px;
}

.cb-36__btn:active {
  translate: 0 2px;
  box-shadow: inset 0 2px 8px rgba(0,0,0,.7);
}

.cb-36__btn:focus-visible {
  outline: 2px solid var(--on);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-36__btn,
    .cb-36__seg {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-36__btn {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-36__lens {
    background: Canvas;
    box-shadow: none;
  }

  .cb-36__seg {
    background: GrayText;
    box-shadow: none;
  }

  .cb-36__seg.is-on {
    background: Highlight;
    box-shadow: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.cb-36__btn');
  if (!btn) return;
  const MAP = { 0:'abcdef', 1:'bc', 2:'abdeg', 3:'abcdg', 4:'bcfg', 5:'acdfg', 6:'acdefg', 7:'abc', 8:'abcdefg', 9:'abcdfg' };
  const digits = [...btn.querySelectorAll('.cb-36__digit')];
  const live = btn.querySelector('.cb-36__sr');
  let value = 0;
  const render = () => {
    const text = String(value % 1000).padStart(digits.length, '0');
    digits.forEach((d, i) => {
      const lit = MAP[text[i]] || '';
      d.querySelectorAll('.cb-36__seg').forEach((s) => s.classList.toggle('is-on', lit.includes(s.dataset.s)));
    });
    live.textContent = String(value % 1000);
  };
  btn.addEventListener('click', () => { value += 1; render(); });
  render();
})();
```

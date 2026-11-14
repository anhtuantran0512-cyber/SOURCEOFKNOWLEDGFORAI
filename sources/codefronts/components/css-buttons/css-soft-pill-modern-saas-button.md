---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-soft-pill-modern-saas-button/"
title: "CSS Soft Pill Modern SaaS Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "The button a 2027 SaaS product ships: a soft pill with a true 1px gradient stroke drawn by mask-composite, an inner top-light, a spring lift on hover, a…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Soft Pill Modern SaaS Button
Source: https://codefronts.com/components/css-buttons/css-soft-pill-modern-saas-button/

The button a 2027 SaaS product ships: a soft pill with a true 1px gradient stroke drawn by mask-composite, an inner top-light, a spring lift on hover, a shortcut chip that dims as the arrow slides, and a focus ring that respects the pill's radius exactly.
## HTML
```html
<div class="cb-32">
  <div class="cb-32__stage">
    <button class="cb-32__btn" type="button">
      <span class="cb-32__label">Create workspace</span>
      <kbd class="cb-32__kbd">⌘ K</kbd>
      <svg class="cb-32__arrow" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13"/><path d="M12.5 6 18.5 12l-6 6"/></svg>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700&display=swap');

.cb-32 {
  --bg: #f7f8fa;
  --surface: #ffffff;
  --ink: #101114;
  --muted: #6c7180;
  --accent: #3d5afe;
  --stroke-a: #e3e6ee;
  --stroke-b: #c9cede;
  --lift: 3px;
  --spring: linear(0,.4 7%,.83 15%,1.06 23%,1.09 28%,1.03 37%,1 52%,1);
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(48rem 30rem at 50% -10%, color-mix(in oklab,var(--accent) 8%,transparent), transparent 70%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-32 {
    --bg: oklch(97.5% .004 265);
    --accent: oklch(52% .22 268);
    --stroke-a: oklch(92% .008 265);
    --stroke-b: oklch(85% .012 265);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-32:not([data-theme="light"]) {
    --bg: #0b0c10;
    --surface: #15171d;
    --ink: #f3f4f8;
    --muted: #9aa0b0;
    --stroke-a: #2b2f3a;
    --stroke-b: #40465a;
    --accent: #7c8dff;
  }
}

.cb-32[data-theme="dark"] {
  --bg: #0b0c10;
  --surface: #15171d;
  --ink: #f3f4f8;
  --muted: #9aa0b0;
  --stroke-a: #2b2f3a;
  --stroke-b: #40465a;
  --accent: #7c8dff;
}

.cb-32,
.cb-32 *,
.cb-32 *::before,
.cb-32 *::after {
  box-sizing: border-box;
}

.cb-32__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-32__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .7rem;
  min-height: 3.25rem;
  padding: 0 .7rem 0 1.5rem;
  border: 0;
  border-radius: 999px;
  font: inherit;
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: -.012em;
  color: var(--ink);
  background: linear-gradient(180deg, var(--surface), color-mix(in oklab,var(--surface) 92%,var(--stroke-a)));
  box-shadow: inset 0 1px 0 color-mix(in oklab,white 85%,transparent), 0 1px 2px color-mix(in oklab,var(--ink) 8%,transparent), 0 10px 24px -14px color-mix(in oklab,var(--ink) 45%,transparent);
  transition: translate .4s cubic-bezier(.16,1,.3,1), box-shadow .35s ease, color .25s ease;
}

@supports (transition-timing-function: linear(0,1)) {
  .cb-32__btn {
    transition: translate .5s var(--spring), box-shadow .35s ease, color .25s ease;
  }
}

.cb-32__btn::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  pointer-events: none;
  background: linear-gradient(160deg, var(--stroke-a), var(--stroke-b));
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  transition: background .3s ease;
}

@supports not ((mask-composite: exclude) or (-webkit-mask-composite: xor)) {
  .cb-32__btn {
    border: 1px solid var(--stroke-b);
  }

  .cb-32__btn::before {
    display: none;
  }
}

.cb-32__kbd {
  font: inherit;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .04em;
  color: var(--muted);
  padding: .3rem .5rem;
  border-radius: .45rem;
  background: color-mix(in oklab,var(--ink) 6%,transparent);
  box-shadow: inset 0 0 0 1px color-mix(in oklab,var(--ink) 8%,transparent);
  transition: opacity .25s ease, translate .4s cubic-bezier(.16,1,.3,1);
}

.cb-32__arrow {
  width: 1.05rem;
  height: 1.05rem;
  margin-right: .45rem;
  color: var(--accent);
  transition: translate .45s cubic-bezier(.16,1,.3,1);
}

.cb-32__btn:hover {
  translate: 0 calc(var(--lift) * -1);
  box-shadow: inset 0 1px 0 color-mix(in oklab,white 90%,transparent), 0 2px 4px color-mix(in oklab,var(--ink) 10%,transparent), 0 18px 34px -16px color-mix(in oklab,var(--accent) 45%,transparent);
}

.cb-32__btn:hover::before {
  background: linear-gradient(160deg, color-mix(in oklab,var(--accent) 45%,var(--stroke-a)), var(--stroke-b));
}

.cb-32__btn:hover .cb-32__kbd {
  opacity: .45;
  translate: -.15rem 0;
}

.cb-32__btn:hover .cb-32__arrow {
  translate: .25rem 0;
}

.cb-32__btn:active {
  translate: 0 1px;
  box-shadow: inset 0 1px 3px color-mix(in oklab,var(--ink) 18%,transparent);
}

.cb-32__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cb-32__btn:disabled {
  cursor: not-allowed;
  color: var(--muted);
  opacity: .6;
  translate: 0;
}

@media (prefers-reduced-motion: reduce) {
  .cb-32__btn,
    .cb-32__kbd,
    .cb-32__arrow,
    .cb-32__btn::before {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-32__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-32__btn::before {
    display: none;
  }

  .cb-32__kbd {
    border: 1px solid ButtonText;
    background: ButtonFace;
  }
}
```

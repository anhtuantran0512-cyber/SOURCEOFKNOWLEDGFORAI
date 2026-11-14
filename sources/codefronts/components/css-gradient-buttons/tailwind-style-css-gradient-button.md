---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/tailwind-style-css-gradient-button/"
title: "Tailwind Style CSS Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A docs-style specimen grid of the four most-loved utility-framework gradient recipes — indigo/purple, cyan/blue, emerald/teal, rose/orange — in pure CSS with…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Style CSS Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/tailwind-style-css-gradient-button/

A docs-style specimen grid of the four most-loved utility-framework gradient recipes — indigo/purple, cyan/blue, emerald/teal, rose/orange — in pure CSS with hover shade-deepening.
## HTML
```html
<div class="gb-18">
  <div class="gb-18__doc">
    <div class="gb-18__dochead">
      <b>Gradient recipes</b>
      <code>bg-gradient-to-r</code>
    </div>
    <div class="gb-18__grid">
      <div class="gb-18__cell">
        <button class="gb-18__btn gb-18__btn--iris" type="button">Deploy project</button>
        <p class="gb-18__util">from-indigo-500 to-purple-500</p>
      </div>
      <div class="gb-18__cell">
        <button class="gb-18__btn gb-18__btn--sky" type="button">Invite your team</button>
        <p class="gb-18__util">from-cyan-500 to-blue-500</p>
      </div>
      <div class="gb-18__cell">
        <button class="gb-18__btn gb-18__btn--mint" type="button">Enable billing</button>
        <p class="gb-18__util">from-emerald-500 to-teal-500</p>
      </div>
      <div class="gb-18__cell">
        <button class="gb-18__btn gb-18__btn--ember" type="button">Upgrade plan</button>
        <p class="gb-18__util">from-rose-500 to-orange-500</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.gb-18,
.gb-18 *,
.gb-18 *::before,
.gb-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-18 ::selection {
  background: #6366f1;
  color: #fff;
}

.gb-18 {
  /* Tailwind-inspired tokens: indigo/purple, cyan/blue, emerald/teal, rose/orange */
  --indigo-500: #6366f1;
  --purple-500: #a855f7;
  --cyan-500: #06b6d4;
  --blue-500: #3b82f6;
  --emerald-500: #10b981;
  --teal-500: #14b8a6;
  --rose-500: #f43f5e;
  --orange-500: #f97316;
  --slate-900: #0f172a;
  --slate-500: #64748b;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: #fff;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-18__doc {
  width: 100%;
  max-width: 520px;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  overflow: hidden;
}

.gb-18__dochead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px;
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
}

.gb-18__dochead b {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--slate-900);
}

.gb-18__dochead code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: 11.5px;
  color: var(--slate-500);
  background: #eef2f7;
  padding: 3px 8px;
  border-radius: 6px;
}

.gb-18__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(210px,1fr));
  gap: 1px;
  background: #e2e8f0;
}

.gb-18__cell {
  background: #fff;
  padding: 26px 22px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}
/* The utility recipe: from/to duotone, shadow-{color}/50, hover
   swaps to deeper shades via a cross-fading ::before layer. */

.gb-18__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  padding: 12px 26px;
  border: none;
  border-radius: 10px;
  font-family: inherit;
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  cursor: pointer;
  background-image: linear-gradient(to right,var(--from),var(--to));
  box-shadow: 0 10px 22px -8px var(--ring);
  transition: box-shadow .3s ease,transform .2s ease;
  -webkit-tap-highlight-color: transparent;
}

.gb-18__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background-image: linear-gradient(to right,var(--from-hover),var(--to-hover));
  opacity: 0;
  transition: opacity .3s ease;
}

.gb-18__btn:hover {
  transform: translateY(-1.5px);
  box-shadow: 0 14px 28px -8px var(--ring);
}

.gb-18__btn:hover::before {
  opacity: 1;
}

.gb-18__btn:active {
  transform: translateY(0) scale(.98);
}

.gb-18__btn:focus-visible {
  outline: 3px solid var(--from);
  outline-offset: 3px;
}

.gb-18__btn--iris {
  --from: var(--indigo-500);
  --to: var(--purple-500);
  --from-hover: #4f46e5;
  --to-hover: #9333ea;
  --ring: rgba(99,102,241,.5);
}

.gb-18__btn--sky {
  --from: var(--cyan-500);
  --to: var(--blue-500);
  --from-hover: #0891b2;
  --to-hover: #2563eb;
  --ring: rgba(6,182,212,.5);
}

.gb-18__btn--mint {
  --from: var(--emerald-500);
  --to: var(--teal-500);
  --from-hover: #059669;
  --to-hover: #0d9488;
  --ring: rgba(16,185,129,.5);
}

.gb-18__btn--ember {
  --from: var(--rose-500);
  --to: var(--orange-500);
  --from-hover: #e11d48;
  --to-hover: #ea580c;
  --ring: rgba(244,63,94,.5);
}

.gb-18__util {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: 10.5px;
  color: var(--slate-500);
  text-align: center;
  line-height: 1.5;
}

@media (prefers-reduced-motion: reduce) {
  .gb-18__btn,
    .gb-18__btn::before {
    transition: none;
  }

  .gb-18__btn:hover {
    transform: none;
  }
}
```

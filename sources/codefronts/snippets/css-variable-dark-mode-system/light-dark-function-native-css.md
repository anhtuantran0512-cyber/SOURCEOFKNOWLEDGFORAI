---
source: "codefronts"
url: "https://codefronts.com/snippets/css-variable-dark-mode-system/light-dark-function-native-css/"
title: "Modern Native Dark Mode with the CSS light-dark() Function and color-scheme"
section: "snippets"
category: "css-variable-dark-mode-system"
category_name: "CSS Variable Dark Mode Systems"
description: "The cutting-edge, media-query-free approach."
has_js: "true"
---

Here's a working CSS Variable Dark Mode System from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern Native Dark Mode with the CSS light-dark() Function and color-scheme
Source: https://codefronts.com/snippets/css-variable-dark-mode-system/light-dark-function-native-css/

The cutting-edge, media-query-free approach. Declare color-scheme: light dark; once, then write every color as light-dark(<light-value>, <dark-value>) — the browser picks the right one based on the resolved scheme, with no @media block and no duplicated rule set. Manual override becomes a one-liner: change color-scheme to light or dark. This is where CSS dark mode is heading.
## HTML
```html
<section class="cdm-05" data-scheme="system">
  <div class="cdm-05__card">
    <span class="cdm-05__tag">light-dark() · no @media</span>
    <h1>One value, both themes</h1>
    <p>Every color here is written once as <code>light-dark(light, dark)</code>. The switch below just rewrites <code>color-scheme</code> — there isn't a single media query in the CSS.</p>
    <div class="cdm-05__seg" role="radiogroup" aria-label="Color scheme">
      <label><input type="radio" name="cdm5" value="system" checked><span>System</span></label>
      <label><input type="radio" name="cdm5" value="light"><span>Light</span></label>
      <label><input type="radio" name="cdm5" value="dark"><span>Dark</span></label>
    </div>
    <div class="cdm-05__demorow">
      <select class="cdm-05__native" aria-label="Native select follows color-scheme"><option>Native controls follow color-scheme</option><option>No custom scrollbar CSS needed</option></select>
    </div>
  </div>
</section>
```
## CSS
```css
.cdm-05,
.cdm-05 *,
.cdm-05 *::before,
.cdm-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdm-05 {
  color-scheme: light dark;
  --accent: light-dark(oklch(0.55 0.19 25),oklch(0.74 0.17 25));
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 32px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: light-dark(oklch(0.98 0.004 60),oklch(0.16 0.02 30));
  color: light-dark(oklch(0.24 0.02 40),oklch(0.95 0.005 40));
}

.cdm-05[data-scheme="light"] {
  color-scheme: light;
}

.cdm-05[data-scheme="dark"] {
  color-scheme: dark;
}

.cdm-05__card {
  width: min(440px,100%);
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 30px;
  border-radius: 20px;
  /* surface tint DERIVED from --accent with relative color syntax */
  background: light-dark(oklch(1 0 0),oklch(from var(--accent) 0.22 calc(c*0.35) h));
  /* elevation swap: soft drop shadow in light, inset border-glow in dark */
  box-shadow: light-dark(0 18px 46px -22px oklch(0 0 0 / .35),0 0 0 1px oklch(1 0 0 / .12) inset);
}

.cdm-05__tag {
  align-self: flex-start;
  padding: 5px 11px;
  border-radius: 999px;
  font: 600 11px/1 ui-monospace,Menlo,monospace;
  color: #fff;
  background: var(--accent);
}

.cdm-05__card h1 {
  font: 700 clamp(22px,4vw,30px)/1.15 system-ui,sans-serif;
  letter-spacing: -.01em;
}

.cdm-05__card p {
  font: 400 14.5px/1.6 system-ui,sans-serif;
  color: light-dark(oklch(0.45 0.02 40),oklch(0.72 0.02 40));
  text-wrap: pretty;
}

.cdm-05 code {
  font: 600 12.5px/1 ui-monospace,Menlo,monospace;
  padding: 2px 5px;
  border-radius: 5px;
  background: light-dark(oklch(0.94 0.006 60),oklch(0.26 0.02 40));
  color: inherit;
}

.cdm-05__seg {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 4px;
  padding: 4px;
  border-radius: 12px;
  background: light-dark(oklch(0.95 0.006 60),oklch(0.22 0.02 40));
}

.cdm-05__seg label {
  position: relative;
}

.cdm-05__seg input {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.cdm-05__seg span {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 40px;
  border-radius: 8px;
  font: 600 13px/1 system-ui,sans-serif;
  color: light-dark(oklch(0.45 0.02 40),oklch(0.72 0.02 40));
  transition: background-color .2s ease,color .2s ease;
}

.cdm-05__seg input:checked + span {
  background: light-dark(oklch(1 0 0),oklch(0.3 0.02 40));
  color: light-dark(oklch(0.24 0.02 40),oklch(0.97 0.005 40));
  box-shadow: 0 1px 4px oklch(0 0 0 / .2);
}

.cdm-05__seg input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdm-05__native {
  min-height: 44px;
  padding: 0 12px;
  border-radius: 10px;
  border: 1px solid light-dark(oklch(0.9 0.008 60),oklch(0.32 0.02 40));
  background: light-dark(oklch(1 0 0),oklch(0.2 0.02 40));
  color: inherit;
  font: 400 14px/1 system-ui,sans-serif;
  width: 100%;
}

.cdm-05__native:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

@media (prefers-reduced-motion: reduce) {
  .cdm-05 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.cdm-05');
  var radios = root.querySelectorAll('input[name="cdm5"]');
  radios.forEach(function (r) {
    r.addEventListener('change', function () {
      // the ENTIRE switch: rewrite color-scheme; light-dark() re-resolves every color
      root.dataset.scheme = r.value;
    });
  });
})();
```

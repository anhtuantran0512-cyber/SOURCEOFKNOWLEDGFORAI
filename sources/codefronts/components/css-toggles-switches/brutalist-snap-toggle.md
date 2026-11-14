---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/brutalist-snap-toggle/"
title: "Brutalist Snap Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "Anti-animation as a statement: a raw, square switch with 3px black borders and a hard offset shadow."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Snap Toggle
Source: https://codefronts.com/components/css-toggles-switches/brutalist-snap-toggle/

Anti-animation as a statement: a raw, square switch with 3px black borders and a hard offset shadow. The block thumb doesn't glide — it SNAPS to the other side in a single 90ms step, the shadow jumps, and the state stamps itself in uppercase mono. Zero easing, zero apology.
## HTML
```html
<section class="tgl-17" aria-label="Brutalist snap toggle">
  <label class="tgl-17__card" for="tgl-17-sw">
    <span class="tgl-17__lbl">NEWSLETTER</span>
    <span class="tgl-17__unit">
      <input type="checkbox" id="tgl-17-sw" class="tgl-17__sw" role="switch">
      <span class="tgl-17__state" aria-hidden="true"><i>OFF</i><i>ON</i></span>
    </span>
  </label>
  <p class="tgl-17__cap">steps(1) — it snaps, it does not glide</p>
</section>
```
## CSS
```css
.tgl-17,
.tgl-17 *,
.tgl-17 *::before,
.tgl-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-17 {
  font-family: ui-monospace,'SF Mono',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 30px;
  padding: 60px 20px;
  background: #f0ede6;
}

.tgl-17__card {
  display: flex;
  align-items: center;
  gap: 30px;
  background: #fff;
  border: 3px solid #000;
  box-shadow: 6px 6px 0 #000;
  padding: 22px 28px;
  cursor: pointer;
  transition: transform .09s steps(1,end),box-shadow .09s steps(1,end);
}

.tgl-17__card:active {
  transform: translate(3px,3px);
  box-shadow: 3px 3px 0 #000;
}

.tgl-17__lbl {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .14em;
  color: #000;
}

.tgl-17__unit {
  position: relative;
  display: block;
}

.tgl-17__sw {
  appearance: none;
  -webkit-appearance: none;
  display: block;
  width: 104px;
  height: 48px;
  border: 3px solid #000;
  background: #fff;
  cursor: pointer;
  position: relative;
  transition: background-color .09s steps(1,end);
}

.tgl-17__sw:checked {
  background: #ffe600;
}

.tgl-17__sw::before {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 36px;
  height: 36px;
  background: #000;
  transition: transform .09s steps(1,end);
}

.tgl-17__sw:checked::before {
  transform: translateX(56px);
}

.tgl-17__state {
  position: absolute;
  inset: 3px;
  display: block;
  pointer-events: none;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .1em;
  color: #000;
}

.tgl-17__state i {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-style: normal;
}

.tgl-17__state i:nth-child(1) {
  right: 10px;
}

.tgl-17__state i:nth-child(2) {
  left: 10px;
  display: none;
}

.tgl-17__sw:checked ~ .tgl-17__state i:nth-child(1) {
  display: none;
}

.tgl-17__sw:checked ~ .tgl-17__state i:nth-child(2) {
  display: block;
}

.tgl-17__sw:focus-visible {
  outline: 4px solid #000;
  outline-offset: 4px;
}

.tgl-17__cap {
  font-size: 12px;
  letter-spacing: .1em;
  color: #8a8578;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-17__card,
    .tgl-17__sw,
    .tgl-17__sw::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — steps(1,end) timing snaps the block thumb in a single frame, and :active pushes the card into its hard offset shadow. */
```

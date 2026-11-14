---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/tiered-size-chart-guide/"
title: "Tiered Size Chart Guide"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A grid-based sizing table that opens from a 'Size guide' link beside the variant picker, with a zero-JS cm/inch unit toggle — the apparel-store measurement…"
has_js: "false"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tiered Size Chart Guide
Source: https://codefronts.com/components/css-modals/tiered-size-chart-guide/

A grid-based sizing table that opens from a 'Size guide' link beside the variant picker, with a zero-JS cm/inch unit toggle — the apparel-store measurement overlay, built entirely from a checkbox and sibling selectors.
## HTML
```html
<div class="cm-08">
  <div class="cm-08__ctx">
    <div class="cm-08__sizes"><span class="cm-08__lbl">Size</span>
      <span class="cm-08__chip">S</span><span class="cm-08__chip cm-08__chip--on">M</span><span class="cm-08__chip">L</span><span class="cm-08__chip">XL</span>
    </div>
    <input type="checkbox" id="cm-08-t" class="cm-08__sr">
    <label for="cm-08-t" class="cm-08__link"><span aria-hidden="true">📏</span> Size guide</label>
  </div>

  <div class="cm-08__overlay" role="dialog" aria-modal="true" aria-labelledby="cm-08-title">
    <div class="cm-08__panel">
      <div class="cm-08__phead">
        <h2 id="cm-08-title">Size guide</h2>
        <div class="cm-08__unit">
          <input type="radio" name="cm-08-u" id="cm-08-cm" checked><label for="cm-08-cm">cm</label>
          <input type="radio" name="cm-08-u" id="cm-08-in"><label for="cm-08-in">in</label>
        </div>
        <label for="cm-08-t" class="cm-08__x" role="button" aria-label="Close size guide">&times;</label>
      </div>
      <div class="cm-08__scroll">
        <table class="cm-08__table">
          <thead><tr><th scope="col">Size</th><th scope="col">Chest</th><th scope="col">Waist</th><th scope="col">Length</th></tr></thead>
          <tbody class="cm-08__body cm-08__body--cm">
            <tr><th scope="row">XS</th><td>86</td><td>71</td><td>68</td></tr>
            <tr><th scope="row">S</th><td>91</td><td>76</td><td>70</td></tr>
            <tr><th scope="row">M</th><td>97</td><td>81</td><td>72</td></tr>
            <tr><th scope="row">L</th><td>102</td><td>86</td><td>74</td></tr>
            <tr><th scope="row">XL</th><td>109</td><td>94</td><td>76</td></tr>
          </tbody>
          <tbody class="cm-08__body cm-08__body--in">
            <tr><th scope="row">XS</th><td>34</td><td>28</td><td>26.8</td></tr>
            <tr><th scope="row">S</th><td>36</td><td>30</td><td>27.6</td></tr>
            <tr><th scope="row">M</th><td>38</td><td>32</td><td>28.3</td></tr>
            <tr><th scope="row">L</th><td>40</td><td>34</td><td>29.1</td></tr>
            <tr><th scope="row">XL</th><td>43</td><td>37</td><td>29.9</td></tr>
          </tbody>
        </table>
      </div>
      <p class="cm-08__note">Body measurements. If you're between sizes, we recommend sizing up for a relaxed fit.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.cm-08,
.cm-08 *,
.cm-08 *::before,
.cm-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-08 {
  --accent: oklch(0.72 0.14 250);
  position: relative;
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#0e1016,#07080b);
}

.cm-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
}

.cm-08__ctx {
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: flex-start;
  padding: 24px;
  border-radius: 16px;
  background: #12151d;
  border: 1px solid #232836;
}

.cm-08__sizes {
  display: flex;
  align-items: center;
  gap: 8px;
}

.cm-08__lbl {
  font-size: 12px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #8890a2;
  margin-right: 6px;
}

.cm-08__chip {
  min-width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  font: 600 13px system-ui;
  color: #c3cad8;
  border: 1px solid #2c3444;
  background: #0e1119;
}

.cm-08__chip--on {
  border-color: var(--accent);
  color: #fff;
  background: color-mix(in oklch,var(--accent) 22%,#0e1119);
}

.cm-08__link {
  cursor: pointer;
  font: 600 13px system-ui;
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 3px;
  padding: 4px;
}

.cm-08__link:hover {
  filter: brightness(1.15);
}

.cm-08__sr:focus-visible+.cm-08__link {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 4px;
}

.cm-08__overlay {
  position: fixed;
  inset: 0;
  z-index: 10;
  display: grid;
  place-items: center;
  padding: 24px;
  background: rgba(6,8,12,.66);
  backdrop-filter: blur(4px);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .28s,visibility .28s;
}

.cm-08:has(.cm-08__sr:checked) .cm-08__overlay {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.cm-08__panel {
  width: min(460px,94vw);
  max-height: 88dvh;
  display: flex;
  flex-direction: column;
  border-radius: 18px;
  background: linear-gradient(180deg,#141822,#0f131b);
  border: 1px solid #262c3c;
  box-shadow: 0 40px 90px -30px #000;
  transform: scale(.96);
  transition: transform .28s;
}

.cm-08:has(.cm-08__sr:checked) .cm-08__panel {
  transform: none;
}

.cm-08__phead {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 20px 22px;
  border-bottom: 1px solid #232a38;
}

.cm-08__phead h2 {
  flex: 1;
  font-size: 18px;
  font-weight: 700;
  color: #f2f5fc;
}

.cm-08__unit {
  display: inline-flex;
  border: 1px solid #2c3444;
  border-radius: 9px;
  overflow: hidden;
}

.cm-08__unit input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cm-08__unit label {
  padding: 7px 14px;
  font: 600 12px system-ui;
  color: #98a1b4;
  cursor: pointer;
  background: #0e1119;
  transition: all .15s;
}

.cm-08__unit input:checked+label {
  background: color-mix(in oklch,var(--accent) 26%,#0e1119);
  color: #fff;
}

.cm-08__unit input:focus-visible+label {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.cm-08__x {
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  cursor: pointer;
  color: #8b93a4;
  font-size: 22px;
  background: transparent;
  transition: background .2s,color .2s;
}

.cm-08__x:hover {
  background: #1c2230;
  color: #fff;
}

.cm-08__scroll {
  overflow: auto;
  padding: 6px 8px;
}

.cm-08__table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.cm-08__table thead th {
  position: sticky;
  top: 0;
  background: #161b26;
  color: #aeb6c6;
  font-weight: 600;
  font-size: 12px;
  letter-spacing: .05em;
  text-transform: uppercase;
  text-align: center;
  padding: 12px 10px;
  border-bottom: 1px solid #2a3140;
}

.cm-08__table th[scope="row"] {
  text-align: left;
  color: #f0f3fa;
  font-weight: 700;
  padding-left: 18px;
}

.cm-08__table td {
  text-align: center;
  padding: 12px 10px;
  color: #c7cedb;
}

.cm-08__table tbody tr:nth-child(odd) {
  background: rgba(255,255,255,.02);
}

.cm-08__table tbody tr:hover {
  background: color-mix(in oklch,var(--accent) 12%,transparent);
}

.cm-08__body--in {
  display: none;
}

.cm-08:has(#cm-08-in:checked) .cm-08__body--cm {
  display: none;
}

.cm-08:has(#cm-08-in:checked) .cm-08__body--in {
  display: table-row-group;
}

.cm-08__note {
  padding: 16px 22px 20px;
  font-size: 12.5px;
  line-height: 1.6;
  color: #8890a2;
  border-top: 1px solid #232a38;
}

@media (prefers-reduced-motion: reduce) {
  .cm-08__overlay,
    .cm-08__panel {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
/* No JavaScript — a checkbox opens the overlay; a radio pair swaps cm/inch tbodies. */
```

---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/data-table-with-glass-header/"
title: "Data Table with Glass Header"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A data table whose sticky header is a frosted Liquid Glass panel: scroll the rows and they warp and blur as they pass beneath the header's lens, while the…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data Table with Glass Header
Source: https://codefronts.com/snippets/css-table-styles/data-table-with-glass-header/

A data table whose sticky header is a frosted Liquid Glass panel: scroll the rows and they warp and blur as they pass beneath the header's lens, while the column titles stay pin-sharp. The pattern developers actually search for — glass that keeps dense tabular data readable.
## HTML
```html
<section class="ct-13" aria-label="Data table with liquid glass header demo">
  <div class="ct-13__wrap" tabindex="0" role="region" aria-label="Scrollable orders table">
    <table class="ct-13__table">
      <caption class="ct-13__cap">Recent orders — scroll to warp rows under the glass header</caption>
      <thead><tr><th scope="col">Order</th><th scope="col">Customer</th><th scope="col">Status</th><th scope="col" class="ct-13__num">Total</th></tr></thead>
      <tbody>
        <tr><td>#10241</td><td>A. Rivera</td><td><span class="ct-13__pill ct-13__pill--ok">Paid</span></td><td class="ct-13__num">$1,204</td></tr>
        <tr><td>#10240</td><td>M. Chen</td><td><span class="ct-13__pill ct-13__pill--wait">Pending</span></td><td class="ct-13__num">$486</td></tr>
        <tr><td>#10239</td><td>S. Okafor</td><td><span class="ct-13__pill ct-13__pill--ok">Paid</span></td><td class="ct-13__num">$2,940</td></tr>
        <tr><td>#10238</td><td>J. Nowak</td><td><span class="ct-13__pill ct-13__pill--wait">Pending</span></td><td class="ct-13__num">$318</td></tr>
        <tr><td>#10237</td><td>L. Haddad</td><td><span class="ct-13__pill ct-13__pill--ok">Paid</span></td><td class="ct-13__num">$1,775</td></tr>
        <tr><td>#10236</td><td>R. Bianchi</td><td><span class="ct-13__pill ct-13__pill--ok">Paid</span></td><td class="ct-13__num">$642</td></tr>
        <tr><td>#10235</td><td>K. Andersen</td><td><span class="ct-13__pill ct-13__pill--wait">Pending</span></td><td class="ct-13__num">$3,510</td></tr>
        <tr><td>#10234</td><td>T. Mbeki</td><td><span class="ct-13__pill ct-13__pill--ok">Paid</span></td><td class="ct-13__num">$925</td></tr>
      </tbody>
    </table>
  </div>
</section>
```
## CSS
```css
.ct-13,
.ct-13 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ct-13 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: linear-gradient(135deg,#3a1c71,#d76d77 55%,#ffaf7b);
}

.ct-13__wrap {
  width: min(460px,100%);
  max-height: 300px;
  overflow: auto;
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,.3);
  background: color-mix(in oklab,white 8%,transparent);
  box-shadow: 0 26px 56px -28px rgba(0,0,0,.65);
}

.ct-13__wrap:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

.ct-13__table {
  width: 100%;
  border-collapse: collapse;
  color: #fff;
  font-size: 14px;
}

.ct-13__cap {
  padding: 12px 16px;
  font-size: 12px;
  color: rgba(255,255,255,.8);
  text-align: left;
}

.ct-13 thead th {
  position: sticky;
  top: 0;
  z-index: 2;
  padding: 13px 16px;
  text-align: left;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: #fff;
  background: color-mix(in oklab,white 20%,transparent);
  border-bottom: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55);
  backdrop-filter: blur(10px) saturate(180%);
  -webkit-backdrop-filter: blur(10px) saturate(180%);
}

.ct-13 td {
  padding: 12px 16px;
  border-bottom: 1px solid rgba(255,255,255,.14);
}

.ct-13 tbody tr:nth-child(odd) {
  background: rgba(255,255,255,.06);
}

.ct-13__num {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

.ct-13__pill {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
}

.ct-13__pill--ok {
  background: color-mix(in oklab,oklch(0.72 0.17 155) 60%,transparent);
  color: #eafff2;
}

.ct-13__pill--wait {
  background: color-mix(in oklab,oklch(0.8 0.15 85) 55%,transparent);
  color: #fff8e6;
}
```

## JavaScript
```js
/* No JavaScript — a position:sticky <thead> with backdrop-filter frosts every row that scrolls beneath it. Give the wrapper a fixed height so the tbody actually scrolls under the glass. */
```

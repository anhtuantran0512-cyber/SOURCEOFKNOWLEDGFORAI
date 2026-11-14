---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/e-commerce-shopping-cart-table/"
title: "E-Commerce Shopping Cart Table"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A polished checkout cart table with CSS-drawn product thumbnails, custom quantity steppers, a smooth row-removal animation, and a gradient checkout CTA — all…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Shopping Cart Table
Source: https://codefronts.com/snippets/css-table-styles/e-commerce-shopping-cart-table/

A polished checkout cart table with CSS-drawn product thumbnails, custom quantity steppers, a smooth row-removal animation, and a gradient checkout CTA — all within a warm light-mode palette.
## HTML
```html
<div class="ct-05">
  <div class="ct-05__title">🛒 Shopping Cart</div>
  <div class="ct-05__count">3 items in your cart</div>
  <table>
    <thead>
      <tr>
        <th>Product</th>
        <th>Unit Price</th>
        <th>Quantity</th>
        <th>Total</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr id="ct-05-row1">
        <td>
          <div class="ct-05__product">
            <div class="ct-05__thumb" style="background:linear-gradient(135deg,#fde68a,#fbbf24)">🎧</div>
            <div>
              <div class="ct-05__pname">ProSound ANC Headphones</div>
              <div class="ct-05__sku">SKU: PS-ANC-900-BLK</div>
              <span class="ct-05__tag">Free Shipping</span>
            </div>
          </div>
        </td>
        <td><div class="ct-05__unit-price">$249.00</div></td>
        <td>
          <div class="ct-05__qty">
            <button class="ct-05__qty-btn">−</button>
            <input class="ct-05__qty-val" type="number" value="1" min="1">
            <button class="ct-05__qty-btn">+</button>
          </div>
        </td>
        <td><div class="ct-05__price">$249.00</div></td>
        <td><button class="ct-05__remove" onclick="this.closest('tr').classList.add('ct-05--removed')" title="Remove">✕</button></td>
      </tr>
      <tr id="ct-05-row2">
        <td>
          <div class="ct-05__product">
            <div class="ct-05__thumb" style="background:linear-gradient(135deg,#c7d2fe,#818cf8)">⌨️</div>
            <div>
              <div class="ct-05__pname">MechKey RGB Keyboard</div>
              <div class="ct-05__sku">SKU: MK-RGB-TKL-WH</div>
              <span class="ct-05__tag">Best Seller</span>
            </div>
          </div>
        </td>
        <td><div class="ct-05__unit-price">$129.00</div></td>
        <td>
          <div class="ct-05__qty">
            <button class="ct-05__qty-btn">−</button>
            <input class="ct-05__qty-val" type="number" value="2" min="1">
            <button class="ct-05__qty-btn">+</button>
          </div>
        </td>
        <td><div class="ct-05__price">$258.00</div></td>
        <td><button class="ct-05__remove" onclick="this.closest('tr').classList.add('ct-05--removed')" title="Remove">✕</button></td>
      </tr>
      <tr id="ct-05-row3">
        <td>
          <div class="ct-05__product">
            <div class="ct-05__thumb" style="background:linear-gradient(135deg,#bbf7d0,#22c55e)">🖱️</div>
            <div>
              <div class="ct-05__pname">ErgoClick Pro Mouse</div>
              <div class="ct-05__sku">SKU: EC-PRO-G502-BK</div>
            </div>
          </div>
        </td>
        <td><div class="ct-05__unit-price">$79.00</div></td>
        <td>
          <div class="ct-05__qty">
            <button class="ct-05__qty-btn">−</button>
            <input class="ct-05__qty-val" type="number" value="1" min="1">
            <button class="ct-05__qty-btn">+</button>
          </div>
        </td>
        <td><div class="ct-05__price">$79.00</div></td>
        <td><button class="ct-05__remove" onclick="this.closest('tr').classList.add('ct-05--removed')" title="Remove">✕</button></td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="3" style="text-align:right;color:var(--muted)">Subtotal</td>
        <td colspan="2" style="text-align:right;font-weight:700">$586.00</td>
      </tr>
      <tr>
        <td colspan="3" style="text-align:right;color:var(--muted)">Shipping</td>
        <td colspan="2" style="text-align:right;color:var(--success);font-weight:700">FREE</td>
      </tr>
      <tr class="ct-05__total-row">
        <td colspan="3" style="text-align:right">Total</td>
        <td colspan="2" style="text-align:right;color:var(--accent)">$586.00</td>
      </tr>
      <tr>
        <td colspan="5">
          <button class="ct-05__checkout">Proceed to Checkout →</button>
        </td>
      </tr>
    </tfoot>
  </table>
</div>
```
## CSS
```css
.ct-05,
.ct-05 *,
.ct-05 *::before,
.ct-05 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-05 ::selection {
  background: #f97316;
  color: #fff;
}

.ct-05 {
  --bg: #fafafa;
  --card: #ffffff;
  --border: #e5e7eb;
  --text: #111827;
  --muted: #6b7280;
  --accent: #f97316;
  --accent2: #dc2626;
  --success: #16a34a;
  --shadow: rgba(0,0,0,0.08);
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  padding: 32px 24px;
  min-height: 100vh;
  color: var(--text);
}

.ct-05__title {
  font-size: 22px;
  font-weight: 800;
  margin-bottom: 6px;
  letter-spacing: -0.5px;
}

.ct-05__count {
  color: var(--muted);
  font-size: 14px;
  margin-bottom: 24px;
}

.ct-05 table {
  width: 100%;
  border-collapse: collapse;
}

.ct-05 thead th {
  padding: 12px 16px;
  text-align: left;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--muted);
  border-bottom: 2px solid var(--border);
}

.ct-05 thead th:last-child {
  text-align: right;
}

.ct-05 thead th:nth-child(3),
.ct-05 thead th:nth-child(4) {
  text-align: center;
}

.ct-05 tbody tr {
  border-bottom: 1px solid var(--border);
  transition: all 0.35s cubic-bezier(0.4,0,0.2,1);
}

.ct-05 tbody tr.ct-05--removed {
  opacity: 0;
  transform: translateX(40px) scaleY(0.5);
  pointer-events: none;
  max-height: 0;
}

.ct-05 tbody td {
  padding: 18px 16px;
  vertical-align: middle;
}

.ct-05 tbody td:last-child {
  text-align: right;
}

.ct-05 tbody td:nth-child(3),
.ct-05 tbody td:nth-child(4) {
  text-align: center;
}
/* Product thumbnail (CSS-only colored square with emoji) */

.ct-05__product {
  display: flex;
  align-items: center;
  gap: 14px;
}

.ct-05__thumb {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  flex-shrink: 0;
  border: 2px solid var(--border);
  transition: transform 0.2s;
}

.ct-05__product:hover .ct-05__thumb {
  transform: scale(1.08) rotate(-2deg);
}

.ct-05__pname {
  font-weight: 700;
  font-size: 14px;
}

.ct-05__sku {
  font-size: 11px;
  color: var(--muted);
  margin-top: 2px;
}

.ct-05__tag {
  display: inline-block;
  font-size: 10px;
  font-weight: 600;
  padding: 2px 7px;
  border-radius: 4px;
  margin-top: 4px;
  background: rgba(249,115,22,0.1);
  color: var(--accent);
}
/* Quantity stepper */

.ct-05__qty {
  display: inline-flex;
  align-items: center;
  gap: 0;
  border: 2px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
}

.ct-05__qty-btn {
  width: 32px;
  height: 32px;
  border: none;
  background: var(--bg);
  font-size: 16px;
  font-weight: 700;
  color: var(--muted);
  cursor: pointer;
  transition: all 0.15s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ct-05__qty-btn:hover {
  background: var(--accent);
  color: #fff;
}

.ct-05__qty-val {
  width: 36px;
  text-align: center;
  font-size: 14px;
  font-weight: 700;
  border: none;
  background: var(--card);
  color: var(--text);
  -moz-appearance: textfield;
}

.ct-05__qty-val::-webkit-outer-spin-button,
.ct-05__qty-val::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.ct-05__unit-price {
  font-size: 13px;
  color: var(--muted);
}

.ct-05__price {
  font-weight: 800;
  font-size: 15px;
}

.ct-05__remove {
  background: none;
  border: 1px solid var(--border);
  width: 32px;
  height: 32px;
  border-radius: 8px;
  color: var(--muted);
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  float: right;
}

.ct-05__remove:hover {
  background: var(--accent2);
  border-color: var(--accent2);
  color: #fff;
}
/* Summary row */

.ct-05 tfoot td {
  padding: 16px;
  font-size: 13px;
}

.ct-05 tfoot tr:first-child td {
  border-top: 2px solid var(--border);
}

.ct-05 tfoot .ct-05__total-row td {
  padding-top: 12px;
  font-size: 16px;
  font-weight: 800;
}

.ct-05__checkout {
  display: block;
  width: 100%;
  margin-top: 16px;
  padding: 14px;
  border-radius: 12px;
  background: linear-gradient(90deg, var(--accent), #fb923c);
  color: #fff;
  font-weight: 800;
  font-size: 15px;
  border: none;
  cursor: pointer;
  text-align: center;
  transition: all 0.2s;
  letter-spacing: 0.5px;
  box-shadow: 0 6px 20px rgba(249,115,22,0.35);
}

.ct-05__checkout:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(249,115,22,0.5);
}

@media (prefers-reduced-motion: reduce) {
  .ct-05 tbody tr,
    .ct-05__thumb,
    .ct-05__checkout {
    transition: none;
    animation: none;
  }
}
```

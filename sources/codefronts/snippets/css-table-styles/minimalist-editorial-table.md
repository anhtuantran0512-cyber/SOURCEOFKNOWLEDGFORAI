---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/minimalist-editorial-table/"
title: "Minimalist Editorial Table"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A magazine-style book review index built with serif typography, borderless rows, a single bold rule separating header from body, and a CSS arrow that slides…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Editorial Table
Source: https://codefronts.com/snippets/css-table-styles/minimalist-editorial-table/

A magazine-style book review index built with serif typography, borderless rows, a single bold rule separating header from body, and a CSS arrow that slides in on row hover.
## HTML
```html
<div class="ct-08">
  <div class="ct-08__masthead">
    <div class="ct-08__journal">The Marginalia Review</div>
    <div class="ct-08__issue">Issue No. 48<br>Summer Quarter, 2025</div>
  </div>
  <div class="ct-08__dateline">Literature · Art · Culture · Ideas</div>
  <div class="ct-08__section-title">Notable Works of the Season</div>
  <div class="ct-08__deck">An editorial index of the quarter's most significant titles, curated by our panel of contributing critics and independent reviewers.</div>
  <table>
    <thead>
      <tr>
        <th>Title &amp; Author</th>
        <th>Genre</th>
        <th>Pages</th>
        <th>Published</th>
        <th>Rating</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <div class="ct-08__work-title">The Architecture of Forgetting</div>
          <div class="ct-08__author">Miriam Osei-Bonsu</div>
        </td>
        <td><div class="ct-08__genre">Literary<br>Fiction</div></td>
        <td style="font-variant-numeric:tabular-nums;font-size:13px">384</td>
        <td style="font-size:13px;color:var(--muted)">Mar 2025</td>
        <td>
          <div class="ct-08__score">9.2</div>
          <div class="ct-08__stars">★★★★★</div>
        </td>
      </tr>
      <tr>
        <td>
          <div class="ct-08__work-title">Meridian</div>
          <div class="ct-08__author">Takeshi Murakami-White</div>
        </td>
        <td><div class="ct-08__genre">Essay<br>Collection</div></td>
        <td style="font-variant-numeric:tabular-nums;font-size:13px">228</td>
        <td style="font-size:13px;color:var(--muted)">Jan 2025</td>
        <td>
          <div class="ct-08__score">8.7</div>
          <div class="ct-08__stars">★★★★½</div>
        </td>
      </tr>
      <tr>
        <td>
          <div class="ct-08__work-title">Salt Coast Elegy</div>
          <div class="ct-08__author">Priya Venkatesh</div>
        </td>
        <td><div class="ct-08__genre">Poetry</div></td>
        <td style="font-variant-numeric:tabular-nums;font-size:13px">112</td>
        <td style="font-size:13px;color:var(--muted)">Feb 2025</td>
        <td>
          <div class="ct-08__score">9.5</div>
          <div class="ct-08__stars">★★★★★</div>
        </td>
      </tr>
      <tr>
        <td>
          <div class="ct-08__work-title">Cartographies of the Unseen</div>
          <div class="ct-08__author">Elara J. Hoffmann</div>
        </td>
        <td><div class="ct-08__genre">Narrative<br>Non-fiction</div></td>
        <td style="font-variant-numeric:tabular-nums;font-size:13px">471</td>
        <td style="font-size:13px;color:var(--muted)">Apr 2025</td>
        <td>
          <div class="ct-08__score">8.1</div>
          <div class="ct-08__stars">★★★★</div>
        </td>
      </tr>
      <tr>
        <td>
          <div class="ct-08__work-title">A Brief History of Thresholds</div>
          <div class="ct-08__author">Tobias Lund</div>
        </td>
        <td><div class="ct-08__genre">Autofiction</div></td>
        <td style="font-variant-numeric:tabular-nums;font-size:13px">296</td>
        <td style="font-size:13px;color:var(--muted)">May 2025</td>
        <td>
          <div class="ct-08__score">7.9</div>
          <div class="ct-08__stars">★★★★</div>
        </td>
      </tr>
    </tbody>
  </table>
  <div class="ct-08__footer">
    <span>Ratings out of 10 · Panel consensus</span>
    <span>© The Marginalia Review, 2025</span>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

.ct-08,
.ct-08 *,
.ct-08 *::before,
.ct-08 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-08 ::selection {
  background: #1a1a1a;
  color: #fff;
}

.ct-08 {
  --bg: #fdf8f3;
  --text: #1a1a1a;
  --muted: #8a8a8a;
  --border: #1a1a1a;
  --border-light: #e8e0d6;
  --accent: #b5472a;
  font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  padding: 48px 40px;
  min-height: 100vh;
  color: var(--text);
}

.ct-08__masthead {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 6px;
  padding-bottom: 12px;
  border-bottom: 3px solid var(--border);
}

.ct-08__journal {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -1px;
}

.ct-08__issue {
  text-align: right;
  font-size: 11px;
  color: var(--muted);
  line-height: 1.6;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.ct-08__dateline {
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 32px;
  margin-top: 4px;
}

.ct-08__section-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 20px;
  font-style: italic;
  margin-bottom: 4px;
}

.ct-08__deck {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 28px;
  line-height: 1.6;
}

.ct-08 table {
  width: 100%;
  border-collapse: collapse;
}

.ct-08 thead th {
  padding: 10px 0 10px 0;
  text-align: left;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--muted);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}

.ct-08 thead th:not(:first-child) {
  padding-left: 20px;
}

.ct-08 thead th:last-child {
  text-align: right;
}

.ct-08 tbody tr {
  border-bottom: 1px solid var(--border-light);
}

.ct-08 tbody tr:last-child {
  border-bottom: 1px solid var(--border);
}

.ct-08 tbody tr:hover td:first-child::before {
  content: '→';
  position: absolute;
  left: -18px;
  color: var(--accent);
  font-weight: 700;
  animation: ct-08-arrowin 0.2s ease-out;
}

@keyframes ct-08-arrowin {
  from {
    opacity: 0;
    transform: translateX(-6px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.ct-08 tbody td {
  padding: 16px 0;
  font-size: 14px;
  vertical-align: top;
  line-height: 1.5;
}

.ct-08 tbody td:first-child {
  position: relative;
  padding-left: 0;
}

.ct-08 tbody td:not(:first-child) {
  padding-left: 20px;
}

.ct-08 tbody td:last-child {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

.ct-08__work-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 14px;
  font-style: italic;
  font-weight: 400;
  color: var(--text);
  margin-bottom: 2px;
}

.ct-08__author {
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 0.5px;
}

.ct-08__genre {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--muted);
}

.ct-08__stars {
  color: var(--accent);
  font-size: 12px;
  letter-spacing: -1px;
}

.ct-08__score {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
}

.ct-08__score-sub {
  font-size: 11px;
  color: var(--muted);
}

.ct-08__footer {
  margin-top: 28px;
  padding-top: 12px;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 1px;
  text-transform: uppercase;
}

@media (prefers-reduced-motion: reduce) {
  .ct-08 tbody tr:hover td:first-child::before {
    animation: none;
  }
}
```

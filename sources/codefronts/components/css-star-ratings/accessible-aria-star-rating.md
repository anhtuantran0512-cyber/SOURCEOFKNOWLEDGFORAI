---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/accessible-aria-star-rating/"
title: "Accessible ARIA Star Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A WCAG 2.1 AA-compliant rating widget with visible :focus-visible rings, semantic fieldset/legend markup, and a JS-updated ARIA live region that announces…"
has_js: "true"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible ARIA Star Rating
Source: https://codefronts.com/components/css-star-ratings/accessible-aria-star-rating/

A WCAG 2.1 AA-compliant rating widget with visible :focus-visible rings, semantic fieldset/legend markup, and a JS-updated ARIA live region that announces selections to screen readers.
## HTML
```html
<div class="sr-05">
  <div class="sr-05__card">
    <div class="sr-05__a11y-badge">♿ WCAG 2.1 AA</div>
    <div class="sr-05__title">Accessibility-First Rating</div>
    <div class="sr-05__desc">Fully keyboard navigable. Focus indicators visible. Screen reader announces your selection via an ARIA live region.</div>

    <fieldset class="sr-05__fieldset" aria-label="Star rating from 1 to 5">
      <legend class="sr-05__legend">Rate your experience (use Tab + Arrow keys)</legend>
      <div class="sr-05__stars" role="radiogroup">
        <input type="radio" id="sr-05-r5" name="sr-05-rate" value="5" aria-label="5 out of 5 stars — Excellent">
        <label for="sr-05-r5" title="5 – Excellent">5</label>
        <input type="radio" id="sr-05-r4" name="sr-05-rate" value="4" aria-label="4 out of 5 stars — Very Good">
        <label for="sr-05-r4" title="4 – Very Good">4</label>
        <input type="radio" id="sr-05-r3" name="sr-05-rate" value="3" aria-label="3 out of 5 stars — Good">
        <label for="sr-05-r3" title="3 – Good">3</label>
        <input type="radio" id="sr-05-r2" name="sr-05-rate" value="2" aria-label="2 out of 5 stars — Fair">
        <label for="sr-05-r2" title="2 – Fair">2</label>
        <input type="radio" id="sr-05-r1" name="sr-05-rate" value="1" aria-label="1 out of 5 stars — Poor">
        <label for="sr-05-r1" title="1 – Poor">1</label>
      </div>
    </fieldset>

    <!-- ARIA live region (screen reader only) -->
    <div aria-live="polite" aria-atomic="true" class="sr-05__sr-only" id="sr-05-live"></div>

    <div class="sr-05__status" role="status">
      <div class="sr-05__status-icon">⭐</div>
      <div class="sr-05__status-text">
        <span class="sr-05__default">Click a star or use arrow keys to rate</span>
        <span class="sr-05__r1"><em>Rated 1 out of 5 stars</em> — Poor</span>
        <span class="sr-05__r2"><em>Rated 2 out of 5 stars</em> — Fair</span>
        <span class="sr-05__r3"><em>Rated 3 out of 5 stars</em> — Good</span>
        <span class="sr-05__r4"><em>Rated 4 out of 5 stars</em> — Very Good</span>
        <span class="sr-05__r5"><em>Rated 5 out of 5 stars</em> — Excellent!</span>
      </div>
    </div>

    <div class="sr-05__keyboard-hint">
      <span class="sr-05__key">Tab</span> to focus
      <span class="sr-05__key">←</span><span class="sr-05__key">→</span> to change
    </div>
  </div>
</div>
```
## CSS
```css
.sr-05,
.sr-05 *,
.sr-05 *::before,
.sr-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-05 ::selection {
  background: #7c3aed;
  color: #fff;
}

.sr-05 {
  --violet: #7c3aed;
  --violet-light: #a78bfa;
  --violet-ring: rgba(124,58,237,0.4);
  --bg: #faf5ff;
  --bg-card: #fff;
  --text: #1e1b4b;
  --text-muted: #6b7280;
  --border: #e5e7eb;
  --focus-ring: #7c3aed;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-05__card {
  background: var(--bg-card);
  border-radius: 20px;
  border: 1px solid var(--border);
  padding: 36px 40px 32px;
  max-width: 440px;
  width: 100%;
  box-shadow: 0 4px 24px rgba(124,58,237,0.08);
}

.sr-05__a11y-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(124,58,237,0.1);
  color: var(--violet);
  border-radius: 8px;
  padding: 5px 12px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.4px;
  margin-bottom: 20px;
}

.sr-05__title {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 6px;
}

.sr-05__desc {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 28px;
  line-height: 1.5;
}
/* Fieldset removes default browser chrome */

.sr-05__fieldset {
  border: none;
  padding: 0;
}

.sr-05__legend {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 14px;
  display: block;
  width: 100%;
}

.sr-05__stars {
  display: flex;
  flex-direction: row-reverse;
  justify-content: flex-end;
  gap: 6px;
  margin-bottom: 20px;
}

.sr-05__stars input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-05__stars label {
  cursor: pointer;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), background 0.2s;
  /* Hide the digit text content of the label — the star shape is
       drawn by the ::before pseudo-element, and the radio's
       aria-label="N out of 5 stars" already provides the value to
       screen readers, so the visible digit is redundant. */
  font-size: 0;
}

.sr-05__stars label::before {
  content: '';
  width: 40px;
  height: 40px;
  display: block;
  background: #ddd6fe;
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  transition: background 0.2s ease, filter 0.2s ease;
}
/* Focus-visible ring on the LABEL when radio is focused */

.sr-05__stars input[type="radio"]:focus-visible + label {
  outline: 3px solid var(--focus-ring);
  outline-offset: 3px;
  background: rgba(124,58,237,0.08);
}
/* Hover fill cascade */

.sr-05__stars label:hover::before,
.sr-05__stars label:hover ~ label::before {
  background: var(--violet-light);
  filter: drop-shadow(0 0 6px var(--violet-ring));
}
/* Checked fill cascade */

.sr-05__stars input:checked ~ label::before {
  background: var(--violet);
  filter: drop-shadow(0 0 8px var(--violet-ring));
}

.sr-05__stars input:checked + label::before {
  filter: drop-shadow(0 0 12px rgba(124,58,237,0.6));
  transform: scale(1.1);
}

.sr-05__stars label:hover {
  transform: scale(1.1);
}
/* Visually hidden live region */

.sr-05__sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}
/* Visible confirmation panel */

.sr-05__status {
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(124,58,237,0.06);
  border: 1px solid rgba(124,58,237,0.2);
  border-radius: 12px;
  padding: 14px 16px;
  margin-bottom: 20px;
  min-height: 60px;
  transition: border-color 0.2s;
}

.sr-05__status-icon {
  font-size: 24px;
}

.sr-05__status-text {
  font-size: 0.88rem;
  color: var(--text);
  font-weight: 500;
}

.sr-05__status-text em {
  font-style: normal;
  font-weight: 700;
  color: var(--violet);
}
/* Show status based on checked state */

.sr-05__status-text .sr-05__default {
  display: block;
}

.sr-05__status-text .sr-05__r1,
.sr-05__status-text .sr-05__r2,
.sr-05__status-text .sr-05__r3,
.sr-05__status-text .sr-05__r4,
.sr-05__status-text .sr-05__r5 {
  display: none;
}

.sr-05__fieldset:has(#sr-05-r1:checked) ~ .sr-05__status .sr-05__default {
  display: none;
}

.sr-05__fieldset:has(#sr-05-r1:checked) ~ .sr-05__status .sr-05__r1 {
  display: block;
}

.sr-05__fieldset:has(#sr-05-r2:checked) ~ .sr-05__status .sr-05__default {
  display: none;
}

.sr-05__fieldset:has(#sr-05-r2:checked) ~ .sr-05__status .sr-05__r2 {
  display: block;
}

.sr-05__fieldset:has(#sr-05-r3:checked) ~ .sr-05__status .sr-05__default {
  display: none;
}

.sr-05__fieldset:has(#sr-05-r3:checked) ~ .sr-05__status .sr-05__r3 {
  display: block;
}

.sr-05__fieldset:has(#sr-05-r4:checked) ~ .sr-05__status .sr-05__default {
  display: none;
}

.sr-05__fieldset:has(#sr-05-r4:checked) ~ .sr-05__status .sr-05__r4 {
  display: block;
}

.sr-05__fieldset:has(#sr-05-r5:checked) ~ .sr-05__status .sr-05__default {
  display: none;
}

.sr-05__fieldset:has(#sr-05-r5:checked) ~ .sr-05__status .sr-05__r5 {
  display: block;
}

.sr-05__keyboard-hint {
  font-size: 0.75rem;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 8px;
}

.sr-05__key {
  display: inline-flex;
  background: #f3f4f6;
  border: 1px solid #d1d5db;
  border-bottom: 2px solid #9ca3af;
  border-radius: 5px;
  padding: 2px 7px;
  font-size: 0.72rem;
  font-family: monospace;
  color: #374151;
}

@media (prefers-reduced-motion: reduce) {
  .sr-05__stars label,
    .sr-05__stars label::before,
    .sr-05__status {
    transition: none;
  }
}
```

## JavaScript
```js
// Update ARIA live region on change — degrades gracefully without JS
const live = document.getElementById('sr-05-live');
const labels = ['Poor','Fair','Good','Very Good','Excellent'];
document.querySelectorAll('input[name="sr-05-rate"]').forEach(r => {
  r.addEventListener('change', () => {
    if (live) live.textContent = `Rated ${r.value} out of 5 stars — ${labels[r.value - 1]}`;
  });
});
```

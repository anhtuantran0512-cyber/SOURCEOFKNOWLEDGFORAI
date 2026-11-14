---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/emoji-feedback-reaction-scale/"
title: "Emoji Feedback Reaction Scale"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A dark-mode NPS survey widget with five emoji reactions — angry to ecstatic — using CSS filter grayscale for inactive states that vivid-color on hover or…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Emoji Feedback Reaction Scale
Source: https://codefronts.com/components/css-star-ratings/emoji-feedback-reaction-scale/

A dark-mode NPS survey widget with five emoji reactions — angry to ecstatic — using CSS filter grayscale for inactive states that vivid-color on hover or selection via :has().
## HTML
```html
<div class="sr-07">
  <div class="sr-07__card">
    <div class="sr-07__brand">
      <div class="sr-07__brand-dot"></div>
      <span class="sr-07__brand-name">QuickPulse Survey</span>
    </div>
    <div class="sr-07__title">How was your delivery? 📦</div>
    <div class="sr-07__sub">Your feedback takes 2 seconds and helps us improve.</div>

    <form class="sr-07__form">
      <div class="sr-07__reactions">
        <input type="radio" id="sr-07-e1" name="sr-07-feel" value="1">
        <div class="sr-07__reaction-item">
          <label for="sr-07-e1">😡</label>
          <span class="sr-07__rlabel">Terrible</span>
        </div>

        <input type="radio" id="sr-07-e2" name="sr-07-feel" value="2">
        <div class="sr-07__reaction-item">
          <label for="sr-07-e2">😕</label>
          <span class="sr-07__rlabel">Poor</span>
        </div>

        <input type="radio" id="sr-07-e3" name="sr-07-feel" value="3">
        <div class="sr-07__reaction-item">
          <label for="sr-07-e3">😐</label>
          <span class="sr-07__rlabel">Okay</span>
        </div>

        <input type="radio" id="sr-07-e4" name="sr-07-feel" value="4">
        <div class="sr-07__reaction-item">
          <label for="sr-07-e4">😊</label>
          <span class="sr-07__rlabel">Good</span>
        </div>

        <input type="radio" id="sr-07-e5" name="sr-07-feel" value="5">
        <div class="sr-07__reaction-item">
          <label for="sr-07-e5">🤩</label>
          <span class="sr-07__rlabel">Amazing!</span>
        </div>
      </div>

      <div class="sr-07__response">
        <span class="sr-07__resp-default">Select your reaction above</span>
        <span class="sr-07__resp-1">😡 We're sorry to hear that. We'll make it right.</span>
        <span class="sr-07__resp-2">😕 Thanks for letting us know. We'll improve.</span>
        <span class="sr-07__resp-3">😐 Noted! We're always working to do better.</span>
        <span class="sr-07__resp-4">😊 Glad it went well! Thanks for your time.</span>
        <span class="sr-07__resp-5">🤩 Awesome! You made our day. Thank you!</span>
      </div>
    </form>

    <div class="sr-07__footer-text">Anonymous · No account needed</div>
  </div>
</div>
```
## CSS
```css
.sr-07,
.sr-07 *,
.sr-07 *::before,
.sr-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-07 ::selection {
  background: #f97316;
  color: #fff;
}

.sr-07 {
  --bg-page: #0f172a;
  --bg-card: #1e293b;
  --bg-track: #334155;
  --text: #f1f5f9;
  --text-muted: #94a3b8;
  --border: #334155;
  --c1: #ef4444;
  --c2: #f97316;
  --c3: #eab308;
  --c4: #22c55e;
  --c5: #06b6d4;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-page);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-07__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 36px 40px 32px;
  max-width: 460px;
  width: 100%;
  text-align: center;
  box-shadow: 0 24px 64px rgba(0,0,0,0.5);
}

.sr-07__brand {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 20px;
}

.sr-07__brand-dot {
  width: 10px;
  height: 10px;
  background: linear-gradient(135deg, #f97316, #ef4444);
  border-radius: 50%;
}

.sr-07__brand-name {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1.5px;
}

.sr-07__title {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 6px;
}

.sr-07__sub {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 32px;
}
/* Emoji reaction buttons */

.sr-07__reactions {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-bottom: 28px;
}

.sr-07__reactions input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-07__reaction-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.sr-07__reactions label {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 64px;
  height: 64px;
  border-radius: 20px;
  background: var(--bg-track);
  cursor: pointer;
  font-size: 32px;
  /* Start greyed out */
  filter: grayscale(1) opacity(0.45);
  transition: filter 0.25s ease, transform 0.25s cubic-bezier(.34,1.56,.64,1), background 0.25s ease, box-shadow 0.25s ease;
}

.sr-07__rlabel {
  font-size: 0.7rem;
  color: var(--text-muted);
  font-weight: 600;
  transition: color 0.2s;
}
/* Hover: full color + lift */

.sr-07__reactions label:hover {
  filter: grayscale(0) opacity(1);
  transform: scale(1.18) translateY(-4px);
}
/* Each emoji gets its own glow color */

.sr-07__reactions:has(#sr-07-e1 + .sr-07__reaction-item label:hover) label,
.sr-07__reaction-item:has(label:hover) label {
  filter: grayscale(0) opacity(1);
}
/* Checked states: full color + shadow glow */

#sr-07-e1:checked + .sr-07__reaction-item label {
  filter: grayscale(0) opacity(1);
  background: rgba(239,68,68,0.2);
  box-shadow: 0 0 0 2px var(--c1), 0 8px 24px rgba(239,68,68,0.35);
  transform: scale(1.12) translateY(-3px);
}

#sr-07-e2:checked + .sr-07__reaction-item label {
  filter: grayscale(0) opacity(1);
  background: rgba(249,115,22,0.2);
  box-shadow: 0 0 0 2px var(--c2), 0 8px 24px rgba(249,115,22,0.35);
  transform: scale(1.12) translateY(-3px);
}

#sr-07-e3:checked + .sr-07__reaction-item label {
  filter: grayscale(0) opacity(1);
  background: rgba(234,179,8,0.2);
  box-shadow: 0 0 0 2px var(--c3), 0 8px 24px rgba(234,179,8,0.35);
  transform: scale(1.12) translateY(-3px);
}

#sr-07-e4:checked + .sr-07__reaction-item label {
  filter: grayscale(0) opacity(1);
  background: rgba(34,197,94,0.2);
  box-shadow: 0 0 0 2px var(--c4), 0 8px 24px rgba(34,197,94,0.35);
  transform: scale(1.12) translateY(-3px);
}

#sr-07-e5:checked + .sr-07__reaction-item label {
  filter: grayscale(0) opacity(1);
  background: rgba(6,182,212,0.2);
  box-shadow: 0 0 0 2px var(--c5), 0 8px 24px rgba(6,182,212,0.35);
  transform: scale(1.12) translateY(-3px);
}
/* Checked labels color */

#sr-07-e1:checked + .sr-07__reaction-item .sr-07__rlabel {
  color: var(--c1);
}

#sr-07-e2:checked + .sr-07__reaction-item .sr-07__rlabel {
  color: var(--c2);
}

#sr-07-e3:checked + .sr-07__reaction-item .sr-07__rlabel {
  color: var(--c3);
}

#sr-07-e4:checked + .sr-07__reaction-item .sr-07__rlabel {
  color: var(--c4);
}

#sr-07-e5:checked + .sr-07__reaction-item .sr-07__rlabel {
  color: var(--c5);
}
/* Dim others when one checked */

.sr-07__form:has(input:checked) .sr-07__reaction-item:not(:has(input:checked)) label {
  filter: grayscale(1) opacity(0.3);
}
/* Response display */

.sr-07__response {
  background: var(--bg-track);
  border-radius: 14px;
  padding: 16px 20px;
  margin-bottom: 20px;
  min-height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.88rem;
  color: var(--text-muted);
  transition: background 0.25s;
}

.sr-07__form:has(#sr-07-e1:checked) .sr-07__response {
  background: rgba(239,68,68,0.1);
  color: var(--c1);
}

.sr-07__form:has(#sr-07-e2:checked) .sr-07__response {
  background: rgba(249,115,22,0.1);
  color: var(--c2);
}

.sr-07__form:has(#sr-07-e3:checked) .sr-07__response {
  background: rgba(234,179,8,0.1);
  color: var(--c3);
}

.sr-07__form:has(#sr-07-e4:checked) .sr-07__response {
  background: rgba(34,197,94,0.1);
  color: var(--c4);
}

.sr-07__form:has(#sr-07-e5:checked) .sr-07__response {
  background: rgba(6,182,212,0.1);
  color: var(--c5);
}

.sr-07__resp-default {
  display: block;
  font-weight: 500;
}

.sr-07__resp-1,
.sr-07__resp-2,
.sr-07__resp-3,
.sr-07__resp-4,
.sr-07__resp-5 {
  display: none;
  font-weight: 700;
}

.sr-07__form:has(#sr-07-e1:checked) .sr-07__resp-default,
.sr-07__form:has(#sr-07-e2:checked) .sr-07__resp-default,
.sr-07__form:has(#sr-07-e3:checked) .sr-07__resp-default,
.sr-07__form:has(#sr-07-e4:checked) .sr-07__resp-default,
.sr-07__form:has(#sr-07-e5:checked) .sr-07__resp-default {
  display: none;
}

.sr-07__form:has(#sr-07-e1:checked) .sr-07__resp-1 {
  display: block;
}

.sr-07__form:has(#sr-07-e2:checked) .sr-07__resp-2 {
  display: block;
}

.sr-07__form:has(#sr-07-e3:checked) .sr-07__resp-3 {
  display: block;
}

.sr-07__form:has(#sr-07-e4:checked) .sr-07__resp-4 {
  display: block;
}

.sr-07__form:has(#sr-07-e5:checked) .sr-07__resp-5 {
  display: block;
}

.sr-07__footer-text {
  font-size: 0.75rem;
  color: var(--text-muted);
}

@media (prefers-reduced-motion: reduce) {
  .sr-07__reactions label {
    transition: filter 0.1s;
  }
}
```

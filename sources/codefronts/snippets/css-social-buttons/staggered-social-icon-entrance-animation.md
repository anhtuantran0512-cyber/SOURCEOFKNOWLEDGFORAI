---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/staggered-social-icon-entrance-animation/"
title: "Staggered Social Icon Entrance Animation"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "Six marks rise and fade in sequence on load, each one offset by a per-child animation-delay."
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Staggered Social Icon Entrance Animation
Source: https://codefronts.com/snippets/css-social-buttons/staggered-social-icon-entrance-animation/

Six marks rise and fade in sequence on load, each one offset by a per-child animation-delay. A checkbox lets you replay the sequence with no JavaScript by swapping to a second identical keyframe set. The reduced-motion block does the thing most builds get wrong: it removes the motion and pins the icons at full opacity instead of leaving them stuck invisible.
## HTML
```html
<div class="soc-05">
  <div class="soc-05__stage">
    <div class="soc-05__card">
      <p class="soc-05__eyebrow">On load</p>
      <h2 class="soc-05__title">Six marks, sixty milliseconds apart</h2>
      <ul class="soc-05__row">
        <li class="soc-05__item"><a class="soc-05__btn" style="--brand:#0f1419" href="https://example.com/jordanlee" target="_blank" rel="noopener" aria-label="Jordan Lee on X">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg></a></li>
        <li class="soc-05__item"><a class="soc-05__btn" style="--brand:#0a66c2" href="https://example.com/in/jordanlee" target="_blank" rel="noopener" aria-label="Jordan Lee on LinkedIn">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg></a></li>
        <li class="soc-05__item"><a class="soc-05__btn" style="--brand:#6f42c1" href="https://example.com/jordanlee" target="_blank" rel="noopener" aria-label="Jordan Lee on GitHub">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.6"/><path d="m9.8 9.4-2.3 2.6 2.3 2.6"/><path d="m14.2 9.4 2.3 2.6-2.3 2.6"/></svg></a></li>
        <li class="soc-05__item"><a class="soc-05__btn" style="--brand:#e1306c" href="https://example.com/jordanlee" target="_blank" rel="noopener" aria-label="Jordan Lee on Instagram">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/><circle cx="12" cy="12" r="3.9"/><circle cx="17.1" cy="6.9" r="1.15" fill="currentColor" stroke="none"/></svg></a></li>
        <li class="soc-05__item"><a class="soc-05__btn" style="--brand:#ff0033" href="https://example.com/@jordanlee" target="_blank" rel="noopener" aria-label="Jordan Lee on YouTube">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="2.6" y="5.2" width="18.8" height="13.6" rx="4.4"/><path d="m10.4 9.4 5 2.6-5 2.6Z" fill="currentColor"/></svg></a></li>
        <li class="soc-05__item"><a class="soc-05__btn" style="--brand:#00b894" href="https://example.com/rss" target="_blank" rel="noopener" aria-label="Subscribe to the RSS feed">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M6 17.6h.01"/><path d="M6 12.4a5.6 5.6 0 0 1 5.6 5.6"/><path d="M6 7.2a10.8 10.8 0 0 1 10.8 10.8"/></svg></a></li>
      </ul>
      <label class="soc-05__replay">
        <input class="soc-05__toggle" type="checkbox">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 11.5A8 8 0 1 1 17.2 6"/><path d="M20.5 4v4.2h-4.2"/></svg>
        <span>Replay the sequence</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-05 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --size: 2.875rem;
  --step: 70ms;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .soc-05 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-05:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
  }
}

.soc-05[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
}

.soc-05,
.soc-05 *,
.soc-05 *::before,
.soc-05 *::after {
  box-sizing: border-box;
}

.soc-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-05__card {
  inline-size: min(34rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-05__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-05__title {
  margin: 0 0 1.6rem;
  font-size: clamp(1.05rem,1rem + .8vw,1.3rem);
  font-weight: 600;
  line-height: 1.35;
  letter-spacing: -.02em;
}

.soc-05__row {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  margin: 0 0 1.5rem;
  padding: 0;
  list-style: none;
}

@keyframes soc-05-rise {
  from {
    opacity: 0;
    translate: 0 14px;
    scale: .94;
  }

  to {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }
}

@keyframes soc-05-rise-b {
  from {
    opacity: 0;
    translate: 0 14px;
    scale: .94;
  }

  to {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }
}

.soc-05__item {
  animation: soc-05-rise .55s cubic-bezier(.16,1,.3,1) both var(--d,0ms);
}

.soc-05__item:nth-child(1) {
  --d: 0ms;
}

.soc-05__item:nth-child(2) {
  --d: calc(var(--step) * 1);
}

.soc-05__item:nth-child(3) {
  --d: calc(var(--step) * 2);
}

.soc-05__item:nth-child(4) {
  --d: calc(var(--step) * 3);
}

.soc-05__item:nth-child(5) {
  --d: calc(var(--step) * 4);
}

.soc-05__item:nth-child(6) {
  --d: calc(var(--step) * 5);
}

.soc-05:has(.soc-05__toggle:checked) .soc-05__item {
  animation-name: soc-05-rise-b;
}

.soc-05__btn {
  display: grid;
  place-items: center;
  inline-size: var(--size);
  block-size: var(--size);
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--surface);
  color: var(--muted);
  text-decoration: none;
  -webkit-tap-highlight-color: transparent;
  transition: color .2s ease, background-color .2s ease, border-color .2s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.soc-05__btn svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.soc-05__btn:hover {
  color: var(--brand);
  translate: 0 -2px;
  border-color: color-mix(in oklab,var(--brand) 45%,var(--line));
  background: color-mix(in oklab,var(--brand) 10%,var(--surface));
}

.soc-05__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
  color: var(--brand);
}

.soc-05__replay {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 2.75rem;
  padding: 0 1rem;
  border: 1px solid var(--line);
  border-radius: .8rem;
  background: var(--surface);
  font-size: .85rem;
  font-weight: 550;
  color: var(--fg);
  cursor: pointer;
  user-select: none;
  transition: border-color .2s ease, background-color .2s ease;
}

.soc-05__replay:hover {
  border-color: color-mix(in oklab,var(--fg) 25%,var(--line));
}

.soc-05__replay svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  color: var(--muted);
}

.soc-05__toggle {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.soc-05__replay:has(.soc-05__toggle:focus-visible) {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .soc-05__item {
    animation: none;
    opacity: 1;
    translate: none;
    scale: 1;
  }

  .soc-05:has(.soc-05__toggle:checked) .soc-05__item {
    animation: none;
    opacity: 1;
  }

  .soc-05__btn {
    transition-duration: 1ms;
  }

  .soc-05__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-05__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
  }
}
```

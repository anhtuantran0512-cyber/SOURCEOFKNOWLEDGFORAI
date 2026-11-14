---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/inline-svg-social-icon-bar-no-icon-fonts/"
title: "Inline SVG Social Icon Bar No Icon Fonts"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "The reference build the rest of this collection reuses: six hand-drawn inline SVG marks in a horizontal bar, each carrying its own brand colour as a custom…"
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline SVG Social Icon Bar No Icon Fonts
Source: https://codefronts.com/snippets/css-social-buttons/inline-svg-social-icon-bar-no-icon-fonts/

The reference build the rest of this collection reuses: six hand-drawn inline SVG marks in a horizontal bar, each carrying its own brand colour as a custom property on the anchor so one shared rule styles all six. No icon font, no sprite sheet, no network request — the icons ship inside the markup and inherit colour through currentColor. Hover lifts the mark and tints its surface.
## HTML
```html
<div class="soc-01">
  <div class="soc-01__stage">
    <div class="soc-01__card">
      <p class="soc-01__eyebrow">Follow along</p>
      <h2 class="soc-01__title">Alex Chen ships design engineering notes every Tuesday.</h2>
      <ul class="soc-01__bar">
        <li><a class="soc-01__btn" style="--brand:#0f1419" href="https://example.com/alexchen" target="_blank" rel="noopener" aria-label="Follow Alex Chen on X">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg>
        </a></li>
        <li><a class="soc-01__btn" style="--brand:#0a66c2" href="https://example.com/in/alexchen" target="_blank" rel="noopener" aria-label="Connect with Alex Chen on LinkedIn">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg>
        </a></li>
        <li><a class="soc-01__btn" style="--brand:#6f42c1" href="https://example.com/alexchen" target="_blank" rel="noopener" aria-label="View Alex Chen on GitHub">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.6"/><path d="m9.8 9.4-2.3 2.6 2.3 2.6"/><path d="m14.2 9.4 2.3 2.6-2.3 2.6"/></svg>
        </a></li>
        <li><a class="soc-01__btn" style="--brand:#e1306c" href="https://example.com/alexchen" target="_blank" rel="noopener" aria-label="Follow Alex Chen on Instagram">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/><circle cx="12" cy="12" r="3.9"/><circle cx="17.1" cy="6.9" r="1.15" fill="currentColor" stroke="none"/></svg>
        </a></li>
        <li><a class="soc-01__btn" style="--brand:#ff0033" href="https://example.com/@alexchen" target="_blank" rel="noopener" aria-label="Subscribe to Alex Chen on YouTube">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="2.6" y="5.2" width="18.8" height="13.6" rx="4.4"/><path d="m10.4 9.4 5 2.6-5 2.6Z" fill="currentColor"/></svg>
        </a></li>
        <li><a class="soc-01__btn" style="--brand:#6364ff" href="https://example.com/@alexchen" target="_blank" rel="noopener" aria-label="Follow Alex Chen on Mastodon">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16V10a3.2 3.2 0 0 1 6-1.5 3.2 3.2 0 0 1 6 1.5v6"/><path d="M4.5 16.5c1.6 2.4 12 2.7 15 .2"/></svg>
        </a></li>
      </ul>
      <p class="soc-01__note">Six marks · zero external requests</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-01 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --radius: 1.25rem;
  --size: 2.875rem;
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
  .soc-01 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-01:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
  }
}

.soc-01[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
}

.soc-01,
.soc-01 *,
.soc-01 *::before,
.soc-01 *::after {
  box-sizing: border-box;
}

.soc-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-01__card {
  inline-size: min(34rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-01__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-01__title {
  margin: 0 0 1.5rem;
  font-size: clamp(1.05rem,1rem + .8vw,1.35rem);
  font-weight: 600;
  line-height: 1.35;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.soc-01__bar {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.soc-01__btn {
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
  transition: translate .22s cubic-bezier(.16,1,.3,1), color .22s ease, background-color .22s ease, border-color .22s ease, box-shadow .22s ease;
}

.soc-01__btn svg {
  inline-size: 1.3rem;
  block-size: 1.3rem;
  transition: scale .22s cubic-bezier(.16,1,.3,1);
}

.soc-01__btn:hover {
  color: var(--brand);
  translate: 0 -3px;
  border-color: color-mix(in oklab,var(--brand) 40%,var(--line));
  background: color-mix(in oklab,var(--brand) 9%,var(--surface));
  box-shadow: 0 10px 22px -14px color-mix(in oklab,var(--brand) 80%,transparent);
}

.soc-01__btn:hover svg {
  scale: 1.08;
}

.soc-01__btn:focus-visible {
  outline: 2px solid color-mix(in oklab,var(--brand) 75%,var(--ring));
  outline-offset: 3px;
  color: var(--brand);
}

.soc-01__btn:active {
  translate: 0 -1px;
}

.soc-01__note {
  margin: 1.4rem 0 0;
  font-size: .78rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .soc-01__btn,
    .soc-01__btn svg {
    transition-duration: 1ms;
  }

  .soc-01__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-01__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .soc-01__btn:hover,
    .soc-01__btn:focus-visible {
    color: Highlight;
    border-color: Highlight;
    background: Canvas;
  }
}
```

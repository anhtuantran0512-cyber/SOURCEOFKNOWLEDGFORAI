---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/social-icon-buttons-with-css-tooltips/"
title: "Social Icon Buttons with CSS Tooltips"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "A tooltip that shows the account handle, opens on hover and on keyboard focus, and is genuinely removed from the page at rest rather than sitting invisible…"
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Social Icon Buttons with CSS Tooltips
Source: https://codefronts.com/snippets/css-social-buttons/social-icon-buttons-with-css-tooltips/

A tooltip that shows the account handle, opens on hover and on keyboard focus, and is genuinely removed from the page at rest rather than sitting invisible on top of your layout. Built with display:none plus transition-behavior: allow-discrete and @starting-style, so it animates in both directions without a line of JavaScript.
## HTML
```html
<div class="soc-04">
  <div class="soc-04__stage">
    <div class="soc-04__card">
      <p class="soc-04__eyebrow">Hover or tab</p>
      <h2 class="soc-04__title">Handles on demand, without a tooltip library</h2>
      <ul class="soc-04__row">
        <li class="soc-04__item">
          <a class="soc-04__btn" style="--brand:#0f1419" href="https://example.com/alexchen" target="_blank" rel="noopener" aria-label="Alex Chen on X" aria-describedby="soc-04-t1">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg>
          </a>
          <span class="soc-04__tip" id="soc-04-t1" role="tooltip">@alexchen</span>
        </li>
        <li class="soc-04__item">
          <a class="soc-04__btn" style="--brand:#0a66c2" href="https://example.com/in/alexchen" target="_blank" rel="noopener" aria-label="Alex Chen on LinkedIn" aria-describedby="soc-04-t2">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg>
          </a>
          <span class="soc-04__tip" id="soc-04-t2" role="tooltip">in/alexchen</span>
        </li>
        <li class="soc-04__item">
          <a class="soc-04__btn" style="--brand:#6f42c1" href="https://example.com/alexchen" target="_blank" rel="noopener" aria-label="Alex Chen on GitHub" aria-describedby="soc-04-t3">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.6"/><path d="m9.8 9.4-2.3 2.6 2.3 2.6"/><path d="m14.2 9.4 2.3 2.6-2.3 2.6"/></svg>
          </a>
          <span class="soc-04__tip" id="soc-04-t3" role="tooltip">@alexchen</span>
        </li>
        <li class="soc-04__item">
          <a class="soc-04__btn" style="--brand:#e1306c" href="https://example.com/alexchen" target="_blank" rel="noopener" aria-label="Alex Chen on Instagram" aria-describedby="soc-04-t4">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/><circle cx="12" cy="12" r="3.9"/><circle cx="17.1" cy="6.9" r="1.15" fill="currentColor" stroke="none"/></svg>
          </a>
          <span class="soc-04__tip" id="soc-04-t4" role="tooltip">@alex.builds</span>
        </li>
        <li class="soc-04__item">
          <a class="soc-04__btn" style="--brand:#6364ff" href="https://example.com/@alexchen" target="_blank" rel="noopener" aria-label="Alex Chen on Mastodon" aria-describedby="soc-04-t5">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16V10a3.2 3.2 0 0 1 6-1.5 3.2 3.2 0 0 1 6 1.5v6"/><path d="M4.5 16.5c1.6 2.4 12 2.7 15 .2"/></svg>
          </a>
          <span class="soc-04__tip" id="soc-04-t5" role="tooltip">@[email protected]</span>
        </li>
      </ul>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.soc-04 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --tip-bg: #15151c;
  --tip-fg: #f6f6f8;
  --size: 2.875rem;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
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
  .soc-04 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
    --tip-bg: oklch(21% .015 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-04:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
    --tip-bg: #e9e9ef;
    --tip-fg: #101015;
  }
}

.soc-04[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
  --tip-bg: #e9e9ef;
  --tip-fg: #101015;
}

.soc-04,
.soc-04 *,
.soc-04 *::before,
.soc-04 *::after {
  box-sizing: border-box;
}

.soc-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-04__card {
  inline-size: min(34rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem) clamp(1.5rem,4vw,2.25rem) clamp(1.75rem,4vw,2.5rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-04__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-04__title {
  margin: 0 0 2.6rem;
  font-size: clamp(1.05rem,1rem + .8vw,1.3rem);
  font-weight: 600;
  line-height: 1.35;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.soc-04__row {
  display: flex;
  flex-wrap: wrap;
  gap: .65rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.soc-04__item {
  position: relative;
}

.soc-04__btn {
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

.soc-04__btn svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.soc-04__btn:hover,
.soc-04__btn:focus-visible {
  color: var(--brand);
  translate: 0 -2px;
  border-color: color-mix(in oklab,var(--brand) 45%,var(--line));
  background: color-mix(in oklab,var(--brand) 10%,var(--surface));
}

.soc-04__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-04__tip {
  display: none;
  opacity: 0;
  translate: 0 4px;
  position: absolute;
  bottom: calc(100% + .55rem);
  left: 50%;
  margin-inline-start: -50%;
  inline-size: max-content;
  max-inline-size: 12rem;
  padding: .4rem .6rem;
  border-radius: .55rem;
  background: var(--tip-bg);
  color: var(--tip-fg);
  font-family: var(--mono);
  font-size: .75rem;
  pointer-events: none;
  z-index: 5;
  text-align: center;
  transition: opacity .18s ease, translate .18s cubic-bezier(.16,1,.3,1), display .18s allow-discrete;
}

.soc-04__tip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  margin-inline-start: -.25rem;
  border: .3rem solid transparent;
  border-top-color: var(--tip-bg);
}

.soc-04__btn:hover + .soc-04__tip,
.soc-04__btn:focus-visible + .soc-04__tip {
  display: block;
  opacity: 1;
  translate: 0 0;
}

@starting-style {
  .soc-04__btn:hover + .soc-04__tip,
    .soc-04__btn:focus-visible + .soc-04__tip {
    opacity: 0;
    translate: 0 4px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .soc-04__tip {
    transition: display .01s allow-discrete;
    translate: none;
  }

  .soc-04__btn {
    transition-duration: 1ms;
  }

  .soc-04__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-04__tip {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }

  .soc-04__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
  }
}
```

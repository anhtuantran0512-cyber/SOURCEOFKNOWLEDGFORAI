---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/accessible-circular-social-icon-buttons/"
title: "Accessible Circular Social Icon Buttons"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "Icon-only circles done the way an audit wants them: a visually-hidden label utility built on clip-path, an aria-label on every control, a two-pixel…"
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Circular Social Icon Buttons
Source: https://codefronts.com/snippets/css-social-buttons/accessible-circular-social-icon-buttons/

Icon-only circles done the way an audit wants them: a visually-hidden label utility built on clip-path, an aria-label on every control, a two-pixel focus-visible ring with offset, and a genuine 46px target around a 20px glyph. Focus reveals the hidden label as a caption under the row, so the technique teaches itself while you tab through it.
## HTML
```html
<div class="soc-03">
  <div class="soc-03__stage">
    <div class="soc-03__card">
      <p class="soc-03__eyebrow">Tab through the row</p>
      <h2 class="soc-03__title">Every circle has a hidden label, a real name and a 46px target.</h2>
      <ul class="soc-03__row">
        <li class="soc-03__item"><a class="soc-03__btn" style="--brand:#0f1419" href="https://example.com/priyasharma" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg>
          <span class="soc-03__sr">Priya Sharma on X</span>
        </a></li>
        <li class="soc-03__item"><a class="soc-03__btn" style="--brand:#0a66c2" href="https://example.com/in/priyasharma" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg>
          <span class="soc-03__sr">Priya Sharma on LinkedIn</span>
        </a></li>
        <li class="soc-03__item"><a class="soc-03__btn" style="--brand:#6f42c1" href="https://example.com/priyasharma" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.6"/><path d="m9.8 9.4-2.3 2.6 2.3 2.6"/><path d="m14.2 9.4 2.3 2.6-2.3 2.6"/></svg>
          <span class="soc-03__sr">Priya Sharma on GitHub</span>
        </a></li>
        <li class="soc-03__item"><a class="soc-03__btn" style="--brand:#00b894" href="https://example.com/rss" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M6 17.6h.01"/><path d="M6 12.4a5.6 5.6 0 0 1 5.6 5.6"/><path d="M6 7.2a10.8 10.8 0 0 1 10.8 10.8"/></svg>
          <span class="soc-03__sr">Subscribe to the RSS feed</span>
        </a></li>
        <li class="soc-03__item"><a class="soc-03__btn" style="--brand:#d4453b" href="mailto:[email protected]">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.2" width="18" height="13.6" rx="3.4"/><path d="m4.4 8 6.7 4.7a1.6 1.6 0 0 0 1.8 0L19.6 8"/></svg>
          <span class="soc-03__sr">Email Priya Sharma</span>
        </a></li>
      </ul>
      <p class="soc-03__cap" aria-hidden="true"><span class="soc-03__capText">Focus a button to reveal its label</span></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-03 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
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
  .soc-03 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
    --ring: oklch(56% .19 265);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-03:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
    --ring: #7c9bff;
  }
}

.soc-03[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
  --ring: #7c9bff;
}

.soc-03,
.soc-03 *,
.soc-03 *::before,
.soc-03 *::after {
  box-sizing: border-box;
}

.soc-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-03__card {
  inline-size: min(34rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-03__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-03__title {
  margin: 0 0 1.6rem;
  font-size: clamp(1.05rem,1rem + .8vw,1.3rem);
  font-weight: 600;
  line-height: 1.35;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.soc-03__row {
  display: flex;
  flex-wrap: wrap;
  gap: .65rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.soc-03__sr {
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

.soc-03__btn {
  display: grid;
  place-items: center;
  inline-size: var(--size);
  block-size: var(--size);
  border: 1px solid var(--line);
  border-radius: 50%;
  background: var(--surface);
  color: var(--muted);
  text-decoration: none;
  -webkit-tap-highlight-color: transparent;
  transition: translate .2s cubic-bezier(.16,1,.3,1), color .2s ease, background-color .2s ease, border-color .2s ease;
}

.soc-03__btn svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.soc-03__btn:hover {
  color: var(--brand);
  border-color: color-mix(in oklab,var(--brand) 45%,var(--line));
  background: color-mix(in oklab,var(--brand) 10%,var(--surface));
  translate: 0 -2px;
}

.soc-03__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
  color: var(--brand);
  background: color-mix(in oklab,var(--brand) 12%,var(--surface));
}

.soc-03__cap {
  margin: 1.5rem 0 0;
  min-block-size: 2.25rem;
  display: flex;
  align-items: center;
  padding: .5rem .8rem;
  border-radius: .7rem;
  background: color-mix(in oklab,var(--fg) 4%,var(--surface));
  border: 1px dashed var(--line);
  font-size: .82rem;
  color: var(--muted);
  min-inline-size: 0;
}

.soc-03__capText {
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.soc-03__row:has(.soc-03__btn:focus-visible) + .soc-03__cap {
  color: var(--fg);
  border-style: solid;
}

.soc-03__row:has(.soc-03__item:nth-child(1) .soc-03__btn:focus-visible) + .soc-03__cap .soc-03__capText::after {
  content: "Priya Sharma on X";
}

.soc-03__row:has(.soc-03__item:nth-child(2) .soc-03__btn:focus-visible) + .soc-03__cap .soc-03__capText::after {
  content: "Priya Sharma on LinkedIn";
}

.soc-03__row:has(.soc-03__item:nth-child(3) .soc-03__btn:focus-visible) + .soc-03__cap .soc-03__capText::after {
  content: "Priya Sharma on GitHub";
}

.soc-03__row:has(.soc-03__item:nth-child(4) .soc-03__btn:focus-visible) + .soc-03__cap .soc-03__capText::after {
  content: "Subscribe to the RSS feed";
}

.soc-03__row:has(.soc-03__item:nth-child(5) .soc-03__btn:focus-visible) + .soc-03__cap .soc-03__capText::after {
  content: "Email Priya Sharma";
}

.soc-03__row:has(.soc-03__btn:focus-visible) + .soc-03__cap .soc-03__capText {
  font-size: 0;
}

.soc-03__row:has(.soc-03__btn:focus-visible) + .soc-03__cap .soc-03__capText::after {
  font-size: .82rem;
  font-weight: 550;
}

@media (prefers-reduced-motion: reduce) {
  .soc-03__btn {
    transition-duration: 1ms;
  }

  .soc-03__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-03__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .soc-03__btn:hover,
    .soc-03__btn:focus-visible {
    color: Highlight;
    border-color: Highlight;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/ghost-outline-social-buttons-brand-hover/"
title: "Ghost Outline Social Buttons Brand Hover"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "Border-only buttons in a neutral resting state that fill with the channel's brand colour on hover and on focus."
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ghost Outline Social Buttons Brand Hover
Source: https://codefronts.com/snippets/css-social-buttons/ghost-outline-social-buttons-brand-hover/

Border-only buttons in a neutral resting state that fill with the channel's brand colour on hover and on focus. Border, background and label transition together on one easing so the change reads as a single motion rather than three effects arriving at different times — the restrained option for pages where the social row is not the primary action.
## HTML
```html
<div class="soc-18">
  <div class="soc-18__stage">
    <div class="soc-18__card">
      <p class="soc-18__eyebrow">Elsewhere</p>
      <h2 class="soc-18__title">Quiet until you reach for them</h2>
      <div class="soc-18__row">
        <a class="soc-18__btn" style="--brand:#0f1419;--on-brand:#ffffff" href="https://example.com/jordanlee" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg>
          <span>Follow on X</span>
        </a>
        <a class="soc-18__btn" style="--brand:#0a66c2;--on-brand:#ffffff" href="https://example.com/in/jordanlee" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg>
          <span>Connect</span>
        </a>
        <a class="soc-18__btn" style="--brand:#6f42c1;--on-brand:#ffffff" href="https://example.com/jordanlee" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.6"/><path d="m9.8 9.4-2.3 2.6 2.3 2.6"/><path d="m14.2 9.4 2.3 2.6-2.3 2.6"/></svg>
          <span>Source</span>
        </a>
        <a class="soc-18__btn" style="--brand:#ffd400;--on-brand:#1b1500" href="https://example.com/support" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 5h11l-1 9.2A4 4 0 0 1 12.5 18h-1a4 4 0 0 1-4-3.8Z"/><path d="M17.2 7.4h1.6a2 2 0 0 1 0 4h-1.2"/><path d="M8 21h8"/></svg>
          <span>Buy a coffee</span>
        </a>
        <a class="soc-18__btn" style="--brand:#0e8a55;--on-brand:#ffffff" href="https://example.com/newsletter" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.2" width="18" height="13.6" rx="3.4"/><path d="m4.4 8 6.7 4.7a1.6 1.6 0 0 0 1.8 0L19.6 8"/></svg>
          <span>Newsletter</span>
        </a>
      </div>
      <p class="soc-18__note">Border, fill and label move on one easing — try it with the keyboard too.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-18 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #d8d8e0;
  --ring: #3d63ff;
  --ease: cubic-bezier(.16,1,.3,1);
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
  .soc-18 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(88% .006 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-18:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #33333d;
  }
}

.soc-18[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #33333d;
}

.soc-18,
.soc-18 *,
.soc-18 *::before,
.soc-18 *::after {
  box-sizing: border-box;
}

.soc-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-18__card {
  inline-size: min(34rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-18__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-18__title {
  margin: 0 0 1.6rem;
  font-size: clamp(1.05rem,1rem + .8vw,1.35rem);
  font-weight: 600;
  letter-spacing: -.02em;
}

.soc-18__row {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.soc-18__btn {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-block-size: 2.875rem;
  padding: 0 1.15rem;
  min-inline-size: 0;
  border: 1.5px solid var(--line);
  border-radius: .85rem;
  background: transparent;
  color: var(--fg);
  text-decoration: none;
  font-size: .9rem;
  font-weight: 550;
  transition: background-color .26s var(--ease), border-color .26s var(--ease), color .26s var(--ease), box-shadow .26s var(--ease);
}

.soc-18__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.soc-18__btn span {
  min-inline-size: 0;
}

.soc-18__btn:hover,
.soc-18__btn:focus-visible {
  background: var(--brand);
  border-color: var(--brand);
  color: var(--on-brand);
  box-shadow: 0 14px 28px -18px color-mix(in oklab,var(--brand) 90%,transparent);
}

.soc-18__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-18__note {
  margin: 1.5rem 0 0;
  font-size: .8rem;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .soc-18__btn {
    transition-duration: 1ms;
  }
}

@media (forced-colors: active) {
  .soc-18__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .soc-18__btn:hover,
    .soc-18__btn:focus-visible {
    background: Highlight;
    color: HighlightText;
    border-color: Highlight;
  }
}
```

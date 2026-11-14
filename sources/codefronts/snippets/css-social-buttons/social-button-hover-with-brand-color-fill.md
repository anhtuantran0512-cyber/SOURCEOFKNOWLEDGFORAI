---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/social-button-hover-with-brand-color-fill/"
title: "Social Button Hover with Brand Color Fill"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "Brand colour floods each button from the bottom edge on hover, and the label and mark invert to white as the fill passes beneath them."
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Social Button Hover with Brand Color Fill
Source: https://codefronts.com/snippets/css-social-buttons/social-button-hover-with-brand-color-fill/

Brand colour floods each button from the bottom edge on hover, and the label and mark invert to white as the fill passes beneath them. The fill is a transformed pseudo-element — scaleY() on a ::before with transform-origin at the bottom — not a background-position hack and not a width transition, so it stays on the compositor and never triggers layout.
## HTML
```html
<div class="soc-02">
  <div class="soc-02__stage">
    <div class="soc-02__card">
      <p class="soc-02__eyebrow">Share this article</p>
      <h2 class="soc-02__title">Designing focus states people can actually see</h2>
      <div class="soc-02__row">
        <a class="soc-02__btn" style="--brand:#0f1419;--on-brand:#ffffff" href="https://example.com/share/x" target="_blank" rel="noopener">
          <span class="soc-02__in">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg>
            <span>Post</span>
          </span>
        </a>
        <a class="soc-02__btn" style="--brand:#0a66c2;--on-brand:#ffffff" href="https://example.com/share/linkedin" target="_blank" rel="noopener">
          <span class="soc-02__in">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg>
            <span>LinkedIn</span>
          </span>
        </a>
        <a class="soc-02__btn" style="--brand:#ff4500;--on-brand:#ffffff" href="https://example.com/share/reddit" target="_blank" rel="noopener">
          <span class="soc-02__in">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="7.4"/><circle cx="9.4" cy="12.4" r=".95" fill="currentColor" stroke="none"/><circle cx="14.6" cy="12.4" r=".95" fill="currentColor" stroke="none"/><path d="M9.3 15.6a4.2 4.2 0 0 0 5.4 0"/><path d="M12 5.6 13.4 3"/></svg>
            <span>Reddit</span>
          </span>
        </a>
        <a class="soc-02__btn" style="--brand:#1877f2;--on-brand:#ffffff" href="https://example.com/share/facebook" target="_blank" rel="noopener">
          <span class="soc-02__in">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/><path d="M14.6 8.2h-1.3a1.9 1.9 0 0 0-1.9 1.9v6.3"/><path d="M9.9 12.4h4.2"/></svg>
            <span>Facebook</span>
          </span>
        </a>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-02 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
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
  .soc-02 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-02:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
  }
}

.soc-02[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
}

.soc-02,
.soc-02 *,
.soc-02 *::before,
.soc-02 *::after {
  box-sizing: border-box;
}

.soc-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-02__card {
  inline-size: min(36rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-02__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-02__title {
  margin: 0 0 1.6rem;
  font-size: clamp(1.05rem,1rem + .8vw,1.35rem);
  font-weight: 600;
  line-height: 1.35;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.soc-02__row {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.soc-02__btn {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  min-inline-size: 0;
  display: inline-grid;
  align-items: center;
  min-block-size: 2.875rem;
  padding: 0 1.15rem;
  border: 1px solid var(--line);
  border-radius: .85rem;
  background: var(--surface);
  color: var(--fg);
  text-decoration: none;
  font-size: .9rem;
  font-weight: 550;
  transition: color .3s ease, border-color .3s ease, box-shadow .3s ease;
  -webkit-tap-highlight-color: transparent;
}

.soc-02__in {
  position: relative;
  display: flex;
  align-items: center;
  gap: .5rem;
  min-inline-size: 0;
}

.soc-02__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.soc-02__btn::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background: var(--brand);
  transform-origin: bottom;
  scale: 1 0;
  transition: scale .38s cubic-bezier(.16,1,.3,1);
}

.soc-02__btn:hover,
.soc-02__btn:focus-visible {
  color: var(--on-brand);
  border-color: var(--brand);
  box-shadow: 0 12px 26px -16px color-mix(in oklab,var(--brand) 85%,transparent);
}

.soc-02__btn:hover::before,
.soc-02__btn:focus-visible::before {
  scale: 1 1;
}

.soc-02__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-02__btn:active::before {
  scale: 1 1;
}

@media (prefers-reduced-motion: reduce) {
  .soc-02__btn::before {
    transition-duration: 1ms;
  }

  .soc-02__btn {
    transition-duration: 1ms;
  }
}

@media (forced-colors: active) {
  .soc-02__btn::before {
    display: none;
  }

  .soc-02__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .soc-02__btn:hover,
    .soc-02__btn:focus-visible {
    background: Highlight;
    color: HighlightText;
  }
}
```

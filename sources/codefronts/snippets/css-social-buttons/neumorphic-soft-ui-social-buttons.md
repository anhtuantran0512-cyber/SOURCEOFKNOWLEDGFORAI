---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/neumorphic-soft-ui-social-buttons/"
title: "Neumorphic Soft UI Social Buttons"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "Soft-UI social buttons that actually press: a light shadow at the top-left, a dark one at the bottom-right, and both inverted to inset on :active so the…"
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft UI Social Buttons
Source: https://codefronts.com/snippets/css-social-buttons/neumorphic-soft-ui-social-buttons/

Soft-UI social buttons that actually press: a light shadow at the top-left, a dark one at the bottom-right, and both inverted to inset on :active so the control sinks into the surface. Because low-contrast edges are the known failure of this style, every button also carries a brand-coloured icon and a real focus ring rather than relying on shadow alone.
## HTML
```html
<div class="soc-16">
  <div class="soc-16__stage">
    <div class="soc-16__panel">
      <p class="soc-16__eyebrow">Soft UI</p>
      <h2 class="soc-16__title">Press one — the surface sinks</h2>
      <div class="soc-16__row">
        <a class="soc-16__btn" style="--brand:#0f1419" href="https://example.com/alexchen" target="_blank" rel="noopener" aria-label="Alex Chen on X">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg>
        </a>
        <a class="soc-16__btn" style="--brand:#0a66c2" href="https://example.com/in/alexchen" target="_blank" rel="noopener" aria-label="Alex Chen on LinkedIn">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg>
        </a>
        <a class="soc-16__btn" style="--brand:#e1306c" href="https://example.com/alexchen" target="_blank" rel="noopener" aria-label="Alex Chen on Instagram">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/><circle cx="12" cy="12" r="3.9"/><circle cx="17.1" cy="6.9" r="1.15" fill="currentColor" stroke="none"/></svg>
        </a>
        <a class="soc-16__btn" style="--brand:#6f42c1" href="https://example.com/alexchen" target="_blank" rel="noopener" aria-label="Alex Chen on GitHub">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.6"/><path d="m9.8 9.4-2.3 2.6 2.3 2.6"/><path d="m14.2 9.4 2.3 2.6-2.3 2.6"/></svg>
        </a>
        <a class="soc-16__btn" style="--brand:#0e8a55" href="mailto:[email protected]" aria-label="Email Alex Chen">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.2" width="18" height="13.6" rx="3.4"/><path d="m4.4 8 6.7 4.7a1.6 1.6 0 0 0 1.8 0L19.6 8"/></svg>
        </a>
      </div>
      <p class="soc-16__note">Shadows carry the depth; the coloured glyph and focus ring carry the contrast.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-16 {
  --surface: #e8eaf0;
  --fg: #2a2d38;
  --muted: #6b7080;
  --ring: #3d63ff;
  --light: #ffffff;
  --shade: #c2c6d2;
  --size: 3.5rem;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--surface);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .soc-16 {
    --surface: oklch(92.5% .008 265);
    --fg: oklch(32% .02 265);
    --muted: oklch(55% .02 265);
    --light: color-mix(in oklab,var(--surface) 55%,white);
    --shade: color-mix(in oklab,var(--surface) 62%,#5b6072);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-16:not([data-theme="light"]) {
    --surface: #22242c;
    --fg: #e6e8ef;
    --muted: #9aa0b0;
    --light: #2e313b;
    --shade: #14151a;
  }
}

.soc-16[data-theme="dark"] {
  --surface: #22242c;
  --fg: #e6e8ef;
  --muted: #9aa0b0;
  --light: #2e313b;
  --shade: #14151a;
}

.soc-16,
.soc-16 *,
.soc-16 *::before,
.soc-16 *::after {
  box-sizing: border-box;
}

.soc-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-16__panel {
  inline-size: min(32rem,100%);
  padding: clamp(1.75rem,5vw,2.75rem);
  border-radius: 2rem;
  background: var(--surface);
  box-shadow: -10px -10px 24px var(--light), 12px 12px 30px var(--shade);
}

.soc-16__eyebrow {
  margin: 0 0 .5rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-16__title {
  margin: 0 0 1.75rem;
  font-size: clamp(1.05rem,1rem + .8vw,1.3rem);
  font-weight: 600;
  letter-spacing: -.02em;
}

.soc-16__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.soc-16__btn {
  display: grid;
  place-items: center;
  inline-size: var(--size);
  block-size: var(--size);
  border-radius: 1.15rem;
  background: var(--surface);
  color: var(--brand);
  text-decoration: none;
  box-shadow: -6px -6px 13px var(--light), 6px 6px 14px var(--shade);
  transition: box-shadow .22s ease, scale .18s cubic-bezier(.16,1,.3,1), color .2s ease;
  -webkit-tap-highlight-color: transparent;
}

.soc-16__btn svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
}

.soc-16__btn:hover {
  scale: 1.03;
  box-shadow: -8px -8px 16px var(--light), 8px 8px 18px var(--shade);
}

.soc-16__btn:active {
  scale: .98;
  box-shadow: inset -4px -4px 9px var(--light), inset 4px 4px 10px var(--shade);
}

.soc-16__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 4px;
}

.soc-16__note {
  margin: 1.75rem 0 0;
  font-size: .8rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-contrast: more) {
  .soc-16__btn {
    border: 1px solid var(--fg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .soc-16__btn {
    transition: box-shadow .01s;
  }

  .soc-16__btn:hover {
    scale: 1;
  }

  .soc-16__btn:active {
    scale: 1;
  }
}

@media (forced-colors: active) {
  .soc-16__panel,
    .soc-16__btn {
    box-shadow: none;
    border: 1px solid ButtonText;
  }

  .soc-16__btn {
    color: ButtonText;
  }
}
```

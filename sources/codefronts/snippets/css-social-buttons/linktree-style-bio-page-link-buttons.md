---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/linktree-style-bio-page-link-buttons/"
title: "Linktree Style Bio Page Link Buttons"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "A self-hosted link-in-bio stack: monogram avatar and handle at the top, then full-width channel buttons each with a leading mark and a trailing chevron that…"
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Linktree Style Bio Page Link Buttons
Source: https://codefronts.com/snippets/css-social-buttons/linktree-style-bio-page-link-buttons/

A self-hosted link-in-bio stack: monogram avatar and handle at the top, then full-width channel buttons each with a leading mark and a trailing chevron that slides on hover. One column, real anchors, no framework — the version you paste into a personal site instead of renting a hosted page.
## HTML
```html
<div class="soc-13">
  <div class="soc-13__stage">
    <main class="soc-13__page">
      <header class="soc-13__head">
        <span class="soc-13__avatar" aria-hidden="true">SR</span>
        <h1 class="soc-13__name">Sam Rivera</h1>
        <p class="soc-13__handle">@samrivera</p>
        <p class="soc-13__bio">Front-end engineer · Weekly CSS teardowns · Sydney</p>
      </header>
      <nav class="soc-13__list" aria-label="Sam Rivera's links">
        <a class="soc-13__link" style="--brand:#ff0033" href="https://example.com/@samrivera" target="_blank" rel="noopener">
          <span class="soc-13__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="2.6" y="5.2" width="18.8" height="13.6" rx="4.4"/><path d="m10.4 9.4 5 2.6-5 2.6Z" fill="currentColor"/></svg></span>
          <span class="soc-13__label">Latest teardown on YouTube<small>New · 12 min</small></span>
          <svg class="soc-13__chev" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9.5 5.5 7 6.5-7 6.5"/></svg>
        </a>
        <a class="soc-13__link" style="--brand:#0f1419" href="https://example.com/samrivera" target="_blank" rel="noopener">
          <span class="soc-13__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg></span>
          <span class="soc-13__label">Daily notes on X<small>@samrivera</small></span>
          <svg class="soc-13__chev" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9.5 5.5 7 6.5-7 6.5"/></svg>
        </a>
        <a class="soc-13__link" style="--brand:#6f42c1" href="https://example.com/samrivera" target="_blank" rel="noopener">
          <span class="soc-13__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.6"/><path d="m9.8 9.4-2.3 2.6 2.3 2.6"/><path d="m14.2 9.4 2.3 2.6-2.3 2.6"/></svg></span>
          <span class="soc-13__label">Open source on GitHub<small>34 repositories</small></span>
          <svg class="soc-13__chev" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9.5 5.5 7 6.5-7 6.5"/></svg>
        </a>
        <a class="soc-13__link" style="--brand:#e1306c" href="https://example.com/samrivera" target="_blank" rel="noopener">
          <span class="soc-13__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/><circle cx="12" cy="12" r="3.9"/><circle cx="17.1" cy="6.9" r="1.15" fill="currentColor" stroke="none"/></svg></span>
          <span class="soc-13__label">Work in progress on Instagram<small>@sam.builds</small></span>
          <svg class="soc-13__chev" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9.5 5.5 7 6.5-7 6.5"/></svg>
        </a>
        <a class="soc-13__link" style="--brand:#0e8a55" href="https://example.com/newsletter" target="_blank" rel="noopener">
          <span class="soc-13__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.2" width="18" height="13.6" rx="3.4"/><path d="m4.4 8 6.7 4.7a1.6 1.6 0 0 0 1.8 0L19.6 8"/></svg></span>
          <span class="soc-13__label">Join the Friday newsletter<small>4,900 readers</small></span>
          <svg class="soc-13__chev" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9.5 5.5 7 6.5-7 6.5"/></svg>
        </a>
      </nav>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap');

.soc-13 {
  --bg: #f2f2f5;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --row: 3.75rem;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(120% 60% at 50% 0%,color-mix(in oklab,#7c5cff 14%,transparent),transparent 70%), var(--bg);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .soc-13 {
    --bg: oklch(96% .004 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-13:not([data-theme="light"]) {
    --bg: #08080b;
    --surface: #14141a;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
  }
}

.soc-13[data-theme="dark"] {
  --bg: #08080b;
  --surface: #14141a;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
}

.soc-13,
.soc-13 *,
.soc-13 *::before,
.soc-13 *::after {
  box-sizing: border-box;
}

.soc-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3rem);
}

.soc-13__page {
  inline-size: min(26rem,100%);
}

.soc-13__head {
  text-align: center;
  margin-block-end: 1.5rem;
}

.soc-13__avatar {
  display: grid;
  place-items: center;
  inline-size: 4.5rem;
  block-size: 4.5rem;
  margin: 0 auto .9rem;
  border-radius: 50%;
  background: linear-gradient(140deg,#7c5cff,#2ec8b0);
  color: #fff;
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: .02em;
  box-shadow: 0 12px 30px -14px color-mix(in oklab,#7c5cff 70%,transparent);
}

.soc-13__name {
  margin: 0;
  font-size: 1.35rem;
  font-weight: 600;
  letter-spacing: -.025em;
}

.soc-13__handle {
  margin: .15rem 0 .6rem;
  font-size: .9rem;
  color: var(--muted);
}

.soc-13__bio {
  margin: 0;
  font-size: .85rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.soc-13__list {
  display: grid;
  gap: .6rem;
}

.soc-13__link {
  display: grid;
  grid-template-columns: 2.5rem 1fr 1.25rem;
  align-items: center;
  gap: .85rem;
  min-block-size: var(--row);
  padding: .55rem .9rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
  color: var(--fg);
  text-decoration: none;
  box-shadow: 0 1px 2px rgb(0 0 0/.04);
  transition: translate .2s cubic-bezier(.16,1,.3,1), border-color .2s ease, box-shadow .2s ease;
}

.soc-13__tile {
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: .75rem;
  background: color-mix(in oklab,var(--brand) 14%,var(--surface));
  color: var(--brand);
}

.soc-13__tile svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.soc-13__label {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
  font-size: .93rem;
  font-weight: 550;
  letter-spacing: -.01em;
  overflow-wrap: anywhere;
}

.soc-13__label small {
  font-size: .76rem;
  font-weight: 400;
  color: var(--muted);
}

.soc-13__chev {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  color: var(--muted);
  transition: translate .2s cubic-bezier(.16,1,.3,1), color .2s ease;
}

.soc-13__link:hover {
  translate: 0 -2px;
  border-color: color-mix(in oklab,var(--brand) 40%,var(--line));
  box-shadow: 0 16px 32px -22px color-mix(in oklab,var(--brand) 85%,transparent);
}

.soc-13__link:hover .soc-13__chev,
.soc-13__link:focus-visible .soc-13__chev {
  translate: .25rem 0;
  color: var(--brand);
}

.soc-13__link:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .soc-13__link,
    .soc-13__chev {
    transition-duration: 1ms;
  }

  .soc-13__link:hover {
    translate: none;
  }

  .soc-13__link:hover .soc-13__chev {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-13__link {
    border: 1px solid ButtonText;
  }

  .soc-13__tile {
    border: 1px solid ButtonText;
    color: ButtonText;
  }
}
```

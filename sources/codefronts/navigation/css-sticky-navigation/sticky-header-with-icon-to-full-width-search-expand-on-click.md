---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-icon-to-full-width-search-expand-on-click/"
title: "Sticky Header with Icon-to-Full-Width Search Expand on Click"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "Space-saving search for a header that already has too much in it: a magnifier that expands into a full-width field on activation, pushing the navigation…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header with Icon-to-Full-Width Search Expand on Click
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-icon-to-full-width-search-expand-on-click/

Space-saving search for a header that already has too much in it: a magnifier that expands into a full-width field on activation, pushing the navigation aside, then collapses on Escape or blur. The interaction lives or dies on focus management, which is where most implementations fall down.
## HTML
```html
<section class="sn-20" aria-label="Expanding search in sticky header demo">
    <header class="sn-20__bar" id="sn-20-bar">
      <a class="sn-20__brand" href="#sn-20-s1"><span class="sn-20__logo" aria-hidden="true"></span>Archive</a>
      <nav class="sn-20__nav" id="sn-20-nav" aria-label="Primary">
        <a class="sn-20__link" href="#sn-20-s1" aria-current="page">Collection</a>
        <a class="sn-20__link" href="#sn-20-s2">Exhibitions</a>
        <a class="sn-20__link" href="#sn-20-s3">Visit</a>
      </nav>
      <div class="sn-20__search" id="sn-20-search" data-open="false" role="search">
        <button class="sn-20__toggle" type="button" id="sn-20-toggle" aria-expanded="false" aria-controls="sn-20-input" aria-label="Open search">
          <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m13.5 13.5 3.5 3.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </button>
        <label class="sn-20__sr" for="sn-20-input">Search the collection</label>
        <input class="sn-20__input" id="sn-20-input" type="search" placeholder="Search the collection…" autocomplete="off" inert>
        <button class="sn-20__clear" type="button" id="sn-20-clear" aria-label="Close search" tabindex="-1">
          <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="m4 4 8 8M12 4l-8 8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        </button>
      </div>
    </header>
  <div class="sn-20__intro">
    <div class="sn-20__introin">
    <p class="sn-20__intro-eyebrow">inline-size · focus · Escape</p>
    <h2 class="sn-20__intro-title">One header, two modes</h2>
    <p class="sn-20__intro-sub">Click the magnifier, type, then press Escape.</p>
    </div>
  </div>
    <p class="sn-20__live" id="sn-20-live" role="status" aria-live="polite"></p>
    <main>
      <section class="sn-20__sec" id="sn-20-s1">
        <p class="sn-20__kicker">Focus first</p>
        <h3 class="sn-20__h">Expand and focus in one frame</h3>
        <p class="sn-20__p">The input is always mounted at zero width, so it can take focus the instant it opens — no gap where the keyboard has nowhere to go.</p>
      </section>
      <section class="sn-20__sec" id="sn-20-s2">
        <p class="sn-20__kicker">Escape</p>
        <h3 class="sn-20__h">Give the focus back</h3>
        <p class="sn-20__p">Closing returns focus to the magnifier. Without that, the next Tab press restarts from the top of the document.</p>
      </section>
      <section class="sn-20__sec" id="sn-20-s3">
        <p class="sn-20__kicker">Typed input is sacred</p>
        <h3 class="sn-20__h">Only collapse when empty</h3>
        <p class="sn-20__p">Blurring a field that contains a query and watching it disappear is the fastest way to lose a user's trust in a search box.</p>
      </section>
    </main>
  <footer class="sn-20__pagefoot">
    <p class="sn-20__pagefootin">Sticky navigation pattern 20 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-20-bg);
  --sn-20-bg: oklch(0.94 0.006 20);
  --sn-20-surface: oklch(0.995 0.002 20);
  --sn-20-ink: oklch(0.2 0.016 20);
  --sn-20-mut: oklch(0.51 0.016 20);
  --sn-20-acc: oklch(0.5 0.19 22);
  --sn-20-line: oklch(0.2 0.016 20/.13);
  --sn-20-h: 64px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-20-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-20 *,
.sn-20 *::before,
.sn-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-20__eyebrow,
.sn-20__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-20-acc);
}

.sn-20__title,
.sn-20__intro-title {
  font-size: clamp(23px,3.5vw,36px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-20__sub,
.sn-20__intro-sub {
  font-size: 14.4px;
  line-height: 1.6;
  color: var(--sn-20-mut);
  text-wrap: pretty;
}

.sn-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sn-20__bar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: var(--sn-20-h);
  padding: 0 clamp(12px,2.4vw,20px);
  background: color-mix(in oklch,var(--sn-20-surface) 90%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-20-line);
}

.sn-20__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.03em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-20__logo {
  width: 9px;
  height: 20px;
  border-radius: 2px;
  background: var(--sn-20-acc);
}

.sn-20__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
  min-width: 0;
  opacity: 1;
  transition: opacity .24s ease;
}

.sn-20__link {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--sn-20-mut);
  text-decoration: none;
  white-space: nowrap;
  transition: color .18s ease,background .18s ease;
}

.sn-20__link:hover {
  color: var(--sn-20-ink);
  background: oklch(0.2 0.016 20/.05);
}

.sn-20__link[aria-current="page"] {
  color: var(--sn-20-acc);
}

.sn-20__search {
  display: flex;
  align-items: center;
  gap: 4px;
  flex: none;
  inline-size: 44px;
  block-size: 44px;
  padding-inline: 0;
  border: 1px solid transparent;
  border-radius: 99px;
  background: transparent;
  overflow: hidden;
  transition: inline-size .34s cubic-bezier(.32,.72,.3,1),background .24s ease,border-color .24s ease,padding .24s ease;
}

.sn-20__search[data-open="true"] {
  inline-size: min(100%,420px);
  padding-inline: 6px 6px;
  background: oklch(0.2 0.016 20/.04);
  border-color: var(--sn-20-line);
}

.sn-20__search[data-open="true"]:focus-within {
  border-color: var(--sn-20-acc);
  background: var(--sn-20-surface);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--sn-20-acc) 16%,transparent);
}

.sn-20__toggle {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 0;
  border-radius: 99px;
  background: transparent;
  color: var(--sn-20-mut);
  cursor: pointer;
  transition: color .18s ease,background .18s ease;
}

.sn-20__toggle:hover {
  color: var(--sn-20-ink);
  background: oklch(0.2 0.016 20/.05);
}

.sn-20__toggle svg {
  inline-size: 19px;
  block-size: 19px;
}

.sn-20__input {
  flex: 1;
  min-width: 0;
  border: 0;
  background: transparent;
  font-family: inherit;
  font-size: 14.2px;
  color: var(--sn-20-ink);
  opacity: 0;
  outline: none;
  transition: opacity .2s ease .06s;
}

.sn-20__search[data-open="true"] .sn-20__input {
  opacity: 1;
}

.sn-20__input::placeholder {
  color: color-mix(in oklch,var(--sn-20-mut) 75%,transparent);
}

.sn-20__clear {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 30px;
  block-size: 30px;
  border: 0;
  border-radius: 99px;
  background: oklch(0.2 0.016 20/.07);
  color: var(--sn-20-mut);
  cursor: pointer;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s ease;
}

.sn-20__search[data-open="true"] .sn-20__clear {
  opacity: 1;
  pointer-events: auto;
}

.sn-20__clear svg {
  inline-size: 13px;
  block-size: 13px;
}

.sn-20__toggle:focus-visible,
.sn-20__clear:focus-visible,
.sn-20__link:focus-visible,
.sn-20__brand:focus-visible {
  outline: 2px solid var(--sn-20-acc);
  outline-offset: 2px;
}

.sn-20__live {
  padding: 8px clamp(16px,3vw,24px) 0;
  min-height: 26px;
  font-size: 12.5px;
  color: var(--sn-20-acc);
}

.sn-20__sec {
  scroll-margin-top: var(--sn-20-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,46px);
  border-bottom: 1px solid var(--sn-20-line);
}

.sn-20__sec:nth-child(even) {
  background: oklch(0.975 0.004 20);
}

.sn-20__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-20-acc);
}

.sn-20__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-20__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-20-mut);
  text-wrap: pretty;
}

@media (max-width: 640px) {
  .sn-20__bar:has(.sn-20__search[data-open="true"]) .sn-20__nav {
    opacity: 0;
    pointer-events: none;
    inline-size: 0;
    overflow: hidden;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-20 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-20) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-20-h) + 10px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-20) {
    scroll-behavior: auto;
  }
}

.sn-20__bar,
.sn-20__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-20__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-20__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
}

.sn-20__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-20__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-20__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-20__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-20__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-20-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-20-mut);
  animation: sn-20-cue 2.6s ease-in-out infinite;
}

@keyframes sn-20-cue {
  0%,
    100% {
    transform: translateY(0);
    opacity: .75;
  }

  50% {
    transform: translateY(5px);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-20__intro::after {
    animation: none;
  }
}

.sn-20__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-20-line);
}

.sn-20__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-20-mut);
  text-align: center;
}

.sn-20__intro-title,
.sn-20__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-20');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const shell = root.querySelector('#sn-20-search');
  const toggle = root.querySelector('#sn-20-toggle');
  const input = root.querySelector('#sn-20-input');
  const clear = root.querySelector('#sn-20-clear');
  const live = root.querySelector('#sn-20-live');
  const set = (open, restore) => {
    shell.dataset.open = String(open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Search the collection' : 'Open search');
    input.toggleAttribute('inert', !open);
    clear.tabIndex = open ? 0 : -1;
    if (open) input.focus();
    else if (restore) toggle.focus();
  };
  toggle.addEventListener('click', () => set(shell.dataset.open !== 'true', true));
  clear.addEventListener('click', () => { input.value = ''; live.textContent = ''; set(false, true); });
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') set(false, true);
    if (e.key === 'Enter') { e.preventDefault(); live.textContent = input.value.trim() ? 'Searching for “' + input.value.trim() + '”…' : 'Type a query to search'; }
  });
  shell.addEventListener('focusout', (e) => {
    if (!shell.contains(e.relatedTarget) && !input.value.trim()) set(false, false);
  });
})();
```

---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/tailwind-css-pagination-component/"
title: "Tailwind CSS Pagination Component"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "The utility-first pagination bar written out in full, with the exact class string you would paste into a Tailwind project — plus the @apply-style component…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Pagination Component
Source: https://codefronts.com/navigation/css-pagination/tailwind-css-pagination-component/

The utility-first pagination bar written out in full, with the exact class string you would paste into a Tailwind project — plus the @apply-style component classes that stop twelve number buttons from each carrying forty utilities. No CDN and no build step: the demo reproduces those utilities as scoped vanilla CSS so it renders identically in an isolated frame.
## HTML
```html
<section class="pgn-07" aria-label="Tailwind CSS Pagination Component demo">
  <div class="stage">
    <header class="mb-8">
      <p class="eyebrow">Utility-first markup</p>
      <h2 class="text-2xl font-semibold tracking-tight">Tailwind class names, zero runtime</h2>
      <p class="text-sm text-muted mt-2 max-w-lg">The markup below is the exact utility string you would paste into a Tailwind project. The stylesheet reproduces those utilities as scoped vanilla CSS, so the demo renders identically with no build step and no CDN.</p>
    </header>

    <nav aria-label="Pagination" class="inline-flex items-center gap-1 rounded-xl border bg-surface p-1 shadow-sm">
      <button type="button" class="btn-ghost px-3" aria-label="Previous page">
        <svg viewBox="0 0 20 20" class="icon" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="hidden-sm">Previous</span>
      </button>

      <ol class="flex items-center gap-1">
        <li><button type="button" class="btn-ghost">1</button></li>
        <li><button type="button" class="btn-ghost">2</button></li>
        <li><button type="button" class="btn-solid" aria-current="page">3</button></li>
        <li><button type="button" class="btn-ghost">4</button></li>
        <li aria-hidden="true" class="gap">…</li>
        <li><button type="button" class="btn-ghost">12</button></li>
      </ol>

      <button type="button" class="btn-ghost px-3" aria-label="Next page">
        <span class="hidden-sm">Next</span>
        <svg viewBox="0 0 20 20" class="icon" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </nav>

    <p class="text-xs text-muted mt-6">Equivalent Tailwind source: <code>class="inline-flex items-center gap-1 rounded-xl border border-zinc-200 bg-white p-1 shadow-sm"</code></p>
  </div>
</section>
```
## CSS
```css
.pgn-07 {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f4f4f5;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #18181b;
  --acc-fg: #ffffff;
  --ring: #6366f1;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-07 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96.5% .003 286);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(22% .008 286);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-07:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --surface-2: #1c1c20;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #fafafa;
    --acc-fg: #09090b;
    --ring: #818cf8;
  }
}

.pgn-07[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --surface-2: #1c1c20;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
}

.pgn-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,5vw,4rem);
  background: var(--bg);
  color: var(--text);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.pgn-07,
.pgn-07 *,
.pgn-07 *::before,
.pgn-07 *::after {
  box-sizing: border-box;
}

.pgn-07 .stage {
  width: 100%;
  max-width: 46rem;
}

.pgn-07 .eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}
/* utility layer — what @apply / the Tailwind build would emit, scoped to .pgn-07 */

.pgn-07 .flex {
  display: flex;
}

.pgn-07 .inline-flex {
  display: inline-flex;
}

.pgn-07 .items-center {
  align-items: center;
}

.pgn-07 .gap-1 {
  gap: .25rem;
}

.pgn-07 .mb-8 {
  margin-bottom: 2rem;
}

.pgn-07 .mt-2 {
  margin-top: .5rem;
}

.pgn-07 .mt-6 {
  margin-top: 1.5rem;
}

.pgn-07 .p-1 {
  padding: .25rem;
}

.pgn-07 .px-3 {
  padding-inline: .75rem;
}

.pgn-07 .max-w-lg {
  max-width: 32rem;
}

.pgn-07 .rounded-xl {
  border-radius: .75rem;
}

.pgn-07 .border {
  border: 1px solid var(--line);
}

.pgn-07 .bg-surface {
  background: var(--surface);
}

.pgn-07 .shadow-sm {
  box-shadow: 0 1px 2px color-mix(in oklab,var(--text) 8%,transparent);
}

.pgn-07 .text-2xl {
  font-size: 1.5rem;
  line-height: 1.2;
}

.pgn-07 .text-sm {
  font-size: .875rem;
  line-height: 1.6;
}

.pgn-07 .text-xs {
  font-size: .75rem;
  line-height: 1.6;
}

.pgn-07 .font-semibold {
  font-weight: 600;
}

.pgn-07 .tracking-tight {
  letter-spacing: -.025em;
}

.pgn-07 .text-muted {
  color: var(--muted);
}

.pgn-07 h2,
.pgn-07 p {
  margin: 0;
}

.pgn-07 ol {
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-07 code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .6875rem;
  background: var(--surface-2);
  padding: .15rem .35rem;
  border-radius: .25rem;
}
/* component classes — the @apply targets */

.pgn-07 .btn-ghost,
.pgn-07 .btn-solid {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .35rem;
  min-width: 2.75rem;
  height: 2.75rem;
  padding-inline: .5rem;
  border: 0;
  border-radius: .5rem;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: .875rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .15s ease, color .15s ease;
}

.pgn-07 .btn-ghost:hover {
  background: var(--surface-2);
}

.pgn-07 .btn-solid {
  background: var(--acc);
  color: var(--acc-fg);
}

.pgn-07 .btn-solid:hover {
  opacity: .9;
}

.pgn-07 .btn-ghost:focus-visible,
.pgn-07 .btn-solid:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-07 .icon {
  width: 1.05rem;
  height: 1.05rem;
  color: var(--muted);
}

.pgn-07 .gap {
  display: grid;
  place-items: end center;
  min-width: 1.5rem;
  height: 2.75rem;
  padding-bottom: .6rem;
  color: var(--muted);
}

@media (max-width: 34rem) {
  .pgn-07 .hidden-sm {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip-path: inset(50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .pgn-07 * {
    animation: none !important;
    transition: none !important;
  }
}
```

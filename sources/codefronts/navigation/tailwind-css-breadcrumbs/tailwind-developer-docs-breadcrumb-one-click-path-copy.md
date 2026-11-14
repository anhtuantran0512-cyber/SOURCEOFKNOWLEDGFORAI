---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-developer-docs-breadcrumb-one-click-path-copy/"
title: "Tailwind Developer Docs Breadcrumb with One-Click Path Copy"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The terminal-flavoured docs trail: monospace crumbs, slash separators, and a copy button that puts the whole path on the clipboard for pasting into a PR or a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Developer Docs Breadcrumb with One-Click Path Copy
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-developer-docs-breadcrumb-one-click-path-copy/

The terminal-flavoured docs trail: monospace crumbs, slash separators, and a copy button that puts the whole path on the clipboard for pasting into a PR or a ticket. The copied state is a data-copied attribute, so the icon swap and the button's own recolour both read it through variants.
## HTML
```html
<section class="tbc-22 w-full min-h-svh grid place-items-center px-5 py-8 font-tbc22-mono text-tbc22-ink bg-[radial-gradient(1200px_600px_at_50%_-10%,oklch(0.28_0.05_265/0.55),transparent_60%),var(--color-tbc22-bg)]">
  <nav aria-label="Documentation breadcrumb" class="inline-flex items-center gap-2 max-w-full overflow-x-auto pl-4 pr-2 py-2 rounded-xl bg-tbc22-surface border border-tbc22-edge shadow-[inset_0_1px_0_oklch(1_0_0/0.04),0_10px_30px_-12px_oklch(0_0_0/0.6)] text-[15px]/[1.2] [scrollbar-width:thin]">
    <ol class="inline-flex flex-nowrap items-center gap-1 list-none m-0 p-0">
      <li class="inline-flex items-center whitespace-nowrap"><a href="#" class="px-2 py-1.5 rounded-md text-tbc22-mut no-underline transition-colors duration-150 hover:text-tbc22-hover hover:bg-[color-mix(in_oklch,var(--color-tbc22-acc)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc22-acc focus-visible:outline-offset-2">docs</a></li>
      <li class="inline-flex items-center whitespace-nowrap before:content-['/'] before:px-1 before:select-none before:text-tbc22-sep"><a href="#" class="px-2 py-1.5 rounded-md text-tbc22-mut no-underline transition-colors duration-150 hover:text-tbc22-hover hover:bg-[color-mix(in_oklch,var(--color-tbc22-acc)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc22-acc focus-visible:outline-offset-2">api</a></li>
      <li class="inline-flex items-center whitespace-nowrap before:content-['/'] before:px-1 before:select-none before:text-tbc22-sep"><a href="#" class="px-2 py-1.5 rounded-md text-tbc22-mut no-underline transition-colors duration-150 hover:text-tbc22-hover hover:bg-[color-mix(in_oklch,var(--color-tbc22-acc)_8%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc22-acc focus-visible:outline-offset-2">authentication</a></li>
      <li class="inline-flex items-center whitespace-nowrap before:content-['/'] before:px-1 before:select-none before:text-tbc22-sep"><a href="#" aria-current="page" class="px-2 py-1.5 rounded-md font-semibold cursor-default no-underline text-tbc22-acc bg-[color-mix(in_oklch,var(--color-tbc22-acc)_12%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc22-acc focus-visible:outline-offset-2">oauth2</a></li>
    </ol>
    <button type="button" aria-label="Copy path to clipboard" data-path="docs/api/authentication/oauth2" class="group relative grid place-items-center flex-none w-11 h-11 rounded-lg cursor-pointer appearance-none text-tbc22-ink bg-[color-mix(in_oklch,var(--color-tbc22-surface)_70%,oklch(0.28_0.02_260))] border border-tbc22-edge transition-[background-color,color,border-color,scale] duration-150 hover:text-white hover:border-[color-mix(in_oklch,var(--color-tbc22-acc)_40%,var(--color-tbc22-edge))] hover:bg-[color-mix(in_oklch,var(--color-tbc22-acc)_10%,var(--color-tbc22-surface))] active:scale-96 focus-visible:outline-2 focus-visible:outline-tbc22-acc focus-visible:outline-offset-2 data-copied:border-[color-mix(in_oklch,var(--color-tbc22-acc)_60%,var(--color-tbc22-edge))] data-copied:bg-[color-mix(in_oklch,var(--color-tbc22-acc)_15%,var(--color-tbc22-surface))] motion-reduce:transition-none motion-reduce:active:scale-100">
      <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="absolute inset-0 m-auto w-4.5 h-4.5 transition-[opacity,scale] duration-200 group-data-copied:opacity-0 group-data-copied:scale-60"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>
      <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" class="absolute inset-0 m-auto w-4.5 h-4.5 opacity-0 scale-60 text-tbc22-acc transition-[opacity,scale] duration-200 group-data-copied:opacity-100 group-data-copied:scale-100"><path d="m5 12 5 5L20 7"/></svg>
    </button>
    <span role="status" aria-live="polite" aria-atomic="true" class="sr-only"></span>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc22-bg: #1e2028;
  --color-tbc22-bg: oklch(0.16 0.02 260);
  --color-tbc22-surface: #2a2d36;
  --color-tbc22-surface: oklch(0.21 0.02 260);
  --color-tbc22-edge: #454955;
  --color-tbc22-edge: oklch(0.32 0.02 260 / 0.6);
  --color-tbc22-ink: #cfd2db;
  --color-tbc22-ink: oklch(0.82 0.02 260);
  --color-tbc22-mut: #9ba0ad;
  --color-tbc22-mut: oklch(0.68 0.02 260);
  --color-tbc22-hover: #eceef4;
  --color-tbc22-hover: oklch(0.92 0.02 260);
  --color-tbc22-sep: #6b7080;
  --color-tbc22-sep: oklch(0.5 0.02 260);
  --color-tbc22-acc: #c79df5;
  --color-tbc22-acc: oklch(0.78 0.17 300);
  --font-tbc22-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
}

.tbc-22 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tbc-22 button[data-path]').forEach(function (btn) {
    if (btn.dataset.bound) return; btn.dataset.bound = '1';
    var live = btn.parentElement.querySelector('[role="status"]'), timer;
    btn.addEventListener('click', function () {
      navigator.clipboard.writeText(btn.dataset.path).then(function () {
        btn.toggleAttribute('data-copied', true);
        if (live) live.textContent = 'Path copied to clipboard';
        clearTimeout(timer);
        timer = setTimeout(function () {
          btn.removeAttribute('data-copied');
          if (live) live.textContent = '';
        }, 1200);
      }).catch(function () {
        if (live) live.textContent = 'Copy failed — clipboard unavailable';
      });
    });
  });
})();
```

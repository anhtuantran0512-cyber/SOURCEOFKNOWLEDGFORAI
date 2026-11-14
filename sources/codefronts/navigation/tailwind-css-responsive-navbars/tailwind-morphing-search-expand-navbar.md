---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-morphing-search-expand-navbar/"
title: "Tailwind Morphing Search Expand Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "A search icon that grows into a field while the nav links step aside."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Morphing Search Expand Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-morphing-search-expand-navbar/

A search icon that grows into a field while the nav links step aside. One attribute on the root — data-searching — drives three elements at once: the capsule's width, the input's opacity, and the links' fade-out. The script focuses, collapses on Escape or outside click, and touches no styles.
## HTML
```html
<div class="tnb-15 group w-full min-h-svh bg-tnb15-page font-tnb15-sans text-tnb15-ink" aria-label="Morphing search expand navbar demo">
  <input type="checkbox" id="tnb15-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="sticky top-0 z-100 border-b border-tnb15-edge bg-white shadow-[0_1px_3px_oklch(0_0_0/0.05)]">
    <nav class="mx-auto flex h-16 max-w-6xl items-center gap-6 px-5 md:px-8" aria-label="Primary">
      <a href="#home" class="shrink-0 text-xl font-extrabold tracking-[-0.03em] text-tnb15-ink no-underline">Synapse<span class="text-tnb15-acc">.</span></a>
      <ul class="hidden flex-1 list-none items-center gap-1 transition-opacity duration-300 group-data-searching:pointer-events-none group-data-searching:opacity-0 md:flex motion-reduce:transition-none">
        <li><a href="#home" aria-current="page" class="block rounded-lg px-3.5 py-2 text-sm font-semibold text-tnb15-acc no-underline">Home</a></li>
        <li><a href="#features" class="block rounded-lg px-3.5 py-2 text-sm font-semibold text-tnb15-mut no-underline transition-colors duration-150 hover:bg-tnb15-tint hover:text-tnb15-ink">Features</a></li>
        <li><a href="#pricing" class="block rounded-lg px-3.5 py-2 text-sm font-semibold text-tnb15-mut no-underline transition-colors duration-150 hover:bg-tnb15-tint hover:text-tnb15-ink">Pricing</a></li>
        <li><a href="#docs" class="block rounded-lg px-3.5 py-2 text-sm font-semibold text-tnb15-mut no-underline transition-colors duration-150 hover:bg-tnb15-tint hover:text-tnb15-ink">Docs</a></li>
        <li><a href="#blog" class="block rounded-lg px-3.5 py-2 text-sm font-semibold text-tnb15-mut no-underline transition-colors duration-150 hover:bg-tnb15-tint hover:text-tnb15-ink">Blog</a></li>
      </ul>
      <div class="ml-auto flex w-10 items-center overflow-hidden rounded-[10px] border-[1.5px] border-transparent bg-tnb15-tint transition-[width,border-color,background] duration-400 ease-out group-data-searching:w-70 group-data-searching:border-tnb15-acc group-data-searching:bg-white motion-reduce:transition-none">
        <button type="button" id="tnb15-search-btn" aria-expanded="false" aria-controls="tnb15-search-input" aria-label="Search" class="grid size-10 shrink-0 cursor-pointer place-items-center rounded-[10px] border-0 bg-transparent text-base text-tnb15-acc">&#128269;</button>
        <input type="search" id="tnb15-search-input" placeholder="Search docs, features…" aria-label="Search query" class="pointer-events-none min-w-0 flex-1 border-0 bg-transparent pr-3 text-sm font-medium text-tnb15-ink opacity-0 outline-none transition-opacity duration-300 placeholder:text-tnb15-mut group-data-searching:pointer-events-auto group-data-searching:opacity-100 motion-reduce:transition-none">
      </div>
      <a href="#signup" class="hidden shrink-0 rounded-lg bg-tnb15-acc px-4 py-2 text-sm font-bold text-white no-underline transition-[background,translate] duration-200 hover:-translate-y-px hover:bg-tnb15-accdark md:block motion-reduce:transition-none motion-reduce:hover:translate-y-0">Sign up</a>
      <label for="tnb15-menu" class="flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb15-ink transition-transform duration-300 group-has-checked:translate-y-2 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb15-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb15-ink transition-transform duration-300 group-has-checked:-translate-y-2 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </nav>
    <div class="hidden border-t border-tnb15-edge px-5 py-2 max-md:group-has-checked:grid">
      <a href="#home" class="flex min-h-11 items-center rounded-lg px-2 text-[15px] font-semibold text-tnb15-acc no-underline">Home</a>
      <a href="#features" class="flex min-h-11 items-center rounded-lg px-2 text-[15px] font-semibold text-tnb15-mut no-underline transition-colors hover:bg-tnb15-tint hover:text-tnb15-ink">Features</a>
      <a href="#pricing" class="flex min-h-11 items-center rounded-lg px-2 text-[15px] font-semibold text-tnb15-mut no-underline transition-colors hover:bg-tnb15-tint hover:text-tnb15-ink">Pricing</a>
      <a href="#docs" class="flex min-h-11 items-center rounded-lg px-2 text-[15px] font-semibold text-tnb15-mut no-underline transition-colors hover:bg-tnb15-tint hover:text-tnb15-ink">Docs</a>
      <a href="#signup" class="mt-2 flex min-h-11 items-center justify-center rounded-lg bg-tnb15-acc text-sm font-bold text-white no-underline">Sign up</a>
    </div>
  </header>
  <main class="mx-auto max-w-3xl px-5 py-16 md:px-8">
    <h1 class="mb-4 text-4xl font-extrabold tracking-[-0.04em] text-tnb15-ink">Morphing Search Expand</h1>
    <p class="text-lg leading-relaxed text-tnb15-mut">Click the magnifier: the capsule grows from <code class="rounded bg-tnb15-tint px-1.5 py-0.5 text-[0.9em] text-tnb15-acc">w-10</code> to <code class="rounded bg-tnb15-tint px-1.5 py-0.5 text-[0.9em] text-tnb15-acc">w-70</code>, the field fades in and the links step aside. Escape or a click outside collapses it.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb15-page: #f8fafc;
  --color-tnb15-page: oklch(0.98 0.004 250);
  --color-tnb15-ink: #0f172a;
  --color-tnb15-ink: oklch(0.22 0.03 260);
  --color-tnb15-mut: #64748b;
  --color-tnb15-mut: oklch(0.55 0.03 255);
  --color-tnb15-edge: #e2e8f0;
  --color-tnb15-edge: oklch(0.91 0.01 250);
  --color-tnb15-tint: #eff6ff;
  --color-tnb15-tint: oklch(0.97 0.02 250);
  --color-tnb15-acc: #3b82f6;
  --color-tnb15-acc: oklch(0.62 0.19 258);
  --color-tnb15-accdark: #2563eb;
  --color-tnb15-accdark: oklch(0.55 0.21 258);
  --font-tnb15-sans: 'Figtree', system-ui, sans-serif;
}

.tnb-15 {
  width: 100%;
  min-height: 100svh;
}

.tnb-15 ::selection {
  background: var(--color-tnb15-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tnb-15').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var btn = root.querySelector('#tnb15-search-btn');
    var input = root.querySelector('#tnb15-search-input');
    if (!btn || !input) return;
    var isOpen = function () { return root.hasAttribute('data-searching'); };

    function set(open) {
      root.toggleAttribute('data-searching', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) setTimeout(function () { input.focus(); }, 300);
      else { input.value = ''; btn.focus(); }
    }

    btn.addEventListener('click', function (e) { e.stopPropagation(); set(!isOpen()); });
    input.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
    document.addEventListener('click', function (e) {
      if (isOpen() && !root.contains(e.target)) set(false);
      else if (isOpen() && !e.target.closest('#tnb15-search-btn') && !e.target.closest('#tnb15-search-input') && root.contains(e.target)) set(false);
    });
  });
})();
```

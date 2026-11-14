---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-breadcrumb-reading-progress-navbar/"
title: "Tailwind Breadcrumb Reading Progress Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "A docs header with a breadcrumb trail, a section pill row and a reading-progress bar."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Breadcrumb Reading Progress Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-breadcrumb-reading-progress-navbar/

A docs header with a breadcrumb trail, a section pill row and a reading-progress bar. The port changes one important thing: the script writes a single custom property, --tnb08-read, and the bar renders it as scale-x-[var(--tnb08-read)] — a compositor transform instead of a per-frame width, which is the difference between a smooth bar and a janky one.
## HTML
```html
<div class="tnb-08 group w-full min-h-svh bg-white font-tnb08-sans text-tnb08-ink" style="--tnb08-read:0" aria-label="Breadcrumb reading progress navbar demo">
  <input type="checkbox" id="tnb08-menu" class="sr-only peer" aria-label="Toggle section menu">
  <header class="sticky top-0 z-100 border-b border-tnb08-edge bg-white">
    <div class="h-[3px] bg-tnb08-track">
      <div class="relative h-full origin-left scale-x-[var(--tnb08-read)] bg-linear-[90deg,var(--color-tnb08-acc),var(--color-tnb08-acc2)] after:absolute after:-top-px after:right-0 after:size-[5px] after:rounded-full after:bg-tnb08-acc2 after:shadow-[0_0_6px_var(--color-tnb08-acc2)] after:content-['']" role="progressbar" aria-label="Reading progress"></div>
    </div>
    <div class="flex h-14 items-center gap-0 px-5 md:px-8">
      <a href="#docs" class="mr-6 shrink-0 text-lg font-bold tracking-[-0.02em] text-tnb08-ink no-underline">Docs</a>
      <nav class="flex-1 overflow-hidden" aria-label="Breadcrumb">
        <ol class="flex list-none items-center">
          <li class="flex items-center text-sm whitespace-nowrap"><a href="#home" class="rounded px-2 py-1 font-medium text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">Home</a></li>
          <li class="flex items-center text-sm whitespace-nowrap before:mx-2 before:text-xs before:text-tnb08-edge before:content-['/'] max-md:hidden"><a href="#guide" class="rounded px-2 py-1 font-medium text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">Guide</a></li>
          <li class="flex items-center text-sm whitespace-nowrap before:mx-2 before:text-xs before:text-tnb08-edge before:content-['/'] max-md:hidden"><a href="#css" class="rounded px-2 py-1 font-medium text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">CSS</a></li>
          <li class="flex items-center text-sm whitespace-nowrap before:mx-2 before:text-xs before:text-tnb08-edge before:content-['/']"><span aria-current="page" class="px-2 py-1 font-semibold text-tnb08-ink">Responsive Navbar</span></li>
        </ol>
      </nav>
      <span class="mx-5 hidden h-6 w-px shrink-0 bg-tnb08-edge lg:block" aria-hidden="true"></span>
      <ul class="hidden list-none items-center gap-0 overflow-x-auto [scrollbar-width:none] lg:flex">
        <li><a href="#overview" aria-current="page" class="block rounded-full px-3.5 py-1.5 text-[13px] font-semibold whitespace-nowrap text-tnb08-acc no-underline aria-[current=page]:bg-tnb08-acc/8">Overview</a></li>
        <li><a href="#install" class="block rounded-full px-3.5 py-1.5 text-[13px] font-medium whitespace-nowrap text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">Installation</a></li>
        <li><a href="#usage" class="block rounded-full px-3.5 py-1.5 text-[13px] font-medium whitespace-nowrap text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">Usage</a></li>
        <li><a href="#api" class="block rounded-full px-3.5 py-1.5 text-[13px] font-medium whitespace-nowrap text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">API</a></li>
        <li><a href="#examples" class="block rounded-full px-3.5 py-1.5 text-[13px] font-medium whitespace-nowrap text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">Examples</a></li>
      </ul>
      <div class="ml-auto flex shrink-0 items-center gap-2">
        <span class="hidden text-[13px] text-tnb08-mut sm:block">12 min read</span>
        <a href="#edit" class="hidden rounded-md border border-tnb08-edge px-3 py-1.5 text-[13px] font-semibold text-tnb08-ink no-underline transition-colors hover:bg-tnb08-hover sm:block">Edit page</a>
        <label for="tnb08-menu" class="flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 lg:hidden" aria-hidden="true">
          <span class="block h-0.5 w-5 rounded-sm bg-tnb08-ink transition-transform duration-300 group-has-checked:translate-y-2 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
          <span class="block h-0.5 w-5 rounded-sm bg-tnb08-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
          <span class="block h-0.5 w-5 rounded-sm bg-tnb08-ink transition-transform duration-300 group-has-checked:-translate-y-2 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
        </label>
      </div>
    </div>
    <div class="hidden border-t border-tnb08-edge px-5 py-2 max-lg:group-has-checked:grid">
      <a href="#overview" class="flex min-h-11 items-center rounded-md px-2 text-sm font-semibold text-tnb08-acc no-underline">Overview</a>
      <a href="#install" class="flex min-h-11 items-center rounded-md px-2 text-sm font-medium text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">Installation</a>
      <a href="#usage" class="flex min-h-11 items-center rounded-md px-2 text-sm font-medium text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">Usage</a>
      <a href="#api" class="flex min-h-11 items-center rounded-md px-2 text-sm font-medium text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">API</a>
      <a href="#examples" class="flex min-h-11 items-center rounded-md px-2 text-sm font-medium text-tnb08-mut no-underline transition-colors hover:bg-tnb08-hover hover:text-tnb08-ink">Examples</a>
    </div>
  </header>
  <main class="mx-auto grid max-w-3xl gap-6 px-5 py-12 md:px-8">
    <h1 class="text-4xl font-bold tracking-[-0.03em] text-tnb08-ink">Breadcrumb + Reading Progress</h1>
    <p class="text-lg leading-relaxed text-tnb08-mut">Scroll: the bar fills. The script sets <code class="rounded bg-tnb08-hover px-1.5 py-0.5 text-[0.9em]">--tnb08-read</code> from 0 to 1 and the fill is <code class="rounded bg-tnb08-hover px-1.5 py-0.5 text-[0.9em]">scale-x-[var(--tnb08-read)]</code> — no width writes, no layout per frame.</p>
    <p class="leading-relaxed text-tnb08-mut">The breadcrumb separators are generated by <code class="rounded bg-tnb08-hover px-1.5 py-0.5 text-[0.9em]">before:content-['/']</code> on every crumb but the first, so dropping a level cannot leave a stray slash behind.</p>
    <p class="leading-relaxed text-tnb08-mut">Below <code class="rounded bg-tnb08-hover px-1.5 py-0.5 text-[0.9em]">md</code> the middle crumbs hide themselves and the section pills move into the disclosure — the truncation rule lives on the crumbs, not in a media query far away.</p>
    <p class="leading-relaxed text-tnb08-mut">Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</p>
    <p class="leading-relaxed text-tnb08-mut">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    <p class="leading-relaxed text-tnb08-mut">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua, and the bar above should now be close to full.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb08-ink: #111110;
  --color-tnb08-ink: oklch(0.19 0.002 90);
  --color-tnb08-mut: #6f6a63;
  --color-tnb08-mut: oklch(0.53 0.01 85);
  --color-tnb08-edge: #e4e4e0;
  --color-tnb08-edge: oklch(0.91 0.003 90);
  --color-tnb08-track: #eeeeea;
  --color-tnb08-track: oklch(0.94 0.003 90);
  --color-tnb08-hover: #f4f4f2;
  --color-tnb08-hover: oklch(0.96 0.002 90);
  --color-tnb08-acc: #10b981;
  --color-tnb08-acc: oklch(0.68 0.16 165);
  --color-tnb08-acc2: #06d6a0;
  --color-tnb08-acc2: oklch(0.78 0.16 170);
  --font-tnb08-sans: 'IBM Plex Sans', system-ui, sans-serif;
}

.tnb-08 {
  width: 100%;
  min-height: 100svh;
}

.tnb-08 ::selection {
  background: var(--color-tnb08-acc);
  color: #fff;
}

.tnb-08 ul::-webkit-scrollbar {
  display: none;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tnb-08').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var ticking = false;
    function read() {
      ticking = false;
      var total = document.documentElement.scrollHeight - window.innerHeight;
      var pct = total > 0 ? Math.min(1, window.scrollY / total) : 0;
      root.style.setProperty('--tnb08-read', String(pct));
      var bar = root.querySelector('[role="progressbar"]');
      if (bar) bar.setAttribute('aria-valuenow', String(Math.round(pct * 100)));
    }
    function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(read); } }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    read();
  });
})();
```

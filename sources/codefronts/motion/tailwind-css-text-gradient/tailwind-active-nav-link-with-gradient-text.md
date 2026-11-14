---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-active-nav-link-with-gradient-text/"
title: "Tailwind Active Nav Link with Gradient Text"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "A dashboard header where the current page is styled entirely from aria-current=\"page\": a tinted pill, gradient label and a gradient underline that scales in."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Active Nav Link with Gradient Text
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-active-nav-link-with-gradient-text/

A dashboard header where the current page is styled entirely from aria-current="page": a tinted pill, gradient label and a gradient underline that scales in. The script only moves one attribute &mdash; every visual lives in aria-[current=page]: and group-aria-[current=page]: variants, so styling and accessibility can never disagree.
## HTML
```html
<section class="ttg-07 w-full min-h-svh bg-ttg07-bg font-ttg07-sans text-ttg07-ink" aria-label="Active navigation link gradient demo" data-ttg07>
  <header class="border-b border-ttg07-line bg-white">
    <div class="mx-auto flex h-16 max-w-5xl items-center gap-6 px-5">
      <a href="#" class="flex flex-none items-center gap-2 text-[17px] font-extrabold tracking-[-0.02em]"><span aria-hidden="true" class="grid size-7 place-items-center rounded-lg bg-linear-135 from-ttg07-a to-ttg07-b text-xs text-white">N</span>Nexus</a>
      <nav class="-mx-1 flex flex-1 gap-1 overflow-x-auto px-1 [scrollbar-width:none]" aria-label="Main">
        <a href="#" data-ttg07-link class="group relative inline-flex min-h-11 flex-none items-center rounded-lg px-3.5 text-[14.5px] font-medium text-ttg07-mut transition-colors after:absolute after:inset-x-3 after:-bottom-[10px] after:h-0.5 after:origin-center after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-ttg07-a after:to-ttg07-b after:transition-transform after:duration-300 hover:bg-ttg07-ink/5 hover:text-ttg07-ink focus-visible:outline-2 focus-visible:outline-ttg07-a aria-[current=page]:bg-ttg07-a/8 aria-[current=page]:font-semibold aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none"><span class="group-aria-[current=page]:bg-linear-to-r group-aria-[current=page]:from-ttg07-a group-aria-[current=page]:to-ttg07-b group-aria-[current=page]:bg-clip-text group-aria-[current=page]:text-transparent">Dashboard</span></a>
        <a href="#" data-ttg07-link aria-current="page" class="group relative inline-flex min-h-11 flex-none items-center rounded-lg px-3.5 text-[14.5px] font-medium text-ttg07-mut transition-colors after:absolute after:inset-x-3 after:-bottom-[10px] after:h-0.5 after:origin-center after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-ttg07-a after:to-ttg07-b after:transition-transform after:duration-300 hover:bg-ttg07-ink/5 hover:text-ttg07-ink focus-visible:outline-2 focus-visible:outline-ttg07-a aria-[current=page]:bg-ttg07-a/8 aria-[current=page]:font-semibold aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none"><span class="group-aria-[current=page]:bg-linear-to-r group-aria-[current=page]:from-ttg07-a group-aria-[current=page]:to-ttg07-b group-aria-[current=page]:bg-clip-text group-aria-[current=page]:text-transparent">Analytics</span></a>
        <a href="#" data-ttg07-link class="group relative inline-flex min-h-11 flex-none items-center rounded-lg px-3.5 text-[14.5px] font-medium text-ttg07-mut transition-colors after:absolute after:inset-x-3 after:-bottom-[10px] after:h-0.5 after:origin-center after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-ttg07-a after:to-ttg07-b after:transition-transform after:duration-300 hover:bg-ttg07-ink/5 hover:text-ttg07-ink focus-visible:outline-2 focus-visible:outline-ttg07-a aria-[current=page]:bg-ttg07-a/8 aria-[current=page]:font-semibold aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none"><span class="group-aria-[current=page]:bg-linear-to-r group-aria-[current=page]:from-ttg07-a group-aria-[current=page]:to-ttg07-b group-aria-[current=page]:bg-clip-text group-aria-[current=page]:text-transparent">Projects</span></a>
        <a href="#" data-ttg07-link class="group relative inline-flex min-h-11 flex-none items-center rounded-lg px-3.5 text-[14.5px] font-medium text-ttg07-mut transition-colors after:absolute after:inset-x-3 after:-bottom-[10px] after:h-0.5 after:origin-center after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-ttg07-a after:to-ttg07-b after:transition-transform after:duration-300 hover:bg-ttg07-ink/5 hover:text-ttg07-ink focus-visible:outline-2 focus-visible:outline-ttg07-a aria-[current=page]:bg-ttg07-a/8 aria-[current=page]:font-semibold aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none"><span class="group-aria-[current=page]:bg-linear-to-r group-aria-[current=page]:from-ttg07-a group-aria-[current=page]:to-ttg07-b group-aria-[current=page]:bg-clip-text group-aria-[current=page]:text-transparent">Settings</span></a>
      </nav>
      <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-linear-135 from-ttg07-a to-ttg07-b text-xs font-bold text-white ring-2 ring-white ring-offset-1 ring-offset-ttg07-line max-sm:hidden">AK</span>
    </div>
  </header>
  <main class="mx-auto max-w-5xl px-5 py-10">
    <h1 class="text-[28px] font-extrabold tracking-[-0.03em]"><span data-ttg07-page>Analytics</span> <span class="bg-linear-to-r from-ttg07-a to-ttg07-b bg-clip-text text-transparent">overview</span></h1>
    <p class="mt-1.5 text-[15px] text-ttg07-mut">Your performance at a glance for the last 30 days.</p>
    <dl class="mt-8 grid gap-4 sm:grid-cols-3">
      <div class="flex flex-col-reverse gap-1 rounded-2xl border border-ttg07-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)]"><dt class="text-[13px] text-ttg07-mut">Revenue</dt><dd class="text-[28px] font-bold tracking-tight tabular-nums">$124K</dd></div>
      <div class="flex flex-col-reverse gap-1 rounded-2xl border border-ttg07-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)]"><dt class="text-[13px] text-ttg07-mut">Sessions</dt><dd class="text-[28px] font-bold tracking-tight tabular-nums">8,432</dd></div>
      <div class="flex flex-col-reverse gap-1 rounded-2xl border border-ttg07-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)]"><dt class="text-[13px] text-ttg07-mut">Conversion</dt><dd class="text-[28px] font-bold tracking-tight tabular-nums">3.4%</dd></div>
    </dl>
    <p class="mt-6 text-[13px] text-ttg07-mut">Click any nav item — the script only moves <code class="rounded bg-ttg07-ink/5 px-1.5 py-0.5 text-ttg07-ink">aria-current</code>.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg07-bg: #f6f8fb;
  --color-ttg07-bg: oklch(0.977 0.005 255);
  --color-ttg07-ink: #0f1626;
  --color-ttg07-ink: oklch(0.2 0.03 260);
  --color-ttg07-mut: #556072;
  --color-ttg07-mut: oklch(0.48 0.03 260);
  --color-ttg07-line: #e2e7ef;
  --color-ttg07-line: oklch(0.925 0.01 260);
  --color-ttg07-a: #2f6cf0;
  --color-ttg07-a: oklch(0.57 0.2 262);
  --color-ttg07-b: #8a4cf0;
  --color-ttg07-b: oklch(0.57 0.23 295);
  --font-ttg07-sans: 'Geist', system-ui, sans-serif;
}

.ttg-07 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttg07]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const links = root.querySelectorAll('[data-ttg07-link]');
    const page = root.querySelector('[data-ttg07-page]');
    links.forEach((link) => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        links.forEach((l) => l.removeAttribute('aria-current'));
        link.setAttribute('aria-current', 'page');
        if (page) page.textContent = link.textContent.trim();
      });
    });
  });
})();
```

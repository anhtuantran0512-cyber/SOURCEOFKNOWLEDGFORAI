---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-navbar-link-hover-effects/"
title: "Tailwind Navbar Link Hover Effects — 5 Animated Styles"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "Five nav-link hover treatments in one header, side by side, so you compare them in context: a scale-x underline, a clip-up fill, a gradient sweep, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Navbar Link Hover Effects — 5 Animated Styles
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-navbar-link-hover-effects/

Five nav-link hover treatments in one header, side by side, so you compare them in context: a scale-x underline, a clip-up fill, a gradient sweep, a dual-layer label swap and a bracket reveal. Every one runs on transform and opacity only, and every one fires on focus-visible as well as hover.
## HTML
```html
<div class="thd-19 group/thd19 w-full min-h-svh bg-thd19-bg bg-[linear-gradient(transparent_calc(100%-1px),var(--color-thd19-line)_1px)] bg-size-[100%_28px] font-thd19-mono text-thd19-ink antialiased">
  <a href="#thd-19-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:bg-thd19-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-bold focus:text-thd19-bg">Skip to content</a>
  <header class="sticky top-0 z-40 border-b border-thd19-line bg-thd19-bg/90 backdrop-blur-md">
    <div class="mx-auto flex h-16 max-w-7xl items-center gap-6 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-19-main" class="flex items-center gap-1.5 whitespace-nowrap text-[15px] font-bold"><span aria-hidden="true" class="text-thd19-acc">&#9655;</span>phosphor<span class="text-thd19-mut">.sh</span><span aria-hidden="true" class="ml-0.5 inline-block h-4 w-2 animate-pulse bg-thd19-acc motion-reduce:animate-none"></span></a>
      <nav aria-label="Main" class="hidden md:block">
        <ul class="flex items-center gap-7 text-[13.5px]">
          <li><a href="#thd-19-main" aria-current="page" class="relative inline-block py-2 outline-none after:absolute after:inset-x-0 after:bottom-1 after:h-0.5 after:origin-right after:scale-x-0 after:bg-thd19-acc after:transition-transform after:duration-300 after:content-[''] hover:after:origin-left hover:after:scale-x-100 focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none">Overview</a></li>
          <li><a href="#thd-19-main" class="relative isolate inline-block px-2 py-2 outline-none transition-colors duration-300 before:absolute before:inset-0 before:-z-10 before:bg-thd19-acc before:transition-[clip-path] before:duration-300 before:ease-out before:content-[''] before:[clip-path:inset(100%_0_0)] hover:text-thd19-bg hover:before:[clip-path:inset(0)] focus-visible:text-thd19-bg focus-visible:before:[clip-path:inset(0)] motion-reduce:before:transition-none">Runtime</a></li>
          <li><a href="#thd-19-main" class="inline-block bg-[linear-gradient(90deg,var(--color-thd19-ink)_50%,var(--color-thd19-acc)_50%,#22d3ee)] bg-size-[200%_100%] bg-position-[0%_0] bg-clip-text py-2 text-transparent outline-none transition-[background-position] duration-500 hover:bg-position-[100%_0] focus-visible:bg-position-[100%_0] motion-reduce:transition-none forced-colors:text-[LinkText]">Pipelines</a></li>
          <li><a href="#thd-19-main" class="group/sw relative inline-block h-9 overflow-hidden py-2 leading-5 outline-none focus-visible:ring-1 focus-visible:ring-thd19-acc"><span class="block transition-transform duration-300 ease-[cubic-bezier(.7,0,.2,1)] group-hover/sw:-translate-y-[calc(100%+.5rem)] group-focus-visible/sw:-translate-y-[calc(100%+.5rem)] motion-reduce:transition-none">Registry</span><span aria-hidden="true" class="absolute left-0 top-full block text-thd19-acc transition-transform duration-300 ease-[cubic-bezier(.7,0,.2,1)] group-hover/sw:-translate-y-[calc(100%+.5rem)] group-focus-visible/sw:-translate-y-[calc(100%+.5rem)] motion-reduce:transition-none">Registry</span></a></li>
          <li><a href="#thd-19-main" class="relative inline-block py-2 outline-none before:absolute before:-left-3 before:text-thd19-acc before:opacity-0 before:transition before:duration-200 before:content-['['] after:absolute after:-right-3 after:text-thd19-acc after:opacity-0 after:transition after:duration-200 after:content-[']'] hover:before:-left-2.5 hover:before:opacity-100 hover:after:-right-2.5 hover:after:opacity-100 focus-visible:before:opacity-100 focus-visible:after:opacity-100 before:translate-x-2 after:-translate-x-2 hover:before:translate-x-0 hover:after:translate-x-0 focus-visible:before:translate-x-0 focus-visible:after:translate-x-0">Docs</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-2">
        <input id="thd-19-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-19-t" class="grid size-11 cursor-pointer place-items-center text-thd19-mut hover:text-thd19-acc peer-focus-visible/t:outline-1 peer-focus-visible/t:outline-thd19-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px] group-has-[#thd-19-t:checked]/thd19:hidden"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-19-t:checked]/thd19:block"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-19-main" class="hidden px-2 py-2 text-[13.5px] text-thd19-mut hover:text-thd19-ink sm:block">Log in</a>
        <a href="#thd-19-main" class="grid min-h-11 place-items-center border border-thd19-acc px-4 text-[13.5px] font-bold text-thd19-acc transition-colors hover:bg-thd19-acc hover:text-thd19-bg">$ install</a>
      </div>
    </div>
  </header>
  <main id="thd-19-main" class="mx-auto max-w-7xl px-[clamp(.75rem,3vw,1.5rem)] py-12">
    <p class="text-sm text-thd19-mut"><span class="text-thd19-acc">~/phosphor</span> $ cat effects.md</p>
    <h1 class="mt-3 max-w-[20ch] text-[clamp(1.8rem,5vw,3rem)] font-extrabold leading-[1.1] tracking-[-.03em]">Five hover effects. One header.</h1>
    <ol class="mt-6 grid max-w-3xl gap-2 text-sm">
      <li class="flex gap-3 border-l-2 border-thd19-acc bg-thd19-panel px-4 py-3"><span class="text-thd19-acc">01</span><span><strong>Overview</strong> &mdash; underline grows left, exits right (<code>origin</code> swap).</span></li>
      <li class="flex gap-3 border-l-2 border-thd19-acc bg-thd19-panel px-4 py-3"><span class="text-thd19-acc">02</span><span><strong>Runtime</strong> &mdash; fill rises from the baseline with <code>clip-path: inset()</code>.</span></li>
      <li class="flex gap-3 border-l-2 border-thd19-acc bg-thd19-panel px-4 py-3"><span class="text-thd19-acc">03</span><span><strong>Pipelines</strong> &mdash; gradient sweeps through clipped text.</span></li>
      <li class="flex gap-3 border-l-2 border-thd19-acc bg-thd19-panel px-4 py-3"><span class="text-thd19-acc">04</span><span><strong>Registry</strong> &mdash; label rolls up, accent copy rolls in.</span></li>
      <li class="flex gap-3 border-l-2 border-thd19-acc bg-thd19-panel px-4 py-3"><span class="text-thd19-acc">05</span><span><strong>Docs</strong> &mdash; brackets slide in around the word.</span></li>
    </ol>
    <div aria-hidden="true" class="h-[50svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd19-bg: var(--thd19-bg);
  --color-thd19-panel: var(--thd19-panel);
  --color-thd19-ink: var(--thd19-ink);
  --color-thd19-mut: var(--thd19-mut);
  --color-thd19-line: var(--thd19-line);
  --color-thd19-acc: var(--thd19-acc);
}

@theme {
  --font-thd19-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.thd-19 {
  width: 100%;
  min-height: 100svh;
  --thd19-bg: #07100b;
  --thd19-panel: #0c1a12;
  --thd19-ink: #d8f5e3;
  --thd19-mut: #8fb39e;
  --thd19-line: rgb(74 222 128 / 0.07);
  --thd19-acc: #4ade80;
}

.thd-19:has(#thd-19-t:checked) {
  --thd19-bg: #f3f8f4;
  --thd19-panel: #ffffff;
  --thd19-ink: #0b2415;
  --thd19-mut: #4a6555;
  --thd19-line: rgb(11 36 21 / 0.06);
  --thd19-acc: #15803d;
}
```

---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-header-github-star-button/"
title: "Tailwind Header with GitHub Star Button"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "The header every open-source project ships: wordmark with a version chip, a short docs nav, and a two-part star button linking to the repository."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Header with GitHub Star Button
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-header-github-star-button/

The header every open-source project ships: wordmark with a version chip, a short docs nav, and a two-part star button linking to the repository. Monochrome with a hard offset shadow — shadow-[4px_4px_0_var(--color-thd11-ink)] — that presses flat on click, and a count in tabular figures so it never nudges the layout.
## HTML
```html
<div class="thd-11 group/thd11 w-full min-h-svh bg-thd11-bg bg-[radial-gradient(var(--color-thd11-dot)_1px,transparent_1px)] bg-size-[22px_22px] font-thd11-sans text-thd11-ink antialiased">
  <a href="#thd-11-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:border-2 focus:border-thd11-ink focus:bg-thd11-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-bold">Skip to content</a>
  <header class="sticky top-0 z-40 border-b-2 border-thd11-ink bg-thd11-bg">
    <div class="mx-auto flex h-16 max-w-6xl items-center gap-3 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-11-main" class="flex items-baseline gap-1 font-thd11-mono text-lg font-bold tracking-tight">stackless<span class="text-thd11-mut">/ui</span></a>
      <span class="hidden border-2 border-thd11-ink bg-thd11-acc px-1.5 font-thd11-mono text-[11px] font-bold sm:inline">v2.0</span>
      <nav aria-label="Main" class="ml-4 hidden md:block">
        <ul class="flex items-center gap-1 text-[15px] font-medium">
          <li><a href="#thd-11-main" aria-current="page" class="border-2 border-transparent px-2.5 py-1.5 hover:border-thd11-ink aria-[current=page]:border-thd11-ink aria-[current=page]:bg-thd11-ink aria-[current=page]:text-thd11-bg">Docs</a></li>
          <li><a href="#thd-11-main" class="border-2 border-transparent px-2.5 py-1.5 hover:border-thd11-ink">Components</a></li>
          <li><a href="#thd-11-main" class="border-2 border-transparent px-2.5 py-1.5 hover:border-thd11-ink">Themes</a></li>
          <li><a href="#thd-11-main" class="border-2 border-transparent px-2.5 py-1.5 hover:border-thd11-ink">Blog</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-2">
        <input id="thd-11-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-11-t" class="grid size-11 cursor-pointer place-items-center border-2 border-transparent hover:border-thd11-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-offset-2 peer-focus-visible/t:outline-thd11-ink">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-11-t:checked]/thd11:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-11-t:checked]/thd11:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-11-main" class="hidden px-2 py-2 font-thd11-mono text-sm underline decoration-2 underline-offset-4 hover:bg-thd11-acc sm:block">Changelog</a>
        <a href="#thd-11-main" aria-label="Star stackless on GitHub, 12,400 stars" class="group/star flex min-h-11 items-stretch divide-x-2 divide-thd11-ink border-2 border-thd11-ink bg-thd11-bg font-thd11-mono text-sm font-bold shadow-[4px_4px_0_var(--color-thd11-ink)] transition-[translate,box-shadow] duration-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thd11-ink active:translate-x-1 active:translate-y-1 active:shadow-none">
          <span aria-hidden="true" class="flex items-center gap-2 px-3 transition-colors group-hover/star:bg-thd11-ink group-hover/star:text-thd11-bg group-focus-visible/star:bg-thd11-ink group-focus-visible/star:text-thd11-bg"><svg viewBox="0 0 24 24" fill="currentColor" class="size-4"><path d="M12 .5C5.7.5.5 5.7.5 12a11.5 11.5 0 0 0 7.9 10.9c.6.1.8-.3.8-.6v-2c-3.2.7-3.9-1.5-3.9-1.5-.5-1.3-1.3-1.7-1.3-1.7-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.6-.3-5.3-1.3-5.3-5.7 0-1.3.5-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.2 1.2a11 11 0 0 1 5.8 0c2.2-1.5 3.2-1.2 3.2-1.2.6 1.6.2 2.8.1 3.1.8.8 1.2 1.9 1.2 3.1 0 4.4-2.7 5.4-5.3 5.7.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A11.5 11.5 0 0 0 23.5 12C23.5 5.7 18.3.5 12 .5Z"/></svg><span class="hidden sm:inline">Star</span></span>
          <span aria-hidden="true" class="flex items-center gap-1.5 bg-thd11-acc px-3 tabular-nums text-black"><svg viewBox="0 0 24 24" fill="currentColor" class="size-3.5"><path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9L12 3.5Z"/></svg>12.4k</span>
        </a>
      </div>
    </div>
  </header>
  <main id="thd-11-main" class="mx-auto max-w-6xl px-[clamp(.75rem,3vw,1.5rem)] py-[clamp(3rem,9vw,6rem)]">
    <p class="inline-block border-2 border-thd11-ink bg-thd11-acc px-2 py-0.5 font-thd11-mono text-xs font-bold text-black">MIT &middot; 0 deps</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(2.4rem,7vw,4.6rem)] font-bold leading-[.95] tracking-[-.04em] text-balance">Headless components, no runtime.</h1>
    <p class="mt-5 max-w-[50ch] text-lg text-thd11-mut">Click the star button &mdash; it presses flat into the page. The count uses tabular figures, so 12.4k&rarr;12.5k never shifts the bar.</p>
    <pre class="mt-8 inline-block border-2 border-thd11-ink bg-thd11-bg px-4 py-3 font-thd11-mono text-sm shadow-[4px_4px_0_var(--color-thd11-ink)]"><code>npm i @stackless/ui</code></pre>
    <div aria-hidden="true" class="h-[60svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd11-bg: var(--thd11-bg);
  --color-thd11-ink: var(--thd11-ink);
  --color-thd11-mut: var(--thd11-mut);
  --color-thd11-dot: var(--thd11-dot);
  --color-thd11-acc: var(--thd11-acc);
}

@theme {
  --font-thd11-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thd11-mono: 'Space Mono', ui-monospace, monospace;
}

.thd-11 {
  width: 100%;
  min-height: 100svh;
  --thd11-bg: #fafaf7;
  --thd11-ink: #0d0d0d;
  --thd11-mut: #4a4a48;
  --thd11-dot: rgb(13 13 13 / 0.12);
  --thd11-acc: #d4ff3f;
}

.thd-11:has(#thd-11-t:checked) {
  --thd11-bg: #0d0d0d;
  --thd11-ink: #f2f2ee;
  --thd11-mut: #b0b0aa;
  --thd11-dot: rgb(242 242 238 / 0.1);
  --thd11-acc: #d4ff3f;
}
```

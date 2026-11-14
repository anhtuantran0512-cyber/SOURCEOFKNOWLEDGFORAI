---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-two-row-header-top-utility-bar/"
title: "Tailwind Two Row Header with Top Utility Bar"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "The double-decker enterprise header: a dense utility strip for support, docs, status, region, currency and language, then the primary bar with logo, main…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Two Row Header with Top Utility Bar
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-two-row-header-top-utility-bar/

The double-decker enterprise header: a dense utility strip for support, docs, status, region, currency and language, then the primary bar with logo, main nav, search and the demo CTA. Zero radius, sharp hairlines, ultra-compact spacing — the vocabulary banks, healthcare portals and B2B platforms use. Three pure-CSS switchers, and only the primary bar sticks.
## HTML
```html
<div class="thd-18 group/thd18 w-full min-h-svh bg-thd18-bg font-thd18-sans text-thd18-ink antialiased">
  <a href="#thd-18-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:bg-thd18-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <div class="relative z-50 border-b border-thd18-line bg-thd18-strip text-[12.5px]">
    <div class="mx-auto flex h-9 max-w-7xl items-center gap-3 px-[clamp(.75rem,3vw,1.5rem)]">
      <nav aria-label="Utility" class="hidden min-w-0 md:block">
        <ul class="flex items-center divide-x divide-thd18-line2">
          <li class="pr-3"><a href="#thd-18-main" class="text-thd18-mut hover:text-thd18-ink hover:underline">Support</a></li>
          <li class="px-3"><a href="#thd-18-main" class="text-thd18-mut hover:text-thd18-ink hover:underline">Documentation</a></li>
          <li class="px-3"><a href="#thd-18-main" class="inline-flex items-center gap-1.5 text-thd18-mut hover:text-thd18-ink hover:underline"><span aria-hidden="true" class="size-1.5 rounded-full bg-emerald-500"></span>Status</a></li>
          <li class="pl-3"><a href="#thd-18-main" class="text-thd18-mut hover:text-thd18-ink hover:underline">Partner portal</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center">
        <input id="thd-18-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-18-t" class="grid h-9 w-9 cursor-pointer place-items-center text-thd18-mut hover:bg-thd18-ink/5 hover:text-thd18-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:-outline-offset-2 peer-focus-visible/t:outline-thd18-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-4 group-has-[#thd-18-t:checked]/thd18:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-4 group-has-[#thd-18-t:checked]/thd18:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <div class="group/rg relative">
          <button type="button" aria-haspopup="menu" class="flex h-9 items-center gap-1 px-2.5 text-thd18-mut hover:bg-thd18-ink/5 hover:text-thd18-ink group-focus-within/rg:bg-thd18-ink/5"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true" class="size-3.5"><circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.6 2.5 14.4 0 17M12 3.5c-2.5 2.6-2.5 14.4 0 17"/></svg><span class="hidden sm:inline">United Kingdom</span><span class="sm:hidden">UK</span></button>
          <ul role="menu" aria-label="Region" class="invisible absolute right-0 top-full z-50 w-48 border border-thd18-line bg-thd18-panel py-1 opacity-0 shadow-lg transition-[opacity,visibility] duration-100 group-hover/rg:visible group-hover/rg:opacity-100 group-focus-within/rg:visible group-focus-within/rg:opacity-100">
            <li role="none"><a role="menuitem" href="#thd-18-main" aria-current="true" class="flex min-h-11 items-center justify-between px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5 aria-[current=true]:font-semibold aria-[current=true]:text-thd18-acc">United Kingdom <span aria-hidden="true">&#10003;</span></a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">Ireland</a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">Germany</a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">United States</a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">Singapore</a></li>
          </ul>
        </div>
        <div class="group/cur relative">
          <button type="button" aria-haspopup="menu" class="flex h-9 items-center px-2.5 tabular-nums text-thd18-mut hover:bg-thd18-ink/5 hover:text-thd18-ink group-focus-within/cur:bg-thd18-ink/5">GBP &pound;</button>
          <ul role="menu" aria-label="Currency" class="invisible absolute right-0 top-full z-50 w-36 border border-thd18-line bg-thd18-panel py-1 opacity-0 shadow-lg transition-[opacity,visibility] duration-100 group-hover/cur:visible group-hover/cur:opacity-100 group-focus-within/cur:visible group-focus-within/cur:opacity-100">
            <li role="none"><a role="menuitem" href="#thd-18-main" aria-current="true" class="flex min-h-11 items-center justify-between px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5 aria-[current=true]:font-semibold aria-[current=true]:text-thd18-acc">GBP &pound; <span aria-hidden="true">&#10003;</span></a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">EUR &euro;</a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">USD $</a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">SGD S$</a></li>
          </ul>
        </div>
        <div class="group/lang relative">
          <button type="button" aria-haspopup="menu" class="flex h-9 items-center px-2.5 text-thd18-mut hover:bg-thd18-ink/5 hover:text-thd18-ink group-focus-within/lang:bg-thd18-ink/5">EN</button>
          <ul role="menu" aria-label="Language" class="invisible absolute right-0 top-full z-50 w-40 border border-thd18-line bg-thd18-panel py-1 opacity-0 shadow-lg transition-[opacity,visibility] duration-100 group-hover/lang:visible group-hover/lang:opacity-100 group-focus-within/lang:visible group-focus-within/lang:opacity-100">
            <li role="none"><a role="menuitem" href="#thd-18-main" lang="en" aria-current="true" class="flex min-h-11 items-center justify-between px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5 aria-[current=true]:font-semibold aria-[current=true]:text-thd18-acc">English <span aria-hidden="true">&#10003;</span></a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" lang="de" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">Deutsch</a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" lang="fr" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">Fran&ccedil;ais</a></li>
            <li role="none"><a role="menuitem" href="#thd-18-main" lang="ja" class="flex min-h-11 items-center px-3 text-[13px] hover:bg-thd18-ink/5 focus-visible:bg-thd18-ink/5">&#26085;&#26412;&#35486;</a></li>
          </ul>
        </div>
        <a href="#thd-18-main" class="ml-1 flex h-9 items-center border-l border-thd18-line2 pl-3 font-semibold text-thd18-acc hover:underline">Sign in</a>
      </div>
    </div>
  </div>
  <header class="sticky top-0 z-40 border-b-2 border-thd18-ink bg-thd18-panel">
    <div class="mx-auto flex h-16 max-w-7xl items-center gap-6 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-18-main" class="flex items-center gap-2.5 leading-none"><span aria-hidden="true" class="grid size-8 place-items-center bg-thd18-acc font-extrabold text-white">C</span><span><span class="block text-[15px] font-extrabold uppercase tracking-[.06em]">Charter</span><span class="block text-[10px] font-semibold uppercase tracking-[.2em] text-thd18-mut">Financial Systems</span></span></a>
      <nav aria-label="Main" class="hidden lg:block">
        <ul class="flex h-16 items-stretch text-sm font-semibold">
          <li><a href="#thd-18-main" aria-current="page" class="flex h-full items-center border-b-[3px] border-transparent px-3.5 pt-[3px] hover:border-thd18-line2 aria-[current=page]:border-thd18-acc aria-[current=page]:text-thd18-acc">Platform</a></li>
          <li><a href="#thd-18-main" class="flex h-full items-center border-b-[3px] border-transparent px-3.5 pt-[3px] hover:border-thd18-line2">Industries</a></li>
          <li><a href="#thd-18-main" class="flex h-full items-center border-b-[3px] border-transparent px-3.5 pt-[3px] hover:border-thd18-line2">Compliance</a></li>
          <li><a href="#thd-18-main" class="flex h-full items-center border-b-[3px] border-transparent px-3.5 pt-[3px] hover:border-thd18-line2">Resources</a></li>
          <li><a href="#thd-18-main" class="flex h-full items-center border-b-[3px] border-transparent px-3.5 pt-[3px] hover:border-thd18-line2">Company</a></li>
        </ul>
      </nav>
      <label class="ml-auto hidden min-h-10 w-52 items-center gap-2 border border-thd18-line2 bg-thd18-bg px-3 text-sm focus-within:border-thd18-acc focus-within:outline-2 focus-within:outline-thd18-acc/30 md:flex">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true" class="size-4 flex-none text-thd18-mut"><circle cx="11" cy="11" r="6.4"/><path d="m15.8 15.8 5.2 5.2"/></svg>
        <input type="search" placeholder="Search Charter" aria-label="Search" class="min-w-0 flex-1 bg-transparent outline-none placeholder:text-thd18-mut">
      </label>
      <a href="#thd-18-main" class="ml-auto grid min-h-11 place-items-center whitespace-nowrap bg-thd18-acc px-5 text-sm font-bold text-white transition-colors hover:bg-thd18-ink md:ml-0">Request a demo</a>
    </div>
  </header>
  <main id="thd-18-main" class="mx-auto max-w-7xl px-[clamp(.75rem,3vw,1.5rem)] py-12">
    <p class="text-xs font-bold uppercase tracking-[.18em] text-thd18-acc">Treasury &middot; Payments &middot; Risk</p>
    <h1 class="mt-3 max-w-[20ch] text-[clamp(2rem,5.5vw,3.6rem)] font-extrabold leading-[1.05] tracking-[-.02em]">Core banking infrastructure, audited to the line.</h1>
    <p class="mt-4 max-w-[56ch] text-thd18-mut">Scroll: the utility strip leaves, the primary bar stays. Hover or Tab to region, currency and language &mdash; each is a pure-CSS menu.</p>
    <div aria-hidden="true" class="h-[70svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd18-bg: var(--thd18-bg);
  --color-thd18-strip: var(--thd18-strip);
  --color-thd18-panel: var(--thd18-panel);
  --color-thd18-ink: var(--thd18-ink);
  --color-thd18-mut: var(--thd18-mut);
  --color-thd18-line: var(--thd18-line);
  --color-thd18-line2: var(--thd18-line2);
  --color-thd18-acc: var(--thd18-acc);
}

@theme {
  --font-thd18-sans: 'Public Sans', system-ui, sans-serif;
}

.thd-18 {
  width: 100%;
  min-height: 100svh;
  --thd18-bg: #f3f5f8;
  --thd18-strip: #e9edf2;
  --thd18-panel: #ffffff;
  --thd18-ink: #0b1a2e;
  --thd18-mut: #4c5b70;
  --thd18-line: #d6dde7;
  --thd18-line2: #b3bfcf;
  --thd18-acc: #0a4bb8;
}

.thd-18:has(#thd-18-t:checked) {
  --thd18-bg: #070e1a;
  --thd18-strip: #0b1424;
  --thd18-panel: #0f1a2d;
  --thd18-ink: #e6edf7;
  --thd18-mut: #9aa9bf;
  --thd18-line: #1e2b43;
  --thd18-line2: #34445f;
  --thd18-acc: #5b9bff;
}
```

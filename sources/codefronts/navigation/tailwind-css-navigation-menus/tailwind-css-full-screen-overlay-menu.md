---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-full-screen-overlay-menu/"
title: "Tailwind CSS Full-Screen Overlay Menu"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A cinematic, portfolio-grade overlay: the menu wipes down with a clip-path reveal, giant links rise out of masks one after another, and hovering one link…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Full-Screen Overlay Menu
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-full-screen-overlay-menu/

A cinematic, portfolio-grade overlay: the menu wipes down with a clip-path reveal, giant links rise out of masks one after another, and hovering one link dims the rest. A side column carries contact details and socials. Everything replays on every open because it is built from transitions. Zero JavaScript.
## HTML
```html
<div class="tnv-05 group/root min-h-svh w-full bg-tnv05-bg font-tnv05-sans text-tnv05-ink antialiased selection:bg-tnv05-acc selection:text-white">
  <input type="checkbox" id="tnv05-toggle" class="sr-only" aria-controls="tnv05-overlay">
  <header class="fixed inset-x-0 top-0 z-50 flex items-center justify-between px-6 py-6 sm:px-10">
    <a href="#" class="text-2xl font-extrabold tracking-[-0.04em]">Vol<span class="text-tnv05-acc">ta</span></a>
    <label for="tnv05-toggle" class="group/btn flex h-11 cursor-pointer items-center gap-3 rounded-full border border-white/10 bg-white/[0.06] pr-2 pl-4 text-xs font-bold tracking-[0.14em] uppercase backdrop-blur-md transition-colors select-none hover:bg-white/10 group-has-[#tnv05-toggle:focus-visible]/root:ring-2 group-has-[#tnv05-toggle:focus-visible]/root:ring-tnv05-acc">
      <span class="grid"><span class="col-start-1 row-start-1 transition-opacity group-has-checked/root:opacity-0">Menu</span><span class="col-start-1 row-start-1 opacity-0 transition-opacity group-has-checked/root:opacity-100">Close</span></span>
      <span class="grid size-8 place-items-center rounded-full bg-tnv05-ink text-tnv05-bg"><span class="grid gap-1"><span class="block h-0.5 w-3.5 rounded-full bg-current transition-[translate,rotate] duration-300 group-has-checked/root:translate-y-[3px] group-has-checked/root:rotate-45"></span><span class="block h-0.5 w-3.5 rounded-full bg-current transition-[translate,rotate] duration-300 group-has-checked/root:-translate-y-[3px] group-has-checked/root:-rotate-45"></span></span></span>
    </label>
  </header>
  <div id="tnv05-overlay" role="dialog" aria-label="Site menu" class="invisible fixed inset-0 z-40 grid overflow-y-auto bg-tnv05-bg bg-[radial-gradient(50%_50%_at_90%_100%,var(--color-tnv05-glow),transparent)] [clip-path:inset(0_0_100%_0)] transition-[clip-path,visibility] duration-[650ms] ease-[cubic-bezier(.77,0,.175,1)] group-has-checked/root:visible group-has-checked/root:[clip-path:inset(0)] motion-reduce:transition-none">
    <div class="mx-auto grid w-full max-w-6xl content-center gap-12 px-6 pt-28 pb-12 sm:px-10 lg:grid-cols-[1fr_16rem] lg:items-end">
      <nav aria-label="Primary">
        <ul class="group/list">
          <li class="overflow-hidden"><a href="#" style="--i:1" class="group/l inline-flex translate-y-full items-start gap-4 py-1 text-[clamp(2.75rem,8vw,5.75rem)] leading-[1.02] font-extrabold tracking-[-0.045em] text-white outline-none transition-[translate,color] delay-[calc(var(--i)*70ms_+_220ms)] duration-700 ease-[cubic-bezier(.23,1,.32,1)] group-hover/list:text-white/25 group-has-checked/root:translate-y-0 hover:text-white! focus-visible:text-tnv05-acc! motion-reduce:transition-none"><span class="mt-[0.6em] font-tnv05-mono text-xs font-medium tracking-wider text-tnv05-acc opacity-0 transition-opacity group-hover/l:opacity-100">01</span>Work</a></li>
          <li class="overflow-hidden"><a href="#" style="--i:2" class="group/l inline-flex translate-y-full items-start gap-4 py-1 text-[clamp(2.75rem,8vw,5.75rem)] leading-[1.02] font-extrabold tracking-[-0.045em] text-white outline-none transition-[translate,color] delay-[calc(var(--i)*70ms_+_220ms)] duration-700 ease-[cubic-bezier(.23,1,.32,1)] group-hover/list:text-white/25 group-has-checked/root:translate-y-0 hover:text-white! focus-visible:text-tnv05-acc! motion-reduce:transition-none"><span class="mt-[0.6em] font-tnv05-mono text-xs font-medium tracking-wider text-tnv05-acc opacity-0 transition-opacity group-hover/l:opacity-100">02</span>Studio</a></li>
          <li class="overflow-hidden"><a href="#" style="--i:3" class="group/l inline-flex translate-y-full items-start gap-4 py-1 text-[clamp(2.75rem,8vw,5.75rem)] leading-[1.02] font-extrabold tracking-[-0.045em] text-white outline-none transition-[translate,color] delay-[calc(var(--i)*70ms_+_220ms)] duration-700 ease-[cubic-bezier(.23,1,.32,1)] group-hover/list:text-white/25 group-has-checked/root:translate-y-0 hover:text-white! focus-visible:text-tnv05-acc! motion-reduce:transition-none"><span class="mt-[0.6em] font-tnv05-mono text-xs font-medium tracking-wider text-tnv05-acc opacity-0 transition-opacity group-hover/l:opacity-100">03</span>Services</a></li>
          <li class="overflow-hidden"><a href="#" style="--i:4" class="group/l inline-flex translate-y-full items-start gap-4 py-1 text-[clamp(2.75rem,8vw,5.75rem)] leading-[1.02] font-extrabold tracking-[-0.045em] text-white outline-none transition-[translate,color] delay-[calc(var(--i)*70ms_+_220ms)] duration-700 ease-[cubic-bezier(.23,1,.32,1)] group-hover/list:text-white/25 group-has-checked/root:translate-y-0 hover:text-white! focus-visible:text-tnv05-acc! motion-reduce:transition-none"><span class="mt-[0.6em] font-tnv05-mono text-xs font-medium tracking-wider text-tnv05-acc opacity-0 transition-opacity group-hover/l:opacity-100">04</span>Journal</a></li>
          <li class="overflow-hidden"><a href="#" style="--i:5" class="group/l inline-flex translate-y-full items-start gap-4 py-1 text-[clamp(2.75rem,8vw,5.75rem)] leading-[1.02] font-extrabold tracking-[-0.045em] text-white outline-none transition-[translate,color] delay-[calc(var(--i)*70ms_+_220ms)] duration-700 ease-[cubic-bezier(.23,1,.32,1)] group-hover/list:text-white/25 group-has-checked/root:translate-y-0 hover:text-white! focus-visible:text-tnv05-acc! motion-reduce:transition-none"><span class="mt-[0.6em] font-tnv05-mono text-xs font-medium tracking-wider text-tnv05-acc opacity-0 transition-opacity group-hover/l:opacity-100">05</span>Contact</a></li>
        </ul>
      </nav>
      <div class="grid translate-y-4 gap-6 border-t border-white/10 pt-6 text-sm opacity-0 transition-[translate,opacity] delay-[600ms] duration-700 group-has-checked/root:translate-y-0 group-has-checked/root:opacity-100 motion-reduce:transition-none lg:border-t-0 lg:border-l lg:pt-0 lg:pl-8">
        <div><p class="font-tnv05-mono text-[11px] tracking-wider text-tnv05-mut uppercase">New business</p><a href="#" class="mt-1 block font-semibold underline-offset-4 hover:underline">[email protected]</a></div>
        <div class="flex flex-wrap gap-x-4 gap-y-2 font-semibold text-tnv05-mut [&_a]:transition-colors [&_a:hover]:text-white"><a href="#">Instagram</a><a href="#">Dribbble</a><a href="#">LinkedIn</a><a href="#">X</a></div>
        <a href="#" class="inline-flex min-h-12 w-fit items-center gap-2 rounded-full bg-tnv05-acc px-6 font-bold text-white shadow-[0_10px_40px_-10px_var(--color-tnv05-acc)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Start a project<svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
      </div>
    </div>
  </div>
  <main class="grid min-h-svh place-items-center px-6 py-28 text-center [&_code]:rounded [&_code]:bg-white/[0.08] [&_code]:px-1.5 [&_code]:font-tnv05-mono [&_code]:text-[0.8em]">
    <div>
      <h1 class="text-[clamp(3rem,10vw,7rem)] leading-[0.95] font-extrabold tracking-[-0.055em]">Design <span class="bg-linear-135 from-tnv05-acc to-tnv05-acc2 bg-clip-text text-transparent">beyond</span><br>the ordinary</h1>
      <p class="mx-auto mt-6 max-w-md text-[17px]/[1.65] text-tnv05-mut text-pretty">Open the menu. It wipes in with <code>clip-path</code>, the links rise from masks on a stagger, and hovering one dims the rest. Close and reopen: it all replays.</p>
    </div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv05-bg: #09090b;
  --color-tnv05-bg: oklch(0.141 0.005 286);
  --color-tnv05-glow: #d946ef2e;
  --color-tnv05-glow: oklch(0.667 0.295 322 / 0.18);
  --color-tnv05-ink: #fafafa;
  --color-tnv05-ink: oklch(0.985 0 0);
  --color-tnv05-mut: #a1a1aa;
  --color-tnv05-mut: oklch(0.705 0.015 286);
  --color-tnv05-acc: #d946ef;
  --color-tnv05-acc: oklch(0.667 0.295 322);
  --color-tnv05-acc2: #e879f9;
  --color-tnv05-acc2: oklch(0.74 0.238 322);
  --font-tnv05-sans: 'Syne', system-ui, sans-serif;
  --font-tnv05-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tnv-05 {
  width: 100%;
  min-height: 100svh;
}
```

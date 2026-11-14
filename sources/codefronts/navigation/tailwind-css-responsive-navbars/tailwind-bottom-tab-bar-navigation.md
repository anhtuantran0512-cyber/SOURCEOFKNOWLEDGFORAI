---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-bottom-tab-bar-navigation/"
title: "Tailwind Bottom Tab Bar Navigation"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "Desktop gets a conventional top bar; phones get an iOS-style bottom tab bar with a lifted centre action."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Bottom Tab Bar Navigation
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-bottom-tab-bar-navigation/

Desktop gets a conventional top bar; phones get an iOS-style bottom tab bar with a lifted centre action. The pair is one component: hidden md:flex on the top nav, md:hidden on the tab bar, and pb-[env(safe-area-inset-bottom)] so the home indicator never covers a tab.
## HTML
```html
<div class="tnb-10 w-full min-h-svh bg-tnb10-page font-tnb10-sans text-tnb10-ink" aria-label="Bottom tab bar navigation demo">
  <nav class="hidden h-16 items-center gap-6 border-b border-tnb10-edge bg-white px-8 shadow-[0_1px_3px_oklch(0_0_0/0.05)] md:flex" aria-label="Primary">
    <a href="#home" class="shrink-0 text-xl font-extrabold tracking-[-0.02em] text-tnb10-ink no-underline">Pulse<span class="text-tnb10-acc">.</span></a>
    <ul class="flex flex-1 list-none items-center gap-0">
      <li><a href="#home" aria-current="page" class="flex items-center gap-1.5 rounded-lg px-3.5 py-2 text-sm font-bold text-tnb10-acc no-underline aria-[current=page]:bg-tnb10-tint"><span aria-hidden="true">&#127968;</span>Home</a></li>
      <li><a href="#analytics" class="flex items-center gap-1.5 rounded-lg px-3.5 py-2 text-sm font-bold text-tnb10-mut no-underline transition-colors duration-150 hover:bg-tnb10-tint hover:text-tnb10-acc"><span aria-hidden="true">&#128202;</span>Analytics</a></li>
      <li><a href="#messages" class="flex items-center gap-1.5 rounded-lg px-3.5 py-2 text-sm font-bold text-tnb10-mut no-underline transition-colors duration-150 hover:bg-tnb10-tint hover:text-tnb10-acc"><span aria-hidden="true">&#128172;</span>Messages</a></li>
      <li><a href="#files" class="flex items-center gap-1.5 rounded-lg px-3.5 py-2 text-sm font-bold text-tnb10-mut no-underline transition-colors duration-150 hover:bg-tnb10-tint hover:text-tnb10-acc"><span aria-hidden="true">&#128193;</span>Files</a></li>
      <li><a href="#profile" class="flex items-center gap-1.5 rounded-lg px-3.5 py-2 text-sm font-bold text-tnb10-mut no-underline transition-colors duration-150 hover:bg-tnb10-tint hover:text-tnb10-acc"><span aria-hidden="true">&#128100;</span>Profile</a></li>
    </ul>
    <a href="#upgrade" class="ml-auto shrink-0 rounded-lg bg-tnb10-acc px-4 py-2 text-sm font-bold text-white no-underline transition-[background,translate] duration-200 hover:-translate-y-px hover:bg-tnb10-accdark motion-reduce:transition-none motion-reduce:hover:translate-y-0">Upgrade plan</a>
  </nav>
  <nav class="fixed inset-x-0 bottom-0 z-200 border-t border-tnb10-edge bg-white pb-[env(safe-area-inset-bottom)] shadow-[0_-4px_20px_oklch(0_0_0/0.07)] md:hidden" aria-label="Primary">
    <ul class="flex list-none items-stretch px-2">
      <li class="flex-1"><a href="#home" aria-current="page" class="flex min-h-14 flex-col items-center justify-center gap-0.5 rounded-lg text-[11px] font-bold text-tnb10-mut no-underline transition-colors duration-200 aria-[current=page]:text-tnb10-acc"><span class="grid h-7 w-9 place-items-center rounded-full text-xl transition-[background,transform] duration-200 group-hover:bg-tnb10-hover aria-[current=page]:bg-tnb10-tint" aria-hidden="true">&#127968;</span>Home</a></li>
      <li class="flex-1"><a href="#stats" class="relative flex min-h-14 flex-col items-center justify-center gap-0.5 rounded-lg text-[11px] font-bold text-tnb10-mut no-underline transition-colors duration-200 hover:text-tnb10-ink"><span class="grid h-7 w-9 place-items-center rounded-full text-xl" aria-hidden="true">&#128202;</span><span class="absolute top-1.5 right-[calc(50%-22px)] min-w-4 rounded-full bg-tnb10-danger px-1.5 text-center text-[10px] leading-4 font-extrabold text-white ring-2 ring-white">2</span>Stats</a></li>
      <li class="flex-1"><a href="#new" class="flex min-h-14 flex-col items-center justify-center gap-0.5 rounded-lg text-[11px] font-bold text-tnb10-acc no-underline"><span class="grid h-10 w-11 -translate-y-2 place-items-center rounded-2xl bg-linear-[135deg,var(--color-tnb10-acc),var(--color-tnb10-acc2)] text-2xl text-white shadow-[0_4px_12px_oklch(0.59_0.2_278/0.45)] transition-transform duration-200 hover:-translate-y-2.5 hover:scale-105 motion-reduce:transition-none" aria-hidden="true">&#65291;</span>New</a></li>
      <li class="flex-1"><a href="#chat" class="relative flex min-h-14 flex-col items-center justify-center gap-0.5 rounded-lg text-[11px] font-bold text-tnb10-mut no-underline transition-colors duration-200 hover:text-tnb10-ink"><span class="grid h-7 w-9 place-items-center rounded-full text-xl" aria-hidden="true">&#128172;</span><span class="absolute top-1.5 right-[calc(50%-22px)] min-w-4 rounded-full bg-tnb10-danger px-1.5 text-center text-[10px] leading-4 font-extrabold text-white ring-2 ring-white">5</span>Chat</a></li>
      <li class="flex-1"><a href="#profile" class="flex min-h-14 flex-col items-center justify-center gap-0.5 rounded-lg text-[11px] font-bold text-tnb10-mut no-underline transition-colors duration-200 hover:text-tnb10-ink"><span class="grid h-7 w-9 place-items-center rounded-full text-xl" aria-hidden="true">&#128100;</span>Profile</a></li>
    </ul>
  </nav>
  <main class="mx-auto max-w-3xl px-5 pt-10 pb-28 md:px-8 md:pb-16">
    <h1 class="mb-4 text-3xl font-extrabold tracking-[-0.03em] text-tnb10-ink md:text-4xl">Bottom Tab Bar Navigation</h1>
    <p class="text-lg leading-relaxed text-tnb10-mut">Narrow the frame: the top bar leaves and the thumb bar arrives, centre action lifted out of the strip. The bottom inset is <code class="rounded bg-tnb10-tint px-1.5 py-0.5 text-[0.9em] text-tnb10-acc">pb-[env(safe-area-inset-bottom)]</code>, which is zero on hardware that has no notch.</p>
    <div class="mt-8 grid gap-4 sm:grid-cols-2">
      <div class="rounded-2xl border border-tnb10-edge bg-white p-5 text-sm text-tnb10-mut">Five tabs maximum — beyond that, labels truncate and the bar stops being scannable.</div>
      <div class="rounded-2xl border border-tnb10-edge bg-white p-5 text-sm text-tnb10-mut">Badges use <code>ring-2 ring-white</code>, so retinting the bar does not orphan a white border.</div>
    </div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb10-page: #f7f7fb;
  --color-tnb10-page: oklch(0.98 0.004 280);
  --color-tnb10-ink: #1e1b4b;
  --color-tnb10-ink: oklch(0.28 0.08 280);
  --color-tnb10-mut: #8a8fa3;
  --color-tnb10-mut: oklch(0.65 0.02 275);
  --color-tnb10-edge: #e5e7eb;
  --color-tnb10-edge: oklch(0.91 0.005 265);
  --color-tnb10-hover: #f3f4f6;
  --color-tnb10-hover: oklch(0.96 0.003 265);
  --color-tnb10-tint: #eef2ff;
  --color-tnb10-tint: oklch(0.95 0.02 275);
  --color-tnb10-acc: #6366f1;
  --color-tnb10-acc: oklch(0.59 0.2 278);
  --color-tnb10-acc2: #8b5cf6;
  --color-tnb10-acc2: oklch(0.63 0.22 295);
  --color-tnb10-accdark: #4f46e5;
  --color-tnb10-accdark: oklch(0.53 0.22 278);
  --color-tnb10-danger: #ef4444;
  --color-tnb10-danger: oklch(0.63 0.22 25);
  --font-tnb10-sans: 'Nunito', system-ui, sans-serif;
}

.tnb-10 {
  width: 100%;
  min-height: 100svh;
}

.tnb-10 ::selection {
  background: var(--color-tnb10-acc);
  color: #fff;
}
```

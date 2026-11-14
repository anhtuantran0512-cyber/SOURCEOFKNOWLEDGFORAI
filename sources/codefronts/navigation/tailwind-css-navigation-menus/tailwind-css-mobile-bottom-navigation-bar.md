---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-mobile-bottom-navigation-bar/"
title: "Tailwind CSS Mobile Bottom Navigation Bar with Animated Icons"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "An app-style floating dock: five icons, and the active one expands into a tinted pill that reveals its label, each tab in its own colour."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Mobile Bottom Navigation Bar with Animated Icons
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-mobile-bottom-navigation-bar/

An app-style floating dock: five icons, and the active one expands into a tinted pill that reveals its label, each tab in its own colour. Icons spring on selection, a Messages badge shows until you open Messages, and the page above swaps with a starting: fade. Radios behind the scenes mean arrow keys work. Zero JavaScript.
## HTML
```html
<div class="tnv-11 group/root flex min-h-svh w-full flex-col bg-tnv11-bg font-tnv11-sans text-tnv11-ink antialiased selection:bg-rose-500 selection:text-white">
  <input type="radio" name="tnv11" id="tnv11-t1" class="sr-only" aria-label="Home" checked><input type="radio" name="tnv11" id="tnv11-t2" class="sr-only" aria-label="Messages"><input type="radio" name="tnv11" id="tnv11-t3" class="sr-only" aria-label="Explore"><input type="radio" name="tnv11" id="tnv11-t4" class="sr-only" aria-label="Saved"><input type="radio" name="tnv11" id="tnv11-t5" class="sr-only" aria-label="Profile">
  <header class="flex h-16 items-center justify-between border-b border-white/[0.07] bg-tnv11-surface px-6 sm:px-10">
    <span class="text-lg font-bold tracking-[-0.01em]">Nova<span class="text-rose-400">App</span></span>
    <span class="grid size-9 place-items-center rounded-full bg-linear-135 from-violet-500 to-rose-500 text-xs font-bold">AK</span>
  </header>
  <main class="grid flex-1 place-items-center px-6 pt-14 pb-40 text-center [&_code]:rounded [&_code]:bg-white/[0.08] [&_code]:px-1.5 [&_code]:font-tnv11-mono [&_code]:text-[0.85em] [&>section]:hidden [&>section]:max-w-sm [&>section]:flex-col [&>section]:items-center [&>section]:gap-4 [&>section]:transition-[opacity,translate] [&>section]:duration-300 [&>section]:starting:translate-y-2 [&>section]:starting:opacity-0 [&_h2]:text-3xl [&_h2]:font-bold [&_h2]:tracking-[-0.02em] [&_p]:text-[15px]/[1.65] [&_p]:text-tnv11-mut [&_[data-ic]]:mb-2 [&_[data-ic]]:grid [&_[data-ic]]:size-[72px] [&_[data-ic]]:place-items-center [&_[data-ic]]:rounded-[22px] [&_[data-ic]_svg]:size-8">
    <section class="group-has-[#tnv11-t1:checked]/root:flex"><span data-ic class="bg-rose-500/12 text-rose-400"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><path d="M9 22V12h6v10"/></svg></span><h2>Home</h2><p>Your personalised feed. The active tab expands into a labelled pill and its icon springs with <code>scale-110</code>.</p></section>
    <section class="group-has-[#tnv11-t2:checked]/root:flex"><span data-ic class="bg-cyan-500/12 text-cyan-400"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></span><h2>Messages</h2><p>3 unread conversations. The badge on the dock disappears now that you've opened this tab.</p></section>
    <section class="group-has-[#tnv11-t3:checked]/root:flex"><span data-ic class="bg-emerald-500/12 text-emerald-400"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg></span><h2>Explore</h2><p>Trending content. The search icon tilts as it activates, a small touch of personality per tab.</p></section>
    <section class="group-has-[#tnv11-t4:checked]/root:flex"><span data-ic class="bg-amber-500/12 text-amber-400"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 000-7.78z"/></svg></span><h2>Saved</h2><p>Everything you've bookmarked. Each tab owns a colour, so you always know where you are.</p></section>
    <section class="group-has-[#tnv11-t5:checked]/root:flex"><span data-ic class="bg-violet-500/12 text-violet-400"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></span><h2>Profile</h2><p>Your account and settings. Use the arrow keys on the dock: it's a real radio group.</p></section>
  </main>
  <nav aria-label="App" class="fixed bottom-6 left-1/2 z-20 flex -translate-x-1/2 items-center gap-1 rounded-full border border-white/[0.08] bg-tnv11-surface/85 p-2 shadow-[0_16px_40px_-8px_rgb(0_0_0/0.6)] backdrop-blur-xl group-has-[input:focus-visible]/root:ring-2 group-has-[input:focus-visible]/root:ring-white/40 [&_label]:flex [&_label]:h-12 [&_label]:cursor-pointer [&_label]:items-center [&_label]:gap-2 [&_label]:rounded-full [&_label]:px-3.5 [&_label]:text-tnv11-mut [&_label]:transition-[background-color,color] [&_label]:duration-300 [&_label]:select-none [&_label:hover]:text-white [&_svg]:size-[22px] [&_svg]:transition-[scale,rotate] [&_svg]:duration-300 [&_svg]:ease-[cubic-bezier(.34,1.56,.64,1)] [&_[data-t]]:max-w-0 [&_[data-t]]:overflow-hidden [&_[data-t]]:text-[13px] [&_[data-t]]:font-bold [&_[data-t]]:whitespace-nowrap [&_[data-t]]:opacity-0 [&_[data-t]]:transition-[max-width,opacity] [&_[data-t]]:duration-300 motion-reduce:[&_*]:transition-none">
    <label for="tnv11-t1" class="group-has-[#tnv11-t1:checked]/root:bg-rose-500/15 group-has-[#tnv11-t1:checked]/root:text-rose-400 group-has-[#tnv11-t1:checked]/root:[&_svg]:scale-110 group-has-[#tnv11-t1:checked]/root:[&_[data-t]]:max-w-24 group-has-[#tnv11-t1:checked]/root:[&_[data-t]]:opacity-100"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><path d="M9 22V12h6v10"/></svg><span data-t>Home</span></label>
    <label for="tnv11-t2" class="relative group-has-[#tnv11-t2:checked]/root:bg-cyan-500/15 group-has-[#tnv11-t2:checked]/root:text-cyan-400 group-has-[#tnv11-t2:checked]/root:[&_svg]:scale-110 group-has-[#tnv11-t2:checked]/root:[&_[data-t]]:max-w-24 group-has-[#tnv11-t2:checked]/root:[&_[data-t]]:opacity-100"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg><span data-t>Messages</span><span aria-label="3 unread" class="absolute top-1.5 left-7 grid size-[18px] place-items-center rounded-full border-2 border-tnv11-surface bg-rose-500 text-[10px] font-bold text-white transition-[scale] duration-300 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-[#tnv11-t2:checked]/root:scale-0">3</span></label>
    <label for="tnv11-t3" class="group-has-[#tnv11-t3:checked]/root:bg-emerald-500/15 group-has-[#tnv11-t3:checked]/root:text-emerald-400 group-has-[#tnv11-t3:checked]/root:[&_svg]:scale-110 group-has-[#tnv11-t3:checked]/root:[&_svg]:-rotate-12 group-has-[#tnv11-t3:checked]/root:[&_[data-t]]:max-w-24 group-has-[#tnv11-t3:checked]/root:[&_[data-t]]:opacity-100"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg><span data-t>Explore</span></label>
    <label for="tnv11-t4" class="group-has-[#tnv11-t4:checked]/root:bg-amber-500/15 group-has-[#tnv11-t4:checked]/root:text-amber-400 group-has-[#tnv11-t4:checked]/root:[&_svg]:scale-110 group-has-[#tnv11-t4:checked]/root:[&_svg]:fill-current group-has-[#tnv11-t4:checked]/root:[&_[data-t]]:max-w-24 group-has-[#tnv11-t4:checked]/root:[&_[data-t]]:opacity-100"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 000-7.78z"/></svg><span data-t>Saved</span></label>
    <label for="tnv11-t5" class="group-has-[#tnv11-t5:checked]/root:bg-violet-500/15 group-has-[#tnv11-t5:checked]/root:text-violet-400 group-has-[#tnv11-t5:checked]/root:[&_svg]:scale-110 group-has-[#tnv11-t5:checked]/root:[&_[data-t]]:max-w-24 group-has-[#tnv11-t5:checked]/root:[&_[data-t]]:opacity-100"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg><span data-t>Profile</span></label>
  </nav>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv11-bg: #0f0f13;
  --color-tnv11-bg: oklch(0.17 0.008 285);
  --color-tnv11-surface: #18181f;
  --color-tnv11-surface: oklch(0.21 0.012 285);
  --color-tnv11-ink: #f5f5fa;
  --color-tnv11-ink: oklch(0.97 0.005 285);
  --color-tnv11-mut: #a1a1aa;
  --color-tnv11-mut: oklch(0.705 0.015 286);
  --font-tnv11-sans: 'Urbanist', system-ui, sans-serif;
  --font-tnv11-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tnv-11 {
  width: 100%;
  min-height: 100svh;
}
```

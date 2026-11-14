---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-header-notification-dropdown-user-menu/"
title: "Tailwind Header with Notification Dropdown and User Menu"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "The right-hand utility cluster taken seriously: a bell with an unread pill that pulses on arrival, a notifications panel grouped into Today and Earlier, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Header with Notification Dropdown and User Menu
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-header-notification-dropdown-user-menu/

The right-hand utility cluster taken seriously: a bell with an unread pill that pulses on arrival, a notifications panel grouped into Today and Earlier, and an avatar menu with profile, preferences and sign out. Both panels open on group-hover and group-focus-within — the whole cluster is keyboard-operable with zero script.
## HTML
```html
<div class="thd-10 group/thd10 w-full min-h-svh bg-thd10-bg font-thd10-sans text-thd10-ink antialiased">
  <a href="#thd-10-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd10-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-thd10-on">Skip to content</a>
  <header class="sticky top-0 z-40 border-b border-thd10-line bg-thd10-bg/85 backdrop-blur-lg">
    <div class="mx-auto flex h-16 max-w-7xl items-center gap-3 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-10-main" class="flex items-center gap-2 text-lg font-bold tracking-tight"><span aria-hidden="true" class="grid size-8 place-items-center rounded-xl bg-thd10-acc text-thd10-on"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M4 18V7l8 6 8-6v11"/></svg></span>Marlow</a>
      <nav aria-label="Main" class="ml-6 hidden md:block">
        <ul class="flex items-center gap-1 text-sm font-medium">
          <li><a href="#thd-10-main" aria-current="page" class="rounded-lg px-3 py-2 text-thd10-mut hover:text-thd10-ink aria-[current=page]:bg-thd10-panel aria-[current=page]:text-thd10-ink">Inbox</a></li>
          <li><a href="#thd-10-main" class="rounded-lg px-3 py-2 text-thd10-mut hover:text-thd10-ink">Threads</a></li>
          <li><a href="#thd-10-main" class="rounded-lg px-3 py-2 text-thd10-mut hover:text-thd10-ink">Directory</a></li>
          <li><a href="#thd-10-main" class="rounded-lg px-3 py-2 text-thd10-mut hover:text-thd10-ink">Reports</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1">
        <input id="thd-10-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-10-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-thd10-mut hover:bg-thd10-ink/8 hover:text-thd10-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd10-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px] group-has-[#thd-10-t:checked]/thd10:hidden"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-10-t:checked]/thd10:block"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <div class="group/bell relative">
          <button type="button" aria-haspopup="true" aria-label="Notifications, 3 unread" class="relative grid size-11 place-items-center rounded-full text-thd10-mut hover:bg-thd10-ink/8 hover:text-thd10-ink group-focus-within/bell:bg-thd10-ink/8">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="size-5"><path d="M6 16v-5a6 6 0 0 1 12 0v5l1.5 2h-15L6 16Z"/><path d="M10 20.5a2 2 0 0 0 4 0"/></svg>
            <span aria-hidden="true" class="absolute right-1 top-1.5 grid min-w-[18px] place-items-center rounded-full bg-thd10-acc px-1 text-[10px] font-bold leading-[18px] tabular-nums text-thd10-on ring-2 ring-thd10-bg">3<span class="absolute inset-0 animate-thd10-ping rounded-full bg-thd10-acc/60 motion-reduce:hidden"></span></span>
          </button>
          <div class="invisible absolute right-0 top-full z-50 mt-2 w-[min(23rem,calc(100vw-1.5rem))] origin-top-right scale-95 rounded-2xl border border-thd10-line bg-thd10-panel opacity-0 shadow-[0_30px_70px_-30px_rgb(0_0_0/.6)] transition-[opacity,scale,visibility] duration-150 before:absolute before:inset-x-0 before:-top-2 before:h-2 before:content-[''] group-hover/bell:visible group-hover/bell:scale-100 group-hover/bell:opacity-100 group-focus-within/bell:visible group-focus-within/bell:scale-100 group-focus-within/bell:opacity-100">
            <div class="flex items-center justify-between border-b border-thd10-line px-4 py-3"><p class="font-semibold">Notifications <span class="ml-1 rounded-full bg-thd10-acc/15 px-2 py-0.5 text-xs text-thd10-acc">3 unread</span></p><a href="#thd-10-main" class="text-xs font-semibold text-thd10-acc hover:underline">Mark all read</a></div>
            <div class="max-h-[22rem] overflow-y-auto overscroll-contain p-1.5">
              <p class="px-2.5 pb-1 pt-2 text-[11px] font-semibold uppercase tracking-[.1em] text-thd10-mut">Today</p>
              <a href="#thd-10-main" data-unread class="group/n flex gap-3 rounded-xl p-2.5 hover:bg-thd10-ink/5 focus-visible:bg-thd10-ink/5 data-unread:bg-thd10-acc/8"><span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-violet-500/20 text-xs font-bold text-violet-400">PS</span><span class="min-w-0 flex-1 text-sm leading-snug"><span class="group-data-unread/n:font-semibold">Priya Sharma</span> requested review on <strong class="font-semibold">Billing rewrite</strong><span class="mt-0.5 block text-xs text-thd10-mut">4 min ago</span></span><span class="sr-only">Unread</span><span aria-hidden="true" class="mt-1.5 hidden size-2 flex-none rounded-full bg-thd10-acc group-data-unread/n:block"></span></a>
              <a href="#thd-10-main" data-unread class="group/n flex gap-3 rounded-xl p-2.5 hover:bg-thd10-ink/5 focus-visible:bg-thd10-ink/5 data-unread:bg-thd10-acc/8"><span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-emerald-500/20 text-emerald-400"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="m5 12 4.5 4.5L19 7"/></svg></span><span class="min-w-0 flex-1 text-sm leading-snug">Deploy <span class="font-mono text-xs">#4821</span> finished in 2m 14s on eu-west<span class="mt-0.5 block text-xs text-thd10-mut">26 min ago</span></span><span class="sr-only">Unread</span><span aria-hidden="true" class="mt-1.5 hidden size-2 flex-none rounded-full bg-thd10-acc group-data-unread/n:block"></span></a>
              <a href="#thd-10-main" data-unread class="group/n flex gap-3 rounded-xl p-2.5 hover:bg-thd10-ink/5 focus-visible:bg-thd10-ink/5 data-unread:bg-thd10-acc/8"><span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-amber-500/20 text-xs font-bold text-amber-400">JL</span><span class="min-w-0 flex-1 text-sm leading-snug"><span class="group-data-unread/n:font-semibold">Jordan Lee</span> mentioned you in <strong class="font-semibold">Q3 retro</strong><span class="mt-0.5 block text-xs text-thd10-mut">1 h ago</span></span><span class="sr-only">Unread</span><span aria-hidden="true" class="mt-1.5 hidden size-2 flex-none rounded-full bg-thd10-acc group-data-unread/n:block"></span></a>
              <p class="px-2.5 pb-1 pt-3 text-[11px] font-semibold uppercase tracking-[.1em] text-thd10-mut">Earlier</p>
              <a href="#thd-10-main" class="group/n flex gap-3 rounded-xl p-2.5 text-thd10-mut hover:bg-thd10-ink/5 focus-visible:bg-thd10-ink/5"><span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-sky-500/20 text-xs font-bold text-sky-400">SR</span><span class="min-w-0 flex-1 text-sm leading-snug">Sam Rivera added 2 members to <strong class="font-semibold text-thd10-ink">Support</strong><span class="mt-0.5 block text-xs">Yesterday</span></span></a>
              <a href="#thd-10-main" class="group/n flex gap-3 rounded-xl p-2.5 text-thd10-mut hover:bg-thd10-ink/5 focus-visible:bg-thd10-ink/5"><span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-thd10-ink/10"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" class="size-4"><path d="M4 6h16M4 12h16M4 18h10"/></svg></span><span class="min-w-0 flex-1 text-sm leading-snug">Weekly digest for Northwind is ready<span class="mt-0.5 block text-xs">Mon</span></span></a>
            </div>
            <a href="#thd-10-main" class="block border-t border-thd10-line px-4 py-3 text-center text-sm font-semibold text-thd10-acc hover:bg-thd10-ink/5">Open notification centre</a>
          </div>
        </div>
        <div class="group/me relative">
          <button type="button" aria-haspopup="menu" class="flex min-h-11 items-center gap-2.5 rounded-full py-1 pl-1 pr-1 hover:bg-thd10-ink/8 sm:pr-3">
            <span aria-hidden="true" class="relative grid size-9 place-items-center rounded-full bg-gradient-to-br from-teal-400 to-cyan-600 text-xs font-bold text-white">AC<span class="absolute -bottom-0.5 -right-0.5 size-3 rounded-full bg-emerald-400 ring-2 ring-thd10-bg"></span></span>
            <span class="hidden text-left leading-tight sm:block"><span class="block text-sm font-semibold">Alex Chen</span><span class="block text-xs text-thd10-mut">Support lead</span></span>
          </button>
          <div role="menu" aria-label="Account" class="invisible absolute right-0 top-full z-50 mt-2 w-60 origin-top-right scale-95 rounded-2xl border border-thd10-line bg-thd10-panel p-1.5 opacity-0 shadow-[0_30px_70px_-30px_rgb(0_0_0/.6)] transition-[opacity,scale,visibility] duration-150 before:absolute before:inset-x-0 before:-top-2 before:h-2 before:content-[''] group-hover/me:visible group-hover/me:scale-100 group-hover/me:opacity-100 group-focus-within/me:visible group-focus-within/me:scale-100 group-focus-within/me:opacity-100">
            <a role="menuitem" href="#thd-10-main" class="flex min-h-10 items-center rounded-lg px-2.5 text-sm hover:bg-thd10-ink/5 focus-visible:bg-thd10-ink/5">Profile</a>
            <a role="menuitem" href="#thd-10-main" class="flex min-h-10 items-center justify-between rounded-lg px-2.5 text-sm hover:bg-thd10-ink/5 focus-visible:bg-thd10-ink/5">Preferences <kbd class="rounded border border-thd10-line px-1.5 text-[11px] text-thd10-mut">&#8984;,</kbd></a>
            <a role="menuitem" href="#thd-10-main" class="flex min-h-10 items-center rounded-lg px-2.5 text-sm hover:bg-thd10-ink/5 focus-visible:bg-thd10-ink/5">Notification rules</a>
            <a role="menuitem" href="#thd-10-main" class="flex min-h-10 items-center rounded-lg px-2.5 text-sm hover:bg-thd10-ink/5 focus-visible:bg-thd10-ink/5">Keyboard shortcuts</a>
            <a role="menuitem" href="#thd-10-main" class="mt-1 flex min-h-10 items-center rounded-lg border-t border-thd10-line px-2.5 text-sm text-rose-400 hover:bg-rose-500/10 focus-visible:bg-rose-500/10">Sign out</a>
          </div>
        </div>
      </div>
    </div>
  </header>
  <main id="thd-10-main" class="mx-auto max-w-7xl px-[clamp(.75rem,3vw,1.5rem)] py-12">
    <h1 class="text-[clamp(1.8rem,4.5vw,2.6rem)] font-bold tracking-tight">Good afternoon, Alex</h1>
    <p class="mt-2 max-w-[52ch] text-thd10-mut">Hover or Tab to the bell for grouped notifications, or to your avatar for the account menu. Both are pure CSS.</p>
    <div aria-hidden="true" class="h-[70svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd10-bg: var(--thd10-bg);
  --color-thd10-panel: var(--thd10-panel);
  --color-thd10-ink: var(--thd10-ink);
  --color-thd10-mut: var(--thd10-mut);
  --color-thd10-line: var(--thd10-line);
  --color-thd10-acc: var(--thd10-acc);
  --color-thd10-on: var(--thd10-on);
}

@theme {
  --font-thd10-sans: 'Onest', system-ui, sans-serif;
  --animate-thd10-ping: thd10-ping 1.4s cubic-bezier(0,0,0.2,1) 3;

  @keyframes thd10-ping {
    75%,
        100% {
      transform: scale(2);
      opacity: 0;
    }
  }
}

.thd-10 {
  width: 100%;
  min-height: 100svh;
  --thd10-bg: #0a1414;
  --thd10-panel: #112020;
  --thd10-ink: #e8f3f1;
  --thd10-mut: #93aba7;
  --thd10-line: rgb(255 255 255 / 0.08);
  --thd10-acc: #2dd4bf;
  --thd10-on: #032320;
}

.thd-10:has(#thd-10-t:checked) {
  --thd10-bg: #f5f9f8;
  --thd10-panel: #ffffff;
  --thd10-ink: #0d1f1d;
  --thd10-mut: #4d625f;
  --thd10-line: rgb(13 31 29 / 0.1);
  --thd10-acc: #0f8f80;
  --thd10-on: #ffffff;
}
```

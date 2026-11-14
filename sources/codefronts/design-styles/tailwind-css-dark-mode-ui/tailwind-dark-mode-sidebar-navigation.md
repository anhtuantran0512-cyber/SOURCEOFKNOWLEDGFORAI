---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-sidebar-navigation/"
title: "Tailwind Dark Mode Sidebar Navigation Component"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A production navigation rail — brand lockup, six sections with live counters, a System / Light / Dark segmented control, settings and an account footer —…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Sidebar Navigation Component
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-sidebar-navigation/

A production navigation rail — brand lockup, six sections with live counters, a System / Light / Dark segmented control, settings and an account footer — that keeps its hierarchy in both themes because every surface, icon stroke and hairline is a token. The active item carries a filled surface and an accent edge drawn with aria-[current=page]:before:, so state never rests on colour alone.
## HTML
```html
<div class="tdm-05 scheme-light-dark has-[#tdm-05-light:checked]:scheme-light has-[#tdm-05-dark:checked]:scheme-dark grid w-full min-h-svh place-items-center bg-tdm05-bg px-4 py-10 font-tdm05-sans text-tdm05-ink antialiased transition-colors duration-300">
  <div class="grid w-full max-w-6xl overflow-hidden rounded-[28px] border border-tdm05-line bg-tdm05-canvas shadow-tdm05-frame md:min-h-[min(42rem,86vh)] md:grid-cols-[17.5rem_minmax(0,1fr)]">
    <nav class="flex flex-col gap-5 border-b border-tdm05-line bg-tdm05-rail p-4 md:border-r md:border-b-0" aria-label="Workspace">
      <button type="button" class="flex min-h-12 items-center gap-3 rounded-xl px-2 text-left transition hover:bg-tdm05-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm05-focus">
        <span class="grid size-9 flex-none place-items-center rounded-xl bg-tdm05-acc text-tdm05-acc-ink shadow-[inset_0_1px_0_rgb(255_255_255/.25)]"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5 20.5 7.3v9.4L12 21.5l-8.5-4.8V7.3Z"/><path d="M12 8v8M8.5 10l7 4M15.5 10l-7 4"/></svg></span>
        <span class="grid min-w-0 flex-1"><span class="text-sm font-semibold tracking-tight">Northwind</span><span class="text-xs text-tdm05-mut">Pro workspace</span></span>
        <svg class="size-4 text-tdm05-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m7 15 5 5 5-5M7 9l5-5 5 5"/></svg>
      </button>
      <ul class="grid gap-0.5">
        <li><a href="#tdm-05" aria-current="page" class="group/link relative flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tdm05-mut transition hover:bg-tdm05-hover hover:text-tdm05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm05-focus aria-[current=page]:bg-tdm05-active aria-[current=page]:text-tdm05-ink aria-[current=page]:before:absolute aria-[current=page]:before:inset-y-2.5 aria-[current=page]:before:-left-1 aria-[current=page]:before:w-[3px] aria-[current=page]:before:rounded-full aria-[current=page]:before:bg-tdm05-acc aria-[current=page]:before:content-[''] forced-colors:aria-[current=page]:outline forced-colors:aria-[current=page]:outline-1">
          <svg class="size-[18px] flex-none text-tdm05-icon transition-colors group-hover/link:text-tdm05-ink group-aria-[current=page]/link:text-tdm05-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.5"/></svg>
          <span class="flex-1">Overview</span>
        </a></li>
        <li><a href="#tdm-05" class="group/link relative flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tdm05-mut transition hover:bg-tdm05-hover hover:text-tdm05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm05-focus aria-[current=page]:bg-tdm05-active aria-[current=page]:text-tdm05-ink aria-[current=page]:before:absolute aria-[current=page]:before:inset-y-2.5 aria-[current=page]:before:-left-1 aria-[current=page]:before:w-[3px] aria-[current=page]:before:rounded-full aria-[current=page]:before:bg-tdm05-acc aria-[current=page]:before:content-[''] forced-colors:aria-[current=page]:outline forced-colors:aria-[current=page]:outline-1">
          <svg class="size-[18px] flex-none text-tdm05-icon transition-colors group-hover/link:text-tdm05-ink group-aria-[current=page]/link:text-tdm05-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 20.5h17M6.5 16.5v-5M11 16.5V6.5M15.5 16.5v-8M20 16.5V12"/></svg>
          <span class="flex-1">Analytics</span><span class="rounded-md bg-tdm05-ink/8 px-1.5 py-0.5 font-tdm05-mono text-[11px] tabular-nums text-tdm05-mut">12</span>
        </a></li>
        <li><a href="#tdm-05" class="group/link relative flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tdm05-mut transition hover:bg-tdm05-hover hover:text-tdm05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm05-focus aria-[current=page]:bg-tdm05-active aria-[current=page]:text-tdm05-ink aria-[current=page]:before:absolute aria-[current=page]:before:inset-y-2.5 aria-[current=page]:before:-left-1 aria-[current=page]:before:w-[3px] aria-[current=page]:before:rounded-full aria-[current=page]:before:bg-tdm05-acc aria-[current=page]:before:content-[''] forced-colors:aria-[current=page]:outline forced-colors:aria-[current=page]:outline-1">
          <svg class="size-[18px] flex-none text-tdm05-icon transition-colors group-hover/link:text-tdm05-ink group-aria-[current=page]/link:text-tdm05-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.8 20.5 7.5v9L12 21.2l-8.5-4.7v-9Z"/><path d="M3.8 7.6 12 12.2l8.2-4.6M12 12.2v8.8"/></svg>
          <span class="flex-1">Deployments</span>
        </a></li>
        <li><a href="#tdm-05" class="group/link relative flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tdm05-mut transition hover:bg-tdm05-hover hover:text-tdm05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm05-focus aria-[current=page]:bg-tdm05-active aria-[current=page]:text-tdm05-ink aria-[current=page]:before:absolute aria-[current=page]:before:inset-y-2.5 aria-[current=page]:before:-left-1 aria-[current=page]:before:w-[3px] aria-[current=page]:before:rounded-full aria-[current=page]:before:bg-tdm05-acc aria-[current=page]:before:content-[''] forced-colors:aria-[current=page]:outline forced-colors:aria-[current=page]:outline-1">
          <svg class="size-[18px] flex-none text-tdm05-icon transition-colors group-hover/link:text-tdm05-ink group-aria-[current=page]/link:text-tdm05-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M21.5 20a6.5 6.5 0 0 0-4-6"/></svg>
          <span class="flex-1">Members</span><span class="rounded-md bg-tdm05-ink/8 px-1.5 py-0.5 font-tdm05-mono text-[11px] tabular-nums text-tdm05-mut">28</span>
        </a></li>
        <li><a href="#tdm-05" class="group/link relative flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tdm05-mut transition hover:bg-tdm05-hover hover:text-tdm05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm05-focus aria-[current=page]:bg-tdm05-active aria-[current=page]:text-tdm05-ink aria-[current=page]:before:absolute aria-[current=page]:before:inset-y-2.5 aria-[current=page]:before:-left-1 aria-[current=page]:before:w-[3px] aria-[current=page]:before:rounded-full aria-[current=page]:before:bg-tdm05-acc aria-[current=page]:before:content-[''] forced-colors:aria-[current=page]:outline forced-colors:aria-[current=page]:outline-1">
          <svg class="size-[18px] flex-none text-tdm05-icon transition-colors group-hover/link:text-tdm05-ink group-aria-[current=page]/link:text-tdm05-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg>
          <span class="flex-1">Storage</span>
        </a></li>
        <li><a href="#tdm-05" class="group/link relative flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tdm05-mut transition hover:bg-tdm05-hover hover:text-tdm05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm05-focus aria-[current=page]:bg-tdm05-active aria-[current=page]:text-tdm05-ink aria-[current=page]:before:absolute aria-[current=page]:before:inset-y-2.5 aria-[current=page]:before:-left-1 aria-[current=page]:before:w-[3px] aria-[current=page]:before:rounded-full aria-[current=page]:before:bg-tdm05-acc aria-[current=page]:before:content-[''] forced-colors:aria-[current=page]:outline forced-colors:aria-[current=page]:outline-1">
          <svg class="size-[18px] flex-none text-tdm05-icon transition-colors group-hover/link:text-tdm05-ink group-aria-[current=page]/link:text-tdm05-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 2.5v5M15 2.5v5M6 7.5h12v4a6 6 0 0 1-12 0ZM12 17.5v4"/></svg>
          <span class="flex-1">Integrations</span><span class="rounded-md bg-tdm05-acc/15 px-1.5 py-0.5 font-tdm05-mono text-[10.5px] font-semibold uppercase tracking-wide text-tdm05-acc">New</span>
        </a></li>
      </ul>
      <div class="mt-auto grid gap-3 border-t border-tdm05-line pt-4">
        <fieldset class="grid grid-cols-3 gap-1 rounded-xl border border-tdm05-line bg-tdm05-ink/4 p-1">
          <legend class="sr-only">Theme</legend>
          <label class="flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-lg text-xs font-medium text-tdm05-mut transition hover:text-tdm05-ink has-checked:bg-tdm05-raised has-checked:text-tdm05-ink has-checked:shadow-[0_1px_2px_rgb(0_0_0/.2),inset_0_0_0_1px_var(--color-tdm05-line)] has-focus-visible:outline-2 has-focus-visible:outline-tdm05-focus">
            <input type="radio" name="tdm-05-theme" id="tdm-05-system" class="sr-only" checked><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8.5 20.5h7M12 17v3.5"/></svg>System
          </label>
          <label class="flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-lg text-xs font-medium text-tdm05-mut transition hover:text-tdm05-ink has-checked:bg-tdm05-raised has-checked:text-tdm05-ink has-checked:shadow-[0_1px_2px_rgb(0_0_0/.2),inset_0_0_0_1px_var(--color-tdm05-line)] has-focus-visible:outline-2 has-focus-visible:outline-tdm05-focus">
            <input type="radio" name="tdm-05-theme" id="tdm-05-light" class="sr-only"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>Light
          </label>
          <label class="flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-lg text-xs font-medium text-tdm05-mut transition hover:text-tdm05-ink has-checked:bg-tdm05-raised has-checked:text-tdm05-ink has-checked:shadow-[0_1px_2px_rgb(0_0_0/.2),inset_0_0_0_1px_var(--color-tdm05-line)] has-focus-visible:outline-2 has-focus-visible:outline-tdm05-focus">
            <input type="radio" name="tdm-05-theme" id="tdm-05-dark" class="sr-only"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>Dark
          </label>
        </fieldset>
        <a href="#tdm-05" class="group/link flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm font-medium text-tdm05-mut transition hover:bg-tdm05-hover hover:text-tdm05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm05-focus"><svg class="size-[18px] text-tdm05-icon group-hover/link:text-tdm05-ink" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2.5v2.2M12 19.3v2.2M4.6 4.6l1.6 1.6M17.8 17.8l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.6 19.4l1.6-1.6M17.8 6.2l1.6-1.6"/><circle cx="12" cy="12" r="6.5"/></svg>Settings</a>
        <div class="flex items-center gap-3 rounded-xl border border-tdm05-line bg-tdm05-raised p-2.5">
          <span class="grid size-9 flex-none place-items-center rounded-full bg-linear-to-br from-tdm05-acc to-tdm05-acc2 text-xs font-semibold text-tdm05-acc-ink" aria-hidden="true">JL</span>
          <span class="grid min-w-0"><span class="truncate text-sm font-medium">Jordan Lee</span><span class="truncate text-xs text-tdm05-mut">[email protected]</span></span>
        </div>
      </div>
    </nav>
    <section class="grid content-start gap-6 p-6 sm:p-10" aria-label="Content preview">
      <p class="flex items-center gap-2 font-tdm05-mono text-xs text-tdm05-mut">Overview <span aria-hidden="true">/</span> <span class="text-tdm05-ink">Production</span></p>
      <div class="grid gap-2">
        <h1 class="text-[clamp(1.6rem,3vw,2.3rem)] font-semibold tracking-[-0.035em] text-balance">Readable in both themes</h1>
        <p class="max-w-[60ch] text-[15px]/relaxed text-pretty text-tdm05-mut">Nav surfaces, icon strokes, hairlines and counters each own a token, so the rail keeps its hierarchy when the palette flips. Try System / Light / Dark in the footer.</p>
      </div>
      <div class="grid gap-3 sm:grid-cols-3">
        <div class="grid gap-1 rounded-2xl border border-tdm05-line bg-tdm05-raised p-4"><p class="text-[13px] text-tdm05-mut">Uptime</p><strong class="text-[26px] font-semibold tracking-[-0.03em] tabular-nums">99.98%</strong><p class="font-tdm05-mono text-[11px] text-tdm05-mut">last 30 days</p></div>
        <div class="grid gap-1 rounded-2xl border border-tdm05-line bg-tdm05-raised p-4"><p class="text-[13px] text-tdm05-mut">p95 latency</p><strong class="text-[26px] font-semibold tracking-[-0.03em] tabular-nums">142ms</strong><p class="font-tdm05-mono text-[11px] text-tdm05-mut">iad1 · fra1</p></div>
        <div class="grid gap-1 rounded-2xl border border-tdm05-line bg-tdm05-raised p-4"><p class="text-[13px] text-tdm05-mut">Open PRs</p><strong class="text-[26px] font-semibold tracking-[-0.03em] tabular-nums">7</strong><p class="font-tdm05-mono text-[11px] text-tdm05-mut">2 need review</p></div>
      </div>
      <div class="overflow-hidden rounded-2xl border border-tdm05-line bg-tdm05-raised">
        <p class="border-b border-tdm05-line px-4 py-3 text-sm font-semibold">Recent deployments</p>
        <ul class="divide-y divide-tdm05-line text-sm">
          <li class="flex items-center gap-3 px-4 py-3"><span class="size-2 flex-none rounded-full bg-tdm05-ok" aria-hidden="true"></span><span class="min-w-0 flex-1"><span class="font-medium">web-app</span> <span class="font-tdm05-mono text-xs text-tdm05-mut">main · 4f2a91c</span></span><span class="hidden font-tdm05-mono text-xs text-tdm05-mut sm:inline">2m ago</span><span class="rounded-md border border-tdm05-line px-2 py-0.5 text-xs text-tdm05-mut">Ready</span></li>
          <li class="flex items-center gap-3 px-4 py-3"><span class="size-2 flex-none rounded-full bg-tdm05-ok" aria-hidden="true"></span><span class="min-w-0 flex-1"><span class="font-medium">edge-api</span> <span class="font-tdm05-mono text-xs text-tdm05-mut">feat/tokens · 9be01d3</span></span><span class="hidden font-tdm05-mono text-xs text-tdm05-mut sm:inline">18m ago</span><span class="rounded-md border border-tdm05-line px-2 py-0.5 text-xs text-tdm05-mut">Ready</span></li>
          <li class="flex items-center gap-3 px-4 py-3"><span class="size-2 flex-none rounded-full bg-tdm05-warn" aria-hidden="true"></span><span class="min-w-0 flex-1"><span class="font-medium">docs</span> <span class="font-tdm05-mono text-xs text-tdm05-mut">main · 1ac77e0</span></span><span class="hidden font-tdm05-mono text-xs text-tdm05-mut sm:inline">1h ago</span><span class="rounded-md border border-tdm05-line px-2 py-0.5 text-xs text-tdm05-mut">Building</span></li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm05-bg: light-dark(#e9ecf1, #050608);
  --color-tdm05-rail: light-dark(#ffffff, #0c0e12);
  --color-tdm05-canvas: light-dark(#f7f8fa, #090a0e);
  --color-tdm05-raised: light-dark(#ffffff, #12151c);
  --color-tdm05-ink: light-dark(#0b0d12, #eef1f6);
  --color-tdm05-mut: light-dark(#5a6170, #949db0);
  --color-tdm05-icon: light-dark(#6b7280, #a7b0c0);
  --color-tdm05-line: light-dark(#e3e6ec, #1e222c);
  --color-tdm05-hover: light-dark(rgb(10 12 20 / .045), rgb(255 255 255 / .05));
  --color-tdm05-active: light-dark(rgb(59 91 219 / .08), rgb(124 155 255 / .1));
  --color-tdm05-acc: light-dark(#3b5bdb, #7c9bff);
  --color-tdm05-acc2: light-dark(#7048e8, #b197fc);
  --color-tdm05-acc-ink: light-dark(#ffffff, #070b1a);
  --color-tdm05-focus: light-dark(#3b5bdb, #a8c0ff);
  --color-tdm05-ok: light-dark(#16a34a, #4ade80);
  --color-tdm05-warn: light-dark(#d97706, #fbbf24);
  --shadow-tdm05-frame: 0 50px 100px -60px light-dark(rgb(11 13 18 / .35), rgb(0 0 0 / .9));
  --font-tdm05-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm05-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

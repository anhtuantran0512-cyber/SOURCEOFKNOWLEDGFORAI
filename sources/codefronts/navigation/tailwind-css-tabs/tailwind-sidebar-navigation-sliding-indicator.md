---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/tailwind-sidebar-navigation-sliding-indicator/"
title: "Tailwind Sidebar Navigation with Sliding Indicator"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "An app-shell sidebar on warm stone: icon rows, an olive accent bar that slides vertically to the active row, and a content pane beside it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar Navigation with Sliding Indicator
Source: https://codefronts.com/navigation/tailwind-css-tabs/tailwind-sidebar-navigation-sliding-indicator/

An app-shell sidebar on warm stone: icon rows, an olive accent bar that slides vertically to the active row, and a content pane beside it. The original measured offsetTop; the port slides the bar with translate-y-[calc(var(--i)*(100%+4px))] — each step is one 44px row plus its 4px gap.
## HTML
```html
<section class="ttb-15 group/tabs grid min-h-svh w-full place-items-center bg-ttb15-bg px-5 py-14 font-ttb15-sans text-ttb15-ink" aria-label="Sidebar navigation with sliding indicator demo">
  <div class="grid w-full max-w-2xl justify-items-center gap-7">
    <div class="flex w-full flex-wrap gap-3 rounded-2xl bg-ttb15-panel p-3 shadow-[0_18px_40px_-20px_rgb(58_46_30/0.35)] ring-1 ring-ttb15-ink/8">
      <div class="flex-[1_1_200px]">
        <p class="flex items-center gap-2.5 px-3 pt-2 pb-4 text-sm font-bold"><span aria-hidden="true" class="grid size-7 place-items-center rounded-lg bg-ttb15-acc text-[11px] font-extrabold text-white">NB</span>Northbound</p>
        <div role="radiogroup" aria-label="Workspace" class="relative flex flex-col gap-1 pl-3 [--i:0] has-[#ttb15-r2:checked]:[--i:1] has-[#ttb15-r3:checked]:[--i:2] has-[#ttb15-r4:checked]:[--i:3]">
          <span aria-hidden="true" class="pointer-events-none absolute top-0 left-0 h-11 w-1 translate-y-[calc(var(--i)*(100%+4px))] rounded-r-full bg-ttb15-acc transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:transition-none"></span>
          <label class="group/tab flex h-11 cursor-pointer items-center gap-3 rounded-lg px-3 text-sm font-semibold text-ttb15-mut transition-[color,background-color,translate] duration-300 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:bg-ttb15-acc/8 hover:text-ttb15-ink has-checked:translate-x-1 has-checked:bg-ttb15-acc/10 has-checked:text-ttb15-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-ttb15-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb15" id="ttb15-r1" checked><svg aria-hidden="true" class="size-[18px] transition-transform duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8v10h-6v-7H9v7H3z"/></svg>Home</label>
          <label class="group/tab flex h-11 cursor-pointer items-center gap-3 rounded-lg px-3 text-sm font-semibold text-ttb15-mut transition-[color,background-color,translate] duration-300 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:bg-ttb15-acc/8 hover:text-ttb15-ink has-checked:translate-x-1 has-checked:bg-ttb15-acc/10 has-checked:text-ttb15-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-ttb15-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb15" id="ttb15-r2"><svg aria-hidden="true" class="size-[18px] transition-transform duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h4l3-9 4 18 3-9h6"/></svg>Activity</label>
          <label class="group/tab flex h-11 cursor-pointer items-center gap-3 rounded-lg px-3 text-sm font-semibold text-ttb15-mut transition-[color,background-color,translate] duration-300 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:bg-ttb15-acc/8 hover:text-ttb15-ink has-checked:translate-x-1 has-checked:bg-ttb15-acc/10 has-checked:text-ttb15-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-ttb15-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb15" id="ttb15-r3"><svg aria-hidden="true" class="size-[18px] transition-transform duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/></svg>People</label>
          <label class="group/tab flex h-11 cursor-pointer items-center gap-3 rounded-lg px-3 text-sm font-semibold text-ttb15-mut transition-[color,background-color,translate] duration-300 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:bg-ttb15-acc/8 hover:text-ttb15-ink has-checked:translate-x-1 has-checked:bg-ttb15-acc/10 has-checked:text-ttb15-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-ttb15-acc motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb15" id="ttb15-r4"><svg aria-hidden="true" class="size-[18px] transition-transform duration-400 group-has-checked/tab:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/></svg>Settings</label>
        </div>
      </div>
      <div class="min-w-0 flex-[999_1_300px] rounded-xl bg-ttb15-card p-6 ring-1 ring-ttb15-ink/6">
        <div class="hidden group-has-[#ttb15-r1:checked]/tabs:block"><h3 class="text-xl font-bold">Home</h3><p class="mt-2 text-sm leading-relaxed text-ttb15-mut">Pinned projects, recent files and what changed since your last visit.</p></div>
        <div class="hidden group-has-[#ttb15-r2:checked]/tabs:block"><h3 class="text-xl font-bold">Activity</h3><p class="mt-2 text-sm leading-relaxed text-ttb15-mut">Comments, mentions and edits across every project you follow.</p></div>
        <div class="hidden group-has-[#ttb15-r3:checked]/tabs:block"><h3 class="text-xl font-bold">People</h3><p class="mt-2 text-sm leading-relaxed text-ttb15-mut">Members, guests and pending invitations for this workspace.</p></div>
        <div class="hidden group-has-[#ttb15-r4:checked]/tabs:block"><h3 class="text-xl font-bold">Settings</h3><p class="mt-2 text-sm leading-relaxed text-ttb15-mut">Workspace name, permissions, integrations and billing.</p></div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb15-ink/10 bg-ttb15-card/70 px-3.5 py-2 font-ttb15-mono text-[11.5px] text-ttb15-mut">translate-y-[calc(var(--i)*(100%+4px))] · spring row shift</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb15-bg: #e8dac5;
  --color-ttb15-bg: oklch(0.894 0.032 78.1);
  --color-ttb15-panel: #f1e7d7;
  --color-ttb15-panel: oklch(0.932 0.024 79.7);
  --color-ttb15-card: #fbf7f0;
  --color-ttb15-card: oklch(0.977 0.010 81.8);
  --color-ttb15-ink: #2e2416;
  --color-ttb15-ink: oklch(0.268 0.028 75.4);
  --color-ttb15-mut: #6a5b46;
  --color-ttb15-mut: oklch(0.480 0.037 76.0);
  --color-ttb15-acc: #5f8248;
  --color-ttb15-acc: oklch(0.565 0.093 134.0);
  --color-ttb15-acc-ink: #3f5c2f;
  --color-ttb15-acc-ink: oklch(0.440 0.078 135.3);
  --font-ttb15-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttb15-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-15 {
  width: 100%;
  min-height: 100svh;
}
```

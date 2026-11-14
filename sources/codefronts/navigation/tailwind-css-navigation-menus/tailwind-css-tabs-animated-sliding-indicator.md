---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-tabs-animated-sliding-indicator/"
title: "Tailwind CSS Tabs with Animated Sliding Indicator"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "Three tab patterns in one demo — capsule tabs, underline tabs and an iOS-style segmented control — each with an indicator that glides between options on a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Tabs with Animated Sliding Indicator
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-tabs-animated-sliding-indicator/

Three tab patterns in one demo — capsule tabs, underline tabs and an iOS-style segmented control — each with an indicator that glides between options on a spring curve. Hidden radios drive everything through group-has-[#id:checked]/a:, which means the arrow keys move between tabs natively. Panels fade in with starting:. Zero JavaScript.
## HTML
```html
<div class="tnv-08 grid min-h-svh w-full content-center justify-items-center gap-14 bg-tnv08-bg px-5 py-16 font-tnv08-sans text-tnv08-ink antialiased selection:bg-tnv08-acc selection:text-white">
  <div class="group/a w-full max-w-2xl">
    <p id="tnv08-a-l" class="mb-3.5 text-xs font-bold tracking-[0.1em] text-tnv08-mut uppercase">Capsule tabs</p>
    <div role="radiogroup" aria-labelledby="tnv08-a-l" class="relative grid grid-cols-4 gap-0.5 rounded-2xl border border-tnv08-line bg-white p-1.5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] group-has-[:focus-visible]/a:ring-2 group-has-[:focus-visible]/a:ring-tnv08-acc/40">
      <input type="radio" name="tnv08-a" id="tnv08-a1" class="sr-only" checked><input type="radio" name="tnv08-a" id="tnv08-a2" class="sr-only"><input type="radio" name="tnv08-a" id="tnv08-a3" class="sr-only"><input type="radio" name="tnv08-a" id="tnv08-a4" class="sr-only">
      <span aria-hidden="true" class="absolute inset-y-1.5 left-1.5 w-[calc((100%-18px)/4)] rounded-[11px] bg-tnv08-acc shadow-[0_6px_16px_-6px_var(--color-tnv08-acc)] transition-transform duration-300 ease-[cubic-bezier(.34,1.25,.64,1)] group-has-[#tnv08-a2:checked]/a:translate-x-[calc(100%+2px)] group-has-[#tnv08-a3:checked]/a:translate-x-[calc(200%+4px)] group-has-[#tnv08-a4:checked]/a:translate-x-[calc(300%+6px)] motion-reduce:transition-none"></span>
      <label for="tnv08-a1" class="relative z-10 cursor-pointer rounded-[11px] py-2.5 text-center text-[13px] font-semibold text-tnv08-mut transition-colors select-none hover:text-tnv08-ink sm:text-sm group-has-[#tnv08-a1:checked]/a:text-white">Overview</label>
      <label for="tnv08-a2" class="relative z-10 cursor-pointer rounded-[11px] py-2.5 text-center text-[13px] font-semibold text-tnv08-mut transition-colors select-none hover:text-tnv08-ink sm:text-sm group-has-[#tnv08-a2:checked]/a:text-white">Analytics</label>
      <label for="tnv08-a3" class="relative z-10 cursor-pointer rounded-[11px] py-2.5 text-center text-[13px] font-semibold text-tnv08-mut transition-colors select-none hover:text-tnv08-ink sm:text-sm group-has-[#tnv08-a3:checked]/a:text-white">Reports</label>
      <label for="tnv08-a4" class="relative z-10 cursor-pointer rounded-[11px] py-2.5 text-center text-[13px] font-semibold text-tnv08-mut transition-colors select-none hover:text-tnv08-ink sm:text-sm group-has-[#tnv08-a4:checked]/a:text-white">Settings</label>
    </div>
    <div class="mt-1.5 rounded-2xl border border-tnv08-line bg-white [&>div]:hidden [&>div]:p-7 [&>div]:transition-[opacity,translate] [&>div]:duration-300 [&>div]:starting:translate-y-1 [&>div]:starting:opacity-0 [&_h3]:font-bold [&_p]:mt-2 [&_p]:text-[15px]/[1.6] [&_p]:text-tnv08-mut">
      <div class="group-has-[#tnv08-a1:checked]/a:block"><h3>Overview</h3><p>A summary of every key metric across your workspace, updated in real time.</p></div>
      <div class="group-has-[#tnv08-a2:checked]/a:block"><h3>Analytics</h3><p>Deep-dive charts for traffic, conversions and user behaviour trends.</p></div>
      <div class="group-has-[#tnv08-a3:checked]/a:block"><h3>Reports</h3><p>Scheduled reports delivered to your inbox every Monday morning.</p></div>
      <div class="group-has-[#tnv08-a4:checked]/a:block"><h3>Settings</h3><p>Notifications, integrations and workspace preferences.</p></div>
    </div>
  </div>
  <div class="group/b w-full max-w-2xl">
    <p id="tnv08-b-l" class="mb-3.5 text-xs font-bold tracking-[0.1em] text-tnv08-mut uppercase">Underline tabs</p>
    <div role="radiogroup" aria-labelledby="tnv08-b-l" class="relative grid grid-cols-3 border-b-2 border-tnv08-line group-has-[:focus-visible]/b:outline-2 group-has-[:focus-visible]/b:outline-offset-4 group-has-[:focus-visible]/b:outline-tnv08-acc/40">
      <input type="radio" name="tnv08-b" id="tnv08-b1" class="sr-only" checked><input type="radio" name="tnv08-b" id="tnv08-b2" class="sr-only"><input type="radio" name="tnv08-b" id="tnv08-b3" class="sr-only">
      <span aria-hidden="true" class="absolute -bottom-0.5 left-0 h-0.5 w-1/3 px-6 transition-transform duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-has-[#tnv08-b2:checked]/b:translate-x-full group-has-[#tnv08-b3:checked]/b:translate-x-[200%] motion-reduce:transition-none"><span class="block h-full rounded-full bg-tnv08-acc"></span></span>
      <label for="tnv08-b1" class="cursor-pointer py-3 text-center text-sm font-semibold text-tnv08-mut transition-colors select-none hover:text-tnv08-ink group-has-[#tnv08-b1:checked]/b:text-tnv08-ink">Activity</label>
      <label for="tnv08-b2" class="cursor-pointer py-3 text-center text-sm font-semibold text-tnv08-mut transition-colors select-none hover:text-tnv08-ink group-has-[#tnv08-b2:checked]/b:text-tnv08-ink">Integrations <span class="ml-1 rounded-full bg-tnv08-acc/10 px-1.5 text-[11px] text-tnv08-acc">40+</span></label>
      <label for="tnv08-b3" class="cursor-pointer py-3 text-center text-sm font-semibold text-tnv08-mut transition-colors select-none hover:text-tnv08-ink group-has-[#tnv08-b3:checked]/b:text-tnv08-ink">Members</label>
    </div>
    <div class="rounded-b-2xl border border-t-0 border-tnv08-line bg-white [&>div]:hidden [&>div]:p-7 [&>div]:transition-[opacity,translate] [&>div]:duration-300 [&>div]:starting:translate-y-1 [&>div]:starting:opacity-0 [&_h3]:font-bold [&_p]:mt-2 [&_p]:text-[15px]/[1.6] [&_p]:text-tnv08-mut">
      <div class="group-has-[#tnv08-b1:checked]/b:block"><h3>Activity</h3><p>Everything your team changed in this workspace over the past 7 days.</p></div>
      <div class="group-has-[#tnv08-b2:checked]/b:block"><h3>Integrations</h3><p>Connect Slack, GitHub, Jira and 40+ other tools with one click.</p></div>
      <div class="group-has-[#tnv08-b3:checked]/b:block"><h3>Members</h3><p>Manage roles, permissions and invitations for every member.</p></div>
    </div>
  </div>
  <div class="group/c w-full max-w-2xl">
    <p id="tnv08-c-l" class="mb-3.5 text-xs font-bold tracking-[0.1em] text-tnv08-mut uppercase">Segmented control</p>
    <div class="flex flex-wrap items-center justify-between gap-4">
      <div role="radiogroup" aria-labelledby="tnv08-c-l" class="relative grid w-full max-w-sm grid-cols-3 gap-0.5 rounded-xl bg-tnv08-line p-[3px] group-has-[:focus-visible]/c:ring-2 group-has-[:focus-visible]/c:ring-tnv08-acc/40">
        <input type="radio" name="tnv08-c" id="tnv08-c1" class="sr-only" checked><input type="radio" name="tnv08-c" id="tnv08-c2" class="sr-only"><input type="radio" name="tnv08-c" id="tnv08-c3" class="sr-only">
        <span aria-hidden="true" class="absolute inset-y-[3px] left-[3px] w-[calc((100%-10px)/3)] rounded-[9px] bg-white shadow-[0_1px_4px_rgb(0_0_0/0.12)] transition-transform duration-300 ease-[cubic-bezier(.34,1.25,.64,1)] group-has-[#tnv08-c2:checked]/c:translate-x-[calc(100%+2px)] group-has-[#tnv08-c3:checked]/c:translate-x-[calc(200%+4px)] motion-reduce:transition-none"></span>
        <label for="tnv08-c1" class="relative z-10 cursor-pointer py-2 text-center text-[13px] font-semibold text-tnv08-mut select-none group-has-[#tnv08-c1:checked]/c:text-tnv08-ink">Daily</label>
        <label for="tnv08-c2" class="relative z-10 cursor-pointer py-2 text-center text-[13px] font-semibold text-tnv08-mut select-none group-has-[#tnv08-c2:checked]/c:text-tnv08-ink">Weekly</label>
        <label for="tnv08-c3" class="relative z-10 cursor-pointer py-2 text-center text-[13px] font-semibold text-tnv08-mut select-none group-has-[#tnv08-c3:checked]/c:text-tnv08-ink">Monthly</label>
      </div>
      <p aria-live="polite" class="text-right text-sm text-tnv08-mut [&>span]:hidden [&_b]:text-2xl [&_b]:font-extrabold [&_b]:tracking-[-0.03em] [&_b]:text-tnv08-ink"><span class="group-has-[#tnv08-c1:checked]/c:inline"><b>$2,840</b> today</span><span class="group-has-[#tnv08-c2:checked]/c:inline"><b>$19,410</b> this week</span><span class="group-has-[#tnv08-c3:checked]/c:inline"><b>$84,200</b> this month</span></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv08-bg: #fff1f2;
  --color-tnv08-bg: oklch(0.969 0.015 12);
  --color-tnv08-line: #fecdd3;
  --color-tnv08-line: oklch(0.892 0.058 10);
  --color-tnv08-ink: #1a0a0d;
  --color-tnv08-ink: oklch(0.17 0.02 10);
  --color-tnv08-mut: #9f1239;
  --color-tnv08-mut: oklch(0.455 0.188 14);
  --color-tnv08-acc: #e11d48;
  --color-tnv08-acc: oklch(0.586 0.253 18);
  --font-tnv08-sans: 'Manrope', system-ui, sans-serif;
}

.tnv-08 {
  width: 100%;
  min-height: 100svh;
}
```

---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/vertical-tabs-timeline-progress-tailwind-css/"
title: "Vertical Tabs with Timeline Progress in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A settings sidebar on a timeline rail: hollow dots for each section, a solid glowing dot for the active one, and — new in the port — a progress fill that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tabs with Timeline Progress in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/vertical-tabs-timeline-progress-tailwind-css/

A settings sidebar on a timeline rail: hollow dots for each section, a solid glowing dot for the active one, and — new in the port — a progress fill that runs down the rail to the active step. Beside it, the content pane switches; on phones the two stack.
## HTML
```html
<section class="ttb-08 group/tabs grid min-h-svh w-full place-items-center bg-ttb08-bg px-5 py-14 font-ttb08-sans text-ttb08-ink" aria-label="Vertical timeline tabs demo">
  <div class="grid w-full max-w-2xl justify-items-center gap-7">
    <div class="grid w-full gap-4 rounded-2xl bg-ttb08-card p-4 ring-1 ring-white/8 sm:grid-cols-[210px_1fr]">
      <div role="radiogroup" aria-label="Settings sections" class="relative flex flex-col [--i:0] has-[#ttb08-r2:checked]:[--i:1] has-[#ttb08-r3:checked]:[--i:2] has-[#ttb08-r4:checked]:[--i:3]">
        <span aria-hidden="true" class="absolute top-6 bottom-6 left-[15px] w-0.5 rounded-full bg-ttb08-acc/20"></span>
        <span aria-hidden="true" class="absolute top-6 left-[15px] h-[calc((100%-48px)*var(--i)/3)] w-0.5 rounded-full bg-ttb08-acc transition-[height] duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:transition-none"></span>
        <label class="group/tab relative flex h-12 cursor-pointer items-center gap-3 rounded-lg px-2.5 transition-colors hover:bg-ttb08-acc/6 has-focus-visible:outline-1 has-focus-visible:outline-offset-1 has-focus-visible:outline-dashed has-focus-visible:outline-ttb08-acc"><input class="sr-only" type="radio" name="ttb08" id="ttb08-r1" checked><span aria-hidden="true" class="relative z-10 size-3 flex-none rounded-full border-[1.5px] border-ttb08-acc/50 bg-ttb08-card transition-[background-color,border-color,box-shadow] group-has-checked/tab:border-ttb08-acc group-has-checked/tab:bg-ttb08-acc group-has-checked/tab:shadow-[0_0_10px_color-mix(in_oklab,var(--color-ttb08-acc)_60%,transparent)]"></span><span class="leading-tight"><span class="block text-[13px] font-semibold text-ttb08-mut transition-colors group-has-checked/tab:text-ttb08-acc-ink">Profile</span><span class="block text-[11px] text-ttb08-dim">Name, photo, bio</span></span></label>
        <label class="group/tab relative flex h-12 cursor-pointer items-center gap-3 rounded-lg px-2.5 transition-colors hover:bg-ttb08-acc/6 has-focus-visible:outline-1 has-focus-visible:outline-offset-1 has-focus-visible:outline-dashed has-focus-visible:outline-ttb08-acc"><input class="sr-only" type="radio" name="ttb08" id="ttb08-r2"><span aria-hidden="true" class="relative z-10 size-3 flex-none rounded-full border-[1.5px] border-ttb08-acc/50 bg-ttb08-card transition-[background-color,border-color,box-shadow] group-has-checked/tab:border-ttb08-acc group-has-checked/tab:bg-ttb08-acc group-has-checked/tab:shadow-[0_0_10px_color-mix(in_oklab,var(--color-ttb08-acc)_60%,transparent)]"></span><span class="leading-tight"><span class="block text-[13px] font-semibold text-ttb08-mut transition-colors group-has-checked/tab:text-ttb08-acc-ink">Account</span><span class="block text-[11px] text-ttb08-dim">Email, password, 2FA</span></span></label>
        <label class="group/tab relative flex h-12 cursor-pointer items-center gap-3 rounded-lg px-2.5 transition-colors hover:bg-ttb08-acc/6 has-focus-visible:outline-1 has-focus-visible:outline-offset-1 has-focus-visible:outline-dashed has-focus-visible:outline-ttb08-acc"><input class="sr-only" type="radio" name="ttb08" id="ttb08-r3"><span aria-hidden="true" class="relative z-10 size-3 flex-none rounded-full border-[1.5px] border-ttb08-acc/50 bg-ttb08-card transition-[background-color,border-color,box-shadow] group-has-checked/tab:border-ttb08-acc group-has-checked/tab:bg-ttb08-acc group-has-checked/tab:shadow-[0_0_10px_color-mix(in_oklab,var(--color-ttb08-acc)_60%,transparent)]"></span><span class="leading-tight"><span class="block text-[13px] font-semibold text-ttb08-mut transition-colors group-has-checked/tab:text-ttb08-acc-ink">Billing</span><span class="block text-[11px] text-ttb08-dim">Plan, invoices</span></span></label>
        <label class="group/tab relative flex h-12 cursor-pointer items-center gap-3 rounded-lg px-2.5 transition-colors hover:bg-ttb08-acc/6 has-focus-visible:outline-1 has-focus-visible:outline-offset-1 has-focus-visible:outline-dashed has-focus-visible:outline-ttb08-acc"><input class="sr-only" type="radio" name="ttb08" id="ttb08-r4"><span aria-hidden="true" class="relative z-10 size-3 flex-none rounded-full border-[1.5px] border-ttb08-acc/50 bg-ttb08-card transition-[background-color,border-color,box-shadow] group-has-checked/tab:border-ttb08-acc group-has-checked/tab:bg-ttb08-acc group-has-checked/tab:shadow-[0_0_10px_color-mix(in_oklab,var(--color-ttb08-acc)_60%,transparent)]"></span><span class="leading-tight"><span class="block text-[13px] font-semibold text-ttb08-mut transition-colors group-has-checked/tab:text-ttb08-acc-ink">Logs</span><span class="block text-[11px] text-ttb08-dim">Sessions, activity</span></span></label>
      </div>
      <div class="rounded-xl bg-white/[0.03] p-5 ring-1 ring-white/6">
        <div class="hidden group-has-[#ttb08-r1:checked]/tabs:block"><h3 class="text-lg font-bold">Profile</h3><p class="mt-1.5 text-sm leading-relaxed text-ttb08-mut">How you appear to teammates: display name, avatar and a short bio.</p></div>
        <div class="hidden group-has-[#ttb08-r2:checked]/tabs:block"><h3 class="text-lg font-bold">Account</h3><p class="mt-1.5 text-sm leading-relaxed text-ttb08-mut">Sign-in email, password and two-factor authentication.</p></div>
        <div class="hidden group-has-[#ttb08-r3:checked]/tabs:block"><h3 class="text-lg font-bold">Billing</h3><p class="mt-1.5 text-sm leading-relaxed text-ttb08-mut">Your current plan, payment method and downloadable invoices.</p></div>
        <div class="hidden group-has-[#ttb08-r4:checked]/tabs:block"><h3 class="text-lg font-bold">Logs</h3><p class="mt-1.5 text-sm leading-relaxed text-ttb08-mut">Active sessions and a 90-day record of account activity.</p></div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-ttb08-mono text-[11.5px] text-ttb08-mut">rail fill h-[calc((100%-48px)*var(--i)/3)] · group-has-checked/tab: dot</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb08-bg: #0b0f15;
  --color-ttb08-bg: oklch(0.167 0.014 258.4);
  --color-ttb08-card: #111821;
  --color-ttb08-card: oklch(0.206 0.021 254.9);
  --color-ttb08-ink: #eef4fa;
  --color-ttb08-ink: oklch(0.964 0.010 247.9);
  --color-ttb08-mut: #a7b3c2;
  --color-ttb08-mut: oklch(0.762 0.025 254.0);
  --color-ttb08-dim: #8794a5;
  --color-ttb08-dim: oklch(0.662 0.029 255.1);
  --color-ttb08-acc: #38bdf8;
  --color-ttb08-acc: oklch(0.754 0.139 232.7);
  --color-ttb08-acc-ink: #7dd3fc;
  --color-ttb08-acc-ink: oklch(0.828 0.101 230.3);
  --font-ttb08-sans: 'Geist', system-ui, sans-serif;
  --font-ttb08-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-08 {
  width: 100%;
  min-height: 100svh;
}
```

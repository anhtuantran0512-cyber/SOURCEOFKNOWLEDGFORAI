---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-step-progress-wizard-navbar/"
title: "Tailwind Step Progress Wizard Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "A checkout header: five steps, connector lines that fill behind completed ones, and a summary strip with a progress bar."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Step Progress Wizard Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-step-progress-wizard-navbar/

A checkout header: five steps, connector lines that fill behind completed ones, and a summary strip with a progress bar. Each step declares its own state as data-state="done|current|todo", and every visual — circle fill, label colour, connector — is a data-state-* variant, so advancing the flow means changing one attribute per step.
## HTML
```html
<div class="tnb-17 w-full min-h-svh bg-tnb17-page font-tnb17-sans text-tnb17-ink" style="--tnb17-progress:0.4" aria-label="Step progress wizard navbar demo">
  <header class="sticky top-0 z-100 border-b border-tnb17-edge bg-white shadow-[0_1px_4px_oklch(0_0_0/0.05)]">
    <div class="flex items-center justify-between border-b border-tnb17-edge px-5 py-3 md:px-8">
      <a href="#home" class="text-lg font-extrabold tracking-[-0.02em] text-tnb17-ink no-underline">Form<span class="text-tnb17-acc">Flow</span></a>
      <a href="#help" class="flex items-center gap-2 text-sm font-bold text-tnb17-mut no-underline transition-colors hover:text-tnb17-ink"><span aria-hidden="true">&#128172;</span>Need help?</a>
    </div>
    <ol class="flex items-center overflow-x-auto px-5 py-4 [scrollbar-width:none] md:px-8" aria-label="Checkout steps">
      <li data-state="done" class="peer/s1 flex shrink-0 items-center gap-3 rounded-[10px] px-3 py-1.5">
        <span data-state="done" class="grid size-8 shrink-0 place-items-center rounded-full border-2 border-tnb17-edge text-xs font-extrabold text-tnb17-mut transition-colors duration-300 data-[state=done]:border-tnb17-done data-[state=done]:bg-tnb17-done data-[state=done]:text-white" aria-hidden="true">&#10003;</span>
        <span class="grid max-sm:hidden"><span data-state="done" class="text-[11px] font-bold tracking-[0.04em] text-tnb17-mut uppercase data-[state=done]:text-tnb17-done">Step 1</span><span class="text-sm font-bold text-tnb17-ink">Account</span></span>
      </li>
      <span class="relative mx-1 h-0.5 min-w-8 flex-1 rounded-sm bg-tnb17-edge after:absolute after:inset-0 after:origin-left after:scale-x-0 after:rounded-sm after:bg-tnb17-done after:transition-transform after:duration-500 after:content-[''] peer-data-[state=done]/s1:after:scale-x-100 motion-reduce:after:transition-none sm:max-w-20"></span>
      <li data-state="done" class="peer/s2 flex shrink-0 items-center gap-3 rounded-[10px] px-3 py-1.5">
        <span data-state="done" class="grid size-8 shrink-0 place-items-center rounded-full border-2 border-tnb17-edge text-xs font-extrabold text-tnb17-mut transition-colors duration-300 data-[state=done]:border-tnb17-done data-[state=done]:bg-tnb17-done data-[state=done]:text-white" aria-hidden="true">&#10003;</span>
        <span class="grid max-sm:hidden"><span data-state="done" class="text-[11px] font-bold tracking-[0.04em] text-tnb17-mut uppercase data-[state=done]:text-tnb17-done">Step 2</span><span class="text-sm font-bold text-tnb17-ink">Profile</span></span>
      </li>
      <span class="relative mx-1 h-0.5 min-w-8 flex-1 rounded-sm bg-tnb17-edge after:absolute after:inset-0 after:origin-left after:scale-x-0 after:rounded-sm after:bg-tnb17-done after:transition-transform after:duration-500 after:content-[''] peer-data-[state=done]/s2:after:scale-x-100 motion-reduce:after:transition-none sm:max-w-20"></span>
      <li data-state="current" aria-current="step" class="peer/s3 flex shrink-0 items-center gap-3 rounded-[10px] px-3 py-1.5">
        <span data-state="current" class="grid size-8 shrink-0 place-items-center rounded-full border-2 border-tnb17-edge text-xs font-extrabold text-tnb17-mut transition-colors duration-300 data-[state=current]:border-tnb17-acc data-[state=current]:bg-tnb17-acc data-[state=current]:text-white">3</span>
        <span class="grid max-sm:hidden"><span data-state="current" class="text-[11px] font-bold tracking-[0.04em] text-tnb17-mut uppercase data-[state=current]:text-tnb17-acc">Step 3</span><span class="text-sm font-bold text-tnb17-ink">Payment</span></span>
      </li>
      <span class="relative mx-1 h-0.5 min-w-8 flex-1 rounded-sm bg-tnb17-edge after:absolute after:inset-0 after:origin-left after:scale-x-0 after:rounded-sm after:bg-tnb17-done after:transition-transform after:duration-500 after:content-[''] peer-data-[state=done]/s3:after:scale-x-100 motion-reduce:after:transition-none sm:max-w-20"></span>
      <li data-state="todo" class="peer/s4 flex shrink-0 items-center gap-3 rounded-[10px] px-3 py-1.5">
        <span class="grid size-8 shrink-0 place-items-center rounded-full border-2 border-tnb17-edge text-xs font-extrabold text-tnb17-mut">4</span>
        <span class="grid max-sm:hidden"><span class="text-[11px] font-bold tracking-[0.04em] text-tnb17-mut uppercase">Step 4</span><span class="text-sm font-bold text-tnb17-mut">Review</span></span>
      </li>
      <span class="relative mx-1 h-0.5 min-w-8 flex-1 rounded-sm bg-tnb17-edge after:absolute after:inset-0 after:origin-left after:scale-x-0 after:rounded-sm after:bg-tnb17-done after:transition-transform after:duration-500 after:content-[''] peer-data-[state=done]/s4:after:scale-x-100 motion-reduce:after:transition-none sm:max-w-20"></span>
      <li data-state="todo" class="flex shrink-0 items-center gap-3 rounded-[10px] px-3 py-1.5">
        <span class="grid size-8 shrink-0 place-items-center rounded-full border-2 border-tnb17-edge text-xs font-extrabold text-tnb17-mut">5</span>
        <span class="grid max-sm:hidden"><span class="text-[11px] font-bold tracking-[0.04em] text-tnb17-mut uppercase">Step 5</span><span class="text-sm font-bold text-tnb17-mut">Confirm</span></span>
      </li>
    </ol>
    <div class="flex items-center justify-between gap-4 border-t border-tnb17-acc/10 bg-tnb17-tint px-5 py-2.5 md:px-8">
      <p class="text-[13px] font-bold whitespace-nowrap text-tnb17-acc">Step 3 of 5 &mdash; Payment details</p>
      <div class="h-1.5 max-w-50 flex-1 overflow-hidden rounded-sm bg-tnb17-acc/15" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" aria-label="Checkout progress">
        <div class="h-full origin-left scale-x-[var(--tnb17-progress)] rounded-sm bg-tnb17-acc transition-transform duration-500 motion-reduce:transition-none"></div>
      </div>
      <button type="button" class="cursor-pointer border-0 bg-transparent text-[13px] font-bold whitespace-nowrap text-tnb17-mut transition-colors hover:text-tnb17-ink">Save &amp; exit</button>
    </div>
  </header>
  <main class="mx-auto max-w-xl px-5 py-12 md:px-8">
    <h1 class="mb-4 text-3xl font-extrabold tracking-[-0.03em] text-tnb17-ink">Step Progress Wizard</h1>
    <p class="text-lg leading-relaxed text-tnb17-mut">Each step owns its state as a <code class="rounded bg-tnb17-tint px-1.5 py-0.5 text-[0.9em] text-tnb17-acc">data-state</code> attribute; the connector after it fills only when that step reads <code class="rounded bg-tnb17-tint px-1.5 py-0.5 text-[0.9em] text-tnb17-acc">done</code>, via <code class="rounded bg-tnb17-tint px-1.5 py-0.5 text-[0.9em] text-tnb17-acc">peer-data-[state=done]:</code>.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb17-page: #f7f8fb;
  --color-tnb17-page: oklch(0.98 0.004 275);
  --color-tnb17-ink: #1e2337;
  --color-tnb17-ink: oklch(0.27 0.03 275);
  --color-tnb17-mut: #6f7793;
  --color-tnb17-mut: oklch(0.57 0.03 275);
  --color-tnb17-edge: #e5e8f0;
  --color-tnb17-edge: oklch(0.92 0.008 275);
  --color-tnb17-tint: #f0eeff;
  --color-tnb17-tint: oklch(0.95 0.02 285);
  --color-tnb17-acc: #5b4ef8;
  --color-tnb17-acc: oklch(0.53 0.24 283);
  --color-tnb17-done: #18a957;
  --color-tnb17-done: oklch(0.6 0.16 150);
  --font-tnb17-sans: 'Nunito Sans', system-ui, sans-serif;
}

.tnb-17 {
  width: 100%;
  min-height: 100svh;
}

.tnb-17 ::selection {
  background: var(--color-tnb17-acc);
  color: #fff;
}

.tnb-17 ol::-webkit-scrollbar {
  display: none;
}
```

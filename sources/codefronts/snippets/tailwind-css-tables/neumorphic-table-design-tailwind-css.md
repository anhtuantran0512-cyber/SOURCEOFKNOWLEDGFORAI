---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/neumorphic-table-design-tailwind-css/"
title: "Neumorphic Table Design in Tailwind CSS"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "A soft-UI product analytics grid where card, well, chips and quota rings are all sculpted from one surface colour by paired light/dark shadows — now @theme…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Table Design in Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-tables/neumorphic-table-design-tailwind-css/

A soft-UI product analytics grid where card, well, chips and quota rings are all sculpted from one surface colour by paired light/dark shadows — now @theme tokens (shadow-ttb12-out, shadow-ttb12-in) instead of repeated literals. Hover a row and its chips press in via group-hover/row:shadow-ttb12-in; quota rings are a single conic-gradient fed by a --pct custom property.
## HTML
```html
<section class="ttb-12 grid-cols-1 w-full min-h-svh grid place-items-center bg-ttb12-bg px-5 py-14 font-ttb12-sans text-ttb12-ink" aria-label="Neumorphic table demo">
  <div class="w-full max-w-4xl">
    <header class="mb-8 flex items-center gap-4">
      <span aria-hidden="true" class="grid size-12 place-items-center rounded-2xl text-ttb12-acc shadow-ttb12-out"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg></span>
      <div>
        <h2 class="text-[22px] font-extrabold tracking-tight">Product analytics</h2>
        <p class="mt-0.5 text-sm text-ttb12-mut">Q3 performance by module</p>
      </div>
    </header>
    <div class="rounded-[28px] p-2 shadow-ttb12-out-lg">
      <div class="relative overflow-x-auto rounded-[22px] shadow-ttb12-in-sm">
        <table class="w-full min-w-[640px] border-collapse text-left text-sm">
          <caption class="sr-only">Active users, revenue, trend and quota attainment by product module</caption>
          <thead class="[&_th]:border-b [&_th]:border-ttb12-dark/30 [&_th]:px-5 [&_th]:py-4 [&_th]:text-[10.5px] [&_th]:font-extrabold [&_th]:tracking-[0.16em] [&_th]:text-ttb12-mut [&_th]:uppercase [&_th:not(:first-child)]:text-center">
            <tr><th scope="col">Module</th><th scope="col">Active users</th><th scope="col">Revenue</th><th scope="col">Trend</th><th scope="col">Quota</th></tr>
          </thead>
          <tbody class="[&_td]:px-5 [&_td]:py-4 [&_td]:text-center [&_td]:align-middle [&_tr]:transition-colors [&_tr+tr]:border-t [&_tr+tr]:border-ttb12-dark/20 [&_tr:hover]:bg-ttb12-acc/[0.03]">
            <tr class="group/row">
              <th scope="row" class="px-5 py-4 text-left"><div class="flex items-center gap-3.5"><span aria-hidden="true" class="grid size-10 place-items-center rounded-xl text-xs font-black text-ttb12-acc shadow-ttb12-out-sm">CP</span><span><span class="block font-bold">Core Platform</span><span class="text-xs font-normal text-ttb12-mut">SaaS · Enterprise</span></span></div></th>
              <td><span class="inline-block rounded-full px-4 py-1.5 font-extrabold text-ttb12-acc-ink tabular-nums shadow-ttb12-out-sm transition-shadow duration-200 group-hover/row:shadow-ttb12-in-sm">18,440</span></td>
              <td><span class="inline-block rounded-full px-4 py-1.5 font-extrabold text-ttb12-green tabular-nums shadow-ttb12-out-sm transition-shadow duration-200 group-hover/row:shadow-ttb12-in-sm">$142K</span></td>
              <td><span class="inline-flex items-center gap-1 rounded-full px-3 py-1 text-xs font-bold text-ttb12-green shadow-ttb12-out-xs">▲ 12.4%</span></td>
              <td><span role="img" aria-label="82% of quota" style="--pct:82%;--c:var(--color-ttb12-acc)" class="relative mx-auto grid size-12 place-items-center rounded-full shadow-ttb12-out-sm [background:conic-gradient(var(--c)_var(--pct),transparent_0),var(--color-ttb12-bg)] after:absolute after:inset-[7px] after:rounded-full after:bg-ttb12-bg after:shadow-ttb12-in-xs"><span aria-hidden="true" class="relative z-10 text-[11px] font-black">82%</span></span></td>
            </tr>
            <tr class="group/row">
              <th scope="row" class="px-5 py-4 text-left"><div class="flex items-center gap-3.5"><span aria-hidden="true" class="grid size-10 place-items-center rounded-xl text-xs font-black text-ttb12-pink shadow-ttb12-out-sm">AI</span><span><span class="block font-bold">AI Copilot</span><span class="text-xs font-normal text-ttb12-mut">ML · Inference</span></span></div></th>
              <td><span class="inline-block rounded-full px-4 py-1.5 font-extrabold text-ttb12-pink tabular-nums shadow-ttb12-out-sm transition-shadow duration-200 group-hover/row:shadow-ttb12-in-sm">9,280</span></td>
              <td><span class="inline-block rounded-full px-4 py-1.5 font-extrabold text-ttb12-green tabular-nums shadow-ttb12-out-sm transition-shadow duration-200 group-hover/row:shadow-ttb12-in-sm">$87K</span></td>
              <td><span class="inline-flex items-center gap-1 rounded-full px-3 py-1 text-xs font-bold text-ttb12-green shadow-ttb12-out-xs">▲ 34.1%</span></td>
              <td><span role="img" aria-label="67% of quota" style="--pct:67%;--c:var(--color-ttb12-pink)" class="relative mx-auto grid size-12 place-items-center rounded-full shadow-ttb12-out-sm [background:conic-gradient(var(--c)_var(--pct),transparent_0),var(--color-ttb12-bg)] after:absolute after:inset-[7px] after:rounded-full after:bg-ttb12-bg after:shadow-ttb12-in-xs"><span aria-hidden="true" class="relative z-10 text-[11px] font-black">67%</span></span></td>
            </tr>
            <tr class="group/row">
              <th scope="row" class="px-5 py-4 text-left"><div class="flex items-center gap-3.5"><span aria-hidden="true" class="grid size-10 place-items-center rounded-xl text-xs font-black text-ttb12-green shadow-ttb12-out-sm">AH</span><span><span class="block font-bold">Analytics Hub</span><span class="text-xs font-normal text-ttb12-mut">BI · Reporting</span></span></div></th>
              <td><span class="inline-block rounded-full px-4 py-1.5 font-extrabold text-ttb12-green tabular-nums shadow-ttb12-out-sm transition-shadow duration-200 group-hover/row:shadow-ttb12-in-sm">5,190</span></td>
              <td><span class="inline-block rounded-full px-4 py-1.5 font-extrabold text-ttb12-orange tabular-nums shadow-ttb12-out-sm transition-shadow duration-200 group-hover/row:shadow-ttb12-in-sm">$31K</span></td>
              <td><span class="inline-flex items-center gap-1 rounded-full px-3 py-1 text-xs font-bold text-ttb12-orange shadow-ttb12-out-xs">▼ 3.2%</span></td>
              <td><span role="img" aria-label="41% of quota" style="--pct:41%;--c:var(--color-ttb12-orange)" class="relative mx-auto grid size-12 place-items-center rounded-full shadow-ttb12-out-sm [background:conic-gradient(var(--c)_var(--pct),transparent_0),var(--color-ttb12-bg)] after:absolute after:inset-[7px] after:rounded-full after:bg-ttb12-bg after:shadow-ttb12-in-xs"><span aria-hidden="true" class="relative z-10 text-[11px] font-black">41%</span></span></td>
            </tr>
            <tr class="group/row">
              <th scope="row" class="px-5 py-4 text-left"><div class="flex items-center gap-3.5"><span aria-hidden="true" class="grid size-10 place-items-center rounded-xl text-xs font-black text-ttb12-orange shadow-ttb12-out-sm">AS</span><span><span class="block font-bold">Auth Shield</span><span class="text-xs font-normal text-ttb12-mut">Security · IAM</span></span></div></th>
              <td><span class="inline-block rounded-full px-4 py-1.5 font-extrabold text-ttb12-orange tabular-nums shadow-ttb12-out-sm transition-shadow duration-200 group-hover/row:shadow-ttb12-in-sm">22,100</span></td>
              <td><span class="inline-block rounded-full px-4 py-1.5 font-extrabold text-ttb12-green tabular-nums shadow-ttb12-out-sm transition-shadow duration-200 group-hover/row:shadow-ttb12-in-sm">$58K</span></td>
              <td><span class="inline-flex items-center gap-1 rounded-full px-3 py-1 text-xs font-bold text-ttb12-green shadow-ttb12-out-xs">▲ 8.7%</span></td>
              <td><span role="img" aria-label="95% of quota" style="--pct:95%;--c:var(--color-ttb12-green)" class="relative mx-auto grid size-12 place-items-center rounded-full shadow-ttb12-out-sm [background:conic-gradient(var(--c)_var(--pct),transparent_0),var(--color-ttb12-bg)] after:absolute after:inset-[7px] after:rounded-full after:bg-ttb12-bg after:shadow-ttb12-in-xs"><span aria-hidden="true" class="relative z-10 text-[11px] font-black">95%</span></span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb12-bg: #e6e9f0;
  --color-ttb12-bg: oklch(0.93 0.01 265);
  --color-ttb12-dark: #a3aabe;
  --color-ttb12-dark: oklch(0.74 0.03 265);
  --color-ttb12-ink: #262b48;
  --color-ttb12-ink: oklch(0.29 0.05 275);
  --color-ttb12-mut: #5e6687;
  --color-ttb12-mut: oklch(0.5 0.05 275);
  --color-ttb12-acc: #6c63ff;
  --color-ttb12-acc: oklch(0.58 0.22 280);
  --color-ttb12-acc-ink: #5148e0;
  --color-ttb12-acc-ink: oklch(0.5 0.22 280);
  --color-ttb12-pink: #d63c79;
  --color-ttb12-pink: oklch(0.58 0.19 360);
  --color-ttb12-green: #13857a;
  --color-ttb12-green: oklch(0.55 0.1 180);
  --color-ttb12-orange: #d4542a;
  --color-ttb12-orange: oklch(0.6 0.17 40);
  --font-ttb12-sans: 'Nunito', system-ui, sans-serif;
  --shadow-ttb12-out-lg: 12px 12px 28px var(--color-ttb12-dark), -12px -12px 28px #ffffff;
  --shadow-ttb12-out: 6px 6px 14px var(--color-ttb12-dark), -6px -6px 14px #ffffff;
  --shadow-ttb12-out-sm: 4px 4px 10px var(--color-ttb12-dark), -4px -4px 10px #ffffff;
  --shadow-ttb12-out-xs: 3px 3px 7px var(--color-ttb12-dark), -3px -3px 7px #ffffff;
  --shadow-ttb12-in-sm: inset 4px 4px 10px var(--color-ttb12-dark), inset -4px -4px 10px #ffffff;
  --shadow-ttb12-in-xs: inset 2px 2px 5px var(--color-ttb12-dark), inset -2px -2px 5px #ffffff;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-12 {
  width: 100%;
  min-height: 100svh;
}
```

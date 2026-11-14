---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-vertical-tabs-with-has-active-state-has-checked-variant/"
title: "Tailwind Vertical Tabs with :has() Active State (has-checked Variant)"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A design-studio card whose whole surface re-themes per tab &mdash; border, ambient glow, rail highlight, copy and illustrations &mdash; from one arbitrary…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Tabs with :has() Active State (has-checked Variant)
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-vertical-tabs-with-has-active-state-has-checked-variant/

A design-studio card whose whole surface re-themes per tab &mdash; border, ambient glow, rail highlight, copy and illustrations &mdash; from one arbitrary property per tab: has-[#tvt-13-t3:checked]:[--color-tvt13-acc:var(--color-tvt13-mo)]. Because :has() reads state upward, the radio rail sits after the panels in the source, and a registered @property colour makes the hue itself animate from cyan to orange to magenta to lime.
## HTML
```html
<section class="tvt-13 w-full min-h-svh grid place-items-center bg-tvt13-bg px-4 py-14 font-tvt13-sans text-tvt13-ink antialiased sm:px-6" aria-label="Tailwind vertical tabs with :has() active state demo">
  <div class="@container w-full max-w-[58rem]">
    <div class="group/card relative isolate grid grid-cols-[minmax(12rem,15.5rem)_minmax(0,1fr)] grid-rows-[auto_1fr] overflow-hidden rounded-[24px] bg-tvt13-card shadow-tvt13-card ring-1 ring-tvt13-acc/30 transition-[--color-tvt13-acc,--color-tvt13-acc-ink,--tvt13-spot,opacity,translate] duration-500 ease-[cubic-bezier(.32,.72,.3,1)] [--tvt13-spot:12%] before:pointer-events-none before:absolute before:inset-0 before:-z-10 before:bg-[radial-gradient(45%_70%_at_var(--tvt13-spot)_0%,color-mix(in_oklab,var(--color-tvt13-acc)_24%,transparent),transparent_75%)] has-[#tvt-13-t1:checked]:[--color-tvt13-acc:var(--color-tvt13-res)] has-[#tvt-13-t1:checked]:[--color-tvt13-acc-ink:var(--color-tvt13-res-ink)] has-[#tvt-13-t2:checked]:[--color-tvt13-acc:var(--color-tvt13-ui)] has-[#tvt-13-t2:checked]:[--color-tvt13-acc-ink:var(--color-tvt13-ui-ink)] has-[#tvt-13-t2:checked]:[--tvt13-spot:38%] has-[#tvt-13-t3:checked]:[--color-tvt13-acc:var(--color-tvt13-mo)] has-[#tvt-13-t3:checked]:[--color-tvt13-acc-ink:var(--color-tvt13-mo-ink)] has-[#tvt-13-t3:checked]:[--tvt13-spot:64%] has-[#tvt-13-t4:checked]:[--color-tvt13-acc:var(--color-tvt13-sys)] has-[#tvt-13-t4:checked]:[--color-tvt13-acc-ink:var(--color-tvt13-sys-ink)] has-[#tvt-13-t4:checked]:[--tvt13-spot:88%] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none @max-[40rem]:grid-cols-1 @max-[40rem]:grid-rows-[auto_auto_1fr]">
      <header class="col-span-full flex flex-wrap items-end justify-between @max-[40rem]:block @max-[40rem]:[&>p]:mt-3 gap-x-6 gap-y-3 border-b border-tvt13-line px-5 py-6 sm:px-8">
        <div class="grid gap-2">
          <p class="flex items-center gap-2 font-tvt13-mono text-[11.5px] tracking-[0.14em] text-tvt13-acc-ink uppercase"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt13-acc shadow-[0_0_10px] shadow-tvt13-acc"></span>:has() · the parent selector</p>
          <h2 class="text-[clamp(24px,3.6vw,34px)] leading-[1.06] font-extrabold tracking-[-0.04em] text-balance">The container reacts, <span class="text-tvt13-acc-ink">not just the panel</span></h2>
        </div>
        <p class="max-w-[34ch] text-[13.5px] leading-relaxed text-tvt13-mut text-pretty">Pick a discipline: the border, glow, rail and copy all re-theme from one custom property.</p>
      </header>

      <div class="relative col-start-2 row-start-2 grid p-5 sm:p-8 @max-[40rem]:col-start-1 @max-[40rem]:row-start-3">

        <article aria-labelledby="tvt-13-h1" class="invisible col-start-1 row-start-1 grid translate-y-2 content-start gap-5 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-13-t1:checked]/card:visible group-has-[#tvt-13-t1:checked]/card:translate-y-0 group-has-[#tvt-13-t1:checked]/card:opacity-100 motion-reduce:transition-none">
          <div class="grid gap-2">
            <p class="font-tvt13-mono text-[11.5px] tracking-[0.14em] text-tvt13-acc-ink uppercase">Research</p>
            <h3 id="tvt-13-h1" class="text-[clamp(21px,2.6vw,27px)] leading-tight font-bold tracking-[-0.03em] text-balance">Listen before you draw</h3>
            <p class="max-w-[50ch] text-[14.5px] leading-relaxed text-tvt13-mut text-pretty">Every engagement starts with interviews. The quotes that keep coming up become the brief &mdash; not the loudest stakeholder.</p>
          </div>
          <div aria-hidden="true" class="rounded-2xl bg-tvt13-well p-4 ring-1 ring-tvt13-line">
            <div class="grid grid-cols-3 gap-3 max-[460px]:grid-cols-1"><figure class="rounded-xl bg-tvt13-card p-3 shadow-tvt13-note ring-1 ring-tvt13-line rotate-[-1.5deg]"><blockquote class="text-[12.5px] leading-snug">“I export to a spreadsheet every Friday just to see totals.”</blockquote><figcaption class="mt-2 flex items-center gap-1.5 font-tvt13-mono text-[10.5px] text-tvt13-mut"><span class="size-1.5 rounded-full bg-tvt13-acc"></span>P07 · finance lead</figcaption></figure><figure class="rounded-xl bg-tvt13-card p-3 shadow-tvt13-note ring-1 ring-tvt13-line rotate-[1deg]"><blockquote class="text-[12.5px] leading-snug">“I never know which version my team is looking at.”</blockquote><figcaption class="mt-2 flex items-center gap-1.5 font-tvt13-mono text-[10.5px] text-tvt13-mut"><span class="size-1.5 rounded-full bg-tvt13-acc"></span>P12 · designer</figcaption></figure><figure class="rounded-xl bg-tvt13-card p-3 shadow-tvt13-note ring-1 ring-tvt13-line rotate-[-0.5deg]"><blockquote class="text-[12.5px] leading-snug">“Search is how I navigate. The sidebar is decoration.”</blockquote><figcaption class="mt-2 flex items-center gap-1.5 font-tvt13-mono text-[10.5px] text-tvt13-mut"><span class="size-1.5 rounded-full bg-tvt13-acc"></span>P19 · engineer</figcaption></figure></div>
            <p class="mt-3 flex flex-wrap gap-x-4 gap-y-1 font-tvt13-mono text-[11px] text-tvt13-mut"><span><b class="text-tvt13-ink">38</b> interviews</span><span><b class="text-tvt13-ink">6</b> markets</span><span><b class="text-tvt13-ink">212</b> tagged insights</span></p>
          </div>
          <p class="justify-self-start rounded-full bg-tvt13-acc/10 px-3 py-1.5 font-tvt13-mono text-[11.5px] text-tvt13-acc-ink ring-1 ring-tvt13-acc/25 ring-inset">.card:has(#t1:checked){--acc: cyan}</p>
        </article>

        <article aria-labelledby="tvt-13-h2" class="invisible col-start-1 row-start-1 grid translate-y-2 content-start gap-5 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-13-t2:checked]/card:visible group-has-[#tvt-13-t2:checked]/card:translate-y-0 group-has-[#tvt-13-t2:checked]/card:opacity-100 motion-reduce:transition-none">
          <div class="grid gap-2">
            <p class="font-tvt13-mono text-[11.5px] tracking-[0.14em] text-tvt13-acc-ink uppercase">Interface</p>
            <h3 id="tvt-13-h2" class="text-[clamp(21px,2.6vw,27px)] leading-tight font-bold tracking-[-0.03em] text-balance">Pixels with a purpose</h3>
            <p class="max-w-[50ch] text-[14.5px] leading-relaxed text-tvt13-mut text-pretty">Wireframes are tested with real copy and real data lengths, so nothing breaks the day the marketing team writes the headline.</p>
          </div>
          <div aria-hidden="true" class="rounded-2xl bg-tvt13-well p-4 ring-1 ring-tvt13-line">
            <div class="grid grid-cols-[4.5rem_1fr] gap-3 rounded-xl bg-tvt13-card p-3 ring-1 ring-tvt13-line">
              <div class="grid content-start gap-2"><span class="h-2 rounded-full bg-tvt13-acc"></span><span class="h-2 w-4/5 rounded-full bg-tvt13-line"></span><span class="h-2 w-3/5 rounded-full bg-tvt13-line"></span><span class="h-2 w-4/5 rounded-full bg-tvt13-line"></span></div>
              <div class="grid gap-2.5">
                <div class="flex items-center justify-between"><span class="h-2.5 w-24 rounded-full bg-tvt13-ink/70"></span><span class="h-6 w-16 rounded-lg bg-tvt13-acc"></span></div>
                <div class="grid grid-cols-3 gap-2"><span class="h-12 rounded-lg bg-tvt13-acc/15 ring-1 ring-tvt13-acc/30"></span><span class="h-12 rounded-lg bg-tvt13-well ring-1 ring-tvt13-line"></span><span class="h-12 rounded-lg bg-tvt13-well ring-1 ring-tvt13-line"></span></div>
                <span class="h-2 w-11/12 rounded-full bg-tvt13-line"></span><span class="h-2 w-2/3 rounded-full bg-tvt13-line"></span>
              </div>
            </div>
            <p class="mt-3 flex flex-wrap gap-x-4 gap-y-1 font-tvt13-mono text-[11px] text-tvt13-mut"><span><b class="text-tvt13-ink">64</b> screens</span><span><b class="text-tvt13-ink">AA</b> contrast, both themes</span><span><b class="text-tvt13-ink">44px</b> targets</span></p>
          </div>
          <p class="justify-self-start rounded-full bg-tvt13-acc/10 px-3 py-1.5 font-tvt13-mono text-[11.5px] text-tvt13-acc-ink ring-1 ring-tvt13-acc/25 ring-inset">.card:has(#t2:checked){--acc: orange}</p>
        </article>

        <article aria-labelledby="tvt-13-h3" class="invisible col-start-1 row-start-1 grid translate-y-2 content-start gap-5 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-13-t3:checked]/card:visible group-has-[#tvt-13-t3:checked]/card:translate-y-0 group-has-[#tvt-13-t3:checked]/card:opacity-100 motion-reduce:transition-none">
          <div class="grid gap-2">
            <p class="font-tvt13-mono text-[11.5px] tracking-[0.14em] text-tvt13-acc-ink uppercase">Motion</p>
            <h3 id="tvt-13-h3" class="text-[clamp(21px,2.6vw,27px)] leading-tight font-bold tracking-[-0.03em] text-balance">Timing is a feature</h3>
            <p class="max-w-[50ch] text-[14.5px] leading-relaxed text-tvt13-mut text-pretty">Easing curves are specified, named and shipped as tokens. A 7% overshoot reads as confident; a linear fade reads as a loading state.</p>
          </div>
          <div aria-hidden="true" class="rounded-2xl bg-tvt13-well p-4 ring-1 ring-tvt13-line">
            <svg viewBox="0 0 320 120" class="h-28 w-full text-tvt13-acc" focusable="false">
              <path d="M20 100H300M20 100V12" fill="none" stroke="var(--color-tvt13-line)" stroke-width="1.5"/>
              <path d="M20 100C110 100 120 8 300 12" fill="none" stroke="currentColor" stroke-opacity=".25" stroke-width="8" stroke-linecap="round"/>
              <path d="M20 100C110 100 120 8 300 12" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
              <path d="M20 100 110 100M300 12 120 8" stroke="var(--color-tvt13-mut)" stroke-dasharray="3 4" stroke-width="1.2"/>
              <circle cx="110" cy="100" r="5" fill="var(--color-tvt13-card)" stroke="currentColor" stroke-width="2"/><circle cx="120" cy="8" r="5" fill="var(--color-tvt13-card)" stroke="currentColor" stroke-width="2"/>
              <circle r="6" fill="currentColor" class="motion-safe:animate-tvt13-ride [offset-path:path('M20_100C110_100_120_8_300_12')]"/>
            </svg>
            <p class="mt-1 flex flex-wrap gap-x-4 gap-y-1 font-tvt13-mono text-[11px] text-tvt13-mut"><span>cubic-bezier(.3, 0, .1, 1)</span><span><b class="text-tvt13-ink">240ms</b> enter</span><span><b class="text-tvt13-ink">160ms</b> exit</span></p>
          </div>
          <p class="justify-self-start rounded-full bg-tvt13-acc/10 px-3 py-1.5 font-tvt13-mono text-[11.5px] text-tvt13-acc-ink ring-1 ring-tvt13-acc/25 ring-inset">.card:has(#t3:checked){--acc: magenta}</p>
        </article>

        <article aria-labelledby="tvt-13-h4" class="invisible col-start-1 row-start-1 grid translate-y-2 content-start gap-5 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-13-t4:checked]/card:visible group-has-[#tvt-13-t4:checked]/card:translate-y-0 group-has-[#tvt-13-t4:checked]/card:opacity-100 motion-reduce:transition-none">
          <div class="grid gap-2">
            <p class="font-tvt13-mono text-[11.5px] tracking-[0.14em] text-tvt13-acc-ink uppercase">Systems</p>
            <h3 id="tvt-13-h4" class="text-[clamp(21px,2.6vw,27px)] leading-tight font-bold tracking-[-0.03em] text-balance">One source of truth</h3>
            <p class="max-w-[50ch] text-[14.5px] leading-relaxed text-tvt13-mut text-pretty">Tokens, components and documentation versioned together, so a colour change is a pull request, not a scavenger hunt.</p>
          </div>
          <div aria-hidden="true" class="rounded-2xl bg-tvt13-well p-4 ring-1 ring-tvt13-line">
            <div class="grid grid-cols-5 gap-2"><span class="grid gap-1.5"><span class="h-10 rounded-lg bg-tvt13-acc ring-1 ring-tvt13-line"></span><span class="font-tvt13-mono text-[10px] text-tvt13-mut">accent</span></span><span class="grid gap-1.5"><span class="h-10 rounded-lg bg-tvt13-acc/60 ring-1 ring-tvt13-line"></span><span class="font-tvt13-mono text-[10px] text-tvt13-mut">accent/60</span></span><span class="grid gap-1.5"><span class="h-10 rounded-lg bg-tvt13-acc/25 ring-1 ring-tvt13-line"></span><span class="font-tvt13-mono text-[10px] text-tvt13-mut">accent/25</span></span><span class="grid gap-1.5"><span class="h-10 rounded-lg bg-tvt13-ink ring-1 ring-tvt13-line"></span><span class="font-tvt13-mono text-[10px] text-tvt13-mut">ink</span></span><span class="grid gap-1.5"><span class="h-10 rounded-lg bg-tvt13-card ring-1 ring-tvt13-line"></span><span class="font-tvt13-mono text-[10px] text-tvt13-mut">surface</span></span></div>
            <div class="mt-3 flex flex-wrap items-center gap-2"><span class="rounded-lg bg-tvt13-acc px-3 py-1.5 text-[12px] font-semibold text-tvt13-on">Primary</span><span class="rounded-lg px-3 py-1.5 text-[12px] font-semibold text-tvt13-acc-ink ring-1 ring-tvt13-acc/40">Secondary</span><span class="rounded-full bg-tvt13-acc/12 px-2.5 py-1 font-tvt13-mono text-[10.5px] text-tvt13-acc-ink">v3.2 tokens</span><span class="ms-auto font-tvt13-mono text-[11px] text-tvt13-mut"><b class="text-tvt13-ink">148</b> components</span></div>
          </div>
          <p class="justify-self-start rounded-full bg-tvt13-acc/10 px-3 py-1.5 font-tvt13-mono text-[11.5px] text-tvt13-acc-ink ring-1 ring-tvt13-acc/25 ring-inset">.card:has(#t4:checked){--acc: lime}</p>
        </article>
      </div>

      <!-- The rail comes AFTER the panels in source order. :has() does not care. -->
      <div role="radiogroup" aria-label="Studio disciplines" class="col-start-1 row-start-2 flex flex-col gap-1 border-e border-tvt13-line p-3 @max-[40rem]:row-start-2 @max-[40rem]:grid @max-[40rem]:grid-cols-2 @max-[40rem]:gap-1.5 @max-[40rem]:border-e-0 @max-[40rem]:border-b">

          <label class="group/tab relative flex min-h-14 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-4 text-[15px] font-semibold text-tvt13-mut hover:bg-tvt13-ink/[0.05] hover:text-tvt13-ink has-checked:bg-tvt13-acc/12 has-checked:text-tvt13-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt13-acc motion-reduce:transition-none @max-[40rem]:min-h-11 @max-[40rem]:rounded-full @max-[40rem]:px-3.5 @max-[40rem]:text-[14px]">
            <input type="radio" name="tvt-13-tabs" id="tvt-13-t1" class="sr-only" checked>
            <span aria-hidden="true" class="size-2 shrink-0 rounded-full bg-current opacity-35 transition-[opacity,box-shadow] duration-300 group-has-checked/tab:opacity-100 group-has-checked/tab:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tvt13-acc)_25%,transparent)]"></span>
            <span class="flex-1">Research</span>
            <span class="font-tvt13-mono text-[11px] font-normal text-tvt13-mut tabular-nums @max-[40rem]:hidden">38</span>
          </label>

          <label class="group/tab relative flex min-h-14 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-4 text-[15px] font-semibold text-tvt13-mut hover:bg-tvt13-ink/[0.05] hover:text-tvt13-ink has-checked:bg-tvt13-acc/12 has-checked:text-tvt13-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt13-acc motion-reduce:transition-none @max-[40rem]:min-h-11 @max-[40rem]:rounded-full @max-[40rem]:px-3.5 @max-[40rem]:text-[14px]">
            <input type="radio" name="tvt-13-tabs" id="tvt-13-t2" class="sr-only">
            <span aria-hidden="true" class="size-2 shrink-0 rounded-full bg-current opacity-35 transition-[opacity,box-shadow] duration-300 group-has-checked/tab:opacity-100 group-has-checked/tab:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tvt13-acc)_25%,transparent)]"></span>
            <span class="flex-1">Interface</span>
            <span class="font-tvt13-mono text-[11px] font-normal text-tvt13-mut tabular-nums @max-[40rem]:hidden">64</span>
          </label>

          <label class="group/tab relative flex min-h-14 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-4 text-[15px] font-semibold text-tvt13-mut hover:bg-tvt13-ink/[0.05] hover:text-tvt13-ink has-checked:bg-tvt13-acc/12 has-checked:text-tvt13-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt13-acc motion-reduce:transition-none @max-[40rem]:min-h-11 @max-[40rem]:rounded-full @max-[40rem]:px-3.5 @max-[40rem]:text-[14px]">
            <input type="radio" name="tvt-13-tabs" id="tvt-13-t3" class="sr-only">
            <span aria-hidden="true" class="size-2 shrink-0 rounded-full bg-current opacity-35 transition-[opacity,box-shadow] duration-300 group-has-checked/tab:opacity-100 group-has-checked/tab:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tvt13-acc)_25%,transparent)]"></span>
            <span class="flex-1">Motion</span>
            <span class="font-tvt13-mono text-[11px] font-normal text-tvt13-mut tabular-nums @max-[40rem]:hidden">21</span>
          </label>

          <label class="group/tab relative flex min-h-14 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-4 text-[15px] font-semibold text-tvt13-mut hover:bg-tvt13-ink/[0.05] hover:text-tvt13-ink has-checked:bg-tvt13-acc/12 has-checked:text-tvt13-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt13-acc motion-reduce:transition-none @max-[40rem]:min-h-11 @max-[40rem]:rounded-full @max-[40rem]:px-3.5 @max-[40rem]:text-[14px]">
            <input type="radio" name="tvt-13-tabs" id="tvt-13-t4" class="sr-only">
            <span aria-hidden="true" class="size-2 shrink-0 rounded-full bg-current opacity-35 transition-[opacity,box-shadow] duration-300 group-has-checked/tab:opacity-100 group-has-checked/tab:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tvt13-acc)_25%,transparent)]"></span>
            <span class="flex-1">Systems</span>
            <span class="font-tvt13-mono text-[11px] font-normal text-tvt13-mut tabular-nums @max-[40rem]:hidden">148</span>
          </label>
        <p class="mt-auto px-4 pt-6 pb-2 text-[12px] leading-relaxed text-tvt13-mut @max-[40rem]:hidden">The rail sits after the panels in the source &mdash; better reading order, same control.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt13-bg: #f2f4f9;
  --color-tvt13-bg: oklch(0.968 0.006 265);
  --color-tvt13-card: #fefeff;
  --color-tvt13-card: oklch(0.998 0.002 265);
  --color-tvt13-well: #f5f7fb;
  --color-tvt13-well: oklch(0.975 0.006 265);
  --color-tvt13-ink: #151a26;
  --color-tvt13-ink: oklch(0.22 0.025 265);
  --color-tvt13-mut: #585e69;
  --color-tvt13-mut: oklch(0.48 0.02 265);
  --color-tvt13-line: #dee1e8;
  --color-tvt13-line: oklch(0.91 0.01 265);
  --color-tvt13-on: #fcfcfc;
  --color-tvt13-on: oklch(0.99 0 0);
  --color-tvt13-acc: #0090a8;
  --color-tvt13-acc: oklch(0.6 0.12 215);
  --color-tvt13-acc-ink: #006880;
  --color-tvt13-acc-ink: oklch(0.48 0.1 220);
  --color-tvt13-res: #0090a8;
  --color-tvt13-res: oklch(0.6 0.12 215);
  --color-tvt13-res-ink: #006880;
  --color-tvt13-res-ink: oklch(0.48 0.1 220);
  --color-tvt13-ui: #e15f0a;
  --color-tvt13-ui: oklch(0.64 0.18 45);
  --color-tvt13-ui-ink: #af4000;
  --color-tvt13-ui-ink: oklch(0.52 0.16 42);
  --color-tvt13-mo: #c72da2;
  --color-tvt13-mo: oklch(0.58 0.22 340);
  --color-tvt13-mo-ink: #a90e88;
  --color-tvt13-mo-ink: oklch(0.5 0.21 340);
  --color-tvt13-sys: #31983d;
  --color-tvt13-sys: oklch(0.6 0.16 145);
  --color-tvt13-sys-ink: #0e6d2c;
  --color-tvt13-sys-ink: oklch(0.47 0.13 148);
  --font-tvt13-sans: 'Manrope', system-ui, sans-serif;
  --font-tvt13-mono: 'Fira Code', ui-monospace, monospace;
  --shadow-tvt13-card: 0 1px 2px oklch(0.2 0.02 265 / 0.06), 0 34px 80px -36px oklch(0.25 0.03 265 / 0.45);
  --shadow-tvt13-note: 0 10px 22px -14px oklch(0.2 0.03 265 / 0.45);
  --animate-tvt13-ride: tvt13-ride 2.6s cubic-bezier(0.3, 0, 0.1, 1) infinite;

  @keyframes tvt13-ride {
    0%,
        12% {
      offset-distance: 0%;
    }

    70%,
        100% {
      offset-distance: 100%;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-13 {
  width: 100%;
  min-height: 100svh;
}
/* @property is an at-rule utilities can't emit: registering the accent as a <color> and the glow
   position as a <percentage> is what lets the card's transition glide the hue instead of snapping it. */

@property --color-tvt13-acc {
  syntax: '<color>';
  inherits: true;
  initial-value: #0891b2;
}

@property --color-tvt13-acc-ink {
  syntax: '<color>';
  inherits: true;
  initial-value: #0e7490;
}

@property --tvt13-spot {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 12%;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-13:not([data-theme="light"]) {
    --color-tvt13-bg: #090c13;
    --color-tvt13-bg: oklch(0.155 0.015 265);
    --color-tvt13-card: #12161f;
    --color-tvt13-card: oklch(0.2 0.02 265);
    --color-tvt13-well: #0d1019;
    --color-tvt13-well: oklch(0.175 0.018 265);
    --color-tvt13-ink: #f1f3f8;
    --color-tvt13-ink: oklch(0.965 0.006 265);
    --color-tvt13-mut: #a8aeba;
    --color-tvt13-mut: oklch(0.75 0.018 265);
    --color-tvt13-line: #282e3b;
    --color-tvt13-line: oklch(0.3 0.025 265);
    --color-tvt13-on: #0b0f18;
    --color-tvt13-on: oklch(0.17 0.02 265);
    --color-tvt13-acc: #00d6e7;
    --color-tvt13-acc: oklch(0.8 0.14 205);
    --color-tvt13-acc-ink: #55e1f0;
    --color-tvt13-acc-ink: oklch(0.84 0.12 205);
    --color-tvt13-res: #00d6e7;
    --color-tvt13-res: oklch(0.8 0.14 205);
    --color-tvt13-res-ink: #55e1f0;
    --color-tvt13-res-ink: oklch(0.84 0.12 205);
    --color-tvt13-ui: #ff9a5f;
    --color-tvt13-ui: oklch(0.78 0.16 50);
    --color-tvt13-ui-ink: #ffaf78;
    --color-tvt13-ui-ink: oklch(0.82 0.14 55);
    --color-tvt13-mo: #f674d0;
    --color-tvt13-mo: oklch(0.74 0.19 340);
    --color-tvt13-mo-ink: #fd95dc;
    --color-tvt13-mo-ink: oklch(0.8 0.15 340);
    --color-tvt13-sys: #86e670;
    --color-tvt13-sys: oklch(0.84 0.18 140);
    --color-tvt13-sys-ink: #96ea83;
    --color-tvt13-sys-ink: oklch(0.86 0.16 140);
  }
}

.tvt-13[data-theme="dark"] {
  --color-tvt13-bg: #090c13;
  --color-tvt13-bg: oklch(0.155 0.015 265);
  --color-tvt13-card: #12161f;
  --color-tvt13-card: oklch(0.2 0.02 265);
  --color-tvt13-well: #0d1019;
  --color-tvt13-well: oklch(0.175 0.018 265);
  --color-tvt13-ink: #f1f3f8;
  --color-tvt13-ink: oklch(0.965 0.006 265);
  --color-tvt13-mut: #a8aeba;
  --color-tvt13-mut: oklch(0.75 0.018 265);
  --color-tvt13-line: #282e3b;
  --color-tvt13-line: oklch(0.3 0.025 265);
  --color-tvt13-on: #0b0f18;
  --color-tvt13-on: oklch(0.17 0.02 265);
  --color-tvt13-acc: #00d6e7;
  --color-tvt13-acc: oklch(0.8 0.14 205);
  --color-tvt13-acc-ink: #55e1f0;
  --color-tvt13-acc-ink: oklch(0.84 0.12 205);
  --color-tvt13-res: #00d6e7;
  --color-tvt13-res: oklch(0.8 0.14 205);
  --color-tvt13-res-ink: #55e1f0;
  --color-tvt13-res-ink: oklch(0.84 0.12 205);
  --color-tvt13-ui: #ff9a5f;
  --color-tvt13-ui: oklch(0.78 0.16 50);
  --color-tvt13-ui-ink: #ffaf78;
  --color-tvt13-ui-ink: oklch(0.82 0.14 55);
  --color-tvt13-mo: #f674d0;
  --color-tvt13-mo: oklch(0.74 0.19 340);
  --color-tvt13-mo-ink: #fd95dc;
  --color-tvt13-mo-ink: oklch(0.8 0.15 340);
  --color-tvt13-sys: #86e670;
  --color-tvt13-sys: oklch(0.84 0.18 140);
  --color-tvt13-sys-ink: #96ea83;
  --color-tvt13-sys-ink: oklch(0.86 0.16 140);
}
```

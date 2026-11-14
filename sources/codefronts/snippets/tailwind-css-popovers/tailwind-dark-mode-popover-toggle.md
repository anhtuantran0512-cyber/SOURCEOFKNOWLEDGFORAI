---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-popovers/tailwind-dark-mode-popover-toggle/"
title: "Tailwind Dark Mode Popover Toggle"
section: "snippets"
category: "tailwind-css-popovers"
category_name: "Tailwind CSS Popovers"
description: "One number drives the whole theme."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Popover Toggle
Source: https://codefronts.com/snippets/tailwind-css-popovers/tailwind-dark-mode-popover-toggle/

One number drives the whole theme. @theme inline defines every colour as color-mix(light, dark, var(--tpop19-d)); the root sets --tpop19-d to 0 or 1 with four utilities — dark:, has-checked: and dark:has-checked: for the flip-back — and because --tpop19-d is a registered @property, the root can transition it: the page and the open popover crossfade between palettes in the same frame, zero JS.
## HTML
```html
<section class="tpop-19 group/root w-full min-h-svh bg-tpop19-page px-4.5 py-9.5 font-tpop19-sans text-tpop19-ink transition-[--tpop19-d] duration-500 ease-in-out motion-reduce:transition-none dark:[--tpop19-d:1] has-checked:[--tpop19-d:1] dark:has-checked:[--tpop19-d:0]" aria-label="Dark and light mode popover demo">
  <div class="grid min-h-[calc(100svh-76px)] max-w-full place-items-center">
    <div class="w-full min-w-0 max-w-[27rem] rounded-2xl border border-tpop19-rule bg-tpop19-panel p-4.5 shadow-[0_18px_40px_-30px_oklch(0_0_0/0.45)]">
      <div class="mb-3.5 flex flex-wrap items-center justify-between gap-2.5">
        <p class="text-[10.5px] font-bold uppercase tracking-[0.2em] text-tpop19-mut">Appearance</p>
        <div class="relative flex">
          <input id="tpop-19-switch" type="checkbox" class="peer sr-only">
          <label for="tpop-19-switch" class="inline-flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full border border-tpop19-rule px-3 text-[11.5px] font-bold uppercase tracking-[0.12em] text-tpop19-ink select-none peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tpop19-acc">
            <span aria-hidden="true" class="relative h-4.5 w-8 flex-none rounded-full bg-tpop19-rule">
              <span class="absolute top-0.5 left-0.5 grid size-3.5 place-items-center rounded-full bg-tpop19-ink text-tpop19-panel transition-transform duration-200 motion-reduce:transition-none group-has-checked/root:translate-x-3.5 dark:translate-x-3.5 dark:group-has-checked/root:translate-x-0"></span>
            </span>
            <span class="group-has-checked/root:hidden dark:hidden dark:group-has-checked/root:inline">Light</span>
            <span class="hidden group-has-checked/root:inline dark:inline dark:group-has-checked/root:hidden">Dark</span>
          </label>
        </div>
      </div>
      <h2 class="mb-2.5 text-[clamp(20px,4.4vw,25px)] font-semibold leading-tight tracking-[-0.02em]">One dial, two palettes</h2>
      <p class="mb-4 text-sm leading-relaxed text-tpop19-mut text-pretty">The panel is in the top layer and still inherits the dial, so it crossfades with the page — open it, then flip the switch.</p>
      <button id="tpop-19-trigger" type="button" popovertarget="tpop-19-panel" class="min-h-11 cursor-pointer rounded-xl bg-tpop19-acc px-4 text-[13.5px] font-semibold text-tpop19-onacc transition-[filter] [anchor-name:--tpop19-a] hover:brightness-110 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpop19-acc">Open themed panel</button>
      <dl class="mt-4.5 grid gap-2 border-t border-tpop19-rule pt-3.5">
        <div class="flex min-w-0 items-center justify-between gap-3"><dt class="flex items-center gap-2 font-tpop19-mono text-xs font-semibold text-tpop19-acc"><span aria-hidden="true" class="size-3 rounded-[4px] border border-tpop19-rule bg-tpop19-page"></span>--color-tpop19-page</dt><dd class="text-[12.5px] text-tpop19-mut">page</dd></div>
        <div class="flex min-w-0 items-center justify-between gap-3"><dt class="flex items-center gap-2 font-tpop19-mono text-xs font-semibold text-tpop19-acc"><span aria-hidden="true" class="size-3 rounded-[4px] border border-tpop19-rule bg-tpop19-panel"></span>--color-tpop19-panel</dt><dd class="text-[12.5px] text-tpop19-mut">surfaces</dd></div>
        <div class="flex min-w-0 items-center justify-between gap-3"><dt class="flex items-center gap-2 font-tpop19-mono text-xs font-semibold text-tpop19-acc"><span aria-hidden="true" class="size-3 rounded-[4px] bg-tpop19-ink"></span>--color-tpop19-ink</dt><dd class="text-[12.5px] text-tpop19-mut">text</dd></div>
      </dl>
    </div>
  </div>

  <div popover="auto" id="tpop-19-panel" role="group" aria-label="Themed panel" class="fixed m-auto w-[min(18rem,calc(100vw-28px))] rounded-2xl border border-tpop19-rule bg-tpop19-panel p-4 text-tpop19-ink opacity-0 shadow-[0_20px_40px_-24px_oklch(0_0_0/0.45)] transition-[opacity,translate,display,overlay] duration-150 ease-out transition-discrete [position-anchor:--tpop19-a] [position-area:block-end_span-inline-end] [position-try-fallbacks:flip-block] open:opacity-100 starting:open:-translate-y-1 starting:open:opacity-0 motion-reduce:transition-none supports-[anchor-name:--a]:inset-auto supports-[anchor-name:--a]:m-0 supports-[anchor-name:--a]:mt-2.5">
    <p class="mb-2 text-[11px] font-bold uppercase tracking-[0.16em] text-tpop19-mut">Themed panel</p>
    <p class="mb-3 text-[13.5px] leading-relaxed">Flip the switch with me open. Both surfaces fade in the same frame because they read the same dial.</p>
    <p class="border-t border-tpop19-rule pt-2.5 font-tpop19-mono text-[11.5px] font-semibold text-tpop19-acc">zero JavaScript</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* The theme dial: registered so it can transition (0 = light, 1 = dark). */

@property --tpop19-d {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* inline: each utility carries the expression itself, so it resolves against the dial the element
   inherits rather than once on :root. Light value last, dark value first. */

@theme inline {
  --color-tpop19-page: color-mix(in oklch, oklch(0.185 0.01 270) calc(var(--tpop19-d) * 100%), oklch(0.975 0.003 270));
  --color-tpop19-panel: color-mix(in oklch, oklch(0.235 0.01 270) calc(var(--tpop19-d) * 100%), oklch(1 0 0));
  --color-tpop19-ink: color-mix(in oklch, oklch(0.94 0.008 270) calc(var(--tpop19-d) * 100%), oklch(0.2 0.01 270));
  --color-tpop19-mut: color-mix(in oklch, oklch(0.74 0.015 270) calc(var(--tpop19-d) * 100%), oklch(0.48 0.012 270));
  --color-tpop19-rule: color-mix(in oklch, oklch(0.32 0.012 270) calc(var(--tpop19-d) * 100%), oklch(0.9 0.006 270));
  --color-tpop19-acc: color-mix(in oklch, oklch(0.74 0.12 262) calc(var(--tpop19-d) * 100%), oklch(0.5 0.17 262));
  --color-tpop19-onacc: color-mix(in oklch, oklch(0.185 0.01 270) calc(var(--tpop19-d) * 100%), oklch(1 0 0));
}

@theme {
  --font-tpop19-sans: 'Geist', system-ui, sans-serif;
  --font-tpop19-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpop-19 {
  width: 100%;
  min-height: 100svh;
}
```

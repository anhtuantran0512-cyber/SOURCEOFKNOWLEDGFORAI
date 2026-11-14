---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-modal-dialog-popover-api-clay/"
title: "Tailwind Modal Dialog with Popover API (Clay Floating Depth)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "A tier-4 clay dialog on the native popover API — no focus-trap library, no script."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Modal Dialog with Popover API (Clay Floating Depth)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-modal-dialog-popover-api-clay/

A tier-4 clay dialog on the native popover API — no focus-trap library, no script. The browser owns the top layer, light dismiss, Escape and focus return; Tailwind owns the rest: open:grid, starting:open:scale-94 for the entry, transition-discrete for the exit, and backdrop:backdrop-blur-[7px] for the scrim. New: a labelled close button and drawn check glyphs in the checklist.
## HTML
```html
<section class="tcl-14 w-full min-h-svh grid place-items-center bg-tcl14-bg bg-[radial-gradient(85%_60%_at_50%_0%,var(--color-tcl14-glow),transparent_68%)] px-5 py-14 font-tcl14-sans text-tcl14-ink" aria-label="Clay modal dialog with floating depth demo">
  <div class="grid w-full justify-items-center gap-5">
    <div class="grid w-full max-w-[640px] justify-items-center gap-3.5 rounded-[44px] bg-tcl14-page p-[clamp(26px,4vw,46px)] text-center shadow-tcl14-page">
      <h2 class="font-tcl14-display text-[clamp(26px,3.8vw,36px)] font-extrabold leading-[1.08] tracking-[-0.03em] text-balance">Native popover, clay depth</h2>
      <p class="max-w-[48ch] text-[15px] leading-relaxed text-tcl14-mut text-pretty">The top layer, light dismiss, Escape and focus are the browser's job. Tier-4 shadows and a blurred backdrop are ours.</p>
      <button type="button" popovertarget="tcl-14-dialog" class="mt-1.5 min-h-[58px] cursor-pointer rounded-[26px] bg-tcl14-accent px-8.5 text-base font-bold text-tcl14-accentink shadow-tcl14-cta transition-[translate,scale,box-shadow] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-1 active:translate-y-0.75 active:scale-y-93 active:shadow-tcl14-press focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl14-ink">Publish collection</button>
      <ul class="mt-1.5 flex flex-wrap justify-center gap-2" aria-label="Techniques">
        <li class="rounded-full bg-white/65 px-3 py-1.75 font-tcl14-mono text-[11px] text-tcl14-mut shadow-tcl14-fact">popover="auto"</li>
        <li class="rounded-full bg-white/65 px-3 py-1.75 font-tcl14-mono text-[11px] text-tcl14-mut shadow-tcl14-fact">starting:open:</li>
        <li class="rounded-full bg-white/65 px-3 py-1.75 font-tcl14-mono text-[11px] text-tcl14-mut shadow-tcl14-fact">transition-discrete</li>
        <li class="rounded-full bg-white/65 px-3 py-1.75 font-tcl14-mono text-[11px] text-tcl14-mut shadow-tcl14-fact">backdrop:backdrop-blur</li>
      </ul>
    </div>
    <div id="tcl-14-dialog" popover="auto" aria-labelledby="tcl-14-title" class="fixed inset-0 m-auto max-h-[86svh] w-[min(92vw,460px)] translate-y-3 scale-94 gap-3.5 overflow-auto rounded-[40px] border-0 bg-tcl14-clay p-[clamp(24px,3.6vw,34px)] text-tcl14-ink opacity-0 shadow-tcl14-modal transition-[opacity,scale,translate,display,overlay] transition-discrete duration-300 ease-[cubic-bezier(.2,.9,.3,1.15)] open:grid open:translate-y-0 open:scale-100 open:opacity-100 starting:open:translate-y-3 starting:open:scale-94 starting:open:opacity-0 backdrop:bg-tcl14-scrim backdrop:opacity-0 backdrop:backdrop-blur-[7px] backdrop:transition-[opacity,display,overlay] backdrop:transition-discrete backdrop:duration-300 open:backdrop:opacity-100 starting:open:backdrop:opacity-0 motion-reduce:transition-none">
      <div class="flex items-center justify-between">
        <span aria-hidden="true" class="w-11"></span>
        <span aria-hidden="true" class="h-1.5 w-13.5 rounded-full bg-tcl14-shade/40 shadow-[inset_0_2px_3px_-1px_var(--color-tcl14-shade)]"></span>
        <button type="button" popovertarget="tcl-14-dialog" popovertargetaction="hide" aria-label="Close" class="grid size-11 cursor-pointer place-items-center rounded-full bg-tcl14-soft text-tcl14-ink shadow-tcl14-ghost transition-[translate] hover:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tcl14-ink"><svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8"/></svg></button>
      </div>
      <h3 id="tcl-14-title" class="font-tcl14-display text-[clamp(21px,3vw,25px)] font-extrabold tracking-[-0.025em] text-balance">Publish “20 Tailwind Claymorphism”?</h3>
      <p class="text-[14.5px] leading-relaxed text-tcl14-ink/85 text-pretty">All 20 demos become public and the collection page goes live at once. You can unpublish any single demo later.</p>
      <ul class="mt-0.5 mb-1 grid gap-2">
        <li class="flex items-center gap-2.75 rounded-[20px] bg-tcl14-soft px-3.75 py-2.75 text-[13.5px] font-semibold shadow-tcl14-row"><span aria-hidden="true" class="grid size-5.5 flex-none place-items-center rounded-full bg-tcl14-ok text-white shadow-tcl14-tick"><svg viewBox="0 0 16 16" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 8.5l3 3 6-7"/></svg></span>Snippets validated</li>
        <li class="flex items-center gap-2.75 rounded-[20px] bg-tcl14-soft px-3.75 py-2.75 text-[13.5px] font-semibold shadow-tcl14-row"><span aria-hidden="true" class="grid size-5.5 flex-none place-items-center rounded-full bg-tcl14-ok text-white shadow-tcl14-tick"><svg viewBox="0 0 16 16" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 8.5l3 3 6-7"/></svg></span>Reduced-motion pass</li>
        <li class="flex items-center gap-2.75 rounded-[20px] bg-tcl14-soft px-3.75 py-2.75 text-[13.5px] font-semibold shadow-tcl14-row"><span aria-hidden="true" class="grid size-5.5 flex-none place-items-center rounded-full bg-tcl14-ok text-white shadow-tcl14-tick"><svg viewBox="0 0 16 16" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 8.5l3 3 6-7"/></svg></span>Contrast pass</li>
      </ul>
      <div class="mt-1 flex flex-wrap gap-2.5">
        <button type="button" popovertarget="tcl-14-dialog" popovertargetaction="hide" class="min-h-13 min-w-[130px] flex-1 cursor-pointer rounded-3xl bg-tcl14-soft px-5.5 text-[14.5px] font-bold text-tcl14-ink shadow-tcl14-ghost transition-[translate,scale,box-shadow] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 active:translate-y-0.75 active:scale-y-94 active:shadow-tcl14-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl14-ink">Not yet</button>
        <button type="button" popovertarget="tcl-14-dialog" popovertargetaction="hide" class="min-h-13 min-w-[130px] flex-1 cursor-pointer rounded-3xl bg-tcl14-accent px-5.5 text-[14.5px] font-bold text-tcl14-accentink shadow-tcl14-cta transition-[translate,scale,box-shadow] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 active:translate-y-0.75 active:scale-y-94 active:shadow-tcl14-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl14-ink">Publish now</button>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl14-mono text-[11.5px] text-tcl14-mut">tier-4 elevation · open: + starting:open: · transition-discrete · native top layer</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl14-bg: #ebe3fc;
  --color-tcl14-bg: oklch(0.93 0.035 300);
  --color-tcl14-glow: #fcefff;
  --color-tcl14-glow: oklch(0.97 0.035 310);
  --color-tcl14-page: #f2edfd;
  --color-tcl14-page: oklch(0.955 0.022 300);
  --color-tcl14-clay: #e3d7fb;
  --color-tcl14-clay: oklch(0.9 0.05 300);
  --color-tcl14-soft: #eee7ff;
  --color-tcl14-soft: oklch(0.94 0.034 300);
  --color-tcl14-accent: #c9a5ff;
  --color-tcl14-accent: oklch(0.79 0.14 300);
  --color-tcl14-accentink: #26133f;
  --color-tcl14-accentink: oklch(0.24 0.08 300);
  --color-tcl14-ok: #00884b;
  --color-tcl14-ok: oklch(0.55 0.14 155);
  --color-tcl14-scrim: #3d30526b;
  --color-tcl14-scrim: oklch(0.34 0.06 300 / 0.42);
  --color-tcl14-shade: #6c55948c;
  --color-tcl14-shade: oklch(0.5 0.1 300 / 0.55);
  --color-tcl14-light: #fffdfff2;
  --color-tcl14-light: oklch(1 0.012 300 / 0.95);
  --color-tcl14-ink: #291c3c;
  --color-tcl14-ink: oklch(0.26 0.06 300);
  --color-tcl14-mut: #594f6d;
  --color-tcl14-mut: oklch(0.45 0.05 300);
  --font-tcl14-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl14-page: 0 26px 48px -20px var(--color-tcl14-shade), inset 0 -16px 28px -16px var(--color-tcl14-shade), inset 0 18px 28px -12px var(--color-tcl14-light);
  --shadow-tcl14-modal: 0 60px 110px -30px oklch(0.32 0.08 300 / 0.65), 0 24px 44px -16px var(--color-tcl14-shade), inset 0 -20px 34px -16px var(--color-tcl14-shade), inset 0 24px 34px -10px var(--color-tcl14-light);
  --shadow-tcl14-cta: 0 16px 28px -12px var(--color-tcl14-shade), inset 0 -12px 20px -9px var(--color-tcl14-shade), inset 0 14px 20px -7px var(--color-tcl14-light);
  --shadow-tcl14-ghost: 0 12px 20px -12px var(--color-tcl14-shade), inset 0 -9px 15px -9px var(--color-tcl14-shade), inset 0 11px 15px -7px var(--color-tcl14-light);
  --shadow-tcl14-press: 0 0 0 0 transparent, inset 0 12px 18px -8px var(--color-tcl14-shade), inset 0 -6px 12px -9px var(--color-tcl14-light);
  --shadow-tcl14-row: inset 0 -6px 11px -8px var(--color-tcl14-shade), inset 0 7px 11px -6px var(--color-tcl14-light);
  --shadow-tcl14-fact: inset 0 -4px 8px -7px var(--color-tcl14-shade), inset 0 5px 8px -5px white;
  --shadow-tcl14-tick: inset 0 5px 7px -4px oklch(1 0 0 / 0.6), 0 4px 7px -4px var(--color-tcl14-shade);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-14 {
  width: 100%;
  min-height: 100svh;
}
```

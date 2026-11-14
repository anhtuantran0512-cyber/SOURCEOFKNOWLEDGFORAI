---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-mobile-bottom-navigation-bar-clay/"
title: "Tailwind Mobile Bottom Navigation Bar (Clay Tab Bar)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "A floating clay dock with five destinations, a sliding puffy indicator and the two things production tab bars must get right:…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mobile Bottom Navigation Bar (Clay Tab Bar)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-mobile-bottom-navigation-bar-clay/

A floating clay dock with five destinations, a sliding puffy indicator and the two things production tab bars must get right: pb-[calc(12px+env(safe-area-inset-bottom))] to clear the iPhone home bar, and 56px targets. The pill reads the checked radio through group-has-[#tcl-16-t3:checked]/bar:translate-x-[200%]. New: the screen title follows the active tab, and the incorrect role="tablist" is gone.
## HTML
```html
<section class="tcl-16 w-full min-h-svh grid place-items-center bg-tcl16-bg bg-[radial-gradient(80%_60%_at_50%_0%,var(--color-tcl16-glow),transparent_66%)] px-4 py-12 font-tcl16-sans text-tcl16-ink" aria-label="Clay bottom tab bar for mobile demo">
  <div class="grid w-full justify-items-center gap-5">
    <div class="group/phone w-[min(94vw,372px)] rounded-[56px] bg-tcl16-phone p-3.5 shadow-tcl16-phone">
      <div class="relative grid h-[min(70svh,580px)] grid-rows-[auto_1fr_auto] gap-3.5 overflow-hidden rounded-[44px] bg-tcl16-screen px-4 pt-4.5 shadow-tcl16-screen">
        <header class="flex items-center justify-between px-1.5 py-0.5">
          <h3 class="font-tcl16-display text-[22px] font-semibold tracking-[-0.01em]"><span class="hidden group-has-[#tcl-16-t1:checked]/phone:inline">Home</span><span class="hidden group-has-[#tcl-16-t2:checked]/phone:inline">Library</span><span class="hidden group-has-[#tcl-16-t3:checked]/phone:inline">Streaks</span><span class="hidden group-has-[#tcl-16-t4:checked]/phone:inline">Profile</span><span class="hidden group-has-[#tcl-16-t5:checked]/phone:inline">More</span></h3>
          <span aria-hidden="true" class="size-9.5 rounded-full bg-[oklch(0.84_0.1_340)] shadow-tcl16-av"></span>
        </header>
        <div aria-hidden="true" class="grid content-start gap-2.5 overflow-hidden">
          <div class="flex items-center gap-3 rounded-[26px] bg-tcl16-clay p-3 shadow-tcl16-row"><span class="size-11.5 flex-none rounded-[18px] bg-[oklch(0.84_0.1_30)] shadow-tcl16-thumb"></span><span class="grid flex-1 gap-2"><i class="block h-2.25 rounded-full bg-tcl16-shade/26"></i><i class="block h-2.25 w-[58%] rounded-full bg-tcl16-shade/26"></i></span></div>
          <div class="flex items-center gap-3 rounded-[26px] bg-tcl16-clay p-3 shadow-tcl16-row"><span class="size-11.5 flex-none rounded-[18px] bg-[oklch(0.84_0.09_190)] shadow-tcl16-thumb"></span><span class="grid flex-1 gap-2"><i class="block h-2.25 rounded-full bg-tcl16-shade/26"></i><i class="block h-2.25 w-[58%] rounded-full bg-tcl16-shade/26"></i></span></div>
          <div class="flex items-center gap-3 rounded-[26px] bg-tcl16-clay p-3 shadow-tcl16-row"><span class="size-11.5 flex-none rounded-[18px] bg-[oklch(0.85_0.1_290)] shadow-tcl16-thumb"></span><span class="grid flex-1 gap-2"><i class="block h-2.25 rounded-full bg-tcl16-shade/26"></i><i class="block h-2.25 w-[58%] rounded-full bg-tcl16-shade/26"></i></span></div>
          <div class="flex items-center gap-3 rounded-[26px] bg-tcl16-clay p-3 shadow-tcl16-row"><span class="size-11.5 flex-none rounded-[18px] bg-[oklch(0.86_0.1_145)] shadow-tcl16-thumb"></span><span class="grid flex-1 gap-2"><i class="block h-2.25 rounded-full bg-tcl16-shade/26"></i><i class="block h-2.25 w-[58%] rounded-full bg-tcl16-shade/26"></i></span></div>
        </div>
        <nav aria-label="Main" class="sticky bottom-0 pb-[calc(12px+env(safe-area-inset-bottom,0px))]">
          <div class="group/bar relative grid grid-cols-5 rounded-[32px] bg-tcl16-clay p-2 shadow-tcl16-dock">
            <span aria-hidden="true" class="absolute top-2 left-2 h-[calc(100%-16px)] w-[calc((100%-16px)/5)] rounded-3xl bg-tcl16-accent shadow-tcl16-pill transition-[translate] duration-[360ms] ease-[cubic-bezier(.34,1.45,.5,1)] group-has-[#tcl-16-t2:checked]/bar:translate-x-full group-has-[#tcl-16-t3:checked]/bar:translate-x-[200%] group-has-[#tcl-16-t4:checked]/bar:translate-x-[300%] group-has-[#tcl-16-t5:checked]/bar:translate-x-[400%] motion-reduce:transition-none"></span>
            <label class="group relative flex min-h-14 cursor-pointer flex-col items-center justify-center gap-0.75 overflow-hidden rounded-3xl text-tcl16-mut transition-[color,scale] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:text-tcl16-ink active:scale-94 has-checked:text-tcl16-accentink has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tcl16-ink"><input class="sr-only" type="radio" name="tcl-16-tab" id="tcl-16-t1"><svg class="flex-none transition-[scale] duration-300 group-has-checked:scale-108" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 11.2 12 4l8 7.2V20a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1z" fill="currentColor"/></svg><span class="max-h-0 text-[10.5px] font-semibold whitespace-nowrap opacity-0 transition-[max-height,opacity] duration-300 group-has-checked:max-h-3.5 group-has-checked:opacity-100">Home</span></label>
            <label class="group relative flex min-h-14 cursor-pointer flex-col items-center justify-center gap-0.75 overflow-hidden rounded-3xl text-tcl16-mut transition-[color,scale] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:text-tcl16-ink active:scale-94 has-checked:text-tcl16-accentink has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tcl16-ink"><input class="sr-only" type="radio" name="tcl-16-tab" id="tcl-16-t2" checked><svg class="flex-none transition-[scale] duration-300 group-has-checked:scale-108" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M5 4h9l5 5v11a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zm8 1.8V10h4.2z" fill="currentColor"/></svg><span class="max-h-0 text-[10.5px] font-semibold whitespace-nowrap opacity-0 transition-[max-height,opacity] duration-300 group-has-checked:max-h-3.5 group-has-checked:opacity-100">Library</span></label>
            <label class="group relative flex min-h-14 cursor-pointer flex-col items-center justify-center gap-0.75 overflow-hidden rounded-3xl text-tcl16-mut transition-[color,scale] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:text-tcl16-ink active:scale-94 has-checked:text-tcl16-accentink has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tcl16-ink"><input class="sr-only" type="radio" name="tcl-16-tab" id="tcl-16-t3" aria-describedby="tcl-16-new"><span class="relative"><svg class="flex-none transition-[scale] duration-300 group-has-checked:scale-108" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M12 3.5 14.6 9l6 .9-4.3 4.2 1 6-5.3-2.8-5.3 2.8 1-6L3.4 9.9 9.4 9z" fill="currentColor"/></svg><b id="tcl-16-new" class="absolute -top-0.5 -right-1 size-2.5 rounded-full bg-tcl16-dot shadow-[0_0_0_2px_var(--color-tcl16-clay)] group-has-checked:hidden"><span class="sr-only">New streak reward</span></b></span><span class="max-h-0 text-[10.5px] font-semibold whitespace-nowrap opacity-0 transition-[max-height,opacity] duration-300 group-has-checked:max-h-3.5 group-has-checked:opacity-100">Streaks</span></label>
            <label class="group relative flex min-h-14 cursor-pointer flex-col items-center justify-center gap-0.75 overflow-hidden rounded-3xl text-tcl16-mut transition-[color,scale] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:text-tcl16-ink active:scale-94 has-checked:text-tcl16-accentink has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tcl16-ink"><input class="sr-only" type="radio" name="tcl-16-tab" id="tcl-16-t4"><svg class="flex-none transition-[scale] duration-300 group-has-checked:scale-108" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm0 2c-4 0-7 2.2-7 5v1h14v-1c0-2.8-3-5-7-5z" fill="currentColor"/></svg><span class="max-h-0 text-[10.5px] font-semibold whitespace-nowrap opacity-0 transition-[max-height,opacity] duration-300 group-has-checked:max-h-3.5 group-has-checked:opacity-100">Profile</span></label>
            <label class="group relative flex min-h-14 cursor-pointer flex-col items-center justify-center gap-0.75 overflow-hidden rounded-3xl text-tcl16-mut transition-[color,scale] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] hover:text-tcl16-ink active:scale-94 has-checked:text-tcl16-accentink has-focus-visible:outline-3 has-focus-visible:-outline-offset-3 has-focus-visible:outline-tcl16-ink"><input class="sr-only" type="radio" name="tcl-16-tab" id="tcl-16-t5"><svg class="flex-none transition-[scale] duration-300 group-has-checked:scale-108" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 6h16v2.4H4zm0 4.8h16v2.4H4zm0 4.8h11V18H4z" fill="currentColor"/></svg><span class="max-h-0 text-[10.5px] font-semibold whitespace-nowrap opacity-0 transition-[max-height,opacity] duration-300 group-has-checked:max-h-3.5 group-has-checked:opacity-100">More</span></label>
          </div>
        </nav>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl16-mono text-[11.5px] text-tcl16-mut">one translating pill · group-has-checked: label reveal · env(safe-area-inset-bottom)</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl16-bg: #f7e1ee;
  --color-tcl16-bg: oklch(0.93 0.03 340);
  --color-tcl16-glow: #ffedf8;
  --color-tcl16-glow: oklch(0.97 0.03 350);
  --color-tcl16-phone: #f8eaf3;
  --color-tcl16-phone: oklch(0.95 0.02 340);
  --color-tcl16-screen: #f4daea;
  --color-tcl16-screen: oklch(0.915 0.035 340);
  --color-tcl16-clay: #f7d6eb;
  --color-tcl16-clay: oklch(0.91 0.045 340);
  --color-tcl16-accent: #f59cd8;
  --color-tcl16-accent: oklch(0.8 0.13 340);
  --color-tcl16-accentink: #340f29;
  --color-tcl16-accentink: oklch(0.24 0.07 340);
  --color-tcl16-dot: #de3b3d;
  --color-tcl16-dot: oklch(0.6 0.2 25);
  --color-tcl16-shade: #8b537980;
  --color-tcl16-shade: oklch(0.52 0.09 340 / 0.5);
  --color-tcl16-light: #fffcfff2;
  --color-tcl16-light: oklch(1 0.012 340 / 0.95);
  --color-tcl16-ink: #341a2c;
  --color-tcl16-ink: oklch(0.26 0.05 340);
  --color-tcl16-mut: #674c5d;
  --color-tcl16-mut: oklch(0.45 0.045 340);
  --font-tcl16-display: 'Fredoka', system-ui, sans-serif;
  --font-tcl16-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl16-phone: 0 40px 70px -26px var(--color-tcl16-shade), inset 0 -18px 30px -16px var(--color-tcl16-shade), inset 0 20px 30px -12px var(--color-tcl16-light);
  --shadow-tcl16-screen: inset 0 12px 22px -10px var(--color-tcl16-shade), inset 0 -10px 18px -12px var(--color-tcl16-light);
  --shadow-tcl16-av: 0 8px 14px -7px var(--color-tcl16-shade), inset 0 -6px 10px -7px var(--color-tcl16-shade), inset 0 8px 10px -6px var(--color-tcl16-light);
  --shadow-tcl16-row: 0 12px 20px -14px var(--color-tcl16-shade), inset 0 -8px 14px -10px var(--color-tcl16-shade), inset 0 10px 14px -8px var(--color-tcl16-light);
  --shadow-tcl16-thumb: inset 0 -6px 10px -7px var(--color-tcl16-shade), inset 0 8px 10px -6px var(--color-tcl16-light);
  --shadow-tcl16-dock: 0 26px 44px -18px var(--color-tcl16-shade), inset 0 -12px 20px -12px var(--color-tcl16-shade), inset 0 14px 20px -8px var(--color-tcl16-light);
  --shadow-tcl16-pill: 0 10px 18px -8px var(--color-tcl16-shade), inset 0 -7px 12px -8px var(--color-tcl16-shade), inset 0 9px 12px -6px var(--color-tcl16-light);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-16 {
  width: 100%;
  min-height: 100svh;
}
```

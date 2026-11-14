---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-search-bar-floating-label-input-clay/"
title: "Tailwind Search Bar & Floating Label Input (Clay Inset Style)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Inputs are where clay inverts: a field you type into is a well, not a lifted object."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Search Bar & Floating Label Input (Clay Inset Style)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-search-bar-floating-label-input-clay/

Inputs are where clay inverts: a field you type into is a well, not a lifted object. An inset search bar opens a suggestion tray on focus (group-focus-within/search:grid with a starting: entry), floating labels ride peer-focus:, errors wait for user-invalid:, and the note grows with field-sizing: content. New: suggestions are keyboard-reachable buttons, and a valid email earns a check.
## HTML
```html
<section class="tcl-11 w-full min-h-svh grid place-items-center bg-tcl11-bg px-5 py-14 font-tcl11-sans text-tcl11-ink" aria-label="Clay input field and search bar demo">
  <div class="grid w-full justify-items-center gap-5">
    <div class="grid w-full max-w-[620px] gap-[clamp(20px,3vw,26px)] rounded-[42px] bg-tcl11-panel p-[clamp(22px,3.4vw,36px)] shadow-tcl11-panel">
      <div class="group/search relative">
        <label for="tcl-11-search" class="mb-2.5 block text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl11-mut">Search lessons</label>
        <div class="flex items-center gap-3 rounded-full bg-tcl11-well px-4.5 shadow-tcl11-well transition-shadow duration-300 focus-within:shadow-tcl11-focus">
          <svg class="flex-none text-tcl11-mut" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M10.5 3a7.5 7.5 0 015.9 12.1l4.3 4.3-1.4 1.4-4.3-4.3A7.5 7.5 0 1110.5 3zm0 2a5.5 5.5 0 100 11 5.5 5.5 0 000-11z" fill="currentColor"/></svg>
          <input id="tcl-11-search" type="search" autocomplete="off" placeholder="Try “inset shadows”" class="min-h-14 min-w-0 flex-1 bg-transparent text-[15px] text-tcl11-ink outline-none placeholder:text-tcl11-mut">
          <kbd class="grid size-6.5 flex-none place-items-center rounded-[9px] bg-tcl11-panel font-tcl11-mono text-xs text-tcl11-mut shadow-tcl11-key">/</kbd>
        </div>
        <div class="absolute inset-x-0 top-[calc(100%+10px)] z-10 hidden -translate-y-2 gap-1 rounded-[26px] bg-tcl11-tray p-2.5 opacity-0 shadow-tcl11-tray transition-[opacity,translate,display] transition-discrete duration-300 group-focus-within/search:grid group-focus-within/search:translate-y-0 group-focus-within/search:opacity-100 group-focus-within/search:starting:-translate-y-2 group-focus-within/search:starting:opacity-0 motion-reduce:transition-none" aria-label="Suggestions">
          <button type="button" class="min-h-11 cursor-pointer rounded-[18px] px-4 text-left text-[13.5px] text-tcl11-mut transition-colors hover:bg-tcl11-accent/16 focus-visible:bg-tcl11-accent/16 focus-visible:outline-2 focus-visible:outline-tcl11-accent"><b class="font-semibold text-tcl11-ink">inset box-shadow</b> · technique</button>
          <button type="button" class="min-h-11 cursor-pointer rounded-[18px] px-4 text-left text-[13.5px] text-tcl11-mut transition-colors hover:bg-tcl11-accent/16 focus-visible:bg-tcl11-accent/16 focus-visible:outline-2 focus-visible:outline-tcl11-accent"><b class="font-semibold text-tcl11-ink">clay vs neumorphism</b> · comparison</button>
          <button type="button" class="min-h-11 cursor-pointer rounded-[18px] px-4 text-left text-[13.5px] text-tcl11-mut transition-colors hover:bg-tcl11-accent/16 focus-visible:bg-tcl11-accent/16 focus-visible:outline-2 focus-visible:outline-tcl11-accent"><b class="font-semibold text-tcl11-ink">puffy radius scale</b> · reference</button>
        </div>
      </div>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(220px,1fr))] gap-4">
        <div class="relative flex items-center rounded-3xl bg-tcl11-well px-4.5 shadow-tcl11-well transition-shadow duration-300 focus-within:shadow-tcl11-focus">
          <input id="tcl-11-name" type="text" placeholder=" " class="peer min-h-[62px] w-full bg-transparent pt-4 text-[15px] text-tcl11-ink outline-none">
          <label for="tcl-11-name" class="pointer-events-none absolute top-5 left-4.75 text-[15px] text-tcl11-mut transition-[translate,font-size,color] duration-200 ease-[cubic-bezier(.2,.8,.3,1)] peer-focus:-translate-y-3.25 peer-focus:text-[11px] peer-focus:font-bold peer-focus:tracking-[0.1em] peer-focus:text-tcl11-accentink peer-focus:uppercase peer-[:not(:placeholder-shown)]:-translate-y-3.25 peer-[:not(:placeholder-shown)]:text-[11px] peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:tracking-[0.1em] peer-[:not(:placeholder-shown)]:text-tcl11-accentink peer-[:not(:placeholder-shown)]:uppercase">Display name</label>
        </div>
        <div class="group/f grid gap-2">
          <div class="relative flex items-center gap-2 rounded-3xl bg-tcl11-well px-4.5 shadow-tcl11-well transition-shadow duration-300 focus-within:shadow-tcl11-focus has-user-invalid:shadow-tcl11-error">
            <input id="tcl-11-mail" type="email" placeholder=" " required aria-describedby="tcl-11-mail-hint" class="peer min-h-[62px] w-full bg-transparent pt-4 text-[15px] text-tcl11-ink outline-none">
            <label for="tcl-11-mail" class="pointer-events-none absolute top-5 left-4.75 text-[15px] text-tcl11-mut transition-[translate,font-size,color] duration-200 ease-[cubic-bezier(.2,.8,.3,1)] peer-focus:-translate-y-3.25 peer-focus:text-[11px] peer-focus:font-bold peer-focus:tracking-[0.1em] peer-focus:text-tcl11-accentink peer-focus:uppercase peer-[:not(:placeholder-shown)]:-translate-y-3.25 peer-[:not(:placeholder-shown)]:text-[11px] peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:tracking-[0.1em] peer-[:not(:placeholder-shown)]:text-tcl11-accentink peer-[:not(:placeholder-shown)]:uppercase">Email address</label>
            <svg class="size-5 flex-none scale-50 text-tcl11-ok opacity-0 transition-[scale,opacity] duration-300 ease-[cubic-bezier(.34,1.6,.5,1)] peer-[:valid:not(:placeholder-shown)]:scale-100 peer-[:valid:not(:placeholder-shown)]:opacity-100" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 10.5l3.5 3.5 7.5-8"/></svg>
          </div>
          <p id="tcl-11-mail-hint" class="pl-1.5 text-[12.5px] text-tcl11-mut transition-colors group-has-user-invalid/f:text-tcl11-errink group-has-user-invalid/f:before:font-bold group-has-user-invalid/f:before:content-['Check_this_address_—_']">We only email your weekly streak.</p>
        </div>
      </div>
      <div>
        <label for="tcl-11-note" class="mb-2.5 block text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl11-mut">Practice note</label>
        <div class="rounded-3xl bg-tcl11-well px-4.5 py-3.5 shadow-tcl11-well transition-shadow duration-300 focus-within:shadow-tcl11-focus">
          <textarea id="tcl-11-note" rows="2" placeholder="What did you learn today?" class="block max-h-[180px] min-h-16 w-full resize-none bg-transparent text-[15px] leading-relaxed text-tcl11-ink outline-none [field-sizing:content] placeholder:text-tcl11-mut"></textarea>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl11-mono text-[11.5px] text-tcl11-mut">field = well · focus-within: ring · user-invalid: · starting: tray · field-sizing</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl11-bg: #dbeff9;
  --color-tcl11-bg: oklch(0.94 0.025 230);
  --color-tcl11-panel: #e8f4fb;
  --color-tcl11-panel: oklch(0.96 0.016 230);
  --color-tcl11-tray: #eff9fd;
  --color-tcl11-tray: oklch(0.975 0.012 230);
  --color-tcl11-well: #d1e7f4;
  --color-tcl11-well: oklch(0.915 0.03 235);
  --color-tcl11-accent: #3faff3;
  --color-tcl11-accent: oklch(0.72 0.14 240);
  --color-tcl11-accentink: #0068b2;
  --color-tcl11-accentink: oklch(0.5 0.15 245);
  --color-tcl11-ok: #00884b;
  --color-tcl11-ok: oklch(0.55 0.14 155);
  --color-tcl11-errink: #b71824;
  --color-tcl11-errink: oklch(0.5 0.19 25);
  --color-tcl11-shade: #3e799a99;
  --color-tcl11-shade: oklch(0.55 0.08 235 / 0.6);
  --color-tcl11-light: #f9fffff2;
  --color-tcl11-light: oklch(1 0.01 235 / 0.95);
  --color-tcl11-ink: #0c2a39;
  --color-tcl11-ink: oklch(0.27 0.045 235);
  --color-tcl11-mut: #425c6b;
  --color-tcl11-mut: oklch(0.46 0.04 235);
  --font-tcl11-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl11-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl11-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl11-panel: 0 30px 60px -24px var(--color-tcl11-shade), inset 0 -16px 28px -16px var(--color-tcl11-shade), inset 0 18px 28px -12px var(--color-tcl11-light);
  --shadow-tcl11-well: 0 0 0 0 transparent, inset 0 10px 18px -6px var(--color-tcl11-shade), inset 0 -8px 14px -10px var(--color-tcl11-light);
  --shadow-tcl11-focus: 0 0 0 4px oklch(0.72 0.14 240 / 0.42), inset 0 8px 14px -8px var(--color-tcl11-shade), inset 0 -6px 12px -10px var(--color-tcl11-light);
  --shadow-tcl11-error: 0 0 0 3px oklch(0.62 0.19 25 / 0.55), inset 0 10px 18px -6px oklch(0.62 0.19 25 / 0.45), inset 0 -8px 14px -10px var(--color-tcl11-light);
  --shadow-tcl11-key: 0 4px 8px -5px var(--color-tcl11-shade), inset 0 5px 7px -5px var(--color-tcl11-light);
  --shadow-tcl11-tray: 0 26px 50px -20px var(--color-tcl11-shade), inset 0 -12px 22px -16px var(--color-tcl11-shade), inset 0 14px 22px -12px var(--color-tcl11-light);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-11 {
  width: 100%;
  min-height: 100svh;
}
```

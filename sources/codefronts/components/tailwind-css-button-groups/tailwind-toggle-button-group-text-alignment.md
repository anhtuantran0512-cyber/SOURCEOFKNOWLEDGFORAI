---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-toggle-button-group-text-alignment/"
title: "Tailwind Toggle Button Group for Text Alignment (Radio Inputs, Live Preview)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A single-select icon toggle group — left, centre, right, justify — on hidden radios, so the arrow keys, form submission and screen-reader semantics are all…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Toggle Button Group for Text Alignment (Radio Inputs, Live Preview)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-toggle-button-group-text-alignment/

A single-select icon toggle group — left, centre, right, justify — on hidden radios, so the arrow keys, form submission and screen-reader semantics are all native. The pressed state uses an inset shadow plus a gold indicator bar (has-checked:after:…), and a sample paragraph re-aligns itself live through group-has-[#tbg09-2:checked]/card:text-center.
## HTML
```html
<section class="tbg-09 w-full min-h-svh grid place-items-center bg-tbg09-bg bg-linear-160 from-tbg09-bg to-tbg09-bg2 px-5 py-14 font-tbg09-sans text-tbg09-ink" aria-label="Text alignment toggle button group demo">
  <div class="group/card w-full max-w-[28rem] rounded-3xl border border-tbg09-line bg-white p-6 shadow-tbg09-lift">
    <div class="flex flex-wrap items-center justify-between gap-4">
      <p id="tbg09-label" class="text-xs font-bold uppercase tracking-[0.14em] text-tbg09-acc">Text alignment</p>
      <div role="radiogroup" aria-labelledby="tbg09-label" class="inline-flex gap-1 rounded-2xl border border-tbg09-line bg-tbg09-well p-1">
        <label aria-label="Align left" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg09-mut transition-colors hover:bg-white hover:text-tbg09-ink has-checked:bg-tbg09-acc has-checked:text-white has-checked:inset-shadow-[0_2px_6px_rgb(0_0_0/0.3)] has-checked:after:absolute has-checked:after:bottom-1.5 has-checked:after:h-0.5 has-checked:after:w-3.5 has-checked:after:rounded-full has-checked:after:bg-tbg09-gold has-checked:after:content-[''] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg09-acc motion-reduce:transition-none"><input type="radio" name="tbg09" id="tbg09-1" class="sr-only" checked><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 10h10M4 14h14M4 18h8"/></svg></label>
        <label aria-label="Align center" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg09-mut transition-colors hover:bg-white hover:text-tbg09-ink has-checked:bg-tbg09-acc has-checked:text-white has-checked:inset-shadow-[0_2px_6px_rgb(0_0_0/0.3)] has-checked:after:absolute has-checked:after:bottom-1.5 has-checked:after:h-0.5 has-checked:after:w-3.5 has-checked:after:rounded-full has-checked:after:bg-tbg09-gold has-checked:after:content-[''] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg09-acc motion-reduce:transition-none"><input type="radio" name="tbg09" id="tbg09-2" class="sr-only"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M7 10h10M5 14h14M8 18h8"/></svg></label>
        <label aria-label="Align right" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg09-mut transition-colors hover:bg-white hover:text-tbg09-ink has-checked:bg-tbg09-acc has-checked:text-white has-checked:inset-shadow-[0_2px_6px_rgb(0_0_0/0.3)] has-checked:after:absolute has-checked:after:bottom-1.5 has-checked:after:h-0.5 has-checked:after:w-3.5 has-checked:after:rounded-full has-checked:after:bg-tbg09-gold has-checked:after:content-[''] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg09-acc motion-reduce:transition-none"><input type="radio" name="tbg09" id="tbg09-3" class="sr-only"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M10 10h10M6 14h14M12 18h8"/></svg></label>
        <label aria-label="Justify" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg09-mut transition-colors hover:bg-white hover:text-tbg09-ink has-checked:bg-tbg09-acc has-checked:text-white has-checked:inset-shadow-[0_2px_6px_rgb(0_0_0/0.3)] has-checked:after:absolute has-checked:after:bottom-1.5 has-checked:after:h-0.5 has-checked:after:w-3.5 has-checked:after:rounded-full has-checked:after:bg-tbg09-gold has-checked:after:content-[''] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg09-acc motion-reduce:transition-none"><input type="radio" name="tbg09" id="tbg09-4" class="sr-only"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 10h16M4 14h16M4 18h16"/></svg></label>
      </div>
    </div>
    <p lang="en" class="mt-6 border-t border-tbg09-line pt-5 font-tbg09-serif text-[17px] leading-relaxed text-tbg09-body hyphens-auto group-has-[#tbg09-2:checked]/card:text-center group-has-[#tbg09-3:checked]/card:text-right group-has-[#tbg09-4:checked]/card:text-justify">The garden was quiet in the early hours, the rows of beans still heavy with dew, and the light came slowly over the far hedge like someone unsure of their welcome.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg09-bg: #f7f5ec;
  --color-tbg09-bg2: #eef1e4;
  --color-tbg09-well: #f4f5ec;
  --color-tbg09-line: #e3e6d6;
  --color-tbg09-ink: #20301f;
  --color-tbg09-body: #33432f;
  --color-tbg09-mut: #56654d;
  --color-tbg09-mut: oklch(0.48 0.04 140);
  --color-tbg09-acc: #2c7a4f;
  --color-tbg09-acc: oklch(0.5 0.12 155);
  --color-tbg09-gold: #e3bb4f;
  --color-tbg09-gold: oklch(0.8 0.13 85);
  --shadow-tbg09-lift: 0 18px 40px -24px rgb(40 60 30 / 0.45);
  --font-tbg09-sans: 'DM Sans', system-ui, sans-serif;
  --font-tbg09-serif: 'Newsreader', Georgia, serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-09 {
  width: 100%;
  min-height: 100svh;
}
```

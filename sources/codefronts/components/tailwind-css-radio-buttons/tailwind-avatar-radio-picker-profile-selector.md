---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-avatar-radio-picker-profile-selector/"
title: "Tailwind Avatar Radio Picker (Profile Selector)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "The \"who's watching?\" screen as a proper form control: profile photos where the active one scales up, gains a bright ring and full colour while the rest rest…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Avatar Radio Picker (Profile Selector)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-avatar-radio-picker-profile-selector/

The "who's watching?" screen as a proper form control: profile photos where the active one scales up, gains a bright ring and full colour while the rest rest slightly dimmed. The double ring is ring-3 ring-trb21-acc ring-offset-4 ring-offset-trb21-bg; the sprung lift is motion-safe:. An "Add profile" tile shows how to mix an action into the row without joining the radio group.
## HTML
```html
<section class="trb-21 w-full min-h-svh grid place-items-center bg-trb21-bg px-6 py-14 font-trb21-sans text-trb21-ink" aria-label="User profile avatar selector demo">
  <fieldset>
    <legend class="text-center text-[30px] font-extrabold tracking-[-0.025em]">Who's watching?</legend>
    <div class="mt-9 flex flex-wrap justify-center gap-8">
      <label class="group relative grid cursor-pointer justify-items-center gap-3"><input type="radio" name="trb-21" value="amara" class="sr-only" checked><img class="size-[92px] rounded-full object-cover brightness-80 saturate-70 ring-trb21-acc ring-offset-trb21-bg transition-[scale,filter,box-shadow] duration-350 ease-trb21-spring group-hover:brightness-100 group-hover:saturate-100 group-has-checked:shadow-trb21-lift group-has-checked:ring-3 group-has-checked:ring-offset-4 group-has-checked:brightness-100 group-has-checked:saturate-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-[10px] group-has-focus-visible:outline-white motion-safe:group-has-checked:scale-112" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=300&q=80&auto=format&fit=crop" alt="Amara" loading="lazy"><span class="text-[15px] font-semibold text-trb21-mut transition-colors group-has-checked:text-white">Amara</span></label>
      <label class="group relative grid cursor-pointer justify-items-center gap-3"><input type="radio" name="trb-21" value="jonas" class="sr-only"><img class="size-[92px] rounded-full object-cover brightness-80 saturate-70 ring-trb21-acc ring-offset-trb21-bg transition-[scale,filter,box-shadow] duration-350 ease-trb21-spring group-hover:brightness-100 group-hover:saturate-100 group-has-checked:shadow-trb21-lift group-has-checked:ring-3 group-has-checked:ring-offset-4 group-has-checked:brightness-100 group-has-checked:saturate-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-[10px] group-has-focus-visible:outline-white motion-safe:group-has-checked:scale-112" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&q=80&auto=format&fit=crop" alt="Jonas" loading="lazy"><span class="text-[15px] font-semibold text-trb21-mut transition-colors group-has-checked:text-white">Jonas</span></label>
      <label class="group relative grid cursor-pointer justify-items-center gap-3"><input type="radio" name="trb-21" value="sofia" class="sr-only"><img class="size-[92px] rounded-full object-cover brightness-80 saturate-70 ring-trb21-acc ring-offset-trb21-bg transition-[scale,filter,box-shadow] duration-350 ease-trb21-spring group-hover:brightness-100 group-hover:saturate-100 group-has-checked:shadow-trb21-lift group-has-checked:ring-3 group-has-checked:ring-offset-4 group-has-checked:brightness-100 group-has-checked:saturate-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-[10px] group-has-focus-visible:outline-white motion-safe:group-has-checked:scale-112" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=300&q=80&auto=format&fit=crop" alt="Sofia" loading="lazy"><span class="text-[15px] font-semibold text-trb21-mut transition-colors group-has-checked:text-white">Sofia</span></label>
      <label class="group relative grid cursor-pointer justify-items-center gap-3"><input type="radio" name="trb-21" value="mateo" class="sr-only"><img class="size-[92px] rounded-full object-cover brightness-80 saturate-70 ring-trb21-acc ring-offset-trb21-bg transition-[scale,filter,box-shadow] duration-350 ease-trb21-spring group-hover:brightness-100 group-hover:saturate-100 group-has-checked:shadow-trb21-lift group-has-checked:ring-3 group-has-checked:ring-offset-4 group-has-checked:brightness-100 group-has-checked:saturate-100 group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-[10px] group-has-focus-visible:outline-white motion-safe:group-has-checked:scale-112" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=300&q=80&auto=format&fit=crop" alt="Mateo" loading="lazy"><span class="text-[15px] font-semibold text-trb21-mut transition-colors group-has-checked:text-white">Mateo</span></label>
      <div class="grid justify-items-center gap-3"><button type="button" class="grid size-[92px] cursor-pointer place-items-center rounded-full border-2 border-dashed border-white/25 text-trb21-mut transition-colors hover:border-white/60 hover:text-white focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-white" aria-label="Add profile"><svg class="size-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></button><span aria-hidden="true" class="text-[15px] font-semibold text-trb21-mut">Add</span></div>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb21-bg: #101014;
  --color-trb21-bg: oklch(0.18 0.006 285);
  --color-trb21-ink: #f2f2f5;
  --color-trb21-ink: oklch(0.96 0.004 285);
  --color-trb21-mut: #9c9ca8;
  --color-trb21-mut: oklch(0.7 0.012 285);
  --color-trb21-acc: #f36f5c;
  --color-trb21-acc: oklch(0.7 0.16 30);
  --shadow-trb21-lift: 0 16px 34px -12px oklch(0 0 0 / 0.8);
  --ease-trb21-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb21-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-21 {
  width: 100%;
  min-height: 100svh;
}
```

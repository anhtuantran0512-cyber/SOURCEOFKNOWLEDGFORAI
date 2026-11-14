---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/variable-font-weight-tabs-tailwind-css/"
title: "Variable Font Weight Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Pure type-weight contrast: inactive labels are 200 hairline, the active one dials up to 900 black on Geist's variable axis while a violet rule draws in."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Variable Font Weight Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/variable-font-weight-tabs-tailwind-css/

Pure type-weight contrast: inactive labels are 200 hairline, the active one dials up to 900 black on Geist's variable axis while a violet rule draws in. The port fixes the original's layout jitter — bolding a word makes it wider and shoved its neighbours — by reserving each label's black-weight width with an invisible twin.
## HTML
```html
<section class="ttb-17 group/tabs grid min-h-svh w-full place-items-center bg-ttb17-bg px-5 py-14 font-ttb17-sans text-ttb17-paper" aria-label="Variable font weight tabs demo">
  <div class="grid w-full max-w-xl justify-items-start gap-7">
    <div role="radiogroup" aria-label="Project section" class="flex flex-wrap gap-x-8 gap-y-3">
      <label class="group/tab relative cursor-pointer pb-2.5 text-[28px] leading-none font-extralight tracking-[-0.02em] transition-[font-weight] duration-500 after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:origin-left after:scale-x-0 after:bg-ttb17-acc after:transition-transform after:duration-500 after:ease-[cubic-bezier(0.65,0,0.35,1)] hover:font-normal has-checked:font-black has-checked:after:scale-x-100 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-ttb17-acc motion-reduce:transition-none motion-reduce:after:transition-none"><input class="sr-only" type="radio" name="ttb17" id="ttb17-r1" checked><span class="grid [&>*]:[grid-area:1/1]"><span>Overview</span><span aria-hidden="true" class="invisible font-black">Overview</span></span></label>
      <label class="group/tab relative cursor-pointer pb-2.5 text-[28px] leading-none font-extralight tracking-[-0.02em] transition-[font-weight] duration-500 after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:origin-left after:scale-x-0 after:bg-ttb17-acc after:transition-transform after:duration-500 after:ease-[cubic-bezier(0.65,0,0.35,1)] hover:font-normal has-checked:font-black has-checked:after:scale-x-100 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-ttb17-acc motion-reduce:transition-none motion-reduce:after:transition-none"><input class="sr-only" type="radio" name="ttb17" id="ttb17-r2"><span class="grid [&>*]:[grid-area:1/1]"><span>Activity</span><span aria-hidden="true" class="invisible font-black">Activity</span></span></label>
      <label class="group/tab relative cursor-pointer pb-2.5 text-[28px] leading-none font-extralight tracking-[-0.02em] transition-[font-weight] duration-500 after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:origin-left after:scale-x-0 after:bg-ttb17-acc after:transition-transform after:duration-500 after:ease-[cubic-bezier(0.65,0,0.35,1)] hover:font-normal has-checked:font-black has-checked:after:scale-x-100 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-ttb17-acc motion-reduce:transition-none motion-reduce:after:transition-none"><input class="sr-only" type="radio" name="ttb17" id="ttb17-r3"><span class="grid [&>*]:[grid-area:1/1]"><span>Settings</span><span aria-hidden="true" class="invisible font-black">Settings</span></span></label>
    </div>
    <div class="max-w-[42ch] font-ttb17-serif text-[16px] leading-relaxed text-ttb17-mut">
      <p class="hidden group-has-[#ttb17-r1:checked]/tabs:block">A summary of the project, its members and the decisions made so far.</p>
      <p class="hidden group-has-[#ttb17-r2:checked]/tabs:block">Edits, comments and team mentions over the last seven days.</p>
      <p class="hidden group-has-[#ttb17-r3:checked]/tabs:block">Permissions, integrations and billing controls.</p>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-ttb17-mono text-[11.5px] text-ttb17-mut">font-extralight → font-black · invisible twin = 0 CLS</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb17-bg: #14141c;
  --color-ttb17-bg: oklch(0.195 0.016 284.8);
  --color-ttb17-paper: #ece6d4;
  --color-ttb17-paper: oklch(0.925 0.025 91.6);
  --color-ttb17-mut: #b0aa9b;
  --color-ttb17-mut: oklch(0.739 0.022 88.8);
  --color-ttb17-acc: #8b6dff;
  --color-ttb17-acc: oklch(0.638 0.208 288.5);
  --font-ttb17-sans: 'Geist', system-ui, sans-serif;
  --font-ttb17-serif: 'Newsreader', Georgia, serif;
  --font-ttb17-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-17 {
  width: 100%;
  min-height: 100svh;
}
```

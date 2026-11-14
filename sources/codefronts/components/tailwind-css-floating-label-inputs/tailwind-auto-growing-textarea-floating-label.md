---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-auto-growing-textarea-floating-label/"
title: "Tailwind Auto-Growing Textarea with Floating Label"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "Floating labels on multi-line input, solved: the label anchors to the textarea's first text line (top-[26px], not top-1/2), floats out into a corner-tab chip…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Auto-Growing Textarea with Floating Label
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-auto-growing-textarea-floating-label/

Floating labels on multi-line input, solved: the label anchors to the textarea's first text line (top-[26px], not top-1/2), floats out into a corner-tab chip on the top-left edge, and the field grows with its content via v4's field-sizing-content between min-h-30 and max-h-80 — no autosize library, no listeners.
## HTML
```html
<section class="tfl-14 w-full min-h-svh grid place-items-center bg-tfl14-bg px-5 py-12 font-tfl14-sans" aria-label="Textarea floating label demo">
  <form class="flex w-full max-w-[440px] flex-col gap-5 rounded-3xl bg-white p-8 shadow-[0_24px_60px_-32px_oklch(0.3_0.06_255/0.4)] ring-1 ring-tfl14-ink/5" novalidate>
    <div class="grid gap-1">
      <h3 class="text-2xl font-extrabold tracking-[-0.02em] text-tfl14-ink">Tell us what happened</h3>
      <p class="text-sm text-tfl14-mut">We reply within one business day.</p>
    </div>
    <div class="relative">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl14-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl14-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl14-line-hover focus:border-tfl14-acc focus:ring-4 focus:ring-tfl14-acc/15" type="text" id="tfl-14-subject" name="subject" placeholder=" ">
      <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 text-base text-tfl14-mut transition-[translate,scale,color] duration-[220ms] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:text-tfl14-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 motion-reduce:transition-none" for="tfl-14-subject">Subject</label>
    </div>
    <div class="relative mt-3">
      <textarea class="peer field-sizing-content min-h-30 max-h-80 w-full resize-y rounded-xl rounded-tl-sm border-[1.5px] border-tfl14-line bg-white px-4 py-3.5 text-base/[1.55] text-tfl14-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl14-line-hover focus:border-tfl14-acc focus:ring-4 focus:ring-tfl14-acc/15" id="tfl-14-msg" name="message" placeholder=" " rows="3" maxlength="600" aria-describedby="tfl-14-msg-hint"></textarea>
      <label class="pointer-events-none absolute left-4 top-[26px] z-[2] -ml-2.5 origin-left -translate-y-1/2 rounded-[8px_8px_8px_0] px-2.5 py-[3px] text-base text-tfl14-mut transition-[translate,scale,color,background-color] duration-[220ms] peer-focus:translate-x-[-6px] peer-focus:translate-y-[calc(-50%_-_36px)] peer-focus:scale-80 peer-focus:bg-tfl14-acc peer-focus:font-semibold peer-focus:text-white peer-[:not(:placeholder-shown)]:translate-x-[-6px] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_36px)] peer-[:not(:placeholder-shown)]:scale-80 peer-[:not(:placeholder-shown)]:bg-tfl14-ink peer-[:not(:placeholder-shown)]:font-semibold peer-[:not(:placeholder-shown)]:text-white peer-[:not(:placeholder-shown):focus]:bg-tfl14-acc motion-reduce:transition-none" for="tfl-14-msg">Describe the issue</label>
      <p class="mt-1.5 text-[13px]/snug text-tfl14-mut" id="tfl-14-msg-hint">The field grows as you type — up to 600 characters.</p>
    </div>
    <button class="min-h-12 cursor-pointer rounded-xl bg-tfl14-acc text-[15px] font-bold text-white shadow-[0_10px_24px_-12px_var(--color-tfl14-acc)] transition-[filter,scale] duration-150 hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl14-acc/50" type="button">Submit report</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl14-bg: #eef1f6;
  --color-tfl14-bg: oklch(0.96 0.008 255);
  --color-tfl14-ink: #1a2030;
  --color-tfl14-ink: oklch(0.23 0.03 260);
  --color-tfl14-mut: #5d6479;
  --color-tfl14-mut: oklch(0.5 0.03 262);
  --color-tfl14-line: #d3d8e4;
  --color-tfl14-line: oklch(0.88 0.015 260);
  --color-tfl14-line-hover: #b0b8ca;
  --color-tfl14-line-hover: oklch(0.78 0.025 260);
  --color-tfl14-acc: #2f5fcf;
  --color-tfl14-acc: oklch(0.52 0.18 262);
  --font-tfl14-sans: 'Public Sans', system-ui, sans-serif;
}

.tfl-14 {
  width: 100%;
  min-height: 100svh;
}
```

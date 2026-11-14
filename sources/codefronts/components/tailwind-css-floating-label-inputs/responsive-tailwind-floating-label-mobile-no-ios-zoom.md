---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/responsive-tailwind-floating-label-mobile-no-ios-zoom/"
title: "Responsive Tailwind Floating Label for Mobile (No iOS Zoom)"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "The mobile survival kit, now sized to the form rather than the screen: the form is an @container, and heights, paddings, type and the float distance are…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind Floating Label for Mobile (No iOS Zoom)
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/responsive-tailwind-floating-label-mobile-no-ios-zoom/

The mobile survival kit, now sized to the form rather than the screen: the form is an @container, and heights, paddings, type and the float distance are clamp()s over cqi container units. Input text is floored at 16px so iOS Safari never zoom-jumps, every target is ≥48px, and a tinted highlight lane gives the floated label its own track.
## HTML
```html
<section class="tfl-13 w-full min-h-svh grid place-items-center bg-tfl13-bg px-[clamp(12px,4vw,24px)] py-[clamp(16px,5vw,48px)] font-tfl13-sans" aria-label="Responsive mobile floating label demo">
  <form class="@container w-full max-w-[420px] rounded-[clamp(14px,3vw,22px)] bg-white shadow-[0_22px_55px_-30px_oklch(0.3_0.06_150/0.4)] ring-1 ring-tfl13-ink/5" novalidate>
    <div class="flex flex-col gap-[clamp(14px,4.5cqi,22px)] px-[clamp(16px,6cqi,32px)] py-[clamp(20px,7cqi,36px)]">
      <div class="grid gap-1">
        <h3 class="text-[clamp(21px,6.2cqi,26px)] font-extrabold tracking-[-0.02em] text-tfl13-ink">Get a quote</h3>
        <p class="text-[clamp(13px,3.4cqi,14px)]/normal text-tfl13-mut">Resize this panel — type, spacing and float distance scale with the form.</p>
      </div>
      <div class="relative before:pointer-events-none before:absolute before:inset-x-0.5 before:top-0.5 before:z-[1] before:h-[clamp(22px,6cqi,26px)] before:rounded-t-[10px] before:bg-tfl13-acc/0 before:transition-colors before:duration-[250ms] before:content-[''] focus-within:before:bg-tfl13-acc/12 has-[input:not(:placeholder-shown)]:before:bg-tfl13-acc/12 motion-reduce:before:transition-none">
        <input class="peer h-[clamp(54px,14cqi,60px)] w-full rounded-xl border-[1.5px] border-tfl13-line bg-white px-4 pt-[clamp(20px,5.5cqi,24px)] pb-[clamp(4px,1.5cqi,7px)] text-[max(16px,clamp(16px,4cqi,17px))] text-tfl13-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl13-line-hover focus:border-tfl13-acc focus:ring-4 focus:ring-tfl13-acc/15" type="text" id="tfl-13-name" name="name" placeholder=" " autocomplete="name">
        <label class="pointer-events-none absolute left-4 top-1/2 z-[2] origin-left -translate-y-1/2 text-[max(16px,clamp(16px,4cqi,17px))] text-tfl13-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_clamp(12px,3.5cqi,14px))] peer-focus:scale-70 peer-focus:font-semibold peer-focus:text-tfl13-acc-ink peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_clamp(12px,3.5cqi,14px))] peer-[:not(:placeholder-shown)]:scale-70 motion-reduce:transition-none" for="tfl-13-name">Full name</label>
      </div>
      <div class="relative before:pointer-events-none before:absolute before:inset-x-0.5 before:top-0.5 before:z-[1] before:h-[clamp(22px,6cqi,26px)] before:rounded-t-[10px] before:bg-tfl13-acc/0 before:transition-colors before:duration-[250ms] before:content-[''] focus-within:before:bg-tfl13-acc/12 has-[input:not(:placeholder-shown)]:before:bg-tfl13-acc/12 motion-reduce:before:transition-none">
        <input class="peer h-[clamp(54px,14cqi,60px)] w-full rounded-xl border-[1.5px] border-tfl13-line bg-white px-4 pt-[clamp(20px,5.5cqi,24px)] pb-[clamp(4px,1.5cqi,7px)] text-[max(16px,clamp(16px,4cqi,17px))] text-tfl13-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl13-line-hover focus:border-tfl13-acc focus:ring-4 focus:ring-tfl13-acc/15" type="tel" id="tfl-13-tel" name="tel" placeholder=" " inputmode="tel" autocomplete="tel">
        <label class="pointer-events-none absolute left-4 top-1/2 z-[2] origin-left -translate-y-1/2 text-[max(16px,clamp(16px,4cqi,17px))] text-tfl13-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_clamp(12px,3.5cqi,14px))] peer-focus:scale-70 peer-focus:font-semibold peer-focus:text-tfl13-acc-ink peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_clamp(12px,3.5cqi,14px))] peer-[:not(:placeholder-shown)]:scale-70 motion-reduce:transition-none" for="tfl-13-tel">Mobile number</label>
      </div>
      <div class="relative before:pointer-events-none before:absolute before:inset-x-0.5 before:top-0.5 before:z-[1] before:h-[clamp(22px,6cqi,26px)] before:rounded-t-[10px] before:bg-tfl13-acc/0 before:transition-colors before:duration-[250ms] before:content-[''] focus-within:before:bg-tfl13-acc/12 has-[input:not(:placeholder-shown)]:before:bg-tfl13-acc/12 motion-reduce:before:transition-none">
        <input class="peer h-[clamp(54px,14cqi,60px)] w-full rounded-xl border-[1.5px] border-tfl13-line bg-white px-4 pt-[clamp(20px,5.5cqi,24px)] pb-[clamp(4px,1.5cqi,7px)] text-[max(16px,clamp(16px,4cqi,17px))] text-tfl13-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl13-line-hover focus:border-tfl13-acc focus:ring-4 focus:ring-tfl13-acc/15" type="text" id="tfl-13-zip" name="postal-code" placeholder=" " inputmode="numeric" autocomplete="postal-code">
        <label class="pointer-events-none absolute left-4 top-1/2 z-[2] origin-left -translate-y-1/2 text-[max(16px,clamp(16px,4cqi,17px))] text-tfl13-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_clamp(12px,3.5cqi,14px))] peer-focus:scale-70 peer-focus:font-semibold peer-focus:text-tfl13-acc-ink peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_clamp(12px,3.5cqi,14px))] peer-[:not(:placeholder-shown)]:scale-70 motion-reduce:transition-none" for="tfl-13-zip">ZIP / Postcode</label>
      </div>
      <button class="min-h-12 h-[clamp(48px,13cqi,54px)] cursor-pointer rounded-xl bg-tfl13-acc-ink text-[clamp(15px,4cqi,16px)] font-bold text-white transition-[filter,scale] duration-150 hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl13-acc/60" type="button">Send my quote</button>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl13-bg: #eff4ef;
  --color-tfl13-bg: oklch(0.96 0.01 150);
  --color-tfl13-ink: #17251a;
  --color-tfl13-ink: oklch(0.24 0.03 150);
  --color-tfl13-mut: #56695b;
  --color-tfl13-mut: oklch(0.49 0.03 150);
  --color-tfl13-line: #ccd8cf;
  --color-tfl13-line: oklch(0.87 0.02 150);
  --color-tfl13-line-hover: #a9bcae;
  --color-tfl13-line-hover: oklch(0.77 0.03 150);
  --color-tfl13-acc: #2ea055;
  --color-tfl13-acc: oklch(0.62 0.15 150);
  --color-tfl13-acc-ink: #1d7a3d;
  --color-tfl13-acc-ink: oklch(0.5 0.13 150);
  --font-tfl13-sans: 'Hanken Grotesk', system-ui, sans-serif;
}

.tfl-13 {
  width: 100%;
  min-height: 100svh;
}
```

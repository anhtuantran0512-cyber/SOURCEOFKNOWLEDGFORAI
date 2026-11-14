---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-neumorphic-soft-ui-faq-accordion-cards/"
title: "Tailwind Neumorphic Soft-UI FAQ Accordion Cards"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "Soft-UI done responsibly: cards extruded from a single-material surface with the twin-shadow trick (light top-left, shade bottom-right), pressing physically…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neumorphic Soft-UI FAQ Accordion Cards
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-neumorphic-soft-ui-faq-accordion-cards/

Soft-UI done responsibly: cards extruded from a single-material surface with the twin-shadow trick (light top-left, shade bottom-right), pressing physically inset when opened — the material metaphor doing the state communication. Both shadow colours are color-mix() derivations of one surface token, so retheming is a one-line edit, and the two fixes that make neumorphism shippable are baked in.
## HTML
```html
<section class="tfa-09 w-full min-h-svh grid place-items-center bg-tfa09-surface font-tfa09-sans text-tfa09-ink px-5 py-12">
  <div class="w-[min(600px,100%)]">
    <header>
      <h1 class="text-[clamp(26px,4.5vw,36px)] font-extrabold tracking-[-0.02em]">Device support</h1>
      <p class="mt-3 max-w-[50ch] text-[14.5px] leading-relaxed text-tfa09-mut">One material, one light source. Open a card and it presses into the surface.</p>
    </header>

    <div data-panel class="mt-8 flex flex-col gap-[18px]">
      <details class="group rounded-[20px] bg-tfa09-surface shadow-[-8px_-8px_18px_var(--color-tfa09-hi),8px_8px_18px_var(--color-tfa09-lo)] [&:not([open]):hover]:shadow-[-10px_-10px_22px_var(--color-tfa09-hi),10px_10px_22px_var(--color-tfa09-lo)] open:shadow-[inset_-6px_-6px_14px_var(--color-tfa09-hi),inset_6px_6px_14px_var(--color-tfa09-lo)] transition-[box-shadow] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none" open>
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3.5 rounded-[20px] px-5 py-[18px] text-[15px] font-bold tracking-[-0.01em] transition-[translate,color] duration-250 hover:text-tfa09-acc focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tfa09-acc group-open:translate-x-px group-open:translate-y-px [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="size-2.5 shrink-0 rounded-full bg-tfa09-acc shadow-[-2px_-2px_4px_var(--color-tfa09-hi),2px_2px_4px_var(--color-tfa09-lo)]"></span>How do I pair a new device?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 rounded-[1px] border-b-[2.5px] border-r-[2.5px] border-tfa09-mut transition-[rotate,translate,border-color] duration-350 group-hover:border-tfa09-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa09-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[56ch] pb-[19px] pl-[42px] pr-5 text-[13.5px] leading-[1.75] text-tfa09-mut">Hold the side button for 3 seconds until the ring pulses, then open the app — pairing is automatic within arm's reach. Up to 8 devices can stay paired to one account.</p>
      </details>
      <details class="group rounded-[20px] bg-tfa09-surface shadow-[-8px_-8px_18px_var(--color-tfa09-hi),8px_8px_18px_var(--color-tfa09-lo)] [&:not([open]):hover]:shadow-[-10px_-10px_22px_var(--color-tfa09-hi),10px_10px_22px_var(--color-tfa09-lo)] open:shadow-[inset_-6px_-6px_14px_var(--color-tfa09-hi),inset_6px_6px_14px_var(--color-tfa09-lo)] transition-[box-shadow] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3.5 rounded-[20px] px-5 py-[18px] text-[15px] font-bold tracking-[-0.01em] transition-[translate,color] duration-250 hover:text-tfa09-acc focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tfa09-acc group-open:translate-x-px group-open:translate-y-px [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="size-2.5 shrink-0 rounded-full bg-tfa09-acc shadow-[-2px_-2px_4px_var(--color-tfa09-hi),2px_2px_4px_var(--color-tfa09-lo)]"></span>Why won't it charge past 80%?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 rounded-[1px] border-b-[2.5px] border-r-[2.5px] border-tfa09-mut transition-[rotate,translate,border-color] duration-350 group-hover:border-tfa09-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa09-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[56ch] pb-[19px] pl-[42px] pr-5 text-[13.5px] leading-[1.75] text-tfa09-mut">That is battery care mode, on by default — it doubles cell lifespan. Toggle “Full charge” in the app for trips; it reverts automatically after 48 hours.</p>
      </details>
      <details class="group rounded-[20px] bg-tfa09-surface shadow-[-8px_-8px_18px_var(--color-tfa09-hi),8px_8px_18px_var(--color-tfa09-lo)] [&:not([open]):hover]:shadow-[-10px_-10px_22px_var(--color-tfa09-hi),10px_10px_22px_var(--color-tfa09-lo)] open:shadow-[inset_-6px_-6px_14px_var(--color-tfa09-hi),inset_6px_6px_14px_var(--color-tfa09-lo)] transition-[box-shadow] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3.5 rounded-[20px] px-5 py-[18px] text-[15px] font-bold tracking-[-0.01em] transition-[translate,color] duration-250 hover:text-tfa09-acc focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tfa09-acc group-open:translate-x-px group-open:translate-y-px [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="size-2.5 shrink-0 rounded-full bg-tfa09-acc shadow-[-2px_-2px_4px_var(--color-tfa09-hi),2px_2px_4px_var(--color-tfa09-lo)]"></span>Is it waterproof?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 rounded-[1px] border-b-[2.5px] border-r-[2.5px] border-tfa09-mut transition-[rotate,translate,border-color] duration-350 group-hover:border-tfa09-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa09-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[56ch] pb-[19px] pl-[42px] pr-5 text-[13.5px] leading-[1.75] text-tfa09-mut">IP68 — pool and shower safe, and rinsing after salt water is recommended. The charging contacts are corrosion-sealed, so there are no port covers to lose.</p>
      </details>
      <details class="group rounded-[20px] bg-tfa09-surface shadow-[-8px_-8px_18px_var(--color-tfa09-hi),8px_8px_18px_var(--color-tfa09-lo)] [&:not([open]):hover]:shadow-[-10px_-10px_22px_var(--color-tfa09-hi),10px_10px_22px_var(--color-tfa09-lo)] open:shadow-[inset_-6px_-6px_14px_var(--color-tfa09-hi),inset_6px_6px_14px_var(--color-tfa09-lo)] transition-[box-shadow] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
        <summary class="flex min-h-11 cursor-pointer list-none items-center gap-3.5 rounded-[20px] px-5 py-[18px] text-[15px] font-bold tracking-[-0.01em] transition-[translate,color] duration-250 hover:text-tfa09-acc focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tfa09-acc group-open:translate-x-px group-open:translate-y-px [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="size-2.5 shrink-0 rounded-full bg-tfa09-acc shadow-[-2px_-2px_4px_var(--color-tfa09-hi),2px_2px_4px_var(--color-tfa09-lo)]"></span>How do I factory reset?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 rounded-[1px] border-b-[2.5px] border-r-[2.5px] border-tfa09-mut transition-[rotate,translate,border-color] duration-350 group-hover:border-tfa09-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa09-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[56ch] pb-[19px] pl-[42px] pr-5 text-[13.5px] leading-[1.75] text-tfa09-mut">Settings → Device → Reset in the app, or hold both buttons for 10 seconds until three pulses. Your data stays in the cloud and restores on next pairing.</p>
      </details>
    </div>

    <p class="mt-6 text-[12px] text-tfa09-mut">Twin shadows out = raised · inset = pressed. Contrast held at AA despite the single-hue palette.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa09-surface: #e6e9f0;
  --color-tfa09-surface: oklch(0.92 0.018 250);
  --color-tfa09-hi: #f7f9fc;
  --color-tfa09-hi: color-mix(in oklch, var(--color-tfa09-surface) 35%, white);
  --color-tfa09-lo: #c3c8d6;
  --color-tfa09-lo: color-mix(in oklch, var(--color-tfa09-surface) 72%, oklch(0.55 0.06 260));
  --color-tfa09-ink: #333a4d;
  --color-tfa09-ink: oklch(0.3 0.04 260);
  --color-tfa09-mut: #565e73;
  --color-tfa09-mut: oklch(0.42 0.035 258);
  --color-tfa09-acc: #4a5fd0;
  --color-tfa09-acc: oklch(0.5 0.17 262);
  --font-tfa09-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tfa-09 {
  width: 100%;
  min-height: 100svh;
}

.tfa-09 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-09 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .38s allow-discrete;
  }

  .tfa-09 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-09 details::details-content {
    transition-duration: 1ms;
  }
}
```

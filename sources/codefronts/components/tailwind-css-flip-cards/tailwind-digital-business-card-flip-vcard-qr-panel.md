---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-digital-business-card-flip-vcard-qr-panel/"
title: "Tailwind Digital Business Card Flip with vCard Contacts & QR Panel"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A landscape name card with a holographic edge strip; the back carries phone, email and office as real tel: and mailto: links beside a QR panel."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Digital Business Card Flip with vCard Contacts & QR Panel
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-digital-business-card-flip-vcard-qr-panel/

A landscape name card with a holographic edge strip; the back carries phone, email and office as real tel: and mailto: links beside a QR panel. The port turns three styled divs into actionable links and marks the card up as an h-card microformat, so a contact scraper gets structured data rather than decorated text.
## HTML
```html
<section class="tfc-12 w-full min-h-svh grid place-items-center content-center gap-4 bg-tfc12-bg font-tfc12-sans px-5 py-10 text-tfc12-ink">
  <p class="text-center text-[10px] font-semibold uppercase tracking-[0.2em] text-tfc12-dim">Digital business card &middot; hover, tap or press Space</p>
  <div class="group relative mx-auto h-[230px] w-[380px] max-w-full [perspective:1200px] rounded-2xl print:w-[85.6mm] print:h-[54mm] has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc12-cyan has-[:focus-visible]:outline-offset-4">
    <input id="tfc-12-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-12-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show contact details and QR code</span></label>

    <div class="relative h-full w-full transition-transform duration-700 ease-[cubic-bezier(.4,0,.2,1)] [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)] group-has-checked:[transform:rotateY(180deg)] group-has-[:focus-visible]:[transform:rotateY(180deg)] motion-reduce:transition-none">

      <div class="h-card absolute inset-0 flex items-center gap-5 rounded-2xl overflow-hidden px-7 py-6 bg-linear-135 from-tfc12-panel to-tfc12-panel2 border border-tfc12-cyan/25 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_20px_44px_-18px_oklch(0.5_0.12_205/0.4)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <span aria-hidden="true" class="absolute inset-y-0 right-15 w-1 bg-linear-180 from-transparent via-tfc12-cyan/40 to-transparent"></span>
        <span aria-hidden="true" class="absolute inset-y-0 right-15 w-1 bg-linear-180 from-transparent via-tfc12-violet/40 to-transparent opacity-70"></span>
        <span class="grid size-15 shrink-0 place-items-center rounded-2xl bg-linear-135 from-tfc12-cyan2 to-tfc12-teal text-[22px] font-black text-white shadow-[0_0_20px_oklch(0.65_0.13_205/0.3)]">JD</span>
        <div class="flex-1">
          <p class="p-name text-xl font-extrabold tracking-[-0.02em] text-white">James Dorian</p>
          <p class="p-job-title mt-0.5 text-[11px] font-semibold tracking-[0.06em] text-tfc12-cyan">Chief Technology Officer</p>
          <span class="my-2.5 block h-px bg-white/8"></span>
          <p class="p-org text-[13px] text-tfc12-muted">Nova Systems Inc.</p>
          <div class="mt-2 flex flex-col gap-1 text-[11px] text-tfc12-dim">
            <span class="flex items-center gap-1.5"><span class="size-1 rounded-full bg-tfc12-cyan/60"></span>+1 (415) 555-0198</span>
            <span class="flex items-center gap-1.5"><span class="size-1 rounded-full bg-tfc12-cyan/60"></span>[email protected]</span>
          </div>
        </div>
      </div>

      <div class="absolute inset-0 flex items-center gap-5 rounded-2xl overflow-hidden px-6 py-5 bg-linear-135 from-tfc12-back to-tfc12-back2 border border-tfc12-cyan/20 shadow-[0_1px_2px_oklch(0_0_0/0.5),0_20px_44px_-18px_oklch(0.5_0.12_205/0.4)] [transform:rotateY(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <ul class="relative z-30 flex flex-1 flex-col gap-1.5">
          <li><a href="tel:+14155550198" class="p-tel flex min-h-11 items-center gap-2.5 rounded-lg px-1 no-underline transition-colors duration-200 hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-tfc12-cyan focus-visible:outline-offset-2">
            <span class="grid size-8 shrink-0 place-items-center rounded-lg border border-tfc12-cyan/20 bg-tfc12-cyan/10"><svg viewBox="0 0 24 24" class="size-3.5 fill-none stroke-tfc12-cyan stroke-[1.8]" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.43 2 2 0 0 1 3.6 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.6a16 16 0 0 0 6 6l.92-.92a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.73 16z"/></svg></span>
            <span class="flex flex-col"><span class="text-[9px] uppercase tracking-[0.1em] text-tfc12-dim">Phone</span><span class="text-xs font-semibold text-tfc12-ink/85">+1 (415) 555-0198</span></span>
          </a></li>
          <li><a href="mailto:[email protected]" class="u-email flex min-h-11 items-center gap-2.5 rounded-lg px-1 no-underline transition-colors duration-200 hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-tfc12-cyan focus-visible:outline-offset-2">
            <span class="grid size-8 shrink-0 place-items-center rounded-lg border border-tfc12-cyan/20 bg-tfc12-cyan/10"><svg viewBox="0 0 24 24" class="size-3.5 fill-none stroke-tfc12-cyan stroke-[1.8]" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 7L2 7"/></svg></span>
            <span class="flex flex-col"><span class="text-[9px] uppercase tracking-[0.1em] text-tfc12-dim">Email</span><span class="text-xs font-semibold text-tfc12-ink/85">[email protected]</span></span>
          </a></li>
          <li><a href="https://maps.example.com/novasys" class="p-adr flex min-h-11 items-center gap-2.5 rounded-lg px-1 no-underline transition-colors duration-200 hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-tfc12-cyan focus-visible:outline-offset-2">
            <span class="grid size-8 shrink-0 place-items-center rounded-lg border border-tfc12-cyan/20 bg-tfc12-cyan/10"><svg viewBox="0 0 24 24" class="size-3.5 fill-none stroke-tfc12-cyan stroke-[1.8]" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
            <span class="flex flex-col"><span class="text-[9px] uppercase tracking-[0.1em] text-tfc12-dim">Office</span><span class="text-xs font-semibold text-tfc12-ink/85">San Francisco &middot; Floor 22</span></span>
          </a></li>
        </ul>
        <figure class="m-0 flex shrink-0 flex-col items-center gap-1.5">
          <span class="grid size-25 place-items-center rounded-xl bg-white p-1.5">
            <svg viewBox="0 0 21 21" fill="black" class="size-full" aria-hidden="true">
              <rect x="0" y="0" width="7" height="7" fill="none" stroke="black" stroke-width="1"/><rect x="2" y="2" width="3" height="3"/>
              <rect x="14" y="0" width="7" height="7" fill="none" stroke="black" stroke-width="1"/><rect x="16" y="2" width="3" height="3"/>
              <rect x="0" y="14" width="7" height="7" fill="none" stroke="black" stroke-width="1"/><rect x="2" y="16" width="3" height="3"/>
              <rect x="8" y="0" width="1" height="1"/><rect x="10" y="0" width="1" height="1"/><rect x="12" y="0" width="1" height="1"/>
              <rect x="9" y="2" width="1" height="1"/><rect x="11" y="2" width="1" height="1"/>
              <rect x="8" y="4" width="1" height="1"/><rect x="10" y="4" width="2" height="1"/><rect x="13" y="4" width="1" height="1"/>
              <rect x="7" y="7" width="1" height="1"/><rect x="9" y="7" width="2" height="1"/><rect x="12" y="7" width="1" height="1"/>
              <rect x="7" y="9" width="2" height="1"/><rect x="11" y="9" width="1" height="1"/><rect x="13" y="9" width="1" height="1"/>
              <rect x="8" y="11" width="1" height="1"/><rect x="10" y="11" width="2" height="1"/><rect x="14" y="11" width="1" height="1"/>
              <rect x="7" y="13" width="1" height="1"/><rect x="9" y="13" width="1" height="1"/><rect x="12" y="13" width="2" height="1"/>
              <rect x="8" y="14" width="2" height="1"/><rect x="12" y="14" width="1" height="1"/><rect x="14" y="14" width="1" height="1"/>
              <rect x="9" y="16" width="1" height="1"/><rect x="11" y="16" width="3" height="1"/>
              <rect x="8" y="18" width="2" height="1"/><rect x="12" y="18" width="1" height="1"/><rect x="14" y="18" width="1" height="1"/>
              <rect x="9" y="20" width="1" height="1"/><rect x="11" y="20" width="2" height="1"/><rect x="14" y="20" width="1" height="1"/>
            </svg>
          </span>
          <figcaption class="text-[8px] uppercase tracking-[0.1em] text-tfc12-dim">Sample pattern</figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc12-bg: #04080c;
  --color-tfc12-bg: oklch(0.12 0.01 230);
  --color-tfc12-panel: #0a1520;
  --color-tfc12-panel: oklch(0.18 0.025 240);
  --color-tfc12-panel2: #040e18;
  --color-tfc12-panel2: oklch(0.14 0.02 240);
  --color-tfc12-back: #060e18;
  --color-tfc12-back: oklch(0.15 0.02 240);
  --color-tfc12-back2: #040a12;
  --color-tfc12-back2: oklch(0.12 0.015 240);
  --color-tfc12-cyan: #06b6d4;
  --color-tfc12-cyan: oklch(0.7 0.14 205);
  --color-tfc12-cyan2: #0891b2;
  --color-tfc12-cyan2: oklch(0.6 0.12 210);
  --color-tfc12-teal: #0e7490;
  --color-tfc12-teal: oklch(0.5 0.1 215);
  --color-tfc12-violet: #8b5cf6;
  --color-tfc12-violet: oklch(0.63 0.2 295);
  --color-tfc12-ink: #f0f9ff;
  --color-tfc12-ink: oklch(0.97 0.015 230);
  --color-tfc12-muted: #9fb2c2;
  --color-tfc12-muted: oklch(0.76 0.025 235);
  --color-tfc12-dim: #7b8b99;
  --color-tfc12-dim: oklch(0.63 0.02 235);
  --font-tfc12-sans: 'Sora', system-ui, sans-serif;
}

.tfc-12 {
  width: 100%;
  min-height: 100svh;
}
/* Print: flatten the 3D context and show the front face at ID-1 card size. */

@media print {
  .tfc-12 [style],
    .tfc-12 * {
    transform: none !important;
  }

  .tfc-12 {
    min-height: auto;
    background: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfc-12 * {
    transition-duration: 1ms !important;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/bootstrap-5-accordion-rebuilt-in-tailwind/"
title: "Bootstrap 5 Accordion Rebuilt in Tailwind (and the JavaScript You Delete)"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The migration demo."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bootstrap 5 Accordion Rebuilt in Tailwind (and the JavaScript You Delete)
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/bootstrap-5-accordion-rebuilt-in-tailwind/

The migration demo. Bootstrap's accordion needs bootstrap.bundle.js, a data-bs-parent wiring convention and roughly twenty --bs-accordion-* variables to retheme. The same component in Tailwind is a <details name> group plus one class list: identical look and identical exclusive behaviour, with the JavaScript dependency deleted rather than ported.
## HTML
```html
<section class="tfa-23 w-full min-h-svh grid place-items-center bg-tfa23-bg font-tfa23-sans text-tfa23-ink px-5 py-12">
  <div class="w-[min(660px,100%)]">
    <header>
      <h1 class="text-[clamp(26px,4.6vw,38px)] font-extrabold tracking-[-0.025em]">The Bootstrap accordion, minus Bootstrap</h1>
      <p class="mt-3 max-w-[56ch] text-[15px] leading-relaxed text-tfa23-mut">Same 48px rows, tinted active header and focus glow. <code class="rounded bg-tfa23-tint px-1.5 py-0.5 font-tfa23-mono text-[0.87em] text-tfa23-acc">data-bs-parent</code> becomes <code class="rounded bg-tfa23-tint px-1.5 py-0.5 font-tfa23-mono text-[0.87em] text-tfa23-acc">name</code>, and the bundle goes away.</p>
    </header>

    <div data-panel class="mt-7 overflow-hidden rounded-[14px] border border-tfa23-edge bg-tfa23-panel">
        <details name="tfa23-acc" class="group border-b border-tfa23-edge last:border-b-0" open>
          <summary class="flex min-h-12 cursor-pointer list-none items-center gap-4 bg-transparent px-[18px] py-4 text-[15px] font-semibold text-tfa23-ink transition-colors duration-250 hover:text-tfa23-acc focus-visible:outline-none focus-visible:ring-3 focus-visible:ring-tfa23-ring group-open:bg-tfa23-activebg group-open:text-tfa23-acc [&::-webkit-details-marker]:hidden">Can I really drop the JavaScript?
            <span aria-hidden="true" class="ml-auto shrink-0 text-tfa23-mut transition-[rotate,color] duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-open:-rotate-180 group-open:text-tfa23-acc motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="18" height="18"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <p class="px-[18px] pb-[17px] text-[13.5px] leading-[1.7] text-tfa23-mut">Yes, for the accordion. Exclusivity was the only thing the plugin did that markup could not — and the <em>name</em> attribute does it natively now. Modals and dropdowns are different conversations; disclosure is settled.</p>
        </details>
        <details name="tfa23-acc" class="group border-b border-tfa23-edge last:border-b-0">
          <summary class="flex min-h-12 cursor-pointer list-none items-center gap-4 bg-transparent px-[18px] py-4 text-[15px] font-semibold text-tfa23-ink transition-colors duration-250 hover:text-tfa23-acc focus-visible:outline-none focus-visible:ring-3 focus-visible:ring-tfa23-ring group-open:bg-tfa23-activebg group-open:text-tfa23-acc [&::-webkit-details-marker]:hidden">Which Bootstrap variables map to what?
            <span aria-hidden="true" class="ml-auto shrink-0 text-tfa23-mut transition-[rotate,color] duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-open:-rotate-180 group-open:text-tfa23-acc motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="18" height="18"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <p class="px-[18px] pb-[17px] text-[13.5px] leading-[1.7] text-tfa23-mut">The visible ten — background, colour, border colour, radius, button colour, active background, active colour, focus glow and the two icon data-URIs — become a handful of theme tokens plus inline utilities. The paddings you rarely touched need no tokens at all.</p>
        </details>
        <details name="tfa23-acc" class="group border-b border-tfa23-edge last:border-b-0">
          <summary class="flex min-h-12 cursor-pointer list-none items-center gap-4 bg-transparent px-[18px] py-4 text-[15px] font-semibold text-tfa23-ink transition-colors duration-250 hover:text-tfa23-acc focus-visible:outline-none focus-visible:ring-3 focus-visible:ring-tfa23-ring group-open:bg-tfa23-activebg group-open:text-tfa23-acc [&::-webkit-details-marker]:hidden">How do I recolour the chevron now?
            <span aria-hidden="true" class="ml-auto shrink-0 text-tfa23-mut transition-[rotate,color] duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-open:-rotate-180 group-open:text-tfa23-acc motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="18" height="18"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <p class="px-[18px] pb-[17px] text-[13.5px] leading-[1.7] text-tfa23-mut">It is an inline SVG with stroke: currentColor, so a text-colour utility does it. No percent-encoded data-URI pair, and no more icons vanishing because a hash was not escaped as %23.</p>
        </details>
        <details name="tfa23-acc" class="group border-b border-tfa23-edge last:border-b-0">
          <summary class="flex min-h-12 cursor-pointer list-none items-center gap-4 bg-transparent px-[18px] py-4 text-[15px] font-semibold text-tfa23-ink transition-colors duration-250 hover:text-tfa23-acc focus-visible:outline-none focus-visible:ring-3 focus-visible:ring-tfa23-ring group-open:bg-tfa23-activebg group-open:text-tfa23-acc [&::-webkit-details-marker]:hidden">Does this survive upgrades?
            <span aria-hidden="true" class="ml-auto shrink-0 text-tfa23-mut transition-[rotate,color] duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-open:-rotate-180 group-open:text-tfa23-acc motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="18" height="18"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <p class="px-[18px] pb-[17px] text-[13.5px] leading-[1.7] text-tfa23-mut">Better than either alternative: there is no library version to track. The markup is platform HTML and the styles are utilities compiled from your own config.</p>
        </details>
    </div>

    <p class="mt-5 text-[12.5px] text-tfa23-mut">Zero JS in this demo — the CSS collection's version needed a 12-line collapse shim just to preview.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa23-bg: #141a1f;
  --color-tfa23-bg: oklch(0.19 0.015 240);
  --color-tfa23-panel: #1a2128;
  --color-tfa23-panel: oklch(0.23 0.018 240);
  --color-tfa23-activebg: #1f2d34;
  --color-tfa23-activebg: oklch(0.27 0.03 200);
  --color-tfa23-ink: #eaf0f4;
  --color-tfa23-ink: oklch(0.95 0.008 230);
  --color-tfa23-mut: #b0bcc4;
  --color-tfa23-mut: oklch(0.79 0.015 235);
  --color-tfa23-edge: #333e47;
  --color-tfa23-edge: oklch(0.33 0.022 235);
  --color-tfa23-tint: #1f3a33;
  --color-tfa23-tint: oklch(0.28 0.045 165);
  --color-tfa23-ring: #3f7f68;
  --color-tfa23-ring: oklch(0.55 0.08 165 / 0.45);
  --color-tfa23-acc: #7fd8ab;
  --color-tfa23-acc: oklch(0.84 0.13 165);
  --font-tfa23-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa23-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-23 {
  width: 100%;
  min-height: 100svh;
}

.tfa-23 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-23 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .35s allow-discrete;
  }

  .tfa-23 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-23 details::details-content {
    transition-duration: 1ms;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-dark-mode-faq-accordion-light-dark/"
title: "Tailwind Dark Mode FAQ Accordion with light-dark() and No .dark Class"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The counter-argument to dark:."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode FAQ Accordion with light-dark() and No .dark Class
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-dark-mode-faq-accordion-light-dark/

The counter-argument to dark:. Every colour is declared once as a light-dark() pair inside @theme, and a single color-scheme flip re-skins the whole component — including native scrollbars, form controls and selection colours that a .dark class never reaches. A true two-way switch that starts from the visitor's OS preference, with zero duplicated utilities, a small seed script, and a View Transition cross-fade.
## HTML
```html
<section class="tfa-06 group/tfa06 w-full min-h-svh grid place-items-center bg-tfa06-bg font-tfa06-sans text-tfa06-ink px-5 py-12 [color-scheme:light] has-[#tfa06-mode:checked]:[color-scheme:dark]">
  <div class="w-[min(660px,100%)]">
    <div class="flex items-center justify-between gap-4">
      <span class="text-[14px] font-extrabold tracking-[-0.01em]">Nightshift Docs</span>
      <input id="tfa06-mode" type="checkbox" role="switch" class="peer absolute opacity-0 pointer-events-none">
      <label for="tfa06-mode" title="Dark theme" class="flex min-h-11 cursor-pointer items-center gap-2 rounded-full border border-tfa06-edge bg-tfa06-panel px-2.5 py-1.5 text-tfa06-mut hover:border-tfa06-accedge peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tfa06-acc">
        <span aria-hidden="true" class="text-tfa06-sun"><svg viewBox="0 0 24 24" width="13" height="13"><circle cx="12" cy="12" r="4.4" fill="currentColor"/><g stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5 5l2.1 2.1M16.9 16.9L19 19M19 5l-2.1 2.1M7.1 16.9L5 19"/></g></svg></span>
        <span aria-hidden="true" class="relative h-5 w-9 rounded-full bg-tfa06-edge group-has-[#tfa06-mode:checked]/tfa06:bg-tfa06-acc after:absolute after:left-0.5 after:top-0.5 after:size-4 after:rounded-full after:bg-tfa06-panel after:shadow-[0_1px_4px_var(--color-tfa06-shadow)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-[#tfa06-mode:checked]/tfa06:after:translate-x-4 motion-reduce:after:transition-none"></span>
        <span aria-hidden="true" class="group-has-[#tfa06-mode:checked]/tfa06:text-tfa06-acc"><svg viewBox="0 0 24 24" width="13" height="13"><path d="M20 14.5A8.5 8.5 0 019.5 4a8.5 8.5 0 1010.5 10.5z" fill="currentColor"/></svg></span>
        <span class="sr-only">Dark theme</span>
      </label>
    </div>

    <header class="mt-7">
      <h1 class="text-[clamp(28px,5vw,38px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Frequently asked questions</h1>
      <p class="mt-3 max-w-[54ch] text-[14.5px] leading-[1.7] text-tfa06-mut">Every colour below is one <code class="rounded bg-tfa06-tint px-1.5 py-0.5 font-tfa06-mono text-[0.87em] text-tfa06-acc">light-dark()</code> token. Flip the switch — or your OS theme — and the whole component re-skins.</p>
    </header>

    <div data-panel class="mt-6 flex flex-col gap-2.5">
      <details class="group rounded-2xl border border-tfa06-edge bg-tfa06-panel shadow-[0_4px_16px_var(--color-tfa06-shadow)] open:border-tfa06-accedge" open>
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-4 text-[15px] font-semibold hover:text-tfa06-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa06-acc [&::-webkit-details-marker]:hidden">Does dark mode save battery?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa06-mut transition-[rotate,translate] duration-350 group-hover:border-tfa06-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa06-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[58ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa06-mut">On OLED screens, meaningfully — black pixels are unlit. On LCD panels the backlight runs regardless, so the gain is comfort, not power.</p>
      </details>
      <details class="group rounded-2xl border border-tfa06-edge bg-tfa06-panel shadow-[0_4px_16px_var(--color-tfa06-shadow)] open:border-tfa06-accedge">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-4 text-[15px] font-semibold hover:text-tfa06-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa06-acc [&::-webkit-details-marker]:hidden">Why not just add a .dark class?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa06-mut transition-[rotate,translate] duration-350 group-hover:border-tfa06-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa06-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[58ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa06-mut">Class-swapping duplicates every colour rule and misses native UI: scrollbars, form controls and selection colours stay light. <code class="rounded bg-tfa06-tint px-1.5 py-0.5 font-tfa06-mono text-[0.87em] text-tfa06-acc">color-scheme</code> re-skins those for free, and <code class="rounded bg-tfa06-tint px-1.5 py-0.5 font-tfa06-mono text-[0.87em] text-tfa06-acc">light-dark()</code> keeps each token in one place.</p>
      </details>
      <details class="group rounded-2xl border border-tfa06-edge bg-tfa06-panel shadow-[0_4px_16px_var(--color-tfa06-shadow)] open:border-tfa06-accedge">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-4 text-[15px] font-semibold hover:text-tfa06-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa06-acc [&::-webkit-details-marker]:hidden">Should dark mode be pure black?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa06-mut transition-[rotate,translate] duration-350 group-hover:border-tfa06-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa06-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[58ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa06-mut">Usually no — near-black surfaces (this panel is oklch 0.22) reduce smearing on OLED and let shadows still read. Reserve true black for media canvases.</p>
      </details>
      <details class="group rounded-2xl border border-tfa06-edge bg-tfa06-panel shadow-[0_4px_16px_var(--color-tfa06-shadow)] open:border-tfa06-accedge">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-4 text-[15px] font-semibold hover:text-tfa06-acc focus-visible:rounded-2xl focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa06-acc [&::-webkit-details-marker]:hidden">How do I persist the user's choice?
          <i aria-hidden="true" class="ml-auto size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa06-mut transition-[rotate,translate] duration-350 group-hover:border-tfa06-acc group-open:translate-y-0.5 group-open:rotate-[225deg] group-open:border-tfa06-acc motion-reduce:transition-none"></i>
        </summary>
        <p class="max-w-[58ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa06-mut">Store one value ('light' / 'dark' / 'auto') in localStorage and restore it before first paint in a tiny inline script. The utilities need zero changes — you are only setting the checkbox.</p>
      </details>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa06-mut">Starts from your OS preference, then the switch wins both ways. Checked = <code class="rounded bg-tfa06-tint px-1.5 py-0.5 font-tfa06-mono text-[0.87em] text-tfa06-acc">has-[#tfa06-mode:checked]:[color-scheme:dark]</code>.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  /* Every entry: a plain light value first (pre-2024 floor), then the light-dark() pair. */
  --color-tfa06-bg: #f8f9fc;
  --color-tfa06-bg: light-dark(oklch(0.975 0.008 250), oklch(0.17 0.02 258));
  --color-tfa06-panel: #ffffff;
  --color-tfa06-panel: light-dark(oklch(1 0 0), oklch(0.22 0.022 258));
  --color-tfa06-ink: #2b2f3a;
  --color-tfa06-ink: light-dark(oklch(0.22 0.025 258), oklch(0.96 0.006 250));
  --color-tfa06-mut: #5f6472;
  --color-tfa06-mut: light-dark(oklch(0.47 0.02 255), oklch(0.79 0.015 252));
  --color-tfa06-edge: #e4e6ee;
  --color-tfa06-edge: light-dark(oklch(0.91 0.01 250), oklch(0.32 0.025 256));
  --color-tfa06-accedge: #8ba6e8;
  --color-tfa06-accedge: light-dark(oklch(0.72 0.1 255), oklch(0.55 0.11 250));
  --color-tfa06-tint: #eaeffc;
  --color-tfa06-tint: light-dark(oklch(0.95 0.025 255), oklch(0.27 0.045 252));
  --color-tfa06-acc: #3f5fd0;
  --color-tfa06-acc: light-dark(oklch(0.48 0.19 260), oklch(0.8 0.12 250));
  --color-tfa06-sun: #d99b2b;
  --color-tfa06-sun: light-dark(oklch(0.68 0.14 75), oklch(0.78 0.14 75));
  --color-tfa06-shadow: #d7dae6;
  --color-tfa06-shadow: light-dark(oklch(0.3 0.05 255 / 0.1), oklch(0 0 0 / 0.4));
  --font-tfa06-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa06-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Scheme default is the [color-scheme:light] utility on the root, NOT a rule here:
   unlayered CSS beats Tailwind's utilities layer, so declaring it here would silently defeat
   has-checked:[color-scheme:dark]. */

.tfa-06 {
  width: 100%;
  min-height: 100svh;
}
/* light-dark() tokens do not change computed value when color-scheme flips, so a CSS colour
   transition on them freezes at the start colour in Chromium. The cross-fade is a View
   Transition instead; these two lines just set its timing. */

::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: .45s;
  animation-timing-function: cubic-bezier(.4,0,.2,1);
}

.tfa-06 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-06 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .38s allow-discrete;
  }

  .tfa-06 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-06 details::details-content {
    transition-duration: 1ms;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.tfa-06');if(!root||root.dataset.tfa06)return;root.dataset.tfa06='1';
  var cb=root.querySelector('#tfa06-mode'),mq=window.matchMedia('(prefers-color-scheme: dark)'),touched=false;
  cb.checked=mq.matches;
  var calm=window.matchMedia('(prefers-reduced-motion: reduce)');
  cb.addEventListener('click',function(e){
    touched=true;
    if(!document.startViewTransition||calm.matches)return;
    var next=cb.checked;e.preventDefault();
    document.startViewTransition(function(){cb.checked=next;});
  });
  mq.addEventListener('change',function(e){if(!touched)cb.checked=e.matches;});
})();
```

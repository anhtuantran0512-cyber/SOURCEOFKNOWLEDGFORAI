---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-wave-section-divider-footer-transition/"
title: "Tailwind Wave Section Divider Footer Transition"
section: "layouts"
category: "tailwind-css-wave-section-dividers"
category_name: "Tailwind CSS Wave Section Dividers"
description: "The seamless hand-off into a dark footer: a curved cutout at the footer&rsquo;s top edge scoops the page into it, so the footer reads as the bottom of one…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Wave Section Divider Footer Transition
Source: https://codefronts.com/layouts/tailwind-css-wave-section-dividers/tailwind-wave-section-divider-footer-transition/

The seamless hand-off into a dark footer: a curved cutout at the footer&rsquo;s top edge scoops the page into it, so the footer reads as the bottom of one continuous surface rather than a bolted-on slab. Plus the scalloped variant, which needs no SVG node at all.
## HTML
```html
<section class="twd-05 w-full min-h-svh flex flex-col font-twd05-sans">

  <!-- Curved cutout into a dark footer -->
  <div class="bg-twd05-page text-twd05-pageink px-6 pt-14 pb-10 text-center">
    <p class="text-[15px]">Last content section of the page.</p>
  </div>
  <footer class="relative overflow-hidden bg-twd05-footer text-white px-6 pt-[clamp(100px,14vw,160px)] pb-8">
    <svg class="absolute inset-x-0 -top-px block w-full h-[clamp(56px,9vw,110px)] text-twd05-page [&_path]:fill-current pointer-events-none" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,64 C240,120 480,8 720,40 C960,72 1200,120 1440,72 L1440,0 L0,0 Z"></path>
    </svg>
    <nav aria-label="Footer" class="grid grid-cols-[repeat(auto-fit,minmax(140px,1fr))] gap-7 max-w-[760px] mx-auto">
      <div class="flex flex-col gap-1.5">
        <h3 class="text-xs tracking-[0.14em] uppercase font-semibold text-twd05-accent mb-1">Product</h3>
        <a href="#0" class="w-fit min-h-11 flex items-center text-[14.5px] text-twd05-onfooter no-underline hover:text-white hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-twd05-accent focus-visible:outline-offset-3 rounded-sm">Features</a>
        <a href="#0" class="w-fit min-h-11 flex items-center text-[14.5px] text-twd05-onfooter no-underline hover:text-white hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-twd05-accent focus-visible:outline-offset-3 rounded-sm">Pricing</a>
        <a href="#0" class="w-fit min-h-11 flex items-center text-[14.5px] text-twd05-onfooter no-underline hover:text-white hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-twd05-accent focus-visible:outline-offset-3 rounded-sm">Changelog</a>
      </div>
      <div class="flex flex-col gap-1.5">
        <h3 class="text-xs tracking-[0.14em] uppercase font-semibold text-twd05-accent mb-1">Resources</h3>
        <a href="#0" class="w-fit min-h-11 flex items-center text-[14.5px] text-twd05-onfooter no-underline hover:text-white hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-twd05-accent focus-visible:outline-offset-3 rounded-sm">Docs</a>
        <a href="#0" class="w-fit min-h-11 flex items-center text-[14.5px] text-twd05-onfooter no-underline hover:text-white hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-twd05-accent focus-visible:outline-offset-3 rounded-sm">Snippets</a>
        <a href="#0" class="w-fit min-h-11 flex items-center text-[14.5px] text-twd05-onfooter no-underline hover:text-white hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-twd05-accent focus-visible:outline-offset-3 rounded-sm">Support</a>
      </div>
      <div class="flex flex-col gap-1.5">
        <h3 class="text-xs tracking-[0.14em] uppercase font-semibold text-twd05-accent mb-1">Company</h3>
        <a href="#0" class="w-fit min-h-11 flex items-center text-[14.5px] text-twd05-onfooter no-underline hover:text-white hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-twd05-accent focus-visible:outline-offset-3 rounded-sm">About</a>
        <a href="#0" class="w-fit min-h-11 flex items-center text-[14.5px] text-twd05-onfooter no-underline hover:text-white hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-twd05-accent focus-visible:outline-offset-3 rounded-sm">Careers</a>
        <a href="#0" class="w-fit min-h-11 flex items-center text-[14.5px] text-twd05-onfooter no-underline hover:text-white hover:underline hover:underline-offset-4 focus-visible:outline-2 focus-visible:outline-twd05-accent focus-visible:outline-offset-3 rounded-sm">Contact</a>
      </div>
    </nav>
    <p class="mt-8 text-center text-[12.5px] text-twd05-fine">&copy; 2027 codefronts.com &mdash; wave divider snippets.</p>
  </footer>

  <!-- Scalloped footer edge, no SVG -->
  <div class="bg-twd05-cream text-twd05-creamink px-6 pt-14 pb-9 text-center">
    <p class="text-[15px]">Newsletter, testimonials, whatever sits above your footer.</p>
  </div>
  <footer class="relative bg-twd05-clay text-white px-6 pt-20 pb-11 text-center before:content-[''] before:absolute before:inset-x-0 before:-top-px before:h-[34px] before:bg-twd05-cream before:pointer-events-none before:[mask:radial-gradient(28px_at_50%_100%,transparent_98%,#000)_repeat-x_0_0/56px_34px]">
    <p class="text-[clamp(22px,3.4vw,32px)] font-bold tracking-[-0.02em] mb-2">codefronts</p>
    <p class="text-sm text-twd05-onclay max-w-[52ch] mx-auto">Scallops read friendlier than a single deep curve &mdash; good for consumer and education sites.</p>
  </footer>

</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twd05-page: #f3f5f8;
  --color-twd05-page: oklch(0.96 0.01 250);
  --color-twd05-pageink: #414755;
  --color-twd05-pageink: oklch(0.42 0.02 250);
  --color-twd05-footer: #182028;
  --color-twd05-footer: oklch(0.2 0.03 250);
  --color-twd05-onfooter: #dfe4ea;
  --color-twd05-onfooter: oklch(0.9 0.01 250);
  --color-twd05-fine: #b3bcc5;
  --color-twd05-fine: oklch(0.78 0.01 250);
  --color-twd05-accent: #55d6cb;
  --color-twd05-accent: oklch(0.83 0.12 182);
  --color-twd05-cream: #fbf5ec;
  --color-twd05-cream: oklch(0.97 0.02 60);
  --color-twd05-creamink: #4c4239;
  --color-twd05-creamink: oklch(0.42 0.03 60);
  --color-twd05-clay: #40231d;
  --color-twd05-clay: oklch(0.26 0.06 22);
  --color-twd05-onclay: #e8d5d0;
  --color-twd05-onclay: oklch(0.88 0.02 22);
  --font-twd05-sans: 'Space Grotesk', system-ui, sans-serif;
}

.twd-05 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 15.4 mask shim for the scalloped edge — no prefixed variant form exists. */

.twd-05 footer::before {
  -webkit-mask: radial-gradient(28px at 50% 100%, transparent 98%, #000) repeat-x 0 0/56px 34px;
}
```

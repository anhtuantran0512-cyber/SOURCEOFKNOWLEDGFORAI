---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-paywall-modal-masked-article-fade/"
title: "Tailwind Paywall Modal with Masked Article Fade"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A subscribe wall that fades the article tail into nothing with a gradient mask and blurs whatever is left behind a heavy ::backdrop."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Paywall Modal with Masked Article Fade
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-paywall-modal-masked-article-fade/

A subscribe wall that fades the article tail into nothing with a gradient mask and blurs whatever is left behind a heavy ::backdrop. Two arbitrary properties do the work Tailwind has no scale for — [mask-image:…] and the backdrop composition — and everything else is utilities.
## HTML
```html
<section class="tm-04 relative w-full min-h-svh pt-11 px-7 bg-tm04-bg font-tm04-serif text-tm04-ink">
  <article class="max-w-[600px] mx-auto [mask-image:linear-gradient(#000_55%,transparent)]">
    <p class="mb-3.5 font-tm04-sans text-[11px] tracking-[0.22em] text-tm04-acc">MEMBERS &middot; MARKETS</p>
    <h1 class="mb-3.5 text-[clamp(28px,5vw,40px)] leading-[1.15] font-bold text-tm04-hi">The quiet reshaping of global supply chains</h1>
    <p class="mb-6 font-tm04-sans text-[13px] text-tm04-mut">By A. Okafor &middot; 6 min read</p>
    <p class="mb-4.5 text-lg leading-[1.75] text-tm04-body">For three decades the logistics map optimised relentlessly for a single variable: cost. Factories clustered wherever labour was cheapest, and inventory was pared to the hour.</p>
    <p class="mb-4.5 text-lg leading-[1.75] text-tm04-body">Then the shocks arrived in sequence &mdash; a pandemic, a canal, a war &mdash; and the calculus inverted almost overnight. Resilience, not efficiency, became the word every operations chief&hellip;</p>
  </article>

  <div class="absolute inset-x-0 bottom-0 h-[220px] grid place-items-end justify-center pb-10 bg-[linear-gradient(transparent,var(--color-tm04-bg)_62%)]">
    <button type="button" data-tm04-open class="font-tm04-sans inline-flex items-center justify-center min-h-12 px-8 rounded-xl border-0 text-[15px] font-bold cursor-pointer bg-tm04-acc text-tm04-onacc shadow-[0_14px_40px_-12px_var(--color-tm04-acc)] transition-[filter,translate] duration-200 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Subscribe to keep reading</button>
  </div>

  <dialog id="tm-04-dlg" aria-labelledby="tm-04-title" class="m-auto w-[min(420px,94vw)] p-0 border-0 rounded-[20px] font-tm04-sans text-tm04-ink bg-tm04-card shadow-[0_40px_90px_-30px_#000,0_0_0_1px_var(--color-tm04-edge)] opacity-0 translate-y-3.5 scale-[0.97] transition-[opacity,translate,scale,overlay,display] duration-300 transition-discrete open:opacity-100 open:translate-y-0 open:scale-100 open:starting:opacity-0 open:starting:translate-y-3.5 open:starting:scale-[0.97] open:backdrop:bg-tm04-scrim open:backdrop:backdrop-blur-[9px] motion-reduce:transition-none">
    <div class="relative px-8 pt-8 pb-6">
      <button type="button" data-tm04-close aria-label="Close" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tm04-mut text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-tm04-well hover:text-white focus-visible:outline-2 focus-visible:outline-tm04-acc focus-visible:outline-offset-2">&times;</button>
      <p class="mb-2.5 text-[11px] uppercase tracking-[0.2em] text-tm04-acc">Unlimited access</p>
      <h2 id="tm-04-title" class="mb-5 text-2xl font-extrabold tracking-[-0.01em] text-tm04-hi">Keep reading &mdash; join today</h2>
      <ul class="flex flex-col gap-3 mb-5 list-none p-0">
        <li class="relative pl-7 text-[14.5px] text-tm04-body before:content-['✓'] before:absolute before:left-0 before:top-0 before:font-extrabold before:text-tm04-acc">Every members-only report &amp; analysis</li>
        <li class="relative pl-7 text-[14.5px] text-tm04-body before:content-['✓'] before:absolute before:left-0 before:top-0 before:font-extrabold before:text-tm04-acc">Ad-free reading across all devices</li>
        <li class="relative pl-7 text-[14.5px] text-tm04-body before:content-['✓'] before:absolute before:left-0 before:top-0 before:font-extrabold before:text-tm04-acc">Cancel anytime, no questions asked</li>
      </ul>
      <div class="flex items-baseline gap-1.5 mb-4"><b class="text-[34px] text-white">$8</b><span class="text-sm text-tm04-mut">/ month</span></div>
      <button type="button" class="w-full min-h-12 rounded-xl border-0 bg-tm04-acc text-[15px] font-bold text-tm04-onacc cursor-pointer transition-[filter,translate] duration-200 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Subscribe now</button>
      <p class="mt-4 text-center text-[13px] text-tm04-mut">Already a member? <a href="#login" class="font-semibold text-tm04-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-tm04-acc focus-visible:outline-offset-2">Log in</a></p>
      <button type="button" data-tm04-later class="block mx-auto mt-3 min-h-11 px-3 rounded-md border-0 bg-transparent text-[13px] text-tm04-faint cursor-pointer transition-colors duration-200 hover:text-tm04-mut focus-visible:outline-2 focus-visible:outline-tm04-acc focus-visible:outline-offset-2">Maybe later</button>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm04-bg: #0c0d12;
  --color-tm04-bg: oklch(0.16 0.012 285);
  --color-tm04-card: #181a26;
  --color-tm04-card: oklch(0.23 0.02 285);
  --color-tm04-well: #212436;
  --color-tm04-well: oklch(0.27 0.025 285);
  --color-tm04-edge: #262a3a;
  --color-tm04-edge: oklch(0.3 0.02 285);
  --color-tm04-hi: #f3f4fa;
  --color-tm04-hi: oklch(0.97 0.005 285);
  --color-tm04-ink: #e8e9f0;
  --color-tm04-ink: oklch(0.93 0.008 285);
  --color-tm04-body: #c3c6d4;
  --color-tm04-body: oklch(0.83 0.015 285);
  --color-tm04-mut: #9599aa;
  --color-tm04-mut: oklch(0.7 0.02 285);
  --color-tm04-faint: #70748a;
  --color-tm04-faint: oklch(0.56 0.02 285);
  --color-tm04-acc: #b98cff;
  --color-tm04-acc: oklch(0.72 0.19 300);
  --color-tm04-onacc: #120820;
  --color-tm04-onacc: oklch(0.17 0.05 300);
  --color-tm04-scrim: #08090e80;
  --color-tm04-scrim: oklch(0.12 0.01 285 / 0.5);
  --font-tm04-serif: 'Newsreader', Georgia, 'Times New Roman', serif;
  --font-tm04-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tm-04 {
  width: 100%;
}
/* Safari < 18 mask prefix — the utility emits the unprefixed property only. */

.tm-04 article {
  -webkit-mask-image: linear-gradient(#000 55%, transparent);
}

#tm-04-dlg::backdrop {
  background: oklch(0.12 0.01 285 / 0);
  backdrop-filter: blur(0px);
  transition: background .35s, backdrop-filter .35s, overlay .35s allow-discrete, display .35s allow-discrete;
}

@starting-style {
  #tm-04-dlg[open]::backdrop {
    background: oklch(0.12 0.01 285 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-04');
  var dlg = root.querySelector('#tm-04-dlg');
  root.querySelector('[data-tm04-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tm04-close]').addEventListener('click', function () { dlg.close(); });
  root.querySelector('[data-tm04-later]').addEventListener('click', function () { dlg.close(); });
})();
```

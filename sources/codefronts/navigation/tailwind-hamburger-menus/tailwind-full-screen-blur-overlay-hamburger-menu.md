---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-full-screen-blur-overlay-hamburger-menu/"
title: "Tailwind Full Screen Blur Overlay Hamburger Menu"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "The cinematic takeover: the article behind stays visible but slips out of focus while the links arrive through a blur-to-sharp animation with tracking that…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full Screen Blur Overlay Hamburger Menu
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/tailwind-full-screen-blur-overlay-hamburger-menu/

The cinematic takeover: the article behind stays visible but slips out of focus while the links arrive through a blur-to-sharp animation with tracking that tightens as they land. Two blurs doing opposite jobs &mdash; backdrop-blur-* on the sheet, blur-* on the links &mdash; and Tailwind's naming makes the distinction, which trips up half the implementations of this effect, impossible to confuse.
## HTML
```html
<section class="thb-20 w-full min-h-svh grid justify-center content-start bg-thb20-bg font-thb20-sans text-thb20-ink px-5 py-9" aria-label="Fullscreen blur overlay menu demo">
  <div class="group relative w-[min(400px,88vw)] h-140 rounded-3xl overflow-hidden border border-thb20-edge bg-thb20-bg bg-[radial-gradient(130%_90%_at_80%_-10%,oklch(0.34_0.08_300/0.8),transparent_55%),radial-gradient(100%_80%_at_0%_110%,oklch(0.3_0.07_220/0.7),transparent_50%)]">
    <article class="thb20-page grid content-start gap-3.5 px-7 pt-24 pb-7 transition-[scale] duration-500 ease-thb20" aria-hidden="true">
      <span class="text-[11px] font-bold tracking-[0.22em] uppercase text-thb20-acc">Field Notes &middot; 07</span>
      <h2 class="text-[30px] font-bold leading-[1.06] tracking-[-0.02em]">The city at f/1.4</h2>
      <p class="text-[13.5px] leading-relaxed text-thb20-mut text-pretty">Night photography is an argument between what the eye saw and what the sensor kept. The lens holds one plane in confidence and lets the rest dissolve into rumor &mdash;</p>
      <p class="text-[13.5px] leading-relaxed text-thb20-mut text-pretty">streetlights become coins of light, faces become suggestions. Depth of field is an editor: it decides, frame by frame, what the story is about.</p>
      <p class="text-[13.5px] leading-relaxed text-thb20-mut text-pretty">The same is true of interfaces. Focus is a resource you spend.</p>
    </article>
    <nav id="thb20-sheet" aria-label="Site" class="thb20-sheet absolute inset-0 z-2 flex flex-col justify-center gap-1 px-8.5 bg-[oklch(0.15_0.02_280/0.55)] backdrop-blur-[18px] backdrop-saturate-[1.2] opacity-0 invisible [transition:opacity_.45s,visibility_0s_.45s] group-data-open:opacity-100 group-data-open:visible group-data-open:[transition:opacity_.45s,visibility_0s_0s]">
      <a href="#stories" style="--i:0" class="py-3.25 rounded-md text-[34px] font-bold tracking-[0.12em] text-thb20-ink no-underline opacity-0 blur-[14px] [transition:opacity_.4s,filter_.5s,letter-spacing_.6s_var(--ease-thb20),color_.2s] hover:text-thb20-acc focus-visible:text-thb20-acc focus-visible:outline-2 focus-visible:outline-thb20-acc focus-visible:outline-offset-5 group-data-open:opacity-100 group-data-open:blur-none group-data-open:tracking-normal group-data-open:[transition-delay:calc(150ms+var(--i)*70ms)] motion-reduce:blur-none motion-reduce:tracking-normal motion-reduce:[transition:opacity_.15s]">Stories</a>
      <a href="#prints" style="--i:1" class="py-3.25 rounded-md text-[34px] font-bold tracking-[0.12em] text-thb20-ink no-underline opacity-0 blur-[14px] [transition:opacity_.4s,filter_.5s,letter-spacing_.6s_var(--ease-thb20),color_.2s] hover:text-thb20-acc focus-visible:text-thb20-acc focus-visible:outline-2 focus-visible:outline-thb20-acc focus-visible:outline-offset-5 group-data-open:opacity-100 group-data-open:blur-none group-data-open:tracking-normal group-data-open:[transition-delay:calc(150ms+var(--i)*70ms)] motion-reduce:blur-none motion-reduce:tracking-normal motion-reduce:[transition:opacity_.15s]">Prints</a>
      <a href="#workshops" style="--i:2" class="py-3.25 rounded-md text-[34px] font-bold tracking-[0.12em] text-thb20-ink no-underline opacity-0 blur-[14px] [transition:opacity_.4s,filter_.5s,letter-spacing_.6s_var(--ease-thb20),color_.2s] hover:text-thb20-acc focus-visible:text-thb20-acc focus-visible:outline-2 focus-visible:outline-thb20-acc focus-visible:outline-offset-5 group-data-open:opacity-100 group-data-open:blur-none group-data-open:tracking-normal group-data-open:[transition-delay:calc(150ms+var(--i)*70ms)] motion-reduce:blur-none motion-reduce:tracking-normal motion-reduce:[transition:opacity_.15s]">Workshops</a>
      <a href="#about" style="--i:3" class="py-3.25 rounded-md text-[34px] font-bold tracking-[0.12em] text-thb20-ink no-underline opacity-0 blur-[14px] [transition:opacity_.4s,filter_.5s,letter-spacing_.6s_var(--ease-thb20),color_.2s] hover:text-thb20-acc focus-visible:text-thb20-acc focus-visible:outline-2 focus-visible:outline-thb20-acc focus-visible:outline-offset-5 group-data-open:opacity-100 group-data-open:blur-none group-data-open:tracking-normal group-data-open:[transition-delay:calc(150ms+var(--i)*70ms)] motion-reduce:blur-none motion-reduce:tracking-normal motion-reduce:[transition:opacity_.15s]">About</a>
      <span style="--i:4" class="mt-6.5 font-thb20-mono text-xs tracking-[0.06em] text-thb20-mut opacity-0 blur-[10px] [transition:opacity_.4s,filter_.5s] group-data-open:opacity-100 group-data-open:blur-none group-data-open:[transition-delay:calc(150ms+var(--i)*70ms)] motion-reduce:blur-none" aria-hidden="true">&fnof;/1.4 &middot; everything else can wait</span>
    </nav>
    <header class="absolute inset-x-0 top-0 z-3 flex items-center justify-between h-19 pl-6.5 pr-5">
      <span class="text-[13px] font-extrabold tracking-[0.3em]">APERTURE&amp;CO</span>
      <button type="button" aria-expanded="false" aria-controls="thb20-sheet" aria-label="Open menu" class="thb20-btn grid place-items-center w-11.5 h-11.5 rounded-full border border-[oklch(1_0_0/0.22)] bg-[oklch(1_0_0/0.06)] backdrop-blur-[10px] text-thb20-ink cursor-pointer transition-[background,scale] duration-250 hover:bg-[oklch(1_0_0/0.14)] hover:scale-105 active:scale-94 focus-visible:outline-2 focus-visible:outline-thb20-acc focus-visible:outline-offset-3">
        <span class="relative block w-4.5 h-3" aria-hidden="true">
          <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:translate-y-[5px] group-data-open:rotate-45 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-current transition-[opacity] duration-200 group-data-open:opacity-0 motion-reduce:transition-none"></i>
          <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-current transition-[translate,rotate] duration-300 group-data-open:-translate-y-[5px] group-data-open:-rotate-45 motion-reduce:transition-none"></i>
        </span>
      </button>
    </header>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb20-bg: #2b2740;
  --color-thb20-bg: oklch(0.2 0.025 280);
  --color-thb20-edge: #4c4666;
  --color-thb20-edge: oklch(0.32 0.03 280);
  --color-thb20-ink: #eae7f2;
  --color-thb20-ink: oklch(0.93 0.01 280);
  --color-thb20-mut: #a9a3ba;
  --color-thb20-mut: oklch(0.68 0.02 280);
  --color-thb20-acc: #e0a94e;
  --color-thb20-acc: oklch(0.8 0.13 60);
  --font-thb20-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb20-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb20: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Same rule as demo 07: without a real fallback, an engine with no backdrop-filter
   paints a 55%-alpha sheet and the article reads straight through the links. */

@supports not (backdrop-filter: blur(1px)) {
  .thb-20 .thb20-sheet {
    background: oklch(0.17 0.025 280 / 0.93);
  }

  .thb-20 .thb20-btn {
    background: oklch(0.3 0.05 280 / 0.85);
  }

  .thb-20 .group[data-open] .thb20-page {
    scale: 0.96;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-20 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.thb-20 > .group').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('button[aria-controls="thb20-sheet"]');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
  });
})();
```

---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-video-trailer-modal-aspect-locked-iframe/"
title: "Tailwind Video Trailer Modal with Aspect-Locked Iframe"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A click-to-play trailer overlay: a 16:9 box locked by aspect-video before anything loads, and an iframe whose src is set on open and cleared on close so…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Video Trailer Modal with Aspect-Locked Iframe
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-video-trailer-modal-aspect-locked-iframe/

A click-to-play trailer overlay: a 16:9 box locked by aspect-video before anything loads, and an iframe whose src is set on open and cleared on close so audio stops the instant the dialog does. Zero layout shift, zero orphaned audio.
## HTML
```html
<section class="tm-10 w-full min-h-svh grid place-items-center bg-tm10-bg font-tm10-sans px-6 py-10">
  <button type="button" data-tm10-open class="inline-flex items-center gap-2.5 min-h-11 px-6 rounded-xl text-[15px] font-semibold text-tm10-ink bg-tm10-btn border border-tm10-btnedge cursor-pointer transition-colors duration-200 hover:bg-tm10-btnhover hover:border-tm10-acc focus-visible:outline-2 focus-visible:outline-tm10-acc focus-visible:outline-offset-2"><span aria-hidden="true">▶</span> Watch trailer</button>

  <dialog id="tm-10-dlg" aria-labelledby="tm-10-title" class="m-auto w-[min(780px,94vw)] p-0 border-0 rounded-2xl overflow-hidden text-tm10-ink bg-tm10-card shadow-[0_40px_90px_-30px_#000,0_0_0_1px_var(--color-tm10-edge)] opacity-0 scale-[0.96] transition-[opacity,translate,scale,overlay,display] duration-[280ms] transition-discrete open:opacity-100 open:scale-100 open:starting:opacity-0 open:starting:scale-[0.96] open:backdrop:bg-tm10-scrim open:backdrop:backdrop-blur-[6px] motion-reduce:transition-none">
    <div data-tm10-card>
      <div class="flex items-center justify-between gap-3 px-4 py-3 bg-tm10-bar">
        <h2 id="tm-10-title" class="text-[15px] font-semibold text-tm10-hi">Official Trailer &mdash; &ldquo;Nightfall&rdquo;</h2>
        <button type="button" data-tm10-close aria-label="Close player" class="grid place-items-center size-11 rounded-lg border-0 bg-transparent text-tm10-mut text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-tm10-btnhover hover:text-white focus-visible:outline-2 focus-visible:outline-tm10-acc focus-visible:outline-offset-2">&times;</button>
      </div>
      <div class="relative aspect-video bg-black">
        <!-- Ship this: the src is set from data-src on open and cleared on close.
        <iframe data-tm10-video title="Official Trailer — Nightfall"
          data-src="https://www.youtube-nocookie.com/embed/VIDEO_ID?rel=0"
          class="absolute inset-0 size-full border-0"
          allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe> -->
        <div aria-hidden="true" class="absolute inset-0 flex flex-col items-center justify-center gap-4 bg-[radial-gradient(120%_120%_at_50%_40%,var(--color-tm10-posterA),var(--color-tm10-posterB))]">
          <div class="grid place-items-center size-19 pl-1.5 rounded-full text-[26px] bg-tm10-play text-tm10-onacc shadow-[0_0_50px_-6px_var(--color-tm10-acc)] animate-tm10-pulse motion-reduce:animate-none">▶</div>
          <span class="font-tm10-mono text-xs tracking-[0.14em] text-tm10-mut">16:9 player &middot; your &lt;iframe&gt; here</span>
        </div>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm10-bg: #080607;
  --color-tm10-bg: oklch(0.14 0.012 15);
  --color-tm10-card: #0c0809;
  --color-tm10-card: oklch(0.16 0.012 15);
  --color-tm10-bar: #170f11;
  --color-tm10-bar: oklch(0.2 0.018 15);
  --color-tm10-btn: #1e1215;
  --color-tm10-btn: oklch(0.23 0.04 15);
  --color-tm10-btnhover: #2a181c;
  --color-tm10-btnhover: oklch(0.28 0.05 15);
  --color-tm10-btnedge: #4a2630;
  --color-tm10-btnedge: oklch(0.36 0.09 15);
  --color-tm10-edge: #2a1e22;
  --color-tm10-edge: oklch(0.27 0.02 15);
  --color-tm10-posterA: #2c161c;
  --color-tm10-posterA: oklch(0.27 0.06 15);
  --color-tm10-posterB: #0a0608;
  --color-tm10-posterB: oklch(0.15 0.015 15);
  --color-tm10-hi: #f7edef;
  --color-tm10-hi: oklch(0.95 0.01 15);
  --color-tm10-ink: #e9dade;
  --color-tm10-ink: oklch(0.9 0.015 15);
  --color-tm10-mut: #b3959b;
  --color-tm10-mut: oklch(0.72 0.03 15);
  --color-tm10-acc: #f2557a;
  --color-tm10-acc: oklch(0.68 0.2 15);
  --color-tm10-play: #f8768f;
  --color-tm10-play: oklch(0.74 0.17 15);
  --color-tm10-onacc: #1a0a0d;
  --color-tm10-onacc: oklch(0.2 0.04 15);
  --color-tm10-scrim: #040303b8;
  --color-tm10-scrim: oklch(0.11 0.008 15 / 0.72);
  --font-tm10-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tm10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tm10-pulse: tm10-pulse 2.4s ease-in-out infinite;
}

.tm-10 {
  width: 100%;
}

@keyframes tm10-pulse {
  0%,
    100% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.06);
  }
}

#tm-10-dlg::backdrop {
  background: oklch(0.11 0.008 15 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-10-dlg[open]::backdrop {
    background: oklch(0.11 0.008 15 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-10');
  var dlg = root.querySelector('#tm-10-dlg');
  var card = root.querySelector('[data-tm10-card]');
  var video = root.querySelector('[data-tm10-video]'); // present in production markup
  root.querySelector('[data-tm10-open]').addEventListener('click', function () {
    if (video && video.dataset.src) video.src = video.dataset.src;  // start
    dlg.showModal();
  });
  root.querySelector('[data-tm10-close]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('close', function () { if (video) video.src = ''; }); // stop playback
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```

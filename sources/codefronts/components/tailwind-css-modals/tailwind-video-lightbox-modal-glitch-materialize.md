---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-video-lightbox-modal-glitch-materialize/"
title: "Tailwind Video Lightbox Modal with Chromatic Glitch Materialize"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A cinema-dark video overlay that materialises through a stuttered RGB split — red and cyan bands offset for four stepped frames, then gone."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Video Lightbox Modal with Chromatic Glitch Materialize
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-video-lightbox-modal-glitch-materialize/

A cinema-dark video overlay that materialises through a stuttered RGB split — red and cyan bands offset for four stepped frames, then gone. The port keeps the two pseudo-element clones as before:/after: utilities and registers the stutter as an --animate-* theme entry, because steps() timing is the whole effect.
## HTML
```html
<section class="tw-08 w-full min-h-svh grid place-items-center bg-tw08-bg font-tw08-sans px-6 py-10">
  <button type="button" data-tw08-open class="inline-flex items-center justify-center min-h-11 px-7 rounded-lg border border-tw08-ink bg-transparent font-tw08-mono text-[15px] font-semibold tracking-wide text-tw08-ink cursor-pointer transition-colors duration-200 hover:bg-tw08-ink hover:text-tw08-bg focus-visible:outline-2 focus-visible:outline-tw08-cyan focus-visible:outline-offset-2">&#9654; Watch demo · 2:14</button>

  <dialog id="tw-08-dlg" aria-labelledby="tw-08-title" class="group w-full max-w-none h-full max-h-none m-0 p-8 border-0 bg-transparent open:grid open:place-items-center open:backdrop:bg-tw08-scrim open:backdrop:backdrop-blur-[8px]">
    <button type="button" data-tw08-close aria-label="Close video" class="fixed top-5 right-6 grid place-items-center size-11 rounded-full border border-tw08-edge bg-tw08-glass text-lg text-tw08-ink cursor-pointer transition-[background-color,rotate] duration-200 hover:bg-tw08-glass2 hover:rotate-90 focus-visible:outline-2 focus-visible:outline-tw08-cyan focus-visible:outline-offset-2 motion-reduce:hover:rotate-0">&#10005;</button>

    <div class="w-[min(820px,100%,calc((100svh-170px)*16/9))] opacity-0 group-open:opacity-100 group-open:animate-tw08-stutter motion-reduce:animate-none motion-reduce:opacity-100">
      <h2 id="tw-08-title" class="mb-3.5 font-tw08-mono text-xs font-bold uppercase tracking-[0.14em] text-tw08-sub">Product demo · 2:14</h2>

      <div data-tw08-frame class="group/frame relative aspect-video grid place-items-center rounded-md overflow-hidden border border-tw08-edge bg-tw08-frame shadow-[0_0_0_1px_var(--color-tw08-edge),0_30px_80px_-20px_#000] before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:mix-blend-screen before:bg-tw08-redwash before:[clip-path:polygon(0_15%,100%_15%,100%_35%,0_35%)] before:opacity-0 after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:mix-blend-screen after:bg-tw08-cyanwash after:[clip-path:polygon(0_60%,100%_60%,100%_80%,0_80%)] after:opacity-0 group-open:before:animate-tw08-glitch group-open:after:animate-tw08-glitch motion-reduce:before:animate-none motion-reduce:after:animate-none">
        <span aria-hidden="true" data-tw08-screen class="absolute inset-0 z-0 opacity-0 transition-opacity duration-300 group-data-[playing=true]/frame:opacity-100 group-data-[playing=true]/frame:animate-tw08-scan motion-reduce:animate-none"></span>
        <button type="button" data-tw08-play aria-label="Play video" class="relative z-10 grid place-items-center size-20 pl-1.5 transition-opacity duration-300 group-data-[playing=true]/frame:opacity-0 group-data-[playing=true]/frame:pointer-events-none rounded-full border border-tw08-edge bg-tw08-glass text-[28px] text-tw08-ink cursor-pointer shadow-[0_0_40px_var(--color-tw08-glow)] transition-[background-color,scale] duration-200 hover:bg-tw08-glass2 hover:scale-105 focus-visible:outline-2 focus-visible:outline-tw08-cyan focus-visible:outline-offset-2 motion-reduce:hover:scale-100">&#9654;</button>

        <span data-tw08-chrome class="absolute top-0 inset-x-0 z-10 transition-opacity duration-300 group-data-[playing=true]/frame:opacity-0 flex justify-between items-center px-3.5 py-2.5 font-tw08-mono text-[11px] tracking-wide text-tw08-sub bg-linear-to-b from-tw08-veil to-transparent">
          <span>northlight-demo.mp4</span><span>1080p · 16:9</span>
        </span>
        <span class="absolute bottom-0 inset-x-0 z-30 flex items-center gap-3 px-3.5 py-3 bg-linear-to-t from-tw08-veil to-transparent">
          <button type="button" data-tw08-toggle aria-label="Play video" class="grid place-items-center size-11 shrink-0 rounded-full border border-tw08-edge bg-tw08-glass text-sm text-tw08-ink cursor-pointer transition-colors duration-200 hover:bg-tw08-glass2 focus-visible:outline-2 focus-visible:outline-tw08-cyan focus-visible:outline-offset-2">&#9654;</button>
          <span class="flex-1 h-1 rounded-full bg-tw08-glass2 overflow-hidden"><span data-tw08-bar class="block w-0 h-full rounded-full bg-tw08-cyan transition-[width] duration-200 ease-linear"></span></span>
          <span data-tw08-time class="font-tw08-mono text-[11px] tabular-nums text-tw08-sub">0:00 / 2:14</span>
        </span>
      </div>

      <p class="flex flex-wrap justify-between items-center gap-3.5 mt-3.5 text-sm text-tw08-sub">
        <span>How Northlight ships design updates in hours</span>
        <a href="#" class="font-semibold text-tw08-cyan no-underline hover:underline">Transcript</a>
      </p>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw08-bg: #0a0a0f;
  --color-tw08-bg: oklch(0.14 0.01 285);
  --color-tw08-frame: #14142a;
  --color-tw08-frame: oklch(0.21 0.04 285);
  --color-tw08-ink: #e2e8f0;
  --color-tw08-ink: oklch(0.92 0.01 255);
  --color-tw08-sub: #a3aec2;
  --color-tw08-sub: oklch(0.75 0.02 255);
  --color-tw08-edge: #e2e8f03d;
  --color-tw08-edge: oklch(0.92 0.01 255 / 0.24);
  --color-tw08-glass: #ffffff0f;
  --color-tw08-glass: oklch(1 0 0 / 0.06);
  --color-tw08-glass2: #ffffff24;
  --color-tw08-glass2: oklch(1 0 0 / 0.14);
  --color-tw08-glow: #e2e8f029;
  --color-tw08-glow: oklch(0.92 0.01 255 / 0.16);
  --color-tw08-red: #ff3d40;
  --color-tw08-red: oklch(0.65 0.23 22);
  --color-tw08-cyan: #00fff9;
  --color-tw08-cyan: oklch(0.89 0.15 195);
  --color-tw08-redwash: #ff3d4059;
  --color-tw08-redwash: oklch(0.65 0.23 22 / 0.35);
  --color-tw08-cyanwash: #00fff959;
  --color-tw08-cyanwash: oklch(0.89 0.15 195 / 0.35);
  --color-tw08-veil: #000000a6;
  --color-tw08-veil: oklch(0 0 0 / 0.65);
  --color-tw08-scrim: #000000eb;
  --color-tw08-scrim: oklch(0 0 0 / 0.92);
  --font-tw08-sans: 'Outfit', system-ui, sans-serif;
  --font-tw08-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tw08-stutter: tw08-stutter .4s steps(4) both;
  --animate-tw08-glitch: tw08-glitch .5s steps(2) forwards;
  --animate-tw08-scan: tw08-scan 2.4s linear infinite;
}

.tw-08 {
  width: 100%;
}
/* A self-contained stand-in for the media: moving scanlines over the frame, so the
   demo plays with no network. Swap [data-tw08-screen] for your <iframe>/<video>.
   Only the texture lives here — the playing STATE is utilities on the elements,
   because an unlayered rule loses the cascade to @layer utilities. */

[data-tw08-screen] {
  background: repeating-linear-gradient(0deg, oklch(1 0 0 / 0.05) 0 2px, transparent 2px 4px), radial-gradient(120% 90% at 30% 20%, oklch(0.55 0.18 265 / 0.55), transparent 60%), radial-gradient(100% 80% at 80% 80%, oklch(0.62 0.2 320 / 0.45), transparent 60%);
}

@keyframes tw08-scan {
  to {
    background-position: 0 24px, 6% 0, -6% 0;
  }
}

@keyframes tw08-stutter {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}
/* The chromatic split: stepped offsets, settling to nothing. */

@keyframes tw08-glitch {
  0% {
    opacity: .9;
    translate: -4px 0;
  }

  25% {
    opacity: .7;
    translate: 4px 0;
  }

  50% {
    opacity: .5;
    translate: -2px 0;
  }

  75% {
    opacity: .3;
    translate: 2px 0;
  }

  100% {
    opacity: 0;
    translate: 0 0;
  }
}

#tw-08-dlg::backdrop {
  background: oklch(0 0 0 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s ease, backdrop-filter .3s ease, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tw-08-dlg[open]::backdrop {
    background: oklch(0 0 0 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-08-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-08');
  var dlg = root.querySelector('#tw-08-dlg');
  root.querySelector('[data-tw08-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tw08-close]').addEventListener('click', function () { dlg.close(); });
  // The frame plays a self-contained stand-in so the demo works with no network.
  // For a real deployment, mount your player here instead — click-to-load, so the
  // page never pays for an iframe the viewer did not ask for:
  //   var el = document.createElement('iframe');
  //   el.src = 'https://www.youtube-nocookie.com/embed/ID?autoplay=1&rel=0';
  //   el.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
  //   el.className = 'absolute inset-0 w-full h-full border-0 z-20';
  //   frame.appendChild(el);
  var frame = root.querySelector('[data-tw08-frame]');
  var bar = root.querySelector('[data-tw08-bar]');
  var time = root.querySelector('[data-tw08-time]');
  var toggle = root.querySelector('[data-tw08-toggle]');
  var DURATION = 134; // 2:14
  var at = 0, tick = null;

  function clock(s) { var m = Math.floor(s / 60), r = Math.floor(s % 60); return m + ':' + (r < 10 ? '0' : '') + r; }
  function paint() {
    bar.style.width = (at / DURATION * 100) + '%';
    time.textContent = clock(at) + ' / ' + clock(DURATION);
  }
  function play() {
    if (tick) return;
    frame.setAttribute('data-playing', 'true');
    toggle.innerHTML = '&#10073;&#10073;';
    toggle.setAttribute('aria-label', 'Pause video');
    tick = setInterval(function () {
      at += 0.2;
      if (at >= DURATION) { at = DURATION; paint(); pause(); return; }
      paint();
    }, 200);
  }
  function pause() {
    clearInterval(tick); tick = null;
    toggle.innerHTML = '&#9654;';
    toggle.setAttribute('aria-label', 'Play video');
  }
  function reset() { pause(); at = 0; paint(); frame.removeAttribute('data-playing'); }

  root.querySelector('[data-tw08-play]').addEventListener('click', play);
  toggle.addEventListener('click', function () { tick ? pause() : play(); });
  // Closing must stop playback — a dialog that keeps a player running is the
  // classic "where is that audio coming from?" bug.
  dlg.addEventListener('close', reset);
  paint();
  // Full-bleed dialog: the edge controls are fixed and sit outside the stage's rect,
  // so light-dismiss tests the event target instead of coordinates.
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
})();
```

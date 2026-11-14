---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-infinite-text-marquee-that-speeds-up-on-hover/"
title: "Tailwind Infinite Text Marquee that Speeds Up on Hover"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "Streetwear ticker tapes in counter-flow: two tilted strips loop with animate-tth26-roll and its reverse twin."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Infinite Text Marquee that Speeds Up on Hover
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-infinite-text-marquee-that-speeds-up-on-hover/

Streetwear ticker tapes in counter-flow: two tilted strips loop with animate-tth26-roll and its reverse twin. Hovering a strip surges it to 4× with updatePlaybackRate(4) — no phase jump, which a CSS duration swap can't do. A real aria-pressed pause button styles itself with aria-pressed: and starts pressed for reduced-motion users.
## HTML
```html
<section class="tth-26 @container w-full min-h-svh grid place-items-center overflow-clip bg-tth26-bg py-14 font-tth26-sans text-tth26-ink" aria-label="Marquee speed up on hover demo">
  <div class="flex w-full flex-col gap-[clamp(22px,4cqi,36px)]">
    <header class="flex items-center justify-between gap-4 px-[clamp(20px,5cqi,64px)]">
      <h2 class="text-[clamp(30px,6cqi,54px)] font-black tracking-[-0.04em] [font-stretch:110%]">ARCHIVE&nbsp;/&nbsp;004</h2>
      <button type="button" data-tth26-pause aria-pressed="false" class="group/pause inline-flex min-h-[46px] cursor-pointer items-center gap-2.5 rounded-full border-2 border-tth26-ink bg-tth26-paper px-5 text-[13px] font-extrabold uppercase tracking-[0.06em] transition-colors duration-250 hover:bg-tth26-ink hover:text-tth26-paper aria-pressed:border-tth26-acc aria-pressed:bg-tth26-acc aria-pressed:text-tth26-paper focus-visible:outline-3 focus-visible:outline-offset-[3px] focus-visible:outline-tth26-acc"><span aria-hidden="true" class="flex gap-[3px] group-aria-pressed/pause:hidden"><i class="h-3 w-[3px] bg-current"></i><i class="h-3 w-[3px] bg-current"></i></span><span aria-hidden="true" class="hidden size-0 border-y-[6px] border-l-[9px] border-y-transparent border-l-current group-aria-pressed/pause:block"></span><span data-tth26-label>Pause tickers</span></button>
    </header>
    <div id="tth26-top" class="-rotate-[1.6deg] scale-x-[1.02] cursor-pointer overflow-clip bg-tth26-ink py-3.5 text-tth26-paper">
      <div data-tth26-track class="flex w-max animate-tth26-roll">
        <p class="whitespace-nowrap pr-[0.5em] text-[clamp(17px,3cqi,26px)] font-extrabold tracking-[0.04em]">NEW DROP 004 &#9670; FREE SHIPPING OVER $120 &#9670; STORE OPENS FRI 10:00 &#9670; NO RESTOCKS &#9670;&nbsp;</p>
        <p aria-hidden="true" class="whitespace-nowrap pr-[0.5em] text-[clamp(17px,3cqi,26px)] font-extrabold tracking-[0.04em]">NEW DROP 004 &#9670; FREE SHIPPING OVER $120 &#9670; STORE OPENS FRI 10:00 &#9670; NO RESTOCKS &#9670;&nbsp;</p>
      </div>
    </div>
    <div class="-mt-1 rotate-[1.2deg] scale-x-[1.02] cursor-pointer overflow-clip bg-tth26-acc py-3.5 text-tth26-paper">
      <div data-tth26-track class="flex w-max animate-tth26-roll-rev">
        <p class="whitespace-nowrap pr-[0.5em] text-[clamp(17px,3cqi,26px)] font-extrabold tracking-[0.04em]">WORLDWIDE &#9671; 100% RECYCLED FLEECE &#9671; SIZE RUNS BIG &#9671; MEMBERS EARLY ACCESS THU &#9671;&nbsp;</p>
        <p aria-hidden="true" class="whitespace-nowrap pr-[0.5em] text-[clamp(17px,3cqi,26px)] font-extrabold tracking-[0.04em]">WORLDWIDE &#9671; 100% RECYCLED FLEECE &#9671; SIZE RUNS BIG &#9671; MEMBERS EARLY ACCESS THU &#9671;&nbsp;</p>
      </div>
    </div>
    <p class="max-w-[64ch] px-[clamp(20px,5cqi,64px)] text-[12.5px] leading-[1.7] text-tth26-mut">Hover a strip: <code class="rounded bg-tth26-chip px-1.5 py-px font-tth26-mono text-[0.9em]">anim.updatePlaybackRate(4)</code> surges it with zero phase jump &mdash; the thing a CSS duration swap can't do. Counter-flow directions are the streetwear tell.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth26-bg: #f5f4f0;
  --color-tth26-bg: oklch(0.96 0.005 90);
  --color-tth26-chip: #e3e2dd;
  --color-tth26-chip: oklch(0.9 0.008 90);
  --color-tth26-ink: #121210;
  --color-tth26-ink: oklch(0.17 0.005 90);
  --color-tth26-paper: #fdfdfb;
  --color-tth26-paper: oklch(0.99 0.002 90);
  --color-tth26-mut: #5f5e59;
  --color-tth26-mut: oklch(0.46 0.01 90);
  --color-tth26-acc: #d63a1f;
  --color-tth26-acc: oklch(0.58 0.21 30);
  --font-tth26-sans: 'Archivo', system-ui, sans-serif;
  --font-tth26-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tth26-roll: tth26-roll 16s linear infinite;
  --animate-tth26-roll-rev: tth26-roll 22s linear infinite reverse;

  @keyframes tth26-roll {
    to {
      transform: translateX(-50%);
    }
  }
}

.tth-26 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var tracks = [].slice.call(document.querySelectorAll('[data-tth26-track]'));
  var anims = tracks.map(function (t) {
    return (t.getAnimations ? t.getAnimations() : []).filter(function (x) { return x.animationName === 'tth26-roll'; })[0];
  });
  tracks.forEach(function (t, i) {
    var a = anims[i]; if (!a) return;
    t.parentElement.addEventListener('pointerenter', function () { a.updatePlaybackRate(4); });
    t.parentElement.addEventListener('pointerleave', function () { a.updatePlaybackRate(1); });
  });
  var btn = document.querySelector('[data-tth26-pause]'), label = btn && btn.querySelector('[data-tth26-label]');
  function set(pause) {
    btn.setAttribute('aria-pressed', String(pause));
    label.textContent = pause ? 'Play tickers' : 'Pause tickers';
    anims.forEach(function (a) { if (a) pause ? a.pause() : a.play(); });
  }
  if (btn) { set(reduced); btn.addEventListener('click', function () { set(btn.getAttribute('aria-pressed') !== 'true'); }); }
})();
```

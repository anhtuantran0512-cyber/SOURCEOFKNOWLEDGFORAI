---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-amber-and-green-phosphor-monitor/"
title: "Tailwind Amber and Green Phosphor Monitor"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "Two monochrome tubes side by side with the phosphor named on each: P1 green and P3 amber."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Amber and Green Phosphor Monitor
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-amber-and-green-phosphor-monitor/

Two monochrome tubes side by side with the phosphor named on each: P1 green and P3 amber. Persistence is a real trailing fade on newly written lines rather than a static glow, and the port changes how the script talks to the CSS &mdash; it sets a data- attribute and a data-* variant does the styling, which is the pattern to reach for whenever JS and utilities meet.
## HTML
```html
<section class="twr-08 relative block w-full min-h-svh box-border bg-twr08-bg text-twr08-ink font-twr08-mono" aria-labelledby="twr-08-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-08-title">Monochrome phosphor monitors, P1 green and P3 amber</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-08-theme">
    <label class="grid place-items-center size-11 rounded-full border border-twr08-line bg-twr08-surface text-twr08-ink2 cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-twr08-acc peer-focus-visible:outline-offset-2" for="twr-08-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle light surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-6 max-w-[74rem] mx-auto px-[clamp(0.85rem,0.5rem+2vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <header class="grid gap-1.5 min-w-0">
      <p class="m-0 text-[0.68rem] tracking-[0.14em] uppercase text-twr08-ink2">Monochrome CRT &middot; phosphor persistence and bloom</p>
      <h3 class="m-0 min-w-0 text-balance text-[clamp(1.3rem,1rem+1.9vw,2.05rem)] font-semibold leading-tight tracking-[-0.02em]">Two phosphors, one code path</h3>
    </header>

    <div class="grid grid-cols-[minmax(0,1fr)] gap-4.5 md:grid-cols-2">
      <article class="min-w-0 grid gap-2.5 rounded-[10px] bg-[#3c3f3a] p-[clamp(0.6rem,0.4rem+1vw,1rem)] [--twr-08-p:#33ff66] [--twr-08-p-dim:#1c7a3a] [--twr-08-decay:1400ms] [box-shadow:inset_0_2px_0_rgba(255,255,255,0.22),inset_0_-3px_0_rgba(0,0,0,0.45),0_16px_34px_-18px_rgba(0,0,0,0.7)]" aria-labelledby="twr-08-l1">
        <div class="relative isolate overflow-hidden rounded-[14px] min-h-[clamp(200px,34vw,300px)] p-[clamp(0.7rem,0.5rem+1vw,1.1rem)] [background:radial-gradient(120%_100%_at_50%_40%,#0b0d0b_0%,#050605_78%)] [box-shadow:inset_0_0_0_2px_#000,inset_0_0_26px_8px_rgba(0,0,0,0.8)]">
          <div class="twr-08__feed min-w-0 grid content-start gap-[0.18em] text-[clamp(0.62rem,0.5rem+0.7vw,0.85rem)] leading-relaxed text-[var(--twr-08-p-dim)]" data-twr-08-feed="p1" role="log" aria-live="off" aria-relevant="additions"></div>
          <div class="absolute inset-x-0 h-[22%] z-3 pointer-events-none animate-twr08-retrace motion-reduce:animate-none motion-reduce:opacity-0 [background:linear-gradient(to_bottom,rgba(255,255,255,0)_0%,rgba(255,255,255,0.045)_50%,rgba(255,255,255,0)_100%)]" aria-hidden="true"></div>
        </div>
        <div class="grid gap-1.5 min-w-0">
          <h4 class="m-0 min-w-0 text-[0.78rem] tracking-[0.06em] text-[#e8e6dd]" id="twr-08-l1">P1 &middot; zinc silicate green</h4>
          <dl class="m-0 flex flex-wrap gap-x-5 gap-y-1 text-[0.7rem] text-[#c3c0b5]">
            <div class="flex gap-1.5 min-w-0"><dt class="m-0 text-[#9c998f]">Decay</dt><dd class="m-0">long &mdash; 1.4 s visible</dd></div>
            <div class="flex gap-1.5 min-w-0"><dt class="m-0 text-[#9c998f]">Peak</dt><dd class="m-0">525 nm</dd></div>
          </dl>
        </div>
      </article>

      <article class="min-w-0 grid gap-2.5 rounded-[10px] bg-[#423d34] p-[clamp(0.6rem,0.4rem+1vw,1rem)] [--twr-08-p:#ffb000] [--twr-08-p-dim:#8a5f00] [--twr-08-decay:600ms] [box-shadow:inset_0_2px_0_rgba(255,255,255,0.22),inset_0_-3px_0_rgba(0,0,0,0.45),0_16px_34px_-18px_rgba(0,0,0,0.7)]" aria-labelledby="twr-08-l2">
        <div class="relative isolate overflow-hidden rounded-[14px] min-h-[clamp(200px,34vw,300px)] p-[clamp(0.7rem,0.5rem+1vw,1.1rem)] [background:radial-gradient(120%_100%_at_50%_40%,#0b0d0b_0%,#050605_78%)] [box-shadow:inset_0_0_0_2px_#000,inset_0_0_26px_8px_rgba(0,0,0,0.8)]">
          <div class="twr-08__feed min-w-0 grid content-start gap-[0.18em] text-[clamp(0.62rem,0.5rem+0.7vw,0.85rem)] leading-relaxed text-[var(--twr-08-p-dim)]" data-twr-08-feed="p3" role="log" aria-live="off" aria-relevant="additions"></div>
          <div class="absolute inset-x-0 h-[22%] z-3 pointer-events-none animate-twr08-retrace motion-reduce:animate-none motion-reduce:opacity-0 [background:linear-gradient(to_bottom,rgba(255,255,255,0)_0%,rgba(255,255,255,0.045)_50%,rgba(255,255,255,0)_100%)]" aria-hidden="true"></div>
        </div>
        <div class="grid gap-1.5 min-w-0">
          <h4 class="m-0 min-w-0 text-[0.78rem] tracking-[0.06em] text-[#e8e6dd]" id="twr-08-l2">P3 &middot; zinc beryllium amber</h4>
          <dl class="m-0 flex flex-wrap gap-x-5 gap-y-1 text-[0.7rem] text-[#c3c0b5]">
            <div class="flex gap-1.5 min-w-0"><dt class="m-0 text-[#9c998f]">Decay</dt><dd class="m-0">medium &mdash; 0.6 s visible</dd></div>
            <div class="flex gap-1.5 min-w-0"><dt class="m-0 text-[#9c998f]">Peak</dt><dd class="m-0">602 nm</dd></div>
          </dl>
        </div>
      </article>
    </div>

    <template data-twr-08-line>
      <p class="m-0 min-w-0 whitespace-pre-wrap [overflow-wrap:anywhere] text-[var(--twr-08-p-dim)] transition-[color,text-shadow] duration-[var(--twr-08-decay)] ease-out motion-reduce:transition-none data-fresh:text-[var(--twr-08-p)] data-fresh:[text-shadow:0_0_3px_var(--twr-08-p),0_0_9px_var(--twr-08-p)]"><span class="inline-block w-[3ch]" data-mark></span><span data-text></span></p>
    </template>

    <aside class="min-w-0 grid gap-2.5 border border-twr08-line bg-twr08-surface p-[clamp(0.85rem,0.6rem+1vw,1.2rem)]">
      <h4 class="m-0 text-[0.72rem] tracking-[0.1em] uppercase text-twr08-ink2">State without colour</h4>
      <p class="m-0 min-w-0 max-w-[68ch] text-[0.85rem] leading-relaxed text-pretty text-twr08-ink2">One hue means no colour coding. Every line below marks its state with a bracket glyph in a fixed column and a written word, so the distinction survives on a display that has exactly one colour to give.</p>
      <ul class="list-none m-0 p-0 flex flex-wrap gap-x-5 gap-y-1.5 text-[0.8rem]">
        <li class="flex items-center gap-2 min-w-0"><span class="text-twr08-acc">[ ]</span> routine</li>
        <li class="flex items-center gap-2 min-w-0"><span class="text-twr08-acc">[!]</span> warning</li>
        <li class="flex items-center gap-2 min-w-0"><span class="text-twr08-acc">[x]</span> fault</li>
        <li class="flex items-center gap-2 min-w-0"><span class="text-twr08-acc">[&gt;]</span> awaiting input</li>
      </ul>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr08-bg: #1a1c1e;
  --color-twr08-bg: oklch(0.23 0.004 220);
  --color-twr08-surface: #262a2d;
  --color-twr08-surface: oklch(0.30 0.006 220);
  --color-twr08-ink: #eef1f2;
  --color-twr08-ink: oklch(0.96 0.003 220);
  --color-twr08-ink2: #aab2b6;
  --color-twr08-ink2: oklch(0.76 0.008 220);
  --color-twr08-line: #3e4548;
  --color-twr08-line: oklch(0.37 0.008 220);
  --color-twr08-acc: #86d7c4;
  --color-twr08-acc: oklch(0.84 0.09 172);
  --font-twr08-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --animate-twr08-retrace: twr-08-retrace 7s linear infinite;
}

@keyframes twr-08-retrace {
  from {
    transform: translateY(-120%);
  }

  to {
    transform: translateY(560%);
  }
}

.twr-08:has(#twr-08-theme:checked) {
  --color-twr08-bg: #dfe2e3;
  --color-twr08-bg: oklch(0.90 0.004 220);
  --color-twr08-surface: #f4f6f6;
  --color-twr08-surface: oklch(0.97 0.002 220);
  --color-twr08-ink: #16191b;
  --color-twr08-ink: oklch(0.20 0.005 220);
  --color-twr08-ink2: #4a5255;
  --color-twr08-ink2: oklch(0.43 0.009 220);
  --color-twr08-line: #aab1b4;
  --color-twr08-line: oklch(0.75 0.007 220);
  --color-twr08-acc: #0d6d5b;
  --color-twr08-acc: oklch(0.48 0.1 172);
}
```

## JavaScript
```js
/* The script sets state only — a data attribute — and never a style or a class.
   Appearance lives in data-fresh: variants on the template line. */
(function () {
  var root = document.querySelector('.twr-08');
  if (!root) return;
  var tpl = root.querySelector('[data-twr-08-line]');
  var feeds = Array.prototype.slice.call(root.querySelectorAll('[data-twr-08-feed]'));
  var lines = [
    ['[ ]', 'MEM CHECK 640K OK'], ['[ ]', 'SEEK TRK 00 SEC 01'],
    ['[!]', 'PARITY RETRY 1 OF 3'], ['[ ]', 'BUFFER FLUSHED 4096B'],
    ['[x]', 'DEVICE 2 NOT READY'], ['[ ]', 'LINK 1200 BAUD 8N1'],
    ['[>]', 'AWAITING OPERATOR'], ['[ ]', 'SPOOL QUEUE EMPTY']
  ];
  var i = 0;
  function write() {
    var pair = lines[i % lines.length];
    feeds.forEach(function (feed) {
      var node = tpl.content.firstElementChild.cloneNode(true);
      node.querySelector('[data-mark]').textContent = pair[0];
      node.querySelector('[data-text]').textContent = pair[1];
      node.setAttribute('data-fresh', '');
      feed.appendChild(node);
      requestAnimationFrame(function () {
        requestAnimationFrame(function () { node.removeAttribute('data-fresh'); });
      });
      while (feed.childElementCount > 9) feed.removeChild(feed.firstElementChild);
    });
    i += 1;
  }
  write();
  var timer = setInterval(write, 1500);
  root.__twrCleanup = function () {
    clearInterval(timer);
    feeds.forEach(function (f) { f.textContent = ''; });
  };
})();
```

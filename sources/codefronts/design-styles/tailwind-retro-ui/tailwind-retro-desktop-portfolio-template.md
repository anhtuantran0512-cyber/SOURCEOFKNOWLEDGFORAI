---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-retro-desktop-portfolio-template/"
title: "Tailwind Retro Desktop Portfolio Template"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A portfolio laid out as a desktop: menu bar, icon field and two windows you can move."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Retro Desktop Portfolio Template
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-retro-desktop-portfolio-template/

A portfolio laid out as a desktop: menu bar, icon field and two windows you can move. The drag is the point &mdash; a pointer-only implementation fails keyboard operability outright, so every title bar is focusable, responds to the arrow keys, and the script writes only custom properties and data- attributes, never a style rule or a class.
## HTML
```html
<section class="twr-20 relative block w-full min-h-svh box-border overflow-hidden bg-twr20-deska text-twr20-ink font-twr20-sans [background-image:linear-gradient(180deg,var(--color-twr20-deska),var(--color-twr20-deskb)),repeating-linear-gradient(90deg,rgba(255,255,255,0.28)_0_1px,rgba(0,0,0,0)_1px_6px)]" aria-labelledby="twr-20-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-20-title">Retro desktop portfolio with movable windows</h2>

  <div class="absolute top-[calc(44px+0.75rem)] right-4 z-30">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-20-theme">
    <label class="grid place-items-center size-11 rounded-full cursor-pointer border border-twr20-line bg-twr20-surface text-twr20-ink2 peer-focus-visible:outline-2 peer-focus-visible:outline-twr20-acc peer-focus-visible:outline-offset-2" for="twr-20-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark desktop</span>
    </label>
  </div>

  <div class="relative z-20 flex items-center gap-2 min-h-11 px-2 min-w-0 bg-twr20-chrome/90 border-b border-twr20-line">
    <span class="flex-none size-4 rounded-sm bg-twr20-acc" aria-hidden="true"></span>
    <nav class="min-w-0" aria-label="Desktop menu">
      <ul class="list-none m-0 p-0 flex">
        <li><button class="min-h-11 min-w-11 px-3 border-0 bg-transparent font-inherit text-[0.82rem] text-twr20-ink cursor-pointer rounded hover:bg-twr20-ink/8 focus-visible:outline-2 focus-visible:outline-twr20-acc focus-visible:outline-offset-[-3px]" type="button">File</button></li>
        <li><button class="min-h-11 min-w-11 px-3 border-0 bg-transparent font-inherit text-[0.82rem] text-twr20-ink cursor-pointer rounded hover:bg-twr20-ink/8 focus-visible:outline-2 focus-visible:outline-twr20-acc focus-visible:outline-offset-[-3px]" type="button">View</button></li>
        <li><button class="min-h-11 min-w-11 px-3 border-0 bg-transparent font-inherit text-[0.82rem] text-twr20-ink cursor-pointer rounded hover:bg-twr20-ink/8 focus-visible:outline-2 focus-visible:outline-twr20-acc focus-visible:outline-offset-[-3px]" type="button">Work</button></li>
        <li><button class="min-h-11 min-w-11 px-3 border-0 bg-transparent font-inherit text-[0.82rem] text-twr20-ink cursor-pointer rounded hover:bg-twr20-ink/8 focus-visible:outline-2 focus-visible:outline-twr20-acc focus-visible:outline-offset-[-3px]" type="button">Contact</button></li>
      </ul>
    </nav>
    <span class="ms-auto px-2 font-twr20-mono text-[0.75rem] whitespace-nowrap text-twr20-ink2">Sam Rivera &middot; 11:42</span>
  </div>

  <div class="relative min-h-[calc(100svh-44px)] px-[clamp(0.75rem,0.5rem+1.5vw,2rem)] pt-4 pb-16">
    <ul class="list-none m-0 p-0 flex flex-wrap gap-2 sm:flex-col sm:w-28">
      <li><button class="w-24 min-h-24 px-1 py-2 border-0 cursor-pointer bg-transparent font-inherit text-[0.72rem] leading-tight text-twr20-ink grid justify-items-center gap-1.5 rounded hover:bg-white/35 focus-visible:outline-2 focus-visible:outline-twr20-acc focus-visible:outline-offset-[-3px]" type="button"><span class="block w-8 h-6 bg-[#e8c777] [clip-path:polygon(0_14%,42%_14%,50%_0,100%_0,100%_100%,0_100%)]" aria-hidden="true"></span>Selected Work</button></li>
      <li><button class="w-24 min-h-24 px-1 py-2 border-0 cursor-pointer bg-transparent font-inherit text-[0.72rem] leading-tight text-twr20-ink grid justify-items-center gap-1.5 rounded hover:bg-white/35 focus-visible:outline-2 focus-visible:outline-twr20-acc focus-visible:outline-offset-[-3px]" type="button"><span class="block w-7 h-7 bg-white border border-twr20-line [clip-path:polygon(0_0,72%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></span>About.txt</button></li>
      <li><button class="w-24 min-h-24 px-1 py-2 border-0 cursor-pointer bg-transparent font-inherit text-[0.72rem] leading-tight text-twr20-ink grid justify-items-center gap-1.5 rounded hover:bg-white/35 focus-visible:outline-2 focus-visible:outline-twr20-acc focus-visible:outline-offset-[-3px]" type="button"><span class="block w-7 h-7 rounded-sm bg-[#9aa4bf] [clip-path:polygon(0_0,100%_0,100%_100%,0_100%)]" aria-hidden="true"></span>Archive</button></li>
    </ul>

    <article class="twr-20__win absolute min-w-0 w-[min(26rem,calc(100%-2rem))] rounded-lg overflow-hidden bg-twr20-surface border border-twr20-line [translate:var(--twr-20-x)_var(--twr-20-y)] [box-shadow:0_18px_40px_-20px_rgba(23,22,31,0.55)] top-4 left-[clamp(1rem,20vw,9rem)] [--twr-20-x:0px] [--twr-20-y:0px]" id="twr-20-win-1" data-twr-20-win aria-labelledby="twr-20-w1t">
      <div class="twr-20__cap flex items-center gap-2.5 min-h-11 px-3 cursor-grab select-none [touch-action:none] bg-twr20-chrome border-b border-twr20-line rounded-t-lg focus-visible:outline-2 focus-visible:outline-twr20-acc focus-visible:outline-offset-[-3px] active:cursor-grabbing" data-twr-20-handle tabindex="0" role="button" aria-describedby="twr-20-hint">
        <span class="flex flex-none gap-1" aria-hidden="true"><i class="block size-2.5 rounded-full bg-[#e0685f]"></i><i class="block size-2.5 rounded-full bg-[#e2b24a]"></i><i class="block size-2.5 rounded-full bg-[#63b463]"></i></span>
        <span class="min-w-0 overflow-hidden text-ellipsis whitespace-nowrap text-[0.82rem] font-semibold" id="twr-20-w1t">Selected Work &mdash; 2024 to 2026</span>
      </div>
      <div class="min-w-0 px-4 py-3">
        <ul class="list-none m-0 p-0 min-w-0">
          <li class="flex flex-wrap items-baseline justify-between gap-x-3 gap-y-0.5 min-w-0 border-b border-twr20-line/60 py-2 last:border-b-0"><span class="min-w-0 text-[0.92rem] font-semibold">Ledger</span><span class="min-w-0 font-twr20-mono text-[0.72rem] text-twr20-ink2">Design system &middot; 2026</span></li>
          <li class="flex flex-wrap items-baseline justify-between gap-x-3 gap-y-0.5 min-w-0 border-b border-twr20-line/60 py-2 last:border-b-0"><span class="min-w-0 text-[0.92rem] font-semibold">Northgate Radio</span><span class="min-w-0 font-twr20-mono text-[0.72rem] text-twr20-ink2">Product design &middot; 2025</span></li>
          <li class="flex flex-wrap items-baseline justify-between gap-x-3 gap-y-0.5 min-w-0 border-b border-twr20-line/60 py-2 last:border-b-0"><span class="min-w-0 text-[0.92rem] font-semibold">Field Notes</span><span class="min-w-0 font-twr20-mono text-[0.72rem] text-twr20-ink2">Editorial tooling &middot; 2025</span></li>
          <li class="flex flex-wrap items-baseline justify-between gap-x-3 gap-y-0.5 min-w-0 border-b border-twr20-line/60 py-2 last:border-b-0"><span class="min-w-0 text-[0.92rem] font-semibold">Sable</span><span class="min-w-0 font-twr20-mono text-[0.72rem] text-twr20-ink2">Identity &middot; 2024</span></li>
        </ul>
      </div>
    </article>

    <article class="twr-20__win absolute min-w-0 w-[min(26rem,calc(100%-2rem))] rounded-lg overflow-hidden bg-twr20-surface border border-twr20-line [translate:var(--twr-20-x)_var(--twr-20-y)] [box-shadow:0_18px_40px_-20px_rgba(23,22,31,0.55)] top-[clamp(15rem,34vw,20rem)] left-[clamp(1rem,26vw,14rem)] [--twr-20-x:0px] [--twr-20-y:0px]" id="twr-20-win-2" data-twr-20-win aria-labelledby="twr-20-w2t">
      <div class="twr-20__cap flex items-center gap-2.5 min-h-11 px-3 cursor-grab select-none [touch-action:none] bg-twr20-chrome border-b border-twr20-line rounded-t-lg focus-visible:outline-2 focus-visible:outline-twr20-acc focus-visible:outline-offset-[-3px] active:cursor-grabbing" data-twr-20-handle tabindex="0" role="button" aria-describedby="twr-20-hint">
        <span class="flex flex-none gap-1" aria-hidden="true"><i class="block size-2.5 rounded-full bg-[#e0685f]"></i><i class="block size-2.5 rounded-full bg-[#e2b24a]"></i><i class="block size-2.5 rounded-full bg-[#63b463]"></i></span>
        <span class="min-w-0 overflow-hidden text-ellipsis whitespace-nowrap text-[0.82rem] font-semibold" id="twr-20-w2t">About.txt</span>
      </div>
      <div class="min-w-0 grid gap-2.5 px-4 py-3">
        <p class="m-0 min-w-0 text-[0.92rem] leading-relaxed text-pretty">Product designer working on tools for people who make things. Previously at two consultancies and one very small hardware company.</p>
        <p class="m-0 min-w-0 text-[0.92rem] leading-relaxed text-pretty">This desktop is keyboard-operable: focus a title bar and use the arrow keys. Hold Shift for larger steps.</p>
        <p class="m-0 font-twr20-mono text-[0.78rem] text-twr20-acc">[email protected]</p>
      </div>
    </article>

    <p class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-20-hint">Move this window with the arrow keys, or drag the title bar. Hold Shift for larger steps.</p>

    <p class="absolute bottom-4 left-[clamp(0.75rem,0.5rem+1.5vw,2rem)] m-0 min-w-0 font-twr20-mono text-[0.72rem] text-twr20-ink2">Drag a title bar, or focus one with <kbd class="px-1 py-0.5 rounded-sm border border-twr20-line bg-twr20-surface">Tab</kbd> and use the arrow keys.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr20-deska: #dcd9ec;
  --color-twr20-deska: oklch(0.88 0.025 290);
  --color-twr20-deskb: #c6c2de;
  --color-twr20-deskb: oklch(0.82 0.035 290);
  --color-twr20-surface: #ffffff;
  --color-twr20-chrome: #edecf4;
  --color-twr20-ink: #17161f;
  --color-twr20-ink: oklch(0.20 0.012 290);
  --color-twr20-ink2: #4c4a5c;
  --color-twr20-ink2: oklch(0.43 0.018 290);
  --color-twr20-line: #a9a5c0;
  --color-twr20-line: oklch(0.72 0.026 290);
  --color-twr20-acc: #4b2ad0;
  --color-twr20-acc: oklch(0.44 0.21 285);
  --font-twr20-sans: 'Archivo', system-ui, -apple-system, 'Segoe UI', Arial, sans-serif;
  --font-twr20-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
/* A dragging window should not animate towards the pointer. The attribute is
   set by the script; the declaration stays here because it must win over any
   transition utility applied to the window. */

.twr-20__win[data-dragging] {
  transition: none;
}

.twr-20:has(#twr-20-theme:checked) {
  --color-twr20-deska: #191727;
  --color-twr20-deska: oklch(0.22 0.03 290);
  --color-twr20-deskb: #100f1c;
  --color-twr20-deskb: oklch(0.17 0.028 290);
  --color-twr20-surface: #201e2e;
  --color-twr20-chrome: #2a2839;
  --color-twr20-ink: #efeef7;
  --color-twr20-ink: oklch(0.95 0.008 290);
  --color-twr20-ink2: #aeaac4;
  --color-twr20-ink2: oklch(0.75 0.02 290);
  --color-twr20-line: #423e58;
  --color-twr20-line: oklch(0.38 0.03 290);
  --color-twr20-acc: #b7a4ff;
  --color-twr20-acc: oklch(0.80 0.14 285);
}
```

## JavaScript
```js
/* The script writes two custom properties and one data attribute. It never
   sets a style rule and never toggles a class — the markup owns appearance. */
(function () {
  var root = document.querySelector('.twr-20');
  if (!root) return;
  var STEP = 16;
  var BIG = 64;
  var z = 10;
  var handles = Array.prototype.slice.call(root.querySelectorAll('[data-twr-20-handle]'));
  var bound = [];

  function num(win, prop) {
    return parseFloat(win.style.getPropertyValue(prop)) || 0;
  }
  function move(win, dx, dy) {
    win.style.setProperty('--twr-20-x', (num(win, '--twr-20-x') + dx) + 'px');
    win.style.setProperty('--twr-20-y', (num(win, '--twr-20-y') + dy) + 'px');
  }
  function raise(win) { win.style.zIndex = String(++z); }

  handles.forEach(function (handle) {
    var win = handle.closest('[data-twr-20-win]');
    var startX = 0, startY = 0, baseX = 0, baseY = 0;

    function onDown(e) {
      raise(win);
      startX = e.clientX; startY = e.clientY;
      baseX = num(win, '--twr-20-x'); baseY = num(win, '--twr-20-y');
      win.dataset.dragging = '';
      handle.setPointerCapture(e.pointerId);
    }
    function onMove(e) {
      if (!('dragging' in win.dataset)) return;
      win.style.setProperty('--twr-20-x', (baseX + e.clientX - startX) + 'px');
      win.style.setProperty('--twr-20-y', (baseY + e.clientY - startY) + 'px');
    }
    function onUp() { delete win.dataset.dragging; }
    function onKey(e) {
      var step = e.shiftKey ? BIG : STEP;
      if (e.key === 'ArrowLeft') { move(win, -step, 0); }
      else if (e.key === 'ArrowRight') { move(win, step, 0); }
      else if (e.key === 'ArrowUp') { move(win, 0, -step); }
      else if (e.key === 'ArrowDown') { move(win, 0, step); }
      else { return; }
      e.preventDefault();
    }
    function onFocus() { raise(win); }

    handle.addEventListener('pointerdown', onDown);
    handle.addEventListener('pointermove', onMove);
    handle.addEventListener('pointerup', onUp);
    handle.addEventListener('pointercancel', onUp);
    handle.addEventListener('keydown', onKey);
    win.addEventListener('focusin', onFocus);
    bound.push([handle, win, onDown, onMove, onUp, onKey, onFocus]);
  });

  root.__twrCleanup = function () {
    bound.forEach(function (b) {
      b[0].removeEventListener('pointerdown', b[2]);
      b[0].removeEventListener('pointermove', b[3]);
      b[0].removeEventListener('pointerup', b[4]);
      b[0].removeEventListener('pointercancel', b[4]);
      b[0].removeEventListener('keydown', b[5]);
      b[1].removeEventListener('focusin', b[6]);
    });
    bound.length = 0;
  };
})();
```

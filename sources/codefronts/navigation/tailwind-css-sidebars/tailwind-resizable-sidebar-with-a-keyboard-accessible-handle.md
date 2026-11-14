---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-resizable-sidebar-with-a-keyboard-accessible-handle/"
title: "Tailwind Resizable Sidebar with a Keyboard Accessible Handle"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "A drag handle that only works with a mouse excludes every keyboard user, and a <div> with a col-resize cursor tells assistive technology nothing."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Resizable Sidebar with a Keyboard Accessible Handle
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-resizable-sidebar-with-a-keyboard-accessible-handle/

A drag handle that only works with a mouse excludes every keyboard user, and a <div> with a col-resize cursor tells assistive technology nothing. This one is a real role="separator" with aria-valuenow, driven by pointer events AND arrow keys &mdash; and in the port the live width stays where it has to: a custom property the panel reads through w-[var(--tsb10-w)].
## HTML
```html
<section class="tsb-10 block relative w-full min-h-svh bg-tsb10-bg text-tsb10-ink font-tsb10-sans leading-[1.55]" aria-label="Aperture editor">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-10-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-10-theme">
    <label class="grid place-items-center w-11 h-11 border border-tsb10-line bg-tsb10-surf text-tsb10-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb10-acc peer-focus-visible:outline-offset-2" for="tsb-10-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="flex min-w-0 h-svh bg-tsb10-surf max-r34:flex-col max-r34:h-auto max-r34:min-h-svh" id="tsb-10-app" style="--tsb10-w: 17rem;">
    <main class="flex-1 flex flex-col gap-2.5 min-w-0 p-4 bg-tsb10-bg max-r34:min-h-56">
      <p class="m-0 font-tsb10-mono text-[0.72rem] text-tsb10-mut">Artboard &mdash; Meridian marketing site</p>
      <div class="flex-1 min-h-0 grid grid-cols-[minmax(0,1fr)] gap-2.5 [&>span]:border [&>span]:border-tsb10-line [&>span]:bg-tsb10-surf2" aria-hidden="true">
        <span class="!border-tsb10-acc"></span>
        <span></span>
        <span></span>
      </div>
    </main>

    <div class="flex-none grid place-items-center w-3.5 -mx-1 z-3 cursor-col-resize bg-transparent [touch-action:none] [&:hover>span]:bg-tsb10-acc [&:hover>span]:w-1 [&:focus-visible>span]:bg-tsb10-acc [&:focus-visible>span]:w-1 focus-visible:outline-2 focus-visible:outline-tsb10-acc focus-visible:-outline-offset-1 max-r34:hidden" id="tsb-10-handle" role="separator" tabindex="0" aria-orientation="vertical"
         aria-label="Resize layers panel" aria-valuemin="200" aria-valuemax="440" aria-valuenow="272" aria-controls="tsb-10-panel">
      <span class="block w-0.5 h-full bg-tsb10-line" aria-hidden="true"></span>
    </div>

    <aside class="flex-none flex flex-col min-w-0 w-[var(--tsb10-w)] border-l border-tsb10-line max-r34:w-full max-r34:border-l-0 max-r34:border-t" id="tsb-10-panel">
      <div class="flex items-center gap-2 px-2.5 py-2 border-b border-tsb10-line">
        <p class="mr-auto m-0 font-tsb10-mono text-[0.78rem] tracking-[0.1em] uppercase text-tsb10-mut">Layers</p>
        <output class="font-tsb10-mono text-[0.78rem] tabular-nums text-tsb10-acc" id="tsb-10-value">272px</output>
      </div>
      <nav class="flex-1 min-h-0 overflow-y-auto p-1 [overscroll-behavior:contain]" aria-label="Layer groups">
        <ul class="list-none m-0 p-0">
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 overflow-hidden text-ellipsis whitespace-nowrap text-[0.88rem] text-tsb10-ink no-underline hover:bg-tsb10-surf2 focus-visible:outline-2 focus-visible:outline-tsb10-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb10-accsoft aria-[current=page]:text-tsb10-acc aria-[current=page]:font-semibold aria-[current=page]:[&>span]:bg-tsb10-acc" href="#tsb-10-panel" aria-current="page"><span class="flex-none w-2 h-2 bg-tsb10-mut" aria-hidden="true"></span>Hero / masthead</a></li>
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 overflow-hidden text-ellipsis whitespace-nowrap text-[0.88rem] text-tsb10-ink no-underline hover:bg-tsb10-surf2 focus-visible:outline-2 focus-visible:outline-tsb10-acc focus-visible:-outline-offset-2" href="#tsb-10-panel"><span class="flex-none w-2 h-2 bg-tsb10-mut" aria-hidden="true"></span>Feature grid</a></li>
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 overflow-hidden text-ellipsis whitespace-nowrap text-[0.88rem] text-tsb10-ink no-underline hover:bg-tsb10-surf2 focus-visible:outline-2 focus-visible:outline-tsb10-acc focus-visible:-outline-offset-2" href="#tsb-10-panel"><span class="flex-none w-2 h-2 bg-tsb10-mut" aria-hidden="true"></span>Pricing table</a></li>
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 overflow-hidden text-ellipsis whitespace-nowrap text-[0.88rem] text-tsb10-ink no-underline hover:bg-tsb10-surf2 focus-visible:outline-2 focus-visible:outline-tsb10-acc focus-visible:-outline-offset-2" href="#tsb-10-panel"><span class="flex-none w-2 h-2 bg-tsb10-mut" aria-hidden="true"></span>Footer / legal</a></li>
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 overflow-hidden text-ellipsis whitespace-nowrap text-[0.88rem] text-tsb10-ink no-underline hover:bg-tsb10-surf2 focus-visible:outline-2 focus-visible:outline-tsb10-acc focus-visible:-outline-offset-2" href="#tsb-10-panel"><span class="flex-none w-2 h-2 bg-tsb10-mut" aria-hidden="true"></span>Annotations</a></li>
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 overflow-hidden text-ellipsis whitespace-nowrap text-[0.88rem] text-tsb10-ink no-underline hover:bg-tsb10-surf2 focus-visible:outline-2 focus-visible:outline-tsb10-acc focus-visible:-outline-offset-2" href="#tsb-10-panel"><span class="flex-none w-2 h-2 bg-tsb10-mut" aria-hidden="true"></span>Grid guides</a></li>
        </ul>
      </nav>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb10-bg: #1a1a1c;
  --color-tsb10-bg: oklch(22% 0.003 285);
  --color-tsb10-surf: #232326;
  --color-tsb10-surf: oklch(26% 0.004 285);
  --color-tsb10-surf2: #2c2c30;
  --color-tsb10-surf2: oklch(30% 0.005 285);
  --color-tsb10-line: #3a3a3f;
  --color-tsb10-line: oklch(37% 0.006 285);
  --color-tsb10-ink: #ececef;
  --color-tsb10-ink: oklch(94% 0.003 285);
  --color-tsb10-mut: #9b9ba3;
  --color-tsb10-mut: oklch(67% 0.008 285);
  --color-tsb10-acc: #d8d84a;
  --color-tsb10-acc: oklch(86% 0.17 105);
  --color-tsb10-accsoft: #33331a;
  --color-tsb10-accsoft: oklch(30% 0.05 105);
  --font-tsb10-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb10-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  --breakpoint-r34: 34rem;
}
/* Root rule: the full-bleed contract. The live panel width is NOT here — it is an inline
   custom property on the app shell, because it changes on every pointer move and no
   static utility can express it. */

.tsb-10 {
  width: 100%;
  min-height: 100svh;
}

.tsb-10 *,
.tsb-10 *::before,
.tsb-10 *::after {
  box-sizing: border-box;
}
/* Dark-first demo: the @theme block IS the dark palette and the light mirror lives in
   prefers-color-scheme: light. */

.tsb-10:has(.tsb-10-theme-input:checked) {
  --color-tsb10-bg: #f2f2f0;
  --color-tsb10-surf: #ffffff;
  --color-tsb10-surf2: #e7e7e3;
  --color-tsb10-line: #cfcfc9;
  --color-tsb10-ink: #1a1a18;
  --color-tsb10-mut: #5e5e58;
  --color-tsb10-acc: #6b6b12;
  --color-tsb10-acc: oklch(48% 0.13 105);
  --color-tsb10-accsoft: #eaeacb;
}

@media (prefers-color-scheme: light) {
  .tsb-10 {
    --color-tsb10-bg: #f2f2f0;
    --color-tsb10-surf: #ffffff;
    --color-tsb10-surf2: #e7e7e3;
    --color-tsb10-line: #cfcfc9;
    --color-tsb10-ink: #1a1a18;
    --color-tsb10-mut: #5e5e58;
    --color-tsb10-acc: #6b6b12;
    --color-tsb10-acc: oklch(48% 0.13 105);
    --color-tsb10-accsoft: #eaeacb;
  }

  .tsb-10:has(.tsb-10-theme-input:checked) {
    --color-tsb10-bg: #1a1a1c;
    --color-tsb10-surf: #232326;
    --color-tsb10-surf2: #2c2c30;
    --color-tsb10-line: #3a3a3f;
    --color-tsb10-ink: #ececef;
    --color-tsb10-mut: #9b9ba3;
    --color-tsb10-acc: #d8d84a;
    --color-tsb10-acc: oklch(86% 0.17 105);
    --color-tsb10-accsoft: #33331a;
  }
}

@media (prefers-color-scheme: dark) {
  .tsb-10:has(.tsb-10-theme-input:checked) {
    --color-tsb10-bg: #f2f2f0;
    --color-tsb10-surf: #ffffff;
    --color-tsb10-surf2: #e7e7e3;
    --color-tsb10-line: #cfcfc9;
    --color-tsb10-ink: #1a1a18;
    --color-tsb10-mut: #5e5e58;
    --color-tsb10-acc: #6b6b12;
    --color-tsb10-acc: oklch(48% 0.13 105);
    --color-tsb10-accsoft: #eaeacb;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tsb-10').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var app = root.querySelector('#tsb-10-app'),
        handle = root.querySelector('#tsb-10-handle'),
        out = root.querySelector('#tsb-10-value'),
        KEY = 'tsb-10:panel-w', MIN = 200, MAX = 440, w;
    function clamp(n) { return Math.min(MAX, Math.max(MIN, Math.round(n))); }
    try { w = clamp(Number(localStorage.getItem(KEY)) || 272); } catch (e) { w = 272; }
    function set(next) {
      w = clamp(next);
      app.style.setProperty('--tsb10-w', w + 'px');
      handle.setAttribute('aria-valuenow', String(w));
      out.textContent = w + 'px';
      try { localStorage.setItem(KEY, String(w)); } catch (e) { /* storage blocked: session only */ }
    }
    function onKey(e) {
      var step = e.shiftKey ? 64 : 16,
          map = { ArrowLeft: w + step, ArrowRight: w - step, Home: MAX, End: MIN };
      if (!(e.key in map)) return;
      e.preventDefault();
      set(map[e.key]);
    }
    function onMove(e) { set(app.getBoundingClientRect().right - e.clientX); }
    function onUp(e) { handle.releasePointerCapture(e.pointerId); handle.removeEventListener('pointermove', onMove); }
    function onDown(e) {
      handle.setPointerCapture(e.pointerId);
      handle.addEventListener('pointermove', onMove);
      handle.addEventListener('pointerup', onUp, { once: true });
    }
    handle.addEventListener('keydown', onKey);
    handle.addEventListener('pointerdown', onDown);
    set(w);
    root.__tsbCleanup = function () {
      handle.removeEventListener('keydown', onKey);
      handle.removeEventListener('pointerdown', onDown);
      handle.removeEventListener('pointermove', onMove);
    };
  });
})();
```

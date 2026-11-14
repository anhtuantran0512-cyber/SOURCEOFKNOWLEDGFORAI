---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-persisting-sidebar-collapse-state-across-reloads/"
title: "Tailwind Persisting Sidebar Collapse State Across Reloads"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "A collapse toggle the user has to re-click on every reload is a toggle that does not work."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Persisting Sidebar Collapse State Across Reloads
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-persisting-sidebar-collapse-state-across-reloads/

A collapse toggle the user has to re-click on every reload is a toggle that does not work. This one writes to localStorage and restores on load &mdash; and the detail that makes it feel native is the second attribute: data-noanim, read by group-data-noanim:transition-none, which suppresses the width transition for exactly one frame so the restored rail appears already collapsed instead of animating into place.
## HTML
```html
<section class="tsb-07 block relative w-full min-h-svh bg-tsb07-bg text-tsb07-ink font-tsb07-sans leading-[1.55]" aria-label="Prism analytics">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-07-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-07-theme">
    <label class="grid place-items-center w-11 h-11 border border-tsb07-line bg-tsb07-surf text-tsb07-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb07-acc peer-focus-visible:outline-offset-2" for="tsb-07-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="group flex min-w-0 min-h-svh bg-tsb07-surf max-r30:flex-col" data-collapsed="false" data-noanim>
    <aside class="flex-none flex flex-col min-w-0 w-[var(--tsb07-w-open)] bg-tsb07-surf2 border-r border-tsb07-line transition-[width] duration-200 ease-out group-data-[collapsed=true]:w-[var(--tsb07-w-rail)] group-data-noanim:transition-none motion-reduce:transition-none max-r30:w-full max-r30:border-r-0 max-r30:border-b max-r30:group-data-[collapsed=true]:w-full" id="tsb-07-rail">
      <div class="flex items-center gap-2 px-2.5 py-2 pr-14 border-b border-tsb07-line group-data-[collapsed=true]:flex-col group-data-[collapsed=true]:gap-1 group-data-[collapsed=true]:px-0 group-data-[collapsed=true]:py-1.5 r30:pr-2.5">
        <span class="flex-none grid place-items-center w-7.5 h-7.5 bg-tsb07-acc text-tsb07-onacc text-[0.7rem] font-bold tracking-[0.06em]" aria-hidden="true">PR</span>
        <p class="mr-auto m-0 min-w-0 overflow-hidden font-tsb07-display text-[0.82rem] tracking-[0.2em] uppercase group-data-[collapsed=true]:mr-0 group-data-[collapsed=true]:flex-none"><span class="min-w-0 overflow-hidden text-ellipsis group-data-[collapsed=true]:absolute group-data-[collapsed=true]:w-px group-data-[collapsed=true]:h-px group-data-[collapsed=true]:whitespace-nowrap group-data-[collapsed=true]:[clip-path:inset(50%)]">Prism</span></p>
        <button class="flex-none grid place-items-center w-11 h-11 border-0 bg-transparent text-tsb07-ink cursor-pointer [&>svg]:w-4.5 [&>svg]:h-4.5 focus-visible:outline-2 focus-visible:outline-tsb07-acc focus-visible:-outline-offset-2" type="button" id="tsb-07-toggle" aria-expanded="true" aria-controls="tsb-07-rail">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h10M4 18h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]" data-tsb-07-label>Collapse sidebar</span>
        </button>
      </div>
      <nav class="min-w-0 px-1.5 py-1.5" aria-label="Prism reports">
        <ul class="list-none m-0 p-0">
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 text-[0.9rem] text-tsb07-ink no-underline whitespace-nowrap hover:bg-tsb07-surf focus-visible:outline-2 focus-visible:outline-tsb07-acc focus-visible:-outline-offset-2 aria-[current=page]:bg-tsb07-accsoft aria-[current=page]:text-tsb07-acc aria-[current=page]:font-semibold aria-[current=page]:[&>span:first-child]:text-tsb07-acc" href="#tsb-07-main" aria-current="page"><span class="flex-none w-6 font-tsb07-mono text-[0.72rem] text-tsb07-mut" aria-hidden="true">01</span><span class="min-w-0 overflow-hidden text-ellipsis group-data-[collapsed=true]:absolute group-data-[collapsed=true]:w-px group-data-[collapsed=true]:h-px group-data-[collapsed=true]:whitespace-nowrap group-data-[collapsed=true]:[clip-path:inset(50%)]">Overview</span></a></li>
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 text-[0.9rem] text-tsb07-ink no-underline whitespace-nowrap hover:bg-tsb07-surf focus-visible:outline-2 focus-visible:outline-tsb07-acc focus-visible:-outline-offset-2" href="#tsb-07-main"><span class="flex-none w-6 font-tsb07-mono text-[0.72rem] text-tsb07-mut" aria-hidden="true">02</span><span class="min-w-0 overflow-hidden text-ellipsis group-data-[collapsed=true]:absolute group-data-[collapsed=true]:w-px group-data-[collapsed=true]:h-px group-data-[collapsed=true]:whitespace-nowrap group-data-[collapsed=true]:[clip-path:inset(50%)]">Acquisition</span></a></li>
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 text-[0.9rem] text-tsb07-ink no-underline whitespace-nowrap hover:bg-tsb07-surf focus-visible:outline-2 focus-visible:outline-tsb07-acc focus-visible:-outline-offset-2" href="#tsb-07-main"><span class="flex-none w-6 font-tsb07-mono text-[0.72rem] text-tsb07-mut" aria-hidden="true">03</span><span class="min-w-0 overflow-hidden text-ellipsis group-data-[collapsed=true]:absolute group-data-[collapsed=true]:w-px group-data-[collapsed=true]:h-px group-data-[collapsed=true]:whitespace-nowrap group-data-[collapsed=true]:[clip-path:inset(50%)]">Retention</span></a></li>
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 text-[0.9rem] text-tsb07-ink no-underline whitespace-nowrap hover:bg-tsb07-surf focus-visible:outline-2 focus-visible:outline-tsb07-acc focus-visible:-outline-offset-2" href="#tsb-07-main"><span class="flex-none w-6 font-tsb07-mono text-[0.72rem] text-tsb07-mut" aria-hidden="true">04</span><span class="min-w-0 overflow-hidden text-ellipsis group-data-[collapsed=true]:absolute group-data-[collapsed=true]:w-px group-data-[collapsed=true]:h-px group-data-[collapsed=true]:whitespace-nowrap group-data-[collapsed=true]:[clip-path:inset(50%)]">Revenue</span></a></li>
          <li><a class="flex items-center gap-2.5 min-w-0 min-h-11 px-2.5 py-2 text-[0.9rem] text-tsb07-ink no-underline whitespace-nowrap hover:bg-tsb07-surf focus-visible:outline-2 focus-visible:outline-tsb07-acc focus-visible:-outline-offset-2" href="#tsb-07-main"><span class="flex-none w-6 font-tsb07-mono text-[0.72rem] text-tsb07-mut" aria-hidden="true">05</span><span class="min-w-0 overflow-hidden text-ellipsis group-data-[collapsed=true]:absolute group-data-[collapsed=true]:w-px group-data-[collapsed=true]:h-px group-data-[collapsed=true]:whitespace-nowrap group-data-[collapsed=true]:[clip-path:inset(50%)]">Audit log</span></a></li>
        </ul>
      </nav>
    </aside>

    <main class="flex-1 min-w-0 grid gap-5 content-start px-5 pt-6 pb-10 r46:px-9 r46:pt-10 r46:pb-12" id="tsb-07-main">
      <div class="grid grid-cols-[minmax(0,1fr)] gap-3 r34:grid-cols-3">
        <div class="min-w-0 px-4 py-3.5 border border-tsb07-line"><p class="m-0 mb-1 text-[0.7rem] tracking-[0.12em] uppercase text-tsb07-mut">Active workspaces</p><p class="m-0 font-tsb07-display text-[1.45rem] tabular-nums">1,284</p></div>
        <div class="min-w-0 px-4 py-3.5 border border-tsb07-line"><p class="m-0 mb-1 text-[0.7rem] tracking-[0.12em] uppercase text-tsb07-mut">Weekly retention</p><p class="m-0 font-tsb07-display text-[1.45rem] tabular-nums">71.4%</p></div>
        <div class="min-w-0 px-4 py-3.5 border border-tsb07-line"><p class="m-0 mb-1 text-[0.7rem] tracking-[0.12em] uppercase text-tsb07-mut">Net revenue</p><p class="m-0 font-tsb07-display text-[1.45rem] tabular-nums">$418k</p></div>
      </div>
      <div class="flex items-end gap-1.5 h-48 p-3 border border-tsb07-line [&>span]:flex-1 [&>span]:min-w-0 [&>span]:bg-tsb07-acc [&>span]:opacity-75 [&>span]:h-[calc(var(--tsb07-h)*1%)]" aria-hidden="true">
        <span style="--tsb07-h:32"></span><span style="--tsb07-h:48"></span><span style="--tsb07-h:41"></span>
        <span style="--tsb07-h:66"></span><span style="--tsb07-h:58"></span><span style="--tsb07-h:74"></span>
        <span style="--tsb07-h:69"></span><span style="--tsb07-h:88"></span><span style="--tsb07-h:79"></span>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb07-bg: #eef4f1;
  --color-tsb07-bg: oklch(95.5% 0.012 172);
  --color-tsb07-surf: #ffffff;
  --color-tsb07-surf: oklch(100% 0 0);
  --color-tsb07-surf2: #e2ebe7;
  --color-tsb07-surf2: oklch(92.5% 0.016 172);
  --color-tsb07-line: #cbd8d2;
  --color-tsb07-line: oklch(86% 0.02 172);
  --color-tsb07-ink: #16211d;
  --color-tsb07-ink: oklch(21% 0.018 172);
  --color-tsb07-mut: #5a6a64;
  --color-tsb07-mut: oklch(47% 0.02 172);
  --color-tsb07-acc: #0f7a63;
  --color-tsb07-acc: oklch(50% 0.1 172);
  --color-tsb07-accsoft: #d5eae4;
  --color-tsb07-accsoft: oklch(91% 0.03 172);
  --color-tsb07-onacc: #ffffff;
  --color-tsb07-onacc: oklch(100% 0 0);
  --font-tsb07-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb07-display: 'Archivo', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --font-tsb07-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  --breakpoint-r30: 30rem;
  --breakpoint-r34: 34rem;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract plus the two rail widths, which are geometry read
   by w-[var(...)] rather than a colour scale. */

.tsb-07 {
  width: 100%;
  min-height: 100svh;
  --tsb07-w-open: 14.5rem;
  --tsb07-w-rail: 4.25rem;
}

.tsb-07 *,
.tsb-07 *::before,
.tsb-07 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks. */

.tsb-07:has(.tsb-07-theme-input:checked) {
  --color-tsb07-bg: #0b1210;
  --color-tsb07-surf: #121a18;
  --color-tsb07-surf2: #18221f;
  --color-tsb07-line: #26332f;
  --color-tsb07-ink: #e9f1ee;
  --color-tsb07-mut: #93a4a0;
  --color-tsb07-acc: #62d9b8;
  --color-tsb07-acc: oklch(82% 0.12 172);
  --color-tsb07-accsoft: #12302a;
  --color-tsb07-onacc: #0b1210;
}

@media (prefers-color-scheme: dark) {
  .tsb-07 {
    --color-tsb07-bg: #0b1210;
    --color-tsb07-surf: #121a18;
    --color-tsb07-surf2: #18221f;
    --color-tsb07-line: #26332f;
    --color-tsb07-ink: #e9f1ee;
    --color-tsb07-mut: #93a4a0;
    --color-tsb07-acc: #62d9b8;
    --color-tsb07-acc: oklch(82% 0.12 172);
    --color-tsb07-accsoft: #12302a;
    --color-tsb07-onacc: #0b1210;
  }

  .tsb-07:has(.tsb-07-theme-input:checked) {
    --color-tsb07-bg: #eef4f1;
    --color-tsb07-surf: #ffffff;
    --color-tsb07-surf2: #e2ebe7;
    --color-tsb07-line: #cbd8d2;
    --color-tsb07-ink: #16211d;
    --color-tsb07-mut: #5a6a64;
    --color-tsb07-acc: #0f7a63;
    --color-tsb07-acc: oklch(50% 0.1 172);
    --color-tsb07-accsoft: #d5eae4;
    --color-tsb07-onacc: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-07:has(.tsb-07-theme-input:checked) {
    --color-tsb07-bg: #0b1210;
    --color-tsb07-surf: #121a18;
    --color-tsb07-surf2: #18221f;
    --color-tsb07-line: #26332f;
    --color-tsb07-ink: #e9f1ee;
    --color-tsb07-mut: #93a4a0;
    --color-tsb07-acc: #62d9b8;
    --color-tsb07-acc: oklch(82% 0.12 172);
    --color-tsb07-accsoft: #12302a;
    --color-tsb07-onacc: #0b1210;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tsb-07').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var app = root.querySelector('.group'),
        btn = root.querySelector('#tsb-07-toggle'),
        label = btn.querySelector('[data-tsb-07-label]'),
        KEY = 'tsb-07:rail-collapsed';
    function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
    function write(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
    function paint(collapsed) {
      app.setAttribute('data-collapsed', String(collapsed));
      btn.setAttribute('aria-expanded', String(!collapsed));
      label.textContent = collapsed ? 'Expand sidebar' : 'Collapse sidebar';
    }
    // In production this runs as an inline script in <head>, so the restored width is
    // correct in the first frame and data-noanim is not needed at all.
    app.setAttribute('data-noanim', '');
    paint(read() === 'true');
    requestAnimationFrame(function () { app.removeAttribute('data-noanim'); });
    function toggle() {
      var collapsed = app.getAttribute('data-collapsed') !== 'true';
      write(String(collapsed));
      paint(collapsed);
    }
    btn.addEventListener('click', toggle);
    root.__tsbCleanup = function () { btn.removeEventListener('click', toggle); };
  });
})();
```

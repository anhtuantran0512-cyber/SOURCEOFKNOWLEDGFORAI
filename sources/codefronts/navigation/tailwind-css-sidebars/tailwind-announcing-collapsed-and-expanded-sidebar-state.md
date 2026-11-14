---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-announcing-collapsed-and-expanded-sidebar-state/"
title: "Tailwind Announcing Collapsed and Expanded Sidebar State"
section: "navigation"
category: "tailwind-css-sidebars"
category_name: "Tailwind CSS Sidebars"
description: "A rail that collapses to icons has to say so."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Announcing Collapsed and Expanded Sidebar State
Source: https://codefronts.com/navigation/tailwind-css-sidebars/tailwind-announcing-collapsed-and-expanded-sidebar-state/

A rail that collapses to icons has to say so. The control is a real button carrying aria-expanded, its accessible name changes with the state, and the labels become visually hidden rather than display:none &mdash; so the collapsed rail still announces &ldquo;Albums, link&rdquo;. In utilities the whole collapsed geometry reads off one data-state attribute through group-data-[state=collapsed]:.
## HTML
```html
<section class="tsb-05 block relative w-full min-h-svh bg-tsb05-bg text-tsb05-ink font-tsb05-sans leading-[1.55]" aria-label="Nova player">
  <div class="absolute top-3.5 right-3.5 z-60">
    <input class="tsb-05-theme-input peer absolute inset-0 w-full h-full m-0 opacity-0 cursor-pointer" type="checkbox" id="tsb-05-theme">
    <label class="grid place-items-center w-11 h-11 rounded-[1.4rem] border border-tsb05-line bg-tsb05-surf text-tsb05-ink cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-tsb05-acc peer-focus-visible:outline-offset-2" for="tsb-05-theme">
      <svg class="w-4.5 h-4.5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">Toggle dark theme</span>
    </label>
  </div>

  <div class="group flex min-w-0 min-h-svh bg-tsb05-surf max-r30:flex-col" data-state="expanded">
    <div class="flex-none flex flex-col min-w-0 w-[var(--tsb05-w-open)] bg-tsb05-rail text-tsb05-onrail transition-[width] duration-[220ms] ease-out group-data-[state=collapsed]:w-[var(--tsb05-w-rail)] max-r30:w-full max-r30:group-data-[state=collapsed]:w-full motion-reduce:transition-none" id="tsb-05-rail">
      <div class="flex items-center gap-1.5 px-2.5 py-2.5 pr-14 r30:pr-2.5">
        <p class="mr-auto m-0 flex items-center gap-2 min-w-0 font-tsb05-display text-[1.05rem] font-bold text-tsb05-acc"><span aria-hidden="true">&#9679;</span><span class="min-w-0 overflow-hidden text-ellipsis group-data-[state=collapsed]:absolute group-data-[state=collapsed]:w-px group-data-[state=collapsed]:h-px group-data-[state=collapsed]:whitespace-nowrap group-data-[state=collapsed]:[clip-path:inset(50%)]">Nova</span></p>
        <button class="flex-none grid place-items-center w-11 h-11 rounded-[1.4rem] border-0 bg-white/10 text-inherit cursor-pointer focus-visible:outline-2 focus-visible:outline-tsb05-acc focus-visible:outline-offset-2" type="button" id="tsb-05-toggle" aria-expanded="true" aria-controls="tsb-05-rail">
          <svg class="w-4.5 h-4.5 transition-transform duration-200 ease-out group-data-[state=collapsed]:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14 6l-6 6 6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]" data-tsb-05-label>Collapse sidebar</span>
        </button>
      </div>
      <nav class="min-w-0 px-2 pt-1 pb-3" aria-label="Nova library">
        <ul class="list-none m-0 p-0 grid gap-0.5">
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.93rem] text-inherit no-underline whitespace-nowrap [&>svg]:w-5 [&>svg]:h-5 [&>svg]:flex-none [&>svg]:opacity-75 hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-tsb05-acc focus-visible:outline-offset-2 aria-[current=page]:bg-tsb05-acc aria-[current=page]:text-tsb05-onacc aria-[current=page]:font-semibold aria-[current=page]:[&>svg]:opacity-100 group-data-[state=collapsed]:justify-center group-data-[state=collapsed]:gap-0" href="#tsb-05-main" aria-current="page">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <span class="min-w-0 overflow-hidden text-ellipsis group-data-[state=collapsed]:absolute group-data-[state=collapsed]:w-px group-data-[state=collapsed]:h-px group-data-[state=collapsed]:whitespace-nowrap group-data-[state=collapsed]:[clip-path:inset(50%)]">Listen now</span></a></li>
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.93rem] text-inherit no-underline whitespace-nowrap [&>svg]:w-5 [&>svg]:h-5 [&>svg]:flex-none [&>svg]:opacity-75 hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-tsb05-acc focus-visible:outline-offset-2 group-data-[state=collapsed]:justify-center group-data-[state=collapsed]:gap-0" href="#tsb-05-main">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="2.4" fill="currentColor"/></svg>
            <span class="min-w-0 overflow-hidden text-ellipsis group-data-[state=collapsed]:absolute group-data-[state=collapsed]:w-px group-data-[state=collapsed]:h-px group-data-[state=collapsed]:whitespace-nowrap group-data-[state=collapsed]:[clip-path:inset(50%)]">Albums</span></a></li>
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.93rem] text-inherit no-underline whitespace-nowrap [&>svg]:w-5 [&>svg]:h-5 [&>svg]:flex-none [&>svg]:opacity-75 hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-tsb05-acc focus-visible:outline-offset-2 group-data-[state=collapsed]:justify-center group-data-[state=collapsed]:gap-0" href="#tsb-05-main">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 19V7l12-2v12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="6" cy="19" r="2.2" fill="currentColor"/><circle cx="18" cy="17" r="2.2" fill="currentColor"/></svg>
            <span class="min-w-0 overflow-hidden text-ellipsis group-data-[state=collapsed]:absolute group-data-[state=collapsed]:w-px group-data-[state=collapsed]:h-px group-data-[state=collapsed]:whitespace-nowrap group-data-[state=collapsed]:[clip-path:inset(50%)]">Playlists</span></a></li>
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.93rem] text-inherit no-underline whitespace-nowrap [&>svg]:w-5 [&>svg]:h-5 [&>svg]:flex-none [&>svg]:opacity-75 hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-tsb05-acc focus-visible:outline-offset-2 group-data-[state=collapsed]:justify-center group-data-[state=collapsed]:gap-0" href="#tsb-05-main">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.6-7-9a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 4.4-7 9-7 9Z" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
            <span class="min-w-0 overflow-hidden text-ellipsis group-data-[state=collapsed]:absolute group-data-[state=collapsed]:w-px group-data-[state=collapsed]:h-px group-data-[state=collapsed]:whitespace-nowrap group-data-[state=collapsed]:[clip-path:inset(50%)]">Favourites</span></a></li>
          <li><a class="flex items-center gap-3 min-w-0 min-h-11 px-2.5 py-2 rounded-[1.4rem] text-[0.93rem] text-inherit no-underline whitespace-nowrap [&>svg]:w-5 [&>svg]:h-5 [&>svg]:flex-none [&>svg]:opacity-75 hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-tsb05-acc focus-visible:outline-offset-2 group-data-[state=collapsed]:justify-center group-data-[state=collapsed]:gap-0" href="#tsb-05-main">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 18V9m5 9V5m5 13v-7m5 7V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <span class="min-w-0 overflow-hidden text-ellipsis group-data-[state=collapsed]:absolute group-data-[state=collapsed]:w-px group-data-[state=collapsed]:h-px group-data-[state=collapsed]:whitespace-nowrap group-data-[state=collapsed]:[clip-path:inset(50%)]">Recently played</span></a></li>
        </ul>
      </nav>
    </div>

    <main class="flex-1 min-w-0 px-5 pt-6 pb-10 r46:px-9 r46:pt-10 r46:pb-12" id="tsb-05-main">
      <p class="m-0 mb-1 text-[0.72rem] tracking-[0.12em] uppercase text-tsb05-acc2">Now playing</p>
      <h2 class="m-0 mb-1 font-tsb05-display text-[clamp(1.35rem,3.4vw,1.9rem)] leading-[1.15]">Field Recordings, Vol. 2</h2>
      <p class="m-0 mb-5 text-[0.85rem] text-tsb05-mut">Basalt Ensemble &middot; 11 tracks &middot; 48 min</p>
      <ol class="list-none m-0 p-0 grid gap-px max-w-[34rem] rounded-[0.7rem] overflow-hidden bg-tsb05-line [&>li]:flex [&>li]:items-center [&>li]:gap-3 [&>li]:min-w-0 [&>li]:px-3.5 [&>li]:py-2.5 [&>li]:bg-tsb05-surf [&>li]:text-[0.9rem] [&>li>span]:text-[0.8rem] [&>li>span]:tabular-nums [&>li>span]:text-tsb05-mut [&>li>em]:ml-auto [&>li>em]:not-italic [&>li>em]:text-[0.82rem] [&>li>em]:tabular-nums [&>li>em]:text-tsb05-mut">
        <li><span>1</span> Low Tide <em>4:12</em></li>
        <li><span>2</span> Harbour Wall <em>3:48</em></li>
        <li><span>3</span> Kestrel <em>5:31</em></li>
        <li><span>4</span> Slack Water <em>4:02</em></li>
        <li><span>5</span> Two Bells <em>3:19</em></li>
        <li><span>6</span> Ebb <em>6:07</em></li>
      </ol>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsb05-bg: #f4f5f3;
  --color-tsb05-bg: oklch(96% 0.004 130);
  --color-tsb05-surf: #ffffff;
  --color-tsb05-surf: oklch(100% 0 0);
  --color-tsb05-surf2: #e9ebe6;
  --color-tsb05-surf2: oklch(93% 0.008 130);
  --color-tsb05-rail: #16181a;
  --color-tsb05-rail: oklch(20% 0.005 250);
  --color-tsb05-line: #d6d9d3;
  --color-tsb05-line: oklch(87% 0.008 130);
  --color-tsb05-ink: #14161a;
  --color-tsb05-ink: oklch(19% 0.008 250);
  --color-tsb05-mut: #5d6268;
  --color-tsb05-mut: oklch(48% 0.012 250);
  --color-tsb05-onrail: #e8ebe4;
  --color-tsb05-onrail: oklch(93% 0.012 130);
  --color-tsb05-acc: #4f7a15;
  --color-tsb05-acc: oklch(56% 0.16 128);
  --color-tsb05-acc2: #4f7a15;
  --color-tsb05-acc2: oklch(50% 0.16 128);
  --color-tsb05-onacc: #10140a;
  --color-tsb05-onacc: oklch(98% 0.01 130);
  --font-tsb05-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-tsb05-display: 'Nunito', ui-rounded, system-ui, sans-serif;
  --breakpoint-r30: 30rem;
  --breakpoint-r46: 46rem;
}
/* Root rule: the full-bleed contract, plus the two rail widths. These are geometry read
   by w-[var(--tsb05-w-open)] and its collapsed twin, not a colour scale, so they stay
   plain custom properties rather than becoming @theme utilities. */

.tsb-05 {
  width: 100%;
  min-height: 100svh;
  --tsb05-w-open: 15rem;
  --tsb05-w-rail: 4.25rem;
}

.tsb-05 *,
.tsb-05 *::before,
.tsb-05 *::after {
  box-sizing: border-box;
}
/* Token flip for the pure-CSS theme toggle, plus the two mandatory mirror blocks.
   In the dark palette the lime accent carries dark ink, so --color-tsb05-onacc flips too. */

.tsb-05:has(.tsb-05-theme-input:checked) {
  --color-tsb05-bg: #050506;
  --color-tsb05-surf: #0e0f11;
  --color-tsb05-surf2: #16181b;
  --color-tsb05-rail: #0a0b0c;
  --color-tsb05-line: #23262a;
  --color-tsb05-ink: #eef0ec;
  --color-tsb05-mut: #949a9f;
  --color-tsb05-onrail: #eef0ec;
  --color-tsb05-acc: #b6f24a;
  --color-tsb05-acc: oklch(90% 0.22 128);
  --color-tsb05-acc2: #b6f24a;
  --color-tsb05-onacc: #10140a;
}

@media (prefers-color-scheme: dark) {
  .tsb-05 {
    --color-tsb05-bg: #050506;
    --color-tsb05-surf: #0e0f11;
    --color-tsb05-surf2: #16181b;
    --color-tsb05-rail: #0a0b0c;
    --color-tsb05-line: #23262a;
    --color-tsb05-ink: #eef0ec;
    --color-tsb05-mut: #949a9f;
    --color-tsb05-onrail: #eef0ec;
    --color-tsb05-acc: #b6f24a;
    --color-tsb05-acc: oklch(90% 0.22 128);
    --color-tsb05-acc2: #b6f24a;
    --color-tsb05-onacc: #10140a;
  }

  .tsb-05:has(.tsb-05-theme-input:checked) {
    --color-tsb05-bg: #f4f5f3;
    --color-tsb05-surf: #ffffff;
    --color-tsb05-surf2: #e9ebe6;
    --color-tsb05-rail: #16181a;
    --color-tsb05-line: #d6d9d3;
    --color-tsb05-ink: #14161a;
    --color-tsb05-mut: #5d6268;
    --color-tsb05-onrail: #e8ebe4;
    --color-tsb05-acc: #4f7a15;
    --color-tsb05-acc: oklch(56% 0.16 128);
    --color-tsb05-acc2: #4f7a15;
    --color-tsb05-onacc: #f7fbef;
  }
}

@media (prefers-color-scheme: light) {
  .tsb-05:has(.tsb-05-theme-input:checked) {
    --color-tsb05-bg: #050506;
    --color-tsb05-surf: #0e0f11;
    --color-tsb05-surf2: #16181b;
    --color-tsb05-rail: #0a0b0c;
    --color-tsb05-line: #23262a;
    --color-tsb05-ink: #eef0ec;
    --color-tsb05-mut: #949a9f;
    --color-tsb05-onrail: #eef0ec;
    --color-tsb05-acc: #b6f24a;
    --color-tsb05-acc: oklch(90% 0.22 128);
    --color-tsb05-acc2: #b6f24a;
    --color-tsb05-onacc: #10140a;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tsb-05').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var app = root.querySelector('.group'),
        btn = root.querySelector('#tsb-05-toggle'),
        label = btn.querySelector('[data-tsb-05-label]');
    function toggle() {
      var next = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', String(next));
      app.setAttribute('data-state', next ? 'expanded' : 'collapsed');
      label.textContent = next ? 'Collapse sidebar' : 'Expand sidebar';
    }
    btn.addEventListener('click', toggle);
    root.__tsbCleanup = function () { btn.removeEventListener('click', toggle); };
  });
})();
```

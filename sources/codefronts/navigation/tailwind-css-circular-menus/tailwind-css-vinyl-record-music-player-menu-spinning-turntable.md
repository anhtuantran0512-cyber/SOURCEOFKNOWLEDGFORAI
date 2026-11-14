---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-vinyl-record-music-player-menu-spinning-turntable/"
title: "Tailwind CSS Vinyl Record Music Player Menu (Spinning Turntable)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A turntable you browse with: grooves are one repeating-radial-gradient, a conic sheen sweeps across them, and picking a track drops the tonearm and starts…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Vinyl Record Music Player Menu (Spinning Turntable)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-vinyl-record-music-player-menu-spinning-turntable/

A turntable you browse with: grooves are one repeating-radial-gradient, a conic sheen sweeps across them, and picking a track drops the tonearm and starts the spin. Play state is a single data-playing attribute; the record resumes from its exact groove because group-data-playing/deck:[animation-play-state:running] toggles play-state instead of the animation.
## HTML
```html
<section class="tcm-21 w-full min-h-svh grid place-items-center bg-tcm21-bg bg-[radial-gradient(55%_50%_at_30%_40%,var(--color-tcm21-glow),transparent_72%)] px-4 py-14 font-tcm21-sans text-tcm21-ink antialiased sm:px-5" aria-label="Vinyl record music player menu demo">
  <div class="grid w-full justify-items-center gap-7">
    <div id="tcm-21-deck" class="group/deck relative grid w-full max-w-[44rem] items-center gap-7 rounded-[1.75rem] bg-linear-to-br from-tcm21-wood to-tcm21-wood2 p-5 shadow-tcm21-deck ring-1 ring-tcm21-line sm:grid-cols-[auto_1fr] sm:p-7">
      <div class="relative mx-auto size-[min(17rem,78vw)]">
        <div aria-hidden="true" class="absolute inset-0 rounded-full bg-tcm21-platter shadow-tcm21-platter">
          <div class="absolute inset-[3.5%] grid place-items-center rounded-full bg-[conic-gradient(from_40deg,transparent_0_8%,oklch(1_0_0/0.07)_10%,transparent_13%_48%,oklch(1_0_0/0.07)_51%,transparent_54%),repeating-radial-gradient(circle,#1d1d1f_0_2px,#141415_2px_4px)] animate-tcm21-spin [animation-play-state:paused] group-data-playing/deck:[animation-play-state:running] motion-reduce:animate-none">
            <div class="grid size-[42%] place-content-center justify-items-center rounded-full bg-linear-to-br from-tcm21-label to-tcm21-label2 text-center text-white shadow-[inset_0_0_0_6px_oklch(0_0_0/0.12)]">
              <b class="text-[clamp(10px,3vw,13px)] tracking-[0.2em]">MIDNIGHT</b><i class="text-[9px] tracking-[0.3em] not-italic opacity-80">SIDE A · 33⅓</i>
            </div>
            <span class="absolute size-2.5 rounded-full bg-tcm21-pin shadow-[inset_0_1px_2px_oklch(0_0_0/0.6)]"></span>
          </div>
        </div>
        <div aria-hidden="true" class="absolute top-[4%] right-[-3%] h-[72%] w-4 origin-[50%_1.4rem] rotate-[-26deg] transition-[rotate] duration-800 ease-[cubic-bezier(.4,0,.3,1)] group-data-playing/deck:rotate-0 drop-shadow-[0_8px_10px_oklch(0_0_0/0.45)] motion-reduce:transition-none">
          <span class="absolute top-0 left-0 size-7 -translate-x-1.5 rounded-full bg-[radial-gradient(circle_at_35%_30%,#f4f4f5,#a1a1aa)] ring-2 ring-black/10"></span>
          <span class="absolute top-5 left-[6px] h-[78%] w-1 rounded-full bg-linear-to-r from-zinc-200 to-zinc-400"></span>
          <span class="absolute bottom-0 left-0 h-6 w-4 rounded-[3px] bg-linear-to-b from-tcm21-label to-tcm21-label2"></span>
        </div>
      </div>
      <div class="grid gap-4">
        <header class="flex items-end justify-between gap-3">
          <div><p class="font-tcm21-mono text-[11px] tracking-[0.16em] text-tcm21-mut uppercase">LP · 2026</p><h2 class="font-tcm21-serif text-[1.65rem] leading-none">Midnight</h2></div>
          <button type="button" data-play aria-pressed="false" aria-label="Play" class="grid size-12 cursor-pointer place-items-center rounded-full bg-linear-to-br from-tcm21-label to-tcm21-label2 text-white shadow-tcm21-btn transition-[scale] duration-200 hover:scale-105 active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm21-ring">
            <svg viewBox="0 0 24 24" class="size-5 group-data-playing/deck:hidden" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13l10.5-6.5z"/></svg>
            <svg viewBox="0 0 24 24" class="hidden size-5 group-data-playing/deck:block" fill="currentColor" aria-hidden="true"><path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z"/></svg>
          </button>
        </header>
        <fieldset><legend class="sr-only">Choose a track</legend>
          <ol class="grid gap-1">
          <li>
            <input type="radio" name="tcm-21-track" id="tcm-21-t0" value="Neon Rain" class="peer sr-only">
            <label for="tcm-21-t0" class="group/t flex min-h-12 cursor-pointer items-center gap-3 rounded-xl px-3.5 text-[14px] font-semibold ring-1 ring-transparent transition-[background-color,box-shadow] duration-200 hover:bg-tcm21-row peer-checked:bg-tcm21-label/15 peer-checked:ring-tcm21-label/50 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm21-ring">
              <span class="w-5 font-tcm21-mono text-[11px] text-tcm21-mut tabular-nums">01</span>
              <span class="flex-1">Neon Rain</span>
              <span aria-hidden="true" class="hidden items-end gap-[2px] [.peer:checked~*_&]:flex"><i class="h-2 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq motion-reduce:animate-none"></i><i class="h-3 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq [animation-delay:-.4s] motion-reduce:animate-none"></i><i class="h-2.5 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq [animation-delay:-.2s] motion-reduce:animate-none"></i></span>
              <span class="font-tcm21-mono text-[11.5px] text-tcm21-mut tabular-nums">3:42</span>
            </label>
          </li>
          <li>
            <input type="radio" name="tcm-21-track" id="tcm-21-t1" value="Slow Motion" class="peer sr-only">
            <label for="tcm-21-t1" class="group/t flex min-h-12 cursor-pointer items-center gap-3 rounded-xl px-3.5 text-[14px] font-semibold ring-1 ring-transparent transition-[background-color,box-shadow] duration-200 hover:bg-tcm21-row peer-checked:bg-tcm21-label/15 peer-checked:ring-tcm21-label/50 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm21-ring">
              <span class="w-5 font-tcm21-mono text-[11px] text-tcm21-mut tabular-nums">02</span>
              <span class="flex-1">Slow Motion</span>
              <span aria-hidden="true" class="hidden items-end gap-[2px] [.peer:checked~*_&]:flex"><i class="h-2 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq motion-reduce:animate-none"></i><i class="h-3 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq [animation-delay:-.4s] motion-reduce:animate-none"></i><i class="h-2.5 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq [animation-delay:-.2s] motion-reduce:animate-none"></i></span>
              <span class="font-tcm21-mono text-[11.5px] text-tcm21-mut tabular-nums">4:18</span>
            </label>
          </li>
          <li>
            <input type="radio" name="tcm-21-track" id="tcm-21-t2" value="Afterglow" class="peer sr-only">
            <label for="tcm-21-t2" class="group/t flex min-h-12 cursor-pointer items-center gap-3 rounded-xl px-3.5 text-[14px] font-semibold ring-1 ring-transparent transition-[background-color,box-shadow] duration-200 hover:bg-tcm21-row peer-checked:bg-tcm21-label/15 peer-checked:ring-tcm21-label/50 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm21-ring">
              <span class="w-5 font-tcm21-mono text-[11px] text-tcm21-mut tabular-nums">03</span>
              <span class="flex-1">Afterglow</span>
              <span aria-hidden="true" class="hidden items-end gap-[2px] [.peer:checked~*_&]:flex"><i class="h-2 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq motion-reduce:animate-none"></i><i class="h-3 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq [animation-delay:-.4s] motion-reduce:animate-none"></i><i class="h-2.5 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq [animation-delay:-.2s] motion-reduce:animate-none"></i></span>
              <span class="font-tcm21-mono text-[11.5px] text-tcm21-mut tabular-nums">3:05</span>
            </label>
          </li>
          <li>
            <input type="radio" name="tcm-21-track" id="tcm-21-t3" value="Daybreak" class="peer sr-only">
            <label for="tcm-21-t3" class="group/t flex min-h-12 cursor-pointer items-center gap-3 rounded-xl px-3.5 text-[14px] font-semibold ring-1 ring-transparent transition-[background-color,box-shadow] duration-200 hover:bg-tcm21-row peer-checked:bg-tcm21-label/15 peer-checked:ring-tcm21-label/50 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm21-ring">
              <span class="w-5 font-tcm21-mono text-[11px] text-tcm21-mut tabular-nums">04</span>
              <span class="flex-1">Daybreak</span>
              <span aria-hidden="true" class="hidden items-end gap-[2px] [.peer:checked~*_&]:flex"><i class="h-2 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq motion-reduce:animate-none"></i><i class="h-3 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq [animation-delay:-.4s] motion-reduce:animate-none"></i><i class="h-2.5 w-[3px] rounded-full bg-tcm21-label animate-tcm21-eq [animation-delay:-.2s] motion-reduce:animate-none"></i></span>
              <span class="font-tcm21-mono text-[11.5px] text-tcm21-mut tabular-nums">5:01</span>
            </label>
          </li>
          </ol>
        </fieldset>
        <p data-now role="status" class="font-tcm21-mono text-[12px] text-tcm21-mut">Select a track to drop the needle</p>
      </div>
    </div>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm21-card px-3.5 py-2 text-center font-tcm21-mono text-[11.5px] text-tcm21-mut ring-1 ring-tcm21-line ">animate-tcm21-spin · group-data-playing/deck:[animation-play-state:running] · tonearm rotate</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm21-bg: #f6efe7;
  --color-tcm21-bg: oklch(0.955 0.013 71.3);
  --color-tcm21-glow: #fecdd380;
  --color-tcm21-glow: oklch(0.892 0.056 10 / 0.5);
  --color-tcm21-wood: #fbf5ee;
  --color-tcm21-wood: oklch(0.973 0.011 71.9);
  --color-tcm21-wood2: #f1e5d6;
  --color-tcm21-wood2: oklch(0.927 0.024 73.6);
  --color-tcm21-platter: #1f1f22;
  --color-tcm21-platter: oklch(0.241 0.006 286);
  --color-tcm21-pin: #e7e5e4;
  --color-tcm21-pin: oklch(0.923 0.003 48.7);
  --color-tcm21-row: #efe3d3;
  --color-tcm21-row: oklch(0.921 0.025 75.3);
  --color-tcm21-ink: #2a1d14;
  --color-tcm21-ink: oklch(0.244 0.026 55.8);
  --color-tcm21-mut: #6e5a4a;
  --color-tcm21-mut: oklch(0.483 0.036 60.5);
  --color-tcm21-line: #e6d6c3;
  --color-tcm21-line: oklch(0.884 0.031 72.1);
  --color-tcm21-label: #e11d48;
  --color-tcm21-label: oklch(0.586 0.222 17.6);
  --color-tcm21-label2: #9f1239;
  --color-tcm21-label2: oklch(0.455 0.171 13.7);
  --color-tcm21-ring: #be123c;
  --color-tcm21-ring: oklch(0.514 0.198 16.9);
  --color-tcm21-card: #fffaf4;
  --color-tcm21-card: oklch(0.987 0.01 72.7);
  --font-tcm21-sans: 'DM Sans', system-ui, sans-serif;
  --font-tcm21-serif: 'DM Serif Display', Georgia, serif;
  --font-tcm21-mono: 'DM Mono', ui-monospace, monospace;
  --shadow-tcm21-deck: 0 1px 0 oklch(1 0 0 / 0.5) inset, 0 34px 70px -30px oklch(0.3 0.06 50 / 0.6);
  --shadow-tcm21-platter: 0 18px 36px -12px oklch(0 0 0 / 0.6), inset 0 0 0 5px oklch(0.25 0 0);
  --shadow-tcm21-btn: 0 12px 26px -10px oklch(0.5 0.2 15 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.3);
  --animate-tcm21-spin: tcm21-spin 1.8s linear infinite;
  --animate-tcm21-eq: tcm21-eq 0.8s ease-in-out infinite alternate;

  @keyframes tcm21-spin {
    to {
      rotate: 360deg;
    }
  }

  @keyframes tcm21-eq {
    from {
      scale: 1 0.4;
    }

    to {
      scale: 1 1.3;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-21 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: listening room: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-21:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm21-bg: #120c09;
    --color-tcm21-bg: oklch(0.161 0.012 48.2);
    --color-tcm21-glow: #88133766;
    --color-tcm21-glow: oklch(0.41 0.15 10.3 / 0.4);
    --color-tcm21-wood: #2a1d15;
    --color-tcm21-wood: oklch(0.244 0.025 52.8);
    --color-tcm21-wood2: #1b130e;
    --color-tcm21-wood2: oklch(0.195 0.016 53.5);
    --color-tcm21-platter: #0b0b0c;
    --color-tcm21-platter: oklch(0.15 0.002 286.1);
    --color-tcm21-pin: #d6d3d1;
    --color-tcm21-pin: oklch(0.869 0.004 56.4);
    --color-tcm21-row: #33241a;
    --color-tcm21-row: oklch(0.275 0.029 54.9);
    --color-tcm21-ink: #f8ece0;
    --color-tcm21-ink: oklch(0.949 0.021 67.6);
    --color-tcm21-mut: #c2a995;
    --color-tcm21-mut: oklch(0.751 0.04 60.8);
    --color-tcm21-line: #3d2c20;
    --color-tcm21-line: oklch(0.309 0.032 56.4);
    --color-tcm21-label: #f43f5e;
    --color-tcm21-label: oklch(0.645 0.215 16.4);
    --color-tcm21-label2: #be123c;
    --color-tcm21-label2: oklch(0.514 0.198 16.9);
    --color-tcm21-ring: #fda4af;
    --color-tcm21-ring: oklch(0.81 0.106 11.6);
    --color-tcm21-card: #201610;
    --color-tcm21-card: oklch(0.211 0.02 52.3);
  }
}

.tcm-21[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm21-bg: #120c09;
  --color-tcm21-bg: oklch(0.161 0.012 48.2);
  --color-tcm21-glow: #88133766;
  --color-tcm21-glow: oklch(0.41 0.15 10.3 / 0.4);
  --color-tcm21-wood: #2a1d15;
  --color-tcm21-wood: oklch(0.244 0.025 52.8);
  --color-tcm21-wood2: #1b130e;
  --color-tcm21-wood2: oklch(0.195 0.016 53.5);
  --color-tcm21-platter: #0b0b0c;
  --color-tcm21-platter: oklch(0.15 0.002 286.1);
  --color-tcm21-pin: #d6d3d1;
  --color-tcm21-pin: oklch(0.869 0.004 56.4);
  --color-tcm21-row: #33241a;
  --color-tcm21-row: oklch(0.275 0.029 54.9);
  --color-tcm21-ink: #f8ece0;
  --color-tcm21-ink: oklch(0.949 0.021 67.6);
  --color-tcm21-mut: #c2a995;
  --color-tcm21-mut: oklch(0.751 0.04 60.8);
  --color-tcm21-line: #3d2c20;
  --color-tcm21-line: oklch(0.309 0.032 56.4);
  --color-tcm21-label: #f43f5e;
  --color-tcm21-label: oklch(0.645 0.215 16.4);
  --color-tcm21-label2: #be123c;
  --color-tcm21-label2: oklch(0.514 0.198 16.9);
  --color-tcm21-ring: #fda4af;
  --color-tcm21-ring: oklch(0.81 0.106 11.6);
  --color-tcm21-card: #201610;
  --color-tcm21-card: oklch(0.211 0.02 52.3);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-21-deck');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const btn = root.querySelector('[data-play]'), now = root.querySelector('[data-now]');
  const first = root.querySelector('input[name="tcm-21-track"]');
  const set = (on) => {
    root.toggleAttribute('data-playing', on);
    btn.setAttribute('aria-pressed', String(on));
    btn.setAttribute('aria-label', on ? 'Pause' : 'Play');
    const t = root.querySelector('input[name="tcm-21-track"]:checked');
    now.textContent = t ? (on ? '▶ Now playing — ' : '❚❚ Paused — ') + t.value : 'Select a track to drop the needle';
  };
  root.addEventListener('change', (e) => { if (e.target.name === 'tcm-21-track') set(true); });
  btn.addEventListener('click', () => {
    if (!root.querySelector('input[name="tcm-21-track"]:checked')) first.checked = true;
    set(!root.hasAttribute('data-playing'));
  });
})();
```

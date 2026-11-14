---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-grain-paint-cost-byte-size-measured/"
title: "Tailwind Grain Paint Cost and Byte Size Measured Live"
section: "design-styles"
category: "tailwind-css-grain-texture"
category_name: "Tailwind CSS Grain Texture"
description: "Everyone repeats that SVG filters are expensive."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Grain Paint Cost and Byte Size Measured Live
Source: https://codefronts.com/design-styles/tailwind-css-grain-texture/tailwind-grain-paint-cost-byte-size-measured/

Everyone repeats that SVG filters are expensive. Nobody says how expensive. This demo measures it live in your own browser: median frame time for four surfaces — no grain, cached data URI, live 5-octave filter, six blended layers — plus the real byte size of each texture token, read out of computed styles rather than estimated. The only demo in the collection with JavaScript, and it exists because the numbers have to be yours, not mine.
## HTML
```html
<section class="gtw-06 relative block w-full min-h-svh bg-gtw06-bg text-gtw06-ink" aria-labelledby="gtw-06-title">
  <svg class="absolute w-0 h-0 overflow-hidden" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="gtw-06-oct5" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="5" seed="17" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
  </svg>

  <div class="absolute top-[clamp(1rem,3vw,1.75rem)] right-[clamp(0.85rem,3vw,1.75rem)] z-40">
    <input type="checkbox" id="gtw-06-theme" class="gtw-06-theme peer sr-only">
    <label for="gtw-06-theme" class="grid place-items-center w-11 h-11 rounded-full border border-gtw06-line bg-gtw06-surf text-gtw06-ink cursor-pointer transition-colors duration-200 hover:border-gtw06-acc peer-focus-visible:outline-2 peer-focus-visible:outline-gtw06-acc peer-focus-visible:outline-offset-[3px]">
      <svg viewBox="0 0 24 24" class="w-5 h-5" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <main class="w-[min(70rem,calc(100%-clamp(1.5rem,5vw,4rem)))] mx-auto pt-[clamp(3rem,8vw,5.5rem)] pb-[clamp(2.5rem,6vw,4rem)] grid gap-[clamp(1.8rem,4.5vw,2.8rem)]">
    <header class="max-w-[46rem] grid gap-3">
      <p class="m-0 font-gtw06-mono text-[0.72rem] font-medium tracking-[0.18em] uppercase text-gtw06-acc">Measured, not guessed · 06</p>
      <h1 id="gtw-06-title" class="m-0 font-gtw06-display text-[clamp(2rem,5.2vw,3.3rem)] font-semibold leading-[1.04] tracking-[-0.035em] text-balance">What grain actually costs on this machine</h1>
      <p class="m-0 max-w-[40rem] text-gtw06-mut text-[clamp(0.95rem,1.9vw,1.08rem)] text-pretty">Four surfaces, one animated property, median frame time across a real sample. Then the byte size of each texture definition, read out of the computed styles rather than estimated.</p>
    </header>

    <section class="grid gap-4 p-[clamp(1.1rem,3vw,1.8rem)] rounded-2xl border border-gtw06-line bg-gtw06-surf" aria-labelledby="gtw-06-h-paint">
      <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-[0.6rem] pb-[0.7rem] border-b border-gtw06-line">
        <h2 id="gtw-06-h-paint" class="m-0 font-gtw06-display text-[clamp(1.1rem,2.6vw,1.35rem)] font-semibold leading-tight">Paint cost</h2>
        <div class="flex flex-wrap items-center gap-[0.8rem]">
          <p class="m-0 font-gtw06-mono text-[0.8rem] leading-none text-gtw06-mut" role="status" data-gtw-06-status>Ready</p>
          <button type="button" data-gtw-06-run data-gtw06-frames="48" class="inline-flex items-center min-h-11 px-[1.1rem] rounded-[10px] border-0 bg-gtw06-acc text-gtw06-onacc font-gtw06-display text-[0.85rem] font-semibold leading-none cursor-pointer transition-[filter] duration-200 hover:brightness-[1.07] disabled:opacity-55 disabled:cursor-progress focus-visible:outline-2 focus-visible:outline-gtw06-acc focus-visible:outline-offset-[3px]">Run measurement</button>
        </div>
      </div>

      <ul class="list-none m-0 p-0 grid gap-[0.55rem]" data-gtw-06-rows>
        <li class="grid items-center gap-x-[0.85rem] gap-y-2 grid-cols-[44px_minmax(0,1fr)_auto] min-[46rem]:grid-cols-[52px_minmax(9rem,15rem)_minmax(0,1fr)_5.5rem]" data-gtw06-row="control">
          <span data-gtw-06-stage="control" class="relative isolate h-11 rounded-lg overflow-hidden bg-[linear-gradient(135deg,var(--color-gtw06-acc),color-mix(in_oklab,var(--color-gtw06-acc)_25%,var(--color-gtw06-surf)))]"></span>
          <span class="col-span-2 min-[46rem]:col-auto text-[0.9rem]">No grain <em class="block not-italic text-[0.76rem] text-gtw06-mut">control</em></span>
          <span class="relative block col-span-2 min-[46rem]:col-auto h-[10px] rounded-full overflow-hidden bg-[color-mix(in_oklab,var(--color-gtw06-ink)_10%,transparent)]"><span data-gtw-06-fill style="--gtw06-pct: 0" class="absolute inset-y-0 left-0 w-[calc(var(--gtw06-pct,0)*1%)] rounded-full bg-gtw06-acc transition-[width] duration-[420ms] ease-[cubic-bezier(0.22,1,0.36,1)] motion-reduce:transition-none"></span></span>
          <span data-gtw-06-ms class="justify-self-end font-gtw06-mono text-[0.92rem] font-medium leading-none tabular-nums">—</span>
        </li>
        <li class="grid items-center gap-x-[0.85rem] gap-y-2 grid-cols-[44px_minmax(0,1fr)_auto] min-[46rem]:grid-cols-[52px_minmax(9rem,15rem)_minmax(0,1fr)_5.5rem]" data-gtw06-row="datauri">
          <span data-gtw-06-stage="datauri" class="relative isolate h-11 rounded-lg overflow-hidden bg-[linear-gradient(135deg,var(--color-gtw06-acc),color-mix(in_oklab,var(--color-gtw06-acc)_25%,var(--color-gtw06-surf)))] after:content-[''] after:absolute after:-inset-[2px] after:bg-[image:var(--gtw06-noise-fine)] after:opacity-50 after:mix-blend-overlay"></span>
          <span class="col-span-2 min-[46rem]:col-auto text-[0.9rem]">Data URI grain <em class="block not-italic text-[0.76rem] text-gtw06-mut">3 octaves, cached</em></span>
          <span class="relative block col-span-2 min-[46rem]:col-auto h-[10px] rounded-full overflow-hidden bg-[color-mix(in_oklab,var(--color-gtw06-ink)_10%,transparent)]"><span data-gtw-06-fill style="--gtw06-pct: 0" class="absolute inset-y-0 left-0 w-[calc(var(--gtw06-pct,0)*1%)] rounded-full bg-gtw06-acc transition-[width] duration-[420ms] ease-[cubic-bezier(0.22,1,0.36,1)] motion-reduce:transition-none"></span></span>
          <span data-gtw-06-ms class="justify-self-end font-gtw06-mono text-[0.92rem] font-medium leading-none tabular-nums">—</span>
        </li>
        <li class="grid items-center gap-x-[0.85rem] gap-y-2 grid-cols-[44px_minmax(0,1fr)_auto] min-[46rem]:grid-cols-[52px_minmax(9rem,15rem)_minmax(0,1fr)_5.5rem]" data-gtw06-row="filter">
          <span data-gtw-06-stage="filter" class="relative isolate h-11 rounded-lg overflow-hidden bg-[linear-gradient(135deg,var(--color-gtw06-acc),color-mix(in_oklab,var(--color-gtw06-acc)_25%,var(--color-gtw06-surf)))] after:content-[''] after:absolute after:-inset-[2px] after:[filter:url(#gtw-06-oct5)] after:opacity-50 after:mix-blend-overlay"></span>
          <span class="col-span-2 min-[46rem]:col-auto text-[0.9rem]">Live SVG filter <em class="block not-italic text-[0.76rem] text-gtw06-mut">5 octaves, re-evaluated</em></span>
          <span class="relative block col-span-2 min-[46rem]:col-auto h-[10px] rounded-full overflow-hidden bg-[color-mix(in_oklab,var(--color-gtw06-ink)_10%,transparent)]"><span data-gtw-06-fill style="--gtw06-pct: 0" class="absolute inset-y-0 left-0 w-[calc(var(--gtw06-pct,0)*1%)] rounded-full bg-gtw06-acc transition-[width] duration-[420ms] ease-[cubic-bezier(0.22,1,0.36,1)] motion-reduce:transition-none"></span></span>
          <span data-gtw-06-ms class="justify-self-end font-gtw06-mono text-[0.92rem] font-medium leading-none tabular-nums">—</span>
        </li>
        <li class="grid items-center gap-x-[0.85rem] gap-y-2 grid-cols-[44px_minmax(0,1fr)_auto] min-[46rem]:grid-cols-[52px_minmax(9rem,15rem)_minmax(0,1fr)_5.5rem]" data-gtw06-row="stack">
          <span data-gtw-06-stage="stack" class="relative isolate h-11 rounded-lg overflow-hidden bg-[linear-gradient(135deg,var(--color-gtw06-acc),color-mix(in_oklab,var(--color-gtw06-acc)_25%,var(--color-gtw06-surf)))] after:content-[''] after:absolute after:-inset-[2px] after:bg-[image:var(--gtw06-noise-fine),var(--gtw06-noise-coarse),var(--gtw06-noise-fine)] after:opacity-45 after:mix-blend-overlay before:content-[''] before:absolute before:-inset-[2px] before:bg-[image:var(--gtw06-noise-coarse),var(--gtw06-noise-fine),var(--gtw06-noise-coarse)] before:opacity-45 before:mix-blend-soft-light"></span>
          <span class="col-span-2 min-[46rem]:col-auto text-[0.9rem]">Six blended layers <em class="block not-italic text-[0.76rem] text-gtw06-mut">the expensive case</em></span>
          <span class="relative block col-span-2 min-[46rem]:col-auto h-[10px] rounded-full overflow-hidden bg-[color-mix(in_oklab,var(--color-gtw06-ink)_10%,transparent)]"><span data-gtw-06-fill style="--gtw06-pct: 0" class="absolute inset-y-0 left-0 w-[calc(var(--gtw06-pct,0)*1%)] rounded-full bg-gtw06-acc transition-[width] duration-[420ms] ease-[cubic-bezier(0.22,1,0.36,1)] motion-reduce:transition-none"></span></span>
          <span data-gtw-06-ms class="justify-self-end font-gtw06-mono text-[0.92rem] font-medium leading-none tabular-nums">—</span>
        </li>
      </ul>
      <p class="m-0 text-gtw06-mut text-[0.83rem] text-pretty">Median milliseconds per frame while a sub-pixel translate forces a repaint. Lower is better. Close devtools and keep the tab focused for a number worth quoting.</p>
    </section>

    <section class="grid gap-4 p-[clamp(1.1rem,3vw,1.8rem)] rounded-2xl border border-gtw06-line bg-gtw06-surf" aria-labelledby="gtw-06-h-bytes">
      <div class="flex flex-wrap items-center justify-between gap-x-4 gap-y-[0.6rem] pb-[0.7rem] border-b border-gtw06-line">
        <h2 id="gtw-06-h-bytes" class="m-0 font-gtw06-display text-[clamp(1.1rem,2.6vw,1.35rem)] font-semibold leading-tight">Byte size</h2>
        <p class="m-0 text-gtw06-mut text-[0.85rem]">Read from computed styles, percent-encoding included.</p>
      </div>
      <dl class="m-0 grid gap-[0.6rem] grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))]" data-gtw-06-bytes>
        <div class="grid gap-[0.2rem] px-[0.9rem] py-[0.8rem] rounded-xl border border-gtw06-line bg-[color-mix(in_oklab,var(--color-gtw06-acc)_7%,transparent)]"><dt class="m-0 text-[0.78rem] text-gtw06-mut">Fine grain token</dt><dd data-gtw-06-byte="fine" class="m-0 font-gtw06-mono text-[1.05rem] font-semibold leading-tight tabular-nums">—</dd></div>
        <div class="grid gap-[0.2rem] px-[0.9rem] py-[0.8rem] rounded-xl border border-gtw06-line bg-[color-mix(in_oklab,var(--color-gtw06-acc)_7%,transparent)]"><dt class="m-0 text-[0.78rem] text-gtw06-mut">Coarse grain token</dt><dd data-gtw-06-byte="coarse" class="m-0 font-gtw06-mono text-[1.05rem] font-semibold leading-tight tabular-nums">—</dd></div>
        <div class="grid gap-[0.2rem] px-[0.9rem] py-[0.8rem] rounded-xl border border-gtw06-line bg-[color-mix(in_oklab,var(--color-gtw06-acc)_7%,transparent)]"><dt class="m-0 text-[0.78rem] text-gtw06-mut">Both, gzip-ish estimate</dt><dd data-gtw-06-byte="gz" class="m-0 font-gtw06-mono text-[1.05rem] font-semibold leading-tight tabular-nums">—</dd></div>
        <div class="grid gap-[0.2rem] px-[0.9rem] py-[0.8rem] rounded-xl border border-gtw06-line bg-[color-mix(in_oklab,var(--color-gtw06-acc)_7%,transparent)]"><dt class="m-0 text-[0.78rem] text-gtw06-mut">Typical seamless PNG</dt><dd class="m-0 font-gtw06-mono text-[1.05rem] font-semibold leading-tight tabular-nums">148 KB · 1 request</dd></div>
      </dl>
    </section>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-gtw06-bg: #131313;
  --color-gtw06-bg: oklch(0.2 0 0);
  --color-gtw06-surf: #1c1c1c;
  --color-gtw06-surf: oklch(0.25 0 0);
  --color-gtw06-line: #2e2e2e;
  --color-gtw06-line: oklch(0.33 0 0);
  --color-gtw06-ink: #f3f1ee;
  --color-gtw06-ink: oklch(0.96 0.005 80);
  --color-gtw06-mut: #9c968e;
  --color-gtw06-mut: oklch(0.71 0.01 80);
  --color-gtw06-acc: #fbbf24;
  --color-gtw06-acc: oklch(0.83 0.15 80);
  --color-gtw06-onacc: #1c1400;
  --color-gtw06-onacc: oklch(0.22 0.04 85);
  --font-gtw06-display: 'Space Grotesk', 'Inter Tight', ui-sans-serif, system-ui, sans-serif;
  --font-gtw06-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}

.gtw-06 {
  width: 100%;
  min-height: 100svh;
  --gtw06-noise-fine: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='150' height='150'%3E%3Cfilter id='gtw06a'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='150' height='150' filter='url(%23gtw06a)' opacity='0.6'/%3E%3C/svg%3E");
  --gtw06-noise-coarse: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='gtw06b'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.28' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='220' height='220' filter='url(%23gtw06b)' opacity='0.5'/%3E%3C/svg%3E");
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.55;
}

.gtw-06:has(.gtw-06-theme:checked) {
  --color-gtw06-bg: #f4f2ef;
  --color-gtw06-bg: oklch(0.96 0.005 80);
  --color-gtw06-surf: #ffffff;
  --color-gtw06-surf: oklch(1 0 0);
  --color-gtw06-line: #dedad4;
  --color-gtw06-line: oklch(0.89 0.008 80);
  --color-gtw06-ink: #131313;
  --color-gtw06-ink: oklch(0.2 0 0);
  --color-gtw06-mut: #625d55;
  --color-gtw06-mut: oklch(0.48 0.01 80);
  --color-gtw06-acc: #b45309;
  --color-gtw06-acc: oklch(0.52 0.14 62);
  --color-gtw06-onacc: #fffbeb;
  --color-gtw06-onacc: oklch(0.99 0.02 90);
}

@media (prefers-color-scheme: light) {
  .gtw-06 {
    --color-gtw06-bg: #f4f2ef;
    --color-gtw06-bg: oklch(0.96 0.005 80);
    --color-gtw06-surf: #ffffff;
    --color-gtw06-surf: oklch(1 0 0);
    --color-gtw06-line: #dedad4;
    --color-gtw06-line: oklch(0.89 0.008 80);
    --color-gtw06-ink: #131313;
    --color-gtw06-ink: oklch(0.2 0 0);
    --color-gtw06-mut: #625d55;
    --color-gtw06-mut: oklch(0.48 0.01 80);
    --color-gtw06-acc: #b45309;
    --color-gtw06-acc: oklch(0.52 0.14 62);
    --color-gtw06-onacc: #fffbeb;
    --color-gtw06-onacc: oklch(0.99 0.02 90);
  }

  .gtw-06:has(.gtw-06-theme:checked) {
    --color-gtw06-bg: #131313;
    --color-gtw06-bg: oklch(0.2 0 0);
    --color-gtw06-surf: #1c1c1c;
    --color-gtw06-surf: oklch(0.25 0 0);
    --color-gtw06-line: #2e2e2e;
    --color-gtw06-line: oklch(0.33 0 0);
    --color-gtw06-ink: #f3f1ee;
    --color-gtw06-ink: oklch(0.96 0.005 80);
    --color-gtw06-mut: #9c968e;
    --color-gtw06-mut: oklch(0.71 0.01 80);
    --color-gtw06-acc: #fbbf24;
    --color-gtw06-acc: oklch(0.83 0.15 80);
    --color-gtw06-onacc: #1c1400;
    --color-gtw06-onacc: oklch(0.22 0.04 85);
  }
}

@media (prefers-color-scheme: dark) {
  .gtw-06:has(.gtw-06-theme:checked) {
    --color-gtw06-bg: #f4f2ef;
    --color-gtw06-bg: oklch(0.96 0.005 80);
    --color-gtw06-surf: #ffffff;
    --color-gtw06-surf: oklch(1 0 0);
    --color-gtw06-line: #dedad4;
    --color-gtw06-line: oklch(0.89 0.008 80);
    --color-gtw06-ink: #131313;
    --color-gtw06-ink: oklch(0.2 0 0);
    --color-gtw06-mut: #625d55;
    --color-gtw06-mut: oklch(0.48 0.01 80);
    --color-gtw06-acc: #b45309;
    --color-gtw06-acc: oklch(0.52 0.14 62);
    --color-gtw06-onacc: #fffbeb;
    --color-gtw06-onacc: oklch(0.99 0.02 90);
  }
}
```

## JavaScript
```js
const root = document.querySelector('.gtw-06');
const runBtn = root.querySelector('[data-gtw-06-run]');
const statusEl = root.querySelector('[data-gtw-06-status]');
const rows = Array.from(root.querySelectorAll('[data-gtw06-row]'));
const frames = Number(runBtn.dataset.gtw06Frames || 48);
let rafId = 0;
let cancelled = false;

function bytes(str) {
  return new TextEncoder().encode(str).length;
}

function fmt(n) {
  return n >= 1024 ? (n / 1024).toFixed(1) + ' KB' : n + ' B';
}

function reportBytes() {
  const cs = getComputedStyle(root);
  const fine = cs.getPropertyValue('--gtw06-noise-fine').trim();
  const coarse = cs.getPropertyValue('--gtw06-noise-coarse').trim();
  const bf = bytes(fine);
  const bc = bytes(coarse);
  const set = (key, val) => {
    const el = root.querySelector('[data-gtw-06-byte="' + key + '"]');
    if (el) el.textContent = val;
  };
  set('fine', fmt(bf));
  set('coarse', fmt(bc));
  set('gz', '~' + fmt(Math.round((bf + bc) * 0.42)) + ' over the wire');
}

function median(list) {
  const s = list.slice().sort((a, b) => a - b);
  const mid = s.length >> 1;
  return s.length % 2 ? s[mid] : (s[mid - 1] + s[mid]) / 2;
}

function measure(stage) {
  return new Promise((resolve) => {
    const deltas = [];
    let last = performance.now();
    let i = 0;
    stage.style.willChange = 'transform';
    const tick = (now) => {
      if (cancelled) { stage.style.willChange = ''; resolve(0); return; }
      deltas.push(now - last);
      last = now;
      stage.style.transform = 'translate3d(' + ((i % 2) * 0.5) + 'px,0,0)';
      i += 1;
      if (i < frames) { rafId = requestAnimationFrame(tick); }
      else {
        stage.style.willChange = '';
        stage.style.transform = '';
        resolve(median(deltas.slice(4)));
      }
    };
    rafId = requestAnimationFrame(tick);
  });
}

function paintRow(r, peak) {
  const msEl = r.row.querySelector('[data-gtw-06-ms]');
  const fill = r.row.querySelector('[data-gtw-06-fill]');
  if (msEl) msEl.textContent = r.ms.toFixed(2) + ' ms';
  if (fill) fill.style.setProperty('--gtw06-pct', String(Math.max(4, Math.round((r.ms / peak) * 100))));
}

async function run() {
  runBtn.disabled = true;
  const results = [];
  for (const row of rows) {
    if (cancelled) break;
    const key = row.dataset.gtw06Row;
    statusEl.textContent = 'Measuring ' + key + '…';
    const stage = row.querySelector('[data-gtw-06-stage]');
    const ms = await measure(stage);
    results.push({ row: row, ms: ms });
  }
  if (cancelled) return;
  const peak = Math.max.apply(null, results.map((r) => r.ms)) || 1;
  results.forEach((r) => paintRow(r, peak));
  statusEl.textContent = 'Median of ' + frames + ' frames · run again for variance';
  runBtn.disabled = false;
}

reportBytes();
runBtn.addEventListener('click', run);

root.__gtwCleanup = () => {
  cancelled = true;
  cancelAnimationFrame(rafId);
  runBtn.removeEventListener('click', run);
};
```

---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-css-pagination-with-go-to-page-input/"
title: "Tailwind CSS Pagination with Go to Page Input"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "For a 64-page audit log, numbered buttons stop helping &mdash; you need a box."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Pagination with Go to Page Input
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-css-pagination-with-go-to-page-input/

For a 64-page audit log, numbered buttons stop helping &mdash; you need a box. Previous and Next bracket a Go to page field that validates in JavaScript (min/max outside a form validate nothing), steps with the arrow keys, resets with Escape, and shows errors through aria-invalid: utilities plus a message that fades in with starting:. The script only sets aria-invalid, hidden and disabled.
## HTML
```html
<section class="tpg-05 w-full min-h-svh grid place-items-center bg-tpg05-bg bg-[radial-gradient(75%_60%_at_50%_0%,var(--color-tpg05-glow),transparent_72%)] px-5 py-14 font-tpg05-sans text-tpg05-ink antialiased" aria-label="Tailwind CSS pagination with go to page input demo">
  <div class="grid w-full max-w-[44rem] grid-cols-[minmax(0,1fr)] justify-items-center gap-6">
    <article id="tpg-05-log" class="w-full overflow-hidden rounded-2xl bg-tpg05-card shadow-tpg05-card ring-1 ring-tpg05-line">
      <header class="flex flex-wrap items-end justify-between gap-x-6 gap-y-2 px-4 pt-5 pb-4 sm:px-5">
        <div>
          <h2 class="flex items-center gap-2 text-[17px] font-semibold tracking-[-0.015em]"><span aria-hidden="true" class="size-2 rounded-full bg-linear-to-br from-tpg05-acc to-tpg05-acc2 shadow-[0_0_10px] shadow-tpg05-acc2/70 ring-4 ring-tpg05-hi/20 animate-pulse motion-reduce:animate-none"></span>Audit log</h2>
          <p class="mt-0.5 text-[13px] text-tpg05-mut tabular-nums" role="status" aria-live="polite" data-status>Page 12 of 64, entries 45–48</p>
        </div>
        <p class="font-tpg05-mono text-[12px] text-tpg05-mut tabular-nums">256 entries · last 30 days</p>
      </header>
      <ol class="divide-y divide-tpg05-line border-y border-tpg05-line">
        <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-5">
          <span data-n class="w-10 shrink-0 font-tpg05-mono text-[12px] font-medium text-tpg05-acc-ink tabular-nums">#45</span>
          <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-lg max-sm:hidden bg-linear-to-br from-tpg05-acc/22 to-tpg05-acc2/12 font-tpg05-mono text-[11px] font-semibold text-tpg05-acc-ink ring-1 ring-tpg05-acc/25 ring-inset">MO</span>
          <div class="min-w-0 flex-1">
            <p class="text-[14px] leading-snug text-pretty"><b class="font-semibold">maya.o</b> <span class="text-tpg05-mut">rotated an API key</span></p>
            <p class="mt-0.5 truncate font-tpg05-mono text-[12px] text-tpg05-mut">key_live_••••4f2a</p>
          </div>
          <time class="shrink-0 font-tpg05-mono text-[12px] text-tpg05-mut tabular-nums">09:42</time>
        </li>
        <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-5">
          <span data-n class="w-10 shrink-0 font-tpg05-mono text-[12px] font-medium text-tpg05-acc-ink tabular-nums">#46</span>
          <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-lg max-sm:hidden bg-linear-to-br from-tpg05-acc/22 to-tpg05-acc2/12 font-tpg05-mono text-[11px] font-semibold text-tpg05-acc-ink ring-1 ring-tpg05-acc/25 ring-inset">DB</span>
          <div class="min-w-0 flex-1">
            <p class="text-[14px] leading-snug text-pretty"><b class="font-semibold">deploy-bot</b> <span class="text-tpg05-mut">promoted a build to production</span></p>
            <p class="mt-0.5 truncate font-tpg05-mono text-[12px] text-tpg05-mut">build 8812 · web</p>
          </div>
          <time class="shrink-0 font-tpg05-mono text-[12px] text-tpg05-mut tabular-nums">09:31</time>
        </li>
        <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-5">
          <span data-n class="w-10 shrink-0 font-tpg05-mono text-[12px] font-medium text-tpg05-acc-ink tabular-nums">#47</span>
          <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-lg max-sm:hidden bg-linear-to-br from-tpg05-acc/22 to-tpg05-acc2/12 font-tpg05-mono text-[11px] font-semibold text-tpg05-acc-ink ring-1 ring-tpg05-acc/25 ring-inset">SR</span>
          <div class="min-w-0 flex-1">
            <p class="text-[14px] leading-snug text-pretty"><b class="font-semibold">sam.r</b> <span class="text-tpg05-mut">changed a role</span></p>
            <p class="mt-0.5 truncate font-tpg05-mono text-[12px] text-tpg05-mut">priya.s · Viewer → Editor</p>
          </div>
          <time class="shrink-0 font-tpg05-mono text-[12px] text-tpg05-mut tabular-nums">09:18</time>
        </li>
        <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-5">
          <span data-n class="w-10 shrink-0 font-tpg05-mono text-[12px] font-medium text-tpg05-acc-ink tabular-nums">#48</span>
          <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-lg max-sm:hidden bg-linear-to-br from-tpg05-acc/22 to-tpg05-acc2/12 font-tpg05-mono text-[11px] font-semibold text-tpg05-acc-ink ring-1 ring-tpg05-acc/25 ring-inset">JL</span>
          <div class="min-w-0 flex-1">
            <p class="text-[14px] leading-snug text-pretty"><b class="font-semibold">jordan.l</b> <span class="text-tpg05-mut">signed in from a new device</span></p>
            <p class="mt-0.5 truncate font-tpg05-mono text-[12px] text-tpg05-mut">Lisbon, PT · Safari 19</p>
          </div>
          <time class="shrink-0 font-tpg05-mono text-[12px] text-tpg05-mut tabular-nums">08:57</time>
        </li>
      </ol>
      <div class="@container/pg bg-tpg05-sub px-3 py-3 sm:px-4">
        <nav aria-label="Pagination" class="flex items-center justify-between gap-2 @max-[36rem]/pg:flex-wrap">
          <button type="button" data-prev class="inline-flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-lg bg-tpg05-card px-3.5 text-[14px] font-medium text-tpg05-ink shadow-tpg05-btn ring-1 ring-tpg05-line transition-[background-color,color,box-shadow,scale,opacity,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:-translate-y-px hover:bg-tpg05-acc/10 hover:text-tpg05-acc-ink hover:ring-tpg05-acc/50 active:translate-y-0 active:scale-[0.97] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg05-ring disabled:cursor-not-allowed disabled:opacity-45 disabled:shadow-none disabled:hover:translate-y-0 disabled:hover:bg-tpg05-card disabled:hover:text-tpg05-ink disabled:hover:ring-tpg05-line @max-[36rem]/pg:flex-1"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>Previous</button>
          <div class="flex items-center justify-center gap-2 @max-[36rem]/pg:order-first @max-[36rem]/pg:w-full">
            <label for="tpg-05-input" class="text-[13.5px] text-tpg05-mut">Go to page</label>
            <input id="tpg-05-input" type="text" inputmode="numeric" autocomplete="off" enterkeyhint="go" value="12" aria-invalid="false" aria-describedby="tpg-05-of" class="h-11 w-16 rounded-lg bg-linear-to-b from-tpg05-card to-tpg05-acc/12 text-center font-tpg05-mono text-[15px] font-semibold text-tpg05-acc-ink tabular-nums shadow-tpg05-inset ring-1 ring-tpg05-acc/45 transition-[background-color,color,box-shadow,scale,opacity,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none ring-inset hover:ring-tpg05-acc/80 focus:shadow-tpg05-well focus:outline-2 focus:outline-offset-2 focus:outline-tpg05-ring aria-invalid:text-tpg05-warn aria-invalid:ring-2 aria-invalid:ring-tpg05-warn aria-invalid:focus:outline-tpg05-warn">
            <span id="tpg-05-of" class="text-[13.5px] text-tpg05-mut tabular-nums">of 64</span>
            <button type="button" data-go class="inline-flex min-h-11 min-w-11 cursor-pointer items-center justify-center gap-1 rounded-lg bg-linear-to-br from-tpg05-acc to-tpg05-acc2 px-3.5 text-[14px] font-semibold text-tpg05-acc-fg shadow-tpg05-go transition-[background-color,color,box-shadow,scale,opacity,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:-translate-y-px hover:shadow-tpg05-go-hover hover:brightness-105 active:translate-y-0 active:scale-[0.96] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg05-ring">Go<svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false"><path d="M4.5 10h10M10.5 5.5 15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          </div>
          <button type="button" data-next class="inline-flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-lg bg-tpg05-card px-3.5 text-[14px] font-medium text-tpg05-ink shadow-tpg05-btn ring-1 ring-tpg05-line transition-[background-color,color,box-shadow,scale,opacity,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:-translate-y-px hover:bg-tpg05-acc/10 hover:text-tpg05-acc-ink hover:ring-tpg05-acc/50 active:translate-y-0 active:scale-[0.97] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg05-ring disabled:cursor-not-allowed disabled:opacity-45 disabled:shadow-none disabled:hover:translate-y-0 disabled:hover:bg-tpg05-card disabled:hover:text-tpg05-ink disabled:hover:ring-tpg05-line @max-[36rem]/pg:flex-1">Next<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
        </nav>
        <p id="tpg-05-msg" data-msg hidden class="mt-2.5 flex items-center justify-center gap-1.5 text-[13px] font-medium text-tpg05-warn transition-[opacity,translate] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:-translate-y-1 starting:opacity-0 motion-reduce:transition-none"><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M10 6.5v4.2M10 13.4v.1" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>Enter a page between 1 and 64.</p>
      </div>
    </article>
    <p class="flex flex-wrap items-center justify-center gap-1.5 text-[12.5px] text-tpg05-mut">In the box: <kbd class="rounded-md bg-tpg05-card px-1.5 py-0.5 font-tpg05-mono text-[11px] text-tpg05-ink ring-1 ring-tpg05-line">↑</kbd><kbd class="rounded-md bg-tpg05-card px-1.5 py-0.5 font-tpg05-mono text-[11px] text-tpg05-ink ring-1 ring-tpg05-line">↓</kbd> step · <kbd class="rounded-md bg-tpg05-card px-1.5 py-0.5 font-tpg05-mono text-[11px] text-tpg05-ink ring-1 ring-tpg05-line">Enter</kbd> go · <kbd class="rounded-md bg-tpg05-card px-1.5 py-0.5 font-tpg05-mono text-[11px] text-tpg05-ink ring-1 ring-tpg05-line">Esc</kbd> reset</p>
    <p aria-hidden="true" class="rounded-full bg-tpg05-card px-3.5 py-2 text-center font-tpg05-mono text-[11.5px] text-tpg05-mut ring-1 ring-tpg05-line">aria-invalid: · starting: · @container/pg</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg05-bg: #fdf4e5;
  --color-tpg05-bg: oklch(0.97 0.022 80);
  --color-tpg05-glow: #ffd394b3;
  --color-tpg05-glow: oklch(0.9 0.1 70 / 0.7);
  --color-tpg05-card: #fffefa;
  --color-tpg05-card: oklch(0.997 0.006 85);
  --color-tpg05-sub: #fdf5e9;
  --color-tpg05-sub: oklch(0.974 0.018 78);
  --color-tpg05-ink: #2a1b11;
  --color-tpg05-ink: oklch(0.24 0.03 55);
  --color-tpg05-mut: #6b5648;
  --color-tpg05-mut: oklch(0.47 0.035 55);
  --color-tpg05-line: #ebdcc7;
  --color-tpg05-line: oklch(0.9 0.032 75);
  --color-tpg05-acc: #fe9a00;
  --color-tpg05-acc: oklch(0.769 0.188 70.08);
  --color-tpg05-acc2: #ff6900;
  --color-tpg05-acc2: oklch(0.705 0.213 47.6);
  --color-tpg05-acc-fg: #361404;
  --color-tpg05-acc-fg: oklch(0.24 0.06 45);
  --color-tpg05-acc-ink: #993e00;
  --color-tpg05-acc-ink: oklch(0.48 0.14 48);
  --color-tpg05-hi: #f89d00;
  --color-tpg05-hi: oklch(0.77 0.17 70);
  --color-tpg05-ring: #d06300;
  --color-tpg05-ring: oklch(0.62 0.17 55);
  --color-tpg05-warn: #be2323;
  --color-tpg05-warn: oklch(0.52 0.19 27);
  --font-tpg05-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-tpg05-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tpg05-card: 0 1px 2px oklch(0.35 0.06 55 / 0.07), 0 26px 56px -24px oklch(0.55 0.15 55 / 0.3);
  --shadow-tpg05-btn: 0 1px 2px oklch(0.35 0.06 55 / 0.08);
  --shadow-tpg05-inset: inset 0 1px 2px oklch(0.4 0.1 55 / 0.1);
  --shadow-tpg05-well: inset 0 1px 2px oklch(0.4 0.1 55 / 0.1), 0 0 0 4px oklch(0.77 0.17 70 / 0.22), 0 6px 18px -6px oklch(0.7 0.2 50 / 0.45);
  --shadow-tpg05-go: 0 6px 16px -6px oklch(0.68 0.2 48 / 0.6), 0 1px 2px oklch(0.4 0.12 45 / 0.3), inset 0 1px 0 oklch(1 0.02 85 / 0.45);
  --shadow-tpg05-go-hover: 0 10px 24px -6px oklch(0.68 0.2 48 / 0.7), 0 1px 2px oklch(0.4 0.12 45 / 0.3), inset 0 1px 0 oklch(1 0.02 85 / 0.5);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-05 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tpg-05:not([data-theme="light"]) {
    --color-tpg05-bg: #170d07;
    --color-tpg05-bg: oklch(0.17 0.022 50);
    --color-tpg05-glow: #54280280;
    --color-tpg05-glow: oklch(0.33 0.08 55 / 0.5);
    --color-tpg05-card: #21150e;
    --color-tpg05-card: oklch(0.21 0.024 50);
    --color-tpg05-sub: #2a1b13;
    --color-tpg05-sub: oklch(0.24 0.028 52);
    --color-tpg05-ink: #f7f1e7;
    --color-tpg05-ink: oklch(0.96 0.015 80);
    --color-tpg05-mut: #c3b19d;
    --color-tpg05-mut: oklch(0.77 0.035 70);
    --color-tpg05-line: #493224;
    --color-tpg05-line: oklch(0.34 0.04 52);
    --color-tpg05-acc: #fe9a00;
    --color-tpg05-acc: oklch(0.769 0.188 70.08);
    --color-tpg05-acc2: #ff6900;
    --color-tpg05-acc2: oklch(0.705 0.213 47.6);
    --color-tpg05-acc-fg: #361404;
    --color-tpg05-acc-fg: oklch(0.24 0.06 45);
    --color-tpg05-acc-ink: #ffbb65;
    --color-tpg05-acc-ink: oklch(0.84 0.13 70);
    --color-tpg05-hi: #fea92f;
    --color-tpg05-hi: oklch(0.8 0.16 70);
    --color-tpg05-ring: #ffa746;
    --color-tpg05-ring: oklch(0.8 0.15 65);
    --color-tpg05-warn: #ff847d;
    --color-tpg05-warn: oklch(0.75 0.15 25);
  }
}

.tpg-05[data-theme="dark"] {
  --color-tpg05-bg: #170d07;
  --color-tpg05-bg: oklch(0.17 0.022 50);
  --color-tpg05-glow: #54280280;
  --color-tpg05-glow: oklch(0.33 0.08 55 / 0.5);
  --color-tpg05-card: #21150e;
  --color-tpg05-card: oklch(0.21 0.024 50);
  --color-tpg05-sub: #2a1b13;
  --color-tpg05-sub: oklch(0.24 0.028 52);
  --color-tpg05-ink: #f7f1e7;
  --color-tpg05-ink: oklch(0.96 0.015 80);
  --color-tpg05-mut: #c3b19d;
  --color-tpg05-mut: oklch(0.77 0.035 70);
  --color-tpg05-line: #493224;
  --color-tpg05-line: oklch(0.34 0.04 52);
  --color-tpg05-acc: #fe9a00;
  --color-tpg05-acc: oklch(0.769 0.188 70.08);
  --color-tpg05-acc2: #ff6900;
  --color-tpg05-acc2: oklch(0.705 0.213 47.6);
  --color-tpg05-acc-fg: #361404;
  --color-tpg05-acc-fg: oklch(0.24 0.06 45);
  --color-tpg05-acc-ink: #ffbb65;
  --color-tpg05-acc-ink: oklch(0.84 0.13 70);
  --color-tpg05-hi: #fea92f;
  --color-tpg05-hi: oklch(0.8 0.16 70);
  --color-tpg05-ring: #ffa746;
  --color-tpg05-ring: oklch(0.8 0.15 65);
  --color-tpg05-warn: #ff847d;
  --color-tpg05-warn: oklch(0.75 0.15 25);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tpg-05-log');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const input = root.querySelector('#tpg-05-input');
  const msg = root.querySelector('[data-msg]');
  const status = root.querySelector('[data-status]');
  const prev = root.querySelector('[data-prev]');
  const next = root.querySelector('[data-next]');
  const nums = [...root.querySelectorAll('[data-n]')];
  const total = 64, per = 4;
  let current = 12;
  const invalid = (bad) => {
    msg.hidden = !bad;
    input.setAttribute('aria-invalid', String(bad));
    input.setAttribute('aria-describedby', bad ? 'tpg-05-of tpg-05-msg' : 'tpg-05-of');
  };
  const paint = (p) => {
    current = p;
    const first = (p - 1) * per + 1;
    input.value = p;
    nums.forEach((el, i) => { el.textContent = '#' + (first + i); });
    status.textContent = 'Page ' + p + ' of ' + total + ', entries ' + first + '–' + p * per;
    prev.disabled = p === 1;
    next.disabled = p === total;
    invalid(false);
  };
  const jump = () => {
    const n = Number.parseInt(input.value, 10);
    if (!Number.isInteger(n) || n < 1 || n > total) { invalid(true); input.focus(); input.select(); return; }
    paint(n);
  };
  input.addEventListener('input', () => { input.value = input.value.replace(/[^0-9]/g, '').slice(0, 3); invalid(false); });
  input.addEventListener('focus', () => input.select());
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') { e.preventDefault(); jump(); }
    else if (e.key === 'Escape') { input.value = current; invalid(false); }
    else if (e.key === 'ArrowUp' || e.key === 'ArrowDown') {
      e.preventDefault();
      const n = (Number.parseInt(input.value, 10) || current) + (e.key === 'ArrowUp' ? 1 : -1);
      input.value = Math.min(total, Math.max(1, n));
      invalid(false);
    }
  });
  root.querySelector('[data-go]').addEventListener('click', jump);
  prev.addEventListener('click', () => { paint(current - 1); if (prev.disabled) next.focus(); });
  next.addEventListener('click', () => { paint(current + 1); if (next.disabled) prev.focus(); });
})();
```

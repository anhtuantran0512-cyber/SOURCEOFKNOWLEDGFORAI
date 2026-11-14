---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-full-screen-analytics-dashboard-no-scroll/"
title: "Tailwind CSS Full-Screen Analytics Dashboard (100vh, No Scroll)"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "The NOC-wall contract: every pixel of the viewport, zero scrollbars."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Full-Screen Analytics Dashboard (100vh, No Scroll)
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-full-screen-analytics-dashboard-no-scroll/

The NOC-wall contract: every pixel of the viewport, zero scrollbars. Status bar, KPI strip, chart grid and incident ticker are rows of grid-rows-[2.75rem_auto_minmax(0,1fr)_2.25rem] on an h-svh overflow-hidden frame, type rides clamp(), and gauges sweep in on a registered @property angle. New in the port: the clock actually ticks, and the ticker has a pause button (WCAG 2.2.2) driven by has-checked:.
## HTML
```html
<section class="tdl-16 @container/ops w-full min-h-svh bg-tdl16-bg font-tdl16-sans text-tdl16-ink antialiased" aria-label="Full-screen command center demo">
  <div class="group/ops grid h-svh grid-rows-[2.75rem_auto_minmax(0,1fr)_2.25rem] gap-3 overflow-hidden bg-[radial-gradient(140%_100%_at_50%_-20%,var(--color-tdl16-glow),transparent_55%)] p-3 @max-[40rem]/ops:h-auto @max-[40rem]/ops:grid-rows-[2.75rem_auto_auto_2.25rem]">
    <header class="flex items-center gap-4 px-1.5 text-[13px]">
      <strong class="flex items-center gap-2.5 font-semibold tracking-[0.08em] uppercase"><i aria-hidden="true" class="size-2.25 rounded-full bg-tdl16-ok animate-tdl16-pulse"></i>ATLAS · Global Ops</strong>
      <span class="rounded-full border border-tdl16-ok/35 bg-tdl16-ok/10 px-3 py-1 text-[11px] font-semibold tracking-[0.1em] text-tdl16-ok uppercase @max-[34rem]/ops:hidden">All regions nominal</span>
      <time data-clock class="ml-auto font-tdl16-mono text-[13px] text-tdl16-cyan tabular-nums">21:04:52 UTC</time>
    </header>
    <div class="grid grid-cols-[repeat(auto-fit,minmax(min(9.5rem,100%),1fr))] gap-3 [&>article]:rounded-xl [&>article]:border [&>article]:border-tdl16-edge [&>article]:bg-linear-160 [&>article]:from-tdl16-panel2 [&>article]:to-tdl16-panel [&>article]:px-3.75 [&>article]:py-2.75 [&_h3]:text-[10.5px] [&_h3]:font-semibold [&_h3]:tracking-[0.12em] [&_h3]:text-tdl16-mut [&_h3]:uppercase [&_p]:my-0.5 [&_p]:text-[clamp(22px,2.6cqi+8px,38px)]/[1.15] [&_p]:font-semibold [&_p]:tabular-nums [&>article>small]:text-[11px] [&>article>small]:font-semibold">
      <article><h3>Requests / s</h3><p>84,210</p><small class="text-tdl16-ok">▲ steady</small></article>
      <article><h3>Error rate</h3><p>0.03%</p><small class="text-tdl16-ok">within SLO</small></article>
      <article><h3>P99 latency</h3><p>412<small class="text-[0.5em] text-tdl16-mut"> ms</small></p><small class="text-tdl16-warn">▲ 8% · eu-west</small></article>
      <article><h3>Active incidents</h3><p>1</p><small class="text-tdl16-warn">sev-3 · queue lag</small></article>
    </div>
    <div class="grid min-h-0 grid-cols-3 gap-3 @max-[40rem]/ops:grid-cols-1 @max-[40rem]/ops:auto-rows-[10rem] [&>article]:flex [&>article]:min-h-0 [&>article]:flex-col [&>article]:gap-2.5 [&>article]:overflow-hidden [&>article]:rounded-xl [&>article]:border [&>article]:border-tdl16-edge [&>article]:bg-tdl16-panel [&>article]:px-3.75 [&>article]:py-3.25 [&_h3]:text-[10.5px] [&_h3]:font-semibold [&_h3]:tracking-[0.12em] [&_h3]:text-tdl16-mut [&_h3]:uppercase">
      <article>
        <h3 class="flex justify-between">Throughput · 60 min<span class="font-tdl16-mono tracking-normal text-tdl16-cyan normal-case">5.1M req</span></h3>
        <div aria-hidden="true" class="flex min-h-0 flex-1 items-end gap-1.5 *:h-[92%] *:flex-1 *:origin-bottom *:rounded-t-[3px] *:bg-linear-to-t *:from-tdl16-cyan/20 *:to-tdl16-cyan *:[scale:1_var(--s)] *:animate-tdl16-eq"><i style="--s:.5"></i><i style="--s:.7;animation-delay:.12s"></i><i style="--s:.6;animation-delay:.24s"></i><i style="--s:.85;animation-delay:.36s"></i><i style="--s:.65;animation-delay:.48s"></i><i style="--s:.9;animation-delay:.6s"></i><i style="--s:.75;animation-delay:.72s"></i><i style="--s:.95;animation-delay:.84s"></i><i style="--s:.7;animation-delay:.96s"></i><i style="--s:.8;animation-delay:1.08s"></i></div>
      </article>
      <article>
        <h3>Saturation</h3>
        <div class="flex flex-1 flex-wrap items-center justify-around gap-2 pb-4 [&>div]:relative [&>div]:grid [&>div]:aspect-square [&>div]:w-[clamp(64px,7cqi,104px)] [&>div]:place-items-center [&>div]:before:absolute [&>div]:before:inset-0 [&>div]:before:rounded-full [&>div]:before:bg-[conic-gradient(var(--c)_var(--tdl16-a),var(--color-tdl16-track)_0)] [&>div]:before:[mask:radial-gradient(circle,transparent_58%,black_59%)] [&>div]:before:animate-tdl16-sweep [&>div]:before:content-[''] [&_b]:relative [&_b]:text-[clamp(15px,1.8cqi,22px)] [&_b]:font-semibold [&_b]:tabular-nums [&_b_small]:text-[0.55em] [&_b_small]:text-tdl16-mut [&>div>span]:absolute [&>div>span]:-bottom-1 [&>div>span]:left-1/2 [&>div>span]:-translate-x-1/2 [&>div>span]:translate-y-full [&>div>span]:text-[10px] [&>div>span]:font-semibold [&>div>span]:tracking-[0.14em] [&>div>span]:text-tdl16-mut">
          <div style="--val:68;--c:var(--color-tdl16-cyan)" role="img" aria-label="CPU 68 percent"><b>68<small>%</small></b><span>CPU</span></div>
          <div style="--val:41;--c:var(--color-tdl16-ok)" role="img" aria-label="Memory 41 percent"><b>41<small>%</small></b><span>MEM</span></div>
          <div style="--val:83;--c:var(--color-tdl16-warn)" role="img" aria-label="Disk I/O 83 percent"><b>83<small>%</small></b><span>I/O</span></div>
        </div>
      </article>
      <article>
        <h3>Regions</h3>
        <ul class="grid min-h-0 flex-1 content-evenly gap-2 [&>li]:grid [&>li]:grid-cols-[4.25rem_minmax(0,1fr)_2.5rem] [&>li]:items-center [&>li]:gap-2.5 [&>li]:text-[12.5px] [&_b]:font-tdl16-mono [&_b]:text-[11.5px] [&_b]:font-medium [&_b]:text-tdl16-mut [&_em]:text-right [&_em]:font-semibold [&_em]:not-italic [&_em]:tabular-nums [&_li>span]:h-1.75 [&_li>span]:overflow-hidden [&_li>span]:rounded-full [&_li>span]:bg-tdl16-track [&_li>span>i]:block [&_li>span>i]:h-full [&_li>span>i]:w-(--w) [&_li>span>i]:rounded-full [&_li>span>i]:bg-linear-to-r [&_li>span>i]:from-tdl16-cyan/60 [&_li>span>i]:to-tdl16-cyan">
          <li><b>us-east</b><span><i style="--w:62%"></i></span><em>62%</em></li>
          <li><b>us-west</b><span><i style="--w:48%"></i></span><em>48%</em></li>
          <li><b>eu-west</b><span><i style="--w:87%" class="from-tdl16-warn! to-tdl16-hot!"></i></span><em class="text-tdl16-warn">87%</em></li>
          <li><b>ap-south</b><span><i style="--w:35%"></i></span><em>35%</em></li>
        </ul>
      </article>
    </div>
    <footer aria-label="Incident ticker" class="flex items-center overflow-hidden rounded-[10px] border border-tdl16-edge bg-tdl16-panel">
      <label class="flex h-full flex-none cursor-pointer items-center gap-1.5 border-r border-tdl16-edge px-3 text-[11px] font-semibold tracking-[0.08em] text-tdl16-mut uppercase transition-colors hover:text-tdl16-ink has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-tdl16-cyan"><input class="peer sr-only" type="checkbox" id="tdl16-pause"><svg viewBox="0 0 24 24" class="size-3.5 fill-current peer-checked:hidden" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg><svg viewBox="0 0 24 24" class="hidden size-3.5 fill-current peer-checked:block" aria-hidden="true"><path d="M7 5v14l12-7Z"/></svg><span class="peer-checked:hidden">Pause</span><span class="hidden peer-checked:inline">Play</span></label>
      <div class="min-w-0 flex-1 overflow-hidden mask-x-from-95% mask-x-to-100%">
        <div class="flex w-max animate-tdl16-tick whitespace-nowrap hover:[animation-play-state:paused] group-has-[#tdl16-pause:checked]/ops:[animation-play-state:paused] *:px-3 *:text-[12.5px] *:text-tdl16-mut"><span><b class="text-tdl16-warn">⚠ sev-3</b> · queue lag eu-west · ETA 20m &nbsp;·&nbsp; <b class="text-tdl16-ok">✓</b> deploy v3.02 healthy across 6 regions &nbsp;·&nbsp; ◇ maintenance window Sun 02:00 UTC &nbsp;·&nbsp; <b class="text-tdl16-ok">✓</b> backup verified 21:00 &nbsp;·&nbsp;</span><span aria-hidden="true"><b class="text-tdl16-warn">⚠ sev-3</b> · queue lag eu-west · ETA 20m &nbsp;·&nbsp; <b class="text-tdl16-ok">✓</b> deploy v3.02 healthy across 6 regions &nbsp;·&nbsp; ◇ maintenance window Sun 02:00 UTC &nbsp;·&nbsp; <b class="text-tdl16-ok">✓</b> backup verified 21:00 &nbsp;·&nbsp;</span></div>
      </div>
    </footer>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl16-bg: #0b1820;
  --color-tdl16-bg: oklch(0.14 0.02 230);
  --color-tdl16-panel: #13232c;
  --color-tdl16-panel: oklch(0.19 0.025 230);
  --color-tdl16-panel2: #1a2c36;
  --color-tdl16-panel2: oklch(0.225 0.028 230);
  --color-tdl16-edge: #273a45;
  --color-tdl16-edge: oklch(0.29 0.03 230);
  --color-tdl16-track: #22333d;
  --color-tdl16-track: oklch(0.27 0.03 230);
  --color-tdl16-glow: #1c3442;
  --color-tdl16-glow: oklch(0.24 0.045 230 / 0.9);
  --color-tdl16-ink: #e6eef1;
  --color-tdl16-ink: oklch(0.94 0.01 210);
  --color-tdl16-mut: #9db0ba;
  --color-tdl16-mut: oklch(0.74 0.03 220);
  --color-tdl16-cyan: #56cfe6;
  --color-tdl16-cyan: oklch(0.8 0.12 210);
  --color-tdl16-ok: #4fd88e;
  --color-tdl16-ok: oklch(0.79 0.16 155);
  --color-tdl16-warn: #f0c04a;
  --color-tdl16-warn: oklch(0.83 0.14 85);
  --color-tdl16-hot: #e8553e;
  --color-tdl16-hot: oklch(0.65 0.19 30);
  --font-tdl16-sans: 'Chakra Petch', system-ui, sans-serif;
  --font-tdl16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tdl16-pulse: tdl16-pulse 2.2s infinite;
  --animate-tdl16-eq: tdl16-eq 1.6s ease-in-out infinite alternate;
  --animate-tdl16-sweep: tdl16-sweep 1.2s cubic-bezier(0.2,0.7,0.2,1) 0.3s both;
  --animate-tdl16-tick: tdl16-tick 28s linear infinite;

  @keyframes tdl16-pulse {
    0%,
        100% {
      box-shadow: 0 0 0 0 var(--color-tdl16-ok);
    }

    70% {
      box-shadow: 0 0 0 9px transparent;
    }
  }

  @keyframes tdl16-eq {
    to {
      scale: 1 calc(var(--s) * .55);
    }
  }

  @keyframes tdl16-sweep {
    from {
      --tdl16-a: 0deg;
    }

    to {
      --tdl16-a: calc(var(--val) * 3.6deg);
    }
  }

  @keyframes tdl16-tick {
    to {
      translate: -50% 0;
    }
  }
}
/* At-rule: the gauge angle must be registered to interpolate. */

@property --tdl16-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.tdl-16 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-16 * {
    animation: none !important;
  }

  .tdl-16 [role="img"]::before {
    --tdl16-a: calc(var(--val) * 3.6deg);
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tdl-16 [data-clock]').forEach((el) => {
    if (el.dataset.bound) return; el.dataset.bound = '1';
    const tick = () => {
      const d = new Date();
      el.textContent = d.toISOString().slice(11, 19) + ' UTC';
      el.setAttribute('datetime', d.toISOString());
    };
    tick(); setInterval(tick, 1000);
  });
})();
```

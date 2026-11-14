---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-segmented-pip-countdown-auto-off-toggle/"
title: "Tailwind Segmented Pip Countdown Auto-Off Toggle"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The auto-off idea made countable: instead of a smooth ring, ten pips extinguish one per second, so the remaining time is a number you can read at a glance."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Segmented Pip Countdown Auto-Off Toggle
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-segmented-pip-countdown-auto-off-toggle/

The auto-off idea made countable: instead of a smooth ring, ten pips extinguish one per second, so the remaining time is a number you can read at a glance. Discrete beats read as urgency in a way a sweeping arc never does.
## HTML
```html
<section class="ttg-30 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg30-bg font-ttg30-sans" aria-label="Segmented countdown auto-off toggle">
  <div class="w-[min(360px,100%)] flex flex-col gap-5 px-7 py-6 rounded-[22px] bg-ttg30-card border border-ttg30-edge">
    <div class="flex items-start justify-between gap-5">
      <span class="flex flex-col gap-0.5">
        <b class="text-[16px] font-bold text-ttg30-ink">Temporary admin</b>
        <span class="text-[12.5px] text-ttg30-mute">Elevated rights, revoked automatically</span>
      </span>
      <input type="checkbox" id="ttg-30-sw" role="switch" aria-label="Temporary admin access" class="appearance-none shrink-0 w-14 h-8 rounded-full bg-ttg30-off relative cursor-pointer transition-colors duration-300 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-7 before:h-7 before:rounded-full before:bg-white before:shadow-[0_2px_6px_oklch(0_0_0/0.5)] before:transition-transform before:duration-300 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg30-warn checked:before:translate-x-6 focus-visible:outline-3 focus-visible:outline-ttg30-warn focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:before:transition-none">
    </div>
    <div id="ttg-30-pips" class="flex gap-1.5 data-counting:[&_.ttg30-pip]:[animation:ttg30-out_1s_steps(1,end)_calc(var(--i)*1s)_forwards]">
      <i style="--i:0" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
      <i style="--i:1" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
      <i style="--i:2" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
      <i style="--i:3" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
      <i style="--i:4" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
      <i style="--i:5" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
      <i style="--i:6" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
      <i style="--i:7" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
      <i style="--i:8" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
      <i style="--i:9" class="ttg30-pip h-1.5 flex-1 rounded-full bg-ttg30-pipoff"></i>
    </div>
    <p id="ttg-30-live" aria-live="polite" class="font-ttg30-mono text-[12px] tracking-[0.08em] text-ttg30-mute">Off &middot; grants 10s when enabled</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg30-bg: #121419;
  --color-ttg30-bg: oklch(0.19 0.008 265);
  --color-ttg30-card: #1a1e26;
  --color-ttg30-card: oklch(0.24 0.01 265);
  --color-ttg30-edge: #2a303b;
  --color-ttg30-edge: oklch(0.31 0.012 265);
  --color-ttg30-off: #343b48;
  --color-ttg30-off: oklch(0.36 0.014 265);
  --color-ttg30-pipoff: #333a47;
  --color-ttg30-pipoff: oklch(0.35 0.014 265);
  --color-ttg30-warn: #f0a63c;
  --color-ttg30-warn: oklch(0.78 0.15 68);
  --color-ttg30-ink: #e7eaf2;
  --color-ttg30-ink: oklch(0.93 0.008 265);
  --color-ttg30-mute: #939bad;
  --color-ttg30-mute: oklch(0.68 0.015 265);
  --font-ttg30-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg30-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}
/* Pips start lit when armed and snap out one per second; steps(1) because a pip is a
   discrete unit of time, not a fade. */

@keyframes ttg30-out {
  0% {
    background-color: var(--color-ttg30-warn);
  }

  100% {
    background-color: var(--color-ttg30-pipoff);
  }
}

.ttg-30 {
  width: 100%;
  min-height: 100svh;
}

.ttg-30 input[type="checkbox"] {
  -webkit-appearance: none;
}
/* Armed but not yet extinguished: every pip is lit until its delay elapses. */

.ttg-30 [data-counting] .ttg30-pip {
  background-color: var(--color-ttg30-warn);
}
```

## JavaScript
```js
(() => {
  const TOTAL = 10;
  const sw = document.querySelector('#ttg-30-sw');
  const pips = document.querySelector('#ttg-30-pips');
  const live = document.querySelector('#ttg-30-live');
  if (!sw || !pips || !live) return;
  let tick = null, end = null;

  const stop = (msg) => {
    clearInterval(tick); tick = null;
    pips.removeAttribute('data-counting');
    live.textContent = msg;
  };

  sw.addEventListener('change', () => {
    clearInterval(tick);
    if (!sw.checked) { stop('Off \u00b7 grants 10s when enabled'); return; }
    pips.removeAttribute('data-counting');
    void pips.offsetWidth; // restart the staggered pip animations
    pips.setAttribute('data-counting', '');
    end = Date.now() + TOTAL * 1000;
    live.textContent = 'Admin access \u2014 ' + TOTAL + 's remaining';
    tick = setInterval(() => {
      const left = Math.max(0, Math.round((end - Date.now()) / 1000));
      if (left <= 0) { sw.checked = false; stop('Expired \u2014 access revoked'); return; }
      live.textContent = 'Admin access \u2014 ' + left + 's remaining';
    }, 1000);
  });
})();
```

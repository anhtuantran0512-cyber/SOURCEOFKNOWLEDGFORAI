---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-guarded-kill-switch-safety-cover/"
title: "Tailwind Guarded Kill Switch Under a Flip-Up Safety Cover"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The finale: a red safety cover you must flip up before the switch beneath can be thrown, exactly like the guarded toggles on aircraft panels."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Guarded Kill Switch Under a Flip-Up Safety Cover
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-guarded-kill-switch-safety-cover/

The finale: a red safety cover you must flip up before the switch beneath can be thrown, exactly like the guarded toggles on aircraft panels. Two deliberate actions, a warning strip that wakes up, and closing the cover kills the switch automatically.
## HTML
```html
<section class="ttg-47 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg47-bg font-ttg47-mono" aria-label="Guarded kill switch">
  <div id="ttg-47-panel" class="relative w-[min(340px,100%)] flex flex-col gap-5 px-7 py-6 rounded-[18px] bg-linear-165 from-ttg47-panelhi to-ttg47-panello shadow-[0_28px_56px_-28px_oklch(0_0_0/0.95),inset_0_1px_0_oklch(1_0_0/0.08)] has-checked:[&_.ttg47-stripe]:animate-ttg47-pulse motion-reduce:has-checked:[&_.ttg47-stripe]:animate-none">
    <span aria-hidden="true" class="ttg47-stripe h-1.5 rounded-full opacity-40 [background:repeating-linear-gradient(135deg,var(--color-ttg47-hazard)_0_10px,var(--color-ttg47-panelhi)_10px_20px)]"></span>
    <span class="flex flex-col gap-0.5">
      <b class="text-[14px] font-bold tracking-[0.16em] text-ttg47-ink">MASTER CUTOFF</b>
      <span class="font-ttg47-sans text-[12.5px] text-ttg47-mute">Flip the guard, then throw the switch</span>
    </span>
    <div class="relative h-28 perspective-[420px]">
      <div class="absolute inset-0 flex items-center justify-center gap-4 rounded-xl bg-ttg47-recess shadow-[inset_0_3px_10px_oklch(0_0_0/0.8)]">
        <input type="checkbox" id="ttg-47-kill" role="switch" aria-label="Master cutoff" disabled class="appearance-none w-20 h-11 rounded-full bg-ttg47-trackoff relative cursor-pointer transition-[background-color,opacity] duration-300 disabled:opacity-40 disabled:cursor-not-allowed before:content-[''] before:absolute before:top-1 before:left-1 before:w-9 before:h-9 before:rounded-full before:bg-ttg47-thumb before:shadow-[0_2px_6px_oklch(0_0_0/0.6)] before:transition-transform before:duration-300 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg47-hazard checked:before:translate-x-9 focus-visible:outline-3 focus-visible:outline-ttg47-focus focus-visible:outline-offset-4 motion-reduce:transition-none motion-reduce:before:transition-none">
        <span id="ttg-47-state" class="font-ttg47-sans text-[13px] font-bold tracking-[0.08em] text-ttg47-mute">SAFE</span>
      </div>
      <input type="checkbox" id="ttg-47-guard" class="peer sr-only" aria-label="Safety cover">
      <label for="ttg-47-guard" class="absolute inset-0 grid place-items-center rounded-xl cursor-pointer origin-top bg-linear-to-b from-ttg47-coverhi to-ttg47-coverlo border-2 border-ttg47-coveredge shadow-[0_10px_20px_-8px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.3)] transition-transform duration-[420ms] ease-[cubic-bezier(0.35,1.25,0.5,1)] peer-checked:-rotate-x-[105deg] peer-focus-visible:outline-3 peer-focus-visible:outline-ttg47-focus peer-focus-visible:outline-offset-4 motion-reduce:duration-100">
        <span class="flex flex-col items-center gap-1 text-center">
          <b class="text-[12px] font-extrabold tracking-[0.2em] text-white">LIFT GUARD</b>
          <span class="font-ttg47-sans text-[10.5px] tracking-[0.1em] text-white/80">Two-step arming</span>
        </span>
      </label>
    </div>
    <p id="ttg-47-live" aria-live="polite" class="font-ttg47-sans text-[12px] text-ttg47-mute">Guard closed &middot; switch locked</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg47-bg: #15171b;
  --color-ttg47-bg: oklch(0.21 0.005 265);
  --color-ttg47-panelhi: #33373e;
  --color-ttg47-panelhi: oklch(0.33 0.007 265);
  --color-ttg47-panello: #24272c;
  --color-ttg47-panello: oklch(0.27 0.006 265);
  --color-ttg47-recess: #17191d;
  --color-ttg47-recess: oklch(0.2 0.005 265);
  --color-ttg47-coverhi: #d8452f;
  --color-ttg47-coverhi: oklch(0.58 0.2 28);
  --color-ttg47-coverlo: #97281c;
  --color-ttg47-coverlo: oklch(0.43 0.17 28);
  --color-ttg47-coveredge: #f07a63;
  --color-ttg47-coveredge: oklch(0.7 0.16 30);
  --color-ttg47-hazard: #f0a63c;
  --color-ttg47-hazard: oklch(0.78 0.15 68);
  --color-ttg47-trackoff: #3a3f49;
  --color-ttg47-trackoff: oklch(0.38 0.012 265);
  --color-ttg47-thumb: #e7eaf0;
  --color-ttg47-thumb: oklch(0.93 0.006 265);
  --color-ttg47-ink: #e8ebf1;
  --color-ttg47-ink: oklch(0.93 0.006 265);
  --color-ttg47-mute: #9aa1ad;
  --color-ttg47-mute: oklch(0.71 0.012 265);
  --color-ttg47-focus: #6cb6f0;
  --color-ttg47-focus: oklch(0.74 0.14 235);
  --font-ttg47-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --font-ttg47-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-ttg47-pulse: ttg47-pulse 1.6s ease-in-out infinite;
}

@keyframes ttg47-pulse {
  0%,
    100% {
    opacity: 0.4;
  }

  50% {
    opacity: 1;
  }
}

.ttg-47 {
  width: 100%;
  min-height: 100svh;
}

.ttg-47 input[type="checkbox"] {
  -webkit-appearance: none;
}
```

## JavaScript
```js
(() => {
  const guard = document.querySelector('#ttg-47-guard');
  const kill = document.querySelector('#ttg-47-kill');
  const state = document.querySelector('#ttg-47-state');
  const live = document.querySelector('#ttg-47-live');
  if (!guard || !kill || !state || !live) return;

  const report = () => {
    const armed = kill.checked;
    state.textContent = armed ? 'ARMED' : 'SAFE';
    state.style.color = armed ? 'var(--color-ttg47-hazard)' : '';
    live.textContent = !guard.checked
      ? 'Guard closed \u00b7 switch locked'
      : (armed ? 'Cutoff ARMED \u2014 close the guard to disarm' : 'Guard open \u00b7 switch unlocked');
  };

  guard.addEventListener('change', () => {
    kill.disabled = !guard.checked;
    if (!guard.checked) kill.checked = false; // closing the cover always disarms
    report();
  });
  kill.addEventListener('change', report);
  report();
})();
```

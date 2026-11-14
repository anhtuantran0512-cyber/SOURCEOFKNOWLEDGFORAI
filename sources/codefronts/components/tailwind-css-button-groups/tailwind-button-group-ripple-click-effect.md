---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-button-group-ripple-click-effect/"
title: "Tailwind Button Group with Ripple Click Effect (Radar Shockwave Feedback)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A reactor-control action row with satisfying click feedback: a radar shockwave expands from exactly where you clicked, the primary action breathes with an…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Button Group with Ripple Click Effect (Radar Shockwave Feedback)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-button-group-ripple-click-effect/

A reactor-control action row with satisfying click feedback: a radar shockwave expands from exactly where you clicked, the primary action breathes with an @property-animated glow, and a console line logs each command. The CSS original only rippled from the centre while the mouse was held (quick clicks barely showed); a tiny script now sets --x/--y and re-arms data-fire:after:animate-tbg24-wave on every press.
## HTML
```html
<section class="tbg-24 w-full min-h-svh grid place-items-center bg-tbg24-bg bg-[radial-gradient(120%_120%_at_50%_40%,var(--color-tbg24-glow),transparent_70%)] px-5 py-14 font-tbg24-sans text-tbg24-ink" aria-label="Ripple click effect button group demo">
  <div data-tbg24-panel class="grid w-full max-w-[38rem] gap-4">
    <p class="ml-0.5 text-xs font-bold uppercase tracking-[0.14em] text-tbg24-acc">Reactor controls</p>
    <div role="group" aria-label="Reactor controls" class="flex flex-wrap gap-3.5">
      <button type="button" data-tbg24-btn style="--c:#37f5c5" class="relative isolate h-14 cursor-pointer overflow-hidden rounded-2xl border-[1.5px] border-[color-mix(in_oklab,var(--c)_55%,var(--color-tbg24-key))] bg-tbg24-key px-6.5 text-[15px] font-bold tracking-[0.04em] text-(--c) shadow-[0_0_var(--tbg24-g)_-2px_var(--c)] animate-tbg24-breathe transition-[color,background-color] duration-200 after:pointer-events-none after:absolute after:top-(--y) after:left-(--x) after:-z-1 after:aspect-square after:w-[120%] after:-translate-1/2 after:scale-0 after:rounded-full after:bg-[radial-gradient(circle,color-mix(in_oklab,var(--c)_70%,transparent)_0_40%,transparent_60%)] after:opacity-0 after:content-[''] hover:bg-[color-mix(in_oklab,var(--c)_16%,var(--color-tbg24-key))] hover:text-tbg24-ink active:bg-[color-mix(in_oklab,var(--c)_26%,var(--color-tbg24-key))] data-fire:after:animate-tbg24-wave focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-(--c) motion-reduce:animate-none motion-reduce:data-fire:after:animate-none [--x:50%] [--y:50%]">Engage</button>
      <button type="button" data-tbg24-btn style="--c:#5cc8ff" class="relative isolate h-14 cursor-pointer overflow-hidden rounded-2xl border-[1.5px] border-[color-mix(in_oklab,var(--c)_55%,var(--color-tbg24-key))] bg-tbg24-key px-6.5 text-[15px] font-bold tracking-[0.04em] text-(--c) transition-[color,background-color] duration-200 after:pointer-events-none after:absolute after:top-(--y) after:left-(--x) after:-z-1 after:aspect-square after:w-[120%] after:-translate-1/2 after:scale-0 after:rounded-full after:bg-[radial-gradient(circle,color-mix(in_oklab,var(--c)_70%,transparent)_0_40%,transparent_60%)] after:opacity-0 after:content-[''] hover:bg-[color-mix(in_oklab,var(--c)_16%,var(--color-tbg24-key))] hover:text-tbg24-ink active:bg-[color-mix(in_oklab,var(--c)_26%,var(--color-tbg24-key))] data-fire:after:animate-tbg24-wave focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-(--c) motion-reduce:data-fire:after:animate-none [--x:50%] [--y:50%]">Scan</button>
      <button type="button" data-tbg24-btn style="--c:#ffb84d" class="relative isolate h-14 cursor-pointer overflow-hidden rounded-2xl border-[1.5px] border-[color-mix(in_oklab,var(--c)_55%,var(--color-tbg24-key))] bg-tbg24-key px-6.5 text-[15px] font-bold tracking-[0.04em] text-(--c) transition-[color,background-color] duration-200 after:pointer-events-none after:absolute after:top-(--y) after:left-(--x) after:-z-1 after:aspect-square after:w-[120%] after:-translate-1/2 after:scale-0 after:rounded-full after:bg-[radial-gradient(circle,color-mix(in_oklab,var(--c)_70%,transparent)_0_40%,transparent_60%)] after:opacity-0 after:content-[''] hover:bg-[color-mix(in_oklab,var(--c)_16%,var(--color-tbg24-key))] hover:text-tbg24-ink active:bg-[color-mix(in_oklab,var(--c)_26%,var(--color-tbg24-key))] data-fire:after:animate-tbg24-wave focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-(--c) motion-reduce:data-fire:after:animate-none [--x:50%] [--y:50%]">Vent</button>
      <button type="button" data-tbg24-btn style="--c:#ff6b84" class="relative isolate h-14 cursor-pointer overflow-hidden rounded-2xl border-[1.5px] border-[color-mix(in_oklab,var(--c)_55%,var(--color-tbg24-key))] bg-tbg24-key px-6.5 text-[15px] font-bold tracking-[0.04em] text-(--c) transition-[color,background-color] duration-200 after:pointer-events-none after:absolute after:top-(--y) after:left-(--x) after:-z-1 after:aspect-square after:w-[120%] after:-translate-1/2 after:scale-0 after:rounded-full after:bg-[radial-gradient(circle,color-mix(in_oklab,var(--c)_70%,transparent)_0_40%,transparent_60%)] after:opacity-0 after:content-[''] hover:bg-[color-mix(in_oklab,var(--c)_16%,var(--color-tbg24-key))] hover:text-tbg24-ink active:bg-[color-mix(in_oklab,var(--c)_26%,var(--color-tbg24-key))] data-fire:after:animate-tbg24-wave focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-(--c) motion-reduce:data-fire:after:animate-none [--x:50%] [--y:50%]">Abort</button>
    </div>
    <p role="log" aria-live="polite" data-tbg24-log class="ml-0.5 min-h-5 font-tbg24-mono text-[12.5px] text-tbg24-mut">› Standing by</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* @property is an at-rule with no utility: it makes the glow radius animatable. */

@property --tbg24-g {
  syntax: "<length>";
  inherits: false;
  initial-value: 0px;
}

@theme {
  --color-tbg24-bg: #03100e;
  --color-tbg24-glow: #072620;
  --color-tbg24-key: #0a1a17;
  --color-tbg24-ink: #eafffa;
  --color-tbg24-mut: #8fc4b6;
  --color-tbg24-mut: oklch(0.78 0.06 175);
  --color-tbg24-acc: #4fd6b8;
  --font-tbg24-sans: 'Chakra Petch', system-ui, sans-serif;
  --font-tbg24-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbg24-wave: tbg24-wave 0.6s ease-out;
  --animate-tbg24-breathe: tbg24-breathe 2.6s ease-in-out infinite;

  @keyframes tbg24-wave {
    0% {
      scale: 0;
      opacity: 0.65;
    }

    100% {
      scale: 2.6;
      opacity: 0;
    }
  }

  @keyframes tbg24-breathe {
    0%,
        100% {
      --tbg24-g: 14px;
    }

    50% {
      --tbg24-g: 34px;
    }
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-24 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tbg24-panel]').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const log = panel.querySelector('[data-tbg24-log]');
    panel.querySelectorAll('[data-tbg24-btn]').forEach((btn) => {
      const fire = (x, y) => {
        btn.style.setProperty('--x', x);
        btn.style.setProperty('--y', y);
        btn.removeAttribute('data-fire');
        void btn.offsetWidth;
        btn.setAttribute('data-fire', '');
      };
      btn.addEventListener('pointerdown', (e) => {
        const r = btn.getBoundingClientRect();
        fire((e.clientX - r.left) + 'px', (e.clientY - r.top) + 'px');
      });
      btn.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') fire('50%', '50%');
      });
      btn.addEventListener('click', () => {
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        log.textContent = '› ' + btn.textContent.trim().toUpperCase() + ' acknowledged · ' + time;
      });
    });
  });
})();
```

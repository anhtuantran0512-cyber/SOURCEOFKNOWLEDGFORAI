---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-glowing-button-countdown-card/"
title: "Tailwind Glowing Button Dark Mode Countdown Card"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A product-launch card with a genuinely emissive CTA: the glow is a wide, low-alpha accent shadow-* layered under a tight inner highlight, so the button looks…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glowing Button Dark Mode Countdown Card
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-glowing-button-countdown-card/

A product-launch card with a genuinely emissive CTA: the glow is a wide, low-alpha accent shadow-* layered under a tight inner highlight, so the button looks lit rather than blurred. A live countdown ticks in tabular figures (fifteen lines of script — the only JS in the collection, and never for theming), and the email field and button share one glowing frame that brightens on has-focus-visible:.
## HTML
```html
<div class="tdm-20 scheme-dark grid w-full min-h-svh place-items-center bg-tdm20-bg bg-[radial-gradient(100%_70%_at_50%_-10%,#1a1430,transparent_62%)] px-4 py-12 font-tdm20-sans text-tdm20-ink antialiased">
  <article class="relative grid w-full max-w-[34rem] gap-7 overflow-hidden rounded-[30px] border border-tdm20-line bg-tdm20-surface p-7 shadow-[0_60px_120px_-60px_rgb(0_0_0/.9)] sm:p-9">
    <span aria-hidden="true" class="pointer-events-none absolute -top-32 left-1/2 h-64 w-[28rem] -translate-x-1/2 rounded-full bg-tdm20-acc/25 blur-3xl"></span>
    <header class="relative flex flex-wrap items-center justify-between gap-3">
      <span class="inline-flex items-center gap-2 rounded-full border border-tdm20-acc/30 bg-tdm20-acc/10 px-3 py-1.5 text-xs font-medium text-tdm20-acc-hi"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>Launching in</span>
      <p class="font-tdm20-mono text-xs text-tdm20-muted">v4.2 · Phosphor</p>
    </header>
    <h1 class="relative text-[clamp(1.9rem,5vw,2.6rem)] font-semibold leading-[1.08] tracking-[-0.04em] text-balance">Command palette, rebuilt for the dark</h1>
    <p class="relative text-[15px]/relaxed text-pretty text-tdm20-muted">Fuzzy search over every surface, 60fps on a five-year-old laptop, and a theme layer that flips without a single line of script.</p>
    <div role="timer" aria-live="off" aria-label="Time until launch" class="relative grid grid-cols-4 gap-2">
      <div class="grid justify-items-center gap-1 rounded-2xl border border-tdm20-line bg-tdm20-raised py-4"><b id="tdm-20-d" class="font-tdm20-mono text-[clamp(1.6rem,5vw,2.2rem)] font-semibold tracking-tight tabular-nums">02</b><span class="text-[11px] uppercase tracking-[0.14em] text-tdm20-muted">days</span></div>
      <div class="grid justify-items-center gap-1 rounded-2xl border border-tdm20-line bg-tdm20-raised py-4"><b id="tdm-20-h" class="font-tdm20-mono text-[clamp(1.6rem,5vw,2.2rem)] font-semibold tracking-tight tabular-nums">14</b><span class="text-[11px] uppercase tracking-[0.14em] text-tdm20-muted">hrs</span></div>
      <div class="grid justify-items-center gap-1 rounded-2xl border border-tdm20-line bg-tdm20-raised py-4"><b id="tdm-20-m" class="font-tdm20-mono text-[clamp(1.6rem,5vw,2.2rem)] font-semibold tracking-tight tabular-nums">37</b><span class="text-[11px] uppercase tracking-[0.14em] text-tdm20-muted">min</span></div>
      <div class="grid justify-items-center gap-1 rounded-2xl border border-tdm20-line bg-tdm20-raised py-4"><b id="tdm-20-s" class="font-tdm20-mono text-[clamp(1.6rem,5vw,2.2rem)] font-semibold tracking-tight tabular-nums">05</b><span class="text-[11px] uppercase tracking-[0.14em] text-tdm20-muted">sec</span></div>
    </div>
    <form onsubmit="return false" class="relative flex flex-wrap gap-2 rounded-2xl border border-tdm20-line bg-tdm20-raised p-1.5 transition has-focus-visible:border-tdm20-acc/60 has-focus-visible:ring-4 has-focus-visible:ring-tdm20-acc/20">
      <label for="tdm-20-email" class="sr-only">Email address</label>
      <input id="tdm-20-email" type="email" inputmode="email" placeholder="[email protected]" autocomplete="email" class="min-h-12 min-w-0 flex-1 bg-transparent px-3.5 text-[15px] text-tdm20-ink outline-none placeholder:text-tdm20-muted/80">
      <button type="submit" class="group/cta inline-flex min-h-12 flex-none items-center gap-2 rounded-xl bg-tdm20-acc px-5 text-[15px] font-semibold text-tdm20-acc-ink shadow-tdm20-glow transition-[box-shadow,filter] duration-300 hover:shadow-tdm20-glow-hi hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tdm20-focus motion-reduce:transition-none">Notify me<svg class="size-4 transition-transform group-hover/cta:translate-x-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 5.5l6.5 6.5-6.5 6.5"/></svg></button>
    </form>
    <footer class="relative flex items-center gap-3">
      <span class="flex -space-x-2" aria-hidden="true"><i class="grid size-8 place-items-center rounded-full border-2 border-tdm20-surface text-[10px] font-semibold not-italic text-tdm20-acc-ink bg-tdm20-acc-hi">AC</i><i class="grid size-8 place-items-center rounded-full border-2 border-tdm20-surface text-[10px] font-semibold not-italic text-tdm20-acc-ink bg-[#f0abfc]">PS</i><i class="grid size-8 place-items-center rounded-full border-2 border-tdm20-surface text-[10px] font-semibold not-italic text-tdm20-acc-ink bg-[#93c5fd]">JL</i></span>
      <p class="text-[13px] text-tdm20-muted"><strong class="font-semibold text-tdm20-ink tabular-nums">2,481</strong> developers on the list · no spam, one email</p>
    </footer>
  </article>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm20-bg: #08070d;
  --color-tdm20-surface: #111019;
  --color-tdm20-raised: #171626;
  --color-tdm20-ink: #f2f0fa;
  --color-tdm20-muted: #a19dbb;
  --color-tdm20-line: #272339;
  --color-tdm20-acc: #8b5cf6;
  --color-tdm20-acc-hi: #c4b5fd;
  --color-tdm20-acc-ink: #0d0720;
  --color-tdm20-focus: #ddd6fe;
  --shadow-tdm20-glow: inset 0 1px 0 rgb(255 255 255 / .28), 0 0 0 1px rgb(167 139 250 / .55), 0 10px 40px -6px rgb(139 92 246 / .55);
  --shadow-tdm20-glow-hi: inset 0 1px 0 rgb(255 255 255 / .35), 0 0 0 1px rgb(196 181 253 / .8), 0 14px 56px -4px rgb(167 139 250 / .75);
  --font-tdm20-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm20-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tdm-20');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const pad = (n) => String(n).padStart(2, '0');
  const target = Date.now() + 2 * 864e5 + 14 * 36e5 + 37 * 6e4 + 5e3;
  const out = ['d', 'h', 'm', 's'].map((k) => root.querySelector('#tdm-20-' + k));
  const tick = () => {
    const left = Math.max(0, target - Date.now()) / 1000 | 0;
    [left / 86400, left / 3600 % 24, left / 60 % 60, left % 60]
      .forEach((v, i) => { out[i].textContent = pad(v | 0); });
  };
  tick();
  setInterval(tick, 1000);
})();
```

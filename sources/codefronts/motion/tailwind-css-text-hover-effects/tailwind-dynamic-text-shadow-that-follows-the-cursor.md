---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-dynamic-text-shadow-that-follows-the-cursor/"
title: "Tailwind Dynamic Text Shadow that Follows the Cursor"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "You hold the lamp: every heading and card casts a shadow away from the cursor, longer and softer with distance, while a pool of light follows the pointer…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dynamic Text Shadow that Follows the Cursor
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-dynamic-text-shadow-that-follows-the-cursor/

You hold the lamp: every heading and card casts a shadow away from the cursor, longer and softer with distance, while a pool of light follows the pointer across the stage. The script writes --tth25-sx/sy/sb; the markup consumes them in [text-shadow:var(--tth25-sx,0px)_var(--tth25-sy,5px)_…] — and the fallbacks are the resting design.
## HTML
```html
<section class="tth-25 @container w-full min-h-svh grid place-items-center bg-tth25-bg bg-[radial-gradient(340px_340px_at_var(--tth25-lx,50%)_var(--tth25-ly,25%),oklch(0.99_0.03_90/0.9),transparent_70%)] px-5 py-14 font-tth25-sans text-tth25-ink" data-tth25-board aria-label="Dynamic light source shadow demo">
  <div class="flex w-full max-w-[53.75rem] flex-col gap-[clamp(20px,3.6cqi,32px)]">
    <header class="flex flex-col items-center gap-3 text-center">
      <h2 data-tth25-lit class="text-[clamp(40px,8cqi,76px)] font-extrabold leading-none tracking-[-0.03em] [text-shadow:var(--tth25-sx,0px)_var(--tth25-sy,5px)_var(--tth25-sb,9px)_color-mix(in_oklch,var(--color-tth25-sh)_38%,transparent)] transition-[text-shadow] duration-80 ease-linear motion-reduce:transition-none">The Lamp Test</h2>
      <p class="max-w-[52ch] text-[15px] leading-[1.65] text-tth25-mut">Move the cursor &mdash; you're holding the light. Every shadow points away from it; length and blur grow with distance.</p>
    </header>
    <div class="grid grid-cols-3 gap-[clamp(12px,2.4cqi,20px)] @max-[38rem]:grid-cols-1">
      <a href="#tth25-top" data-tth25-lit class="flex flex-col gap-2 rounded-2xl border border-tth25-line bg-tth25-card p-[clamp(16px,3cqi,24px)] no-underline shadow-[var(--tth25-sx,0px)_var(--tth25-sy,6px)_calc(var(--tth25-sb,9px)*2.4)_-6px_color-mix(in_oklch,var(--color-tth25-sh)_22%,transparent)] transition-[border-color,box-shadow] duration-80 hover:border-tth25-ink focus-visible:border-tth25-ink focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth25-ink"><h3 data-tth25-lit class="text-[clamp(22px,3.6cqi,30px)] font-extrabold tracking-[-0.02em] [text-shadow:var(--tth25-sx,0px)_var(--tth25-sy,5px)_var(--tth25-sb,9px)_color-mix(in_oklch,var(--color-tth25-sh)_38%,transparent)] transition-[text-shadow] duration-80 ease-linear">Umbra</h3><p class="text-[13.5px] leading-[1.6] text-tth25-mut">The hard core of a shadow &mdash; short and sharp when light is near.</p></a>
      <a href="#tth25-top" data-tth25-lit class="flex flex-col gap-2 rounded-2xl border border-tth25-line bg-tth25-card p-[clamp(16px,3cqi,24px)] no-underline shadow-[var(--tth25-sx,0px)_var(--tth25-sy,6px)_calc(var(--tth25-sb,9px)*2.4)_-6px_color-mix(in_oklch,var(--color-tth25-sh)_22%,transparent)] transition-[border-color,box-shadow] duration-80 hover:border-tth25-ink focus-visible:border-tth25-ink focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth25-ink"><h3 data-tth25-lit class="text-[clamp(22px,3.6cqi,30px)] font-extrabold tracking-[-0.02em] [text-shadow:var(--tth25-sx,0px)_var(--tth25-sy,5px)_var(--tth25-sb,9px)_color-mix(in_oklch,var(--color-tth25-sh)_38%,transparent)] transition-[text-shadow] duration-80 ease-linear">Penumbra</h3><p class="text-[13.5px] leading-[1.6] text-tth25-mut">The soft fringe &mdash; watch blur climb as the lamp walks away.</p></a>
      <a href="#tth25-top" data-tth25-lit class="flex flex-col gap-2 rounded-2xl border border-tth25-line bg-tth25-card p-[clamp(16px,3cqi,24px)] no-underline shadow-[var(--tth25-sx,0px)_var(--tth25-sy,6px)_calc(var(--tth25-sb,9px)*2.4)_-6px_color-mix(in_oklch,var(--color-tth25-sh)_22%,transparent)] transition-[border-color,box-shadow] duration-80 hover:border-tth25-ink focus-visible:border-tth25-ink focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth25-ink"><h3 data-tth25-lit class="text-[clamp(22px,3.6cqi,30px)] font-extrabold tracking-[-0.02em] [text-shadow:var(--tth25-sx,0px)_var(--tth25-sy,5px)_var(--tth25-sb,9px)_color-mix(in_oklch,var(--color-tth25-sh)_38%,transparent)] transition-[text-shadow] duration-80 ease-linear">Cast</h3><p class="text-[13.5px] leading-[1.6] text-tth25-mut">Direction disagrees per card &mdash; that's what sells one shared lamp.</p></a>
    </div>
    <p id="tth25-top" class="text-center text-[12.5px] text-tth25-mut">JS writes <code class="rounded bg-tth25-chip px-1.5 py-px font-tth25-mono text-[0.9em]">--tth25-sx/sy/sb</code> per element; Tailwind owns the shadows. No pointer? The fallback values <em>are</em> the resting design.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth25-bg: #f4f1ea;
  --color-tth25-bg: oklch(0.95 0.008 85);
  --color-tth25-card: #fcfbf8;
  --color-tth25-card: oklch(0.985 0.005 85);
  --color-tth25-chip: #e6e2d8;
  --color-tth25-chip: oklch(0.9 0.01 85);
  --color-tth25-ink: #1f1e2e;
  --color-tth25-ink: oklch(0.24 0.02 275);
  --color-tth25-mut: #5b5a6a;
  --color-tth25-mut: oklch(0.47 0.02 275);
  --color-tth25-line: #ddd8cc;
  --color-tth25-line: oklch(0.88 0.012 85);
  --color-tth25-sh: #252a3a;
  --color-tth25-sh: oklch(0.25 0.03 265);
  --font-tth25-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tth25-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-25 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  var board = document.querySelector('[data-tth25-board]');
  if (!board) return;
  var targets = [].slice.call(board.querySelectorAll('[data-tth25-lit]'));
  var rects = [];
  function measure() { rects = targets.map(function (el) { return el.getBoundingClientRect(); }); }
  measure();
  addEventListener('resize', measure);
  addEventListener('scroll', measure, true);
  board.addEventListener('pointermove', function (e) {
    var br = board.getBoundingClientRect();
    board.style.setProperty('--tth25-lx', ((e.clientX - br.left) / br.width * 100).toFixed(1) + '%');
    board.style.setProperty('--tth25-ly', ((e.clientY - br.top) / br.height * 100).toFixed(1) + '%');
    targets.forEach(function (el, i) {
      var r = rects[i] || el.getBoundingClientRect();
      var dx = (r.left + r.width / 2) - e.clientX, dy = (r.top + r.height / 2) - e.clientY;
      var d = Math.hypot(dx, dy) || 1, pull = Math.min(d / 14, 18);
      el.style.setProperty('--tth25-sx', (dx / d * pull).toFixed(1) + 'px');
      el.style.setProperty('--tth25-sy', (dy / d * pull).toFixed(1) + 'px');
      el.style.setProperty('--tth25-sb', (2 + pull * 1.1).toFixed(1) + 'px');
    });
  });
})();
```

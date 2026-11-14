---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-pixel-art-scaling-with-image-rendering/"
title: "Tailwind Pixel Art Scaling with Image Rendering"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "The same 12&times;12 sprite at 1&times;, 4&times; and 8&times; with default smoothing on the left and nearest-neighbour on the right, both sides labelled,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pixel Art Scaling with Image Rendering
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-pixel-art-scaling-with-image-rendering/

The same 12&times;12 sprite at 1&times;, 4&times; and 8&times; with default smoothing on the left and nearest-neighbour on the right, both sides labelled, plus the two things people get wrong: a non-integer scale factor reintroduces blur even with the property set, and the property does nothing to a shape drawn in CSS rather than sampled from a bitmap. The port has one genuinely awkward corner &mdash; a two-declaration progressive fallback has no utility form.
## HTML
```html
<section class="twr-02 relative block w-full min-h-svh box-border bg-twr02-bg text-twr02-ink font-twr02-sans" aria-labelledby="twr-02-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-02-title">Pixel art scaling comparison</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-02-theme">
    <label class="grid place-items-center size-11 rounded-full border border-twr02-line bg-twr02-surface text-twr02-ink2 cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-twr02-acc peer-focus-visible:outline-offset-2" for="twr-02-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-[clamp(1.5rem,1rem+2vw,2.5rem)] max-w-[72rem] mx-auto px-[clamp(0.85rem,0.5rem+2vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <header class="grid gap-1.5 min-w-0">
      <p class="m-0 font-twr02-mono text-[0.7rem] tracking-[0.14em] uppercase text-twr02-ink2">Source bitmap &middot; 12 &times; 12 px &middot; 5-colour</p>
      <h3 class="m-0 min-w-0 text-[clamp(1.25rem,1rem+1.6vw,2rem)] font-[650] leading-[1.12] tracking-[-0.02em] text-balance">Nearest-neighbour against the default sampler</h3>
    </header>

    <div class="grid grid-cols-[minmax(0,1fr)] gap-4 md:grid-cols-2">
      <article class="min-w-0 grid content-start gap-3.5 rounded border border-twr02-line bg-twr02-surface p-[clamp(0.85rem,0.6rem+1vw,1.25rem)]" aria-labelledby="twr-02-a">
        <h4 class="m-0 flex flex-wrap items-center gap-1.5 min-w-0 text-[0.78rem] font-medium text-twr02-ink2" id="twr-02-a"><span class="min-w-0 [overflow-wrap:anywhere] font-twr02-mono text-[0.68rem] px-1.5 py-0.5 rounded-sm border border-current text-twr02-warn">image-rendering: auto</span> smoothed</h4>
        <ul class="list-none m-0 p-0 flex flex-wrap items-end gap-3">
          <li class="relative flex-none min-w-0 grid place-items-center gap-1.5 p-3 border border-twr02-line bg-twr02-cell [background-image:linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%),linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%)] [background-size:12px_12px] [background-position:0_0,6px_6px]"><span class="font-twr02-mono text-[0.65rem] tracking-[0.08em] text-twr02-ink2">1&times;</span><img class="block size-3" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at original size, smoothed"></li>
          <li class="relative flex-none min-w-0 grid place-items-center gap-1.5 p-3 border border-twr02-line bg-twr02-cell [background-image:linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%),linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%)] [background-size:12px_12px] [background-position:0_0,6px_6px]"><span class="font-twr02-mono text-[0.65rem] tracking-[0.08em] text-twr02-ink2">4&times;</span><img class="block w-[calc(12*var(--twr-02-px))] h-[calc(12*var(--twr-02-px))]" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at four times size, smoothed"></li>
          <li class="relative flex-none min-w-0 grid place-items-center gap-1.5 p-3 border border-twr02-line bg-twr02-cell [background-image:linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%),linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%)] [background-size:12px_12px] [background-position:0_0,6px_6px]"><span class="font-twr02-mono text-[0.65rem] tracking-[0.08em] text-twr02-ink2">8&times;</span><img class="block w-[calc(24*var(--twr-02-px))] h-[calc(24*var(--twr-02-px))]" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at eight times size, smoothed"></li>
        </ul>
      </article>

      <article class="min-w-0 grid content-start gap-3.5 rounded border border-twr02-line bg-twr02-surface p-[clamp(0.85rem,0.6rem+1vw,1.25rem)]" aria-labelledby="twr-02-b">
        <h4 class="m-0 flex flex-wrap items-center gap-1.5 min-w-0 text-[0.78rem] font-medium text-twr02-ink2" id="twr-02-b"><span class="min-w-0 [overflow-wrap:anywhere] font-twr02-mono text-[0.68rem] px-1.5 py-0.5 rounded-sm border border-current text-twr02-ok">image-rendering: pixelated</span> nearest-neighbour</h4>
        <ul class="list-none m-0 p-0 flex flex-wrap items-end gap-3">
          <li class="relative flex-none min-w-0 grid place-items-center gap-1.5 p-3 border border-twr02-line bg-twr02-cell [background-image:linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%),linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%)] [background-size:12px_12px] [background-position:0_0,6px_6px]"><span class="font-twr02-mono text-[0.65rem] tracking-[0.08em] text-twr02-ink2">1&times;</span><img class="block size-3 twr-02__sharp" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at original size, nearest-neighbour"></li>
          <li class="relative flex-none min-w-0 grid place-items-center gap-1.5 p-3 border border-twr02-line bg-twr02-cell [background-image:linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%),linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%)] [background-size:12px_12px] [background-position:0_0,6px_6px]"><span class="font-twr02-mono text-[0.65rem] tracking-[0.08em] text-twr02-ink2">4&times;</span><img class="block w-[calc(12*var(--twr-02-px))] h-[calc(12*var(--twr-02-px))] twr-02__sharp" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at four times size, nearest-neighbour"></li>
          <li class="relative flex-none min-w-0 grid place-items-center gap-1.5 p-3 border border-twr02-line bg-twr02-cell [background-image:linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%),linear-gradient(45deg,rgba(0,0,0,0.05)_25%,transparent_25%_75%,rgba(0,0,0,0.05)_75%)] [background-size:12px_12px] [background-position:0_0,6px_6px]"><span class="font-twr02-mono text-[0.65rem] tracking-[0.08em] text-twr02-ink2">8&times;</span><img class="block w-[calc(24*var(--twr-02-px))] h-[calc(24*var(--twr-02-px))] twr-02__sharp" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite at eight times size, nearest-neighbour"></li>
        </ul>
      </article>
    </div>

    <div class="grid grid-cols-[minmax(0,1fr)] gap-4 md:grid-cols-2">
      <article class="min-w-0 grid content-start gap-3.5 rounded border border-twr02-line bg-twr02-surface p-[clamp(0.85rem,0.6rem+1vw,1.25rem)]" aria-labelledby="twr-02-t1">
        <h4 class="m-0 font-twr02-mono text-[0.72rem] tracking-[0.1em] uppercase text-twr02-warn" id="twr-02-t1">Trap 1 &middot; fractional scale</h4>
        <div class="flex flex-wrap gap-4">
          <figure class="m-0 min-w-0 grid justify-items-center gap-2 p-3.5 border border-twr02-line bg-twr02-cell">
            <img class="block w-[calc(24*var(--twr-02-px))] h-[calc(24*var(--twr-02-px))] twr-02__sharp" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite scaled by a whole number">
            <figcaption class="min-w-0 [overflow-wrap:anywhere] text-center font-twr02-mono text-[0.65rem] text-twr02-ink2">8.0&times; &mdash; integer, clean</figcaption>
          </figure>
          <figure class="m-0 min-w-0 grid justify-items-center gap-2 p-3.5 border border-twr02-line bg-twr02-cell">
            <img class="block w-[calc(12px*var(--twr-02-bad)*1.4)] h-[calc(12px*var(--twr-02-bad)*1.4)] twr-02__sharp" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAtUlEQVR4AVyQoQ7CUAxFuycZCQgIOIJC8R84BN+JwPEfYFAESYJBDAvvNLls7ZKz3t7e7m0rlq52MvsOSWP7Lyi0vj1siHwt+gKmQhqoyieDVxCYNJfFyAANaECTIesnYIjxdC7pNfdhYfv8+Pt7st5yX63+o2nOh70BGtCAFuGE3fFkoCEa1FPDwn2zwgtkLyzwJ0K6Ntkr3fvV6ClUuC7bBtBQ94za1ayfgMBggKaCNDPpHwAAAP//UvV+hwAAAAZJREFUAwAt51rN7RbRewAAAABJRU5ErkJggg==" alt="Sprite scaled by a fractional factor">
            <figcaption class="min-w-0 [overflow-wrap:anywhere] text-center font-twr02-mono text-[0.65rem] text-twr02-ink2">5.7&times; &mdash; fractional, resampled</figcaption>
          </figure>
        </div>
        <p class="m-0 min-w-0 text-[0.78rem] leading-normal text-pretty text-twr02-ink2">Both carry <code class="font-twr02-mono text-[0.92em] bg-twr02-cell px-1 rounded-sm">[image-rendering:pixelated]</code>. The property cannot invent a fractional device pixel.</p>
      </article>

      <article class="min-w-0 grid content-start gap-3.5 rounded border border-twr02-line bg-twr02-surface p-[clamp(0.85rem,0.6rem+1vw,1.25rem)]" aria-labelledby="twr-02-t2">
        <h4 class="m-0 font-twr02-mono text-[0.72rem] tracking-[0.1em] uppercase text-twr02-warn" id="twr-02-t2">Trap 2 &middot; CSS-drawn shapes</h4>
        <div class="flex flex-wrap gap-4">
          <figure class="m-0 min-w-0 grid justify-items-center gap-2 p-3.5 border border-twr02-line bg-twr02-cell">
            <span class="size-24 rounded-full bg-[#2ce8f5] border-4 border-[#0b0f14] [image-rendering:pixelated]" aria-hidden="true"></span>
            <figcaption class="min-w-0 [overflow-wrap:anywhere] text-center font-twr02-mono text-[0.65rem] text-twr02-ink2">rounded-full disc &mdash; property ignored</figcaption>
          </figure>
          <figure class="m-0 min-w-0 grid justify-items-center gap-2 p-3.5 border border-twr02-line bg-twr02-cell">
            <span class="twr-02__stepped size-2 m-11 bg-transparent" aria-hidden="true"></span>
            <figcaption class="min-w-0 [overflow-wrap:anywhere] text-center font-twr02-mono text-[0.65rem] text-twr02-ink2">stepped box-shadow &mdash; real pixels</figcaption>
          </figure>
        </div>
        <p class="m-0 min-w-0 text-[0.78rem] leading-normal text-pretty text-twr02-ink2"><code class="font-twr02-mono text-[0.92em] bg-twr02-cell px-1 rounded-sm">image-rendering</code> is a hint to the image sampler. A painted shape never reaches it.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr02-bg: #efece4;
  --color-twr02-bg: oklch(0.94 0.011 90);
  --color-twr02-surface: #fffdf8;
  --color-twr02-surface: oklch(0.99 0.006 90);
  --color-twr02-cell: #e4e0d5;
  --color-twr02-cell: oklch(0.90 0.013 90);
  --color-twr02-ink: #191712;
  --color-twr02-ink: oklch(0.19 0.01 80);
  --color-twr02-ink2: #555044;
  --color-twr02-ink2: oklch(0.45 0.015 80);
  --color-twr02-line: #b8b2a3;
  --color-twr02-line: oklch(0.77 0.017 90);
  --color-twr02-acc: #b4321e;
  --color-twr02-acc: oklch(0.50 0.17 32);
  --color-twr02-warn: #b4321e;
  --color-twr02-warn: oklch(0.50 0.17 32);
  --color-twr02-ok: #1c6b3a;
  --color-twr02-ok: oklch(0.47 0.12 152);
  --font-twr02-sans: 'Archivo', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-twr02-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

.twr-02 {
  --twr-02-px: 4px;
  --twr-02-bad: 5.7;
}
/* A progressive two-declaration fallback has no utility form: two competing
   utilities land in the same layer and source order decides. Keep the pair. */

.twr-02__sharp {
  image-rendering: crisp-edges;
  image-rendering: pixelated;
}
/* Sixty shadow layers is not a design-scale value. As one arbitrary token it
   would be an unreadable multi-thousand-character class. */

.twr-02__stepped {
  box-shadow: -24px -40px 0 0 #0b0f14, -16px -40px 0 0 #0b0f14, -8px -40px 0 0 #0b0f14, 0 -40px 0 0 #0b0f14, 8px -40px 0 0 #0b0f14, -40px -32px 0 0 #0b0f14, -32px -32px 0 0 #2ce8f5, -24px -32px 0 0 #2ce8f5, -16px -32px 0 0 #2ce8f5, -8px -32px 0 0 #2ce8f5, 0 -32px 0 0 #2ce8f5, 8px -32px 0 0 #2ce8f5, 16px -32px 0 0 #0b0f14, -48px -24px 0 0 #0b0f14, -40px -24px 0 0 #2ce8f5, -32px -24px 0 0 #2ce8f5, -24px -24px 0 0 #2ce8f5, -16px -24px 0 0 #2ce8f5, -8px -24px 0 0 #2ce8f5, 0 -24px 0 0 #2ce8f5, 8px -24px 0 0 #2ce8f5, 16px -24px 0 0 #2ce8f5, 24px -24px 0 0 #0b0f14, -48px -16px 0 0 #0b0f14, -40px -16px 0 0 #2ce8f5, -32px -16px 0 0 #2ce8f5, -24px -16px 0 0 #2ce8f5, -16px -16px 0 0 #2ce8f5, -8px -16px 0 0 #2ce8f5, 0 -16px 0 0 #2ce8f5, 8px -16px 0 0 #2ce8f5, 16px -16px 0 0 #2ce8f5, 24px -16px 0 0 #0b0f14, -48px -8px 0 0 #0b0f14, -40px -8px 0 0 #2ce8f5, -32px -8px 0 0 #2ce8f5, -24px -8px 0 0 #2ce8f5, -16px -8px 0 0 #2ce8f5, -8px -8px 0 0 #2ce8f5, 0 -8px 0 0 #2ce8f5, 8px -8px 0 0 #2ce8f5, 16px -8px 0 0 #2ce8f5, 24px -8px 0 0 #0b0f14, -48px 0 0 0 #0b0f14, -40px 0 0 0 #2ce8f5, -32px 0 0 0 #2ce8f5, -24px 0 0 0 #2ce8f5, -16px 0 0 0 #2ce8f5, -8px 0 0 0 #2ce8f5, 0 0 0 0 #2ce8f5, 8px 0 0 0 #2ce8f5, 16px 0 0 0 #2ce8f5, 24px 0 0 0 #0b0f14, -40px 8px 0 0 #0b0f14, -32px 8px 0 0 #2ce8f5, -24px 8px 0 0 #2ce8f5, -16px 8px 0 0 #2ce8f5, -8px 8px 0 0 #2ce8f5, 0 8px 0 0 #2ce8f5, 8px 8px 0 0 #2ce8f5, 16px 8px 0 0 #0b0f14, -32px 16px 0 0 #0b0f14, -24px 16px 0 0 #0b0f14, -16px 16px 0 0 #0b0f14, -8px 16px 0 0 #0b0f14, 0 16px 0 0 #0b0f14, 8px 16px 0 0 #0b0f14;
}

.twr-02:has(#twr-02-theme:checked) {
  --color-twr02-bg: #16150f;
  --color-twr02-bg: oklch(0.19 0.008 90);
  --color-twr02-surface: #201e17;
  --color-twr02-surface: oklch(0.25 0.01 90);
  --color-twr02-cell: #2b291f;
  --color-twr02-cell: oklch(0.30 0.012 90);
  --color-twr02-ink: #f3f0e8;
  --color-twr02-ink: oklch(0.96 0.006 90);
  --color-twr02-ink2: #aca597;
  --color-twr02-ink2: oklch(0.74 0.012 90);
  --color-twr02-line: #454134;
  --color-twr02-line: oklch(0.38 0.014 90);
  --color-twr02-acc: #ff8f74;
  --color-twr02-acc: oklch(0.76 0.13 36);
  --color-twr02-warn: #ff8f74;
  --color-twr02-warn: oklch(0.76 0.13 36);
  --color-twr02-ok: #6fd396;
  --color-twr02-ok: oklch(0.78 0.13 152);
}
```

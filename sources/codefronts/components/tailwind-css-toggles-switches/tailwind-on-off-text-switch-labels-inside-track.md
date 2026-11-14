---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-on-off-text-switch-labels-inside-track/"
title: "Tailwind ON / OFF Text Switch with Labels Inside the Track"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "State spelled out, not inferred: ON and OFF live inside a 96px track, the thumb covers the inactive word, and the active one fades in."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind ON / OFF Text Switch with Labels Inside the Track
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-on-off-text-switch-labels-inside-track/

State spelled out, not inferred: ON and OFF live inside a 96px track, the thumb covers the inactive word, and the active one fades in. The port is a peer masterclass &mdash; one sr-only checkbox drives a track, two words and a thumb, all through peer-checked:.
## HTML
```html
<section class="ttg-06 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg06-bg font-ttg06-sans" aria-label="Text labelled ON OFF switch">
  <div class="flex items-center gap-8 px-7 py-5 rounded-3xl bg-white border border-ttg06-edge shadow-[0_18px_40px_-30px_oklch(0.4_0.05_265/0.5)]">
    <span class="flex flex-col gap-0.5">
      <span id="ttg-06-l" class="text-[15.5px] font-semibold text-ttg06-ink">Maintenance mode</span>
      <span class="text-[12.5px] text-ttg06-mute">Serves a status page to every visitor</span>
    </span>
    <input type="checkbox" id="ttg-06-sw" role="switch" aria-labelledby="ttg-06-l" class="peer sr-only">
    <label for="ttg-06-sw" aria-hidden="true" class="relative shrink-0 w-24 h-10 rounded-full bg-ttg06-off cursor-pointer transition-colors duration-300 text-[12.5px] font-extrabold tracking-[0.08em] text-white peer-checked:bg-ttg06-on peer-focus-visible:outline-3 peer-focus-visible:outline-ttg06-focus peer-focus-visible:outline-offset-3 peer-checked:[&_.ttg06-on]:opacity-100 peer-checked:[&_.ttg06-on]:translate-x-0 peer-checked:[&_.ttg06-off]:opacity-0 peer-checked:[&_.ttg06-off]:translate-x-1.5 peer-checked:[&_.ttg06-thumb]:translate-x-14">
      <span class="ttg06-on absolute inset-y-0 left-4 flex items-center opacity-0 -translate-x-1.5 transition-[opacity,transform] duration-300 motion-reduce:transition-opacity">ON</span>
      <span class="ttg06-off absolute inset-y-0 right-3.5 flex items-center opacity-100 transition-[opacity,transform] duration-300 motion-reduce:transition-opacity">OFF</span>
      <span class="ttg06-thumb absolute top-1 left-1 w-8 h-8 rounded-full bg-white shadow-[0_2px_6px_oklch(0.35_0.04_265/0.35)] transition-transform duration-300 ease-[cubic-bezier(0.25,0.9,0.3,1.1)] motion-reduce:duration-100"></span>
    </label>
  </div>
  <p class="font-ttg06-mono text-[11px] tracking-[0.14em] uppercase text-ttg06-mute">State in words, not just colour</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg06-bg: #f3f4f8;
  --color-ttg06-bg: oklch(0.96 0.005 265);
  --color-ttg06-edge: #e6e7ef;
  --color-ttg06-edge: oklch(0.93 0.006 265);
  --color-ttg06-off: #6b7385;
  --color-ttg06-off: oklch(0.55 0.02 265);
  --color-ttg06-on: #2f8f5b;
  --color-ttg06-on: oklch(0.58 0.14 155);
  --color-ttg06-ink: #262b36;
  --color-ttg06-ink: oklch(0.28 0.012 265);
  --color-ttg06-mute: #868c9b;
  --color-ttg06-mute: oklch(0.62 0.015 265);
  --color-ttg06-focus: #4665e8;
  --color-ttg06-focus: oklch(0.55 0.19 265);
  --font-ttg06-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg06-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.ttg-06 {
  width: 100%;
  min-height: 100svh;
}
```

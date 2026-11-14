---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-kbd-keys/terminal-style-monospace-kbd-keys-tailwind/"
title: "Terminal-Style Monospace Kbd Keys in Tailwind"
section: "snippets"
category: "tailwind-css-kbd-keys"
category_name: "Tailwind CSS Kbd Keys"
description: "CLI help output rendered as a terminal window: monospace caps for Ctrl + C, Ctrl + R and friends, a <dl> of key → effect, comment-style descriptions and a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terminal-Style Monospace Kbd Keys in Tailwind
Source: https://codefronts.com/snippets/tailwind-css-kbd-keys/terminal-style-monospace-kbd-keys-tailwind/

CLI help output rendered as a terminal window: monospace caps for Ctrl + C, Ctrl + R and friends, a <dl> of key → effect, comment-style descriptions and a blinking block caret driven by an @theme animation token (--animate-kbd19-blink). Light mode becomes a warm paper terminal; dark mode is classic green-on-black.
## HTML
```html
<section class="kbd-19 relative w-full min-h-svh scheme-light kbd19-dark:scheme-dark bg-kbd19-bg text-kbd19-ink font-kbd19-mono" aria-label="Terminal monospace kbd key demo">
  <div class="grid min-h-svh place-items-center px-5 pt-20 pb-12">
      <section class="w-full min-w-0 max-w-[40rem] overflow-hidden rounded-xl border border-kbd19-rim bg-kbd19-term shadow-[0_30px_60px_-30px_var(--color-kbd19-shade)]">
        <div class="flex items-center gap-2 border-b border-kbd19-rim bg-kbd19-bar px-4 py-3">
          <span aria-hidden="true" class="flex gap-1.5"><span class="size-3 rounded-full bg-[#ff5f57]"></span><span class="size-3 rounded-full bg-[#febc2e]"></span><span class="size-3 rounded-full bg-[#28c840]"></span></span>
          <span class="ml-2 text-[12px] text-kbd19-mut">priya@atlas: ~/project</span>
        </div>
        <div class="p-5 text-[13.5px] leading-relaxed sm:p-6">
          <p><span class="text-kbd19-acc">$</span> atlas --help keys</p>
          <dl class="mt-3">
          <div class="grid gap-1 py-1.5 sm:grid-cols-[8.5rem_minmax(0,1fr)] sm:gap-4"><dt><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">Ctrl</kbd><span class="text-[11px] text-kbd19-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">C</kbd></kbd></dt><dd class="min-w-0 text-kbd19-ink"><span aria-hidden="true" class="text-kbd19-mut"># </span>send SIGINT to the foreground job</dd></div>
          <div class="grid gap-1 py-1.5 sm:grid-cols-[8.5rem_minmax(0,1fr)] sm:gap-4"><dt><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">Ctrl</kbd><span class="text-[11px] text-kbd19-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">D</kbd></kbd></dt><dd class="min-w-0 text-kbd19-ink"><span aria-hidden="true" class="text-kbd19-mut"># </span>end of input, close the session</dd></div>
          <div class="grid gap-1 py-1.5 sm:grid-cols-[8.5rem_minmax(0,1fr)] sm:gap-4"><dt><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">Ctrl</kbd><span class="text-[11px] text-kbd19-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">R</kbd></kbd></dt><dd class="min-w-0 text-kbd19-ink"><span aria-hidden="true" class="text-kbd19-mut"># </span>reverse search through history</dd></div>
          <div class="grid gap-1 py-1.5 sm:grid-cols-[8.5rem_minmax(0,1fr)] sm:gap-4"><dt><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">Ctrl</kbd><span class="text-[11px] text-kbd19-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">L</kbd></kbd></dt><dd class="min-w-0 text-kbd19-ink"><span aria-hidden="true" class="text-kbd19-mut"># </span>clear the screen, keep the buffer</dd></div>
          <div class="grid gap-1 py-1.5 sm:grid-cols-[8.5rem_minmax(0,1fr)] sm:gap-4"><dt><kbd class="inline-flex items-center gap-1"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">Ctrl</kbd><span class="text-[11px] text-kbd19-mut" aria-hidden="true">+</span><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">Z</kbd></kbd></dt><dd class="min-w-0 text-kbd19-ink"><span aria-hidden="true" class="text-kbd19-mut"># </span>suspend, resume with <span class="text-kbd19-acc">fg</span></dd></div>
          <div class="grid gap-1 py-1.5 sm:grid-cols-[8.5rem_minmax(0,1fr)] sm:gap-4"><dt><kbd class="inline-flex items-center gap-1.5"><kbd class="inline-flex h-6 min-w-6 items-center justify-center rounded-[4px] border border-kbd19-rim bg-kbd19-cap px-1.5 text-[12px] font-semibold leading-none text-kbd19-capink shadow-[0_2px_0_var(--color-kbd19-edge)]">Tab</kbd><span class="rounded bg-kbd19-chip px-1.5 py-0.5 text-[11px] font-semibold text-kbd19-acc"><span aria-hidden="true">×2</span><span class="sr-only">twice</span></span></kbd></dt><dd class="min-w-0 text-kbd19-ink"><span aria-hidden="true" class="text-kbd19-mut"># </span>list every completion candidate</dd></div>
          </dl>
          <p class="mt-3 flex items-center gap-2"><span class="text-kbd19-acc">$</span><span aria-hidden="true" class="inline-block h-[1.15em] w-[0.6em] bg-kbd19-acc animate-kbd19-blink motion-reduce:animate-none"></span></p>
        </div>
      </section>
  </div>
  <div class="absolute top-3.5 right-4 z-10">
    <input id="kbd-19-theme" type="checkbox" class="peer sr-only">
    <label for="kbd-19-theme" class="inline-flex min-h-11 cursor-pointer select-none items-center gap-2.5 rounded-full border border-current/55 px-4 font-sans text-[11px] font-bold uppercase leading-none tracking-[0.16em] text-kbd19-ink transition-colors hover:border-current peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-kbd19-acc">
      <span aria-hidden="true" class="size-3 flex-none rounded-full bg-current transition-[background-color,box-shadow] duration-300 kbd19-dark:bg-transparent kbd19-dark:shadow-[inset_-4px_-2px_0_0_currentColor] motion-reduce:transition-none"></span>
      <span class="kbd19-dark:hidden">Light</span><span class="hidden kbd19-dark:inline">Dark</span><span class="sr-only"> theme</span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Theme state: follows the OS; the corner switch flips it for THIS demo only. */

@custom-variant kbd19-dark {
  @media (prefers-color-scheme: dark) {
    &:where(.kbd-19:not(:has(#kbd-19-theme:checked)), .kbd-19:not(:has(#kbd-19-theme:checked)) *) {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    &:where(.kbd-19:has(#kbd-19-theme:checked), .kbd-19:has(#kbd-19-theme:checked) *) {
      @slot;
    }
  }
}
/* Every colour is light-dark(day, night): the root's scheme-light / scheme-dark utility picks the side. */

@theme {
  --color-kbd19-bg: light-dark(#e7e2d4, #050607);
  --color-kbd19-bg: light-dark(oklch(0.913 0.02 90.6), oklch(0.121 0.004 245.5));
  --color-kbd19-term: light-dark(#fbf6e7, #0b0f0c);
  --color-kbd19-term: light-dark(oklch(0.973 0.02 91.6), oklch(0.163 0.009 152.9));
  --color-kbd19-bar: light-dark(#efe8d4, #121814);
  --color-kbd19-bar: light-dark(oklch(0.931 0.028 90.9), oklch(0.201 0.012 156));
  --color-kbd19-shade: light-dark(#3a2f1a59, #000000cc);
  --color-kbd19-shade: light-dark(oklch(0.312 0.037 82.7 / 0.35), oklch(0 0 0 / 0.8));
  --color-kbd19-ink: light-dark(#33372f, #cfe8d3);
  --color-kbd19-ink: light-dark(oklch(0.33 0.015 129), oklch(0.907 0.039 150));
  --color-kbd19-mut: light-dark(#5d6157, #7f9884);
  --color-kbd19-mut: light-dark(oklch(0.486 0.016 124.8), oklch(0.654 0.041 151));
  --color-kbd19-rim: light-dark(#d4cbb2, #1f2b22);
  --color-kbd19-rim: light-dark(oklch(0.843 0.035 90.5), oklch(0.275 0.023 152.3));
  --color-kbd19-chip: light-dark(#ece4cc, #13261a);
  --color-kbd19-chip: light-dark(oklch(0.919 0.033 91.7), oklch(0.248 0.034 155.3));
  --color-kbd19-cap: light-dark(#efe8d4, #14201a);
  --color-kbd19-cap: light-dark(oklch(0.931 0.028 90.9), oklch(0.23 0.021 162.5));
  --color-kbd19-edge: light-dark(#bfb596, #010302);
  --color-kbd19-edge: light-dark(oklch(0.773 0.044 92.3), oklch(0.09 0.011 165.3));
  --color-kbd19-capink: light-dark(#24271f, #e4f5e7);
  --color-kbd19-capink: light-dark(oklch(0.267 0.015 124.2), oklch(0.954 0.026 150.8));
  --color-kbd19-acc: light-dark(#2f7d32, #4ade80);
  --color-kbd19-acc: light-dark(oklch(0.524 0.134 144), oklch(0.8 0.182 151.7));
  --font-kbd19-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-kbd19-blink: kbd19-blink 1.1s steps(1) infinite;

  @keyframes kbd19-blink {
    50% {
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as utilities so the stage is sized before the browser build compiles. */

.kbd-19 {
  width: 100%;
  min-height: 100svh;
  position: relative;
}
```

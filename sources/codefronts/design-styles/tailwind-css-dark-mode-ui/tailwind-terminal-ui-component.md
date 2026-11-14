---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-terminal-ui-component/"
title: "Tailwind Terminal UI Component — Retro Dark Console"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A terminal with prompt history, streamed output and a live input line — phosphor green on black, a 3% scanline overlay and a blinking block caret."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Terminal UI Component — Retro Dark Console
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-terminal-ui-component/

A terminal with prompt history, streamed output and a live input line — phosphor green on black, a 3% scanline overlay and a blinking block caret. The retro reference is deliberate, the contrast is not: the green measures 13:1 on the substrate, dim output still clears 6:1, and warnings carry a glyph as well as amber. Output lines stream in on load with starting: and staggered delays — no script.
## HTML
```html
<div class="tdm-14 scheme-only-dark grid w-full min-h-svh place-items-center bg-tdm14-void bg-[radial-gradient(90%_70%_at_50%_0%,#08141a,transparent_70%)] px-4 py-12 font-tdm14-mono text-tdm14-ink antialiased">
  <section aria-label="Terminal" class="relative w-full max-w-3xl overflow-hidden rounded-2xl border border-tdm14-hair bg-tdm14-panel shadow-[0_0_0_1px_rgb(0_0_0),0_40px_120px_-30px_var(--color-tdm14-glow)]">
    <span aria-hidden="true" class="pointer-events-none absolute inset-0 z-10 bg-[repeating-linear-gradient(0deg,rgb(255_255_255/.03)_0_1px,transparent_1px_3px)]"></span>
    <header class="flex items-center gap-3 border-b border-tdm14-hair bg-tdm14-bar px-4 py-3 text-xs">
      <span class="flex gap-1.5" aria-hidden="true"><i class="size-3 rounded-full bg-tdm14-hair"></i><i class="size-3 rounded-full bg-tdm14-hair"></i><i class="size-3 rounded-full bg-tdm14-hair"></i></span>
      <p class="flex-1 truncate text-center text-tdm14-dim">alex@meridian — ~/apps/web</p>
      <span class="inline-flex items-center gap-2 rounded-full border border-tdm14-hair px-2.5 py-1 text-tdm14-phosphor"><span class="size-1.5 rounded-full bg-tdm14-phosphor shadow-[0_0_8px_var(--color-tdm14-phosphor)] animate-tdm14-pulse motion-reduce:animate-none" aria-hidden="true"></span>connected</span>
    </header>
    <div class="grid gap-1.5 px-5 py-5 text-[13.5px]/6 sm:px-6">
      <p class="flex gap-3 text-tdm14-ink font-medium  transition duration-500 ease-out delay-[0ms] starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><span aria-hidden="true" class="w-3 flex-none text-center"><span class="text-tdm14-phosphor">$</span></span><span class="min-w-0 break-words">pnpm build --filter web</span></p>
      <p class="flex gap-3 text-tdm14-dim  transition duration-500 ease-out delay-[120ms] starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><span aria-hidden="true" class="w-3 flex-none text-center"><span class="text-tdm14-dim">·</span></span><span class="min-w-0 break-words">Resolving 412 packages … done in 1.8s</span></p>
      <p class="flex gap-3 text-tdm14-dim  transition duration-500 ease-out delay-[240ms] starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><span aria-hidden="true" class="w-3 flex-none text-center"><span class="text-tdm14-dim">·</span></span><span class="min-w-0 break-words">Compiled 96 routes with the edge runtime</span></p>
      <p class="flex gap-3 text-tdm14-amber  transition duration-500 ease-out delay-[360ms] starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><span aria-hidden="true" class="w-3 flex-none text-center"><span class="text-tdm14-amber">!</span></span><span class="min-w-0 break-words"><span class="sr-only">Warning: </span>theme.css: 3 selectors exceed specificity budget</span></p>
      <p class="flex gap-3 text-tdm14-dim  transition duration-500 ease-out delay-[480ms] starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><span aria-hidden="true" class="w-3 flex-none text-center"><span class="text-tdm14-dim">·</span></span><span class="min-w-0 break-words">Bundle 184 kB gzip (−12 kB from main)</span></p>
      <p class="flex gap-3 text-tdm14-phosphor  transition duration-500 ease-out delay-[600ms] starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><span aria-hidden="true" class="w-3 flex-none text-center"><span class="text-tdm14-phosphor">✓</span></span><span class="min-w-0 break-words">Build succeeded in 14.2s</span></p>
      <p class="flex gap-3 text-tdm14-ink font-medium mt-3 transition duration-500 ease-out delay-[720ms] starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><span aria-hidden="true" class="w-3 flex-none text-center"><span class="text-tdm14-phosphor">$</span></span><span class="min-w-0 break-words">node scripts/audit-contrast.mjs</span></p>
      <p class="flex gap-3 text-tdm14-dim  transition duration-500 ease-out delay-[840ms] starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><span aria-hidden="true" class="w-3 flex-none text-center"><span class="text-tdm14-dim">·</span></span><span class="min-w-0 break-words">Checked 148 token pairs against WCAG AA</span></p>
      <p class="flex gap-3 text-tdm14-phosphor  transition duration-500 ease-out delay-[960ms] starting:translate-y-1 starting:opacity-0 motion-reduce:transition-none"><span aria-hidden="true" class="w-3 flex-none text-center"><span class="text-tdm14-phosphor">✓</span></span><span class="min-w-0 break-words">All pairs pass — lowest ratio 4.71:1</span></p>
    </div>
    <form onsubmit="return false" class="flex items-center gap-3 border-t border-tdm14-hair bg-tdm14-bar px-5 py-3 text-[13.5px] sm:px-6">
      <label for="tdm-14-input" class="sr-only">Terminal command</label>
      <span aria-hidden="true" class="text-tdm14-phosphor">$</span>
      <input id="tdm-14-input" type="text" autocomplete="off" spellcheck="false" placeholder="git switch -c theme/tokens" class="min-h-11 flex-1 bg-transparent text-tdm14-ink caret-tdm14-phosphor outline-none [caret-shape:block] placeholder:text-tdm14-dim/70">
      <kbd class="hidden rounded-md border border-tdm14-hair px-2 py-1 text-[11px] text-tdm14-dim sm:inline">⏎ run</kbd>
    </form>
  </section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm14-void: #03050a;
  --color-tdm14-panel: #070b0f;
  --color-tdm14-bar: #0a1015;
  --color-tdm14-hair: rgb(126 255 168 / .16);
  --color-tdm14-phosphor: #7effa8;
  --color-tdm14-dim: #93bba4;
  --color-tdm14-amber: #ffc866;
  --color-tdm14-ink: #dcffe8;
  --color-tdm14-glow: rgb(126 255 168 / .16);
  --font-tdm14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tdm14-pulse: tdm14-pulse 2.4s ease-in-out infinite;

  @keyframes tdm14-pulse {
    50% {
      opacity: 0.35;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

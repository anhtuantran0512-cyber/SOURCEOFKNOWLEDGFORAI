---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-toggle-data-theme/"
title: "Tailwind Dark Mode Toggle with data-theme Attribute Override"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "The layer you add when a visitor needs to disagree with their operating system."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Toggle with data-theme Attribute Override
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-toggle-data-theme/

The layer you add when a visitor needs to disagree with their operating system. A data-theme attribute beats the OS, and a pure-CSS checkbox read by has-[#tdm-02-toggle:checked]: beats both. The CSS original needed four re-declared token blocks; here the whole cascade is six utilities on one element, including the flip-back rule that keeps the switch working for visitors whose OS already matches your default.
## HTML
```html
<div class="tdm-02 scheme-light-dark has-[#tdm-02-toggle:checked]:scheme-dark dark:has-[#tdm-02-toggle:checked]:scheme-light data-[theme=light]:scheme-light data-[theme=dark]:scheme-dark data-[theme=light]:has-[#tdm-02-toggle:checked]:scheme-dark! data-[theme=dark]:has-[#tdm-02-toggle:checked]:scheme-light! grid w-full min-h-svh place-items-center bg-tdm02-bg bg-[radial-gradient(70%_50%_at_80%_0%,var(--color-tdm02-glow),transparent_70%)] px-4 py-12 font-tdm02-sans text-tdm02-ink antialiased transition-colors duration-300">
  <!-- Host override: add data-theme="light" or data-theme="dark" to this root. -->
  <div class="w-full max-w-4xl overflow-hidden rounded-[28px] border border-tdm02-line bg-tdm02-surface shadow-tdm02-shell">
    <header class="flex items-center justify-between gap-4 border-b border-tdm02-line bg-tdm02-bar px-5 py-3.5">
      <div class="flex min-w-0 items-center gap-3">
        <span class="grid size-9 flex-none place-items-center rounded-xl bg-tdm02-acc/15 text-tdm02-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5 20.5 7.3v9.4L12 21.5l-8.5-4.8V7.3Z"/><path d="M12 8v8M8.5 10l7 4M15.5 10l-7 4"/></svg></span>
        <span class="font-semibold tracking-tight">Atlas</span>
        <span class="hidden rounded-md border border-tdm02-line px-2 py-1 font-tdm02-mono text-[11px] text-tdm02-mut sm:inline">data-theme</span>
      </div>
      <div class="flex items-center gap-3">
        <span class="hidden items-center gap-1.5 font-tdm02-mono text-xs text-tdm02-mut sm:flex">resolved
          <span class="grid rounded-md bg-tdm02-acc/12 px-2 py-1" aria-hidden="true"><span class="col-start-1 row-start-1 text-tdm02-on-light">light</span><span class="col-start-1 row-start-1 text-tdm02-on-dark">dark&nbsp;</span></span>
        </span>
        <label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm02-line bg-tdm02-surface transition duration-200 hover:-translate-y-px hover:border-tdm02-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm02-focus motion-reduce:transition-none ">
        <input id="tdm-02-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm02-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm02-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label>
      </div>
    </header>
    <div class="grid md:grid-cols-[minmax(0,1fr)_19rem]">
      <section class="grid content-start gap-5 p-6 sm:p-8">
        <div class="grid gap-2">
          <p class="font-tdm02-mono text-[11px] uppercase tracking-[0.16em] text-tdm02-acc">Project settings</p>
          <h1 class="text-[clamp(1.6rem,3vw,2.1rem)] font-semibold tracking-[-0.035em]">Appearance</h1>
          <p class="max-w-[54ch] text-[15px]/relaxed text-pretty text-tdm02-mut">The attribute beats the media query. The checkbox beats the attribute. Every visitor gets a switch that flips in both directions.</p>
        </div>
        <ul class="grid gap-2.5">
          <li class="flex items-center justify-between gap-4 rounded-2xl border border-tdm02-line bg-tdm02-raised px-4 py-3.5 transition hover:border-tdm02-acc/40">
            <div class="flex min-w-0 items-center gap-3.5">
              <span class="grid size-8 flex-none place-items-center rounded-lg bg-tdm02-acc/12 font-tdm02-mono text-xs font-semibold text-tdm02-acc">1</span>
              <div class="min-w-0"><p class="text-sm font-medium">Match system preference</p><p class="mt-0.5 text-[13px] text-tdm02-mut">Falls back to <code class="font-tdm02-mono text-[12px] text-tdm02-ink">scheme-light-dark</code></p></div>
            </div>
            <span class="flex-none rounded-full border px-2.5 py-1 font-tdm02-mono text-[11px] font-medium border-tdm02-line text-tdm02-mut">Layer 1</span>
          </li>
          <li class="flex items-center justify-between gap-4 rounded-2xl border border-tdm02-line bg-tdm02-raised px-4 py-3.5 transition hover:border-tdm02-acc/40">
            <div class="flex min-w-0 items-center gap-3.5">
              <span class="grid size-8 flex-none place-items-center rounded-lg bg-tdm02-acc/12 font-tdm02-mono text-xs font-semibold text-tdm02-acc">2</span>
              <div class="min-w-0"><p class="text-sm font-medium">Workspace override</p><p class="mt-0.5 text-[13px] text-tdm02-mut">Set <code class="font-tdm02-mono text-[12px] text-tdm02-ink">data-theme</code> on the root element</p></div>
            </div>
            <span class="flex-none rounded-full border px-2.5 py-1 font-tdm02-mono text-[11px] font-medium border-tdm02-line text-tdm02-mut">Layer 2</span>
          </li>
          <li class="flex items-center justify-between gap-4 rounded-2xl border border-tdm02-line bg-tdm02-raised px-4 py-3.5 transition hover:border-tdm02-acc/40">
            <div class="flex min-w-0 items-center gap-3.5">
              <span class="grid size-8 flex-none place-items-center rounded-lg bg-tdm02-acc/12 font-tdm02-mono text-xs font-semibold text-tdm02-acc">3</span>
              <div class="min-w-0"><p class="text-sm font-medium">In-page switch</p><p class="mt-0.5 text-[13px] text-tdm02-mut">Read by <code class="font-tdm02-mono text-[12px] text-tdm02-ink">has-[#…:checked]:</code>, zero script</p></div>
            </div>
            <span class="flex-none rounded-full border px-2.5 py-1 font-tdm02-mono text-[11px] font-medium border-transparent bg-tdm02-acc text-tdm02-acc-ink">Layer 3</span>
          </li>
        </ul>
      </section>
      <aside class="grid content-start gap-4 border-t border-tdm02-line bg-tdm02-bar p-6 md:border-t-0 md:border-l">
        <h2 class="text-sm font-semibold">Cascade order</h2>
        <ol class="grid gap-2 font-tdm02-mono text-[12px] text-tdm02-mut">
          <li class="rounded-lg border border-tdm02-line bg-tdm02-surface px-3 py-2"><span class="text-tdm02-ink">scheme-light-dark</span> — the default</li>
          <li class="rounded-lg border border-tdm02-line bg-tdm02-surface px-3 py-2"><span class="text-tdm02-ink">data-[theme=…]:</span> — host override</li>
          <li class="rounded-lg border border-tdm02-acc/50 bg-tdm02-acc/10 px-3 py-2"><span class="text-tdm02-ink">has-[#…:checked]:</span> — the visitor wins</li>
        </ol>
        <p class="text-[13px]/relaxed text-pretty text-tdm02-mut"><strong class="font-semibold text-tdm02-ink">Flip-back rule.</strong> <code class="font-tdm02-mono text-tdm02-ink">dark:has-[…]:scheme-light</code> sorts after the plain <code class="font-tdm02-mono text-tdm02-ink">has-</code> utility, so on a dark-OS machine the switch has somewhere to travel.</p>
      </aside>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm02-bg: light-dark(#f4f4f7, #0a0a0c);
  --color-tdm02-glow: light-dark(#ede9fe, #1d1533);
  --color-tdm02-surface: light-dark(#ffffff, #121218);
  --color-tdm02-bar: light-dark(#fafafb, #0f0f14);
  --color-tdm02-raised: light-dark(#fbfbfc, #17171f);
  --color-tdm02-ink: light-dark(#0b0b0f, #f4f4f5);
  --color-tdm02-mut: light-dark(#5a5d66, #a1a1ae);
  --color-tdm02-line: light-dark(#e4e4ea, #26262f);
  --color-tdm02-acc: light-dark(#6d28d9, #a78bfa);
  --color-tdm02-acc-ink: light-dark(#ffffff, #120c22);
  --color-tdm02-focus: light-dark(#6d28d9, #c4b5fd);
  --color-tdm02-sun: light-dark(#b45309, transparent);
  --color-tdm02-moon: light-dark(transparent, #e9d5ff);
  --color-tdm02-on-light: light-dark(#6d28d9, transparent);
  --color-tdm02-on-dark: light-dark(transparent, #c4b5fd);
  --shadow-tdm02-shell: 0 1px 0 light-dark(rgb(255 255 255 / .9), rgb(255 255 255 / .05)) inset, 0 40px 80px -48px light-dark(rgb(15 15 25 / .28), rgb(0 0 0 / .85));
  --font-tdm02-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm02-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

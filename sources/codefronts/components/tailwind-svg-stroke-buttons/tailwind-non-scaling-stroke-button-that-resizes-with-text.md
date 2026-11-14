---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-non-scaling-stroke-button-that-resizes-with-text/"
title: "Tailwind Non Scaling Stroke Button That Resizes with Text"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Six languages, right-to-left included, each button sized by its own text &mdash; and a border that does not draw but wipes, using…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Non Scaling Stroke Button That Resizes with Text
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-non-scaling-stroke-button-that-resizes-with-text/

Six languages, right-to-left included, each button sized by its own text &mdash; and a border that does not draw but wipes, using [clip-path:inset(0_100%_0_0)] instead of a dash constant, so nothing has to know the perimeter at any label width. The Arabic row is the lesson: clip-path takes physical edges only, so it needs rtl:[clip-path:inset(0_0_0_100%)].
## HTML
```html
<section class="svgb-10 relative block w-full min-h-svh bg-svgb10-bg text-svgb10-fg font-svgb10-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-10-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/20 bg-current/7 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/15 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-10-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-items-center p-[clamp(22px,5vw,68px)]">
    <div class="w-full max-w-220 flex flex-col gap-[clamp(20px,3vw,32px)]">
      <p class="m-0 font-svgb10-serif italic text-[clamp(22px,3.6vw,38px)] tracking-[-0.02em] leading-[1.15]">One component &middot; six locales &middot; zero fixed widths</p>

      <ul class="list-none m-0 p-0 flex flex-col gap-3.5">
        <li class="flex items-center gap-4 pb-1 pt-3.5 border-t border-svgb10-rest">
          <span class="flex-none w-[42px] font-svgb10-mono text-[10.5px] tracking-[0.14em] uppercase text-svgb10-muted">en</span>
          <button class="group relative inline-grid place-items-center min-w-23 min-h-14 px-[26px] border-0 bg-transparent text-[15px] font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb10-stroke focus-visible:outline-offset-[3px]" type="button">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-rest [stroke-width:2] transition-[stroke] duration-200 motion-reduce:transition-none group-hover:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)] group-focus-visible:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)]" x="1" y="1" width="198" height="54"/></svg>
            <svg class="absolute inset-0 w-full h-full overflow-visible [clip-path:inset(0_100%_0_0)] rtl:[clip-path:inset(0_0_0_100%)] transition-[clip-path] duration-[760ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[clip-path:inset(0_0_0_0)] group-focus-visible:[clip-path:inset(0_0_0_0)] motion-reduce:transition-none" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-stroke [stroke-width:2] [vector-effect:non-scaling-stroke]" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="absolute -inset-y-1 w-[1.5px] start-0 bg-svgb10-stroke opacity-0 pointer-events-none group-hover:animate-svgb10-seam group-focus-visible:animate-svgb10-seam motion-reduce:hidden" aria-hidden="true"></span>
            <span class="relative z-[1] outline-none">Start free trial</span>
          </button>
        </li>
        <li class="flex items-center gap-4 pb-1 pt-3.5 border-t border-svgb10-rest">
          <span class="flex-none w-[42px] font-svgb10-mono text-[10.5px] tracking-[0.14em] uppercase text-svgb10-muted">de</span>
          <button class="group relative inline-grid place-items-center min-w-23 min-h-14 px-[26px] border-0 bg-transparent text-[15px] font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb10-stroke focus-visible:outline-offset-[3px]" type="button">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-rest [stroke-width:2] transition-[stroke] duration-200 motion-reduce:transition-none group-hover:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)] group-focus-visible:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)]" x="1" y="1" width="198" height="54"/></svg>
            <svg class="absolute inset-0 w-full h-full overflow-visible [clip-path:inset(0_100%_0_0)] rtl:[clip-path:inset(0_0_0_100%)] transition-[clip-path] duration-[760ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[clip-path:inset(0_0_0_0)] group-focus-visible:[clip-path:inset(0_0_0_0)] motion-reduce:transition-none" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-stroke [stroke-width:2] [vector-effect:non-scaling-stroke]" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="absolute -inset-y-1 w-[1.5px] start-0 bg-svgb10-stroke opacity-0 pointer-events-none group-hover:animate-svgb10-seam group-focus-visible:animate-svgb10-seam motion-reduce:hidden" aria-hidden="true"></span>
            <span class="relative z-[1] outline-none" lang="de">Kostenlos testen starten</span>
          </button>
        </li>
        <li class="flex items-center gap-4 pb-1 pt-3.5 border-t border-svgb10-rest">
          <span class="flex-none w-[42px] font-svgb10-mono text-[10.5px] tracking-[0.14em] uppercase text-svgb10-muted">fi</span>
          <button class="group relative inline-grid place-items-center min-w-23 min-h-14 px-[26px] border-0 bg-transparent text-[15px] font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb10-stroke focus-visible:outline-offset-[3px]" type="button">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-rest [stroke-width:2] transition-[stroke] duration-200 motion-reduce:transition-none group-hover:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)] group-focus-visible:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)]" x="1" y="1" width="198" height="54"/></svg>
            <svg class="absolute inset-0 w-full h-full overflow-visible [clip-path:inset(0_100%_0_0)] rtl:[clip-path:inset(0_0_0_100%)] transition-[clip-path] duration-[760ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[clip-path:inset(0_0_0_0)] group-focus-visible:[clip-path:inset(0_0_0_0)] motion-reduce:transition-none" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-stroke [stroke-width:2] [vector-effect:non-scaling-stroke]" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="absolute -inset-y-1 w-[1.5px] start-0 bg-svgb10-stroke opacity-0 pointer-events-none group-hover:animate-svgb10-seam group-focus-visible:animate-svgb10-seam motion-reduce:hidden" aria-hidden="true"></span>
            <span class="relative z-[1] outline-none" lang="fi">Aloita maksuton kokeilujakso</span>
          </button>
        </li>
        <li class="flex items-center gap-4 pb-1 pt-3.5 border-t border-svgb10-rest">
          <span class="flex-none w-[42px] font-svgb10-mono text-[10.5px] tracking-[0.14em] uppercase text-svgb10-muted">ja</span>
          <button class="group relative inline-grid place-items-center min-w-23 min-h-14 px-[26px] border-0 bg-transparent text-[15px] font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb10-stroke focus-visible:outline-offset-[3px]" type="button">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-rest [stroke-width:2] transition-[stroke] duration-200 motion-reduce:transition-none group-hover:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)] group-focus-visible:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)]" x="1" y="1" width="198" height="54"/></svg>
            <svg class="absolute inset-0 w-full h-full overflow-visible [clip-path:inset(0_100%_0_0)] rtl:[clip-path:inset(0_0_0_100%)] transition-[clip-path] duration-[760ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[clip-path:inset(0_0_0_0)] group-focus-visible:[clip-path:inset(0_0_0_0)] motion-reduce:transition-none" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-stroke [stroke-width:2] [vector-effect:non-scaling-stroke]" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="absolute -inset-y-1 w-[1.5px] start-0 bg-svgb10-stroke opacity-0 pointer-events-none group-hover:animate-svgb10-seam group-focus-visible:animate-svgb10-seam motion-reduce:hidden" aria-hidden="true"></span>
            <span class="relative z-[1] outline-none" lang="ja">&#28961;&#26009;&#12487;&#12514;</span>
          </button>
        </li>
        <li class="flex items-center gap-4 pb-1 pt-3.5 border-t border-svgb10-rest" dir="rtl">
          <span class="flex-none w-[42px] font-svgb10-mono text-[10.5px] tracking-[0.14em] uppercase text-svgb10-muted">ar</span>
          <button class="group relative inline-grid place-items-center min-w-23 min-h-14 px-[26px] border-0 bg-transparent text-[15px] font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb10-stroke focus-visible:outline-offset-[3px]" type="button">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-rest [stroke-width:2] transition-[stroke] duration-200 motion-reduce:transition-none group-hover:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)] group-focus-visible:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)]" x="1" y="1" width="198" height="54"/></svg>
            <svg class="absolute inset-0 w-full h-full overflow-visible [clip-path:inset(0_100%_0_0)] rtl:[clip-path:inset(0_0_0_100%)] transition-[clip-path] duration-[760ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[clip-path:inset(0_0_0_0)] group-focus-visible:[clip-path:inset(0_0_0_0)] motion-reduce:transition-none" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-stroke [stroke-width:2] [vector-effect:non-scaling-stroke]" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="absolute -inset-y-1 w-[1.5px] start-0 bg-svgb10-stroke opacity-0 pointer-events-none group-hover:animate-svgb10-seam group-focus-visible:animate-svgb10-seam motion-reduce:hidden" aria-hidden="true"></span>
            <span class="relative z-[1] outline-none" lang="ar">&#1575;&#1576;&#1583;&#1571; &#1575;&#1604;&#1606;&#1587;&#1582;&#1577; &#1575;&#1604;&#1605;&#1580;&#1575;&#1606;&#1610;&#1577;</span>
          </button>
        </li>
        <li class="flex items-center gap-4 pb-1 pt-3.5 border-t border-svgb10-rest">
          <span class="flex-none w-[42px] font-svgb10-mono text-[10.5px] tracking-[0.14em] uppercase text-svgb10-muted">live</span>
          <button class="group relative inline-grid place-items-center min-w-23 min-h-14 px-[26px] border-0 bg-transparent text-[15px] font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb10-stroke focus-visible:outline-offset-[3px] [&_[contenteditable]]:min-w-[4ch] [&_[contenteditable]]:[caret-color:var(--color-svgb10-stroke)]" type="button">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-rest [stroke-width:2] transition-[stroke] duration-200 motion-reduce:transition-none group-hover:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)] group-focus-visible:stroke-[color-mix(in_oklab,var(--color-svgb10-warn)_45%,transparent)]" x="1" y="1" width="198" height="54"/></svg>
            <svg class="absolute inset-0 w-full h-full overflow-visible [clip-path:inset(0_100%_0_0)] rtl:[clip-path:inset(0_0_0_100%)] transition-[clip-path] duration-[760ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[clip-path:inset(0_0_0_0)] group-focus-visible:[clip-path:inset(0_0_0_0)] motion-reduce:transition-none" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="fill-none stroke-svgb10-stroke [stroke-width:2] [vector-effect:non-scaling-stroke]" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="absolute -inset-y-1 w-[1.5px] start-0 bg-svgb10-stroke opacity-0 pointer-events-none group-hover:animate-svgb10-seam group-focus-visible:animate-svgb10-seam motion-reduce:hidden" aria-hidden="true"></span>
            <span class="relative z-[1] outline-none" contenteditable="true" spellcheck="false">Type to resize the frame</span>
          </button>
        </li>
      </ul>

      <div class="grid gap-[clamp(16px,3vw,28px)] grid-cols-[repeat(auto-fit,minmax(min(100%,280px),1fr))] pt-1.5 border-t border-svgb10-rest">
        <div class="flex flex-col gap-2">
          <div class="relative grid place-items-center h-22">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true">
              <rect class="fill-none stroke-svgb10-stroke [stroke-width:2] [vector-effect:non-scaling-stroke]" x="2" y="2" width="196" height="52" rx="14" vector-effect="non-scaling-stroke"/>
            </svg>
            <span class="relative font-svgb10-mono text-xs">non-scaling-stroke</span>
          </div>
          <code class="font-svgb10-mono text-[11px] text-svgb10-muted">even 2px on all four edges</code>
        </div>
        <div class="flex flex-col gap-2">
          <div class="relative grid place-items-center h-22">
            <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true">
              <rect class="fill-none stroke-svgb10-warn [stroke-width:2]" x="2" y="2" width="196" height="52" rx="14"/>
            </svg>
            <span class="relative font-svgb10-mono text-xs">unprotected</span>
          </div>
          <code class="font-svgb10-mono text-[11px] text-svgb10-muted">uneven &middot; the more-scaled axis paints thicker</code>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb10-bg: #f7f5f0;
  --color-svgb10-bg: oklch(0.972 0.008 90);
  --color-svgb10-fg: #17161a;
  --color-svgb10-fg: oklch(0.20 0.006 290);
  --color-svgb10-muted: #6c6a75;
  --color-svgb10-muted: oklch(0.555 0.012 290);
  --color-svgb10-rest: rgba(23, 22, 26, 0.16);
  --color-svgb10-rest: oklch(0.20 0.006 290 / 0.16);
  --color-svgb10-stroke: #5b21f0;
  --color-svgb10-stroke: oklch(0.46 0.26 295);
  --color-svgb10-warn: #c4341f;
  --color-svgb10-warn: oklch(0.53 0.19 32);
  --font-svgb10-sans: 'Inter Tight', system-ui, sans-serif;
  --font-svgb10-serif: 'Instrument Serif', ui-serif, Georgia, serif;
  --font-svgb10-mono: 'JetBrains Mono', ui-monospace, monospace;
  /* the seam marks the wipe front; inset-inline-start is logical, so the same
       keyframe travels the correct way in both reading directions */
  --animate-svgb10-seam: svgb10-seam 760ms cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

@keyframes svgb10-seam {
  0% {
    inset-inline-start: 0;
    opacity: 0;
  }

  10% {
    opacity: 1;
  }

  86% {
    opacity: 1;
  }

  100% {
    inset-inline-start: 100%;
    opacity: 0;
  }
}

.svgb-10:has(#svgb-10-theme:checked) {
  --color-svgb10-bg: #0f0e12;
  --color-svgb10-bg: oklch(0.18 0.006 290);
  --color-svgb10-fg: #f0eff4;
  --color-svgb10-fg: oklch(0.96 0.004 290);
  --color-svgb10-muted: #918f9c;
  --color-svgb10-muted: oklch(0.68 0.012 290);
  --color-svgb10-rest: rgba(240, 239, 244, 0.18);
  --color-svgb10-rest: oklch(0.96 0.004 290 / 0.18);
  --color-svgb10-stroke: #c4a8ff;
  --color-svgb10-stroke: oklch(0.82 0.15 295);
  --color-svgb10-warn: #ff9478;
  --color-svgb10-warn: oklch(0.75 0.16 32);
}
```

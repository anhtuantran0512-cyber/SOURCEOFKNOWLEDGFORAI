---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-orbiting-button-animation-with-offset-path/"
title: "Tailwind CSS Orbiting Button Animation with offset-path"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A SaaS hero where a single &ldquo;What&rsquo;s new&rdquo; satellite circles the primary CTA on a CSS Motion Path &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Orbiting Button Animation with offset-path
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-orbiting-button-animation-with-offset-path/

A SaaS hero where a single &ldquo;What&rsquo;s new&rdquo; satellite circles the primary CTA on a CSS Motion Path &mdash; [offset-path:circle(6.75rem_at_50%_50%)] with [offset-rotate:0deg] so it never banks. Hover or tab into the system and the satellite eases to a predictable dock at 12 o&rsquo;clock, ready to click, with an unread badge and tooltip. Zero JavaScript.
## HTML
```html
<section class="tcm-17 w-full min-h-svh grid place-items-center overflow-hidden bg-tcm17-bg bg-[radial-gradient(50%_45%_at_50%_55%,var(--color-tcm17-glow),transparent_72%)] px-5 py-14 font-tcm17-sans text-tcm17-ink antialiased" aria-label="Orbiting button with offset-path demo">
  <div class="grid w-full max-w-[38rem] justify-items-center gap-6 text-center">
    <p class="inline-flex items-center gap-2 rounded-full bg-tcm17-card px-3 py-1 text-[12.5px] font-medium text-tcm17-mut ring-1 ring-tcm17-line"><span aria-hidden="true" class="rounded-full bg-linear-to-r from-tcm17-a to-tcm17-b px-1.5 text-[10.5px] font-bold text-white">NEW</span>Orbit 2.0 is live</p>
    <h2 class="text-[clamp(2rem,6vw,3.25rem)] leading-[1.02] font-bold tracking-[-0.045em] text-balance">Ship faster with a <span class="bg-linear-to-r from-tcm17-a-ink to-tcm17-b bg-clip-text text-transparent">workspace that orbits you</span></h2>
    <p class="max-w-[30rem] text-[15.5px] leading-relaxed text-tcm17-mut text-pretty">Docs, tasks and deploys in one place. Free for teams up to five &mdash; no card required.</p>
    <div class="group/sys relative mt-2 grid size-[17rem] place-items-center">
      <span aria-hidden="true" class="absolute inset-[1.75rem] rounded-full border border-dashed border-tcm17-a/55"></span>
      <span aria-hidden="true" class="absolute inset-[3.25rem] rounded-full bg-tcm17-a/10 blur-2xl"></span>
      <a href="#tcm-17-signup" class="relative rounded-full bg-linear-to-br from-tcm17-a to-tcm17-a2 px-7 py-4.5 text-[16px] font-semibold tracking-[-0.01em] text-white shadow-tcm17-cta transition-[scale,box-shadow] duration-300 hover:scale-[1.04] active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm17-ring">Start free trial</a>
      <a href="#tcm-17-changelog" class="group/sat absolute top-1/2 left-1/2 -m-6 grid size-12 place-items-center rounded-full bg-linear-to-br from-tcm17-b to-tcm17-b2 text-tcm17-on shadow-tcm17-sat [offset-path:circle(6.75rem_at_50%_50%)] [offset-rotate:0deg] animate-tcm17-orbit transition-[offset-distance,scale] duration-700 ease-[cubic-bezier(.16,1,.3,1)] group-hover/sys:animate-none group-hover/sys:[offset-distance:75%] group-hover/sys:scale-110 group-focus-within/sys:animate-none group-focus-within/sys:[offset-distance:75%] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm17-ring motion-reduce:animate-none motion-reduce:[offset-distance:75%]" aria-label="What's new: 3 updates">
        <svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3.5l1.9 5 5.1 1.6-5.1 1.7L12 17l-1.9-5.2L5 10.1l5.1-1.6z"/></svg>
        <span aria-hidden="true" class="absolute -top-1 -right-1 grid size-5 place-items-center rounded-full bg-tcm17-card text-[10px] font-bold text-tcm17-a-ink ring-2 ring-tcm17-b">3</span>
        <span aria-hidden="true" class="pointer-events-none absolute bottom-[calc(100%+0.6rem)] left-1/2 -translate-x-1/2 translate-y-1 rounded-lg bg-tcm17-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 transition-[opacity,translate] duration-200 group-hover/sat:translate-y-0 group-hover/sat:opacity-100 group-focus-visible/sat:translate-y-0 group-focus-visible/sat:opacity-100">What&rsquo;s new</span>
      </a>
    </div>
    <p class="text-[13px] text-tcm17-mut">Hover the system &mdash; the satellite docks at 12 o&rsquo;clock</p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm17-card px-3.5 py-2 text-center font-tcm17-mono text-[11.5px] text-tcm17-mut ring-1 ring-tcm17-line ">[offset-path:circle(6.75rem_at_50%_50%)] · [offset-rotate:0deg] · group-hover/sys:[offset-distance:75%]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm17-bg: #f5f4ff;
  --color-tcm17-bg: oklch(0.971 0.015 290.3);
  --color-tcm17-glow: #c7d2feb3;
  --color-tcm17-glow: oklch(0.87 0.062 274 / 0.7);
  --color-tcm17-card: #ffffff;
  --color-tcm17-card: oklch(1 0 0);
  --color-tcm17-ink: #14122e;
  --color-tcm17-ink: oklch(0.202 0.054 283.7);
  --color-tcm17-mut: #5a587a;
  --color-tcm17-mut: oklch(0.476 0.054 286.8);
  --color-tcm17-line: #e3e1f5;
  --color-tcm17-line: oklch(0.917 0.027 290.5);
  --color-tcm17-a: #4f46e5;
  --color-tcm17-a: oklch(0.511 0.23 277);
  --color-tcm17-a2: #7c3aed;
  --color-tcm17-a2: oklch(0.541 0.247 293);
  --color-tcm17-a-ink: #4338ca;
  --color-tcm17-a-ink: oklch(0.457 0.215 277);
  --color-tcm17-b: #f59e0b;
  --color-tcm17-b: oklch(0.769 0.165 70.1);
  --color-tcm17-b2: #f97316;
  --color-tcm17-b2: oklch(0.705 0.187 47.6);
  --color-tcm17-on: #2a1503;
  --color-tcm17-on: oklch(0.221 0.046 60.1);
  --color-tcm17-tip: #14122e;
  --color-tcm17-tip: oklch(0.202 0.054 283.7);
  --color-tcm17-ring: #4338ca;
  --color-tcm17-ring: oklch(0.457 0.215 277);
  --font-tcm17-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcm17-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm17-cta: 0 18px 40px -14px oklch(0.45 0.22 280 / 0.75), inset 0 1px 0 oklch(1 0 0 / 0.3);
  --shadow-tcm17-sat: 0 0 0 5px oklch(0.8 0.16 75 / 0.22), 0 10px 22px -8px oklch(0.7 0.18 60 / 0.8);
  --animate-tcm17-orbit: tcm17-orbit 12s linear infinite;

  @keyframes tcm17-orbit {
    from {
      offset-distance: 75%;
    }

    to {
      offset-distance: 175%;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-17 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: starlight: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-17:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm17-bg: #0b0a1d;
    --color-tcm17-bg: oklch(0.158 0.039 283.3);
    --color-tcm17-glow: #3730a366;
    --color-tcm17-glow: oklch(0.398 0.177 277.4 / 0.4);
    --color-tcm17-card: #16143a;
    --color-tcm17-card: oklch(0.219 0.071 281.1);
    --color-tcm17-ink: #f1f0ff;
    --color-tcm17-ink: oklch(0.96 0.02 289.1);
    --color-tcm17-mut: #aaa8d0;
    --color-tcm17-mut: oklch(0.747 0.057 287.2);
    --color-tcm17-line: #2a2856;
    --color-tcm17-line: oklch(0.305 0.081 282.5);
    --color-tcm17-a: #6366f1;
    --color-tcm17-a: oklch(0.585 0.204 277.1);
    --color-tcm17-a2: #8b5cf6;
    --color-tcm17-a2: oklch(0.606 0.219 292.7);
    --color-tcm17-a-ink: #a5b4fc;
    --color-tcm17-a-ink: oklch(0.785 0.104 274.7);
    --color-tcm17-b: #fbbf24;
    --color-tcm17-b: oklch(0.837 0.164 84.4);
    --color-tcm17-b2: #fb923c;
    --color-tcm17-b2: oklch(0.758 0.159 55.9);
    --color-tcm17-on: #2a1503;
    --color-tcm17-on: oklch(0.221 0.046 60.1);
    --color-tcm17-tip: #020617;
    --color-tcm17-tip: oklch(0.129 0.041 264.7);
    --color-tcm17-ring: #a5b4fc;
    --color-tcm17-ring: oklch(0.785 0.104 274.7);
  }
}

.tcm-17[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm17-bg: #0b0a1d;
  --color-tcm17-bg: oklch(0.158 0.039 283.3);
  --color-tcm17-glow: #3730a366;
  --color-tcm17-glow: oklch(0.398 0.177 277.4 / 0.4);
  --color-tcm17-card: #16143a;
  --color-tcm17-card: oklch(0.219 0.071 281.1);
  --color-tcm17-ink: #f1f0ff;
  --color-tcm17-ink: oklch(0.96 0.02 289.1);
  --color-tcm17-mut: #aaa8d0;
  --color-tcm17-mut: oklch(0.747 0.057 287.2);
  --color-tcm17-line: #2a2856;
  --color-tcm17-line: oklch(0.305 0.081 282.5);
  --color-tcm17-a: #6366f1;
  --color-tcm17-a: oklch(0.585 0.204 277.1);
  --color-tcm17-a2: #8b5cf6;
  --color-tcm17-a2: oklch(0.606 0.219 292.7);
  --color-tcm17-a-ink: #a5b4fc;
  --color-tcm17-a-ink: oklch(0.785 0.104 274.7);
  --color-tcm17-b: #fbbf24;
  --color-tcm17-b: oklch(0.837 0.164 84.4);
  --color-tcm17-b2: #fb923c;
  --color-tcm17-b2: oklch(0.758 0.159 55.9);
  --color-tcm17-on: #2a1503;
  --color-tcm17-on: oklch(0.221 0.046 60.1);
  --color-tcm17-tip: #020617;
  --color-tcm17-tip: oklch(0.129 0.041 264.7);
  --color-tcm17-ring: #a5b4fc;
  --color-tcm17-ring: oklch(0.785 0.104 274.7);
}
```

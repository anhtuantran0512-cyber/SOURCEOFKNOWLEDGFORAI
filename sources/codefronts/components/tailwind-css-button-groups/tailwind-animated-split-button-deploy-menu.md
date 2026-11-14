---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-animated-split-button-deploy-menu/"
title: "Tailwind Animated Split Button Deploy Menu (Staggered Dropdown Reveal)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A developer-tool split button &mdash; Deploy plus environment menu &mdash; where the menu wipes open with an animated clip-path and each item phases in from…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Split Button Deploy Menu (Staggered Dropdown Reveal)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-animated-split-button-deploy-menu/

A developer-tool split button &mdash; Deploy plus environment menu &mdash; where the menu wipes open with an animated clip-path and each item phases in from a blur on a staggered delay. Items now show coloured environment dots and their target, and production is flagged as protected, so the menu helps people pick the right place to ship.
## HTML
```html
<section class="tbg-15 w-full min-h-svh grid justify-items-center content-start bg-tbg15-bg bg-[radial-gradient(120%_100%_at_50%_0%,var(--color-tbg15-glow),transparent_70%)] px-5 pt-32 pb-16 font-tbg15-sans text-tbg15-ink" aria-label="Animated split button deploy menu demo">
  <div class="relative inline-flex rounded-2xl shadow-tbg15-lift">
    <button type="button" class="inline-flex h-13 cursor-pointer items-center gap-2.5 rounded-l-2xl bg-linear-120 from-tbg15-a1 to-tbg15-a2 pr-6 pl-5 text-[15.5px] font-bold text-tbg15-on transition hover:brightness-110 active:brightness-95 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg15-a1">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l9 16H3z"/></svg>
      Deploy
    </button>
    <details class="group/more relative">
      <summary aria-label="More deploy options" class="relative grid h-13 w-12.5 cursor-pointer list-none place-items-center rounded-r-2xl border-l border-tbg15-a1/30 bg-white/6 backdrop-blur-sm transition hover:bg-white/10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg15-a1 [&::-webkit-details-marker]:hidden before:absolute before:size-2.5 before:-translate-y-0.5 before:rotate-45 before:border-r-[2.5px] before:border-b-[2.5px] before:border-tbg15-a2 before:opacity-0 before:transition-[rotate,translate,opacity] before:duration-300 before:content-[''] after:absolute after:size-2.5 after:-translate-y-0.5 after:rotate-45 after:border-r-[2.5px] after:border-b-[2.5px] after:border-tbg15-a1 after:transition-[rotate,translate] after:duration-300 after:content-[''] group-open/more:before:translate-x-[-3px] group-open/more:before:translate-y-0.5 group-open/more:before:-rotate-135 group-open/more:before:opacity-80 group-open/more:after:translate-x-[3px] group-open/more:after:translate-y-0.5 group-open/more:after:-rotate-135 motion-reduce:before:transition-none motion-reduce:after:transition-none"></summary>
      <div role="menu" aria-label="Deploy targets" class="absolute top-[calc(100%+0.625rem)] right-0 z-20 hidden w-72 flex-col gap-0.5 rounded-2xl border border-tbg15-a1/22 bg-tbg15-menu/92 p-1.5 shadow-tbg15-menu backdrop-blur-lg group-open/more:flex group-open/more:animate-tbg15-wipe motion-reduce:animate-none!">
        <button type="button" role="menuitem" class="flex min-h-12 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-left opacity-0 hover:bg-tbg15-a1/12 focus-visible:bg-tbg15-a1/12 focus-visible:outline-2 focus-visible:outline-tbg15-a1 group-open/more:animate-tbg15-phase [animation-delay:50ms] motion-reduce:animate-none! motion-reduce:opacity-100"><span aria-hidden="true" class="size-2 flex-none rounded-full bg-tbg15-ok"></span><span class="grid"><span class="text-[14.5px] font-semibold">Preview</span><span class="font-tbg15-mono text-[11.5px] text-tbg15-mut">pr-482.preview.app</span></span></button>
        <button type="button" role="menuitem" class="flex min-h-12 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-left opacity-0 hover:bg-tbg15-a1/12 focus-visible:bg-tbg15-a1/12 focus-visible:outline-2 focus-visible:outline-tbg15-a1 group-open/more:animate-tbg15-phase [animation-delay:110ms] motion-reduce:animate-none! motion-reduce:opacity-100"><span aria-hidden="true" class="size-2 flex-none rounded-full bg-tbg15-warn"></span><span class="grid"><span class="text-[14.5px] font-semibold">Staging</span><span class="font-tbg15-mono text-[11.5px] text-tbg15-mut">staging.acme.dev</span></span></button>
        <button type="button" role="menuitem" class="flex min-h-12 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-left opacity-0 hover:bg-tbg15-a1/12 focus-visible:bg-tbg15-a1/12 focus-visible:outline-2 focus-visible:outline-tbg15-a1 group-open/more:animate-tbg15-phase [animation-delay:170ms] motion-reduce:animate-none! motion-reduce:opacity-100"><span aria-hidden="true" class="size-2 flex-none rounded-full bg-tbg15-prod"></span><span class="grid"><span class="text-[14.5px] font-semibold">Production</span><span class="font-tbg15-mono text-[11.5px] text-tbg15-mut">acme.com</span></span><span class="ml-auto rounded-md border border-tbg15-prod/40 px-1.5 py-0.5 text-[10.5px] font-semibold text-tbg15-prod">Protected</span></button>
        <div role="separator" class="mx-2 my-1 h-px bg-tbg15-a1/15"></div>
        <button type="button" role="menuitem" class="flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-left text-[14.5px] font-semibold text-tbg15-mut opacity-0 hover:bg-tbg15-a1/12 hover:text-tbg15-ink focus-visible:bg-tbg15-a1/12 focus-visible:outline-2 focus-visible:outline-tbg15-a1 group-open/more:animate-tbg15-phase [animation-delay:230ms] motion-reduce:animate-none! motion-reduce:opacity-100"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12a8 8 0 1 0 2.3-5.6M4 4v4h4"/></svg>Roll back last deploy</button>
      </div>
    </details>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg15-bg: #060810;
  --color-tbg15-glow: #101a2c;
  --color-tbg15-menu: #0e1628;
  --color-tbg15-ink: #dce9f7;
  --color-tbg15-mut: #9bb0c8;
  --color-tbg15-mut: oklch(0.76 0.04 245);
  --color-tbg15-on: #07101c;
  --color-tbg15-a1: #4fd8f0;
  --color-tbg15-a1: oklch(0.82 0.13 205);
  --color-tbg15-a2: #9b6bff;
  --color-tbg15-a2: oklch(0.65 0.2 295);
  --color-tbg15-ok: #4ade80;
  --color-tbg15-warn: #fbbf24;
  --color-tbg15-prod: #fb7185;
  --shadow-tbg15-lift: 0 0 0 1px rgb(120 200 255 / 0.2), 0 20px 50px -24px rgb(30 120 255 / 0.6);
  --shadow-tbg15-menu: 0 30px 60px -24px rgb(20 80 220 / 0.7);
  --font-tbg15-sans: 'Geologica', system-ui, sans-serif;
  --font-tbg15-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbg15-wipe: tbg15-wipe 0.35s cubic-bezier(0.2, 0.7, 0.3, 1) both;
  --animate-tbg15-phase: tbg15-phase 0.4s ease both;

  @keyframes tbg15-wipe {
    from {
      clip-path: inset(0 0 100% 0 round 14px);
      opacity: 0;
    }

    to {
      clip-path: inset(0 0 0 0 round 14px);
      opacity: 1;
    }
  }

  @keyframes tbg15-phase {
    from {
      opacity: 0;
      filter: blur(6px);
      translate: 0 -6px;
    }

    to {
      opacity: 1;
      filter: blur(0);
      translate: 0 0;
    }
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-15 {
  width: 100%;
  min-height: 100svh;
}
```

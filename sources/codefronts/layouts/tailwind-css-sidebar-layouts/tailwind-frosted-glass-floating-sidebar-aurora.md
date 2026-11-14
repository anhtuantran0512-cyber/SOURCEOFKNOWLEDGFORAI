---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-frosted-glass-floating-sidebar-aurora/"
title: "Tailwind Frosted Glass Floating Sidebar with Animated Aurora"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The showpiece: a floating frosted pane over a slowly drifting aurora, with heavy blur and saturation, a light-catching hairline, glass nav pills and a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Frosted Glass Floating Sidebar with Animated Aurora
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-frosted-glass-floating-sidebar-aurora/

The showpiece: a floating frosted pane over a slowly drifting aurora, with heavy blur and saturation, a light-catching hairline, glass nav pills and a glowing gradient CTA &mdash; art-directed to the edge while staying readable, keyboard-navigable and reduced-motion safe.
## HTML
```html
<section class="tsl-30 relative isolate w-full h-svh min-h-svh grid grid-cols-[auto_1fr] overflow-hidden font-tsl30-sans text-tsl30-ink bg-[oklch(0.15_0.03_290)] before:content-[''] before:absolute before:-inset-[30%] before:-z-10 before:pointer-events-none before:bg-[radial-gradient(38%_42%_at_30%_30%,oklch(0.55_0.22_310/0.8),transparent_70%),radial-gradient(34%_38%_at_72%_62%,oklch(0.6_0.18_230/0.7),transparent_70%),radial-gradient(30%_34%_at_50%_85%,oklch(0.65_0.16_180/0.5),transparent_70%)] before:animate-tsl30-drift motion-reduce:before:animate-none">
  <aside aria-label="Portfolio" class="tsl-30-glass w-64 m-5 flex flex-col px-4 py-6 rounded-[22px] border border-transparent backdrop-blur-[22px] backdrop-saturate-[1.8] shadow-[0_12px_40px_oklch(0_0_0/0.35),inset_0_1px_0_rgb(255_255_255/0.2)]">
    <div class="flex items-center gap-[11px] px-2.5 pt-0.5 pb-6 text-base font-bold tracking-[0.01em]"><span aria-hidden="true" class="w-7 h-7 rounded-full bg-[conic-gradient(oklch(0.75_0.16_310),oklch(0.75_0.14_230),oklch(0.78_0.14_180),oklch(0.75_0.16_310))] shadow-[0_0_16px_oklch(0.7_0.18_290/0.6)]"></span>Aurora Studio</div>
    <nav class="flex flex-col gap-1">
      <a href="#" aria-current="page" class="flex items-center min-h-11 px-3.5 rounded-xl text-[14.5px] font-medium text-tsl30-mut no-underline transition-colors duration-200 hover:text-tsl30-ink hover:bg-white/10 aria-[current=page]:text-tsl30-ink aria-[current=page]:bg-white/[0.16] aria-[current=page]:shadow-[inset_0_1px_0_rgb(255_255_255/0.18)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px]">Work</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-xl text-[14.5px] font-medium text-tsl30-mut no-underline transition-colors duration-200 hover:text-tsl30-ink hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px]">About</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-xl text-[14.5px] font-medium text-tsl30-mut no-underline transition-colors duration-200 hover:text-tsl30-ink hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px]">Journal</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-xl text-[14.5px] font-medium text-tsl30-mut no-underline transition-colors duration-200 hover:text-tsl30-ink hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px]">Contact</a>
    </nav>
    <a href="#" class="group mt-auto flex items-center justify-center gap-2.5 min-h-12 rounded-[14px] text-sm font-bold no-underline text-tsl30-onaccent bg-[linear-gradient(120deg,oklch(0.85_0.1_310),oklch(0.87_0.09_220))] shadow-[0_6px_24px_oklch(0.7_0.18_290/0.45)] transition-[translate,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[0_10px_32px_oklch(0.7_0.18_290/0.6)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">Start a project<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-current stroke-[2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-transform duration-200 group-hover:translate-x-[3px] motion-reduce:transition-none motion-reduce:group-hover:translate-x-0"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></a>
  </aside>
  <main class="grid content-center gap-[18px] px-14 py-12">
    <h1 class="text-[clamp(34px,5vw,54px)] font-extrabold leading-[1.08] tracking-[-0.02em] [text-shadow:0_2px_24px_oklch(0_0_0/0.3)]">Design that<br>holds light.</h1>
    <p class="max-w-[46ch] text-[15px] leading-[1.7] text-tsl30-mut text-pretty">A brand &amp; digital studio. The sidebar is one pane of frosted glass over a living aurora &mdash; blur, saturation and a light-catching hairline.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl30-ink: #f7f5fb;
  --color-tsl30-ink: oklch(0.97 0.005 300);
  --color-tsl30-mut: #ccc6d9;
  --color-tsl30-mut: oklch(0.86 0.02 300);
  --color-tsl30-onaccent: #24203a;
  --color-tsl30-onaccent: oklch(0.2 0.04 300);
  --font-tsl30-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-tsl30-drift: tsl30-drift 24s ease-in-out infinite alternate;
}

@keyframes tsl30-drift {
  from {
    transform: translate3d(-3%, -2%, 0) rotate(0deg) scale(1);
  }

  to {
    transform: translate3d(3%, 2%, 0) rotate(4deg) scale(1.08);
  }
}

.tsl-30 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* The lit-glass hairline again (see demo 16): two background layers with
   different clip boxes, the one thing with no utility path. */

.tsl-30-glass {
  background: linear-gradient(rgb(255 255 255 / 0.1), rgb(255 255 255 / 0.08)) padding-box, linear-gradient(155deg, rgb(255 255 255 / 0.6), rgb(255 255 255 / 0.15) 35%, rgb(255 255 255 / 0.04)) border-box;
  -webkit-backdrop-filter: blur(22px) saturate(1.8);
}
```

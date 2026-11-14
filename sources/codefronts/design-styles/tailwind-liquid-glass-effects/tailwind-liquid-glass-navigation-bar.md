---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-navigation-bar/"
title: "Tailwind Liquid Glass Navigation Bar"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A sticky bar that turns into a frosted lens as content scrolls beneath it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Navigation Bar
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-navigation-bar/

A sticky bar that turns into a frosted lens as content scrolls beneath it. The port's payoff is the active state: what was a [aria-current=page] attribute selector in a stylesheet becomes an aria-[current=page]: variant sitting on the link itself, so the pill treatment and the semantics that drive it are one line apart.
## HTML
```html
<section class="lgt-03 relative h-svh min-h-svh w-full overflow-y-auto bg-lgt03-bg font-lgt03-sans" aria-label="Tailwind liquid glass navigation bar">
  <header class="sticky top-0 z-10 flex items-center justify-between gap-5 border-b border-white/25 bg-white/10 px-[clamp(16px,4vw,32px)] py-3.5 backdrop-blur-[20px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_10px_30px_-20px_rgba(0,0,0,.8)]">
    <span class="text-xl font-extrabold tracking-[-0.01em] text-white">Lumen</span>
    <nav class="flex gap-1.5" aria-label="Primary">
      <a href="#lgt-03-scroll" aria-current="page" class="rounded-full px-3.5 py-2 text-sm font-semibold text-white/85 no-underline transition-colors duration-200 hover:bg-white/16 hover:text-white focus-visible:bg-white/16 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white aria-[current=page]:bg-white aria-[current=page]:text-lgt03-bg">Home</a>
      <a href="#lgt-03-scroll" class="rounded-full px-3.5 py-2 text-sm font-semibold text-white/85 no-underline transition-colors duration-200 hover:bg-white/16 hover:text-white focus-visible:bg-white/16 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white aria-[current=page]:bg-white aria-[current=page]:text-lgt03-bg">Work</a>
      <a href="#lgt-03-scroll" class="rounded-full px-3.5 py-2 text-sm font-semibold text-white/85 no-underline transition-colors duration-200 hover:bg-white/16 hover:text-white focus-visible:bg-white/16 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white aria-[current=page]:bg-white aria-[current=page]:text-lgt03-bg">Studio</a>
      <a href="#lgt-03-scroll" class="rounded-full px-3.5 py-2 text-sm font-semibold text-white/85 no-underline transition-colors duration-200 hover:bg-white/16 hover:text-white focus-visible:bg-white/16 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white aria-[current=page]:bg-white aria-[current=page]:text-lgt03-bg">Contact</a>
    </nav>
  </header>
  <div id="lgt-03-scroll" class="mx-auto flex max-w-235 flex-col items-center gap-7 px-[clamp(16px,4vw,40px)] pt-7 pb-30">
    <img src="https://picsum.photos/seed/lgnav-a/900/500" width="900" height="500" alt="Coastline at dawn" class="block h-auto w-full rounded-[18px] shadow-[0_20px_44px_-24px_rgba(0,0,0,.7)]">
    <h3 class="text-center text-2xl font-extrabold text-white">Scroll &mdash; watch content frost under the bar</h3>
    <img src="https://picsum.photos/seed/lgnav-b/900/500" width="900" height="500" alt="City at night" class="block h-auto w-full rounded-[18px] shadow-[0_20px_44px_-24px_rgba(0,0,0,.7)]">
    <p class="max-w-[52ch] text-center text-base leading-relaxed text-white/75">The sticky bar samples and blurs whatever slides beneath it, in real time, on the compositor &mdash; no scroll listener, no JavaScript.</p>
    <img src="https://picsum.photos/seed/lgnav-c/900/500" width="900" height="500" alt="Mountain range" class="block h-auto w-full rounded-[18px] shadow-[0_20px_44px_-24px_rgba(0,0,0,.7)]">
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt03-bg: #0e0b1a;
  --color-lgt03-bg: oklch(0.16 0.03 295);
  --font-lgt03-sans: 'Manrope', system-ui, sans-serif;
}
```

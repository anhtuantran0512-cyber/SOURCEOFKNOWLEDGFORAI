---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-visionos-glass-navbar/"
title: "Tailwind visionOS Glass Navbar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The spatial-computing slab: a dark, heavily frosted panel with a bright specular rim and a deep ambient shadow, tuned so links stay legible over video and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind visionOS Glass Navbar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-visionos-glass-navbar/

The spatial-computing slab: a dark, heavily frosted panel with a bright specular rim and a deep ambient shadow, tuned so links stay legible over video and photography. The port stacks three backdrop-* utilities to compose blur(40px) saturate(140%) brightness(1.05), and keeps the expensive paint boxed in with [contain:layout_paint].
## HTML
```html
<section class="nbtw-04 grid place-items-center w-full min-h-svh p-6 font-nb04-sans bg-[radial-gradient(90%_120%_at_70%_10%,#1b2b4d,#070a14_70%),url('https://picsum.photos/seed/nb04dark/1000/700')] bg-center bg-cover [background-blend-mode:soft-light]" aria-label="visionOS style glass navbar demo">
  <nav class="flex flex-wrap items-center gap-x-5 gap-y-3 w-[min(760px,94%)] px-4.5 py-3.5 rounded-[22px] isolate [contain:layout_paint] text-white bg-[color-mix(in_oklab,black_34%,transparent)] border border-white/[0.16] shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_34px_70px_-26px_rgba(0,0,0,.85)] backdrop-blur-[40px] backdrop-saturate-[1.4] backdrop-brightness-[1.05]" aria-label="Primary">
    <span class="flex items-center gap-2.5 text-[17px] font-extrabold tracking-[-0.01em]">
      <span class="size-3.5 rounded-full bg-[radial-gradient(circle_at_30%_30%,#fff,var(--color-nb04-accent))] shadow-[0_0_14px_var(--color-nb04-accent)]" aria-hidden="true"></span>Horizon
    </span>
    <div class="flex flex-wrap gap-1.5 ms-auto">
      <a class="flex items-center min-h-10 px-[15px] rounded-xl no-underline text-white/[0.86] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.14] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:bg-white/20 aria-[current=page]:text-white" href="#nbtw-04" aria-current="page">Spaces</a>
      <a class="flex items-center min-h-10 px-[15px] rounded-xl no-underline text-white/[0.86] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.14] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-04">Immersive</a>
      <a class="flex items-center min-h-10 px-[15px] rounded-xl no-underline text-white/[0.86] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.14] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-04">Library</a>
      <a class="flex items-center min-h-10 px-[15px] rounded-xl no-underline text-white/[0.86] text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.14] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-04">Shared</a>
    </div>
    <button class="min-h-10 px-5 rounded-xl border border-[color-mix(in_oklab,var(--color-nb04-accent)_50%,white)] bg-[linear-gradient(180deg,color-mix(in_oklab,var(--color-nb04-accent)_80%,white),var(--color-nb04-accent))] text-[#04121a] text-[14.5px] font-bold cursor-pointer transition-transform duration-200 hover:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:transition-none" type="button">Enter</button>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-nb04-accent: #45b8e0;
  --color-nb04-accent: oklch(0.72 0.16 210);
  --font-nb04-sans: system-ui, 'Segoe UI', sans-serif;
}
```

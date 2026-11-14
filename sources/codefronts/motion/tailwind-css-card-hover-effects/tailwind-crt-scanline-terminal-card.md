---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-crt-scanline-terminal-card/"
title: "Tailwind CRT Scanline Terminal Card with Sweeping Beam"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A phosphor-green cold-storage terminal with static scanlines, a refresh beam that sweeps top to bottom, a blinking block cursor and a CRT vignette."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CRT Scanline Terminal Card with Sweeping Beam
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-crt-scanline-terminal-card/

A phosphor-green cold-storage terminal with static scanlines, a refresh beam that sweeps top to bottom, a blinking block cursor and a CRT vignette. Four stacked overlays, two keyframes, and every one of them addressed from the markup.
## HTML
```html
<section class="tch-14 w-full min-h-svh grid place-items-center bg-tch14-bg font-tch14-mono p-8">
  <article tabindex="0" class="group relative w-[340px] h-[430px] rounded-[10px] overflow-hidden cursor-pointer outline-none bg-tch14-card border border-tch14-green/60 shadow-[0_0_25px_rgb(0_255_120/0.12),inset_0_0_30px_rgb(0_255_120/0.05)] focus-visible:outline-2 focus-visible:outline-tch14-green focus-visible:outline-offset-4">
    <div class="relative z-1 h-full p-[2.2rem] flex flex-col justify-between text-tch14-green [text-shadow:0_0_4px_rgb(56_255_142/0.6)]">
      <span class="text-[0.8rem] tracking-[0.1em] opacity-70">&gt; SYSTEM/READY_</span>
      <h2 class="font-tch14-display text-[3.4rem] leading-[0.95]">VAULT<br>OS 9<span class="inline-block w-[0.6ch] bg-tch14-green animate-tch14-blink motion-reduce:animate-none">&nbsp;</span></h2>
      <p class="text-[0.85rem] leading-[1.6] opacity-85">Cold-storage terminal for archival data. Phosphor-green display, zero network exposure.</p>
      <div class="flex justify-between text-[0.75rem] border-t border-dashed border-tch14-green/40 pt-3 opacity-70"><span>UPTIME 4096d</span><span>MEM 64K OK</span></div>
    </div>
    <div class="absolute inset-0 z-2 pointer-events-none bg-[repeating-linear-gradient(0deg,rgb(0_0_0/0.25)_0_1px,transparent_1px_3px)]"></div>
    <div class="absolute inset-x-0 -top-20 h-20 z-3 pointer-events-none opacity-0 transition-opacity duration-300 bg-linear-to-b from-transparent via-tch14-green/20 to-transparent group-hover:opacity-100 group-hover:animate-tch14-sweep group-focus-visible:opacity-100 group-focus-visible:animate-tch14-sweep motion-reduce:animate-none motion-reduce:group-hover:animate-none"></div>
    <div class="absolute inset-0 z-4 pointer-events-none bg-[radial-gradient(ellipse_at_center,transparent_60%,rgb(0_0_0/0.5))]"></div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@keyframes tch14-sweep {
  0% {
    top: -80px;
  }

  100% {
    top: 100%;
  }
}

@keyframes tch14-blink {
  50% {
    opacity: 0;
  }
}

@theme {
  --color-tch14-bg: #04110a;
  --color-tch14-bg: oklch(0.14 0.03 155);
  --color-tch14-card: #021006;
  --color-tch14-card: oklch(0.12 0.03 155);
  --color-tch14-green: #38ff8e;
  --color-tch14-green: oklch(0.88 0.21 152);
  --font-tch14-mono: 'Share Tech Mono', ui-monospace, monospace;
  --font-tch14-display: 'VT323', ui-monospace, monospace;
  --animate-tch14-sweep: tch14-sweep 2s linear infinite;
  --animate-tch14-blink: tch14-blink 1s steps(1) infinite;
}

.tch-14 {
  width: 100%;
  min-height: 100svh;
}
```

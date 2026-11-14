---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-neon-glow-text-with-flicker-animation/"
title: "Tailwind Neon Glow Text with Flicker Animation"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A bar sign that ignites when you hover it: unlit glass tubes sputter on with a steps(1) keyframe, then hold a five-layer glow from v4's text-shadow-* theme…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Glow Text with Flicker Animation
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-neon-glow-text-with-flicker-animation/

A bar sign that ignites when you hover it: unlit glass tubes sputter on with a steps(1) keyframe, then hold a five-layer glow from v4's text-shadow-* theme namespace. The faulty W keeps buzzing, and the pill outline lights 180ms after the letters. One aria-label speaks the whole sign.
## HTML
```html
<section class="tth-07 w-full min-h-svh grid place-items-center bg-tth07-wall bg-[radial-gradient(80%_60%_at_50%_38%,var(--color-tth07-glow),var(--color-tth07-wall)_72%)] px-5 py-14 font-tth07-sans text-tth07-ink" aria-label="Neon flicker text demo">
  <div class="flex flex-col items-center gap-[clamp(22px,4vw,34px)] text-center">
    <a id="tth07-top" href="#tth07-top" aria-label="Night Owl — cocktails till 3 a.m." class="group/sign flex flex-col items-center gap-[clamp(8px,1.6vw,14px)] rounded-[22px] border border-white/5 bg-black/20 px-[clamp(26px,5vw,52px)] py-[clamp(20px,4vw,36px)] no-underline shadow-[inset_0_0_60px_oklch(0_0_0/0.4)] focus-visible:outline-2 focus-visible:outline-offset-[6px] focus-visible:outline-tth07-tube">
      <span aria-hidden="true" class="block font-tth07-neon text-[clamp(52px,12vw,120px)] leading-[0.95] tracking-[0.06em] text-tth07-off [text-shadow:0_0_0.1em_color-mix(in_oklch,var(--color-tth07-tube)_18%,transparent)] transition-[color,text-shadow] duration-450 group-hover/sign:text-tth07-lit group-hover/sign:text-shadow-tth07-cyan group-hover/sign:animate-tth07-ignite group-focus-visible/sign:text-tth07-lit group-focus-visible/sign:text-shadow-tth07-cyan pointer-coarse:text-tth07-lit pointer-coarse:text-shadow-tth07-cyan motion-reduce:animate-none!">NIGHT</span>
      <span aria-hidden="true" class="block font-tth07-neon text-[clamp(52px,12vw,120px)] leading-[0.95] tracking-[0.06em] text-tth07-off2 [text-shadow:0_0_0.1em_color-mix(in_oklch,var(--color-tth07-tube2)_18%,transparent)] transition-[color,text-shadow] duration-450 group-hover/sign:text-tth07-lit2 group-hover/sign:text-shadow-tth07-pink group-hover/sign:animate-tth07-ignite-slow group-focus-visible/sign:text-tth07-lit2 group-focus-visible/sign:text-shadow-tth07-pink pointer-coarse:text-tth07-lit2 pointer-coarse:text-shadow-tth07-pink motion-reduce:animate-none!">O<i class="not-italic animate-tth07-buzz-off group-hover/sign:animate-tth07-buzz-on motion-reduce:animate-none!">W</i>L</span>
      <span aria-hidden="true" class="mt-1.5 rounded-full border-2 border-tth07-off2/60 px-[22px] py-2.5 text-[clamp(13px,2vw,17px)] font-bold lowercase tracking-[0.22em] text-tth07-off2 transition-[color,border-color,box-shadow,text-shadow] duration-500 group-hover/sign:border-tth07-tube2 group-hover/sign:text-tth07-lit2 group-hover/sign:delay-180 group-hover/sign:[text-shadow:0_0_0.3em_var(--color-tth07-tube2)] group-hover/sign:shadow-[0_0_0.6em_color-mix(in_oklch,var(--color-tth07-tube2)_55%,transparent),inset_0_0_0.5em_color-mix(in_oklch,var(--color-tth07-tube2)_35%,transparent)] group-focus-visible/sign:border-tth07-tube2 group-focus-visible/sign:text-tth07-lit2">cocktails &middot; til 3 a.m.</span>
    </a>
    <p class="max-w-[52ch] text-[12.5px] leading-[1.7] text-tth07-mut">Hover the sign and hold &mdash; ignition is a <code class="rounded bg-tth07-chip px-1.5 py-px font-tth07-mono text-[0.92em] text-tth07-tube">steps(1)</code> sputter, the glow is a five-layer <code class="rounded bg-tth07-chip px-1.5 py-px font-tth07-mono text-[0.92em] text-tth07-tube">text-shadow-*</code> token, and the W was always going to be the problem.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth07-wall: #150f18;
  --color-tth07-wall: oklch(0.16 0.012 310);
  --color-tth07-glow: #1e1622;
  --color-tth07-glow: oklch(0.21 0.022 310);
  --color-tth07-chip: #251d29;
  --color-tth07-chip: oklch(0.24 0.015 310);
  --color-tth07-ink: #ece6ef;
  --color-tth07-ink: oklch(0.93 0.01 300);
  --color-tth07-mut: #a59bab;
  --color-tth07-mut: oklch(0.72 0.02 300);
  --color-tth07-tube: #4fdbe6;
  --color-tth07-tube: oklch(0.83 0.14 195);
  --color-tth07-tube2: #f25ba6;
  --color-tth07-tube2: oklch(0.73 0.21 350);
  --color-tth07-off: #4a5a62;
  --color-tth07-off: oklch(0.44 0.03 220);
  --color-tth07-off2: #6f4155;
  --color-tth07-off2: oklch(0.44 0.07 350);
  --color-tth07-lit: #e8fbfd;
  --color-tth07-lit: oklch(0.97 0.03 195);
  --color-tth07-lit2: #fde0ee;
  --color-tth07-lit2: oklch(0.94 0.06 350);
  --font-tth07-neon: 'Tilt Neon', ui-rounded, system-ui, sans-serif;
  --font-tth07-sans: 'Outfit', system-ui, sans-serif;
  --font-tth07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --text-shadow-tth07-cyan: 0 0 0.03em oklch(1 0 0 / 0.9), 0 0 0.12em var(--color-tth07-tube), 0 0 0.35em var(--color-tth07-tube), 0 0 0.85em color-mix(in oklch, var(--color-tth07-tube) 65%, transparent), 0 0 1.6em color-mix(in oklch, var(--color-tth07-tube) 40%, transparent);
  --text-shadow-tth07-pink: 0 0 0.03em oklch(1 0 0 / 0.9), 0 0 0.12em var(--color-tth07-tube2), 0 0 0.35em var(--color-tth07-tube2), 0 0 0.85em color-mix(in oklch, var(--color-tth07-tube2) 65%, transparent), 0 0 1.6em color-mix(in oklch, var(--color-tth07-tube2) 40%, transparent);
  --animate-tth07-ignite: tth07-ignite 0.95s steps(1, end);
  --animate-tth07-ignite-slow: tth07-ignite 1.15s steps(1, end);
  --animate-tth07-buzz-off: tth07-buzz-off 5s steps(1, end) infinite;
  --animate-tth07-buzz-on: tth07-buzz-on 3.2s steps(1, end) infinite;

  @keyframes tth07-ignite {
    0%,
        9%,
        24%,
        56% {
      text-shadow: none;
      opacity: 0.4;
    }

    5%,
        12%,
        28%,
        54%,
        60%,
        100% {
      opacity: 1;
    }
  }

  @keyframes tth07-buzz-off {
    0%,
        100% {
      opacity: 1;
    }

    7%,
        9.5%,
        42% {
      opacity: 0.55;
    }

    8%,
        43.5%,
        71% {
      opacity: 1;
    }

    70% {
      opacity: 0.7;
    }
  }

  @keyframes tth07-buzz-on {
    0%,
        100% {
      opacity: 1;
    }

    11%,
        13%,
        57%,
        58.6% {
      opacity: 0.5;
    }

    12%,
        14%,
        58%,
        60% {
      opacity: 1;
    }
  }
}

.tth-07 {
  width: 100%;
  min-height: 100svh;
}
```

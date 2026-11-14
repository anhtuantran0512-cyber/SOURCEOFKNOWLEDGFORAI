---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-y2k-aqua-gloss-interface-kit/"
title: "Tailwind Y2K Aqua Gloss Interface Kit"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "The early-2000s gel look, built correctly: glossy pill buttons, translucent panels over a pinstriped ground, and a candy-stripe progress bar that flows."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Y2K Aqua Gloss Interface Kit
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-y2k-aqua-gloss-interface-kit/

The early-2000s gel look, built correctly: glossy pill buttons, translucent panels over a pinstriped ground, and a candy-stripe progress bar that flows. The gloss is the interesting part &mdash; four separate highlights, not one gradient &mdash; and in utilities it becomes a before:/after: pair on the button itself, which is the clearest the technique has ever looked.
## HTML
```html
<section class="twr-18 relative block w-full min-h-svh box-border bg-twr18-bg text-twr18-ink font-twr18-sans [background-image:repeating-linear-gradient(180deg,var(--color-twr18-stripe)_0_1px,rgba(255,255,255,0)_1px_4px)]" aria-labelledby="twr-18-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-18-title">Y2K aqua gloss interface kit</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-18-theme">
    <label class="grid place-items-center size-11 rounded-full cursor-pointer bg-twr18-surface text-twr18-ink2 border border-white/70 [box-shadow:inset_0_1px_0_rgba(255,255,255,0.9),0_4px_10px_-6px_rgba(11,91,166,0.6)] peer-focus-visible:outline-2 peer-focus-visible:outline-twr18-acc peer-focus-visible:outline-offset-2" for="twr-18-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-5 max-w-[68rem] mx-auto px-[clamp(0.85rem,0.5rem+2vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <header class="min-w-0 grid gap-1.5">
      <p class="m-0 font-twr18-mono text-[0.68rem] tracking-[0.16em] uppercase text-twr18-ink2">Gel surfaces &middot; four light events per control</p>
      <h3 class="m-0 min-w-0 font-bold tracking-[-0.02em] text-[clamp(1.6rem,1.2rem+2.4vw,2.6rem)] text-twr18-geld">Aqua Kit</h3>
    </header>

    <div class="grid gap-5 grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]">
      <article class="min-w-0 grid content-start gap-3.5 rounded-xl border border-white/70 bg-twr18-surface/85 p-[clamp(0.9rem,0.6rem+1.2vw,1.4rem)] [box-shadow:inset_0_1px_0_rgba(255,255,255,0.9),0_10px_26px_-16px_rgba(11,91,166,0.55)]" aria-labelledby="twr-18-p1">
        <h4 class="m-0 text-[0.72rem] tracking-[0.14em] uppercase text-twr18-ink2" id="twr-18-p1">Pill buttons</h4>
        <div class="flex flex-wrap gap-3">
          <button class="relative min-h-11 px-6 py-2.5 rounded-full border-0 cursor-pointer font-inherit text-[0.88rem] font-semibold text-white overflow-hidden [text-shadow:0_1px_1px_rgba(0,0,0,0.35)] before:content-[''] before:absolute before:inset-x-1.5 before:top-1 before:h-[42%] before:rounded-[999px] before:bg-[linear-gradient(180deg,rgba(255,255,255,0.9),rgba(255,255,255,0.15))] before:pointer-events-none after:content-[''] after:absolute after:inset-x-2 after:bottom-0.5 after:h-[30%] after:rounded-[999px] after:bg-[linear-gradient(0deg,rgba(255,255,255,0.45),rgba(255,255,255,0))] after:pointer-events-none active:translate-y-px focus-visible:outline-2 focus-visible:outline-twr18-acc focus-visible:outline-offset-2 bg-twr18-gel [box-shadow:inset_0_-4px_8px_rgba(0,0,0,0.28),0_0_0_1px_rgba(11,91,166,0.55),0_8px_16px_-10px_rgba(11,91,166,0.8)]" type="button">Continue</button>
          <button class="relative min-h-11 px-6 py-2.5 rounded-full border-0 cursor-pointer font-inherit text-[0.88rem] font-semibold text-white overflow-hidden [text-shadow:0_1px_1px_rgba(0,0,0,0.35)] before:content-[''] before:absolute before:inset-x-1.5 before:top-1 before:h-[42%] before:rounded-[999px] before:bg-[linear-gradient(180deg,rgba(255,255,255,0.9),rgba(255,255,255,0.15))] before:pointer-events-none after:content-[''] after:absolute after:inset-x-2 after:bottom-0.5 after:h-[30%] after:rounded-[999px] after:bg-[linear-gradient(0deg,rgba(255,255,255,0.45),rgba(255,255,255,0))] after:pointer-events-none active:translate-y-px focus-visible:outline-2 focus-visible:outline-twr18-acc focus-visible:outline-offset-2 bg-twr18-green [box-shadow:inset_0_-4px_8px_rgba(0,0,0,0.28),0_0_0_1px_rgba(33,109,16,0.55),0_8px_16px_-10px_rgba(33,109,16,0.8)]" type="button">Install</button>
          <button class="relative min-h-11 px-6 py-2.5 rounded-full border-0 cursor-pointer font-inherit text-[0.88rem] font-semibold text-white overflow-hidden [text-shadow:0_1px_1px_rgba(0,0,0,0.35)] before:content-[''] before:absolute before:inset-x-1.5 before:top-1 before:h-[42%] before:rounded-[999px] before:bg-[linear-gradient(180deg,rgba(255,255,255,0.9),rgba(255,255,255,0.15))] before:pointer-events-none after:content-[''] after:absolute after:inset-x-2 after:bottom-0.5 after:h-[30%] after:rounded-[999px] after:bg-[linear-gradient(0deg,rgba(255,255,255,0.45),rgba(255,255,255,0))] after:pointer-events-none active:translate-y-px focus-visible:outline-2 focus-visible:outline-twr18-acc focus-visible:outline-offset-2 bg-twr18-red [box-shadow:inset_0_-4px_8px_rgba(0,0,0,0.28),0_0_0_1px_rgba(163,38,15,0.55),0_8px_16px_-10px_rgba(163,38,15,0.8)]" type="button">Cancel</button>
        </div>
        <div class="flex flex-wrap gap-3">
          <button class="relative grid place-items-center size-12 rounded-full border-0 cursor-pointer overflow-hidden [box-shadow:inset_0_-3px_6px_rgba(0,0,0,0.3),inset_0_2px_2px_rgba(255,255,255,0.55),0_0_0_1px_rgba(0,0,0,0.18),0_6px_10px_-6px_rgba(0,0,0,0.5)] before:content-[''] before:absolute before:inset-x-1.5 before:top-1 before:h-[38%] before:rounded-[999px] before:bg-[linear-gradient(180deg,rgba(255,255,255,0.95),rgba(255,255,255,0.1))] before:pointer-events-none active:translate-y-px focus-visible:outline-2 focus-visible:outline-twr18-acc focus-visible:outline-offset-2 bg-twr18-gel" type="button" aria-label="Play"><span class="relative z-1 block size-3 bg-white [clip-path:polygon(0_0,100%_50%,0_100%)]" aria-hidden="true"></span></button>
          <button class="relative grid place-items-center size-12 rounded-full border-0 cursor-pointer overflow-hidden [box-shadow:inset_0_-3px_6px_rgba(0,0,0,0.3),inset_0_2px_2px_rgba(255,255,255,0.55),0_0_0_1px_rgba(0,0,0,0.18),0_6px_10px_-6px_rgba(0,0,0,0.5)] before:content-[''] before:absolute before:inset-x-1.5 before:top-1 before:h-[38%] before:rounded-[999px] before:bg-[linear-gradient(180deg,rgba(255,255,255,0.95),rgba(255,255,255,0.1))] before:pointer-events-none active:translate-y-px focus-visible:outline-2 focus-visible:outline-twr18-acc focus-visible:outline-offset-2 bg-twr18-green" type="button" aria-label="Stop"><span class="relative z-1 block size-3 bg-white" aria-hidden="true"></span></button>
          <button class="relative grid place-items-center size-12 rounded-full border-0 cursor-pointer overflow-hidden [box-shadow:inset_0_-3px_6px_rgba(0,0,0,0.3),inset_0_2px_2px_rgba(255,255,255,0.55),0_0_0_1px_rgba(0,0,0,0.18),0_6px_10px_-6px_rgba(0,0,0,0.5)] before:content-[''] before:absolute before:inset-x-1.5 before:top-1 before:h-[38%] before:rounded-[999px] before:bg-[linear-gradient(180deg,rgba(255,255,255,0.95),rgba(255,255,255,0.1))] before:pointer-events-none active:translate-y-px focus-visible:outline-2 focus-visible:outline-twr18-acc focus-visible:outline-offset-2 bg-twr18-red" type="button" aria-label="Eject"><span class="relative z-1 block size-3 bg-white [clip-path:polygon(50%_0,100%_100%,0_100%)]" aria-hidden="true"></span></button>
        </div>
        <p class="m-0 min-w-0 text-[0.78rem] leading-relaxed text-pretty text-twr18-ink2">Specular cap, bounce light, rim light, contact shadow. Four layers, one surface.</p>
      </article>

      <article class="min-w-0 grid content-start gap-3.5 rounded-xl border border-white/70 bg-twr18-surface/85 p-[clamp(0.9rem,0.6rem+1.2vw,1.4rem)] [box-shadow:inset_0_1px_0_rgba(255,255,255,0.9),0_10px_26px_-16px_rgba(11,91,166,0.55)] supports-[backdrop-filter]:bg-twr18-surface/60 supports-[backdrop-filter]:backdrop-blur-md" aria-labelledby="twr-18-p2">
        <h4 class="m-0 text-[0.72rem] tracking-[0.14em] uppercase text-twr18-ink2" id="twr-18-p2">Progress</h4>
        <div class="relative h-4 min-w-0 rounded-full overflow-hidden bg-[#dfe7ee] [box-shadow:inset_0_2px_4px_rgba(11,32,50,0.25)]" role="progressbar" aria-valuenow="68" aria-valuemin="0" aria-valuemax="100" aria-label="Installing, 68 percent">
          <span class="block h-full rounded-full [width:68%] bg-twr18-gel [background-image:repeating-linear-gradient(45deg,rgba(255,255,255,0.45)_0_10px,rgba(255,255,255,0)_10px_20px)] [background-size:28px_28px] animate-twr18-flow motion-reduce:animate-none [box-shadow:inset_0_1px_0_rgba(255,255,255,0.75),inset_0_-3px_6px_rgba(0,0,0,0.22)]"></span>
        </div>
        <p class="m-0 font-twr18-mono text-[0.72rem] tabular-nums text-twr18-ink2">Installing components &mdash; 68%</p>
        <div class="relative h-4 min-w-0 rounded-full overflow-hidden bg-[#dfe7ee] [box-shadow:inset_0_2px_4px_rgba(11,32,50,0.25)]" role="progressbar" aria-valuenow="24" aria-valuemin="0" aria-valuemax="100" aria-label="Downloading, 24 percent">
          <span class="block h-full rounded-full [width:24%] bg-twr18-gel [background-image:repeating-linear-gradient(45deg,rgba(255,255,255,0.45)_0_10px,rgba(255,255,255,0)_10px_20px)] [background-size:28px_28px] animate-twr18-flow motion-reduce:animate-none [box-shadow:inset_0_1px_0_rgba(255,255,255,0.75),inset_0_-3px_6px_rgba(0,0,0,0.22)]"></span>
        </div>
        <p class="m-0 font-twr18-mono text-[0.72rem] tabular-nums text-twr18-ink2">Downloading &mdash; 24%</p>
        <p class="m-0 min-w-0 text-[0.78rem] leading-relaxed text-pretty text-twr18-ink2">This panel is opaque by default and only becomes translucent under <code class="font-twr18-mono">supports-[backdrop-filter]</code>.</p>
      </article>

      <article class="min-w-0 grid content-start gap-3.5 rounded-xl border border-white/70 bg-twr18-surface/85 p-[clamp(0.9rem,0.6rem+1.2vw,1.4rem)] [box-shadow:inset_0_1px_0_rgba(255,255,255,0.9),0_10px_26px_-16px_rgba(11,91,166,0.55)]" aria-labelledby="twr-18-p3">
        <h4 class="m-0 text-[0.72rem] tracking-[0.14em] uppercase text-twr18-ink2" id="twr-18-p3">Toggles and tabs</h4>
        <div class="flex flex-wrap gap-3">
          <span class="relative inline-flex">
            <input class="peer absolute size-px opacity-0 m-0" type="checkbox" id="twr-18-t1" checked>
            <label class="flex items-center gap-2.5 min-h-11 px-3 py-2 rounded-full cursor-pointer text-[0.82rem] font-semibold bg-white/70 [box-shadow:inset_0_1px_0_rgba(255,255,255,0.9),0_0_0_1px_rgba(11,91,166,0.25)] peer-checked:[&_[data-knob]]:translate-x-5 peer-checked:[&_[data-track]]:bg-twr18-gel peer-focus-visible:outline-2 peer-focus-visible:outline-twr18-acc peer-focus-visible:outline-offset-2" for="twr-18-t1">
              <span class="block w-11 h-6 p-0.5 rounded-full bg-[#cfdae4] transition-colors duration-150 [box-shadow:inset_0_2px_4px_rgba(11,32,50,0.28)]" data-track><span class="block size-5 rounded-full bg-white transition-transform duration-150 [box-shadow:0_1px_2px_rgba(0,0,0,0.35)]" data-knob aria-hidden="true"></span></span>Sound
            </label>
          </span>
          <span class="relative inline-flex">
            <input class="peer absolute size-px opacity-0 m-0" type="checkbox" id="twr-18-t2">
            <label class="flex items-center gap-2.5 min-h-11 px-3 py-2 rounded-full cursor-pointer text-[0.82rem] font-semibold bg-white/70 [box-shadow:inset_0_1px_0_rgba(255,255,255,0.9),0_0_0_1px_rgba(11,91,166,0.25)] peer-checked:[&_[data-knob]]:translate-x-5 peer-checked:[&_[data-track]]:bg-twr18-gel peer-focus-visible:outline-2 peer-focus-visible:outline-twr18-acc peer-focus-visible:outline-offset-2" for="twr-18-t2">
              <span class="block w-11 h-6 p-0.5 rounded-full bg-[#cfdae4] transition-colors duration-150 [box-shadow:inset_0_2px_4px_rgba(11,32,50,0.28)]" data-track><span class="block size-5 rounded-full bg-white transition-transform duration-150 [box-shadow:0_1px_2px_rgba(0,0,0,0.35)]" data-knob aria-hidden="true"></span></span>Shuffle
            </label>
          </span>
        </div>
        <div class="flex min-w-0 rounded-full overflow-hidden [box-shadow:inset_0_1px_0_rgba(255,255,255,0.8),0_0_0_1px_rgba(11,91,166,0.3)]" role="tablist" aria-label="Library view">
          <button class="min-h-11 px-4 py-2 border-0 cursor-pointer font-inherit text-[0.8rem] font-semibold first:rounded-s-full last:rounded-e-full focus-visible:outline-2 focus-visible:outline-twr18-acc focus-visible:outline-offset-2 bg-twr18-gel text-white [text-shadow:0_1px_1px_rgba(0,0,0,0.35)]" type="button" role="tab" aria-selected="true">Albums</button>
          <button class="min-h-11 px-4 py-2 border-0 cursor-pointer font-inherit text-[0.8rem] font-semibold first:rounded-s-full last:rounded-e-full focus-visible:outline-2 focus-visible:outline-twr18-acc focus-visible:outline-offset-2 bg-white/70 text-twr18-ink" type="button" role="tab" aria-selected="false">Artists</button>
          <button class="min-h-11 px-4 py-2 border-0 cursor-pointer font-inherit text-[0.8rem] font-semibold first:rounded-s-full last:rounded-e-full focus-visible:outline-2 focus-visible:outline-twr18-acc focus-visible:outline-offset-2 bg-white/70 text-twr18-ink" type="button" role="tab" aria-selected="false">Genres</button>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr18-gel: #2f97e8;
  --color-twr18-geld: #0b5ba6;
  --color-twr18-gell: #a9defc;
  --color-twr18-green: #4fb62f;
  --color-twr18-red: #e8543a;
  --color-twr18-bg: #eef3f8;
  --color-twr18-bg: oklch(0.96 0.011 240);
  --color-twr18-stripe: #e3ebf3;
  --color-twr18-surface: #ffffff;
  --color-twr18-ink: #14202b;
  --color-twr18-ink: oklch(0.21 0.02 245);
  --color-twr18-ink2: #4a5a68;
  --color-twr18-ink2: oklch(0.45 0.02 245);
  --color-twr18-acc: #0b5ba6;
  --color-twr18-acc: oklch(0.45 0.15 245);
  --font-twr18-sans: 'Nunito', ui-rounded, 'Lucida Grande', 'Segoe UI', system-ui, sans-serif;
  --font-twr18-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --animate-twr18-flow: twr-18-flow 1.1s linear infinite;
}

@keyframes twr-18-flow {
  from {
    background-position: 0 0;
  }

  to {
    background-position: 28px 0;
  }
}

.twr-18:has(#twr-18-theme:checked) {
  --color-twr18-bg: #101821;
  --color-twr18-bg: oklch(0.20 0.02 245);
  --color-twr18-stripe: #16202b;
  --color-twr18-surface: #1c2836;
  --color-twr18-ink: #eaf2f8;
  --color-twr18-ink: oklch(0.95 0.008 245);
  --color-twr18-ink2: #a8b8c6;
  --color-twr18-ink2: oklch(0.76 0.015 245);
  --color-twr18-acc: #8fd0ff;
  --color-twr18-acc: oklch(0.82 0.11 245);
}
```

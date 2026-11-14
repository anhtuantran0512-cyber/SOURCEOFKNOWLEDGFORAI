---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-retro-futuristic-terminal-interface/"
title: "Tailwind Retro Futuristic Terminal Interface"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A command console that boots: staggered POST lines, a typed command and a live status column, all under the CRT treatment from demo 01."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Retro Futuristic Terminal Interface
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-retro-futuristic-terminal-interface/

A command console that boots: staggered POST lines, a typed command and a live status column, all under the CRT treatment from demo 01. The boot reveal is pure CSS with the text in the DOM from the start &mdash; and in utilities the stagger becomes something you can read off each line, because every line carries its own [animation-delay:...].
## HTML
```html
<section class="twr-10 relative block w-full min-h-svh box-border bg-twr10-bg text-twr10-ink font-twr10-mono" aria-labelledby="twr-10-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-10-title">Retro futuristic terminal console</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-10-theme">
    <label class="grid place-items-center size-11 rounded border border-twr10-line bg-twr10-surface text-twr10-ink2 cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-twr10-acc peer-focus-visible:outline-offset-2" for="twr-10-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle light surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-4 max-w-[76rem] mx-auto px-[clamp(0.6rem,0.4rem+1.5vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <p class="m-0 justify-self-start min-w-0 rounded-[3px] border border-twr10-line px-2.5 py-1.5 text-[0.68rem] tracking-[0.14em] uppercase text-twr10-ink2">DEC VT-series &middot; 80-column serial console</p>

    <div class="min-w-0 rounded-[34px] bg-[#23282b] p-[clamp(0.7rem,0.5rem+1.2vw,1.3rem)] [box-shadow:inset_0_2px_0_rgba(255,255,255,0.18),inset_0_-3px_0_rgba(0,0,0,0.55),0_20px_44px_-22px_rgba(0,0,0,0.8)]">
      <div class="relative isolate overflow-hidden rounded-[var(--twr-10-curve)] p-[clamp(0.9rem,0.6rem+1.6vw,1.8rem)] [background:radial-gradient(120%_100%_at_50%_42%,#082018_0%,var(--color-twr10-tube)_76%)] [box-shadow:inset_0_0_0_2px_#04100b,inset_0_0_32px_8px_rgba(0,0,0,0.8)]">
        <div class="relative z-2 grid grid-cols-[minmax(0,1fr)] gap-5 md:grid-cols-[minmax(0,1fr)_minmax(0,15rem)]">
          <div class="min-w-0 grid content-start gap-3.5">
            <h3 class="m-0 min-w-0 font-bold tracking-[0.16em] text-twr10-fg text-[clamp(0.95rem,0.75rem+1.2vw,1.35rem)] [text-shadow:0_0_6px_rgba(125,250,176,0.55)]">ORION-7 SYSTEM CONSOLE</h3>
            <ol class="list-none m-0 p-0 grid gap-1 min-w-0 text-twr10-fgdim text-[clamp(0.66rem,0.55rem+0.65vw,0.85rem)]">
              <li class="min-w-0 [overflow-wrap:anywhere] opacity-0 animate-twr10-in [animation-delay:calc(0*140ms)] motion-reduce:animate-none motion-reduce:opacity-100" style="--twr-10-i: 0">POST . . . . . . . . . . . . . <b class="font-bold text-twr10-fg">OK</b></li>
              <li class="min-w-0 [overflow-wrap:anywhere] opacity-0 animate-twr10-in [animation-delay:calc(1*140ms)] motion-reduce:animate-none motion-reduce:opacity-100" style="--twr-10-i: 1">CPU 0 &nbsp;33 MHz &nbsp;CACHE 8K &nbsp; <b class="font-bold text-twr10-fg">OK</b></li>
              <li class="min-w-0 [overflow-wrap:anywhere] opacity-0 animate-twr10-in [animation-delay:calc(2*140ms)] motion-reduce:animate-none motion-reduce:opacity-100" style="--twr-10-i: 2">RAM 0000&mdash;FFFF &nbsp;16384K &nbsp; <b class="font-bold text-twr10-fg">OK</b></li>
              <li class="min-w-0 [overflow-wrap:anywhere] opacity-0 animate-twr10-in [animation-delay:calc(3*140ms)] motion-reduce:animate-none motion-reduce:opacity-100" style="--twr-10-i: 3">CONTROLLER SCSI ID 7 . . . . . <b class="font-bold text-twr10-fg">OK</b></li>
              <li class="min-w-0 [overflow-wrap:anywhere] opacity-0 animate-twr10-in [animation-delay:calc(4*140ms)] motion-reduce:animate-none motion-reduce:opacity-100" style="--twr-10-i: 4">MOUNT /dev/rd0 &nbsp;READ ONLY &nbsp;<b class="font-bold text-twr10-fg">OK</b></li>
              <li class="min-w-0 [overflow-wrap:anywhere] opacity-0 animate-twr10-in [animation-delay:calc(5*140ms)] motion-reduce:animate-none motion-reduce:opacity-100" style="--twr-10-i: 5">LINK ETH0 &nbsp;10BASE-T &nbsp; . . <b class="font-bold text-twr10-fg">UP</b></li>
              <li class="min-w-0 [overflow-wrap:anywhere] opacity-0 animate-twr10-in [animation-delay:calc(6*140ms)] motion-reduce:animate-none motion-reduce:opacity-100" style="--twr-10-i: 6">CLOCK SYNC &nbsp;DRIFT 0.004s . <b class="font-bold text-twr10-fg">OK</b></li>
              <li class="min-w-0 [overflow-wrap:anywhere] opacity-0 animate-twr10-in [animation-delay:calc(7*140ms)] motion-reduce:animate-none motion-reduce:opacity-100" style="--twr-10-i: 7">SENSOR 4 &nbsp;OUT OF RANGE . . <b class="font-bold text-twr10-warn">CHECK</b></li>
              <li class="min-w-0 [overflow-wrap:anywhere] opacity-0 animate-twr10-in [animation-delay:calc(8*140ms)] motion-reduce:animate-none motion-reduce:opacity-100" style="--twr-10-i: 8">KERNEL 2.0.34 &nbsp;LOADED . . . <b class="font-bold text-twr10-fg">OK</b></li>
            </ol>
            <p class="m-0 flex flex-wrap items-center gap-x-[0.5ch] min-w-0 text-twr10-fg text-[clamp(0.7rem,0.58rem+0.7vw,0.9rem)]">
              <span class="text-twr10-acc">orion:~$</span>
              <span class="inline-block w-0 overflow-hidden whitespace-nowrap animate-twr10-type motion-reduce:animate-none motion-reduce:w-[22ch]">status --all --verbose</span>
              <span class="inline-block w-[0.6em] h-[1.1em] bg-twr10-fg animate-twr10-blink motion-reduce:animate-none" aria-hidden="true"></span>
            </p>
          </div>

          <aside class="min-w-0 grid content-start gap-2.5 rounded border border-[rgba(125,250,176,0.28)] bg-[rgba(125,250,176,0.04)] px-3.5 py-3" aria-label="System status">
            <h4 class="m-0 text-[0.66rem] tracking-[0.2em] text-twr10-acc">STATUS</h4>
            <dl class="m-0 grid gap-1 text-[0.72rem] text-twr10-fgdim">
              <div class="flex justify-between gap-3 min-w-0"><dt class="m-0">LOAD</dt><dd class="m-0 tabular-nums text-twr10-fg">0.42</dd></div>
              <div class="flex justify-between gap-3 min-w-0"><dt class="m-0">MEM</dt><dd class="m-0 tabular-nums text-twr10-fg">11208K</dd></div>
              <div class="flex justify-between gap-3 min-w-0"><dt class="m-0">SWAP</dt><dd class="m-0 tabular-nums text-twr10-fg">0K</dd></div>
              <div class="flex justify-between gap-3 min-w-0"><dt class="m-0">PROC</dt><dd class="m-0 tabular-nums text-twr10-fg">37</dd></div>
              <div class="flex justify-between gap-3 min-w-0"><dt class="m-0">UPTIME</dt><dd class="m-0 tabular-nums text-twr10-fg">04:11</dd></div>
              <div class="flex justify-between gap-3 min-w-0"><dt class="m-0">TEMP</dt><dd class="m-0 tabular-nums text-twr10-fg">41C</dd></div>
            </dl>
            <div class="flex items-center gap-2 min-w-0 text-[0.7rem] text-twr10-fgdim" role="img" aria-label="Bus utilisation, 62 percent">
              <span>BUS</span>
              <span class="flex-1 min-w-0 h-2.5 p-px border border-[rgba(125,250,176,0.4)]"><span class="block h-full w-[62%] [background:repeating-linear-gradient(90deg,var(--color-twr10-fg)_0_4px,rgba(0,0,0,0)_4px_6px)]"></span></span>
              <span class="tabular-nums text-twr10-fg">62%</span>
            </div>
          </aside>
        </div>

        <div class="twr-10__scan absolute inset-0 z-4 pointer-events-none opacity-50 [background:repeating-linear-gradient(to_bottom,rgba(0,0,0,0)_0,rgba(0,0,0,0)_calc(var(--twr-10-scan)-1px),rgba(0,0,0,0.7)_calc(var(--twr-10-scan)-1px),rgba(0,0,0,0.7)_var(--twr-10-scan))]" aria-hidden="true"></div>
        <div class="absolute -inset-px z-5 pointer-events-none [background:radial-gradient(118%_106%_at_50%_50%,rgba(0,0,0,0)_54%,rgba(0,0,0,0.5)_86%,rgba(0,0,0,0.88)_100%)]" aria-hidden="true"></div>
      </div>

      <div class="flex items-center justify-between gap-3 min-w-0 pt-2.5 px-1.5 pb-0.5 text-[0.62rem] tracking-[0.2em] text-[#8d9498]">
        <span>VT-320 / SERIAL A</span>
        <span class="flex-none size-[9px] rounded-full bg-[#63f0a0] [box-shadow:0_0_8px_2px_rgba(99,240,160,0.65)]" aria-hidden="true"></span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr10-fg: #7dfab0;
  --color-twr10-fg: oklch(0.90 0.14 158);
  --color-twr10-fgdim: #3f9f6d;
  --color-twr10-fgdim: oklch(0.63 0.11 158);
  --color-twr10-warn: #ffd166;
  --color-twr10-warn: oklch(0.87 0.13 85);
  --color-twr10-tube: #04120c;
  --color-twr10-bg: #0c1013;
  --color-twr10-bg: oklch(0.16 0.008 210);
  --color-twr10-surface: #171c20;
  --color-twr10-surface: oklch(0.23 0.009 210);
  --color-twr10-ink: #eaeff1;
  --color-twr10-ink: oklch(0.95 0.004 210);
  --color-twr10-ink2: #9ba5aa;
  --color-twr10-ink2: oklch(0.71 0.009 210);
  --color-twr10-line: #333c41;
  --color-twr10-line: oklch(0.33 0.01 210);
  --color-twr10-acc: #6ee7b7;
  --color-twr10-acc: oklch(0.85 0.12 165);
  --font-twr10-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, monospace;
  --animate-twr10-in: twr-10-in 320ms ease-out forwards;
  --animate-twr10-type: twr-10-type 1.6s steps(22, end) 1.4s forwards;
  --animate-twr10-blink: twr-10-blink 1.1s steps(1, end) infinite;
}

.twr-10 {
  --twr-10-scan: 3px;
  --twr-10-curve: 20px;
}

@keyframes twr-10-in {
  from {
    opacity: 0;
    transform: translateY(2px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}
/* The 22 here must equal the steps() count in --animate-twr10-type and the
   motion-reduce:w-[22ch] utility in the markup. */

@keyframes twr-10-type {
  to {
    width: 22ch;
  }
}

@keyframes twr-10-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}
/* No variant form, and unlayered so it outranks the arbitrary background. */

@media (min-resolution: 1.5dppx) {
  .twr-10__scan {
    background: repeating-linear-gradient(
          to bottom,
          rgba(0, 0, 0, 0) 0,
          rgba(0, 0, 0, 0.6) calc(var(--twr-10-scan) * 0.5),
          rgba(0, 0, 0, 0) calc(var(--twr-10-scan) * 1.34)
        );
  }
}

.twr-10:has(#twr-10-theme:checked) {
  --color-twr10-bg: #d8dcde;
  --color-twr10-bg: oklch(0.88 0.005 210);
  --color-twr10-surface: #eef1f2;
  --color-twr10-surface: oklch(0.95 0.003 210);
  --color-twr10-ink: #14181a;
  --color-twr10-ink: oklch(0.19 0.006 210);
  --color-twr10-ink2: #4a5257;
  --color-twr10-ink2: oklch(0.43 0.01 210);
  --color-twr10-line: #a6aeb2;
  --color-twr10-line: oklch(0.74 0.008 210);
  --color-twr10-acc: #0c6b4d;
  --color-twr10-acc: oklch(0.46 0.11 165);
}
```

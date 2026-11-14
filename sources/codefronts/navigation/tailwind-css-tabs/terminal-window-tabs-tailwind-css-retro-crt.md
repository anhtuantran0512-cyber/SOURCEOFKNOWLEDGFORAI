---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/terminal-window-tabs-tailwind-css-retro-crt/"
title: "Terminal Window Tabs in Tailwind CSS (Retro CRT)"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A phosphor-green terminal: traffic-light title bar, tabs for three shells, scanlines, a vignette and a blinking block cursor after the prompt."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terminal Window Tabs in Tailwind CSS (Retro CRT)
Source: https://codefronts.com/navigation/tailwind-css-tabs/terminal-window-tabs-tailwind-css-retro-crt/

A phosphor-green terminal: traffic-light title bar, tabs for three shells, scanlines, a vignette and a blinking block cursor after the prompt. The port sets the output in VT323, a face drawn from DEC terminal glyphs, and makes the glow a token-driven [text-shadow:…].
## HTML
```html
<section class="ttb-09 group/tabs grid min-h-svh w-full place-items-center bg-ttb09-bg px-5 py-14 font-ttb09-mono text-ttb09-ph" aria-label="Retro CRT terminal tabs demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-xl overflow-hidden rounded-xl bg-ttb09-screen ring-1 ring-ttb09-ph/20 shadow-[0_0_0_1px_rgb(0_0_0),0_28px_60px_-20px_rgb(0_0_0/0.8),0_0_40px_-10px_color-mix(in_oklab,var(--color-ttb09-ph)_25%,transparent)]">
      <div class="flex items-center gap-2 border-b border-ttb09-ph/12 bg-ttb09-bar px-3.5 py-2.5">
        <span aria-hidden="true" class="size-3 rounded-full bg-ttb09-red"></span><span aria-hidden="true" class="size-3 rounded-full bg-ttb09-yellow"></span><span aria-hidden="true" class="size-3 rounded-full bg-ttb09-green"></span>
        <span class="flex-1 text-center text-[11px] tracking-[0.04em] text-ttb09-mut">terminal — bash — 80×24</span>
      </div>
      <div role="radiogroup" aria-label="Shell" class="flex border-b border-ttb09-ph/12">
        <label class="flex min-h-10 flex-1 cursor-pointer items-center justify-center border-r border-ttb09-ph/10 text-xs text-ttb09-tab transition-colors last:border-r-0 hover:bg-ttb09-ph/5 hover:text-ttb09-ph has-checked:bg-ttb09-ph/10 has-checked:text-ttb09-ph has-checked:[text-shadow:0_0_6px_color-mix(in_oklab,var(--color-ttb09-ph)_70%,transparent)] has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb09-ph"><input class="sr-only" type="radio" name="ttb09" id="ttb09-r1" checked>~/main</label>
        <label class="flex min-h-10 flex-1 cursor-pointer items-center justify-center border-r border-ttb09-ph/10 text-xs text-ttb09-tab transition-colors last:border-r-0 hover:bg-ttb09-ph/5 hover:text-ttb09-ph has-checked:bg-ttb09-ph/10 has-checked:text-ttb09-ph has-checked:[text-shadow:0_0_6px_color-mix(in_oklab,var(--color-ttb09-ph)_70%,transparent)] has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb09-ph"><input class="sr-only" type="radio" name="ttb09" id="ttb09-r2">~/logs</label>
        <label class="flex min-h-10 flex-1 cursor-pointer items-center justify-center text-xs text-ttb09-tab transition-colors hover:bg-ttb09-ph/5 hover:text-ttb09-ph has-checked:bg-ttb09-ph/10 has-checked:text-ttb09-ph has-checked:[text-shadow:0_0_6px_color-mix(in_oklab,var(--color-ttb09-ph)_70%,transparent)] has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb09-ph"><input class="sr-only" type="radio" name="ttb09" id="ttb09-r3">~/cron</label>
      </div>
      <div class="min-h-44 bg-[repeating-linear-gradient(0deg,transparent_0_2px,var(--color-ttb09-scan)_2px_3px)] px-5 py-4 font-ttb09-crt text-[20px] leading-[1.25] shadow-[inset_0_0_60px_rgb(0_0_0/0.6)] [text-shadow:0_0_4px_color-mix(in_oklab,var(--color-ttb09-ph)_45%,transparent)]">
        <div class="hidden group-has-[#ttb09-r1:checked]/tabs:block"><p><span class="text-ttb09-dim">$</span> ls -la</p><p>drwxr-xr-x  src/</p><p>-rw-r--r--  README.md</p><p><span class="text-ttb09-dim">$</span> <span aria-hidden="true" class="inline-block h-[0.9em] w-[0.55em] translate-y-[0.1em] animate-ttb09-blink bg-ttb09-ph motion-reduce:animate-none"></span></p></div>
        <div class="hidden group-has-[#ttb09-r2:checked]/tabs:block"><p><span class="text-ttb09-dim">$</span> tail -f app.log</p><p>[12:04] GET /api 200 · 18ms</p><p>[12:05] GET /api 200 · 21ms</p><p><span aria-hidden="true" class="inline-block h-[0.9em] w-[0.55em] translate-y-[0.1em] animate-ttb09-blink bg-ttb09-ph motion-reduce:animate-none"></span></p></div>
        <div class="hidden group-has-[#ttb09-r3:checked]/tabs:block"><p><span class="text-ttb09-dim">$</span> crontab -l</p><p>0 * * * *    ./sync.sh</p><p>*/5 * * * *  ./ping.sh</p><p><span class="text-ttb09-dim">$</span> <span aria-hidden="true" class="inline-block h-[0.9em] w-[0.55em] translate-y-[0.1em] animate-ttb09-blink bg-ttb09-ph motion-reduce:animate-none"></span></p></div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb09-ph/15 px-3.5 py-2 text-[11.5px] text-ttb09-mut">scanline gradient · inset vignette · [text-shadow] bloom · steps(1) cursor</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb09-bg: #080908;
  --color-ttb09-bg: oklch(0.138 0.003 145.4);
  --color-ttb09-screen: #050605;
  --color-ttb09-screen: oklch(0.120 0.004 145.3);
  --color-ttb09-bar: #121412;
  --color-ttb09-bar: oklch(0.188 0.005 145.4);
  --color-ttb09-ph: #4ade80;
  --color-ttb09-ph: oklch(0.800 0.182 151.7);
  --color-ttb09-tab: #74c08f;
  --color-ttb09-tab: oklch(0.745 0.104 154.7);
  --color-ttb09-dim: #2f9a58;
  --color-ttb09-dim: oklch(0.610 0.138 152.2);
  --color-ttb09-scan: #4ade800d;
  --color-ttb09-scan: oklch(0.800 0.182 151.7 / 0.05);
  --color-ttb09-mut: #9aa39c;
  --color-ttb09-mut: oklch(0.706 0.014 152.5);
  --color-ttb09-red: #ff5f57;
  --color-ttb09-red: oklch(0.694 0.196 26.4);
  --color-ttb09-yellow: #febc2e;
  --color-ttb09-yellow: oklch(0.835 0.161 80.9);
  --color-ttb09-green: #28c840;
  --color-ttb09-green: oklch(0.728 0.217 144.7);
  --font-ttb09-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttb09-crt: 'VT323', ui-monospace, monospace;
  --animate-ttb09-blink: ttb09-blink 1.05s steps(1, end) infinite;

  @keyframes ttb09-blink {
    0%,
        49% {
      opacity: 1;
    }

    50%,
        100% {
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-09 {
  width: 100%;
  min-height: 100svh;
}
```

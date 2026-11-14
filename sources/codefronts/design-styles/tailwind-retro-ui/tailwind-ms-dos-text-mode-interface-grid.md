---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-ms-dos-text-mode-interface-grid/"
title: "Tailwind MS DOS Text Mode Interface Grid"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A character-cell interface reproduced as one: an 80&times;25 field where every cell is exactly one monospace advance, framed with code page 437 box-drawing…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind MS DOS Text Mode Interface Grid
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-ms-dos-text-mode-interface-grid/

A character-cell interface reproduced as one: an 80&times;25 field where every cell is exactly one monospace advance, framed with code page 437 box-drawing characters and restricted to the 16-colour CGA palette as theme tokens. The constraint is the subject &mdash; nothing can sit between two cells &mdash; and Tailwind's container-query utilities turn out to be the cleanest way yet to make 80 columns fit their frame exactly.
## HTML
```html
<section class="twr-06 relative block w-full min-h-svh box-border bg-twr06-bg text-twr06-ink font-twr06-mono" aria-labelledby="twr-06-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-06-title">MS-DOS text mode character grid</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-06-theme">
    <label class="grid place-items-center size-11 border border-twr06-line bg-twr06-surface text-twr06-ink2 cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-twr06-acc peer-focus-visible:outline-offset-2" for="twr-06-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-4.5 max-w-[72rem] mx-auto px-[clamp(0.6rem,0.4rem+1.5vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16 lg:grid-cols-2">
    <p class="m-0 justify-self-start min-w-0 lg:col-span-2 border border-twr06-line bg-twr06-surface px-2.5 py-1.5 text-[0.68rem] tracking-[0.12em] uppercase text-twr06-ink2">IBM CGA &middot; 16 colours &middot; 80 &times; 25 text mode &middot; code page 437</p>

    <div class="min-w-0 lg:col-span-2 rounded-md bg-[#6d6f70] p-[clamp(0.5rem,0.3rem+1vw,1rem)] [box-shadow:inset_0_1px_0_rgba(255,255,255,0.35),inset_0_-2px_0_rgba(0,0,0,0.4),0_14px_30px_-16px_rgba(0,0,0,0.6)]">
      <div class="@container min-w-0 overflow-hidden grid grid-cols-[minmax(0,1fr)] content-start border-2 border-[#1b1d1f] bg-twr06-blue text-twr06-ltgrey">
        <div class="flex items-center min-h-[1.6em] px-[0.5ch] min-w-0 overflow-hidden whitespace-nowrap bg-twr06-ltgrey text-twr06-k text-[clamp(0.66rem,0.55rem+0.6vw,0.85rem)]" role="presentation">
          <span class="font-bold text-twr06-red">F</span><span>ile</span>
          <span class="flex-none w-[2ch]"></span>
          <span class="font-bold text-twr06-red">E</span><span>dit</span>
          <span class="flex-none w-[2ch]"></span>
          <span class="font-bold text-twr06-red">S</span><span>earch</span>
          <span class="flex-none w-[2ch]"></span>
          <span class="font-bold text-twr06-red">O</span><span>ptions</span>
          <span class="ms-auto ps-[1ch] text-[#303030]">MEM 640K</span>
        </div>

        <pre class="twr-06__art hidden md:block m-0 py-2 min-w-0 overflow-hidden font-inherit whitespace-pre text-center leading-[1.16] text-twr06-ltcyan text-[min(0.95rem,2.02cqi)]" aria-hidden="true">╔══════════════════════════════════════════════════════════════════════════════╗
║  C:\ ─ Directory of drive C  ─  6 file(s)  ─  90,671 bytes                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Name            Size      Date        Attr    Type                          ║
║  ────────────────────────────────────────────────────────────────────        ║
║  AUTOEXEC.BAT      1,024   04-12-1995  A       Batch file                    ║
║  COMMAND.COM      54,619   05-31-1994  RA      Command interpreter           ║
║  CONFIG.SYS          412   04-12-1995  A       System configuration          ║
║  HIMEM.SYS        29,136   05-31-1994  RA      Extended memory manager       ║
║  README.TXT        7,880   11-03-1995  A       Text                          ║
║                                                                              ║
║  Every glyph above occupies exactly one cell. Nothing sits between two cells.║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝</pre>
        <pre class="twr-06__art block md:hidden m-0 py-2 min-w-0 overflow-hidden font-inherit whitespace-pre text-center leading-[1.16] text-twr06-ltcyan text-[min(0.95rem,4.1cqi)]" aria-hidden="true">╔══════════════════════════════════════╗
║  C:\ ─ 6 file(s), 90,671 bytes       ║
╠══════════════════════════════════════╣
║ Name          Size    Attr           ║
║ ─────────────────────────────────────║
║ AUTOEXEC.BAT  1,024   A              ║
║ COMMAND.COM  54,619   RA             ║
║ CONFIG.SYS      412   A              ║
║ HIMEM.SYS    29,136   RA             ║
║ README.TXT    7,880   A              ║
║                                      ║
║  One glyph = one cell. No between.   ║
║                                      ║
║                                      ║
╚══════════════════════════════════════╝</pre>
        <p class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">A DOS-style file manager panel listing AUTOEXEC.BAT, CONFIG.SYS, COMMAND.COM and HIMEM.SYS with sizes and dates, framed in double-line box characters.</p>

        <div class="flex flex-wrap items-center gap-x-[2ch] min-h-[1.6em] px-[0.5ch] min-w-0 bg-twr06-ltgrey text-twr06-k text-[clamp(0.66rem,0.55rem+0.6vw,0.85rem)]">
          <span><span class="font-bold text-twr06-red">F1</span> Help</span>
          <span><span class="font-bold text-twr06-red">F3</span> Open</span>
          <span><span class="font-bold text-twr06-red">F10</span> Menu</span>
          <span class="ms-auto text-[#303030]">80 &times; 25</span>
        </div>
      </div>
    </div>

    <aside class="min-w-0 grid content-start gap-2.5 border border-twr06-line bg-twr06-surface p-[clamp(0.8rem,0.6rem+0.8vw,1.1rem)]">
      <h3 class="m-0 text-[0.72rem] tracking-[0.1em] uppercase text-twr06-ink2">Cell inspector &mdash; the grid the text lands on</h3>
      <div class="grid grid-cols-12 gap-px min-w-0 border border-twr06-line bg-twr06-line text-[clamp(0.8rem,0.6rem+1.4vw,1.35rem)]" aria-hidden="true">
        <span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">╔</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">═</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">═</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">╦</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">═</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">═</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">╗</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan text-twr06-yellow">█</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan text-twr06-yellow">▓</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan text-twr06-yellow">▒</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan text-twr06-yellow">░</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan"> </span>
        <span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">║</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">A</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">B</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">║</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">C</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">D</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">║</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">─</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">┼</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">─</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">┤</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan"> </span>
        <span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">╚</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">═</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">═</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">╩</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">═</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">═</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">╝</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">└</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">┴</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan">┘</span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan"> </span><span class="grid place-items-center aspect-square min-w-0 leading-none bg-twr06-blue text-twr06-ltcyan"> </span>
      </div>
      <p class="m-0 min-w-0 text-[0.8rem] leading-relaxed text-pretty text-twr06-ink2">Each box is <code class="bg-twr06-bg px-1">1ch</code> wide and one line-height tall. The frame is characters, not borders &mdash; a border would have to live between two cells, and there is no between.</p>
    </aside>

    <aside class="min-w-0 grid content-start gap-2.5 border border-twr06-line bg-twr06-surface p-[clamp(0.8rem,0.6rem+0.8vw,1.1rem)]">
      <h3 class="m-0 text-[0.72rem] tracking-[0.1em] uppercase text-twr06-ink2">CGA palette &mdash; 16 defined values</h3>
      <ul class="list-none m-0 p-0 min-w-0 grid gap-0.5 grid-cols-[repeat(auto-fit,minmax(min(100%,7.5rem),1fr))]">
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#000000]">0 black</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#0000aa]">1 blue</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#00aa00]">2 green</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#00aaaa]">3 cyan</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#aa0000]">4 red</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#aa00aa]">5 magenta</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#aa5500]">6 brown</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#aaaaaa]">7 lt grey</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#555555]">8 dk grey</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#5555ff]">9 lt blue</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#55ff55]">10 lt green</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#55ffff]">11 lt cyan</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#ff5555]">12 lt red</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#ff55ff]">13 lt magenta</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#ffff55]">14 yellow</li>
        <li class="min-w-0 flex items-center gap-2 px-2 py-1.5 text-[0.68rem] text-twr06-ink2 border border-twr06-line before:content-[''] before:flex-none before:size-4 before:border before:border-twr06-line before:bg-[#ffffff]">15 white</li>
      </ul>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr06-k: #000000;
  --color-twr06-blue: #0000aa;
  --color-twr06-cyan: #00aaaa;
  --color-twr06-ltgrey: #aaaaaa;
  --color-twr06-dkgrey: #555555;
  --color-twr06-ltcyan: #55ffff;
  --color-twr06-yellow: #ffff55;
  --color-twr06-white: #ffffff;
  --color-twr06-red: #aa0000;
  --color-twr06-bg: #c9ccd2;
  --color-twr06-bg: oklch(0.84 0.008 260);
  --color-twr06-surface: #eef0f3;
  --color-twr06-surface: oklch(0.95 0.004 260);
  --color-twr06-ink: #14171c;
  --color-twr06-ink: oklch(0.19 0.008 260);
  --color-twr06-ink2: #464e58;
  --color-twr06-ink2: oklch(0.42 0.014 260);
  --color-twr06-line: #9aa1ab;
  --color-twr06-line: oklch(0.71 0.012 260);
  --color-twr06-acc: #1247c9;
  --color-twr06-acc: oklch(0.45 0.2 264);
  --font-twr06-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, 'Cascadia Mono', Consolas, monospace;
}
/* A feature query that substitutes the very property it tests cannot be a
   variant — the utility and the fallback would compete in the same layer. */

@supports not (font-size: 1cqi) {
  .twr-06__art {
    font-size: clamp(0.35rem, 1.6vw, 0.95rem);
  }
}

.twr-06:has(#twr-06-theme:checked) {
  --color-twr06-bg: #101318;
  --color-twr06-bg: oklch(0.18 0.008 260);
  --color-twr06-surface: #1a1e25;
  --color-twr06-surface: oklch(0.24 0.01 260);
  --color-twr06-ink: #eef1f5;
  --color-twr06-ink: oklch(0.96 0.004 260);
  --color-twr06-ink2: #a3abb6;
  --color-twr06-ink2: oklch(0.74 0.012 260);
  --color-twr06-line: #39414c;
  --color-twr06-line: oklch(0.35 0.014 260);
  --color-twr06-acc: #7fa8ff;
  --color-twr06-acc: oklch(0.76 0.13 264);
}
```

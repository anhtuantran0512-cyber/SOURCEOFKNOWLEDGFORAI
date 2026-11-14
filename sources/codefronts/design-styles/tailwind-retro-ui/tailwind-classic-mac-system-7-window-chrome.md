---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-classic-mac-system-7-window-chrome/"
title: "Tailwind Classic Mac System 7 Window Chrome"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "The other great desktop metaphor, and a deliberate contrast to the bevelled 16-bit look: horizontal pinstripe title bar, square close box on the left, grow…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Classic Mac System 7 Window Chrome
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-classic-mac-system-7-window-chrome/

The other great desktop metaphor, and a deliberate contrast to the bevelled 16-bit look: horizontal pinstripe title bar, square close box on the left, grow box bottom-right, one-pixel black outline everywhere and no colour at all. Two colours means every state has to be spatial &mdash; which turns out to suit utilities well, because each state is a different set of properties rather than a different shade of one token.
## HTML
```html
<section class="twr-05 relative block w-full min-h-svh box-border bg-twr05-w text-twr05-k font-twr05-sans [background-image:repeating-conic-gradient(var(--twr-05-desk-b)_0%_25%,var(--twr-05-desk-a)_0%_50%)] [background-size:4px_4px]" aria-labelledby="twr-05-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-05-title">Classic Macintosh System 7 window chrome</h2>

  <div class="absolute top-[calc(44px+0.75rem)] right-4 z-8">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-05-theme">
    <label class="grid place-items-center size-11 cursor-pointer rounded border border-twr05-k bg-twr05-w text-twr05-k [box-shadow:2px_2px_0_0_var(--color-twr05-k)] peer-focus-visible:outline-2 peer-focus-visible:outline-twr05-acc peer-focus-visible:outline-offset-2" for="twr-05-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark desktop pattern</span>
    </label>
  </div>

  <div class="relative z-4 flex items-center gap-2 min-h-11 px-2 overflow-x-auto bg-twr05-w border-b border-twr05-k [scrollbar-width:thin]">
    <span class="flex-none w-3.5 h-4 mx-1.5 bg-twr05-k [clip-path:polygon(52%_0,62%_9%,55%_14%,78%_20%,96%_44%,82%_62%,92%_86%,68%_100%,50%_92%,32%_100%,8%_86%,4%_50%,20%_20%,44%_15%)]" aria-hidden="true"></span>
    <nav class="min-w-0" aria-label="System 7 menu bar">
      <ul class="list-none m-0 p-0 flex">
        <li><button class="min-h-11 min-w-11 px-2.5 border-0 bg-transparent font-inherit text-[0.85rem] text-twr05-k cursor-pointer whitespace-nowrap hover:bg-twr05-k hover:text-twr05-w focus-visible:outline-2 focus-visible:outline-twr05-acc focus-visible:outline-offset-[-3px]" type="button">File</button></li>
        <li><button class="min-h-11 min-w-11 px-2.5 border-0 bg-transparent font-inherit text-[0.85rem] text-twr05-k cursor-pointer whitespace-nowrap hover:bg-twr05-k hover:text-twr05-w focus-visible:outline-2 focus-visible:outline-twr05-acc focus-visible:outline-offset-[-3px]" type="button">Edit</button></li>
        <li><button class="min-h-11 min-w-11 px-2.5 border-0 bg-transparent font-inherit text-[0.85rem] text-twr05-k cursor-pointer whitespace-nowrap hover:bg-twr05-k hover:text-twr05-w focus-visible:outline-2 focus-visible:outline-twr05-acc focus-visible:outline-offset-[-3px]" type="button">View</button></li>
        <li><button class="min-h-11 min-w-11 px-2.5 border-0 bg-transparent font-inherit text-[0.85rem] text-twr05-k cursor-pointer whitespace-nowrap hover:bg-twr05-k hover:text-twr05-w focus-visible:outline-2 focus-visible:outline-twr05-acc focus-visible:outline-offset-[-3px]" type="button">Label</button></li>
        <li><button class="min-h-11 min-w-11 px-2.5 border-0 bg-transparent font-inherit text-[0.85rem] text-twr05-k cursor-pointer whitespace-nowrap hover:bg-twr05-k hover:text-twr05-w focus-visible:outline-2 focus-visible:outline-twr05-acc focus-visible:outline-offset-[-3px]" type="button">Special</button></li>
      </ul>
    </nav>
    <span class="ms-auto px-2.5 font-twr05-mono text-[0.78rem] whitespace-nowrap">System 7.1</span>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] items-start gap-6 max-w-[62rem] mx-auto px-[clamp(0.6rem,0.4rem+1.5vw,2rem)] pt-[clamp(1.25rem,1rem+2vw,3rem)] pb-16 lg:grid-cols-[minmax(0,1.6fr)_minmax(0,1fr)]">
    <div class="group is-active min-w-0 bg-twr05-w border border-twr05-k [box-shadow:2px_2px_0_0_var(--color-twr05-k)]">
      <div class="flex items-center gap-2 min-w-0 min-h-11 px-1.5 border-b border-twr05-k group-[.is-active]:[background:repeating-linear-gradient(to_bottom,var(--color-twr05-k)_0_1px,var(--color-twr05-w)_1px_var(--twr-05-stripe))]">
        <span class="relative flex-none grid place-items-center size-11 before:content-[''] before:size-[15px] before:border before:border-twr05-k before:bg-twr05-w" role="img" aria-label="Close box"><span class="absolute size-[7px] border border-twr05-k bg-twr05-w" aria-hidden="true"></span></span>
        <span class="flex-1 min-w-0 mx-1 px-2.5 py-0.5 text-center text-[0.85rem] font-bold bg-twr05-w overflow-hidden text-ellipsis whitespace-nowrap">Macintosh HD</span>
        <span class="relative flex-none grid place-items-center size-11 before:content-[''] before:size-[15px] before:border before:border-twr05-k before:bg-twr05-w" role="img" aria-label="Zoom box"><span class="absolute size-[9px] border border-twr05-k bg-twr05-w" aria-hidden="true"></span></span>
      </div>
      <div class="flex flex-wrap gap-x-5 gap-y-1 min-w-0 px-3 py-2 text-[0.78rem] border-b border-twr05-k">
        <span>4 items</span>
        <span>18.2 MB in disk</span>
        <span>21.6 MB available</span>
      </div>
      <ul class="list-none m-0 p-0 min-w-0">
        <li class="grid grid-cols-[28px_minmax(0,1fr)_auto] items-center gap-x-2.5 min-h-11 px-3 py-1.5 text-[0.85rem] border-b border-twr05-k last:border-b-0 sm:grid-cols-[28px_minmax(0,1fr)_5.5rem_7rem]">
          <span class="size-[20px] h-4 bg-twr05-k [clip-path:polygon(0_18%,40%_18%,48%_4%,100%_4%,100%_100%,0_100%)]" aria-hidden="true"></span>
          <span class="min-w-0 overflow-hidden text-ellipsis whitespace-nowrap">System Folder</span>
          <span class="font-twr05-mono text-[0.75rem] tabular-nums whitespace-nowrap">6,144K</span>
          <span class="hidden sm:block font-twr05-mono text-[0.75rem] whitespace-nowrap">Tue, Mar 4</span>
        </li>
        <li class="grid grid-cols-[28px_minmax(0,1fr)_auto] items-center gap-x-2.5 min-h-11 px-3 py-1.5 text-[0.85rem] border-b border-twr05-k last:border-b-0 sm:grid-cols-[28px_minmax(0,1fr)_5.5rem_7rem] bg-twr05-k text-twr05-w" aria-current="true">
          <span class="w-4 h-4 bg-twr05-k [clip-path:polygon(0_0,72%_0,100%_26%,100%_100%,0_100%)] bg-twr05-w" aria-hidden="true"></span>
          <span class="min-w-0 overflow-hidden text-ellipsis whitespace-nowrap">Read Me First</span>
          <span class="font-twr05-mono text-[0.75rem] tabular-nums whitespace-nowrap">12K</span>
          <span class="hidden sm:block font-twr05-mono text-[0.75rem] whitespace-nowrap">Tue, Mar 4</span>
        </li>
        <li class="grid grid-cols-[28px_minmax(0,1fr)_auto] items-center gap-x-2.5 min-h-11 px-3 py-1.5 text-[0.85rem] border-b border-twr05-k last:border-b-0 sm:grid-cols-[28px_minmax(0,1fr)_5.5rem_7rem]">
          <span class="w-4 h-4 bg-twr05-k [clip-path:polygon(0_0,72%_0,100%_26%,100%_100%,0_100%)]" aria-hidden="true"></span>
          <span class="min-w-0 overflow-hidden text-ellipsis whitespace-nowrap">Scrapbook File</span>
          <span class="font-twr05-mono text-[0.75rem] tabular-nums whitespace-nowrap">88K</span>
          <span class="hidden sm:block font-twr05-mono text-[0.75rem] whitespace-nowrap">Fri, Feb 28</span>
        </li>
        <li class="grid grid-cols-[28px_minmax(0,1fr)_auto] items-center gap-x-2.5 min-h-11 px-3 py-1.5 text-[0.85rem] border-b border-twr05-k last:border-b-0 sm:grid-cols-[28px_minmax(0,1fr)_5.5rem_7rem] text-[#6b6b6b]" aria-disabled="true">
          <span class="w-4 h-4 bg-twr05-k [clip-path:polygon(0_0,72%_0,100%_26%,100%_100%,0_100%)] opacity-45" aria-hidden="true"></span>
          <span class="min-w-0 overflow-hidden text-ellipsis whitespace-nowrap">Locked Archive <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">(unavailable)</span></span>
          <span class="font-twr05-mono text-[0.75rem] tabular-nums whitespace-nowrap">1,204K</span>
          <span class="hidden sm:block font-twr05-mono text-[0.75rem] whitespace-nowrap">Sun, Jan 12</span>
        </li>
      </ul>
      <div class="flex items-stretch min-w-0 border-t border-twr05-k">
        <div class="flex-1 min-w-0 min-h-5 flex items-center p-0.5 bg-twr05-w [background-image:repeating-conic-gradient(#8a8a8a_0%_25%,var(--color-twr05-w)_0%_50%)] [background-size:2px_2px]" aria-hidden="true"><span class="block w-[38%] h-3.5 bg-twr05-w border border-twr05-k"></span></div>
        <button class="flex-none grid place-items-center size-11 p-0 border-0 border-s border-twr05-k bg-twr05-w cursor-nwse-resize focus-visible:outline-2 focus-visible:outline-twr05-acc focus-visible:outline-offset-[-3px]" type="button" aria-label="Resize window">
          <span class="size-[15px] border border-twr05-k [background:linear-gradient(135deg,rgba(0,0,0,0)_48%,var(--color-twr05-k)_48%_56%,rgba(0,0,0,0)_56%),linear-gradient(135deg,rgba(0,0,0,0)_68%,var(--color-twr05-k)_68%_76%,rgba(0,0,0,0)_76%),var(--color-twr05-w)]" aria-hidden="true"></span>
        </button>
      </div>
    </div>

    <div class="group min-w-0 max-w-[30rem] bg-twr05-w border border-twr05-k [box-shadow:2px_2px_0_0_var(--color-twr05-k)]">
      <div class="flex items-center gap-2 min-w-0 min-h-11 px-1.5 border-b border-twr05-k group-[.is-active]:[background:repeating-linear-gradient(to_bottom,var(--color-twr05-k)_0_1px,var(--color-twr05-w)_1px_var(--twr-05-stripe))]">
        <span class="relative flex-none grid place-items-center size-11 before:content-[''] before:size-[15px] before:border before:border-twr05-k before:bg-twr05-w" role="img" aria-label="Close box (window inactive)"></span>
        <span class="flex-1 min-w-0 mx-1 px-2.5 py-0.5 text-center text-[0.85rem] font-bold bg-twr05-w overflow-hidden text-ellipsis whitespace-nowrap">Inactive Window</span>
        <span class="relative flex-none grid place-items-center size-11 before:content-[''] before:size-[15px] before:border before:border-twr05-k before:bg-twr05-w"></span>
      </div>
      <div class="min-w-0 px-3.5 py-3.5">
        <p class="m-0 min-w-0 text-[0.85rem] leading-relaxed text-pretty">No stripes, empty boxes. That is the entire focus indicator &mdash; there is no second colour to dim.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr05-k: #000000;
  --color-twr05-w: #ffffff;
  --color-twr05-acc: #0b4fd0;
  --color-twr05-acc: oklch(0.45 0.2 262);
  --font-twr05-sans: system-ui, -apple-system, 'Lucida Grande', Helvetica, Arial, sans-serif;
  --font-twr05-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Monaco, Menlo, monospace;
}

.twr-05 {
  --twr-05-stripe: 2px;
  --twr-05-desk-a: #ffffff;
  --twr-05-desk-b: #b9b9b9;
}
/* The artefact is white by definition — there was no dark System 7 — so the
   toggle changes the desk pattern around the window, never the window. */

.twr-05:has(#twr-05-theme:checked) {
  --twr-05-desk-a: #2a2a2a;
  --twr-05-desk-b: #000000;
}
```

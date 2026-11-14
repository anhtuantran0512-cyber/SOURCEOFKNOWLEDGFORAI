---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-keyboard-shortcut-tooltip-animated-keycaps/"
title: "Tailwind Keyboard Shortcut Tooltip with Animated 3D Keycaps"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A toolbar tooltip that wears its shortcut as little extruded keycaps which depress on a loop while the pill is shown."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Keyboard Shortcut Tooltip with Animated 3D Keycaps
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-keyboard-shortcut-tooltip-animated-keycaps/

A toolbar tooltip that wears its shortcut as little extruded keycaps which depress on a loop while the pill is shown. The port's win is the intent gate: group-hover:delay-400 states the reveal delay on the pill itself, beside the group-focus-visible:delay-0 that makes the keyboard path instant &mdash; in CSS those two live inside one positional three-value transition-delay list nobody can read.
## HTML
```html
<section class="ttp-02 w-full min-h-svh flex items-start justify-center bg-ttp02-stage font-ttp02-sans text-ttp02-ink px-7 pt-[130px] pb-15">
  <div class="w-full max-w-[600px] bg-white border border-ttp02-edge rounded-[10px] overflow-visible shadow-[0_20px_48px_-16px_rgba(0,0,0,0.15)]">
    <div class="h-8.5 flex items-center gap-[7px] px-3 bg-ttp02-bar border-b border-ttp02-edge rounded-t-[10px]">
      <span class="w-2.5 h-2.5 rounded-full bg-ttp02-dot"></span><span class="w-2.5 h-2.5 rounded-full bg-ttp02-dot"></span><span class="w-2.5 h-2.5 rounded-full bg-ttp02-dot"></span>
      <span class="flex-1 text-center text-[11.5px] tracking-[0.02em] text-ttp02-muted">Untitled Document — Composer</span>
    </div>

    <div class="flex flex-wrap items-center gap-1 px-3 py-2.5 border-b border-ttp02-edge overflow-visible">
      <div class="flex gap-0.5 px-1.5 border-r border-ttp02-edge">
        <button type="button" aria-label="Save" aria-keyshortcuts="Meta+S" aria-describedby="ttp02-t1" class="group relative grid place-items-center w-9 h-9 p-0 rounded-[7px] border-0 bg-transparent text-ttp02-icon cursor-pointer transition-colors duration-150 hover:bg-ttp02-hover hover:text-ttp02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp02-focus">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="w-[17px] h-[17px]" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span id="ttp02-t1" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-50 flex items-center gap-2.25 whitespace-nowrap -translate-x-1/2 translate-y-1 rounded-[7px] bg-ttp02-pill px-2.5 py-[7px] text-[11.5px] text-white opacity-0 shadow-[0_6px_18px_-4px_rgba(0,0,0,0.3),0_2px_6px_-2px_rgba(0,0,0,0.2)] transition-[opacity,translate] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] after:content-[''] after:absolute after:top-full after:left-1/2 after:w-[7px] after:h-[7px] after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-45 after:bg-ttp02-pill group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-400 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-0 motion-reduce:transition-opacity">
            <span class="font-medium">Save</span>
            <kbd class="flex gap-[3px] not-italic"><span class="ttp02-key group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⌘</span><span class="ttp02-key [animation-delay:100ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">S</span></kbd>
          </span>
        </button>
        <button type="button" aria-label="Undo" aria-keyshortcuts="Meta+Z" aria-describedby="ttp02-t2" class="group relative grid place-items-center w-9 h-9 p-0 rounded-[7px] border-0 bg-transparent text-ttp02-icon cursor-pointer transition-colors duration-150 hover:bg-ttp02-hover hover:text-ttp02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp02-focus">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="w-[17px] h-[17px]" aria-hidden="true"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>
          <span id="ttp02-t2" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-50 flex items-center gap-2.25 whitespace-nowrap -translate-x-1/2 translate-y-1 rounded-[7px] bg-ttp02-pill px-2.5 py-[7px] text-[11.5px] text-white opacity-0 shadow-[0_6px_18px_-4px_rgba(0,0,0,0.3),0_2px_6px_-2px_rgba(0,0,0,0.2)] transition-[opacity,translate] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] after:content-[''] after:absolute after:top-full after:left-1/2 after:w-[7px] after:h-[7px] after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-45 after:bg-ttp02-pill group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-400 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-0 motion-reduce:transition-opacity">
            <span class="font-medium">Undo</span>
            <kbd class="flex gap-[3px] not-italic"><span class="ttp02-key group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⌘</span><span class="ttp02-key [animation-delay:100ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">Z</span></kbd>
          </span>
        </button>
        <button type="button" aria-label="Redo" aria-keyshortcuts="Meta+Shift+Z" aria-describedby="ttp02-t3" class="group relative grid place-items-center w-9 h-9 p-0 rounded-[7px] border-0 bg-transparent text-ttp02-icon cursor-pointer transition-colors duration-150 hover:bg-ttp02-hover hover:text-ttp02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp02-focus">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="w-[17px] h-[17px]" aria-hidden="true"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.13-9.36L23 10"/></svg>
          <span id="ttp02-t3" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-50 flex items-center gap-2.25 whitespace-nowrap -translate-x-1/2 translate-y-1 rounded-[7px] bg-ttp02-pill px-2.5 py-[7px] text-[11.5px] text-white opacity-0 shadow-[0_6px_18px_-4px_rgba(0,0,0,0.3),0_2px_6px_-2px_rgba(0,0,0,0.2)] transition-[opacity,translate] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] after:content-[''] after:absolute after:top-full after:left-1/2 after:w-[7px] after:h-[7px] after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-45 after:bg-ttp02-pill group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-400 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-0 motion-reduce:transition-opacity">
            <span class="font-medium">Redo</span>
            <kbd class="flex gap-[3px] not-italic"><span class="ttp02-key group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⌘</span><span class="ttp02-key [animation-delay:100ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⇧</span><span class="ttp02-key [animation-delay:200ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">Z</span></kbd>
          </span>
        </button>
      </div>

      <div class="flex gap-0.5 px-1.5 border-r border-ttp02-edge">
        <button type="button" aria-label="Bold" aria-pressed="true" aria-keyshortcuts="Meta+B" aria-describedby="ttp02-t4" class="group relative grid place-items-center w-9 h-9 p-0 rounded-[7px] border-0 bg-ttp02-active text-ttp02-ink cursor-pointer transition-colors duration-150 hover:bg-ttp02-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp02-focus">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-[17px] h-[17px]" aria-hidden="true"><path d="M6 4h8a4 4 0 0 1 4 4 4 4 0 0 1-4 4H6z"/><path d="M6 12h9a4 4 0 0 1 4 4 4 4 0 0 1-4 4H6z"/></svg>
          <span id="ttp02-t4" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-50 flex items-center gap-2.25 whitespace-nowrap -translate-x-1/2 translate-y-1 rounded-[7px] bg-ttp02-pill px-2.5 py-[7px] text-[11.5px] text-white opacity-0 shadow-[0_6px_18px_-4px_rgba(0,0,0,0.3),0_2px_6px_-2px_rgba(0,0,0,0.2)] transition-[opacity,translate] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] after:content-[''] after:absolute after:top-full after:left-1/2 after:w-[7px] after:h-[7px] after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-45 after:bg-ttp02-pill group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-400 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-0 motion-reduce:transition-opacity">
            <span class="font-medium">Bold</span>
            <kbd class="flex gap-[3px] not-italic"><span class="ttp02-key group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⌘</span><span class="ttp02-key [animation-delay:100ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">B</span></kbd>
          </span>
        </button>
        <button type="button" aria-label="Italic" aria-keyshortcuts="Meta+I" aria-describedby="ttp02-t5" class="group relative grid place-items-center w-9 h-9 p-0 rounded-[7px] border-0 bg-transparent text-ttp02-icon cursor-pointer transition-colors duration-150 hover:bg-ttp02-hover hover:text-ttp02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp02-focus">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-[17px] h-[17px]" aria-hidden="true"><line x1="19" y1="4" x2="10" y2="4"/><line x1="14" y1="20" x2="5" y2="20"/><line x1="15" y1="4" x2="9" y2="20"/></svg>
          <span id="ttp02-t5" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-50 flex items-center gap-2.25 whitespace-nowrap -translate-x-1/2 translate-y-1 rounded-[7px] bg-ttp02-pill px-2.5 py-[7px] text-[11.5px] text-white opacity-0 shadow-[0_6px_18px_-4px_rgba(0,0,0,0.3),0_2px_6px_-2px_rgba(0,0,0,0.2)] transition-[opacity,translate] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] after:content-[''] after:absolute after:top-full after:left-1/2 after:w-[7px] after:h-[7px] after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-45 after:bg-ttp02-pill group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-400 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-0 motion-reduce:transition-opacity">
            <span class="font-medium">Italic</span>
            <kbd class="flex gap-[3px] not-italic"><span class="ttp02-key group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⌘</span><span class="ttp02-key [animation-delay:100ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">I</span></kbd>
          </span>
        </button>
        <button type="button" aria-label="Underline" aria-keyshortcuts="Meta+U" aria-describedby="ttp02-t6" class="group relative grid place-items-center w-9 h-9 p-0 rounded-[7px] border-0 bg-transparent text-ttp02-icon cursor-pointer transition-colors duration-150 hover:bg-ttp02-hover hover:text-ttp02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp02-focus">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="w-[17px] h-[17px]" aria-hidden="true"><path d="M6 3v7a6 6 0 0 0 6 6 6 6 0 0 0 6-6V3"/><line x1="4" y1="21" x2="20" y2="21"/></svg>
          <span id="ttp02-t6" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-50 flex items-center gap-2.25 whitespace-nowrap -translate-x-1/2 translate-y-1 rounded-[7px] bg-ttp02-pill px-2.5 py-[7px] text-[11.5px] text-white opacity-0 shadow-[0_6px_18px_-4px_rgba(0,0,0,0.3),0_2px_6px_-2px_rgba(0,0,0,0.2)] transition-[opacity,translate] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] after:content-[''] after:absolute after:top-full after:left-1/2 after:w-[7px] after:h-[7px] after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-45 after:bg-ttp02-pill group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-400 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-0 motion-reduce:transition-opacity">
            <span class="font-medium">Underline</span>
            <kbd class="flex gap-[3px] not-italic"><span class="ttp02-key group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⌘</span><span class="ttp02-key [animation-delay:100ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">U</span></kbd>
          </span>
        </button>
      </div>

      <div class="flex gap-0.5 px-1.5">
        <button type="button" aria-label="Align left" aria-keyshortcuts="Meta+Shift+L" aria-describedby="ttp02-t7" class="group relative grid place-items-center w-9 h-9 p-0 rounded-[7px] border-0 bg-transparent text-ttp02-icon cursor-pointer transition-colors duration-150 hover:bg-ttp02-hover hover:text-ttp02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp02-focus">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="w-[17px] h-[17px]" aria-hidden="true"><line x1="17" y1="10" x2="3" y2="10"/><line x1="21" y1="6" x2="3" y2="6"/><line x1="21" y1="14" x2="3" y2="14"/><line x1="17" y1="18" x2="3" y2="18"/></svg>
          <span id="ttp02-t7" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-50 flex w-[200px] flex-col items-start gap-[7px] text-left -translate-x-1/2 translate-y-1 rounded-[7px] bg-ttp02-pill px-3 py-2.5 text-[11.5px] text-white opacity-0 shadow-[0_6px_18px_-4px_rgba(0,0,0,0.3),0_2px_6px_-2px_rgba(0,0,0,0.2)] transition-[opacity,translate] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] after:content-[''] after:absolute after:top-full after:left-1/2 after:w-[7px] after:h-[7px] after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-45 after:bg-ttp02-pill group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-400 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-0 motion-reduce:transition-opacity">
            <span class="flex w-full items-center justify-between gap-2.5">
              <span class="font-medium">Align Left</span>
              <kbd class="flex gap-[3px] not-italic"><span class="ttp02-key group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⌘</span><span class="ttp02-key [animation-delay:100ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⇧</span><span class="ttp02-key [animation-delay:200ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">L</span></kbd>
            </span>
            <span class="w-full border-t border-white/20 pt-[5px] text-[11px] leading-[1.5] text-white/75">Aligns the current paragraph to the left edge of the column.</span>
          </span>
        </button>
        <button type="button" aria-label="Settings" aria-keyshortcuts="Meta+," aria-describedby="ttp02-t8" class="group relative grid place-items-center w-9 h-9 p-0 rounded-[7px] border-0 bg-transparent text-ttp02-icon cursor-pointer transition-colors duration-150 hover:bg-ttp02-hover hover:text-ttp02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp02-focus">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="w-[17px] h-[17px]" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
          <span id="ttp02-t8" role="tooltip" class="pointer-events-none absolute bottom-[calc(100%+10px)] left-1/2 z-50 flex items-center gap-2.25 whitespace-nowrap -translate-x-1/2 translate-y-1 rounded-[7px] bg-ttp02-pill px-2.5 py-[7px] text-[11.5px] text-white opacity-0 shadow-[0_6px_18px_-4px_rgba(0,0,0,0.3),0_2px_6px_-2px_rgba(0,0,0,0.2)] transition-[opacity,translate] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] after:content-[''] after:absolute after:top-full after:left-1/2 after:w-[7px] after:h-[7px] after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-45 after:bg-ttp02-pill group-hover:opacity-100 group-hover:translate-y-0 group-hover:delay-400 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 group-focus-visible:delay-0 motion-reduce:transition-opacity">
            <span class="font-medium">Settings</span>
            <kbd class="flex gap-[3px] not-italic"><span class="ttp02-key group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">⌘</span><span class="ttp02-key [animation-delay:100ms] group-hover:animate-ttp02-press group-focus-visible:animate-ttp02-press motion-reduce:animate-none">,</span></kbd>
          </span>
        </button>
      </div>
    </div>

    <div class="px-9 pt-7 pb-9 text-[13px] leading-[1.7] text-ttp02-body">
      <h3 class="font-ttp02-serif text-2xl font-normal tracking-[-0.01em] text-ttp02-ink m-0 mb-2.5">The cursor as a finger.</h3>
      <p class="max-w-[480px] m-0">Hover or tab to any toolbar button to see its keycap; the keys depress on a loop, the way a real chord would feel if you held the gesture <em class="font-ttp02-serif italic font-medium text-ttp02-accent">just</em> long enough to second-guess it.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp02-stage: #f5f5f3;
  --color-ttp02-stage: oklch(0.96 0.002 100);
  --color-ttp02-bar: #fafaf8;
  --color-ttp02-bar: oklch(0.98 0.002 100);
  --color-ttp02-edge: #e6e6e2;
  --color-ttp02-edge: oklch(0.92 0.003 100);
  --color-ttp02-dot: #e2e2de;
  --color-ttp02-dot: oklch(0.9 0.003 100);
  --color-ttp02-ink: #1a1a1a;
  --color-ttp02-ink: oklch(0.21 0 0);
  --color-ttp02-body: #4d4d4d;
  --color-ttp02-body: oklch(0.42 0 0);
  --color-ttp02-muted: #6b6b6b;
  --color-ttp02-muted: oklch(0.52 0 0);
  --color-ttp02-icon: #444444;
  --color-ttp02-icon: oklch(0.39 0 0);
  --color-ttp02-hover: #f0f0ec;
  --color-ttp02-hover: oklch(0.95 0.003 100);
  --color-ttp02-active: #e8e8e4;
  --color-ttp02-active: oklch(0.92 0.003 100);
  --color-ttp02-pill: #1a1a1a;
  --color-ttp02-pill: oklch(0.21 0 0);
  --color-ttp02-keytop: #3d3d3d;
  --color-ttp02-keytop: oklch(0.36 0 0);
  --color-ttp02-keybot: #2a2a2a;
  --color-ttp02-keybot: oklch(0.28 0 0);
  --color-ttp02-keyedge: #4a4a4a;
  --color-ttp02-keyedge: oklch(0.41 0 0);
  --color-ttp02-keyink: #f5f5f3;
  --color-ttp02-keyink: oklch(0.96 0.002 100);
  --color-ttp02-accent: #2d6a4f;
  --color-ttp02-accent: oklch(0.47 0.09 158);
  --color-ttp02-focus: #2d6a4f;
  --color-ttp02-focus: oklch(0.47 0.09 158);
  --font-ttp02-sans: 'Inter', system-ui, sans-serif;
  --font-ttp02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttp02-serif: Georgia, 'Times New Roman', serif;
  --animate-ttp02-press: ttp02-press 1.6s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes ttp02-press {
  0%,
    50%,
    100% {
    transform: translateY(0);
    border-bottom-width: 2px;
  }

  25% {
    transform: translateY(1px);
    border-bottom-width: 1px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.04);
  }
}

.ttp-02 {
  width: 100%;
  min-height: 100svh;
}
/* The keycap is the one repeated object in the demo, and it carries
   fourteen declarations on eighteen elements. @apply is the honest
   answer: the utilities are still the source of truth, and the markup
   stays readable enough to see the animation variants beside it. */

.ttp-02 .ttp02-key {
  @apply inline-flex items-center justify-center min-w-5 h-5 px-[5px] rounded-[4px] border border-ttp02-keyedge border-b-2 bg-linear-to-b from-ttp02-keytop to-ttp02-keybot font-ttp02-mono text-[10px] text-ttp02-keyink shadow-[inset_0_1px_0_rgba(255,255,255,0.08)];
}
```

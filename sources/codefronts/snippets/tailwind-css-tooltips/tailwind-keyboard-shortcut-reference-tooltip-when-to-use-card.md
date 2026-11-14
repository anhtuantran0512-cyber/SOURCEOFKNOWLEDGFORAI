---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-keyboard-shortcut-reference-tooltip-when-to-use-card/"
title: "Tailwind Keyboard Shortcut Reference Tooltip with When-To-Use Card"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A shortcut list where each row opens a full reference card to its left: big keycaps, plain-English description, three when-to-use lines and related chords as…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Keyboard Shortcut Reference Tooltip with When-To-Use Card
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-keyboard-shortcut-reference-tooltip-when-to-use-card/

A shortcut list where each row opens a full reference card to its left: big keycaps, plain-English description, three when-to-use lines and related chords as pills. The port's shape is two @apply keycap sizes plus one card shell &mdash; the same object at two scales, stated once each.
## HTML
```html
<section class="ttp-10 w-full min-h-svh bg-ttp10-bg py-9 pr-7 pl-[320px] font-ttp10-mono max-xl:pl-7">
  <div class="mx-auto flex max-w-[480px] flex-col gap-0.5">

    <div class="group relative">
      <div tabindex="0" role="button" aria-describedby="ttp10-k1" aria-keyshortcuts="Meta+S" class="flex cursor-help items-center justify-between rounded-md px-3 py-2.5 transition-colors duration-100 group-hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp10-acc">
        <span class="text-[12.5px] text-ttp10-ink">Save file</span>
        <kbd class="flex items-center gap-1 not-italic"><span class="ttp10-key">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-key">S</span></kbd>
      </div>
      <div id="ttp10-k1" role="tooltip" class="ttp10-card">
        <div class="border-b border-white/8 px-3.5 pt-3.5 pb-2.75">
          <div class="mb-1.75 text-[15px] font-semibold text-ttp10-bright">Save File</div>
          <kbd class="flex items-center gap-1.25 not-italic"><span class="ttp10-keybig">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-keybig">S</span></kbd>
        </div>
        <p class="m-0 border-b border-white/6 px-3.5 py-2.75 font-ttp10-sans text-[11.5px] leading-[1.55] text-ttp10-body">Saves the current file to disk immediately. If the file has never been saved, opens a Save As dialog to choose a name and location.</p>
        <div class="border-b border-white/6 px-3.5 py-2.5">
          <div class="mb-1.5 text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">When to use</div>
          <div class="ttp10-when">After every meaningful change to preserve work</div>
          <div class="ttp10-when">Before switching branches or running tests</div>
          <div class="ttp10-when">Before closing the editor or tab</div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-3.5 py-2.5">
          <div class="mb-0.5 w-full text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">Related</div>
          <span class="ttp10-pill">⌘ ⇧ S — Save As</span><span class="ttp10-pill">⌘ ⌥ S — Save All</span>
        </div>
      </div>
    </div>

    <div class="group relative">
      <div tabindex="0" role="button" aria-describedby="ttp10-k2" aria-keyshortcuts="Meta+Z" class="flex cursor-help items-center justify-between rounded-md px-3 py-2.5 transition-colors duration-100 group-hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp10-acc">
        <span class="text-[12.5px] text-ttp10-ink">Undo</span>
        <kbd class="flex items-center gap-1 not-italic"><span class="ttp10-key">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-key">Z</span></kbd>
      </div>
      <div id="ttp10-k2" role="tooltip" class="ttp10-card">
        <div class="border-b border-white/8 px-3.5 pt-3.5 pb-2.75">
          <div class="mb-1.75 text-[15px] font-semibold text-ttp10-bright">Undo</div>
          <kbd class="flex items-center gap-1.25 not-italic"><span class="ttp10-keybig">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-keybig">Z</span></kbd>
        </div>
        <p class="m-0 border-b border-white/6 px-3.5 py-2.75 font-ttp10-sans text-[11.5px] leading-[1.55] text-ttp10-body">Reverses the last editing action, stepping backwards through the undo history one action at a time. History is preserved across saves.</p>
        <div class="border-b border-white/6 px-3.5 py-2.5">
          <div class="mb-1.5 text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">When to use</div>
          <div class="ttp10-when">After accidentally deleting or overwriting text</div>
          <div class="ttp10-when">To compare before/after a refactor</div>
          <div class="ttp10-when">To recover from an unwanted auto-format</div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-3.5 py-2.5">
          <div class="mb-0.5 w-full text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">Related</div>
          <span class="ttp10-pill">⌘ ⇧ Z — Redo</span><span class="ttp10-pill">⌘ K U — Clear history</span>
        </div>
      </div>
    </div>

    <div class="group relative">
      <div tabindex="0" role="button" aria-describedby="ttp10-k3" aria-keyshortcuts="Meta+Shift+P" class="flex cursor-help items-center justify-between rounded-md px-3 py-2.5 transition-colors duration-100 group-hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp10-acc">
        <span class="text-[12.5px] text-ttp10-ink">Command palette</span>
        <kbd class="flex items-center gap-1 not-italic"><span class="ttp10-key">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-key">⇧</span><span class="ttp10-plus">+</span><span class="ttp10-key">P</span></kbd>
      </div>
      <div id="ttp10-k3" role="tooltip" class="ttp10-card">
        <div class="border-b border-white/8 px-3.5 pt-3.5 pb-2.75">
          <div class="mb-1.75 text-[15px] font-semibold text-ttp10-bright">Command Palette</div>
          <kbd class="flex items-center gap-1.25 not-italic"><span class="ttp10-keybig">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-keybig">⇧</span><span class="ttp10-plus">+</span><span class="ttp10-keybig">P</span></kbd>
        </div>
        <p class="m-0 border-b border-white/6 px-3.5 py-2.75 font-ttp10-sans text-[11.5px] leading-[1.55] text-ttp10-body">Opens a searchable list of every editor command, extension action and setting. The fastest way to trigger any feature without memorising its location.</p>
        <div class="border-b border-white/6 px-3.5 py-2.5">
          <div class="mb-1.5 text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">When to use</div>
          <div class="ttp10-when">To find any command without digging through menus</div>
          <div class="ttp10-when">To run a formatter, linter or task</div>
          <div class="ttp10-when">To change settings quickly by name</div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-3.5 py-2.5">
          <div class="mb-0.5 w-full text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">Related</div>
          <span class="ttp10-pill">⌘ P — Quick open file</span><span class="ttp10-pill">⌘ ⇧ O — Go to symbol</span>
        </div>
      </div>
    </div>

    <div class="group relative">
      <div tabindex="0" role="button" aria-describedby="ttp10-k4" aria-keyshortcuts="Meta+F" class="flex cursor-help items-center justify-between rounded-md px-3 py-2.5 transition-colors duration-100 group-hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp10-acc">
        <span class="text-[12.5px] text-ttp10-ink">Find in file</span>
        <kbd class="flex items-center gap-1 not-italic"><span class="ttp10-key">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-key">F</span></kbd>
      </div>
      <div id="ttp10-k4" role="tooltip" class="ttp10-card">
        <div class="border-b border-white/8 px-3.5 pt-3.5 pb-2.75">
          <div class="mb-1.75 text-[15px] font-semibold text-ttp10-bright">Find in File</div>
          <kbd class="flex items-center gap-1.25 not-italic"><span class="ttp10-keybig">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-keybig">F</span></kbd>
        </div>
        <p class="m-0 border-b border-white/6 px-3.5 py-2.75 font-ttp10-sans text-[11.5px] leading-[1.55] text-ttp10-body">Opens an inline search bar. Supports plain text, regular expressions and case-sensitive matching. Highlights all occurrences inside the active file.</p>
        <div class="border-b border-white/6 px-3.5 py-2.5">
          <div class="mb-1.5 text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">When to use</div>
          <div class="ttp10-when">To locate a variable, function or string in the file</div>
          <div class="ttp10-when">To count occurrences of a term before refactoring</div>
          <div class="ttp10-when">With regex to find patterns (e.g. unused imports)</div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-3.5 py-2.5">
          <div class="mb-0.5 w-full text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">Related</div>
          <span class="ttp10-pill">⌘ H — Find &amp; Replace</span><span class="ttp10-pill">⌘ ⇧ F — Find in workspace</span>
        </div>
      </div>
    </div>

    <div class="group relative">
      <div tabindex="0" role="button" aria-describedby="ttp10-k5" aria-keyshortcuts="Meta+/" class="flex cursor-help items-center justify-between rounded-md px-3 py-2.5 transition-colors duration-100 group-hover:bg-white/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp10-acc">
        <span class="text-[12.5px] text-ttp10-ink">Toggle comment</span>
        <kbd class="flex items-center gap-1 not-italic"><span class="ttp10-key">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-key">/</span></kbd>
      </div>
      <div id="ttp10-k5" role="tooltip" class="ttp10-card">
        <div class="border-b border-white/8 px-3.5 pt-3.5 pb-2.75">
          <div class="mb-1.75 text-[15px] font-semibold text-ttp10-bright">Toggle Comment</div>
          <kbd class="flex items-center gap-1.25 not-italic"><span class="ttp10-keybig">⌘</span><span class="ttp10-plus">+</span><span class="ttp10-keybig">/</span></kbd>
        </div>
        <p class="m-0 border-b border-white/6 px-3.5 py-2.75 font-ttp10-sans text-[11.5px] leading-[1.55] text-ttp10-body">Toggles line comments on the current line or all selected lines. Uses the correct comment syntax for the file's language automatically.</p>
        <div class="border-b border-white/6 px-3.5 py-2.5">
          <div class="mb-1.5 text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">When to use</div>
          <div class="ttp10-when">To temporarily disable a block of code for debugging</div>
          <div class="ttp10-when">To add an explanatory comment above a function</div>
          <div class="ttp10-when">To comment multiple lines at once (select first)</div>
        </div>
        <div class="flex flex-wrap gap-1.5 px-3.5 py-2.5">
          <div class="mb-0.5 w-full text-[8.5px] uppercase tracking-[0.1em] text-ttp10-dim">Related</div>
          <span class="ttp10-pill">⌘ ⇧ / — Block comment</span><span class="ttp10-pill">⌘ K C — Add comment</span>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp10-bg: #111116;
  --color-ttp10-bg: oklch(0.18 0.008 285);
  --color-ttp10-panel: #1c1c24;
  --color-ttp10-panel: oklch(0.23 0.01 285);
  --color-ttp10-bright: #f0f0f4;
  --color-ttp10-bright: oklch(0.95 0.004 285);
  --color-ttp10-ink: #c8c8d2;
  --color-ttp10-ink: oklch(0.83 0.008 285);
  --color-ttp10-body: #aaaab6;
  --color-ttp10-body: oklch(0.74 0.008 285);
  --color-ttp10-dim: #9494a2;
  --color-ttp10-dim: oklch(0.67 0.01 285);
  --color-ttp10-acc: #8b8bf5;
  --color-ttp10-acc: oklch(0.7 0.12 285);
  --font-ttp10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttp10-sans: 'Inter', system-ui, sans-serif;
}

.ttp-10 {
  width: 100%;
  min-height: 100svh;
}
/* One keycap recipe at two scales, one card shell, one bullet, one
   pill — each repeated five times or more across the demo. */

.ttp-10 .ttp10-key {
  @apply inline-flex items-center rounded-[4px] border border-white/15 border-b-2 border-b-white/20 bg-white/8 px-1.75 py-0.75 text-[10.5px] font-medium leading-none tracking-[0.02em] text-ttp10-ink;
}

.ttp-10 .ttp10-keybig {
  @apply inline-flex items-center rounded-[5px] border border-white/16 border-b-3 border-b-white/22 bg-white/8 px-2.5 py-1 text-[11.5px] font-semibold text-ttp10-bright;
}

.ttp-10 .ttp10-plus {
  @apply text-[9.5px] text-ttp10-dim;
}

.ttp-10 .ttp10-when {
  @apply relative mb-1 pl-2.5 font-ttp10-sans text-[10.5px] leading-[1.4] text-ttp10-body before:absolute before:left-0 before:-top-px before:text-[11px] before:text-ttp10-dim before:content-['›'];
}

.ttp-10 .ttp10-pill {
  @apply rounded-[4px] border border-white/10 bg-white/6 px-1.75 py-0.5 text-[10px] text-ttp10-body;
}

.ttp-10 .ttp10-card {
  @apply pointer-events-none invisible absolute top-1/2 right-[calc(100%+12px)] z-30 block w-65 -translate-y-1/2 -translate-x-1.5 overflow-hidden rounded-[11px] border border-white/10 bg-ttp10-panel text-left opacity-0 shadow-[0_16px_44px_rgba(0,0,0,0.85)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-x-0 group-focus-within:opacity-100;
}

@media (max-width: 1279px) {
  .ttp-10 .ttp10-card {
    @apply static hidden mt-2 w-full translate-x-0 translate-y-0 group-hover:block group-focus-within:block;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-split-button-anchor-popover-dropdown/"
title: "Tailwind Split Button with Anchor-Positioned Popover Dropdown (No JS)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A primary action fused to a caret that opens a real popover menu, tethered with CSS Anchor Positioning written as arbitrary properties —…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split Button with Anchor-Positioned Popover Dropdown (No JS)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-split-button-anchor-popover-dropdown/

A primary action fused to a caret that opens a real popover menu, tethered with CSS Anchor Positioning written as arbitrary properties — [anchor-name:--tbg01-anc] on the caret, [position-anchor:--tbg01-anc] top-[anchor(bottom)] on the menu. The menu lives in the top layer, so no overflow-hidden parent can clip it, and v4's open: + starting: variants animate it in and out. Zero JavaScript.
## HTML
```html
<section class="tbg-01 w-full min-h-svh grid justify-items-center content-start bg-tbg01-bg bg-[radial-gradient(110%_80%_at_50%_0%,var(--color-tbg01-glow),transparent_70%)] px-5 pt-32 pb-16 font-tbg01-sans text-tbg01-ink" aria-label="Anchor-positioned popover split button demo">
  <div class="grid justify-items-center gap-10">
    <div class="group/split relative inline-flex rounded-2xl shadow-tbg01-lift">
      <button type="button" class="inline-flex h-12 cursor-pointer items-center gap-2.5 rounded-l-2xl bg-tbg01-acc pr-5 pl-4.5 text-[15px] font-semibold text-white transition hover:brightness-110 active:brightness-95 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg01-acc-d">
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>
        Export CSV
      </button>
      <button type="button" popovertarget="tbg01-menu" aria-label="More export formats" class="[anchor-name:--tbg01-anc] grid h-12 w-12 cursor-pointer place-items-center rounded-r-2xl border-l border-black/20 bg-tbg01-acc-d text-white transition hover:brightness-110 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg01-acc-d">
        <svg class="transition-transform duration-300 group-has-[:popover-open]/split:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <div id="tbg01-menu" popover role="menu" aria-label="Export formats" class="m-0 mt-2 bottom-auto left-auto top-[anchor(bottom)] right-[anchor(right)] [position-anchor:--tbg01-anc] [position-try-fallbacks:flip-block] w-64 rounded-2xl border border-tbg01-line bg-white p-1.5 font-tbg01-sans text-tbg01-ink shadow-tbg01-menu opacity-0 -translate-y-1.5 transition-[opacity,translate,display,overlay] duration-200 transition-discrete open:translate-y-0 open:opacity-100 starting:open:-translate-y-1.5 starting:open:opacity-0 motion-reduce:translate-y-0 not-supports-[anchor-name:--x]:inset-0 not-supports-[anchor-name:--x]:m-auto not-supports-[anchor-name:--x]:h-fit">
        <p class="px-3 pt-2 pb-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-tbg01-mut">Export as</p>
        <button type="button" role="menuitem" popovertarget="tbg01-menu" popovertargetaction="hide" class="flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-left text-[14.5px] font-medium hover:bg-tbg01-tint focus-visible:bg-tbg01-tint focus-visible:outline-2 focus-visible:outline-tbg01-acc">JSON <span class="ml-auto font-tbg01-mono text-xs text-tbg01-mut">.json</span></button>
        <button type="button" role="menuitem" popovertarget="tbg01-menu" popovertargetaction="hide" class="flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-left text-[14.5px] font-medium hover:bg-tbg01-tint focus-visible:bg-tbg01-tint focus-visible:outline-2 focus-visible:outline-tbg01-acc">Excel workbook <span class="ml-auto font-tbg01-mono text-xs text-tbg01-mut">.xlsx</span></button>
        <button type="button" role="menuitem" popovertarget="tbg01-menu" popovertargetaction="hide" class="flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-left text-[14.5px] font-medium hover:bg-tbg01-tint focus-visible:bg-tbg01-tint focus-visible:outline-2 focus-visible:outline-tbg01-acc">PDF report <span class="ml-auto font-tbg01-mono text-xs text-tbg01-mut">.pdf</span></button>
        <div role="separator" class="mx-2 my-1.5 h-px bg-tbg01-line"></div>
        <button type="button" role="menuitem" popovertarget="tbg01-menu" popovertargetaction="hide" class="flex min-h-11 w-full cursor-pointer items-center gap-3 rounded-xl px-3 text-left text-[14.5px] font-medium hover:bg-tbg01-tint focus-visible:bg-tbg01-tint focus-visible:outline-2 focus-visible:outline-tbg01-acc">Copy to clipboard <kbd class="ml-auto rounded-md border border-tbg01-line px-1.5 py-0.5 font-tbg01-mono text-[11px] text-tbg01-mut">⌘C</kbd></button>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tbg01-ink/10 bg-white/60 px-3.5 py-2 font-tbg01-mono text-[11.5px] text-tbg01-mut">popover · [anchor-name] · open: + starting:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg01-bg: #eceef3;
  --color-tbg01-bg: oklch(0.95 0.006 265);
  --color-tbg01-glow: #ffffff;
  --color-tbg01-ink: #2b1a15;
  --color-tbg01-ink: oklch(0.25 0.03 35);
  --color-tbg01-mut: #6e5d57;
  --color-tbg01-mut: oklch(0.5 0.025 35);
  --color-tbg01-line: #efe3df;
  --color-tbg01-line: oklch(0.92 0.015 35);
  --color-tbg01-tint: #fcefeb;
  --color-tbg01-tint: oklch(0.96 0.02 35);
  --color-tbg01-acc: #e5452f;
  --color-tbg01-acc: oklch(0.6 0.2 30);
  --color-tbg01-acc-d: #c4321f;
  --color-tbg01-acc-d: oklch(0.52 0.19 30);
  --shadow-tbg01-lift: 0 14px 34px -16px rgb(120 30 10 / 0.55);
  --shadow-tbg01-menu: 0 26px 54px -22px rgb(120 40 20 / 0.45), 0 2px 6px rgb(0 0 0 / 0.04);
  --font-tbg01-sans: 'Geist', system-ui, sans-serif;
  --font-tbg01-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-01 {
  width: 100%;
  min-height: 100svh;
}
```

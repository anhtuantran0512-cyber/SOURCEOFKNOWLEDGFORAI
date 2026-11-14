---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-navigation-bar-rail-drawer/"
title: "Tailwind Material Design Navigation Bar, Rail and Drawer"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "The three M3 navigation containers side by side &mdash; bottom navigation bar, rail and standard drawer &mdash; all driven by radios and peer-checked:, so…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Navigation Bar, Rail and Drawer
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-navigation-bar-rail-drawer/

The three M3 navigation containers side by side &mdash; bottom navigation bar, rail and standard drawer &mdash; all driven by radios and peer-checked:, so the active tab, its pill indicator and its filled icon all change with no JavaScript. The port's win is the indicator: an M3 active pill is one peer-checked: background on the icon box, not a ::before rule per item.
## HTML
```html
<section class="tmd-03 w-full min-h-svh bg-tmd03-bg font-tmd03-sans text-tmd03-onsurface px-5 py-9" aria-label="Material Design navigation containers demo">
  <div class="w-[min(1100px,100%)] mx-auto grid gap-6">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Navigation bar, rail &amp; drawer</h2>
      <p class="text-sm text-tmd03-onvariant">One item recipe, three containers. Radios carry the state; <code class="font-tmd03-mono text-[12px]">peer-checked:</code> carries the look.</p>
    </header>

    <div class="grid gap-5 grid-cols-[repeat(auto-fit,minmax(min(320px,100%),1fr))]">
      <div class="grid grid-rows-[1fr_auto] min-h-80 rounded-3xl overflow-hidden bg-tmd03-surface shadow-tmd03-1">
        <div class="grid content-start gap-3 p-5">
          <div class="flex items-center gap-3">
            <button type="button" aria-label="Open navigation" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd03-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd03-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd03-icon text-[22px] leading-none" aria-hidden="true">menu</span></button>
            <span class="text-[17px] font-medium">Inbox</span>
            <span class="ml-auto font-tmd03-mono text-[11px] uppercase tracking-[0.08em] text-tmd03-onvariant">Bottom bar</span>
          </div>
          <div class="h-3 w-[78%] rounded-full bg-tmd03-outlinevariant" aria-hidden="true"></div>
          <div class="h-3 w-[62%] rounded-full bg-tmd03-outlinevariant" aria-hidden="true"></div>
          <div class="h-3 w-[70%] rounded-full bg-tmd03-outlinevariant" aria-hidden="true"></div>
        </div>
        <nav aria-label="Primary" class="group/bar grid grid-cols-4 border-t border-tmd03-outlinevariant bg-tmd03-surfacecontainer">
          <input type="radio" name="tmd03-bar" id="tmd03-bar-1" class="peer/b1 sr-only" checked>
          <label for="tmd03-bar-1" class="grid justify-items-center gap-1 pt-3 pb-2.5 cursor-pointer text-tmd03-onvariant text-xs font-medium transition-colors duration-200 group-has-[#tmd03-bar-1:checked]/bar:text-tmd03-onsurface peer-focus-visible/b1:outline-2 peer-focus-visible/b1:-outline-offset-2 peer-focus-visible/b1:outline-tmd03-primary">
            <span class="relative grid place-items-center w-16 h-8 rounded-full transition-colors duration-200 group-has-[#tmd03-bar-1:checked]/bar:bg-tmd03-secondarycontainer group-has-[#tmd03-bar-1:checked]/bar:text-tmd03-onsecondarycontainer motion-reduce:transition-none"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-bar-1:checked]/bar:[font-variation-settings:'FILL'_1]" aria-hidden="true">inbox</span></span>Inbox
          </label>
          <input type="radio" name="tmd03-bar" id="tmd03-bar-2" class="peer/b2 sr-only">
          <label for="tmd03-bar-2" class="grid justify-items-center gap-1 pt-3 pb-2.5 cursor-pointer text-tmd03-onvariant text-xs font-medium transition-colors duration-200 group-has-[#tmd03-bar-2:checked]/bar:text-tmd03-onsurface peer-focus-visible/b2:outline-2 peer-focus-visible/b2:-outline-offset-2 peer-focus-visible/b2:outline-tmd03-primary">
            <span class="relative grid place-items-center w-16 h-8 rounded-full transition-colors duration-200 group-has-[#tmd03-bar-2:checked]/bar:bg-tmd03-secondarycontainer group-has-[#tmd03-bar-2:checked]/bar:text-tmd03-onsecondarycontainer motion-reduce:transition-none"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-bar-2:checked]/bar:[font-variation-settings:'FILL'_1]" aria-hidden="true">send</span><b class="absolute top-0.5 right-2.5 min-w-4 h-4 px-1 grid place-items-center rounded-full bg-tmd03-error text-tmd03-onerror font-tmd03-mono text-[10px] tabular-nums">3</b></span>Sent
          </label>
          <input type="radio" name="tmd03-bar" id="tmd03-bar-3" class="peer/b3 sr-only">
          <label for="tmd03-bar-3" class="grid justify-items-center gap-1 pt-3 pb-2.5 cursor-pointer text-tmd03-onvariant text-xs font-medium transition-colors duration-200 group-has-[#tmd03-bar-3:checked]/bar:text-tmd03-onsurface peer-focus-visible/b3:outline-2 peer-focus-visible/b3:-outline-offset-2 peer-focus-visible/b3:outline-tmd03-primary">
            <span class="relative grid place-items-center w-16 h-8 rounded-full transition-colors duration-200 group-has-[#tmd03-bar-3:checked]/bar:bg-tmd03-secondarycontainer group-has-[#tmd03-bar-3:checked]/bar:text-tmd03-onsecondarycontainer motion-reduce:transition-none"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-bar-3:checked]/bar:[font-variation-settings:'FILL'_1]" aria-hidden="true">drafts</span></span>Drafts
          </label>
          <input type="radio" name="tmd03-bar" id="tmd03-bar-4" class="peer/b4 sr-only">
          <label for="tmd03-bar-4" class="grid justify-items-center gap-1 pt-3 pb-2.5 cursor-pointer text-tmd03-onvariant text-xs font-medium transition-colors duration-200 group-has-[#tmd03-bar-4:checked]/bar:text-tmd03-onsurface peer-focus-visible/b4:outline-2 peer-focus-visible/b4:-outline-offset-2 peer-focus-visible/b4:outline-tmd03-primary">
            <span class="relative grid place-items-center w-16 h-8 rounded-full transition-colors duration-200 group-has-[#tmd03-bar-4:checked]/bar:bg-tmd03-secondarycontainer group-has-[#tmd03-bar-4:checked]/bar:text-tmd03-onsecondarycontainer motion-reduce:transition-none"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-bar-4:checked]/bar:[font-variation-settings:'FILL'_1]" aria-hidden="true">settings</span></span>Settings
          </label>
        </nav>
      </div>

      <div class="grid grid-cols-[80px_1fr] min-h-80 rounded-3xl overflow-hidden bg-tmd03-surface shadow-tmd03-1">
        <nav aria-label="Rail" class="group/rail grid content-start gap-2 py-4 bg-tmd03-surfacecontainer border-r border-tmd03-outlinevariant">
          <button type="button" aria-label="Open menu" class="relative overflow-hidden grid place-items-center justify-self-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd03-onsurface mb-1 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd03-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd03-icon text-[22px] leading-none" aria-hidden="true">menu</span></button>
          <input type="radio" name="tmd03-rail" id="tmd03-rail-1" class="peer/r1 sr-only" checked>
          <label for="tmd03-rail-1" class="grid justify-items-center gap-1 py-1.5 cursor-pointer text-tmd03-onvariant text-[11px] font-medium group-has-[#tmd03-rail-1:checked]/rail:text-tmd03-onsurface peer-focus-visible/r1:outline-2 peer-focus-visible/r1:-outline-offset-2 peer-focus-visible/r1:outline-tmd03-primary">
            <span class="grid place-items-center w-14 h-8 rounded-full transition-colors duration-200 group-has-[#tmd03-rail-1:checked]/rail:bg-tmd03-secondarycontainer group-has-[#tmd03-rail-1:checked]/rail:text-tmd03-onsecondarycontainer motion-reduce:transition-none"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-rail-1:checked]/rail:[font-variation-settings:'FILL'_1]" aria-hidden="true">dashboard</span></span>Home
          </label>
          <input type="radio" name="tmd03-rail" id="tmd03-rail-2" class="peer/r2 sr-only">
          <label for="tmd03-rail-2" class="grid justify-items-center gap-1 py-1.5 cursor-pointer text-tmd03-onvariant text-[11px] font-medium group-has-[#tmd03-rail-2:checked]/rail:text-tmd03-onsurface peer-focus-visible/r2:outline-2 peer-focus-visible/r2:-outline-offset-2 peer-focus-visible/r2:outline-tmd03-primary">
            <span class="grid place-items-center w-14 h-8 rounded-full transition-colors duration-200 group-has-[#tmd03-rail-2:checked]/rail:bg-tmd03-secondarycontainer group-has-[#tmd03-rail-2:checked]/rail:text-tmd03-onsecondarycontainer motion-reduce:transition-none"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-rail-2:checked]/rail:[font-variation-settings:'FILL'_1]" aria-hidden="true">bar_chart</span></span>Reports
          </label>
          <input type="radio" name="tmd03-rail" id="tmd03-rail-3" class="peer/r3 sr-only">
          <label for="tmd03-rail-3" class="grid justify-items-center gap-1 py-1.5 cursor-pointer text-tmd03-onvariant text-[11px] font-medium group-has-[#tmd03-rail-3:checked]/rail:text-tmd03-onsurface peer-focus-visible/r3:outline-2 peer-focus-visible/r3:-outline-offset-2 peer-focus-visible/r3:outline-tmd03-primary">
            <span class="grid place-items-center w-14 h-8 rounded-full transition-colors duration-200 group-has-[#tmd03-rail-3:checked]/rail:bg-tmd03-secondarycontainer group-has-[#tmd03-rail-3:checked]/rail:text-tmd03-onsecondarycontainer motion-reduce:transition-none"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-rail-3:checked]/rail:[font-variation-settings:'FILL'_1]" aria-hidden="true">group</span></span>Team
          </label>
        </nav>
        <div class="grid content-start gap-3 p-5">
          <span class="font-tmd03-mono text-[11px] uppercase tracking-[0.08em] text-tmd03-onvariant">Navigation rail &middot; 80px</span>
          <div class="h-28 rounded-2xl bg-linear-[150deg,#c62828,#ef5350_70%,#ffcdd2]" aria-hidden="true"></div>
          <div class="h-3 w-[72%] rounded-full bg-tmd03-outlinevariant" aria-hidden="true"></div>
          <div class="h-3 w-[54%] rounded-full bg-tmd03-outlinevariant" aria-hidden="true"></div>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-[repeat(auto-fit,minmax(min(256px,100%),1fr))] gap-5">
      <nav aria-label="Drawer" class="group/dr has-checked:ring-1 has-checked:ring-tmd03-outlinevariant grid content-start gap-1 p-3 rounded-3xl bg-tmd03-surfacecontainer">
        <span class="px-4 py-2 font-tmd03-mono text-[11px] uppercase tracking-[0.08em] text-tmd03-onvariant">Standard drawer</span>
        <input type="radio" name="tmd03-drawer" id="tmd03-dr-1" class="peer/d1 sr-only" checked>
        <label for="tmd03-dr-1" class="relative overflow-hidden flex items-center gap-3 min-h-14 px-4 rounded-full cursor-pointer text-sm font-medium text-tmd03-onvariant transition-colors duration-200 group-has-[#tmd03-dr-1:checked]/dr:bg-tmd03-secondarycontainer group-has-[#tmd03-dr-1:checked]/dr:text-tmd03-onsecondarycontainer peer-focus-visible/d1:outline-2 peer-focus-visible/d1:-outline-offset-2 peer-focus-visible/d1:outline-tmd03-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-dr-1:checked]/dr:[font-variation-settings:'FILL'_1]" aria-hidden="true">inbox</span>Inbox<span class="ml-auto font-tmd03-mono text-xs tabular-nums">24</span></label>
        <input type="radio" name="tmd03-drawer" id="tmd03-dr-2" class="peer/d2 sr-only">
        <label for="tmd03-dr-2" class="relative overflow-hidden flex items-center gap-3 min-h-14 px-4 rounded-full cursor-pointer text-sm font-medium text-tmd03-onvariant transition-colors duration-200 group-has-[#tmd03-dr-2:checked]/dr:bg-tmd03-secondarycontainer group-has-[#tmd03-dr-2:checked]/dr:text-tmd03-onsecondarycontainer peer-focus-visible/d2:outline-2 peer-focus-visible/d2:-outline-offset-2 peer-focus-visible/d2:outline-tmd03-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-dr-2:checked]/dr:[font-variation-settings:'FILL'_1]" aria-hidden="true">star</span>Starred<span class="ml-auto font-tmd03-mono text-xs tabular-nums">6</span></label>
        <input type="radio" name="tmd03-drawer" id="tmd03-dr-3" class="peer/d3 sr-only">
        <label for="tmd03-dr-3" class="relative overflow-hidden flex items-center gap-3 min-h-14 px-4 rounded-full cursor-pointer text-sm font-medium text-tmd03-onvariant transition-colors duration-200 group-has-[#tmd03-dr-3:checked]/dr:bg-tmd03-secondarycontainer group-has-[#tmd03-dr-3:checked]/dr:text-tmd03-onsecondarycontainer peer-focus-visible/d3:outline-2 peer-focus-visible/d3:-outline-offset-2 peer-focus-visible/d3:outline-tmd03-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd03-icon text-[22px] leading-none group-has-[#tmd03-dr-3:checked]/dr:[font-variation-settings:'FILL'_1]" aria-hidden="true">label</span>Labels</label>
        <hr class="my-2 border-0 border-t border-tmd03-outlinevariant">
        <label for="tmd03-dr-1" class="px-4 pb-1 text-xs text-tmd03-onvariant">Selecting any destination adds a hairline ring to this drawer via <span class="font-tmd03-mono text-[11px]">has-checked:</span>.</label>
      </nav>
      <div class="grid content-center gap-2 p-6 rounded-3xl bg-tmd03-surface shadow-tmd03-1">
        <h3 class="text-lg font-medium">Why radios, not divs</h3>
        <p class="text-sm leading-6 text-tmd03-onvariant text-pretty">A native radio group is one tab stop, arrow-key traversable, announced as &ldquo;2 of 4&rdquo;, and restores on back-navigation. Every one of those behaviours would be JavaScript in a <span class="font-tmd03-mono text-[12px]">div role=&quot;tab&quot;</span> rebuild &mdash; and the styling hook, <span class="font-tmd03-mono text-[12px]">peer-checked:</span>, is shorter than the class-toggling it replaces.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd03-bg: #fafafa;
  --color-tmd03-bg: oklch(0.985 0 89.9);
  --color-tmd03-surface: #fffbfe;
  --color-tmd03-surface: oklch(0.992 0.006 334);
  --color-tmd03-surfacecontainer: #f3eff4;
  --color-tmd03-surfacecontainer: oklch(0.957 0.008 319.4);
  --color-tmd03-primary: #c62828;
  --color-tmd03-primary: oklch(0.539 0.194 26.7);
  --color-tmd03-secondarycontainer: #ffdad6;
  --color-tmd03-secondarycontainer: oklch(0.918 0.042 25.2);
  --color-tmd03-onsecondarycontainer: #410002;
  --color-tmd03-onsecondarycontainer: oklch(0.236 0.096 27.2);
  --color-tmd03-onsurface: #1c1b1f;
  --color-tmd03-onsurface: oklch(0.225 0.008 297.2);
  --color-tmd03-onvariant: #4f4b52;
  --color-tmd03-onvariant: oklch(0.419 0.013 311);
  --color-tmd03-outlinevariant: #ddd5dd;
  --color-tmd03-outlinevariant: oklch(0.882 0.014 325.7);
  --color-tmd03-error: #b3261e;
  --color-tmd03-error: oklch(0.501 0.178 28.7);
  --color-tmd03-onerror: #ffffff;
  --color-tmd03-onerror: oklch(1 0 89.9);
  --font-tmd03-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd03-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd03-icon: 'Material Symbols Outlined';
  --shadow-tmd03-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
}

.tmd-03 {
  width: 100%;
  min-height: 100svh;
}

.tmd-03 [class*="font-tmd03-icon"] {
  font-feature-settings: 'liga';
}
```

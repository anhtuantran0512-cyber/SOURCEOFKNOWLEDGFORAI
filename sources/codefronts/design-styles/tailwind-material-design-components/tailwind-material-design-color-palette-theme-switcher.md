---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-color-palette-theme-switcher/"
title: "Tailwind Material Design Color Palette and Theme Switcher"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "The M3 colour system laid out as role pairs &mdash; primary / on-primary, container / on-container, surface tiers, error &mdash; with four themes switchable…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Color Palette and Theme Switcher
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-color-palette-theme-switcher/

The M3 colour system laid out as role pairs &mdash; primary / on-primary, container / on-container, surface tiers, error &mdash; with four themes switchable by radio and no JavaScript. It is also the collection's one honest lesson about v4: @theme tokens are build-time, so a runtime theme swap uses plain custom properties consumed as bg-[var(--p)], and knowing which to reach for is the whole skill.
## HTML
```html
<section class="tmd-13 w-full min-h-svh bg-tmd13-bg font-tmd13-sans text-tmd13-onsurface px-5 py-9" aria-label="Material Design colour roles and theme switcher demo">
  <div class="w-[min(960px,100%)] mx-auto grid gap-6 [--p:#6750a4] [--on-p:#ffffff] [--pc:#eaddff] [--on-pc:#21005d] [--s:#625b71] [--sc:#e8def8] [--t:#7d5260] [--tc:#ffd8e4] has-[#tmd13-teal:checked]:[--p:#006874] has-[#tmd13-teal:checked]:[--pc:#a2d0d8] has-[#tmd13-teal:checked]:[--on-pc:#001f25] has-[#tmd13-teal:checked]:[--s:#4a6267] has-[#tmd13-teal:checked]:[--sc:#cce8ed] has-[#tmd13-teal:checked]:[--t:#525e7d] has-[#tmd13-teal:checked]:[--tc:#dae2ff] has-[#tmd13-rose:checked]:[--p:#b5271f] has-[#tmd13-rose:checked]:[--pc:#ffdad6] has-[#tmd13-rose:checked]:[--on-pc:#410002] has-[#tmd13-rose:checked]:[--s:#775652] has-[#tmd13-rose:checked]:[--sc:#ffdad6] has-[#tmd13-rose:checked]:[--t:#6c5d2f] has-[#tmd13-rose:checked]:[--tc:#f6e1a6] has-[#tmd13-forest:checked]:[--p:#1f6b34] has-[#tmd13-forest:checked]:[--pc:#b8f2be] has-[#tmd13-forest:checked]:[--on-pc:#00210c] has-[#tmd13-forest:checked]:[--s:#51634f] has-[#tmd13-forest:checked]:[--sc:#d4e8cf] has-[#tmd13-forest:checked]:[--t:#39656b] has-[#tmd13-forest:checked]:[--tc:#bcebf2] transition-[background-color] duration-300">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Colour roles &amp; runtime themes</h2>
      <p class="text-sm text-tmd13-onvariant text-pretty"><code class="font-tmd13-mono text-[12px]">@theme</code> tokens are build-time; a switcher needs plain custom properties read as <code class="font-tmd13-mono text-[12px]">bg-[var(--p)]</code>. Both are here, doing the jobs they are good at.</p>
    </header>

    <fieldset class="border-0 p-0 m-0">
      <legend class="mb-2 font-tmd13-mono text-[11px] uppercase tracking-[0.1em] text-tmd13-onvariant">Theme</legend>
      <div class="flex flex-wrap gap-2">
        <input type="radio" name="tmd13-theme" id="tmd13-purple" class="peer/pu sr-only" checked>
        <label for="tmd13-purple" class="inline-flex items-center gap-2 min-h-11 px-4 rounded-full border border-tmd13-outlinevariant cursor-pointer text-sm font-medium peer-checked/pu:bg-[var(--p)] peer-checked/pu:text-[var(--on-p)] peer-checked/pu:border-transparent peer-focus-visible/pu:outline-2 peer-focus-visible/pu:outline-offset-2 peer-focus-visible/pu:outline-[var(--p)] transition-colors duration-200"><span class="w-4 h-4 rounded-full bg-[#6750a4]"></span>Purple</label>
        <input type="radio" name="tmd13-theme" id="tmd13-teal" class="peer/te sr-only">
        <label for="tmd13-teal" class="inline-flex items-center gap-2 min-h-11 px-4 rounded-full border border-tmd13-outlinevariant cursor-pointer text-sm font-medium peer-checked/te:bg-[var(--p)] peer-checked/te:text-[var(--on-p)] peer-checked/te:border-transparent peer-focus-visible/te:outline-2 peer-focus-visible/te:outline-offset-2 peer-focus-visible/te:outline-[var(--p)] transition-colors duration-200"><span class="w-4 h-4 rounded-full bg-[#006874]"></span>Teal</label>
        <input type="radio" name="tmd13-theme" id="tmd13-rose" class="peer/ro sr-only">
        <label for="tmd13-rose" class="inline-flex items-center gap-2 min-h-11 px-4 rounded-full border border-tmd13-outlinevariant cursor-pointer text-sm font-medium peer-checked/ro:bg-[var(--p)] peer-checked/ro:text-[var(--on-p)] peer-checked/ro:border-transparent peer-focus-visible/ro:outline-2 peer-focus-visible/ro:outline-offset-2 peer-focus-visible/ro:outline-[var(--p)] transition-colors duration-200"><span class="w-4 h-4 rounded-full bg-[#b5271f]"></span>Rose</label>
        <input type="radio" name="tmd13-theme" id="tmd13-forest" class="peer/fo sr-only">
        <label for="tmd13-forest" class="inline-flex items-center gap-2 min-h-11 px-4 rounded-full border border-tmd13-outlinevariant cursor-pointer text-sm font-medium peer-checked/fo:bg-[var(--p)] peer-checked/fo:text-[var(--on-p)] peer-checked/fo:border-transparent peer-focus-visible/fo:outline-2 peer-focus-visible/fo:outline-offset-2 peer-focus-visible/fo:outline-[var(--p)] transition-colors duration-200"><span class="w-4 h-4 rounded-full bg-[#1f6b34]"></span>Forest</label>
      </div>
    </fieldset>

    <div class="grid gap-3 grid-cols-[repeat(auto-fit,minmax(min(150px,100%),1fr))]">
      <div class="grid content-between gap-6 min-h-28 p-4 rounded-2xl bg-[var(--p)] text-[var(--on-p)] transition-[background-color,color] duration-300"><b class="text-[13px] font-medium">Primary</b><span class="font-tmd13-mono text-[11px] opacity-80">on-primary</span></div>
      <div class="grid content-between gap-6 min-h-28 p-4 rounded-2xl bg-[var(--pc)] text-[var(--on-pc)] transition-[background-color,color] duration-300"><b class="text-[13px] font-medium">Primary container</b><span class="font-tmd13-mono text-[11px] opacity-80">on-primary-container</span></div>
      <div class="grid content-between gap-6 min-h-28 p-4 rounded-2xl bg-[var(--s)] text-white transition-[background-color] duration-300"><b class="text-[13px] font-medium">Secondary</b><span class="font-tmd13-mono text-[11px] opacity-80">on-secondary</span></div>
      <div class="grid content-between gap-6 min-h-28 p-4 rounded-2xl bg-[var(--sc)] text-[#1d192b] transition-[background-color] duration-300"><b class="text-[13px] font-medium">Secondary container</b><span class="font-tmd13-mono text-[11px] opacity-70">on-secondary-container</span></div>
      <div class="grid content-between gap-6 min-h-28 p-4 rounded-2xl bg-[var(--t)] text-white transition-[background-color] duration-300"><b class="text-[13px] font-medium">Tertiary</b><span class="font-tmd13-mono text-[11px] opacity-80">on-tertiary</span></div>
      <div class="grid content-between gap-6 min-h-28 p-4 rounded-2xl bg-[var(--tc)] text-[#31111d] transition-[background-color] duration-300"><b class="text-[13px] font-medium">Tertiary container</b><span class="font-tmd13-mono text-[11px] opacity-70">on-tertiary-container</span></div>
      <div class="grid content-between gap-6 min-h-28 p-4 rounded-2xl bg-tmd13-error text-white"><b class="text-[13px] font-medium">Error</b><span class="font-tmd13-mono text-[11px] opacity-80">on-error</span></div>
      <div class="grid content-between gap-6 min-h-28 p-4 rounded-2xl bg-tmd13-surface text-tmd13-onsurface border border-tmd13-outlinevariant"><b class="text-[13px] font-medium">Surface</b><span class="font-tmd13-mono text-[11px] text-tmd13-onvariant">on-surface</span></div>
    </div>

    <div class="grid gap-4 p-5.5 rounded-3xl bg-tmd13-surface border border-tmd13-outlinevariant">
      <span class="font-tmd13-mono text-[11px] uppercase tracking-[0.1em] text-tmd13-onvariant">Tonal ramp from the live seed &mdash; color-mix()</span>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(64px,1fr))] gap-1 overflow-hidden rounded-xl">
        <div class="h-16 bg-[color-mix(in_oklab,var(--p)_12%,white)] transition-[background-color] duration-300"></div>
        <div class="h-16 bg-[color-mix(in_oklab,var(--p)_28%,white)] transition-[background-color] duration-300"></div>
        <div class="h-16 bg-[color-mix(in_oklab,var(--p)_46%,white)] transition-[background-color] duration-300"></div>
        <div class="h-16 bg-[color-mix(in_oklab,var(--p)_68%,white)] transition-[background-color] duration-300"></div>
        <div class="h-16 bg-[var(--p)] transition-[background-color] duration-300"></div>
        <div class="h-16 bg-[color-mix(in_oklab,var(--p)_78%,black)] transition-[background-color] duration-300"></div>
        <div class="h-16 bg-[color-mix(in_oklab,var(--p)_58%,black)] transition-[background-color] duration-300"></div>
        <div class="h-16 bg-[color-mix(in_oklab,var(--p)_34%,black)] transition-[background-color] duration-300"></div>
      </div>
      <p class="text-sm leading-6 text-tmd13-onvariant text-pretty">Eight tone stops from one seed. M3 derives its whole palette this way, which is why a theme switcher only needs to move one value.</p>
    </div>

    <div class="grid gap-3 p-5.5 rounded-3xl bg-tmd13-surface border border-tmd13-outlinevariant">
      <span class="font-tmd13-mono text-[11px] uppercase tracking-[0.1em] text-tmd13-onvariant">Components under the live theme</span>
      <div class="flex flex-wrap items-center gap-3">
        <button type="button" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full border-0 bg-[var(--p)] text-[var(--on-p)] cursor-pointer text-sm font-medium transition-[background-color] duration-300 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--p)] before:absolute before:inset-0 before:bg-[color-mix(in_oklab,var(--on-p)_8%,transparent)] before:opacity-0 before:transition-opacity hover:before:opacity-100"><span class="font-tmd13-icon text-[18px] leading-none" aria-hidden="true">palette</span>Filled</button>
        <button type="button" class="relative overflow-hidden inline-flex items-center min-h-10 px-6 rounded-full bg-[var(--pc)] text-[var(--on-pc)] border-0 cursor-pointer text-sm font-medium transition-[background-color] duration-300 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--p)] before:absolute before:inset-0 before:bg-[color-mix(in_oklab,var(--on-pc)_8%,transparent)] before:opacity-0 before:transition-opacity hover:before:opacity-100">Tonal</button>
        <span class="inline-flex items-center gap-2 h-8 px-3 rounded-lg bg-[var(--tc)] text-[#31111d] text-xs font-medium transition-[background-color] duration-300">Tertiary chip</span>
        <span class="inline-flex items-center h-8 px-3 rounded-lg bg-[color-mix(in_oklab,var(--p)_12%,transparent)] text-[var(--p)] text-xs font-medium">12% state layer</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd13-bg: #f7f4fb;
  --color-tmd13-bg: oklch(0.971 0.01 305.4);
  --color-tmd13-surface: #fffbfe;
  --color-tmd13-surface: oklch(0.992 0.006 334);
  --color-tmd13-onsurface: #1c1b1f;
  --color-tmd13-onsurface: oklch(0.225 0.008 297.2);
  --color-tmd13-onvariant: #4a4458;
  --color-tmd13-onvariant: oklch(0.401 0.034 298.6);
  --color-tmd13-outlinevariant: #d8d2e0;
  --color-tmd13-outlinevariant: oklch(0.873 0.02 305.2);
  --color-tmd13-error: #b3261e;
  --color-tmd13-error: oklch(0.501 0.178 28.7);
  --font-tmd13-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd13-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd13-icon: 'Material Symbols Outlined';
}

.tmd-13 {
  width: 100%;
  min-height: 100svh;
}

.tmd-13 .font-tmd13-icon {
  font-feature-settings: 'liga';
}
```

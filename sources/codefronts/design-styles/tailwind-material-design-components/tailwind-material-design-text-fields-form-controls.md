---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-text-fields-form-controls/"
title: "Tailwind Material Design Text Fields and Form Controls"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "Filled and outlined text fields with true floating labels, plus select, textarea, checkbox, radio, switch and slider &mdash; and every one of them is…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Text Fields and Form Controls
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-text-fields-form-controls/

Filled and outlined text fields with true floating labels, plus select, textarea, checkbox, radio, switch and slider &mdash; and every one of them is peer-driven, so the label, the underline and the helper text all read the input's own state. The port also upgrades validation: user-invalid: shows errors only after the user has actually interacted, which the CSS version's :invalid could not do.
## HTML
```html
<section class="tmd-04 w-full min-h-svh bg-tmd04-bg font-tmd04-sans text-tmd04-onsurface px-5 py-9" aria-label="Material Design form controls demo">
  <form class="w-[min(720px,100%)] mx-auto grid gap-6" novalidate>
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Text fields &amp; form controls</h2>
      <p class="text-sm text-tmd04-onvariant">Floating labels on <code class="font-tmd04-mono text-[12px]">peer-[:not(:placeholder-shown)]:</code>, errors on <code class="font-tmd04-mono text-[12px]">user-invalid:</code>.</p>
    </header>

    <div class="grid gap-5 p-5.5 rounded-3xl bg-tmd04-surface shadow-tmd04-1">
      <span class="font-tmd04-mono text-[11px] uppercase tracking-[0.1em] text-tmd04-onvariant">Text fields</span>

      <div class="grid gap-1.5">
        <div class="relative rounded-t-md bg-tmd04-fieldfill after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-tmd04-primary after:scale-x-0 after:transition-transform after:duration-200 focus-within:after:scale-x-100 motion-reduce:after:transition-none">
          <input type="text" id="tmd04-name" placeholder=" " autocomplete="name" class="peer w-full min-h-14 pt-6 pb-2 px-4 bg-transparent border-0 border-b border-tmd04-outline rounded-t-md font-tmd04-sans text-[15px] text-tmd04-onsurface outline-none">
          <label for="tmd04-name" class="absolute left-4 top-4 pointer-events-none text-[15px] text-tmd04-onvariant transition-all duration-200 peer-focus:top-1.5 peer-focus:text-[11px] peer-focus:text-tmd04-primary peer-[:not(:placeholder-shown)]:top-1.5 peer-[:not(:placeholder-shown)]:text-[11px] motion-reduce:transition-none">Full name</label>
        </div>
        <p class="px-4 text-xs text-tmd04-onvariant">Filled variant &mdash; underline scales in from the centre on focus.</p>
      </div>

      <div class="group/email grid gap-1.5">
        <div class="relative">
          <input type="email" id="tmd04-email" placeholder=" " required autocomplete="email" aria-describedby="tmd04-email-help" class="peer w-full min-h-14 pt-6 pb-2 px-4 bg-transparent rounded-md border border-tmd04-outline font-tmd04-sans text-[15px] text-tmd04-onsurface outline-none transition-[border-color,box-shadow] duration-150 focus:border-tmd04-primary focus:shadow-[inset_0_0_0_1px_var(--color-tmd04-primary)] user-invalid:border-tmd04-error user-invalid:shadow-[inset_0_0_0_1px_var(--color-tmd04-error)]">
          <label for="tmd04-email" class="absolute left-4 top-4 pointer-events-none text-[15px] text-tmd04-onvariant transition-all duration-200 peer-focus:top-1.5 peer-focus:text-[11px] peer-focus:text-tmd04-primary peer-[:not(:placeholder-shown)]:top-1.5 peer-[:not(:placeholder-shown)]:text-[11px] peer-user-invalid:text-tmd04-error motion-reduce:transition-none">Email address</label>
          <span class="font-tmd04-icon absolute right-4 top-4 text-[20px] leading-none text-tmd04-error opacity-0 peer-user-invalid:opacity-100" aria-hidden="true">error</span>
        </div>
        <p id="tmd04-email-help" class="px-4 text-xs text-tmd04-onvariant group-has-[:user-invalid]/email:text-tmd04-error">Outlined variant &mdash; type something invalid, then leave the field.</p>
      </div>

      <div class="grid gap-1.5">
        <div class="relative">
          <textarea id="tmd04-notes" rows="3" placeholder=" " class="peer w-full pt-6 pb-2 px-4 bg-transparent rounded-md border border-tmd04-outline font-tmd04-sans text-[15px] leading-6 text-tmd04-onsurface outline-none resize-y transition-colors duration-150 focus:border-tmd04-primary"></textarea>
          <label for="tmd04-notes" class="absolute left-4 top-4 pointer-events-none text-[15px] text-tmd04-onvariant transition-all duration-200 peer-focus:top-1.5 peer-focus:text-[11px] peer-focus:text-tmd04-primary peer-[:not(:placeholder-shown)]:top-1.5 peer-[:not(:placeholder-shown)]:text-[11px] motion-reduce:transition-none">Notes</label>
        </div>
        <div class="flex justify-between px-4 text-xs text-tmd04-onvariant"><span>Supporting text</span><span class="font-tmd04-mono tabular-nums">0 / 240</span></div>
      </div>

      <label class="grid gap-1.5 has-[:disabled]:opacity-38">
        <span class="px-1 text-xs font-medium text-tmd04-onvariant">Region</span>
        <select class="w-full min-h-14 px-4 bg-transparent rounded-md border border-tmd04-outline font-tmd04-sans text-[15px] text-tmd04-onsurface outline-none cursor-pointer transition-colors duration-150 focus:border-tmd04-primary">
          <option>North Atlantic</option>
          <option>Baltic</option>
          <option>Mediterranean</option>
        </select>
      </label>
    </div>

    <div class="grid gap-5 p-5.5 rounded-3xl bg-tmd04-surface shadow-tmd04-1">
      <span class="font-tmd04-mono text-[11px] uppercase tracking-[0.1em] text-tmd04-onvariant">Selection controls</span>
      <div class="grid gap-3 grid-cols-[repeat(auto-fit,minmax(min(220px,100%),1fr))]">
        <div class="grid gap-2">
          <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer"><input type="checkbox" checked class="w-5 h-5 accent-tmd04-primary cursor-pointer">Sync offline copies</label>
          <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer"><input type="checkbox" class="w-5 h-5 accent-tmd04-primary cursor-pointer">Include archived</label>
          <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer has-[:disabled]:opacity-38"><input type="checkbox" disabled class="w-5 h-5 accent-tmd04-primary">Unavailable option</label>
        </div>
        <fieldset class="grid gap-2 border-0 p-0 m-0">
          <legend class="text-xs font-medium text-tmd04-onvariant mb-1">Cadence</legend>
          <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer"><input type="radio" name="tmd04-cadence" checked class="w-5 h-5 accent-tmd04-primary cursor-pointer">Hourly</label>
          <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer"><input type="radio" name="tmd04-cadence" class="w-5 h-5 accent-tmd04-primary cursor-pointer">Daily</label>
          <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer"><input type="radio" name="tmd04-cadence" class="w-5 h-5 accent-tmd04-primary cursor-pointer">Weekly</label>
        </fieldset>
        <div class="grid gap-3 content-start">
          <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer">
            <input type="checkbox" role="switch" checked class="peer sr-only">
            <span class="relative w-13 h-8 rounded-full bg-tmd04-outlinevariant border-2 border-tmd04-outline transition-colors duration-200 peer-checked:bg-tmd04-primary peer-checked:border-tmd04-primary peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmd04-primary after:absolute after:top-1/2 after:left-1 after:[transform:translate(0,-50%)] after:w-4 after:h-4 after:rounded-full after:bg-tmd04-outline after:transition-[transform,background,width,height] after:duration-200 peer-checked:after:[transform:translate(20px,-50%)] peer-checked:after:w-6 peer-checked:after:h-6 peer-checked:after:bg-tmd04-onprimary motion-reduce:transition-none motion-reduce:after:transition-none" aria-hidden="true"></span>
            Push notifications
          </label>
          <div class="grid gap-1">
            <label for="tmd04-range" class="text-xs font-medium text-tmd04-onvariant">Sampling depth</label>
            <input type="range" id="tmd04-range" min="0" max="100" value="62" class="w-full h-11 accent-tmd04-primary cursor-pointer">
          </div>
        </div>
      </div>
      <div class="flex flex-wrap gap-2 pt-1">
        <button type="submit" class="relative overflow-hidden inline-flex items-center gap-2 min-h-10 px-6 rounded-full border-0 bg-tmd04-primary text-tmd04-onprimary cursor-pointer text-sm font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd04-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08] active:before:opacity-[0.12]">Save changes</button>
        <button type="reset" class="relative overflow-hidden min-h-10 px-4 rounded-full border-0 bg-transparent cursor-pointer text-sm font-medium text-tmd04-primary focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd04-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Reset</button>
      </div>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd04-bg: #f1f8f7;
  --color-tmd04-bg: oklch(0.974 0.008 186.9);
  --color-tmd04-surface: #ffffff;
  --color-tmd04-surface: oklch(1 0 89.9);
  --color-tmd04-fieldfill: #eaf3f1;
  --color-tmd04-fieldfill: oklch(0.957 0.01 181.4);
  --color-tmd04-primary: #00695c;
  --color-tmd04-primary: oklch(0.467 0.084 180.4);
  --color-tmd04-onprimary: #ffffff;
  --color-tmd04-onprimary: oklch(1 0 89.9);
  --color-tmd04-onsurface: #1c1b1f;
  --color-tmd04-onsurface: oklch(0.225 0.008 297.2);
  --color-tmd04-onvariant: #4a5b58;
  --color-tmd04-onvariant: oklch(0.456 0.022 183.5);
  --color-tmd04-outline: #79817f;
  --color-tmd04-outline: oklch(0.596 0.01 179.4);
  --color-tmd04-outlinevariant: #c9d6d3;
  --color-tmd04-outlinevariant: oklch(0.865 0.015 180.6);
  --color-tmd04-error: #b3261e;
  --color-tmd04-error: oklch(0.501 0.178 28.7);
  --font-tmd04-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd04-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd04-icon: 'Material Symbols Outlined';
  --shadow-tmd04-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
}

.tmd-04 {
  width: 100%;
  min-height: 100svh;
}

.tmd-04 .font-tmd04-icon {
  font-feature-settings: 'liga';
}
```

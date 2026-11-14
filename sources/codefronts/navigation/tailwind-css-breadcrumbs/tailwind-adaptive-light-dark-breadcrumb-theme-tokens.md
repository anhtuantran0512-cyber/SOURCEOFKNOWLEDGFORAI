---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-adaptive-light-dark-breadcrumb-theme-tokens/"
title: "Tailwind Adaptive Light & Dark Mode Breadcrumb Bar with Theme Tokens"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "A trail whose entire skin flips light to dark from one block of custom properties, with no JavaScript and no class-toggling framework: a hidden checkbox…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Adaptive Light & Dark Mode Breadcrumb Bar with Theme Tokens
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-adaptive-light-dark-breadcrumb-theme-tokens/

A trail whose entire skin flips light to dark from one block of custom properties, with no JavaScript and no class-toggling framework: a hidden checkbox flips the tokens through has-checked:, so every crumb, separator and hover tint recolours from the same five variables. The SaaS-dashboard treatment, frosted glass included.
## HTML
```html
<section class="tbc-03 w-full min-h-svh grid place-items-center px-5 py-9 font-tbc03-sans [--tbc03-bg:oklch(1_0_0/.7)] [--tbc03-text:oklch(0.5_0.02_265)] [--tbc03-strong:oklch(0.25_0.02_265)] [--tbc03-sep:oklch(0.75_0.02_265)] [--tbc03-hover:oklch(0.95_0.01_265)] [--tbc03-line:oklch(0.85_0.01_265/.7)] [--tbc03-stage:oklch(0.97_0.005_265)] bg-[var(--tbc03-stage)] [color-scheme:light] transition-colors duration-300 has-checked:[--tbc03-bg:oklch(0.2_0.02_265/.7)] has-checked:[--tbc03-text:oklch(0.72_0.02_265)] has-checked:[--tbc03-strong:oklch(0.96_0.01_265)] has-checked:[--tbc03-sep:oklch(0.5_0.02_265)] has-checked:[--tbc03-hover:oklch(0.28_0.02_265)] has-checked:[--tbc03-line:oklch(0.4_0.02_265/.5)] has-checked:[--tbc03-stage:oklch(0.14_0.02_265)] has-checked:[color-scheme:dark] motion-reduce:transition-none">
  <div class="flex flex-wrap items-center justify-center gap-4">
    <nav aria-label="Breadcrumb">
      <ol class="flex flex-wrap items-center list-none m-0 px-3.5 py-2 rounded-xl bg-[var(--tbc03-bg)] border border-[var(--tbc03-line)] backdrop-blur-md transition-colors duration-300 motion-reduce:transition-none">
        <li class="flex items-center"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-lg text-[13.5px] font-medium text-[var(--tbc03-text)] no-underline transition-colors duration-200 hover:text-[var(--tbc03-strong)] hover:bg-[var(--tbc03-hover)] focus-visible:outline-2 focus-visible:outline-tbc03-acc focus-visible:outline-offset-2">Dashboard</a></li>
        <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-[var(--tbc03-sep)]"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-lg text-[13.5px] font-medium text-[var(--tbc03-text)] no-underline transition-colors duration-200 hover:text-[var(--tbc03-strong)] hover:bg-[var(--tbc03-hover)] focus-visible:outline-2 focus-visible:outline-tbc03-acc focus-visible:outline-offset-2">Projects</a></li>
        <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-[var(--tbc03-sep)]"><a href="#" class="flex items-center min-h-9 px-2.5 rounded-lg text-[13.5px] font-medium text-[var(--tbc03-text)] no-underline transition-colors duration-200 hover:text-[var(--tbc03-strong)] hover:bg-[var(--tbc03-hover)] focus-visible:outline-2 focus-visible:outline-tbc03-acc focus-visible:outline-offset-2">Aurora</a></li>
        <li class="flex items-center before:content-['\203A'] before:mx-2 before:text-[var(--tbc03-sep)]"><a href="#" aria-current="page" class="flex items-center min-h-9 px-2.5 rounded-lg text-[13.5px] font-semibold text-[var(--tbc03-strong)] no-underline bg-[color-mix(in_oklab,var(--color-tbc03-acc)_18%,transparent)] focus-visible:outline-2 focus-visible:outline-tbc03-acc focus-visible:outline-offset-2">Settings</a></li>
      </ol>
    </nav>
    <div>
      <input type="checkbox" id="tbc03-theme" class="peer sr-only">
      <label for="tbc03-theme" class="inline-flex items-center gap-2 min-h-11 px-4 rounded-full select-none cursor-pointer bg-[var(--tbc03-bg)] border border-[var(--tbc03-line)] backdrop-blur-md text-[12.5px] font-semibold text-[var(--tbc03-strong)] transition-colors duration-200 hover:bg-[var(--tbc03-hover)] peer-focus-visible:outline-2 peer-focus-visible:outline-tbc03-acc peer-focus-visible:outline-offset-2 motion-reduce:transition-none">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" class="w-3.5 h-3.5 peer-checked:hidden"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" class="w-3.5 h-3.5 hidden peer-checked:block"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
        Theme
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc03-acc: #6f7ede;
  --color-tbc03-acc: oklch(0.62 0.16 265);
  --font-tbc03-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-03 {
  width: 100%;
  min-height: 100svh;
}
/* Icon swap needs the checkbox as a preceding sibling of the label, and the SVGs are
   inside the label: peer-checked: cannot reach INTO a peer, so the two icon rules are
   the one part of this demo utilities cannot express. */

.tbc-03 input:checked ~ label svg:first-of-type {
  display: none;
}

.tbc-03 input:checked ~ label svg:last-of-type {
  display: block;
}
```

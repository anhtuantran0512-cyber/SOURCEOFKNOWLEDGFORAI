---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-expansion-panels-accordion/"
title: "Tailwind Material Design Expansion Panels and Accordion"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "Expansion panels on <details>, with the one thing the checkbox-hack version could never have: name=\"…\" makes the accordion exclusive natively, so opening one…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Expansion Panels and Accordion
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-expansion-panels-accordion/

Expansion panels on <details>, with the one thing the checkbox-hack version could never have: name="…" makes the accordion exclusive natively, so opening one panel closes the others with no script and no radio hack. Tailwind styles the whole thing through open: and a direct-child arbitrary variant.
## HTML
```html
<section class="tmd-11 w-full min-h-svh bg-tmd11-bg font-tmd11-sans text-tmd11-onsurface px-5 py-9" aria-label="Material Design expansion panels demo">
  <div class="w-[min(760px,100%)] mx-auto grid gap-6">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Expansion panels</h2>
      <p class="text-sm text-tmd11-onvariant">Native <code class="font-tmd11-mono text-[12px]">&lt;details name&gt;</code> exclusivity &mdash; open one and the browser closes the rest.</p>
    </header>

    <div class="grid gap-2">
      <details name="tmd11-acc" open class="group/p rounded-xl bg-tmd11-surface border border-tmd11-outlinevariant overflow-hidden transition-shadow duration-200 open:shadow-tmd11-1 motion-reduce:transition-none">
        <summary class="flex items-center gap-3 min-h-14 px-4 cursor-pointer list-none select-none text-[15px] font-medium [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd11-primary">
          <span class="font-tmd11-icon text-[20px] leading-none text-tmd11-primary" aria-hidden="true">tune</span>
          <span class="flex-1">Sensor configuration</span>
          <span class="font-tmd11-mono text-[11px] text-tmd11-onvariant">4 sensors</span>
          <span class="font-tmd11-icon text-[22px] leading-none text-tmd11-onvariant transition-transform duration-250 group-open/p:rotate-180 motion-reduce:transition-none" aria-hidden="true">expand_more</span>
        </summary>
        <div class="grid [grid-template-rows:0fr] transition-[grid-template-rows] duration-300 ease-out group-open/p:[grid-template-rows:1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden">
            <div class="grid gap-3 px-4 pt-1 pb-4 border-t border-tmd11-outlinevariant">
              <p class="text-sm leading-6 text-tmd11-onvariant text-pretty">The body animates from a <span class="font-tmd11-mono text-[12px]">0fr</span> grid track to <span class="font-tmd11-mono text-[12px]">1fr</span>. Padding lives on this inner element, never on the animating one &mdash; padding does not compress.</p>
              <div class="flex flex-wrap gap-2">
                <span class="inline-flex items-center h-8 px-3 rounded-lg bg-tmd11-primarycontainer text-tmd11-onprimarycontainer text-xs font-medium">CTD</span>
                <span class="inline-flex items-center h-8 px-3 rounded-lg bg-tmd11-primarycontainer text-tmd11-onprimarycontainer text-xs font-medium">Fluorometer</span>
                <span class="inline-flex items-center h-8 px-3 rounded-lg bg-tmd11-primarycontainer text-tmd11-onprimarycontainer text-xs font-medium">Oxygen optode</span>
                <span class="inline-flex items-center h-8 px-3 rounded-lg bg-tmd11-primarycontainer text-tmd11-onprimarycontainer text-xs font-medium">Turbidity</span>
              </div>
            </div>
          </div>
        </div>
      </details>

      <details name="tmd11-acc" class="group/p rounded-xl bg-tmd11-surface border border-tmd11-outlinevariant overflow-hidden transition-shadow duration-200 open:shadow-tmd11-1 motion-reduce:transition-none">
        <summary class="flex items-center gap-3 min-h-14 px-4 cursor-pointer list-none select-none text-[15px] font-medium [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd11-primary">
          <span class="font-tmd11-icon text-[20px] leading-none text-tmd11-primary" aria-hidden="true">schedule</span>
          <span class="flex-1">Sampling schedule</span>
          <span class="font-tmd11-mono text-[11px] text-tmd11-onvariant">hourly</span>
          <span class="font-tmd11-icon text-[22px] leading-none text-tmd11-onvariant transition-transform duration-250 group-open/p:rotate-180 motion-reduce:transition-none" aria-hidden="true">expand_more</span>
        </summary>
        <div class="grid [grid-template-rows:0fr] transition-[grid-template-rows] duration-300 ease-out group-open/p:[grid-template-rows:1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden">
            <div class="grid gap-3 px-4 pt-1 pb-4 border-t border-tmd11-outlinevariant">
              <p class="text-sm leading-6 text-tmd11-onvariant text-pretty">Opening this panel closed the one above &mdash; the browser did that, because both share <span class="font-tmd11-mono text-[12px]">name=&quot;tmd11-acc&quot;</span>.</p>
              <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer"><input type="checkbox" checked class="w-5 h-5 accent-tmd11-primary">Pause during transit</label>
            </div>
          </div>
        </div>
      </details>

      <details name="tmd11-acc" class="group/p rounded-xl bg-tmd11-surface border border-tmd11-outlinevariant overflow-hidden transition-shadow duration-200 open:shadow-tmd11-1 motion-reduce:transition-none">
        <summary class="flex items-center gap-3 min-h-14 px-4 cursor-pointer list-none select-none text-[15px] font-medium [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd11-primary">
          <span class="font-tmd11-icon text-[20px] leading-none text-tmd11-primary" aria-hidden="true">layers</span>
          <span class="flex-1">Nested panels</span>
          <span class="font-tmd11-icon text-[22px] leading-none text-tmd11-onvariant transition-transform duration-250 group-open/p:rotate-180 motion-reduce:transition-none" aria-hidden="true">expand_more</span>
        </summary>
        <div class="grid [grid-template-rows:0fr] transition-[grid-template-rows] duration-300 ease-out group-open/p:[grid-template-rows:1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden">
            <div class="grid gap-2 px-4 pt-3 pb-4 border-t border-tmd11-outlinevariant">
              <p class="text-sm leading-6 text-tmd11-onvariant text-pretty">This is why the group is <em>named</em>: an unnamed <span class="font-tmd11-mono text-[12px]">group-open:</span> would match through this open parent and flip the child's chevron too.</p>
              <details class="group/c rounded-lg bg-tmd11-surface2 overflow-hidden">
                <summary class="flex items-center gap-2 min-h-12 px-3 cursor-pointer list-none text-sm font-medium [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd11-primary"><span class="flex-1">Child panel &mdash; its own state</span><span class="font-tmd11-icon text-[20px] leading-none transition-transform duration-250 group-open/c:rotate-180" aria-hidden="true">expand_more</span></summary>
                <div class="grid [grid-template-rows:0fr] transition-[grid-template-rows] duration-250 group-open/c:[grid-template-rows:1fr]"><div class="min-h-0 overflow-hidden"><p class="px-3 pb-3 text-sm leading-6 text-tmd11-onvariant">Correct: the parent's chevron stays pointing down while this one turns.</p></div></div>
              </details>
            </div>
          </div>
        </div>
      </details>
    </div>

    <p class="text-sm leading-6 text-tmd11-onvariant text-pretty"><code class="font-tmd11-mono text-[12px]">&lt;details&gt;</code> also gives find-in-page reveal, a <code class="font-tmd11-mono text-[12px]">toggle</code> event and correct expanded-state announcement &mdash; none of which the checkbox-hack accordion had.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd11-bg: #f4f1f9;
  --color-tmd11-bg: oklch(0.963 0.011 303.1);
  --color-tmd11-surface: #fffbfe;
  --color-tmd11-surface: oklch(0.992 0.006 334);
  --color-tmd11-surface2: #f1eef8;
  --color-tmd11-surface2: oklch(0.954 0.014 299.8);
  --color-tmd11-primary: #5c6bc0;
  --color-tmd11-primary: oklch(0.556 0.132 273.8);
  --color-tmd11-primarycontainer: #e3e5f7;
  --color-tmd11-primarycontainer: oklch(0.926 0.024 280.8);
  --color-tmd11-onprimarycontainer: #131a45;
  --color-tmd11-onprimarycontainer: oklch(0.241 0.081 271.9);
  --color-tmd11-onsurface: #1c1b1f;
  --color-tmd11-onsurface: oklch(0.225 0.008 297.2);
  --color-tmd11-onvariant: #4c4a55;
  --color-tmd11-onvariant: oklch(0.415 0.018 293.9);
  --color-tmd11-outlinevariant: #d6d2e0;
  --color-tmd11-outlinevariant: oklch(0.871 0.02 299);
  --font-tmd11-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd11-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd11-icon: 'Material Symbols Outlined';
  --shadow-tmd11-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 2px 6px 2px rgb(0 0 0 / 0.15);
}
/* The progressive upgrade: where supported, heights can interpolate to keyword values,
   which makes the 0fr/1fr grid dance unnecessary. Declared root-scoped, harmless
   everywhere else. There is no utility for it. */

.tmd-11 {
  width: 100%;
  min-height: 100svh;
  interpolate-size: allow-keywords;
}

.tmd-11 .font-tmd11-icon {
  font-feature-settings: 'liga';
}
```

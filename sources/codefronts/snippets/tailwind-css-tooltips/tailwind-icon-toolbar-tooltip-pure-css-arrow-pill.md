---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-icon-toolbar-tooltip-pure-css-arrow-pill/"
title: "Tailwind Icon Toolbar Tooltip with Pure-CSS Arrow Pill"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "The workhorse: unlabeled toolbar icons that name themselves on hover in a small dark pill with a CSS-triangle tail."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Icon Toolbar Tooltip with Pure-CSS Arrow Pill
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-icon-toolbar-tooltip-pure-css-arrow-pill/

The workhorse: unlabeled toolbar icons that name themselves on hover in a small dark pill with a CSS-triangle tail. This is the whole collection in miniature &mdash; one group, one after: arrow built from border widths, one 140ms transition, and nothing else.
## HTML
```html
<section class="ttp-20 w-full min-h-svh bg-ttp20-bg px-7 pt-20 pb-15 font-ttp20-sans">
  <div class="flex justify-center">
    <div class="inline-flex flex-wrap items-center gap-0.5 rounded-lg border border-ttp20-edge bg-ttp20-bar p-1.25" role="toolbar" aria-label="Text formatting">

      <span class="group relative inline-block">
        <button type="button" aria-label="Bold" aria-pressed="true" aria-describedby="ttp20-l1" class="ttp20-btn aria-pressed:bg-ttp20-hover aria-pressed:text-white">B</button>
        <span id="ttp20-l1" role="tooltip" class="ttp20-tip">Bold</span>
      </span>
      <span class="group relative inline-block">
        <button type="button" aria-label="Italic" aria-describedby="ttp20-l2" class="ttp20-btn italic">I</button>
        <span id="ttp20-l2" role="tooltip" class="ttp20-tip">Italic</span>
      </span>
      <span class="group relative inline-block">
        <button type="button" aria-label="Underline" aria-describedby="ttp20-l3" class="ttp20-btn underline">U</button>
        <span id="ttp20-l3" role="tooltip" class="ttp20-tip">Underline</span>
      </span>
      <span class="group relative inline-block">
        <button type="button" aria-label="Strikethrough" aria-describedby="ttp20-l4" class="ttp20-btn line-through">S</button>
        <span id="ttp20-l4" role="tooltip" class="ttp20-tip">Strikethrough</span>
      </span>

      <span class="mx-1 inline-block h-5 w-px shrink-0 bg-ttp20-edge" aria-hidden="true"></span>

      <span class="group relative inline-block">
        <button type="button" aria-label="Insert link" aria-describedby="ttp20-l5" class="ttp20-btn"><svg viewBox="0 0 16 16" class="h-[15px] w-[15px] fill-current" aria-hidden="true"><path d="M6.354 5.5H4a3 3 0 0 0 0 6h3a3 3 0 0 0 2.83-4H9v.5A2 2 0 0 1 7 9.5H4a2 2 0 0 1 0-4h1.535c.218-.376.495-.717.82-1z"/><path d="M9 5.5a3 3 0 0 0-2.83 4h1.098A2 2 0 0 1 9 6.5h3a2 2 0 1 1 0 4h-1.535a4 4 0 0 1-.82 1H12a3 3 0 1 0 0-6H9z"/></svg></button>
        <span id="ttp20-l5" role="tooltip" class="ttp20-tip">Insert link</span>
      </span>
      <span class="group relative inline-block">
        <button type="button" aria-label="Insert image" aria-describedby="ttp20-l6" class="ttp20-btn"><svg viewBox="0 0 16 16" class="h-[15px] w-[15px] fill-current" aria-hidden="true"><path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/><path d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2h-12zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1h12z"/></svg></button>
        <span id="ttp20-l6" role="tooltip" class="ttp20-tip">Insert image</span>
      </span>
      <span class="group relative inline-block">
        <button type="button" aria-label="Code block" aria-describedby="ttp20-l7" class="ttp20-btn font-mono text-[11px] font-bold">&lt;/&gt;</button>
        <span id="ttp20-l7" role="tooltip" class="ttp20-tip">Code block</span>
      </span>

      <span class="mx-1 inline-block h-5 w-px shrink-0 bg-ttp20-edge" aria-hidden="true"></span>

      <span class="group relative inline-block">
        <button type="button" aria-label="Bullet list" aria-describedby="ttp20-l8" class="ttp20-btn"><svg viewBox="0 0 16 16" class="h-[15px] w-[15px] fill-current" aria-hidden="true"><path fill-rule="evenodd" d="M5 11.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zm-3 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm0 4a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm0 4a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/></svg></button>
        <span id="ttp20-l8" role="tooltip" class="ttp20-tip">Bullet list</span>
      </span>
      <span class="group relative inline-block">
        <button type="button" aria-label="Checklist" aria-describedby="ttp20-l9" class="ttp20-btn"><svg viewBox="0 0 16 16" class="h-[15px] w-[15px] fill-current" aria-hidden="true"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M10.97 4.97a.75.75 0 0 1 1.071 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.235.235 0 0 1 .02-.022z"/></svg></button>
        <span id="ttp20-l9" role="tooltip" class="ttp20-tip">Checklist</span>
      </span>

      <span class="mx-1 inline-block h-5 w-px shrink-0 bg-ttp20-edge" aria-hidden="true"></span>

      <span class="group relative inline-block">
        <button type="button" aria-label="Preferences" aria-describedby="ttp20-l10" class="ttp20-btn"><svg viewBox="0 0 16 16" class="h-[15px] w-[15px] fill-current" aria-hidden="true"><path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/></svg></button>
        <span id="ttp20-l10" role="tooltip" class="ttp20-tip">Preferences</span>
      </span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp20-bg: #141414;
  --color-ttp20-bg: oklch(0.19 0 0);
  --color-ttp20-bar: #1f1f1f;
  --color-ttp20-bar: oklch(0.23 0 0);
  --color-ttp20-edge: #333333;
  --color-ttp20-edge: oklch(0.33 0 0);
  --color-ttp20-hover: #2e2e2e;
  --color-ttp20-hover: oklch(0.3 0 0);
  --color-ttp20-icon: #9b9b9b;
  --color-ttp20-icon: oklch(0.68 0 0);
  --color-ttp20-pill: #18181b;
  --color-ttp20-pill: oklch(0.21 0.005 285);
  --font-ttp20-sans: system-ui, -apple-system, sans-serif;
}

.ttp-20 {
  width: 100%;
  min-height: 100svh;
}
/* Ten buttons, ten pills, one recipe each. */

.ttp-20 .ttp20-btn {
  @apply inline-flex h-8 w-8 cursor-help items-center justify-center rounded-[5px] border-0 bg-transparent p-0 text-[13px] font-semibold text-ttp20-icon transition-colors duration-100 hover:bg-ttp20-hover hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white/70;
}

.ttp-20 .ttp20-tip {
  @apply pointer-events-none invisible absolute bottom-[calc(100%+8px)] left-1/2 z-100 block translate-y-1 -translate-x-1/2 whitespace-nowrap rounded-[5px] bg-ttp20-pill px-2.5 py-1.25 text-[11.5px] leading-none text-white opacity-0 transition-[opacity,translate,visibility] duration-150 ease-[cubic-bezier(0.22,1,0.36,1)] after:absolute after:top-full after:left-1/2 after:-translate-x-1/2 after:border-4 after:border-transparent after:border-t-ttp20-pill after:content-[''] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100;
}
```

---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-isometric-3d-layered-breadcrumb-extruded-tiles/"
title: "Tailwind Isometric 3D Layered Breadcrumb with Extruded Tiles"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "The trail tilted onto an isometric plane: perspective on the stage, a rotateX/rotateZ plane, and crumbs extruded by a stack of six hairline shadows so each…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Isometric 3D Layered Breadcrumb with Extruded Tiles
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-isometric-3d-layered-breadcrumb-extruded-tiles/

The trail tilted onto an isometric plane: perspective on the stage, a rotateX/rotateZ plane, and crumbs extruded by a stack of six hairline shadows so each reads as a physical tile. Hover lifts a tile toward the viewer on the Z axis; motion-reduce: flattens the whole scene to 2D.
## HTML
```html
<section class="tbc-09 w-full min-h-svh grid place-items-center bg-tbc09-bg font-tbc09-sans px-10 pt-14 pb-18 perspective-[900px]">
  <nav aria-label="Breadcrumb" class="transform-3d rotate-x-[52deg] rotate-z-[-42deg] motion-reduce:rotate-x-0 motion-reduce:rotate-z-0">
    <ol class="flex gap-4 list-none m-0 p-0 transform-3d">
      <li><a href="#" class="flex items-center justify-center min-w-[74px] h-11 px-3.5 rounded-lg text-[13px] font-bold text-white no-underline bg-tbc09-tile shadow-[0_1px_var(--color-tbc09-side),0_2px_var(--color-tbc09-side),0_3px_var(--color-tbc09-side),0_4px_var(--color-tbc09-side),0_5px_var(--color-tbc09-side),0_6px_var(--color-tbc09-side2),0_8px_12px_oklch(0_0_0/0.3)] transition-[translate,box-shadow] duration-200 hover:translate-z-4 hover:shadow-[0_2px_var(--color-tbc09-side),0_4px_var(--color-tbc09-side),0_6px_var(--color-tbc09-side),0_8px_var(--color-tbc09-side),0_10px_var(--color-tbc09-side),0_12px_var(--color-tbc09-side2),0_20px_22px_oklch(0_0_0/0.32)] focus-visible:outline-none focus-visible:translate-z-4 focus-visible:shadow-[0_2px_var(--color-tbc09-side),0_4px_var(--color-tbc09-side),0_6px_var(--color-tbc09-side),0_8px_var(--color-tbc09-side),0_10px_var(--color-tbc09-side),0_12px_var(--color-tbc09-side2),0_0_0_3px_white,0_20px_22px_oklch(0_0_0/0.32)] motion-reduce:transition-none motion-reduce:hover:translate-z-0 motion-reduce:shadow-[0_2px_6px_oklch(0_0_0/0.2)]">Home</a></li>
      <li><a href="#" class="flex items-center justify-center min-w-[74px] h-11 px-3.5 rounded-lg text-[13px] font-bold text-white no-underline bg-tbc09-tile shadow-[0_1px_var(--color-tbc09-side),0_2px_var(--color-tbc09-side),0_3px_var(--color-tbc09-side),0_4px_var(--color-tbc09-side),0_5px_var(--color-tbc09-side),0_6px_var(--color-tbc09-side2),0_8px_12px_oklch(0_0_0/0.3)] transition-[translate,box-shadow] duration-200 hover:translate-z-4 hover:shadow-[0_2px_var(--color-tbc09-side),0_4px_var(--color-tbc09-side),0_6px_var(--color-tbc09-side),0_8px_var(--color-tbc09-side),0_10px_var(--color-tbc09-side),0_12px_var(--color-tbc09-side2),0_20px_22px_oklch(0_0_0/0.32)] focus-visible:outline-none focus-visible:translate-z-4 focus-visible:shadow-[0_2px_var(--color-tbc09-side),0_4px_var(--color-tbc09-side),0_6px_var(--color-tbc09-side),0_8px_var(--color-tbc09-side),0_10px_var(--color-tbc09-side),0_12px_var(--color-tbc09-side2),0_0_0_3px_white,0_20px_22px_oklch(0_0_0/0.32)] motion-reduce:transition-none motion-reduce:hover:translate-z-0 motion-reduce:shadow-[0_2px_6px_oklch(0_0_0/0.2)]">World</a></li>
      <li><a href="#" class="flex items-center justify-center min-w-[74px] h-11 px-3.5 rounded-lg text-[13px] font-bold text-white no-underline bg-tbc09-tile shadow-[0_1px_var(--color-tbc09-side),0_2px_var(--color-tbc09-side),0_3px_var(--color-tbc09-side),0_4px_var(--color-tbc09-side),0_5px_var(--color-tbc09-side),0_6px_var(--color-tbc09-side2),0_8px_12px_oklch(0_0_0/0.3)] transition-[translate,box-shadow] duration-200 hover:translate-z-4 hover:shadow-[0_2px_var(--color-tbc09-side),0_4px_var(--color-tbc09-side),0_6px_var(--color-tbc09-side),0_8px_var(--color-tbc09-side),0_10px_var(--color-tbc09-side),0_12px_var(--color-tbc09-side2),0_20px_22px_oklch(0_0_0/0.32)] focus-visible:outline-none focus-visible:translate-z-4 focus-visible:shadow-[0_2px_var(--color-tbc09-side),0_4px_var(--color-tbc09-side),0_6px_var(--color-tbc09-side),0_8px_var(--color-tbc09-side),0_10px_var(--color-tbc09-side),0_12px_var(--color-tbc09-side2),0_0_0_3px_white,0_20px_22px_oklch(0_0_0/0.32)] motion-reduce:transition-none motion-reduce:hover:translate-z-0 motion-reduce:shadow-[0_2px_6px_oklch(0_0_0/0.2)]">Levels</a></li>
      <li><a href="#" aria-current="page" class="flex items-center justify-center min-w-[74px] h-11 px-3.5 rounded-lg text-[13px] font-bold text-white no-underline translate-z-2 bg-tbc09-current shadow-[0_1px_var(--color-tbc09-currentside),0_2px_var(--color-tbc09-currentside),0_3px_var(--color-tbc09-currentside),0_4px_var(--color-tbc09-currentside),0_5px_var(--color-tbc09-currentside),0_6px_var(--color-tbc09-currentside2),0_8px_12px_oklch(0_0_0/0.3)] focus-visible:outline-none focus-visible:shadow-[0_1px_var(--color-tbc09-currentside),0_3px_var(--color-tbc09-currentside),0_5px_var(--color-tbc09-currentside),0_6px_var(--color-tbc09-currentside2),0_0_0_3px_white,0_12px_16px_oklch(0_0_0/0.3)] motion-reduce:translate-z-0 motion-reduce:shadow-[0_2px_6px_oklch(0_0_0/0.2)]">Stage 4</a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc09-bg: #dfe0f0;
  --color-tbc09-bg: oklch(0.94 0.02 265);
  --color-tbc09-tile: #7b87d8;
  --color-tbc09-tile: oklch(0.62 0.13 265);
  --color-tbc09-side: #4a56a8;
  --color-tbc09-side: oklch(0.42 0.1 265);
  --color-tbc09-side2: #454f9e;
  --color-tbc09-side2: oklch(0.4 0.09 265);
  --color-tbc09-current: #e8794f;
  --color-tbc09-current: oklch(0.68 0.19 30);
  --color-tbc09-currentside: #a84f2c;
  --color-tbc09-currentside: oklch(0.5 0.14 30);
  --color-tbc09-currentside2: #9e4a29;
  --color-tbc09-currentside2: oklch(0.48 0.13 30);
  --font-tbc09-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-09 {
  width: 100%;
  min-height: 100svh;
}
```

---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-3d-cube-image-viewer-radio-rotation/"
title: "Tailwind 3D Cube Image Viewer with Radio-Driven Rotation"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "Six photographs mapped onto the faces of a real 3D cube that rotates to whichever face you pick."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Cube Image Viewer with Radio-Driven Rotation
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-3d-cube-image-viewer-radio-rotation/

Six photographs mapped onto the faces of a real 3D cube that rotates to whichever face you pick. The controls are actual radio buttons, so the viewer is keyboard- and screen-reader-operable — and in Tailwind the checked state reaches the cube through a named group-has-[...] variant rather than six stylesheet rules.
## HTML
```html
<section class="tgl-17 group/cube w-full min-h-svh flex flex-col items-center justify-center gap-10 px-5 py-10 font-tgl17-sans [--size:240px] [--half:120px] bg-[radial-gradient(120%_120%_at_50%_20%,oklch(0.2_0.02_215),oklch(0.09_0.01_215))]" aria-label="3D cube image viewer">
  <fieldset class="border-0 m-0 p-0 flex flex-wrap justify-center gap-2">
    <legend class="w-full text-center mb-3 font-tgl17-mono text-[11px] tracking-[0.2em] uppercase text-tgl17-mut">Choose a face</legend>
    <label class="cursor-pointer"><input type="radio" name="tgl-17" value="front" checked class="peer sr-only"><span class="block px-4 py-2 min-h-11 content-center rounded-[10px] border border-tgl17-edge bg-tgl17-chip text-tgl17-mut text-[13px] font-semibold transition-colors duration-200 hover:border-tgl17-acc hover:text-white peer-checked:bg-tgl17-acc peer-checked:text-tgl17-ink peer-checked:border-tgl17-acc peer-focus-visible:outline-3 peer-focus-visible:outline-tgl17-acc peer-focus-visible:outline-offset-2">Front</span></label>
    <label class="cursor-pointer"><input type="radio" name="tgl-17" value="right" class="peer sr-only"><span class="block px-4 py-2 min-h-11 content-center rounded-[10px] border border-tgl17-edge bg-tgl17-chip text-tgl17-mut text-[13px] font-semibold transition-colors duration-200 hover:border-tgl17-acc hover:text-white peer-checked:bg-tgl17-acc peer-checked:text-tgl17-ink peer-checked:border-tgl17-acc peer-focus-visible:outline-3 peer-focus-visible:outline-tgl17-acc peer-focus-visible:outline-offset-2">Right</span></label>
    <label class="cursor-pointer"><input type="radio" name="tgl-17" value="back" class="peer sr-only"><span class="block px-4 py-2 min-h-11 content-center rounded-[10px] border border-tgl17-edge bg-tgl17-chip text-tgl17-mut text-[13px] font-semibold transition-colors duration-200 hover:border-tgl17-acc hover:text-white peer-checked:bg-tgl17-acc peer-checked:text-tgl17-ink peer-checked:border-tgl17-acc peer-focus-visible:outline-3 peer-focus-visible:outline-tgl17-acc peer-focus-visible:outline-offset-2">Back</span></label>
    <label class="cursor-pointer"><input type="radio" name="tgl-17" value="left" class="peer sr-only"><span class="block px-4 py-2 min-h-11 content-center rounded-[10px] border border-tgl17-edge bg-tgl17-chip text-tgl17-mut text-[13px] font-semibold transition-colors duration-200 hover:border-tgl17-acc hover:text-white peer-checked:bg-tgl17-acc peer-checked:text-tgl17-ink peer-checked:border-tgl17-acc peer-focus-visible:outline-3 peer-focus-visible:outline-tgl17-acc peer-focus-visible:outline-offset-2">Left</span></label>
    <label class="cursor-pointer"><input type="radio" name="tgl-17" value="top" class="peer sr-only"><span class="block px-4 py-2 min-h-11 content-center rounded-[10px] border border-tgl17-edge bg-tgl17-chip text-tgl17-mut text-[13px] font-semibold transition-colors duration-200 hover:border-tgl17-acc hover:text-white peer-checked:bg-tgl17-acc peer-checked:text-tgl17-ink peer-checked:border-tgl17-acc peer-focus-visible:outline-3 peer-focus-visible:outline-tgl17-acc peer-focus-visible:outline-offset-2">Top</span></label>
    <label class="cursor-pointer"><input type="radio" name="tgl-17" value="bottom" class="peer sr-only"><span class="block px-4 py-2 min-h-11 content-center rounded-[10px] border border-tgl17-edge bg-tgl17-chip text-tgl17-mut text-[13px] font-semibold transition-colors duration-200 hover:border-tgl17-acc hover:text-white peer-checked:bg-tgl17-acc peer-checked:text-tgl17-ink peer-checked:border-tgl17-acc peer-focus-visible:outline-3 peer-focus-visible:outline-tgl17-acc peer-focus-visible:outline-offset-2">Bottom</span></label>
  </fieldset>
  <div class="[perspective:900px] w-[var(--size)] h-[var(--size)]">
    <div class="relative w-full h-full transform-3d [transform:rotateX(-18deg)_rotateY(-24deg)] transition-transform duration-[800ms] ease-[cubic-bezier(0.4,0.1,0.2,1)] group-has-[input[value=front]:checked]/cube:[transform:rotateY(0deg)] group-has-[input[value=right]:checked]/cube:[transform:rotateY(-90deg)] group-has-[input[value=back]:checked]/cube:[transform:rotateY(-180deg)] group-has-[input[value=left]:checked]/cube:[transform:rotateY(90deg)] group-has-[input[value=top]:checked]/cube:[transform:rotateX(-90deg)] group-has-[input[value=bottom]:checked]/cube:[transform:rotateX(90deg)] motion-reduce:transition-none">
      <figure class="absolute inset-0 m-0 rounded-md overflow-hidden shadow-[inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:translateZ(var(--half))]"><img src="https://images.unsplash.com/photo-1539109136881-3be0616acf4b?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera, front view" loading="lazy" decoding="async" class="block w-full h-full object-cover"></figure>
      <figure class="absolute inset-0 m-0 rounded-md overflow-hidden shadow-[inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:rotateY(90deg)_translateZ(var(--half))]"><img src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera, right side" loading="lazy" decoding="async" class="block w-full h-full object-cover"></figure>
      <figure class="absolute inset-0 m-0 rounded-md overflow-hidden shadow-[inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:rotateY(180deg)_translateZ(var(--half))]"><img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera, back view" loading="lazy" decoding="async" class="block w-full h-full object-cover"></figure>
      <figure class="absolute inset-0 m-0 rounded-md overflow-hidden shadow-[inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:rotateY(-90deg)_translateZ(var(--half))]"><img src="https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera, left side" loading="lazy" decoding="async" class="block w-full h-full object-cover"></figure>
      <figure class="absolute inset-0 m-0 rounded-md overflow-hidden shadow-[inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:rotateX(90deg)_translateZ(var(--half))]"><img src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera, top plate" loading="lazy" decoding="async" class="block w-full h-full object-cover"></figure>
      <figure class="absolute inset-0 m-0 rounded-md overflow-hidden shadow-[inset_0_0_0_1px_rgba(255,255,255,0.08)] [transform:rotateX(-90deg)_translateZ(var(--half))]"><img src="https://images.unsplash.com/photo-1470770841072-f978cf4d019e?q=80&w=400&h=400&auto=format&fit=crop" alt="Camera, base" loading="lazy" decoding="async" class="block w-full h-full object-cover"></figure>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl17-chip: #0e161b;
  --color-tgl17-chip: oklch(0.19 0.015 215);
  --color-tgl17-edge: #223038;
  --color-tgl17-edge: oklch(0.29 0.018 215);
  --color-tgl17-mut: #a9bcc4;
  --color-tgl17-mut: oklch(0.78 0.02 215);
  --color-tgl17-ink: #041318;
  --color-tgl17-ink: oklch(0.15 0.015 215);
  --color-tgl17-acc: #4fc4dd;
  --color-tgl17-acc: oklch(0.76 0.12 205);
  --font-tgl17-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tgl17-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.tgl-17 {
  width: 100%;
  min-height: 100svh;
}

.tgl-17 ::selection {
  background: var(--color-tgl17-acc);
  color: var(--color-tgl17-ink);
}
```

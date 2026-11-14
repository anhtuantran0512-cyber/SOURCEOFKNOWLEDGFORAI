---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-animated-gradient-border-pill-buttons/"
title: "Tailwind Animated Gradient Border Pill Buttons (Rotating Conic Ring)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "Plan-selector pills ringed by a rotating conic-gradient border &mdash; slow violet for idle pills, a fast solar ring plus blurred halo for the chosen one."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Gradient Border Pill Buttons (Rotating Conic Ring)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-animated-gradient-border-pill-buttons/

Plan-selector pills ringed by a rotating conic-gradient border &mdash; slow violet for idle pills, a fast solar ring plus blurred halo for the chosen one. The border is the padding-box/border-box trick in a single arbitrary [background:…], spun by an @property angle. The CSS original's halo used z-index:-1 and vanished behind the page background; an isolate wrapper fixes it.
## HTML
```html
<section class="tbg-23 w-full min-h-svh grid place-items-center bg-tbg23-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-tbg23-glow),transparent_70%)] px-5 py-14 font-tbg23-sans text-tbg23-ink" aria-label="Animated gradient border pill buttons demo">
  <div class="grid w-full max-w-[34rem] gap-4">
    <p id="tbg23-label" class="ml-0.5 font-tbg23-display text-xs font-medium uppercase tracking-[0.16em] text-tbg23-acc">Energy plan</p>
    <div role="radiogroup" aria-labelledby="tbg23-label" class="isolate flex flex-wrap gap-4">
      <label class="relative flex min-h-13 cursor-pointer items-center gap-2.5 rounded-full border-2 border-transparent px-7 text-[15px] font-bold text-tbg23-mut animate-tbg23-spin transition-colors duration-250 [background:linear-gradient(var(--color-tbg23-pill),var(--color-tbg23-pill))_padding-box,conic-gradient(from_var(--tbg23-a),#5b3a8a,#8a5bd6,#3a5b8a,#5b3a8a)_border-box] hover:text-tbg23-ink has-checked:animate-tbg23-spin-fast has-checked:text-white has-checked:[background:linear-gradient(var(--color-tbg23-pill-on),var(--color-tbg23-pill-on))_padding-box,conic-gradient(from_var(--tbg23-a),#ff7a18,#ff2bd0,#ffd24c,#ff7a18)_border-box] has-checked:before:absolute has-checked:before:-inset-1 has-checked:before:-z-1 has-checked:before:rounded-full has-checked:before:bg-[conic-gradient(from_var(--tbg23-a),#ff7a18,#ff2bd0,#ffd24c,#ff7a18)] has-checked:before:opacity-55 has-checked:before:blur-[11px] has-checked:before:animate-tbg23-spin-fast has-checked:before:content-[''] has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-tbg23-sun motion-reduce:animate-none! motion-reduce:before:animate-none!"><input type="radio" name="tbg23" class="sr-only" checked><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>Solar</label>
      <label class="relative flex min-h-13 cursor-pointer items-center gap-2.5 rounded-full border-2 border-transparent px-7 text-[15px] font-bold text-tbg23-mut animate-tbg23-spin transition-colors duration-250 [background:linear-gradient(var(--color-tbg23-pill),var(--color-tbg23-pill))_padding-box,conic-gradient(from_var(--tbg23-a),#5b3a8a,#8a5bd6,#3a5b8a,#5b3a8a)_border-box] hover:text-tbg23-ink has-checked:animate-tbg23-spin-fast has-checked:text-white has-checked:[background:linear-gradient(var(--color-tbg23-pill-on),var(--color-tbg23-pill-on))_padding-box,conic-gradient(from_var(--tbg23-a),#ff7a18,#ff2bd0,#ffd24c,#ff7a18)_border-box] has-checked:before:absolute has-checked:before:-inset-1 has-checked:before:-z-1 has-checked:before:rounded-full has-checked:before:bg-[conic-gradient(from_var(--tbg23-a),#ff7a18,#ff2bd0,#ffd24c,#ff7a18)] has-checked:before:opacity-55 has-checked:before:blur-[11px] has-checked:before:animate-tbg23-spin-fast has-checked:before:content-[''] has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-tbg23-sun motion-reduce:animate-none! motion-reduce:before:animate-none!"><input type="radio" name="tbg23" class="sr-only"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="1.8" fill="currentColor"/><ellipse cx="12" cy="12" rx="9" ry="3.6"/><ellipse cx="12" cy="12" rx="9" ry="3.6" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="3.6" transform="rotate(120 12 12)"/></svg>Fusion</label>
      <label class="relative flex min-h-13 cursor-pointer items-center gap-2.5 rounded-full border-2 border-transparent px-7 text-[15px] font-bold text-tbg23-mut animate-tbg23-spin transition-colors duration-250 [background:linear-gradient(var(--color-tbg23-pill),var(--color-tbg23-pill))_padding-box,conic-gradient(from_var(--tbg23-a),#5b3a8a,#8a5bd6,#3a5b8a,#5b3a8a)_border-box] hover:text-tbg23-ink has-checked:animate-tbg23-spin-fast has-checked:text-white has-checked:[background:linear-gradient(var(--color-tbg23-pill-on),var(--color-tbg23-pill-on))_padding-box,conic-gradient(from_var(--tbg23-a),#ff7a18,#ff2bd0,#ffd24c,#ff7a18)_border-box] has-checked:before:absolute has-checked:before:-inset-1 has-checked:before:-z-1 has-checked:before:rounded-full has-checked:before:bg-[conic-gradient(from_var(--tbg23-a),#ff7a18,#ff2bd0,#ffd24c,#ff7a18)] has-checked:before:opacity-55 has-checked:before:blur-[11px] has-checked:before:animate-tbg23-spin-fast has-checked:before:content-[''] has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-tbg23-sun motion-reduce:animate-none! motion-reduce:before:animate-none!"><input type="radio" name="tbg23" class="sr-only"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 19c0-8 5-13 14-14-1 9-6 14-14 14zM5 19l7-7"/></svg>Hybrid</label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* @property is an at-rule with no utility: it makes the ring angle animatable. */

@property --tbg23-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tbg23-bg: #08040c;
  --color-tbg23-glow: #1a0d23;
  --color-tbg23-pill: #160c1f;
  --color-tbg23-pill-on: #1d0f15;
  --color-tbg23-ink: #f0e6ff;
  --color-tbg23-mut: #c6b6dc;
  --color-tbg23-mut: oklch(0.8 0.05 300);
  --color-tbg23-acc: #d59bff;
  --color-tbg23-sun: #ffd24c;
  --font-tbg23-sans: 'Manrope', system-ui, sans-serif;
  --font-tbg23-display: 'Unbounded', system-ui, sans-serif;
  --animate-tbg23-spin: tbg23-spin 7s linear infinite;
  --animate-tbg23-spin-fast: tbg23-spin 3s linear infinite;

  @keyframes tbg23-spin {
    to {
      --tbg23-a: 360deg;
    }
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-23 {
  width: 100%;
  min-height: 100svh;
}
```

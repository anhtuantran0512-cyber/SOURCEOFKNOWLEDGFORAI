---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-hamburger-to-close-button/"
title: "Tailwind Hamburger to Close Button with aria-expanded Variants"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "Three bars become an ×."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hamburger to Close Button with aria-expanded Variants
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-hamburger-to-close-button/

Three bars become an ×. The port's win is that the animation now keys off the accessibility attribute the toggle already has to set: group-aria-expanded:rotate-45 reads aria-expanded directly, so the icon state and the announced state cannot drift.
## HTML
```html
<section class="tab-14 w-full min-h-svh bg-tab14-bg font-tab14-sans">
  <div id="tab14-shell" class="group" data-open="false">
    <div class="flex items-center justify-between px-6 py-4 border-b border-white/8">
      <span class="text-[1.1rem] font-bold tracking-[-0.01em] text-tab14-ink">MyApp</span>
      <button type="button" id="tab14-btn" aria-label="Toggle navigation" aria-expanded="false" aria-controls="tab14-menu" class="group/btn flex flex-col items-center justify-center gap-1.5 size-11 bg-white/6 border border-white/10 rounded-lg cursor-pointer transition-colors duration-[250ms] hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab14-acc aria-expanded:bg-tab14-acc/20 aria-expanded:border-tab14-acc/40">
        <span class="block w-6 h-0.5 rounded-sm bg-tab14-ink origin-center transition-[translate,rotate,scale,opacity,background-color] duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-aria-expanded/btn:translate-y-2 group-aria-expanded/btn:rotate-45 group-aria-expanded/btn:bg-tab14-acc motion-reduce:transition-none"></span>
        <span class="block w-6 h-0.5 rounded-sm bg-tab14-ink origin-center transition-[scale,opacity] duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-aria-expanded/btn:scale-x-0 group-aria-expanded/btn:opacity-0 motion-reduce:transition-none"></span>
        <span class="block w-6 h-0.5 rounded-sm bg-tab14-ink origin-center transition-[translate,rotate,scale,opacity,background-color] duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-aria-expanded/btn:-translate-y-2 group-aria-expanded/btn:-rotate-45 group-aria-expanded/btn:bg-tab14-acc motion-reduce:transition-none"></span>
      </button>
    </div>
    <nav id="tab14-menu" aria-label="Main" class="flex flex-col overflow-hidden max-h-0 px-6 opacity-0 transition-[max-height,opacity,padding] duration-[400ms] ease-[cubic-bezier(0.4,0,0.2,1)] group-data-[open=true]:max-h-52 group-data-[open=true]:opacity-100 group-data-[open=true]:py-4 motion-reduce:transition-none">
      <a href="#" class="flex items-center min-h-11 text-[0.95rem] font-semibold text-tab14-mut no-underline border-b border-white/5 transition-colors duration-200 hover:text-tab14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab14-acc">Home</a>
      <a href="#" class="flex items-center min-h-11 text-[0.95rem] font-semibold text-tab14-mut no-underline border-b border-white/5 transition-colors duration-200 hover:text-tab14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab14-acc">Features</a>
      <a href="#" class="flex items-center min-h-11 text-[0.95rem] font-semibold text-tab14-mut no-underline border-b border-white/5 transition-colors duration-200 hover:text-tab14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab14-acc">Pricing</a>
      <a href="#" class="flex items-center min-h-11 text-[0.95rem] font-semibold text-tab14-mut no-underline transition-colors duration-200 hover:text-tab14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab14-acc">Docs</a>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab14-bg: #0f172a;
  --color-tab14-bg: oklch(0.21 0.04 258);
  --color-tab14-ink: #e2e8f0;
  --color-tab14-ink: oklch(0.92 0.01 250);
  --color-tab14-mut: #94a3b8;
  --color-tab14-mut: oklch(0.72 0.03 255);
  --color-tab14-acc: #a78bfa;
  --color-tab14-acc: oklch(0.74 0.15 292);
  --font-tab14-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tab-14 {
  width: 100%;
  min-height: 100svh;
}

.tab-14 ::selection {
  background: var(--color-tab14-acc);
  color: #14091f;
}
```

## JavaScript
```js
(function () {
  var shell = document.getElementById('tab14-shell');
  var btn = document.getElementById('tab14-btn');
  if (!shell || !btn) return;
  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') !== 'true';
    btn.setAttribute('aria-expanded', String(open));
    shell.dataset.open = String(open);
  });
})();
```

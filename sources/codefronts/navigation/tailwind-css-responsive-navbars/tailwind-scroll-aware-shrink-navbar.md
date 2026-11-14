---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-scroll-aware-shrink-navbar/"
title: "Tailwind Scroll-Aware Shrink Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "A transparent hero header that becomes a compact frosted strip once the page moves."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll-Aware Shrink Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-scroll-aware-shrink-navbar/

A transparent hero header that becomes a compact frosted strip once the page moves. The script's entire job is one attribute — data-scrolled on the root — and every visual consequence is a group-data-scrolled: utility on the element it affects: the height, the logo colour, the link colour, the ghost-to-solid CTA.
## HTML
```html
<div class="tnb-06 group w-full min-h-svh bg-tnb06-page font-tnb06-sans" aria-label="Scroll-aware shrink navbar demo">
  <input type="checkbox" id="tnb06-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="fixed inset-x-0 top-0 z-200 h-20 transition-[height,background,box-shadow,backdrop-filter] duration-400 group-data-scrolled:h-15 group-data-scrolled:bg-white/95 group-data-scrolled:backdrop-blur-lg group-data-scrolled:shadow-[0_1px_3px_oklch(0_0_0/0.1),0_4px_16px_oklch(0_0_0/0.06)] motion-reduce:transition-none">
    <nav class="mx-auto flex h-full max-w-6xl items-center gap-6 px-5 md:px-8" aria-label="Primary">
      <a href="#home" class="shrink-0 text-xl font-extrabold tracking-[-0.03em] text-tnb06-paper no-underline transition-colors duration-400 group-data-scrolled:text-tnb06-ink motion-reduce:transition-none">Kol<span class="text-tnb06-acc">or</span></a>
      <ul class="hidden flex-1 list-none items-center gap-1 md:flex">
        <li><a href="#home" aria-current="page" class="rounded-lg px-3.5 py-2 text-sm font-semibold text-tnb06-acc no-underline">Home</a></li>
        <li><a href="#work" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tnb06-paper/85 no-underline transition-colors duration-400 hover:bg-white/12 hover:text-tnb06-paper group-data-scrolled:text-tnb06-ink/70 group-data-scrolled:hover:bg-tnb06-acc/10 group-data-scrolled:hover:text-tnb06-acc motion-reduce:transition-none">Work</a></li>
        <li><a href="#services" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tnb06-paper/85 no-underline transition-colors duration-400 hover:bg-white/12 hover:text-tnb06-paper group-data-scrolled:text-tnb06-ink/70 group-data-scrolled:hover:bg-tnb06-acc/10 group-data-scrolled:hover:text-tnb06-acc motion-reduce:transition-none">Services</a></li>
        <li><a href="#studio" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tnb06-paper/85 no-underline transition-colors duration-400 hover:bg-white/12 hover:text-tnb06-paper group-data-scrolled:text-tnb06-ink/70 group-data-scrolled:hover:bg-tnb06-acc/10 group-data-scrolled:hover:text-tnb06-acc motion-reduce:transition-none">Studio</a></li>
        <li><a href="#contact" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tnb06-paper/85 no-underline transition-colors duration-400 hover:bg-white/12 hover:text-tnb06-paper group-data-scrolled:text-tnb06-ink/70 group-data-scrolled:hover:bg-tnb06-acc/10 group-data-scrolled:hover:text-tnb06-acc motion-reduce:transition-none">Contact</a></li>
      </ul>
      <a href="#hire" class="hidden shrink-0 rounded-lg border-2 border-white/35 px-5 py-2 text-sm font-semibold text-tnb06-paper no-underline transition-[background,border-color,color,translate] duration-400 hover:-translate-y-px group-data-scrolled:border-transparent group-data-scrolled:bg-tnb06-acc group-data-scrolled:text-tnb06-ink md:block motion-reduce:transition-none motion-reduce:hover:translate-y-0">Hire us</a>
      <label for="tnb06-menu" class="ml-auto flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb06-paper transition-[transform,background] duration-300 group-has-checked:translate-y-2 group-has-checked:rotate-45 group-data-scrolled:bg-tnb06-ink motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb06-paper transition-[opacity,background] duration-300 group-has-checked:opacity-0 group-data-scrolled:bg-tnb06-ink motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb06-paper transition-[transform,background] duration-300 group-has-checked:-translate-y-2 group-has-checked:-rotate-45 group-data-scrolled:bg-tnb06-ink motion-reduce:transition-none"></span>
      </label>
    </nav>
    <div class="hidden border-b border-black/8 bg-white/97 px-5 py-3 backdrop-blur-lg max-md:group-has-checked:grid">
      <a href="#home" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb06-acc no-underline">Home</a>
      <a href="#work" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb06-ink/80 no-underline transition-colors hover:bg-tnb06-acc/10 hover:text-tnb06-acc">Work</a>
      <a href="#services" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb06-ink/80 no-underline transition-colors hover:bg-tnb06-acc/10 hover:text-tnb06-acc">Services</a>
      <a href="#studio" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb06-ink/80 no-underline transition-colors hover:bg-tnb06-acc/10 hover:text-tnb06-acc">Studio</a>
      <a href="#contact" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb06-ink/80 no-underline transition-colors hover:bg-tnb06-acc/10 hover:text-tnb06-acc">Contact</a>
      <a href="#hire" class="mt-2 flex min-h-11 items-center justify-center rounded-lg bg-tnb06-acc text-sm font-semibold text-tnb06-ink no-underline">Hire us</a>
    </div>
  </header>
  <section class="relative grid min-h-svh place-items-center overflow-hidden bg-linear-[135deg,var(--color-tnb06-page)_0%,var(--color-tnb06-page2)_50%,var(--color-tnb06-page)_100%] px-6 text-center">
    <div class="relative z-10 max-w-2xl">
      <h1 class="mb-4 text-[clamp(2rem,5vw,4rem)] font-extrabold tracking-[-0.04em] text-tnb06-paper">Scroll to shrink the navbar</h1>
      <p class="mx-auto max-w-lg text-lg leading-relaxed text-tnb06-paper/65">Past 60px the script sets one attribute. Height, background, shadow, logo, links and button all answer it with <code class="rounded bg-white/10 px-1.5 py-0.5 text-[0.9em]">group-data-scrolled:</code> utilities.</p>
      <p class="mt-12 animate-tnb06-bob text-sm text-tnb06-paper/40 motion-reduce:animate-none">&#8595; scroll down &#8595;</p>
    </div>
  </section>
  <main class="mx-auto max-w-3xl px-6 py-20">
    <h2 class="mb-4 text-2xl font-bold tracking-[-0.03em] text-tnb06-paper">Page content area</h2>
    <p class="text-lg leading-relaxed text-tnb06-paper/60">Scroll back to the top and the bar returns to its transparent hero state — the same transition, run backwards, because there is only one set of declarations.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb06-page: #1a1206;
  --color-tnb06-page: oklch(0.21 0.03 70);
  --color-tnb06-page2: #3d2b00;
  --color-tnb06-page2: oklch(0.32 0.07 75);
  --color-tnb06-ink: #1a1206;
  --color-tnb06-ink: oklch(0.21 0.03 70);
  --color-tnb06-paper: #faf5ee;
  --color-tnb06-paper: oklch(0.97 0.01 80);
  --color-tnb06-acc: #e8a838;
  --color-tnb06-acc: oklch(0.78 0.13 78);
  --font-tnb06-sans: 'Outfit', system-ui, sans-serif;
  --animate-tnb06-bob: tnb06-bob 2s ease-in-out infinite;
}

@keyframes tnb06-bob {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(6px);
  }
}

.tnb-06 {
  width: 100%;
  min-height: 100svh;
}

.tnb-06 ::selection {
  background: var(--color-tnb06-acc);
  color: #1a1206;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tnb-06').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var ticking = false;
    function read() {
      ticking = false;
      root.toggleAttribute('data-scrolled', window.scrollY > 60);
    }
    function onScroll() {
      if (!ticking) { ticking = true; requestAnimationFrame(read); }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    read();
  });
})();
```

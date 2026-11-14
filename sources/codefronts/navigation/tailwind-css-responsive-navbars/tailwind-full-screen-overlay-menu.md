---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-full-screen-overlay-menu/"
title: "Tailwind Full-Screen Overlay Menu"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "The agency overlay: a full-viewport curtain of oversized type that drops from the top, its links cascading in on a stagger."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full-Screen Overlay Menu
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-full-screen-overlay-menu/

The agency overlay: a full-viewport curtain of oversized type that drops from the top, its links cascading in on a stagger. The open state is aria-expanded on the button, so style and semantics cannot drift — and the stagger is one utility reading a per-link --i.
## HTML
```html
<div class="tnb-14 w-full min-h-svh bg-tnb14-page font-tnb14-sans text-tnb14-ink" aria-label="Full-screen overlay menu demo">
  <header class="group fixed inset-x-0 top-0 z-500">
    <div class="relative z-510 flex items-center justify-between px-5 py-5 md:px-10">
      <a href="#home" class="font-tnb14-display text-2xl tracking-[0.1em] text-tnb14-ink no-underline transition-colors duration-400 group-has-aria-expanded:text-tnb14-paper motion-reduce:transition-none">Forma</a>
      <button type="button" id="tnb14-toggle" aria-expanded="false" aria-controls="tnb14-overlay" aria-label="Toggle menu" class="flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 rounded-full border-0 bg-transparent transition-colors duration-200 hover:bg-black/6 group-has-aria-expanded:hover:bg-white/10">
        <span class="block h-0.5 w-7 rounded-sm bg-tnb14-ink transition-[transform,background] duration-400 group-has-aria-expanded:translate-y-2 group-has-aria-expanded:rotate-45 group-has-aria-expanded:bg-tnb14-paper motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-7 rounded-sm bg-tnb14-ink transition-[opacity,background] duration-300 group-has-aria-expanded:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-7 rounded-sm bg-tnb14-ink transition-[transform,background] duration-400 group-has-aria-expanded:-translate-y-2 group-has-aria-expanded:-rotate-45 group-has-aria-expanded:bg-tnb14-paper motion-reduce:transition-none"></span>
      </button>
    </div>
    <div id="tnb14-overlay" class="invisible fixed inset-0 z-505 flex -translate-y-full flex-col bg-tnb14-overlay px-6 pt-25 pb-10 transition-[transform,visibility] duration-600 ease-out group-has-aria-expanded:visible group-has-aria-expanded:translate-y-0 md:px-10 motion-reduce:transition-none">
      <nav class="flex flex-1 flex-col justify-center" aria-label="Overlay">
        <ul class="list-none border-t border-tnb14-paper/10">
          <li class="border-b border-tnb14-paper/10" style="--i:1"><a href="#studio" class="group/row flex translate-y-6 items-center justify-between py-5 no-underline opacity-0 transition-[opacity,transform,padding] duration-400 group-has-aria-expanded:translate-y-0 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[transition-delay:calc(var(--i)*60ms)] hover:pl-4 motion-reduce:transition-none"><span class="self-start pt-2 text-xs font-semibold tracking-[0.1em] text-tnb14-paper/30">01</span><span class="flex-1 px-4 font-tnb14-display text-[clamp(2.5rem,6vw,5rem)] leading-none tracking-[0.04em] text-tnb14-paper transition-colors duration-200 group-hover/row:text-tnb14-acc">Studio</span><span class="text-2xl text-tnb14-paper/30 transition-[color,transform] duration-200 group-hover/row:translate-x-1 group-hover/row:text-tnb14-acc" aria-hidden="true">&rarr;</span></a></li>
          <li class="border-b border-tnb14-paper/10" style="--i:2"><a href="#work" class="group/row flex translate-y-6 items-center justify-between py-5 no-underline opacity-0 transition-[opacity,transform,padding] duration-400 group-has-aria-expanded:translate-y-0 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[transition-delay:calc(var(--i)*60ms)] hover:pl-4 motion-reduce:transition-none"><span class="self-start pt-2 text-xs font-semibold tracking-[0.1em] text-tnb14-paper/30">02</span><span class="flex-1 px-4 font-tnb14-display text-[clamp(2.5rem,6vw,5rem)] leading-none tracking-[0.04em] text-tnb14-paper transition-colors duration-200 group-hover/row:text-tnb14-acc">Work</span><span class="text-2xl text-tnb14-paper/30 transition-[color,transform] duration-200 group-hover/row:translate-x-1 group-hover/row:text-tnb14-acc" aria-hidden="true">&rarr;</span></a></li>
          <li class="border-b border-tnb14-paper/10" style="--i:3"><a href="#services" class="group/row flex translate-y-6 items-center justify-between py-5 no-underline opacity-0 transition-[opacity,transform,padding] duration-400 group-has-aria-expanded:translate-y-0 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[transition-delay:calc(var(--i)*60ms)] hover:pl-4 motion-reduce:transition-none"><span class="self-start pt-2 text-xs font-semibold tracking-[0.1em] text-tnb14-paper/30">03</span><span class="flex-1 px-4 font-tnb14-display text-[clamp(2.5rem,6vw,5rem)] leading-none tracking-[0.04em] text-tnb14-paper transition-colors duration-200 group-hover/row:text-tnb14-acc">Services</span><span class="text-2xl text-tnb14-paper/30 transition-[color,transform] duration-200 group-hover/row:translate-x-1 group-hover/row:text-tnb14-acc" aria-hidden="true">&rarr;</span></a></li>
          <li class="border-b border-tnb14-paper/10" style="--i:4"><a href="#journal" class="group/row flex translate-y-6 items-center justify-between py-5 no-underline opacity-0 transition-[opacity,transform,padding] duration-400 group-has-aria-expanded:translate-y-0 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[transition-delay:calc(var(--i)*60ms)] hover:pl-4 motion-reduce:transition-none"><span class="self-start pt-2 text-xs font-semibold tracking-[0.1em] text-tnb14-paper/30">04</span><span class="flex-1 px-4 font-tnb14-display text-[clamp(2.5rem,6vw,5rem)] leading-none tracking-[0.04em] text-tnb14-paper transition-colors duration-200 group-hover/row:text-tnb14-acc">Journal</span><span class="text-2xl text-tnb14-paper/30 transition-[color,transform] duration-200 group-hover/row:translate-x-1 group-hover/row:text-tnb14-acc" aria-hidden="true">&rarr;</span></a></li>
          <li class="border-b border-tnb14-paper/10" style="--i:5"><a href="#contact" class="group/row flex translate-y-6 items-center justify-between py-5 no-underline opacity-0 transition-[opacity,transform,padding] duration-400 group-has-aria-expanded:translate-y-0 group-has-aria-expanded:opacity-100 group-has-aria-expanded:[transition-delay:calc(var(--i)*60ms)] hover:pl-4 motion-reduce:transition-none"><span class="self-start pt-2 text-xs font-semibold tracking-[0.1em] text-tnb14-paper/30">05</span><span class="flex-1 px-4 font-tnb14-display text-[clamp(2.5rem,6vw,5rem)] leading-none tracking-[0.04em] text-tnb14-paper transition-colors duration-200 group-hover/row:text-tnb14-acc">Contact</span><span class="text-2xl text-tnb14-paper/30 transition-[color,transform] duration-200 group-hover/row:translate-x-1 group-hover/row:text-tnb14-acc" aria-hidden="true">&rarr;</span></a></li>
        </ul>
      </nav>
      <div class="flex flex-wrap items-center justify-between gap-4 border-t border-tnb14-paper/10 pt-6">
        <div class="flex gap-6">
          <a href="#instagram" class="text-xs font-medium tracking-[0.08em] text-tnb14-paper/40 uppercase no-underline transition-colors hover:text-tnb14-paper">Instagram</a>
          <a href="#behance" class="text-xs font-medium tracking-[0.08em] text-tnb14-paper/40 uppercase no-underline transition-colors hover:text-tnb14-paper">Behance</a>
          <a href="#linkedin" class="text-xs font-medium tracking-[0.08em] text-tnb14-paper/40 uppercase no-underline transition-colors hover:text-tnb14-paper">LinkedIn</a>
        </div>
        <p class="text-xs tracking-[0.04em] text-tnb14-paper/40">hello@<a href="#mail" class="text-tnb14-acc no-underline">forma.studio</a></p>
      </div>
    </div>
  </header>
  <main class="px-5 pt-28 pb-16 md:px-10">
    <h1 class="mb-8 font-tnb14-display text-[clamp(3rem,8vw,7rem)] leading-[0.9] tracking-[0.04em] text-tnb14-ink">Full-Screen<br>Overlay Menu</h1>
    <p class="max-w-xl text-lg leading-relaxed text-tnb14-mut">Open it, then press Escape — the curtain closes and focus returns to the button. The rows cascade on a <code class="rounded bg-black/6 px-1.5 py-0.5 text-[0.9em]">--i</code> index, so adding a sixth link needs no new CSS.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb14-page: #f0ede8;
  --color-tnb14-page: oklch(0.94 0.008 75);
  --color-tnb14-overlay: #1a1612;
  --color-tnb14-overlay: oklch(0.22 0.01 60);
  --color-tnb14-ink: #1a1612;
  --color-tnb14-ink: oklch(0.22 0.01 60);
  --color-tnb14-mut: #6b5f4a;
  --color-tnb14-mut: oklch(0.48 0.03 75);
  --color-tnb14-paper: #f0ede8;
  --color-tnb14-paper: oklch(0.94 0.008 75);
  --color-tnb14-acc: #e85d26;
  --color-tnb14-acc: oklch(0.65 0.19 40);
  --font-tnb14-display: 'Bebas Neue', Impact, sans-serif;
  --font-tnb14-sans: 'DM Sans', system-ui, sans-serif;
}

.tnb-14 {
  width: 100%;
  min-height: 100svh;
}

.tnb-14 ::selection {
  background: var(--color-tnb14-acc);
  color: #f0ede8;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tnb-14').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var btn = root.querySelector('#tnb14-toggle');
    var overlay = root.querySelector('#tnb14-overlay');
    if (!btn || !overlay) return;
    var isOpen = function () { return btn.getAttribute('aria-expanded') === 'true'; };

    function set(open) {
      btn.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
      if (open) {
        var first = overlay.querySelector('a[href]');
        if (first) setTimeout(function () { first.focus(); }, 350);
      } else {
        btn.focus();
      }
    }

    btn.addEventListener('click', function () { set(!isOpen()); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen()) set(false);
    });
    overlay.addEventListener('click', function (e) {
      if (e.target.closest('a[href]')) set(false);
    });
  });
})();
```

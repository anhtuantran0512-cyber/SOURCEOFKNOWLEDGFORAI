---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-responsive-glass-navbar-with-burger/"
title: "Tailwind Responsive Glass Navbar with Burger"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "A glass navbar that collapses behind an animated burger &mdash; ported so the container query lives on the elements that respond to it (@max-[560px]:hidden)…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive Glass Navbar with Burger
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-responsive-glass-navbar-with-burger/

A glass navbar that collapses behind an animated burger &mdash; ported so the container query lives on the elements that respond to it (@max-[560px]:hidden) and the open state lives on one data-open attribute. That pairing is exactly what a React component wants: useState writes the attribute, and every visual consequence is already in the JSX class strings.
## HTML
```html
<section class="nbtw-08 group relative block w-full min-h-svh overflow-hidden font-nb08-sans bg-[linear-gradient(130deg,#1fa2ff,#12d8fa_50%,#a6ffcb)]" id="nbtw-08-root" data-open="false" aria-label="Responsive glass navbar with burger demo">
  <header class="@container relative z-[6] flex items-center gap-4 mx-auto mt-4 max-w-130 px-4 py-3 rounded-[18px] text-[#0a2540] bg-white/[0.24] border border-white/50 shadow-[inset_0_1px_0_rgba(255,255,255,.7),0_16px_36px_-20px_rgba(0,0,0,.4)] backdrop-blur-[20px] backdrop-saturate-[1.8]">
    <a class="text-[17px] font-extrabold no-underline text-[#0a2540] focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2" href="#nbtw-08">⬡ Stateful</a>
    <nav class="flex gap-1 ms-auto @max-[560px]:hidden" aria-label="Primary">
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-[#0a2540] text-[14.5px] font-semibold transition-colors duration-200 hover:bg-white/45 focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2 aria-[current=page]:bg-white/60" href="#nbtw-08" aria-current="page">Home</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-[#0a2540] text-[14.5px] font-semibold transition-colors duration-200 hover:bg-white/45 focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2" href="#nbtw-08">Features</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-[#0a2540] text-[14.5px] font-semibold transition-colors duration-200 hover:bg-white/45 focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2" href="#nbtw-08">Team</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-[#0a2540] text-[14.5px] font-semibold transition-colors duration-200 hover:bg-white/45 focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2" href="#nbtw-08">Contact</a>
    </nav>
    <button class="hidden ms-auto size-11 flex-col items-center justify-center gap-[5px] border-0 bg-transparent cursor-pointer @max-[560px]:flex focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2" id="nbtw-08-burger" type="button" aria-expanded="false" aria-controls="nbtw-08-sheet" aria-label="Menu">
      <span class="w-5.5 h-0.5 rounded-sm bg-[#0a2540] transition-[transform,opacity] duration-300 group-data-[open=true]:translate-y-[7px] group-data-[open=true]:rotate-45 motion-reduce:transition-none"></span>
      <span class="w-5.5 h-0.5 rounded-sm bg-[#0a2540] transition-[transform,opacity] duration-300 group-data-[open=true]:opacity-0 motion-reduce:transition-none"></span>
      <span class="w-5.5 h-0.5 rounded-sm bg-[#0a2540] transition-[transform,opacity] duration-300 group-data-[open=true]:-translate-y-[7px] group-data-[open=true]:-rotate-45 motion-reduce:transition-none"></span>
    </button>
  </header>
  <div class="absolute z-[5] left-1/2 top-[86px] -translate-x-1/2 -translate-y-2.5 w-[calc(100%-32px)] max-w-130 flex flex-col gap-1 p-2.5 rounded-[18px] bg-white/[0.28] border border-white/50 shadow-[0_24px_50px_-24px_rgba(0,0,0,.5)] backdrop-blur-[22px] backdrop-saturate-[1.8] opacity-0 invisible pointer-events-none transition-[opacity,transform,visibility] duration-300 group-data-[open=true]:opacity-100 group-data-[open=true]:visible group-data-[open=true]:pointer-events-auto group-data-[open=true]:translate-y-0 motion-reduce:transition-none" id="nbtw-08-sheet" role="group" aria-label="Mobile menu">
    <a class="flex items-center min-h-11 px-3.5 rounded-xl no-underline text-[#0a2540] text-[15px] font-semibold transition-colors duration-200 hover:bg-white/45 focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2 aria-[current=page]:bg-white/60" href="#nbtw-08" aria-current="page">Home</a>
    <a class="flex items-center min-h-11 px-3.5 rounded-xl no-underline text-[#0a2540] text-[15px] font-semibold transition-colors duration-200 hover:bg-white/45 focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2" href="#nbtw-08">Features</a>
    <a class="flex items-center min-h-11 px-3.5 rounded-xl no-underline text-[#0a2540] text-[15px] font-semibold transition-colors duration-200 hover:bg-white/45 focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2" href="#nbtw-08">Team</a>
    <a class="flex items-center min-h-11 px-3.5 rounded-xl no-underline text-[#0a2540] text-[15px] font-semibold transition-colors duration-200 hover:bg-white/45 focus-visible:outline-2 focus-visible:outline-[#0a2540] focus-visible:outline-offset-2" href="#nbtw-08">Contact</a>
  </div>
  <div class="grid place-items-center min-h-[60svh] px-6">
    <p class="max-w-[38ch] text-center text-[#0a2540] text-[15px] font-semibold leading-[1.6]">Narrow the preview below 560px: the links hide and the burger appears, both stated as <code>@max-[560px]:</code> utilities on the elements themselves.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb08-sans: system-ui, 'Segoe UI', sans-serif;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#nbtw-08-root');
  const burger = document.querySelector('#nbtw-08-burger');
  const sheet = document.querySelector('#nbtw-08-sheet');
  if (!root || !burger || !sheet) return;
  let open = false;                       // React: const [open, setOpen] = useState(false)
  const render = () => {
    root.dataset.open = String(open);     // React: data-open={String(open)}
    burger.setAttribute('aria-expanded', String(open));
    if (open) sheet.querySelector('a').focus();
  };
  burger.addEventListener('click', () => { open = !open; render(); });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && open) { open = false; render(); burger.focus(); }
  });
  root.addEventListener('click', (e) => {
    if (open && !e.target.closest('header') && !e.target.closest('#nbtw-08-sheet')) { open = false; render(); }
  });
})();
```

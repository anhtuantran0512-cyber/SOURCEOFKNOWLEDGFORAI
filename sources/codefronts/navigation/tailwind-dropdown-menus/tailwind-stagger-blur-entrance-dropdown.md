---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-stagger-blur-entrance-dropdown/"
title: "Tailwind Stagger Blur Entrance Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "Items that crystallise out of a frosted blur, one after another."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stagger Blur Entrance Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-stagger-blur-entrance-dropdown/

Items that crystallise out of a frosted blur, one after another. The CSS version computes the stagger in JavaScript and writes inline transitionDelay on every item; here the delays are declarative — style="--i:3" plus one utility — and the script shrinks to a single attribute toggle.
## HTML
```html
<section class="tdd-18 w-full min-h-svh grid justify-center content-start bg-linear-[135deg,var(--color-tdd18-bg1),var(--color-tdd18-bg2)] font-tdd18-sans text-tdd18-ink px-5 py-9" aria-label="Stagger blur entrance dropdown demo">
  <nav class="flex w-[min(480px,100%)] items-center justify-between rounded-2xl border border-tdd18-edge bg-white px-4 py-3 shadow-[0_4px_20px_oklch(0.54_0.24_295/0.1)]" aria-label="Primary">
    <span class="text-lg font-bold tracking-[-0.5px] text-tdd18-acc">Specter</span>
    <div class="group relative">
      <button type="button" id="tdd18-btn" aria-expanded="false" aria-controls="tdd18-panel" class="flex min-h-11 cursor-pointer items-center gap-2 rounded-[10px] border-0 bg-tdd18-acc px-4.5 py-2 font-tdd18-sans text-sm font-semibold text-white transition-opacity duration-150 hover:opacity-90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd18-acc aria-expanded:opacity-85">
        Menu
        <span class="size-2 rounded-full bg-tdd18-dot transition-[scale,background] duration-300 ease-tdd18 group-data-open:scale-150 group-data-open:bg-tdd18-dot2 motion-reduce:transition-none" aria-hidden="true"></span>
      </button>
      <div id="tdd18-panel" class="pointer-events-none invisible absolute top-[calc(100%+10px)] right-0 flex min-w-50 flex-col gap-0.5 rounded-2xl border border-tdd18-edge bg-white p-2 opacity-0 shadow-[0_12px_40px_oklch(0.54_0.24_295/0.18)] transition-[opacity,visibility] duration-200 group-data-open:pointer-events-auto group-data-open:visible group-data-open:opacity-100">
        <a href="#launch" style="--i:0" class="flex items-center gap-2.5 rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd18-ink no-underline opacity-0 translate-y-1.5 blur-[6px] transition-[opacity,translate,filter,background] duration-300 hover:bg-tdd18-tint focus-visible:bg-tdd18-tint focus-visible:outline-none group-data-open:translate-y-0 group-data-open:opacity-100 group-data-open:blur-none group-data-open:[transition-delay:calc(var(--i)*55ms)] motion-reduce:blur-none motion-reduce:[transition-delay:0ms]">&#128640; Launch</a>
        <a href="#discover" style="--i:1" class="flex items-center gap-2.5 rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd18-ink no-underline opacity-0 translate-y-1.5 blur-[6px] transition-[opacity,translate,filter,background] duration-300 hover:bg-tdd18-tint focus-visible:bg-tdd18-tint focus-visible:outline-none group-data-open:translate-y-0 group-data-open:opacity-100 group-data-open:blur-none group-data-open:[transition-delay:calc(var(--i)*55ms)] motion-reduce:blur-none motion-reduce:[transition-delay:0ms]">&#127775; Discover</a>
        <a href="#metrics" style="--i:2" class="flex items-center gap-2.5 rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd18-ink no-underline opacity-0 translate-y-1.5 blur-[6px] transition-[opacity,translate,filter,background] duration-300 hover:bg-tdd18-tint focus-visible:bg-tdd18-tint focus-visible:outline-none group-data-open:translate-y-0 group-data-open:opacity-100 group-data-open:blur-none group-data-open:[transition-delay:calc(var(--i)*55ms)] motion-reduce:blur-none motion-reduce:[transition-delay:0ms]">&#128202; Metrics</a>
        <a href="#community" style="--i:3" class="flex items-center gap-2.5 rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd18-ink no-underline opacity-0 translate-y-1.5 blur-[6px] transition-[opacity,translate,filter,background] duration-300 hover:bg-tdd18-tint focus-visible:bg-tdd18-tint focus-visible:outline-none group-data-open:translate-y-0 group-data-open:opacity-100 group-data-open:blur-none group-data-open:[transition-delay:calc(var(--i)*55ms)] motion-reduce:blur-none motion-reduce:[transition-delay:0ms]">&#128172; Community</a>
        <a href="#security" style="--i:4" class="flex items-center gap-2.5 rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd18-ink no-underline opacity-0 translate-y-1.5 blur-[6px] transition-[opacity,translate,filter,background] duration-300 hover:bg-tdd18-tint focus-visible:bg-tdd18-tint focus-visible:outline-none group-data-open:translate-y-0 group-data-open:opacity-100 group-data-open:blur-none group-data-open:[transition-delay:calc(var(--i)*55ms)] motion-reduce:blur-none motion-reduce:[transition-delay:0ms]">&#128274; Security</a>
        <div class="my-1 h-px bg-tdd18-edge" aria-hidden="true"></div>
        <a href="#upgrade" style="--i:5" class="flex items-center gap-2.5 rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-bold text-tdd18-acc no-underline opacity-0 translate-y-1.5 blur-[6px] transition-[opacity,translate,filter,background] duration-300 hover:bg-tdd18-tint focus-visible:bg-tdd18-tint focus-visible:outline-none group-data-open:translate-y-0 group-data-open:opacity-100 group-data-open:blur-none group-data-open:[transition-delay:calc(var(--i)*55ms)] motion-reduce:blur-none motion-reduce:[transition-delay:0ms]">&#9889; Upgrade</a>
      </div>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd18-bg1: #faf5ff;
  --color-tdd18-bg1: oklch(0.98 0.02 305);
  --color-tdd18-bg2: #ede9fe;
  --color-tdd18-bg2: oklch(0.94 0.03 295);
  --color-tdd18-ink: #18181b;
  --color-tdd18-ink: oklch(0.22 0.005 285);
  --color-tdd18-edge: #e4e4e7;
  --color-tdd18-edge: oklch(0.91 0.004 285);
  --color-tdd18-tint: #f5f3ff;
  --color-tdd18-tint: oklch(0.97 0.02 295);
  --color-tdd18-acc: #7c3aed;
  --color-tdd18-acc: oklch(0.54 0.24 295);
  --color-tdd18-dot: #a78bfa;
  --color-tdd18-dot: oklch(0.74 0.14 295);
  --color-tdd18-dot2: #c4b5fd;
  --color-tdd18-dot2: oklch(0.83 0.09 295);
  --font-tdd18-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tdd18: cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tdd-18 {
  width: 100%;
  min-height: 100svh;
}

.tdd-18 ::selection {
  background: var(--color-tdd18-acc);
  color: #ede9fe;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tdd-18').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var wrap = root.querySelector('.group'),
        btn = root.querySelector('#tdd18-btn');
    if (!wrap || !btn) return;
    function set(open) {
      wrap.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
    }
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      set(btn.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) set(false); });
    root.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && wrap.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
  });
})();
```

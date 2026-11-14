---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-scattered-photos-pinch-to-centre-on-hover/"
title: "Tailwind Scattered Photos Pinch to Centre on Hover"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Hover one photo and the whole cluster gathers toward the centre and dims, while the one you touched brightens and rises."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scattered Photos Pinch to Centre on Hover
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-scattered-photos-pinch-to-centre-on-hover/

Hover one photo and the whole cluster gathers toward the centre and dims, while the one you touched brightens and rises. The group behaviour is group-has-hover: &mdash; Tailwind's variant form of :has(:hover) &mdash; and the spotlight override needs the ! modifier, because the hovered photo has to beat a rule its own parent just applied to it.
## HTML
```html
<section class="stk-19 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk19-sans bg-stk19-bg" aria-label="Pinch-to-focus photo cluster">
  <div class="group relative w-[min(360px,90vw)] h-85">
    <a class="absolute left-1/2 top-1/2 -ml-[75px] -mt-[75px] size-37.5 overflow-hidden rounded-[14px] shadow-[0_16px_34px_-18px_rgba(0,0,0,0.8)] [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,filter] duration-450 ease-stk19 group-has-hover:brightness-50 group-has-hover:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] group-has-focus-visible:brightness-50 group-has-focus-visible:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] hover:z-10 hover:brightness-110! hover:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:z-10 focus-visible:outline-none focus-visible:brightness-110! focus-visible:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:shadow-[0_0_0_3px_var(--color-stk19-ring),0_24px_44px_-18px_rgba(0,0,0,0.9)] motion-reduce:group-has-hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))] motion-reduce:hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))_scale(1.1)]!" href="#" style="--x:-120px;--y:-40px;--r:-7deg">
      <img class="block size-full object-cover" src="https://picsum.photos/seed/tw-pinch-1/260/260" width="260" height="260" alt="Street market stall at night">
    </a>
    <a class="absolute left-1/2 top-1/2 -ml-[75px] -mt-[75px] size-37.5 overflow-hidden rounded-[14px] shadow-[0_16px_34px_-18px_rgba(0,0,0,0.8)] [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,filter] duration-450 ease-stk19 group-has-hover:brightness-50 group-has-hover:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] group-has-focus-visible:brightness-50 group-has-focus-visible:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] hover:z-10 hover:brightness-110! hover:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:z-10 focus-visible:outline-none focus-visible:brightness-110! focus-visible:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:shadow-[0_0_0_3px_var(--color-stk19-ring),0_24px_44px_-18px_rgba(0,0,0,0.9)] motion-reduce:group-has-hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))] motion-reduce:hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))_scale(1.1)]!" href="#" style="--x:110px;--y:-60px;--r:6deg">
      <img class="block size-full object-cover" src="https://picsum.photos/seed/tw-pinch-2/260/260" width="260" height="260" alt="Neon-lit alleyway">
    </a>
    <a class="absolute left-1/2 top-1/2 -ml-[75px] -mt-[75px] size-37.5 overflow-hidden rounded-[14px] shadow-[0_16px_34px_-18px_rgba(0,0,0,0.8)] [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,filter] duration-450 ease-stk19 group-has-hover:brightness-50 group-has-hover:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] group-has-focus-visible:brightness-50 group-has-focus-visible:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] hover:z-10 hover:brightness-110! hover:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:z-10 focus-visible:outline-none focus-visible:brightness-110! focus-visible:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:shadow-[0_0_0_3px_var(--color-stk19-ring),0_24px_44px_-18px_rgba(0,0,0,0.9)] motion-reduce:group-has-hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))] motion-reduce:hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))_scale(1.1)]!" href="#" style="--x:-90px;--y:70px;--r:5deg">
      <img class="block size-full object-cover" src="https://picsum.photos/seed/tw-pinch-3/260/260" width="260" height="260" alt="Rooftop garden in summer">
    </a>
    <a class="absolute left-1/2 top-1/2 -ml-[75px] -mt-[75px] size-37.5 overflow-hidden rounded-[14px] shadow-[0_16px_34px_-18px_rgba(0,0,0,0.8)] [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,filter] duration-450 ease-stk19 group-has-hover:brightness-50 group-has-hover:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] group-has-focus-visible:brightness-50 group-has-focus-visible:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] hover:z-10 hover:brightness-110! hover:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:z-10 focus-visible:outline-none focus-visible:brightness-110! focus-visible:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:shadow-[0_0_0_3px_var(--color-stk19-ring),0_24px_44px_-18px_rgba(0,0,0,0.9)] motion-reduce:group-has-hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))] motion-reduce:hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))_scale(1.1)]!" href="#" style="--x:120px;--y:60px;--r:-6deg">
      <img class="block size-full object-cover" src="https://picsum.photos/seed/tw-pinch-4/260/260" width="260" height="260" alt="Harbour lights reflected on water">
    </a>
    <a class="absolute left-1/2 top-1/2 -ml-[75px] -mt-[75px] size-37.5 overflow-hidden rounded-[14px] shadow-[0_16px_34px_-18px_rgba(0,0,0,0.8)] [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,filter] duration-450 ease-stk19 group-has-hover:brightness-50 group-has-hover:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] group-has-focus-visible:brightness-50 group-has-focus-visible:[transform:translate(calc(var(--x)*0.3),calc(var(--y)*0.3))_rotate(0deg)] hover:z-10 hover:brightness-110! hover:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:z-10 focus-visible:outline-none focus-visible:brightness-110! focus-visible:[transform:translate(0,0)_rotate(0deg)_scale(1.25)]! focus-visible:shadow-[0_0_0_3px_var(--color-stk19-ring),0_24px_44px_-18px_rgba(0,0,0,0.9)] motion-reduce:group-has-hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))] motion-reduce:hover:[transform:translate(var(--x),var(--y))_rotate(var(--r))_scale(1.1)]!" href="#" style="--x:0px;--y:0px;--r:2deg">
      <img class="block size-full object-cover" src="https://picsum.photos/seed/tw-pinch-5/260/260" width="260" height="260" alt="Landscape blurred past a train window">
    </a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk19-bg: #0c0d13;
  --color-stk19-bg: oklch(0.14 0.012 275);
  --color-stk19-ring: #5aa8e8;
  --color-stk19-ring: oklch(0.70 0.15 250);
  --font-stk19-sans: 'Archivo', system-ui, sans-serif;
  --ease-stk19: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```

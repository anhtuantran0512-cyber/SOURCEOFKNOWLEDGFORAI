---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-login-signup-modal-native-dialog-starting-style/"
title: "Tailwind Login / Signup Modal with Native Dialog & Starting-Style"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "The reference-grade auth overlay: one native <dialog> flips between Sign in and Create account with zero-JS tabs, floating labels and a blurring backdrop."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Login / Signup Modal with Native Dialog & Starting-Style
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-login-signup-modal-native-dialog-starting-style/

The reference-grade auth overlay: one native <dialog> flips between Sign in and Create account with zero-JS tabs, floating labels and a blurring backdrop. The port's win is open: + open:starting: + transition-discrete — the closed state, the open state and the frame the browser paints before the transition all sit in one class list on the element that animates.
## HTML
```html
<section class="tm-01 w-full min-h-svh grid place-items-center bg-tm01-bg font-tm01-sans px-6 py-10">
  <button type="button" data-tm01-open class="inline-flex items-center justify-center min-h-11 px-7 rounded-xl text-[15px] font-semibold text-tm01-ink bg-tm01-btn border border-tm01-btnedge cursor-pointer transition-colors duration-200 hover:bg-tm01-btnhover hover:border-tm01-acc focus-visible:outline-2 focus-visible:outline-tm01-acc focus-visible:outline-offset-2">Sign in</button>

  <dialog id="tm-01-dlg" aria-labelledby="tm-01-title" class="m-auto w-[min(400px,94vw)] p-0 border-0 rounded-[18px] text-tm01-ink bg-tm01-card shadow-[0_30px_80px_-30px_#000,0_0_0_1px_var(--color-tm01-edge)] opacity-0 translate-y-2.5 scale-[0.98] transition-[opacity,translate,scale,overlay,display] duration-300 ease-out transition-discrete open:opacity-100 open:translate-y-0 open:scale-100 open:starting:opacity-0 open:starting:translate-y-2.5 open:starting:scale-[0.98] open:backdrop:bg-tm01-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <form method="dialog" class="group relative p-8">
      <input type="radio" name="tm-01-tab" id="tm-01-in" class="peer/in sr-only" checked>
      <input type="radio" name="tm-01-tab" id="tm-01-up" class="peer/up sr-only">

      <button type="submit" value="close" aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tm01-mut text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-tm01-well hover:text-tm01-ink focus-visible:outline-2 focus-visible:outline-tm01-acc focus-visible:outline-offset-2">&times;</button>

      <div class="relative grid grid-cols-2 mt-1 mb-6 p-1 rounded-xl bg-tm01-well border border-tm01-edge">
        <span aria-hidden="true" class="absolute z-[1] inset-y-1 left-1 w-[calc(50%-0.25rem)] rounded-lg bg-tm01-pill border border-tm01-pilledge transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-[#tm-01-up:checked]:translate-x-full motion-reduce:transition-none"></span>
        <label for="tm-01-in" class="relative z-[2] grid place-items-center min-h-10 rounded-lg text-[13.5px] font-semibold text-tm01-mut cursor-pointer transition-colors duration-200 group-has-[#tm-01-in:checked]:text-white group-has-[#tm-01-in:focus-visible]:outline-2 group-has-[#tm-01-in:focus-visible]:outline-tm01-acc group-has-[#tm-01-in:focus-visible]:outline-offset-2">Sign in</label>
        <label for="tm-01-up" class="relative z-[2] grid place-items-center min-h-10 rounded-lg text-[13.5px] font-semibold text-tm01-mut cursor-pointer transition-colors duration-200 group-has-[#tm-01-up:checked]:text-white group-has-[#tm-01-up:focus-visible]:outline-2 group-has-[#tm-01-up:focus-visible]:outline-tm01-acc group-has-[#tm-01-up:focus-visible]:outline-offset-2">Create account</label>
      </div>

      <h2 id="tm-01-title" class="mb-5 text-[22px] font-bold tracking-[-0.01em] text-tm01-hi">
        <span class="group-has-[#tm-01-up:checked]:hidden">Welcome back</span>
        <span class="hidden group-has-[#tm-01-up:checked]:inline">Create your account</span>
      </h2>

      <div class="relative mb-3.5 hidden group-has-[#tm-01-up:checked]:block">
        <input type="text" id="tm-01-name" placeholder=" " autocomplete="name" class="peer w-full pt-[18px] pb-2 px-3.5 rounded-[10px] border border-tm01-edge bg-tm01-well text-[15px] text-tm01-hi transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm01-acc focus:shadow-[0_0_0_3px_var(--color-tm01-ring)]">
        <label for="tm-01-name" class="absolute left-3.5 top-[15px] origin-left text-[15px] text-tm01-mut pointer-events-none transition-[transform,font-size,color] duration-200 peer-focus:-translate-y-2.5 peer-focus:text-[11px] peer-focus:text-tm01-acc peer-[:not(:placeholder-shown)]:-translate-y-2.5 peer-[:not(:placeholder-shown)]:text-[11px] peer-[:not(:placeholder-shown)]:text-tm01-acc motion-reduce:transition-none">Full name</label>
      </div>

      <div class="relative mb-3.5">
        <input type="email" id="tm-01-email" placeholder=" " required autocomplete="email" class="peer w-full pt-[18px] pb-2 px-3.5 rounded-[10px] border border-tm01-edge bg-tm01-well text-[15px] text-tm01-hi transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm01-acc focus:shadow-[0_0_0_3px_var(--color-tm01-ring)]">
        <label for="tm-01-email" class="absolute left-3.5 top-[15px] origin-left text-[15px] text-tm01-mut pointer-events-none transition-[transform,font-size,color] duration-200 peer-focus:-translate-y-2.5 peer-focus:text-[11px] peer-focus:text-tm01-acc peer-[:not(:placeholder-shown)]:-translate-y-2.5 peer-[:not(:placeholder-shown)]:text-[11px] peer-[:not(:placeholder-shown)]:text-tm01-acc motion-reduce:transition-none">Email address</label>
      </div>

      <div class="relative mb-3.5">
        <input type="password" id="tm-01-pass" placeholder=" " required autocomplete="current-password" class="peer w-full pt-[18px] pb-2 px-3.5 rounded-[10px] border border-tm01-edge bg-tm01-well text-[15px] text-tm01-hi transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm01-acc focus:shadow-[0_0_0_3px_var(--color-tm01-ring)]">
        <label for="tm-01-pass" class="absolute left-3.5 top-[15px] origin-left text-[15px] text-tm01-mut pointer-events-none transition-[transform,font-size,color] duration-200 peer-focus:-translate-y-2.5 peer-focus:text-[11px] peer-focus:text-tm01-acc peer-[:not(:placeholder-shown)]:-translate-y-2.5 peer-[:not(:placeholder-shown)]:text-[11px] peer-[:not(:placeholder-shown)]:text-tm01-acc motion-reduce:transition-none">Password</label>
      </div>

      <button type="button" data-tm01-submit class="w-full min-h-11 mt-2 rounded-[10px] border-0 bg-tm01-acc text-[15px] font-bold text-tm01-onacc cursor-pointer transition-[filter,translate] duration-200 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">
        <span class="group-has-[#tm-01-up:checked]:hidden">Sign in</span>
        <span class="hidden group-has-[#tm-01-up:checked]:inline">Create account</span>
      </button>
      <p class="mt-4 text-center text-[12.5px] leading-relaxed text-tm01-mut">By continuing you agree to our Terms &amp; Privacy Policy.</p>
    </form>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm01-bg: #0b0e14;
  --color-tm01-bg: oklch(0.16 0.015 260);
  --color-tm01-card: #141821;
  --color-tm01-card: oklch(0.21 0.017 260);
  --color-tm01-well: #0c0f16;
  --color-tm01-well: oklch(0.17 0.015 260);
  --color-tm01-edge: #232a36;
  --color-tm01-edge: oklch(0.29 0.017 260);
  --color-tm01-btn: #151b27;
  --color-tm01-btn: oklch(0.22 0.025 260);
  --color-tm01-btnedge: #2a3346;
  --color-tm01-btnedge: oklch(0.32 0.03 260);
  --color-tm01-btnhover: #1c2536;
  --color-tm01-btnhover: oklch(0.26 0.035 260);
  --color-tm01-ink: #e7ecf5;
  --color-tm01-ink: oklch(0.92 0.01 260);
  --color-tm01-hi: #f3f6fc;
  --color-tm01-hi: oklch(0.97 0.006 260);
  --color-tm01-mut: #9aa3b4;
  --color-tm01-mut: oklch(0.72 0.02 260);
  --color-tm01-acc: #7aa2ff;
  --color-tm01-acc: oklch(0.72 0.16 255);
  --color-tm01-onacc: #06101f;
  --color-tm01-onacc: oklch(0.18 0.04 255);
  --color-tm01-pill: #253049;
  --color-tm01-pill: oklch(0.32 0.06 258);
  --color-tm01-pilledge: #3c4f7a;
  --color-tm01-pilledge: oklch(0.44 0.1 258);
  --color-tm01-ring: #7aa2ff4d;
  --color-tm01-ring: oklch(0.72 0.16 255 / 0.3);
  --color-tm01-scrim: #06080ca3;
  --color-tm01-scrim: oklch(0.13 0.01 260 / 0.64);
  --font-tm01-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the width half of the full-bleed contract; the height comes from the
   markup's min-h-svh utility. */

.tm-01 {
  width: 100%;
}
/* The one thing the variants cannot hold: the ::backdrop enter/exit transition.
   open:backdrop:* sets the lit state; these four lines animate it in and out. */

#tm-01-dlg::backdrop {
  background: oklch(0.13 0.01 260 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-01-dlg[open]::backdrop {
    background: oklch(0.13 0.01 260 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tm-01-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-01');
  var dlg = root.querySelector('#tm-01-dlg');
  var card = dlg.querySelector('form');
  root.querySelector('[data-tm01-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tm01-submit]').addEventListener('click', function () { dlg.close(); });
  // Light-dismiss: the click landed on the dialog box, outside the card's rect.
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```

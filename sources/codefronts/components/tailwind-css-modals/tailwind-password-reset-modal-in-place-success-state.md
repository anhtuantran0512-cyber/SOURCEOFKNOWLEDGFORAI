---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-password-reset-modal-in-place-success-state/"
title: "Tailwind Password Reset Modal with In-Place Success State"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A single-input recovery dialog that swaps in place to a neutral 'check your inbox' panel."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Password Reset Modal with In-Place Success State
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-password-reset-modal-in-place-success-state/

A single-input recovery dialog that swaps in place to a neutral 'check your inbox' panel. The port replaces the original's hidden-toggling JavaScript with one data-view attribute on the dialog and two data-[view=…]: variants — the state lives in the DOM where the styles can read it, and the controller shrinks to one assignment.
## HTML
```html
<section class="tm-02 w-full min-h-svh grid place-items-center bg-tm02-bg font-tm02-sans px-6 py-10">
  <button type="button" data-tm02-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-xl text-sm font-semibold text-tm02-ink bg-tm02-btn border border-tm02-edge cursor-pointer transition-colors duration-200 hover:bg-tm02-well hover:border-tm02-acc focus-visible:outline-2 focus-visible:outline-tm02-acc focus-visible:outline-offset-2">Forgot password?</button>

  <dialog id="tm-02-dlg" data-view="form" aria-labelledby="tm-02-title" class="group m-auto w-[min(400px,94vw)] p-0 border-0 rounded-[18px] text-center text-tm02-ink bg-tm02-card shadow-[0_30px_80px_-30px_#000,0_0_0_1px_var(--color-tm02-edge)] opacity-0 scale-[0.96] transition-[opacity,translate,scale,overlay,display] duration-[260ms] transition-discrete open:opacity-100 open:scale-100 open:starting:opacity-0 open:starting:scale-[0.96] open:backdrop:bg-tm02-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <div class="relative px-8 pt-9 pb-8">
      <button type="button" data-tm02-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tm02-mut text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-tm02-well hover:text-tm02-ink focus-visible:outline-2 focus-visible:outline-tm02-acc focus-visible:outline-offset-2">&times;</button>

      <div class="group-data-[view=done]:hidden">
        <div aria-hidden="true" class="grid place-items-center size-15 mx-auto mt-1 mb-4.5 rounded-2xl text-[28px] bg-tm02-acctint text-tm02-acc shadow-[0_0_0_1px_var(--color-tm02-accedge),0_0_34px_-8px_var(--color-tm02-acc)]">&#9993;</div>
        <h2 id="tm-02-title" class="mb-2.5 text-[21px] font-bold tracking-[-0.01em] text-tm02-hi">Reset your password</h2>
        <p class="mb-5 text-sm leading-relaxed text-tm02-mut">Enter the email tied to your account and we&#39;ll send a secure reset link.</p>
        <form data-tm02-form novalidate class="text-left">
          <div class="relative mb-3.5">
            <input type="email" id="tm-02-email" placeholder=" " required autocomplete="email" class="peer w-full pt-[18px] pb-2 px-3.5 rounded-[10px] border border-tm02-edge bg-tm02-well text-[15px] text-tm02-hi transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm02-acc focus:shadow-[0_0_0_3px_var(--color-tm02-ring)] user-invalid:border-tm02-bad user-invalid:shadow-[0_0_0_3px_var(--color-tm02-badring)]">
            <label for="tm-02-email" class="absolute left-3.5 top-[15px] origin-left text-[15px] text-tm02-mut pointer-events-none transition-[transform,font-size,color] duration-200 peer-focus:-translate-y-2.5 peer-focus:text-[11px] peer-focus:text-tm02-acc peer-[:not(:placeholder-shown)]:-translate-y-2.5 peer-[:not(:placeholder-shown)]:text-[11px] peer-[:not(:placeholder-shown)]:text-tm02-acc motion-reduce:transition-none">Email address</label>
            <p class="hidden mt-1.5 text-xs text-tm02-bad peer-user-invalid:block">Enter a valid email address.</p>
          </div>
          <button type="submit" class="w-full min-h-11 rounded-[10px] border-0 bg-tm02-acc text-[15px] font-bold text-tm02-onacc cursor-pointer transition-[filter,translate] duration-200 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Send reset link</button>
        </form>
      </div>

      <div class="hidden group-data-[view=done]:block">
        <div aria-hidden="true" class="grid place-items-center size-15 mx-auto mt-1 mb-4.5 rounded-2xl text-[28px] bg-tm02-oktint text-tm02-ok shadow-[0_0_0_1px_var(--color-tm02-okedge),0_0_40px_-8px_var(--color-tm02-ok)] animate-tm02-pop motion-reduce:animate-none">&#10003;</div>
        <h2 class="mb-2.5 text-[21px] font-bold tracking-[-0.01em] text-tm02-hi">Check your inbox</h2>
        <p class="mb-5 text-sm leading-relaxed text-tm02-mut">If an account exists for <b data-tm02-mail class="text-tm02-hi font-semibold">that address</b>, a reset link is on its way. It expires in 30&nbsp;minutes.</p>
        <button type="button" data-tm02-ack class="w-full min-h-11 rounded-[10px] border-0 bg-tm02-acc text-[15px] font-bold text-tm02-onacc cursor-pointer transition-[filter,translate] duration-200 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Got it</button>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm02-bg: #080b0c;
  --color-tm02-bg: oklch(0.15 0.012 200);
  --color-tm02-card: #131b1e;
  --color-tm02-card: oklch(0.21 0.015 200);
  --color-tm02-well: #0c1315;
  --color-tm02-well: oklch(0.17 0.012 200);
  --color-tm02-btn: #111a1d;
  --color-tm02-btn: oklch(0.2 0.015 200);
  --color-tm02-edge: #26343a;
  --color-tm02-edge: oklch(0.3 0.015 200);
  --color-tm02-ink: #e7eef0;
  --color-tm02-ink: oklch(0.92 0.008 200);
  --color-tm02-hi: #f0f6f7;
  --color-tm02-hi: oklch(0.96 0.005 200);
  --color-tm02-mut: #9dabaf;
  --color-tm02-mut: oklch(0.73 0.015 200);
  --color-tm02-acc: #4fd0e0;
  --color-tm02-acc: oklch(0.79 0.12 200);
  --color-tm02-acctint: #10282c;
  --color-tm02-acctint: oklch(0.24 0.04 200);
  --color-tm02-accedge: #2e6d77;
  --color-tm02-accedge: oklch(0.45 0.07 200);
  --color-tm02-onacc: #04161a;
  --color-tm02-onacc: oklch(0.18 0.03 200);
  --color-tm02-ok: #7ae2a8;
  --color-tm02-ok: oklch(0.85 0.16 150);
  --color-tm02-oktint: #122a1e;
  --color-tm02-oktint: oklch(0.25 0.05 150);
  --color-tm02-okedge: #37785a;
  --color-tm02-okedge: oklch(0.48 0.09 150);
  --color-tm02-bad: #f08a8a;
  --color-tm02-bad: oklch(0.72 0.15 25);
  --color-tm02-badring: #f08a8a3d;
  --color-tm02-badring: oklch(0.72 0.15 25 / 0.24);
  --color-tm02-ring: #4fd0e047;
  --color-tm02-ring: oklch(0.79 0.12 200 / 0.28);
  --color-tm02-scrim: #04080999;
  --color-tm02-scrim: oklch(0.12 0.008 200 / 0.62);
  --font-tm02-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tm02-pop: tm02-pop .4s cubic-bezier(.2,1.4,.4,1) both;
}

.tm-02 {
  width: 100%;
}

@keyframes tm02-pop {
  from {
    transform: scale(.4);
    opacity: 0;
  }

  to {
    transform: scale(1);
    opacity: 1;
  }
}

#tm-02-dlg::backdrop {
  background: oklch(0.12 0.008 200 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-02-dlg[open]::backdrop {
    background: oklch(0.12 0.008 200 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-02');
  var dlg = root.querySelector('#tm-02-dlg');
  var email = root.querySelector('#tm-02-email');
  root.querySelector('[data-tm02-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tm02-close]').addEventListener('click', function () { dlg.close(); });
  root.querySelector('[data-tm02-ack]').addEventListener('click', function () { dlg.close(); });
  root.querySelector('[data-tm02-form]').addEventListener('submit', function (e) {
    e.preventDefault();
    if (!email.checkValidity()) { email.reportValidity(); return; }
    root.querySelector('[data-tm02-mail]').textContent = email.value;
    dlg.dataset.view = 'done';                       // the only state change
    root.querySelector('[data-tm02-ack]').focus();   // never strand focus
  });
  dlg.addEventListener('close', function () { dlg.dataset.view = 'form'; });
})();
```

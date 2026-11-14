---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-success-error-result-modal-drawn-svg-icon/"
title: "Tailwind Success / Error Result Modal with Drawn SVG Icon"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "The result modal: a tick that draws itself on success, a cross that draws and shakes on error."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Success / Error Result Modal with Drawn SVG Icon
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-success-error-result-modal-drawn-svg-icon/

The result modal: a tick that draws itself on success, a cross that draws and shakes on error. One data-state on the dialog drives both, read by group-data-[state=ok]: and group-data-[state=err]: on the SVG parts — no class juggling in the controller.
## HTML
```html
<section class="tm-12 w-full min-h-svh grid place-items-center bg-tm12-bg font-tm12-sans px-6 py-10">
  <div class="flex flex-wrap justify-center gap-3">
    <button type="button" data-tm12-ok class="inline-flex items-center justify-center min-h-11 px-5 rounded-xl border-0 bg-tm12-ok text-sm font-bold text-tm12-onok cursor-pointer transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tm12-ok">Simulate success</button>
    <button type="button" data-tm12-err class="inline-flex items-center justify-center min-h-11 px-5 rounded-xl bg-tm12-badtint border border-tm12-badedge text-sm font-bold text-tm12-badink cursor-pointer transition-colors duration-200 hover:bg-tm12-badhover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tm12-bad">Simulate error</button>
  </div>

  <dialog id="tm-12-dlg" data-state="busy" aria-labelledby="tm-12-title" class="group m-auto w-[min(360px,92vw)] p-0 rounded-3xl border border-white/10 bg-tm12-card text-center text-tm12-ink shadow-[0_40px_90px_-30px_#000] opacity-0 translate-y-3 scale-[0.96] transition-[opacity,translate,scale,overlay,display] duration-[280ms] transition-discrete open:opacity-100 open:translate-y-0 open:scale-100 open:starting:opacity-0 open:starting:translate-y-3 open:starting:scale-[0.96] open:backdrop:bg-tm12-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <div class="px-8 pt-9 pb-7">
      <div aria-hidden="true" class="mx-auto mb-5 grid size-20 place-items-center group-data-[state=err]:animate-tm12-shake motion-reduce:animate-none">
        <svg viewBox="0 0 52 52" class="size-20">
          <circle cx="26" cy="26" r="24" fill="none" stroke-width="3" class="stroke-tm12-ring opacity-50 group-data-[state=ok]:stroke-tm12-ok group-data-[state=ok]:opacity-100 group-data-[state=ok]:animate-tm12-ring group-data-[state=err]:stroke-tm12-bad group-data-[state=err]:opacity-100 group-data-[state=err]:animate-tm12-ring motion-reduce:animate-none motion-reduce:[stroke-dasharray:160_160]"></circle>
          <path data-tm12-mark d="" fill="none" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" class="[stroke-dasharray:48] [stroke-dashoffset:48] group-data-[state=ok]:stroke-tm12-okmark group-data-[state=ok]:animate-tm12-draw group-data-[state=err]:stroke-tm12-badmark group-data-[state=err]:animate-tm12-draw motion-reduce:animate-none motion-reduce:[stroke-dashoffset:0]"></path>
        </svg>
      </div>
      <h2 id="tm-12-title" data-tm12-title class="text-[22px] font-extrabold tracking-tight">Working&hellip;</h2>
      <p data-tm12-msg role="status" aria-live="polite" class="mt-2 text-sm leading-relaxed text-tm12-mut">Processing your request.</p>
      <button type="button" data-tm12-done class="mt-6 w-full min-h-12 rounded-xl border-0 bg-tm12-btn text-[15px] font-bold text-tm12-onbtn cursor-pointer transition-[background-color,translate] duration-200 hover:bg-white active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tm12-ok motion-reduce:active:translate-y-0">Done</button>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm12-bg: #060908;
  --color-tm12-bg: oklch(0.14 0.012 165);
  --color-tm12-card: #17191b;
  --color-tm12-card: oklch(0.22 0.005 165);
  --color-tm12-ink: #eceeef;
  --color-tm12-ink: oklch(0.94 0.004 165);
  --color-tm12-mut: #a3a8ab;
  --color-tm12-mut: oklch(0.74 0.008 165);
  --color-tm12-ring: #4a4f52;
  --color-tm12-ring: oklch(0.42 0.006 165);
  --color-tm12-btn: #ededed;
  --color-tm12-btn: oklch(0.94 0.002 165);
  --color-tm12-onbtn: #1a1c1d;
  --color-tm12-onbtn: oklch(0.23 0.004 165);
  --color-tm12-ok: #4ade9a;
  --color-tm12-ok: oklch(0.8 0.17 155);
  --color-tm12-okmark: #7cf0b8;
  --color-tm12-okmark: oklch(0.87 0.17 155);
  --color-tm12-onok: #04231a;
  --color-tm12-onok: oklch(0.22 0.05 165);
  --color-tm12-bad: #f0553f;
  --color-tm12-bad: oklch(0.66 0.21 25);
  --color-tm12-badmark: #ff7a66;
  --color-tm12-badmark: oklch(0.73 0.19 25);
  --color-tm12-badink: #ffc9c0;
  --color-tm12-badink: oklch(0.86 0.07 25);
  --color-tm12-badtint: #2a1310;
  --color-tm12-badtint: oklch(0.24 0.06 25);
  --color-tm12-badhover: #3a1a16;
  --color-tm12-badhover: oklch(0.29 0.08 25);
  --color-tm12-badedge: #7a3128;
  --color-tm12-badedge: oklch(0.43 0.13 25);
  --color-tm12-scrim: #0408079e;
  --color-tm12-scrim: oklch(0.12 0.008 165 / 0.62);
  --font-tm12-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tm12-ring: tm12-ring .5s ease forwards;
  --animate-tm12-draw: tm12-draw .45s .25s cubic-bezier(.2,1.3,.4,1) forwards;
  --animate-tm12-shake: tm12-shake .4s .55s both;
}

.tm-12 {
  width: 100%;
}

@keyframes tm12-ring {
  from {
    stroke-dasharray: 0 160;
  }

  to {
    stroke-dasharray: 160 160;
  }
}

@keyframes tm12-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes tm12-shake {
  0%,
    100% {
    transform: translateX(0);
  }

  20% {
    transform: translateX(-6px);
  }

  40% {
    transform: translateX(6px);
  }

  60% {
    transform: translateX(-4px);
  }

  80% {
    transform: translateX(4px);
  }
}

#tm-12-dlg::backdrop {
  background: oklch(0.12 0.008 165 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-12-dlg[open]::backdrop {
    background: oklch(0.12 0.008 165 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-12');
  var dlg = root.querySelector('#tm-12-dlg');
  var mark = root.querySelector('[data-tm12-mark]');
  var title = root.querySelector('[data-tm12-title]');
  var msg = root.querySelector('[data-tm12-msg]');
  var CHECK = 'M14 27 l8 8 l16 -17';
  var CROSS = 'M18 18 L34 34 M34 18 L18 34';

  function show(kind) {
    var ok = kind === 'ok';
    dlg.dataset.state = 'busy';
    mark.setAttribute('d', ok ? CHECK : CROSS);
    title.textContent = ok ? 'All done!' : 'Something went wrong';
    msg.textContent = ok ? "Your changes were saved successfully." : "We could not save your changes. Please try again.";
    msg.setAttribute('role', ok ? 'status' : 'alert');
    msg.setAttribute('aria-live', ok ? 'polite' : 'assertive');
    if (!dlg.open) dlg.showModal();
    void dlg.offsetWidth;            // reflow so the stroke animation restarts
    dlg.dataset.state = ok ? 'ok' : 'err';
    root.querySelector('[data-tm12-done]').focus();
  }

  root.querySelector('[data-tm12-ok]').addEventListener('click', function () { show('ok'); });
  root.querySelector('[data-tm12-err]').addEventListener('click', function () { show('err'); });
  root.querySelector('[data-tm12-done]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('close', function () { dlg.dataset.state = 'busy'; });
})();
```

---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/success-error-feedback-state/"
title: "Success / Error Feedback State"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A micro-interaction result modal that draws an animated tick for success or a shaking cross for error after an async action — styled with Tailwind utilities,…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Success / Error Feedback State
Source: https://codefronts.com/components/css-modals/success-error-feedback-state/

A micro-interaction result modal that draws an animated tick for success or a shaking cross for error after an async action — styled with Tailwind utilities, the animation stroke drawn in a few keyframes. The satisfying 'it worked' / 'it failed' confirmation.
## HTML
```html
<script src="https://cdn.tailwindcss.com"></script>
<div class="cm-12 min-h-[100dvh] grid place-items-center gap-0 p-8 font-sans" style="background:radial-gradient(120% 120% at 50% 0%,#0a1110,#060908)">
  <div class="flex gap-3">
    <button class="cm-12__ok cursor-pointer rounded-xl bg-emerald-500 px-5 py-3 text-[14px] font-bold text-emerald-950 transition hover:brightness-110 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-emerald-300">Simulate success</button>
    <button class="cm-12__err cursor-pointer rounded-xl border border-rose-500/50 bg-rose-500/10 px-5 py-3 text-[14px] font-bold text-rose-200 transition hover:bg-rose-500/20 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-rose-400">Simulate error</button>
  </div>

  <dialog class="cm-12__dlg w-[min(360px,92vw)] rounded-3xl border border-white/10 bg-neutral-900 p-0 text-center text-neutral-100 shadow-2xl">
    <div class="px-8 pb-7 pt-9">
      <div class="cm-12__icon mx-auto mb-5 grid h-20 w-20 place-items-center">
        <svg viewBox="0 0 52 52" class="h-20 w-20"><circle class="cm-12__ring" cx="26" cy="26" r="24" fill="none" stroke-width="3"></circle><path class="cm-12__mark" fill="none" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" d=""></path></svg>
      </div>
      <h2 class="cm-12__title text-[22px] font-extrabold tracking-tight">Working…</h2>
      <p class="cm-12__msg mt-2 text-[14px] leading-relaxed text-neutral-400" role="status">Processing your request.</p>
      <button class="cm-12__done mt-6 w-full rounded-xl bg-neutral-100 px-4 py-3 text-[15px] font-bold text-neutral-900 transition hover:bg-white active:translate-y-px focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-emerald-400" type="button">Done</button>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-12__dlg {
  margin: auto;
  opacity: 0;
  transform: translateY(12px) scale(.96);
  transition: opacity .28s,transform .28s,overlay .28s allow-discrete,display .28s allow-discrete;
}

.cm-12__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-12__dlg[open] {
    opacity: 0;
    transform: translateY(12px) scale(.96);
  }
}

.cm-12__dlg::backdrop {
  background: rgba(4,8,7,0);
  backdrop-filter: blur(0);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-12__dlg[open]::backdrop {
  background: rgba(4,8,7,.62);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-12__dlg[open]::backdrop {
    background: rgba(4,8,7,0);
    backdrop-filter: blur(0);
  }
}

.cm-12__ring {
  stroke: #3f3f46;
  opacity: .5;
}

.cm-12__mark {
  stroke-dasharray: 48;
  stroke-dashoffset: 48;
}

.cm-12__dlg.is-ok .cm-12__ring {
  stroke: oklch(0.8 0.17 155);
  opacity: 1;
  animation: cm-12-ring .5s ease forwards;
}

.cm-12__dlg.is-ok .cm-12__mark {
  stroke: oklch(0.85 0.17 155);
  animation: cm-12-draw .45s .25s cubic-bezier(.2,1.3,.4,1) forwards;
}

.cm-12__dlg.is-err .cm-12__ring {
  stroke: oklch(0.68 0.2 22);
  opacity: 1;
  animation: cm-12-ring .5s ease forwards;
}

.cm-12__dlg.is-err .cm-12__mark {
  stroke: oklch(0.72 0.2 22);
  animation: cm-12-draw .45s .25s ease forwards;
}

.cm-12__dlg.is-err .cm-12__icon {
  animation: cm-12-shake .4s .55s both;
}

@keyframes cm-12-ring {
  from {
    stroke-dasharray: 0 160;
  }

  to {
    stroke-dasharray: 160 160;
  }
}

@keyframes cm-12-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes cm-12-shake {
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

@media (prefers-reduced-motion: reduce) {
  .cm-12__dlg,
    .cm-12__dlg::backdrop {
    transition-duration: .001s;
  }

  .cm-12__mark {
    stroke-dashoffset: 0;
  }

  .cm-12__ring {
    stroke-dasharray: 160 160;
  }

  .cm-12__dlg .cm-12__icon,
    .cm-12__dlg .cm-12__mark,
    .cm-12__dlg .cm-12__ring {
    animation: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-12');
  var dlg = root.querySelector('.cm-12__dlg');
  var title = root.querySelector('.cm-12__title');
  var msg = root.querySelector('.cm-12__msg');
  var mark = root.querySelector('.cm-12__mark');
  var CHECK = 'M14 27 l8 8 l16 -17';
  var CROSS = 'M18 18 L34 34 M34 18 L18 34';
  function show(kind){
    dlg.classList.remove('is-ok','is-err');
    mark.setAttribute('d', kind === 'ok' ? CHECK : CROSS);
    title.textContent = kind === 'ok' ? 'All done!' : 'Something went wrong';
    msg.textContent = kind === 'ok' ? 'Your changes were saved successfully.' : 'We couldn\'t save your changes. Please try again.';
    msg.setAttribute('role', kind === 'ok' ? 'status' : 'alert');
    dlg.showModal();
    // reflow so the stroke animation restarts each time
    void dlg.offsetWidth;
    dlg.classList.add(kind === 'ok' ? 'is-ok' : 'is-err');
  }
  root.querySelector('.cm-12__ok').addEventListener('click', function(){ show('ok'); });
  root.querySelector('.cm-12__err').addEventListener('click', function(){ show('err'); });
  root.querySelector('.cm-12__done').addEventListener('click', function(){ dlg.close(); });
})();
```

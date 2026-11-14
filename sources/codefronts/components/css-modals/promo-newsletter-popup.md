---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/promo-newsletter-popup/"
title: "Promo / Newsletter Popup"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A high-contrast, timed coupon capture styled entirely with Tailwind utility classes: a bold cream card with one email field and a strong CTA that fires once…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Promo / Newsletter Popup
Source: https://codefronts.com/components/css-modals/promo-newsletter-popup/

A high-contrast, timed coupon capture styled entirely with Tailwind utility classes: a bold cream card with one email field and a strong CTA that fires once after a delay. The copy-paste conversion popup for utility-first stacks.
## HTML
```html
<script src="https://cdn.tailwindcss.com"></script>
<div class="cm-07 min-h-[100dvh] grid place-items-center p-8 font-sans" style="background:radial-gradient(120% 120% at 50% 0%,#141019,#08060b)">
  <div class="flex flex-col items-center gap-3">
    <button class="cm-07__open cursor-pointer rounded-xl border border-white/15 bg-white/5 px-6 py-3 text-[15px] font-semibold text-neutral-100 transition hover:bg-white/10 focus-visible:outline focus-visible:outline-2 focus-visible:outline-fuchsia-400">Show popup</button>
    <span class="font-mono text-xs tracking-widest text-neutral-500">auto-opens once after 3s</span>
  </div>

  <dialog class="cm-07__dlg w-[min(430px,94vw)] overflow-hidden rounded-3xl border border-black/10 bg-neutral-50 p-0 text-neutral-900 shadow-2xl">
    <div class="relative">
      <button class="cm-07__x absolute right-3 top-3 grid h-9 w-9 place-items-center rounded-lg text-neutral-400 transition hover:bg-black/5 hover:text-neutral-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-fuchsia-500" type="button" aria-label="Close popup">&times;</button>
      <div class="h-2 w-full bg-gradient-to-r from-fuchsia-500 via-rose-500 to-amber-400"></div>
      <div class="px-8 pb-8 pt-9 text-center">
        <p class="mb-2 text-xs font-bold uppercase tracking-[0.2em] text-fuchsia-600">Members get 15% off</p>
        <h2 class="cm-07__title mb-2 text-[26px] font-extrabold leading-tight tracking-tight">Unlock your welcome code</h2>
        <p class="mb-6 text-[14px] leading-relaxed text-neutral-500">Join the list for first access to drops and a coupon in your inbox today.</p>
        <form class="cm-07__form flex flex-col gap-3">
          <label for="cm-07-email" class="sr-only">Email address</label>
          <input id="cm-07-email" type="email" required placeholder="[email protected]" class="w-full rounded-xl border border-neutral-300 bg-white px-4 py-3.5 text-[15px] text-neutral-900 placeholder-neutral-400 focus:border-fuchsia-500 focus:outline-none focus:ring-4 focus:ring-fuchsia-500/20">
          <button type="submit" class="w-full rounded-xl bg-neutral-900 px-4 py-3.5 text-[15px] font-bold text-white transition hover:bg-neutral-800 active:translate-y-px focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-fuchsia-500">Claim my 15% off</button>
        </form>
        <p class="mt-4 text-[11px] text-neutral-400">No spam. Unsubscribe anytime.</p>
      </div>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-07__dlg {
  margin: auto;
  opacity: 0;
  transform: translateY(16px) scale(.96);
  transition: opacity .3s,transform .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-07__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-07__dlg[open] {
    opacity: 0;
    transform: translateY(16px) scale(.96);
  }
}

.cm-07__dlg::backdrop {
  background: rgba(6,6,10,0);
  backdrop-filter: blur(0);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-07__dlg[open]::backdrop {
  background: rgba(6,6,10,.6);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-07__dlg[open]::backdrop {
    background: rgba(6,6,10,0);
    backdrop-filter: blur(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cm-07__dlg,
    .cm-07__dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-07');
  var dlg = root.querySelector('.cm-07__dlg');
  var opened = false;
  function open(){ if(!dlg.open){ dlg.showModal(); opened = true; } }
  root.querySelector('.cm-07__open').addEventListener('click', open);
  root.querySelector('.cm-07__x').addEventListener('click', function(){ dlg.close(); });
  // timed trigger — fires once
  setTimeout(function(){ if(!opened) open(); }, 3000);
  root.querySelector('.cm-07__form').addEventListener('submit', function(e){
    e.preventDefault();
    root.querySelector('.cm-07__title').textContent = 'You\'re in — check your inbox! 🎉';
    var f = this; setTimeout(function(){ dlg.close(); }, 1200);
    f.style.display = 'none';
  });
})();
```

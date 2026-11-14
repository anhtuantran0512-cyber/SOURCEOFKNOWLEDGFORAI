---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-multi-step-onboarding-modal-data-step-variants/"
title: "Tailwind Multi-Step Onboarding Modal with data-step Variants"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A three-step product tour in a dialog: art, one idea per panel, progress dots and a Skip that always works."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Step Onboarding Modal with data-step Variants
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-multi-step-onboarding-modal-data-step-variants/

A three-step product tour in a dialog: art, one idea per panel, progress dots and a Skip that always works. One data-step on the card selects the panel, the dot and the button labels, so the controller sets a number and nothing else.
## HTML
```html
<section class="tm-14 w-full min-h-svh grid place-items-center bg-tm14-bg font-tm14-sans px-6 py-10">
  <button type="button" data-tm14-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-xl text-[15px] font-semibold text-tm14-ink bg-tm14-btn border border-tm14-btnedge cursor-pointer transition-colors duration-200 hover:bg-tm14-btnhover hover:border-tm14-acc focus-visible:outline-2 focus-visible:outline-tm14-acc focus-visible:outline-offset-2">Start tour</button>

  <dialog id="tm-14-dlg" aria-labelledby="tm-14-title" class="m-auto w-[min(440px,94vw)] p-0 border-0 rounded-[20px] text-tm14-ink bg-tm14-card shadow-[0_40px_90px_-30px_#000,0_0_0_1px_var(--color-tm14-edge)] opacity-0 scale-[0.97] transition-[opacity,translate,scale,overlay,display] duration-[280ms] transition-discrete open:opacity-100 open:scale-100 open:starting:opacity-0 open:starting:scale-[0.97] open:backdrop:bg-tm14-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <div data-tm14-card data-step="0" class="group relative p-7">
      <button type="button" data-tm14-skip class="absolute top-3 right-4 min-h-11 px-2 border-0 bg-transparent text-[13px] font-semibold text-tm14-mut cursor-pointer rounded-md transition-colors duration-200 hover:text-tm14-ink focus-visible:outline-2 focus-visible:outline-tm14-acc focus-visible:outline-offset-2">Skip</button>

      <div class="min-h-[230px] pt-3.5">
        <section class="hidden group-data-[step=0]:block text-center animate-tm14-in motion-reduce:animate-none">
          <div aria-hidden="true" class="grid place-items-center size-24 mx-auto mb-5 rounded-[22px] text-[42px] bg-tm14-arttint shadow-[inset_0_0_0_1px_var(--color-tm14-artedge),0_0_50px_-14px_var(--color-tm14-acc)]">📊</div>
          <h2 id="tm-14-title" tabindex="-1" class="mb-2.5 text-[22px] font-bold text-tm14-hi outline-none">Welcome to your dashboard</h2>
          <p class="max-w-[34ch] mx-auto text-[14.5px] leading-relaxed text-tm14-mut">Everything about your projects, in one live view. Let&#39;s take 30 seconds to get you oriented.</p>
        </section>
        <section class="hidden group-data-[step=1]:block text-center animate-tm14-in motion-reduce:animate-none">
          <div aria-hidden="true" class="grid place-items-center size-24 mx-auto mb-5 rounded-[22px] text-[42px] bg-tm14-arttint shadow-[inset_0_0_0_1px_var(--color-tm14-artedge),0_0_50px_-14px_var(--color-tm14-acc)]">🔎</div>
          <h2 tabindex="-1" class="mb-2.5 text-[22px] font-bold text-tm14-hi outline-none">Filter &amp; find anything</h2>
          <p class="max-w-[34ch] mx-auto text-[14.5px] leading-relaxed text-tm14-mut">Slice by status, owner or date, then save the view. Your team sees the same filtered board instantly.</p>
        </section>
        <section class="hidden group-data-[step=2]:block text-center animate-tm14-in motion-reduce:animate-none">
          <div aria-hidden="true" class="grid place-items-center size-24 mx-auto mb-5 rounded-[22px] text-[42px] bg-tm14-arttint shadow-[inset_0_0_0_1px_var(--color-tm14-artedge),0_0_50px_-14px_var(--color-tm14-acc)]">🤝</div>
          <h2 tabindex="-1" class="mb-2.5 text-[22px] font-bold text-tm14-hi outline-none">Invite your team</h2>
          <p class="max-w-[34ch] mx-auto text-[14.5px] leading-relaxed text-tm14-mut">Add teammates and assign roles. You can always change permissions later from Settings.</p>
        </section>
      </div>

      <div class="mt-6">
        <div aria-hidden="true" class="flex justify-center gap-[7px] mb-2.5">
          <i class="h-[7px] w-[7px] rounded-full bg-tm14-dot transition-all duration-[250ms] group-data-[step=0]:w-5.5 group-data-[step=0]:rounded group-data-[step=0]:bg-tm14-acc motion-reduce:transition-none"></i>
          <i class="h-[7px] w-[7px] rounded-full bg-tm14-dot transition-all duration-[250ms] group-data-[step=1]:w-5.5 group-data-[step=1]:rounded group-data-[step=1]:bg-tm14-acc motion-reduce:transition-none"></i>
          <i class="h-[7px] w-[7px] rounded-full bg-tm14-dot transition-all duration-[250ms] group-data-[step=2]:w-5.5 group-data-[step=2]:rounded group-data-[step=2]:bg-tm14-acc motion-reduce:transition-none"></i>
        </div>
        <p data-tm14-count aria-live="polite" class="mb-4 text-center font-tm14-mono text-xs tracking-[0.12em] text-tm14-faint">Step 1 of 3</p>
        <div class="grid grid-cols-2 gap-3">
          <button type="button" data-tm14-back disabled class="min-h-12 rounded-xl text-[14.5px] font-bold cursor-pointer text-tm14-ink bg-tm14-btn border border-tm14-btnedge transition-colors duration-200 hover:bg-tm14-btnhover disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-tm14-btn focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Back</button>
          <button type="button" data-tm14-next class="min-h-12 rounded-xl text-[14.5px] font-bold cursor-pointer border-0 bg-tm14-acc text-tm14-onacc transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Next</button>
        </div>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm14-bg: #08070c;
  --color-tm14-bg: oklch(0.14 0.015 285);
  --color-tm14-card: #161426;
  --color-tm14-card: oklch(0.21 0.025 285);
  --color-tm14-btn: #191627;
  --color-tm14-btn: oklch(0.22 0.025 285);
  --color-tm14-btnhover: #221d35;
  --color-tm14-btnhover: oklch(0.26 0.035 285);
  --color-tm14-btnedge: #322d49;
  --color-tm14-btnedge: oklch(0.32 0.04 285);
  --color-tm14-edge: #2a2742;
  --color-tm14-edge: oklch(0.29 0.035 285);
  --color-tm14-arttint: #221c3d;
  --color-tm14-arttint: oklch(0.27 0.06 285);
  --color-tm14-artedge: #443a70;
  --color-tm14-artedge: oklch(0.4 0.09 285);
  --color-tm14-dot: #37324e;
  --color-tm14-dot: oklch(0.33 0.035 285);
  --color-tm14-hi: #f4f2fc;
  --color-tm14-hi: oklch(0.96 0.008 285);
  --color-tm14-ink: #ddd9ee;
  --color-tm14-ink: oklch(0.89 0.018 285);
  --color-tm14-mut: #a7a2c2;
  --color-tm14-mut: oklch(0.73 0.03 285);
  --color-tm14-faint: #8d87ad;
  --color-tm14-faint: oklch(0.63 0.035 285);
  --color-tm14-acc: #9d8bfa;
  --color-tm14-acc: oklch(0.72 0.16 285);
  --color-tm14-onacc: #0a0616;
  --color-tm14-onacc: oklch(0.16 0.04 285);
  --color-tm14-scrim: #06050aa3;
  --color-tm14-scrim: oklch(0.12 0.012 285 / 0.64);
  --font-tm14-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tm14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tm14-in: tm14-in .35s ease both;
}

.tm-14 {
  width: 100%;
}

@keyframes tm14-in {
  from {
    opacity: 0;
    transform: translateX(14px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

#tm-14-dlg::backdrop {
  background: oklch(0.12 0.012 285 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-14-dlg[open]::backdrop {
    background: oklch(0.12 0.012 285 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-14');
  var dlg = root.querySelector('#tm-14-dlg');
  var card = root.querySelector('[data-tm14-card]');
  var count = root.querySelector('[data-tm14-count]');
  var back = root.querySelector('[data-tm14-back]');
  var next = root.querySelector('[data-tm14-next]');
  var total = 3, i = 0;

  function render() {
    card.dataset.step = i;                       // the only state change
    count.textContent = 'Step ' + (i + 1) + ' of ' + total;
    back.disabled = i === 0;
    next.textContent = i === total - 1 ? 'Get started' : 'Next';
    var h = card.querySelectorAll('h2')[i];
    if (h) h.focus();                            // move focus with the content
  }

  root.querySelector('[data-tm14-open]').addEventListener('click', function () { i = 0; render(); dlg.showModal(); });
  root.querySelector('[data-tm14-skip]').addEventListener('click', function () { dlg.close(); });
  back.addEventListener('click', function () { if (i > 0) { i--; render(); } });
  next.addEventListener('click', function () { if (i < total - 1) { i++; render(); } else dlg.close(); });
})();
```

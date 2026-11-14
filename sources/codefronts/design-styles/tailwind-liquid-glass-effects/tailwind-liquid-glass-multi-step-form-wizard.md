---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-multi-step-form-wizard/"
title: "Tailwind Liquid Glass Multi-Step Form Wizard"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "An onboarding wizard whose progress dots physically merge as the fill grows toward them &mdash; the goo filter from demo 04, applied to a progress track."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Multi-Step Form Wizard
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-multi-step-form-wizard/

An onboarding wizard whose progress dots physically merge as the fill grows toward them &mdash; the goo filter from demo 04, applied to a progress track. The port's discipline: the script sets data-active, aria-current and one custom property, and every visual consequence is a variant in the markup.
## HTML
```html
<section id="lgt-20-root" class="lgt-20 grid w-full min-h-svh place-items-center p-15 font-lgt20-sans [background:radial-gradient(circle_at_25%_20%,#2a2350,#120f24_60%),radial-gradient(circle_at_80%_90%,#1c2f55,#120f24_60%)]" style="--p:0%" aria-label="Tailwind liquid glass multi-step wizard">
  <svg width="0" height="0" aria-hidden="true" class="absolute">
    <filter id="lgt-20-goo">
      <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="b"/>
      <feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -8"/>
    </filter>
  </svg>

  <form novalidate class="w-[min(440px,94vw)] rounded-[26px] border border-white/30 bg-white/11 p-7.5 text-white backdrop-blur-[24px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.45),0_40px_80px_-34px_rgba(0,0,0,.7)]">

    <div aria-hidden="true" class="mb-2 h-6.5">
      <div class="relative h-6.5 [filter:url(#lgt-20-goo)]">
        <span class="absolute top-2.25 left-2.25 h-2 rounded-full bg-lgt20-accent transition-[width] duration-500 ease-out [width:var(--p,0%)] motion-reduce:transition-none"></span>
        <span data-dot data-active class="absolute top-0.75 left-0 size-5 rounded-full bg-lgt20-track transition-colors duration-400 data-active:bg-lgt20-accent"></span>
        <span data-dot class="absolute top-0.75 left-[calc(50%-10px)] size-5 rounded-full bg-lgt20-track transition-colors duration-400 data-active:bg-lgt20-accent"></span>
        <span data-dot class="absolute top-0.75 right-0 size-5 rounded-full bg-lgt20-track transition-colors duration-400 data-active:bg-lgt20-accent"></span>
      </div>
    </div>

    <p id="lgt-20-count" aria-live="polite" class="mb-4.5 text-xs font-bold uppercase tracking-[0.08em] text-white/70">Step 1 of 3</p>

    <div class="relative">
      <fieldset data-step data-active class="hidden border-0 p-0 data-active:block data-active:animate-lgt20-slide motion-reduce:data-active:animate-none">
        <legend class="mb-4 p-0 text-xl font-extrabold">Your details</legend>
        <label for="lgt-20-name" class="mt-3.5 mb-1.75 block text-xs font-semibold uppercase tracking-[0.05em] text-white/70">Name</label>
        <input id="lgt-20-name" type="text" required placeholder="Ada Lovelace" class="w-full rounded-[12px] border border-white/25 bg-white/8 px-3.5 py-3 text-[15px] text-white outline-none transition-[border-color,box-shadow] duration-200 placeholder:text-white/50 focus:border-lgt20-accent focus:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-lgt20-accent)_40%,transparent)] user-invalid:border-lgt20-err user-invalid:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-lgt20-err)_40%,transparent)]">
        <label for="lgt-20-email" class="mt-3.5 mb-1.75 block text-xs font-semibold uppercase tracking-[0.05em] text-white/70">Email</label>
        <input id="lgt-20-email" type="email" required placeholder="[email protected]" class="w-full rounded-[12px] border border-white/25 bg-white/8 px-3.5 py-3 text-[15px] text-white outline-none transition-[border-color,box-shadow] duration-200 placeholder:text-white/50 focus:border-lgt20-accent focus:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-lgt20-accent)_40%,transparent)] user-invalid:border-lgt20-err user-invalid:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-lgt20-err)_40%,transparent)]">
      </fieldset>

      <fieldset data-step class="hidden border-0 p-0 data-active:block data-active:animate-lgt20-slide motion-reduce:data-active:animate-none">
        <legend class="mb-4 p-0 text-xl font-extrabold">Workspace</legend>
        <label for="lgt-20-org" class="mt-3.5 mb-1.75 block text-xs font-semibold uppercase tracking-[0.05em] text-white/70">Organization</label>
        <input id="lgt-20-org" type="text" required placeholder="Studio Lumen" class="w-full rounded-[12px] border border-white/25 bg-white/8 px-3.5 py-3 text-[15px] text-white outline-none transition-[border-color,box-shadow] duration-200 placeholder:text-white/50 focus:border-lgt20-accent focus:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-lgt20-accent)_40%,transparent)] user-invalid:border-lgt20-err user-invalid:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-lgt20-err)_40%,transparent)]">
        <label for="lgt-20-role" class="mt-3.5 mb-1.75 block text-xs font-semibold uppercase tracking-[0.05em] text-white/70">Role</label>
        <input id="lgt-20-role" type="text" placeholder="Design lead" class="w-full rounded-[12px] border border-white/25 bg-white/8 px-3.5 py-3 text-[15px] text-white outline-none transition-[border-color,box-shadow] duration-200 placeholder:text-white/50 focus:border-lgt20-accent focus:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-lgt20-accent)_40%,transparent)]">
      </fieldset>

      <fieldset data-step class="hidden border-0 p-0 data-active:block data-active:animate-lgt20-slide motion-reduce:data-active:animate-none">
        <legend class="mb-4 p-0 text-xl font-extrabold">All set</legend>
        <p class="py-3 text-base leading-relaxed text-white/90">Review and finish &mdash; your Liquid Glass workspace is ready to launch.</p>
      </fieldset>
    </div>

    <div class="mt-6 flex justify-between gap-3">
      <button id="lgt-20-back" type="button" disabled class="cursor-pointer rounded-[12px] border border-white/30 bg-white/12 px-6 py-3 text-[15px] font-bold text-white transition-[background-color,transform,opacity] duration-200 not-disabled:hover:-translate-y-0.5 not-disabled:hover:bg-white/20 disabled:cursor-not-allowed disabled:opacity-40 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">Back</button>
      <button id="lgt-20-next" type="button" class="cursor-pointer rounded-[12px] border border-lgt20-accent/60 bg-linear-to-b from-lgt20-accent-top to-lgt20-accent px-6 py-3 text-[15px] font-bold text-white transition-[filter,transform] duration-200 hover:-translate-y-0.5 hover:brightness-110 focus-visible:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">Next</button>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt20-accent: #7c5cf0;
  --color-lgt20-accent: oklch(0.66 0.19 285);
  --color-lgt20-accent-top: #9b83f6;
  --color-lgt20-accent-top: oklch(0.72 0.16 285);
  --color-lgt20-track: #3d3763;
  --color-lgt20-err: #e2503c;
  --color-lgt20-err: oklch(0.65 0.2 25);
  --font-lgt20-sans: 'Manrope', system-ui, sans-serif;
  --animate-lgt20-slide: lgt-20-slide 0.4s ease;
}

@keyframes lgt-20-slide {
  from {
    opacity: 0;
    transform: translateX(14px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lgt-20-root');
  const steps = [...root.querySelectorAll('[data-step]')];
  const dots = [...root.querySelectorAll('[data-dot]')];
  const fill = root.querySelector('[data-dot]').parentElement.querySelector('span');
  const count = root.querySelector('#lgt-20-count');
  const back = root.querySelector('#lgt-20-back');
  const next = root.querySelector('#lgt-20-next');
  let i = 0;
  const last = steps.length - 1;

  const paint = () => {
    steps.forEach((s, n) => n === i ? s.setAttribute('data-active', '') : s.removeAttribute('data-active'));
    dots.forEach((d, n) => n <= i ? d.setAttribute('data-active', '') : d.removeAttribute('data-active'));
    root.style.setProperty('--p', (i / last * 100) + '%');
    count.textContent = 'Step ' + (i + 1) + ' of ' + steps.length;
    back.disabled = i === 0;
    next.textContent = i === last ? 'Finish' : 'Next';
    const f = steps[i].querySelector('input');
    if (f) f.focus();
  };

  // Constraint validation does the work; :user-invalid paints the result.
  const validate = () => [...steps[i].querySelectorAll('input[required]')]
    .map(inp => { inp.reportValidity?.(); return inp.checkValidity(); })
    .every(Boolean);

  next.addEventListener('click', () => {
    if (i === last) { count.textContent = 'Complete'; return; }
    if (!validate()) return;
    i++; paint();
  });
  back.addEventListener('click', () => { if (i > 0) { i--; paint(); } });
  paint();
})();
```

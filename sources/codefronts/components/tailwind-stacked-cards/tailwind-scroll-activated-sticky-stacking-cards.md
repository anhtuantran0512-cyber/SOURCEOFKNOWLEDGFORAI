---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-scroll-activated-sticky-stacking-cards/"
title: "Tailwind Scroll Activated Sticky Stacking Cards"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "The How-It-Works sequence: each step pins, and the one behind it scales down and dims as the next slides over."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll Activated Sticky Stacking Cards
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-scroll-activated-sticky-stacking-cards/

The How-It-Works sequence: each step pins, and the one behind it scales down and dims as the next slides over. An IntersectionObserver sets one data-state per card &mdash; ahead, live, behind &mdash; and every visual difference is a data-[state=…] variant, which is both cheaper than scroll maths and far easier to read.
## HTML
```html
<section class="stk-29 relative w-full min-h-svh bg-stk29-void font-stk29-sans text-white">
  <div class="pointer-events-none fixed -inset-[30%] z-0 blur-[30px] animate-stk29-drift motion-reduce:animate-none [background-image:radial-gradient(40%_40%_at_25%_25%,var(--color-stk29-aur1),transparent_70%),radial-gradient(45%_45%_at_75%_30%,var(--color-stk29-aur2),transparent_70%),radial-gradient(50%_50%_at_50%_80%,var(--color-stk29-aur3),transparent_70%)]" aria-hidden="true"></div>
  <div class="pointer-events-none fixed inset-0 z-0 mix-blend-overlay [background-image:repeating-linear-gradient(0deg,rgba(255,255,255,0.02)_0_1px,transparent_1px_3px)]" aria-hidden="true"></div>
  <div class="fixed right-6 top-1/2 z-5 flex -translate-y-1/2 flex-col gap-3.5" id="stk-29-rail" aria-hidden="true">
    <span class="block size-2 rounded-full bg-white/25 transition-all duration-400 data-[on=true]:h-6.5 data-[on=true]:rounded-md data-[on=true]:bg-white data-[on=true]:shadow-[0_0_14px_rgba(255,255,255,0.6)]" data-on="true"></span>
    <span class="block size-2 rounded-full bg-white/25 transition-all duration-400 data-[on=true]:h-6.5 data-[on=true]:rounded-md data-[on=true]:bg-white data-[on=true]:shadow-[0_0_14px_rgba(255,255,255,0.6)]"></span>
    <span class="block size-2 rounded-full bg-white/25 transition-all duration-400 data-[on=true]:h-6.5 data-[on=true]:rounded-md data-[on=true]:bg-white data-[on=true]:shadow-[0_0_14px_rgba(255,255,255,0.6)]"></span>
    <span class="block size-2 rounded-full bg-white/25 transition-all duration-400 data-[on=true]:h-6.5 data-[on=true]:rounded-md data-[on=true]:bg-white data-[on=true]:shadow-[0_0_14px_rgba(255,255,255,0.6)]"></span>
  </div>
  <p class="sr-only" id="stk-29-live" aria-live="polite"></p>
  <div class="relative z-1 mx-auto w-[min(460px,92vw)] pt-[55vh] pb-[75vh]" id="stk-29-steps">
    <section class="sticky top-[20vh] mb-9 flex h-80 flex-col justify-between overflow-hidden rounded-[28px] p-9.5 origin-top backdrop-blur-[6px] shadow-[0_40px_80px_rgba(0,0,0,0.55),inset_0_0_0_1px_rgba(255,255,255,0.08)] transition-[transform,filter] duration-500 ease-stk29 data-[state=behind]:scale-[0.94] data-[state=behind]:brightness-[0.7] data-[state=behind]:-translate-y-2 motion-reduce:transition-none motion-reduce:scale-100! motion-reduce:brightness-100!" data-state="live" data-label="Discover">
      <div class="absolute inset-0 -z-1 opacity-95 bg-[size:200%_200%] animate-stk29-flow motion-reduce:animate-none bg-linear-[135deg,var(--color-stk29-a1),var(--color-stk29-a2)_45%,var(--color-stk29-a3)]" aria-hidden="true"></div>
      <div class="absolute -top-1/2 -left-[30%] h-[200%] w-1/2 animate-stk29-sweep motion-reduce:animate-none [background-image:linear-gradient(90deg,transparent,rgba(255,255,255,0.35),transparent)]" aria-hidden="true"></div>
      <div class="flex items-center gap-3.5">
        <span class="font-stk29-serif text-[4rem] italic leading-[0.8] opacity-90 [text-shadow:0_4px_20px_rgba(0,0,0,0.3)]">01</span>
        <span class="ml-auto rounded-full border border-white/25 bg-white/18 px-3.5 py-1.75 text-[0.62rem] tracking-[0.22em] uppercase backdrop-blur-[6px]">Phase one</span>
      </div>
      <div>
        <h2 class="m-0 font-stk29-serif text-[2.4rem] tracking-[-0.01em]">Discover</h2>
        <p class="m-0 mt-1 max-w-[32ch] font-light leading-relaxed opacity-90">We map your goals and audit exactly where you stand today.</p>
        <div class="mt-4 h-1 overflow-hidden rounded bg-white/25"><i class="block h-full w-1/4 rounded bg-white transition-[width] duration-500"></i></div>
      </div>
    </section>
    <section class="sticky top-[20vh] mb-9 flex h-80 flex-col justify-between overflow-hidden rounded-[28px] p-9.5 origin-top backdrop-blur-[6px] shadow-[0_40px_80px_rgba(0,0,0,0.55),inset_0_0_0_1px_rgba(255,255,255,0.08)] transition-[transform,filter] duration-500 ease-stk29 data-[state=behind]:scale-[0.94] data-[state=behind]:brightness-[0.7] data-[state=behind]:-translate-y-2 motion-reduce:transition-none motion-reduce:scale-100! motion-reduce:brightness-100!" data-state="ahead" data-label="Design">
      <div class="absolute inset-0 -z-1 opacity-95 bg-[size:200%_200%] animate-stk29-flow motion-reduce:animate-none bg-linear-[135deg,var(--color-stk29-b1),var(--color-stk29-b2)_45%,var(--color-stk29-b3)]" aria-hidden="true"></div>
      <div class="absolute -top-1/2 -left-[30%] h-[200%] w-1/2 animate-stk29-sweep motion-reduce:animate-none [background-image:linear-gradient(90deg,transparent,rgba(255,255,255,0.35),transparent)]" aria-hidden="true"></div>
      <div class="flex items-center gap-3.5">
        <span class="font-stk29-serif text-[4rem] italic leading-[0.8] opacity-90 [text-shadow:0_4px_20px_rgba(0,0,0,0.3)]">02</span>
        <span class="ml-auto rounded-full border border-white/25 bg-white/18 px-3.5 py-1.75 text-[0.62rem] tracking-[0.22em] uppercase backdrop-blur-[6px]">Phase two</span>
      </div>
      <div>
        <h2 class="m-0 font-stk29-serif text-[2.4rem] tracking-[-0.01em]">Design</h2>
        <p class="m-0 mt-1 max-w-[32ch] font-light leading-relaxed opacity-90">Concepts take shape through rapid, collaborative iteration.</p>
        <div class="mt-4 h-1 overflow-hidden rounded bg-white/25"><i class="block h-full w-2/4 rounded bg-white transition-[width] duration-500"></i></div>
      </div>
    </section>
    <section class="sticky top-[20vh] mb-9 flex h-80 flex-col justify-between overflow-hidden rounded-[28px] p-9.5 origin-top backdrop-blur-[6px] shadow-[0_40px_80px_rgba(0,0,0,0.55),inset_0_0_0_1px_rgba(255,255,255,0.08)] transition-[transform,filter] duration-500 ease-stk29 data-[state=behind]:scale-[0.94] data-[state=behind]:brightness-[0.7] data-[state=behind]:-translate-y-2 motion-reduce:transition-none motion-reduce:scale-100! motion-reduce:brightness-100!" data-state="ahead" data-label="Build">
      <div class="absolute inset-0 -z-1 opacity-95 bg-[size:200%_200%] animate-stk29-flow motion-reduce:animate-none bg-linear-[135deg,var(--color-stk29-c1),var(--color-stk29-c2)_50%,var(--color-stk29-c3)]" aria-hidden="true"></div>
      <div class="absolute -top-1/2 -left-[30%] h-[200%] w-1/2 animate-stk29-sweep motion-reduce:animate-none [background-image:linear-gradient(90deg,transparent,rgba(255,255,255,0.35),transparent)]" aria-hidden="true"></div>
      <div class="flex items-center gap-3.5">
        <span class="font-stk29-serif text-[4rem] italic leading-[0.8] opacity-90 [text-shadow:0_4px_20px_rgba(0,0,0,0.3)]">03</span>
        <span class="ml-auto rounded-full border border-white/25 bg-white/18 px-3.5 py-1.75 text-[0.62rem] tracking-[0.22em] uppercase backdrop-blur-[6px]">Phase three</span>
      </div>
      <div>
        <h2 class="m-0 font-stk29-serif text-[2.4rem] tracking-[-0.01em]">Build</h2>
        <p class="m-0 mt-1 max-w-[32ch] font-light leading-relaxed opacity-90">Production-ready code, tested and shipped with real care.</p>
        <div class="mt-4 h-1 overflow-hidden rounded bg-white/25"><i class="block h-full w-3/4 rounded bg-white transition-[width] duration-500"></i></div>
      </div>
    </section>
    <section class="sticky top-[20vh] mb-9 flex h-80 flex-col justify-between overflow-hidden rounded-[28px] p-9.5 origin-top backdrop-blur-[6px] shadow-[0_40px_80px_rgba(0,0,0,0.55),inset_0_0_0_1px_rgba(255,255,255,0.08)] transition-[transform,filter] duration-500 ease-stk29 data-[state=behind]:scale-[0.94] data-[state=behind]:brightness-[0.7] data-[state=behind]:-translate-y-2 motion-reduce:transition-none motion-reduce:scale-100! motion-reduce:brightness-100!" data-state="ahead" data-label="Launch">
      <div class="absolute inset-0 -z-1 opacity-95 bg-[size:200%_200%] animate-stk29-flow motion-reduce:animate-none bg-linear-[135deg,var(--color-stk29-d1),var(--color-stk29-d2)_45%,var(--color-stk29-d3)]" aria-hidden="true"></div>
      <div class="absolute -top-1/2 -left-[30%] h-[200%] w-1/2 animate-stk29-sweep motion-reduce:animate-none [background-image:linear-gradient(90deg,transparent,rgba(255,255,255,0.35),transparent)]" aria-hidden="true"></div>
      <div class="flex items-center gap-3.5">
        <span class="font-stk29-serif text-[4rem] italic leading-[0.8] opacity-90 [text-shadow:0_4px_20px_rgba(0,0,0,0.3)]">04</span>
        <span class="ml-auto rounded-full border border-white/25 bg-white/18 px-3.5 py-1.75 text-[0.62rem] tracking-[0.22em] uppercase backdrop-blur-[6px]">Phase four</span>
      </div>
      <div>
        <h2 class="m-0 font-stk29-serif text-[2.4rem] tracking-[-0.01em]">Launch</h2>
        <p class="m-0 mt-1 max-w-[32ch] font-light leading-relaxed opacity-90">We go live, measure everything, then refine what works.</p>
        <div class="mt-4 h-1 overflow-hidden rounded bg-white/25"><i class="block h-full w-full rounded bg-white transition-[width] duration-500"></i></div>
      </div>
    </section>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk29-void: #05060a;
  --color-stk29-void: oklch(0.08 0.012 275);
  --color-stk29-aur1: rgba(99, 102, 241, 0.30);
  --color-stk29-aur2: rgba(236, 72, 153, 0.26);
  --color-stk29-aur3: rgba(45, 212, 191, 0.24);
  --color-stk29-a1: #1e1b4b;
  --color-stk29-a2: #4338ca;
  --color-stk29-a3: #6d28d9;
  --color-stk29-b1: #831843;
  --color-stk29-b2: #be185d;
  --color-stk29-b3: #f43f5e;
  --color-stk29-c1: #064e3b;
  --color-stk29-c2: #0d9488;
  --color-stk29-c3: #2dd4bf;
  --color-stk29-d1: #7c2d12;
  --color-stk29-d2: #ea580c;
  --color-stk29-d3: #f59e0b;
  --font-stk29-sans: 'Geist', system-ui, sans-serif;
  --font-stk29-serif: 'Instrument Serif', Georgia, serif;
  --ease-stk29: cubic-bezier(0.3, 0.9, 0.3, 1);
  --animate-stk29-flow: stk-29-flow 9s ease infinite;
  --animate-stk29-drift: stk-29-drift 20s ease-in-out infinite alternate;
  --animate-stk29-sweep: stk-29-sweep 6s ease-in-out infinite;
}

@keyframes stk-29-flow {
  0%,
    100% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }
}

@keyframes stk-29-drift {
  from {
    transform: translate(-3%, -2%) scale(1);
  }

  to {
    transform: translate(4%, 3%) scale(1.1);
  }
}

@keyframes stk-29-sweep {
  0%,
    100% {
    transform: rotate(18deg) translateX(-300px);
  }

  50% {
    transform: rotate(18deg) translateX(700px);
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.stk-29');
  if (!root) return;
  const steps = [...root.querySelectorAll('#stk-29-steps > section')];
  const pips = [...root.querySelectorAll('#stk-29-rail > span')];
  const live = root.querySelector('#stk-29-live');
  let current = -1;

  function setCurrent(i) {
    if (i === current) return;
    current = i;
    steps.forEach((s, n) => { s.dataset.state = n < i ? 'behind' : n === i ? 'live' : 'ahead'; });
    pips.forEach((p, n) => { if (n === i) p.dataset.on = 'true'; else delete p.dataset.on; });
    /* A pin is a visual event and nothing more — say which step it is. */
    live.textContent = 'Step ' + (i + 1) + ' of ' + steps.length + ': ' + steps[i].dataset.label;
  }

  /* An observer, not a scroll listener: nothing here runs per frame and no
     layout is read during scrolling. */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) setCurrent(steps.indexOf(e.target));
    });
  }, { rootMargin: '-20% 0px -60% 0px', threshold: 0 });

  steps.forEach((s) => io.observe(s));
  setCurrent(0);
})();
```

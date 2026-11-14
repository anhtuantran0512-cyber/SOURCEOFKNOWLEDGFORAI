---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-toast-notification/"
title: "Tailwind Liquid Glass Toast Notification"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "Frosted toasts sliding in from the top-right and stacking without turning to mush."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Toast Notification
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-toast-notification/

Frosted toasts sliding in from the top-right and stacking without turning to mush. The port's real content is the anti-pattern it avoids: each toast gets isolate so overlapping frosts never compound, and the type variants are data-type attributes styled by variants rather than three near-identical class strings in the script.
## HTML
```html
<section id="lgt-14-root" class="lgt-14 relative grid w-full min-h-svh place-items-center overflow-hidden bg-lgt14-bg font-lgt14-sans" aria-label="Tailwind liquid glass toast notifications">
  <img src="https://picsum.photos/seed/lgtoast/1100/750" width="1100" height="750" alt="Dashboard backdrop" class="absolute inset-0 size-full object-cover">

  <div class="relative z-1 flex flex-wrap justify-center gap-3">
    <button type="button" data-spawn="success" class="cursor-pointer rounded-full border border-white/35 bg-white/14 px-5 py-3 text-sm font-bold text-white backdrop-blur-[14px] backdrop-saturate-160 transition-transform duration-150 hover:-translate-y-0.5 focus-visible:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Success toast</button>
    <button type="button" data-spawn="info" class="cursor-pointer rounded-full border border-white/35 bg-white/14 px-5 py-3 text-sm font-bold text-white backdrop-blur-[14px] backdrop-saturate-160 transition-transform duration-150 hover:-translate-y-0.5 focus-visible:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Info toast</button>
    <button type="button" data-spawn="error" class="cursor-pointer rounded-full border border-white/35 bg-white/14 px-5 py-3 text-sm font-bold text-white backdrop-blur-[14px] backdrop-saturate-160 transition-transform duration-150 hover:-translate-y-0.5 focus-visible:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Error toast</button>
  </div>

  <div id="lgt-14-region" role="region" aria-label="Notifications" aria-live="polite" class="pointer-events-none absolute top-5 right-5 z-50 flex w-[min(320px,86vw)] flex-col gap-3"></div>

  <template id="lgt-14-tpl">
    <div class="pointer-events-auto relative isolate flex items-start gap-3 overflow-hidden rounded-[16px] border border-white/30 bg-white/14 py-3.5 pr-10 pl-3.5 text-white backdrop-blur-[20px] backdrop-saturate-180 shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_20px_40px_-20px_rgba(0,0,0,.7)] animate-lgt14-in data-closing:animate-lgt14-out motion-reduce:animate-none after:absolute after:bottom-0 after:left-0 after:h-0.75 after:w-full after:origin-left after:bg-white/70 after:[animation:lgt-14-rim_var(--life,4000ms)_linear_forwards] motion-reduce:after:hidden">
      <span data-slot="ico" class="grid size-6.5 flex-none place-items-center rounded-full text-sm font-black text-white data-[type=success]:bg-lgt14-ok data-[type=info]:bg-lgt14-info data-[type=error]:bg-lgt14-err"></span>
      <div class="text-sm leading-snug"><strong data-slot="title" class="mb-0.5 block font-extrabold"></strong><span data-slot="body"></span></div>
      <button type="button" data-slot="close" aria-label="Dismiss" class="absolute top-2 right-2 grid size-6 cursor-pointer place-items-center rounded-full border-0 bg-white/16 text-[13px] text-white hover:bg-white/30 focus-visible:bg-white/30 focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-white">&#10005;</button>
    </div>
  </template>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt14-bg: #0e0b1a;
  --color-lgt14-ok: #34c48a;
  --color-lgt14-ok: oklch(0.72 0.16 160);
  --color-lgt14-info: #5b8def;
  --color-lgt14-info: oklch(0.7 0.16 250);
  --color-lgt14-err: #e2503c;
  --color-lgt14-err: oklch(0.65 0.2 25);
  --font-lgt14-sans: 'Manrope', system-ui, sans-serif;
  --animate-lgt14-in: lgt-14-in 0.4s cubic-bezier(0.2, 0.9, 0.2, 1);
  --animate-lgt14-out: lgt-14-out 0.3s ease forwards;
}

@keyframes lgt-14-in {
  from {
    opacity: 0;
    transform: translateX(110%);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes lgt-14-out {
  to {
    opacity: 0;
    transform: translateX(110%);
  }
}

@keyframes lgt-14-rim {
  from {
    transform: scaleX(1);
  }

  to {
    transform: scaleX(0);
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lgt-14-root');
  const region = root.querySelector('#lgt-14-region');
  const tpl = root.querySelector('#lgt-14-tpl');
  const LIFE = 4000;
  const copy = {
    success: { ico: '✓', title: 'Saved', body: 'Your changes are live.' },
    info:    { ico: 'i', title: 'Heads up', body: 'A new version is available.' },
    error:   { ico: '!', title: 'Upload failed', body: 'Check your connection and retry.' }
  };

  const toast = type => {
    const c = copy[type] || copy.info;
    const el = tpl.content.firstElementChild.cloneNode(true);
    el.style.setProperty('--life', LIFE + 'ms');
    const ico = el.querySelector('[data-slot="ico"]');
    ico.dataset.type = type;
    ico.textContent = c.ico;
    el.querySelector('[data-slot="title"]').textContent = c.title;
    el.querySelector('[data-slot="body"]').textContent = c.body;
    region.appendChild(el);

    const kill = () => {
      el.dataset.closing = '';
      el.addEventListener('animationend', () => el.remove(), { once: true });
      setTimeout(() => el.remove(), 400);
    };
    const t = setTimeout(kill, LIFE);
    el.querySelector('[data-slot="close"]').addEventListener('click', () => { clearTimeout(t); kill(); });
  };

  root.querySelectorAll('[data-spawn]').forEach(b => b.addEventListener('click', () => toast(b.dataset.spawn)));
})();
```

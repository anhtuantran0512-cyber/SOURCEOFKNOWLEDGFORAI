---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-hold-to-confirm-button-group/"
title: "Tailwind Hold-to-Confirm Button Group with Gradient Progress (Press and Hold)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A publish bar where the primary action is press-and-hold: holding fills the button left-to-right (an @property width animated on active:after:), letting go…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hold-to-Confirm Button Group with Gradient Progress (Press and Hold)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-hold-to-confirm-button-group/

A publish bar where the primary action is press-and-hold: holding fills the button left-to-right (an @property width animated on active:after:), letting go early cancels, and completing it flips the button to a green Published state via data-done:. The CSS original drew the fill but nothing ever happened; a 20-line listener on animationend now makes it a real confirmation pattern.
## HTML
```html
<section class="tbg-18 w-full min-h-svh grid place-items-center bg-tbg18-bg bg-[radial-gradient(120%_120%_at_80%_0%,var(--color-tbg18-glow),transparent_70%)] px-5 py-14 font-tbg18-sans text-tbg18-ink" aria-label="Hold to confirm button group demo">
  <div class="grid w-full max-w-[36rem] gap-3.5">
    <p class="ml-0.5 text-xs font-bold uppercase tracking-[0.16em] text-tbg18-acc">Ready to ship</p>
    <div role="group" aria-label="Publish actions" class="flex flex-wrap gap-3">
      <button type="button" data-tbg18-hold class="group relative isolate inline-flex h-14 min-w-52 cursor-pointer items-center justify-center gap-2.5 overflow-hidden rounded-2xl bg-[linear-gradient(90deg,#4d7cff,#c04dff,#ff5db8,#4d7cff)] bg-size-[250%_100%] px-7 text-base font-extrabold text-tbg18-on shadow-tbg18-lift select-none animate-tbg18-flow after:absolute after:inset-y-0 after:left-0 after:-z-1 after:w-(--tbg18-p) after:border-r-2 after:border-white/70 after:bg-white/30 after:content-[''] hover:brightness-108 active:after:animate-tbg18-fill data-done:animate-none data-done:bg-tbg18-ok data-done:after:hidden focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg18-acc motion-reduce:animate-none">
        <svg class="group-data-done:hidden" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
        <svg class="hidden group-data-done:block" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>
        <span class="group-data-done:hidden">Hold to publish</span><span class="hidden group-data-done:inline">Published</span>
      </button>
      <button type="button" class="h-14 cursor-pointer rounded-2xl border-[1.5px] border-tbg18-line bg-white/3 px-6 text-[15px] font-bold text-tbg18-soft transition-[border-color,background-color] duration-200 hover:border-tbg18-hover hover:bg-white/6 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg18-acc">Save draft</button>
      <button type="button" class="inline-flex h-14 cursor-pointer items-center gap-2 rounded-2xl border-[1.5px] border-tbg18-line bg-white/3 px-6 text-[15px] font-bold text-tbg18-soft transition-[border-color,background-color] duration-200 hover:border-tbg18-hover hover:bg-white/6 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg18-acc"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M10 13a4 4 0 0 0 5.7.6l2.6-2.6a4 4 0 0 0-5.6-5.7l-1.5 1.5M14 11a4 4 0 0 0-5.7-.6L5.7 13a4 4 0 0 0 5.6 5.7l1.5-1.5"/></svg>Share link</button>
    </div>
    <p class="ml-0.5 text-[13px] text-tbg18-mut">Press and hold for 1.4 s to publish. Let go to cancel.</p>
    <span role="status" aria-live="polite" class="sr-only" data-tbg18-status></span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* @property is an at-rule with no utility: it makes the fill width animatable. */

@property --tbg18-p {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 0%;
}

@theme {
  --color-tbg18-bg: #080a14;
  --color-tbg18-glow: #161c31;
  --color-tbg18-ink: #eef1ff;
  --color-tbg18-soft: #ccd5f2;
  --color-tbg18-mut: #9aa6cc;
  --color-tbg18-mut: oklch(0.74 0.05 270);
  --color-tbg18-line: #2b3452;
  --color-tbg18-hover: #4a5a88;
  --color-tbg18-on: #0a0e1c;
  --color-tbg18-acc: #8ea0ff;
  --color-tbg18-ok: #4ade80;
  --color-tbg18-ok: oklch(0.8 0.18 150);
  --shadow-tbg18-lift: 0 14px 34px -14px rgb(120 90 255 / 0.8);
  --font-tbg18-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-tbg18-flow: tbg18-flow 4s linear infinite;
  --animate-tbg18-fill: tbg18-fill 1.4s cubic-bezier(0.4, 0, 0.2, 1) forwards;

  @keyframes tbg18-flow {
    to {
      background-position: 250% 0;
    }
  }

  @keyframes tbg18-fill {
    from {
      --tbg18-p: 0%;
    }

    to {
      --tbg18-p: 100%;
    }
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-18 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tbg18-hold]').forEach((btn) => {
    if (btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const status = btn.closest('section').querySelector('[data-tbg18-status]');
    let t = 0;
    btn.addEventListener('touchstart', () => {}, { passive: true });
    btn.addEventListener('animationend', (e) => {
      if (e.animationName !== 'tbg18-fill' || btn.hasAttribute('data-done')) return;
      btn.setAttribute('data-done', '');
      status.textContent = 'Published';
      clearTimeout(t);
      t = setTimeout(() => { btn.removeAttribute('data-done'); status.textContent = ''; }, 2600);
    });
  });
})();
```

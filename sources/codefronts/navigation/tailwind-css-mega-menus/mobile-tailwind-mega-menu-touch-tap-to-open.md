---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/mobile-tailwind-mega-menu-touch-tap-to-open/"
title: "Mobile Tailwind Mega Menu for Touch Devices (Tap to Open)"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "Hover does not exist on a phone, and emulated hover is how mega menus end up needing a double tap on iOS."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile Tailwind Mega Menu for Touch Devices (Tap to Open)
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/mobile-tailwind-mega-menu-touch-tap-to-open/

Hover does not exist on a phone, and emulated hover is how mega menus end up needing a double tap on iOS. This mobile storefront drops hover entirely below a fine pointer: one tap toggles a panel, a second tap closes it, and only one panel is open at a time. Panels slide open with an animated grid-rows-[0fr] &rarr; grid-rows-[1fr] transition instead of snapping from display: none.
## HTML
```html
<section class="tmm-10 relative w-full min-h-svh bg-tmm10-bg bg-[radial-gradient(70rem_34rem_at_12%_-10%,color-mix(in_oklab,var(--color-tmm10-acc2)_18%,transparent),transparent_62%),radial-gradient(50rem_28rem_at_95%_8%,color-mix(in_oklab,var(--color-tmm10-acc)_16%,transparent),transparent_60%)] font-tmm10-sans leading-[1.55] text-tmm10-ink [&_:focus-visible]:rounded-xl [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm10-acc" aria-labelledby="tmm10-title">
  <h2 class="sr-only" id="tmm10-title">Nova</h2>

  <div class="absolute top-3 right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm10-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmm10-line bg-tmm10-surf text-tmm10-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm10-acc" for="tmm10-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <div class="grid min-h-svh place-items-center px-[clamp(0.75rem,4vw,2rem)] py-[clamp(3.5rem,9vw,5rem)]">
    <div class="w-[min(23rem,100%)] overflow-hidden rounded-[34px] border border-tmm10-line bg-tmm10-surf shadow-tmm10-device ring-8 ring-tmm10-ink/5">
      <div class="flex items-center justify-between px-5 pt-2.5 pb-1 font-tmm10-display text-[0.76rem]/none font-bold text-tmm10-mut" aria-hidden="true"><span>9:41</span><span class="h-1.5 w-10 rounded-full bg-tmm10-ink/18"></span></div>
      <header class="relative z-5">
        <div class="flex items-center justify-between gap-2 px-3 py-1.5">
          <span class="grid size-11 place-items-center text-tmm10-ink" aria-hidden="true"><svg class="size-5" viewBox="0 0 24 24" focusable="false"><path d="M4 7h16M4 12h16M4 17h10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
          <a class="font-tmm10-display text-[1.1rem]/none font-extrabold tracking-[0.16em] text-tmm10-acc" href="#tmm10-title">NOVA</a>
          <span class="relative grid size-11 place-items-center text-tmm10-ink" aria-hidden="true"><svg class="size-5" viewBox="0 0 24 24" focusable="false"><path d="M5 8h14l-1.2 11H6.2Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 8a3 3 0 0 1 6 0" fill="none" stroke="currentColor" stroke-width="1.7"/></svg><span class="absolute top-2 right-2 size-2 rounded-full bg-tmm10-acc ring-2 ring-tmm10-surf"></span></span>
        </div>
        <nav data-tmm10-nav class="px-3 pt-1 pb-3" aria-label="Primary">
          <ul class="grid gap-1.5">
            <li data-tmm10-item class="relative min-w-0">
              <button data-tmm10-tap type="button" aria-expanded="false" aria-controls="tmm10-panel-shop" class="flex min-h-12 w-full cursor-pointer touch-manipulation items-center justify-between gap-2 rounded-2xl border border-tmm10-line bg-tmm10-surf px-3.5 font-tmm10-display text-[0.98rem]/none font-bold text-tmm10-ink transition-colors select-none active:scale-[0.99] tmm10-open:border-[color-mix(in_oklab,var(--color-tmm10-acc)_40%,var(--color-tmm10-line))] tmm10-open:bg-[color-mix(in_oklab,var(--color-tmm10-acc)_12%,var(--color-tmm10-surf))] tmm10-open:text-tmm10-acc">Shop
                <svg class="size-[18px] transition-transform duration-200 tmm10-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
              </button>
              <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-300 ease-tmm10-out tmm10-open:grid-rows-[1fr] motion-reduce:transition-none" id="tmm10-panel-shop" aria-label="Shop">
                <div class="invisible min-h-0 overflow-hidden tmm10-open:visible">
                  <div class="mt-1.5 rounded-2xl bg-[color-mix(in_oklab,var(--color-tmm10-acc2)_9%,var(--color-tmm10-surf))] p-2">
                    <a class="grid min-h-[54px] content-center gap-px rounded-xl bg-tmm10-acc px-3 py-1.5 text-tmm10-on-acc" href="#tmm10-title"><b class="flex items-center justify-between font-tmm10-display text-[0.94rem]/tight font-bold">Shop all<span aria-hidden="true">&rarr;</span></b><span class="text-[0.74rem] opacity-90">420 styles in stock</span></a>
                    <ul class="mt-1.5 grid gap-0.5">
                      <li><a href="#tmm10-title" class="flex min-h-12 items-center justify-between gap-2 rounded-xl px-3 text-[0.92rem] text-tmm10-ink transition-colors hover:bg-tmm10-acc/12 active:bg-tmm10-acc/16">Running<span class="rounded-full text-tmm10-mut font-tmm10-display text-[0.72rem]/none font-bold">128</span></a></li>
                      <li><a href="#tmm10-title" class="flex min-h-12 items-center justify-between gap-2 rounded-xl px-3 text-[0.92rem] text-tmm10-ink transition-colors hover:bg-tmm10-acc/12 active:bg-tmm10-acc/16">Trail<span class="rounded-full text-tmm10-mut font-tmm10-display text-[0.72rem]/none font-bold">64</span></a></li>
                      <li><a href="#tmm10-title" class="flex min-h-12 items-center justify-between gap-2 rounded-xl px-3 text-[0.92rem] text-tmm10-ink transition-colors hover:bg-tmm10-acc/12 active:bg-tmm10-acc/16">Recovery<span class="rounded-full text-tmm10-mut font-tmm10-display text-[0.72rem]/none font-bold">31</span></a></li>
                      <li><a href="#tmm10-title" class="flex min-h-12 items-center justify-between gap-2 rounded-xl px-3 text-[0.92rem] text-tmm10-ink transition-colors hover:bg-tmm10-acc/12 active:bg-tmm10-acc/16">Accessories<span class="rounded-full text-tmm10-mut font-tmm10-display text-[0.72rem]/none font-bold">92</span></a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </li>
            <li data-tmm10-item class="relative min-w-0">
              <button data-tmm10-tap type="button" aria-expanded="false" aria-controls="tmm10-panel-collections" class="flex min-h-12 w-full cursor-pointer touch-manipulation items-center justify-between gap-2 rounded-2xl border border-tmm10-line bg-tmm10-surf px-3.5 font-tmm10-display text-[0.98rem]/none font-bold text-tmm10-ink transition-colors select-none active:scale-[0.99] tmm10-open:border-[color-mix(in_oklab,var(--color-tmm10-acc)_40%,var(--color-tmm10-line))] tmm10-open:bg-[color-mix(in_oklab,var(--color-tmm10-acc)_12%,var(--color-tmm10-surf))] tmm10-open:text-tmm10-acc">Collections
                <svg class="size-[18px] transition-transform duration-200 tmm10-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
              </button>
              <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-300 ease-tmm10-out tmm10-open:grid-rows-[1fr] motion-reduce:transition-none" id="tmm10-panel-collections" aria-label="Collections">
                <div class="invisible min-h-0 overflow-hidden tmm10-open:visible">
                  <div class="mt-1.5 rounded-2xl bg-[color-mix(in_oklab,var(--color-tmm10-acc2)_9%,var(--color-tmm10-surf))] p-2">
                    <a class="grid min-h-[54px] content-center gap-px rounded-xl bg-tmm10-acc px-3 py-1.5 text-tmm10-on-acc" href="#tmm10-title"><b class="flex items-center justify-between font-tmm10-display text-[0.94rem]/tight font-bold">All collections<span aria-hidden="true">&rarr;</span></b><span class="text-[0.74rem] opacity-90">Seasonal drops</span></a>
                    <ul class="mt-1.5 grid gap-0.5">
                      <li><a href="#tmm10-title" class="flex min-h-12 items-center justify-between gap-2 rounded-xl px-3 text-[0.92rem] text-tmm10-ink transition-colors hover:bg-tmm10-acc/12 active:bg-tmm10-acc/16">Winter series<span class="rounded-full bg-tmm10-acc2 px-2 py-1 text-tmm10-on-acc font-tmm10-display text-[0.72rem]/none font-bold">new</span></a></li>
                      <li><a href="#tmm10-title" class="flex min-h-12 items-center justify-between gap-2 rounded-xl px-3 text-[0.92rem] text-tmm10-ink transition-colors hover:bg-tmm10-acc/12 active:bg-tmm10-acc/16">Long distance<span class="rounded-full text-tmm10-mut font-tmm10-display text-[0.72rem]/none font-bold">24</span></a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </li>
            <li data-tmm10-item class="relative min-w-0">
              <button data-tmm10-tap type="button" aria-expanded="false" aria-controls="tmm10-panel-stories" class="flex min-h-12 w-full cursor-pointer touch-manipulation items-center justify-between gap-2 rounded-2xl border border-tmm10-line bg-tmm10-surf px-3.5 font-tmm10-display text-[0.98rem]/none font-bold text-tmm10-ink transition-colors select-none active:scale-[0.99] tmm10-open:border-[color-mix(in_oklab,var(--color-tmm10-acc)_40%,var(--color-tmm10-line))] tmm10-open:bg-[color-mix(in_oklab,var(--color-tmm10-acc)_12%,var(--color-tmm10-surf))] tmm10-open:text-tmm10-acc">Stories
                <svg class="size-[18px] transition-transform duration-200 tmm10-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
              </button>
              <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-300 ease-tmm10-out tmm10-open:grid-rows-[1fr] motion-reduce:transition-none" id="tmm10-panel-stories" aria-label="Stories">
                <div class="invisible min-h-0 overflow-hidden tmm10-open:visible">
                  <div class="mt-1.5 rounded-2xl bg-[color-mix(in_oklab,var(--color-tmm10-acc2)_9%,var(--color-tmm10-surf))] p-2">
                    <a class="grid min-h-[54px] content-center gap-px rounded-xl bg-tmm10-acc px-3 py-1.5 text-tmm10-on-acc" href="#tmm10-title"><b class="flex items-center justify-between font-tmm10-display text-[0.94rem]/tight font-bold">All stories<span aria-hidden="true">&rarr;</span></b><span class="text-[0.74rem] opacity-90">Athlete diaries and field tests</span></a>
                    <ul class="mt-1.5 grid gap-0.5">
                      <li><a href="#tmm10-title" class="flex min-h-12 items-center justify-between gap-2 rounded-xl px-3 text-[0.92rem] text-tmm10-ink transition-colors hover:bg-tmm10-acc/12 active:bg-tmm10-acc/16">Athlete diaries<span class="rounded-full text-tmm10-mut font-tmm10-display text-[0.72rem]/none font-bold">12</span></a></li>
                      <li><a href="#tmm10-title" class="flex min-h-12 items-center justify-between gap-2 rounded-xl px-3 text-[0.92rem] text-tmm10-ink transition-colors hover:bg-tmm10-acc/12 active:bg-tmm10-acc/16">Field testing<span class="rounded-full text-tmm10-mut font-tmm10-display text-[0.72rem]/none font-bold">7</span></a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </nav>
      </header>
      <main class="grid gap-2.5 px-3 pt-1 pb-4">
        <p class="grid min-h-[34px] place-items-center rounded-full bg-tmm10-acc2/16 font-tmm10-display text-[0.74rem]/none font-bold tracking-[0.08em] text-tmm10-acc2 uppercase">Free returns for 60 days</p>
        <div class="grid gap-0.5 rounded-[20px] bg-[linear-gradient(150deg,color-mix(in_oklab,var(--color-tmm10-acc)_22%,transparent),color-mix(in_oklab,var(--color-tmm10-acc2)_20%,transparent))] px-5 py-4.5">
          <p class="font-tmm10-display text-[0.7rem]/none font-bold tracking-[0.18em] text-tmm10-acc uppercase">New in</p>
          <p class="font-tmm10-display text-2xl/tight font-extrabold tracking-[-0.02em]">Nova Drift 3</p>
          <p class="text-[0.86rem] text-tmm10-mut">&pound;135 &middot; four colourways</p>
        </div>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm10-bg: #fdf2f8;
  --color-tmm10-bg: oklch(0.97 0.015 345);
  --color-tmm10-surf: #ffffff;
  --color-tmm10-surf: oklch(1 0 0);
  --color-tmm10-line: #f3d8e6;
  --color-tmm10-line: oklch(0.91 0.035 345);
  --color-tmm10-ink: #2c1a26;
  --color-tmm10-ink: oklch(0.25 0.035 345);
  --color-tmm10-mut: #735868;
  --color-tmm10-mut: oklch(0.5 0.04 345);
  --color-tmm10-acc: #be185d;
  --color-tmm10-acc: oklch(0.52 0.2 355);
  --color-tmm10-acc2: #7c3aed;
  --color-tmm10-acc2: oklch(0.52 0.24 295);
  --color-tmm10-on-acc: #ffffff;
  --color-tmm10-on-acc: oklch(1 0 0);
  --font-tmm10-display: 'Quicksand', ui-rounded, system-ui, sans-serif;
  --font-tmm10-sans: 'Figtree', system-ui, sans-serif;
  --shadow-tmm10-device: 0 40px 90px -44px rgb(44 26 38 / 0.7);
  --ease-tmm10-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-10 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-10:has(#tmm10-theme:checked) {
  --color-tmm10-bg: #150d13;
  --color-tmm10-bg: oklch(0.17 0.02 345);
  --color-tmm10-surf: #1f1520;
  --color-tmm10-surf: oklch(0.21 0.025 340);
  --color-tmm10-line: #3a2733;
  --color-tmm10-line: oklch(0.31 0.035 345);
  --color-tmm10-ink: #fbeef5;
  --color-tmm10-ink: oklch(0.96 0.015 345);
  --color-tmm10-mut: #bb9aad;
  --color-tmm10-mut: oklch(0.74 0.045 345);
  --color-tmm10-acc: #f9a8d4;
  --color-tmm10-acc: oklch(0.8 0.13 350);
  --color-tmm10-acc2: #c4b5fd;
  --color-tmm10-acc2: oklch(0.81 0.1 295);
  --color-tmm10-on-acc: #24101c;
  --color-tmm10-on-acc: oklch(0.2 0.04 345);
}

@media (prefers-color-scheme: dark) {
  .tmm-10 {
    --color-tmm10-bg: #150d13;
    --color-tmm10-bg: oklch(0.17 0.02 345);
    --color-tmm10-surf: #1f1520;
    --color-tmm10-surf: oklch(0.21 0.025 340);
    --color-tmm10-line: #3a2733;
    --color-tmm10-line: oklch(0.31 0.035 345);
    --color-tmm10-ink: #fbeef5;
    --color-tmm10-ink: oklch(0.96 0.015 345);
    --color-tmm10-mut: #bb9aad;
    --color-tmm10-mut: oklch(0.74 0.045 345);
    --color-tmm10-acc: #f9a8d4;
    --color-tmm10-acc: oklch(0.8 0.13 350);
    --color-tmm10-acc2: #c4b5fd;
    --color-tmm10-acc2: oklch(0.81 0.1 295);
    --color-tmm10-on-acc: #24101c;
    --color-tmm10-on-acc: oklch(0.2 0.04 345);
  }

  .tmm-10:has(#tmm10-theme:checked) {
    --color-tmm10-bg: #fdf2f8;
    --color-tmm10-bg: oklch(0.97 0.015 345);
    --color-tmm10-surf: #ffffff;
    --color-tmm10-surf: oklch(1 0 0);
    --color-tmm10-line: #f3d8e6;
    --color-tmm10-line: oklch(0.91 0.035 345);
    --color-tmm10-ink: #2c1a26;
    --color-tmm10-ink: oklch(0.25 0.035 345);
    --color-tmm10-mut: #735868;
    --color-tmm10-mut: oklch(0.5 0.04 345);
    --color-tmm10-acc: #be185d;
    --color-tmm10-acc: oklch(0.52 0.2 355);
    --color-tmm10-acc2: #7c3aed;
    --color-tmm10-acc2: oklch(0.52 0.24 295);
    --color-tmm10-on-acc: #ffffff;
    --color-tmm10-on-acc: oklch(1 0 0);
  }
}
/* Hover only opens for a fine pointer; touch relies on the scripted [data-open]. */

@custom-variant tmm10-open {
  &:where([data-tmm10-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) and (pointer: fine) {
    &:where([data-tmm10-item]:hover *) {
      @slot;
    }
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tmm-10');
  if (!root || root.__tmmCleanup) return;
  const nav = root.querySelector('[data-tmm10-nav]');

  const setOpen = (item, on) => {
    item.toggleAttribute('data-open', on);
    item.querySelector('[data-tmm10-tap]').setAttribute('aria-expanded', String(on));
  };
  const toggle = (item) => {
    const open = item.hasAttribute('data-open');
    nav.querySelectorAll('[data-tmm10-item][data-open]').forEach((i) => setOpen(i, false));
    setOpen(item, !open);
  };

  // Touch: act on pointerdown and suppress the focus, so a tapped trigger never sticks open
  // through :focus-within. The follow-up click is swallowed so the tap cannot toggle twice.
  let swallow = false;
  const onPointerDown = (e) => {
    const t = e.target.closest('[data-tmm10-tap]');
    if (!t || e.pointerType === 'mouse') return;
    e.preventDefault();
    swallow = true;
    toggle(t.closest('[data-tmm10-item]'));
  };
  const onClick = (e) => {
    const t = e.target.closest('[data-tmm10-tap]');
    if (!t) return;
    if (swallow) { swallow = false; return; }
    toggle(t.closest('[data-tmm10-item]'));
  };
  const onKey = (e) => {
    if (e.key !== 'Escape') return;
    const item = e.target.closest('[data-tmm10-item]');
    if (!item) return;
    setOpen(item, false);
    item.querySelector('[data-tmm10-tap]').focus();
  };

  nav.addEventListener('pointerdown', onPointerDown);
  nav.addEventListener('click', onClick);
  nav.addEventListener('keydown', onKey);
  root.__tmmCleanup = () => {
    nav.removeEventListener('pointerdown', onPointerDown);
    nav.removeEventListener('click', onClick);
    nav.removeEventListener('keydown', onKey);
  };
})();
```

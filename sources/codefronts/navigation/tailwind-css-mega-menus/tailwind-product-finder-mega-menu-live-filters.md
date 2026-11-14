---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-product-finder-mega-menu-live-filters/"
title: "Tailwind Product Finder Mega Menu with Live Filters"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "The mega panel as a product finder: grouped <fieldset> facets, a budget slider and a live result count announced through role=\"status\"."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Product Finder Mega Menu with Live Filters
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-product-finder-mega-menu-live-filters/

The mega panel as a product finder: grouped <fieldset> facets, a budget slider and a live result count announced through role="status". Checkbox rows become selectable chips with Tailwind's has-checked: variant &mdash; no custom checkbox markup. A badge on the trigger shows how many filters are active even when the panel is closed, and Clear filters resets everything in one tap.
## HTML
```html
<section class="tmm-19 relative w-full min-h-svh bg-tmm19-bg font-tmm19-sans leading-normal text-tmm19-ink accent-tmm19-acc [&_:focus-visible]:rounded-sm [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm19-acc" aria-labelledby="tmm19-title">
  <h2 class="sr-only" id="tmm19-title">Ranger Outfitters</h2>

  <div class="absolute top-3 right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm19-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-none border border-tmm19-line bg-tmm19-surf text-tmm19-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm19-acc" for="tmm19-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b border-tmm19-line bg-tmm19-surf">
    <div class="mx-auto flex min-h-17 w-[min(76rem,calc(100%-2rem))] flex-wrap items-stretch gap-x-[clamp(0.5rem,2vw,2rem)] pr-15 max-[52rem]:flex-col max-[52rem]:py-2.5">
      <a class="grid content-center font-tmm19-display text-base/none font-bold tracking-[0.06em] text-tmm19-ink" href="#tmm19-title">RANGER<span class="mt-0.5 font-tmm19-sans text-[0.6rem]/[1.2] font-normal tracking-[0.26em] text-tmm19-mut uppercase">outfitters</span></a>
      <nav class="flex min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-1 max-[52rem]:flex-col">
          <li data-tmm19-item class="flex items-stretch max-[52rem]:block">
            <button data-tmm19-trigger type="button" id="tmm19-trigger-find" aria-expanded="false" aria-controls="tmm19-panel-find" class="inline-flex min-h-11 cursor-pointer items-center gap-2 px-3.5 text-[0.92rem]/none font-semibold text-tmm19-ink transition-colors hover:text-tmm19-acc tmm19-open:bg-tmm19-acc tmm19-open:text-tmm19-on-acc!"><svg class="size-4" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16M7 12h10M10 18h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Find your kit<span data-tmm19-badge class="grid min-w-5 place-items-center rounded-full bg-tmm19-acc px-1 text-[0.68rem] text-tmm19-on-acc tmm19-open:bg-tmm19-on-acc tmm19-open:text-tmm19-acc">2</span></button>
            <div data-tmm19-panel class="invisible absolute top-full left-1/2 z-30 grid w-[min(58rem,calc(100vw-2rem))] -translate-x-1/2 -translate-y-1.5 border border-t-0 border-tmm19-line bg-tmm19-surf opacity-0 shadow-tmm19-panel pointer-events-none transition-[opacity,translate,visibility] duration-160 min-[62rem]:grid-cols-[minmax(0,1fr)_17rem] tmm19-open:visible tmm19-open:translate-y-0 tmm19-open:opacity-100 tmm19-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:w-full max-[52rem]:translate-x-0 max-[52rem]:translate-y-0 max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:tmm19-open:grid" id="tmm19-panel-find" aria-labelledby="tmm19-trigger-find">
              <div class="translate-y-2.5 opacity-0 transition-[opacity,translate] duration-[200ms,340ms] ease-tmm19-out delay-20 tmm19-open:translate-y-0 tmm19-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none grid min-w-0 grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[clamp(0.75rem,2.4vw,1.5rem)] p-[clamp(0.9rem,2.6vw,1.4rem)]">
                <fieldset class="grid min-w-0 content-start gap-0.5">
                  <legend class="pb-1.5 font-tmm19-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm19-mut uppercase">Activity</legend>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter checked> Trail running</label>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter> Alpine</label>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter> Bikepacking</label>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter> Sea kayak</label>
                </fieldset>
                <fieldset class="grid min-w-0 content-start gap-0.5">
                  <legend class="pb-1.5 font-tmm19-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm19-mut uppercase">Season</legend>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter> Three season</label>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter checked> Winter</label>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter> Expedition</label>
                </fieldset>
                <fieldset class="grid min-w-0 content-start gap-0.5">
                  <legend class="pb-1.5 font-tmm19-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm19-mut uppercase">Weight class</legend>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter> Ultralight</label>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter> Standard</label>
                  <label class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-lg border border-transparent px-2 text-[0.9rem] transition-colors hover:bg-tmm19-ink/4 has-checked:border-tmm19-acc/40 has-checked:bg-tmm19-acc/10 has-checked:font-semibold has-focus-visible:outline-2 has-focus-visible:outline-tmm19-acc"><input class="size-[18px] flex-none accent-tmm19-acc focus-visible:outline-none" type="checkbox" data-tmm19-filter> Heavy duty</label>
                </fieldset>
                <fieldset class="grid min-w-0 content-start gap-1">
                  <legend class="pb-1.5 font-tmm19-display text-[0.72rem]/none font-bold tracking-[0.16em] text-tmm19-mut uppercase">Budget ceiling</legend>
                  <label class="flex min-h-8 items-center gap-1.5 text-[0.86rem] text-tmm19-mut" for="tmm19-price">up to <b data-tmm19-price class="text-[0.98rem] text-tmm19-acc tabular-nums">&pound;420</b></label>
                  <input class="min-h-11 w-full" type="range" id="tmm19-price" min="80" max="900" step="20" value="420" data-tmm19-filter>
                  <p class="text-[0.76rem] text-tmm19-mut text-pretty">Includes 2-year repair cover on every item.</p>
                </fieldset>
              </div>
              <div class="translate-y-2.5 opacity-0 transition-[opacity,translate] duration-[200ms,340ms] ease-tmm19-out delay-110 tmm19-open:translate-y-0 tmm19-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none grid min-w-0 content-start gap-2.5 border-l border-tmm19-line bg-tmm19-acc/8 p-[clamp(0.9rem,2.6vw,1.4rem)] max-[62rem]:border-t max-[62rem]:border-l-0">
                <p class="text-[0.9rem] text-tmm19-mut" role="status" aria-live="polite"><b data-tmm19-count class="block font-tmm19-display text-[clamp(1.6rem,5vw,2.2rem)]/none text-tmm19-ink tabular-nums">168</b> products match</p>
                <button type="button" class="inline-flex min-h-11 cursor-pointer items-center justify-center gap-2 bg-tmm19-acc px-4.5 text-[0.88rem]/none font-bold text-tmm19-on-acc transition-[filter] hover:brightness-110">See results <span aria-hidden="true">&rarr;</span></button>
                <button data-tmm19-clear type="button" class="inline-flex min-h-11 cursor-pointer items-center justify-center border border-tmm19-line px-4 text-[0.85rem]/none font-semibold text-tmm19-ink transition-colors hover:border-tmm19-acc hover:text-tmm19-acc">Clear filters</button>
                <ul class="mt-1 grid gap-px border-t border-tmm19-line pt-2.5">
                  <li><a class="flex min-h-11 items-center text-[0.88rem] text-tmm19-ink hover:text-tmm19-acc" href="#tmm19-title">Best sellers</a></li>
                  <li><a class="flex min-h-11 items-center text-[0.88rem] text-tmm19-ink hover:text-tmm19-acc" href="#tmm19-title">Field-tested picks</a></li>
                  <li><a class="flex min-h-11 items-center text-[0.88rem] text-tmm19-ink hover:text-tmm19-acc" href="#tmm19-title">Clearance</a></li>
                </ul>
              </div>
            </div>
          </li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 text-[0.92rem]/none font-semibold text-tmm19-ink hover:text-tmm19-acc" href="#tmm19-title">Repairs</a></li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 text-[0.92rem]/none font-semibold text-tmm19-ink hover:text-tmm19-acc" href="#tmm19-title">Guides</a></li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 text-[0.92rem]/none font-semibold text-tmm19-ink hover:text-tmm19-acc" href="#tmm19-title">Hire</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-2 max-[52rem]:ml-0">
        <a class="inline-flex min-h-11 items-center px-2.5 text-[0.86rem] font-semibold text-tmm19-mut hover:text-tmm19-ink" href="#tmm19-title">Stores</a>
        <a class="inline-flex min-h-[38px] items-center gap-2 border border-tmm19-line px-3.5 text-[0.84rem]/none font-semibold text-tmm19-ink hover:border-tmm19-acc" href="#tmm19-title">Bag <span class="grid size-5 place-items-center bg-tmm19-ink text-[0.68rem] text-tmm19-surf">3</span></a>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(76rem,calc(100%-2rem))] py-[clamp(3rem,9vw,5.5rem)]">
    <div class="grid max-w-[34rem] gap-2">
      <p class="font-tmm19-display text-[0.74rem]/none font-semibold tracking-[0.18em] text-tmm19-acc uppercase">Field tested in the Cairngorms since 1988</p>
      <h1 class="font-tmm19-display text-[clamp(2.2rem,7vw,4rem)]/none font-bold tracking-[-0.03em]">Kit that comes back.</h1>
      <p class="text-[clamp(0.95rem,2.3vw,1.1rem)] text-tmm19-mut text-pretty">Every item repairable, every repair costed up front.</p>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm19-bg: #eceef0;
  --color-tmm19-bg: oklch(0.947 0.004 250);
  --color-tmm19-surf: #ffffff;
  --color-tmm19-surf: oklch(1 0 0);
  --color-tmm19-line: #c9ced4;
  --color-tmm19-line: oklch(0.85 0.01 250);
  --color-tmm19-ink: #16191c;
  --color-tmm19-ink: oklch(0.21 0.006 250);
  --color-tmm19-mut: #59616a;
  --color-tmm19-mut: oklch(0.48 0.014 250);
  --color-tmm19-acc: #b34103;
  --color-tmm19-acc: oklch(0.5 0.18 45);
  --color-tmm19-on-acc: #ffffff;
  --color-tmm19-on-acc: oklch(1 0 0);
  --font-tmm19-display: 'Zilla Slab', Rockwell, serif;
  --font-tmm19-sans: 'Albert Sans', system-ui, sans-serif;
  --shadow-tmm19-panel: 0 24px 56px -30px rgb(22 25 28 / 0.6);
  --ease-tmm19-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm19-open: instead of a repeated selector list. */

@custom-variant tmm19-open {
  &:where([data-tmm19-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm19-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-19 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-19:has(#tmm19-theme:checked) {
  --color-tmm19-bg: #0c0e10;
  --color-tmm19-bg: oklch(0.16 0.004 250);
  --color-tmm19-surf: #15181b;
  --color-tmm19-surf: oklch(0.2 0.006 250);
  --color-tmm19-line: #282d32;
  --color-tmm19-line: oklch(0.29 0.008 250);
  --color-tmm19-ink: #eef1f3;
  --color-tmm19-ink: oklch(0.95 0.004 250);
  --color-tmm19-mut: #9aa3ab;
  --color-tmm19-mut: oklch(0.71 0.012 250);
  --color-tmm19-acc: #ff8a4c;
  --color-tmm19-acc: oklch(0.76 0.16 50);
  --color-tmm19-on-acc: #1f0c02;
  --color-tmm19-on-acc: oklch(0.18 0.04 50);
}

@media (prefers-color-scheme: dark) {
  .tmm-19 {
    --color-tmm19-bg: #0c0e10;
    --color-tmm19-bg: oklch(0.16 0.004 250);
    --color-tmm19-surf: #15181b;
    --color-tmm19-surf: oklch(0.2 0.006 250);
    --color-tmm19-line: #282d32;
    --color-tmm19-line: oklch(0.29 0.008 250);
    --color-tmm19-ink: #eef1f3;
    --color-tmm19-ink: oklch(0.95 0.004 250);
    --color-tmm19-mut: #9aa3ab;
    --color-tmm19-mut: oklch(0.71 0.012 250);
    --color-tmm19-acc: #ff8a4c;
    --color-tmm19-acc: oklch(0.76 0.16 50);
    --color-tmm19-on-acc: #1f0c02;
    --color-tmm19-on-acc: oklch(0.18 0.04 50);
  }

  .tmm-19:has(#tmm19-theme:checked) {
    --color-tmm19-bg: #eceef0;
    --color-tmm19-bg: oklch(0.947 0.004 250);
    --color-tmm19-surf: #ffffff;
    --color-tmm19-surf: oklch(1 0 0);
    --color-tmm19-line: #c9ced4;
    --color-tmm19-line: oklch(0.85 0.01 250);
    --color-tmm19-ink: #16191c;
    --color-tmm19-ink: oklch(0.21 0.006 250);
    --color-tmm19-mut: #59616a;
    --color-tmm19-mut: oklch(0.48 0.014 250);
    --color-tmm19-acc: #b34103;
    --color-tmm19-acc: oklch(0.5 0.18 45);
    --color-tmm19-on-acc: #ffffff;
    --color-tmm19-on-acc: oklch(1 0 0);
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tmm-19');
  if (!root || root.__tmmCleanup) return;
  const item = root.querySelector('[data-tmm19-item]');
  const panel = root.querySelector('[data-tmm19-panel]');
  const trigger = root.querySelector('[data-tmm19-trigger]');
  const countEl = root.querySelector('[data-tmm19-count]');
  const priceEl = root.querySelector('[data-tmm19-price]');
  const badge = root.querySelector('[data-tmm19-badge]');
  const slider = root.querySelector('input[type="range"][data-tmm19-filter]');
  const boxes = [...root.querySelectorAll('input[type="checkbox"][data-tmm19-filter]')];
  const gbp = new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP', maximumFractionDigits: 0 });
  const defaults = boxes.map((b) => b.checked);
  let t = 0;

  const recount = () => {
    const picked = boxes.filter((b) => b.checked).length;
    const ceiling = Number(slider.value);
    priceEl.textContent = gbp.format(ceiling);
    badge.textContent = String(picked);
    badge.hidden = picked === 0;
    // Debounce the live region so a dragged slider announces once, not forty times.
    clearTimeout(t);
    t = setTimeout(() => { countEl.textContent = String(Math.max(6, Math.round((420 - picked * 62) * (ceiling / 420)))); }, 180);
  };
  const setOpen = (on) => { item.toggleAttribute('data-open', on); trigger.setAttribute('aria-expanded', String(on)); };

  const onInput = (e) => { if (e.target.matches('[data-tmm19-filter]')) recount(); };
  const onClick = (e) => {
    if (e.target.closest('[data-tmm19-trigger]')) setOpen(!item.hasAttribute('data-open'));
    if (e.target.closest('[data-tmm19-clear]')) { boxes.forEach((b) => { b.checked = false; }); slider.value = slider.max; recount(); }
  };
  const onDocClick = (e) => { if (!item.contains(e.target)) setOpen(false); };
  const onKey = (e) => { if (e.key === 'Escape') { setOpen(false); trigger.focus(); } };
  const onFocusOut = (e) => { if (!e.relatedTarget || !item.contains(e.relatedTarget)) setOpen(false); };

  panel.addEventListener('input', onInput);
  item.addEventListener('click', onClick);
  document.addEventListener('click', onDocClick);
  item.addEventListener('keydown', onKey);
  item.addEventListener('focusout', onFocusOut);
  recount();
  root.__tmmCleanup = () => {
    panel.removeEventListener('input', onInput);
    item.removeEventListener('click', onClick);
    document.removeEventListener('click', onDocClick);
    item.removeEventListener('keydown', onKey);
    item.removeEventListener('focusout', onFocusOut);
    clearTimeout(t);
  };
})();
```

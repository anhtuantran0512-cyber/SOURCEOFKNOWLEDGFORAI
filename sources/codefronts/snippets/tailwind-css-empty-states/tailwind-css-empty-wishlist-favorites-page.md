---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-wishlist-favorites-page/"
title: "Tailwind CSS Empty Wishlist / Favorites Page"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A fashion store's \"Saved\" page with three empty tabs — saved pieces, price alerts, size holds — switched by radio inputs, no JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Empty Wishlist / Favorites Page
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-wishlist-favorites-page/

A fashion store's "Saved" page with three empty tabs — saved pieces, price alerts, size holds — switched by radio inputs, no JavaScript. The heart on each "Last looked at" card is a real checkbox: tap one and the empty Saved tab fills with that piece, because the panel reads the hearts with group-has-[#id:checked]/w:.
## HTML
```html
<div class="tes-09 w-full min-h-svh bg-tes09-bg font-tes09-sans text-tes09-ink antialiased">
  <header class="flex flex-wrap items-center gap-x-8 gap-y-2 border-b border-tes09-line px-[clamp(1rem,4vw,3rem)] py-4">
    <a href="#" class="font-tes09-serif text-2xl focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes09-acc">Maren &amp; Co</a>
    <nav aria-label="Shop" class="order-3 flex w-full gap-5 overflow-x-auto text-sm text-tes09-mut sm:order-none sm:w-auto sm:flex-1">
      <a href="#" class="py-2 hover:text-tes09-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes09-acc">New in</a><a href="#" class="py-2 hover:text-tes09-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes09-acc">Knitwear</a><a href="#" class="py-2 hover:text-tes09-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes09-acc">Outerwear</a><a href="#" class="py-2 hover:text-tes09-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes09-acc">Archive</a>
    </nav>
    <span class="ml-auto text-sm text-tes09-mut">Account</span>
  </header>
  <main class="group/w mx-auto grid w-full max-w-6xl gap-10 px-[clamp(1rem,4vw,3rem)] py-[clamp(2rem,5vw,3.5rem)]">
    <div class="grid gap-2">
      <h1 class="font-tes09-serif text-[clamp(2.4rem,5vw,3.6rem)] leading-none tracking-tight">Saved</h1>
      <p class="max-w-[52ch] text-[15px]/7 text-tes09-mut text-pretty">Pieces you keep, price drops you asked us to watch, and the sizes we will hold for you.</p>
    </div>
    <div class="grid gap-5">
      <div role="radiogroup" aria-label="Saved sections" class="flex w-fit max-w-full gap-1 overflow-x-auto rounded-full bg-tes09-sunk p-1 text-sm">
        <label class="relative inline-flex min-h-10 cursor-pointer items-center gap-2 rounded-full px-4 whitespace-nowrap text-tes09-mut transition has-checked:bg-tes09-card has-checked:text-tes09-ink has-checked:shadow-sm has-focus-visible:outline-2 has-focus-visible:outline-tes09-acc"><input type="radio" name="tes09-tab" id="tes09-t1" checked class="sr-only">Saved pieces<i aria-hidden="true" class="hidden size-1.5 rounded-full bg-tes09-acc group-has-[[data-heart]:checked]/w:block"></i></label>
        <label class="inline-flex min-h-10 cursor-pointer items-center rounded-full px-4 whitespace-nowrap text-tes09-mut transition has-checked:bg-tes09-card has-checked:text-tes09-ink has-checked:shadow-sm has-focus-visible:outline-2 has-focus-visible:outline-tes09-acc"><input type="radio" name="tes09-tab" id="tes09-t2" class="sr-only">Price alerts</label>
        <label class="inline-flex min-h-10 cursor-pointer items-center rounded-full px-4 whitespace-nowrap text-tes09-mut transition has-checked:bg-tes09-card has-checked:text-tes09-ink has-checked:shadow-sm has-focus-visible:outline-2 has-focus-visible:outline-tes09-acc"><input type="radio" name="tes09-tab" id="tes09-t3" class="sr-only">Size holds</label>
      </div>
      <section aria-label="Saved pieces" class="hidden min-h-72 overflow-hidden rounded-3xl border border-tes09-line bg-tes09-card group-has-[#tes09-t1:checked]/w:grid">
        <div class="relative grid place-items-center px-6 py-14 group-has-[[data-heart]:checked]/w:hidden">
          <div aria-hidden="true" class="absolute inset-0 grid grid-cols-4 gap-4 p-6 opacity-50 [mask-image:radial-gradient(closest-side,transparent_55%,#000)]"><span class="rounded-2xl border border-dashed border-tes09-line2"></span><span class="rounded-2xl border border-dashed border-tes09-line2"></span><span class="rounded-2xl border border-dashed border-tes09-line2"></span><span class="rounded-2xl border border-dashed border-tes09-line2"></span></div>
          <div class="relative grid max-w-sm justify-items-center text-center">
            <span aria-hidden="true" class="grid size-16 place-items-center rounded-full bg-tes09-acc/10 text-tes09-acc ring-8 ring-tes09-acc/5"><svg class="size-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg></span>
            <p class="mt-5 font-tes09-serif text-3xl">Nothing saved yet</p>
            <p class="mt-2 text-sm/6 text-tes09-mut text-pretty">Tap the heart on any piece and it waits here — we will tell you before it sells out.</p>
            <a href="#" class="mt-5 inline-flex min-h-11 items-center rounded-full bg-tes09-ink px-6 text-sm font-medium text-white transition hover:bg-tes09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes09-acc">Browse new in</a>
          </div>
        </div>
        <ul class="hidden content-start divide-y divide-tes09-line p-2 group-has-[[data-heart]:checked]/w:grid">
          <li class="hidden items-center gap-4 p-3 transition-opacity duration-300 starting:opacity-0 group-has-[#tes09-h1:checked]/w:flex"><img src="https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=160&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="56" height="70" class="h-17.5 w-14 rounded-lg bg-tes09-sunk object-cover"><span class="grid flex-1"><b class="text-sm font-medium">Merino wool coat</b><span class="text-xs text-tes09-mut">£340 · we'll warn you before it sells out</span></span><label for="tes09-h1" class="min-h-11 cursor-pointer content-center rounded-full px-3 text-xs text-tes09-mut hover:text-tes09-ink">Remove</label></li>
          <li class="hidden items-center gap-4 p-3 transition-opacity duration-300 starting:opacity-0 group-has-[#tes09-h2:checked]/w:flex"><img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=160&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="56" height="70" class="h-17.5 w-14 rounded-lg bg-tes09-sunk object-cover"><span class="grid flex-1"><b class="text-sm font-medium">Boxy cotton shirt</b><span class="text-xs text-tes09-mut">£95 · we'll warn you before it sells out</span></span><label for="tes09-h2" class="min-h-11 cursor-pointer content-center rounded-full px-3 text-xs text-tes09-mut hover:text-tes09-ink">Remove</label></li>
          <li class="hidden items-center gap-4 p-3 transition-opacity duration-300 starting:opacity-0 group-has-[#tes09-h3:checked]/w:flex"><img src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=160&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="56" height="70" class="h-17.5 w-14 rounded-lg bg-tes09-sunk object-cover"><span class="grid flex-1"><b class="text-sm font-medium">Ribbed knit vest</b><span class="text-xs text-tes09-mut">£120 · we'll warn you before it sells out</span></span><label for="tes09-h3" class="min-h-11 cursor-pointer content-center rounded-full px-3 text-xs text-tes09-mut hover:text-tes09-ink">Remove</label></li>
        </ul>
      </section>
      <section aria-label="Price alerts" class="hidden min-h-72 place-items-center rounded-3xl border border-tes09-line bg-tes09-card px-6 py-14 group-has-[#tes09-t2:checked]/w:grid">
        <div class="grid max-w-sm justify-items-center text-center">
          <span aria-hidden="true" class="grid size-16 place-items-center rounded-full bg-tes09-acc/10 text-tes09-acc ring-8 ring-tes09-acc/5"><svg class="size-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15zM10 20.5h4"/></svg></span>
          <p class="mt-5 font-tes09-serif text-3xl">No price alerts running</p>
          <p class="mt-2 text-sm/6 text-tes09-mut text-pretty">Set one on a piece and we email you the moment it moves — once per item, never a digest.</p>
          <a href="#" class="mt-5 inline-flex min-h-11 items-center rounded-full bg-tes09-ink px-6 text-sm font-medium text-white transition hover:bg-tes09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes09-acc">See the archive sale</a>
        </div>
      </section>
      <section aria-label="Size holds" class="hidden min-h-72 place-items-center rounded-3xl border border-tes09-line bg-tes09-card px-6 py-14 group-has-[#tes09-t3:checked]/w:grid">
        <div class="grid max-w-sm justify-items-center text-center">
          <span aria-hidden="true" class="grid size-16 place-items-center rounded-full bg-tes09-acc/10 text-tes09-acc ring-8 ring-tes09-acc/5"><svg class="size-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 4a2 2 0 0 1 2 2c0 1.2-2 1.8-2 3l8.5 6.3a1 1 0 0 1-.6 1.7H4.1a1 1 0 0 1-.6-1.7L12 9"/></svg></span>
          <p class="mt-5 font-tes09-serif text-3xl">No sizes on hold</p>
          <p class="mt-2 text-sm/6 text-tes09-mut text-pretty">In-store staff can hold a size for 48 hours. Ask at the counter and it appears here.</p>
          <a href="#" class="mt-5 inline-flex min-h-11 items-center rounded-full bg-tes09-ink px-6 text-sm font-medium text-white transition hover:bg-tes09-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes09-acc">Find a store</a>
        </div>
      </section>
    </div>
    <section aria-labelledby="tes09-last" class="grid gap-4">
      <h2 id="tes09-last" class="font-tes09-serif text-2xl italic text-tes09-mut">Last looked at</h2>
      <ul class="grid grid-cols-[repeat(auto-fill,minmax(12rem,1fr))] gap-5">
        <li class="group grid gap-2.5"><figure class="relative aspect-4/5 overflow-hidden rounded-2xl bg-tes09-sunk"><img src="https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=520&amp;q=80&amp;auto=format&amp;fit=crop" alt="Folded wool coat on a bench" width="520" height="650" loading="lazy" decoding="async" class="size-full object-cover transition-transform duration-500 group-hover:scale-105"><label class="absolute top-2.5 right-2.5 grid size-11 cursor-pointer place-items-center rounded-full bg-white/85 text-tes09-ink shadow-sm backdrop-blur transition hover:scale-105 has-checked:text-tes09-acc"><input type="checkbox" id="tes09-h1" data-heart class="peer sr-only" aria-label="Save Merino wool coat"><svg class="size-5 transition peer-checked:fill-current peer-checked:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg><span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tes09-acc"></span></label></figure><p class="flex justify-between text-sm"><span class="font-medium">Merino wool coat</span><span class="tabular-nums text-tes09-mut">£340</span></p></li>
        <li class="group grid gap-2.5"><figure class="relative aspect-4/5 overflow-hidden rounded-2xl bg-tes09-sunk"><img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=520&amp;q=80&amp;auto=format&amp;fit=crop" alt="Clothing rail in a boutique" width="520" height="650" loading="lazy" decoding="async" class="size-full object-cover transition-transform duration-500 group-hover:scale-105"><label class="absolute top-2.5 right-2.5 grid size-11 cursor-pointer place-items-center rounded-full bg-white/85 text-tes09-ink shadow-sm backdrop-blur transition hover:scale-105 has-checked:text-tes09-acc"><input type="checkbox" id="tes09-h2" data-heart class="peer sr-only" aria-label="Save Boxy cotton shirt"><svg class="size-5 transition peer-checked:fill-current peer-checked:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg><span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tes09-acc"></span></label></figure><p class="flex justify-between text-sm"><span class="font-medium">Boxy cotton shirt</span><span class="tabular-nums text-tes09-mut">£95</span></p></li>
        <li class="group grid gap-2.5"><figure class="relative aspect-4/5 overflow-hidden rounded-2xl bg-tes09-sunk"><img src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=520&amp;q=80&amp;auto=format&amp;fit=crop" alt="Model wearing knitwear" width="520" height="650" loading="lazy" decoding="async" class="size-full object-cover transition-transform duration-500 group-hover:scale-105"><label class="absolute top-2.5 right-2.5 grid size-11 cursor-pointer place-items-center rounded-full bg-white/85 text-tes09-ink shadow-sm backdrop-blur transition hover:scale-105 has-checked:text-tes09-acc"><input type="checkbox" id="tes09-h3" data-heart class="peer sr-only" aria-label="Save Ribbed knit vest"><svg class="size-5 transition peer-checked:fill-current peer-checked:scale-110" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg><span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tes09-acc"></span></label></figure><p class="flex justify-between text-sm"><span class="font-medium">Ribbed knit vest</span><span class="tabular-nums text-tes09-mut">£120</span></p></li>
      </ul>
    </section>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes09-bg: #f7f4f1;
  --color-tes09-bg: oklch(0.966 0.007 60);
  --color-tes09-card: #fffdfb;
  --color-tes09-card: oklch(0.995 0.003 60);
  --color-tes09-sunk: #eee9e3;
  --color-tes09-sunk: oklch(0.93 0.011 60);
  --color-tes09-line: #e4ddd5;
  --color-tes09-line: oklch(0.9 0.014 60);
  --color-tes09-line2: #cbbfb2;
  --color-tes09-line2: oklch(0.8 0.022 60);
  --color-tes09-ink: #1f1a17;
  --color-tes09-ink: oklch(0.21 0.01 50);
  --color-tes09-mut: #645a52;
  --color-tes09-mut: oklch(0.47 0.018 55);
  --color-tes09-acc: #b4294f;
  --color-tes09-acc: oklch(0.52 0.18 10);
  --font-tes09-sans: 'Geist', system-ui, sans-serif;
  --font-tes09-serif: 'Instrument Serif', Georgia, serif;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-09 {
  width: 100%;
  min-height: 100svh;
}

.tes-09 [hidden] {
  display: none !important;
}
```

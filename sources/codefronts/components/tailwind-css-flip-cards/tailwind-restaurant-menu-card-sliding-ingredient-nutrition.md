---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-restaurant-menu-card-sliding-ingredient-nutrition/"
title: "Tailwind Restaurant Menu Card with Sliding Ingredient & Nutrition Reveal"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "The one card in the set with no 3D at all: the front slides out left while the back slides in from the right, like pulling a card from a file."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Restaurant Menu Card with Sliding Ingredient & Nutrition Reveal
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-restaurant-menu-card-sliding-ingredient-nutrition/

The one card in the set with no 3D at all: the front slides out left while the back slides in from the right, like pulling a card from a file. It proves the pattern is about the reveal, not the rotation &mdash; and because there is no preserve-3d, the frosted price tag's backdrop-blur actually works, which it would not inside a 3D context in Firefox.
## HTML
```html
<section class="tfc-13 w-full min-h-svh grid place-items-center bg-tfc13-bg font-tfc13-sans px-5 py-10 text-tfc13-cream">
  <div class="group relative w-[340px] max-w-full h-[470px] overflow-hidden rounded-2xl shadow-[0_1px_2px_oklch(0_0_0/0.5),0_22px_48px_-18px_oklch(0.3_0.08_50/0.7)] has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc13-amber has-[:focus-visible]:outline-offset-4">
    <input id="tfc-13-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-13-flip" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show ingredients, allergens and nutrition for Spaghetti al Ragu</span></label>

    <div class="absolute inset-0 flex flex-col rounded-2xl overflow-hidden bg-tfc13-panel border border-tfc13-amber/20 transition-transform duration-[550ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:-translate-x-full group-has-checked:-translate-x-full group-has-[:focus-visible]:-translate-x-full motion-reduce:transition-none">
      <div class="relative grid h-55 shrink-0 place-items-center overflow-hidden bg-linear-160 from-tfc13-stage via-tfc13-stage2 to-tfc13-stage3 before:absolute before:inset-0 before:bg-[radial-gradient(circle_at_50%_60%,oklch(0.6_0.13_60/0.3),transparent_65%)]">
        <svg class="relative z-1" width="180" height="160" viewBox="0 0 180 160" fill="none" role="img" aria-label="Illustration of a plate of spaghetti with meatballs, sauce and basil">
          <ellipse cx="90" cy="110" rx="78" ry="30" fill="oklch(0.25 0.03 60 / 0.6)"/>
          <ellipse cx="90" cy="105" rx="76" ry="28" fill="#2a1a08"/>
          <ellipse cx="90" cy="103" rx="68" ry="24" fill="#1a0e04"/>
          <path d="M55 95 Q70 80 85 95 Q100 110 115 95 Q130 80 125 95" stroke="oklch(0.65 0.14 65 / 0.8)" stroke-width="5" fill="none" stroke-linecap="round"/>
          <path d="M60 100 Q75 85 90 100 Q105 115 120 100" stroke="oklch(0.58 0.12 55 / 0.7)" stroke-width="4" fill="none" stroke-linecap="round"/>
          <path d="M65 90 Q80 75 95 90 Q110 105 125 90" stroke="oklch(0.75 0.15 70 / 0.6)" stroke-width="3" fill="none" stroke-linecap="round"/>
          <circle cx="72" cy="88" r="14" fill="oklch(0.45 0.1 50 / 0.85)"/>
          <circle cx="72" cy="88" r="10" fill="oklch(0.52 0.1 50 / 0.8)"/>
          <circle cx="108" cy="93" r="13" fill="oklch(0.45 0.1 50 / 0.85)"/>
          <circle cx="108" cy="93" r="9" fill="oklch(0.52 0.1 50 / 0.8)"/>
          <ellipse cx="90" cy="95" rx="35" ry="12" fill="oklch(0.45 0.18 30 / 0.35)"/>
          <circle cx="78" cy="76" r="3" fill="oklch(0.73 0.18 150 / 0.7)"/>
          <circle cx="85" cy="74" r="2" fill="oklch(0.73 0.18 150 / 0.6)"/>
          <circle cx="95" cy="78" r="2.5" fill="oklch(0.73 0.18 150 / 0.7)"/>
          <ellipse cx="90" cy="85" rx="20" ry="6" fill="oklch(0.95 0.06 85 / 0.3)"/>
        </svg>
        <p class="absolute top-3.5 right-3.5 z-2 rounded-full border border-tfc13-amber/40 bg-black/70 px-3 py-1.5 text-base font-extrabold text-tfc13-amber backdrop-blur-md">$24</p>
      </div>
      <div class="flex flex-1 flex-col gap-2 p-5">
        <p class="text-[10px] font-bold uppercase tracking-[0.15em] text-tfc13-amber">Italian &middot; Pasta</p>
        <h3 class="text-[22px] font-extrabold tracking-[-0.02em] text-tfc13-cream">Spaghetti al Ragu</h3>
        <p class="text-[13px] leading-[1.6] text-tfc13-muted text-pretty">House-made spaghetti with slow-cooked Bolognese, fresh parmesan, and wild basil.</p>
        <ul class="mt-1 flex flex-wrap gap-1.5">
          <li class="rounded-full border border-tfc13-red/20 bg-tfc13-red/10 px-2.5 py-0.5 text-[10px] text-tfc13-cream/75">Medium spice</li>
          <li class="rounded-full border border-tfc13-red/20 bg-tfc13-red/10 px-2.5 py-0.5 text-[10px] text-tfc13-cream/75">Chef's pick</li>
        </ul>
        <p class="mt-auto text-[10px] tracking-[0.08em] text-tfc13-dim">Hover, tap or press Space for ingredients &amp; nutrition &rarr;</p>
      </div>
    </div>

    <div class="absolute inset-0 flex translate-x-full flex-col gap-3 rounded-2xl overflow-hidden p-6 bg-linear-160 from-tfc13-back to-tfc13-back2 border border-tfc13-red/20 transition-transform duration-[550ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:translate-x-0 group-has-checked:translate-x-0 group-has-[:focus-visible]:translate-x-0 motion-reduce:transition-none">
      <h3 class="text-[10px] font-bold uppercase tracking-[0.15em] text-tfc13-amber">Key ingredients</h3>
      <ul class="grid grid-cols-2 gap-1.5 text-xs text-tfc13-cream/75">
        <li class="flex items-center gap-2 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc13-amber">Spaghetti pasta</li>
        <li class="flex items-center gap-2 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc13-amber">Beef mince (15%)</li>
        <li class="flex items-center gap-2 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc13-amber">San Marzano tomato</li>
        <li class="flex items-center gap-2 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc13-amber">Parmigiano 24mo</li>
        <li class="flex items-center gap-2 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc13-amber">Soffritto base</li>
        <li class="flex items-center gap-2 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc13-amber">Fresh basil</li>
        <li class="flex items-center gap-2 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc13-amber">Dry white wine</li>
        <li class="flex items-center gap-2 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc13-amber">Extra virgin olive oil</li>
      </ul>
      <h3 class="text-[10px] font-bold uppercase tracking-[0.15em] text-tfc13-amber">Allergens</h3>
      <ul class="flex flex-wrap gap-1.5">
        <li class="flex items-center gap-1 rounded-md border border-tfc13-red/35 bg-tfc13-red/10 px-2 py-1 text-[10px] font-semibold text-tfc13-cream/80"><span aria-hidden="true">&#9888;</span>Gluten</li>
        <li class="flex items-center gap-1 rounded-md border border-tfc13-red/35 bg-tfc13-red/10 px-2 py-1 text-[10px] font-semibold text-tfc13-cream/80"><span aria-hidden="true">&#9888;</span>Dairy</li>
        <li class="flex items-center gap-1 rounded-md border border-tfc13-red/35 bg-tfc13-red/10 px-2 py-1 text-[10px] font-semibold text-tfc13-cream/80"><span aria-hidden="true">&#9888;</span>Sulphites</li>
      </ul>
      <h3 class="text-[10px] font-bold uppercase tracking-[0.15em] text-tfc13-amber">Nutrition per serving</h3>
      <dl class="grid grid-cols-4 gap-1.5">
        <div class="rounded-lg border border-white/7 bg-white/4 px-1 py-2 text-center"><dd class="text-[15px] font-extrabold text-tfc13-cream">620</dd><dt class="mt-0.5 text-[9px] uppercase tracking-[0.08em] text-tfc13-dim">kcal</dt></div>
        <div class="rounded-lg border border-white/7 bg-white/4 px-1 py-2 text-center"><dd class="text-[15px] font-extrabold text-tfc13-cream">42g</dd><dt class="mt-0.5 text-[9px] uppercase tracking-[0.08em] text-tfc13-dim">Carbs</dt></div>
        <div class="rounded-lg border border-white/7 bg-white/4 px-1 py-2 text-center"><dd class="text-[15px] font-extrabold text-tfc13-cream">38g</dd><dt class="mt-0.5 text-[9px] uppercase tracking-[0.08em] text-tfc13-dim">Protein</dt></div>
        <div class="rounded-lg border border-white/7 bg-white/4 px-1 py-2 text-center"><dd class="text-[15px] font-extrabold text-tfc13-cream">22g</dd><dt class="mt-0.5 text-[9px] uppercase tracking-[0.08em] text-tfc13-dim">Fat</dt></div>
      </dl>
      <button type="button" class="relative z-30 mt-auto min-h-11 w-full rounded-xl bg-linear-135 from-tfc13-red to-tfc13-amber text-[13px] font-extrabold tracking-[0.04em] text-white transition-opacity duration-150 hover:opacity-90 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Add to order &mdash; $24</button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc13-bg: #0c0400;
  --color-tfc13-bg: oklch(0.13 0.02 45);
  --color-tfc13-panel: #111008;
  --color-tfc13-panel: oklch(0.17 0.015 80);
  --color-tfc13-stage: #1a0800;
  --color-tfc13-stage: oklch(0.18 0.05 45);
  --color-tfc13-stage2: #2d1200;
  --color-tfc13-stage2: oklch(0.24 0.07 50);
  --color-tfc13-stage3: #0d0800;
  --color-tfc13-stage3: oklch(0.14 0.02 60);
  --color-tfc13-back: #0e0800;
  --color-tfc13-back: oklch(0.15 0.02 60);
  --color-tfc13-back2: #12090a;
  --color-tfc13-back2: oklch(0.16 0.02 25);
  --color-tfc13-red: #dc2626;
  --color-tfc13-red: oklch(0.58 0.21 27);
  --color-tfc13-amber: #d97706;
  --color-tfc13-amber: oklch(0.68 0.16 60);
  --color-tfc13-cream: #fef3c7;
  --color-tfc13-cream: oklch(0.96 0.06 92);
  --color-tfc13-muted: #c5b48d;
  --color-tfc13-muted: oklch(0.79 0.05 90);
  --color-tfc13-dim: #8e8265;
  --color-tfc13-dim: oklch(0.63 0.03 90);
  --font-tfc13-sans: 'Sora', system-ui, sans-serif;
}

.tfc-13 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-13 * {
    transition-duration: 1ms !important;
  }
}
```

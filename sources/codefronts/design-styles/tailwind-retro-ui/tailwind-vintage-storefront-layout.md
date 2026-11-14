---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-vintage-storefront-layout/"
title: "Tailwind Vintage Storefront Layout"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A mail-order catalogue page: ruled columns, small caps, halftone product plates and a printed price block with the order code set in monospace."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vintage Storefront Layout
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-vintage-storefront-layout/

A mail-order catalogue page: ruled columns, small caps, halftone product plates and a printed price block with the order code set in monospace. The typographic decisions are the demo &mdash; catalogue type was small, tightly leaded and heavily tracked in the labels, and only some of those choices survive contact with an accessibility audit unchanged.
## HTML
```html
<section class="twr-19 relative block w-full min-h-svh box-border bg-twr19-paper text-twr19-ink font-twr19-serif" aria-labelledby="twr-19-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-19-title">Vintage mail-order catalogue storefront</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-19-theme">
    <label class="grid place-items-center size-11 rounded-full cursor-pointer border border-twr19-rule bg-twr19-paper2 text-twr19-ink2 peer-focus-visible:outline-2 peer-focus-visible:outline-twr19-acc peer-focus-visible:outline-offset-2" for="twr-19-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-7 max-w-[68rem] mx-auto px-[clamp(0.9rem,0.6rem+2vw,2.5rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <header class="min-w-0 grid justify-items-center gap-2.5 text-center border-b-2 border-twr19-ink pb-5">
      <p class="m-0 font-twr19-mono text-[0.7rem] tracking-[0.2em] uppercase text-twr19-ink2">Established 1932 &middot; Northgate &amp; Co.</p>
      <h3 class="m-0 min-w-0 text-[clamp(2rem,1.4rem+3.6vw,3.4rem)] font-semibold leading-none tracking-[0.02em] [font-variant-caps:all-small-caps] uppercase">Autumn Catalogue</h3>
      <p class="m-0 min-w-0 text-[0.98rem] italic text-twr19-ink2">Outerwear, knitwear and workshirts &mdash; pages 44 to 47</p>
      <nav class="min-w-0" aria-label="Catalogue sections">
        <ul class="list-none m-0 p-0 flex flex-wrap justify-center gap-x-2 gap-y-1">
          <li><button class="min-h-11 px-3.5 py-2 border-0 cursor-pointer bg-transparent font-twr19-serif text-[0.82rem] tracking-[var(--twr-19-track)] [font-variant-caps:all-small-caps] uppercase text-twr19-ink2 hover:text-twr19-ink focus-visible:outline-2 focus-visible:outline-twr19-acc focus-visible:outline-offset-2 text-twr19-ink border-b border-twr19-ink" type="button">Outerwear</button></li>
          <li><button class="min-h-11 px-3.5 py-2 border-0 cursor-pointer bg-transparent font-twr19-serif text-[0.82rem] tracking-[var(--twr-19-track)] [font-variant-caps:all-small-caps] uppercase text-twr19-ink2 hover:text-twr19-ink focus-visible:outline-2 focus-visible:outline-twr19-acc focus-visible:outline-offset-2" type="button">Knitwear</button></li>
          <li><button class="min-h-11 px-3.5 py-2 border-0 cursor-pointer bg-transparent font-twr19-serif text-[0.82rem] tracking-[var(--twr-19-track)] [font-variant-caps:all-small-caps] uppercase text-twr19-ink2 hover:text-twr19-ink focus-visible:outline-2 focus-visible:outline-twr19-acc focus-visible:outline-offset-2" type="button">Shirting</button></li>
          <li><button class="min-h-11 px-3.5 py-2 border-0 cursor-pointer bg-transparent font-twr19-serif text-[0.82rem] tracking-[var(--twr-19-track)] [font-variant-caps:all-small-caps] uppercase text-twr19-ink2 hover:text-twr19-ink focus-visible:outline-2 focus-visible:outline-twr19-acc focus-visible:outline-offset-2" type="button">Order form</button></li>
        </ul>
      </nav>
    </header>

    <ul class="list-none m-0 p-0 grid gap-x-6 gap-y-7 grid-cols-[repeat(auto-fit,minmax(min(100%,16rem),1fr))]">
      <li class="min-w-0 grid content-start gap-2.5 border-t border-twr19-rule pt-4">
        <span class="block w-full aspect-square bg-twr19-paper2 [background-image:repeating-radial-gradient(circle_at_0_0,rgba(33,28,20,0.55)_0_1.4px,rgba(0,0,0,0)_1.4px_var(--twr-19-dot))] [background-size:var(--twr-19-dot)_var(--twr-19-dot)] [box-shadow:inset_0_0_0_1px_var(--color-twr19-rule)]" role="img" aria-label="Catalogue plate: waxed cotton field coat, halftone illustration"></span>
        <h4 class="m-0 min-w-0 font-twr19-serif text-[1.05rem] font-semibold tracking-[var(--twr-19-track)] [font-variant-caps:all-small-caps] uppercase">Waxed Field Coat</h4>
        <p class="m-0 min-w-0 font-twr19-serif text-[0.95rem] leading-relaxed text-pretty text-twr19-ink">Four-pocket waxed cotton with corduroy collar and storm cuffs. Made in Yorkshire on a twelve-week lead.</p>
        <p class="m-0 min-w-0 font-twr19-serif text-[0.82rem] italic text-twr19-ink2">Olive, Navy, Sand &middot; sizes 36&ndash;46</p>
        <p class="m-0 flex items-start font-twr19-serif leading-none text-[clamp(1.6rem,1.3rem+1.4vw,2.1rem)]"><span class="mt-[0.15em] me-[0.05em] text-[0.55em]">&pound;</span>148<span class="mt-[0.15em] text-[0.5em]">00</span></p>
        <p class="m-0 font-twr19-mono text-[0.75rem] tabular-nums tracking-[0.04em] text-twr19-ink2">Order no. NG&ndash;4412</p>
      </li>
      <li class="min-w-0 grid content-start gap-2.5 border-t border-twr19-rule pt-4">
        <span class="block w-full aspect-square bg-twr19-paper2 [background-image:repeating-radial-gradient(circle_at_0_0,rgba(33,28,20,0.42)_0_1.4px,rgba(0,0,0,0)_1.4px_var(--twr-19-dot))] [background-size:var(--twr-19-dot)_var(--twr-19-dot)] [box-shadow:inset_0_0_0_1px_var(--color-twr19-rule)]" role="img" aria-label="Catalogue plate: lambswool crew neck jumper, halftone illustration"></span>
        <h4 class="m-0 min-w-0 font-twr19-serif text-[1.05rem] font-semibold tracking-[var(--twr-19-track)] [font-variant-caps:all-small-caps] uppercase">Lambswool Crew</h4>
        <p class="m-0 min-w-0 font-twr19-serif text-[0.95rem] leading-relaxed text-pretty text-twr19-ink">Seven-gauge lambswool, fully fashioned shoulders, ribbed hem. Sixteen colours held in stock year round.</p>
        <p class="m-0 min-w-0 font-twr19-serif text-[0.82rem] italic text-twr19-ink2">Sixteen colours &middot; sizes S&ndash;XXL</p>
        <p class="m-0 flex items-start font-twr19-serif leading-none text-[clamp(1.6rem,1.3rem+1.4vw,2.1rem)]"><span class="mt-[0.15em] me-[0.05em] text-[0.55em]">&pound;</span>62<span class="mt-[0.15em] text-[0.5em]">50</span></p>
        <p class="m-0 font-twr19-mono text-[0.75rem] tabular-nums tracking-[0.04em] text-twr19-ink2">Order no. NG&ndash;2207</p>
      </li>
      <li class="min-w-0 grid content-start gap-2.5 border-t border-twr19-rule pt-4">
        <span class="block w-full aspect-square bg-twr19-paper2 [background-image:repeating-radial-gradient(circle_at_0_0,rgba(33,28,20,0.5)_0_1.4px,rgba(0,0,0,0)_1.4px_var(--twr-19-dot))] [background-size:var(--twr-19-dot)_var(--twr-19-dot)] [box-shadow:inset_0_0_0_1px_var(--color-twr19-rule)]" role="img" aria-label="Catalogue plate: brushed cotton workshirt, halftone illustration"></span>
        <h4 class="m-0 min-w-0 font-twr19-serif text-[1.05rem] font-semibold tracking-[var(--twr-19-track)] [font-variant-caps:all-small-caps] uppercase">Brushed Workshirt</h4>
        <p class="m-0 min-w-0 font-twr19-serif text-[0.95rem] leading-relaxed text-pretty text-twr19-ink">Heavyweight brushed cotton, double-needle seams, two flap pockets. Cut generous through the body.</p>
        <p class="m-0 min-w-0 font-twr19-serif text-[0.82rem] italic text-twr19-ink2">Check or plain &middot; sizes 14&frac12;&ndash;18</p>
        <p class="m-0 flex items-start font-twr19-serif leading-none text-[clamp(1.6rem,1.3rem+1.4vw,2.1rem)]"><span class="mt-[0.15em] me-[0.05em] text-[0.55em]">&pound;</span>44<span class="mt-[0.15em] text-[0.5em]">00</span></p>
        <p class="m-0 font-twr19-mono text-[0.75rem] tabular-nums tracking-[0.04em] text-twr19-ink2">Order no. NG&ndash;1180</p>
      </li>
      <li class="min-w-0 grid content-start gap-2.5 border-t border-twr19-rule pt-4">
        <span class="block w-full aspect-square bg-twr19-paper2 [background-image:repeating-radial-gradient(circle_at_0_0,rgba(33,28,20,0.62)_0_1.4px,rgba(0,0,0,0)_1.4px_var(--twr-19-dot))] [background-size:var(--twr-19-dot)_var(--twr-19-dot)] [box-shadow:inset_0_0_0_1px_var(--color-twr19-rule)]" role="img" aria-label="Catalogue plate: moleskin trousers, halftone illustration"></span>
        <h4 class="m-0 min-w-0 font-twr19-serif text-[1.05rem] font-semibold tracking-[var(--twr-19-track)] [font-variant-caps:all-small-caps] uppercase">Moleskin Trousers</h4>
        <p class="m-0 min-w-0 font-twr19-serif text-[0.95rem] leading-relaxed text-pretty text-twr19-ink">Peached moleskin with a straight leg and side adjusters. Softens considerably after the first wash.</p>
        <p class="m-0 min-w-0 font-twr19-serif text-[0.82rem] italic text-twr19-ink2">Tobacco, Slate &middot; waist 30&ndash;42</p>
        <p class="m-0 flex items-start font-twr19-serif leading-none text-[clamp(1.6rem,1.3rem+1.4vw,2.1rem)]"><span class="mt-[0.15em] me-[0.05em] text-[0.55em]">&pound;</span>78<span class="mt-[0.15em] text-[0.5em]">00</span></p>
        <p class="m-0 font-twr19-mono text-[0.75rem] tabular-nums tracking-[0.04em] text-twr19-ink2">Order no. NG&ndash;3095</p>
      </li>
    </ul>

    <footer class="min-w-0 border-t-2 border-twr19-ink pt-4">
      <p class="m-0 min-w-0 max-w-[70ch] text-[0.92rem] leading-relaxed text-pretty text-twr19-ink2">Post free on orders over &pound;120. Telephone orders taken 9 to 5, Monday to Saturday. Type here keeps the catalogue's proportions &mdash; small caps, tracked labels, ruled columns &mdash; and raises the body size and ink weight to a pairing that actually reads.</p>
    </footer>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr19-paper: #f3ecdd;
  --color-twr19-paper: oklch(0.94 0.022 88);
  --color-twr19-paper2: #e9e0cd;
  --color-twr19-paper2: oklch(0.90 0.026 88);
  --color-twr19-ink: #211c14;
  --color-twr19-ink: oklch(0.23 0.017 70);
  --color-twr19-ink2: #57503f;
  --color-twr19-ink2: oklch(0.45 0.02 82);
  --color-twr19-rule: #a89a7e;
  --color-twr19-rule: oklch(0.70 0.03 84);
  --color-twr19-acc: #8c2f14;
  --color-twr19-acc: oklch(0.42 0.15 40);
  --font-twr19-serif: 'Spectral', ui-serif, Georgia, 'Times New Roman', serif;
  --font-twr19-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

.twr-19 {
  --twr-19-dot: 6px;
  --twr-19-track: 0.16em;
}

.twr-19:has(#twr-19-theme:checked) {
  --color-twr19-paper: #17140e;
  --color-twr19-paper: oklch(0.19 0.014 82);
  --color-twr19-paper2: #201c14;
  --color-twr19-paper2: oklch(0.24 0.016 82);
  --color-twr19-ink: #f2ebdc;
  --color-twr19-ink: oklch(0.94 0.014 82);
  --color-twr19-ink2: #b7ad97;
  --color-twr19-ink2: oklch(0.76 0.02 82);
  --color-twr19-rule: #4a4335;
  --color-twr19-rule: oklch(0.40 0.02 82);
  --color-twr19-acc: #ff9a72;
  --color-twr19-acc: oklch(0.78 0.13 40);
}
```

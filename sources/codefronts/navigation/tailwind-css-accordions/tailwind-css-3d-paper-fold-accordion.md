---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-3d-paper-fold-accordion/"
title: "Tailwind CSS 3D Paper Fold Accordion"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "An invitation whose sections unfold like letter flaps."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS 3D Paper Fold Accordion
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-3d-paper-fold-accordion/

An invitation whose sections unfold like letter flaps. Each panel is a real 3D plane hinged at its top edge (perspective-[900px] on the item, origin-top on the flap) that swings down from rotateX(-90deg) with a paper-settle overshoot, while a crease shadow slides off the sheet. Tailwind v4's 3D transform utilities and a ::details-content transition also let it fold back up on close, something the CSS original had to skip.
## HTML
```html
<section class="tac-20 w-full min-h-svh grid place-items-center bg-tac20-bg bg-[radial-gradient(90%_70%_at_50%_0%,var(--color-tac20-glow),transparent_70%)] px-5 py-16 font-tac20-sans text-tac20-ink [interpolate-size:allow-keywords]" aria-label="3D paper fold accordion demo">
  <div class="grid w-full justify-items-center gap-8">
    <article class="relative w-full max-w-[540px] rounded-[6px] bg-tac20-card px-[clamp(20px,5vw,40px)] pt-14 pb-[clamp(24px,5vw,36px)] shadow-[0_1px_1px_oklch(0.4_0.05_60/0.08),0_6px_14px_-4px_oklch(0.4_0.05_60/0.14),0_32px_60px_-28px_oklch(0.35_0.06_50/0.45)] ring-1 ring-tac20-line before:pointer-events-none before:absolute before:inset-2.5 before:rounded-[3px] before:border before:border-dashed before:border-tac20-line">
      <svg class="absolute top-0 left-1/2 size-16 -translate-x-1/2 -translate-y-1/2 drop-shadow-[0_4px_6px_oklch(0.35_0.1_30/0.35)]" viewBox="0 0 64 64" aria-hidden="true"><path d="M32 3c5 0 7 3 11 4s8 0 10 4 0 8 2 11 6 6 5 10-5 6-5 10 2 9-2 11-8 1-11 3-5 6-10 6-7-4-11-5-8 1-10-3-1-8-3-11-6-5-5-9 4-7 4-11-3-8 1-11 8-1 11-3 5-6 8-6z" fill="#b5432c"/><circle cx="32" cy="32" r="17" fill="none" stroke="#e07a5f" stroke-width="1.5" opacity=".7"/><path d="M24 24v16h7M35 40V24h5a4.5 4.5 0 0 1 0 9h-5" fill="none" stroke="#f6dccf" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>

      <header class="text-center">
        <p class="font-tac20-mono text-[11.5px] tracking-[0.22em] uppercase text-tac20-acc-ink">You are cordially invited</p>
        <h2 class="mt-3 font-tac20-serif text-[clamp(28px,5.2vw,38px)] leading-[1.05] font-semibold tracking-[-0.02em] text-balance italic">The Midsummer Letterpress Fair</h2>
        <p class="mx-auto mt-3 max-w-[38ch] text-[15px] leading-relaxed text-tac20-mut text-pretty">A day of hand-cranked presses, paper swaps and too much ink, at the old print works on Fanø.</p>
      </header>

      <div class="mt-8 grid gap-3">
        <details class="group perspective-[900px] [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-[550ms] [&::details-content]:ease-[cubic-bezier(.4,0,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none" open>
          <summary class="relative z-10 flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-t-[4px] rounded-b-[4px] border border-tac20-line bg-tac20-paper px-5 py-3 shadow-[0_1px_0_oklch(1_0_0/0.8)_inset,0_2px_4px_-2px_oklch(0.4_0.05_60/0.2)] transition-colors hover:bg-tac20-paper2 group-open:rounded-b-none group-open:bg-tac20-paper2 group-open:[border-bottom-style:dashed] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tac20-acc [&::-webkit-details-marker]:hidden">
            <span class="font-tac20-serif text-lg font-semibold text-tac20-acc italic" aria-hidden="true">i.</span>
            <span class="flex-1 font-tac20-serif text-[18px] font-semibold tracking-[-0.01em]">When &amp; where</span>
            <span class="grid size-8 place-items-center rounded-full border border-tac20-line text-tac20-acc-ink transition-transform duration-500 group-open:rotate-180 motion-reduce:transition-none" aria-hidden="true"><svg class="size-3.5" viewBox="0 0 16 16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="origin-top [backface-visibility:hidden] [transform:rotateX(-90deg)] transition-transform duration-[550ms] ease-[cubic-bezier(.4,0,.2,1)] group-open:[transform:none] group-open:animate-tac20-unfold motion-reduce:transition-none motion-reduce:group-open:animate-none">
            <div class="relative rounded-b-[4px] border border-t-0 border-tac20-line bg-tac20-paper bg-[repeating-linear-gradient(180deg,transparent_0_27px,var(--color-tac20-rule)_27px_28px)] bg-position-[0_16px] px-5 pt-4 pb-5 shadow-[0_10px_18px_-12px_oklch(0.35_0.06_50/0.45)] before:pointer-events-none before:absolute before:inset-0 before:bg-linear-to-b before:from-tac20-crease before:to-transparent before:to-70% before:opacity-100 before:transition-opacity before:duration-[550ms] group-open:before:opacity-0 group-open:before:animate-tac20-shade motion-reduce:before:hidden">
              <div class="grid gap-4 sm:grid-cols-[auto_1fr] sm:items-center">
                <div class="flex w-max items-stretch overflow-hidden rounded-md border border-tac20-acc/40 bg-tac20-card text-center">
                  <span class="grid place-items-center bg-tac20-acc px-2.5 font-tac20-mono text-[11px] tracking-[0.15em] text-tac20-card uppercase [writing-mode:vertical-rl] rotate-180">June</span>
                  <span class="px-4 py-2"><span class="block font-tac20-serif text-[34px] leading-none font-bold">20</span><span class="mt-1 block font-tac20-mono text-[11px] tracking-[0.12em] text-tac20-mut uppercase">Saturday</span></span>
                </div>
                <p class="text-[15px] leading-[28px] text-tac20-ink/85 text-pretty">10am until dusk, in the old print works on Fanø. The building has no number; follow the smell of ink and the sound of the Heidelberg.</p>
              </div>
            </div>
          </div>
        </details>

        <details class="group perspective-[900px] [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-[550ms] [&::details-content]:ease-[cubic-bezier(.4,0,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none">
          <summary class="relative z-10 flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-t-[4px] rounded-b-[4px] border border-tac20-line bg-tac20-paper px-5 py-3 shadow-[0_1px_0_oklch(1_0_0/0.8)_inset,0_2px_4px_-2px_oklch(0.4_0.05_60/0.2)] transition-colors hover:bg-tac20-paper2 group-open:rounded-b-none group-open:bg-tac20-paper2 group-open:[border-bottom-style:dashed] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tac20-acc [&::-webkit-details-marker]:hidden">
            <span class="font-tac20-serif text-lg font-semibold text-tac20-acc italic" aria-hidden="true">ii.</span>
            <span class="flex-1 font-tac20-serif text-[18px] font-semibold tracking-[-0.01em]">What to bring</span>
            <span class="grid size-8 place-items-center rounded-full border border-tac20-line text-tac20-acc-ink transition-transform duration-500 group-open:rotate-180 motion-reduce:transition-none" aria-hidden="true"><svg class="size-3.5" viewBox="0 0 16 16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="origin-top [backface-visibility:hidden] [transform:rotateX(-90deg)] transition-transform duration-[550ms] ease-[cubic-bezier(.4,0,.2,1)] group-open:[transform:none] group-open:animate-tac20-unfold motion-reduce:transition-none motion-reduce:group-open:animate-none">
            <div class="relative rounded-b-[4px] border border-t-0 border-tac20-line bg-tac20-paper bg-[repeating-linear-gradient(180deg,transparent_0_27px,var(--color-tac20-rule)_27px_28px)] bg-position-[0_16px] px-5 pt-4 pb-5 shadow-[0_10px_18px_-12px_oklch(0.35_0.06_50/0.45)] before:pointer-events-none before:absolute before:inset-0 before:bg-linear-to-b before:from-tac20-crease before:to-transparent before:to-70% before:opacity-100 before:transition-opacity before:duration-[550ms] group-open:before:opacity-0 group-open:before:animate-tac20-shade motion-reduce:before:hidden">
              <ul class="grid gap-0 text-[15px] leading-[28px] text-tac20-ink/85">
                <li class="flex gap-3"><span class="mt-[7px] size-3.5 flex-none rotate-[-4deg] rounded-[3px] border-[1.5px] border-tac20-acc" aria-hidden="true"></span>Paper you love, for the swap tables</li>
                <li class="flex gap-3"><span class="mt-[7px] size-3.5 flex-none rotate-[3deg] rounded-[3px] border-[1.5px] border-tac20-acc" aria-hidden="true"></span>Cash: most stalls cannot take cards</li>
                <li class="flex gap-3"><span class="mt-[7px] size-3.5 flex-none rotate-[-2deg] rounded-[3px] border-[1.5px] border-tac20-acc" aria-hidden="true"></span>An apron you do not mind ruining</li>
              </ul>
            </div>
          </div>
        </details>

        <details class="group perspective-[900px] [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-[550ms] [&::details-content]:ease-[cubic-bezier(.4,0,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none">
          <summary class="relative z-10 flex min-h-14 cursor-pointer list-none items-center gap-4 rounded-t-[4px] rounded-b-[4px] border border-tac20-line bg-tac20-paper px-5 py-3 shadow-[0_1px_0_oklch(1_0_0/0.8)_inset,0_2px_4px_-2px_oklch(0.4_0.05_60/0.2)] transition-colors hover:bg-tac20-paper2 group-open:rounded-b-none group-open:bg-tac20-paper2 group-open:[border-bottom-style:dashed] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tac20-acc [&::-webkit-details-marker]:hidden">
            <span class="font-tac20-serif text-lg font-semibold text-tac20-acc italic" aria-hidden="true">iii.</span>
            <span class="flex-1 font-tac20-serif text-[18px] font-semibold tracking-[-0.01em]">RSVP</span>
            <span class="grid size-8 place-items-center rounded-full border border-tac20-line text-tac20-acc-ink transition-transform duration-500 group-open:rotate-180 motion-reduce:transition-none" aria-hidden="true"><svg class="size-3.5" viewBox="0 0 16 16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="origin-top [backface-visibility:hidden] [transform:rotateX(-90deg)] transition-transform duration-[550ms] ease-[cubic-bezier(.4,0,.2,1)] group-open:[transform:none] group-open:animate-tac20-unfold motion-reduce:transition-none motion-reduce:group-open:animate-none">
            <div class="relative rounded-b-[4px] border border-t-0 border-tac20-line bg-tac20-paper bg-[repeating-linear-gradient(180deg,transparent_0_27px,var(--color-tac20-rule)_27px_28px)] bg-position-[0_16px] px-5 pt-4 pb-5 shadow-[0_10px_18px_-12px_oklch(0.35_0.06_50/0.45)] before:pointer-events-none before:absolute before:inset-0 before:bg-linear-to-b before:from-tac20-crease before:to-transparent before:to-70% before:opacity-100 before:transition-opacity before:duration-[550ms] group-open:before:opacity-0 group-open:before:animate-tac20-shade motion-reduce:before:hidden">
              <div class="flex items-start gap-4">
                <p class="flex-1 text-[15px] leading-[28px] text-tac20-ink/85 text-pretty">Post a card to the workshop (yes, actual post) or sign the ledger at the studio. Reply by <strong class="font-semibold text-tac20-ink">1 June</strong>.</p>
                <svg class="w-14 flex-none rotate-[6deg] drop-shadow-[0_2px_3px_oklch(0.35_0.06_50/0.3)] max-[400px]:hidden" viewBox="0 0 56 68" aria-hidden="true"><path d="M3 0h4a3 3 0 0 0 6 0h4a3 3 0 0 0 6 0h4a3 3 0 0 0 6 0h4a3 3 0 0 0 6 0h4a3 3 0 0 0 6 0v4a3 3 0 0 0 0 6v4a3 3 0 0 0 0 6v4a3 3 0 0 0 0 6v4a3 3 0 0 0 0 6v4a3 3 0 0 0 0 6v4a3 3 0 0 0 0 6v6h-4a3 3 0 0 0-6 0h-4a3 3 0 0 0-6 0h-4a3 3 0 0 0-6 0h-4a3 3 0 0 0-6 0H7a3 3 0 0 0-6 0H0v-6a3 3 0 0 0 0-6v-4a3 3 0 0 0 0-6v-4a3 3 0 0 0 0-6v-4a3 3 0 0 0 0-6v-4a3 3 0 0 0 0-6v-4a3 3 0 0 0 0-6V0z" fill="#fffaf0"/><rect x="6" y="6" width="44" height="56" rx="1" fill="#2f5d62"/><circle cx="36" cy="22" r="7" fill="#f2c14e"/><path d="M6 50l12-14 9 9 8-7 15 14v10H6z" fill="#e9dcc3"/><path d="M6 56l14-10 10 6 20-8v18H6z" fill="#b5432c"/></svg>
              </div>
              <button type="button" class="mt-3 inline-flex min-h-11 items-center gap-2 rounded-full bg-tac20-acc px-5 text-sm font-semibold text-tac20-card shadow-[0_6px_14px_-6px_oklch(0.45_0.14_35/0.7)] transition hover:bg-tac20-acc-ink active:translate-y-px focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tac20-acc">
                <svg class="size-4" viewBox="0 0 16 16" aria-hidden="true"><rect x="2" y="3" width="12" height="11" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M2 6.5h12M5.5 1.5v3M10.5 1.5v3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>Add to calendar
              </button>
            </div>
          </div>
        </details>
      </div>

      <p class="mt-7 text-center font-tac20-mono text-[11.5px] tracking-[0.12em] text-tac20-mut uppercase">Free entry · Children &amp; dogs welcome</p>
    </article>
    <p aria-hidden="true" class="rounded-full border border-tac20-line bg-tac20-card/70 px-3.5 py-2 font-tac20-mono text-[11.5px] text-tac20-mut">perspective-[900px] · origin-top · group-open:animate-tac20-unfold</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac20-bg: #ece3d3;
  --color-tac20-bg: oklch(0.91 0.022 80);
  --color-tac20-glow: #f8f2e6;
  --color-tac20-glow: oklch(0.96 0.015 85);
  --color-tac20-card: #fdf9f1;
  --color-tac20-card: oklch(0.982 0.011 85);
  --color-tac20-paper: #fbf6eb;
  --color-tac20-paper: oklch(0.973 0.014 85);
  --color-tac20-paper2: #f5eddd;
  --color-tac20-paper2: oklch(0.945 0.022 82);
  --color-tac20-line: #dccfb8;
  --color-tac20-line: oklch(0.86 0.03 80);
  --color-tac20-rule: #eee2cb;
  --color-tac20-rule: oklch(0.91 0.03 82);
  --color-tac20-crease: #5a3d1a66;
  --color-tac20-crease: oklch(0.36 0.06 65 / 0.4);
  --color-tac20-ink: #2e2618;
  --color-tac20-ink: oklch(0.27 0.025 75);
  --color-tac20-mut: #6c5f4a;
  --color-tac20-mut: oklch(0.49 0.035 75);
  --color-tac20-acc: #b5432c;
  --color-tac20-acc: oklch(0.53 0.15 35);
  --color-tac20-acc-ink: #93351f;
  --color-tac20-acc-ink: oklch(0.46 0.14 35);
  --font-tac20-serif: 'Fraunces', Georgia, serif;
  --font-tac20-sans: 'Manrope', system-ui, sans-serif;
  --font-tac20-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --animate-tac20-unfold: tac20-unfold 0.7s cubic-bezier(0.3, 1.25, 0.4, 1);
  --animate-tac20-shade: tac20-shade 0.7s ease-out;

  @keyframes tac20-unfold {
    from {
      transform: rotateX(-90deg);
    }

    to {
      transform: rotateX(0deg);
    }
  }

  @keyframes tac20-shade {
    from {
      opacity: 1;
    }

    to {
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-20 {
  width: 100%;
  min-height: 100svh;
}
```

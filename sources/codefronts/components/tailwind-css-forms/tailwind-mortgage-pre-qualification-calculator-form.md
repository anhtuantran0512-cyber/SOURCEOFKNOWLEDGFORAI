---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-mortgage-pre-qualification-calculator-form/"
title: "Tailwind Mortgage Pre-Qualification Calculator Form"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's pre-qualification calculator, ported one-for-one to Tailwind v4: linked slider + number inputs for home price and down payment,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mortgage Pre-Qualification Calculator Form
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-mortgage-pre-qualification-calculator-form/

The CSS collection's pre-qualification calculator, ported one-for-one to Tailwind v4: linked slider + number inputs for home price and down payment, loan-term and credit-band segmented controls, income and debts — and a live results panel with a house photo, a conic-gradient() donut whose slices animate through three registered @property percentages, a DTI gauge with 36% and 43% markers, a colour-coded verdict and key facts.
## HTML
```html
<div class="tf-16 relative block min-h-svh w-full bg-tf16-bg pt-[72px] font-tf16-sans leading-[normal] text-tf16-ink antialiased motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,4vw,3.5rem)]">
    <div class="@container w-full max-w-[66rem]">
      <div class="grid overflow-hidden rounded-3xl border border-tf16-line bg-tf16-card shadow-[0_40px_80px_-45px_rgba(25,26,23,.5)] @[54rem]:grid-cols-[minmax(0,1.15fr)_minmax(0,1fr)]">
        <div class="grid content-start gap-[1.3rem] p-[clamp(1.25rem,4cqi,2.5rem)]" role="form" aria-labelledby="tf-16-title">
          <p class="text-[.76rem] font-bold tracking-[.12em] text-tf16-accent uppercase">Pre-qualify in 60 seconds · No credit impact</p>
          <h2 id="tf-16-title" class="-mt-2 text-[clamp(1.6rem,4.4cqi,2.4rem)] leading-[1.05] font-extrabold tracking-[-.04em] [font-stretch:110%]">How much home can you afford?</h2>
          <div class="grid gap-[.35rem]">
            <div class="flex flex-wrap items-center justify-between gap-2"><label for="tf-16-price-n" class="text-[.88rem] font-semibold">Home price</label><div class="flex min-h-11 items-center gap-[.2rem] rounded-[.7rem] border border-tf16-line bg-tf16-soft px-3 font-bold [transition:border-color_.2s,box-shadow_.2s] focus-within:border-tf16-accent focus-within:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf16-accent)_20%,transparent)]"><span aria-hidden="true" class="text-tf16-muted">$</span><input id="tf-16-price-n" type="number" min="100000" max="2000000" step="5000" value="485000" class="border-0 bg-transparent text-[1.05rem] font-bold text-tf16-ink tabular-nums [-moz-appearance:textfield] focus:outline-none [&::-webkit-inner-spin-button]:appearance-none w-[7.5rem] text-right"></div></div>
            <input type="range" class="tf-16__range h-10 w-full cursor-pointer appearance-none rounded-[.4rem] bg-transparent [--fill:50%] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf16-accent [&::-moz-range-thumb]:size-[1.3rem] [&::-moz-range-thumb]:rounded-[.4rem] [&::-moz-range-thumb]:border-2 [&::-moz-range-thumb]:border-tf16-accent [&::-moz-range-thumb]:bg-tf16-card [&::-moz-range-track]:h-[.4rem] [&::-moz-range-track]:rounded-full [&::-moz-range-track]:bg-[linear-gradient(90deg,var(--color-tf16-accent)_var(--fill),var(--color-tf16-line)_var(--fill))] [&::-webkit-slider-runnable-track]:h-[.4rem] [&::-webkit-slider-runnable-track]:rounded-full [&::-webkit-slider-runnable-track]:bg-[linear-gradient(90deg,var(--color-tf16-accent)_var(--fill),var(--color-tf16-line)_var(--fill))] [&::-webkit-slider-thumb]:-mt-[.6rem] [&::-webkit-slider-thumb]:size-[1.6rem] [&::-webkit-slider-thumb]:rotate-45 [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:rounded-[.5rem] [&::-webkit-slider-thumb]:border-2 [&::-webkit-slider-thumb]:border-tf16-accent [&::-webkit-slider-thumb]:bg-tf16-card [&::-webkit-slider-thumb]:shadow-[0_4px_10px_-3px_rgba(0,0,0,.3)] [&::-webkit-slider-thumb]:[transition:scale_.2s_var(--ease-tf16)] active:[&::-webkit-slider-thumb]:scale-115" data-pair="tf-16-price-n" min="100000" max="2000000" step="5000" value="485000" aria-label="Home price slider">
          </div>
          <div class="grid gap-[.35rem]">
            <div class="flex flex-wrap items-center justify-between gap-2"><label for="tf-16-down-n" class="text-[.88rem] font-semibold">Down payment <b class="tf-16__downamt ml-[.3rem] font-medium text-tf16-muted"></b></label><div class="flex min-h-11 items-center gap-[.2rem] rounded-[.7rem] border border-tf16-line bg-tf16-soft px-3 font-bold [transition:border-color_.2s,box-shadow_.2s] focus-within:border-tf16-accent focus-within:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf16-accent)_20%,transparent)]"><input id="tf-16-down-n" type="number" min="3" max="60" step="1" value="20" class="border-0 bg-transparent text-[1.05rem] font-bold text-tf16-ink tabular-nums [-moz-appearance:textfield] focus:outline-none [&::-webkit-inner-spin-button]:appearance-none w-[7.5rem] text-right"><span aria-hidden="true" class="text-tf16-muted">%</span></div></div>
            <input type="range" class="tf-16__range h-10 w-full cursor-pointer appearance-none rounded-[.4rem] bg-transparent [--fill:50%] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf16-accent [&::-moz-range-thumb]:size-[1.3rem] [&::-moz-range-thumb]:rounded-[.4rem] [&::-moz-range-thumb]:border-2 [&::-moz-range-thumb]:border-tf16-accent [&::-moz-range-thumb]:bg-tf16-card [&::-moz-range-track]:h-[.4rem] [&::-moz-range-track]:rounded-full [&::-moz-range-track]:bg-[linear-gradient(90deg,var(--color-tf16-accent)_var(--fill),var(--color-tf16-line)_var(--fill))] [&::-webkit-slider-runnable-track]:h-[.4rem] [&::-webkit-slider-runnable-track]:rounded-full [&::-webkit-slider-runnable-track]:bg-[linear-gradient(90deg,var(--color-tf16-accent)_var(--fill),var(--color-tf16-line)_var(--fill))] [&::-webkit-slider-thumb]:-mt-[.6rem] [&::-webkit-slider-thumb]:size-[1.6rem] [&::-webkit-slider-thumb]:rotate-45 [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:rounded-[.5rem] [&::-webkit-slider-thumb]:border-2 [&::-webkit-slider-thumb]:border-tf16-accent [&::-webkit-slider-thumb]:bg-tf16-card [&::-webkit-slider-thumb]:shadow-[0_4px_10px_-3px_rgba(0,0,0,.3)] [&::-webkit-slider-thumb]:[transition:scale_.2s_var(--ease-tf16)] active:[&::-webkit-slider-thumb]:scale-115" data-pair="tf-16-down-n" min="3" max="60" step="1" value="20" aria-label="Down payment percent slider">
          </div>
          <fieldset class="grid min-w-0 grid-cols-3 gap-[.35rem]"><legend class="mb-2 p-0 text-[.88rem] font-semibold">Loan term</legend>
            <label class="group/sg relative text-[.88rem] font-semibold"><input type="radio" name="tf-16-t" value="15" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 place-items-center rounded-[.65rem] border border-tf16-line text-[.88rem] font-semibold transition-all duration-200 group-hover/sg:border-tf16-muted peer-checked:border-tf16-ink peer-checked:bg-tf16-ink peer-checked:text-tf16-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf16-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">15 yr</span></label><label class="group/sg relative text-[.88rem] font-semibold"><input type="radio" name="tf-16-t" value="20" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 place-items-center rounded-[.65rem] border border-tf16-line text-[.88rem] font-semibold transition-all duration-200 group-hover/sg:border-tf16-muted peer-checked:border-tf16-ink peer-checked:bg-tf16-ink peer-checked:text-tf16-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf16-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">20 yr</span></label><label class="group/sg relative text-[.88rem] font-semibold"><input type="radio" name="tf-16-t" value="30" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 place-items-center rounded-[.65rem] border border-tf16-line text-[.88rem] font-semibold transition-all duration-200 group-hover/sg:border-tf16-muted peer-checked:border-tf16-ink peer-checked:bg-tf16-ink peer-checked:text-tf16-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf16-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">30 yr</span></label>
          </fieldset>
          <fieldset class="grid min-w-0 grid-cols-[repeat(auto-fit,minmax(4.5rem,1fr))] gap-[.35rem]"><legend class="mb-2 p-0 text-[.88rem] font-semibold">Credit score</legend>
            <label class="group/sg relative text-[.88rem] font-semibold"><input type="radio" name="tf-16-c" value="760" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 place-items-center rounded-[.65rem] border border-tf16-line text-[.88rem] font-semibold transition-all duration-200 group-hover/sg:border-tf16-muted peer-checked:border-tf16-ink peer-checked:bg-tf16-ink peer-checked:text-tf16-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf16-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">760+</span></label><label class="group/sg relative text-[.88rem] font-semibold"><input type="radio" name="tf-16-c" value="700" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 place-items-center rounded-[.65rem] border border-tf16-line text-[.88rem] font-semibold transition-all duration-200 group-hover/sg:border-tf16-muted peer-checked:border-tf16-ink peer-checked:bg-tf16-ink peer-checked:text-tf16-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf16-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">700–759</span></label><label class="group/sg relative text-[.88rem] font-semibold"><input type="radio" name="tf-16-c" value="660" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 place-items-center rounded-[.65rem] border border-tf16-line text-[.88rem] font-semibold transition-all duration-200 group-hover/sg:border-tf16-muted peer-checked:border-tf16-ink peer-checked:bg-tf16-ink peer-checked:text-tf16-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf16-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">660–699</span></label><label class="group/sg relative text-[.88rem] font-semibold"><input type="radio" name="tf-16-c" value="620" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 place-items-center rounded-[.65rem] border border-tf16-line text-[.88rem] font-semibold transition-all duration-200 group-hover/sg:border-tf16-muted peer-checked:border-tf16-ink peer-checked:bg-tf16-ink peer-checked:text-tf16-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf16-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">620–659</span></label><label class="group/sg relative text-[.88rem] font-semibold"><input type="radio" name="tf-16-c" value="580" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-11 place-items-center rounded-[.65rem] border border-tf16-line text-[.88rem] font-semibold transition-all duration-200 group-hover/sg:border-tf16-muted peer-checked:border-tf16-ink peer-checked:bg-tf16-ink peer-checked:text-tf16-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf16-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">&lt;620</span></label>
          </fieldset>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-4">
            <div class="grid gap-[.35rem]"><label for="tf-16-inc" class="text-[.88rem] font-semibold">Annual household income</label><div class="flex min-h-11 items-center gap-[.2rem] rounded-[.7rem] border border-tf16-line bg-tf16-soft px-3 font-bold [transition:border-color_.2s,box-shadow_.2s] focus-within:border-tf16-accent focus-within:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf16-accent)_20%,transparent)]"><span aria-hidden="true" class="text-tf16-muted">$</span><input id="tf-16-inc" type="number" min="0" step="1000" value="142000" class="border-0 bg-transparent text-[1.05rem] font-bold text-tf16-ink tabular-nums [-moz-appearance:textfield] focus:outline-none [&::-webkit-inner-spin-button]:appearance-none w-full text-left"></div></div>
            <div class="grid gap-[.35rem]"><label for="tf-16-debt" class="text-[.88rem] font-semibold">Monthly debts <span class="font-normal text-tf16-muted">car, cards, loans</span></label><div class="flex min-h-11 items-center gap-[.2rem] rounded-[.7rem] border border-tf16-line bg-tf16-soft px-3 font-bold [transition:border-color_.2s,box-shadow_.2s] focus-within:border-tf16-accent focus-within:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf16-accent)_20%,transparent)]"><span aria-hidden="true" class="text-tf16-muted">$</span><input id="tf-16-debt" type="number" min="0" step="50" value="650" class="border-0 bg-transparent text-[1.05rem] font-bold text-tf16-ink tabular-nums [-moz-appearance:textfield] focus:outline-none [&::-webkit-inner-spin-button]:appearance-none w-full text-left"></div></div>
          </div>
        </div>
        <aside class="grid content-start gap-[1.2rem] border-t border-tf16-line bg-tf16-soft p-[clamp(1.25rem,4cqi,2.25rem)] @[54rem]:border-t-0 @[54rem]:border-l" aria-labelledby="tf-16-out-h">
          <figure class="-mx-[clamp(1.25rem,4cqi,2.25rem)] -mt-[clamp(1.25rem,4cqi,2.25rem)] h-36 bg-[#b9b4a6]"><img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800&h=400&fit=crop&auto=format&q=70" width="800" height="400" alt="Modern two-storey house with a pool at dusk" loading="lazy" decoding="async" class="block size-full object-cover"></figure>
          <h3 id="tf-16-out-h" class="sr-only">Your estimate</h3>
          <div class="flex flex-wrap items-center gap-5">
            <div class="tf-16__donut relative grid aspect-square w-[9.5rem] flex-none place-items-center rounded-full bg-[conic-gradient(var(--color-tf16-c1)_0_var(--tf-16-a),var(--color-tf16-c2)_0_var(--tf-16-b),var(--color-tf16-c3)_0_var(--tf-16-c),var(--color-tf16-c4)_0)] [--tf-16-a:0%] [transition:--tf-16-a_.7s_var(--ease-tf16),--tf-16-b_.7s_var(--ease-tf16),--tf-16-c_.7s_var(--ease-tf16)] forced-colors:border-2 forced-colors:border-[CanvasText]" aria-hidden="true"><div class="grid aspect-square w-[72%] content-center place-items-center rounded-full bg-tf16-soft text-center"><b class="tf-16__pay text-[1.45rem] font-extrabold tracking-[-.03em] tabular-nums">$0</b><small class="text-[.72rem] text-tf16-muted">per month</small></div></div>
            <ul class="grid min-w-44 flex-1 list-none gap-[.45rem] text-[.86rem]">
              <li style="--c:var(--color-tf16-c1)" class="flex items-center gap-2 before:size-[.7rem] before:flex-none before:rounded-[.2rem] before:bg-[var(--c)] before:content-['']"><span class="flex-1 text-tf16-muted">Principal &amp; interest</span><b class="tabular-nums" data-k="pi"></b></li>
              <li style="--c:var(--color-tf16-c2)" class="flex items-center gap-2 before:size-[.7rem] before:flex-none before:rounded-[.2rem] before:bg-[var(--c)] before:content-['']"><span class="flex-1 text-tf16-muted">Property tax</span><b class="tabular-nums" data-k="tax"></b></li>
              <li style="--c:var(--color-tf16-c3)" class="flex items-center gap-2 before:size-[.7rem] before:flex-none before:rounded-[.2rem] before:bg-[var(--c)] before:content-['']"><span class="flex-1 text-tf16-muted">Home insurance</span><b class="tabular-nums" data-k="ins"></b></li>
              <li style="--c:var(--color-tf16-c4)" class="flex items-center gap-2 before:size-[.7rem] before:flex-none before:rounded-[.2rem] before:bg-[var(--c)] before:content-['']"><span class="flex-1 text-tf16-muted">PMI</span><b class="tabular-nums" data-k="pmi"></b></li>
            </ul>
          </div>
          <p class="sr-only" aria-live="polite" id="tf-16-live"></p>
          <div class="grid gap-2 text-[.88rem] font-semibold">
            <div class="flex flex-wrap items-center justify-between gap-2"><span>Debt-to-income</span><b class="tf-16__dtival">0%</b></div>
            <div class="tf-16__gauge relative h-[.6rem] rounded-full bg-[linear-gradient(90deg,var(--color-tf16-ok)_0_36%,var(--color-tf16-warn)_36%_43%,var(--color-tf16-bad)_43%)]" aria-hidden="true"><i class="absolute top-1/2 left-[var(--dti,0%)] -mt-[.55rem] -ml-[.55rem] size-[1.1rem] rounded-full border-[3px] border-tf16-ink bg-tf16-card [transition:left_.6s_var(--ease-tf16)]"></i><span style="left:36%" class="absolute -top-1 -bottom-1 w-0.5 bg-tf16-card"></span><span style="left:43%" class="absolute -top-1 -bottom-1 w-0.5 bg-tf16-card"></span></div>
          </div>
          <div class="tf-16__verdict rounded-[.9rem] border px-4 py-[.9rem] data-[v=bad]:bg-[color-mix(in_oklab,var(--color-tf16-bad)_9%,var(--color-tf16-card))] data-[v=bad]:text-tf16-bad data-[v=ok]:bg-[color-mix(in_oklab,var(--color-tf16-ok)_9%,var(--color-tf16-card))] data-[v=ok]:text-tf16-ok data-[v=warn]:bg-[color-mix(in_oklab,var(--color-tf16-warn)_10%,var(--color-tf16-card))] data-[v=warn]:text-tf16-warn" data-v="ok"><b class="tf-16__vtitle block text-[1rem]"></b><p class="tf-16__vtext mt-[.25rem] text-[.86rem] leading-[1.45] text-tf16-ink"></p></div>
          <dl class="grid grid-cols-3 gap-2"><div class="rounded-[.7rem] border border-tf16-line bg-tf16-card px-[.7rem] py-[.65rem]"><dt class="text-[.7rem] font-semibold text-tf16-muted">Loan amount</dt><dd class="mt-[.15rem] text-[.95rem] font-bold tabular-nums" data-k="loan"></dd></div><div class="rounded-[.7rem] border border-tf16-line bg-tf16-card px-[.7rem] py-[.65rem]"><dt class="text-[.7rem] font-semibold text-tf16-muted">Est. rate</dt><dd class="mt-[.15rem] text-[.95rem] font-bold tabular-nums" data-k="rate"></dd></div><div class="rounded-[.7rem] border border-tf16-line bg-tf16-card px-[.7rem] py-[.65rem]"><dt class="text-[.7rem] font-semibold text-tf16-muted">Max price (43% DTI)</dt><dd class="mt-[.15rem] text-[.95rem] font-bold tabular-nums" data-k="max"></dd></div></dl>
          <button type="button" class="tf-16__cta min-h-[3.2rem] cursor-pointer rounded-[.85rem] border-0 bg-tf16-accent text-[1rem] font-bold text-tf16-on [transition:translate_.2s_var(--ease-tf16),filter_.2s] hover:-translate-y-0.5 hover:brightness-107 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf16-ink forced-colors:border forced-colors:border-[ButtonText]">Get pre-qualified</button>
          <p class="-mt-[.6rem] text-center text-[.74rem] text-tf16-muted">Estimates only — not a loan offer. Rates for illustration.</p>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf16-bg: #ecebe6;
  --color-tf16-card: #fbfaf7;
  --color-tf16-ink: #191a17;
  --color-tf16-muted: #6a6b63;
  --color-tf16-line: #e0ded6;
  --color-tf16-soft: #f2f1ec;
  --color-tf16-accent: #2f5d50;
  --color-tf16-on: #fff;
  --color-tf16-c1: #2f5d50;
  --color-tf16-c2: #8fb3a5;
  --color-tf16-c3: #d6a45c;
  --color-tf16-c4: #c46b4f;
  --color-tf16-ok: #2f7d4a;
  --color-tf16-warn: #b7791f;
  --color-tf16-bad: #b33a2b;
  --font-tf16-sans: "Archivo", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf16: cubic-bezier(0.16,1,0.3,1);
}
/* Registered so the donut's slice boundaries can transition — at-rules, so they stay CSS. */

@property --tf-16-a {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

@property --tf-16-b {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

@property --tf-16-c {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-16[data-theme="dark"] {
  color-scheme: dark;
  --color-tf16-bg: #0f100e;
  --color-tf16-card: #171815;
  --color-tf16-ink: #efeee8;
  --color-tf16-muted: #a3a49a;
  --color-tf16-line: #2a2b26;
  --color-tf16-soft: #1e1f1b;
  --color-tf16-accent: #7fc4ad;
  --color-tf16-on: #0c1f19;
  --color-tf16-c1: #7fc4ad;
  --color-tf16-c2: #3f7466;
  --color-tf16-c3: #e0b06a;
  --color-tf16-c4: #e08466;
  --color-tf16-ok: #6fcf8f;
  --color-tf16-warn: #f0b54d;
  --color-tf16-bad: #ff7d6b;
}

@media (prefers-color-scheme: dark) {
  .tf-16:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf16-bg: #0f100e;
    --color-tf16-card: #171815;
    --color-tf16-ink: #efeee8;
    --color-tf16-muted: #a3a49a;
    --color-tf16-line: #2a2b26;
    --color-tf16-soft: #1e1f1b;
    --color-tf16-accent: #7fc4ad;
    --color-tf16-on: #0c1f19;
    --color-tf16-c1: #7fc4ad;
    --color-tf16-c2: #3f7466;
    --color-tf16-c3: #e0b06a;
    --color-tf16-c4: #e08466;
    --color-tf16-ok: #6fcf8f;
    --color-tf16-warn: #f0b54d;
    --color-tf16-bad: #ff7d6b;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-16').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.tf-16');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const fmt = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  const RATES = { 760: .0612, 700: .0645, 660: .0689, 620: .0749, 580: .0839 }, TAX = .011, INS = 1600;
  const pmt = (loan, rate, years) => { const r = rate / 12, n = years * 12; return loan * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1); };
  const fill = (r) => r.style.setProperty('--fill', ((r.value - r.min) / (r.max - r.min)) * 100 + '%');
  root.querySelectorAll('.tf-16__range').forEach((r) => {
    const n = root.querySelector('#' + r.dataset.pair);
    r.addEventListener('input', () => { n.value = r.value; fill(r); calc(); });
    n.addEventListener('input', () => { r.value = n.value; fill(r); calc(); });
    fill(r);
  });
  root.addEventListener('change', calc);
  root.querySelectorAll('#tf-16-inc, #tf-16-debt').forEach((i) => i.addEventListener('input', calc));
  function calc() {
    const price = Number($('#tf-16-price-n').value) || 0, down = Math.min(60, Math.max(3, Number($('#tf-16-down-n').value) || 0)) / 100;
    const years = Number($('[name="tf-16-t"]:checked').value), band = $('[name="tf-16-c"]:checked').value;
    const rate = RATES[band] - (years === 15 ? .0065 : years === 20 ? .003 : 0);
    const loan = price * (1 - down), pi = pmt(loan, rate, years), tax = price * TAX / 12, ins = INS / 12, pmi = down < .2 ? loan * .005 / 12 : 0;
    const total = pi + tax + ins + pmi, income = (Number($('#tf-16-inc').value) || 0) / 12, debts = Number($('#tf-16-debt').value) || 0;
    const dti = income ? (total + debts) / income : 1;
    const d = $('.tf-16__donut'), a = pi / total * 100, b = a + tax / total * 100, c = b + ins / total * 100;
    d.style.setProperty('--tf-16-a', a + '%'); d.style.setProperty('--tf-16-b', b + '%'); d.style.setProperty('--tf-16-c', c + '%');
    $('.tf-16__pay').textContent = fmt.format(total);
    $('[data-k="pi"]').textContent = fmt.format(pi); $('[data-k="tax"]').textContent = fmt.format(tax);
    $('[data-k="ins"]').textContent = fmt.format(ins); $('[data-k="pmi"]').textContent = pmi ? fmt.format(pmi) : '—';
    $('.tf-16__downamt').textContent = '(' + fmt.format(price * down) + ')';
    $('[data-k="loan"]').textContent = fmt.format(loan); $('[data-k="rate"]').textContent = (rate * 100).toFixed(2) + '%';
    const budget = income * .43 - debts, perK = (pmt(1000 * (1 - down), rate, years) + 1000 * TAX / 12 + (down < .2 ? 1000 * (1 - down) * .005 / 12 : 0));
    $('[data-k="max"]').textContent = budget > ins ? fmt.format(Math.max(0, (budget - ins) / perK * 1000)) : '—';
    const pct = Math.round(dti * 100);
    $('.tf-16__dtival').textContent = pct + '%';
    $('.tf-16__gauge').style.setProperty('--dti', Math.min(100, pct) + '%');
    const v = $('.tf-16__verdict');
    if (dti <= .36) { v.dataset.v = 'ok'; $('.tf-16__vtitle').textContent = 'Likely to pre-qualify'; $('.tf-16__vtext').textContent = 'Your DTI is comfortably under 36%. Most lenders would see this as a strong application.'; }
    else if (dti <= .43) { v.dataset.v = 'warn'; $('.tf-16__vtitle').textContent = 'Borderline — but possible'; $('.tf-16__vtext').textContent = 'You\'re between 36% and 43% DTI. A larger down payment or paying off a debt would strengthen your file.'; }
    else { v.dataset.v = 'bad'; $('.tf-16__vtitle').textContent = 'Stretch for this price'; $('.tf-16__vtext').textContent = 'Above 43% DTI, most qualified mortgages won\'t fit. Try a lower price or longer term.'; }
    $('#tf-16-live').textContent = 'Estimated payment ' + fmt.format(total) + ' per month. ' + $('.tf-16__vtitle').textContent + '.';
  }
  $('.tf-16__cta').addEventListener('click', () => { $('.tf-16__cta').textContent = 'Great — we\'ll email your pre-qualification letter'; });
  calc();
})();
```

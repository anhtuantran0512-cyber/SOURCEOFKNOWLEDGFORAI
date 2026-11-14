---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-multi-step-insurance-quote-form/"
title: "Tailwind Multi-Step Insurance Quote Form"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's three-step lead-gen quote, ported one-for-one to Tailwind v4: big icon radio cards for Auto, Home, Life or Renters, a details step whose…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Step Insurance Quote Form
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-multi-step-insurance-quote-form/

The CSS collection's three-step lead-gen quote, ported one-for-one to Tailwind v4: big icon radio cards for Auto, Home, Life or Renters, a details step whose questions change with that choice via group-has-[[value=home]:checked]/root:grid (inapplicable fields disabled), a styled coverage-level slider, a segmented progress bar keyed to data-step, and a sticky estimate panel whose monthly range tweens as you go.
## HTML
```html
<div class="tf-12 group/root relative block min-h-svh w-full bg-tf12-bg pt-[72px] font-tf12-sans leading-[normal] text-tf12-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none! motion-reduce:**:after:transition-none!" data-step="1">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,4vw,3.5rem)]">
    <div class="@container w-full max-w-[62rem]">
      <div class="grid overflow-hidden rounded-3xl border border-tf12-line bg-tf12-card shadow-[0_40px_80px_-45px_rgba(11,27,51,.45)] @[50rem]:grid-cols-[minmax(0,1fr)_18rem]">
        <div class="grid content-start gap-[1.1rem] p-[clamp(1.25rem,4cqi,2.5rem)]" role="form" aria-labelledby="tf-12-title">
          <p class="text-[.78rem] font-bold tracking-[.12em] text-tf12-accent uppercase">Free quote · 2 minutes</p>
          <h2 id="tf-12-title" class="-mt-[.4rem] text-[clamp(1.5rem,4cqi,2.1rem)] leading-[1.1] font-extrabold tracking-[-.03em]">Let's find you better coverage</h2>
          <div class="grid grid-cols-3 gap-[.35rem]" aria-hidden="true"><i class="relative h-[.35rem] overflow-hidden rounded-full bg-tf12-line after:absolute after:inset-0 after:origin-left after:scale-x-0 after:bg-tf12-accent after:[transition:scale_.6s_var(--ease-tf12)] after:content-[''] forced-colors:after:bg-[Highlight] after:scale-x-100"></i><i class="relative h-[.35rem] overflow-hidden rounded-full bg-tf12-line after:absolute after:inset-0 after:origin-left after:scale-x-0 after:bg-tf12-accent after:[transition:scale_.6s_var(--ease-tf12)] after:content-[''] forced-colors:after:bg-[Highlight] in-data-[step=2]:after:scale-x-100 in-data-[step=3]:after:scale-x-100 in-data-[step=4]:after:scale-x-100"></i><i class="relative h-[.35rem] overflow-hidden rounded-full bg-tf12-line after:absolute after:inset-0 after:origin-left after:scale-x-0 after:bg-tf12-accent after:[transition:scale_.6s_var(--ease-tf12)] after:content-[''] forced-colors:after:bg-[Highlight] in-data-[step=3]:after:scale-x-100 in-data-[step=4]:after:scale-x-100"></i></div>
          <p class="tf-12__stepname -mt-2 text-[.85rem] font-semibold text-tf12-muted" aria-live="polite">Step 1 of 3 · Coverage</p>
          <fieldset class="tf-12__step grid min-w-0 animate-tf12-in gap-4" data-i="1">
            <legend class="sr-only">What would you like to insure?</legend>
            <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,9rem),1fr))] gap-[.7rem]">
              <label class="group/t relative text-[.86rem] font-semibold"><input type="radio" name="tf-12-type" value="auto" checked class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid justify-items-start gap-[.15rem] rounded-[1.1rem] border-[1.5px] border-tf12-line bg-tf12-soft p-[1.1rem] [transition:all_.25s_var(--ease-tf12)] group-hover/t:border-[color-mix(in_oklab,var(--color-tf12-accent)_40%,var(--color-tf12-line))] peer-checked:border-tf12-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf12-accent)_7%,var(--color-tf12-card))] peer-checked:shadow-[0_12px_24px_-16px_var(--color-tf12-accent)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tf12-accent forced-colors:peer-checked:outline-2 forced-colors:peer-checked:outline-[Highlight]"><svg viewBox="0 0 32 32" aria-hidden="true" class="mb-[.6rem] size-9 fill-none stroke-tf12-muted stroke-[1.6] [stroke-linecap:round] [stroke-linejoin:round] [transition:stroke_.25s,translate_.35s_var(--ease-tf12)] group-hover/t:-translate-y-0.5 group-has-checked/t:stroke-tf12-accent"><path d="M5 20v-4l3-6h16l3 6v4"/><rect x="3" y="16" width="26" height="6" rx="2"/><circle cx="9" cy="23" r="2.5"/><circle cx="23" cy="23" r="2.5"/></svg><b class="font-bold">Auto</b><small class="text-[.78rem] font-normal text-tf12-muted">Cars &amp; motorbikes</small></span></label>
              <label class="group/t relative text-[.86rem] font-semibold"><input type="radio" name="tf-12-type" value="home" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid justify-items-start gap-[.15rem] rounded-[1.1rem] border-[1.5px] border-tf12-line bg-tf12-soft p-[1.1rem] [transition:all_.25s_var(--ease-tf12)] group-hover/t:border-[color-mix(in_oklab,var(--color-tf12-accent)_40%,var(--color-tf12-line))] peer-checked:border-tf12-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf12-accent)_7%,var(--color-tf12-card))] peer-checked:shadow-[0_12px_24px_-16px_var(--color-tf12-accent)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tf12-accent forced-colors:peer-checked:outline-2 forced-colors:peer-checked:outline-[Highlight]"><svg viewBox="0 0 32 32" aria-hidden="true" class="mb-[.6rem] size-9 fill-none stroke-tf12-muted stroke-[1.6] [stroke-linecap:round] [stroke-linejoin:round] [transition:stroke_.25s,translate_.35s_var(--ease-tf12)] group-hover/t:-translate-y-0.5 group-has-checked/t:stroke-tf12-accent"><path d="M4 15 16 5l12 10"/><path d="M7 13v13h18V13"/><path d="M13 26v-7h6v7"/></svg><b class="font-bold">Home</b><small class="text-[.78rem] font-normal text-tf12-muted">Buildings &amp; contents</small></span></label>
              <label class="group/t relative text-[.86rem] font-semibold"><input type="radio" name="tf-12-type" value="life" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid justify-items-start gap-[.15rem] rounded-[1.1rem] border-[1.5px] border-tf12-line bg-tf12-soft p-[1.1rem] [transition:all_.25s_var(--ease-tf12)] group-hover/t:border-[color-mix(in_oklab,var(--color-tf12-accent)_40%,var(--color-tf12-line))] peer-checked:border-tf12-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf12-accent)_7%,var(--color-tf12-card))] peer-checked:shadow-[0_12px_24px_-16px_var(--color-tf12-accent)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tf12-accent forced-colors:peer-checked:outline-2 forced-colors:peer-checked:outline-[Highlight]"><svg viewBox="0 0 32 32" aria-hidden="true" class="mb-[.6rem] size-9 fill-none stroke-tf12-muted stroke-[1.6] [stroke-linecap:round] [stroke-linejoin:round] [transition:stroke_.25s,translate_.35s_var(--ease-tf12)] group-hover/t:-translate-y-0.5 group-has-checked/t:stroke-tf12-accent"><path d="M16 27s-10-6-10-14a5.5 5.5 0 0 1 10-3 5.5 5.5 0 0 1 10 3c0 8-10 14-10 14Z"/><path d="M9 16h4l2-3 2 6 2-3h4"/></svg><b class="font-bold">Life</b><small class="text-[.78rem] font-normal text-tf12-muted">Term &amp; whole life</small></span></label>
              <label class="group/t relative text-[.86rem] font-semibold"><input type="radio" name="tf-12-type" value="renters" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid justify-items-start gap-[.15rem] rounded-[1.1rem] border-[1.5px] border-tf12-line bg-tf12-soft p-[1.1rem] [transition:all_.25s_var(--ease-tf12)] group-hover/t:border-[color-mix(in_oklab,var(--color-tf12-accent)_40%,var(--color-tf12-line))] peer-checked:border-tf12-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf12-accent)_7%,var(--color-tf12-card))] peer-checked:shadow-[0_12px_24px_-16px_var(--color-tf12-accent)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tf12-accent forced-colors:peer-checked:outline-2 forced-colors:peer-checked:outline-[Highlight]"><svg viewBox="0 0 32 32" aria-hidden="true" class="mb-[.6rem] size-9 fill-none stroke-tf12-muted stroke-[1.6] [stroke-linecap:round] [stroke-linejoin:round] [transition:stroke_.25s,translate_.35s_var(--ease-tf12)] group-hover/t:-translate-y-0.5 group-has-checked/t:stroke-tf12-accent"><rect x="6" y="4" width="20" height="24" rx="2"/><path d="M11 9h3M18 9h3M11 14h3M18 14h3M11 19h3M18 19h3M14 28v-4h4v4"/></svg><b class="font-bold">Renters</b><small class="text-[.78rem] font-normal text-tf12-muted">Your belongings</small></span></label>
            </div>
          </fieldset>
          <fieldset class="tf-12__step grid min-w-0 animate-tf12-in gap-4" data-i="2" hidden>
            <legend class="sr-only">Tell us a little more</legend>
            <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-4">
              <div class="grid gap-[.4rem]"><label for="tf-12-zip" class="text-[.86rem] font-semibold">ZIP / postcode</label><input id="tf-12-zip" autocomplete="postal-code" required placeholder="10001" class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"></div>
              <div class="grid gap-[.4rem]"><label for="tf-12-age" class="text-[.86rem] font-semibold">Your age</label><select id="tf-12-age" required class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"><option value="">Select</option><option value="1.35">18–24</option><option value="1.1">25–34</option><option value="1" selected>35–49</option><option value="1.05">50–64</option><option value="1.3">65+</option></select></div>
            </div>
            <div class="tf-12__cond tf-12__cond--auto hidden grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-4 group-has-[[value=auto]:checked]/root:grid">
              <div class="grid gap-[.4rem]"><label for="tf-12-yr" class="text-[.86rem] font-semibold">Vehicle year</label><input id="tf-12-yr" type="number" min="1990" max="2027" value="2022" required class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"></div>
              <div class="grid gap-[.4rem]"><label for="tf-12-mi" class="text-[.86rem] font-semibold">Annual mileage</label><select id="tf-12-mi" class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"><option>Under 7,500</option><option selected>7,500–12,000</option><option>12,000+</option></select></div>
            </div>
            <div class="tf-12__cond tf-12__cond--home hidden grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-4 group-has-[[value=home]:checked]/root:grid">
              <div class="grid gap-[.4rem]"><label for="tf-12-hv" class="text-[.86rem] font-semibold">Rebuild value ($)</label><input id="tf-12-hv" type="number" min="50000" step="10000" value="350000" required class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"></div>
              <div class="grid gap-[.4rem]"><label for="tf-12-built" class="text-[.86rem] font-semibold">Year built</label><input id="tf-12-built" type="number" min="1800" max="2027" value="1998" class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"></div>
            </div>
            <div class="tf-12__cond tf-12__cond--life hidden grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-4 group-has-[[value=life]:checked]/root:grid">
              <div class="grid gap-[.4rem]"><label for="tf-12-term" class="text-[.86rem] font-semibold">Term length</label><select id="tf-12-term" class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"><option>10 years</option><option selected>20 years</option><option>30 years</option></select></div>
              <div class="grid gap-[.4rem]"><label for="tf-12-smk" class="text-[.86rem] font-semibold">Tobacco use in last 12 months?</label><select id="tf-12-smk" class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"><option>No</option><option>Yes</option></select></div>
            </div>
            <div class="tf-12__cond tf-12__cond--renters hidden grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-4 group-has-[[value=renters]:checked]/root:grid">
              <div class="grid gap-[.4rem]"><label for="tf-12-cv" class="text-[.86rem] font-semibold">Contents value ($)</label><input id="tf-12-cv" type="number" min="5000" step="1000" value="25000" required class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"></div>
            </div>
            <div class="grid gap-[.4rem]">
              <div class="flex items-baseline justify-between"><label for="tf-12-level" class="text-[.86rem] font-semibold">Coverage level</label><output for="tf-12-level" class="tf-12__lvl text-[.9rem] font-bold text-tf12-accent">Standard</output></div>
              <input id="tf-12-level" type="range" min="1" max="3" step="1" value="2" aria-valuetext="Standard" class="h-11 w-full cursor-pointer appearance-none rounded-[.5rem] bg-transparent [--fill:50%] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf12-accent [&::-moz-range-thumb]:size-[1.2rem] [&::-moz-range-thumb]:rounded-full [&::-moz-range-thumb]:border-[3px] [&::-moz-range-thumb]:border-tf12-accent [&::-moz-range-thumb]:bg-tf12-card [&::-moz-range-track]:h-[.45rem] [&::-moz-range-track]:rounded-full [&::-moz-range-track]:bg-[linear-gradient(90deg,var(--color-tf12-accent)_var(--fill),var(--color-tf12-line)_var(--fill))] [&::-webkit-slider-runnable-track]:h-[.45rem] [&::-webkit-slider-runnable-track]:rounded-full [&::-webkit-slider-runnable-track]:bg-[linear-gradient(90deg,var(--color-tf12-accent)_var(--fill),var(--color-tf12-line)_var(--fill))] [&::-webkit-slider-thumb]:-mt-[.53rem] [&::-webkit-slider-thumb]:size-6 [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:border-[3px] [&::-webkit-slider-thumb]:border-tf12-accent [&::-webkit-slider-thumb]:bg-tf12-card [&::-webkit-slider-thumb]:shadow-[0_4px_10px_-3px_var(--color-tf12-accent)] [&::-webkit-slider-thumb]:[transition:scale_.2s_var(--ease-tf12)] active:[&::-webkit-slider-thumb]:scale-115">
              <div class="-mt-[.4rem] flex justify-between text-[.75rem] text-tf12-muted" aria-hidden="true"><span>Basic</span><span>Standard</span><span>Premium</span></div>
            </div>
          </fieldset>
          <fieldset class="tf-12__step grid min-w-0 animate-tf12-in gap-4" data-i="3" hidden>
            <legend class="sr-only">Where should we send your quote?</legend>
            <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-4">
              <div class="grid gap-[.4rem]"><label for="tf-12-n" class="text-[.86rem] font-semibold">Full name</label><input id="tf-12-n" autocomplete="name" required class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"></div>
              <div class="grid gap-[.4rem]"><label for="tf-12-e" class="text-[.86rem] font-semibold">Email</label><input id="tf-12-e" type="email" autocomplete="email" required class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"></div>
            </div>
            <div class="grid gap-[.4rem]"><label for="tf-12-p" class="text-[.86rem] font-semibold">Phone <span class="font-normal text-tf12-muted">Optional — only if you'd like a call</span></label><input id="tf-12-p" type="tel" autocomplete="tel" class="min-h-12 w-full rounded-[.75rem] border border-tf12-line bg-tf12-soft px-[.9rem] py-[.65rem] text-[1rem] text-tf12-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf12-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf12-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-[#dc2626]"></div>
            <label class="flex cursor-pointer items-start gap-[.65rem] text-[.86rem] leading-[1.45] font-normal text-tf12-muted"><input type="checkbox" required class="mt-[.12rem] size-[1.15rem] flex-none accent-tf12-accent"><span>I agree to be contacted about my quote. No spam, and we never sell your data.</span></label>
          </fieldset>
          <div class="tf-12__done animate-tf12-in rounded-2xl border border-[color-mix(in_oklab,var(--color-tf12-ok)_35%,transparent)] bg-[color-mix(in_oklab,var(--color-tf12-ok)_10%,var(--color-tf12-card))] px-5 py-4 outline-none" hidden tabindex="-1"><h3 class="mb-[.3rem] text-[1.17em] font-bold text-tf12-ok">Your quote is on its way</h3><p class="text-tf12-muted">We've emailed your personalised quote. A licensed advisor is available if you have questions.</p></div>
          <div class="flex justify-between gap-3 pt-2 in-data-[step=4]:hidden">
            <button type="button" class="tf-12__back inline-flex min-h-[3.1rem] cursor-pointer items-center gap-2 rounded-[.85rem] px-[1.4rem] font-bold [transition:translate_.2s_var(--ease-tf12),filter_.2s,background_.2s] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf12-ink border border-tf12-line bg-transparent text-tf12-ink hover:bg-tf12-soft in-data-[step=1]:invisible">Back</button>
            <button type="button" class="tf-12__next group/n inline-flex min-h-[3.1rem] cursor-pointer items-center gap-2 rounded-[.85rem] px-[1.4rem] font-bold [transition:translate_.2s_var(--ease-tf12),filter_.2s,background_.2s] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf12-ink ml-auto border-0 bg-tf12-accent text-tf12-on shadow-[0_12px_24px_-12px_var(--color-tf12-accent)] hover:-translate-y-0.5">Continue<svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.1rem] fill-none stroke-current stroke-[2.2] [stroke-linecap:round] [stroke-linejoin:round] [transition:translate_.3s_var(--ease-tf12)] group-hover/n:translate-x-[3px]"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
          </div>
        </div>
        <aside class="relative grid content-start gap-4 overflow-hidden [background:radial-gradient(20rem_16rem_at_100%_0%,color-mix(in_oklab,var(--color-tf12-sky)_45%,transparent),transparent_70%),linear-gradient(160deg,#0f2f6b,#0a1a3a)] p-[clamp(1.25rem,4cqi,2.25rem)] text-[#eaf2ff] after:absolute after:-right-12 after:-bottom-12 after:size-40 after:rounded-full after:border-[1.5rem] after:border-white/5 after:content-[''] forced-colors:border-l forced-colors:border-[CanvasText] forced-colors:bg-[Canvas] forced-colors:text-[CanvasText]" aria-labelledby="tf-12-est-h">
          <p id="tf-12-est-h" class="text-[.78rem] font-bold tracking-[.12em] uppercase opacity-75">Estimated premium</p>
          <p class="text-[clamp(2rem,6cqi,2.6rem)] leading-none font-extrabold tracking-[-.03em] tabular-nums" aria-live="polite"><b class="tf-12__lo">$0</b>–<b class="tf-12__hi">$0</b><small class="ml-[.2rem] text-[1rem] font-medium opacity-70">/mo</small></p>
          <ul class="grid list-none gap-[.55rem] border-t border-white/12 pt-4 text-[.88rem]"><li class="flex gap-[.55rem] before:font-extrabold before:text-tf12-sky before:content-['✓']">No obligation, no credit check</li><li class="flex gap-[.55rem] before:font-extrabold before:text-tf12-sky before:content-['✓']">Compare 12+ A-rated insurers</li><li class="flex gap-[.55rem] before:font-extrabold before:text-tf12-sky before:content-['✓']">Switch and save in minutes</li></ul>
          <p class="text-[.75rem] opacity-65">Indicative only. Your final price depends on underwriting.</p>
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
  --color-tf12-bg: #eef3fa;
  --color-tf12-card: #ffffff;
  --color-tf12-ink: #0b1b33;
  --color-tf12-muted: #5a6a82;
  --color-tf12-line: #dde5f0;
  --color-tf12-soft: #f5f8fc;
  --color-tf12-accent: #1d5bd8;
  --color-tf12-on: #fff;
  --color-tf12-sky: #7cc4ff;
  --color-tf12-ok: #0f9d6b;
  --font-tf12-sans: "Red Hat Display", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf12: cubic-bezier(0.16,1,0.3,1);
  --animate-tf12-in: tf12-in 0.45s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf12-in {
    from {
      opacity: 0;
      translate: 0 10px;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-12[data-theme="dark"] {
  color-scheme: dark;
  --color-tf12-bg: #07101e;
  --color-tf12-card: #0d1a2d;
  --color-tf12-ink: #e6eefb;
  --color-tf12-muted: #93a3bd;
  --color-tf12-line: #1d2d46;
  --color-tf12-soft: #112138;
  --color-tf12-accent: #5b8cff;
  --color-tf12-on: #04122e;
  --color-tf12-sky: #7cc4ff;
  --color-tf12-ok: #34d399;
}

@media (prefers-color-scheme: dark) {
  .tf-12:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf12-bg: #07101e;
    --color-tf12-card: #0d1a2d;
    --color-tf12-ink: #e6eefb;
    --color-tf12-muted: #93a3bd;
    --color-tf12-line: #1d2d46;
    --color-tf12-soft: #112138;
    --color-tf12-accent: #5b8cff;
    --color-tf12-on: #04122e;
    --color-tf12-sky: #7cc4ff;
    --color-tf12-ok: #34d399;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-12').forEach((root) => {
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
  const root = document.querySelector('.tf-12');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const steps = [...root.querySelectorAll('.tf-12__step')], names = ['Coverage', 'Details', 'Contact'];
  const BASE = { auto: 92, home: 68, life: 34, renters: 16 }, LEVEL = [0, .72, 1, 1.45], LVL_NAME = ['', 'Basic', 'Standard', 'Premium'];
  let i = 0, shown = [0, 0];
  const range = $('#tf-12-level');
  const type = () => $('[name="tf-12-type"]:checked').value;
  const syncCond = () => root.querySelectorAll('.tf-12__cond').forEach((c) => {
    const on = c.classList.contains('tf-12__cond--' + type());
    c.querySelectorAll('input, select').forEach((f) => { f.disabled = !on; });
  });
  const tween = (lo, hi) => {
    const from = shown.slice(), t0 = performance.now();
    const step = (t) => {
      const k = Math.min(1, (t - t0) / 450), e = 1 - Math.pow(1 - k, 3);
      $('.tf-12__lo').textContent = '$' + Math.round(from[0] + (lo - from[0]) * e);
      $('.tf-12__hi').textContent = '$' + Math.round(from[1] + (hi - from[1]) * e);
      if (k < 1) requestAnimationFrame(step); else shown = [lo, hi];
    };
    requestAnimationFrame(step);
  };
  const estimate = () => {
    const age = Number($('#tf-12-age').value) || 1, lvl = LEVEL[range.value], t = type();
    let base = BASE[t] * age * lvl;
    if (t === 'home') base *= (Number($('#tf-12-hv').value) || 350000) / 350000;
    if (t === 'renters') base *= (Number($('#tf-12-cv').value) || 25000) / 25000;
    if (t === 'life' && $('#tf-12-smk').value === 'Yes') base *= 2.1;
    if (t === 'auto') base *= Math.max(.8, 1 + (2022 - (Number($('#tf-12-yr').value) || 2022)) * -0.01);
    tween(Math.round(base * .88), Math.round(base * 1.18));
  };
  const setRange = () => {
    range.style.setProperty('--fill', ((range.value - 1) / 2) * 100 + '%');
    $('.tf-12__lvl').textContent = LVL_NAME[range.value]; range.setAttribute('aria-valuetext', LVL_NAME[range.value]);
  };
  const show = (n) => {
    i = n; steps.forEach((s, j) => { s.hidden = j !== i; });
    root.dataset.step = i + 1;
    $('.tf-12__stepname').textContent = 'Step ' + (i + 1) + ' of ' + steps.length + ' · ' + names[i];
    $('.tf-12__next').firstChild.textContent = i === steps.length - 1 ? 'Get my quote' : 'Continue';
    const first = steps[i].querySelector('input:not([disabled]), select:not([disabled])'); if (first) first.focus();
  };
  $('.tf-12__next').addEventListener('click', () => {
    const bad = [...steps[i].querySelectorAll('input, select')].find((f) => !f.disabled && !f.checkValidity());
    if (bad) { bad.reportValidity(); return; }
    if (i < steps.length - 1) return show(i + 1);
    steps.forEach((s) => { s.hidden = true; }); root.dataset.step = 4;
    $('.tf-12__stepname').textContent = 'Done';
    const d = $('.tf-12__done'); d.hidden = false; d.focus();
  });
  $('.tf-12__back').addEventListener('click', () => { if (i > 0) show(i - 1); });
  root.addEventListener('input', () => { setRange(); estimate(); });
  root.addEventListener('change', (e) => { if (e.target.name === 'tf-12-type') syncCond(); estimate(); });
  syncCond(); setRange(); estimate();
})();
```

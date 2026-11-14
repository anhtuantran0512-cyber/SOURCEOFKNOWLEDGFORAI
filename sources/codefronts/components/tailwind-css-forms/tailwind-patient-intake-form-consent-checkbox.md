---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-patient-intake-form-consent-checkbox/"
title: "Tailwind Patient Intake Form with Consent Checkbox"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's new-patient intake, ported one-for-one to Tailwind v4 and still accessibility-first: Atkinson Hyperlegible type at 17px, numbered…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Patient Intake Form with Consent Checkbox
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-patient-intake-form-consent-checkbox/

The CSS collection's new-patient intake, ported one-for-one to Tailwind v4 and still accessibility-first: Atkinson Hyperlegible type at 17px, numbered sections that tick themselves off, a live completion meter, a 0–10 pain slider that names the level in words and shifts from green to red, allergy and insurance follow-ups revealed with group-has-[[value=yes]:checked]/q:grid, a consent box unlocked by an IntersectionObserver once read to the end, and a typed signature on a ruled pad.
## HTML
```html
<div class="tf-15 relative block min-h-svh w-full bg-tf15-bg pt-[72px] font-tf15-sans text-[1.0625rem] leading-[normal] text-tf15-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,4vw,3.5rem)]">
    <div class="grid w-full max-w-[44rem] gap-6 rounded-3xl border border-tf15-line bg-tf15-card p-[clamp(1.25rem,5vw,2.5rem)] shadow-[0_30px_70px_-40px_rgba(13,38,36,.45)]" role="form" aria-labelledby="tf-15-title">
      <header class="grid gap-[.6rem]">
        <div class="flex items-center gap-[.55rem] font-bold text-tf15-accent"><span aria-hidden="true" class="grid size-[1.8rem] place-items-center rounded-[.5rem] bg-tf15-accent text-[1.3rem] leading-none text-tf15-on">+</span>Harbor Family Clinic</div>
        <h2 id="tf-15-title" class="mt-[.2rem] text-[clamp(1.6rem,4vw,2.1rem)] font-bold tracking-[-.01em]">New patient intake</h2>
        <p class="leading-[1.5] text-tf15-muted">About 6 minutes. Your information is encrypted and only seen by your care team.</p>
        <div class="mt-[.4rem] flex items-center gap-[.9rem]"><div class="h-2 flex-1 overflow-hidden rounded-full bg-tf15-line" aria-hidden="true"><i class="block h-full origin-left rounded-[inherit] bg-tf15-accent [scale:var(--done,0)_1] [transition:scale_.5s_var(--ease-tf15)] forced-colors:bg-[Highlight]"></i></div><span class="tf-15__pct min-w-[7.5rem] text-right text-[.9rem] font-bold tabular-nums" aria-live="polite">0% complete</span></div>
      </header>
      <section class="tf-15__sec group/sec grid gap-[1.05rem] border-t border-tf15-line pt-[1.4rem]" aria-labelledby="tf-15-s1"><h3 id="tf-15-s1" class="flex items-center gap-[.65rem] text-[1.2rem] font-bold"><span class="grid size-[1.9rem] place-items-center rounded-full border-[1.5px] border-tf15-accent bg-tf15-soft text-[.95rem] text-tf15-accent group-[.is-done]/sec:bg-tf15-accent group-[.is-done]/sec:text-[length:0] group-[.is-done]/sec:text-tf15-on group-[.is-done]/sec:before:text-[.95rem] group-[.is-done]/sec:before:content-['✓']">1</span>About you</h3>
        <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4">
          <div class="grid gap-[.45rem]"><label for="tf-15-fn" class="text-[1rem] font-bold">Legal first name</label><input id="tf-15-fn" autocomplete="given-name" required class="min-h-[3.1rem] w-full rounded-[.75rem] border-2 border-tf15-line bg-tf15-soft px-[.95rem] py-[.7rem] text-tf15-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf15-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf15-accent)_22%,transparent)] focus-visible:outline-none user-invalid:border-tf15-bad"></div>
          <div class="grid gap-[.45rem]"><label for="tf-15-ln" class="text-[1rem] font-bold">Last name</label><input id="tf-15-ln" autocomplete="family-name" required class="min-h-[3.1rem] w-full rounded-[.75rem] border-2 border-tf15-line bg-tf15-soft px-[.95rem] py-[.7rem] text-tf15-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf15-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf15-accent)_22%,transparent)] focus-visible:outline-none user-invalid:border-tf15-bad"></div>
          <div class="grid gap-[.45rem]"><label for="tf-15-dob" class="text-[1rem] font-bold">Date of birth</label><input id="tf-15-dob" type="date" autocomplete="bday" required class="min-h-[3.1rem] w-full rounded-[.75rem] border-2 border-tf15-line bg-tf15-soft px-[.95rem] py-[.7rem] text-tf15-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf15-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf15-accent)_22%,transparent)] focus-visible:outline-none user-invalid:border-tf15-bad"></div>
          <div class="grid gap-[.45rem]"><label for="tf-15-ph" class="text-[1rem] font-bold">Mobile phone</label><input id="tf-15-ph" type="tel" autocomplete="tel" required class="min-h-[3.1rem] w-full rounded-[.75rem] border-2 border-tf15-line bg-tf15-soft px-[.95rem] py-[.7rem] text-tf15-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf15-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf15-accent)_22%,transparent)] focus-visible:outline-none user-invalid:border-tf15-bad"></div>
        </div>
      </section>
      <section class="tf-15__sec group/sec grid gap-[1.05rem] border-t border-tf15-line pt-[1.4rem]" aria-labelledby="tf-15-s2"><h3 id="tf-15-s2" class="flex items-center gap-[.65rem] text-[1.2rem] font-bold"><span class="grid size-[1.9rem] place-items-center rounded-full border-[1.5px] border-tf15-accent bg-tf15-soft text-[.95rem] text-tf15-accent group-[.is-done]/sec:bg-tf15-accent group-[.is-done]/sec:text-[length:0] group-[.is-done]/sec:text-tf15-on group-[.is-done]/sec:before:text-[.95rem] group-[.is-done]/sec:before:content-['✓']">2</span>Today's visit</h3>
        <div class="grid gap-[.45rem]"><label for="tf-15-why" class="text-[1rem] font-bold">Main reason for your visit</label><textarea id="tf-15-why" rows="2" required placeholder="e.g. Persistent cough for two weeks" class="min-h-[3.1rem] w-full rounded-[.75rem] border-2 border-tf15-line bg-tf15-soft px-[.95rem] py-[.7rem] text-tf15-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf15-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf15-accent)_22%,transparent)] focus-visible:outline-none user-invalid:border-tf15-bad resize-y leading-[1.5]"></textarea></div>
        <div class="grid gap-[.45rem]">
          <div class="flex flex-wrap items-baseline justify-between gap-2"><label for="tf-15-pain" class="text-[1rem] font-bold">Current pain level</label><output class="tf-15__painout font-bold text-[var(--pc,var(--color-tf15-accent))]" for="tf-15-pain">0 — No pain</output></div>
          <input id="tf-15-pain" type="range" min="0" max="10" value="0" aria-valuetext="0 — No pain" class="h-11 w-full cursor-pointer appearance-none rounded-[.5rem] bg-transparent [--pc:#16a34a] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tf15-accent [&::-moz-range-thumb]:size-[1.3rem] [&::-moz-range-thumb]:rounded-full [&::-moz-range-thumb]:border-4 [&::-moz-range-thumb]:border-[var(--pc)] [&::-moz-range-thumb]:bg-tf15-card [&::-moz-range-track]:h-[.6rem] [&::-moz-range-track]:rounded-full [&::-moz-range-track]:bg-[linear-gradient(90deg,#16a34a,#eab308_50%,#dc2626)] [&::-webkit-slider-runnable-track]:h-[.6rem] [&::-webkit-slider-runnable-track]:rounded-full [&::-webkit-slider-runnable-track]:bg-[linear-gradient(90deg,#16a34a,#eab308_50%,#dc2626)] [&::-webkit-slider-thumb]:-mt-[.575rem] [&::-webkit-slider-thumb]:size-7 [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:border-4 [&::-webkit-slider-thumb]:border-[var(--pc)] [&::-webkit-slider-thumb]:bg-tf15-card [&::-webkit-slider-thumb]:shadow-[0_3px_8px_rgba(0,0,0,.25)]">
          <div class="-mt-[.4rem] flex justify-between text-[.85rem] text-tf15-muted" aria-hidden="true"><span>0</span><span>5</span><span>10</span></div>
        </div>
      </section>
      <section class="tf-15__sec group/sec grid gap-[1.05rem] border-t border-tf15-line pt-[1.4rem]" aria-labelledby="tf-15-s3"><h3 id="tf-15-s3" class="flex items-center gap-[.65rem] text-[1.2rem] font-bold"><span class="grid size-[1.9rem] place-items-center rounded-full border-[1.5px] border-tf15-accent bg-tf15-soft text-[.95rem] text-tf15-accent group-[.is-done]/sec:bg-tf15-accent group-[.is-done]/sec:text-[length:0] group-[.is-done]/sec:text-tf15-on group-[.is-done]/sec:before:text-[.95rem] group-[.is-done]/sec:before:content-['✓']">3</span>Medical history</h3>
        <fieldset class="group/q grid min-w-0 gap-[.8rem]">
          <legend class="mb-[.6rem] p-0 text-[1rem] font-bold">Do you have any allergies to medicines, foods or latex?</legend>
          <div class="flex flex-wrap gap-2"><label class="relative text-[1rem] font-bold"><input type="radio" name="tf-15-al" value="no" required class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-12 min-w-28 items-center gap-[.55rem] rounded-[.75rem] border-2 border-tf15-line px-[1.1rem] font-bold transition-all duration-200 before:size-[1.1rem] before:rounded-full before:border-2 before:border-tf15-muted before:[transition:border_.2s_var(--ease-tf15)] before:content-[''] peer-checked:border-tf15-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf15-accent)_9%,var(--color-tf15-card))] peer-checked:before:border-[6px] peer-checked:before:border-tf15-accent peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf15-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">No</span></label><label class="relative text-[1rem] font-bold"><input type="radio" name="tf-15-al" value="yes" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-12 min-w-28 items-center gap-[.55rem] rounded-[.75rem] border-2 border-tf15-line px-[1.1rem] font-bold transition-all duration-200 before:size-[1.1rem] before:rounded-full before:border-2 before:border-tf15-muted before:[transition:border_.2s_var(--ease-tf15)] before:content-[''] peer-checked:border-tf15-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf15-accent)_9%,var(--color-tf15-card))] peer-checked:before:border-[6px] peer-checked:before:border-tf15-accent peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf15-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Yes</span></label></div>
          <div class="hidden gap-[.45rem] group-has-[[value=yes]:checked]/q:grid group-has-[[value=yes]:checked]/q:animate-tf15-in"><label for="tf-15-ald" class="text-[1rem] font-bold">Please list them and the reaction</label><textarea id="tf-15-ald" rows="2" placeholder="e.g. Penicillin — hives" class="min-h-[3.1rem] w-full rounded-[.75rem] border-2 border-tf15-line bg-tf15-soft px-[.95rem] py-[.7rem] text-tf15-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf15-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf15-accent)_22%,transparent)] focus-visible:outline-none user-invalid:border-tf15-bad resize-y leading-[1.5]"></textarea></div>
        </fieldset>
        <fieldset class="flex min-w-0 flex-wrap gap-2"><legend class="mb-[.6rem] p-0 text-[1rem] font-bold w-full">Ongoing conditions <span class="text-[.9rem] font-normal text-tf15-muted">Select any</span></legend>
          <label class="relative text-[1rem] font-bold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-11 items-center gap-[.4rem] rounded-full border-2 border-tf15-line px-4 text-[.95rem] font-normal transition-all duration-200 peer-checked:border-tf15-accent peer-checked:bg-tf15-accent peer-checked:text-tf15-on peer-checked:before:content-['✓'] peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf15-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Asthma</span></label><label class="relative text-[1rem] font-bold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-11 items-center gap-[.4rem] rounded-full border-2 border-tf15-line px-4 text-[.95rem] font-normal transition-all duration-200 peer-checked:border-tf15-accent peer-checked:bg-tf15-accent peer-checked:text-tf15-on peer-checked:before:content-['✓'] peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf15-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Diabetes</span></label><label class="relative text-[1rem] font-bold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-11 items-center gap-[.4rem] rounded-full border-2 border-tf15-line px-4 text-[.95rem] font-normal transition-all duration-200 peer-checked:border-tf15-accent peer-checked:bg-tf15-accent peer-checked:text-tf15-on peer-checked:before:content-['✓'] peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf15-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">High blood pressure</span></label><label class="relative text-[1rem] font-bold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-11 items-center gap-[.4rem] rounded-full border-2 border-tf15-line px-4 text-[.95rem] font-normal transition-all duration-200 peer-checked:border-tf15-accent peer-checked:bg-tf15-accent peer-checked:text-tf15-on peer-checked:before:content-['✓'] peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf15-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Heart condition</span></label><label class="relative text-[1rem] font-bold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-11 items-center gap-[.4rem] rounded-full border-2 border-tf15-line px-4 text-[.95rem] font-normal transition-all duration-200 peer-checked:border-tf15-accent peer-checked:bg-tf15-accent peer-checked:text-tf15-on peer-checked:before:content-['✓'] peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf15-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Anxiety / depression</span></label>
        </fieldset>
      </section>
      <section class="tf-15__sec group/sec grid gap-[1.05rem] border-t border-tf15-line pt-[1.4rem]" aria-labelledby="tf-15-s4"><h3 id="tf-15-s4" class="flex items-center gap-[.65rem] text-[1.2rem] font-bold"><span class="grid size-[1.9rem] place-items-center rounded-full border-[1.5px] border-tf15-accent bg-tf15-soft text-[.95rem] text-tf15-accent group-[.is-done]/sec:bg-tf15-accent group-[.is-done]/sec:text-[length:0] group-[.is-done]/sec:text-tf15-on group-[.is-done]/sec:before:text-[.95rem] group-[.is-done]/sec:before:content-['✓']">4</span>Insurance</h3>
        <fieldset class="group/q grid min-w-0 gap-[.8rem]">
          <legend class="mb-[.6rem] p-0 text-[1rem] font-bold">How will you pay for today's visit?</legend>
          <div class="flex flex-wrap gap-2"><label class="relative text-[1rem] font-bold"><input type="radio" name="tf-15-ins" value="yes" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-12 min-w-28 items-center gap-[.55rem] rounded-[.75rem] border-2 border-tf15-line px-[1.1rem] font-bold transition-all duration-200 before:size-[1.1rem] before:rounded-full before:border-2 before:border-tf15-muted before:[transition:border_.2s_var(--ease-tf15)] before:content-[''] peer-checked:border-tf15-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf15-accent)_9%,var(--color-tf15-card))] peer-checked:before:border-[6px] peer-checked:before:border-tf15-accent peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf15-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Insurance</span></label><label class="relative text-[1rem] font-bold"><input type="radio" name="tf-15-ins" value="self" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-12 min-w-28 items-center gap-[.55rem] rounded-[.75rem] border-2 border-tf15-line px-[1.1rem] font-bold transition-all duration-200 before:size-[1.1rem] before:rounded-full before:border-2 before:border-tf15-muted before:[transition:border_.2s_var(--ease-tf15)] before:content-[''] peer-checked:border-tf15-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf15-accent)_9%,var(--color-tf15-card))] peer-checked:before:border-[6px] peer-checked:before:border-tf15-accent peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf15-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Self-pay</span></label></div>
          <div class="hidden gap-[.45rem] group-has-[[value=yes]:checked]/q:grid group-has-[[value=yes]:checked]/q:animate-tf15-in grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4">
            <div class="grid gap-[.45rem]"><label for="tf-15-prov" class="text-[1rem] font-bold">Insurance provider</label><input id="tf-15-prov" placeholder="e.g. Aetna, BUPA, Medibank" class="min-h-[3.1rem] w-full rounded-[.75rem] border-2 border-tf15-line bg-tf15-soft px-[.95rem] py-[.7rem] text-tf15-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf15-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf15-accent)_22%,transparent)] focus-visible:outline-none user-invalid:border-tf15-bad"></div>
            <div class="grid gap-[.45rem]"><label for="tf-15-mem" class="text-[1rem] font-bold">Member ID</label><input id="tf-15-mem" spellcheck="false" class="min-h-[3.1rem] w-full rounded-[.75rem] border-2 border-tf15-line bg-tf15-soft px-[.95rem] py-[.7rem] text-tf15-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf15-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf15-accent)_22%,transparent)] focus-visible:outline-none user-invalid:border-tf15-bad"></div>
          </div>
        </fieldset>
      </section>
      <section class="tf-15__sec group/sec grid gap-[1.05rem] border-t border-tf15-line pt-[1.4rem]" aria-labelledby="tf-15-s5"><h3 id="tf-15-s5" class="flex items-center gap-[.65rem] text-[1.2rem] font-bold"><span class="grid size-[1.9rem] place-items-center rounded-full border-[1.5px] border-tf15-accent bg-tf15-soft text-[.95rem] text-tf15-accent group-[.is-done]/sec:bg-tf15-accent group-[.is-done]/sec:text-[length:0] group-[.is-done]/sec:text-tf15-on group-[.is-done]/sec:before:text-[.95rem] group-[.is-done]/sec:before:content-['✓']">5</span>Consent</h3>
        <div class="tf-15__terms max-h-44 overflow-auto rounded-[.9rem] border-2 border-tf15-line bg-tf15-soft px-[1.15rem] py-4 text-[.95rem] leading-[1.6] [scrollbar-gutter:stable] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tf15-accent [&_h4]:mt-[.9rem] [&_h4]:mb-[.25rem] [&_h4]:text-[1rem] [&_h4]:font-bold [&_h4:first-child]:mt-0 [&_p]:text-tf15-muted" tabindex="0" role="region" aria-label="Consent to treatment and privacy notice">
          <h4>Consent to treatment</h4>
          <p>I consent to examination and treatment by the clinicians of Harbor Family Clinic, including routine diagnostic procedures. I understand I may ask questions and refuse any part of my care at any time.</p>
          <h4>Use of health information</h4>
          <p>My health information will be used to provide care, arrange payment and run clinic operations, as described in the Notice of Privacy Practices. It will not be sold or used for marketing.</p>
          <h4>Financial responsibility</h4>
          <p>I am responsible for charges not covered by my insurer, including co-pays and deductibles. Missed appointments without 24 hours' notice may incur a fee.</p>
          <h4>Communication</h4>
          <p>The clinic may contact me by phone, SMS or email for reminders and results. I can change these preferences at any time.</p>
          <span class="tf-15__end block h-px" aria-hidden="true"></span>
        </div>
        <p class="tf-15__scrollhint -mt-[.4rem] text-[.9rem] font-bold text-tf15-warn [&.is-ok]:text-tf15-accent" aria-live="polite">Scroll to the end of the consent text to continue.</p>
        <label class="flex cursor-pointer items-start gap-3 rounded-[.9rem] border-2 border-tf15-line p-4 text-[1rem] font-bold [transition:border-color_.2s,background_.2s] has-checked:border-tf15-accent has-checked:bg-[color-mix(in_oklab,var(--color-tf15-accent)_7%,var(--color-tf15-card))] has-disabled:cursor-not-allowed has-disabled:opacity-55"><input type="checkbox" id="tf-15-consent" disabled required class="mt-[.05rem] size-[1.4rem] flex-none accent-tf15-accent"><span>I have read and agree to the consent and privacy notice above.</span></label>
        <div class="grid gap-[.45rem]"><label for="tf-15-sig" class="text-[1rem] font-bold">Type your full name as signature</label><input id="tf-15-sig" required autocomplete="name" class="min-h-[3.1rem] w-full rounded-[.75rem] border-2 border-tf15-line bg-tf15-soft px-[.95rem] py-[.7rem] text-tf15-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf15-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf15-accent)_22%,transparent)] focus-visible:outline-none user-invalid:border-tf15-bad"></div>
        <div class="relative flex min-h-20 items-end justify-between border-b-2 border-tf15-ink [background:repeating-linear-gradient(transparent_0_1.95rem,color-mix(in_oklab,var(--color-tf15-line)_70%,transparent)_1.95rem_2rem)] px-4 pt-2 pb-[.6rem] before:absolute before:bottom-[.6rem] before:left-[.2rem] before:text-[.9rem] before:text-tf15-muted before:content-['✕']" aria-hidden="true"><span class="tf-15__sigtext pl-4 font-tf15-script text-[2.4rem] leading-none font-medium text-tf15-accent opacity-35 [&.is-on]:opacity-100">Your signature</span><small class="tf-15__sigdate text-[.85rem] text-tf15-muted"></small></div>
      </section>
      <button type="button" class="tf-15__submit min-h-[3.4rem] cursor-pointer rounded-[.9rem] border-0 bg-tf15-accent text-[1.1rem] font-bold text-tf15-on [transition:opacity_.2s,translate_.2s_var(--ease-tf15)] [.tf-15:not(:has(#tf-15-consent:checked))_&]:opacity-50 hover:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tf15-ink forced-colors:border-2 forced-colors:border-[ButtonText]">Submit intake form</button>
      <p class="tf-15__status -mt-[.6rem] text-center font-bold empty:hidden data-[ok=false]:text-tf15-bad data-[ok=true]:text-tf15-accent" role="status"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf15-bg: #eaf3f2;
  --color-tf15-card: #ffffff;
  --color-tf15-ink: #0d2624;
  --color-tf15-muted: #4a6461;
  --color-tf15-line: #d3e3e1;
  --color-tf15-soft: #f3f9f8;
  --color-tf15-accent: #0f766e;
  --color-tf15-on: #fff;
  --color-tf15-warn: #b45309;
  --color-tf15-bad: #b91c1c;
  --font-tf15-sans: "Atkinson Hyperlegible", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-tf15-script: "Caveat", "Brush Script MT", cursive;
  --ease-tf15: cubic-bezier(0.16,1,0.3,1);
  --animate-tf15-in: tf15-in 0.35s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf15-in {
    from {
      opacity: 0;
      translate: 0 -6px;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-15[data-theme="dark"] {
  color-scheme: dark;
  --color-tf15-bg: #071312;
  --color-tf15-card: #0d1d1c;
  --color-tf15-ink: #e3f2f0;
  --color-tf15-muted: #9ab8b4;
  --color-tf15-line: #1f3533;
  --color-tf15-soft: #112624;
  --color-tf15-accent: #2dd4bf;
  --color-tf15-on: #032220;
  --color-tf15-warn: #fbbf24;
  --color-tf15-bad: #f87171;
}

@media (prefers-color-scheme: dark) {
  .tf-15:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf15-bg: #071312;
    --color-tf15-card: #0d1d1c;
    --color-tf15-ink: #e3f2f0;
    --color-tf15-muted: #9ab8b4;
    --color-tf15-line: #1f3533;
    --color-tf15-soft: #112624;
    --color-tf15-accent: #2dd4bf;
    --color-tf15-on: #032220;
    --color-tf15-warn: #fbbf24;
    --color-tf15-bad: #f87171;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-15').forEach((root) => {
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
  const root = document.querySelector('.tf-15');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const PAIN = ['No pain', 'Very mild', 'Mild', 'Uncomfortable', 'Moderate', 'Distracting', 'Moderate to severe', 'Severe', 'Very severe', 'Intense', 'Worst imaginable'];
  const pain = $('#tf-15-pain'), out = $('.tf-15__painout');
  const setPain = () => {
    const v = Number(pain.value), hue = 140 - v * 14, c = 'hsl(' + hue + ' 75% 38%)';
    out.textContent = v + ' — ' + PAIN[v]; pain.setAttribute('aria-valuetext', out.textContent);
    pain.style.setProperty('--pc', c); out.style.setProperty('--pc', c);
  };
  pain.addEventListener('input', setPain); setPain();
  const consent = $('#tf-15-consent'), hint = $('.tf-15__scrollhint'), terms = $('.tf-15__terms');
  new IntersectionObserver(([e]) => {
    if (e.isIntersecting && consent.disabled) { consent.disabled = false; hint.textContent = 'Thanks for reading — you can now give consent.'; hint.classList.add('is-ok'); }
  }, { root: terms, threshold: 1 }).observe($('.tf-15__end'));
  const sig = $('#tf-15-sig'), sigText = $('.tf-15__sigtext');
  $('.tf-15__sigdate').textContent = new Intl.DateTimeFormat('en-US', { dateStyle: 'medium' }).format(new Date());
  sig.addEventListener('input', () => { sigText.textContent = sig.value || 'Your signature'; sigText.classList.toggle('is-on', !!sig.value); });
  const secs = [...root.querySelectorAll('.tf-15__sec')];
  const progress = () => {
    let done = 0, total = 0;
    secs.forEach((s) => {
      const req = [...s.querySelectorAll('[required]')], seen = new Set();
      const ok = req.filter((f) => { if (f.type === 'radio') { if (seen.has(f.name)) return false; seen.add(f.name); return !!s.querySelector('[name="' + f.name + '"]:checked'); } return f.type === 'checkbox' ? f.checked : f.value.trim() && f.checkValidity(); }).length;
      const count = req.filter((f) => f.type !== 'radio').length + seen.size || 1;
      total += req.length ? count : 0; done += ok;
      s.classList.toggle('is-done', !req.length ? false : ok === count);
    });
    const pct = total ? Math.round((done / total) * 100) : 0;
    root.style.setProperty('--done', pct / 100); $('.tf-15__pct').textContent = pct + '% complete';
  };
  root.addEventListener('input', progress); root.addEventListener('change', progress); progress();
  $('.tf-15__submit').addEventListener('click', () => {
    const status = $('.tf-15__status');
    const bad = [...root.querySelectorAll('[required]')].find((f) => f.type === 'radio' ? !root.querySelector('[name="' + f.name + '"]:checked') : !f.checkValidity());
    if (bad) { status.dataset.ok = 'false'; status.textContent = consent.disabled ? 'Please read the consent text to the end.' : 'A few required answers are missing.'; (consent.disabled ? terms : bad).focus(); return; }
    status.dataset.ok = 'true'; status.textContent = 'Submitted securely. Please arrive 10 minutes early — see you soon.';
  });
})();
```

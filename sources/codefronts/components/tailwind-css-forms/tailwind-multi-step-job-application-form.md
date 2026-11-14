---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-multi-step-job-application-form/"
title: "Tailwind Multi-Step Job Application Form"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's careers application, ported one-for-one to Tailwind v4: a photo job header, three calm steps — About you, Résumé, Final questions — with…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Step Job Application Form
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-multi-step-job-application-form/

The CSS collection's careers application, ported one-for-one to Tailwind v4: a photo job header, three calm steps — About you, Résumé, Final questions — with a step indicator that is a real ordered list carrying aria-current="step", per-step native validation, a résumé drop zone limited to PDF/DOC/DOCX under 5 MB that turns into a file card via group-has-[input:valid]/rs:, work-authorisation radio cards and a review summary before submit.
## HTML
```html
<div class="tf-08 relative block min-h-svh w-full bg-tf08-bg pt-[72px] font-tf08-sans leading-[normal] text-tf08-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!" data-step="1">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,5vw,4rem)]">
    <div class="w-full max-w-[42rem] overflow-hidden rounded-[1.75rem] border border-tf08-line bg-tf08-card shadow-[0_30px_70px_-40px_rgba(70,35,10,.5)]">
      <header class="relative grid">
        <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=900&h=360&fit=crop&auto=format&q=70" width="900" height="360" alt="Product team collaborating around a table with laptops" loading="lazy" decoding="async" class="h-48 w-full bg-[#c9b49c] object-cover [grid-area:1/1]">
        <div class="self-end bg-[linear-gradient(transparent,rgba(30,15,5,.85))] px-[clamp(1.25rem,5vw,2.25rem)] py-6 text-white [grid-area:1/1]">
          <p class="mb-[.35rem] text-[.8rem] font-semibold tracking-[.08em] uppercase opacity-85">Fieldnote · Design team</p>
          <h2 class="font-tf08-serif text-[clamp(1.6rem,5vw,2.2rem)] leading-[1.1] font-normal tracking-[-.01em]">Senior Product Designer</h2>
          <ul class="mt-[.8rem] flex list-none flex-wrap gap-[.4rem]" aria-label="Job details"><li class="rounded-full bg-white/18 px-[.65rem] py-[.3rem] text-[.78rem] font-semibold backdrop-blur-sm">Remote · US / UK</li><li class="rounded-full bg-white/18 px-[.65rem] py-[.3rem] text-[.78rem] font-semibold backdrop-blur-sm">Full-time</li><li class="rounded-full bg-white/18 px-[.65rem] py-[.3rem] text-[.78rem] font-semibold backdrop-blur-sm">$145k–$175k</li></ul>
        </div>
      </header>
      <ol class="tf-08__steps grid list-none grid-cols-3 gap-2 border-b border-tf08-line px-[clamp(1.25rem,5vw,2.25rem)] py-[1.1rem]" aria-label="Application progress">
        <li aria-current="step" class="group/li relative flex items-center gap-[.55rem] text-[.85rem] font-semibold text-tf08-muted not-last:after:mx-1 not-last:after:h-0.5 not-last:after:flex-1 not-last:after:rounded-[2px] not-last:after:bg-tf08-line not-last:after:content-[''] aria-[current=step]:text-tf08-ink max-[34rem]:gap-0 max-[34rem]:text-[length:0] max-[34rem]:aria-[current=step]:gap-[.55rem] max-[34rem]:aria-[current=step]:text-[.85rem] [&.is-done]:after:bg-tf08-accent"><span class="grid size-7 flex-none place-items-center rounded-full border-[1.5px] border-tf08-line bg-tf08-card text-[.8rem] [transition:all_.3s_var(--ease-tf08)] group-aria-[current=step]/li:border-tf08-accent group-aria-[current=step]/li:text-tf08-accent group-aria-[current=step]/li:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_15%,transparent)] group-[.is-done]/li:border-tf08-accent group-[.is-done]/li:bg-tf08-accent group-[.is-done]/li:text-[length:0] group-[.is-done]/li:text-tf08-on group-[.is-done]/li:before:text-[.8rem] group-[.is-done]/li:before:content-['✓'] forced-colors:group-[.is-done]/li:bg-[Highlight] forced-colors:group-[.is-done]/li:text-[HighlightText]">1</span>About you</li>
        <li class="group/li relative flex items-center gap-[.55rem] text-[.85rem] font-semibold text-tf08-muted not-last:after:mx-1 not-last:after:h-0.5 not-last:after:flex-1 not-last:after:rounded-[2px] not-last:after:bg-tf08-line not-last:after:content-[''] aria-[current=step]:text-tf08-ink max-[34rem]:gap-0 max-[34rem]:text-[length:0] max-[34rem]:aria-[current=step]:gap-[.55rem] max-[34rem]:aria-[current=step]:text-[.85rem] [&.is-done]:after:bg-tf08-accent"><span class="grid size-7 flex-none place-items-center rounded-full border-[1.5px] border-tf08-line bg-tf08-card text-[.8rem] [transition:all_.3s_var(--ease-tf08)] group-aria-[current=step]/li:border-tf08-accent group-aria-[current=step]/li:text-tf08-accent group-aria-[current=step]/li:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_15%,transparent)] group-[.is-done]/li:border-tf08-accent group-[.is-done]/li:bg-tf08-accent group-[.is-done]/li:text-[length:0] group-[.is-done]/li:text-tf08-on group-[.is-done]/li:before:text-[.8rem] group-[.is-done]/li:before:content-['✓'] forced-colors:group-[.is-done]/li:bg-[Highlight] forced-colors:group-[.is-done]/li:text-[HighlightText]">2</span>Résumé</li>
        <li class="group/li relative flex items-center gap-[.55rem] text-[.85rem] font-semibold text-tf08-muted not-last:after:mx-1 not-last:after:h-0.5 not-last:after:flex-1 not-last:after:rounded-[2px] not-last:after:bg-tf08-line not-last:after:content-[''] aria-[current=step]:text-tf08-ink max-[34rem]:gap-0 max-[34rem]:text-[length:0] max-[34rem]:aria-[current=step]:gap-[.55rem] max-[34rem]:aria-[current=step]:text-[.85rem] [&.is-done]:after:bg-tf08-accent"><span class="grid size-7 flex-none place-items-center rounded-full border-[1.5px] border-tf08-line bg-tf08-card text-[.8rem] [transition:all_.3s_var(--ease-tf08)] group-aria-[current=step]/li:border-tf08-accent group-aria-[current=step]/li:text-tf08-accent group-aria-[current=step]/li:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_15%,transparent)] group-[.is-done]/li:border-tf08-accent group-[.is-done]/li:bg-tf08-accent group-[.is-done]/li:text-[length:0] group-[.is-done]/li:text-tf08-on group-[.is-done]/li:before:text-[.8rem] group-[.is-done]/li:before:content-['✓'] forced-colors:group-[.is-done]/li:bg-[Highlight] forced-colors:group-[.is-done]/li:text-[HighlightText]">3</span>Final questions</li>
      </ol>
      <div class="grid gap-5 p-[clamp(1.25rem,5vw,2.25rem)]" role="form" aria-label="Job application">
        <fieldset class="tf-08__step grid min-w-0 animate-tf08-step gap-[1.05rem]" data-i="1">
          <legend tabindex="-1" class="mb-[.3rem] p-0 font-tf08-serif text-[1.45rem] font-normal outline-none">About you</legend>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4">
            <div class="grid gap-[.4rem]"><label for="tf-08-fn" class="text-[.86rem] font-semibold">First name</label><input id="tf-08-fn" autocomplete="given-name" required class="min-h-12 w-full rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[.95rem] py-[.7rem] text-[1rem] text-tf08-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf08),background_.2s] focus-visible:border-tf08-accent focus-visible:bg-tf08-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf08-bad"></div>
            <div class="grid gap-[.4rem]"><label for="tf-08-ln" class="text-[.86rem] font-semibold">Last name</label><input id="tf-08-ln" autocomplete="family-name" required class="min-h-12 w-full rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[.95rem] py-[.7rem] text-[1rem] text-tf08-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf08),background_.2s] focus-visible:border-tf08-accent focus-visible:bg-tf08-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf08-bad"></div>
          </div>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4">
            <div class="grid gap-[.4rem]"><label for="tf-08-em" class="text-[.86rem] font-semibold">Email</label><input id="tf-08-em" type="email" autocomplete="email" required class="min-h-12 w-full rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[.95rem] py-[.7rem] text-[1rem] text-tf08-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf08),background_.2s] focus-visible:border-tf08-accent focus-visible:bg-tf08-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf08-bad"></div>
            <div class="grid gap-[.4rem]"><label for="tf-08-ph" class="text-[.86rem] font-semibold">Phone</label><input id="tf-08-ph" type="tel" autocomplete="tel" placeholder="+1 555 010 1234" class="min-h-12 w-full rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[.95rem] py-[.7rem] text-[1rem] text-tf08-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf08),background_.2s] focus-visible:border-tf08-accent focus-visible:bg-tf08-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf08-bad"></div>
          </div>
          <div class="grid gap-[.4rem]"><label for="tf-08-loc" class="text-[.86rem] font-semibold">Current location</label><input id="tf-08-loc" autocomplete="address-level2" placeholder="City, country" required class="min-h-12 w-full rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[.95rem] py-[.7rem] text-[1rem] text-tf08-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf08),background_.2s] focus-visible:border-tf08-accent focus-visible:bg-tf08-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf08-bad"></div>
          <div class="grid gap-[.4rem]"><label for="tf-08-li" class="text-[.86rem] font-semibold">LinkedIn or portfolio URL</label><input id="tf-08-li" type="url" placeholder="https://" autocomplete="url" class="min-h-12 w-full rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[.95rem] py-[.7rem] text-[1rem] text-tf08-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf08),background_.2s] focus-visible:border-tf08-accent focus-visible:bg-tf08-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf08-bad"></div>
        </fieldset>
        <fieldset class="tf-08__step grid min-w-0 animate-tf08-step gap-[1.05rem]" data-i="2" hidden>
          <legend tabindex="-1" class="mb-[.3rem] p-0 font-tf08-serif text-[1.45rem] font-normal outline-none">Résumé</legend>
          <div class="group/rs">
            <label class="relative grid cursor-pointer justify-items-center gap-[.35rem] rounded-[1.1rem] border-[1.5px] border-dashed border-[color-mix(in_oklab,var(--color-tf08-accent)_45%,var(--color-tf08-line))] bg-[color-mix(in_oklab,var(--color-tf08-accent)_4%,var(--color-tf08-soft))] px-4 py-8 text-center [transition:background_.2s,border-color_.2s] group-has-[input:valid]/rs:hidden focus-within:outline-2 focus-within:outline-offset-3 focus-within:outline-tf08-accent hover:bg-[color-mix(in_oklab,var(--color-tf08-accent)_9%,var(--color-tf08-soft))] text-[.86rem] font-semibold">
              <input type="file" id="tf-08-cv" accept=".pdf,.doc,.docx" required aria-describedby="tf-08-cv-hint" class="absolute inset-0 w-full cursor-pointer opacity-0">
              <span aria-hidden="true"><svg viewBox="0 0 24 24" class="size-[2.2rem] fill-none stroke-tf08-accent stroke-[1.5] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5Z"/><path d="M14 3v5h5M12 17v-6M9.5 13.5 12 11l2.5 2.5"/></svg></span>
              <b>Upload your résumé</b>
              <span id="tf-08-cv-hint" class="text-[.82rem] font-normal text-tf08-muted">PDF, DOC or DOCX · max 5 MB</span>
            </label>
            <div class="hidden animate-tf08-file grid-cols-[auto_1fr_auto] items-center gap-[.9rem] rounded-[1.1rem] border border-tf08-line bg-tf08-soft p-4 group-has-[input:valid]/rs:grid">
              <span class="tf-08__ficon grid h-[3.25rem] w-11 place-items-center rounded-[.5rem] bg-tf08-accent text-[.7rem] font-bold tracking-[.05em] text-tf08-on [clip-path:polygon(0_0,72%_0,100%_22%,100%_100%,0_100%)]" aria-hidden="true">PDF</span>
              <div><b class="tf-08__fname block text-[.95rem] break-all">resume.pdf</b><small class="tf-08__fsize text-[.8rem] text-tf08-muted">—</small></div>
              <div class="flex gap-1"><label for="tf-08-cv" class="inline-flex min-h-10 cursor-pointer items-center rounded-[.6rem] border-0 bg-transparent px-[.7rem] font-semibold text-tf08-accent hover:bg-tf08-accent/10 focus-visible:outline-2 focus-visible:outline-tf08-accent text-[.86rem]">Replace</label><button type="button" class="tf-08__rm inline-flex min-h-10 cursor-pointer items-center rounded-[.6rem] border-0 bg-transparent px-[.7rem] font-semibold text-tf08-accent hover:bg-tf08-accent/10 focus-visible:outline-2 focus-visible:outline-tf08-accent text-[.85rem]">Remove</button></div>
            </div>
          </div>
          <p class="tf-08__msg -mt-[.4rem] text-[.82rem] text-tf08-bad empty:hidden" aria-live="polite"></p>
          <div class="grid gap-[.4rem]"><label for="tf-08-cl" class="text-[.86rem] font-semibold">Cover letter <span class="font-normal text-tf08-muted">Optional</span></label><textarea id="tf-08-cl" rows="5" placeholder="Tell us about a product decision you're proud of and why." class="min-h-12 w-full rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[.95rem] py-[.7rem] text-[1rem] text-tf08-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf08),background_.2s] focus-visible:border-tf08-accent focus-visible:bg-tf08-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf08-bad resize-y leading-[1.55]"></textarea></div>
        </fieldset>
        <fieldset class="tf-08__step grid min-w-0 animate-tf08-step gap-[1.05rem]" data-i="3" hidden>
          <legend tabindex="-1" class="mb-[.3rem] p-0 font-tf08-serif text-[1.45rem] font-normal outline-none">Final questions</legend>
          <fieldset class="flex flex-wrap gap-2">
            <legend class="mb-[.55rem] text-[.86rem] font-semibold">Are you authorised to work in the US or UK?</legend>
            <label class="relative text-[.86rem] font-semibold"><input type="radio" name="tf-08-auth" value="Yes" required class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.9rem] items-center gap-[.55rem] rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[1.1rem] font-medium transition-all duration-200 before:size-4 before:rounded-full before:border-[1.5px] before:border-tf08-muted before:[transition:border_.25s_var(--ease-tf08)] before:content-[''] peer-checked:border-tf08-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf08-accent)_8%,var(--color-tf08-card))] peer-checked:before:border-[5px] peer-checked:before:border-tf08-accent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf08-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Yes</span></label>
            <label class="relative text-[.86rem] font-semibold"><input type="radio" name="tf-08-auth" value="Requires sponsorship" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.9rem] items-center gap-[.55rem] rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[1.1rem] font-medium transition-all duration-200 before:size-4 before:rounded-full before:border-[1.5px] before:border-tf08-muted before:[transition:border_.25s_var(--ease-tf08)] before:content-[''] peer-checked:border-tf08-accent peer-checked:bg-[color-mix(in_oklab,var(--color-tf08-accent)_8%,var(--color-tf08-card))] peer-checked:before:border-[5px] peer-checked:before:border-tf08-accent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf08-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">I'll need sponsorship</span></label>
          </fieldset>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4">
            <div class="grid gap-[.4rem]"><label for="tf-08-start" class="text-[.86rem] font-semibold">Earliest start date</label><input id="tf-08-start" type="date" required class="min-h-12 w-full rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[.95rem] py-[.7rem] text-[1rem] text-tf08-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf08),background_.2s] focus-visible:border-tf08-accent focus-visible:bg-tf08-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf08-bad"></div>
            <div class="grid gap-[.4rem]"><label for="tf-08-src" class="text-[.86rem] font-semibold">How did you hear about us?</label><select id="tf-08-src" class="min-h-12 w-full rounded-[.8rem] border border-tf08-line bg-tf08-soft px-[.95rem] py-[.7rem] text-[1rem] text-tf08-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf08),background_.2s] focus-visible:border-tf08-accent focus-visible:bg-tf08-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf08-accent)_18%,transparent)] focus-visible:outline-none user-invalid:border-tf08-bad"><option>LinkedIn</option><option>Referral</option><option>Company website</option><option>Dribbble</option><option>Other</option></select></div>
          </div>
          <div class="rounded-2xl border border-tf08-line bg-tf08-soft px-5 py-[1.1rem]" aria-label="Review your application">
            <h3 class="mb-[.6rem] font-tf08-serif text-[1.05rem] font-normal">Review</h3>
            <dl class="grid gap-[.4rem]"><div class="flex justify-between gap-4 text-[.9rem]"><dt class="text-tf08-muted">Name</dt><dd class="text-right font-semibold break-words" data-review="name"></dd></div><div class="flex justify-between gap-4 text-[.9rem]"><dt class="text-tf08-muted">Email</dt><dd class="text-right font-semibold break-words" data-review="email"></dd></div><div class="flex justify-between gap-4 text-[.9rem]"><dt class="text-tf08-muted">Résumé</dt><dd class="text-right font-semibold break-words" data-review="cv"></dd></div></dl>
          </div>
        </fieldset>
        <div class="tf-08__done grid animate-tf08-done justify-items-center gap-[.4rem] py-6 text-center outline-none" hidden tabindex="-1">
          <span aria-hidden="true" class="grid size-[3.75rem] place-items-center rounded-full bg-tf08-ok text-[1.6rem] font-bold text-white">✓</span><h3 class="mt-[.6rem] font-tf08-serif text-[1.6rem] font-normal">Application received</h3><p class="text-tf08-muted">We'll review it within 5 working days. Keep an eye on your inbox.</p>
        </div>
        <div class="flex justify-between gap-3 border-t border-tf08-line pt-[1.1rem] in-[.is-sent]:hidden">
          <button type="button" class="tf-08__back min-h-12 cursor-pointer rounded-[.85rem] px-[1.4rem] font-semibold [transition:translate_.2s_var(--ease-tf08),filter_.2s,background_.2s] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf08-ink border border-tf08-line bg-transparent text-tf08-ink hover:bg-tf08-soft in-data-[step=1]:invisible">Back</button>
          <button type="button" class="tf-08__next min-h-12 cursor-pointer rounded-[.85rem] px-[1.4rem] font-semibold [transition:translate_.2s_var(--ease-tf08),filter_.2s,background_.2s] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf08-ink ml-auto border-0 bg-tf08-accent text-tf08-on shadow-[0_10px_22px_-12px_var(--color-tf08-accent)] hover:-translate-y-0.5 hover:brightness-106 forced-colors:border forced-colors:border-[ButtonText]">Continue</button>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf08-bg: #f5efe6;
  --color-tf08-card: #fffcf7;
  --color-tf08-ink: #2a1d15;
  --color-tf08-muted: #7a6758;
  --color-tf08-line: #eadfce;
  --color-tf08-soft: #f8f2e8;
  --color-tf08-accent: #c2502b;
  --color-tf08-on: #fff;
  --color-tf08-ok: #3f7d4e;
  --color-tf08-bad: #b42318;
  --font-tf08-serif: "Young Serif", ui-serif, Georgia, serif;
  --font-tf08-sans: "Hanken Grotesk", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf08: cubic-bezier(0.16,1,0.3,1);
  --animate-tf08-step: tf08-in 0.45s cubic-bezier(0.16,1,0.3,1);
  --animate-tf08-file: tf08-in 0.4s cubic-bezier(0.16,1,0.3,1);
  --animate-tf08-done: tf08-in 0.5s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf08-in {
    from {
      opacity: 0;
      translate: 14px 0;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-08[data-theme="dark"] {
  color-scheme: dark;
  --color-tf08-bg: #17110d;
  --color-tf08-card: #1f1813;
  --color-tf08-ink: #f4e9dc;
  --color-tf08-muted: #b19c88;
  --color-tf08-line: #3a2d23;
  --color-tf08-soft: #271e17;
  --color-tf08-accent: #f07a4f;
  --color-tf08-on: #2a0f04;
  --color-tf08-ok: #7bc58b;
  --color-tf08-bad: #ff8a7a;
}

@media (prefers-color-scheme: dark) {
  .tf-08:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf08-bg: #17110d;
    --color-tf08-card: #1f1813;
    --color-tf08-ink: #f4e9dc;
    --color-tf08-muted: #b19c88;
    --color-tf08-line: #3a2d23;
    --color-tf08-soft: #271e17;
    --color-tf08-accent: #f07a4f;
    --color-tf08-on: #2a0f04;
    --color-tf08-ok: #7bc58b;
    --color-tf08-bad: #ff8a7a;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-08').forEach((root) => {
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
  const root = document.querySelector('.tf-08');
  if (!root) return;
  const steps = [...root.querySelectorAll('.tf-08__step')], dots = [...root.querySelectorAll('.tf-08__steps li')];
  const next = root.querySelector('.tf-08__next'), back = root.querySelector('.tf-08__back');
  const cv = root.querySelector('#tf-08-cv'), msg = root.querySelector('.tf-08__msg'), MAX_MB = 5;
  let i = 0;
  const show = (n) => {
    i = n;
    steps.forEach((s, j) => { s.hidden = j !== i; });
    dots.forEach((d, j) => { d.classList.toggle('is-done', j < i); if (j === i) d.setAttribute('aria-current', 'step'); else d.removeAttribute('aria-current'); });
    root.dataset.step = i + 1;
    next.textContent = i === steps.length - 1 ? 'Submit application' : 'Continue';
    if (i === steps.length - 1) {
      const v = (id) => root.querySelector(id).value;
      root.querySelector('[data-review="name"]').textContent = v('#tf-08-fn') + ' ' + v('#tf-08-ln');
      root.querySelector('[data-review="email"]').textContent = v('#tf-08-em');
      root.querySelector('[data-review="cv"]').textContent = cv.files[0] ? cv.files[0].name : '—';
    }
    steps[i].querySelector('legend').focus();
  };
  next.addEventListener('click', () => {
    const bad = [...steps[i].querySelectorAll('input, select, textarea')].find((f) => !f.checkValidity());
    if (bad) { if (bad === cv) { msg.textContent = 'Please upload your résumé to continue.'; cv.focus(); } else bad.reportValidity(); return; }
    if (i < steps.length - 1) return show(i + 1);
    steps.forEach((s) => { s.hidden = true; });
    dots.forEach((d) => { d.classList.add('is-done'); d.removeAttribute('aria-current'); });
    root.classList.add('is-sent');
    const done = root.querySelector('.tf-08__done'); done.hidden = false; done.focus();
  });
  back.addEventListener('click', () => { if (i > 0) show(i - 1); });
  cv.addEventListener('change', () => {
    const f = cv.files[0]; msg.textContent = '';
    if (!f) return;
    if (f.size > MAX_MB * 1048576 || !/\.(pdf|docx?)$/i.test(f.name)) {
      msg.textContent = f.name + ' isn\'t a PDF/DOC under ' + MAX_MB + ' MB.'; cv.value = ''; return;
    }
    root.querySelector('.tf-08__fname').textContent = f.name;
    root.querySelector('.tf-08__fsize').textContent = (f.size / 1024).toFixed(0) + ' KB · ready to send';
    root.querySelector('.tf-08__ficon').textContent = f.name.split('.').pop().toUpperCase();
  });
  root.querySelector('.tf-08__rm').addEventListener('click', () => { cv.value = ''; cv.focus(); });
  const start = root.querySelector('#tf-08-start'); start.min = new Date().toISOString().slice(0, 10);
})();
```

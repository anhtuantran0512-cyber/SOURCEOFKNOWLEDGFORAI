---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-law-firm-consultation-request-form/"
title: "Tailwind Law Firm Consultation Request Form"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's consultation request, ported one-for-one to Tailwind v4: an attorney profile in deep green and brass beside a calm editorial form —…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Law Firm Consultation Request Form
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-law-firm-consultation-request-form/

The CSS collection's consultation request, ported one-for-one to Tailwind v4: an attorney profile in deep green and brass beside a calm editorial form — practice-area cards with a drawn check, an urgent-deadline switch that reveals a court date via group-has-checked/u:grid, an opposing-party field for conflict checks, a word-counted summary, contact-time chips and the no-attorney-client-relationship acknowledgement.
## HTML
```html
<div class="tf-17 relative block min-h-svh w-full bg-tf17-bg pt-[72px] font-tf17-sans leading-[normal] text-tf17-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,4vw,3.5rem)]">
    <div class="@container w-full max-w-[66rem]">
      <div class="grid overflow-hidden rounded-[.75rem] border border-tf17-line bg-tf17-card shadow-[0_40px_80px_-45px_rgba(20,30,25,.5)] @[52rem]:grid-cols-[19rem_minmax(0,1fr)]">
        <aside class="grid content-start gap-5 bg-[#183a2e] p-[clamp(1.25rem,4cqi,2.25rem)] text-[#efe9da] in-data-[theme=dark]:bg-[#0f241c]">
          <p class="font-tf17-serif text-[1.35rem] font-medium tracking-[.01em]">Whitcombe &amp; Hale <span class="ml-[.3rem] text-[.75rem] tracking-[.2em] text-tf17-brass">LLP</span></p>
          <figure class="grid gap-[.7rem] @max-[51.99rem]:grid-cols-[5rem_1fr] @max-[51.99rem]:items-center">
            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=480&fit=crop&crop=faces&auto=format&q=75" width="400" height="480" alt="Portrait of managing partner Daniel Hale" loading="lazy" decoding="async" class="aspect-[5/6] h-auto w-full max-w-60 rounded-[.35rem] bg-[#2a4a3e] object-cover contrast-105 grayscale-25 shadow-[0_0_0_1px_rgba(255,255,255,.08),.5rem_.5rem_0_-.1rem_color-mix(in_oklab,var(--color-tf17-brass)_40%,transparent)] @max-[51.99rem]:aspect-square @max-[51.99rem]:w-20 @max-[51.99rem]:rounded-full @max-[51.99rem]:shadow-none">
            <figcaption class="grid"><b class="font-tf17-serif text-[1.15rem] font-medium">Daniel Hale</b><span class="text-[.8rem] text-[#b9c4bc]">Managing Partner</span></figcaption>
          </figure>
          <blockquote class="border-l-2 border-tf17-brass pl-4 font-tf17-serif text-[1.1rem] leading-[1.45] font-normal text-[#f4ecd8] italic">“You'll speak with an attorney — not a call centre — within one business day.”</blockquote>
          <ul class="grid list-none gap-2 text-[.85rem] text-[#cbd4cd]"><li class="flex gap-[.55rem] before:font-tf17-serif before:text-tf17-brass before:content-['§']">Admitted in NY, NJ &amp; CA</li><li class="flex gap-[.55rem] before:font-tf17-serif before:text-tf17-brass before:content-['§']">27 years in practice</li><li class="flex gap-[.55rem] before:font-tf17-serif before:text-tf17-brass before:content-['§']">Free, confidential 30-min consultation</li></ul>
        </aside>
        <div class="grid content-start gap-[1.2rem] p-[clamp(1.25rem,4cqi,2.5rem)]" role="form" aria-labelledby="tf-17-title">
          <h2 id="tf-17-title" class="font-tf17-serif text-[clamp(1.8rem,4.5cqi,2.5rem)] leading-[1.05] font-normal tracking-[-.01em]">Request a consultation</h2>
          <p class="-mt-[.6rem] leading-[1.55] text-tf17-muted">Tell us briefly what's happening. Everything you share is kept strictly confidential.</p>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4">
            <div class="grid gap-[.4rem]"><label for="tf-17-n" class="text-[.84rem] font-semibold">Full name</label><input id="tf-17-n" autocomplete="name" required class="min-h-[2.9rem] w-full rounded-[.35rem] border border-tf17-line bg-tf17-soft px-[.85rem] py-[.6rem] text-[.97rem] text-tf17-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf17-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf17-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf17-bad"></div>
            <div class="grid gap-[.4rem]"><label for="tf-17-e" class="text-[.84rem] font-semibold">Email</label><input id="tf-17-e" type="email" autocomplete="email" required class="min-h-[2.9rem] w-full rounded-[.35rem] border border-tf17-line bg-tf17-soft px-[.85rem] py-[.6rem] text-[.97rem] text-tf17-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf17-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf17-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf17-bad"></div>
            <div class="grid gap-[.4rem]"><label for="tf-17-p" class="text-[.84rem] font-semibold">Phone</label><input id="tf-17-p" type="tel" autocomplete="tel" required class="min-h-[2.9rem] w-full rounded-[.35rem] border border-tf17-line bg-tf17-soft px-[.85rem] py-[.6rem] text-[.97rem] text-tf17-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf17-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf17-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf17-bad"></div>
            <div class="grid gap-[.4rem]"><label for="tf-17-st" class="text-[.84rem] font-semibold">State / jurisdiction</label><select id="tf-17-st" class="min-h-[2.9rem] w-full rounded-[.35rem] border border-tf17-line bg-tf17-soft px-[.85rem] py-[.6rem] text-[.97rem] text-tf17-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf17-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf17-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf17-bad"><option>New York</option><option>New Jersey</option><option>California</option><option>Other</option></select></div>
          </div>
          <fieldset class="grid min-w-0 grid-cols-[repeat(auto-fit,minmax(min(100%,14rem),1fr))] gap-2"><legend class="col-span-full mb-[.6rem] p-0 text-[.84rem] font-semibold">Practice area</legend>
            <label class="group/ar relative text-[.84rem] font-semibold"><input type="radio" name="tf-17-a" value="family" required class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.1rem] rounded-[.4rem] border border-tf17-line py-[.8rem] pr-[2.6rem] pl-[.95rem] [transition:border-color_.2s,background_.2s] after:absolute after:top-1/2 after:right-[.95rem] after:-mt-[.55rem] after:h-[.85rem] after:w-[.45rem] after:scale-0 after:rotate-45 after:border-r-2 after:border-b-2 after:border-tf17-accent after:[transition:scale_.3s_var(--ease-tf17)] after:content-[''] group-hover/ar:border-tf17-muted group-has-checked/ar:border-tf17-accent group-has-checked/ar:bg-[color-mix(in_oklab,var(--color-tf17-accent)_6%,var(--color-tf17-card))] group-has-checked/ar:after:scale-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:group-has-checked/ar:outline-2 forced-colors:group-has-checked/ar:outline-[Highlight]"><b class="font-tf17-serif text-[1.02rem] font-medium">Family &amp; divorce</b><small class="text-[.78rem] font-normal text-tf17-muted">Custody, separation, support</small></span></label>
            <label class="group/ar relative text-[.84rem] font-semibold"><input type="radio" name="tf-17-a" value="employment" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.1rem] rounded-[.4rem] border border-tf17-line py-[.8rem] pr-[2.6rem] pl-[.95rem] [transition:border-color_.2s,background_.2s] after:absolute after:top-1/2 after:right-[.95rem] after:-mt-[.55rem] after:h-[.85rem] after:w-[.45rem] after:scale-0 after:rotate-45 after:border-r-2 after:border-b-2 after:border-tf17-accent after:[transition:scale_.3s_var(--ease-tf17)] after:content-[''] group-hover/ar:border-tf17-muted group-has-checked/ar:border-tf17-accent group-has-checked/ar:bg-[color-mix(in_oklab,var(--color-tf17-accent)_6%,var(--color-tf17-card))] group-has-checked/ar:after:scale-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:group-has-checked/ar:outline-2 forced-colors:group-has-checked/ar:outline-[Highlight]"><b class="font-tf17-serif text-[1.02rem] font-medium">Employment</b><small class="text-[.78rem] font-normal text-tf17-muted">Dismissal, discrimination, contracts</small></span></label>
            <label class="group/ar relative text-[.84rem] font-semibold"><input type="radio" name="tf-17-a" value="injury" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.1rem] rounded-[.4rem] border border-tf17-line py-[.8rem] pr-[2.6rem] pl-[.95rem] [transition:border-color_.2s,background_.2s] after:absolute after:top-1/2 after:right-[.95rem] after:-mt-[.55rem] after:h-[.85rem] after:w-[.45rem] after:scale-0 after:rotate-45 after:border-r-2 after:border-b-2 after:border-tf17-accent after:[transition:scale_.3s_var(--ease-tf17)] after:content-[''] group-hover/ar:border-tf17-muted group-has-checked/ar:border-tf17-accent group-has-checked/ar:bg-[color-mix(in_oklab,var(--color-tf17-accent)_6%,var(--color-tf17-card))] group-has-checked/ar:after:scale-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:group-has-checked/ar:outline-2 forced-colors:group-has-checked/ar:outline-[Highlight]"><b class="font-tf17-serif text-[1.02rem] font-medium">Personal injury</b><small class="text-[.78rem] font-normal text-tf17-muted">Accidents, medical negligence</small></span></label>
            <label class="group/ar relative text-[.84rem] font-semibold"><input type="radio" name="tf-17-a" value="estate" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.1rem] rounded-[.4rem] border border-tf17-line py-[.8rem] pr-[2.6rem] pl-[.95rem] [transition:border-color_.2s,background_.2s] after:absolute after:top-1/2 after:right-[.95rem] after:-mt-[.55rem] after:h-[.85rem] after:w-[.45rem] after:scale-0 after:rotate-45 after:border-r-2 after:border-b-2 after:border-tf17-accent after:[transition:scale_.3s_var(--ease-tf17)] after:content-[''] group-hover/ar:border-tf17-muted group-has-checked/ar:border-tf17-accent group-has-checked/ar:bg-[color-mix(in_oklab,var(--color-tf17-accent)_6%,var(--color-tf17-card))] group-has-checked/ar:after:scale-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:group-has-checked/ar:outline-2 forced-colors:group-has-checked/ar:outline-[Highlight]"><b class="font-tf17-serif text-[1.02rem] font-medium">Wills &amp; estates</b><small class="text-[.78rem] font-normal text-tf17-muted">Probate, trusts, disputes</small></span></label>
            <label class="group/ar relative text-[.84rem] font-semibold"><input type="radio" name="tf-17-a" value="business" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.1rem] rounded-[.4rem] border border-tf17-line py-[.8rem] pr-[2.6rem] pl-[.95rem] [transition:border-color_.2s,background_.2s] after:absolute after:top-1/2 after:right-[.95rem] after:-mt-[.55rem] after:h-[.85rem] after:w-[.45rem] after:scale-0 after:rotate-45 after:border-r-2 after:border-b-2 after:border-tf17-accent after:[transition:scale_.3s_var(--ease-tf17)] after:content-[''] group-hover/ar:border-tf17-muted group-has-checked/ar:border-tf17-accent group-has-checked/ar:bg-[color-mix(in_oklab,var(--color-tf17-accent)_6%,var(--color-tf17-card))] group-has-checked/ar:after:scale-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:group-has-checked/ar:outline-2 forced-colors:group-has-checked/ar:outline-[Highlight]"><b class="font-tf17-serif text-[1.02rem] font-medium">Business</b><small class="text-[.78rem] font-normal text-tf17-muted">Formation, disputes, M&amp;A</small></span></label>
            <label class="group/ar relative text-[.84rem] font-semibold"><input type="radio" name="tf-17-a" value="immigration" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="relative grid gap-[.1rem] rounded-[.4rem] border border-tf17-line py-[.8rem] pr-[2.6rem] pl-[.95rem] [transition:border-color_.2s,background_.2s] after:absolute after:top-1/2 after:right-[.95rem] after:-mt-[.55rem] after:h-[.85rem] after:w-[.45rem] after:scale-0 after:rotate-45 after:border-r-2 after:border-b-2 after:border-tf17-accent after:[transition:scale_.3s_var(--ease-tf17)] after:content-[''] group-hover/ar:border-tf17-muted group-has-checked/ar:border-tf17-accent group-has-checked/ar:bg-[color-mix(in_oklab,var(--color-tf17-accent)_6%,var(--color-tf17-card))] group-has-checked/ar:after:scale-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:group-has-checked/ar:outline-2 forced-colors:group-has-checked/ar:outline-[Highlight]"><b class="font-tf17-serif text-[1.02rem] font-medium">Immigration</b><small class="text-[.78rem] font-normal text-tf17-muted">Visas, green cards, appeals</small></span></label>
          </fieldset>
          <div class="group/u grid gap-[.8rem] rounded-[.4rem] border border-dashed border-[color-mix(in_oklab,var(--color-tf17-brass)_60%,var(--color-tf17-line))] bg-[color-mix(in_oklab,var(--color-tf17-brass)_5%,var(--color-tf17-card))] px-4 py-[.9rem]">
            <label class="relative flex min-h-10 cursor-pointer items-center gap-3 text-[.84rem] font-semibold"><input type="checkbox" id="tf-17-urg" role="switch" class="peer absolute m-0 h-6 w-[2.6rem] cursor-pointer opacity-0"><i aria-hidden="true" class="relative h-6 w-[2.6rem] flex-none rounded-full bg-tf17-line [transition:background_.25s] after:absolute after:top-[.15rem] after:left-[.15rem] after:size-[1.2rem] after:rounded-full after:bg-white after:shadow-[0_1px_3px_rgba(0,0,0,.3)] after:[transition:translate_.35s_var(--ease-tf17)] after:content-[''] peer-checked:bg-tf17-brass peer-checked:after:translate-x-[1.1rem] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent"></i><span>I have a court date or legal deadline</span></label>
            <div class="hidden gap-[.4rem] group-has-checked/u:grid group-has-checked/u:animate-tf17-in"><label for="tf-17-cd" class="text-[.84rem] font-semibold">Date of hearing or deadline</label><input id="tf-17-cd" type="date" class="min-h-[2.9rem] w-full rounded-[.35rem] border border-tf17-line bg-tf17-soft px-[.85rem] py-[.6rem] text-[.97rem] text-tf17-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf17-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf17-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf17-bad"></div>
          </div>
          <div class="grid gap-[.4rem]"><label for="tf-17-op" class="text-[.84rem] font-semibold">Other party's name <span class="font-normal text-tf17-muted">For our conflict check</span></label><input id="tf-17-op" placeholder="Person or company, if any" class="min-h-[2.9rem] w-full rounded-[.35rem] border border-tf17-line bg-tf17-soft px-[.85rem] py-[.6rem] text-[.97rem] text-tf17-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf17-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf17-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf17-bad"></div>
          <div class="grid gap-[.4rem]">
            <p class="mb-[.35rem] flex items-center gap-[.55rem] text-[.82rem] text-tf17-accent"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.05rem] flex-none fill-none stroke-current stroke-[1.8] [stroke-linecap:round]"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>Protected and confidential. Share only a brief outline — details can wait for the call.</p>
            <div class="flex items-baseline justify-between"><label for="tf-17-sum" class="text-[.84rem] font-semibold">Brief summary of your matter</label><span class="tf-17__wc text-[.78rem] text-tf17-muted tabular-nums [&.is-long]:font-semibold [&.is-long]:text-tf17-brass" aria-hidden="true">0 words</span></div>
            <textarea id="tf-17-sum" rows="4" required aria-describedby="tf-17-wc-live" class="min-h-[2.9rem] w-full rounded-[.35rem] border border-tf17-line bg-tf17-soft px-[.85rem] py-[.6rem] text-[.97rem] text-tf17-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf17-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf17-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf17-bad resize-y leading-[1.55]"></textarea>
            <p class="sr-only" id="tf-17-wc-live" aria-live="polite"></p>
          </div>
          <fieldset class="flex min-w-0 flex-wrap gap-[.4rem]"><legend class="mb-[.6rem] w-full p-0 text-[.84rem] font-semibold">Best time to reach you</legend>
            <label class="relative text-[.84rem] font-semibold"><input type="checkbox" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf17-line px-[.95rem] text-[.85rem] font-normal transition-all duration-200 peer-checked:border-tf17-accent peer-checked:bg-tf17-accent peer-checked:text-tf17-on peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Morning</span></label><label class="relative text-[.84rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf17-line px-[.95rem] text-[.85rem] font-normal transition-all duration-200 peer-checked:border-tf17-accent peer-checked:bg-tf17-accent peer-checked:text-tf17-on peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Afternoon</span></label><label class="relative text-[.84rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf17-line px-[.95rem] text-[.85rem] font-normal transition-all duration-200 peer-checked:border-tf17-accent peer-checked:bg-tf17-accent peer-checked:text-tf17-on peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Evening</span></label>
            <label class="relative ml-auto max-[36rem]:ml-0 text-[.84rem] font-semibold"><input type="radio" name="tf-17-via" value="phone" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf17-line px-[.95rem] text-[.85rem] font-normal transition-all duration-200 peer-checked:border-tf17-accent peer-checked:bg-tf17-accent peer-checked:text-tf17-on peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">By phone</span></label><label class="relative text-[.84rem] font-semibold"><input type="radio" name="tf-17-via" value="video" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf17-line px-[.95rem] text-[.85rem] font-normal transition-all duration-200 peer-checked:border-tf17-accent peer-checked:bg-tf17-accent peer-checked:text-tf17-on peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Video call</span></label><label class="relative text-[.84rem] font-semibold"><input type="radio" name="tf-17-via" value="email" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf17-line px-[.95rem] text-[.85rem] font-normal transition-all duration-200 peer-checked:border-tf17-accent peer-checked:bg-tf17-accent peer-checked:text-tf17-on peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf17-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Email</span></label>
          </fieldset>
          <label class="flex cursor-pointer items-start gap-[.65rem] text-[.84rem] leading-[1.45] font-normal text-tf17-muted"><input type="checkbox" required class="mt-[.12rem] size-[1.15rem] flex-none accent-tf17-accent"><span>I understand that submitting this form does not create an attorney–client relationship.</span></label>
          <button type="button" class="tf-17__send min-h-[3.2rem] cursor-pointer rounded-[.35rem] border-0 bg-tf17-accent text-[1rem] font-semibold tracking-[.02em] text-tf17-on shadow-[inset_0_-3px_0_color-mix(in_oklab,black_25%,transparent)] [transition:filter_.2s,translate_.2s_var(--ease-tf17)] hover:-translate-y-px hover:brightness-112 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf17-brass forced-colors:border forced-colors:border-[ButtonText]">Request my consultation</button>
          <div class="tf-17__done animate-tf17-done border-l-[3px] border-tf17-brass bg-tf17-soft px-[1.1rem] py-4 outline-none" hidden tabindex="-1"><b class="font-tf17-serif text-[1.2rem] font-medium">Request received</b><p class="mt-[.3rem] text-tf17-muted">Your reference is <strong class="tf-17__ref"></strong>. An attorney will contact you within one business day.</p></div>
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
  --color-tf17-bg: #ebe8df;
  --color-tf17-card: #fdfbf6;
  --color-tf17-ink: #1b211d;
  --color-tf17-muted: #5f665f;
  --color-tf17-line: #e1dccf;
  --color-tf17-soft: #f6f3ec;
  --color-tf17-accent: #1f4a3a;
  --color-tf17-on: #f8f4ea;
  --color-tf17-brass: #a8834a;
  --color-tf17-bad: #a3271b;
  --font-tf17-serif: "Newsreader", ui-serif, Georgia, serif;
  --font-tf17-sans: "Public Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf17: cubic-bezier(0.16,1,0.3,1);
  --animate-tf17-in: tf17-in 0.35s cubic-bezier(0.16,1,0.3,1);
  --animate-tf17-done: tf17-in 0.4s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf17-in {
    from {
      opacity: 0;
      translate: 0 -6px;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-17[data-theme="dark"] {
  color-scheme: dark;
  --color-tf17-bg: #0e1210;
  --color-tf17-card: #151a17;
  --color-tf17-ink: #ece8de;
  --color-tf17-muted: #a3a99f;
  --color-tf17-line: #29302b;
  --color-tf17-soft: #1a201c;
  --color-tf17-accent: #8cc5ad;
  --color-tf17-on: #0b1c15;
  --color-tf17-brass: #d1ab6e;
  --color-tf17-bad: #ff8a7a;
}

@media (prefers-color-scheme: dark) {
  .tf-17:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf17-bg: #0e1210;
    --color-tf17-card: #151a17;
    --color-tf17-ink: #ece8de;
    --color-tf17-muted: #a3a99f;
    --color-tf17-line: #29302b;
    --color-tf17-soft: #1a201c;
    --color-tf17-accent: #8cc5ad;
    --color-tf17-on: #0b1c15;
    --color-tf17-brass: #d1ab6e;
    --color-tf17-bad: #ff8a7a;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-17').forEach((root) => {
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
  const root = document.querySelector('.tf-17');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const WORDS = 250;
  const urg = $('#tf-17-urg'), court = $('#tf-17-cd');
  court.min = new Date().toISOString().slice(0, 10);
  urg.addEventListener('change', () => { court.required = urg.checked; if (urg.checked) court.focus(); });
  const sum = $('#tf-17-sum'), wc = $('.tf-17__wc'), live = $('#tf-17-wc-live');
  let warned = false;
  sum.addEventListener('input', () => {
    const n = (sum.value.trim().match(/\S+/g) || []).length, long = n > WORDS;
    wc.textContent = n + ' word' + (n === 1 ? '' : 's') + (long ? ' — feel free to save details for the call' : '');
    wc.classList.toggle('is-long', long);
    if (long !== warned) { live.textContent = long ? 'Over ' + WORDS + ' words. You can share more details on the call.' : ''; warned = long; }
  });
  $('.tf-17__send').addEventListener('click', () => {
    const bad = [...root.querySelectorAll('[required]')].find((f) => f.type === 'radio' ? !root.querySelector('[name="' + f.name + '"]:checked') : !f.checkValidity());
    if (bad) { bad.focus(); if (bad.reportValidity) bad.reportValidity(); return; }
    $('.tf-17__ref').textContent = 'WH-' + new Date().getFullYear() + '-' + String(Math.floor(Math.random() * 90000) + 10000);
    const done = $('.tf-17__done'); done.hidden = false; $('.tf-17__send').hidden = true; done.focus();
  });
})();
```

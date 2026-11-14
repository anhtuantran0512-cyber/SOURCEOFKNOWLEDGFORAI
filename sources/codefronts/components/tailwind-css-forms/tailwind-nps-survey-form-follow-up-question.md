---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-nps-survey-form-follow-up-question/"
title: "Tailwind NPS Survey Form with Follow-Up Question"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's Net Promoter Score survey, ported one-for-one to Tailwind v4 — and the survey logic is still zero JavaScript (the only script is the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind NPS Survey Form with Follow-Up Question
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-nps-survey-form-follow-up-question/

The CSS collection's Net Promoter Score survey, ported one-for-one to Tailwind v4 — and the survey logic is still zero JavaScript (the only script is the theme toggle). Eleven real radios are tinted along an oklch() red-amber-green ramp from one --h hue per label; choosing a score reveals a different follow-up for detractors, passives and promoters with group-has-[.is-d:checked]/root:grid, a progress bar fills, a band label appears, and a checkbox-driven thank-you bursts in.
## HTML
```html
<div class="tf-07 group/root relative block min-h-svh w-full [background:var(--tf07-wash),var(--color-tf07-bg)] pt-[72px] font-tf07-sans leading-[normal] text-tf07-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,5vw,4rem)]">
    <div class="relative w-full max-w-[40rem] rounded-[1.75rem] border border-tf07-line bg-tf07-card p-[clamp(1.25rem,5vw,2.5rem)] shadow-[0_30px_70px_-40px_rgba(60,30,120,.45)]" role="form" aria-labelledby="tf-07-legend">
      <input type="checkbox" id="tf-07-sent" class="tf-07__sendbox pointer-events-none absolute size-px opacity-0" aria-label="Submit feedback">
      <div class="grid gap-[1.4rem] group-has-[.tf-07\_\_sendbox:checked]/root:hidden">
        <div class="flex items-center gap-[.7rem]">
          <span class="grid size-[2.2rem] place-items-center rounded-[.7rem] bg-tf07-ink font-extrabold text-tf07-card" aria-hidden="true">L</span>
          <span class="text-[.82rem] font-semibold text-tf07-muted">Quick feedback · 30 seconds</span>
        </div>
        <div class="-mt-[.4rem] h-[.3rem] overflow-hidden rounded-full bg-tf07-line" aria-hidden="true"><i class="block h-full w-full origin-left scale-x-8 rounded-[inherit] bg-[linear-gradient(90deg,#f43f5e,#f59e0b,#22c55e)] [transition:scale_.6s_var(--ease-tf07)] group-has-[[name=tf-07-s]:checked]/root:scale-x-60 group-has-[.tf-07\_\_q_textarea:not(:placeholder-shown)]/root:scale-x-92!"></i></div>
        <fieldset class="min-w-0">
          <legend id="tf-07-legend" class="p-0 leading-[1.25] font-bold tracking-[-.025em] text-balance mb-[1.1rem] text-[clamp(1.25rem,3.6vw,1.6rem)]">How likely are you to recommend Loop to a friend or colleague?</legend>
          <div class="group/sc grid grid-cols-11 gap-[.35rem] max-[30rem]:grid-cols-6">
            <label style="--i:0" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="0" class="is-d peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">0</span></label>
            <label style="--i:1" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="1" class="is-d peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">1</span></label>
            <label style="--i:2" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="2" class="is-d peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">2</span></label>
            <label style="--i:3" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="3" class="is-d peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">3</span></label>
            <label style="--i:4" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="4" class="is-d peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">4</span></label>
            <label style="--i:5" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="5" class="is-d peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">5</span></label>
            <label style="--i:6" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="6" class="is-d peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">6</span></label>
            <label style="--i:7" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="7" class="is-p peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">7</span></label>
            <label style="--i:8" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="8" class="is-p peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">8</span></label>
            <label style="--i:9" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="9" class="is-r peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">9</span></label>
            <label style="--i:10" class="group/l relative [--h:calc(25+var(--i)*12.5)]"><input type="radio" name="tf-07-s" value="10" class="is-r peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="grid aspect-[1/1.15] min-h-11 place-items-center rounded-[.8rem] border border-tf07-line bg-tf07-soft text-[clamp(.85rem,2.4vw,1.05rem)] font-bold tabular-nums [transition:background_.25s,color_.25s,translate_.3s_var(--ease-tf07),scale_.3s_var(--ease-tf07),box-shadow_.25s] group-hover/l:-translate-y-[3px] group-hover/l:border-[oklch(70%_.16_var(--h))] group-has-checked/sc:peer-not-checked:opacity-55 peer-checked:-translate-y-1 peer-checked:scale-108 peer-checked:border-transparent peer-checked:bg-[oklch(72%_.17_var(--h))] peer-checked:text-[oklch(20%_.06_var(--h))] peer-checked:shadow-[0_10px_20px_-8px_oklch(60%_.18_var(--h))] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-ink max-[30rem]:aspect-auto forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">10</span></label>
          </div>
          <div class="mt-[.7rem] flex items-center justify-between gap-2 text-[.78rem] font-semibold text-tf07-muted" aria-hidden="true"><span>Not likely</span><span class="before:rounded-full before:px-[.6rem] before:py-[.2rem] before:text-[.72rem] before:tracking-[.06em] before:uppercase before:content-[''] group-has-[.is-d:checked]/root:before:bg-[#ffe4e6] group-has-[.is-d:checked]/root:before:text-[#9f1239] group-has-[.is-d:checked]/root:before:content-['Detractor'] group-has-[.is-p:checked]/root:before:bg-[#fef3c7] group-has-[.is-p:checked]/root:before:text-[#92400e] group-has-[.is-p:checked]/root:before:content-['Passive'] group-has-[.is-r:checked]/root:before:bg-[#dcfce7] group-has-[.is-r:checked]/root:before:text-[#166534] group-has-[.is-r:checked]/root:before:content-['Promoter']"></span><span>Extremely likely</span></div>
        </fieldset>
        <fieldset class="tf-07__q hidden min-w-0 gap-[.8rem] rounded-[1.25rem] border border-tf07-line bg-tf07-soft p-5 group-has-[.is-d:checked]/root:grid group-has-[.is-d:checked]/root:animate-tf07-in">
          <legend class="p-0 leading-[1.25] font-bold tracking-[-.025em] text-balance float-left mb-[.2rem] w-full text-[1.05rem]">We're sorry to hear that. What disappointed you most?</legend>
          <div class="flex flex-wrap gap-[.45rem]">
            <label class="relative"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf07-line bg-tf07-card px-[.95rem] text-[.88rem] font-semibold transition-all duration-200 peer-checked:border-tf07-ink peer-checked:bg-tf07-ink peer-checked:text-tf07-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Missing features</span></label>
            <label class="relative"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf07-line bg-tf07-card px-[.95rem] text-[.88rem] font-semibold transition-all duration-200 peer-checked:border-tf07-ink peer-checked:bg-tf07-ink peer-checked:text-tf07-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Too expensive</span></label>
            <label class="relative"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf07-line bg-tf07-card px-[.95rem] text-[.88rem] font-semibold transition-all duration-200 peer-checked:border-tf07-ink peer-checked:bg-tf07-ink peer-checked:text-tf07-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Bugs or slowness</span></label>
            <label class="relative"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf07-line bg-tf07-card px-[.95rem] text-[.88rem] font-semibold transition-all duration-200 peer-checked:border-tf07-ink peer-checked:bg-tf07-ink peer-checked:text-tf07-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Hard to learn</span></label>
            <label class="relative"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf07-line bg-tf07-card px-[.95rem] text-[.88rem] font-semibold transition-all duration-200 peer-checked:border-tf07-ink peer-checked:bg-tf07-ink peer-checked:text-tf07-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Support experience</span></label>
          </div>
          <label for="tf-07-d" class="text-[.85rem] font-semibold">What's one thing we should fix first?</label>
          <textarea id="tf-07-d" rows="3" placeholder="Be as blunt as you like — this goes straight to the product team." class="min-h-[5.5rem] w-full resize-y rounded-[.9rem] border border-tf07-line bg-tf07-card px-[.95rem] py-[.8rem] text-[.95rem] leading-[1.5] text-tf07-ink [field-sizing:content] focus-visible:border-tf07-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf07-accent)_18%,transparent)] focus-visible:outline-none"></textarea>
          <label class="flex min-h-10 cursor-pointer items-center gap-[.55rem] text-[.88rem] text-tf07-muted"><input type="checkbox" class="m-0 size-[1.1rem] accent-tf07-accent"><span>It's OK to contact me about this</span></label>
        </fieldset>
        <fieldset class="tf-07__q hidden min-w-0 gap-[.8rem] rounded-[1.25rem] border border-tf07-line bg-tf07-soft p-5 group-has-[.is-p:checked]/root:grid group-has-[.is-p:checked]/root:animate-tf07-in">
          <legend class="p-0 leading-[1.25] font-bold tracking-[-.025em] text-balance float-left mb-[.2rem] w-full text-[1.05rem]">Thanks! What would make Loop a 10 for you?</legend>
          <label for="tf-07-p" class="text-[.85rem] font-semibold">One improvement, big or small</label>
          <textarea id="tf-07-p" rows="3" placeholder="e.g. Calendar sync, a better mobile app, cheaper team plans…" class="min-h-[5.5rem] w-full resize-y rounded-[.9rem] border border-tf07-line bg-tf07-card px-[.95rem] py-[.8rem] text-[.95rem] leading-[1.5] text-tf07-ink [field-sizing:content] focus-visible:border-tf07-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf07-accent)_18%,transparent)] focus-visible:outline-none"></textarea>
        </fieldset>
        <fieldset class="tf-07__q hidden min-w-0 gap-[.8rem] rounded-[1.25rem] border border-tf07-line bg-tf07-soft p-5 group-has-[.is-r:checked]/root:grid group-has-[.is-r:checked]/root:animate-tf07-in">
          <legend class="p-0 leading-[1.25] font-bold tracking-[-.025em] text-balance float-left mb-[.2rem] w-full text-[1.05rem]">Amazing. What do you love most about Loop?</legend>
          <div class="flex flex-wrap gap-[.45rem]">
            <label class="relative"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf07-line bg-tf07-card px-[.95rem] text-[.88rem] font-semibold transition-all duration-200 peer-checked:border-tf07-ink peer-checked:bg-tf07-ink peer-checked:text-tf07-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Speed</span></label>
            <label class="relative"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf07-line bg-tf07-card px-[.95rem] text-[.88rem] font-semibold transition-all duration-200 peer-checked:border-tf07-ink peer-checked:bg-tf07-ink peer-checked:text-tf07-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Design</span></label>
            <label class="relative"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf07-line bg-tf07-card px-[.95rem] text-[.88rem] font-semibold transition-all duration-200 peer-checked:border-tf07-ink peer-checked:bg-tf07-ink peer-checked:text-tf07-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Integrations</span></label>
            <label class="relative"><input type="checkbox" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-10 items-center rounded-full border border-tf07-line bg-tf07-card px-[.95rem] text-[.88rem] font-semibold transition-all duration-200 peer-checked:border-tf07-ink peer-checked:bg-tf07-ink peer-checked:text-tf07-card peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf07-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Support team</span></label>
          </div>
          <label for="tf-07-r" class="text-[.85rem] font-semibold">Mind if we quote you? <span class="font-normal text-tf07-muted">Optional</span></label>
          <textarea id="tf-07-r" rows="3" placeholder="A sentence we could share with other teams…" class="min-h-[5.5rem] w-full resize-y rounded-[.9rem] border border-tf07-line bg-tf07-card px-[.95rem] py-[.8rem] text-[.95rem] leading-[1.5] text-tf07-ink [field-sizing:content] focus-visible:border-tf07-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf07-accent)_18%,transparent)] focus-visible:outline-none"></textarea>
        </fieldset>
        <div class="flex flex-wrap items-center justify-between gap-4">
          <span class="text-[.82rem] text-tf07-muted">You can skip any question.</span>
          <label for="tf-07-sent" class="inline-flex min-h-12 cursor-pointer items-center rounded-full px-6 font-bold select-none [transition:translate_.2s_var(--ease-tf07),opacity_.2s,filter_.2s] group-has-[.tf-07\_\_sendbox:focus-visible]/root:outline-2 group-has-[.tf-07\_\_sendbox:focus-visible]/root:outline-offset-3 group-has-[.tf-07\_\_sendbox:focus-visible]/root:outline-tf07-ink forced-colors:border forced-colors:border-[ButtonText] bg-tf07-accent text-tf07-on hover:-translate-y-0.5 hover:brightness-108 [.tf-07:not(:has([name=tf-07-s]:checked))_&]:pointer-events-none [.tf-07:not(:has([name=tf-07-s]:checked))_&]:opacity-40" aria-hidden="true">Send feedback</label>
        </div>
      </div>
      <div class="hidden justify-items-center gap-[.6rem] pt-8 pb-4 text-center group-has-[.tf-07\_\_sendbox:checked]/root:grid group-has-[.tf-07\_\_sendbox:checked]/root:animate-tf07-thanks" role="status">
        <div class="relative size-[4.5rem] rounded-full bg-[linear-gradient(135deg,#f472b6,#a78bfa,#34d399)] after:absolute after:inset-0 after:grid after:place-items-center after:text-[2rem] after:font-extrabold after:text-white after:content-['✓']" aria-hidden="true"><i style="--n:0;--a:0deg" class="absolute top-1/2 left-1/2 size-2 rounded-full bg-[hsl(calc(var(--n,0)*60)_80%_65%)] opacity-0 group-has-[.tf-07\_\_sendbox:checked]/root:animate-tf07-burst"></i><i style="--n:1;--a:60deg" class="absolute top-1/2 left-1/2 size-2 rounded-full bg-[hsl(calc(var(--n,0)*60)_80%_65%)] opacity-0 group-has-[.tf-07\_\_sendbox:checked]/root:animate-tf07-burst"></i><i style="--n:2;--a:120deg" class="absolute top-1/2 left-1/2 size-2 rounded-full bg-[hsl(calc(var(--n,0)*60)_80%_65%)] opacity-0 group-has-[.tf-07\_\_sendbox:checked]/root:animate-tf07-burst"></i><i style="--n:3;--a:180deg" class="absolute top-1/2 left-1/2 size-2 rounded-full bg-[hsl(calc(var(--n,0)*60)_80%_65%)] opacity-0 group-has-[.tf-07\_\_sendbox:checked]/root:animate-tf07-burst"></i><i style="--n:4;--a:240deg" class="absolute top-1/2 left-1/2 size-2 rounded-full bg-[hsl(calc(var(--n,0)*60)_80%_65%)] opacity-0 group-has-[.tf-07\_\_sendbox:checked]/root:animate-tf07-burst"></i><i style="--n:5;--a:300deg" class="absolute top-1/2 left-1/2 size-2 rounded-full bg-[hsl(calc(var(--n,0)*60)_80%_65%)] opacity-0 group-has-[.tf-07\_\_sendbox:checked]/root:animate-tf07-burst"></i></div>
        <h3 class="mt-[.8rem] text-[1.6rem] font-bold tracking-[-.03em]">Thank you — that genuinely helps.</h3>
        <p class="mb-4 max-w-[26rem] text-tf07-muted">We read every response. Your feedback has been shared with the product team.</p>
        <label for="tf-07-sent" class="inline-flex min-h-12 cursor-pointer items-center rounded-full px-6 font-bold select-none [transition:translate_.2s_var(--ease-tf07),opacity_.2s,filter_.2s] group-has-[.tf-07\_\_sendbox:focus-visible]/root:outline-2 group-has-[.tf-07\_\_sendbox:focus-visible]/root:outline-offset-3 group-has-[.tf-07\_\_sendbox:focus-visible]/root:outline-tf07-ink forced-colors:border forced-colors:border-[ButtonText] border border-tf07-line bg-transparent text-tf07-ink">Edit my answer</label>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf07-bg: #f4f1fb;
  --color-tf07-card: #ffffff;
  --color-tf07-ink: #1e1b2e;
  --color-tf07-muted: #6b6880;
  --color-tf07-line: #e7e3f3;
  --color-tf07-soft: #f7f5fd;
  --color-tf07-accent: #6d28d9;
  --color-tf07-on: #fff;
  --font-tf07-sans: "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf07: cubic-bezier(0.16,1,0.3,1);
  --animate-tf07-in: tf07-in 0.55s cubic-bezier(0.16,1,0.3,1);
  --animate-tf07-thanks: tf07-in 0.6s cubic-bezier(0.16,1,0.3,1);
  --animate-tf07-burst: tf07-burst 0.9s 0.15s cubic-bezier(0.16,1,0.3,1) both;

  @keyframes tf07-in {
    from {
      opacity: 0;
      translate: 0 12px;
      scale: 0.98;
    }
  }

  @keyframes tf07-burst {
    0% {
      opacity: 1;
      transform: translate(-50%,-50%) rotate(var(--a)) translateY(0);
    }

    100% {
      opacity: 0;
      transform: translate(-50%,-50%) rotate(var(--a)) translateY(-3.6rem);
    }
  }
}
/* Root rule: full-bleed contract + scheme switch, plus the pastel wash behind the card.
   @theme holds the light values; dark values override the same variables. */

.tf-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
  --tf07-wash: radial-gradient(40rem 30rem at 15% 10%, #ffe4e6, transparent 60%), radial-gradient(40rem 30rem at 85% 90%, #dcfce7, transparent 60%), radial-gradient(40rem 30rem at 90% 10%, #e0e7ff, transparent 60%);
}

.tf-07[data-theme="dark"] {
  color-scheme: dark;
  --tf07-wash: none;
  --color-tf07-bg: #100e18;
  --color-tf07-card: #181524;
  --color-tf07-ink: #efecf8;
  --color-tf07-muted: #a29db8;
  --color-tf07-line: #2b2740;
  --color-tf07-soft: #1f1b2e;
  --color-tf07-accent: #a78bfa;
  --color-tf07-on: #160a33;
}

@media (prefers-color-scheme: dark) {
  .tf-07:not([data-theme="light"]) {
    color-scheme: dark;
    --tf07-wash: radial-gradient(40rem 30rem at 15% 10%, #3b0d1a55, transparent 60%), radial-gradient(40rem 30rem at 85% 90%, #0b3b2255, transparent 60%);
    --color-tf07-bg: #100e18;
    --color-tf07-card: #181524;
    --color-tf07-ink: #efecf8;
    --color-tf07-muted: #a29db8;
    --color-tf07-line: #2b2740;
    --color-tf07-soft: #1f1b2e;
    --color-tf07-accent: #a78bfa;
    --color-tf07-on: #160a33;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-07').forEach((root) => {
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

```

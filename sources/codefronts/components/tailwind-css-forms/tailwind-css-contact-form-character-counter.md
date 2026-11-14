---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-css-contact-form-character-counter/"
title: "Tailwind CSS Contact Form with Character Counter"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's contact form, rebuilt one-for-one in Tailwind v4 utilities: a textarea that grows with [field-sizing:content], a circular counter ring…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Contact Form with Character Counter
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-css-contact-form-character-counter/

The CSS collection's contact form, rebuilt one-for-one in Tailwind v4 utilities: a textarea that grows with [field-sizing:content], a circular counter ring driven by a registered @property that shifts from calm to amber to red as the limit approaches, threshold-only screen-reader announcements, topic chips built from real radios with peer-checked:, and user-invalid: errors that wait until the user has actually left a field.
## HTML
```html
<div class="tf-01 relative block min-h-svh w-full [background:radial-gradient(60rem_40rem_at_110%_-10%,color-mix(in_oklab,var(--color-tf01-accent)_14%,transparent),transparent_60%),radial-gradient(50rem_30rem_at_-20%_110%,color-mix(in_oklab,#a16207_12%,transparent),transparent_60%),var(--color-tf01-bg)] pt-[72px] leading-[normal] font-tf01-sans text-tf01-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,5vw,4rem)]">
    <div class="relative w-full max-w-[40rem] animate-tf01-rise rounded-3xl border border-tf01-line bg-tf01-card p-[clamp(1.5rem,5vw,2.75rem)] shadow-[inset_0_1px_0_color-mix(in_oklab,white_60%,transparent),0_30px_60px_-30px_color-mix(in_oklab,var(--color-tf01-ink)_30%,transparent)]" role="form" aria-labelledby="tf-01-title">
      <header class="tf-01__head">
        <p class="mb-3 text-[.75rem] font-semibold tracking-[.14em] text-tf01-accent uppercase">Get in touch</p>
        <h2 id="tf-01-title" class="font-tf01-serif text-[clamp(2.1rem,6vw,3.1rem)] leading-none font-normal tracking-[-.02em] text-balance">Tell us what you're <em class="text-tf01-accent">building.</em></h2>
        <p class="mt-[.9rem] max-w-[34rem] leading-[1.55] text-pretty text-tf01-muted">We reply to every message within one business day. Fields marked <span aria-hidden="true">*</span><span class="sr-only">with an asterisk</span> are required.</p>
      </header>
      <div class="tf-01__body mt-8 grid gap-[1.35rem]">
        <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,14rem),1fr))] gap-[1.35rem]">
          <div class="group/f grid gap-[.45rem]">
            <label for="tf-01-name" class="text-[.875rem] font-semibold">Full name <span aria-hidden="true">*</span></label>
            <input id="tf-01-name" name="name" type="text" autocomplete="name" required placeholder="Ada Lovelace" aria-describedby="tf-01-name-err" class="min-h-[3.1rem] w-full rounded-[.85rem] border border-tf01-line bg-tf01-field px-4 py-[.85rem] text-[1rem] text-tf01-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf01),background_.2s] placeholder:text-tf01-muted/75 hover:border-[color-mix(in_oklab,var(--color-tf01-ink)_30%,var(--color-tf01-line))] focus-visible:border-tf01-accent focus-visible:bg-tf01-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf01-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf01-bad in-[.is-tried]:invalid:border-tf01-bad">
            <p id="tf-01-name-err" class="hidden items-center gap-[.4rem] text-[.8125rem] text-tf01-bad group-has-[:user-invalid]/f:flex group-has-[:user-invalid]/f:animate-tf01-shake in-[.is-tried]:group-has-[:invalid]/f:flex"><svg viewBox="0 0 16 16" aria-hidden="true" class="size-4 flex-none fill-none stroke-current stroke-[1.6] [stroke-linecap:round]"><circle cx="8" cy="8" r="7"/><path d="M8 4.5v4M8 11h.01"/></svg>Please enter your name.</p>
          </div>
          <div class="group/f grid gap-[.45rem]">
            <label for="tf-01-email" class="text-[.875rem] font-semibold">Work email <span aria-hidden="true">*</span></label>
            <input id="tf-01-email" name="email" type="email" autocomplete="email" required placeholder="[email protected]" aria-describedby="tf-01-email-err" class="min-h-[3.1rem] w-full rounded-[.85rem] border border-tf01-line bg-tf01-field px-4 py-[.85rem] text-[1rem] text-tf01-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf01),background_.2s] placeholder:text-tf01-muted/75 hover:border-[color-mix(in_oklab,var(--color-tf01-ink)_30%,var(--color-tf01-line))] focus-visible:border-tf01-accent focus-visible:bg-tf01-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf01-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf01-bad in-[.is-tried]:invalid:border-tf01-bad">
            <p id="tf-01-email-err" class="hidden items-center gap-[.4rem] text-[.8125rem] text-tf01-bad group-has-[:user-invalid]/f:flex group-has-[:user-invalid]/f:animate-tf01-shake in-[.is-tried]:group-has-[:invalid]/f:flex"><svg viewBox="0 0 16 16" aria-hidden="true" class="size-4 flex-none fill-none stroke-current stroke-[1.6] [stroke-linecap:round]"><circle cx="8" cy="8" r="7"/><path d="M8 4.5v4M8 11h.01"/></svg>Enter an email like [email protected].</p>
          </div>
        </div>
        <fieldset class="flex flex-wrap gap-2">
          <legend class="mb-[.6rem] text-[.875rem] font-semibold">What's this about?</legend>
          <label class="group/c relative cursor-pointer"><input type="radio" name="tf-01-topic" value="project" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.6rem] items-center gap-[.4rem] rounded-full border border-tf01-line bg-tf01-field px-4 text-[.9rem] font-medium [transition:background_.2s,color_.2s,border-color_.2s,scale_.2s_var(--ease-tf01)] before:size-[.45rem] before:scale-60 before:rounded-full before:bg-current before:opacity-25 before:[transition:opacity_.2s,scale_.3s_var(--ease-tf01)] before:content-[''] group-hover/c:border-[color-mix(in_oklab,var(--color-tf01-ink)_30%,var(--color-tf01-line))] group-active/c:scale-96 peer-checked:border-tf01-ink peer-checked:bg-tf01-ink peer-checked:text-tf01-card peer-checked:before:scale-100 peer-checked:before:bg-tf01-accent peer-checked:before:opacity-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tf01-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">New project</span></label>
          <label class="group/c relative cursor-pointer"><input type="radio" name="tf-01-topic" value="support" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.6rem] items-center gap-[.4rem] rounded-full border border-tf01-line bg-tf01-field px-4 text-[.9rem] font-medium [transition:background_.2s,color_.2s,border-color_.2s,scale_.2s_var(--ease-tf01)] before:size-[.45rem] before:scale-60 before:rounded-full before:bg-current before:opacity-25 before:[transition:opacity_.2s,scale_.3s_var(--ease-tf01)] before:content-[''] group-hover/c:border-[color-mix(in_oklab,var(--color-tf01-ink)_30%,var(--color-tf01-line))] group-active/c:scale-96 peer-checked:border-tf01-ink peer-checked:bg-tf01-ink peer-checked:text-tf01-card peer-checked:before:scale-100 peer-checked:before:bg-tf01-accent peer-checked:before:opacity-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tf01-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Support</span></label>
          <label class="group/c relative cursor-pointer"><input type="radio" name="tf-01-topic" value="press" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.6rem] items-center gap-[.4rem] rounded-full border border-tf01-line bg-tf01-field px-4 text-[.9rem] font-medium [transition:background_.2s,color_.2s,border-color_.2s,scale_.2s_var(--ease-tf01)] before:size-[.45rem] before:scale-60 before:rounded-full before:bg-current before:opacity-25 before:[transition:opacity_.2s,scale_.3s_var(--ease-tf01)] before:content-[''] group-hover/c:border-[color-mix(in_oklab,var(--color-tf01-ink)_30%,var(--color-tf01-line))] group-active/c:scale-96 peer-checked:border-tf01-ink peer-checked:bg-tf01-ink peer-checked:text-tf01-card peer-checked:before:scale-100 peer-checked:before:bg-tf01-accent peer-checked:before:opacity-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tf01-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Press</span></label>
          <label class="group/c relative cursor-pointer"><input type="radio" name="tf-01-topic" value="careers" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.6rem] items-center gap-[.4rem] rounded-full border border-tf01-line bg-tf01-field px-4 text-[.9rem] font-medium [transition:background_.2s,color_.2s,border-color_.2s,scale_.2s_var(--ease-tf01)] before:size-[.45rem] before:scale-60 before:rounded-full before:bg-current before:opacity-25 before:[transition:opacity_.2s,scale_.3s_var(--ease-tf01)] before:content-[''] group-hover/c:border-[color-mix(in_oklab,var(--color-tf01-ink)_30%,var(--color-tf01-line))] group-active/c:scale-96 peer-checked:border-tf01-ink peer-checked:bg-tf01-ink peer-checked:text-tf01-card peer-checked:before:scale-100 peer-checked:before:bg-tf01-accent peer-checked:before:opacity-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tf01-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Careers</span></label>
          <label class="group/c relative cursor-pointer"><input type="radio" name="tf-01-topic" value="other" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.6rem] items-center gap-[.4rem] rounded-full border border-tf01-line bg-tf01-field px-4 text-[.9rem] font-medium [transition:background_.2s,color_.2s,border-color_.2s,scale_.2s_var(--ease-tf01)] before:size-[.45rem] before:scale-60 before:rounded-full before:bg-current before:opacity-25 before:[transition:opacity_.2s,scale_.3s_var(--ease-tf01)] before:content-[''] group-hover/c:border-[color-mix(in_oklab,var(--color-tf01-ink)_30%,var(--color-tf01-line))] group-active/c:scale-96 peer-checked:border-tf01-ink peer-checked:bg-tf01-ink peer-checked:text-tf01-card peer-checked:before:scale-100 peer-checked:before:bg-tf01-accent peer-checked:before:opacity-100 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tf01-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Something else</span></label>
        </fieldset>
        <div class="group/f grid gap-[.45rem]">
          <div class="flex items-center justify-between gap-4">
            <label for="tf-01-msg" class="text-[.875rem] font-semibold">Message <span aria-hidden="true">*</span></label>
            <div class="tf-01__counter group/ct inline-flex items-center gap-2 text-[.8125rem] text-tf01-muted tabular-nums [--ring-c:var(--color-tf01-ok)] data-[state=over]:text-tf01-bad data-[state=over]:[--ring-c:var(--color-tf01-bad)] data-[state=warn]:text-tf01-warn data-[state=warn]:[--ring-c:var(--color-tf01-warn)]" data-state="ok" aria-hidden="true">
              <span class="size-5 rounded-full bg-[conic-gradient(var(--ring-c)_calc(var(--tf-01-p)*1%),var(--color-tf01-line)_0)] [mask:radial-gradient(farthest-side,transparent_62%,#000_66%)] [transition:--tf-01-p_.35s_var(--ease-tf01),scale_.3s_var(--ease-tf01)] group-data-[state=over]/ct:scale-115 forced-colors:bg-[CanvasText]"></span>
              <span><b class="tf-01__n font-semibold text-tf01-ink group-data-[state=over]/ct:text-tf01-bad">0</b> / <span class="tf-01__max">500</span></span>
            </div>
          </div>
          <textarea id="tf-01-msg" name="message" required minlength="20" data-max="500" placeholder="A few sentences on goals, timeline and budget help us route you to the right person." aria-describedby="tf-01-msg-hint tf-01-msg-err" class="max-h-[20rem] min-h-[8.5rem] w-full resize-y rounded-[.85rem] border border-tf01-line bg-tf01-field px-4 py-[.85rem] text-[1rem] leading-[1.55] text-tf01-ink [field-sizing:content] [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf01),background_.2s] placeholder:text-tf01-muted/75 hover:border-[color-mix(in_oklab,var(--color-tf01-ink)_30%,var(--color-tf01-line))] focus-visible:border-tf01-accent focus-visible:bg-tf01-card focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf01-accent)_20%,transparent)] focus-visible:outline-none user-invalid:border-tf01-bad in-[.is-tried]:invalid:border-tf01-bad"></textarea>
          <p id="tf-01-msg-hint" class="text-[.8125rem] text-tf01-muted">Minimum 20 characters. <span class="tf-01__left">500 characters remaining.</span></p>
          <p id="tf-01-msg-err" class="hidden items-center gap-[.4rem] text-[.8125rem] text-tf01-bad group-has-[:user-invalid]/f:flex group-has-[:user-invalid]/f:animate-tf01-shake in-[.is-tried]:group-has-[:invalid]/f:flex"><svg viewBox="0 0 16 16" aria-hidden="true" class="size-4 flex-none fill-none stroke-current stroke-[1.6] [stroke-linecap:round]"><circle cx="8" cy="8" r="7"/><path d="M8 4.5v4M8 11h.01"/></svg><span class="tf-01__msgerr">Write at least 20 characters.</span></p>
          <p class="sr-only" aria-live="polite" id="tf-01-live"></p>
        </div>
        <div class="flex flex-wrap items-center justify-between gap-4 pt-2">
          <label class="inline-flex min-h-11 cursor-pointer items-center gap-[.6rem] text-[.9rem] text-tf01-muted"><input type="checkbox" name="copy" class="m-0 size-[1.15rem] accent-tf01-accent"><span>Send me a copy of this message</span></label>
          <button class="tf-01__send group/s inline-flex min-h-[3.1rem] cursor-pointer items-center gap-[.6rem] rounded-full border-0 bg-tf01-accent px-6 font-semibold text-tf01-on shadow-[0_10px_24px_-10px_color-mix(in_oklab,var(--color-tf01-accent)_80%,black)] [transition:translate_.2s_var(--ease-tf01),box-shadow_.2s_var(--ease-tf01),filter_.2s] hover:-translate-y-0.5 hover:brightness-105 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf01-ink active:translate-y-px forced-colors:border forced-colors:border-[ButtonText]" type="button">
            <span>Send message</span>
            <svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.1rem] fill-none stroke-current stroke-[1.9] [stroke-linejoin:round] [transition:translate_.35s_var(--ease-tf01),rotate_.35s_var(--ease-tf01)] group-hover/s:translate-x-[3px] group-hover/s:-translate-y-[3px] group-hover/s:-rotate-8"><path d="M4 12 20 4l-5 16-3-7-8-1Z"/></svg>
          </button>
        </div>
      </div>
      <div class="tf-01__done grid animate-tf01-done justify-items-center gap-[.6rem] px-4 pt-12 pb-4 text-center outline-none" hidden tabindex="-1">
        <span class="grid size-[4.5rem] place-items-center rounded-full bg-tf01-ok/16 text-tf01-ok" aria-hidden="true"><svg viewBox="0 0 24 24" class="size-[2.2rem] animate-tf01-draw fill-none stroke-current stroke-[2.4] [stroke-dasharray:24] [stroke-dashoffset:24] [stroke-linecap:round] [stroke-linejoin:round] motion-reduce:[stroke-dashoffset:0]"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>
        <h3 class="mt-2 font-tf01-serif text-[2.4rem] leading-none font-normal">Message sent.</h3>
        <p class="mb-4 text-tf01-muted">Thanks — a real person will reply within one business day.</p>
        <button class="tf-01__again inline-flex min-h-[3.1rem] cursor-pointer items-center gap-[.6rem] rounded-full border-0 bg-tf01-accent px-6 font-semibold text-tf01-on shadow-[0_10px_24px_-10px_color-mix(in_oklab,var(--color-tf01-accent)_80%,black)] [transition:translate_.2s_var(--ease-tf01),box-shadow_.2s_var(--ease-tf01),filter_.2s] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf01-ink forced-colors:border forced-colors:border-[ButtonText]" type="button">Send another</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf01-bg: #f3eee5;
  --color-tf01-card: #fffdf9;
  --color-tf01-field: #faf7f1;
  --color-tf01-ink: #1c1915;
  --color-tf01-muted: #6a6257;
  --color-tf01-line: #e2d9c9;
  --color-tf01-accent: #c2410c;
  --color-tf01-on: #fff;
  --color-tf01-ok: #3f6212;
  --color-tf01-warn: #b45309;
  --color-tf01-bad: #b91c1c;
  --font-tf01-serif: "Instrument Serif", ui-serif, Georgia, serif;
  --font-tf01-sans: "Geist", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf01: cubic-bezier(0.16,1,0.3,1);
  --animate-tf01-rise: tf01-rise 0.8s cubic-bezier(0.16,1,0.3,1) both;
  --animate-tf01-done: tf01-rise 0.6s cubic-bezier(0.16,1,0.3,1) both;
  --animate-tf01-shake: tf01-shake 0.35s cubic-bezier(0.16,1,0.3,1);
  --animate-tf01-draw: tf01-draw 0.6s 0.2s cubic-bezier(0.16,1,0.3,1) forwards;

  @keyframes tf01-rise {
    from {
      opacity: 0;
      translate: 0 18px;
    }
  }

  @keyframes tf01-shake {
    30% {
      translate: -3px 0;
    }

    60% {
      translate: 2px 0;
    }
  }

  @keyframes tf01-draw {
    to {
      stroke-dashoffset: 0;
    }
  }
}
/* Registered so the counter ring's sweep can transition between keystrokes — an at-rule, so it stays CSS. */

@property --tf-01-p {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-01[data-theme="dark"] {
  color-scheme: dark;
  --color-tf01-bg: #14120f;
  --color-tf01-card: #1d1a16;
  --color-tf01-field: #24201b;
  --color-tf01-ink: #f3ede4;
  --color-tf01-muted: #a59c8f;
  --color-tf01-line: #3a342c;
  --color-tf01-accent: #fb923c;
  --color-tf01-on: #1c0d02;
  --color-tf01-ok: #a3e635;
  --color-tf01-warn: #fbbf24;
  --color-tf01-bad: #f87171;
}

@media (prefers-color-scheme: dark) {
  .tf-01:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf01-bg: #14120f;
    --color-tf01-card: #1d1a16;
    --color-tf01-field: #24201b;
    --color-tf01-ink: #f3ede4;
    --color-tf01-muted: #a59c8f;
    --color-tf01-line: #3a342c;
    --color-tf01-accent: #fb923c;
    --color-tf01-on: #1c0d02;
    --color-tf01-ok: #a3e635;
    --color-tf01-warn: #fbbf24;
    --color-tf01-bad: #f87171;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-01').forEach((root) => {
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
  const root = document.querySelector('.tf-01');
  if (!root) return;
  const ta = root.querySelector('#tf-01-msg');
  const counter = root.querySelector('.tf-01__counter');
  const n = root.querySelector('.tf-01__n');
  const left = root.querySelector('.tf-01__left');
  const live = root.querySelector('#tf-01-live');
  const msgErr = root.querySelector('.tf-01__msgerr');
  const body = root.querySelector('.tf-01__body');
  const head = root.querySelector('.tf-01__head');
  const done = root.querySelector('.tf-01__done');
  const MAX = Number(ta.dataset.max) || 500, WARN = 50;
  root.querySelector('.tf-01__max').textContent = MAX;
  let lastState = 'ok';
  const update = () => {
    const len = ta.value.length, rem = MAX - len;
    const state = rem < 0 ? 'over' : rem <= WARN ? 'warn' : 'ok';
    root.style.setProperty('--tf-01-p', Math.min(100, (len / MAX) * 100));
    counter.dataset.state = state;
    n.textContent = len;
    left.textContent = rem >= 0 ? rem + ' characters remaining.' : Math.abs(rem) + ' characters over the limit.';
    ta.setCustomValidity(rem < 0 ? 'Too long' : '');
    msgErr.textContent = rem < 0 ? 'Please shorten your message by ' + Math.abs(rem) + ' characters.' : 'Write at least 20 characters.';
    if (state !== lastState) { live.textContent = left.textContent; lastState = state; }
  };
  ta.addEventListener('input', update);
  update();
  root.querySelector('.tf-01__send').addEventListener('click', () => {
    const fields = [...root.querySelectorAll('input[required], textarea[required]')];
    const bad = fields.find((f) => !f.checkValidity());
    if (bad) { root.classList.add('is-tried'); bad.focus(); return; }
    body.hidden = true; head.hidden = true; done.hidden = false; done.focus();
  });
  root.querySelector('.tf-01__again').addEventListener('click', () => {
    root.querySelectorAll('input[type="text"], input[type="email"], textarea').forEach((f) => { f.value = ''; });
    root.classList.remove('is-tried'); update();
    done.hidden = true; body.hidden = false; head.hidden = false;
    root.querySelector('#tf-01-name').focus();
  });
})();
```

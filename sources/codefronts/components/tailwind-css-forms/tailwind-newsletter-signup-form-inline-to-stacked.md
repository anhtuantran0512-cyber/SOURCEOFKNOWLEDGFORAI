---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-newsletter-signup-form-inline-to-stacked/"
title: "Tailwind Newsletter Signup Form, Inline to Stacked"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's newsletter form, ported one-for-one to Tailwind v4: it adapts to whatever slot it's dropped into using v4's built-in container queries,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Newsletter Signup Form, Inline to Stacked
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-newsletter-signup-form-inline-to-stacked/

The CSS collection's newsletter form, ported one-for-one to Tailwind v4: it adapts to whatever slot it's dropped into using v4's built-in container queries, morphing from a full-width stack to a split row to a single fused pill. Drag the frame's corner to watch it reflow live — a readout names the current layout — with type that scales in cqi, topic chips, and a neo-brutalist offset shadow.
## HTML
```html
<div class="tf-05 relative block min-h-svh w-full [background:radial-gradient(circle_at_1px_1px,color-mix(in_oklab,var(--color-tf05-ink)_14%,transparent)_1px,transparent_0)_0_0_/_22px_22px,var(--color-tf05-bg)] pt-[72px] font-tf05-sans leading-[normal] text-tf05-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,4vw,3rem)]">
    <div class="grid w-full max-w-[64rem] gap-3">
      <p class="text-[.8rem] font-semibold tracking-[.04em] text-tf05-muted uppercase tabular-nums [@media(hover:none)]:hidden" aria-hidden="true"><span class="tf-05__w">—</span> · <span class="tf-05__mode rounded-[.3rem] bg-tf05-accent px-[.45rem] py-[.1rem] text-tf05-on">layout</span> · drag the corner ↘</p>
      <div class="tf-05__frame @container/nl w-full max-w-full min-w-[17rem] overflow-hidden rounded-[1.75rem] bg-tf05-paper shadow-[0_0_0_2px_var(--color-tf05-ink),10px_10px_0_var(--color-tf05-ink)] [resize:horizontal] forced-colors:border-2 forced-colors:border-[CanvasText] [@media(hover:none)]:[resize:none]">
        <div class="grid gap-[1.1rem] p-[clamp(1.25rem,6cqi,3.5rem)]" role="form" aria-labelledby="tf-05-title">
          <div class="flex justify-between border-b-2 border-tf05-ink pb-[.9rem] text-[.75rem] font-semibold tracking-[.12em] text-tf05-muted uppercase" aria-hidden="true"><span>No. 142</span><span class="@max-[29.99rem]/nl:hidden">Every Friday</span></div>
          <h2 id="tf-05-title" class="text-[clamp(2rem,10cqi,5.5rem)] leading-[.92] font-extrabold tracking-[-.045em] text-balance [font-variation-settings:'opsz'_96]">The Friday <em class="bg-[linear-gradient(transparent_58%,var(--color-tf05-accent)_58%_92%,transparent_92%)] px-[.05em] not-italic">Fold.</em></h2>
          <p class="max-w-[38rem] text-[clamp(1rem,2.4cqi,1.2rem)] leading-[1.5] text-pretty text-tf05-muted">One email a week on front-end craft — new CSS, honest benchmarks, and one thing worth stealing. Read by 48,000 developers.</p>
          <div class="mt-[.4rem] grid gap-[.6rem] @[30rem]/nl:grid-cols-[minmax(0,1fr)_auto] @[44rem]/nl:gap-0 @[44rem]/nl:rounded-full @[44rem]/nl:bg-tf05-field @[44rem]/nl:p-[.4rem] @[44rem]/nl:shadow-[inset_0_0_0_2px_var(--color-tf05-ink)] @[44rem]/nl:transition-shadow @[44rem]/nl:duration-200 @[44rem]/nl:focus-within:shadow-[inset_0_0_0_3px_var(--color-tf05-ink),0_0_0_5px_var(--color-tf05-accent)]">
            <label for="tf-05-email" class="sr-only">Email address</label>
            <input id="tf-05-email" type="email" autocomplete="email" required placeholder="[email protected]" aria-describedby="tf-05-note" class="min-h-[3.4rem] w-full rounded-2xl border-0 bg-tf05-field px-[1.2rem] text-[1.05rem] text-tf05-ink shadow-[inset_0_0_0_2px_var(--color-tf05-ink)] transition-shadow duration-200 placeholder:text-tf05-muted/80 focus-visible:shadow-[inset_0_0_0_3px_var(--color-tf05-ink),0_0_0_5px_var(--color-tf05-accent)] focus-visible:outline-none user-invalid:shadow-[inset_0_0_0_2px_var(--color-tf05-bad)] @[44rem]/nl:rounded-full @[44rem]/nl:bg-transparent @[44rem]/nl:shadow-none!">
            <button class="tf-05__btn group/b inline-flex min-h-[3.4rem] cursor-pointer items-center justify-center gap-[.55rem] rounded-2xl border-0 bg-tf05-accent px-[1.6rem] text-[1.05rem] font-extrabold tracking-[-.01em] text-tf05-on shadow-[inset_0_0_0_2px_var(--color-tf05-ink),4px_4px_0_var(--color-tf05-ink)] [transition:translate_.15s_var(--ease-tf05),box-shadow_.15s_var(--ease-tf05)] hover:-translate-x-0.5 hover:-translate-y-0.5 hover:shadow-[inset_0_0_0_2px_var(--color-tf05-ink),6px_6px_0_var(--color-tf05-ink)] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tf05-ink active:translate-x-[3px] active:translate-y-[3px] active:shadow-[inset_0_0_0_2px_var(--color-tf05-ink),0_0_0_var(--color-tf05-ink)] forced-colors:border-2 forced-colors:border-[ButtonText] @max-[29.99rem]/nl:w-full @[44rem]/nl:rounded-full @[44rem]/nl:shadow-[inset_0_0_0_2px_var(--color-tf05-ink)] @[44rem]/nl:hover:translate-x-0 @[44rem]/nl:hover:translate-y-0 @[44rem]/nl:hover:shadow-[inset_0_0_0_2px_var(--color-tf05-ink)] @[44rem]/nl:hover:brightness-105 @[44rem]/nl:active:translate-x-0 @[44rem]/nl:active:translate-y-0 @[44rem]/nl:active:scale-97" type="button"><span>Subscribe</span><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.2rem] fill-none stroke-current stroke-[2.4] [stroke-linecap:round] [stroke-linejoin:round] [transition:translate_.3s_var(--ease-tf05)] group-hover/b:translate-x-[3px]"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
          </div>
          <fieldset class="flex flex-wrap gap-[.45rem]">
            <legend class="sr-only">Topics you're interested in</legend>
            <label class="relative cursor-pointer"><input type="checkbox" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.4rem] items-center gap-[.4rem] rounded-full px-[.9rem] text-[.88rem] font-semibold shadow-[inset_0_0_0_1.5px_color-mix(in_oklab,var(--color-tf05-ink)_40%,transparent)] [transition:background_.2s,box-shadow_.2s] before:font-extrabold before:[transition:rotate_.3s_var(--ease-tf05)] before:content-['+'] peer-checked:bg-tf05-ink peer-checked:text-tf05-paper peer-checked:shadow-none peer-checked:before:content-['✓'] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf05-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">CSS</span></label>
            <label class="relative cursor-pointer"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.4rem] items-center gap-[.4rem] rounded-full px-[.9rem] text-[.88rem] font-semibold shadow-[inset_0_0_0_1.5px_color-mix(in_oklab,var(--color-tf05-ink)_40%,transparent)] [transition:background_.2s,box-shadow_.2s] before:font-extrabold before:[transition:rotate_.3s_var(--ease-tf05)] before:content-['+'] peer-checked:bg-tf05-ink peer-checked:text-tf05-paper peer-checked:shadow-none peer-checked:before:content-['✓'] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf05-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Accessibility</span></label>
            <label class="relative cursor-pointer"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.4rem] items-center gap-[.4rem] rounded-full px-[.9rem] text-[.88rem] font-semibold shadow-[inset_0_0_0_1.5px_color-mix(in_oklab,var(--color-tf05-ink)_40%,transparent)] [transition:background_.2s,box-shadow_.2s] before:font-extrabold before:[transition:rotate_.3s_var(--ease-tf05)] before:content-['+'] peer-checked:bg-tf05-ink peer-checked:text-tf05-paper peer-checked:shadow-none peer-checked:before:content-['✓'] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf05-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Performance</span></label>
            <label class="relative cursor-pointer"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.4rem] items-center gap-[.4rem] rounded-full px-[.9rem] text-[.88rem] font-semibold shadow-[inset_0_0_0_1.5px_color-mix(in_oklab,var(--color-tf05-ink)_40%,transparent)] [transition:background_.2s,box-shadow_.2s] before:font-extrabold before:[transition:rotate_.3s_var(--ease-tf05)] before:content-['+'] peer-checked:bg-tf05-ink peer-checked:text-tf05-paper peer-checked:shadow-none peer-checked:before:content-['✓'] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf05-ink forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Design systems</span></label>
          </fieldset>
          <p class="text-[.85rem] text-tf05-muted" id="tf-05-note">No spam. Unsubscribe in one click.</p>
          <p class="tf-05__status font-semibold empty:hidden data-[ok=false]:text-tf05-bad data-[ok=true]:animate-tf05-pop data-[ok=true]:rounded-2xl data-[ok=true]:bg-tf05-accent data-[ok=true]:px-[1.1rem] data-[ok=true]:py-[.9rem] data-[ok=true]:text-tf05-on" role="status" aria-live="polite"></p>
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
  --color-tf05-bg: #ecebe4;
  --color-tf05-paper: #fbfaf5;
  --color-tf05-ink: #0d0d0b;
  --color-tf05-muted: #56554e;
  --color-tf05-field: #ffffff;
  --color-tf05-accent: #c6f432;
  --color-tf05-on: #0d0d0b;
  --color-tf05-bad: #d4380d;
  --font-tf05-sans: "Bricolage Grotesque", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf05: cubic-bezier(0.16,1,0.3,1);
  --animate-tf05-pop: tf05-pop 0.5s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf05-pop {
    from {
      scale: 0.95;
      opacity: 0;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch. @theme holds the light values; dark values
   override the same variables, forced by data-theme="dark" or picked up from the OS. */

.tf-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
}

.tf-05[data-theme="dark"] {
  color-scheme: dark;
  --color-tf05-bg: #0f0f0d;
  --color-tf05-paper: #181815;
  --color-tf05-ink: #f4f3ea;
  --color-tf05-muted: #a8a698;
  --color-tf05-field: #22221e;
  --color-tf05-accent: #c6f432;
  --color-tf05-on: #0d0d0b;
  --color-tf05-bad: #ff7a45;
}

@media (prefers-color-scheme: dark) {
  .tf-05:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf05-bg: #0f0f0d;
    --color-tf05-paper: #181815;
    --color-tf05-ink: #f4f3ea;
    --color-tf05-muted: #a8a698;
    --color-tf05-field: #22221e;
    --color-tf05-accent: #c6f432;
    --color-tf05-on: #0d0d0b;
    --color-tf05-bad: #ff7a45;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-05').forEach((root) => {
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
  const root = document.querySelector('.tf-05');
  if (!root) return;
  const frame = root.querySelector('.tf-05__frame'), w = root.querySelector('.tf-05__w'), mode = root.querySelector('.tf-05__mode');
  const rem = parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;
  new ResizeObserver(([e]) => {
    const px = Math.round(e.contentBoxSize ? e.contentBoxSize[0].inlineSize : e.contentRect.width);
    w.textContent = px + 'px';
    mode.textContent = px >= 44 * rem ? 'fused pill' : px >= 30 * rem ? 'split row' : 'stacked';
  }).observe(frame);
  const email = root.querySelector('#tf-05-email'), status = root.querySelector('.tf-05__status');
  const go = () => {
    if (!email.checkValidity() || !email.value) { status.dataset.ok = 'false'; status.textContent = 'Please enter a valid email address.'; email.focus(); return; }
    status.dataset.ok = 'true';
    status.textContent = 'Almost there — check ' + email.value + ' and confirm your subscription.';
  };
  root.querySelector('.tf-05__btn').addEventListener('click', go);
  email.addEventListener('keydown', (e) => { if (e.key === 'Enter') go(); });
})();
```

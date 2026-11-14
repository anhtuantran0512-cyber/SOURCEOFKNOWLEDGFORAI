---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/tailwind-cookie-consent-banner-dismiss-button/"
title: "Tailwind Cookie Consent Banner Dismiss Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "A GDPR-style consent bar whose Dismiss pill carries a CSS-drawn × after its label."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cookie Consent Banner Dismiss Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/tailwind-cookie-consent-banner-dismiss-button/

A GDPR-style consent bar whose Dismiss pill carries a CSS-drawn × after its label. data-dismissed:translate-y-[120%] data-dismissed:opacity-0 data-dismissed:invisible slides it away; inert removes it from the tab order the instant it leaves. The port also fixes the original's dead "Accept all" button — both choices now close the banner and announce what happened.
## HTML
```html
<section class="tcb-05 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb05-bg),var(--color-tcb05-bg2))] px-6 py-12 font-tcb05-sans" aria-label="Cookie banner dismiss button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="grid w-full max-w-[34rem] justify-items-center gap-4">
      <div id="tcb-05-banner" role="region" aria-label="Cookie consent" class="flex w-full flex-wrap items-center gap-x-6 gap-y-4 rounded-[1.25rem] bg-tcb05-surface px-6 py-5 text-tcb05-ink shadow-[0_24px_54px_-26px_var(--color-tcb05-shadow)] ring-1 ring-white/8 transition-[translate,opacity,visibility] duration-350 data-dismissed:invisible data-dismissed:translate-y-[120%] data-dismissed:opacity-0 motion-reduce:transition-none">
        <div class="flex flex-1 basis-56 items-start gap-3">
          <span aria-hidden="true" class="mt-0.5 grid size-8 flex-none place-items-center rounded-full bg-tcb05-acc/15 text-tcb05-acc"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 3a9 9 0 1 0 9 9 3 3 0 0 1-3-3 3 3 0 0 1-3-3 3 3 0 0 1-3-3Z"/><circle cx="9" cy="13" r=".8" fill="currentColor"/><circle cx="14" cy="16" r=".8" fill="currentColor"/></svg></span>
          <p class="text-[13.5px]/[1.55] text-tcb05-ink/90 text-pretty">We use cookies to improve your experience and analyse traffic. <a href="#" class="font-medium text-tcb05-ink underline decoration-tcb05-acc underline-offset-3 hover:decoration-2 focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcb05-acc">Policy</a></p>
        </div>
        <div class="flex gap-2.5">
          <button type="button" data-choice="accepted" class="inline-flex min-h-11 cursor-pointer items-center rounded-full border-[1.5px] border-tcb05-acc bg-tcb05-acc px-4.5 text-[13.5px] font-semibold text-tcb05-on transition duration-150 hover:-translate-y-px hover:shadow-[0_8px_18px_-8px_rgb(0_0_0/0.5)] focus-visible:outline-[2.5px] focus-visible:outline-offset-2 focus-visible:outline-tcb05-acc active:translate-y-0 active:scale-97 motion-reduce:transition-none">Accept all</button>
          <button type="button" data-choice="essential" class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-full border-[1.5px] border-tcb05-ink/45 px-4.5 text-[13.5px] font-semibold transition duration-150 hover:-translate-y-px hover:border-tcb05-ink/70 hover:shadow-[0_8px_18px_-8px_rgb(0_0_0/0.5)] focus-visible:outline-[2.5px] focus-visible:outline-offset-2 focus-visible:outline-tcb05-acc active:translate-y-0 active:scale-97 motion-reduce:transition-none">
            Dismiss
            <span aria-hidden="true" class="relative size-2.5 before:absolute before:top-1/2 before:left-1/2 before:h-[1.8px] before:w-3 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-current after:absolute after:top-1/2 after:left-1/2 after:h-[1.8px] after:w-3 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-current"></span>
          </button>
        </div>
      </div>
      <p id="tcb-05-status" role="status" class="min-h-5 text-[13px] text-tcb05-mut"></p>
      <button id="tcb-05-reset" type="button" hidden class="min-h-11 cursor-pointer px-2 text-[13px] font-medium text-tcb05-mut underline decoration-dashed underline-offset-4 hover:text-tcb05-surface focus-visible:outline-2 focus-visible:outline-tcb05-surface">Show banner again</button>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb05-mono text-[11.5px] text-tcb05-mut ring-1 ring-black/8">data-dismissed: · invisible · inert</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb05-bg: #f1f6f7;
  --color-tcb05-bg: oklch(0.96 0.008 200);
  --color-tcb05-bg2: #e1eaed;
  --color-tcb05-bg2: oklch(0.92 0.015 210);
  --color-tcb05-surface: #1f2230;
  --color-tcb05-surface: oklch(0.23 0.02 270);
  --color-tcb05-ink: #e8e9f0;
  --color-tcb05-ink: oklch(0.93 0.01 270);
  --color-tcb05-mut: #3f5761;
  --color-tcb05-mut: oklch(0.42 0.04 220);
  --color-tcb05-acc: #4fd4a2;
  --color-tcb05-acc: oklch(0.78 0.14 160);
  --color-tcb05-on: #0d2a1f;
  --color-tcb05-on: oklch(0.22 0.04 160);
  --color-tcb05-shadow: #22253ab3;
  --color-tcb05-shadow: oklch(0.3 0.04 270 / 0.7);
  --font-tcb05-sans: 'Geist', system-ui, sans-serif;
  --font-tcb05-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-05 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const banner = document.getElementById('tcb-05-banner');
  if (!banner || banner.dataset.wired) return;
  banner.dataset.wired = '1';
  const reset = document.getElementById('tcb-05-reset');
  const status = document.getElementById('tcb-05-status');
  banner.querySelectorAll('[data-choice]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const choice = btn.dataset.choice;
      banner.setAttribute('data-dismissed', '');
      banner.inert = true;
      status.textContent = choice === 'accepted' ? 'All cookies accepted.' : 'Only essential cookies will be used.';
      // Production: localStorage.setItem('consent', choice);
      reset.hidden = false;
      reset.focus();
    });
  });
  reset.addEventListener('click', () => {
    banner.removeAttribute('data-dismissed');
    banner.inert = false;
    status.textContent = '';
    reset.hidden = true;
  });
})();
```

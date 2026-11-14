---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-login-form-focus-ring/"
title: "Accessible Tailwind Dark Mode Login Form with Focus Rings"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A sign-in form where the focus indicator is the feature."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind Dark Mode Login Form with Focus Rings
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-login-form-focus-ring/

A sign-in form where the focus indicator is the feature. Every control — email, password, reveal toggle, remember-me, both buttons and the recovery link — carries a 2px focus-visible:outline-tdm08-focus ring in a per-theme token measured at 3:1 or better. Proxied rings (has-focus-visible:) put the indicator on the visible element when the real input is hidden.
## HTML
```html
<div class="tdm-08 scheme-light-dark has-[#tdm-08-toggle:checked]:scheme-dark dark:has-[#tdm-08-toggle:checked]:scheme-light grid w-full min-h-svh place-items-center bg-tdm08-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-tdm08-glow),transparent_70%)] px-4 py-12 font-tdm08-sans text-tdm08-ink antialiased transition-colors duration-300">
  <div class="grid w-full max-w-5xl items-start gap-5 lg:grid-cols-[minmax(0,1fr)_22rem]">
    <form novalidate class="grid gap-5 rounded-[28px] border border-tdm08-line bg-tdm08-surface p-6 shadow-tdm08-card sm:p-9">
      <header class="flex items-start gap-4">
        <span class="grid size-11 flex-none place-items-center rounded-2xl bg-tdm08-acc/14 text-tdm08-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/></svg></span>
        <div class="flex-1"><h1 class="text-xl font-semibold tracking-tight">Sign in to Meridian</h1><p class="mt-1 text-sm text-tdm08-mut">Every focus state below is audited at 3:1 minimum.</p></div>
        <label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm08-line bg-tdm08-surface transition duration-200 hover:-translate-y-px hover:border-tdm08-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm08-focus motion-reduce:transition-none ">
        <input id="tdm-08-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm08-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm08-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label>
      </header>
      <div class="grid gap-2">
        <label for="tdm-08-email" class="text-sm font-medium">Work email</label>
        <input id="tdm-08-email" name="email" type="email" required inputmode="email" autocomplete="username" placeholder="[email protected]" class="min-h-12 rounded-xl border border-tdm08-line bg-tdm08-field px-4 text-[15px] text-tdm08-ink placeholder:text-tdm08-mut/70 transition hover:border-tdm08-mut/50 focus-visible:border-tdm08-focus focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm08-focus user-invalid:border-tdm08-danger">
      </div>
      <div class="group/pw grid gap-2">
        <div class="flex items-center justify-between"><label for="tdm-08-pass" class="text-sm font-medium">Password</label><a href="#tdm-08" class="rounded text-sm font-medium text-tdm08-acc underline decoration-tdm08-acc/40 underline-offset-4 hover:decoration-tdm08-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm08-focus">Forgot?</a></div>
        <div class="relative">
          <input id="tdm-08-pass" name="password" type="text" autocomplete="current-password" placeholder="At least 12 characters" spellcheck="false" class="min-h-12 w-full rounded-xl border border-tdm08-line bg-tdm08-field ps-4 pe-14 text-[15px] text-tdm08-ink [-webkit-text-security:disc] placeholder:text-tdm08-mut/70 placeholder-shown:[-webkit-text-security:none] group-has-[#tdm-08-reveal:checked]/pw:[-webkit-text-security:none] transition hover:border-tdm08-mut/50 focus-visible:border-tdm08-focus focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm08-focus">
          <label class="absolute inset-y-0.5 end-0.5 grid w-12 cursor-pointer place-items-center rounded-[10px] text-tdm08-mut transition hover:text-tdm08-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm08-focus">
            <input type="checkbox" id="tdm-08-reveal" class="sr-only"><span class="sr-only">Show password</span>
            <svg class="size-5 group-has-[#tdm-08-reveal:checked]/pw:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 12S6 5 12 5s9.5 7 9.5 7-3.5 7-9.5 7-9.5-7-9.5-7Z"/><circle cx="12" cy="12" r="3"/></svg><svg class="hidden size-5 group-has-[#tdm-08-reveal:checked]/pw:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3l18 18M10.6 5.1A9.6 9.6 0 0 1 12 5c6 0 9.5 7 9.5 7a17 17 0 0 1-2.7 3.6M6.6 6.6A17 17 0 0 0 2.5 12S6 19 12 19a9.4 9.4 0 0 0 5.4-1.6M9.9 9.9a3 3 0 0 0 4.2 4.2"/></svg>
          </label>
        </div>
      </div>
      <label class="group/rm flex min-h-11 w-fit cursor-pointer items-center gap-3 rounded-lg pe-2 text-sm text-tdm08-mut has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm08-focus">
        <input type="checkbox" id="tdm-08-remember" class="sr-only">
        <span class="grid size-5 place-items-center rounded-md border border-tdm08-line bg-tdm08-field transition group-has-checked/rm:border-tdm08-acc group-has-checked/rm:bg-tdm08-acc" aria-hidden="true"><svg class="size-3.5 text-tdm08-acc-ink opacity-0 transition group-has-checked/rm:opacity-100" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>
        Keep me signed in on this device
      </label>
      <div class="grid gap-2.5 sm:grid-cols-2">
        <button type="button" class="min-h-12 rounded-xl bg-tdm08-acc px-5 text-[15px] font-semibold text-tdm08-acc-ink shadow-[0_10px_30px_-12px_var(--color-tdm08-acc)] transition hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm08-focus motion-reduce:transition-none">Continue</button>
        <button type="button" class="inline-flex min-h-12 items-center justify-center gap-2 rounded-xl border border-tdm08-line px-5 text-[15px] font-medium transition hover:bg-tdm08-ink/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm08-focus"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 7 8.5 6 8.5-6"/></svg>Email me a link</button>
      </div>
    </form>
    <aside aria-label="Focus ring audit" class="grid gap-4 rounded-[28px] border border-tdm08-line bg-tdm08-raised p-6">
      <h2 class="flex items-center gap-2 text-sm font-semibold"><svg class="size-4 text-tdm08-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 4.5 6v6c0 4.5 3.2 7.8 7.5 9 4.3-1.2 7.5-4.5 7.5-9V6Z"/><path d="m9 12 2 2 4-4"/></svg>Focus audit — WCAG 2.2 (2.4.13)</h2>
      <ul class="grid gap-1.5">
        <li class="flex items-center justify-between gap-3 rounded-xl border border-tdm08-line bg-tdm08-surface px-3 py-2.5 text-[13px]"><span class="flex items-center gap-2"><svg class="size-3.5 text-tdm08-ok" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Email field</span><span class="text-right font-tdm08-mono text-[11px] text-tdm08-mut">2px ring · offset 2 · <b class="font-medium text-tdm08-ink">12.1:1</b></span></li>
        <li class="flex items-center justify-between gap-3 rounded-xl border border-tdm08-line bg-tdm08-surface px-3 py-2.5 text-[13px]"><span class="flex items-center gap-2"><svg class="size-3.5 text-tdm08-ok" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Password field</span><span class="text-right font-tdm08-mono text-[11px] text-tdm08-mut">2px ring · offset 2 · <b class="font-medium text-tdm08-ink">12.1:1</b></span></li>
        <li class="flex items-center justify-between gap-3 rounded-xl border border-tdm08-line bg-tdm08-surface px-3 py-2.5 text-[13px]"><span class="flex items-center gap-2"><svg class="size-3.5 text-tdm08-ok" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Reveal toggle</span><span class="text-right font-tdm08-mono text-[11px] text-tdm08-mut">proxied via has- · <b class="font-medium text-tdm08-ink">12.1:1</b></span></li>
        <li class="flex items-center justify-between gap-3 rounded-xl border border-tdm08-line bg-tdm08-surface px-3 py-2.5 text-[13px]"><span class="flex items-center gap-2"><svg class="size-3.5 text-tdm08-ok" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Remember checkbox</span><span class="text-right font-tdm08-mono text-[11px] text-tdm08-mut">ring on label · <b class="font-medium text-tdm08-ink">12.1:1</b></span></li>
        <li class="flex items-center justify-between gap-3 rounded-xl border border-tdm08-line bg-tdm08-surface px-3 py-2.5 text-[13px]"><span class="flex items-center gap-2"><svg class="size-3.5 text-tdm08-ok" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Primary button</span><span class="text-right font-tdm08-mono text-[11px] text-tdm08-mut">ring outside fill · <b class="font-medium text-tdm08-ink">5.4:1</b></span></li>
        <li class="flex items-center justify-between gap-3 rounded-xl border border-tdm08-line bg-tdm08-surface px-3 py-2.5 text-[13px]"><span class="flex items-center gap-2"><svg class="size-3.5 text-tdm08-ok" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Recovery link</span><span class="text-right font-tdm08-mono text-[11px] text-tdm08-mut">underline + ring · <b class="font-medium text-tdm08-ink">7.1:1</b></span></li>
      </ul>
      <p class="text-[13px]/relaxed text-pretty text-tdm08-mut">Dark ring <code class="font-tdm08-mono text-tdm08-ink">#67e8f9</code> on <code class="font-tdm08-mono text-tdm08-ink">#0b0d11</code>. Light ring <code class="font-tdm08-mono text-tdm08-ink">#4c1d95</code> on <code class="font-tdm08-mono text-tdm08-ink">#ffffff</code>. Press <kbd class="rounded border border-tdm08-line px-1 font-tdm08-mono text-[11px]">Tab</kbd> to walk the form.</p>
    </aside>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm08-bg: light-dark(#f2f3f7, #07080b);
  --color-tdm08-glow: light-dark(rgb(76 29 149 / .07), rgb(34 211 238 / .07));
  --color-tdm08-surface: light-dark(#ffffff, #0f1116);
  --color-tdm08-raised: light-dark(#f8f8fb, #12151c);
  --color-tdm08-field: light-dark(#f7f7fa, #0b0d11);
  --color-tdm08-ink: light-dark(#0b0d12, #f3f5f8);
  --color-tdm08-mut: light-dark(#585e6b, #9aa3b2);
  --color-tdm08-line: light-dark(#dfe2e9, #252935);
  --color-tdm08-acc: light-dark(#5b21b6, #22d3ee);
  --color-tdm08-acc-ink: light-dark(#ffffff, #04212b);
  --color-tdm08-focus: light-dark(#4c1d95, #67e8f9);
  --color-tdm08-danger: light-dark(#be123c, #fb7185);
  --color-tdm08-ok: light-dark(#15803d, #4ade80);
  --color-tdm08-sun: light-dark(#b45309, transparent);
  --color-tdm08-moon: light-dark(transparent, #a5f3fc);
  --shadow-tdm08-card: 0 40px 90px -60px light-dark(rgb(30 20 60 / .35), rgb(0 0 0 / .9));
  --font-tdm08-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm08-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

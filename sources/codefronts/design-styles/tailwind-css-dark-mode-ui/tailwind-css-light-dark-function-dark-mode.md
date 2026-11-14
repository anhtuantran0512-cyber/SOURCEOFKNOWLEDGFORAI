---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-css-light-dark-function-dark-mode/"
title: "Tailwind CSS light-dark() Dark Mode Without Media Queries"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "The modern way to write a theme, taken to its limit: no media query and no token block for the demo surface."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS light-dark() Dark Mode Without Media Queries
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-css-light-dark-function-dark-mode/

The modern way to write a theme, taken to its limit: no media query and no token block for the demo surface. Every colour on the review card is an arbitrary value — bg-[light-dark(#fff,#13151a)] — and the switch changes a single property, color-scheme, via scheme-* utilities. A locked panel pins scheme-only-light to prove one subtree can opt out.
## HTML
```html
<div class="tdm-04 scheme-light-dark has-[#tdm-04-toggle:checked]:scheme-dark dark:has-[#tdm-04-toggle:checked]:scheme-light grid w-full min-h-svh place-items-center bg-[light-dark(#eef1f4,#07080a)] px-4 py-12 font-tdm04-sans text-[light-dark(#0a0b0d,#f2f4f7)] antialiased transition-colors duration-300">
  <div class="w-full max-w-5xl overflow-hidden rounded-[28px] border border-[light-dark(#e1e5ea,#21252c)] bg-[light-dark(#ffffff,#0e1014)] shadow-[0_40px_80px_-50px_light-dark(#0a0b0d40,#000000e6)]">
    <header class="flex items-center justify-between gap-4 border-b border-[light-dark(#e4e7ec,#21252c)] px-5 py-3.5">
      <div class="flex items-center gap-3">
        <span class="grid size-10 place-items-center rounded-xl bg-[light-dark(#ccfbf1,#0f2f2b)] text-[light-dark(#0f766e,#5eead4)]"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3c.6 4.3 2.7 6.4 7 7-4.3.6-6.4 2.7-7 7-.6-4.3-2.7-6.4-7-7 4.3-.6 6.4-2.7 7-7Z"/></svg></span>
        <div><p class="font-tdm04-mono text-sm font-semibold">light-dark()</p><p class="text-xs text-[light-dark(#5a616e,#98a0ae)]">one value, both themes</p></div>
      </div>
      <label class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl border border-[light-dark(#e1e5ea,#2a2f38)] bg-[light-dark(#f6f7f9,#151820)] px-3.5 text-sm font-medium transition hover:border-[light-dark(#0f766e,#5eead4)] has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-[light-dark(#0f766e,#99f6e4)]">
        <input id="tdm-04-toggle" type="checkbox" class="sr-only">
        <span class="grid"><svg class="col-start-1 row-start-1 size-4 text-[light-dark(#b45309,transparent)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg><svg class="col-start-1 row-start-1 size-4 text-[light-dark(transparent,#5eead4)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg></span>
        Invert scheme
      </label>
    </header>
    <div class="grid md:grid-cols-2">
      <section class="grid content-start gap-5 p-6 sm:p-8">
        <h1 class="text-[clamp(1.6rem,3vw,2.2rem)] font-semibold tracking-[-0.035em]">Zero media queries</h1>
        <p class="max-w-[48ch] text-[15px]/relaxed text-pretty text-[light-dark(#5a616e,#98a0ae)]">Each colour declares its light and dark value inline. The switch changes one property — <code class="font-tdm04-mono text-[13px] text-[light-dark(#0a0b0d,#f2f4f7)]">color-scheme</code> — and every value below re-resolves.</p>
        <dl class="grid gap-2 font-tdm04-mono text-[12.5px]">
          <div class="flex flex-wrap items-center justify-between gap-2 rounded-xl border border-[light-dark(#e4e7ec,#262a32)] bg-[light-dark(#f6f7f9,#13151a)] px-3.5 py-2.5"><dt class="text-[light-dark(#0f766e,#5eead4)]">bg</dt><dd class="flex items-center gap-2 text-[light-dark(#5a616e,#98a0ae)]"><span class="size-3.5 rounded border border-[light-dark(#0000001a,#ffffff26)] bg-[light-dark(#f6f7f9,#0a0b0d)]"></span>light-dark(#f6f7f9, #0a0b0d)</dd></div>
          <div class="flex flex-wrap items-center justify-between gap-2 rounded-xl border border-[light-dark(#e4e7ec,#262a32)] bg-[light-dark(#f6f7f9,#13151a)] px-3.5 py-2.5"><dt class="text-[light-dark(#0f766e,#5eead4)]">surface</dt><dd class="flex items-center gap-2 text-[light-dark(#5a616e,#98a0ae)]"><span class="size-3.5 rounded border border-[light-dark(#0000001a,#ffffff26)] bg-[light-dark(#ffffff,#13151a)]"></span>light-dark(#ffffff, #13151a)</dd></div>
          <div class="flex flex-wrap items-center justify-between gap-2 rounded-xl border border-[light-dark(#e4e7ec,#262a32)] bg-[light-dark(#f6f7f9,#13151a)] px-3.5 py-2.5"><dt class="text-[light-dark(#0f766e,#5eead4)]">ink</dt><dd class="flex items-center gap-2 text-[light-dark(#5a616e,#98a0ae)]"><span class="size-3.5 rounded border border-[light-dark(#0000001a,#ffffff26)] bg-[light-dark(#0a0b0d,#f2f4f7)]"></span>light-dark(#0a0b0d, #f2f4f7)</dd></div>
          <div class="flex flex-wrap items-center justify-between gap-2 rounded-xl border border-[light-dark(#e4e7ec,#262a32)] bg-[light-dark(#f6f7f9,#13151a)] px-3.5 py-2.5"><dt class="text-[light-dark(#0f766e,#5eead4)]">accent</dt><dd class="flex items-center gap-2 text-[light-dark(#5a616e,#98a0ae)]"><span class="size-3.5 rounded border border-[light-dark(#0000001a,#ffffff26)] bg-[light-dark(#0f766e,#5eead4)]"></span>light-dark(#0f766e, #5eead4)</dd></div>
        </dl>
      </section>
      <section class="grid content-center gap-4 border-t border-[light-dark(#e4e7ec,#21252c)] bg-[light-dark(#f6f7f9,#0a0b0d)] p-6 sm:p-8 md:border-t-0 md:border-l">
        <article class=" grid gap-3 rounded-2xl border border-[light-dark(#e4e7ec,#262a32)] bg-[light-dark(#ffffff,#13151a)] p-5 text-[light-dark(#0a0b0d,#f2f4f7)] shadow-[0_20px_40px_-30px_light-dark(#0a0b0d40,#000000cc)]">
          <div class="flex items-center gap-3">
            <span class="grid size-9 place-items-center rounded-full bg-[light-dark(#ccfbf1,#0f2f2b)] text-xs font-semibold text-[light-dark(#0f766e,#5eead4)]">PS</span>
            <div class="min-w-0 flex-1"><h2 class="text-[15px] font-semibold tracking-tight">Priya Sharma</h2><p class="font-tdm04-mono text-[11px] text-[light-dark(#5a616e,#98a0ae)]">Inherits page scheme</p></div>
          </div>
          <p class="text-sm/relaxed text-pretty text-[light-dark(#5a616e,#98a0ae)]">Requested review on <code class="font-tdm04-mono text-[12px]">theme.css</code> — 3 files changed.</p>
          <div class="flex gap-2">
            <button type="button" class="min-h-11 rounded-xl bg-[light-dark(#0f766e,#5eead4)] px-4 text-sm font-medium text-[light-dark(#ffffff,#04211c)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[light-dark(#0f766e,#99f6e4)]">Approve</button>
            <button type="button" class="min-h-11 rounded-xl border border-[light-dark(#e1e5ea,#2a2f38)] px-4 text-sm font-medium transition hover:bg-[light-dark(#f1f3f5,#191c22)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[light-dark(#0f766e,#99f6e4)]">Comment</button>
          </div>
        </article>
        <article class="scheme-only-light grid gap-3 rounded-2xl border border-[light-dark(#e4e7ec,#262a32)] bg-[light-dark(#ffffff,#13151a)] p-5 text-[light-dark(#0a0b0d,#f2f4f7)] shadow-[0_20px_40px_-30px_light-dark(#0a0b0d40,#000000cc)]">
          <div class="flex items-center gap-3">
            <span class="grid size-9 place-items-center rounded-full bg-[light-dark(#ccfbf1,#0f2f2b)] text-xs font-semibold text-[light-dark(#0f766e,#5eead4)]"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/></svg></span>
            <div class="min-w-0 flex-1"><h2 class="text-[15px] font-semibold tracking-tight">Locked panel</h2><p class="font-tdm04-mono text-[11px] text-[light-dark(#5a616e,#98a0ae)]">scheme-only-light</p></div>
          </div>
          <p class="text-sm/relaxed text-pretty text-[light-dark(#5a616e,#98a0ae)]">This subtree pins its own scheme, so its colours never invert.</p>
          <div class="flex gap-2">
            <button type="button" class="min-h-11 rounded-xl bg-[light-dark(#0f766e,#5eead4)] px-4 text-sm font-medium text-[light-dark(#ffffff,#04211c)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[light-dark(#0f766e,#99f6e4)]">Approve</button>
            <button type="button" class="min-h-11 rounded-xl border border-[light-dark(#e1e5ea,#2a2f38)] px-4 text-sm font-medium transition hover:bg-[light-dark(#f1f3f5,#191c22)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[light-dark(#0f766e,#99f6e4)]">Comment</button>
          </div>
        </article>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-tdm04-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm04-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-delete-confirmation-dialog/"
title: "Tailwind Dark Mode Delete Confirmation Dialog (Editorial)"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "An editorial take on the confirmation dialog: deep navy rather than neutral black, warm off-white ink rather than pure white, an Instrument Serif headline…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Delete Confirmation Dialog (Editorial)
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-delete-confirmation-dialog/

An editorial take on the confirmation dialog: deep navy rather than neutral black, warm off-white ink rather than pure white, an Instrument Serif headline over a sans body. The palette borrows from newspaper dark modes, where warmth keeps long-form text comfortable — and it turns a destructive action into something read rather than clicked through. Native <dialog>, opened and closed by invoker commands.
## HTML
```html
<div class="tdm-13 scheme-dark grid w-full min-h-svh place-items-center bg-tdm13-navy bg-[radial-gradient(110%_80%_at_15%_0%,#161c3a,transparent_62%)] px-4 py-14 font-tdm13-sans text-tdm13-ink antialiased">
  <div class="grid w-full max-w-2xl gap-6">
    <p class="font-tdm13-sans text-[11px] uppercase tracking-[0.22em] text-tdm13-muted">Workspace · Danger zone</p>
    <h1 class="font-tdm13-serif text-[clamp(2.6rem,7vw,4.4rem)] leading-[0.95] tracking-[-0.01em] text-balance">The Atlantic Review</h1>
    <div class="h-px bg-tdm13-rule" aria-hidden="true"></div>
    <p class="max-w-[56ch] text-[16px]/[1.75] text-pretty text-tdm13-muted">Eleven editors, four hundred drafts and a decade of archives live in this workspace. Removing it is permanent, so the confirmation is deliberately slow to read.</p>
    <div class="flex flex-wrap items-center gap-4">
      <button type="button" command="show-modal" commandfor="tdm-13-dialog" class="inline-flex min-h-12 items-center gap-2.5 rounded-full border border-tdm13-danger/60 px-6 text-[15px] font-medium text-tdm13-danger transition hover:bg-tdm13-danger hover:text-tdm13-danger-ink focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tdm13-focus">Delete workspace <svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 5.5l6.5 6.5-6.5 6.5"/></svg></button>
      <span class="text-[13px] text-tdm13-muted">Owner only · logged to the audit trail</span>
    </div>
  </div>

  <dialog id="tdm-13-dialog" closedby="any" aria-labelledby="tdm-13-t" aria-describedby="tdm-13-b" class="m-auto w-[min(34rem,calc(100%-2rem))] max-w-none rounded-[6px] border border-tdm13-hair bg-tdm13-sheet p-0 text-tdm13-ink shadow-[0_60px_120px_-40px_rgb(0_0_0/.85)] opacity-0 translate-y-6 transition-[opacity,translate,display,overlay] transition-discrete duration-400 ease-out open:opacity-100 open:translate-y-0 starting:open:opacity-0 starting:open:translate-y-6 backdrop:bg-tdm13-scrim backdrop:backdrop-blur-sm motion-reduce:transition-none">
    <div class="grid gap-6 p-7 sm:p-9">
      <div class="flex items-center justify-between">
        <span class="grid size-11 place-items-center rounded-full border border-tdm13-danger/40 text-tdm13-danger"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 6.5h17M9 6.5V4h6v2.5M6 6.5l1 13.5h10l1-13.5M10 11v5M14 11v5"/></svg></span>
        <button type="button" command="close" commandfor="tdm-13-dialog" class="grid size-11 place-items-center rounded-full text-tdm13-muted transition hover:bg-tdm13-ink/8 hover:text-tdm13-ink focus-visible:outline-2 focus-visible:outline-tdm13-focus"><span class="sr-only">Close</span><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
      </div>
      <h2 id="tdm-13-t" class="font-tdm13-serif text-[clamp(1.9rem,5vw,2.5rem)] leading-[1.05] text-balance">Delete <em>The Atlantic Review</em>?</h2>
      <p id="tdm-13-b" class="text-[15px]/[1.7] text-pretty text-tdm13-muted">Every draft, comment thread and published piece will be removed from our servers within 24 hours. Exports created before today remain valid for 30 days.</p>
      <ul class="grid border-y border-tdm13-hair">
        <li class="flex gap-4 py-3 text-[15px] "><span class="font-tdm13-serif text-lg leading-6 text-tdm13-danger italic" aria-hidden="true">i.</span>412 drafts and 1,908 revisions</li>
        <li class="flex gap-4 py-3 text-[15px] border-t border-tdm13-hair"><span class="font-tdm13-serif text-lg leading-6 text-tdm13-danger italic" aria-hidden="true">ii.</span>11 editors lose access immediately</li>
        <li class="flex gap-4 py-3 text-[15px] border-t border-tdm13-hair"><span class="font-tdm13-serif text-lg leading-6 text-tdm13-danger italic" aria-hidden="true">iii.</span>Custom domain released after 24 hours</li>
      </ul>
      <div class="flex flex-wrap-reverse justify-end gap-3">
        <button type="button" command="close" commandfor="tdm-13-dialog" autofocus class="min-h-12 rounded-full border border-tdm13-rule px-6 text-[15px] font-medium transition hover:bg-tdm13-ink/6 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm13-focus">Keep workspace</button>
        <button type="button" command="close" commandfor="tdm-13-dialog" class="inline-flex min-h-12 items-center gap-2 rounded-full bg-tdm13-danger px-6 text-[15px] font-semibold text-tdm13-danger-ink transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm13-focus"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 6.5h17M9 6.5V4h6v2.5M6 6.5l1 13.5h10l1-13.5M10 11v5M14 11v5"/></svg>Delete permanently</button>
      </div>
      <p class="text-center text-xs text-tdm13-muted">Requires owner privileges · logged to the audit trail</p>
    </div>
  </dialog>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm13-navy: #0b0e18;
  --color-tdm13-sheet: #141a2e;
  --color-tdm13-ink: #f4f1e8;
  --color-tdm13-muted: #aab0c6;
  --color-tdm13-rule: rgb(244 241 232 / .24);
  --color-tdm13-hair: rgb(244 241 232 / .12);
  --color-tdm13-danger: #ff8f7a;
  --color-tdm13-danger-ink: #2a0b06;
  --color-tdm13-focus: #8ab4ff;
  --color-tdm13-scrim: rgb(4 6 14 / .76);
  --font-tdm13-serif: 'Instrument Serif', 'Iowan Old Style', Georgia, serif;
  --font-tdm13-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

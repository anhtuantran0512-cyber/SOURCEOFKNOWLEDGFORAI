---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-modal-dialog-backdrop/"
title: "Tailwind Dark Mode Modal Dialog with Blurred Backdrop"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "A real modal, with zero script: a native <dialog> opened by command=\"show-modal\", so focus trapping, Esc, the top layer and inertness are all the browser's."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Modal Dialog with Blurred Backdrop
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-modal-dialog-backdrop/

A real modal, with zero script: a native <dialog> opened by command="show-modal", so focus trapping, Esc, the top layer and inertness are all the browser's. Tailwind styles the scrim with backdrop:, animates entry with starting:open:, and the destructive button only arms once the workspace name is typed — enforced by pattern and group-has-[:valid].
## HTML
```html
<div class="tdm-07 scheme-light-dark has-[#tdm-07-toggle:checked]:scheme-dark dark:has-[#tdm-07-toggle:checked]:scheme-light grid w-full min-h-svh place-items-center bg-tdm07-bg bg-[radial-gradient(80%_60%_at_50%_0%,var(--color-tdm07-glow),transparent_70%)] px-4 py-12 font-tdm07-sans text-tdm07-ink antialiased transition-colors duration-300">
  <section class="grid w-full max-w-xl gap-6 rounded-[28px] border border-tdm07-line bg-tdm07-surface p-6 shadow-tdm07-card sm:p-8">
    <header class="flex items-start justify-between gap-4">
      <div class="grid gap-1.5">
        <p class="font-tdm07-mono text-[11px] uppercase tracking-[0.14em] text-tdm07-mut">Settings / Danger zone</p>
        <h1 class="font-tdm07-mono text-[22px] font-semibold tracking-tight">acme-platform</h1>
      </div>
      <label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm07-line bg-tdm07-surface transition duration-200 hover:-translate-y-px hover:border-tdm07-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm07-focus motion-reduce:transition-none ">
        <input id="tdm-07-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm07-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm07-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label>
    </header>
    <p class="text-[15px]/relaxed text-pretty text-tdm07-mut">Deleting a workspace removes every deployment, environment variable and log stream it owns. The confirmation below is a native dialog — focus-trapped, Esc-dismissable, no script.</p>
    <div class="flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-tdm07-danger/30 bg-tdm07-danger/6 p-4">
      <div class="min-w-0"><p class="text-sm font-semibold">Delete this workspace</p><p class="text-[13px] text-tdm07-mut">3 projects · 41 deployments · 12 secrets</p></div>
      <button type="button" command="show-modal" commandfor="tdm-07-dialog" class="inline-flex min-h-11 items-center gap-2 rounded-xl border border-tdm07-danger/50 px-4 text-sm font-semibold text-tdm07-danger transition hover:bg-tdm07-danger hover:text-tdm07-danger-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm07-focus"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 6.5h17M9 6.5V4h6v2.5M6 6.5l1 13.5h10l1-13.5M10 11v5M14 11v5"/></svg>Delete workspace</button>
    </div>
  </section>

  <dialog id="tdm-07-dialog" closedby="any" aria-labelledby="tdm-07-title" aria-describedby="tdm-07-desc" class="group/dlg m-auto w-[min(32rem,calc(100%-2rem))] max-w-none rounded-[26px] border border-tdm07-line bg-tdm07-raised p-0 text-tdm07-ink shadow-tdm07-sheet opacity-0 translate-y-4 scale-[.97] transition-[opacity,translate,scale,display,overlay] transition-discrete duration-300 ease-out open:opacity-100 open:translate-y-0 open:scale-100 starting:open:opacity-0 starting:open:translate-y-4 starting:open:scale-[.97] backdrop:bg-tdm07-scrim backdrop:opacity-0 backdrop:backdrop-blur-md backdrop:transition-[opacity,display,overlay] backdrop:transition-discrete backdrop:duration-300 open:backdrop:opacity-100 starting:open:backdrop:opacity-0 motion-reduce:transition-none motion-reduce:backdrop:transition-none">
    <div class="grid gap-5 p-6 sm:p-7">
      <div class="flex gap-4">
        <span class="grid size-12 flex-none place-items-center rounded-2xl bg-tdm07-danger/12 text-tdm07-danger ring-1 ring-tdm07-danger/25"><svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.3 4.2 2.6 17.5A2 2 0 0 0 4.3 20.5h15.4a2 2 0 0 0 1.7-3L13.7 4.2a2 2 0 0 0-3.4 0Z"/><path d="M12 9.5v4M12 17h.01"/></svg></span>
        <div class="grid gap-1.5">
          <h2 id="tdm-07-title" class="text-lg font-semibold tracking-tight">Delete this workspace?</h2>
          <p id="tdm-07-desc" class="text-sm/relaxed text-pretty text-tdm07-mut">This cannot be undone. 3 projects, 41 deployments and 12 secrets will be permanently removed.</p>
        </div>
      </div>
      <dl class="grid grid-cols-3 divide-x divide-tdm07-line overflow-hidden rounded-2xl border border-tdm07-line bg-tdm07-field">
        <div class="grid gap-0.5 px-3.5 py-3"><dt class="text-[11px] text-tdm07-mut">Workspace</dt><dd class="truncate font-tdm07-mono text-[13px]">acme-platform</dd></div>
        <div class="grid gap-0.5 px-3.5 py-3"><dt class="text-[11px] text-tdm07-mut">Owner</dt><dd class="truncate font-tdm07-mono text-[13px]">Sam Rivera</dd></div>
        <div class="grid gap-0.5 px-3.5 py-3"><dt class="text-[11px] text-tdm07-mut">Region</dt><dd class="truncate font-tdm07-mono text-[13px]">iad1</dd></div>
      </dl>
      <label for="tdm-07-confirm" class="grid gap-2 text-sm">
        <span class="text-tdm07-mut">Type <strong class="font-tdm07-mono font-semibold text-tdm07-ink">acme-platform</strong> to confirm</span>
        <input id="tdm-07-confirm" type="text" required pattern="acme-platform" placeholder="acme-platform" autocomplete="off" spellcheck="false" class="min-h-12 rounded-xl border border-tdm07-line bg-tdm07-field px-3.5 font-tdm07-mono text-sm text-tdm07-ink placeholder:text-tdm07-mut/60 transition focus-visible:border-tdm07-focus focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-tdm07-focus/60 valid:border-tdm07-danger/60">
      </label>
      <div class="flex flex-wrap items-center justify-between gap-3 border-t border-tdm07-line pt-5">
        <p class="text-xs text-tdm07-mut">Deletion runs immediately.</p>
        <div class="flex gap-2">
          <button type="button" command="close" commandfor="tdm-07-dialog" autofocus class="min-h-11 rounded-xl border border-tdm07-line px-4 text-sm font-medium transition hover:bg-tdm07-ink/6 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm07-focus">Keep workspace</button>
          <button type="button" command="close" commandfor="tdm-07-dialog" class="pointer-events-none inline-flex min-h-11 items-center gap-2 rounded-xl bg-tdm07-danger px-4 text-sm font-semibold text-tdm07-danger-ink opacity-40 transition group-has-[#tdm-07-confirm:valid]/dlg:pointer-events-auto group-has-[#tdm-07-confirm:valid]/dlg:opacity-100 group-has-[#tdm-07-confirm:valid]/dlg:shadow-[0_10px_30px_-10px_var(--color-tdm07-danger)] hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm07-focus"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 6.5h17M9 6.5V4h6v2.5M6 6.5l1 13.5h10l1-13.5M10 11v5M14 11v5"/></svg>Delete forever</button>
        </div>
      </div>
    </div>
  </dialog>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm07-bg: light-dark(#f3f3f6, #09090d);
  --color-tdm07-glow: light-dark(rgb(225 29 72 / .06), rgb(251 113 133 / .07));
  --color-tdm07-surface: light-dark(#ffffff, #111117);
  --color-tdm07-raised: light-dark(#ffffff, #18181f);
  --color-tdm07-field: light-dark(#f7f7f9, #0e0e13);
  --color-tdm07-ink: light-dark(#0c0c12, #f4f4f6);
  --color-tdm07-mut: light-dark(#5b5e69, #9b9baa);
  --color-tdm07-line: light-dark(#e3e3ea, #282833);
  --color-tdm07-acc: light-dark(#be123c, #fb7185);
  --color-tdm07-danger: light-dark(#be123c, #fb7185);
  --color-tdm07-danger-ink: light-dark(#ffffff, #26060f);
  --color-tdm07-focus: light-dark(#0369a1, #7dd3fc);
  --color-tdm07-scrim: light-dark(rgb(20 20 30 / .38), rgb(4 4 8 / .74));
  --color-tdm07-sun: light-dark(#b45309, transparent);
  --color-tdm07-moon: light-dark(transparent, #fecdd3);
  --shadow-tdm07-card: 0 40px 80px -56px light-dark(rgb(15 15 25 / .3), rgb(0 0 0 / .9));
  --shadow-tdm07-sheet: 0 1px 0 light-dark(rgb(255 255 255 / .8), rgb(255 255 255 / .06)) inset, 0 50px 100px -40px rgb(0 0 0 / .6);
  --font-tdm07-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm07-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-session-timeout-warning-modal-countdown/"
title: "Tailwind Session Timeout Warning Modal with Countdown"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "The idle-timeout warning banks and health portals ship, as a native <dialog> styled entirely in utilities: backdrop: blurs the page, open:starting: scales…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Session Timeout Warning Modal with Countdown
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-session-timeout-warning-modal-countdown/

The idle-timeout warning banks and health portals ship, as a native <dialog> styled entirely in utilities: backdrop: blurs the page, open:starting: scales the modal in with no script, and one data-urgent attribute turns the clock, bar and icon red in the final 30 seconds. New: a real expired state and a confirmation toast after Stay signed in.
## HTML
```html
<section class="tcd-03 w-full min-h-svh grid place-items-center bg-tcd03-page px-4 py-12 font-tcd03-sans text-tcd03-ink antialiased" aria-labelledby="tcd-03-title">
  <div class="grid w-full max-w-[880px] justify-items-center gap-5">
    <div aria-hidden="true" class="w-full overflow-hidden rounded-2xl border border-tcd03-rule bg-tcd03-card shadow-tcd03-app">
      <header class="flex flex-wrap items-center justify-between gap-x-4 gap-y-1 border-b border-tcd03-rule px-5 py-3.5 text-[13px] text-tcd03-mut">
        <strong class="flex items-center gap-2 text-sm font-bold text-tcd03-ink"><span class="grid size-6 place-items-center rounded-md bg-tcd03-acc text-[11px] text-white">V</span>Vale Health</strong>
        <span class="flex items-center gap-2"><span class="size-6 rounded-full bg-tcd03-rule"></span>Priya Sharma · Member portal</span>
      </header>
      <div class="px-5 pt-5 pb-7">
        <h2 id="tcd-03-title" class="mb-4 text-[clamp(18px,3vw,22px)] font-bold">Claim 4471-B</h2>
        <div class="grid gap-2.5"><span class="block h-3 rounded-md bg-tcd03-rule"></span><span class="block h-3 w-[82%] rounded-md bg-tcd03-rule"></span><span class="block h-3 w-[64%] rounded-md bg-tcd03-rule"></span><span class="block h-3 w-[47%] rounded-md bg-tcd03-rule"></span></div>
      </div>
    </div>

    <dialog id="tcd-03-dialog" role="alertdialog" aria-labelledby="tcd-03-dtitle" aria-describedby="tcd-03-dtext" class="group/dlg m-auto w-[min(440px,calc(100vw-32px))] rounded-2xl border border-tcd03-rule bg-tcd03-card p-[clamp(22px,4vw,32px)] text-tcd03-ink shadow-tcd03-dialog transition-[opacity,scale] duration-300 backdrop:bg-tcd03-ink/45 backdrop:backdrop-blur-[3px] open:starting:scale-95 open:starting:opacity-0">
      <div aria-hidden="true" class="mb-4 grid size-11 place-items-center rounded-xl bg-tcd03-acc/10 text-tcd03-acc group-data-urgent/dlg:bg-tcd03-danger/10 group-data-urgent/dlg:text-tcd03-danger">
        <svg viewBox="0 0 24 24" width="22" height="22" class="group-data-urgent/dlg:animate-tcd03-tick motion-reduce:animate-none"><circle cx="12" cy="12" r="9.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 7.4v5.1l3.2 2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </div>
      <h3 id="tcd-03-dtitle" data-dtitle class="mb-2 text-[clamp(19px,3.4vw,23px)] font-bold tracking-[-0.01em]">Still there?</h3>
      <p id="tcd-03-dtext" data-dtext class="mb-5 text-[13.5px] leading-relaxed text-tcd03-mut text-pretty">For your security we sign you out after ten minutes without activity. Your claim draft is saved.</p>
      <p role="timer" class="mb-2.5 flex items-baseline justify-between gap-3 text-[15px] font-medium group-data-urgent/dlg:text-tcd03-danger"><span data-label>Your session expires in</span><time datetime="" data-clock class="text-[26px] font-extrabold tracking-[-0.02em] tabular-nums">2:00</time></p>
      <div aria-hidden="true" class="h-1.5 overflow-hidden rounded-full bg-tcd03-rule"><span data-fill class="block h-full w-full rounded-full bg-tcd03-acc transition-[width,background-color] duration-1000 ease-linear group-data-urgent/dlg:bg-tcd03-danger motion-reduce:transition-none"></span></div>
      <div class="mt-6 flex flex-wrap gap-2.5">
        <button type="button" data-extend autofocus class="min-h-11 flex-[1_1_150px] cursor-pointer rounded-xl bg-tcd03-acc px-4 text-sm font-bold text-white shadow-[0_8px_18px_-10px_var(--color-tcd03-acc)] transition hover:brightness-110 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd03-ink">Stay signed in</button>
        <button type="button" data-out class="min-h-11 flex-[1_1_150px] cursor-pointer rounded-xl border border-tcd03-rule px-4 text-sm font-bold transition hover:bg-tcd03-page active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd03-ink group-data-expired/dlg:hidden">Sign out now</button>
      </div>
      <p class="mt-3.5 text-[11.5px] text-tcd03-mut group-data-expired/dlg:hidden">Escape will not close this — the warning needs an answer.</p>
      <output data-live aria-live="polite" class="sr-only"></output>
    </dialog>

    <div class="flex flex-wrap items-center justify-center gap-3">
      <button type="button" data-replay class="min-h-11 cursor-pointer rounded-xl border border-tcd03-rule bg-tcd03-card px-5 text-sm font-bold transition hover:border-tcd03-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd03-acc">Replay the idle warning</button>
      <p data-toast role="status" class="flex items-center gap-2 rounded-full bg-tcd03-ok/12 px-3.5 py-2 text-[13px] font-semibold text-tcd03-ok opacity-0 transition-opacity duration-300 data-show:opacity-100"></p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd03-page: #eef2f8;
  --color-tcd03-page: oklch(0.96 0.012 250);
  --color-tcd03-card: #ffffff;
  --color-tcd03-card: oklch(1 0 0);
  --color-tcd03-ink: #0f1b2d;
  --color-tcd03-ink: oklch(0.24 0.04 255);
  --color-tcd03-mut: #55627a;
  --color-tcd03-mut: oklch(0.49 0.03 258);
  --color-tcd03-rule: #dbe3ef;
  --color-tcd03-rule: oklch(0.91 0.016 252);
  --color-tcd03-acc: #1f5fe0;
  --color-tcd03-acc: oklch(0.52 0.19 262);
  --color-tcd03-danger: #c0392f;
  --color-tcd03-danger: oklch(0.52 0.19 28);
  --color-tcd03-ok: #1e7a4a;
  --color-tcd03-ok: oklch(0.5 0.12 155);
  --font-tcd03-sans: 'Manrope', system-ui, sans-serif;
  --shadow-tcd03-app: 0 14px 30px -18px rgb(15 27 45 / 0.4);
  --shadow-tcd03-dialog: 0 30px 70px -26px rgb(15 27 45 / 0.55);
  --animate-tcd03-tick: tcd03-tick 1s ease-in-out infinite;

  @keyframes tcd03-tick {
    0%,
        100% {
      transform: rotate(0);
    }

    25% {
      transform: rotate(-8deg);
    }

    75% {
      transform: rotate(8deg);
    }
  }
}

.tcd-03 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-03');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const dlg = root.querySelector('#tcd-03-dialog'), q = (s) => dlg.querySelector(s);
  const clock = q('[data-clock]'), fill = q('[data-fill]'), live = q('[data-live]'), extend = q('[data-extend]');
  const toast = root.querySelector('[data-toast]'), WARN = 120e3;
  let target = 0, id = 0, seen = null, tid = 0;
  const stop = () => { clearTimeout(id); id = 0; };
  const notify = (msg) => { clearTimeout(tid); toast.textContent = msg; toast.setAttribute('data-show', ''); tid = setTimeout(() => toast.removeAttribute('data-show'), 2600); };
  const reset = () => {
    dlg.removeAttribute('data-urgent'); dlg.removeAttribute('data-expired');
    q('[data-dtitle]').textContent = 'Still there?';
    q('[data-dtext]').textContent = 'For your security we sign you out after ten minutes without activity. Your claim draft is saved.';
    q('[data-label]').textContent = 'Your session expires in';
    extend.textContent = 'Stay signed in';
  };
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    clock.textContent = Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
    clock.dateTime = new Date(target).toISOString();
    fill.style.width = (ms / WARN * 100).toFixed(1) + '%';
    dlg.toggleAttribute('data-urgent', ms > 0 && ms <= 30e3);
    const b = ms <= 0 ? 'end' : ms <= 30e3 ? 's30' : ms <= 60e3 ? 'm1' : 'm2';
    if (b !== seen) { seen = b; live.textContent = b === 'end' ? 'Session expired. Sign in again to continue.' : 'Session expires in about ' + s + ' seconds. Choose stay signed in or sign out.'; }
    if (ms > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); return; }
    dlg.setAttribute('data-expired', '');
    q('[data-dtitle]').textContent = 'You have been signed out';
    q('[data-dtext]').textContent = 'Your claim draft was saved before the session ended. Sign in again to pick up where you left off.';
    q('[data-label]').textContent = 'Session expired';
    extend.textContent = 'Sign in again';
  };
  const open = () => { stop(); reset(); target = Date.now() + WARN; seen = null; if (!dlg.open) dlg.showModal(); tick(); };
  const close = (msg) => { stop(); dlg.close(); notify(msg); };
  dlg.addEventListener('cancel', (e) => e.preventDefault());
  extend.addEventListener('click', () => close(dlg.hasAttribute('data-expired') ? 'Signed in · session renewed' : 'Session extended by 10 minutes'));
  q('[data-out]').addEventListener('click', () => close('Signed out · draft saved'));
  root.querySelector('[data-replay]').addEventListener('click', open);
  const boot = setTimeout(open, 900);
  root.cleanup = () => { stop(); clearTimeout(boot); clearTimeout(tid); };
})();
```

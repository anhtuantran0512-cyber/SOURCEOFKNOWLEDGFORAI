---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-alert-card-payment-failed/"
title: "Tailwind Dark Mode Alert Card — Payment Failed Notification"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "The card that has to be read: a billing failure notice on a dark surface with a warm ember accent, a slow pulse on the status node and a retry action that is…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Alert Card — Payment Failed Notification
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-alert-card-payment-failed/

The card that has to be read: a billing failure notice on a dark surface with a warm ember accent, a slow pulse on the status node and a retry action that is clearly the primary path. Severity is carried by an icon, a labelled chip and the copy itself — the ember is reinforcement, not the message. Service impact rows pair a dot with a written state.
## HTML
```html
<div class="tdm-22 scheme-dark grid w-full min-h-svh place-items-center bg-tdm22-bg bg-[radial-gradient(100%_65%_at_50%_0%,#1c120a,transparent_64%)] px-4 py-12 font-tdm22-sans text-tdm22-ink antialiased">
  <section role="alert" aria-labelledby="tdm-22-t" class="grid w-full max-w-[38rem] gap-6 rounded-[28px] border border-tdm22-line bg-tdm22-surface p-6 shadow-[0_0_0_1px_rgb(255_139_61/.06),0_50px_100px_-50px_rgb(0_0_0/.9),0_0_80px_-30px_rgb(255_139_61/.25)] sm:p-8 forced-colors:border-[CanvasText] forced-colors:shadow-none">
    <header class="grid gap-4">
      <div class="flex items-center gap-4">
        <span aria-hidden="true" class="relative grid size-12 flex-none place-items-center rounded-full bg-tdm22-ember/15 text-tdm22-ember">
          <span class="absolute inset-0 rounded-full border border-tdm22-ember/60 animate-tdm22-ring motion-reduce:hidden forced-colors:hidden"></span>
          <span class="absolute inset-0 rounded-full border border-tdm22-ember/60 animate-tdm22-ring [animation-delay:1.2s] motion-reduce:hidden forced-colors:hidden"></span>
          <svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6.5 15h3"/></svg>
        </span>
        <span class="inline-flex items-center gap-1.5 rounded-full border border-tdm22-ember/40 bg-tdm22-ember/10 px-3 py-1 text-xs font-semibold text-tdm22-ember"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.3 4.2 2.6 17.5A2 2 0 0 0 4.3 20.5h15.4a2 2 0 0 0 1.7-3L13.7 4.2a2 2 0 0 0-3.4 0Z"/><path d="M12 9.5v4M12 17h.01"/></svg>Action required</span>
      </div>
      <h1 id="tdm-22-t" class="text-[clamp(1.35rem,3vw,1.65rem)] font-semibold leading-tight tracking-[-0.025em] text-balance">Payment for invoice INV-4821 failed</h1>
      <p class="text-[15px]/relaxed text-pretty text-tdm22-muted">Your card ending 4242 was declined on 14 August. Production stays online for <strong class="font-semibold text-tdm22-ink">5 more days</strong>, then deployments pause automatically.</p>
    </header>
    <dl class="grid grid-cols-3 divide-x divide-tdm22-line overflow-hidden rounded-2xl border border-tdm22-line bg-tdm22-raised">
      <div class="grid gap-1 px-4 py-3.5"><dt class="text-xs text-tdm22-muted">Amount due</dt><dd class="font-tdm22-mono text-[13px] font-medium tabular-nums">$1,480.00</dd></div>
      <div class="grid gap-1 px-4 py-3.5"><dt class="text-xs text-tdm22-muted">Attempted</dt><dd class="font-tdm22-mono text-[13px] font-medium tabular-nums">3× · 06:12 UTC</dd></div>
      <div class="grid gap-1 px-4 py-3.5"><dt class="text-xs text-tdm22-muted">Grace ends</dt><dd class="font-tdm22-mono text-[13px] font-medium tabular-nums">19 Aug, 23:59</dd></div>
    </dl>
    <ul class="grid gap-1" aria-label="Service impact">
      <li class="flex items-center gap-3 rounded-xl px-1 py-2 text-sm"><span class="size-2 flex-none rounded-full bg-tdm22-ok ring-4 ring-tdm22-ok/15" aria-hidden="true"></span><span class="flex-1">Edge runtime</span><em class="font-tdm22-mono text-xs not-italic text-tdm22-ok">Online</em></li>
      <li class="flex items-center gap-3 rounded-xl px-1 py-2 text-sm"><span class="size-2 flex-none rounded-full bg-tdm22-ember ring-4 ring-tdm22-ember/15" aria-hidden="true"></span><span class="flex-1">Preview deployments</span><em class="font-tdm22-mono text-xs not-italic text-tdm22-ember">Paused in 5 days</em></li>
      <li class="flex items-center gap-3 rounded-xl px-1 py-2 text-sm"><span class="size-2 flex-none rounded-full bg-tdm22-ember ring-4 ring-tdm22-ember/15" aria-hidden="true"></span><span class="flex-1">Log retention</span><em class="font-tdm22-mono text-xs not-italic text-tdm22-ember">Reduced to 24h</em></li>
    </ul>
    <footer class="flex flex-wrap-reverse items-center justify-between gap-4 border-t border-tdm22-line pt-5">
      <p class="text-[13px] text-tdm22-muted">Billing owner: Sam Rivera</p>
      <div class="flex flex-wrap gap-2">
        <button type="button" class="min-h-11 rounded-xl border border-tdm22-line px-4 text-sm font-medium transition hover:bg-tdm22-ink/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm22-focus">View invoice</button>
        <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tdm22-ember px-4 text-sm font-semibold text-tdm22-ember-ink shadow-[inset_0_1px_0_rgb(255_255_255/.3),0_10px_30px_-10px_var(--color-tdm22-ember)] transition hover:-translate-y-px hover:brightness-105 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm22-focus motion-reduce:transition-none forced-colors:border forced-colors:border-[ButtonText]"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6.5 15h3"/></svg>Update payment method</button>
      </div>
    </footer>
  </section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm22-bg: #0a0806;
  --color-tdm22-surface: #15110e;
  --color-tdm22-raised: #1d1712;
  --color-tdm22-ink: #f7f1ea;
  --color-tdm22-muted: #b5a69b;
  --color-tdm22-line: #302620;
  --color-tdm22-ember: #ff8b3d;
  --color-tdm22-ember-ink: #2b0e02;
  --color-tdm22-ok: #6ee7a8;
  --color-tdm22-focus: #ffc48a;
  --font-tdm22-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm22-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tdm22-ring: tdm22-ring 2.4s cubic-bezier(0.2, 0.6, 0.3, 1) infinite;

  @keyframes tdm22-ring {
    from {
      scale: 0.9;
      opacity: 0.55;
    }

    to {
      scale: 1.9;
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

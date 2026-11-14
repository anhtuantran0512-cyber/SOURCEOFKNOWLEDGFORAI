---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-exclusive-accordion-one-open/"
title: "Tailwind CSS Exclusive Accordion — Only One Open at a Time"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "Open one section and the others close themselves &mdash; with one HTML attribute and zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Exclusive Accordion — Only One Open at a Time
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-exclusive-accordion-one-open/

Open one section and the others close themselves &mdash; with one HTML attribute and zero JavaScript. Every <details> in this dark workspace-settings panel shares name="tac06-settings", so the browser enforces at-most-one-open like a radio group. The active panel is highlighted three ways in utilities: a gradient rail that grows in with open:before:scale-y-100, a violet glass surface, and a filled icon tile; both the opening and the browser-closed panel animate their height through details-content:.
## HTML
```html
<section class="tac-06 w-full min-h-svh grid place-items-center bg-tac06-bg bg-[radial-gradient(60%_50%_at_15%_0%,var(--color-tac06-glow),transparent_70%),radial-gradient(50%_45%_at_95%_100%,var(--color-tac06-glow2),transparent_70%)] px-5 py-14 font-tac06-sans text-tac06-ink [interpolate-size:allow-keywords]" aria-label="Exclusive one-open-at-a-time accordion demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-2xl overflow-hidden rounded-3xl bg-tac06-panel shadow-tac06-panel ring-1 ring-white/8">
      <header class="flex flex-wrap items-center gap-4 border-b border-white/8 px-[clamp(18px,4vw,28px)] py-5">
        <span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-xl bg-linear-to-br from-tac06-acc to-tac06-acc2 text-lg font-bold text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.3)]">N</span>
        <div class="min-w-0 flex-1">
          <p class="text-[13px] text-tac06-mut">Northwind Labs</p>
          <h2 class="text-lg font-semibold sm:text-xl tracking-[-0.02em]">Workspace settings</h2>
        </div>
        <span class="inline-flex items-center gap-1.5 rounded-full bg-tac06-ok/12 max-sm:hidden px-3 py-1 text-xs font-medium text-tac06-ok ring-1 ring-tac06-ok/25"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac06-ok"></span>All changes saved</span>
      </header>

      <div class="grid gap-2 p-[clamp(10px,2.4vw,16px)]">
        <details name="tac06-settings" class="group relative rounded-2xl ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 before:absolute before:inset-y-4 before:left-0 before:w-1 before:origin-top before:scale-y-0 before:rounded-r-full before:bg-linear-to-b before:from-tac06-acc before:to-tac06-acc2 before:transition-[scale] before:duration-400 before:ease-[cubic-bezier(0.22,1,0.36,1)] hover:bg-white/3 open:bg-tac06-acc/10 open:shadow-[inset_0_1px_0_oklch(1_0_0/0.06)] open:ring-tac06-acc/30 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-450 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:transition-none motion-reduce:before:transition-none motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-[72px] cursor-pointer list-none items-center gap-4 rounded-2xl px-4 py-3 outline-none focus-visible:ring-2 focus-visible:ring-tac06-acc sm:px-5 [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-white/6 text-tac06-mut ring-1 ring-white/10 transition-colors duration-300 group-open:bg-linear-to-br group-open:from-tac06-acc group-open:to-tac06-acc-strong group-open:text-white group-open:ring-white/20">
              <svg viewBox="0 0 24 24" width="20" height="20"><rect x="3" y="5.5" width="18" height="13" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M3 10h18M7 15h4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[15.5px] font-semibold transition-colors group-open:text-tac06-acc-soft">Billing</span>
              <span class="mt-0.5 block text-[13px] text-tac06-mut">Plan, invoices &amp; payment method</span>
            </span>
            <span class="flex-none rounded-full bg-white/6 px-2.5 py-1 font-tac06-mono text-[11.5px] text-tac06-mut ring-1 ring-white/10 max-sm:hidden">Team · annual</span>
            <svg aria-hidden="true" class="flex-none text-tac06-mut transition-[rotate,color] duration-300 group-open:rotate-180 group-open:text-tac06-acc-soft motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[4.75rem] sm:pe-6">
            <p class="text-sm leading-relaxed text-tac06-body">You're on the <strong class="font-semibold text-tac06-ink">Team</strong> plan, billed annually. Next invoice on <strong class="font-semibold text-tac06-ink">Aug 12, 2027</strong> for $432.</p>
            <div class="mt-4 rounded-xl bg-tac06-bg/60 p-4 ring-1 ring-white/8">
              <div class="flex items-baseline justify-between gap-3 text-[13px]"><span class="text-tac06-body">Seats used</span><span class="font-tac06-mono text-tac06-ink">18 / 25</span></div>
              <div aria-hidden="true" class="mt-2 h-1.5 overflow-hidden rounded-full bg-white/8"><div class="h-full w-[72%] rounded-full bg-linear-to-r from-tac06-acc to-tac06-acc2"></div></div>
              <div class="mt-3 flex items-center gap-2.5 text-[13px] text-tac06-body"><span aria-hidden="true" class="rounded bg-white/90 px-1.5 py-px text-[10px] font-extrabold tracking-wide text-[oklch(0.3_0.14_272)]">VISA</span>•••• 4242 <span class="text-tac06-mut">· expires 08/28</span></div>
            </div>
            <div class="mt-4 flex flex-wrap gap-2.5">
              <button type="button" class="inline-flex min-h-11 items-center rounded-xl bg-linear-to-b from-tac06-acc to-tac06-acc-strong px-4 text-[13.5px] font-semibold text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_8px_20px_-8px_var(--color-tac06-acc)] transition-[filter,translate] hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac06-acc-soft motion-reduce:transition-none">Manage billing</button>
              <button type="button" class="inline-flex min-h-11 items-center rounded-xl px-4 text-[13.5px] font-semibold text-tac06-ink ring-1 ring-white/14 transition-colors hover:bg-white/6 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac06-acc-soft">Download invoices</button>
            </div>
          </div>
        </details>

        <details name="tac06-settings" class="group relative rounded-2xl ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 before:absolute before:inset-y-4 before:left-0 before:w-1 before:origin-top before:scale-y-0 before:rounded-r-full before:bg-linear-to-b before:from-tac06-acc before:to-tac06-acc2 before:transition-[scale] before:duration-400 before:ease-[cubic-bezier(0.22,1,0.36,1)] hover:bg-white/3 open:bg-tac06-acc/10 open:shadow-[inset_0_1px_0_oklch(1_0_0/0.06)] open:ring-tac06-acc/30 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-450 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:transition-none motion-reduce:before:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-[72px] cursor-pointer list-none items-center gap-4 rounded-2xl px-4 py-3 outline-none focus-visible:ring-2 focus-visible:ring-tac06-acc sm:px-5 [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-white/6 text-tac06-mut ring-1 ring-white/10 transition-colors duration-300 group-open:bg-linear-to-br group-open:from-tac06-acc group-open:to-tac06-acc-strong group-open:text-white group-open:ring-white/20">
              <svg viewBox="0 0 24 24" width="20" height="20"><circle cx="9" cy="8.5" r="3.2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M3.5 19c.6-3.2 2.8-5 5.5-5s4.9 1.8 5.5 5M15.5 5.6a3.1 3.1 0 0 1 0 5.8M17.5 14.4c1.6.6 2.7 2.2 3 4.6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[15.5px] font-semibold transition-colors group-open:text-tac06-acc-soft">Members</span>
              <span class="mt-0.5 block text-[13px] text-tac06-mut">Invites, roles &amp; permissions</span>
            </span>
            <span class="flex-none rounded-full bg-white/6 px-2.5 py-1 font-tac06-mono text-[11.5px] text-tac06-mut ring-1 ring-white/10 max-sm:hidden">18 people</span>
            <svg aria-hidden="true" class="flex-none text-tac06-mut transition-[rotate,color] duration-300 group-open:rotate-180 group-open:text-tac06-acc-soft motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[4.75rem] sm:pe-6">
            <div class="flex flex-wrap items-center gap-3">
              <div aria-hidden="true" class="flex -space-x-1.5">
                <span class="grid size-9 place-items-center rounded-full bg-linear-to-br from-[oklch(0.78_0.12_40)] to-[oklch(0.65_0.18_5)] text-[11px] font-bold text-white ring-2 ring-tac06-panel">AK</span>
                <span class="grid size-9 place-items-center rounded-full bg-linear-to-br from-[oklch(0.78_0.12_225)] to-[oklch(0.6_0.18_270)] text-[11px] font-bold text-white ring-2 ring-tac06-panel">MR</span>
                <span class="grid size-9 place-items-center rounded-full bg-linear-to-br from-[oklch(0.84_0.12_160)] to-[oklch(0.6_0.1_180)] text-[11px] font-bold text-white ring-2 ring-tac06-panel">JL</span>
                <span class="grid size-9 place-items-center rounded-full bg-tac06-raised text-[11px] font-semibold text-tac06-ink ring-2 ring-tac06-panel">+15</span>
              </div>
              <p class="text-sm text-tac06-body">18 members · <span class="text-tac06-acc-soft">3 pending invites</span></p>
            </div>
            <p class="mt-3 text-sm leading-relaxed text-tac06-body">New members join as <strong class="font-semibold text-tac06-ink">Editor</strong>. Guests can view shared projects only and never count toward your seat limit.</p>
            <div class="mt-4 flex flex-wrap gap-2.5">
              <button type="button" class="inline-flex min-h-11 items-center rounded-xl bg-linear-to-b from-tac06-acc to-tac06-acc-strong px-4 text-[13.5px] font-semibold text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_8px_20px_-8px_var(--color-tac06-acc)] transition-[filter,translate] hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac06-acc-soft motion-reduce:transition-none">Invite people</button>
              <button type="button" class="inline-flex min-h-11 items-center rounded-xl px-4 text-[13.5px] font-semibold text-tac06-ink ring-1 ring-white/14 transition-colors hover:bg-white/6 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac06-acc-soft">Edit roles</button>
            </div>
          </div>
        </details>

        <details name="tac06-settings" class="group relative rounded-2xl ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 before:absolute before:inset-y-4 before:left-0 before:w-1 before:origin-top before:scale-y-0 before:rounded-r-full before:bg-linear-to-b before:from-tac06-acc before:to-tac06-acc2 before:transition-[scale] before:duration-400 before:ease-[cubic-bezier(0.22,1,0.36,1)] hover:bg-white/3 open:bg-tac06-acc/10 open:shadow-[inset_0_1px_0_oklch(1_0_0/0.06)] open:ring-tac06-acc/30 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-450 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:transition-none motion-reduce:before:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-[72px] cursor-pointer list-none items-center gap-4 rounded-2xl px-4 py-3 outline-none focus-visible:ring-2 focus-visible:ring-tac06-acc sm:px-5 [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-white/6 text-tac06-mut ring-1 ring-white/10 transition-colors duration-300 group-open:bg-linear-to-br group-open:from-tac06-acc group-open:to-tac06-acc-strong group-open:text-white group-open:ring-white/20">
              <svg viewBox="0 0 24 24" width="20" height="20"><path d="M12 3.2 19 6v5.6c0 4.3-2.9 7.6-7 9.2-4.1-1.6-7-4.9-7-9.2V6z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="m9 12 2.2 2.2L15.2 10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[15.5px] font-semibold transition-colors group-open:text-tac06-acc-soft">Security</span>
              <span class="mt-0.5 block text-[13px] text-tac06-mut">SSO, two-factor &amp; session policy</span>
            </span>
            <span class="flex-none rounded-full bg-white/6 px-2.5 py-1 font-tac06-mono text-[11.5px] text-tac06-mut ring-1 ring-white/10 max-sm:hidden">SSO on</span>
            <svg aria-hidden="true" class="flex-none text-tac06-mut transition-[rotate,color] duration-300 group-open:rotate-180 group-open:text-tac06-acc-soft motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[4.75rem] sm:pe-6">
            <dl class="divide-y divide-white/8 rounded-xl bg-tac06-bg/60 text-[13.5px] ring-1 ring-white/8">
              <div class="flex items-center justify-between gap-3 px-4 py-3"><dt class="text-tac06-body">SAML single sign-on</dt><dd class="font-medium text-tac06-ok">Okta · enabled</dd></div>
              <div class="flex items-center justify-between gap-3 px-4 py-3"><dt class="text-tac06-body">Two-factor for admins</dt><dd class="font-medium text-tac06-ok">Required</dd></div>
              <div class="flex items-center justify-between gap-3 px-4 py-3"><dt class="text-tac06-body">Idle session timeout</dt><dd class="font-tac06-mono text-tac06-ink">30 days</dd></div>
            </dl>
            <div class="mt-4 flex flex-wrap gap-2.5">
              <button type="button" class="inline-flex min-h-11 items-center rounded-xl bg-linear-to-b from-tac06-acc to-tac06-acc-strong px-4 text-[13.5px] font-semibold text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_8px_20px_-8px_var(--color-tac06-acc)] transition-[filter,translate] hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac06-acc-soft motion-reduce:transition-none">Review policy</button>
            </div>
          </div>
        </details>

        <details name="tac06-settings" class="group relative rounded-2xl ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 before:absolute before:inset-y-4 before:left-0 before:w-1 before:origin-top before:scale-y-0 before:rounded-r-full before:bg-linear-to-b before:from-tac06-acc before:to-tac06-acc2 before:transition-[scale] before:duration-400 before:ease-[cubic-bezier(0.22,1,0.36,1)] hover:bg-white/3 open:bg-tac06-acc/10 open:shadow-[inset_0_1px_0_oklch(1_0_0/0.06)] open:ring-tac06-acc/30 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:transition-discrete details-content:duration-450 details-content:ease-[cubic-bezier(0.22,1,0.36,1)] open:details-content:h-auto open:details-content:opacity-100 motion-reduce:transition-none motion-reduce:before:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-[72px] cursor-pointer list-none items-center gap-4 rounded-2xl px-4 py-3 outline-none focus-visible:ring-2 focus-visible:ring-tac06-acc sm:px-5 [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-white/6 text-tac06-mut ring-1 ring-white/10 transition-colors duration-300 group-open:bg-linear-to-br group-open:from-tac06-acc group-open:to-tac06-acc-strong group-open:text-white group-open:ring-white/20">
              <svg viewBox="0 0 24 24" width="20" height="20"><path d="M6.5 16.5V11a5.5 5.5 0 0 1 11 0v5.5l1.5 1.8H5z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M10 20.5a2.2 2.2 0 0 0 4 0" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[15.5px] font-semibold transition-colors group-open:text-tac06-acc-soft">Notifications</span>
              <span class="mt-0.5 block text-[13px] text-tac06-mut">Email digests &amp; Slack alerts</span>
            </span>
            <span class="flex-none rounded-full bg-white/6 px-2.5 py-1 font-tac06-mono text-[11.5px] text-tac06-mut ring-1 ring-white/10 max-sm:hidden">2 channels</span>
            <svg aria-hidden="true" class="flex-none text-tac06-mut transition-[rotate,color] duration-300 group-open:rotate-180 group-open:text-tac06-acc-soft motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-4 pb-5 sm:ps-[4.75rem] sm:pe-6">
            <p class="text-sm leading-relaxed text-tac06-body">A weekly digest lands every Monday at 09:00 in each member's time zone. Incident alerts post to <span class="rounded-md bg-white/8 px-1.5 py-0.5 font-tac06-mono text-[12.5px] text-tac06-ink">#ops-alerts</span> within 30 seconds.</p>
            <div class="mt-4 flex flex-wrap gap-2.5">
              <button type="button" class="inline-flex min-h-11 items-center rounded-xl bg-linear-to-b from-tac06-acc to-tac06-acc-strong px-4 text-[13.5px] font-semibold text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_8px_20px_-8px_var(--color-tac06-acc)] transition-[filter,translate] hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac06-acc-soft motion-reduce:transition-none">Edit channels</button>
              <button type="button" class="inline-flex min-h-11 items-center rounded-xl px-4 text-[13.5px] font-semibold text-tac06-ink ring-1 ring-white/14 transition-colors hover:bg-white/6 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac06-acc-soft">Send test alert</button>
            </div>
          </div>
        </details>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 text-center font-tac06-mono text-[11.5px] text-tac06-mut ring-1 ring-white/10">name="tac06-settings" · open:before:scale-y-100 · details-content:h-auto</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac06-bg: #0d0a18;
  --color-tac06-bg: oklch(0.155 0.03 292);
  --color-tac06-glow: #341a6273;
  --color-tac06-glow: oklch(0.3 0.12 295 / 0.45);
  --color-tac06-glow2: #4a1a4a4d;
  --color-tac06-glow2: oklch(0.3 0.11 335 / 0.3);
  --color-tac06-panel: #171426;
  --color-tac06-panel: oklch(0.205 0.035 292);
  --color-tac06-raised: #2c2843;
  --color-tac06-raised: oklch(0.29 0.045 292);
  --color-tac06-ink: #f3f2fa;
  --color-tac06-ink: oklch(0.965 0.01 292);
  --color-tac06-body: #cecbe0;
  --color-tac06-body: oklch(0.855 0.025 292);
  --color-tac06-mut: #b1aec6;
  --color-tac06-mut: oklch(0.76 0.035 292);
  --color-tac06-acc: #a883ff;
  --color-tac06-acc: oklch(0.7 0.18 295);
  --color-tac06-acc-strong: #8047e1;
  --color-tac06-acc-strong: oklch(0.55 0.22 295);
  --color-tac06-acc-soft: #d1c3ff;
  --color-tac06-acc-soft: oklch(0.85 0.09 295);
  --color-tac06-acc2: #e773d1;
  --color-tac06-acc2: oklch(0.72 0.18 335);
  --color-tac06-ok: #56d298;
  --color-tac06-ok: oklch(0.78 0.14 160);
  --font-tac06-sans: 'Sora', system-ui, sans-serif;
  --font-tac06-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tac06-panel: 0 1px 0 oklch(1 0 0 / 0.06) inset, 0 30px 80px -30px oklch(0.05 0.05 292 / 0.9);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-06 {
  width: 100%;
  min-height: 100svh;
}
```

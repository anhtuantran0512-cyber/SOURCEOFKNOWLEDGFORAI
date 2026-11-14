---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/bootstrap-5-style-vertical-nav-pills-in-tailwind-css/"
title: "Bootstrap 5 Style Vertical Nav Pills in Tailwind CSS"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "Bootstrap 5's vertical nav-pills &mdash; <button role=\"tab\">, aria-controls, focusable tab-panes &mdash; rebuilt as a Tailwind account hub with Home,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bootstrap 5 Style Vertical Nav Pills in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/bootstrap-5-style-vertical-nav-pills-in-tailwind-css/

Bootstrap 5's vertical nav-pills &mdash; <button role="tab">, aria-controls, focusable tab-panes &mdash; rebuilt as a Tailwind account hub with Home, Profile, Messages, Settings and a built-in Bootstrap&rarr;Tailwind class map. The active pill is drawn by aria-selected:, panes animate with data-[state=active]:, and a 25-line script replaces bootstrap.bundle.js by writing attributes only.
## HTML
```html
<section class="tvt-06 w-full min-h-svh grid place-items-center bg-tvt06-bg bg-[radial-gradient(75%_55%_at_50%_0%,var(--color-tvt06-glow),transparent_72%)] px-4 py-14 font-tvt06-sans text-tvt06-ink antialiased sm:px-6" aria-label="Bootstrap 5 style vertical nav pills in Tailwind CSS demo">
  <div class="grid w-full max-w-[56rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tvt06-card px-3 py-1.5 font-tvt06-mono text-[11.5px] ring-1 ring-tvt06-line"><span class="font-semibold text-tvt06-bs">Bootstrap 5.3</span><span aria-hidden="true" class="text-tvt06-mut">&rarr;</span><span class="font-semibold text-tvt06-acc-ink">Tailwind v4</span></p>
      <h2 class="text-[clamp(28px,4.4vw,42px)] leading-[1.05] font-extrabold tracking-[-0.035em] text-balance">Vertical nav pills, <span class="bg-linear-to-r from-tvt06-hl to-tvt06-hl2 bg-clip-text pe-1 text-transparent">without Bootstrap</span></h2>
      <p class="max-w-[50ch] text-[15px] leading-relaxed text-tvt06-mut text-pretty">The exact <code class="font-tvt06-mono text-[13px] text-tvt06-ink">nav-pills</code> / <code class="font-tvt06-mono text-[13px] text-tvt06-ink">tab-pane</code> semantics &mdash; buttons, <code class="font-tvt06-mono text-[13px] text-tvt06-ink">aria-controls</code>, focusable panes &mdash; styled by <code class="font-tvt06-mono text-[13px] text-tvt06-ink">aria-selected:</code> instead of <code class="font-tvt06-mono text-[13px] text-tvt06-ink">.active</code>.</p>
    </header>

    <div id="tvt-06-account" class="@container w-full overflow-hidden rounded-[20px] bg-tvt06-card shadow-tvt06-card ring-1 ring-tvt06-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
      <div class="flex items-center gap-3 border-b border-tvt06-line px-5 py-3.5">
        <span aria-hidden="true" class="flex gap-1.5"><span class="size-3 rounded-full bg-[oklch(0.7_0.18_25)]"></span><span class="size-3 rounded-full bg-[oklch(0.82_0.15_85)]"></span><span class="size-3 rounded-full bg-[oklch(0.75_0.17_150)]"></span></span>
        <p class="flex-1 truncate text-center font-tvt06-mono text-[12px] text-tvt06-mut">app.lumen.io/account</p>
        <span aria-hidden="true" class="w-[46px]"></span>
      </div>
      <div class="flex items-start gap-6 p-4 sm:p-6 @max-[38rem]:flex-col @max-[38rem]:gap-5">
        <div class="w-[13.5rem] shrink-0 @max-[38rem]:w-full">
          <div role="tablist" aria-orientation="vertical" aria-label="Account" class="flex flex-col gap-1 @max-[38rem]:-mx-1 @max-[38rem]:flex-row @max-[38rem]:overflow-x-auto @max-[38rem]:p-1 @max-[38rem]:[scrollbar-width:none]">

            <button type="button" role="tab" id="tvt-06-tab-home" aria-controls="tvt-06-home" aria-selected="true" data-state="active" class="group/pill flex min-h-11 w-full shrink-0 cursor-pointer items-center gap-3 rounded-[10px] px-3.5 text-start text-[14.5px] font-semibold text-tvt06-mut transition-[color,background-color,box-shadow,translate] duration-200 hover:bg-tvt06-acc/8 hover:text-tvt06-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt06-ring aria-selected:bg-linear-to-br aria-selected:from-tvt06-acc aria-selected:to-tvt06-acc2 aria-selected:text-white aria-selected:shadow-tvt06-pill aria-selected:hover:text-white active:translate-y-px motion-reduce:transition-none @max-[38rem]:w-auto"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0"><path d="M3.5 9 10 3.5 16.5 9v7a1 1 0 0 1-1 1h-3.5v-5h-4v5H4.5a1 1 0 0 1-1-1Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg><span class="flex-1 whitespace-nowrap">Home</span></button>

            <button type="button" role="tab" id="tvt-06-tab-profile" aria-controls="tvt-06-profile" aria-selected="false" data-state="inactive" tabindex="-1" class="group/pill flex min-h-11 w-full shrink-0 cursor-pointer items-center gap-3 rounded-[10px] px-3.5 text-start text-[14.5px] font-semibold text-tvt06-mut transition-[color,background-color,box-shadow,translate] duration-200 hover:bg-tvt06-acc/8 hover:text-tvt06-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt06-ring aria-selected:bg-linear-to-br aria-selected:from-tvt06-acc aria-selected:to-tvt06-acc2 aria-selected:text-white aria-selected:shadow-tvt06-pill aria-selected:hover:text-white active:translate-y-px motion-reduce:transition-none @max-[38rem]:w-auto"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="7" r="3.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3.8 16.5a6.4 6.4 0 0 1 12.4 0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span class="flex-1 whitespace-nowrap">Profile</span></button>

            <button type="button" role="tab" id="tvt-06-tab-messages" aria-controls="tvt-06-messages" aria-selected="false" data-state="inactive" tabindex="-1" class="group/pill flex min-h-11 w-full shrink-0 cursor-pointer items-center gap-3 rounded-[10px] px-3.5 text-start text-[14.5px] font-semibold text-tvt06-mut transition-[color,background-color,box-shadow,translate] duration-200 hover:bg-tvt06-acc/8 hover:text-tvt06-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt06-ring aria-selected:bg-linear-to-br aria-selected:from-tvt06-acc aria-selected:to-tvt06-acc2 aria-selected:text-white aria-selected:shadow-tvt06-pill aria-selected:hover:text-white active:translate-y-px motion-reduce:transition-none @max-[38rem]:w-auto"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0"><path d="M3.5 5.5a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-3.5 3v-3h0a2 2 0 0 1-2-2Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg><span class="flex-1 whitespace-nowrap">Messages</span><span class="rounded-full bg-tvt06-acc/12 px-2 py-0.5 text-[11px] font-bold text-tvt06-acc-ink tabular-nums group-aria-selected/pill:bg-white/22 group-aria-selected/pill:text-white">3</span></button>

            <button type="button" role="tab" id="tvt-06-tab-settings" aria-controls="tvt-06-settings" aria-selected="false" data-state="inactive" tabindex="-1" class="group/pill flex min-h-11 w-full shrink-0 cursor-pointer items-center gap-3 rounded-[10px] px-3.5 text-start text-[14.5px] font-semibold text-tvt06-mut transition-[color,background-color,box-shadow,translate] duration-200 hover:bg-tvt06-acc/8 hover:text-tvt06-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt06-ring aria-selected:bg-linear-to-br aria-selected:from-tvt06-acc aria-selected:to-tvt06-acc2 aria-selected:text-white aria-selected:shadow-tvt06-pill aria-selected:hover:text-white active:translate-y-px motion-reduce:transition-none @max-[38rem]:w-auto"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="2.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 2.5v2M10 15.5v2M2.5 10h2M15.5 10h2M4.7 4.7l1.4 1.4M13.9 13.9l1.4 1.4M4.7 15.3l1.4-1.4M13.9 6.1l1.4-1.4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span class="flex-1 whitespace-nowrap">Settings</span></button>
            <span aria-hidden="true" class="mx-3 my-2 h-px bg-tvt06-line @max-[38rem]:hidden"></span>

            <button type="button" role="tab" id="tvt-06-tab-map" aria-controls="tvt-06-map" aria-selected="false" data-state="inactive" tabindex="-1" class="group/pill flex min-h-11 w-full shrink-0 cursor-pointer items-center gap-3 rounded-[10px] px-3.5 text-start text-[14.5px] font-semibold text-tvt06-mut transition-[color,background-color,box-shadow,translate] duration-200 hover:bg-tvt06-acc/8 hover:text-tvt06-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt06-ring aria-selected:bg-linear-to-br aria-selected:from-tvt06-acc aria-selected:to-tvt06-acc2 aria-selected:text-white aria-selected:shadow-tvt06-pill aria-selected:hover:text-white active:translate-y-px motion-reduce:transition-none @max-[38rem]:w-auto"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" focusable="false" class="shrink-0"><path d="M7 3.5 3.5 5v11.5L7 15l6 1.5 3.5-1.5V3.5L13 5 7 3.5ZM7 3.5V15M13 5v11.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg><span class="flex-1 whitespace-nowrap">Class map</span><span class="rounded-md bg-tvt06-bs/12 px-1.5 py-0.5 font-tvt06-mono text-[10px] font-semibold text-tvt06-bs group-aria-selected/pill:bg-white/22 group-aria-selected/pill:text-white">BS5</span></button>
          </div>
        </div>

        <div class="min-w-0 flex-1 border-s border-tvt06-line ps-6 @max-[38rem]:border-s-0 @max-[38rem]:border-t @max-[38rem]:ps-0 @max-[38rem]:pt-5 min-h-[21rem] @max-[38rem]:min-h-0">

          <div role="tabpanel" id="tvt-06-home" aria-labelledby="tvt-06-tab-home" tabindex="0" data-state="active" class="rounded-xl outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt06-ring data-[state=active]:animate-tvt06-in motion-reduce:animate-none">
            <h3 class="text-[clamp(20px,2.4vw,24px)] font-bold tracking-[-0.025em]">Good morning, Riley</h3><p class="mt-1.5 text-[14.5px] text-tvt06-mut text-pretty">Here is what changed since Tuesday.</p>
            <dl class="mt-5 grid grid-cols-3 gap-2.5 sm:gap-3">
              <div class="rounded-xl bg-tvt06-soft p-3 sm:p-4"><dt class="text-[12px] font-medium text-tvt06-mut">Orders</dt><dd class="mt-1 text-[20px] font-extrabold tracking-[-0.03em] tabular-nums sm:text-[24px]">24</dd></div>
              <div class="rounded-xl bg-tvt06-soft p-3 sm:p-4"><dt class="text-[12px] font-medium text-tvt06-mut">Saved</dt><dd class="mt-1 text-[20px] font-extrabold tracking-[-0.03em] tabular-nums sm:text-[24px]">$312</dd></div>
              <div class="rounded-xl bg-tvt06-soft p-3 sm:p-4"><dt class="text-[12px] font-medium text-tvt06-mut">Credits</dt><dd class="mt-1 text-[20px] font-extrabold tracking-[-0.03em] tabular-nums sm:text-[24px]">1.2k</dd></div>
            </dl>
            <div class="mt-4 rounded-xl p-4 ring-1 ring-tvt06-line">
              <p class="flex justify-between text-[13px] font-semibold"><span>Finish setting up your account</span><span class="text-tvt06-mut tabular-nums">3 / 4</span></p>
              <div class="mt-2.5 h-2 overflow-hidden rounded-full bg-tvt06-line"><div class="h-full w-3/4 rounded-full bg-linear-to-r from-tvt06-acc to-tvt06-acc2"></div></div>
              <p class="mt-2.5 text-[12.5px] text-tvt06-mut">Next: verify your phone number for two-factor sign-in.</p>
            </div>
          </div>

          <div role="tabpanel" id="tvt-06-profile" aria-labelledby="tvt-06-tab-profile" tabindex="0" data-state="inactive" hidden class="rounded-xl outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt06-ring data-[state=active]:animate-tvt06-in motion-reduce:animate-none">
            <div class="flex items-center gap-4"><span aria-hidden="true" class="grid size-14 place-items-center rounded-2xl bg-linear-to-br from-[oklch(0.72_0.16_40)] to-[oklch(0.6_0.22_350)] text-[18px] font-bold text-white">RB</span><div><h3 class="text-[clamp(20px,2.4vw,24px)] font-bold tracking-[-0.025em]">Riley Brooks</h3><p class="mt-1.5 text-[14.5px] text-tvt06-mut text-pretty">Product designer · Portland, OR</p></div></div>
            <dl class="mt-5 divide-y divide-tvt06-line rounded-xl ring-1 ring-tvt06-line">
              <div class="flex justify-between gap-4 px-4 py-3 text-[14px]"><dt class="text-tvt06-mut">Email</dt><dd class="truncate font-medium">[email protected]</dd></div>
              <div class="flex justify-between gap-4 px-4 py-3 text-[14px]"><dt class="text-tvt06-mut">Plan</dt><dd class="font-medium">Pro · annual</dd></div>
              <div class="flex justify-between gap-4 px-4 py-3 text-[14px]"><dt class="text-tvt06-mut">Member since</dt><dd class="font-medium">March 2023</dd></div>
            </dl>
            <p class="mt-4 rounded-lg border border-dashed border-tvt06-acc/40 px-3 py-2 font-tvt06-mono text-[11.5px] text-tvt06-acc-ink">role="tabpanel" tabindex="0" &mdash; scrollable panes must be focusable</p>
          </div>

          <div role="tabpanel" id="tvt-06-messages" aria-labelledby="tvt-06-tab-messages" tabindex="0" data-state="inactive" hidden class="rounded-xl outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt06-ring data-[state=active]:animate-tvt06-in motion-reduce:animate-none">
            <h3 class="text-[clamp(20px,2.4vw,24px)] font-bold tracking-[-0.025em]">Messages</h3><p class="mt-1.5 text-[14.5px] text-tvt06-mut text-pretty">3 unread · newest first</p>
            <ul class="mt-5 grid gap-2">
              <li class="flex gap-3 rounded-xl bg-tvt06-soft p-3.5"><span aria-hidden="true" class="mt-1.5 size-2 shrink-0 rounded-full bg-tvt06-acc"></span><div class="min-w-0"><p class="flex justify-between gap-3 text-[14px]"><b class="truncate font-semibold">Order #4021 shipped</b><span class="shrink-0 text-[12px] text-tvt06-mut">9:41</span></p><p class="truncate text-[13px] text-tvt06-mut">Arriving Thursday by 8pm via UPS.</p></div></li>
              <li class="flex gap-3 rounded-xl bg-tvt06-soft p-3.5"><span aria-hidden="true" class="mt-1.5 size-2 shrink-0 rounded-full bg-tvt06-acc"></span><div class="min-w-0"><p class="flex justify-between gap-3 text-[14px]"><b class="truncate font-semibold">Dana from Support</b><span class="shrink-0 text-[12px] text-tvt06-mut">Mon</span></p><p class="truncate text-[13px] text-tvt06-mut">Your refund of $48.00 has been processed.</p></div></li>
              <li class="flex gap-3 rounded-xl p-3.5 ring-1 ring-tvt06-line"><span aria-hidden="true" class="mt-1.5 size-2 shrink-0 rounded-full bg-tvt06-line"></span><div class="min-w-0"><p class="flex justify-between gap-3 text-[14px]"><b class="truncate font-semibold">Weekly digest</b><span class="shrink-0 text-[12px] text-tvt06-mut">Oct 19</span></p><p class="truncate text-[13px] text-tvt06-mut">Five new templates and a price drop on Pro.</p></div></li>
            </ul>
          </div>

          <div role="tabpanel" id="tvt-06-settings" aria-labelledby="tvt-06-tab-settings" tabindex="0" data-state="inactive" hidden class="rounded-xl outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt06-ring data-[state=active]:animate-tvt06-in motion-reduce:animate-none">
            <h3 class="text-[clamp(20px,2.4vw,24px)] font-bold tracking-[-0.025em]">Settings</h3><p class="mt-1.5 text-[14.5px] text-tvt06-mut text-pretty">Switches are <code class="font-tvt06-mono text-[12.5px]">role="switch"</code> buttons styled by <code class="font-tvt06-mono text-[12.5px]">aria-checked:</code>.</p>
            <ul class="mt-5 divide-y divide-tvt06-line rounded-xl ring-1 ring-tvt06-line">
              <li class="flex items-center gap-4 px-4 py-3.5"><div class="min-w-0 flex-1"><p class="text-[14px] font-semibold">Email digests</p><p class="text-[12.5px] text-tvt06-mut">A weekly summary every Monday</p></div><button type="button" role="switch" aria-checked="true" aria-label="Email digests" data-switch class="group/sw relative inline-flex h-7 w-12 shrink-0 cursor-pointer items-center rounded-full bg-tvt06-line p-0.5 transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt06-ring aria-checked:bg-tvt06-acc motion-reduce:transition-none before:absolute before:-inset-2 before:content-['']"><span class="size-6 rounded-full bg-white shadow-[0_1px_3px_oklch(0.2_0.05_290/0.35)] transition-transform duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] group-aria-checked/sw:translate-x-5 motion-reduce:transition-none"></span></button></li>
              <li class="flex items-center gap-4 px-4 py-3.5"><div class="min-w-0 flex-1"><p class="text-[14px] font-semibold">Two-factor sign-in</p><p class="text-[12.5px] text-tvt06-mut">Require a code on new devices</p></div><button type="button" role="switch" aria-checked="true" aria-label="Two-factor sign-in" data-switch class="group/sw relative inline-flex h-7 w-12 shrink-0 cursor-pointer items-center rounded-full bg-tvt06-line p-0.5 transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt06-ring aria-checked:bg-tvt06-acc motion-reduce:transition-none before:absolute before:-inset-2 before:content-['']"><span class="size-6 rounded-full bg-white shadow-[0_1px_3px_oklch(0.2_0.05_290/0.35)] transition-transform duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] group-aria-checked/sw:translate-x-5 motion-reduce:transition-none"></span></button></li>
              <li class="flex items-center gap-4 px-4 py-3.5"><div class="min-w-0 flex-1"><p class="text-[14px] font-semibold">Public profile</p><p class="text-[12.5px] text-tvt06-mut">Let anyone with the link view it</p></div><button type="button" role="switch" aria-checked="false" aria-label="Public profile" data-switch class="group/sw relative inline-flex h-7 w-12 shrink-0 cursor-pointer items-center rounded-full bg-tvt06-line p-0.5 transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt06-ring aria-checked:bg-tvt06-acc motion-reduce:transition-none before:absolute before:-inset-2 before:content-['']"><span class="size-6 rounded-full bg-white shadow-[0_1px_3px_oklch(0.2_0.05_290/0.35)] transition-transform duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] group-aria-checked/sw:translate-x-5 motion-reduce:transition-none"></span></button></li>
            </ul>
          </div>

          <div role="tabpanel" id="tvt-06-map" aria-labelledby="tvt-06-tab-map" tabindex="0" data-state="inactive" hidden class="rounded-xl outline-none focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tvt06-ring data-[state=active]:animate-tvt06-in motion-reduce:animate-none">
            <h3 class="text-[clamp(20px,2.4vw,24px)] font-bold tracking-[-0.025em]">Bootstrap &rarr; Tailwind class map</h3><p class="mt-1.5 text-[14.5px] text-tvt06-mut text-pretty">Same DOM, same ARIA &mdash; only the styling hooks change.</p>
            <div class="mt-4 overflow-x-auto rounded-xl ring-1 ring-tvt06-line">
              <table class="w-full min-w-[30rem] text-start">
                <thead class="bg-tvt06-soft text-[11.5px] font-semibold tracking-[0.08em] text-tvt06-mut uppercase"><tr><th scope="col" class="px-3.5 py-2.5 text-start">Bootstrap 5</th><th scope="col" class="px-3.5 py-2.5 text-start">Tailwind v4</th></tr></thead>
                <tbody>
                  <tr class="border-t border-tvt06-line"><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-bs">.nav.flex-column.nav-pills</td><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-acc-ink">flex flex-col gap-1</td></tr>
                  <tr class="border-t border-tvt06-line"><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-bs">.nav-link.active</td><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-acc-ink">aria-selected:bg-linear-to-br …</td></tr>
                  <tr class="border-t border-tvt06-line"><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-bs">.tab-pane.fade.show.active</td><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-acc-ink">hidden + data-[state=active]:</td></tr>
                  <tr class="border-t border-tvt06-line"><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-bs">.d-flex.align-items-start .me-3</td><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-acc-ink">flex items-start gap-6</td></tr>
                  <tr class="border-t border-tvt06-line"><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-bs">--bs-nav-pills-link-active-bg</td><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-acc-ink">--color-tvt06-acc</td></tr>
                  <tr class="border-t border-tvt06-line"><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-bs">data-bs-toggle="pill" + bundle.js</td><td class="px-3.5 py-2.5 align-top font-tvt06-mono text-[12px] text-tvt06-acc-ink">~25-line IIFE (attributes only)</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt06-card px-3.5 py-2 text-center font-tvt06-mono text-[11.5px] text-tvt06-mut ring-1 ring-tvt06-line">role="tab" · aria-selected: · data-[state]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt06-bg: #f4f3fc;
  --color-tvt06-bg: oklch(0.967 0.012 290);
  --color-tvt06-glow: #d1c9ffa6;
  --color-tvt06-glow: oklch(0.86 0.09 292 / 0.65);
  --color-tvt06-card: #fefeff;
  --color-tvt06-card: oklch(0.997 0.003 290);
  --color-tvt06-soft: #f5f4fe;
  --color-tvt06-soft: oklch(0.97 0.014 290);
  --color-tvt06-ink: #1a172c;
  --color-tvt06-ink: oklch(0.22 0.04 290);
  --color-tvt06-mut: #5d5b70;
  --color-tvt06-mut: oklch(0.48 0.035 290);
  --color-tvt06-line: #e1dfee;
  --color-tvt06-line: oklch(0.91 0.02 290);
  --color-tvt06-acc: #6913eb;
  --color-tvt06-acc: oklch(0.49 0.27 289);
  --color-tvt06-acc2: #a522d2;
  --color-tvt06-acc2: oklch(0.55 0.25 315);
  --color-tvt06-acc-ink: #601dd0;
  --color-tvt06-acc-ink: oklch(0.46 0.24 290);
  --color-tvt06-hl: #6913eb;
  --color-tvt06-hl: oklch(0.49 0.27 289);
  --color-tvt06-hl2: #b431cf;
  --color-tvt06-hl2: oklch(0.58 0.24 320);
  --color-tvt06-ring: #7033ea;
  --color-tvt06-ring: oklch(0.52 0.25 290);
  --color-tvt06-bs: #6e3ead;
  --color-tvt06-bs: oklch(0.48 0.17 300);
  --font-tvt06-sans: 'Figtree', system-ui, sans-serif;
  --font-tvt06-mono: 'Fira Code', ui-monospace, monospace;
  --shadow-tvt06-card: 0 1px 2px oklch(0.3 0.1 290 / 0.06), 0 30px 70px -30px oklch(0.38 0.2 290 / 0.4);
  --shadow-tvt06-pill: 0 10px 22px -10px oklch(0.5 0.27 295 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.25);
  --animate-tvt06-in: tvt06-in 0.36s cubic-bezier(0.16, 1, 0.3, 1);

  @keyframes tvt06-in {
    from {
      opacity: 0;
      translate: 0 8px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-06 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-06:not([data-theme="light"]) {
    --color-tvt06-bg: #0e0b1c;
    --color-tvt06-bg: oklch(0.165 0.035 290);
    --color-tvt06-glow: #371e6e80;
    --color-tvt06-glow: oklch(0.32 0.13 292 / 0.5);
    --color-tvt06-card: #171428;
    --color-tvt06-card: oklch(0.205 0.04 290);
    --color-tvt06-soft: #1e1a32;
    --color-tvt06-soft: oklch(0.235 0.045 290);
    --color-tvt06-ink: #f1f1fa;
    --color-tvt06-ink: oklch(0.96 0.012 290);
    --color-tvt06-mut: #b0aec6;
    --color-tvt06-mut: oklch(0.76 0.035 290);
    --color-tvt06-line: #322e4d;
    --color-tvt06-line: oklch(0.32 0.055 290);
    --color-tvt06-acc: #6f2ef0;
    --color-tvt06-acc: oklch(0.52 0.26 289);
    --color-tvt06-acc2: #a32ace;
    --color-tvt06-acc2: oklch(0.55 0.24 315);
    --color-tvt06-acc-ink: #c8b7ff;
    --color-tvt06-acc-ink: oklch(0.82 0.12 295);
    --color-tvt06-hl: #bcb2ff;
    --color-tvt06-hl: oklch(0.8 0.13 290);
    --color-tvt06-hl2: #f09be8;
    --color-tvt06-hl2: oklch(0.8 0.14 330);
    --color-tvt06-ring: #bda7ff;
    --color-tvt06-ring: oklch(0.78 0.15 295);
    --color-tvt06-bs: #ceacf7;
    --color-tvt06-bs: oklch(0.8 0.11 305);
  }
}

.tvt-06[data-theme="dark"] {
  --color-tvt06-bg: #0e0b1c;
  --color-tvt06-bg: oklch(0.165 0.035 290);
  --color-tvt06-glow: #371e6e80;
  --color-tvt06-glow: oklch(0.32 0.13 292 / 0.5);
  --color-tvt06-card: #171428;
  --color-tvt06-card: oklch(0.205 0.04 290);
  --color-tvt06-soft: #1e1a32;
  --color-tvt06-soft: oklch(0.235 0.045 290);
  --color-tvt06-ink: #f1f1fa;
  --color-tvt06-ink: oklch(0.96 0.012 290);
  --color-tvt06-mut: #b0aec6;
  --color-tvt06-mut: oklch(0.76 0.035 290);
  --color-tvt06-line: #322e4d;
  --color-tvt06-line: oklch(0.32 0.055 290);
  --color-tvt06-acc: #6f2ef0;
  --color-tvt06-acc: oklch(0.52 0.26 289);
  --color-tvt06-acc2: #a32ace;
  --color-tvt06-acc2: oklch(0.55 0.24 315);
  --color-tvt06-acc-ink: #c8b7ff;
  --color-tvt06-acc-ink: oklch(0.82 0.12 295);
  --color-tvt06-hl: #bcb2ff;
  --color-tvt06-hl: oklch(0.8 0.13 290);
  --color-tvt06-hl2: #f09be8;
  --color-tvt06-hl2: oklch(0.8 0.14 330);
  --color-tvt06-ring: #bda7ff;
  --color-tvt06-ring: oklch(0.78 0.15 295);
  --color-tvt06-bs: #ceacf7;
  --color-tvt06-bs: oklch(0.8 0.11 305);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tvt-06-account');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const list = root.querySelector('[role="tablist"]');
  const tabs = [...list.querySelectorAll('[role="tab"]')];
  const show = (tab) => {
    tabs.forEach((t) => {
      const on = t === tab;
      const pane = document.getElementById(t.getAttribute('aria-controls'));
      t.setAttribute('aria-selected', String(on));
      t.dataset.state = on ? 'active' : 'inactive';
      if (on) t.removeAttribute('tabindex'); else t.tabIndex = -1;
      if (pane) { pane.hidden = !on; pane.dataset.state = t.dataset.state; }
    });
    tab.scrollIntoView({ block: 'nearest', inline: 'nearest' });
  };
  list.addEventListener('click', (e) => { const t = e.target.closest('[role="tab"]'); if (t) show(t); });
  list.addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    const to = { ArrowDown: i + 1, ArrowRight: i + 1, ArrowUp: i - 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
    if (to === undefined || i < 0) return;
    e.preventDefault();
    const next = tabs[(to + tabs.length) % tabs.length];
    next.focus(); show(next);
  });
  root.querySelectorAll('[data-switch]').forEach((s) => s.addEventListener('click', () => {
    s.setAttribute('aria-checked', String(s.getAttribute('aria-checked') !== 'true'));
  }));
})();
```

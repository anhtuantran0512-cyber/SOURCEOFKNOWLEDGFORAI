---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-settings-page-layout-with-vertical-tabs-saas-dashboard/"
title: "Tailwind Settings Page Layout with Vertical Tabs (SaaS Dashboard)"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A complete SaaS account-settings screen &mdash; Profile, Notifications, General, Members and API keys &mdash; switched by radios and styled with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Settings Page Layout with Vertical Tabs (SaaS Dashboard)
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-settings-page-layout-with-vertical-tabs-saas-dashboard/

A complete SaaS account-settings screen &mdash; Profile, Notifications, General, Members and API keys &mdash; switched by radios and styled with has-checked:, with real checkbox toggles and zero JavaScript. Its party trick is a save bar that knows when something changed: :checked:not(:default) inside a group-has-[…] variant slides it in the moment any switch leaves its saved state, and out again when you flip it back.
## HTML
```html
<section class="tvt-09 w-full min-h-svh grid place-items-center bg-tvt09-bg bg-[radial-gradient(80%_55%_at_50%_0%,var(--color-tvt09-glow),transparent_70%)] px-4 py-14 font-tvt09-sans text-tvt09-ink antialiased sm:px-6" aria-label="Tailwind settings page with vertical tabs demo">
  <div class="grid w-full max-w-[64rem] justify-items-center gap-7">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tvt09-card px-3 py-1.5 font-tvt09-mono text-[11.5px] text-tvt09-acc-ink ring-1 ring-tvt09-line"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt09-acc shadow-[0_0_0_3px] shadow-tvt09-acc/25"></span>has-checked: · :default · sticky save bar</p>
      <h2 class="text-[clamp(28px,4.4vw,42px)] leading-[1.05] font-bold tracking-[-0.04em] text-balance">Settings that <span class="bg-linear-to-r from-tvt09-hl to-tvt09-hl2 bg-clip-text pe-1 text-transparent">know they've changed</span></h2>
      <p class="max-w-[50ch] text-[15px] leading-relaxed text-tvt09-mut text-pretty">Five sections, real switches, zero JavaScript. Flip any toggle away from its saved value and the save bar slides in; flip it back and it leaves.</p>
    </header>

    <div class="@container w-full starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
      <div class="group/app grid h-[38rem] grid-cols-[15.5rem_minmax(0,1fr)] overflow-hidden rounded-[22px] bg-tvt09-card shadow-tvt09-card ring-1 ring-tvt09-line @max-[46rem]:h-auto @max-[46rem]:grid-cols-1">
        <nav aria-label="Settings sections" class="flex flex-col border-e border-tvt09-line bg-tvt09-rail px-3 pt-4 pb-3 @max-[46rem]:border-e-0 @max-[46rem]:border-b @max-[46rem]:px-3 @max-[46rem]:pt-3">
          <div class="flex items-center gap-2.5 px-2 pb-4 @max-[46rem]:pb-3">
            <span aria-hidden="true" class="grid size-8 place-items-center rounded-[10px] bg-linear-to-br from-tvt09-acc to-tvt09-acc2 text-white shadow-tvt09-pill"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="m10 3 6.5 13h-13Z M7 12h6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></span>
            <span class="leading-tight"><span class="block text-[14px] font-bold tracking-[-0.01em]">Acme Console</span><span class="block text-[12px] text-tvt09-mut">Pro workspace</span></span>
          </div>
          <div role="radiogroup" aria-label="Settings section" class="flex flex-1 flex-col gap-0.5 @max-[46rem]:-mx-3 @max-[46rem]:flex-row @max-[46rem]:gap-1.5 @max-[46rem]:overflow-x-auto @max-[46rem]:px-3 @max-[46rem]:pb-1 @max-[46rem]:[scrollbar-width:none] @max-[46rem]:mask-r-from-85%">
            <p class="px-3 pt-1 pb-1.5 font-tvt09-mono text-[10.5px] tracking-[0.14em] text-tvt09-mut uppercase @max-[46rem]:hidden">Account</p>

            <label class="group/tab relative flex min-h-11 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-3 text-[14px] font-medium text-tvt09-mut transition-[color,background-color,box-shadow] duration-200 select-none hover:bg-tvt09-ink/[0.05] hover:text-tvt09-ink has-checked:bg-tvt09-tab has-checked:font-semibold has-checked:text-tvt09-ink has-checked:shadow-tvt09-tab has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt09-ring motion-reduce:transition-none @max-[46rem]:min-h-10 @max-[46rem]:rounded-full @max-[46rem]:px-3.5 @max-[46rem]:has-checked:bg-tvt09-acc @max-[46rem]:has-checked:text-white @max-[46rem]:has-checked:shadow-tvt09-pill">
              <input type="radio" name="tvt-09-section" id="tvt-09-t1" class="sr-only" checked>
              <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-lg text-current transition-colors duration-200 group-has-checked/tab:bg-tvt09-acc group-has-checked/tab:text-white group-has-checked/tab:shadow-tvt09-pill @max-[46rem]:hidden"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="M10 10a3.2 3.2 0 1 0 0-6.4 3.2 3.2 0 0 0 0 6.4ZM3.8 16.5c.9-2.8 3.3-4.3 6.2-4.3s5.3 1.5 6.2 4.3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="flex-1 whitespace-nowrap">Profile</span>
            </label>

            <label class="group/tab relative flex min-h-11 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-3 text-[14px] font-medium text-tvt09-mut transition-[color,background-color,box-shadow] duration-200 select-none hover:bg-tvt09-ink/[0.05] hover:text-tvt09-ink has-checked:bg-tvt09-tab has-checked:font-semibold has-checked:text-tvt09-ink has-checked:shadow-tvt09-tab has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt09-ring motion-reduce:transition-none @max-[46rem]:min-h-10 @max-[46rem]:rounded-full @max-[46rem]:px-3.5 @max-[46rem]:has-checked:bg-tvt09-acc @max-[46rem]:has-checked:text-white @max-[46rem]:has-checked:shadow-tvt09-pill">
              <input type="radio" name="tvt-09-section" id="tvt-09-t2" class="sr-only">
              <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-lg text-current transition-colors duration-200 group-has-checked/tab:bg-tvt09-acc group-has-checked/tab:text-white group-has-checked/tab:shadow-tvt09-pill @max-[46rem]:hidden"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="M5 13.5V9a5 5 0 0 1 10 0v4.5l1.5 1.5h-13Zm3.5 2.8a1.6 1.6 0 0 0 3 0" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="flex-1 whitespace-nowrap">Notifications</span><span class="size-2 rounded-full bg-tvt09-acc2 shadow-[0_0_0_3px] shadow-tvt09-acc2/20 @max-[46rem]:hidden" aria-label="New"></span>
            </label>
            <p class="px-3 pt-4 pb-1.5 font-tvt09-mono text-[10.5px] tracking-[0.14em] text-tvt09-mut uppercase @max-[46rem]:hidden">Workspace</p>

            <label class="group/tab relative flex min-h-11 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-3 text-[14px] font-medium text-tvt09-mut transition-[color,background-color,box-shadow] duration-200 select-none hover:bg-tvt09-ink/[0.05] hover:text-tvt09-ink has-checked:bg-tvt09-tab has-checked:font-semibold has-checked:text-tvt09-ink has-checked:shadow-tvt09-tab has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt09-ring motion-reduce:transition-none @max-[46rem]:min-h-10 @max-[46rem]:rounded-full @max-[46rem]:px-3.5 @max-[46rem]:has-checked:bg-tvt09-acc @max-[46rem]:has-checked:text-white @max-[46rem]:has-checked:shadow-tvt09-pill">
              <input type="radio" name="tvt-09-section" id="tvt-09-t3" class="sr-only">
              <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-lg text-current transition-colors duration-200 group-has-checked/tab:bg-tvt09-acc group-has-checked/tab:text-white group-has-checked/tab:shadow-tvt09-pill @max-[46rem]:hidden"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="M3.5 3.5h5v5h-5zM11.5 3.5h5v5h-5zM3.5 11.5h5v5h-5zM11.5 11.5h5v5h-5z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="flex-1 whitespace-nowrap">General</span>
            </label>

            <label class="group/tab relative flex min-h-11 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-3 text-[14px] font-medium text-tvt09-mut transition-[color,background-color,box-shadow] duration-200 select-none hover:bg-tvt09-ink/[0.05] hover:text-tvt09-ink has-checked:bg-tvt09-tab has-checked:font-semibold has-checked:text-tvt09-ink has-checked:shadow-tvt09-tab has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt09-ring motion-reduce:transition-none @max-[46rem]:min-h-10 @max-[46rem]:rounded-full @max-[46rem]:px-3.5 @max-[46rem]:has-checked:bg-tvt09-acc @max-[46rem]:has-checked:text-white @max-[46rem]:has-checked:shadow-tvt09-pill">
              <input type="radio" name="tvt-09-section" id="tvt-09-t4" class="sr-only">
              <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-lg text-current transition-colors duration-200 group-has-checked/tab:bg-tvt09-acc group-has-checked/tab:text-white group-has-checked/tab:shadow-tvt09-pill @max-[46rem]:hidden"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="M7.5 9.5a2.7 2.7 0 1 0 0-5.4 2.7 2.7 0 0 0 0 5.4ZM2.5 16c.6-2.4 2.6-3.8 5-3.8s4.4 1.4 5 3.8M13 4.4a2.6 2.6 0 0 1 0 5M14.5 12.4c1.5.5 2.6 1.7 3 3.6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="flex-1 whitespace-nowrap">Members</span><span class="rounded-full bg-tvt09-ink/[0.07] px-2 py-0.5 font-tvt09-mono text-[10.5px] font-semibold text-tvt09-mut tabular-nums group-has-checked/tab:bg-tvt09-acc/12 group-has-checked/tab:text-tvt09-acc-ink @max-[46rem]:hidden">12</span>
            </label>

            <label class="group/tab relative flex min-h-11 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-3 text-[14px] font-medium text-tvt09-mut transition-[color,background-color,box-shadow] duration-200 select-none hover:bg-tvt09-ink/[0.05] hover:text-tvt09-ink has-checked:bg-tvt09-tab has-checked:font-semibold has-checked:text-tvt09-ink has-checked:shadow-tvt09-tab has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt09-ring motion-reduce:transition-none @max-[46rem]:min-h-10 @max-[46rem]:rounded-full @max-[46rem]:px-3.5 @max-[46rem]:has-checked:bg-tvt09-acc @max-[46rem]:has-checked:text-white @max-[46rem]:has-checked:shadow-tvt09-pill">
              <input type="radio" name="tvt-09-section" id="tvt-09-t5" class="sr-only">
              <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-lg text-current transition-colors duration-200 group-has-checked/tab:bg-tvt09-acc group-has-checked/tab:text-white group-has-checked/tab:shadow-tvt09-pill @max-[46rem]:hidden"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="M12.5 7.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM8.5 10.2 3.5 15.5v1.5h2.5v-1.5h1.5V14h1.5l1.2-1.3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
              <span class="flex-1 whitespace-nowrap">API keys</span>
            </label>
          </div>
          <div class="mt-3 flex items-center gap-2.5 rounded-xl bg-tvt09-card p-2.5 ring-1 ring-tvt09-line @max-[46rem]:hidden">
            <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.72_0.14_200)] to-[oklch(0.55_0.18_262)] text-[11px] font-bold text-white">JE</span>
            <span class="min-w-0 leading-tight"><span class="block truncate text-[13px] font-semibold">Jordan Ellis</span><span class="block truncate text-[11.5px] text-tvt09-mut">[email protected]</span></span>
          </div>
        </nav>

        <div class="relative min-h-0 min-w-0">
          <div class="h-full overflow-y-auto overscroll-contain bg-tvt09-card @max-[46rem]:h-auto @max-[46rem]:min-h-[30rem]">

              <section aria-labelledby="tvt-09-h1" class="hidden pb-24 group-has-[#tvt-09-t1:checked]/app:block group-has-[#tvt-09-t1:checked]/app:animate-tvt09-in motion-reduce:animate-none">
                <header class="border-b border-tvt09-line px-6 pt-6 pb-5 @max-[46rem]:px-4">
                  <p class="font-tvt09-mono text-[11px] tracking-[0.12em] text-tvt09-mut uppercase">Settings / Profile</p>
                  <h3 id="tvt-09-h1" class="mt-1.5 text-[21px] font-bold tracking-[-0.025em]">Profile</h3>
                  <p class="mt-1 text-[13.5px] leading-relaxed text-tvt09-mut text-pretty">How you appear to the 12 people in this workspace.</p>
                </header>
                <div class="flex items-center gap-4 border-b border-tvt09-line/70 px-6 py-4 @max-[46rem]:px-4"><span aria-hidden="true" class="grid size-14 shrink-0 place-items-center rounded-2xl bg-linear-to-br from-[oklch(0.72_0.14_200)] to-[oklch(0.55_0.18_262)] text-[18px] font-bold text-white shadow-tvt09-pill">JE</span><div class="min-w-0"><p class="text-[14px] font-semibold">Avatar</p><p class="text-[12.75px] text-tvt09-mut">PNG or JPG, at least 256 × 256</p></div></div>

                <div class="grid min-h-[4.25rem] grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)] items-center gap-5 border-b border-tvt09-line/70 px-6 py-3 last:border-b-0 @max-[46rem]:grid-cols-1 @max-[46rem]:gap-2 @max-[46rem]:px-4">
                  <div class="min-w-0"><p class="text-[14px] font-semibold">Display name</p><p class="mt-0.5 text-[12.75px] leading-snug text-tvt09-mut">Shown on comments and mentions</p></div>
                  <p class="flex min-h-10 min-w-0 items-center rounded-lg bg-tvt09-card px-3 py-2 text-[13.5px] shadow-tvt09-field ring-1 ring-tvt09-line ">Jordan Ellis</p>
                </div>

                <div class="grid min-h-[4.25rem] grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)] items-center gap-5 border-b border-tvt09-line/70 px-6 py-3 last:border-b-0 @max-[46rem]:grid-cols-1 @max-[46rem]:gap-2 @max-[46rem]:px-4">
                  <div class="min-w-0"><p class="text-[14px] font-semibold">Email</p><p class="mt-0.5 text-[12.75px] leading-snug text-tvt09-mut">Used for sign-in and digests</p></div>
                  <p class="flex min-h-10 min-w-0 items-center rounded-lg bg-tvt09-card px-3 py-2 text-[13.5px] shadow-tvt09-field ring-1 ring-tvt09-line ">[email protected]</p>
                </div>

                <div class="grid min-h-[4.25rem] grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)] items-center gap-5 border-b border-tvt09-line/70 px-6 py-3 last:border-b-0 @max-[46rem]:grid-cols-1 @max-[46rem]:gap-2 @max-[46rem]:px-4">
                  <div class="min-w-0"><p class="text-[14px] font-semibold">Time zone</p><p class="mt-0.5 text-[12.75px] leading-snug text-tvt09-mut">Schedules digests and reminders</p></div>
                  <p class="flex min-h-10 min-w-0 items-center rounded-lg bg-tvt09-card px-3 py-2 text-[13.5px] shadow-tvt09-field ring-1 ring-tvt09-line ">UTC−05:00 · New York</p>
                </div>

                <label class="flex min-h-[4.25rem] cursor-pointer items-center justify-between gap-5 border-b border-tvt09-line/70 px-6 py-3 transition-colors duration-200 last:border-b-0 hover:bg-tvt09-ink/[0.025] motion-reduce:transition-none @max-[46rem]:px-4">
                  <span class="min-w-0"><span class="block text-[14px] font-semibold">Public profile</span><span class="mt-0.5 block text-[12.75px] leading-snug text-tvt09-mut text-pretty">Let members outside your team see your activity</span></span>
                  <input type="checkbox" data-pref class="peer sr-only" checked>
                  <span aria-hidden="true" class="relative h-6 w-11 shrink-0 rounded-full bg-tvt09-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.18)] transition-colors duration-250 peer-checked:bg-linear-to-r peer-checked:from-tvt09-acc peer-checked:to-tvt09-acc2 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tvt09-ring after:absolute after:top-0.5 after:start-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_oklch(0.2_0.03_260/0.35)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none forced-colors:border forced-colors:peer-checked:bg-[Highlight]"></span>
                </label>
              </section>

              <section aria-labelledby="tvt-09-h2" class="hidden pb-24 group-has-[#tvt-09-t2:checked]/app:block group-has-[#tvt-09-t2:checked]/app:animate-tvt09-in motion-reduce:animate-none">
                <header class="border-b border-tvt09-line px-6 pt-6 pb-5 @max-[46rem]:px-4">
                  <p class="font-tvt09-mono text-[11px] tracking-[0.12em] text-tvt09-mut uppercase">Settings / Notifications</p>
                  <h3 id="tvt-09-h2" class="mt-1.5 text-[21px] font-bold tracking-[-0.025em]">Notifications</h3>
                  <p class="mt-1 text-[13.5px] leading-relaxed text-tvt09-mut text-pretty">Every switch is a real checkbox: keyboard, screen readers and forced-colours mode all work.</p>
                </header>
                <div class="flex flex-wrap items-center justify-between gap-3 border-b border-tvt09-line/70 px-6 py-4 @max-[46rem]:px-4"><div><p class="text-[14px] font-semibold">Deliver to</p><p class="mt-0.5 text-[12.75px] text-tvt09-mut">Where alerts are sent first</p></div><div role="radiogroup" aria-label="Delivery channel" class="inline-flex rounded-xl bg-tvt09-sub p-1 ring-1 ring-tvt09-line"><label class="flex min-h-9 cursor-pointer items-center rounded-lg px-3.5 text-[13px] font-medium text-tvt09-mut transition-[background-color,color,box-shadow] duration-200 has-checked:bg-tvt09-tab has-checked:font-semibold has-checked:text-tvt09-ink has-checked:shadow-tvt09-tab has-focus-visible:outline-2 has-focus-visible:outline-tvt09-ring motion-reduce:transition-none"><input type="radio" name="tvt-09-delivery" class="sr-only" checked>Email</label><label class="flex min-h-9 cursor-pointer items-center rounded-lg px-3.5 text-[13px] font-medium text-tvt09-mut transition-[background-color,color,box-shadow] duration-200 has-checked:bg-tvt09-tab has-checked:font-semibold has-checked:text-tvt09-ink has-checked:shadow-tvt09-tab has-focus-visible:outline-2 has-focus-visible:outline-tvt09-ring motion-reduce:transition-none"><input type="radio" name="tvt-09-delivery" class="sr-only">Push</label><label class="flex min-h-9 cursor-pointer items-center rounded-lg px-3.5 text-[13px] font-medium text-tvt09-mut transition-[background-color,color,box-shadow] duration-200 has-checked:bg-tvt09-tab has-checked:font-semibold has-checked:text-tvt09-ink has-checked:shadow-tvt09-tab has-focus-visible:outline-2 has-focus-visible:outline-tvt09-ring motion-reduce:transition-none"><input type="radio" name="tvt-09-delivery" class="sr-only">Both</label></div></div>

                <label class="flex min-h-[4.25rem] cursor-pointer items-center justify-between gap-5 border-b border-tvt09-line/70 px-6 py-3 transition-colors duration-200 last:border-b-0 hover:bg-tvt09-ink/[0.025] motion-reduce:transition-none @max-[46rem]:px-4">
                  <span class="min-w-0"><span class="block text-[14px] font-semibold">Mentions</span><span class="mt-0.5 block text-[12.75px] leading-snug text-tvt09-mut text-pretty">When someone @mentions you or replies to your thread</span></span>
                  <input type="checkbox" data-pref class="peer sr-only" checked>
                  <span aria-hidden="true" class="relative h-6 w-11 shrink-0 rounded-full bg-tvt09-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.18)] transition-colors duration-250 peer-checked:bg-linear-to-r peer-checked:from-tvt09-acc peer-checked:to-tvt09-acc2 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tvt09-ring after:absolute after:top-0.5 after:start-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_oklch(0.2_0.03_260/0.35)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none forced-colors:border forced-colors:peer-checked:bg-[Highlight]"></span>
                </label>

                <label class="flex min-h-[4.25rem] cursor-pointer items-center justify-between gap-5 border-b border-tvt09-line/70 px-6 py-3 transition-colors duration-200 last:border-b-0 hover:bg-tvt09-ink/[0.025] motion-reduce:transition-none @max-[46rem]:px-4">
                  <span class="min-w-0"><span class="block text-[14px] font-semibold">Weekly digest</span><span class="mt-0.5 block text-[12.75px] leading-snug text-tvt09-mut text-pretty">A Monday summary of workspace activity</span></span>
                  <input type="checkbox" data-pref class="peer sr-only" checked>
                  <span aria-hidden="true" class="relative h-6 w-11 shrink-0 rounded-full bg-tvt09-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.18)] transition-colors duration-250 peer-checked:bg-linear-to-r peer-checked:from-tvt09-acc peer-checked:to-tvt09-acc2 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tvt09-ring after:absolute after:top-0.5 after:start-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_oklch(0.2_0.03_260/0.35)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none forced-colors:border forced-colors:peer-checked:bg-[Highlight]"></span>
                </label>

                <label class="flex min-h-[4.25rem] cursor-pointer items-center justify-between gap-5 border-b border-tvt09-line/70 px-6 py-3 transition-colors duration-200 last:border-b-0 hover:bg-tvt09-ink/[0.025] motion-reduce:transition-none @max-[46rem]:px-4">
                  <span class="min-w-0"><span class="block text-[14px] font-semibold">Product updates</span><span class="mt-0.5 block text-[12.75px] leading-snug text-tvt09-mut text-pretty">Monthly changelog and new features</span></span>
                  <input type="checkbox" data-pref class="peer sr-only">
                  <span aria-hidden="true" class="relative h-6 w-11 shrink-0 rounded-full bg-tvt09-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.18)] transition-colors duration-250 peer-checked:bg-linear-to-r peer-checked:from-tvt09-acc peer-checked:to-tvt09-acc2 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tvt09-ring after:absolute after:top-0.5 after:start-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_oklch(0.2_0.03_260/0.35)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none forced-colors:border forced-colors:peer-checked:bg-[Highlight]"></span>
                </label>

                <label class="flex min-h-[4.25rem] cursor-pointer items-center justify-between gap-5 border-b border-tvt09-line/70 px-6 py-3 transition-colors duration-200 last:border-b-0 hover:bg-tvt09-ink/[0.025] motion-reduce:transition-none @max-[46rem]:px-4">
                  <span class="min-w-0"><span class="block text-[14px] font-semibold">Marketing email</span><span class="mt-0.5 block text-[12.75px] leading-snug text-tvt09-mut text-pretty">Occasional launch news and events</span></span>
                  <input type="checkbox" data-pref class="peer sr-only">
                  <span aria-hidden="true" class="relative h-6 w-11 shrink-0 rounded-full bg-tvt09-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.18)] transition-colors duration-250 peer-checked:bg-linear-to-r peer-checked:from-tvt09-acc peer-checked:to-tvt09-acc2 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tvt09-ring after:absolute after:top-0.5 after:start-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_oklch(0.2_0.03_260/0.35)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none forced-colors:border forced-colors:peer-checked:bg-[Highlight]"></span>
                </label>
              </section>

              <section aria-labelledby="tvt-09-h3" class="hidden pb-24 group-has-[#tvt-09-t3:checked]/app:block group-has-[#tvt-09-t3:checked]/app:animate-tvt09-in motion-reduce:animate-none">
                <header class="border-b border-tvt09-line px-6 pt-6 pb-5 @max-[46rem]:px-4">
                  <p class="font-tvt09-mono text-[11px] tracking-[0.12em] text-tvt09-mut uppercase">Settings / General</p>
                  <h3 id="tvt-09-h3" class="mt-1.5 text-[21px] font-bold tracking-[-0.025em]">General</h3>
                  <p class="mt-1 text-[13.5px] leading-relaxed text-tvt09-mut text-pretty">Workspace-wide defaults. Changes apply to every member.</p>
                </header>

                <div class="grid min-h-[4.25rem] grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)] items-center gap-5 border-b border-tvt09-line/70 px-6 py-3 last:border-b-0 @max-[46rem]:grid-cols-1 @max-[46rem]:gap-2 @max-[46rem]:px-4">
                  <div class="min-w-0"><p class="text-[14px] font-semibold">Workspace name</p><p class="mt-0.5 text-[12.75px] leading-snug text-tvt09-mut">Visible in invites and the sidebar</p></div>
                  <p class="flex min-h-10 min-w-0 items-center rounded-lg bg-tvt09-card px-3 py-2 text-[13.5px] shadow-tvt09-field ring-1 ring-tvt09-line ">Acme Inc.</p>
                </div>

                <div class="grid min-h-[4.25rem] grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)] items-center gap-5 border-b border-tvt09-line/70 px-6 py-3 last:border-b-0 @max-[46rem]:grid-cols-1 @max-[46rem]:gap-2 @max-[46rem]:px-4">
                  <div class="min-w-0"><p class="text-[14px] font-semibold">Workspace URL</p><p class="mt-0.5 text-[12.75px] leading-snug text-tvt09-mut">Changing it breaks existing links</p></div>
                  <p class="flex min-h-10 min-w-0 items-center rounded-lg bg-tvt09-card px-3 py-2 text-[13.5px] shadow-tvt09-field ring-1 ring-tvt09-line "><span class="text-tvt09-mut">console.acme.app/</span>acme</p>
                </div>

                <label class="flex min-h-[4.25rem] cursor-pointer items-center justify-between gap-5 border-b border-tvt09-line/70 px-6 py-3 transition-colors duration-200 last:border-b-0 hover:bg-tvt09-ink/[0.025] motion-reduce:transition-none @max-[46rem]:px-4">
                  <span class="min-w-0"><span class="block text-[14px] font-semibold">Require two-factor auth</span><span class="mt-0.5 block text-[12.75px] leading-snug text-tvt09-mut text-pretty">Members must enable 2FA before their next sign-in</span></span>
                  <input type="checkbox" data-pref class="peer sr-only" checked>
                  <span aria-hidden="true" class="relative h-6 w-11 shrink-0 rounded-full bg-tvt09-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.18)] transition-colors duration-250 peer-checked:bg-linear-to-r peer-checked:from-tvt09-acc peer-checked:to-tvt09-acc2 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tvt09-ring after:absolute after:top-0.5 after:start-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_oklch(0.2_0.03_260/0.35)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none forced-colors:border forced-colors:peer-checked:bg-[Highlight]"></span>
                </label>
                <div class="m-6 rounded-2xl p-4 ring-1 ring-tvt09-danger/30 bg-tvt09-danger/[0.05] @max-[46rem]:m-4"><p class="text-[14px] font-semibold text-tvt09-danger">Danger zone</p><p class="mt-1 text-[12.75px] text-tvt09-mut">Deleting a workspace removes every project, key and member. This cannot be undone.</p><span class="mt-3 inline-flex min-h-10 items-center rounded-lg bg-tvt09-card px-3.5 text-[13px] font-semibold text-tvt09-danger ring-1 ring-tvt09-danger/40">Delete workspace…</span></div>
              </section>

              <section aria-labelledby="tvt-09-h4" class="hidden pb-24 group-has-[#tvt-09-t4:checked]/app:block group-has-[#tvt-09-t4:checked]/app:animate-tvt09-in motion-reduce:animate-none">
                <header class="border-b border-tvt09-line px-6 pt-6 pb-5 @max-[46rem]:px-4">
                  <p class="font-tvt09-mono text-[11px] tracking-[0.12em] text-tvt09-mut uppercase">Settings / Members</p>
                  <h3 id="tvt-09-h4" class="mt-1.5 text-[21px] font-bold tracking-[-0.025em]">Members</h3>
                  <p class="mt-1 text-[13.5px] leading-relaxed text-tvt09-mut text-pretty">12 of 15 seats used across three roles.</p>
                </header>
                <div class="border-b border-tvt09-line/70 px-6 py-4 @max-[46rem]:px-4"><p class="flex justify-between text-[12.75px] font-semibold"><span>Seats</span><span class="text-tvt09-mut tabular-nums">12 / 15</span></p><div class="mt-2 h-2 overflow-hidden rounded-full bg-tvt09-off"><div class="h-full w-4/5 rounded-full bg-linear-to-r from-tvt09-acc to-tvt09-acc2"></div></div></div>
                <ul class="divide-y divide-tvt09-line/70 border-b border-tvt09-line/70"><li class="flex items-center gap-3 px-6 py-3 @max-[46rem]:px-4"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.72_0.14_200)] to-[oklch(0.55_0.18_262)] text-[12px] font-bold text-white">JE</span><span class="min-w-0 flex-1"><span class="block truncate text-[14px] font-semibold">Jordan Ellis</span><span class="block truncate text-[12.5px] text-tvt09-mut">[email protected]</span></span><span class="rounded-md bg-tvt09-sub px-2 py-1 text-[11.5px] font-semibold text-tvt09-mut ring-1 ring-tvt09-line">Owner</span></li><li class="flex items-center gap-3 px-6 py-3 @max-[46rem]:px-4"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.72_0.16_30)] to-[oklch(0.58_0.2_355)] text-[12px] font-bold text-white">PN</span><span class="min-w-0 flex-1"><span class="block truncate text-[14px] font-semibold">Priya Nair</span><span class="block truncate text-[12.5px] text-tvt09-mut">[email protected]</span></span><span class="rounded-md bg-tvt09-sub px-2 py-1 text-[11.5px] font-semibold text-tvt09-mut ring-1 ring-tvt09-line">Admin</span></li><li class="flex items-center gap-3 px-6 py-3 @max-[46rem]:px-4"><span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-[oklch(0.76_0.15_150)] to-[oklch(0.56_0.14_190)] text-[12px] font-bold text-white">TO</span><span class="min-w-0 flex-1"><span class="block truncate text-[14px] font-semibold">Tom O’Brien</span><span class="block truncate text-[12.5px] text-tvt09-mut">[email protected]</span></span><span class="rounded-md bg-tvt09-sub px-2 py-1 text-[11.5px] font-semibold text-tvt09-mut ring-1 ring-tvt09-line">Editor</span></li></ul>

                <label class="flex min-h-[4.25rem] cursor-pointer items-center justify-between gap-5 border-b border-tvt09-line/70 px-6 py-3 transition-colors duration-200 last:border-b-0 hover:bg-tvt09-ink/[0.025] motion-reduce:transition-none @max-[46rem]:px-4">
                  <span class="min-w-0"><span class="block text-[14px] font-semibold">Domain capture</span><span class="mt-0.5 block text-[12.75px] leading-snug text-tvt09-mut text-pretty">Anyone with an @acme.com address can join</span></span>
                  <input type="checkbox" data-pref class="peer sr-only" checked>
                  <span aria-hidden="true" class="relative h-6 w-11 shrink-0 rounded-full bg-tvt09-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.18)] transition-colors duration-250 peer-checked:bg-linear-to-r peer-checked:from-tvt09-acc peer-checked:to-tvt09-acc2 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tvt09-ring after:absolute after:top-0.5 after:start-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_oklch(0.2_0.03_260/0.35)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none forced-colors:border forced-colors:peer-checked:bg-[Highlight]"></span>
                </label>

                <label class="flex min-h-[4.25rem] cursor-pointer items-center justify-between gap-5 border-b border-tvt09-line/70 px-6 py-3 transition-colors duration-200 last:border-b-0 hover:bg-tvt09-ink/[0.025] motion-reduce:transition-none @max-[46rem]:px-4">
                  <span class="min-w-0"><span class="block text-[14px] font-semibold">Guest links</span><span class="mt-0.5 block text-[12.75px] leading-snug text-tvt09-mut text-pretty">Share read-only views with people outside Acme</span></span>
                  <input type="checkbox" data-pref class="peer sr-only">
                  <span aria-hidden="true" class="relative h-6 w-11 shrink-0 rounded-full bg-tvt09-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.18)] transition-colors duration-250 peer-checked:bg-linear-to-r peer-checked:from-tvt09-acc peer-checked:to-tvt09-acc2 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tvt09-ring after:absolute after:top-0.5 after:start-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_oklch(0.2_0.03_260/0.35)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none forced-colors:border forced-colors:peer-checked:bg-[Highlight]"></span>
                </label>
              </section>

              <section aria-labelledby="tvt-09-h5" class="hidden pb-24 group-has-[#tvt-09-t5:checked]/app:block group-has-[#tvt-09-t5:checked]/app:animate-tvt09-in motion-reduce:animate-none">
                <header class="border-b border-tvt09-line px-6 pt-6 pb-5 @max-[46rem]:px-4">
                  <p class="font-tvt09-mono text-[11px] tracking-[0.12em] text-tvt09-mut uppercase">Settings / API keys</p>
                  <h3 id="tvt-09-h5" class="mt-1.5 text-[21px] font-bold tracking-[-0.025em]">API keys</h3>
                  <p class="mt-1 text-[13.5px] leading-relaxed text-tvt09-mut text-pretty">Long unbreakable strings are exactly why the content column is <code class="font-tvt09-mono text-[12px] text-tvt09-ink">minmax(0,1fr)</code>, not <code class="font-tvt09-mono text-[12px] text-tvt09-ink">1fr</code>.</p>
                </header>

                <div class="border-b border-tvt09-line/70 px-6 py-4 last:border-b-0 @max-[46rem]:px-4">
                  <div class="flex flex-wrap items-center gap-2"><p class="text-[14px] font-semibold">Production</p><span class="rounded-full px-2 py-0.5 text-[11px] font-semibold bg-tvt09-ok/14 text-tvt09-ok">Live</span><p class="ms-auto text-[12.5px] text-tvt09-mut">Created 14 Mar · used 2h ago</p></div>
                  <p class="mt-2.5 flex min-w-0 items-center gap-2 rounded-lg bg-tvt09-code px-3 py-2.5 ring-1 ring-tvt09-line"><code title="Click to select the whole key" class="min-w-0 flex-1 cursor-text font-tvt09-mono text-[12.5px] break-all text-tvt09-ink select-all">sk-demo-REDACTED</code><span aria-hidden="true" class="shrink-0 rounded-md bg-tvt09-card px-2 py-1 font-tvt09-mono text-[10.5px] text-tvt09-mut ring-1 ring-tvt09-line">click · ⌘C</span></p>
                </div>

                <div class="border-b border-tvt09-line/70 px-6 py-4 last:border-b-0 @max-[46rem]:px-4">
                  <div class="flex flex-wrap items-center gap-2"><p class="text-[14px] font-semibold">Staging</p><span class="rounded-full px-2 py-0.5 text-[11px] font-semibold bg-tvt09-sub text-tvt09-mut ring-1 ring-tvt09-line">Test</span><p class="ms-auto text-[12.5px] text-tvt09-mut">Created 2 Feb · used 6d ago</p></div>
                  <p class="mt-2.5 flex min-w-0 items-center gap-2 rounded-lg bg-tvt09-code px-3 py-2.5 ring-1 ring-tvt09-line"><code title="Click to select the whole key" class="min-w-0 flex-1 cursor-text font-tvt09-mono text-[12.5px] break-all text-tvt09-ink select-all">sk-demo-REDACTED</code><span aria-hidden="true" class="shrink-0 rounded-md bg-tvt09-card px-2 py-1 font-tvt09-mono text-[10.5px] text-tvt09-mut ring-1 ring-tvt09-line">click · ⌘C</span></p>
                </div>

                <div class="grid min-h-[4.25rem] grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)] items-center gap-5 border-b border-tvt09-line/70 px-6 py-3 last:border-b-0 @max-[46rem]:grid-cols-1 @max-[46rem]:gap-2 @max-[46rem]:px-4">
                  <div class="min-w-0"><p class="text-[14px] font-semibold">Webhook endpoint</p><p class="mt-0.5 text-[12.75px] leading-snug text-tvt09-mut">Receives signed events</p></div>
                  <p class="flex min-h-10 min-w-0 items-center rounded-lg bg-tvt09-card px-3 py-2 text-[13.5px] shadow-tvt09-field ring-1 ring-tvt09-line font-tvt09-mono text-[12.5px] break-all">https://api.acme.com/v2/hooks/inbound/console-events</p>
                </div>

                <label class="flex min-h-[4.25rem] cursor-pointer items-center justify-between gap-5 border-b border-tvt09-line/70 px-6 py-3 transition-colors duration-200 last:border-b-0 hover:bg-tvt09-ink/[0.025] motion-reduce:transition-none @max-[46rem]:px-4">
                  <span class="min-w-0"><span class="block text-[14px] font-semibold">Rotate keys every 90 days</span><span class="mt-0.5 block text-[12.75px] leading-snug text-tvt09-mut text-pretty">Old keys keep working for 24 hours after rotation</span></span>
                  <input type="checkbox" data-pref class="peer sr-only" checked>
                  <span aria-hidden="true" class="relative h-6 w-11 shrink-0 rounded-full bg-tvt09-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.18)] transition-colors duration-250 peer-checked:bg-linear-to-r peer-checked:from-tvt09-acc peer-checked:to-tvt09-acc2 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tvt09-ring after:absolute after:top-0.5 after:start-0.5 after:size-5 after:rounded-full after:bg-white after:shadow-[0_1px_3px_oklch(0.2_0.03_260/0.35)] after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:after:translate-x-5 motion-reduce:transition-none motion-reduce:after:transition-none forced-colors:border forced-colors:peer-checked:bg-[Highlight]"></span>
                </label>
              </section>
          </div>

          <div role="status" class="pointer-events-none invisible absolute inset-x-4 bottom-4 flex translate-y-4 flex-wrap items-center gap-3 rounded-2xl bg-tvt09-bar px-4 py-3 text-tvt09-bar-ink opacity-0 shadow-tvt09-bar transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-has-[[data-pref]:checked:not(:default),[data-pref]:not(:checked):default]/app:pointer-events-auto group-has-[[data-pref]:checked:not(:default),[data-pref]:not(:checked):default]/app:visible group-has-[[data-pref]:checked:not(:default),[data-pref]:not(:checked):default]/app:translate-y-0 group-has-[[data-pref]:checked:not(:default),[data-pref]:not(:checked):default]/app:opacity-100 motion-reduce:transition-none">
            <span aria-hidden="true" class="size-2 rounded-full bg-tvt09-warn shadow-[0_0_0_4px] shadow-tvt09-warn/25"></span>
            <p class="min-w-0 flex-1 text-[13.5px] font-medium">You have unsaved changes</p>
            <span class="inline-flex min-h-9 items-center rounded-lg px-3 text-[13px] font-semibold text-tvt09-bar-ink/80">Discard</span>
            <span class="inline-flex min-h-9 items-center rounded-lg bg-linear-to-r from-tvt09-acc to-tvt09-acc2 px-3.5 text-[13px] font-semibold text-white shadow-tvt09-pill">Save changes</span>
          </div>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt09-card px-3.5 py-2 text-center font-tvt09-mono text-[11.5px] text-tvt09-mut ring-1 ring-tvt09-line">group-has-[#t2:checked]/app:block · :checked:not(:default)</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt09-bg: #eef3fa;
  --color-tvt09-bg: oklch(0.963 0.01 255);
  --color-tvt09-glow: #b5d3ff99;
  --color-tvt09-glow: oklch(0.86 0.07 258 / 0.6);
  --color-tvt09-card: #fdfeff;
  --color-tvt09-card: oklch(0.997 0.002 255);
  --color-tvt09-rail: #f3f7fc;
  --color-tvt09-rail: oklch(0.975 0.008 255);
  --color-tvt09-tab: #ffffff;
  --color-tvt09-tab: oklch(1 0 0);
  --color-tvt09-sub: #eff4fa;
  --color-tvt09-sub: oklch(0.965 0.01 255);
  --color-tvt09-code: #f3f7fc;
  --color-tvt09-code: oklch(0.975 0.008 255);
  --color-tvt09-off: #cbd1db;
  --color-tvt09-off: oklch(0.86 0.015 258);
  --color-tvt09-ink: #131b29;
  --color-tvt09-ink: oklch(0.22 0.03 262);
  --color-tvt09-mut: #545e6f;
  --color-tvt09-mut: oklch(0.48 0.03 260);
  --color-tvt09-line: #d8dee7;
  --color-tvt09-line: oklch(0.9 0.014 258);
  --color-tvt09-acc: #205bdf;
  --color-tvt09-acc: oklch(0.52 0.21 263);
  --color-tvt09-acc2: #007cb7;
  --color-tvt09-acc2: oklch(0.56 0.17 240);
  --color-tvt09-acc-ink: #1c4cc8;
  --color-tvt09-acc-ink: oklch(0.47 0.2 264);
  --color-tvt09-hl: #1553dd;
  --color-tvt09-hl: oklch(0.5 0.22 263);
  --color-tvt09-hl2: #008db3;
  --color-tvt09-hl2: oklch(0.6 0.15 225);
  --color-tvt09-ring: #1c69e3;
  --color-tvt09-ring: oklch(0.55 0.2 260);
  --color-tvt09-ok: #007e46;
  --color-tvt09-ok: oklch(0.52 0.13 155);
  --color-tvt09-warn: #f2a618;
  --color-tvt09-warn: oklch(0.78 0.16 75);
  --color-tvt09-danger: #cc272e;
  --color-tvt09-danger: oklch(0.55 0.2 25);
  --color-tvt09-bar: #131b29;
  --color-tvt09-bar: oklch(0.22 0.03 262);
  --color-tvt09-bar-ink: #f2f5fb;
  --color-tvt09-bar-ink: oklch(0.97 0.008 255);
  --font-tvt09-sans: 'Onest', system-ui, sans-serif;
  --font-tvt09-mono: 'Fira Code', ui-monospace, monospace;
  --shadow-tvt09-card: 0 1px 2px oklch(0.25 0.04 262 / 0.06), 0 34px 80px -34px oklch(0.35 0.12 262 / 0.42);
  --shadow-tvt09-tab: 0 1px 2px oklch(0.25 0.04 262 / 0.1), 0 4px 12px -6px oklch(0.35 0.1 262 / 0.25), inset 0 0 0 1px oklch(0.5 0.1 262 / 0.08);
  --shadow-tvt09-pill: 0 8px 18px -8px oklch(0.5 0.21 263 / 0.65), inset 0 1px 0 oklch(1 0 0 / 0.25);
  --shadow-tvt09-field: 0 1px 2px oklch(0.25 0.04 262 / 0.06);
  --shadow-tvt09-bar: 0 20px 40px -16px oklch(0.2 0.05 262 / 0.55), 0 2px 6px oklch(0.2 0.05 262 / 0.2);
  --animate-tvt09-in: tvt09-in 0.34s cubic-bezier(0.16, 1, 0.3, 1);

  @keyframes tvt09-in {
    from {
      opacity: 0;
      translate: 0 8px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-09 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-09:not([data-theme="light"]) {
    --color-tvt09-bg: #080c15;
    --color-tvt09-bg: oklch(0.155 0.02 262);
    --color-tvt09-glow: #14306580;
    --color-tvt09-glow: oklch(0.32 0.1 262 / 0.5);
    --color-tvt09-card: #0f151f;
    --color-tvt09-card: oklch(0.195 0.022 262);
    --color-tvt09-rail: #0c1119;
    --color-tvt09-rail: oklch(0.175 0.02 262);
    --color-tvt09-tab: #1c2433;
    --color-tvt09-tab: oklch(0.26 0.03 262);
    --color-tvt09-sub: #161d29;
    --color-tvt09-sub: oklch(0.23 0.025 262);
    --color-tvt09-code: #0a0e17;
    --color-tvt09-code: oklch(0.165 0.02 262);
    --color-tvt09-off: #2f3848;
    --color-tvt09-off: oklch(0.34 0.03 262);
    --color-tvt09-ink: #eef2f7;
    --color-tvt09-ink: oklch(0.96 0.008 255);
    --color-tvt09-mut: #a4afbe;
    --color-tvt09-mut: oklch(0.75 0.025 258);
    --color-tvt09-line: #262e3d;
    --color-tvt09-line: oklch(0.3 0.03 262);
    --color-tvt09-acc: #306ae7;
    --color-tvt09-acc: oklch(0.56 0.2 263);
    --color-tvt09-acc2: #0082c0;
    --color-tvt09-acc2: oklch(0.58 0.16 240);
    --color-tvt09-acc-ink: #95c0ff;
    --color-tvt09-acc-ink: oklch(0.8 0.11 258);
    --color-tvt09-hl: #90b7ff;
    --color-tvt09-hl: oklch(0.78 0.12 262);
    --color-tvt09-hl2: #67d5f5;
    --color-tvt09-hl2: oklch(0.82 0.11 220);
    --color-tvt09-ring: #79afff;
    --color-tvt09-ring: oklch(0.75 0.13 258);
    --color-tvt09-ok: #63d18f;
    --color-tvt09-ok: oklch(0.78 0.14 155);
    --color-tvt09-warn: #f9b73f;
    --color-tvt09-warn: oklch(0.82 0.15 78);
    --color-tvt09-danger: #fd736d;
    --color-tvt09-danger: oklch(0.72 0.17 25);
    --color-tvt09-bar: #eef2f7;
    --color-tvt09-bar: oklch(0.96 0.008 255);
    --color-tvt09-bar-ink: #0e1624;
    --color-tvt09-bar-ink: oklch(0.2 0.03 262);
  }
}

.tvt-09[data-theme="dark"] {
  --color-tvt09-bg: #080c15;
  --color-tvt09-bg: oklch(0.155 0.02 262);
  --color-tvt09-glow: #14306580;
  --color-tvt09-glow: oklch(0.32 0.1 262 / 0.5);
  --color-tvt09-card: #0f151f;
  --color-tvt09-card: oklch(0.195 0.022 262);
  --color-tvt09-rail: #0c1119;
  --color-tvt09-rail: oklch(0.175 0.02 262);
  --color-tvt09-tab: #1c2433;
  --color-tvt09-tab: oklch(0.26 0.03 262);
  --color-tvt09-sub: #161d29;
  --color-tvt09-sub: oklch(0.23 0.025 262);
  --color-tvt09-code: #0a0e17;
  --color-tvt09-code: oklch(0.165 0.02 262);
  --color-tvt09-off: #2f3848;
  --color-tvt09-off: oklch(0.34 0.03 262);
  --color-tvt09-ink: #eef2f7;
  --color-tvt09-ink: oklch(0.96 0.008 255);
  --color-tvt09-mut: #a4afbe;
  --color-tvt09-mut: oklch(0.75 0.025 258);
  --color-tvt09-line: #262e3d;
  --color-tvt09-line: oklch(0.3 0.03 262);
  --color-tvt09-acc: #306ae7;
  --color-tvt09-acc: oklch(0.56 0.2 263);
  --color-tvt09-acc2: #0082c0;
  --color-tvt09-acc2: oklch(0.58 0.16 240);
  --color-tvt09-acc-ink: #95c0ff;
  --color-tvt09-acc-ink: oklch(0.8 0.11 258);
  --color-tvt09-hl: #90b7ff;
  --color-tvt09-hl: oklch(0.78 0.12 262);
  --color-tvt09-hl2: #67d5f5;
  --color-tvt09-hl2: oklch(0.82 0.11 220);
  --color-tvt09-ring: #79afff;
  --color-tvt09-ring: oklch(0.75 0.13 258);
  --color-tvt09-ok: #63d18f;
  --color-tvt09-ok: oklch(0.78 0.14 155);
  --color-tvt09-warn: #f9b73f;
  --color-tvt09-warn: oklch(0.82 0.15 78);
  --color-tvt09-danger: #fd736d;
  --color-tvt09-danger: oklch(0.72 0.17 25);
  --color-tvt09-bar: #eef2f7;
  --color-tvt09-bar: oklch(0.96 0.008 255);
  --color-tvt09-bar-ink: #0e1624;
  --color-tvt09-bar-ink: oklch(0.2 0.03 262);
}
```

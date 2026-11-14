---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-dark-mode-empty-state/"
title: "Tailwind CSS Dark Mode Empty State (dark: Variant)"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "An integrations settings page with no services connected, built to look right in both themes."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Dark Mode Empty State (dark: Variant)
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-dark-mode-empty-state/

An integrations settings page with no services connected, built to look right in both themes. A three-way System / Light / Dark switch is plain radios; Tailwind v4's @custom-variant dark reads them with :has() (and prefers-color-scheme for System), and @theme inline tokens flip in one place — no JavaScript, no flash.
## HTML
```html
<div class="tes-19 w-full min-h-svh font-tes19-sans antialiased">
  <input type="radio" name="tes19-theme" id="tes19-sys" checked class="peer/sys sr-only" aria-label="System theme">
  <input type="radio" name="tes19-theme" id="tes19-light" class="peer/light sr-only" aria-label="Light theme">
  <input type="radio" name="tes19-theme" id="tes19-dark" class="peer/dark sr-only" aria-label="Dark theme">
  <div class="grid min-h-svh bg-tes19-bg text-tes19-ink transition-colors duration-300 [--tes19-acc:#4d5bdb] [--tes19-bg:#f6f7f9] [--tes19-card:#ffffff] [--tes19-ink:#171a22] [--tes19-line:#e1e4ea] [--tes19-mut:#5a6274] [--tes19-sunk:#eef0f4] [color-scheme:light] md:grid-cols-[14rem_minmax(0,1fr)] dark:[--tes19-acc:#9aa6ff] dark:[--tes19-bg:#0e1015] dark:[--tes19-card:#151821] dark:[--tes19-ink:#eef0f6] dark:[--tes19-line:#262a35] dark:[--tes19-mut:#a1a8b9] dark:[--tes19-sunk:#1b1f29] dark:[color-scheme:dark]">
    <aside class="hidden flex-col gap-5 border-r border-tes19-line p-4 md:flex">
      <span class="flex items-center gap-2 px-2 font-semibold"><span aria-hidden="true" class="grid size-6 place-items-center rounded-lg bg-tes19-acc text-[11px] text-tes19-card">B</span>Beacon</span>
      <nav class="grid gap-0.5 text-sm">
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes19-mut hover:bg-tes19-sunk hover:text-tes19-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes19-acc">General</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes19-mut hover:bg-tes19-sunk hover:text-tes19-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes19-acc">Members</a>
        <a href="#" aria-current="page" class="flex min-h-10 items-center rounded-lg bg-tes19-sunk px-3 font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes19-acc">Integrations</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes19-mut hover:bg-tes19-sunk hover:text-tes19-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes19-acc">Billing</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes19-mut hover:bg-tes19-sunk hover:text-tes19-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes19-acc">Audit log</a>
      </nav>
    </aside>
    <main class="flex min-w-0 flex-col gap-6 px-[clamp(1rem,4vw,2.5rem)] py-6">
      <header class="flex flex-wrap items-center justify-between gap-3">
        <h1 class="text-2xl font-semibold tracking-tight">Integrations</h1>
        <div role="radiogroup" aria-label="Appearance" class="flex rounded-xl bg-tes19-sunk p-1 text-sm">
          <label for="tes19-sys" class="inline-flex min-h-10 cursor-pointer items-center gap-1.5 rounded-lg px-3 text-tes19-mut transition [.tes-19:has(#tes19-sys:checked)_&]:bg-tes19-card [.tes-19:has(#tes19-sys:checked)_&]:text-tes19-ink [.tes-19:has(#tes19-sys:checked)_&]:shadow-sm [.tes-19:has(#tes19-sys:focus-visible)_&]:outline-2 [.tes-19:has(#tes19-sys:focus-visible)_&]:outline-tes19-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3.5" y="4.5" width="17" height="11.5" rx="1.5"/><path d="M9 20h6M12 16v4"/></svg>System</label>
          <label for="tes19-light" class="inline-flex min-h-10 cursor-pointer items-center gap-1.5 rounded-lg px-3 text-tes19-mut transition [.tes-19:has(#tes19-light:checked)_&]:bg-tes19-card [.tes-19:has(#tes19-light:checked)_&]:text-tes19-ink [.tes-19:has(#tes19-light:checked)_&]:shadow-sm [.tes-19:has(#tes19-light:focus-visible)_&]:outline-2 [.tes-19:has(#tes19-light:focus-visible)_&]:outline-tes19-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6 7 7M17 17l1.4 1.4M5.6 18.4 7 17M17 7l1.4-1.4"/></svg>Light</label>
          <label for="tes19-dark" class="inline-flex min-h-10 cursor-pointer items-center gap-1.5 rounded-lg px-3 text-tes19-mut transition [.tes-19:has(#tes19-dark:checked)_&]:bg-tes19-card [.tes-19:has(#tes19-dark:checked)_&]:text-tes19-ink [.tes-19:has(#tes19-dark:checked)_&]:shadow-sm [.tes-19:has(#tes19-dark:focus-visible)_&]:outline-2 [.tes-19:has(#tes19-dark:focus-visible)_&]:outline-tes19-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M19.5 14.5A7.5 7.5 0 0 1 9.5 4.5a7.5 7.5 0 1 0 10 10z"/></svg>Dark</label>
        </div>
      </header>
      <section aria-labelledby="tes19-cs" class="overflow-hidden rounded-2xl bg-tes19-card ring-1 ring-tes19-line shadow-[0_1px_2px_rgb(0_0_0/0.04)] dark:shadow-none">
        <div class="flex items-center justify-between border-b border-tes19-line px-5 py-3.5"><span id="tes19-cs" class="text-sm font-medium">Connected services</span><span class="rounded-full bg-tes19-sunk px-2.5 py-1 font-tes19-mono text-[11px] text-tes19-mut">none</span></div>
        <div class="grid justify-items-center px-6 py-14 text-center">
          <span aria-hidden="true" class="relative grid size-18 place-items-center">
            <span class="absolute inset-0 rounded-full bg-tes19-acc/10 dark:bg-tes19-acc/15 dark:shadow-[0_0_60px_-6px_var(--tes19-acc)]"></span>
            <span class="relative flex items-center gap-1"><i class="h-6 w-4 rounded-l-full rounded-r-md border-2 border-tes19-acc"></i><i class="h-0.5 w-2 rounded bg-tes19-acc"></i><i class="h-6 w-4 rounded-l-md rounded-r-full border-2 border-dashed border-tes19-acc"></i></span>
          </span>
          <h2 class="mt-5 text-lg font-semibold">No services connected</h2>
          <p class="mt-1.5 max-w-[44ch] text-sm/6 text-tes19-mut text-pretty">Connect the tools your team already pays for and Beacon starts reading events from them within a minute.</p>
          <div class="mt-5 flex flex-wrap justify-center gap-2.5">
            <button type="button" class="min-h-11 rounded-xl bg-tes19-ink px-5 text-sm font-medium text-tes19-card transition hover:opacity-90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes19-acc">Browse the directory</button>
            <button type="button" class="min-h-11 rounded-xl border border-tes19-line px-4 text-sm hover:bg-tes19-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes19-acc">Create an API key</button>
          </div>
        </div>
        <ul class="grid gap-px border-t border-tes19-line bg-tes19-line sm:grid-cols-3">
          <li class="flex items-center gap-3 bg-tes19-card px-5 py-4 text-sm"><span aria-hidden="true" class="size-8 rounded-lg bg-[conic-gradient(#e01e5a_0_25%,#36c5f0_0_50%,#2eb67d_0_75%,#ecb22e_0)] opacity-90"></span><span class="grid"><b class="font-medium">Slack</b><span class="text-xs text-tes19-mut">Alerts and digests</span></span></li>
          <li class="flex items-center gap-3 bg-tes19-card px-5 py-4 text-sm"><span aria-hidden="true" class="size-8 rounded-lg bg-linear-to-br from-[#5e6ad2] to-[#8b93f0]"></span><span class="grid"><b class="font-medium">Linear</b><span class="text-xs text-tes19-mut">Issue sync</span></span></li>
          <li class="flex items-center gap-3 bg-tes19-card px-5 py-4 text-sm"><span aria-hidden="true" class="size-8 rounded-lg bg-linear-to-br from-[#29b5e8] to-[#7fd6f5]"></span><span class="grid"><b class="font-medium">Snowflake</b><span class="text-xs text-tes19-mut">Warehouse export</span></span></li>
        </ul>
      </section>
    </main>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@custom-variant dark {
  &:where(.tes-19:has(#tes19-dark:checked) *) {
    @slot;
  }

  @media (prefers-color-scheme: dark) {
    &:where(.tes-19:has(#tes19-sys:checked) *) {
      @slot;
    }
  }
}

@theme inline {
  --color-tes19-bg: var(--tes19-bg);
  --color-tes19-card: var(--tes19-card);
  --color-tes19-sunk: var(--tes19-sunk);
  --color-tes19-line: var(--tes19-line);
  --color-tes19-ink: var(--tes19-ink);
  --color-tes19-mut: var(--tes19-mut);
  --color-tes19-acc: var(--tes19-acc);
}

@theme {
  --font-tes19-sans: 'Geist', system-ui, sans-serif;
  --font-tes19-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-19 {
  width: 100%;
  min-height: 100svh;
}

.tes-19 [hidden] {
  display: none !important;
}
```

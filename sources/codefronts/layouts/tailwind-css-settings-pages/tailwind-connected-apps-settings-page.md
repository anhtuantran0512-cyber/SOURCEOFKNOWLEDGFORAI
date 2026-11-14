---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-connected-apps-settings-page/"
title: "Tailwind Connected Apps Settings Page"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A zero-JavaScript integrations directory: category chips that filter the grid, a 'Connected' chip that shows only what you've linked, connect buttons built…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Connected Apps Settings Page
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-connected-apps-settings-page/

A zero-JavaScript integrations directory: category chips that filter the grid, a 'Connected' chip that shows only what you've linked, connect buttons built on real checkboxes that flip to 'Connected' and reveal what each app can access, and a sticky footer whose live count comes from a CSS counter — not a script.
## HTML
```html
<section class="tsp-13 group/apps w-full min-h-svh bg-tsp13-bg px-4 py-10 font-tsp13-sans text-tsp13-ink antialiased [counter-reset:tsp13] sm:px-8 sm:py-14" aria-labelledby="tsp-13-h">
  <div class="mx-auto grid w-full max-w-6xl gap-6 pb-24">
    <header class="grid gap-1"><h1 id="tsp-13-h" class="text-3xl font-extrabold tracking-tight sm:text-4xl">Connected apps</h1><p class="text-pretty text-tsp13-mut">Bring the tools your team already uses into Northwind.</p></header>

    <fieldset class="flex flex-wrap gap-2">
      <legend class="sr-only">Filter apps</legend>
      <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tsp13-line bg-white px-4 text-sm font-semibold text-tsp13-mut transition hover:text-tsp13-ink has-checked:border-transparent has-checked:bg-tsp13-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="radio" name="tsp-13-cat" id="tsp-13-c-all" class="sr-only" checked>All</label>
      <label class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-full border border-tsp13-line bg-white px-4 text-sm font-semibold text-tsp13-mut transition hover:text-tsp13-ink has-checked:border-transparent has-checked:bg-tsp13-acc has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="radio" name="tsp-13-cat" id="tsp-13-c-on" class="sr-only"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</label>
      <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tsp13-line bg-white px-4 text-sm font-semibold text-tsp13-mut transition hover:text-tsp13-ink has-checked:border-transparent has-checked:bg-tsp13-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="radio" name="tsp-13-cat" id="tsp-13-c-comm" class="sr-only">Communication</label>
      <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tsp13-line bg-white px-4 text-sm font-semibold text-tsp13-mut transition hover:text-tsp13-ink has-checked:border-transparent has-checked:bg-tsp13-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="radio" name="tsp-13-cat" id="tsp-13-c-dev" class="sr-only">Developer</label>
      <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tsp13-line bg-white px-4 text-sm font-semibold text-tsp13-mut transition hover:text-tsp13-ink has-checked:border-transparent has-checked:bg-tsp13-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="radio" name="tsp-13-cat" id="tsp-13-c-design" class="sr-only">Design</label>
      <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tsp13-line bg-white px-4 text-sm font-semibold text-tsp13-mut transition hover:text-tsp13-ink has-checked:border-transparent has-checked:bg-tsp13-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="radio" name="tsp-13-cat" id="tsp-13-c-prod" class="sr-only">Productivity</label>
      <label class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-tsp13-line bg-white px-4 text-sm font-semibold text-tsp13-mut transition hover:text-tsp13-ink has-checked:border-transparent has-checked:bg-tsp13-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="radio" name="tsp-13-cat" id="tsp-13-c-sales" class="sr-only">Sales</label>
    </fieldset>

    <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 group-has-[#tsp-13-c-on:checked]/apps:[&>article:not(:has(input:checked))]:hidden group-has-[#tsp-13-c-comm:checked]/apps:[&>[data-cat]:not([data-cat=comm])]:hidden group-has-[#tsp-13-c-dev:checked]/apps:[&>[data-cat]:not([data-cat=dev])]:hidden group-has-[#tsp-13-c-design:checked]/apps:[&>[data-cat]:not([data-cat=design])]:hidden group-has-[#tsp-13-c-prod:checked]/apps:[&>[data-cat]:not([data-cat=prod])]:hidden group-has-[#tsp-13-c-sales:checked]/apps:[&>[data-cat]:not([data-cat=sales])]:hidden">
      <article data-cat="comm" class="group/card grid content-start gap-4 rounded-3xl border border-tsp13-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-24px_rgb(20_20_40/0.3)] has-checked:border-tsp13-acc/40 has-checked:ring-4 has-checked:ring-tsp13-acc/8 motion-reduce:transition-none">
        <div class="flex items-start gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-[#4a154b] text-lg font-extrabold text-white">S</span><div class="min-w-0 flex-1"><h2 class="font-bold">Slack</h2><p class="text-xs font-semibold uppercase tracking-wide text-tsp13-mut">Communication</p></div></div>
        <p class="text-sm text-tsp13-mut">Post updates to channels and turn messages into tasks.</p>
        <div class="hidden gap-1 rounded-2xl bg-tsp13-bg p-3 text-xs text-tsp13-mut group-has-checked/card:grid"><span><strong class="font-semibold text-tsp13-ink">Can:</strong> read channel names, post messages</span><span>Connected by Ava · posting to #eng-alerts</span></div>
        <label class="inline-flex min-h-11 w-fit cursor-pointer items-center gap-2 rounded-xl border border-tsp13-line px-4 text-sm font-bold transition hover:bg-tsp13-bg has-checked:border-emerald-200 has-checked:bg-emerald-50 has-checked:text-emerald-700 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="checkbox" class="sr-only checked:[counter-increment:tsp13]" checked aria-label="Connect Slack"><span class="group-has-checked/card:hidden">Connect</span><span class="hidden items-center gap-1.5 group-has-checked/card:inline-flex"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</span></label>
      </article>
      <article data-cat="dev" class="group/card grid content-start gap-4 rounded-3xl border border-tsp13-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-24px_rgb(20_20_40/0.3)] has-checked:border-tsp13-acc/40 has-checked:ring-4 has-checked:ring-tsp13-acc/8 motion-reduce:transition-none">
        <div class="flex items-start gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-[#1f2328] text-lg font-extrabold text-white">G</span><div class="min-w-0 flex-1"><h2 class="font-bold">GitHub</h2><p class="text-xs font-semibold uppercase tracking-wide text-tsp13-mut">Developer</p></div></div>
        <p class="text-sm text-tsp13-mut">Link pull requests to tasks and close them on merge.</p>
        <div class="hidden gap-1 rounded-2xl bg-tsp13-bg p-3 text-xs text-tsp13-mut group-has-checked/card:grid"><span><strong class="font-semibold text-tsp13-ink">Can:</strong> read repos, PRs and commit status</span><span>Connected by Noah · 14 repositories</span></div>
        <label class="inline-flex min-h-11 w-fit cursor-pointer items-center gap-2 rounded-xl border border-tsp13-line px-4 text-sm font-bold transition hover:bg-tsp13-bg has-checked:border-emerald-200 has-checked:bg-emerald-50 has-checked:text-emerald-700 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="checkbox" class="sr-only checked:[counter-increment:tsp13]" checked aria-label="Connect GitHub"><span class="group-has-checked/card:hidden">Connect</span><span class="hidden items-center gap-1.5 group-has-checked/card:inline-flex"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</span></label>
      </article>
      <article data-cat="design" class="group/card grid content-start gap-4 rounded-3xl border border-tsp13-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-24px_rgb(20_20_40/0.3)] has-checked:border-tsp13-acc/40 has-checked:ring-4 has-checked:ring-tsp13-acc/8 motion-reduce:transition-none">
        <div class="flex items-start gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-linear-135 from-[#f24e1e] via-[#a259ff] to-[#1abcfe] text-lg font-extrabold text-white">F</span><div class="min-w-0 flex-1"><h2 class="font-bold">Figma</h2><p class="text-xs font-semibold uppercase tracking-wide text-tsp13-mut">Design</p></div></div>
        <p class="text-sm text-tsp13-mut">Embed live frames in docs; previews update as designs change.</p>
        <div class="hidden gap-1 rounded-2xl bg-tsp13-bg p-3 text-xs text-tsp13-mut group-has-checked/card:grid"><span><strong class="font-semibold text-tsp13-ink">Can:</strong> read files you share</span><span>Connected by Mia · 6 embeds</span></div>
        <label class="inline-flex min-h-11 w-fit cursor-pointer items-center gap-2 rounded-xl border border-tsp13-line px-4 text-sm font-bold transition hover:bg-tsp13-bg has-checked:border-emerald-200 has-checked:bg-emerald-50 has-checked:text-emerald-700 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="checkbox" class="sr-only checked:[counter-increment:tsp13]" checked aria-label="Connect Figma"><span class="group-has-checked/card:hidden">Connect</span><span class="hidden items-center gap-1.5 group-has-checked/card:inline-flex"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</span></label>
      </article>
      <article data-cat="prod" class="group/card grid content-start gap-4 rounded-3xl border border-tsp13-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-24px_rgb(20_20_40/0.3)] has-checked:border-tsp13-acc/40 has-checked:ring-4 has-checked:ring-tsp13-acc/8 motion-reduce:transition-none">
        <div class="flex items-start gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-[#1a73e8] text-lg font-extrabold text-white">D</span><div class="min-w-0 flex-1"><h2 class="font-bold">Google Drive</h2><p class="text-xs font-semibold uppercase tracking-wide text-tsp13-mut">Productivity</p></div></div>
        <p class="text-sm text-tsp13-mut">Attach Docs, Sheets and Slides with live previews.</p>
        <div class="hidden gap-1 rounded-2xl bg-tsp13-bg p-3 text-xs text-tsp13-mut group-has-checked/card:grid"><span><strong class="font-semibold text-tsp13-ink">Can:</strong> open files you pick</span><span>Connected just now</span></div>
        <label class="inline-flex min-h-11 w-fit cursor-pointer items-center gap-2 rounded-xl border border-tsp13-line px-4 text-sm font-bold transition hover:bg-tsp13-bg has-checked:border-emerald-200 has-checked:bg-emerald-50 has-checked:text-emerald-700 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="checkbox" class="sr-only checked:[counter-increment:tsp13]" aria-label="Connect Google Drive"><span class="group-has-checked/card:hidden">Connect</span><span class="hidden items-center gap-1.5 group-has-checked/card:inline-flex"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</span></label>
      </article>
      <article data-cat="prod" class="group/card grid content-start gap-4 rounded-3xl border border-tsp13-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-24px_rgb(20_20_40/0.3)] has-checked:border-tsp13-acc/40 has-checked:ring-4 has-checked:ring-tsp13-acc/8 motion-reduce:transition-none">
        <div class="flex items-start gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-white text-lg font-extrabold text-black ring-1 ring-tsp13-line">N</span><div class="min-w-0 flex-1"><h2 class="font-bold">Notion</h2><p class="text-xs font-semibold uppercase tracking-wide text-tsp13-mut">Productivity</p></div></div>
        <p class="text-sm text-tsp13-mut">Sync specs and meeting notes into project timelines.</p>
        <div class="hidden gap-1 rounded-2xl bg-tsp13-bg p-3 text-xs text-tsp13-mut group-has-checked/card:grid"><span><strong class="font-semibold text-tsp13-ink">Can:</strong> read pages you share</span><span>Connected just now</span></div>
        <label class="inline-flex min-h-11 w-fit cursor-pointer items-center gap-2 rounded-xl border border-tsp13-line px-4 text-sm font-bold transition hover:bg-tsp13-bg has-checked:border-emerald-200 has-checked:bg-emerald-50 has-checked:text-emerald-700 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="checkbox" class="sr-only checked:[counter-increment:tsp13]" aria-label="Connect Notion"><span class="group-has-checked/card:hidden">Connect</span><span class="hidden items-center gap-1.5 group-has-checked/card:inline-flex"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</span></label>
      </article>
      <article data-cat="dev" class="group/card grid content-start gap-4 rounded-3xl border border-tsp13-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-24px_rgb(20_20_40/0.3)] has-checked:border-tsp13-acc/40 has-checked:ring-4 has-checked:ring-tsp13-acc/8 motion-reduce:transition-none">
        <div class="flex items-start gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-[#362d59] text-lg font-extrabold text-white">S</span><div class="min-w-0 flex-1"><h2 class="font-bold">Sentry</h2><p class="text-xs font-semibold uppercase tracking-wide text-tsp13-mut">Developer</p></div></div>
        <p class="text-sm text-tsp13-mut">Open issues from errors and link them to releases.</p>
        <div class="hidden gap-1 rounded-2xl bg-tsp13-bg p-3 text-xs text-tsp13-mut group-has-checked/card:grid"><span><strong class="font-semibold text-tsp13-ink">Can:</strong> read issues and releases</span><span>Connected just now</span></div>
        <label class="inline-flex min-h-11 w-fit cursor-pointer items-center gap-2 rounded-xl border border-tsp13-line px-4 text-sm font-bold transition hover:bg-tsp13-bg has-checked:border-emerald-200 has-checked:bg-emerald-50 has-checked:text-emerald-700 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="checkbox" class="sr-only checked:[counter-increment:tsp13]" aria-label="Connect Sentry"><span class="group-has-checked/card:hidden">Connect</span><span class="hidden items-center gap-1.5 group-has-checked/card:inline-flex"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</span></label>
      </article>
      <article data-cat="comm" class="group/card grid content-start gap-4 rounded-3xl border border-tsp13-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-24px_rgb(20_20_40/0.3)] has-checked:border-tsp13-acc/40 has-checked:ring-4 has-checked:ring-tsp13-acc/8 motion-reduce:transition-none">
        <div class="flex items-start gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-[#2d8cff] text-lg font-extrabold text-white">Z</span><div class="min-w-0 flex-1"><h2 class="font-bold">Zoom</h2><p class="text-xs font-semibold uppercase tracking-wide text-tsp13-mut">Communication</p></div></div>
        <p class="text-sm text-tsp13-mut">Start a call from any task; recordings attach automatically.</p>
        <div class="hidden gap-1 rounded-2xl bg-tsp13-bg p-3 text-xs text-tsp13-mut group-has-checked/card:grid"><span><strong class="font-semibold text-tsp13-ink">Can:</strong> create meetings, read recordings</span><span>Connected just now</span></div>
        <label class="inline-flex min-h-11 w-fit cursor-pointer items-center gap-2 rounded-xl border border-tsp13-line px-4 text-sm font-bold transition hover:bg-tsp13-bg has-checked:border-emerald-200 has-checked:bg-emerald-50 has-checked:text-emerald-700 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="checkbox" class="sr-only checked:[counter-increment:tsp13]" aria-label="Connect Zoom"><span class="group-has-checked/card:hidden">Connect</span><span class="hidden items-center gap-1.5 group-has-checked/card:inline-flex"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</span></label>
      </article>
      <article data-cat="sales" class="group/card grid content-start gap-4 rounded-3xl border border-tsp13-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-24px_rgb(20_20_40/0.3)] has-checked:border-tsp13-acc/40 has-checked:ring-4 has-checked:ring-tsp13-acc/8 motion-reduce:transition-none">
        <div class="flex items-start gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-[#00a1e0] text-lg font-extrabold text-white">S</span><div class="min-w-0 flex-1"><h2 class="flex items-center gap-2 font-bold">Salesforce <span class="rounded-full bg-amber-100 px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide text-amber-800">Business</span></h2><p class="text-xs font-semibold uppercase tracking-wide text-tsp13-mut">Sales</p></div></div>
        <p class="text-sm text-tsp13-mut">Mirror accounts and opportunities onto customer projects.</p>
        <div class="hidden gap-1 rounded-2xl bg-tsp13-bg p-3 text-xs text-tsp13-mut group-has-checked/card:grid"><span><strong class="font-semibold text-tsp13-ink">Can:</strong> read accounts and opportunities</span><span>Connected just now</span></div>
        <label class="inline-flex min-h-11 w-fit cursor-pointer items-center gap-2 rounded-xl border border-tsp13-line px-4 text-sm font-bold transition hover:bg-tsp13-bg has-checked:border-emerald-200 has-checked:bg-emerald-50 has-checked:text-emerald-700 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="checkbox" class="sr-only checked:[counter-increment:tsp13]" aria-label="Connect Salesforce"><span class="group-has-checked/card:hidden">Connect</span><span class="hidden items-center gap-1.5 group-has-checked/card:inline-flex"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</span></label>
      </article>
      <article data-cat="sales" class="group/card grid content-start gap-4 rounded-3xl border border-tsp13-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-24px_rgb(20_20_40/0.3)] has-checked:border-tsp13-acc/40 has-checked:ring-4 has-checked:ring-tsp13-acc/8 motion-reduce:transition-none">
        <div class="flex items-start gap-4"><span class="grid size-12 flex-none place-items-center rounded-2xl bg-[#ff7a59] text-lg font-extrabold text-white">H</span><div class="min-w-0 flex-1"><h2 class="font-bold">HubSpot</h2><p class="text-xs font-semibold uppercase tracking-wide text-tsp13-mut">Sales</p></div></div>
        <p class="text-sm text-tsp13-mut">Create deals from forms and track handoffs to delivery.</p>
        <div class="hidden gap-1 rounded-2xl bg-tsp13-bg p-3 text-xs text-tsp13-mut group-has-checked/card:grid"><span><strong class="font-semibold text-tsp13-ink">Can:</strong> read contacts and deals</span><span>Connected just now</span></div>
        <label class="inline-flex min-h-11 w-fit cursor-pointer items-center gap-2 rounded-xl border border-tsp13-line px-4 text-sm font-bold transition hover:bg-tsp13-bg has-checked:border-emerald-200 has-checked:bg-emerald-50 has-checked:text-emerald-700 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp13-acc"><input type="checkbox" class="sr-only checked:[counter-increment:tsp13]" aria-label="Connect HubSpot"><span class="group-has-checked/card:hidden">Connect</span><span class="hidden items-center gap-1.5 group-has-checked/card:inline-flex"><span class="size-1.5 rounded-full bg-emerald-500"></span>Connected</span></label>
      </article>
    </div>

    <div class="flex flex-wrap items-center justify-between gap-4 rounded-3xl border border-dashed border-tsp13-line p-5">
      <p class="text-sm text-tsp13-mut"><strong class="font-semibold text-tsp13-ink">Don't see your tool?</strong> Build your own with the REST API and webhooks.</p>
      <a href="#tsp-13-h" class="inline-flex min-h-11 items-center gap-2 rounded-xl px-3 text-sm font-bold text-tsp13-acc transition hover:bg-tsp13-acc/8 focus-visible:outline-2 focus-visible:outline-tsp13-acc">Read the API docs<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
  </div>
  <p class="fixed inset-x-0 bottom-4 z-10 mx-auto flex w-fit items-center gap-2 rounded-full bg-tsp13-ink py-2.5 pl-4 pr-5 text-sm font-semibold text-white shadow-2xl before:grid before:size-6 before:place-items-center before:rounded-full before:bg-tsp13-acc before:text-xs before:font-extrabold before:content-[counter(tsp13)]">connected in this view</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp13-bg: #f5f4f1;
  --color-tsp13-bg: oklch(0.967 0.005 85);
  --color-tsp13-ink: #1b1a17;
  --color-tsp13-ink: oklch(0.215 0.007 85);
  --color-tsp13-mut: #67645c;
  --color-tsp13-mut: oklch(0.51 0.014 85);
  --color-tsp13-line: #e6e3dc;
  --color-tsp13-line: oklch(0.917 0.01 85);
  --color-tsp13-acc: #2f6bff;
  --color-tsp13-acc: oklch(0.573 0.229 262);
  --font-tsp13-sans: 'Bricolage Grotesque', system-ui, sans-serif;
}

.tsp-13 {
  width: 100%;
  min-height: 100svh;
}
```

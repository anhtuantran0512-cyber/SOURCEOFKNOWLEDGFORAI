---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-onboarding-empty-state-setup-checklist/"
title: "Tailwind CSS Onboarding Empty State with Setup Checklist"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "The first-run screen of a project tool: a three-step setup checklist whose headline rewrites itself as you tick, a sidebar progress ring drawn with…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Onboarding Empty State with Setup Checklist
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-onboarding-empty-state-setup-checklist/

The first-run screen of a project tool: a three-step setup checklist whose headline rewrites itself as you tick, a sidebar progress ring drawn with conic-gradient, and a template picker as the secondary path. Ticks are aria-pressed buttons, so every row styles itself with has-aria-pressed: — strike-through, colour and check icon included.
## HTML
```html
<div class="tes-02 w-full min-h-svh bg-tes02-bg font-tes02-sans text-tes02-ink antialiased">
  <div class="grid min-h-svh md:grid-cols-[15rem_minmax(0,1fr)]">
    <aside class="hidden flex-col gap-6 border-r border-tes02-line bg-tes02-side p-4 md:flex">
      <button type="button" class="flex min-h-12 items-center gap-3 rounded-xl p-1.5 text-left transition-colors hover:bg-tes02-card focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc">
        <span aria-hidden="true" class="grid size-9 place-items-center rounded-lg bg-tes02-ink text-xs font-semibold text-white">NL</span>
        <span class="grid flex-1"><span class="text-sm font-semibold">Northline</span><span class="text-xs text-tes02-mut">Team workspace</span></span>
        <svg class="size-4 text-tes02-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m8 10 4-4 4 4M8 14l4 4 4-4"/></svg>
      </button>
      <nav aria-label="Workspace" class="grid gap-0.5">
        <a href="#" aria-current="page" class="flex min-h-10 items-center gap-2.5 rounded-lg bg-tes02-card px-3 text-sm font-medium shadow-xs ring-1 ring-tes02-line focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><svg class="size-4 text-tes02-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M4 10h16M10 10v10"/></svg>Projects</a>
        <a href="#" class="flex min-h-10 items-center gap-2.5 rounded-lg px-3 text-sm text-tes02-mut transition-colors hover:bg-tes02-card hover:text-tes02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12 4 4 10-10"/></svg>My tasks</a>
        <a href="#" class="flex min-h-10 items-center gap-2.5 rounded-lg px-3 text-sm text-tes02-mut transition-colors hover:bg-tes02-card hover:text-tes02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="9" cy="8" r="3.5"/><path d="M3 20a6 6 0 0 1 12 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3 6"/></svg>People</a>
        <a href="#" class="flex min-h-10 items-center gap-2.5 rounded-lg px-3 text-sm text-tes02-mut transition-colors hover:bg-tes02-card hover:text-tes02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3 12h4l3-7 4 14 3-7h4"/></svg>Activity</a>
      </nav>
      <div class="mt-auto flex items-center gap-3 rounded-xl bg-tes02-card p-3 ring-1 ring-tes02-line">
        <span id="tes02-ring" aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-full bg-[conic-gradient(var(--color-tes02-acc)_var(--tes02-p),var(--color-tes02-line)_0)] transition-[--tes02-p] duration-500 ease-out [--tes02-p:0deg]"><span id="tes02-ringtext" class="grid size-8 place-items-center rounded-full bg-tes02-card font-tes02-mono text-[11px] font-medium">0/3</span></span>
        <span class="grid text-xs"><span class="font-semibold">Workspace setup</span><span class="text-tes02-mut">About 2 minutes</span></span>
      </div>
    </aside>
    <div class="flex min-w-0 flex-col">
      <header class="flex min-h-16 items-center justify-between gap-4 border-b border-tes02-line px-[clamp(1rem,4vw,2.5rem)]">
        <span class="text-sm font-medium">Projects</span>
        <div class="flex items-center gap-2">
          <button type="button" class="min-h-10 rounded-lg px-3 text-sm text-tes02-mut transition-colors hover:bg-tes02-side hover:text-tes02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc">Invite</button>
          <span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-tes02-acc text-xs font-semibold text-white">EM</span>
        </div>
      </header>
      <div class="grid flex-1 content-center gap-6 px-[clamp(1rem,4vw,2.5rem)] py-10 lg:grid-cols-[minmax(0,1fr)_17rem] lg:items-start">
        <section id="tes02-setup" class="group/setup relative overflow-hidden rounded-2xl bg-tes02-card p-[clamp(1.25rem,3vw,2rem)] shadow-[0_1px_2px_oklch(0.3_0.03_270/0.06),0_24px_48px_-24px_oklch(0.3_0.05_270/0.25)] ring-1 ring-tes02-line transition-shadow duration-500 data-ready:ring-2 data-ready:ring-tes02-acc/50">
          <span aria-hidden="true" class="pointer-events-none absolute -top-24 -right-24 size-72 rounded-full bg-tes02-acc/10 blur-3xl transition-opacity duration-500 group-data-ready/setup:bg-tes02-ok/20"></span>
          <div class="relative grid gap-2">
            <p class="font-tes02-mono text-[11px] font-medium tracking-[0.14em] text-tes02-acc uppercase">Getting started</p>
            <h1 id="tes02-title" aria-live="polite" class="text-[clamp(1.4rem,2.6vw,1.85rem)] leading-tight font-semibold tracking-tight text-balance">Three steps and Northline is yours</h1>
            <p id="tes02-sub" class="max-w-prose text-sm/6 text-tes02-mut text-pretty">Nothing here yet. Set the basics and your first board builds itself.</p>
          </div>
          <div aria-hidden="true" class="relative mt-5 h-1.5 overflow-hidden rounded-full bg-tes02-line"><span id="tes02-bar" class="block h-full w-0 rounded-full bg-linear-to-r from-tes02-acc to-tes02-ok transition-[width] duration-500 ease-out"></span></div>
          <ol class="relative mt-5 grid gap-2">
            <li class="flex items-center gap-3.5 rounded-xl border border-tes02-line p-3 transition-colors has-[[aria-pressed=true]]:border-tes02-ok/40 has-[[aria-pressed=true]]:bg-tes02-ok/5">
              <button type="button" data-step aria-pressed="false" aria-label="Mark step done: Name your first project" class="group/tick grid size-11 flex-none place-items-center rounded-full border-2 border-dashed border-tes02-line2 text-transparent transition hover:border-tes02-acc aria-pressed:border-solid aria-pressed:border-tes02-ok aria-pressed:bg-tes02-ok aria-pressed:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></button>
              <span class="grid gap-0.5"><span class="text-sm font-medium [li:has([aria-pressed=true])_&]:text-tes02-mut [li:has([aria-pressed=true])_&]:line-through">Name your first project</span><span class="text-xs text-tes02-mut">Boards, timeline and docs come with it.</span></span>
            </li>
            <li class="flex items-center gap-3.5 rounded-xl border border-tes02-line p-3 transition-colors has-[[aria-pressed=true]]:border-tes02-ok/40 has-[[aria-pressed=true]]:bg-tes02-ok/5">
              <button type="button" data-step aria-pressed="false" aria-label="Mark step done: Invite two teammates" class="grid size-11 flex-none place-items-center rounded-full border-2 border-dashed border-tes02-line2 text-transparent transition hover:border-tes02-acc aria-pressed:border-solid aria-pressed:border-tes02-ok aria-pressed:bg-tes02-ok aria-pressed:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></button>
              <span class="grid gap-0.5"><span class="text-sm font-medium [li:has([aria-pressed=true])_&]:text-tes02-mut [li:has([aria-pressed=true])_&]:line-through">Invite two teammates</span><span class="text-xs text-tes02-mut">Assignees make the board useful.</span></span>
            </li>
            <li class="flex items-center gap-3.5 rounded-xl border border-tes02-line p-3 transition-colors has-[[aria-pressed=true]]:border-tes02-ok/40 has-[[aria-pressed=true]]:bg-tes02-ok/5">
              <button type="button" data-step aria-pressed="false" aria-label="Mark step done: Connect a repository" class="grid size-11 flex-none place-items-center rounded-full border-2 border-dashed border-tes02-line2 text-transparent transition hover:border-tes02-acc aria-pressed:border-solid aria-pressed:border-tes02-ok aria-pressed:bg-tes02-ok aria-pressed:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></button>
              <span class="grid gap-0.5"><span class="text-sm font-medium [li:has([aria-pressed=true])_&]:text-tes02-mut [li:has([aria-pressed=true])_&]:line-through">Connect a repository</span><span class="text-xs text-tes02-mut">Commits close tasks automatically.</span></span>
            </li>
          </ol>
          <div class="relative mt-6 flex flex-wrap items-center gap-2.5">
            <button type="button" id="tes02-pri" class="min-h-11 rounded-xl bg-tes02-ink px-5 text-sm font-medium text-white shadow-sm transition hover:bg-tes02-acc active:scale-[.98] group-data-ready/setup:bg-tes02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc">Create your first project</button>
            <button type="button" id="tes02-reset" class="min-h-11 rounded-xl px-3 text-sm text-tes02-mut underline-offset-4 hover:text-tes02-ink hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc">Start over</button>
          </div>
        </section>
        <aside aria-labelledby="tes02-tl" class="grid gap-3">
          <p id="tes02-tl" class="text-xs font-medium text-tes02-mut">Or start from a template</p>
          <ul class="grid gap-2">
            <li><button type="button" class="flex min-h-14 w-full items-center gap-3 rounded-xl bg-tes02-card p-2.5 text-left ring-1 ring-tes02-line transition hover:-translate-y-0.5 hover:shadow-md hover:ring-tes02-acc/40 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><span aria-hidden="true" class="size-10 flex-none rounded-lg bg-[linear-gradient(135deg,#6d5ef6,#a99cff)]"></span><span class="grid"><span class="text-sm font-medium">Product sprint</span><span class="text-xs text-tes02-mut">Backlog, sprint, review</span></span></button></li>
            <li><button type="button" class="flex min-h-14 w-full items-center gap-3 rounded-xl bg-tes02-card p-2.5 text-left ring-1 ring-tes02-line transition hover:-translate-y-0.5 hover:shadow-md hover:ring-tes02-acc/40 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><span aria-hidden="true" class="size-10 flex-none rounded-lg bg-[linear-gradient(135deg,#f08a4b,#ffc58f)]"></span><span class="grid"><span class="text-sm font-medium">Go-to-market launch</span><span class="text-xs text-tes02-mut">Assets, channels, dates</span></span></button></li>
            <li><button type="button" class="flex min-h-14 w-full items-center gap-3 rounded-xl bg-tes02-card p-2.5 text-left ring-1 ring-tes02-line transition hover:-translate-y-0.5 hover:shadow-md hover:ring-tes02-acc/40 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><span aria-hidden="true" class="size-10 flex-none rounded-lg bg-[linear-gradient(135deg,#1f9d76,#7fdcb9)]"></span><span class="grid"><span class="text-sm font-medium">Hiring pipeline</span><span class="text-xs text-tes02-mut">Stages and scorecards</span></span></button></li>
            <li><button type="button" class="flex min-h-14 w-full items-center gap-3 rounded-xl bg-tes02-card p-2.5 text-left ring-1 ring-tes02-line transition hover:-translate-y-0.5 hover:shadow-md hover:ring-tes02-acc/40 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes02-acc"><span aria-hidden="true" class="size-10 flex-none rounded-lg bg-[linear-gradient(135deg,#2f6fe0,#8fc0ff)]"></span><span class="grid"><span class="text-sm font-medium">Support triage</span><span class="text-xs text-tes02-mut">Severity and rotation</span></span></button></li>
          </ul>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes02-bg: #fafafc;
  --color-tes02-bg: oklch(0.985 0.003 270);
  --color-tes02-side: #f3f3f7;
  --color-tes02-side: oklch(0.962 0.005 270);
  --color-tes02-card: #ffffff;
  --color-tes02-card: oklch(1 0 0);
  --color-tes02-line: #e3e3ea;
  --color-tes02-line: oklch(0.913 0.008 270);
  --color-tes02-line2: #c4c4d0;
  --color-tes02-line2: oklch(0.82 0.014 270);
  --color-tes02-ink: #1b1b26;
  --color-tes02-ink: oklch(0.22 0.02 280);
  --color-tes02-mut: #5f5f6e;
  --color-tes02-mut: oklch(0.48 0.02 280);
  --color-tes02-acc: #5b4ee8;
  --color-tes02-acc: oklch(0.53 0.21 280);
  --color-tes02-ok: #14966b;
  --color-tes02-ok: oklch(0.6 0.13 162);
  --font-tes02-sans: 'Geist', system-ui, sans-serif;
  --font-tes02-mono: 'Geist Mono', ui-monospace, monospace;
}

@property --tes02-p {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-02 {
  width: 100%;
  min-height: 100svh;
}

.tes-02 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-02');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const $ = (s) => root.querySelector(s);
  const ticks = [...root.querySelectorAll('[data-step]')];
  const copy = [
    ['Three steps and Northline is yours', 'Nothing here yet. Set the basics and your first board builds itself.'],
    ['Good start', 'Two more and the board fills with your own work.'],
    ['Almost there', 'One step left before Northline runs itself.'],
    ['Workspace ready', 'Create the project and your team lands straight in it.']
  ];
  const paint = () => {
    const done = ticks.filter((t) => t.getAttribute('aria-pressed') === 'true').length;
    $('#tes02-ring').style.setProperty('--tes02-p', (done / 3) * 360 + 'deg');
    $('#tes02-ringtext').textContent = done + '/3';
    $('#tes02-bar').style.width = (done / 3) * 100 + '%';
    $('#tes02-title').textContent = copy[done][0];
    $('#tes02-sub').textContent = copy[done][1];
    $('#tes02-setup').toggleAttribute('data-ready', done === 3);
    $('#tes02-pri').textContent = done === 3 ? 'Open your project' : 'Create your first project';
  };
  ticks.forEach((t) => t.addEventListener('click', () => {
    t.setAttribute('aria-pressed', String(t.getAttribute('aria-pressed') !== 'true'));
    paint();
  }));
  $('#tes02-reset').addEventListener('click', () => { ticks.forEach((t) => t.setAttribute('aria-pressed', 'false')); paint(); });
  paint();
})();
```

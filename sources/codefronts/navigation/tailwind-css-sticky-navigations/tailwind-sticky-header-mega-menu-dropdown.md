---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-mega-menu-dropdown/"
title: "Tailwind Sticky Header with Mega Menu Dropdown"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "A full-width, multi-column mega menu anchored under a sticky header: three product columns with icon tiles plus a featured card, a page scrim behind it, and…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Header with Mega Menu Dropdown
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-mega-menu-dropdown/

A full-width, multi-column mega menu anchored under a sticky header: three product columns with icon tiles plus a featured card, a page scrim behind it, and an entrance that fades and drops 8px. It opens on click and — on real pointers — on hover with intent delays; Escape, scrim clicks and focus leaving all close it, and the closed panel is inert.
## HTML
```html
<div class="tsn-16 group/root w-full min-h-svh bg-tsn16-bg font-tsn16-sans text-tsn16-ink antialiased" aria-label="Mega menu dropdown sticky header demo">
  <a href="#tsn-16-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn16-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn16-bg">Skip to content</a>
  <header data-tsn16-header class="sticky top-0 z-40 border-b border-tsn16-line bg-tsn16-surface">
    <div class="flex h-16 items-center gap-4 px-[max(1.25rem,calc((100%-72rem)/2))] sm:gap-8">
      <a href="#tsn-16-s1" class="flex min-h-11 flex-none items-center gap-2 rounded-lg font-semibold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn16-acc"><span aria-hidden="true" class="grid size-7 place-items-center rounded-md bg-tsn16-ink text-tsn16-surface"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="M3 9h18M8 13h8"/></svg></span>Stackline</a>
      <nav aria-label="Primary" class="flex min-w-0 items-center gap-1">
        <button type="button" data-tsn16-trigger aria-expanded="false" aria-controls="tsn-16-products" class="inline-flex min-h-11 items-center gap-1.5 rounded-full px-3.5 text-sm font-medium text-tsn16-mut transition-colors hover:text-tsn16-ink focus-visible:outline-2 focus-visible:outline-tsn16-acc aria-expanded:bg-tsn16-acc/8 aria-expanded:text-tsn16-ink">Products <svg class="size-4 transition-transform duration-300 group-data-open/root:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6"/></svg></button>
        <a href="#tsn-16-s2" class="inline-flex min-h-11 items-center rounded-full px-3.5 text-sm font-medium text-tsn16-mut hover:text-tsn16-ink focus-visible:outline-2 focus-visible:outline-tsn16-acc max-md:hidden">Customers</a>
        <a href="#tsn-16-s3" class="inline-flex min-h-11 items-center rounded-full px-3.5 text-sm font-medium text-tsn16-mut hover:text-tsn16-ink focus-visible:outline-2 focus-visible:outline-tsn16-acc max-md:hidden">Pricing</a>
        <a href="#tsn-16-s4" class="inline-flex min-h-11 items-center rounded-full px-3.5 text-sm font-medium text-tsn16-mut hover:text-tsn16-ink focus-visible:outline-2 focus-visible:outline-tsn16-acc max-md:hidden">Docs</a>
      </nav>
      <a href="#tsn-16-s3" class="ms-auto inline-flex min-h-11 flex-none items-center rounded-full bg-tsn16-acc px-4 text-sm font-semibold text-white shadow-[0_8px_20px_-8px_var(--color-tsn16-acc)] hover:bg-tsn16-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn16-acc">Deploy now</a>
    </div>
    <div id="tsn-16-products" data-tsn16-panel inert class="invisible absolute inset-x-0 top-full max-h-[calc(100svh-4rem)] -translate-y-2 overflow-y-auto border-b border-tsn16-line bg-tsn16-surface opacity-0 shadow-[0_30px_60px_-30px_rgb(15_25_60/0.35)] transition-[opacity,translate,visibility] duration-200 ease-out group-data-open/root:visible group-data-open/root:translate-y-0 group-data-open/root:opacity-100 motion-reduce:transition-none">
      <div class="grid gap-6 px-[max(1.25rem,calc((100%-72rem)/2))] py-8 md:grid-cols-3 lg:grid-cols-[1fr_1fr_1fr_17rem]">
          <div class="grid content-start gap-1">
            <p class="px-3 pb-1 font-tsn16-mono text-[11px] font-medium uppercase tracking-[0.14em] text-tsn16-mut">Build</p>
            <a href="#tsn-16-s2" class="group/it flex gap-3.5 rounded-xl p-3 transition-colors hover:bg-tsn16-acc/6 focus-visible:outline-2 focus-visible:outline-tsn16-acc">
              <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-lg border border-tsn16-line bg-tsn16-surface text-tsn16-acc transition-colors group-hover/it:border-tsn16-acc/40 group-hover/it:bg-tsn16-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg></span>
              <span class="grid gap-0.5"><span class="text-sm font-semibold">Edge Functions</span><span class="text-[13px] leading-snug text-tsn16-mut">Run code 40ms from every user.</span></span>
            </a>
            <a href="#tsn-16-s2" class="group/it flex gap-3.5 rounded-xl p-3 transition-colors hover:bg-tsn16-acc/6 focus-visible:outline-2 focus-visible:outline-tsn16-acc">
              <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-lg border border-tsn16-line bg-tsn16-surface text-tsn16-acc transition-colors group-hover/it:border-tsn16-acc/40 group-hover/it:bg-tsn16-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m8 8-5 4 5 4M16 8l5 4-5 4"/></svg></span>
              <span class="grid gap-0.5"><span class="text-sm font-semibold">Deployments</span><span class="text-[13px] leading-snug text-tsn16-mut">Preview every pull request.</span></span>
            </a>
            <a href="#tsn-16-s2" class="group/it flex gap-3.5 rounded-xl p-3 transition-colors hover:bg-tsn16-acc/6 focus-visible:outline-2 focus-visible:outline-tsn16-acc">
              <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-lg border border-tsn16-line bg-tsn16-surface text-tsn16-acc transition-colors group-hover/it:border-tsn16-acc/40 group-hover/it:bg-tsn16-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span>
              <span class="grid gap-0.5"><span class="text-sm font-semibold">Storage</span><span class="text-[13px] leading-snug text-tsn16-mut">Objects, KV and Postgres.</span></span>
            </a>
          </div>
          <div class="grid content-start gap-1">
            <p class="px-3 pb-1 font-tsn16-mono text-[11px] font-medium uppercase tracking-[0.14em] text-tsn16-mut">Observe</p>
            <a href="#tsn-16-s2" class="group/it flex gap-3.5 rounded-xl p-3 transition-colors hover:bg-tsn16-acc/6 focus-visible:outline-2 focus-visible:outline-tsn16-acc">
              <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-lg border border-tsn16-line bg-tsn16-surface text-tsn16-acc transition-colors group-hover/it:border-tsn16-acc/40 group-hover/it:bg-tsn16-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg></span>
              <span class="grid gap-0.5"><span class="text-sm font-semibold">Analytics</span><span class="text-[13px] leading-snug text-tsn16-mut">Real-user Core Web Vitals.</span></span>
            </a>
            <a href="#tsn-16-s2" class="group/it flex gap-3.5 rounded-xl p-3 transition-colors hover:bg-tsn16-acc/6 focus-visible:outline-2 focus-visible:outline-tsn16-acc">
              <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-lg border border-tsn16-line bg-tsn16-surface text-tsn16-acc transition-colors group-hover/it:border-tsn16-acc/40 group-hover/it:bg-tsn16-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/></svg></span>
              <span class="grid gap-0.5"><span class="text-sm font-semibold">Logs</span><span class="text-[13px] leading-snug text-tsn16-mut">Searchable, streamed, retained.</span></span>
            </a>
            <a href="#tsn-16-s2" class="group/it flex gap-3.5 rounded-xl p-3 transition-colors hover:bg-tsn16-acc/6 focus-visible:outline-2 focus-visible:outline-tsn16-acc">
              <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-lg border border-tsn16-line bg-tsn16-surface text-tsn16-acc transition-colors group-hover/it:border-tsn16-acc/40 group-hover/it:bg-tsn16-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg></span>
              <span class="grid gap-0.5"><span class="text-sm font-semibold">Monitoring</span><span class="text-[13px] leading-snug text-tsn16-mut">Alerts before users notice.</span></span>
            </a>
          </div>
          <div class="grid content-start gap-1">
            <p class="px-3 pb-1 font-tsn16-mono text-[11px] font-medium uppercase tracking-[0.14em] text-tsn16-mut">Secure</p>
            <a href="#tsn-16-s2" class="group/it flex gap-3.5 rounded-xl p-3 transition-colors hover:bg-tsn16-acc/6 focus-visible:outline-2 focus-visible:outline-tsn16-acc">
              <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-lg border border-tsn16-line bg-tsn16-surface text-tsn16-acc transition-colors group-hover/it:border-tsn16-acc/40 group-hover/it:bg-tsn16-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/></svg></span>
              <span class="grid gap-0.5"><span class="text-sm font-semibold">Firewall</span><span class="text-[13px] leading-snug text-tsn16-mut">Bot and DDoS protection.</span></span>
            </a>
            <a href="#tsn-16-s2" class="group/it flex gap-3.5 rounded-xl p-3 transition-colors hover:bg-tsn16-acc/6 focus-visible:outline-2 focus-visible:outline-tsn16-acc">
              <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-lg border border-tsn16-line bg-tsn16-surface text-tsn16-acc transition-colors group-hover/it:border-tsn16-acc/40 group-hover/it:bg-tsn16-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M10 14a5 5 0 0 0 7.07 0l3-3a5 5 0 0 0-7.07-7.07l-1.5 1.5"/><path d="M14 10a5 5 0 0 0-7.07 0l-3 3a5 5 0 0 0 7.07 7.07l1.5-1.5"/></svg></span>
              <span class="grid gap-0.5"><span class="text-sm font-semibold">Domains</span><span class="text-[13px] leading-snug text-tsn16-mut">Automatic TLS everywhere.</span></span>
            </a>
            <a href="#tsn-16-s2" class="group/it flex gap-3.5 rounded-xl p-3 transition-colors hover:bg-tsn16-acc/6 focus-visible:outline-2 focus-visible:outline-tsn16-acc">
              <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-lg border border-tsn16-line bg-tsn16-surface text-tsn16-acc transition-colors group-hover/it:border-tsn16-acc/40 group-hover/it:bg-tsn16-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg></span>
              <span class="grid gap-0.5"><span class="text-sm font-semibold">Access</span><span class="text-[13px] leading-snug text-tsn16-mut">SSO, roles and audit trails.</span></span>
            </a>
          </div>
        <a href="#tsn-16-s4" class="group/f relative isolate grid min-h-48 content-end overflow-hidden rounded-2xl bg-tsn16-ink p-5 text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn16-acc md:col-span-3 lg:col-span-1">
          <span aria-hidden="true" class="absolute -right-10 -top-10 -z-10 size-48 rounded-full bg-[radial-gradient(circle,var(--color-tsn16-acc),transparent_70%)] opacity-80 transition-transform duration-500 group-hover/f:scale-125"></span>
          <span class="font-tsn16-mono text-[11px] uppercase tracking-[0.14em] text-white/70">New · Ship week</span>
          <span class="mt-2 text-lg font-semibold leading-snug">Edge Functions now cold-start in 9ms</span>
          <span class="mt-3 inline-flex items-center gap-1.5 text-sm font-medium text-white/85">Read the launch post <svg class="size-4 transition-transform group-hover/f:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
        </a>
      </div>
    </div>
  </header>
  <div data-tsn16-scrim aria-hidden="true" class="pointer-events-none fixed inset-0 z-30 bg-tsn16-ink/25 opacity-0 transition-opacity duration-200 group-data-open/root:pointer-events-auto group-data-open/root:opacity-100"></div>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn16-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn16-acc">absolute inset-x-0 top-full · inert</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">A mega menu that behaves</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn16-mut text-pretty">Click — or hover, with a mouse — on <code class="rounded-md bg-tsn16-acc/10 px-1.5 py-0.5 font-tsn16-mono text-[0.86em] text-tsn16-ink">Products</code>. The panel spans the viewport under the pinned bar, dims the page, and closes on Escape, scrim click or focus leaving.</p>
  </div>
  <main id="tsn-16-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-16-s1" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn16-line bg-tsn16-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-16-h1">
      <p class="font-tsn16-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn16-acc">Platform</p>
      <h2 id="tsn-16-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Anchored to a sticky bar</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn16-mut text-pretty">A sticky header is a positioned box, so <code class="rounded-md bg-tsn16-acc/10 px-1.5 py-0.5 font-tsn16-mono text-[0.86em] text-tsn16-ink">absolute inset-x-0 top-full</code> spans its width and pins with it. No portal, no measuring.</p>
    </section>
    <section id="tsn-16-s2" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn16-line bg-tsn16-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-16-h2">
      <p class="font-tsn16-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn16-acc">Customers</p>
      <h2 id="tsn-16-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Hover is an enhancement</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn16-mut text-pretty">Clicking always works. Under <code class="rounded-md bg-tsn16-acc/10 px-1.5 py-0.5 font-tsn16-mono text-[0.86em] text-tsn16-ink">(hover: hover)</code> the menu also opens after 80ms of hovering and waits 220ms before closing, so diagonal mouse paths don’t snap it shut.</p>
    </section>
    <section id="tsn-16-s3" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn16-line bg-tsn16-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-16-h3">
      <p class="font-tsn16-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn16-acc">Pricing</p>
      <h2 id="tsn-16-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Closed means gone</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn16-mut text-pretty"><code class="rounded-md bg-tsn16-acc/10 px-1.5 py-0.5 font-tsn16-mono text-[0.86em] text-tsn16-ink">invisible</code> removes the panel from hit-testing while letting it animate; <code class="rounded-md bg-tsn16-acc/10 px-1.5 py-0.5 font-tsn16-mono text-[0.86em] text-tsn16-ink">inert</code> removes it from the tab order and the accessibility tree.</p>
    </section>
    <section id="tsn-16-s4" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn16-line bg-tsn16-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-16-h4">
      <p class="font-tsn16-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn16-acc">Docs</p>
      <h2 id="tsn-16-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Every exit works</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn16-mut text-pretty">Escape returns focus to the trigger, the scrim closes on click, and tabbing out of the header closes it too. Picking a link closes it before the jump.</p>
    </section>
  </main>
  <footer class="border-t border-tsn16-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn16-mono text-xs text-tsn16-mut">Tailwind sticky navigation · pattern 16 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn16-bg: #f5f6fa;
  --color-tsn16-bg: oklch(0.97 0.006 270);
  --color-tsn16-surface: #ffffff;
  --color-tsn16-surface: oklch(1 0 0);
  --color-tsn16-ink: #111628;
  --color-tsn16-ink: oklch(0.2 0.03 270);
  --color-tsn16-mut: #545b70;
  --color-tsn16-mut: oklch(0.46 0.03 270);
  --color-tsn16-acc: #3456f5;
  --color-tsn16-acc: oklch(0.53 0.23 268);
  --color-tsn16-line: #1116281a;
  --color-tsn16-line: oklch(0.2 0.03 270 / 0.1);
  --font-tsn16-sans: 'Geist', system-ui, sans-serif;
  --font-tsn16-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-16 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-16) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-16').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const hdr = root.querySelector('[data-tsn16-header]');
    const btn = root.querySelector('[data-tsn16-trigger]');
    const panel = root.querySelector('[data-tsn16-panel]');
    const scrim = root.querySelector('[data-tsn16-scrim]');
    let t = 0;
    const set = (open) => {
      clearTimeout(t);
      root.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      panel.inert = !open;
    };
    const isOpen = () => root.hasAttribute('data-open');
    btn.addEventListener('click', () => set(!isOpen()));
    scrim.addEventListener('click', () => set(false));
    panel.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
    root.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && isOpen()) { set(false); btn.focus(); }
    });
    hdr.addEventListener('focusout', (e) => { if (isOpen() && !hdr.contains(e.relatedTarget)) set(false); });
    if (matchMedia('(hover: hover)').matches) {
      [btn, panel].forEach((el) => {
        el.addEventListener('pointerenter', () => { clearTimeout(t); t = setTimeout(() => set(true), 80); });
        el.addEventListener('pointerleave', () => { clearTimeout(t); t = setTimeout(() => set(false), 220); });
      });
    }
  });
})();
```

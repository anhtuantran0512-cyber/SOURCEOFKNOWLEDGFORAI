---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-dark-mode-sticky-navbar-theme-toggle/"
title: "Tailwind Dark Mode Sticky Navbar with Theme Toggle"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "A Light · System · Dark switcher in a sticky header, built the v4 way: @theme inline maps every colour utility to a runtime custom property, so one attribute…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Sticky Navbar with Theme Toggle
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-dark-mode-sticky-navbar-theme-toggle/

A Light · System · Dark switcher in a sticky header, built the v4 way: @theme inline maps every colour utility to a runtime custom property, so one attribute (data-theme) re-themes the whole page with no dark: prefixes in the markup. “System” follows prefers-color-scheme live; the choice persists when storage is available.
## HTML
```html
<div class="tsn-12 w-full min-h-svh bg-tsn12-bg font-tsn12-sans text-tsn12-ink antialiased transition-colors duration-500" aria-label="Dark mode theme toggle navbar demo">
  <a href="#tsn-12-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn12-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn12-bg">Skip to content</a>
  <header class="sticky top-0 z-40 flex h-16 items-center gap-4 border-b border-tsn12-line bg-tsn12-bg/80 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-xl transition-colors duration-500 sm:gap-8">
    <a href="#tsn-12-s1" class="flex min-h-11 flex-none items-center gap-2.5 rounded-lg font-semibold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn12-acc"><span aria-hidden="true" class="size-7 rounded-full bg-[linear-gradient(135deg,var(--color-tsn12-acc)_50%,var(--color-tsn12-ink)_50%)] ring-2 ring-tsn12-line"></span>Halcyon</a>
    <nav aria-label="Primary" class="flex min-w-0 flex-1 gap-1 overflow-x-auto [scrollbar-width:none]">
      <a href="#tsn-12-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn12-mut hover:text-tsn12-ink focus-visible:outline-2 focus-visible:outline-tsn12-acc aria-[current=page]:text-tsn12-ink">Tokens</a>
      <a href="#tsn-12-s2" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn12-mut hover:text-tsn12-ink focus-visible:outline-2 focus-visible:outline-tsn12-acc">System</a>
      <a href="#tsn-12-s3" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn12-mut hover:text-tsn12-ink focus-visible:outline-2 focus-visible:outline-tsn12-acc">Contrast</a>
    </nav>
    <div role="group" aria-label="Colour theme" class="flex flex-none gap-0.5 rounded-full border border-tsn12-line bg-tsn12-ink/5 p-1">
      <button type="button" data-theme-set="light" aria-pressed="false" class="grid size-9 place-items-center rounded-full text-tsn12-mut transition hover:text-tsn12-ink focus-visible:outline-2 focus-visible:outline-tsn12-acc aria-pressed:bg-tsn12-surface aria-pressed:text-tsn12-acc aria-pressed:shadow-[0_1px_3px_rgb(0_0_0/0.15)]"><span class="sr-only">Light</span><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
      <button type="button" data-theme-set="system" aria-pressed="true" class="grid size-9 place-items-center rounded-full text-tsn12-mut transition hover:text-tsn12-ink focus-visible:outline-2 focus-visible:outline-tsn12-acc aria-pressed:bg-tsn12-surface aria-pressed:text-tsn12-acc aria-pressed:shadow-[0_1px_3px_rgb(0_0_0/0.15)]"><span class="sr-only">System</span><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg></button>
      <button type="button" data-theme-set="dark" aria-pressed="false" class="grid size-9 place-items-center rounded-full text-tsn12-mut transition hover:text-tsn12-ink focus-visible:outline-2 focus-visible:outline-tsn12-acc aria-pressed:bg-tsn12-surface aria-pressed:text-tsn12-acc aria-pressed:shadow-[0_1px_3px_rgb(0_0_0/0.15)]"><span class="sr-only">Dark</span><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></svg></button>
    </div>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn12-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn12-acc">@theme inline · data-theme</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">One attribute, two complete themes</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn12-mut text-pretty">Use the switcher in the header. Every surface, line and label re-themes — and the markup does not contain a single <code class="rounded-md bg-tsn12-acc/10 px-1.5 py-0.5 font-tsn12-mono text-[0.86em] text-tsn12-ink">dark:</code> prefix.</p>
  </div>
  <main id="tsn-12-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-12-s1" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn12-line bg-tsn12-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-12-h1">
      <p class="font-tsn12-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn12-acc">Tokens</p>
      <h2 id="tsn-12-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">@theme inline is the switch</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn12-mut text-pretty">With <code class="rounded-md bg-tsn12-acc/10 px-1.5 py-0.5 font-tsn12-mono text-[0.86em] text-tsn12-ink">inline</code>, each colour utility compiles to a <code class="rounded-md bg-tsn12-acc/10 px-1.5 py-0.5 font-tsn12-mono text-[0.86em] text-tsn12-ink">var()</code> read at runtime. Change the variable set on the root, and every utility follows.</p>
    </section>
    <section id="tsn-12-s2" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn12-line bg-tsn12-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-12-h2">
      <p class="font-tsn12-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn12-acc">System</p>
      <h2 id="tsn-12-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Three states, honestly</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn12-mut text-pretty">“System” removes <code class="rounded-md bg-tsn12-acc/10 px-1.5 py-0.5 font-tsn12-mono text-[0.86em] text-tsn12-ink">data-theme</code> and lets <code class="rounded-md bg-tsn12-acc/10 px-1.5 py-0.5 font-tsn12-mono text-[0.86em] text-tsn12-ink">prefers-color-scheme</code> decide — live, if the OS switches at sunset. Light and Dark pin a choice.</p>
    </section>
    <section id="tsn-12-s3" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn12-line bg-tsn12-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-12-h3">
      <p class="font-tsn12-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn12-acc">Contrast</p>
      <h2 id="tsn-12-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Both themes pass</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn12-mut text-pretty">Muted copy is tuned per theme: 6.1:1 on the light surface, 7.4:1 on the dark one. <code class="rounded-md bg-tsn12-acc/10 px-1.5 py-0.5 font-tsn12-mono text-[0.86em] text-tsn12-ink">color-scheme</code> tells native scrollbars to match.</p>
    </section>
    <section id="tsn-12-s4" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn12-line bg-tsn12-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-12-h4">
      <p class="font-tsn12-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn12-acc">Persistence</p>
      <h2 id="tsn-12-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Remembered when allowed</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn12-mut text-pretty">The choice is saved to <code class="rounded-md bg-tsn12-acc/10 px-1.5 py-0.5 font-tsn12-mono text-[0.86em] text-tsn12-ink">localStorage</code> inside a <code class="rounded-md bg-tsn12-acc/10 px-1.5 py-0.5 font-tsn12-mono text-[0.86em] text-tsn12-ink">try</code>, so sandboxed previews that block storage still work — they just forget on reload.</p>
    </section>
  </main>
  <footer class="border-t border-tsn12-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn12-mono text-xs text-tsn12-mut">Tailwind sticky navigation · pattern 12 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";
/* inline: utilities read the variables at runtime, so swapping the set re-themes everything. */

@theme inline {
  --color-tsn12-bg: var(--tsn12-bg);
  --color-tsn12-surface: var(--tsn12-surface);
  --color-tsn12-ink: var(--tsn12-ink);
  --color-tsn12-mut: var(--tsn12-mut);
  --color-tsn12-acc: var(--tsn12-acc);
  --color-tsn12-line: var(--tsn12-line);
  --font-tsn12-sans: 'Geist', system-ui, sans-serif;
  --font-tsn12-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract plus the light token set. */

.tsn-12 {
  width: 100%;
  min-height: 100svh;
  color-scheme: light;
  --tsn12-bg: #f3f7f7;
  --tsn12-bg: oklch(0.975 0.006 200);
  --tsn12-surface: #ffffff;
  --tsn12-surface: oklch(1 0 0);
  --tsn12-ink: #142326;
  --tsn12-ink: oklch(0.24 0.025 210);
  --tsn12-mut: #4d6064;
  --tsn12-mut: oklch(0.47 0.025 210);
  --tsn12-acc: #0b8a87;
  --tsn12-acc: oklch(0.56 0.1 190);
  --tsn12-line: #1423261a;
  --tsn12-line: oklch(0.24 0.025 210 / 0.1);
}

.tsn-12[data-theme="dark"] {
  color-scheme: dark;
  --tsn12-bg: #0d1518;
  --tsn12-bg: oklch(0.17 0.012 230);
  --tsn12-surface: #152024;
  --tsn12-surface: oklch(0.215 0.015 230);
  --tsn12-ink: #e8f1f2;
  --tsn12-ink: oklch(0.95 0.01 210);
  --tsn12-mut: #9db0b4;
  --tsn12-mut: oklch(0.75 0.02 210);
  --tsn12-acc: #4fd6cf;
  --tsn12-acc: oklch(0.8 0.12 185);
  --tsn12-line: #e8f1f21a;
  --tsn12-line: oklch(0.95 0.01 210 / 0.1);
}

@media (prefers-color-scheme: dark) {
  .tsn-12:not([data-theme="light"]) {
    color-scheme: dark;
    --tsn12-bg: #0d1518;
    --tsn12-bg: oklch(0.17 0.012 230);
    --tsn12-surface: #152024;
    --tsn12-surface: oklch(0.215 0.015 230);
    --tsn12-ink: #e8f1f2;
    --tsn12-ink: oklch(0.95 0.01 210);
    --tsn12-mut: #9db0b4;
    --tsn12-mut: oklch(0.75 0.02 210);
    --tsn12-acc: #4fd6cf;
    --tsn12-acc: oklch(0.8 0.12 185);
    --tsn12-line: #e8f1f21a;
    --tsn12-line: oklch(0.95 0.01 210 / 0.1);
  }
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-12) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-12').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const btns = [...root.querySelectorAll('[data-theme-set]')];
    const apply = (v) => {
      if (v === 'system') root.removeAttribute('data-theme');
      else root.setAttribute('data-theme', v);
      btns.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.themeSet === v)));
      try { localStorage.setItem('tsn12-theme', v); } catch (e) {}
    };
    let saved = 'system';
    try { saved = localStorage.getItem('tsn12-theme') || 'system'; } catch (e) {}
    btns.forEach((b) => b.addEventListener('click', () => apply(b.dataset.themeSet)));
    apply(saved);
  });
})();
```

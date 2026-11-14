---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/fix-tailwind-dark-mode-flash-fouc-head-script/"
title: "Fix the Dark Mode Flash (FOUC) in Tailwind CSS with an Inline Head Script"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "The fix for the most-reported dark-mode bug: the split-second white flash on reload before your theme JS runs."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fix the Dark Mode Flash (FOUC) in Tailwind CSS with an Inline Head Script
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/fix-tailwind-dark-mode-flash-fouc-head-script/

The fix for the most-reported dark-mode bug: the split-second white flash on reload before your theme JS runs. A tiny blocking script placed first in <head> reads localStorage (falling back to the OS) and stamps data-theme on <html> before the first paint — and Tailwind's custom variant picks it up from there. Upgrade: the demo now proves it, measuring “theme set” against the browser's real first-paint time.
## HTML
```html
<section data-tdm03-root class="tdm-03 grid min-h-svh w-full place-items-center bg-tdm03-bg bg-[radial-gradient(80%_55%_at_50%_0%,var(--color-tdm03-glow),transparent_70%)] px-5 py-14 font-tdm03-sans text-tdm03-text transition-colors duration-300 motion-reduce:transition-none" aria-label="Prevent dark mode flash with an inline head script demo">
  <div class="w-full max-w-[28rem] rounded-[22px] border border-tdm03-border bg-tdm03-surface p-6 shadow-[0_24px_60px_-28px_oklch(0_0_0/0.45)] transition-colors duration-300 motion-reduce:transition-none sm:p-7">
    <span class="inline-flex items-center gap-1.5 rounded-full bg-tdm03-ok/14 px-2.5 py-1 text-[11px] font-bold tracking-[0.08em] text-tdm03-ok uppercase">
      <svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>
      Loaded flicker-free
    </span>
    <h1 class="mt-4 text-[clamp(24px,4.4vw,32px)]/[1.1] font-bold tracking-[-0.02em] text-balance">No flash of white on reload</h1>
    <p class="mt-3 text-[14.5px]/[1.65] text-tdm03-muted text-pretty">This frame's theme was stamped onto <code class="rounded-md bg-tdm03-text/7 px-1.5 py-0.5 font-tdm03-mono text-[12.5px] font-semibold text-tdm03-text">&lt;html&gt;</code> by a blocking script in <code class="rounded-md bg-tdm03-text/7 px-1.5 py-0.5 font-tdm03-mono text-[12.5px] font-semibold text-tdm03-text">&lt;head&gt;</code> before a single pixel was painted. The timeline is measured live.</p>
    <div class="mt-6 rounded-2xl border border-tdm03-border bg-tdm03-bg/70 p-4">
      <div class="flex items-baseline justify-between gap-3 font-tdm03-mono text-[11.5px] text-tdm03-muted">
        <span>render timeline</span>
        <span data-tdm03-verdict aria-live="polite" class="font-semibold text-tdm03-ok">measuring…</span>
      </div>
      <div class="relative mt-4 h-2 rounded-full bg-tdm03-text/8">
        <span data-tdm03-paint-bar class="absolute inset-y-0 start-0 w-0 rounded-full bg-linear-to-r from-tdm03-accent/60 to-tdm03-text/25 transition-[width] duration-700 ease-out motion-reduce:transition-none"></span>
        <span data-tdm03-theme-mark class="absolute start-0 top-1/2 size-3.5 -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-tdm03-surface bg-tdm03-accent"></span>
        <span data-tdm03-paint-mark class="absolute start-0 top-1/2 size-3.5 -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-tdm03-surface bg-tdm03-text opacity-0 transition-opacity duration-300"></span>
      </div>
      <dl class="mt-4 grid grid-cols-2 gap-3">
        <div><dt class="flex items-center gap-1.5 text-[12px] text-tdm03-muted"><span aria-hidden="true" class="size-2 rounded-full bg-tdm03-accent"></span>Theme set</dt><dd data-tdm03-t-theme class="mt-1 font-tdm03-mono text-[15px] font-semibold">—</dd></div>
        <div><dt class="flex items-center gap-1.5 text-[12px] text-tdm03-muted"><span aria-hidden="true" class="size-2 rounded-full bg-tdm03-text"></span>First paint</dt><dd data-tdm03-t-paint class="mt-1 font-tdm03-mono text-[15px] font-semibold">—</dd></div>
      </dl>
    </div>
    <div class="mt-6 flex flex-wrap gap-2.5">
      <button type="button" data-tdm03-toggle aria-pressed="false" class="group inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl bg-tdm03-accent px-4.5 text-sm font-semibold text-tdm03-on-accent transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tdm03-accent active:scale-[0.98] motion-reduce:transition-none">
        <svg class="size-4" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5Z"/></svg>
        Dark theme
        <span aria-hidden="true" class="rounded-md bg-tdm03-on-accent/15 px-1.5 py-0.5 font-tdm03-mono text-[10.5px] group-aria-pressed:hidden">OFF</span>
        <span aria-hidden="true" class="hidden rounded-md bg-tdm03-on-accent/15 px-1.5 py-0.5 font-tdm03-mono text-[10.5px] group-aria-pressed:inline">ON</span>
      </button>
      <button type="button" data-tdm03-reload class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl border border-tdm03-border bg-tdm03-bg px-4.5 text-sm font-semibold transition hover:bg-tdm03-text/6 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm03-accent motion-reduce:transition-none">
        <svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 11a8 8 0 1 0-2.3 5.7M20 4v7h-7"/></svg>
        Reload to prove it
      </button>
    </div>
    <p class="mt-4 font-tdm03-mono text-[11.5px] text-tdm03-muted">localStorage['tdm03-theme'] = <span data-tdm03-saved class="font-semibold text-tdm03-text">…</span></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Matches when <html> (or any ancestor) carries data-theme="dark" — set by the head script. */

@custom-variant tdm03-dark (&: where([data-theme=dark], [data-theme=dark] *));

@theme inline {
  --color-tdm03-bg: var(--tdm03-bg);
  --color-tdm03-surface: var(--tdm03-surface);
  --color-tdm03-text: var(--tdm03-text);
  --color-tdm03-border: var(--tdm03-border);
  --color-tdm03-accent: var(--tdm03-accent);
  --color-tdm03-muted: color-mix(in oklab, var(--tdm03-text) 64%, var(--tdm03-bg));
  --color-tdm03-glow: color-mix(in oklab, var(--tdm03-accent) 16%, transparent);
  --color-tdm03-ok: oklch(from var(--tdm03-accent) l c 150);
  --color-tdm03-on-accent: oklch(from var(--tdm03-accent) clamp(0.17, (0.62 - l) * 1000, 1) 0 h);
}

@theme {
  --font-tdm03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tdm03-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tdm-03 {
  width: 100%;
  min-height: 100svh;
  --tdm03-bg: oklch(0.982 0.005 230);
  --tdm03-surface: oklch(1 0 0);
  --tdm03-text: oklch(0.24 0.02 240);
  --tdm03-border: oklch(0.9 0.01 235);
  --tdm03-accent: oklch(0.52 0.13 225);

  @variant tdm03-dark {
    --tdm03-bg: oklch(0.15 0.02 240);
    --tdm03-surface: oklch(0.2 0.022 240);
    --tdm03-text: oklch(0.95 0.006 240);
    --tdm03-border: oklch(0.31 0.022 240);
    --tdm03-accent: oklch(0.76 0.12 215);
  }
}
```

## JavaScript
```js
/* PART 1 — headScript (see the headScript field): FIRST thing in <head>, before any CSS.
   PART 2 — this file: the toggle and the live paint-timeline proof, loaded normally. */
(() => {
  const KEY = 'tdm03-theme';
  const html = document.documentElement;
  document.querySelectorAll('[data-tdm03-root]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const $ = (s) => root.querySelector(s);
    const btn = $('[data-tdm03-toggle]');
    const read = () => { try { return localStorage.getItem(KEY); } catch { return null; } };
    const sync = () => {
      btn.setAttribute('aria-pressed', String(html.dataset.theme === 'dark'));
      const saved = read();
      $('[data-tdm03-saved]').textContent = saved ? "'" + saved + "'" : 'not set (OS fallback)';
    };

    // safety net if the head script was missing or storage was blocked
    if (!html.dataset.theme) html.dataset.theme = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    sync();

    btn.addEventListener('click', () => {
      const next = html.dataset.theme === 'dark' ? 'light' : 'dark';
      html.dataset.theme = next;
      html.style.colorScheme = next;
      try { localStorage.setItem(KEY, next); } catch {}
      sync();
    });
    $('[data-tdm03-reload]').addEventListener('click', () => location.reload());

    // live proof: when was the theme set vs. when did the browser first paint?
    const tTheme = parseFloat(html.dataset.tdm03At);
    const fmt = (n) => n.toFixed(1) + ' ms';
    const verdict = $('[data-tdm03-verdict]');
    let done = false;
    const show = (paint) => {
      done = true;
      $('[data-tdm03-t-theme]').textContent = isNaN(tTheme) ? 'blocked' : fmt(tTheme);
      $('[data-tdm03-t-paint]').textContent = paint == null ? 'n/a' : fmt(paint);
      if (paint == null || isNaN(tTheme)) { verdict.textContent = 'paint timing unavailable'; return; }
      const scale = paint * 1.15;
      $('[data-tdm03-theme-mark]').style.insetInlineStart = (tTheme / scale * 100) + '%';
      $('[data-tdm03-paint-mark]').style.insetInlineStart = (paint / scale * 100) + '%';
      $('[data-tdm03-paint-mark]').style.opacity = '1';
      $('[data-tdm03-paint-bar]').style.width = (paint / scale * 100) + '%';
      verdict.textContent = 'theme ' + fmt(paint - tTheme) + ' before paint';
    };
    const pick = (list) => {
      const e = list.find((x) => x.name === 'first-paint') || list.find((x) => x.name === 'first-contentful-paint');
      return e ? e.startTime : null;
    };
    const now = pick(performance.getEntriesByType('paint'));
    if (now != null) return show(now);
    try {
      new PerformanceObserver((list, obs) => {
        const p = pick(list.getEntries());
        if (p != null) { obs.disconnect(); show(p); }
      }).observe({ type: 'paint', buffered: true });
    } catch {}
    setTimeout(() => { if (!done) show(null); }, 3000);
  });
})();
```

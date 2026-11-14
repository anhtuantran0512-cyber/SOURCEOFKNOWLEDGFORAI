---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-prefers-color-scheme/"
title: "Tailwind CSS Dark Mode with prefers-color-scheme (System Theme)"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "The baseline every other pattern builds on: the UI simply obeys the operating system."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Dark Mode with prefers-color-scheme (System Theme)
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-prefers-color-scheme/

The baseline every other pattern builds on: the UI simply obeys the operating system. Each colour token is declared once in @theme as a light-dark() pair, and one utility — scheme-light-dark — hands the choice to the OS. Three panels render identical markup: a scheme-light reference, a scheme-dark reference, and a live panel that follows your system right now.
## HTML
```html
<div class="tdm-01 w-full min-h-svh bg-tdm01-bg bg-[radial-gradient(90%_60%_at_50%_-10%,var(--color-tdm01-glow),transparent_70%)] font-tdm01-sans text-tdm01-ink antialiased scheme-light-dark">
  <!-- Pair with: <meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff">
                  <meta name="theme-color" media="(prefers-color-scheme: dark)"  content="#09090b"> -->
  <div class="mx-auto grid min-h-svh max-w-6xl content-center gap-8 px-5 py-14 sm:px-10">
    <header class="flex flex-wrap items-end justify-between gap-5">
      <div class="grid gap-2.5">
        <p class="font-tdm01-mono text-[11px] uppercase tracking-[0.16em] text-tdm01-acc">prefers-color-scheme · scheme-light-dark</p>
        <h1 class="text-[clamp(1.75rem,3.6vw,2.6rem)] font-semibold tracking-[-0.04em] text-balance">One token set, three renderings</h1>
        <p class="max-w-[60ch] text-[15px]/relaxed text-pretty text-tdm01-mut">Every colour is a <code class="font-tdm01-mono text-[13px] text-tdm01-ink">light-dark()</code> pair in <code class="font-tdm01-mono text-[13px] text-tdm01-ink">@theme</code>. The reference panels pin their scheme; the live panel inherits it from your operating system.</p>
      </div>
      <p class="inline-flex min-h-10 items-center gap-2 rounded-full border border-tdm01-line bg-tdm01-surface px-4 font-tdm01-mono text-xs text-tdm01-mut">
        <svg class="size-4 text-tdm01-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8.5 20.5h7M12 17v3.5"/></svg>
        Your OS reports <strong class="font-semibold text-tdm01-ink dark:hidden">light</strong><strong class="hidden font-semibold text-tdm01-ink dark:inline">dark</strong>
      </p>
    </header>

    <div class="grid grid-cols-[repeat(auto-fit,minmax(16.5rem,1fr))] gap-4">
      <section class="scheme-light grid content-start gap-3 rounded-[22px] border border-tdm01-line bg-tdm01-surface p-3 text-tdm01-ink " aria-label="Forced light">
        <p class="flex items-center justify-between gap-2 px-1.5 pt-1 font-tdm01-mono text-[11px] uppercase tracking-[0.1em] text-tdm01-mut"><span>Forced light</span><code class="normal-case tracking-normal text-tdm01-acc">scheme-light</code></p>
        <article class="grid gap-2.5 rounded-2xl border border-tdm01-line bg-tdm01-raised p-4 shadow-tdm01-card">
          <div class="flex items-center gap-2">
            <span class="size-2 rounded-full bg-tdm01-dot ring-4 ring-tdm01-dot/20" aria-hidden="true"></span>
            <span class="font-tdm01-mono text-[11px] uppercase tracking-[0.1em] text-tdm01-mut">Deploy · Ready</span>
          </div>
          <h2 class="font-tdm01-mono text-[17px] font-semibold tracking-tight">edge-runtime v4.2</h2>
          <p class="text-sm/relaxed text-pretty text-tdm01-mut">Promoted to production 14 minutes ago by Alex Chen.</p>
          <div class="mt-1 flex items-center justify-between gap-3">
            <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tdm01-acc px-4 text-sm font-medium text-tdm01-acc-ink transition duration-200 hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm01-focus motion-reduce:transition-none forced-colors:border forced-colors:border-[ButtonText]">View build <svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 5.5l6.5 6.5-6.5 6.5"/></svg></button>
            <span class="font-tdm01-mono text-xs text-tdm01-mut">iad1</span>
          </div>
        </article>
      </section>
      <section class="scheme-dark grid content-start gap-3 rounded-[22px] border border-tdm01-line bg-tdm01-surface p-3 text-tdm01-ink " aria-label="Forced dark">
        <p class="flex items-center justify-between gap-2 px-1.5 pt-1 font-tdm01-mono text-[11px] uppercase tracking-[0.1em] text-tdm01-mut"><span>Forced dark</span><code class="normal-case tracking-normal text-tdm01-acc">scheme-dark</code></p>
        <article class="grid gap-2.5 rounded-2xl border border-tdm01-line bg-tdm01-raised p-4 shadow-tdm01-card">
          <div class="flex items-center gap-2">
            <span class="size-2 rounded-full bg-tdm01-dot ring-4 ring-tdm01-dot/20" aria-hidden="true"></span>
            <span class="font-tdm01-mono text-[11px] uppercase tracking-[0.1em] text-tdm01-mut">Deploy · Ready</span>
          </div>
          <h2 class="font-tdm01-mono text-[17px] font-semibold tracking-tight">edge-runtime v4.2</h2>
          <p class="text-sm/relaxed text-pretty text-tdm01-mut">Promoted to production 14 minutes ago by Alex Chen.</p>
          <div class="mt-1 flex items-center justify-between gap-3">
            <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tdm01-acc px-4 text-sm font-medium text-tdm01-acc-ink transition duration-200 hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm01-focus motion-reduce:transition-none forced-colors:border forced-colors:border-[ButtonText]">View build <svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 5.5l6.5 6.5-6.5 6.5"/></svg></button>
            <span class="font-tdm01-mono text-xs text-tdm01-mut">iad1</span>
          </div>
        </article>
      </section>
      <section class=" grid content-start gap-3 rounded-[22px] border border-tdm01-line bg-tdm01-surface p-3 text-tdm01-ink ring-2 ring-tdm01-acc/45 ring-offset-4 ring-offset-tdm01-bg" aria-label="Live · your OS">
        <p class="flex items-center justify-between gap-2 px-1.5 pt-1 font-tdm01-mono text-[11px] uppercase tracking-[0.1em] text-tdm01-mut"><span>Live · your OS</span><code class="normal-case tracking-normal text-tdm01-acc">inherited</code></p>
        <article class="grid gap-2.5 rounded-2xl border border-tdm01-line bg-tdm01-raised p-4 shadow-tdm01-card">
          <div class="flex items-center gap-2">
            <span class="size-2 rounded-full bg-tdm01-dot ring-4 ring-tdm01-dot/20" aria-hidden="true"></span>
            <span class="font-tdm01-mono text-[11px] uppercase tracking-[0.1em] text-tdm01-mut">Deploy · Ready</span>
          </div>
          <h2 class="font-tdm01-mono text-[17px] font-semibold tracking-tight">edge-runtime v4.2</h2>
          <p class="text-sm/relaxed text-pretty text-tdm01-mut">Promoted to production 14 minutes ago by Alex Chen.</p>
          <div class="mt-1 flex items-center justify-between gap-3">
            <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tdm01-acc px-4 text-sm font-medium text-tdm01-acc-ink transition duration-200 hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdm01-focus motion-reduce:transition-none forced-colors:border forced-colors:border-[ButtonText]">View build <svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 5.5l6.5 6.5-6.5 6.5"/></svg></button>
            <span class="font-tdm01-mono text-xs text-tdm01-mut">iad1</span>
          </div>
        </article>
      </section>
    </div>

    <aside class="grid gap-4 rounded-[22px] border border-tdm01-line bg-tdm01-surface p-5 sm:p-6">
      <h3 class="text-[15px] font-semibold tracking-tight">What one token flips — swatches drawn by the tokens themselves</h3>
      <dl class="grid gap-2 sm:grid-cols-2">
        <div class="grid grid-cols-[5.5rem_1fr] items-center gap-3 rounded-xl border border-tdm01-line bg-tdm01-bg px-3 py-2.5">
          <dt class="font-tdm01-mono text-[13px] text-tdm01-acc">bg</dt>
          <dd class="flex flex-wrap items-center gap-2 font-tdm01-mono text-xs text-tdm01-mut"><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-bg scheme-light"></span>#ffffff<span class="px-1 text-tdm01-ink" aria-hidden="true">→</span><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-bg scheme-dark"></span>#09090b</dd>
        </div>
        <div class="grid grid-cols-[5.5rem_1fr] items-center gap-3 rounded-xl border border-tdm01-line bg-tdm01-bg px-3 py-2.5">
          <dt class="font-tdm01-mono text-[13px] text-tdm01-acc">surface</dt>
          <dd class="flex flex-wrap items-center gap-2 font-tdm01-mono text-xs text-tdm01-mut"><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-surface scheme-light"></span>#f6f6f7<span class="px-1 text-tdm01-ink" aria-hidden="true">→</span><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-surface scheme-dark"></span>#121216</dd>
        </div>
        <div class="grid grid-cols-[5.5rem_1fr] items-center gap-3 rounded-xl border border-tdm01-line bg-tdm01-bg px-3 py-2.5">
          <dt class="font-tdm01-mono text-[13px] text-tdm01-acc">ink</dt>
          <dd class="flex flex-wrap items-center gap-2 font-tdm01-mono text-xs text-tdm01-mut"><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-ink scheme-light"></span>#0a0a0b<span class="px-1 text-tdm01-ink" aria-hidden="true">→</span><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-ink scheme-dark"></span>#f4f4f5</dd>
        </div>
        <div class="grid grid-cols-[5.5rem_1fr] items-center gap-3 rounded-xl border border-tdm01-line bg-tdm01-bg px-3 py-2.5">
          <dt class="font-tdm01-mono text-[13px] text-tdm01-acc">line</dt>
          <dd class="flex flex-wrap items-center gap-2 font-tdm01-mono text-xs text-tdm01-mut"><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-line scheme-light"></span>#e3e3e7<span class="px-1 text-tdm01-ink" aria-hidden="true">→</span><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-line scheme-dark"></span>#26262c</dd>
        </div>
        <div class="grid grid-cols-[5.5rem_1fr] items-center gap-3 rounded-xl border border-tdm01-line bg-tdm01-bg px-3 py-2.5">
          <dt class="font-tdm01-mono text-[13px] text-tdm01-acc">acc</dt>
          <dd class="flex flex-wrap items-center gap-2 font-tdm01-mono text-xs text-tdm01-mut"><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-acc scheme-light"></span>#4f46e5<span class="px-1 text-tdm01-ink" aria-hidden="true">→</span><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-acc scheme-dark"></span>#8b8bff</dd>
        </div>
        <div class="grid grid-cols-[5.5rem_1fr] items-center gap-3 rounded-xl border border-tdm01-line bg-tdm01-bg px-3 py-2.5">
          <dt class="font-tdm01-mono text-[13px] text-tdm01-acc">dot</dt>
          <dd class="flex flex-wrap items-center gap-2 font-tdm01-mono text-xs text-tdm01-mut"><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-dot scheme-light"></span>#16a34a<span class="px-1 text-tdm01-ink" aria-hidden="true">→</span><span class="size-4 rounded-md border border-tdm01-line bg-tdm01-dot scheme-dark"></span>#4ade80</dd>
        </div>
      </dl>
      <p class="max-w-[68ch] text-[13.5px]/relaxed text-pretty text-tdm01-mut">No toggle ships here on purpose — this is the pure OS-driven baseline. Each pair of swatches is the <em>same</em> utility, <code class="font-tdm01-mono text-tdm01-ink">bg-tdm01-*</code>, under <code class="font-tdm01-mono text-tdm01-ink">scheme-light</code> and <code class="font-tdm01-mono text-tdm01-ink">scheme-dark</code>.</p>
    </aside>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm01-bg: light-dark(#ffffff, #09090b);
  --color-tdm01-glow: light-dark(#eef0ff, #15153a);
  --color-tdm01-surface: light-dark(#f6f6f7, #121216);
  --color-tdm01-raised: light-dark(#ffffff, #18181d);
  --color-tdm01-ink: light-dark(#0a0a0b, #f4f4f5);
  --color-tdm01-mut: light-dark(#55595f, #a1a1aa);
  --color-tdm01-line: light-dark(#e3e3e7, #27272d);
  --color-tdm01-acc: light-dark(#4f46e5, #8b8bff);
  --color-tdm01-acc-ink: light-dark(#ffffff, #0a0a12);
  --color-tdm01-focus: light-dark(#4f46e5, #a5b4fc);
  --color-tdm01-dot: light-dark(#16a34a, #4ade80);
  --shadow-tdm01-card: 0 1px 2px light-dark(rgb(9 9 11 / .08), rgb(0 0 0 / .5)), 0 18px 36px -24px light-dark(rgb(9 9 11 / .22), rgb(0 0 0 / .9));
  --font-tdm01-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm01-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```

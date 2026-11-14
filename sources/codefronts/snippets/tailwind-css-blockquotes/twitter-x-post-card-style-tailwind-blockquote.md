---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/twitter-x-post-card-style-tailwind-blockquote/"
title: "Twitter / X Post Card Style Tailwind Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A lightweight social-post embed: a styled <blockquote cite> instead of a 100KB third-party iframe."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Twitter / X Post Card Style Tailwind Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/twitter-x-post-card-style-tailwind-blockquote/

A lightweight social-post embed: a styled <blockquote cite> instead of a 100KB third-party iframe. The port adds a working, accessible like toggle — aria-pressed drives the pink fill through aria-pressed: and group-aria-pressed/act: variants — and extends the relative timestamp to months.
## HTML
```html
<section class="tbq-19 w-full min-h-svh grid place-items-center bg-tbq19-bg bg-[radial-gradient(70%_55%_at_50%_0%,var(--color-tbq19-glow),transparent)] px-5 py-14 font-tbq19-sans text-tbq19-ink" aria-label="Social post card blockquote demo">
  <div class="grid w-full justify-items-center gap-7">
    <blockquote class="w-full max-w-[500px] rounded-2xl border border-tbq19-line bg-tbq19-card px-5 pt-4.5 pb-2 shadow-[0_24px_50px_-20px_oklch(0_0_0/0.6)]" cite="https://example.social/webfoundry/status/91442">
      <header class="grid grid-cols-[auto_1fr_auto] items-center gap-3">
        <img class="size-11 rounded-full bg-linear-135 from-tbq19-av1 to-tbq19-av2 object-cover" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=120&auto=format&fit=crop" alt="" width="44" height="44" loading="lazy">
        <div class="min-w-0">
          <p class="flex items-center gap-1 text-[15px] font-bold"><span class="truncate">Web Foundry</span><svg class="size-[1.15em] flex-none text-tbq19-blue" viewBox="0 0 22 22" role="img" aria-label="Verified account"><path d="M11 1.6l2.4 1.8 3-.2 1 2.9 2.5 1.6-.9 2.9.9 2.9-2.5 1.6-1 2.9-3-.2-2.4 1.8-2.4-1.8-3 .2-1-2.9L2.1 14l.9-2.9-.9-2.9 2.5-1.6 1-2.9 3 .2z" fill="currentColor"/><path d="M7.4 11.2l2.5 2.5 4.7-5" fill="none" stroke="oklch(0.16 0.01 250)" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></p>
          <p class="text-[13.5px] text-tbq19-mut">@webfoundry</p>
        </div>
        <span aria-hidden="true" class="self-start text-[15px] text-tbq19-mut">✕</span>
      </header>
      <p class="mt-3 text-[15.5px] leading-[1.55] text-pretty">Hot take: the fastest social embed is no embed. A styled &lt;blockquote&gt; with a cite link loads in 3KB, ships zero trackers, and your CLS graph goes flat. The official script is a 100KB iframe you're renting.</p>
      <footer class="mt-3">
        <a class="inline-flex min-h-11 items-center rounded text-[13px] text-tbq19-mut no-underline hover:text-tbq19-ink hover:underline focus-visible:text-tbq19-ink focus-visible:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tbq19-blue" href="https://example.social/webfoundry/status/91442" data-tbq19-time="2026-08-05T09:14:00Z">9:14 AM · Aug 5, 2026</a>
        <ul class="mt-1 flex max-w-[320px] justify-between border-t border-tbq19-line pt-1" aria-label="Engagement">
          <li><button type="button" class="group/act flex min-h-11 cursor-pointer items-center gap-1.5 rounded-full px-2.5 text-[13px] tabular-nums text-tbq19-mut transition-colors duration-200 hover:bg-tbq19-blue/12 hover:text-tbq19-blue focus-visible:bg-tbq19-blue/12 focus-visible:text-tbq19-blue focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tbq19-blue"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 3.5c-4.9 0-8.8 3.4-8.8 7.7 0 4.2 3.9 7.6 8.8 7.6.6 0 1.2 0 1.7-.1l4.6 2.3-1-3.9c2.1-1.4 3.5-3.5 3.5-5.9 0-4.3-3.9-7.7-8.8-7.7z" fill="none" stroke="currentColor" stroke-width="1.7"/></svg><span class="sr-only">Replies: </span>612</button></li>
          <li><button type="button" class="group/act flex min-h-11 cursor-pointer items-center gap-1.5 rounded-full px-2.5 text-[13px] tabular-nums text-tbq19-mut transition-colors duration-200 hover:bg-tbq19-green/12 hover:text-tbq19-green focus-visible:bg-tbq19-green/12 focus-visible:text-tbq19-green focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tbq19-green"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M7 5.5h7a3 3 0 0 1 3 3v2M17 18.5h-7a3 3 0 0 1-3-3v-2" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M14.5 3l3 2.5-3 2.5M9.5 21l-3-2.5 3-2.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="sr-only">Reposts: </span>2,148</button></li>
          <li><button type="button" aria-pressed="false" data-tbq19-like class="group/act flex min-h-11 cursor-pointer items-center gap-1.5 rounded-full px-2.5 text-[13px] tabular-nums text-tbq19-mut transition-colors duration-200 hover:bg-tbq19-pink/12 hover:text-tbq19-pink focus-visible:bg-tbq19-pink/12 focus-visible:text-tbq19-pink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tbq19-pink aria-pressed:text-tbq19-pink"><svg class="transition-transform duration-200 group-aria-pressed/act:scale-110 group-aria-pressed/act:fill-current motion-reduce:transition-none" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="none"><path d="M12 20s-7.5-4.6-9.3-9.3C1.5 7.5 3.6 4.5 6.7 4.5c2 0 3.7 1.1 4.6 2.8h1.4c.9-1.7 2.6-2.8 4.6-2.8 3.1 0 5.2 3 4 6.2C19.5 15.4 12 20 12 20z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg><span class="sr-only">Like, </span><span data-count>9,802</span></button></li>
        </ul>
      </footer>
    </blockquote>
    <p aria-hidden="true" class="rounded-full border border-tbq19-line px-3.5 py-2 font-tbq19-mono text-[11.5px] text-tbq19-mut">3KB vs 100KB embed · aria-pressed: variants · tabular-nums</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq19-bg: #0f141a;
  --color-tbq19-bg: oklch(0.19 0.015 250);
  --color-tbq19-glow: #142030b3;
  --color-tbq19-glow: oklch(0.24 0.035 255 / 0.7);
  --color-tbq19-card: #0a0e11;
  --color-tbq19-card: oklch(0.16 0.01 250);
  --color-tbq19-ink: #eceff2;
  --color-tbq19-ink: oklch(0.95 0.005 250);
  --color-tbq19-mut: #989fa8;
  --color-tbq19-mut: oklch(0.7 0.015 250);
  --color-tbq19-line: #2d343a;
  --color-tbq19-line: oklch(0.32 0.015 250);
  --color-tbq19-blue: #37a8ec;
  --color-tbq19-blue: oklch(0.7 0.14 240);
  --color-tbq19-green: #43c07a;
  --color-tbq19-green: oklch(0.72 0.15 155);
  --color-tbq19-pink: #f7619a;
  --color-tbq19-pink: oklch(0.7 0.19 0);
  --color-tbq19-av1: #1f6a96;
  --color-tbq19-av1: oklch(0.5 0.1 240);
  --color-tbq19-av2: #404272;
  --color-tbq19-av2: oklch(0.4 0.08 280);
  --font-tbq19-sans: 'Geist', system-ui, sans-serif;
  --font-tbq19-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-19 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const rtf = new Intl.RelativeTimeFormat(undefined, { numeric: 'auto' });
  document.querySelectorAll('[data-tbq19-time]').forEach((a) => {
    if (a.dataset.wired) return;
    a.dataset.wired = '1';
    const then = new Date(a.dataset.tbq19Time).getTime();
    if (Number.isNaN(then)) return;
    const mins = Math.round((then - Date.now()) / 60000), abs = Math.abs(mins);
    const [v, u] = abs < 60 ? [mins, 'minute'] : abs < 1440 ? [Math.round(mins / 60), 'hour']
      : abs < 43200 ? [Math.round(mins / 1440), 'day'] : [Math.round(mins / 43200), 'month'];
    a.textContent = rtf.format(v, u) + ' · ' + a.textContent;
  });
  document.querySelectorAll('[data-tbq19-like]').forEach((b) => {
    if (b.dataset.wired) return;
    b.dataset.wired = '1';
    const out = b.querySelector('[data-count]');
    const base = parseInt(out.textContent.replace(/\D/g, ''), 10);
    b.addEventListener('click', () => {
      const on = b.getAttribute('aria-pressed') !== 'true';
      b.setAttribute('aria-pressed', String(on));
      out.textContent = (base + (on ? 1 : 0)).toLocaleString();
    });
  });
})();
```

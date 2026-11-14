---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/tailwind-blockquote-one-click-copy-button/"
title: "Tailwind Blockquote with One-Click Copy Button"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A quote card with a copy button that fades in on hover or focus, flips to a green “Copied” state, and announces success through a polite live region."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Blockquote with One-Click Copy Button
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/tailwind-blockquote-one-click-copy-button/

A quote card with a copy button that fades in on hover or focus, flips to a green “Copied” state, and announces success through a polite live region. The port drives the copied state with a data-copied attribute and v4's bare data-copied: variant, keeps the button always visible on touch (pointer-coarse:), and adds an execCommand fallback for iframes where the Clipboard API is blocked.
## HTML
```html
<section class="tbq-25 w-full min-h-svh grid place-items-center bg-tbq25-bg bg-[radial-gradient(75%_60%_at_50%_0%,var(--color-tbq25-glow),transparent)] px-5 py-14 font-tbq25-sans text-tbq25-ink" aria-label="Blockquote with one-click copy button demo">
  <div class="grid w-full justify-items-center gap-7">
    <figure data-tbq25-card class="group relative w-full max-w-[540px] rounded-[18px] border border-white/10 bg-tbq25-card p-[clamp(26px,4vw,36px)] shadow-[0_22px_54px_oklch(0_0_0/0.4)]">
      <div class="mb-3 flex items-start justify-between gap-3">
        <span aria-hidden="true" class="h-9 font-tbq25-serif text-[64px] leading-[0.9] text-tbq25-acc">“</span>
        <button type="button" data-copy class="group/btn inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-[10px] border border-white/16 bg-white/6 px-3.5 text-[12.5px] font-semibold text-tbq25-quiet opacity-0 transition-[opacity,background-color,border-color,color] duration-200 group-hover:opacity-100 group-focus-within:opacity-100 hover:bg-white/12 hover:text-tbq25-ink focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tbq25-acc pointer-coarse:opacity-100 data-copied:border-tbq25-ok/55 data-copied:bg-tbq25-ok/16 data-copied:text-tbq25-ok data-copied:opacity-100">
          <svg class="group-data-copied/btn:hidden" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><rect x="5.2" y="5.2" width="8.2" height="8.2" rx="1.6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10.8 5.2V4a1.6 1.6 0 0 0-1.6-1.6H4A1.6 1.6 0 0 0 2.4 4v5.2A1.6 1.6 0 0 0 4 10.8h1.2" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
          <svg class="hidden group-data-copied/btn:block" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M2.8 8.6l3.4 3.4 7-7.6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span class="group-data-copied/btn:hidden">Copy quote</span>
          <span class="hidden group-data-copied/btn:inline">Copied</span>
        </button>
      </div>
      <blockquote>
        <p class="font-tbq25-serif text-[clamp(21px,2.9vw,27px)] leading-[1.45] italic text-tbq25-ink text-pretty">Programs must be written for people to read, and only incidentally for machines to execute.</p>
      </blockquote>
      <figcaption class="mt-4 text-[13px] text-tbq25-mut">Harold Abelson, <cite class="italic text-tbq25-quiet">Structure and Interpretation of Computer Programs</cite></figcaption>
      <span role="status" aria-live="polite" class="sr-only"></span>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-white/14 px-3.5 py-2 font-tbq25-mono text-[11.5px] text-tbq25-mut">data-copied: variant · clipboard + fallback · pointer-coarse: visible</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq25-bg: #0f171f;
  --color-tbq25-bg: oklch(0.2 0.02 250);
  --color-tbq25-glow: #0c2a39b3;
  --color-tbq25-glow: oklch(0.27 0.045 235 / 0.7);
  --color-tbq25-card: #1a222c;
  --color-tbq25-card: oklch(0.25 0.022 252);
  --color-tbq25-ink: #eef2f7;
  --color-tbq25-ink: oklch(0.96 0.008 250);
  --color-tbq25-quiet: #c7cfd7;
  --color-tbq25-quiet: oklch(0.85 0.015 250);
  --color-tbq25-mut: #9ba6b1;
  --color-tbq25-mut: oklch(0.72 0.02 250);
  --color-tbq25-acc: #00c0d8;
  --color-tbq25-acc: oklch(0.74 0.13 210);
  --color-tbq25-ok: #61cb7c;
  --color-tbq25-ok: oklch(0.76 0.15 150);
  --font-tbq25-serif: 'Newsreader', Georgia, serif;
  --font-tbq25-sans: 'Geist', system-ui, sans-serif;
  --font-tbq25-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-25 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const copyText = async (text) => {
    try { await navigator.clipboard.writeText(text); return true; }
    catch {
      const ta = Object.assign(document.createElement('textarea'), { value: text });
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;opacity:0';
      document.body.append(ta);
      ta.select();
      const ok = document.execCommand('copy');
      ta.remove();
      return ok;
    }
  };
  document.querySelectorAll('[data-tbq25-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const btn = card.querySelector('[data-copy]');
    const status = card.querySelector('[role="status"]');
    let t = 0;
    btn.addEventListener('click', async () => {
      const text = '\u201C' + card.querySelector('blockquote').textContent.trim() + '\u201D \u2014 ' + card.querySelector('figcaption').textContent.trim();
      const ok = await copyText(text);
      clearTimeout(t);
      if (ok) { btn.setAttribute('data-copied', ''); status.textContent = 'Quote copied to clipboard'; }
      else status.textContent = 'Copy failed \u2014 select the text instead';
      t = setTimeout(() => { btn.removeAttribute('data-copied'); status.textContent = ''; }, 1800);
    });
  });
})();
```

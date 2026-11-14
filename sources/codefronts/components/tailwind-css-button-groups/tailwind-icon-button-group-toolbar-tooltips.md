---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-icon-button-group-toolbar-tooltips/"
title: "Tailwind Icon Button Group Toolbar with Tooltips (Rich Text Editor)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A rich-text formatting toolbar: icon buttons with CSS-only tooltips (after:content-[attr(data-tip)]) that also appear on keyboard focus, real toggle state…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Icon Button Group Toolbar with Tooltips (Rich Text Editor)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-icon-button-group-toolbar-tooltips/

A rich-text formatting toolbar: icon buttons with CSS-only tooltips (after:content-[attr(data-tip)]) that also appear on keyboard focus, real toggle state via aria-pressed:, and a sample paragraph that previews bold, italic and underline as you press them. A short controller adds toolbar arrow-key navigation and the toggles themselves.
## HTML
```html
<section class="tbg-07 w-full min-h-svh grid place-items-center bg-tbg07-bg bg-linear-150 from-tbg07-bg to-tbg07-bg2 px-5 py-14 font-tbg07-sans text-tbg07-ink" aria-label="Icon button group toolbar demo">
  <div class="group/ed w-full max-w-[34rem] rounded-2xl bg-tbg07-bar shadow-tbg07-lift">
    <div data-tbg07-bar role="toolbar" aria-label="Text formatting" class="flex flex-wrap items-center gap-0.5 border-b border-tbg07-line p-1.5">
      <button type="button" data-cmd="bold" aria-label="Bold" aria-pressed="true" data-tip="Bold · ⌘B" tabindex="0" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg07-mut transition-colors hover:bg-tbg07-hover hover:text-tbg07-ink aria-pressed:bg-tbg07-acc aria-pressed:text-tbg07-on focus-visible:z-1 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg07-acc-d before:pointer-events-none before:absolute before:bottom-[calc(100%+4px)] before:left-1/2 before:-translate-x-1/2 before:border-[5px] before:border-transparent before:border-t-tbg07-ink before:opacity-0 before:transition-opacity before:content-[''] hover:before:opacity-100 focus-visible:before:opacity-100 after:pointer-events-none after:absolute after:bottom-[calc(100%+14px)] after:left-1/2 after:-translate-x-1/2 after:rounded-lg after:bg-tbg07-ink after:px-2.5 after:py-1.5 after:text-xs after:font-semibold after:whitespace-nowrap after:text-tbg07-tip after:opacity-0 after:transition-[opacity,translate] after:content-[attr(data-tip)] hover:after:-translate-y-0.5 hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:after:transition-none"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" aria-hidden="true"><path d="M7 5h6a3.5 3.5 0 0 1 0 7H7zM7 12h7a3.5 3.5 0 0 1 0 7H7z"/></svg></button>
      <button type="button" data-cmd="italic" aria-label="Italic" aria-pressed="false" data-tip="Italic · ⌘I" tabindex="-1" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg07-mut transition-colors hover:bg-tbg07-hover hover:text-tbg07-ink aria-pressed:bg-tbg07-acc aria-pressed:text-tbg07-on focus-visible:z-1 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg07-acc-d before:pointer-events-none before:absolute before:bottom-[calc(100%+4px)] before:left-1/2 before:-translate-x-1/2 before:border-[5px] before:border-transparent before:border-t-tbg07-ink before:opacity-0 before:transition-opacity before:content-[''] hover:before:opacity-100 focus-visible:before:opacity-100 after:pointer-events-none after:absolute after:bottom-[calc(100%+14px)] after:left-1/2 after:-translate-x-1/2 after:rounded-lg after:bg-tbg07-ink after:px-2.5 after:py-1.5 after:text-xs after:font-semibold after:whitespace-nowrap after:text-tbg07-tip after:opacity-0 after:transition-[opacity,translate] after:content-[attr(data-tip)] hover:after:-translate-y-0.5 hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:after:transition-none"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M15 5h-5M14 19H9M14 5l-4 14"/></svg></button>
      <button type="button" data-cmd="underline" aria-label="Underline" aria-pressed="false" data-tip="Underline · ⌘U" tabindex="-1" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg07-mut transition-colors hover:bg-tbg07-hover hover:text-tbg07-ink aria-pressed:bg-tbg07-acc aria-pressed:text-tbg07-on focus-visible:z-1 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg07-acc-d before:pointer-events-none before:absolute before:bottom-[calc(100%+4px)] before:left-1/2 before:-translate-x-1/2 before:border-[5px] before:border-transparent before:border-t-tbg07-ink before:opacity-0 before:transition-opacity before:content-[''] hover:before:opacity-100 focus-visible:before:opacity-100 after:pointer-events-none after:absolute after:bottom-[calc(100%+14px)] after:left-1/2 after:-translate-x-1/2 after:rounded-lg after:bg-tbg07-ink after:px-2.5 after:py-1.5 after:text-xs after:font-semibold after:whitespace-nowrap after:text-tbg07-tip after:opacity-0 after:transition-[opacity,translate] after:content-[attr(data-tip)] hover:after:-translate-y-0.5 hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:after:transition-none"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M7 4v7a5 5 0 0 0 10 0V4M6 20h12"/></svg></button>
      <span aria-hidden="true" class="mx-1.5 h-6 w-px bg-tbg07-line"></span>
      <button type="button" data-cmd="link" aria-label="Insert link" data-tip="Link · ⌘K" tabindex="-1" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg07-mut transition-colors hover:bg-tbg07-hover hover:text-tbg07-ink focus-visible:z-1 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg07-acc-d before:pointer-events-none before:absolute before:bottom-[calc(100%+4px)] before:left-1/2 before:-translate-x-1/2 before:border-[5px] before:border-transparent before:border-t-tbg07-ink before:opacity-0 before:transition-opacity before:content-[''] hover:before:opacity-100 focus-visible:before:opacity-100 after:pointer-events-none after:absolute after:bottom-[calc(100%+14px)] after:left-1/2 after:-translate-x-1/2 after:rounded-lg after:bg-tbg07-ink after:px-2.5 after:py-1.5 after:text-xs after:font-semibold after:whitespace-nowrap after:text-tbg07-tip after:opacity-0 after:transition-[opacity,translate] after:content-[attr(data-tip)] hover:after:-translate-y-0.5 hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:after:transition-none"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M10 13a4 4 0 0 0 5.7.6l2.6-2.6a4 4 0 0 0-5.6-5.7l-1.5 1.5M14 11a4 4 0 0 0-5.7-.6L5.7 13a4 4 0 0 0 5.6 5.7l1.5-1.5"/></svg></button>
      <button type="button" data-cmd="code" aria-label="Inline code" aria-pressed="false" data-tip="Code · ⌘E" tabindex="-1" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg07-mut transition-colors hover:bg-tbg07-hover hover:text-tbg07-ink aria-pressed:bg-tbg07-acc aria-pressed:text-tbg07-on focus-visible:z-1 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg07-acc-d before:pointer-events-none before:absolute before:bottom-[calc(100%+4px)] before:left-1/2 before:-translate-x-1/2 before:border-[5px] before:border-transparent before:border-t-tbg07-ink before:opacity-0 before:transition-opacity before:content-[''] hover:before:opacity-100 focus-visible:before:opacity-100 after:pointer-events-none after:absolute after:bottom-[calc(100%+14px)] after:left-1/2 after:-translate-x-1/2 after:rounded-lg after:bg-tbg07-ink after:px-2.5 after:py-1.5 after:text-xs after:font-semibold after:whitespace-nowrap after:text-tbg07-tip after:opacity-0 after:transition-[opacity,translate] after:content-[attr(data-tip)] hover:after:-translate-y-0.5 hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:after:transition-none"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 8l-5 4 5 4M15 8l5 4-5 4"/></svg></button>
      <span aria-hidden="true" class="mx-1.5 h-6 w-px bg-tbg07-line"></span>
      <button type="button" data-cmd="clear" aria-label="Clear formatting" data-tip="Clear formatting" tabindex="-1" class="relative grid size-11 cursor-pointer place-items-center rounded-xl text-tbg07-mut transition-colors hover:bg-tbg07-hover hover:text-tbg07-ink focus-visible:z-1 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg07-acc-d before:pointer-events-none before:absolute before:bottom-[calc(100%+4px)] before:left-1/2 before:-translate-x-1/2 before:border-[5px] before:border-transparent before:border-t-tbg07-ink before:opacity-0 before:transition-opacity before:content-[''] hover:before:opacity-100 focus-visible:before:opacity-100 after:pointer-events-none after:absolute after:bottom-[calc(100%+14px)] after:left-1/2 after:-translate-x-1/2 after:rounded-lg after:bg-tbg07-ink after:px-2.5 after:py-1.5 after:text-xs after:font-semibold after:whitespace-nowrap after:text-tbg07-tip after:opacity-0 after:transition-[opacity,translate] after:content-[attr(data-tip)] hover:after:-translate-y-0.5 hover:after:opacity-100 focus-visible:after:opacity-100 motion-reduce:after:transition-none"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 5h12M10 5L8 19M15 5l-1 5M4 20L20 4"/></svg></button>
    </div>
    <p class="px-6 pt-5 pb-6 font-tbg07-serif text-[19px] leading-relaxed text-tbg07-ink group-has-[[data-cmd=bold][aria-pressed=true]]/ed:font-semibold group-has-[[data-cmd=italic][aria-pressed=true]]/ed:italic group-has-[[data-cmd=underline][aria-pressed=true]]/ed:underline group-has-[[data-cmd=underline][aria-pressed=true]]/ed:decoration-tbg07-acc-d group-has-[[data-cmd=underline][aria-pressed=true]]/ed:underline-offset-4 group-has-[[data-cmd=code][aria-pressed=true]]/ed:font-mono group-has-[[data-cmd=code][aria-pressed=true]]/ed:text-[16px]">Good tools disappear. You notice the work, not the buttons you pressed to make it.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg07-bg: #20261c;
  --color-tbg07-bg2: #2c3626;
  --color-tbg07-bar: #f4f7f0;
  --color-tbg07-line: #d8e0ce;
  --color-tbg07-hover: #e5ecdd;
  --color-tbg07-ink: #1a2415;
  --color-tbg07-tip: #eef4e8;
  --color-tbg07-mut: #4a5c3f;
  --color-tbg07-mut: oklch(0.44 0.05 135);
  --color-tbg07-on: #12200a;
  --color-tbg07-acc: #93cf52;
  --color-tbg07-acc: oklch(0.78 0.16 132);
  --color-tbg07-acc-d: #4d8a1c;
  --color-tbg07-acc-d: oklch(0.56 0.14 135);
  --shadow-tbg07-lift: 0 24px 50px -22px rgb(0 0 0 / 0.75), inset 0 0 0 1px rgb(255 255 255 / 0.6);
  --font-tbg07-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tbg07-serif: 'Newsreader', Georgia, serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-07 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tbg07-bar]').forEach((bar) => {
    if (bar.dataset.wired) return;
    bar.dataset.wired = '1';
    const btns = [...bar.querySelectorAll('button')];
    const focusAt = (i) => {
      btns.forEach((b, j) => { b.tabIndex = j === i ? 0 : -1; });
      btns[i].focus();
    };
    btns.forEach((b, i) => {
      b.addEventListener('click', () => {
        if (b.dataset.cmd === 'clear') {
          btns.forEach((x) => { if (x.hasAttribute('aria-pressed')) x.setAttribute('aria-pressed', 'false'); });
        } else if (b.hasAttribute('aria-pressed')) {
          b.setAttribute('aria-pressed', String(b.getAttribute('aria-pressed') !== 'true'));
        }
      });
      b.addEventListener('keydown', (e) => {
        const n = btns.length;
        const next = { ArrowRight: (i + 1) % n, ArrowLeft: (i - 1 + n) % n, Home: 0, End: n - 1 }[e.key];
        if (next === undefined) return;
        e.preventDefault();
        focusAt(next);
      });
    });
  });
})();
```

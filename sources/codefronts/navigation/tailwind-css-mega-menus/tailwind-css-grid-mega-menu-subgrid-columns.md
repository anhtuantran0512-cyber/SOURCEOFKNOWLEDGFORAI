---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-css-grid-mega-menu-subgrid-columns/"
title: "Tailwind CSS Grid Mega Menu with Subgrid Column Layout"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "An editorial workspace header whose mega panel is a responsive four-column grid: repeat(auto-fit, minmax(11rem, 1fr)) decides how many columns fit, and each…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Grid Mega Menu with Subgrid Column Layout
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-css-grid-mega-menu-subgrid-columns/

An editorial workspace header whose mega panel is a responsive four-column grid: repeat(auto-fit, minmax(11rem, 1fr)) decides how many columns fit, and each column spans three rows with grid-rows-subgrid so headings, link lists and footer counts line up across columns no matter how long a label wraps. Columns unroll left to right on open. Zero JavaScript.
## HTML
```html
<section class="tmm-04 relative w-full min-h-svh bg-tmm04-bg font-tmm04-sans leading-[1.55] text-tmm04-ink [&_:focus-visible]:rounded [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm04-acc" aria-labelledby="tmm04-title">
  <h2 class="sr-only" id="tmm04-title">Quill</h2>

  <div class="absolute top-[11px] right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm04-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmm04-line bg-tmm04-surf text-tmm04-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm04-acc" for="tmm04-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b border-tmm04-line bg-tmm04-surf">
    <div class="mx-auto flex min-h-[66px] w-[min(78rem,calc(100%-2rem))] flex-wrap items-stretch gap-x-[clamp(0.5rem,2vw,2rem)] pr-15 max-[52rem]:flex-col max-[52rem]:py-2">
      <a class="inline-flex items-center gap-2 font-tmm04-display text-xl/none font-semibold text-tmm04-ink" href="#tmm04-title">
        <svg class="size-[22px] text-tmm04-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 19c6-1 10-5 13-14-6 1-11 4-13 10Z" fill="currentColor" opacity=".85"/><path d="M5 19c2-4 5-6 8-7" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>
        Quill
      </a>

      <nav class="flex min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-0.5 max-[52rem]:flex-col">
          <li data-tmm04-item class="flex items-stretch max-[52rem]:block">
            <button type="button" aria-expanded="false" aria-controls="tmm04-panel-library" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 px-3.5 text-[0.92rem]/none font-semibold text-tmm04-ink transition-[color,box-shadow] hover:text-tmm04-acc tmm04-open:text-tmm04-acc! tmm04-open:shadow-[inset_0_-2px_0_var(--color-tmm04-acc)]">Library<svg class="size-3.5 opacity-60 transition-transform duration-200 tmm04-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm04-line bg-tmm04-surf opacity-0 shadow-tmm04-panel pointer-events-none transition-[opacity,visibility] duration-160 tmm04-open:visible tmm04-open:opacity-100 tmm04-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:shadow-none max-[52rem]:tmm04-open:block" id="tmm04-panel-library" aria-label="Library">
              <div class="mx-auto grid w-[min(78rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(11rem,1fr))] gap-x-[clamp(0.85rem,2.4vw,2rem)] gap-y-1 pt-[clamp(1.1rem,3vw,1.9rem)] max-[52rem]:w-full max-[52rem]:px-4">
                <section class="row-span-3 grid min-w-0 grid-rows-[auto_minmax(0,1fr)_auto] gap-1.5 [clip-path:inset(0_0_100%_0)] opacity-0 transition-[clip-path,opacity] duration-[400ms,200ms] ease-[cubic-bezier(0.4,0,0.2,1),ease] delay-30 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm04-open:[clip-path:inset(-8px)] tmm04-open:opacity-100 motion-reduce:[clip-path:none] motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm04-h-writing">
                  <h3 class="font-tmm04-display text-base/tight font-semibold" id="tmm04-h-writing"><span class="mr-1.5 font-tmm04-sans text-[0.7rem] font-semibold text-tmm04-acc tabular-nums">01</span>Writing</h3>
                  <ul class="grid content-start gap-px">
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Drafts<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Style guide<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Collaborative review workflow<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Version history<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Templates<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                  </ul>
                  <p class="flex items-center gap-1.5 border-t border-tmm04-line py-2 font-tmm04-display text-[0.72rem]/snug font-medium tracking-[0.05em] text-tmm04-mut"><span aria-hidden="true" class="size-1 rounded-full bg-tmm04-acc"></span>18 documents</p>
                </section>
                <section class="row-span-3 grid min-w-0 grid-rows-[auto_minmax(0,1fr)_auto] gap-1.5 [clip-path:inset(0_0_100%_0)] opacity-0 transition-[clip-path,opacity] duration-[400ms,200ms] ease-[cubic-bezier(0.4,0,0.2,1),ease] delay-105 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm04-open:[clip-path:inset(-8px)] tmm04-open:opacity-100 motion-reduce:[clip-path:none] motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm04-h-publish">
                  <h3 class="font-tmm04-display text-base/tight font-semibold" id="tmm04-h-publish"><span class="mr-1.5 font-tmm04-sans text-[0.7rem] font-semibold text-tmm04-acc tabular-nums">02</span>Publish</h3>
                  <ul class="grid content-start gap-px">
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Scheduling<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Distribution channels<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Newsletter<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                  </ul>
                  <p class="flex items-center gap-1.5 border-t border-tmm04-line py-2 font-tmm04-display text-[0.72rem]/snug font-medium tracking-[0.05em] text-tmm04-mut"><span aria-hidden="true" class="size-1 rounded-full bg-tmm04-acc"></span>2 channels live</p>
                </section>
                <section class="row-span-3 grid min-w-0 grid-rows-[auto_minmax(0,1fr)_auto] gap-1.5 [clip-path:inset(0_0_100%_0)] opacity-0 transition-[clip-path,opacity] duration-[400ms,200ms] ease-[cubic-bezier(0.4,0,0.2,1),ease] delay-180 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm04-open:[clip-path:inset(-8px)] tmm04-open:opacity-100 motion-reduce:[clip-path:none] motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm04-h-measure">
                  <h3 class="font-tmm04-display text-base/tight font-semibold" id="tmm04-h-measure"><span class="mr-1.5 font-tmm04-sans text-[0.7rem] font-semibold text-tmm04-acc tabular-nums">03</span>Measure</h3>
                  <ul class="grid content-start gap-px">
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Readership<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Retention cohorts<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Referrals<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Export to warehouse<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                  </ul>
                  <p class="flex items-center gap-1.5 border-t border-tmm04-line py-2 font-tmm04-display text-[0.72rem]/snug font-medium tracking-[0.05em] text-tmm04-mut"><span aria-hidden="true" class="size-1 rounded-full bg-tmm04-acc"></span>updated hourly</p>
                </section>
                <section class="row-span-3 grid min-w-0 grid-rows-[auto_minmax(0,1fr)_auto] gap-1.5 [clip-path:inset(0_0_100%_0)] opacity-0 transition-[clip-path,opacity] duration-[400ms,200ms] ease-[cubic-bezier(0.4,0,0.2,1),ease] delay-255 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm04-open:[clip-path:inset(-8px)] tmm04-open:opacity-100 motion-reduce:[clip-path:none] motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm04-h-admin">
                  <h3 class="font-tmm04-display text-base/tight font-semibold" id="tmm04-h-admin"><span class="mr-1.5 font-tmm04-sans text-[0.7rem] font-semibold text-tmm04-acc tabular-nums">04</span>Administration</h3>
                  <ul class="grid content-start gap-px">
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Enterprise single sign-on configuration<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Billing<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                  </ul>
                  <p class="flex items-center gap-1.5 border-t border-tmm04-line py-2 font-tmm04-display text-[0.72rem]/snug font-medium tracking-[0.05em] text-tmm04-mut"><span aria-hidden="true" class="size-1 rounded-full bg-tmm04-acc"></span>owner only</p>
                </section>
              </div>
              <div class="mx-auto flex w-[min(78rem,calc(100%-2rem))] flex-wrap gap-x-[clamp(0.75rem,3vw,2rem)] pt-1 pb-3.5 opacity-0 transition-opacity delay-340 duration-260 tmm04-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none max-[52rem]:w-full max-[52rem]:px-4">
                <a class="inline-flex min-h-11 items-center gap-2 text-[0.82rem]/none font-semibold text-tmm04-ink hover:text-tmm04-acc hover:underline hover:underline-offset-3" href="#tmm04-title">Keyboard shortcuts <kbd class="rounded border border-tmm04-line px-1.5 py-0.5 font-tmm04-sans text-[0.7rem] text-tmm04-mut">?</kbd></a>
                <a class="inline-flex min-h-11 items-center gap-2 text-[0.82rem]/none font-semibold text-tmm04-ink hover:text-tmm04-acc hover:underline hover:underline-offset-3" href="#tmm04-title">Import from Markdown</a>
                <a class="inline-flex min-h-11 items-center gap-2 text-[0.82rem]/none font-semibold text-tmm04-ink hover:text-tmm04-acc hover:underline hover:underline-offset-3" href="#tmm04-title">What's new <span class="rounded-full bg-tmm04-acc px-1.5 py-0.5 text-[0.62rem] font-bold tracking-[0.06em] text-tmm04-on-acc uppercase">3 new</span></a>
              </div>
            </div>
          </li>

          <li data-tmm04-item class="flex items-stretch max-[52rem]:block">
            <button type="button" aria-expanded="false" aria-controls="tmm04-panel-teams" class="inline-flex min-h-11 cursor-pointer items-center gap-1.5 px-3.5 text-[0.92rem]/none font-semibold text-tmm04-ink transition-[color,box-shadow] hover:text-tmm04-acc tmm04-open:text-tmm04-acc! tmm04-open:shadow-[inset_0_-2px_0_var(--color-tmm04-acc)]">Teams<svg class="size-3.5 opacity-60 transition-transform duration-200 tmm04-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm04-line bg-tmm04-surf opacity-0 shadow-tmm04-panel pointer-events-none transition-[opacity,visibility] duration-160 tmm04-open:visible tmm04-open:opacity-100 tmm04-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:shadow-none max-[52rem]:tmm04-open:block" id="tmm04-panel-teams" aria-label="Teams">
              <div class="mx-auto grid w-[min(78rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(11rem,1fr))] gap-x-[clamp(0.85rem,2.4vw,2rem)] gap-y-1 pt-[clamp(1.1rem,3vw,1.9rem)] max-[52rem]:w-full max-[52rem]:px-4">
                <section class="row-span-3 grid min-w-0 grid-rows-[auto_minmax(0,1fr)_auto] gap-1.5 [clip-path:inset(0_0_100%_0)] opacity-0 transition-[clip-path,opacity] duration-[400ms,200ms] ease-[cubic-bezier(0.4,0,0.2,1),ease] delay-30 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm04-open:[clip-path:inset(-8px)] tmm04-open:opacity-100 motion-reduce:[clip-path:none] motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm04-h-people">
                  <h3 class="font-tmm04-display text-base/tight font-semibold" id="tmm04-h-people"><span class="mr-1.5 font-tmm04-sans text-[0.7rem] font-semibold text-tmm04-acc tabular-nums">01</span>People</h3>
                  <ul class="grid content-start gap-px">
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Members<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Guest editors<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Roles<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                  </ul>
                  <p class="flex items-center gap-1.5 border-t border-tmm04-line py-2 font-tmm04-display text-[0.72rem]/snug font-medium tracking-[0.05em] text-tmm04-mut"><span aria-hidden="true" class="size-1 rounded-full bg-tmm04-acc"></span>34 seats</p>
                </section>
                <section class="row-span-3 grid min-w-0 grid-rows-[auto_minmax(0,1fr)_auto] gap-1.5 [clip-path:inset(0_0_100%_0)] opacity-0 transition-[clip-path,opacity] duration-[400ms,200ms] ease-[cubic-bezier(0.4,0,0.2,1),ease] delay-105 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm04-open:[clip-path:inset(-8px)] tmm04-open:opacity-100 motion-reduce:[clip-path:none] motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm04-h-spaces">
                  <h3 class="font-tmm04-display text-base/tight font-semibold" id="tmm04-h-spaces"><span class="mr-1.5 font-tmm04-sans text-[0.7rem] font-semibold text-tmm04-acc tabular-nums">02</span>Spaces</h3>
                  <ul class="grid content-start gap-px">
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Newsroom<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Longform<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                  </ul>
                  <p class="flex items-center gap-1.5 border-t border-tmm04-line py-2 font-tmm04-display text-[0.72rem]/snug font-medium tracking-[0.05em] text-tmm04-mut"><span aria-hidden="true" class="size-1 rounded-full bg-tmm04-acc"></span>2 spaces</p>
                </section>
                <section class="row-span-3 grid min-w-0 grid-rows-[auto_minmax(0,1fr)_auto] gap-1.5 [clip-path:inset(0_0_100%_0)] opacity-0 transition-[clip-path,opacity] duration-[400ms,200ms] ease-[cubic-bezier(0.4,0,0.2,1),ease] delay-180 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm04-open:[clip-path:inset(-8px)] tmm04-open:opacity-100 motion-reduce:[clip-path:none] motion-reduce:opacity-100 motion-reduce:transition-none" aria-labelledby="tmm04-h-flow">
                  <h3 class="font-tmm04-display text-base/tight font-semibold" id="tmm04-h-flow"><span class="mr-1.5 font-tmm04-sans text-[0.7rem] font-semibold text-tmm04-acc tabular-nums">03</span>Workflow</h3>
                  <ul class="grid content-start gap-px">
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Approvals<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Fact checking<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Legal review<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                    <li><a href="#tmm04-title" class="group/l -mx-1.5 flex min-h-11 min-w-0 items-center justify-between gap-2 rounded px-1.5 text-[0.9rem] text-tmm04-mut text-pretty transition-colors hover:bg-tmm04-acc/8 hover:text-tmm04-acc">Embargoes<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/l:translate-x-0 group-hover/l:opacity-100">&rarr;</span></a></li>
                  </ul>
                  <p class="flex items-center gap-1.5 border-t border-tmm04-line py-2 font-tmm04-display text-[0.72rem]/snug font-medium tracking-[0.05em] text-tmm04-mut"><span aria-hidden="true" class="size-1 rounded-full bg-tmm04-acc"></span>4 stages</p>
                </section>
              </div>
              <div class="mx-auto flex w-[min(78rem,calc(100%-2rem))] flex-wrap gap-x-[clamp(0.75rem,3vw,2rem)] pt-1 pb-3.5 opacity-0 transition-opacity delay-340 duration-260 tmm04-open:opacity-100 motion-reduce:opacity-100 motion-reduce:transition-none max-[52rem]:w-full max-[52rem]:px-4">
                <a class="inline-flex min-h-11 items-center gap-2 text-[0.82rem]/none font-semibold text-tmm04-ink hover:text-tmm04-acc hover:underline hover:underline-offset-3" href="#tmm04-title">Invite a teammate <span aria-hidden="true">&rarr;</span></a>
              </div>
            </div>
          </li>

          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 text-[0.92rem]/none font-semibold text-tmm04-ink hover:text-tmm04-acc" href="#tmm04-title">Pricing</a></li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 text-[0.92rem]/none font-semibold text-tmm04-ink hover:text-tmm04-acc" href="#tmm04-title">Help</a></li>
        </ul>
      </nav>

      <div class="ml-auto flex items-center gap-2 max-[52rem]:ml-0">
        <a class="inline-flex min-h-11 items-center px-2.5 text-[0.88rem] font-semibold text-tmm04-mut hover:text-tmm04-ink" href="#tmm04-title">Log in</a>
        <a class="inline-flex min-h-11 items-center gap-1.5 border border-tmm04-ink bg-tmm04-ink px-4 text-[0.88rem] font-semibold text-tmm04-surf transition-colors hover:border-tmm04-acc hover:bg-tmm04-acc" href="#tmm04-title"><span aria-hidden="true" class="text-base/none">+</span> New document</a>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(78rem,calc(100%-2rem))] py-[clamp(3rem,10vw,6rem)]">
    <article class="grid max-w-[42rem] gap-3">
      <p class="text-[0.72rem]/none font-semibold tracking-[0.22em] text-tmm04-acc uppercase">Quill for editorial teams</p>
      <h1 class="font-tmm04-display text-[clamp(2rem,6vw,3.4rem)]/[1.05] font-semibold tracking-[-0.02em] text-balance">Write, review and publish in one place.</h1>
      <p class="text-[clamp(0.95rem,2.4vw,1.1rem)] text-tmm04-mut text-pretty">Drafts that never leave the workflow. Fact checks that stay attached to the sentence. A publish button that knows which channels are live.</p>
    </article>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm04-bg: #faf6ef;
  --color-tmm04-bg: oklch(0.975 0.012 80);
  --color-tmm04-surf: #fffdf9;
  --color-tmm04-surf: oklch(0.995 0.005 80);
  --color-tmm04-line: #e7ddcd;
  --color-tmm04-line: oklch(0.9 0.022 80);
  --color-tmm04-ink: #241d14;
  --color-tmm04-ink: oklch(0.23 0.02 70);
  --color-tmm04-mut: #6e624f;
  --color-tmm04-mut: oklch(0.5 0.035 75);
  --color-tmm04-acc: #9a3412;
  --color-tmm04-acc: oklch(0.48 0.16 40);
  --color-tmm04-on-acc: #ffffff;
  --color-tmm04-on-acc: oklch(1 0 0);
  --font-tmm04-display: 'Roboto Slab', Georgia, serif;
  --font-tmm04-sans: 'Source Sans 3', system-ui, sans-serif;
  --shadow-tmm04-panel: 0 24px 48px -32px rgb(36 29 20 / 0.35);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm04-open: instead of a repeated selector list. */

@custom-variant tmm04-open {
  &:where([data-tmm04-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm04-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-04 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-04:has(#tmm04-theme:checked) {
  --color-tmm04-bg: #14100b;
  --color-tmm04-bg: oklch(0.17 0.012 70);
  --color-tmm04-surf: #1d1811;
  --color-tmm04-surf: oklch(0.21 0.015 70);
  --color-tmm04-line: #342b1f;
  --color-tmm04-line: oklch(0.3 0.025 70);
  --color-tmm04-ink: #f6efe3;
  --color-tmm04-ink: oklch(0.95 0.017 80);
  --color-tmm04-mut: #ab9c85;
  --color-tmm04-mut: oklch(0.71 0.035 80);
  --color-tmm04-acc: #fb923c;
  --color-tmm04-acc: oklch(0.76 0.16 55);
  --color-tmm04-on-acc: #1d1811;
  --color-tmm04-on-acc: oklch(0.21 0.015 70);
}

@media (prefers-color-scheme: dark) {
  .tmm-04 {
    --color-tmm04-bg: #14100b;
    --color-tmm04-bg: oklch(0.17 0.012 70);
    --color-tmm04-surf: #1d1811;
    --color-tmm04-surf: oklch(0.21 0.015 70);
    --color-tmm04-line: #342b1f;
    --color-tmm04-line: oklch(0.3 0.025 70);
    --color-tmm04-ink: #f6efe3;
    --color-tmm04-ink: oklch(0.95 0.017 80);
    --color-tmm04-mut: #ab9c85;
    --color-tmm04-mut: oklch(0.71 0.035 80);
    --color-tmm04-acc: #fb923c;
    --color-tmm04-acc: oklch(0.76 0.16 55);
    --color-tmm04-on-acc: #1d1811;
    --color-tmm04-on-acc: oklch(0.21 0.015 70);
  }

  .tmm-04:has(#tmm04-theme:checked) {
    --color-tmm04-bg: #faf6ef;
    --color-tmm04-bg: oklch(0.975 0.012 80);
    --color-tmm04-surf: #fffdf9;
    --color-tmm04-surf: oklch(0.995 0.005 80);
    --color-tmm04-line: #e7ddcd;
    --color-tmm04-line: oklch(0.9 0.022 80);
    --color-tmm04-ink: #241d14;
    --color-tmm04-ink: oklch(0.23 0.02 70);
    --color-tmm04-mut: #6e624f;
    --color-tmm04-mut: oklch(0.5 0.035 75);
    --color-tmm04-acc: #9a3412;
    --color-tmm04-acc: oklch(0.48 0.16 40);
    --color-tmm04-on-acc: #ffffff;
    --color-tmm04-on-acc: oklch(1 0 0);
  }
}
```

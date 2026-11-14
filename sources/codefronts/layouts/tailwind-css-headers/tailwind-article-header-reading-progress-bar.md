---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-article-header-reading-progress-bar/"
title: "Tailwind Article Header with Reading Progress Bar"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "An editorial header with a hairline meter that fills as the reader moves down the piece — one element scaled with scaleX() on a scroll(root) timeline, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Article Header with Reading Progress Bar
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-article-header-reading-progress-bar/

An editorial header with a hairline meter that fills as the reader moves down the piece — one element scaled with scaleX() on a scroll(root) timeline, a single composited layer instead of a scroll handler. New in this port: the article's title docks into the header once the hero scrolls away, on the same timeline.
## HTML
```html
<div class="thd-06 group/thd06 w-full min-h-svh bg-thd06-bg font-thd06-sans text-thd06-ink antialiased">
  <a href="#thd-06-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd06-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <header class="sticky top-0 z-40 border-b border-thd06-line bg-thd06-bg/92 backdrop-blur-md">
    <div class="mx-auto flex h-14 max-w-6xl items-center gap-4 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-06-main" class="whitespace-nowrap font-thd06-serif text-xl font-semibold italic tracking-tight">The Long Field</a>
      <div class="relative hidden min-w-0 flex-1 md:block">
        <nav aria-label="Sections" class="thd06-navout">
          <ul class="flex items-center gap-5 text-sm font-semibold text-thd06-mut">
            <li><a href="#thd-06-main" aria-current="page" class="py-2 hover:text-thd06-ink aria-[current=page]:text-thd06-acc">Reporting</a></li>
            <li><a href="#thd-06-main" class="py-2 hover:text-thd06-ink">Essays</a></li>
            <li><a href="#thd-06-main" class="py-2 hover:text-thd06-ink">Interviews</a></li>
          </ul>
        </nav>
        <p aria-hidden="true" class="thd06-dock pointer-events-none absolute inset-0 flex items-center truncate font-thd06-serif text-[15px] opacity-0"><span class="truncate">The river that learned to run backwards</span></p>
      </div>
      <div class="ml-auto flex items-center gap-1">
        <input id="thd-06-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-06-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-thd06-mut hover:bg-thd06-ink/5 hover:text-thd06-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd06-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-06-t:checked]/thd06:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-06-t:checked]/thd06:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-06-main" class="grid min-h-10 place-items-center rounded-full bg-thd06-ink px-4 text-sm font-bold text-thd06-bg transition-colors hover:bg-thd06-acc">Subscribe</a>
      </div>
    </div>
    <div aria-hidden="true" class="thd06-meter absolute inset-x-0 -bottom-px h-[3px] origin-left bg-thd06-acc"></div>
  </header>
  <main id="thd-06-main" class="px-[clamp(1rem,4vw,2rem)]">
    <article class="mx-auto max-w-[42rem] py-[clamp(2.5rem,8vw,5rem)]">
      <p class="text-xs font-bold uppercase tracking-[.18em] text-thd06-acc">Reporting &middot; Climate</p>
      <h1 class="mt-3 font-thd06-serif text-[clamp(2.2rem,6.5vw,3.8rem)] font-medium leading-[1.02] tracking-[-.02em] text-balance">The river that learned to run backwards</h1>
      <p class="mt-4 font-thd06-serif text-xl italic leading-snug text-thd06-mut">In the Fens, engineers are letting the sea back in &mdash; and the farmers are helping.</p>
      <div class="mt-6 flex flex-wrap items-center gap-3 border-y border-thd06-line py-3 text-sm">
        <span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-thd06-acc/15 text-xs font-bold text-thd06-acc">JL</span>
        <span><strong>Jordan Lee</strong> <span class="text-thd06-mut">&middot; 25 September 2026</span></span>
        <span class="ml-auto rounded-full bg-thd06-ink/5 px-2.5 py-1 text-xs font-semibold tabular-nums text-thd06-mut">14 min read</span>
      </div>
      <div class="mt-8 space-y-5 font-thd06-serif text-[1.18rem] leading-[1.7]">
        <p class="first-letter:float-left first-letter:mr-2 first-letter:mt-1 first-letter:font-semibold first-letter:text-[3.6rem] first-letter:leading-[.8] first-letter:text-thd06-acc">At low tide the new channel is a ribbon of silver mud, pocked by the feet of oystercatchers. At high tide it is a river again &mdash; only now it flows inland.</p>
        <p>For three centuries the drainage boards of eastern England fought to keep salt water out. The pumps still run, but on this stretch of the Ouse they have been switched off on purpose, and the old sea wall has a forty-metre gap cut through it.</p>
        <p>Scroll, and watch the header: the meter fills with the page, and the headline docks into the bar once this hero has gone.</p>
        <p>&ldquo;We spent a generation losing an argument with the tide,&rdquo; says Sam Rivera, who farms the land either side of the breach. &ldquo;This is the first time it feels like we&rsquo;re negotiating.&rdquo;</p>
        <p>The saltmarsh that has formed in eighteen months already stores more carbon per hectare than the wheat it replaced, and the flood risk to the village upstream has fallen, not risen.</p>
      </div>
      <div aria-hidden="true" class="h-[80svh]"></div>
    </article>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd06-bg: var(--thd06-bg);
  --color-thd06-ink: var(--thd06-ink);
  --color-thd06-mut: var(--thd06-mut);
  --color-thd06-line: var(--thd06-line);
  --color-thd06-acc: var(--thd06-acc);
}

@theme {
  --font-thd06-serif: 'Newsreader', Georgia, serif;
  --font-thd06-sans: 'Source Sans 3', system-ui, sans-serif;
}

.thd-06 {
  width: 100%;
  min-height: 100svh;
  --thd06-bg: #fbf9f4;
  --thd06-ink: #1d1b16;
  --thd06-mut: #5f5a50;
  --thd06-line: #e7e2d6;
  --thd06-acc: #b4441c;
}

.thd-06:has(#thd-06-t:checked) {
  --thd06-bg: #14130f;
  --thd06-ink: #f0ebe0;
  --thd06-mut: #aca596;
  --thd06-line: #2b2922;
  --thd06-acc: #f08a5d;
}

@utility thd06-meter {
  display: none;

  @supports (animation-timeline: scroll()) {
    display: block;
    animation: thd06-fill linear both;
    animation-timeline: scroll(root);
  }
}

@utility thd06-dock {
  @supports (animation-timeline: scroll()) {
    animation: thd06-in linear both;
    animation-timeline: scroll(root);
    animation-range: 320px 420px;
  }
}

@utility thd06-navout {
  @supports (animation-timeline: scroll()) {
    animation: thd06-out linear both;
    animation-timeline: scroll(root);
    animation-range: 320px 420px;
  }
}

@keyframes thd06-fill {
  from {
    scale: 0 1;
  }

  to {
    scale: 1 1;
  }
}

@keyframes thd06-in {
  from {
    opacity: 0;
    translate: 0 0.5rem;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

@keyframes thd06-out {
  to {
    opacity: 0;
    translate: 0 -0.5rem;
    visibility: hidden;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-full-bleed-article-layout-long-form-editorial/"
title: "Tailwind Full-Bleed Article Layout for Long-Form Editorial"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A real magazine feature — dateline, drop-in photography, a full-bleed pull quote and a reading measure that never wavers."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full-Bleed Article Layout for Long-Form Editorial
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-full-bleed-article-layout-long-form-editorial/

A real magazine feature — dateline, drop-in photography, a full-bleed pull quote and a reading measure that never wavers. Body copy locks to 65ch while imagery breaks the gutters, and any element opts into the bleed with one class.
## HTML
```html
<section class="tgx-01 w-full min-h-svh bg-tgx01-paper text-tgx01-ink font-tgx01-serif">
  <article class="grid [grid-template-columns:var(--tgx01-track)] *:[grid-column:content] gap-y-6 pb-16">
    <header class="[grid-column:full] grid [grid-template-columns:inherit] bg-tgx01-ink text-tgx01-paper py-10">
      <div class="[grid-column:content] flex flex-col gap-4">
        <p class="font-tgx01-sans text-[0.7rem] font-semibold tracking-[0.2em] uppercase text-tgx01-accentlight">Atlas Quarterly · Field Report</p>
        <h1 class="text-[clamp(2rem,5.5vw,3.2rem)] leading-[1.06] font-semibold tracking-[-0.015em] text-balance">The last ferry to Vestmanna</h1>
        <p class="font-tgx01-sans text-[0.95rem] leading-[1.6] text-tgx01-papermut max-w-[52ch]">Three days on the Faroese coast road, where the weather writes the timetable and every village keeps one boat in reserve.</p>
        <p class="font-tgx01-sans text-[0.78rem] text-tgx01-papermut">Words &amp; pictures by Marit Solheim · 14 min read · September 2026</p>
      </div>
    </header>
    <figure class="[grid-column:full] flex flex-col gap-2 mt-2">
      <div class="w-full aspect-[21/9] overflow-hidden bg-tgx01-shade">
        <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=2000&h=857&q=80&auto=format&fit=crop" alt="Low cloud breaking over a green coastal ridge above dark water" loading="lazy" class="w-full h-full object-cover">
      </div>
      <figcaption class="font-tgx01-sans text-xs text-tgx01-mut px-6">Sørvágsvatn from the ridge path, 06:40. The figure spans <code class="font-tgx01-mono">grid-column: full</code> — edge to edge, no negative margins.</figcaption>
    </figure>
    <p class="text-[1.06rem] leading-[1.75] first-letter:float-left first-letter:text-[3.1em] first-letter:leading-[0.84] first-letter:pr-[0.1em] first-letter:font-semibold first-letter:text-tgx01-accent">The bus from Tórshavn leaves at ten past seven and will not wait for anyone photographing the harbour. I learn this on the first morning, from a driver who has clearly had the conversation before, and who accelerates away with the sort of patience reserved for people who will now be walking.</p>
    <p class="text-[1.06rem] leading-[1.75]">What replaces the bus is better anyway: a coast road with no shoulder, a tunnel lit like a dance floor, and a run of villages that appear exactly when the fog decides to lift. The measure of a place like this is how long the light holds, and here it holds for about four minutes at a time.</p>
    <blockquote class="[grid-column:full] [grid-template-columns:inherit] grid bg-tgx01-accent text-white py-12 my-4">
      <p class="[grid-column:content] text-[clamp(1.3rem,3.2vw,1.9rem)] leading-[1.35] font-semibold text-balance">&ldquo;You do not plan a week here. You plan a morning, and then you ask someone at the shop what the afternoon is doing.&rdquo;</p>
    </blockquote>
    <p class="text-[1.06rem] leading-[1.75]">By the third day I have stopped checking the forecast, which is the point at which the coast road starts to make sense. The ferry to Vestmanna runs when the sound is calm. The sound is calm when it is calm.</p>
    <figure class="[grid-column:full] grid [grid-template-columns:inherit] gap-y-2 my-2">
      <div class="[grid-column:content] grid grid-cols-2 max-sm:grid-cols-1 gap-3">
        <div class="aspect-[4/3] overflow-hidden rounded-sm bg-tgx01-shade"><img src="https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?w=800&h=600&q=80&auto=format&fit=crop" alt="Narrow path through low pine woodland in flat morning light" loading="lazy" class="w-full h-full object-cover"></div>
        <div class="aspect-[4/3] overflow-hidden rounded-sm bg-tgx01-shade"><img src="https://images.unsplash.com/photo-1426604966848-d7adac402bff?w=800&h=600&q=80&auto=format&fit=crop" alt="Steep green valley falling away toward a river" loading="lazy" class="w-full h-full object-cover"></div>
      </div>
      <figcaption class="[grid-column:content] font-tgx01-sans text-xs text-tgx01-mut">Inland detours: the pass above Saksun (left) and the valley road south (right).</figcaption>
    </figure>
    <p class="text-[1.06rem] leading-[1.75]">The last ferry is at 17:20, and it does wait — for the bus, for the two cyclists, for the man carrying a door. Everything on this coast runs late and nothing is actually missed.</p>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx01-paper: #f9f6f0;
  --color-tgx01-paper: oklch(0.97 0.012 85);
  --color-tgx01-papermut: #cfc7bb;
  --color-tgx01-papermut: oklch(0.83 0.012 85);
  --color-tgx01-shade: #e7e1d7;
  --color-tgx01-shade: oklch(0.91 0.012 85);
  --color-tgx01-ink: #2e2822;
  --color-tgx01-ink: oklch(0.27 0.015 60);
  --color-tgx01-mut: #756b5f;
  --color-tgx01-mut: oklch(0.52 0.02 65);
  --color-tgx01-accent: #9c4a26;
  --color-tgx01-accent: oklch(0.5 0.14 45);
  --color-tgx01-accentlight: #e8a077;
  --color-tgx01-accentlight: oklch(0.78 0.11 45);
  --font-tgx01-serif: 'Fraunces', Georgia, serif;
  --font-tgx01-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx01-mono: ui-monospace, Menlo, monospace;
}
/* Named-line track list: grammar, not design scale — kept in CSS and passed
   into the markup through one arbitrary property. */

.tgx-01 {
  width: 100%;
  min-height: 100svh;
  --tgx01-track: [full-start] minmax(1.5rem, 1fr) [content-start] min(65ch, calc(100% - 3rem)) [content-end] minmax(1.5rem, 1fr) [full-end];
}
```

---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-masonry-grid-dashboard-layout/"
title: "Tailwind CSS Masonry Grid Dashboard Layout (Columns vs Grid Dense)"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "Eight numbered widgets, two packing engines, one switch."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Masonry Grid Dashboard Layout (Columns vs Grid Dense)
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-masonry-grid-dashboard-layout/

Eight numbered widgets, two packing engines, one switch. Engine A is columns-[3_15rem] + break-inside-avoid: true masonry, but it reads down each column. Engine B is grid-flow-dense auto-rows-2 with row-span-(--rows): left-to-right order with holes backfilled, heights quantised to an 8px beat. The numbers on the cards make the trade-off obvious in two seconds; the switch is a radio pair read by group-has-[#tdl15-grid:checked]/board:.
## HTML
```html
<section class="tdl-15 w-full min-h-svh bg-tdl15-bg bg-linear-175 from-tdl15-bg to-tdl15-bg2 font-tdl15-sans text-tdl15-ink antialiased" aria-label="Masonry packing comparison demo">
  <div class="group/board mx-auto w-full max-w-6xl p-4 sm:p-6">
    <header class="mb-4 flex flex-wrap items-center gap-3.5">
      <h2 class="mr-auto text-lg font-semibold tracking-tight">Widget board</h2>
      <fieldset class="flex gap-1 rounded-xl border border-tdl15-edge bg-tdl15-panel p-0.75 [&>label]:flex [&>label]:h-9 [&>label]:cursor-pointer [&>label]:items-center [&>label]:gap-2 [&>label]:rounded-lg [&>label]:px-3.25 [&>label]:text-xs [&>label]:font-semibold [&>label]:text-tdl15-mut [&>label]:transition [&>label:hover]:text-tdl15-ink [&>label:has(:checked)]:bg-tdl15-acc [&>label:has(:checked)]:text-white [&>label:has(:focus-visible)]:outline-2 [&>label:has(:focus-visible)]:outline-offset-2 [&>label:has(:focus-visible)]:outline-tdl15-acc [&_svg]:size-3.5 [&_svg]:fill-none [&_svg]:stroke-current [&_svg]:stroke-2">
        <legend class="sr-only">Packing engine</legend>
        <label><input class="sr-only" type="radio" name="tdl15" id="tdl15-cols" checked><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4v16M12 4v16M19 4v16"/></svg>A · columns</label>
        <label><input class="sr-only" type="radio" name="tdl15" id="tdl15-grid"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="7" height="9" rx="1"/><rect x="13" y="4" width="7" height="5" rx="1"/><rect x="4" y="15" width="7" height="5" rx="1"/><rect x="13" y="11" width="7" height="9" rx="1"/></svg>B · grid dense</label>
      </fieldset>
      <p class="basis-full text-[13px] text-tdl15-mut"><span class="group-has-[#tdl15-grid:checked]/board:hidden">Reading order flows <b class="text-tdl15-accink">down</b> each column — note 1 → 2 → 3 stacking vertically.</span><span class="hidden group-has-[#tdl15-grid:checked]/board:inline">Reading order stays <b class="text-tdl15-accink">left → right</b>; holes are backfilled, heights snap to an 8px beat.</span></p>
    </header>
    <div class="gap-3.5 group-has-[#tdl15-cols:checked]/board:columns-[3_15rem] group-has-[#tdl15-cols:checked]/board:*:mb-3.5 group-has-[#tdl15-cols:checked]/board:*:break-inside-avoid group-has-[#tdl15-grid:checked]/board:grid group-has-[#tdl15-grid:checked]/board:auto-rows-2 group-has-[#tdl15-grid:checked]/board:grid-flow-dense group-has-[#tdl15-grid:checked]/board:grid-cols-[repeat(auto-fill,minmax(min(15rem,100%),1fr))] group-has-[#tdl15-grid:checked]/board:*:row-span-(--rows) *:relative *:flex *:flex-col *:gap-2 *:overflow-hidden *:rounded-2xl *:border *:border-tdl15-edge *:bg-tdl15-panel *:p-4 *:transition *:hover:border-tdl15-acc/50 *:hover:shadow-[0_10px_24px_-18px_var(--color-tdl15-shadow)] [&_h3]:text-[10.5px] [&_h3]:font-semibold [&_h3]:tracking-[0.11em] [&_h3]:text-tdl15-mut [&_h3]:uppercase [&_.n]:absolute [&_.n]:top-2.5 [&_.n]:right-3 [&_.n]:grid [&_.n]:size-6 [&_.n]:place-items-center [&_.n]:rounded-lg [&_.n]:bg-tdl15-acc/12 [&_.n]:text-xs [&_.n]:font-bold [&_.n]:text-tdl15-accink [&_.big]:text-[26px] [&_.big]:font-semibold [&_.big]:tracking-tight [&_.big]:tabular-nums [&_.txt]:text-[13px]/[1.55] [&_.txt]:text-tdl15-mut">
      <article style="--rows:6"><b class="n">1</b><h3>Sales pulse</h3><p class="big">$12,940</p><p class="txt">Today · <span class="font-semibold text-tdl15-good">▲ 7%</span> vs Friday</p></article>
      <article style="--rows:9"><b class="n">2</b><h3>Traffic</h3><div aria-hidden="true" class="flex h-14 items-end gap-1.5 *:h-(--h) *:flex-1 *:rounded-t-[3px] *:bg-linear-to-t *:from-tdl15-acc/30 *:to-tdl15-acc"><i style="--h:40%"></i><i style="--h:62%"></i><i style="--h:50%"></i><i style="--h:78%"></i><i style="--h:66%"></i><i style="--h:92%"></i></div><p class="txt">Organic up 12% after the changelog post hit the front page.</p></article>
      <article style="--rows:7"><b class="n">3</b><h3>Note to self</h3><p class="txt">Ship the pricing experiment behind a flag Tuesday. Watch AOV, not conversion, for the first 48h.</p></article>
      <article style="--rows:5"><b class="n">4</b><h3>NPS</h3><p class="big">+61</p><div aria-hidden="true" class="h-1.5 overflow-hidden rounded-full bg-tdl15-track"><i class="block h-full w-[80.5%] rounded-full bg-tdl15-good"></i></div></article>
      <article style="--rows:8"><b class="n">5</b><h3>On-call</h3><p class="txt">Rotation: Priya → Sam → Jo.</p><p class="txt">Quiet week — 2 pages, both auto-resolved. Postmortem for #221 due Thu.</p></article>
      <article style="--rows:5"><b class="n">6</b><h3>Signups</h3><p class="big">312<small class="text-[13px] font-semibold text-tdl15-mut">/wk</small></p></article>
      <article style="--rows:6"><b class="n">7</b><h3>Churn watch</h3><p class="txt">3 accounts idle 21+ days. Playbook emails queued for Monday 09:00.</p></article>
      <article style="--rows:6"><b class="n">8</b><h3>Build</h3><p class="big flex items-center gap-2 text-tdl15-good!"><i aria-hidden="true" class="size-2.5 rounded-full bg-tdl15-good"></i>passing</p><p class="txt">main · 4m ago</p></article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl15-bg: #fbf8f4;
  --color-tdl15-bg: oklch(0.978 0.007 60);
  --color-tdl15-bg2: #f4efe8;
  --color-tdl15-bg2: oklch(0.955 0.012 60);
  --color-tdl15-panel: #ffffff;
  --color-tdl15-panel: oklch(1 0 0);
  --color-tdl15-track: #efe9e2;
  --color-tdl15-track: oklch(0.94 0.01 60);
  --color-tdl15-edge: #e8e0d6;
  --color-tdl15-edge: oklch(0.91 0.015 60);
  --color-tdl15-ink: #2f2620;
  --color-tdl15-ink: oklch(0.27 0.02 50);
  --color-tdl15-mut: #6a5d53;
  --color-tdl15-mut: oklch(0.49 0.03 50);
  --color-tdl15-acc: #d0612c;
  --color-tdl15-acc: oklch(0.62 0.16 45);
  --color-tdl15-accink: #a5461a;
  --color-tdl15-accink: oklch(0.52 0.15 42);
  --color-tdl15-good: #17804a;
  --color-tdl15-good: oklch(0.52 0.13 155);
  --color-tdl15-shadow: #7a5a44;
  --color-tdl15-shadow: oklch(0.45 0.07 50 / 0.55);
  --font-tdl15-sans: 'Lexend', system-ui, sans-serif;
}

.tdl-15 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-15 * {
    transition: none !important;
  }
}
```

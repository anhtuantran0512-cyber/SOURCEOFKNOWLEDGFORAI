---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/stack-of-three/"
title: "Stacked Tag Cluster Component"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The facepile pattern, generalized to tags: chips overlap with negative margins to compress a long list into a short strip, a cutout ring makes each layer…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked Tag Cluster Component
Source: https://codefronts.com/snippets/css-tags-chips/stack-of-three/

The facepile pattern, generalized to tags: chips overlap with negative margins to compress a long list into a short strip, a cutout ring makes each layer read as stacked paper, and the whole cluster fans open on hover or keyboard focus — margins spring apart with an overshooting bezier. A '+4' overflow chip is a real checkbox toggle that reveals the hidden tags with a pop cascade. Zero JavaScript, and the collapse maths is two CSS declarations.
## HTML
```html
<section class="ctc-09" aria-label="Stacked tag cluster demo">
  <div class="ctc-09__stage">
    <div class="ctc-09__wrap">
      <header class="ctc-09__head">
        <p class="ctc-09__kicker">Stacked clusters · negative margin + cutout ring</p>
        <h1>Seven tags in the space of three</h1>
      </header>
      <div class="ctc-09__panel">
        <p class="ctc-09__lab">01 · Tag stack — hover or Tab in to fan it open</p>
        <div class="ctc-09__cluster">
          <div class="ctc-09__stack">
            <a class="ctc-09__chip" style="--i:1;--h:255" href="#ctc09">react</a>
            <a class="ctc-09__chip" style="--i:2;--h:150" href="#ctc09">vite</a>
            <a class="ctc-09__chip" style="--i:3;--h:40" href="#ctc09">tailwind</a>
            <a class="ctc-09__chip" style="--i:4;--h:320" href="#ctc09">motion</a>
            <a class="ctc-09__chip ctc-09__chip--extra" style="--i:5;--h:200;--d:0" href="#ctc09">storybook</a>
            <a class="ctc-09__chip ctc-09__chip--extra" style="--i:6;--h:95;--d:1" href="#ctc09">playwright</a>
            <a class="ctc-09__chip ctc-09__chip--extra" style="--i:7;--h:10;--d:2" href="#ctc09">turborepo</a>
          </div>
          <input class="ctc-09__sr" type="checkbox" id="ctc09-more">
          <label class="ctc-09__more" for="ctc09-more" style="--i:8"><span data-closed>+3</span><span data-open>−</span></label>
        </div>
      </div>
      <div class="ctc-09__panel">
        <p class="ctc-09__lab">02 · Facepile — same CSS, round geometry, first face on top</p>
        <div class="ctc-09__row">
          <div class="ctc-09__stack ctc-09__stack--faces">
            <span class="ctc-09__face" style="--i:1;--h:250;--img:url(https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=60)"></span>
            <span class="ctc-09__face" style="--i:2;--h:330;--img:url(https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=120&q=60)"></span>
            <span class="ctc-09__face" style="--i:3;--h:20;--img:url(https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=120&q=60)"></span>
            <span class="ctc-09__face" style="--i:4;--h:140;--img:url(https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=60)"></span>
            <span class="ctc-09__face ctc-09__face--n" style="--i:5">+9</span>
          </div>
          <p class="ctc-09__cap">Reviewed by <b>Jonas, Mara + 11 others</b></p>
        </div>
      </div>
      <div class="ctc-09__panel">
        <p class="ctc-09__lab">03 · In context — a card row that stays one line tall no matter how many tags</p>
        <article class="ctc-09__card">
          <div><h3>Design tokens that survive a rebrand</h3><p>14 min read · Engineering</p></div>
          <div class="ctc-09__stack ctc-09__stack--mini">
            <span class="ctc-09__chip" style="--i:1;--h:255">tokens</span>
            <span class="ctc-09__chip" style="--i:2;--h:150">oklch</span>
            <span class="ctc-09__chip" style="--i:3;--h:40">theming</span>
            <span class="ctc-09__chip" style="--i:4;--h:320">figma</span>
          </div>
        </article>
      </div>
      <p class="ctc-09__note">The stack is two declarations — <code>margin-inline-start:-14px</code> and a border matching the surface. The fan-out is the same margin transitioning to <code>5px</code> on <code>:hover</code> / <code>:focus-within</code>.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-09,
.ctc-09 *,
.ctc-09 *::before,
.ctc-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-09 {
  --bg: oklch(0.97 0.007 250);
  --panel: oklch(0.998 0.002 250);
  --ink: oklch(0.24 0.025 255);
  --mut: oklch(0.5 0.02 255);
  --line: oklch(0.89 0.012 250);
  --acc: oklch(0.55 0.17 262);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-09__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 12% -10%,color-mix(in oklch,var(--acc) 12%,transparent),transparent 62%),var(--bg);
  container: ctc09/inline-size;
}

.ctc-09__wrap {
  width: min(700px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-09__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ctc-09__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ctc-09__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-09__panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-09__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 14px;
}

.ctc-09__cluster {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
}

.ctc-09__stack {
  display: flex;
  align-items: center;
}

.ctc-09__stack>* {
  margin-inline-start: -14px;
  z-index: calc(30 - var(--i,0));
  transition: margin .35s cubic-bezier(.34,1.56,.64,1),max-width .35s,opacity .25s,visibility .25s,scale .3s;
}

.ctc-09__stack>*:first-child {
  margin-inline-start: 0;
}

.ctc-09__stack:hover>*,
.ctc-09__stack:focus-within>* {
  margin-inline-start: 5px;
}

.ctc-09__stack:hover>*:first-child,
.ctc-09__stack:focus-within>*:first-child {
  margin-inline-start: 0;
}

.ctc-09__chip {
  --c: oklch(0.62 0.13 var(--h,255));
  display: inline-flex;
  align-items: center;
  min-height: 40px;
  max-width: 200px;
  padding: 0 16px;
  border-radius: 99px;
  border: 3px solid var(--panel);
  background: color-mix(in oklch,var(--c) 16%,oklch(1 0 0));
  color: color-mix(in oklch,var(--c) 72%,var(--ink));
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  white-space: nowrap;
  overflow: hidden;
}

a.ctc-09__chip:hover,
a.ctc-09__chip:focus-visible {
  background: color-mix(in oklch,var(--c) 26%,oklch(1 0 0));
  scale: 1.05;
  z-index: 40;
}

a.ctc-09__chip:focus-visible {
  outline: 2px solid var(--c);
  outline-offset: 1px;
}

.ctc-09__chip--extra {
  max-width: 0;
  padding-inline: 0;
  border-width: 0;
  opacity: 0;
  visibility: hidden;
  margin-inline-start: 0;
  transition-delay: calc(var(--d,0)*.04s);
}

.ctc-09__cluster:has(#ctc09-more:checked) .ctc-09__chip--extra {
  max-width: 200px;
  padding-inline: 16px;
  border-width: 3px;
  opacity: 1;
  visibility: visible;
  margin-inline-start: -14px;
}

.ctc-09__cluster:has(#ctc09-more:checked) .ctc-09__stack:hover .ctc-09__chip--extra,
.ctc-09__cluster:has(#ctc09-more:checked) .ctc-09__stack:focus-within .ctc-09__chip--extra {
  margin-inline-start: 5px;
}

.ctc-09__more {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 40px;
  min-width: 44px;
  padding: 0 12px;
  border-radius: 99px;
  border: 1.5px dashed color-mix(in oklch,var(--acc) 45%,var(--line));
  background: color-mix(in oklch,var(--acc) 8%,transparent);
  color: var(--acc);
  font-size: 13px;
  font-weight: 800;
  cursor: pointer;
  user-select: none;
  transition: background .2s,border-style .2s;
}

.ctc-09__more:hover {
  background: color-mix(in oklch,var(--acc) 15%,transparent);
  border-style: solid;
}

.ctc-09__cluster:has(#ctc09-more:focus-visible) .ctc-09__more {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ctc-09__more [data-open] {
  display: none;
}

.ctc-09__cluster:has(#ctc09-more:checked) .ctc-09__more [data-open] {
  display: inline;
}

.ctc-09__cluster:has(#ctc09-more:checked) .ctc-09__more [data-closed] {
  display: none;
}

.ctc-09__row {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.ctc-09__face {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  border: 3px solid var(--panel);
  background-image: var(--img,none),linear-gradient(140deg,oklch(0.68 0.12 var(--h,250)),oklch(0.5 0.13 calc(var(--h,250) + 45)));
  background-size: cover;
  background-position: center;
}

.ctc-09__face--n {
  display: grid;
  place-items: center;
  font-size: 12.5px;
  font-weight: 800;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 13%,oklch(1 0 0));
}

.ctc-09__cap {
  font-size: 13px;
  color: var(--mut);
}

.ctc-09__cap b {
  color: var(--ink);
  font-weight: 700;
}

.ctc-09__card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 14px 16px;
  background: oklch(0.985 0.004 250);
}

.ctc-09__card h3 {
  font-size: 14.5px;
  font-weight: 750;
  letter-spacing: -.01em;
}

.ctc-09__card p {
  font-size: 11.5px;
  color: var(--mut);
  margin-top: 3px;
}

.ctc-09__stack--mini .ctc-09__chip {
  min-height: 32px;
  font-size: 11.5px;
  padding: 0 12px;
  border-width: 2.5px;
}

.ctc-09__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid var(--acc);
  padding-left: 12px;
}

.ctc-09__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.92 0.01 250);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@container ctc09 (width < 480px) {
  .ctc-09__stack:hover>*,
    .ctc-09__stack:focus-within>* {
    margin-inline-start: -14px;
  }

  .ctc-09__card {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-09 * {
    transition-duration: .01ms !important;
    transition-delay: 0s !important;
  }
}
```

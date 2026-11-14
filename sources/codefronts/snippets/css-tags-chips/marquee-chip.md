---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/marquee-chip/"
title: "Scrolling Text Marquee Badge CSS"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The marquee, resurrected properly: the track holds its content TWICE, slides -50%, and loops with zero visible seam — the two-copy trick that every ticker on…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scrolling Text Marquee Badge CSS
Source: https://codefronts.com/snippets/css-tags-chips/marquee-chip/

The marquee, resurrected properly: the track holds its content TWICE, slides -50%, and loops with zero visible seam — the two-copy trick that every ticker on the web runs on. Fade-out edges come from a transparent-to-black mask on the pill (not overlaid gradients that break on any background), hover pauses the belt so it can actually be read, the duplicate copy is aria-hidden so screen readers hear the text once, and reduced-motion swaps the whole act for static text with an ellipsis.
## HTML
```html
<section class="ctc-21" aria-label="Scrolling marquee badge demo">
  <div class="ctc-21__stage">
    <div class="ctc-21__wrap">
      <header class="ctc-21__head">
        <p class="ctc-21__kicker">Marquee badges · two copies, −50%, no seam</p>
        <h1>Hover any belt to stop it</h1>
      </header>
      <div class="ctc-21__panel">
        <p class="ctc-21__lab">01 · Announcement pill — masked edges, pause on hover</p>
        <div class="ctc-21__row">
          <span class="ctc-21__pill" style="--t:9s"><span class="ctc-21__win"><span class="ctc-21__track"><span>Free shipping on orders over $50 ✦ 30-day returns ✦ New drops every Friday ✦ </span><span aria-hidden="true">Free shipping on orders over $50 ✦ 30-day returns ✦ New drops every Friday ✦ </span></span></span></span>
        </div>
      </div>
      <div class="ctc-21__panel">
        <p class="ctc-21__lab">02 · Status belts — same engine, three speeds, one reversed</p>
        <div class="ctc-21__col">
          <span class="ctc-21__pill ctc-21__pill--ok" style="--t:11s"><i class="ctc-21__dot"></i><span class="ctc-21__win"><span class="ctc-21__track"><span>All systems operational · API 42ms · CDN 8ms · DB 3ms · </span><span aria-hidden="true">All systems operational · API 42ms · CDN 8ms · DB 3ms · </span></span></span></span>
          <span class="ctc-21__pill ctc-21__pill--warn ctc-21__pill--rev" style="--t:7s"><i class="ctc-21__dot"></i><span class="ctc-21__win"><span class="ctc-21__track"><span>Elevated queue times in eu-west · retrying webhooks · </span><span aria-hidden="true">Elevated queue times in eu-west · retrying webhooks · </span></span></span></span>
          <span class="ctc-21__pill ctc-21__pill--live" style="--t:5s"><i class="ctc-21__dot ctc-21__dot--ping"></i><span class="ctc-21__win"><span class="ctc-21__track"><span>LIVE · Keynote starts in 12 min · 4,812 waiting · </span><span aria-hidden="true">LIVE · Keynote starts in 12 min · 4,812 waiting · </span></span></span></span>
        </div>
      </div>
      <p class="ctc-21__note">Spacing lives INSIDE each copy (padding-right on the spans) — flex gap on the track is the classic seam bug. Edges fade via <code>mask-image</code>, so this works over any background. Reduced motion gets static text.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-21,
.ctc-21 *,
.ctc-21 *::before,
.ctc-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-21 {
  --bg: oklch(0.2 0.02 275);
  --panel: oklch(0.245 0.022 275);
  --ink: oklch(0.95 0.008 275);
  --mut: oklch(0.65 0.02 275);
  --line: oklch(0.33 0.025 275);
  --acc: oklch(0.72 0.15 310);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-21__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 85% -10%,oklch(0.32 0.08 310/.45),transparent 62%),var(--bg);
  container: ctc21/inline-size;
}

.ctc-21__wrap {
  width: min(620px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-21__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ctc-21__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-21__panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-21__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 13px;
}

.ctc-21__row {
  display: flex;
}

.ctc-21__col {
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: flex-start;
}

.ctc-21__pill {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  max-width: 100%;
  padding: 0 16px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: oklch(1 0 0/.05);
  font-size: 13px;
  font-weight: 650;
}

.ctc-21__win {
  display: inline-block;
  overflow: hidden;
  max-width: min(380px,62cqi);
  white-space: nowrap;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
  mask-image: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
}

.ctc-21__track {
  display: inline-flex;
  white-space: nowrap;
  animation: ctc21-roll var(--t,9s) linear infinite;
}

.ctc-21__track>span {
  padding-right: 2.5em;
}

@keyframes ctc21-roll {
  to {
    translate: -50% 0;
  }
}

.ctc-21__pill:hover .ctc-21__track,
.ctc-21__pill:focus-visible .ctc-21__track {
  animation-play-state: paused;
}

.ctc-21__pill--rev .ctc-21__track {
  animation-direction: reverse;
}

.ctc-21__pill--ok {
  color: oklch(0.82 0.13 150);
  border-color: color-mix(in oklch,oklch(0.74 0.18 150) 35%,transparent);
  background: color-mix(in oklch,oklch(0.74 0.18 150) 9%,transparent);
}

.ctc-21__pill--warn {
  color: oklch(0.85 0.12 85);
  border-color: color-mix(in oklch,oklch(0.8 0.15 85) 35%,transparent);
  background: color-mix(in oklch,oklch(0.8 0.15 85) 9%,transparent);
}

.ctc-21__pill--live {
  color: oklch(0.82 0.15 25);
  border-color: color-mix(in oklch,oklch(0.62 0.23 25) 45%,transparent);
  background: color-mix(in oklch,oklch(0.62 0.23 25) 12%,transparent);
}

.ctc-21__dot {
  position: relative;
  flex: none;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: currentColor;
}

.ctc-21__dot--ping::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: inherit;
  animation: ctc21-ping 1.6s cubic-bezier(0,0,.2,1) infinite;
}

@keyframes ctc21-ping {
  to {
    scale: 2.5;
    opacity: 0;
  }
}

.ctc-21__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid var(--acc);
  padding-left: 12px;
}

.ctc-21__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(1 0 0/.09);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .ctc-21__track {
    animation: none;
  }

  .ctc-21__track>span[aria-hidden] {
    display: none;
  }

  .ctc-21__win {
    -webkit-mask-image: none;
    mask-image: none;
    text-overflow: ellipsis;
  }

  .ctc-21__dot--ping::before {
    animation: none;
  }
}
```

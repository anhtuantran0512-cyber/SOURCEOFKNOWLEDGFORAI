---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/minimal-dividers/"
title: "Subtle Faded Border-Bottom Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "The divider you should reach for by default in product UI: a hairline that fades to nothing at both ends, so a list of rows never looks like a spreadsheet."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Subtle Faded Border-Bottom Divider CSS
Source: https://codefronts.com/snippets/css-dividers/minimal-dividers/

The divider you should reach for by default in product UI: a hairline that fades to nothing at both ends, so a list of rows never looks like a spreadsheet. Two implementations — a gradient background (works everywhere) and a mask on a real border (keeps border semantics and adapts to any border colour) — plus the :last-child rule that stops the trailing rule everyone forgets.
## HTML
```html
<section class="div-19" aria-label="Subtle faded border-bottom divider demo">
  <div class="div-19__stage">
    <div class="div-19__panel">
      <h2 class="div-19__title">Recent activity</h2>
      <ul class="div-19__list">
        <li class="div-19__row"><span class="div-19__av" aria-hidden="true">M</span><span class="div-19__t">Merged <b>feat/divider-tokens</b></span><span class="div-19__ts">2m</span></li>
        <li class="div-19__row"><span class="div-19__av" aria-hidden="true">R</span><span class="div-19__t">Reviewed <b>mask-fade rules</b></span><span class="div-19__ts">18m</span></li>
        <li class="div-19__row"><span class="div-19__av" aria-hidden="true">D</span><span class="div-19__t">Deployed <b>collection page</b></span><span class="div-19__ts">1h</span></li>
        <li class="div-19__row"><span class="div-19__av" aria-hidden="true">O</span><span class="div-19__t">Opened <b>26 divider specs</b></span><span class="div-19__ts">3h</span></li>
      </ul>
      <div class="div-19__masked" role="separator" aria-label="Divider"></div>
      <p class="div-19__note">Above: gradient rules on <code>.row + .row</code>. Here: a masked 1px border.</p>
    </div>
    <p class="div-19__chip">adjacent-sibling rules · 12%/88% feather · no trailing rule</p>
  </div>
</section>
```
## CSS
```css
.div-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-19-bg);
  --div-19-bg: oklch(0.19 0.012 265);
  --div-19-card: oklch(0.235 0.014 265);
  --div-19-ink: oklch(0.95 0.006 260);
  --div-19-mut: oklch(0.64 0.015 262);
  --div-19-line: color-mix(in oklch,var(--div-19-ink) 22%,transparent);
  --div-19-acc: oklch(0.72 0.14 265);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-19-ink);
}

.div-19 *,
.div-19 *::before,
.div-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  list-style: none;
}

.div-19__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 20px;
  padding: clamp(24px,5vw,60px) clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% 0%,oklch(0.26 0.03 268/.7),transparent);
}

.div-19__panel {
  width: min(94vw,540px);
  background: var(--div-19-card);
  border: 1px solid oklch(1 0 0/.09);
  border-radius: 16px;
  padding: clamp(20px,4vw,28px);
  box-shadow: 0 22px 54px oklch(0 0 0/.4);
}

.div-19__title {
  font-size: 15px;
  font-weight: 650;
  letter-spacing: -.01em;
  margin-bottom: 6px;
  color: var(--div-19-mut);
}

.div-19__row {
  position: relative;
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 15px 2px;
  font-size: 14px;
}

.div-19__row+.div-19__row::before {
  content: '';
  position: absolute;
  inset: 0 0 auto;
  height: 1px;
  background: linear-gradient(90deg,transparent,var(--div-19-line) 12%,var(--div-19-line) 88%,transparent);
}

.div-19__av {
  width: 30px;
  height: 30px;
  flex: none;
  border-radius: 99px;
  display: grid;
  place-items: center;
  font-size: 12px;
  font-weight: 700;
  background: color-mix(in oklch,var(--div-19-acc) 26%,transparent);
  color: oklch(0.93 0.05 265);
}

.div-19__t {
  flex: 1;
  color: var(--div-19-mut);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.div-19__t b {
  color: var(--div-19-ink);
  font-weight: 600;
}

.div-19__ts {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--div-19-mut);
  opacity: .8;
}

.div-19__masked {
  height: 1px;
  margin: 20px 0 14px;
  border-bottom: 1px solid var(--div-19-line);
  -webkit-mask: linear-gradient(90deg,#0000,#000 10%,#000 90%,#0000);
  mask: linear-gradient(90deg,#0000,#000 10%,#000 90%,#0000);
}

.div-19__note {
  font-size: 12.5px;
  color: var(--div-19-mut);
  line-height: 1.6;
}

.div-19__note code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(1 0 0/.08);
  padding: 2px 6px;
  border-radius: 5px;
}

.div-19__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-19-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}
```

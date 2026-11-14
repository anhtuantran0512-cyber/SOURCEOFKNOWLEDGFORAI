---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-accordion-hybrid-details-summary/"
title: "Vertical Tabs Accordion Hybrid (Details/Summary)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "Start with markup that works before a single line of CSS loads — a stack of native <details> disclosures — then let CSS promote it to a two-column vertical…"
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tabs Accordion Hybrid (Details/Summary)
Source: https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-accordion-hybrid-details-summary/

Start with markup that works before a single line of CSS loads — a stack of native <details> disclosures — then let CSS promote it to a two-column vertical tab set on wide screens. The most robust pattern in this collection: no JS, no ARIA to get wrong, and full keyboard and screen-reader support straight from the HTML spec.
## HTML
```html
<section class="vt-08" aria-label="Details and summary tabs hybrid demo">
  <div class="vt-08__stage">
    <div class="vt-08__head">
      <p class="vt-08__eyebrow">&lt;details&gt; · @container · progressive enhancement</p>
      <h2 class="vt-08__title">Accordion first, tabs when there's room</h2>
    </div>
    <div class="vt-08__wrap">
      <div class="vt-08__set">
        <details class="vt-08__item" name="vt-08" open>
          <summary class="vt-08__sum"><span>Works before CSS</span><i class="vt-08__chev" aria-hidden="true"></i></summary>
          <div class="vt-08__body"><div class="vt-08__inner"><h3 class="vt-08__h">HTML that already works</h3><p class="vt-08__p">Disable every stylesheet and this is still a usable, keyboard-operable, screen-reader-friendly FAQ. Layout is the only thing CSS adds.</p></div></div>
        </details>
        <details class="vt-08__item" name="vt-08">
          <summary class="vt-08__sum"><span>Nothing re-implemented</span><i class="vt-08__chev" aria-hidden="true"></i></summary>
          <div class="vt-08__body"><div class="vt-08__inner"><h3 class="vt-08__h">The summary stays a summary</h3><p class="vt-08__p">Only the body moves. Enter and Space still toggle, expanded state is still exposed, and Chrome still force-opens closed panels for Ctrl+F.</p></div></div>
        </details>
        <details class="vt-08__item" name="vt-08">
          <summary class="vt-08__sum"><span>Exclusive by name</span><i class="vt-08__chev" aria-hidden="true"></i></summary>
          <div class="vt-08__body"><div class="vt-08__inner"><h3 class="vt-08__h">One open at a time</h3><p class="vt-08__p">A shared <code>name</code> makes the group behave like radio buttons, which is exactly what turns an accordion into tabs.</p></div></div>
        </details>
        <details class="vt-08__item" name="vt-08">
          <summary class="vt-08__sum"><span>Enhancement only</span><i class="vt-08__chev" aria-hidden="true"></i></summary>
          <div class="vt-08__body"><div class="vt-08__inner"><h3 class="vt-08__h">Fails to a plain accordion</h3><p class="vt-08__p">No container queries? Stacked disclosures. No <code>::details-content</code>? Instant open. Every fallback is still a finished component.</p></div></div>
        </details>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-08-bg);
  --vt-08-bg: oklch(0.955 0.014 145);
  --vt-08-card: oklch(1 0 0);
  --vt-08-ink: oklch(0.24 0.03 155);
  --vt-08-mut: oklch(0.52 0.025 155);
  --vt-08-acc: oklch(0.52 0.13 158);
  --vt-08-line: oklch(0.24 0.03 155/.13);
  interpolate-size: allow-keywords;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-08-ink);
}

.vt-08 *,
.vt-08 *::before,
.vt-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-08__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(16px,2.6vw,28px);
  padding: clamp(20px,5vw,64px);
  background: radial-gradient(80% 55% at 50% 100%,oklch(0.93 0.06 155/.7),transparent);
}

.vt-08__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
  max-width: 54ch;
}

.vt-08__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--vt-08-acc);
}

.vt-08__title {
  font-size: clamp(24px,3.6vw,38px);
  line-height: 1.08;
  letter-spacing: -.028em;
  font-weight: 700;
  text-wrap: balance;
}

.vt-08__wrap {
  container-type: inline-size;
  width: min(94vw,860px);
}

.vt-08__set {
  background: var(--vt-08-card);
  border: 1px solid var(--vt-08-line);
  border-radius: 18px;
  box-shadow: 0 22px 62px -32px oklch(0.24 0.03 155/.42);
  overflow: hidden;
}

.vt-08__item+.vt-08__item {
  border-top: 1px solid var(--vt-08-line);
}

.vt-08__sum {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 56px;
  padding: 0 18px;
  font-size: 14.8px;
  font-weight: 650;
  color: var(--vt-08-mut);
  cursor: pointer;
  list-style: none;
  transition: color .2s ease,background .2s ease;
}

.vt-08__sum::-webkit-details-marker {
  display: none;
}

.vt-08__sum:hover {
  color: var(--vt-08-ink);
  background: oklch(0.24 0.03 155/.04);
}

.vt-08__sum:focus-visible {
  outline: 2px solid var(--vt-08-acc);
  outline-offset: -3px;
}

.vt-08__chev {
  inline-size: 9px;
  block-size: 9px;
  flex: none;
  border-right: 2px solid currentColor;
  border-bottom: 2px solid currentColor;
  rotate: -45deg;
  transition: rotate .3s cubic-bezier(.32,.72,.3,1);
}

.vt-08__item[open]>.vt-08__sum {
  color: var(--vt-08-acc);
  background: color-mix(in oklch,var(--vt-08-acc) 9%,transparent);
}

.vt-08__item[open]>.vt-08__sum .vt-08__chev {
  rotate: 45deg;
}

.vt-08__inner {
  display: grid;
  gap: 10px;
  padding: 4px 18px 20px;
}

.vt-08__h {
  font-size: clamp(17px,2.1vw,22px);
  line-height: 1.24;
  letter-spacing: -.02em;
  font-weight: 680;
  text-wrap: balance;
}

.vt-08__p {
  max-width: 48ch;
  font-size: 14.6px;
  line-height: 1.64;
  color: var(--vt-08-mut);
  text-wrap: pretty;
}

.vt-08__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.24 0.03 155/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.vt-08__item::details-content {
  block-size: 0;
  overflow: hidden;
  opacity: 0;
  transition: block-size .34s cubic-bezier(.32,.72,.3,1),opacity .3s ease,content-visibility .34s allow-discrete;
}

.vt-08__item[open]::details-content {
  block-size: auto;
  opacity: 1;
}

@container (min-width: 700px) {
  .vt-08__set {
    position: relative;
    padding-inline-end: 60%;
    min-height: clamp(250px,30vw,290px);
  }

  .vt-08__set::after {
    content: "";
    position: absolute;
    inset: 0 0 0 40%;
    border-left: 1px solid var(--vt-08-line);
    pointer-events: none;
  }

  .vt-08__item {
    border-top: 0;
  }

  .vt-08__item+.vt-08__item {
    border-top: 1px solid var(--vt-08-line);
  }

  .vt-08__chev {
    rotate: -45deg;
    opacity: .45;
  }

  .vt-08__item[open]>.vt-08__sum .vt-08__chev {
    rotate: -45deg;
    opacity: 1;
  }

  .vt-08__item[open]>.vt-08__sum {
    box-shadow: inset 3px 0 0 var(--vt-08-acc);
  }

  .vt-08__body {
    position: absolute;
    inset: 0 0 0 40%;
    display: grid;
    align-content: center;
    overflow: auto;
  }

  .vt-08__inner {
    padding: clamp(20px,3vw,36px);
    animation: vt-08-in .34s cubic-bezier(.32,.72,.3,1) both;
  }

  .vt-08__item::details-content {
    block-size: auto;
    opacity: 1;
    overflow: visible;
  }
}

@keyframes vt-08-in {
  from {
    opacity: 0;
    translate: 10px 0;
  }

  to {
    opacity: 1;
    translate: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-08 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/icon-only-vertical-tabs-with-tooltips-mini-sidebar/"
title: "Icon-Only Vertical Tabs with Tooltips (Mini Sidebar)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "The 64px collapsed rail every IDE and admin console ships, done properly: icon-only triggers whose names are always available to assistive tech, with…"
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Icon-Only Vertical Tabs with Tooltips (Mini Sidebar)
Source: https://codefronts.com/navigation/css-vertical-tabs/icon-only-vertical-tabs-with-tooltips-mini-sidebar/

The 64px collapsed rail every IDE and admin console ships, done properly: icon-only triggers whose names are always available to assistive tech, with tooltips that appear on hover AND keyboard focus, escape the scroll container, and never get clipped by overflow. The tooltip is a pseudo-element pair, so each tab costs one line of markup.
## HTML
```html
<section class="vt-04" aria-label="Icon-only vertical tabs with tooltips demo">
  <div class="vt-04__stage">
    <div class="vt-04__card" role="radiogroup" aria-label="Editor panels">
      <nav class="vt-04__rail">
        <input class="vt-04__radio" type="radio" name="vt-04" id="vt-04-t1" checked>
        <label class="vt-04__tab" for="vt-04-t1" data-tip="Explorer"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M3 6.5A1.5 1.5 0 0 1 4.5 5h4l2 2.5h9A1.5 1.5 0 0 1 21 9v9a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18z" stroke-width="1.7" stroke-linejoin="round"/></svg><span class="vt-04__sr">Explorer</span></label>
        <input class="vt-04__radio" type="radio" name="vt-04" id="vt-04-t2">
        <label class="vt-04__tab" for="vt-04-t2" data-tip="Search"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.2" stroke-width="1.7"/><path d="m20 20-4.4-4.4" stroke-width="1.7" stroke-linecap="round"/></svg><span class="vt-04__sr">Search</span></label>
        <input class="vt-04__radio" type="radio" name="vt-04" id="vt-04-t3">
        <label class="vt-04__tab" for="vt-04-t3" data-tip="Source control"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="7" cy="6.5" r="2.6" stroke-width="1.7"/><circle cx="7" cy="18" r="2.6" stroke-width="1.7"/><circle cx="17" cy="10" r="2.6" stroke-width="1.7"/><path d="M7 9.1v6.3m0-3.2h5.6a2 2 0 0 0 2-2V12" stroke-width="1.7" stroke-linecap="round"/></svg><span class="vt-04__sr">Source control</span></label>
        <input class="vt-04__radio" type="radio" name="vt-04" id="vt-04-t4">
        <label class="vt-04__tab" for="vt-04-t4" data-tip="Extensions"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 8h5V4.5a1.5 1.5 0 0 1 3 0V8h5v5h3.5a1.5 1.5 0 0 1 0 3H17v4H4z" stroke-width="1.7" stroke-linejoin="round"/></svg><span class="vt-04__sr">Extensions</span></label>
      </nav>
      <div class="vt-04__panels">
        <article class="vt-04__panel" id="vt-04-p1"><p class="vt-04__kicker">Explorer</p><h3 class="vt-04__h">One attribute per tooltip</h3><p class="vt-04__p"><code>content:attr(data-tip)</code> renders the label from the element itself — adding a tab means adding one attribute, not a second node.</p></article>
        <article class="vt-04__panel" id="vt-04-p2"><p class="vt-04__kicker">Search</p><h3 class="vt-04__h">Hover is not enough</h3><p class="vt-04__p">Every tip also fires on <code>:focus-visible</code>. Tab through the rail with the keyboard and watch each name appear.</p></article>
        <article class="vt-04__panel" id="vt-04-p3"><p class="vt-04__kicker">Source control</p><h3 class="vt-04__h">The name lives in the DOM</h3><p class="vt-04__p">A 1px-clipped span carries the accessible name. Pseudo-element text is not dependably exposed to screen readers.</p></article>
        <article class="vt-04__panel" id="vt-04-p4"><p class="vt-04__kicker">Extensions</p><h3 class="vt-04__h">Escape the clip</h3><p class="vt-04__p">The rail keeps <code>overflow:visible</code> and isolates its own stacking context, so tips never get sliced by a rounded corner.</p></article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-04-bg);
  --vt-04-bg: oklch(0.19 0.018 275);
  --vt-04-card: oklch(0.235 0.022 275);
  --vt-04-rail-bg: oklch(0.205 0.02 275);
  --vt-04-ink: oklch(0.96 0.008 275);
  --vt-04-mut: oklch(0.68 0.02 275);
  --vt-04-acc: oklch(0.72 0.16 258);
  --vt-04-line: oklch(1 0 0/.1);
  --vt-04-rail: 64px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-04-ink);
}

.vt-04 *,
.vt-04 *::before,
.vt-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-04__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: clamp(20px,5vw,64px);
  background: radial-gradient(70% 50% at 30% 0%,oklch(0.32 0.07 268/.7),transparent);
}

.vt-04__card {
  width: min(94vw,820px);
  display: grid;
  grid-template-columns: var(--vt-04-rail) 1fr;
  background: var(--vt-04-card);
  border: 1px solid var(--vt-04-line);
  border-radius: 18px;
  box-shadow: 0 28px 70px -34px oklch(0 0 0/.8);
  isolation: isolate;
}

.vt-04__rail {
  display: grid;
  align-content: start;
  gap: 6px;
  padding: 12px 0;
  background: var(--vt-04-rail-bg);
  border-right: 1px solid var(--vt-04-line);
  border-radius: 18px 0 0 18px;
  overflow: visible;
}

.vt-04__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.vt-04__tab {
  position: relative;
  justify-self: center;
  display: grid;
  place-items: center;
  inline-size: 46px;
  block-size: 46px;
  border-radius: 13px;
  color: var(--vt-04-mut);
  cursor: pointer;
  transition: color .2s ease,background .2s ease,transform .2s ease;
}

.vt-04__tab svg {
  inline-size: 21px;
  block-size: 21px;
  flex: none;
  stroke: currentColor;
}

.vt-04__tab::before {
  content: "";
  position: absolute;
  inset-inline-start: -9px;
  inset-block: 11px auto;
  block-size: 24px;
  inline-size: 3px;
  border-radius: 99px;
  background: var(--vt-04-acc);
  scale: 1 0;
  transition: scale .28s cubic-bezier(.32,.72,.3,1);
}

.vt-04__tab::after {
  content: attr(data-tip);
  position: absolute;
  inset-inline-start: calc(100% + 14px);
  inset-block-start: 50%;
  translate: -4px -50%;
  z-index: 5;
  padding: 7px 11px;
  border-radius: 9px;
  background: oklch(0.14 0.015 275);
  border: 1px solid var(--vt-04-line);
  color: var(--vt-04-ink);
  font-size: 12.5px;
  font-weight: 600;
  white-space: nowrap;
  opacity: 0;
  scale: .94;
  pointer-events: none;
  box-shadow: 0 10px 26px -10px oklch(0 0 0/.85);
  transition: opacity .16s ease,scale .16s ease,translate .16s ease;
}

.vt-04__tab:hover {
  color: var(--vt-04-ink);
  background: oklch(1 0 0/.06);
}

.vt-04__tab:hover::after,
.vt-04__radio:focus-visible+.vt-04__tab::after {
  opacity: 1;
  scale: 1;
  translate: 0 -50%;
}

.vt-04__radio:checked+.vt-04__tab {
  color: var(--vt-04-acc);
  background: color-mix(in oklch,var(--vt-04-acc) 15%,transparent);
}

.vt-04__radio:checked+.vt-04__tab::before {
  scale: 1 1;
}

.vt-04__radio:focus-visible+.vt-04__tab {
  outline: 2px solid var(--vt-04-acc);
  outline-offset: 2px;
}

.vt-04__panels {
  display: grid;
  min-height: clamp(240px,32vw,286px);
  padding: clamp(22px,3.6vw,42px);
}

.vt-04__panel {
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 11px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: opacity .3s ease,transform .34s cubic-bezier(.32,.72,.3,1),visibility 0s .34s;
}

.vt-04__card:has(#vt-04-t1:checked) #vt-04-p1,
.vt-04__card:has(#vt-04-t2:checked) #vt-04-p2,
.vt-04__card:has(#vt-04-t3:checked) #vt-04-p3,
.vt-04__card:has(#vt-04-t4:checked) #vt-04-p4 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s;
}

.vt-04__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--vt-04-acc);
}

.vt-04__h {
  font-size: clamp(19px,2.4vw,25px);
  line-height: 1.2;
  letter-spacing: -.022em;
  font-weight: 680;
  text-wrap: balance;
}

.vt-04__p {
  max-width: 44ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--vt-04-mut);
  text-wrap: pretty;
}

.vt-04__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .vt-04 * {
    transition-duration: .01ms !important;
  }
}
```

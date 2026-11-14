---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/inkwell-modal/"
title: "Inkwell Dark Mode Modal Dialog"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "An editorial take on the confirmation dialog: deep navy rather than neutral black, warm off-white ink rather than pure white, a serif display headline over a…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inkwell Dark Mode Modal Dialog
Source: https://codefronts.com/design-styles/css-dark-mode-ui/inkwell-modal/

An editorial take on the confirmation dialog: deep navy rather than neutral black, warm off-white ink rather than pure white, a serif display headline over a sans body. The palette is borrowed from newspaper dark modes, where warmth is what keeps long-form text comfortable — and it turns a destructive prompt into something that reads considered instead of alarming.
## HTML
```html
<div class="dmu-13">
  <div class="dmu-13__stage">
    <div class="dmu-13__page">
      <p class="dmu-13__eyebrow">Workspace &middot; Danger zone</p>
      <h1 class="dmu-13__pageTitle">The Atlantic Review</h1>
      <p class="dmu-13__pageBody">Eleven editors, four hundred drafts and a decade of archives live in this workspace. Removing it is permanent, so the confirmation is deliberately slow to read.</p>

      <details class="dmu-13__d">
        <summary class="dmu-13__open">
          <span class="dmu-13__openBody">Delete workspace</span>
          <span class="dmu-13__dismiss" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11"/></svg>
          </span>
        </summary>

        <div class="dmu-13__sheet" role="dialog" aria-labelledby="dmu-13-t" aria-describedby="dmu-13-b">
          <span class="dmu-13__seal" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.4 19.6 7v6.4c0 3.6-3 6-7.6 7.2-4.6-1.2-7.6-3.6-7.6-7.2V7Z"/><path d="M12 9.2v4.1M12 15.8v.1"/></svg>
          </span>
          <h2 class="dmu-13__title" id="dmu-13-t">Delete <em>The Atlantic Review</em>?</h2>
          <p class="dmu-13__body" id="dmu-13-b">Every draft, comment thread and published piece will be removed from our servers within 24 hours. Exports created before today remain valid for 30 days.</p>

          <ul class="dmu-13__list">
            <li><span aria-hidden="true">&mdash;</span>412 drafts and 1,908 revisions</li>
            <li><span aria-hidden="true">&mdash;</span>11 editors lose access immediately</li>
            <li><span aria-hidden="true">&mdash;</span>Custom domain released after 24 hours</li>
          </ul>

          <div class="dmu-13__actions">
            <button class="dmu-13__btn" type="button">Keep workspace</button>
            <button class="dmu-13__btn dmu-13__btn--danger" type="button">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4.8 7.6h14.4M9.6 7.6V5.4h4.8v2.2M6.8 7.6l.9 11.8h8.6l.9-11.8"/></svg>
              Delete permanently
            </button>
          </div>
          <p class="dmu-13__fine">Requires owner privileges &middot; logged to the audit trail</p>
        </div>
      </details>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap');

.dmu-13 {
  --navy: #0b0e18;
  --page: #101427;
  --sheet: #141a2e;
  --ink: #f4f1e8;
  --muted: #a2a8bf;
  --rule: rgba(244,241,232,.22);
  --hair: rgba(244,241,232,.12);
  --danger: #ff8f7a;
  --danger-ink: #2a0b06;
  --focus: #8ab4ff;
  --scrim: rgba(4,6,14,.78);
  --serif: "Instrument Serif","Iowan Old Style","Palatino Linotype",Georgia,serif;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(120% 80% at 20% 0%,#131832,var(--navy) 62%),var(--navy);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-13,
.dmu-13 *,
.dmu-13 *::before,
.dmu-13 *::after {
  box-sizing: border-box;
}

.dmu-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-13__page {
  width: min(46rem,100%);
  display: grid;
  gap: .75rem;
  padding: clamp(1.5rem,4vw,2.75rem);
  border-radius: 1.2rem;
  background: var(--page);
  border: 1px solid var(--hair);
}

.dmu-13__eyebrow {
  margin: 0;
  font-size: .72rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-13__pageTitle {
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(2rem,5vw,3rem);
  font-weight: 400;
  letter-spacing: -.02em;
  line-height: 1.05;
}

.dmu-13__pageBody {
  margin: .2rem 0 .6rem;
  font-size: .95rem;
  line-height: 1.7;
  color: var(--muted);
  max-width: 52ch;
  text-wrap: pretty;
}

.dmu-13__d summary {
  list-style: none;
}

.dmu-13__d summary::-webkit-details-marker {
  display: none;
}

.dmu-13__open {
  display: inline-flex;
  cursor: pointer;
}

.dmu-13__openBody {
  display: inline-flex;
  align-items: center;
  min-height: 2.9rem;
  padding: 0 1.2rem;
  border-radius: 999px;
  font-size: .88rem;
  font-weight: 500;
  letter-spacing: .01em;
  color: var(--danger);
  border: 1px solid color-mix(in oklab,var(--danger) 45%,transparent);
  transition: background-color .22s ease, translate .22s ease;
}

.dmu-13__open:hover .dmu-13__openBody {
  background: color-mix(in oklab,var(--danger) 14%,transparent);
  translate: 0 -1px;
}

.dmu-13__open:focus-visible {
  outline: none;
}

.dmu-13__open:focus-visible .dmu-13__openBody {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-13__dismiss {
  display: none;
}

.dmu-13__d[open] .dmu-13__openBody {
  opacity: .3;
}

.dmu-13__d[open] .dmu-13__open::after {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 5;
  background: var(--scrim);
  -webkit-backdrop-filter: blur(6px) saturate(.85);
  backdrop-filter: blur(6px) saturate(.85);
}

.dmu-13__d[open] .dmu-13__dismiss {
  position: fixed;
  z-index: 7;
  top: 1.15rem;
  right: 1.15rem;
  display: grid;
  place-items: center;
  width: 2.6rem;
  height: 2.6rem;
  border-radius: 50%;
  color: var(--ink);
  background: var(--sheet);
  border: 1px solid var(--hair);
}

.dmu-13__dismiss svg {
  width: 1rem;
  height: 1rem;
}

.dmu-13__sheet {
  position: fixed;
  z-index: 6;
  top: 50%;
  left: 50%;
  translate: -50% -50%;
  width: min(33rem,calc(100% - 2rem));
  max-height: min(88vh,44rem);
  overflow: auto;
  display: grid;
  gap: .7rem;
  padding: clamp(1.4rem,3.5vw,2rem);
  border-radius: 1.1rem;
  background: linear-gradient(180deg,var(--sheet),var(--page));
  color: var(--ink);
  border: 1px solid var(--hair);
  box-shadow: 0 50px 90px -50px rgba(0,0,0,.9);
  opacity: 1;
  scale: 1;
  transition: opacity .26s ease, scale .26s cubic-bezier(.16,1,.3,1);
}

.dmu-13__sheet::before {
  content: '';
  position: absolute;
  inset: 0 0 auto;
  height: 1px;
  background: linear-gradient(90deg,transparent,var(--rule),transparent);
}

@starting-style {
  .dmu-13__d[open] .dmu-13__sheet {
    opacity: 0;
    scale: .97;
  }
}

.dmu-13__seal {
  display: grid;
  place-items: center;
  width: 2.6rem;
  height: 2.6rem;
  border-radius: 50%;
  color: var(--danger);
  border: 1px solid color-mix(in oklab,var(--danger) 40%,transparent);
}

.dmu-13__seal svg {
  width: 1.3rem;
  height: 1.3rem;
}

.dmu-13__title {
  margin: .2rem 0 0;
  font-family: var(--serif);
  font-size: clamp(1.5rem,3.6vw,2rem);
  font-weight: 400;
  line-height: 1.15;
  letter-spacing: -.01em;
}

.dmu-13__title em {
  font-style: italic;
}

.dmu-13__body {
  margin: 0;
  font-size: .9rem;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.dmu-13__list {
  margin: .2rem 0 .3rem;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .35rem;
  font-size: .83rem;
  color: var(--ink);
}

.dmu-13__list li {
  display: grid;
  grid-template-columns: 1rem 1fr;
  gap: .5rem;
}

.dmu-13__list span {
  color: var(--muted);
}

.dmu-13__actions {
  display: flex;
  gap: .55rem;
  flex-wrap: wrap;
  margin-top: .35rem;
}

.dmu-13__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-height: 2.85rem;
  padding: 0 1.1rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .86rem;
  font-weight: 500;
  background: transparent;
  color: var(--ink);
  border: 1px solid var(--hair);
  transition: background-color .2s ease, translate .2s ease;
}

.dmu-13__btn svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-13__btn:hover {
  translate: 0 -1px;
  background: rgba(244,241,232,.06);
}

.dmu-13__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-13__btn--danger {
  background: var(--danger);
  color: var(--danger-ink);
  border-color: transparent;
  font-weight: 600;
}

.dmu-13__btn--danger:hover {
  background: color-mix(in oklab,var(--danger) 88%,white);
}

.dmu-13__fine {
  margin: .15rem 0 0;
  font-size: .74rem;
  letter-spacing: .02em;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-13__sheet,
    .dmu-13__btn,
    .dmu-13__openBody {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-13__sheet,
    .dmu-13__page {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-13__d[open] .dmu-13__open::after {
    background: Canvas;
    backdrop-filter: none;
  }

  .dmu-13__btn--danger {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
```

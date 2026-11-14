---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-confirm-delete-button/"
title: "CSS Confirm Delete Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A destructive action that asks once, inline, without a modal: the delete button expands to reveal \"Cancel / Yes, delete\" with the confirm option deliberately…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Confirm Delete Button
Source: https://codefronts.com/components/css-buttons/css-confirm-delete-button/

A destructive action that asks once, inline, without a modal: the delete button expands to reveal "Cancel / Yes, delete" with the confirm option deliberately placed second and never under the original cursor position. Grid-track animation, a checkbox for state, and a lid-flip trash icon — all pure CSS.
## HTML
```html
<div class="cb-12">
  <div class="cb-12__stage">
    <span class="cb-12__shell">
      <label class="cb-12__trigger">
        <input type="checkbox" aria-label="Delete this project, requires confirmation">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <g class="cb-12__lid"><path d="M4.5 7h15"/><path d="M9.5 7V5.2A1.2 1.2 0 0 1 10.7 4h2.6a1.2 1.2 0 0 1 1.2 1.2V7"/></g>
          <path d="M6.5 7.8 7.4 19a1.5 1.5 0 0 0 1.5 1.4h6.2a1.5 1.5 0 0 0 1.5-1.4l.9-11.2"/><path d="M10.5 11v6M13.5 11v6"/>
        </svg>
        <span class="cb-12__triggerLabel">Delete project</span>
      </label>
      <span class="cb-12__confirm">
        <span class="cb-12__confirmInner">
          <span class="cb-12__ask">Sure?</span>
          <button class="cb-12__yes" type="button">Yes, delete</button>
        </span>
      </span>
    </span>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700&display=swap');

.cb-12 {
  --bg: #f6f5f3;
  --surface: #ffffff;
  --line: #e3e1dc;
  --text: #1a1817;
  --muted: #6d6862;
  --danger: #b91c1c;
  --danger-ink: #ffffff;
  --radius: .75rem;
  --sans: "Schibsted Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-12 {
    --bg: oklch(96.8% .004 90);
    --danger: oklch(48% .2 27);
    --line: oklch(90% .008 90);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-12:not([data-theme="light"]) {
    --bg: #0d0c0c;
    --surface: #171514;
    --line: #2b2827;
    --text: #f4f1ee;
    --muted: #a29b95;
    --danger: #ef4444;
    --danger-ink: #180505;
  }
}

.cb-12[data-theme="dark"] {
  --bg: #0d0c0c;
  --surface: #171514;
  --line: #2b2827;
  --text: #f4f1ee;
  --muted: #a29b95;
  --danger: #ef4444;
  --danger-ink: #180505;
}

.cb-12,
.cb-12 *,
.cb-12 *::before,
.cb-12 *::after {
  box-sizing: border-box;
}

.cb-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-12__shell {
  display: grid;
  grid-template-columns: auto 0fr;
  align-items: center;
  padding: .35rem;
  border-radius: calc(var(--radius) + .35rem);
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 14px 34px -22px color-mix(in oklab,var(--text) 65%,transparent);
  transition: grid-template-columns .45s cubic-bezier(.16,1,.3,1), border-color .3s ease;
}

.cb-12__trigger {
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-height: 2.75rem;
  padding: 0 1rem;
  border-radius: var(--radius);
  font-size: .9375rem;
  font-weight: 600;
  color: var(--muted);
  transition: color .22s ease, background-color .22s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-12__trigger input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cb-12__trigger svg {
  width: 1.2rem;
  height: 1.2rem;
  flex: none;
}

.cb-12__lid {
  transform-origin: 18% 60%;
  transition: rotate .38s cubic-bezier(.16,1,.3,1), translate .38s cubic-bezier(.16,1,.3,1);
}

.cb-12__trigger:hover {
  color: var(--danger);
  background: color-mix(in oklab,var(--danger) 8%,transparent);
}

.cb-12__shell:has(input:focus-visible) {
  outline: 2px solid var(--danger);
  outline-offset: 3px;
}

.cb-12__shell:has(input:checked) {
  grid-template-columns: auto 1fr;
  border-color: color-mix(in oklab,var(--danger) 45%,var(--line));
}

.cb-12__shell:has(input:checked) .cb-12__trigger {
  color: var(--danger);
}

.cb-12__shell:has(input:checked) .cb-12__lid {
  rotate: -24deg;
  translate: -1px -1.5px;
}

.cb-12__shell:has(input:checked) .cb-12__triggerLabel {
  text-decoration: line-through;
  text-decoration-color: color-mix(in oklab,var(--danger) 60%,transparent);
}

.cb-12__confirm {
  min-width: 0;
  overflow: hidden;
}

.cb-12__confirmInner {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding-left: .5rem;
  padding-right: .15rem;
  opacity: 0;
  translate: -.5rem 0;
  transition: opacity .3s ease .08s, translate .4s cubic-bezier(.16,1,.3,1) .08s;
}

.cb-12__shell:has(input:checked) .cb-12__confirmInner {
  opacity: 1;
  translate: 0 0;
}

.cb-12__ask {
  font-size: .8125rem;
  font-weight: 600;
  color: var(--muted);
  white-space: nowrap;
}

.cb-12__yes {
  cursor: pointer;
  white-space: nowrap;
  border: 0;
  border-radius: var(--radius);
  min-height: 2.75rem;
  padding: 0 1.1rem;
  font: inherit;
  font-size: .875rem;
  font-weight: 700;
  color: var(--danger-ink);
  background: var(--danger);
  box-shadow: 0 8px 18px -12px color-mix(in oklab,var(--danger) 85%,transparent);
  transition: background-color .2s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.cb-12__yes:hover {
  background: color-mix(in oklab,var(--danger) 85%,black);
  translate: 0 -1px;
}

.cb-12__yes:active {
  translate: 0 1px;
}

.cb-12__yes:focus-visible {
  outline: 2px solid var(--danger);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-12__shell,
    .cb-12__confirmInner,
    .cb-12__lid,
    .cb-12__yes,
    .cb-12__trigger {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-12__shell {
    border: 1px solid ButtonText;
  }

  .cb-12__yes {
    background: Highlight;
    color: HighlightText;
  }
}
```

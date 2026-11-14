---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-feature-section-with-code-preview/"
title: "Feature Section with Code Preview Snippet"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "Three feature callouts on the left, a component-usage snippet on the right with a filename tab and a copy button."
has_js: "true"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section with Code Preview Snippet
Source: https://codefronts.com/layouts/css-feature-sections/css-feature-section-with-code-preview/

Three feature callouts on the left, a component-usage snippet on the right with a filename tab and a copy button. Syntax colour is hand-applied spans in a near-monochrome palette with one emerald accent, and the copy button feature-detects the clipboard so a blocked or insecure context gets a select-the-code fallback rather than a dead control.
## HTML
```html
<section class="fs-17" aria-labelledby="fs-17-heading">
  <div class="fs-17__hero" aria-hidden="true">
    <span class="fs-17__wordmark">Basalt UI</span>
    <span class="fs-17__heronav">components · primitives · themes</span>
  </div>

  <div class="fs-17__stage">
    <div class="fs-17__head">
      <p class="fs-17__eyebrow">Composition, not configuration</p>
      <h2 class="fs-17__heading" id="fs-17-heading">Primitives you own, styled with your tokens</h2>
    </div>

    <div class="fs-17__split">
      <ul class="fs-17__callouts">
        <li class="fs-17__callout">
          <span class="fs-17__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 7h16M4 12h16M4 17h10"/></svg></span>
          <h3 class="fs-17__ctitle">Copied in, not installed</h3>
          <p class="fs-17__cprose">The component lands in your repository as source. Edit it, delete a prop, fork it — no wrapper, no upgrade fear.</p>
        </li>
        <li class="fs-17__callout">
          <span class="fs-17__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M9 12h6"/></svg></span>
          <h3 class="fs-17__ctitle">Accessible by construction</h3>
          <p class="fs-17__cprose">Focus management, roles and keyboard behaviour come from the primitive underneath, tested against three screen readers.</p>
        </li>
        <li class="fs-17__callout">
          <span class="fs-17__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="8"/><path d="M12 8v8M8 12h8"/></svg></span>
          <h3 class="fs-17__ctitle">Themed by custom properties</h3>
          <p class="fs-17__cprose">One token file drives radius, spacing and colour across every component. No build-time theme generation.</p>
        </li>
      </ul>

      <div class="fs-17__codepane">
        <div class="fs-17__tabs">
          <span class="fs-17__tab" data-active>invoice-row.tsx</span>
          <span class="fs-17__tab">tokens.css</span>
          <button class="fs-17__copy" type="button">Copy</button>
        </div>
        <pre class="fs-17__pre"><code class="fs-17__code" id="fs-17-code"><span class="fs-17__c">// three primitives, one row</span>
<span class="fs-17__k">import</span> { Row, Badge, Menu } <span class="fs-17__k">from</span> <span class="fs-17__s">"@basalt/ui"</span>;

<span class="fs-17__k">export function</span> <span class="fs-17__f">InvoiceRow</span>({ invoice }) {
  <span class="fs-17__k">return</span> (
    &lt;Row <span class="fs-17__a">interactive</span> <span class="fs-17__a">href</span>={<span class="fs-17__s">"/i/"</span> + invoice.id}&gt;
      &lt;Row.<span class="fs-17__f">Cell</span> <span class="fs-17__a">weight</span>=<span class="fs-17__s">"medium"</span>&gt;{invoice.number}&lt;/Row.Cell&gt;
      &lt;Badge <span class="fs-17__a">tone</span>={invoice.overdue ? <span class="fs-17__s">"danger"</span> : <span class="fs-17__s">"neutral"</span>}&gt;
        {invoice.status}
      &lt;/Badge&gt;
      &lt;Menu <span class="fs-17__a">label</span>=<span class="fs-17__s">"Invoice actions"</span> <span class="fs-17__a">align</span>=<span class="fs-17__s">"end"</span> /&gt;
    &lt;/Row&gt;
  );
}</code></pre>
        <p class="fs-17__status" data-status hidden>Clipboard blocked here — the code is selected, press copy in your browser.</p>
      </div>
    </div>
  </div>

  <div class="fs-17__below" aria-hidden="true">44 components · source lives in your repo · CLI</div>
</section>
```
## CSS
```css
.fs-17 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #0c0c0d;
  --bg: oklch(0.16 0.002 285);
  --pane: #131315;
  --pane: oklch(0.19 0.003 285);
  --ink: #ededee;
  --muted: #8e8e93;
  --muted: oklch(0.65 0.003 285);
  --rule: #26262a;
  --rule: oklch(0.28 0.004 285);
  --accent: #45d483;
  --accent: oklch(0.8 0.16 155);
  --pad: 11px;
  --font-display: "JetBrains Mono", "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-17 *,
.fs-17 *::before,
.fs-17 *::after {
  box-sizing: border-box;
}

.fs-17__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 14px;
  justify-content: space-between;
  align-items: baseline;
  padding: var(--pad) 14px;
  border-block-end: 1px solid var(--rule);
  font: 500 11.5px/1 var(--font-display);
  color: var(--muted);
}

.fs-17__wordmark {
  color: var(--ink);
}

.fs-17__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(24px, 4.5vw, 50px) 12px;
}

.fs-17__head {
  inline-size: 100%;
  max-inline-size: 72rem;
  min-inline-size: 0;
  margin: 0 0 18px;
}

.fs-17__eyebrow {
  margin: 0 0 8px;
  font: 500 11px/1 var(--font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-17__heading {
  margin: 0;
  max-inline-size: 26ch;
  font: 600 clamp(23px, 4vw, 34px)/1.12 var(--font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.fs-17__split {
  inline-size: 100%;
  max-inline-size: 72rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr);
  gap: 12px;
  align-items: start;
}

.fs-17__callouts {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 1px;
  background: var(--rule);
  border: 1px solid var(--rule);
  border-radius: 8px;
  overflow: hidden;
}

.fs-17__callout {
  min-inline-size: 0;
  display: grid;
  grid-template-columns: 26px minmax(0, 1fr);
  gap: 4px 10px;
  padding: 14px 13px;
  background: var(--pane);
}

.fs-17__icon {
  grid-row: span 2;
  display: grid;
  place-items: start center;
  padding-block-start: 2px;
  color: var(--accent);
}

.fs-17__ctitle {
  margin: 0;
  font: 600 14px/1.3 system-ui, sans-serif;
  letter-spacing: -0.01em;
}

.fs-17__cprose {
  margin: 0;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-17__codepane {
  min-inline-size: 0;
  background: var(--pane);
  border: 1px solid var(--rule);
  border-radius: 8px;
  overflow: hidden;
}

.fs-17__tabs {
  display: flex;
  align-items: center;
  gap: 2px;
  padding: 6px 8px;
  border-block-end: 1px solid var(--rule);
}

.fs-17__tab {
  padding: 6px 10px;
  font: 500 11.5px/1 var(--font-display);
  color: var(--muted);
  border-radius: 5px;
}

.fs-17__tab[data-active] {
  color: var(--ink);
  background: color-mix(in oklab, var(--ink) 8%, transparent);
  box-shadow: inset 0 -2px 0 var(--accent);
}

.fs-17__copy {
  margin-inline-start: auto;
  min-height: 30px;
  padding: 0 11px;
  font: 500 11px/1 var(--font-display);
  color: var(--bg);
  background: var(--accent);
  border: 0;
  border-radius: 5px;
  cursor: pointer;
}

.fs-17__copy:hover {
  background: color-mix(in oklab, var(--accent) 82%, white);
}

.fs-17__copy:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.fs-17__pre {
  margin: 0;
  padding: 12px;
  overflow-x: auto;
  tab-size: 2;
}

.fs-17__code {
  font: 400 12.5px/1.7 var(--font-display);
  color: var(--ink);
  white-space: pre;
}

.fs-17__k {
  color: #c4a6ff;
}

.fs-17__f {
  color: #7fd3f5;
}

.fs-17__a {
  color: #f0c073;
}

.fs-17__s {
  color: var(--accent);
}

.fs-17__c {
  color: #6b6b70;
  font-style: italic;
}

.fs-17__status {
  margin: 0;
  padding: 10px 12px;
  border-block-start: 1px solid var(--rule);
  font: 500 11.5px/1.5 var(--font-display);
  color: #f0c073;
}

.fs-17__below {
  padding: var(--pad) 14px;
  border-block-start: 1px solid var(--rule);
  font: 500 11px/1 var(--font-display);
  color: var(--muted);
}

@media (max-width: 820px) {
  .fs-17__split {
    grid-template-columns: minmax(0, 1fr);
  }
}

@media (prefers-color-scheme: light) {
  .fs-17 {
    --bg: #fbfbfc;
    --pane: #ffffff;
    --ink: #121214;
    --muted: #63636b;
    --rule: #e3e3e7;
    --accent: #0f7a45;
  }

  .fs-17__k {
    color: #6b32c9;
  }

  .fs-17__f {
    color: #14607c;
  }

  .fs-17__a {
    color: #8a5300;
  }

  .fs-17__c {
    color: #85858c;
  }

  .fs-17__copy {
    color: #ffffff;
  }

  .fs-17__status {
    color: #8a5300;
  }
}

[data-theme="dark"] .fs-17 {
  --bg: #0c0c0d;
  --pane: #131315;
  --ink: #ededee;
  --muted: #8e8e93;
  --rule: #26262a;
  --accent: #45d483;
}
```

## JavaScript
```js
const pane = document.querySelector('.fs-17__codepane');
if (pane) {
  const code = document.getElementById('fs-17-code');
  const btn = pane.querySelector('.fs-17__copy');
  const status = pane.querySelector('[data-status]');
  const fire = async () => {
    try {
      if (!navigator.clipboard) throw new Error('unavailable');
      await navigator.clipboard.writeText(code.innerText);
      btn.textContent = 'Copied';
      setTimeout(() => { btn.textContent = 'Copy'; }, 1600);
    } catch {
      btn.textContent = 'Selected';
      if (status) status.hidden = false;
      getSelection()?.selectAllChildren(code);
    }
  };
  btn.addEventListener('click', fire);
  btn.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fire(); } });
}
```

---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/framework-agnostic-faq-react-vue-svelte-astro-port-recipe/"
title: "Framework-Agnostic FAQ (React / Vue / Svelte / Astro port recipe)"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "One accordion, five codebases: a working native-details FAQ up top, and beneath it a pure-CSS tab viewer (radio hack — meta!) showing the same component…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Framework-Agnostic FAQ (React / Vue / Svelte / Astro port recipe)
Source: https://codefronts.com/snippets/css-faq-accordion/framework-agnostic-faq-react-vue-svelte-astro-port-recipe/

One accordion, five codebases: a working native-details FAQ up top, and beneath it a pure-CSS tab viewer (radio hack — meta!) showing the same component ported to React, Vue 3, Svelte 5 and Astro. The recipe's thesis: because the behavior lives in the <details> element and the styling in scoped CSS, the 'component' each framework adds is just a data-mapping shell — 15 lines each, no accordion library, no useState gymnastics. Copy the port for your stack; the CSS travels unchanged.
## HTML
```html
<section class="cfa-24" aria-label="Framework agnostic FAQ port recipe">
  <div class="cfa-24__wrap">
    <header class="cfa-24__head">
      <h1>One accordion, five codebases</h1>
      <p>The living component, then the same 15-line shell in each framework. Behavior stays in <code>&lt;details&gt;</code>; frameworks only map data.</p>
    </header>
    <div class="cfa-24__list">
      <details class="cfa-24__item" open>
        <summary class="cfa-24__q">Why no accordion library?<i aria-hidden="true"></i></summary>
        <div class="cfa-24__a"><p>Because the platform ships one. The details element gives you state, keyboard support and semantics; a library would re-implement all three in 40kB and still need this CSS.</p></div>
      </details>
      <details class="cfa-24__item">
        <summary class="cfa-24__q">Where does state live?<i aria-hidden="true"></i></summary>
        <div class="cfa-24__a"><p>In the DOM's open attribute — which means SSR, static builds and server components render working accordions with zero hydration. Lift state into the framework only when a feature (analytics, exclusive mode) actually demands it.</p></div>
      </details>
      <details class="cfa-24__item">
        <summary class="cfa-24__q">Does the CSS need porting?<i aria-hidden="true"></i></summary>
        <div class="cfa-24__a"><p>No — that is the point of keeping it class-based and scoped under one prefix. Paste it in a global stylesheet, a CSS module, or a style block; the selectors don't care who rendered the markup.</p></div>
      </details>
    </div>
    <div class="cfa-24__viewer">
      <div class="cfa-24__tabs" role="presentation">
        <input type="radio" name="cfa24-tab" id="cfa24-t-react" class="cfa-24__trb" checked>
        <label class="cfa-24__tab" for="cfa24-t-react">React</label>
        <input type="radio" name="cfa24-tab" id="cfa24-t-vue" class="cfa-24__trb">
        <label class="cfa-24__tab" for="cfa24-t-vue">Vue 3</label>
        <input type="radio" name="cfa24-tab" id="cfa24-t-svelte" class="cfa-24__trb">
        <label class="cfa-24__tab" for="cfa24-t-svelte">Svelte 5</label>
        <input type="radio" name="cfa24-tab" id="cfa24-t-astro" class="cfa-24__trb">
        <label class="cfa-24__tab" for="cfa24-t-astro">Astro</label>
        <div class="cfa-24__pane" data-pane="react"><pre><code>function Faq({ items }) {
  return (
    &lt;div className="faq-list"&gt;
      {items.map(it =&gt; (
        &lt;details className="faq-item" key={it.q}
                 {...(it.open ? { open: true } : {})}&gt;
          &lt;summary className="faq-q"&gt;
            {it.q}&lt;i aria-hidden="true" /&gt;
          &lt;/summary&gt;
          &lt;div className="faq-a"&gt;&lt;p&gt;{it.a}&lt;/p&gt;&lt;/div&gt;
        &lt;/details&gt;
      ))}
    &lt;/div&gt;
  );
}  // no useState — the DOM holds the state</code></pre></div>
        <div class="cfa-24__pane" data-pane="vue"><pre><code>&lt;script setup&gt;
defineProps({ items: Array })
&lt;/script&gt;

&lt;template&gt;
  &lt;div class="faq-list"&gt;
    &lt;details v-for="it in items" :key="it.q"
             class="faq-item" :open="it.open"&gt;
      &lt;summary class="faq-q"&gt;
        {{ it.q }}&lt;i aria-hidden="true" /&gt;
      &lt;/summary&gt;
      &lt;div class="faq-a"&gt;&lt;p&gt;{{ it.a }}&lt;/p&gt;&lt;/div&gt;
    &lt;/details&gt;
  &lt;/div&gt;
&lt;/template&gt;</code></pre></div>
        <div class="cfa-24__pane" data-pane="svelte"><pre><code>&lt;script&gt;
  let { items } = $props();
&lt;/script&gt;

&lt;div class="faq-list"&gt;
  {#each items as it (it.q)}
    &lt;details class="faq-item" open={it.open}&gt;
      &lt;summary class="faq-q"&gt;
        {it.q}&lt;i aria-hidden="true"&gt;&lt;/i&gt;
      &lt;/summary&gt;
      &lt;div class="faq-a"&gt;&lt;p&gt;{it.a}&lt;/p&gt;&lt;/div&gt;
    &lt;/details&gt;
  {/each}
&lt;/div&gt;</code></pre></div>
        <div class="cfa-24__pane" data-pane="astro"><pre><code>---
// Faq.astro — renders to plain HTML, ships zero JS
const { items } = Astro.props;
---
&lt;div class="faq-list"&gt;
  {items.map(it =&gt; (
    &lt;details class="faq-item" open={it.open}&gt;
      &lt;summary class="faq-q"&gt;
        {it.q}&lt;i aria-hidden="true"&gt;&lt;/i&gt;
      &lt;/summary&gt;
      &lt;div class="faq-a"&gt;&lt;p&gt;{it.a}&lt;/p&gt;&lt;/div&gt;
    &lt;/details&gt;
  ))}
&lt;/div&gt;
&lt;!-- no client: directive — none needed --&gt;</code></pre></div>
      </div>
    </div>
    <p class="cfa-24__foot">The tab viewer above is itself the radio hack from demo 01 — patterns compound. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-24,
.cfa-24 *,
.cfa-24 *::before,
.cfa-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-24 {
  --bg: oklch(0.17 0.02 285);
  --panel: oklch(0.22 0.024 285);
  --ink: oklch(0.95 0.006 280);
  --mut: oklch(0.68 0.018 282);
  --line: oklch(0.32 0.028 284);
  --acc: oklch(0.76 0.16 310);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: radial-gradient(900px 500px at 85% 0%,oklch(0.24 0.05 310/.5),transparent 60%),var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-24__wrap {
  width: min(100%,680px);
}

.cfa-24__head h1 {
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-24__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-24__head code,
.cfa-24__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .87em;
  background: oklch(0.28 0.026 284);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.cfa-24__list {
  margin-top: 22px;
  display: flex;
  flex-direction: column;
  gap: 9px;
  interpolate-size: allow-keywords;
}

.cfa-24__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 13px;
  transition: border-color .3s;
}

.cfa-24__item[open] {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-24__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 15px 17px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 650;
  list-style: none;
  transition: color .2s;
}

.cfa-24__q::-webkit-details-marker {
  display: none;
}

.cfa-24__q:hover {
  color: var(--acc);
}

.cfa-24__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 13px;
}

.cfa-24__q i {
  flex: none;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s;
}

.cfa-24__item[open] .cfa-24__q i {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-24__a p {
  padding: 0 17px 16px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-24__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .35s allow-discrete;
  }

  .cfa-24__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-24__viewer {
  margin-top: 20px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: oklch(0.14 0.018 285);
  overflow: hidden;
}

.cfa-24__tabs {
  display: flex;
  flex-wrap: wrap;
  padding: 10px 10px 0;
}

.cfa-24__trb {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cfa-24__tab {
  min-height: 44px;
  display: grid;
  place-items: center;
  padding: 0 16px;
  border-radius: 10px 10px 0 0;
  font-size: 13px;
  font-weight: 700;
  color: var(--mut);
  cursor: pointer;
  transition: color .2s,background .2s;
}

.cfa-24__tab:hover {
  color: var(--ink);
}

.cfa-24__trb:focus-visible + .cfa-24__tab {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

#cfa24-t-react:checked ~ .cfa-24__tab[for="cfa24-t-react"],
#cfa24-t-vue:checked ~ .cfa-24__tab[for="cfa24-t-vue"],
#cfa24-t-svelte:checked ~ .cfa-24__tab[for="cfa24-t-svelte"],
#cfa24-t-astro:checked ~ .cfa-24__tab[for="cfa24-t-astro"] {
  color: var(--acc);
  background: var(--panel);
}

.cfa-24__pane {
  display: none;
  width: 100%;
  background: var(--panel);
  border-top: 1px solid var(--line);
}

#cfa24-t-react:checked ~ .cfa-24__pane[data-pane="react"],
#cfa24-t-vue:checked ~ .cfa-24__pane[data-pane="vue"],
#cfa24-t-svelte:checked ~ .cfa-24__pane[data-pane="svelte"],
#cfa24-t-astro:checked ~ .cfa-24__pane[data-pane="astro"] {
  display: block;
}

.cfa-24__pane pre {
  overflow-x: auto;
  padding: 18px 20px;
}

.cfa-24__pane code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  line-height: 1.65;
  color: oklch(0.85 0.03 300);
}

.cfa-24__foot {
  margin-top: 20px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-24 *,
    .cfa-24 .cfa-24__item::details-content {
    transition-duration: .01ms !important;
  }
}
```

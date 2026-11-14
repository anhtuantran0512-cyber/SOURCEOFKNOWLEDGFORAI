---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/code-comment/"
title: "Code Comment Accordion — Editor-Themed Collapsible Doc Blocks"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "An accordion cosplaying as your editor: summaries are // comment lines with fold arrows in a line-numbered gutter, and opening one 'unfolds' a…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Code Comment Accordion — Editor-Themed Collapsible Doc Blocks
Source: https://codefronts.com/navigation/css-accordions/code-comment/

An accordion cosplaying as your editor: summaries are // comment lines with fold arrows in a line-numbered gutter, and opening one 'unfolds' a syntax-highlighted code block beneath — exactly how code folding looks in VS Code. Made for API docs, developer landing pages and technical blogs.
## HTML
```html
<section class="acc-27" aria-label="Code comment editor accordion demo">
  <div class="acc-27__win">
    <div class="acc-27__bar"><span class="acc-27__dots"><i></i><i></i><i></i></span><span class="acc-27__tab">quickstart.js</span></div>
    <div class="acc-27__editor">
      <details class="acc-27__fold" open>
        <summary class="acc-27__sum">// how do I authenticate?</summary>
        <pre class="acc-27__code"><code><span class="acc-27__ln"><b class="acc-27__kw">import</b> { Client } <b class="acc-27__kw">from</b> <i class="acc-27__str">'@acme/sdk'</i>;</span>
<span class="acc-27__ln"></span>
<span class="acc-27__ln"><b class="acc-27__kw">const</b> client = <b class="acc-27__kw">new</b> <em class="acc-27__fn">Client</em>({</span>
<span class="acc-27__ln">  apiKey: process.env.<em class="acc-27__fn">ACME_KEY</em>  <s class="acc-27__cm">// server-side only</s></span>
<span class="acc-27__ln">});</span></code></pre>
      </details>
      <details class="acc-27__fold">
        <summary class="acc-27__sum">// how do I fetch a record?</summary>
        <pre class="acc-27__code"><code><span class="acc-27__ln"><b class="acc-27__kw">const</b> order = <b class="acc-27__kw">await</b> client.orders.<em class="acc-27__fn">get</em>(<i class="acc-27__str">'ord_8h2k'</i>);</span>
<span class="acc-27__ln">console.<em class="acc-27__fn">log</em>(order.status); <s class="acc-27__cm">// "shipped"</s></span></code></pre>
      </details>
      <details class="acc-27__fold">
        <summary class="acc-27__sum">// how do I handle errors?</summary>
        <pre class="acc-27__code"><code><span class="acc-27__ln"><b class="acc-27__kw">try</b> {</span>
<span class="acc-27__ln">  <b class="acc-27__kw">await</b> client.orders.<em class="acc-27__fn">create</em>(payload);</span>
<span class="acc-27__ln">} <b class="acc-27__kw">catch</b> (err) {</span>
<span class="acc-27__ln">  <b class="acc-27__kw">if</b> (err.code === <i class="acc-27__str">'rate_limited'</i>) <b class="acc-27__kw">return</b> <em class="acc-27__fn">retry</em>(err.after);</span>
<span class="acc-27__ln">  <b class="acc-27__kw">throw</b> err; <s class="acc-27__cm">// everything else is yours</s></span>
<span class="acc-27__ln">}</span></code></pre>
      </details>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-27,
.acc-27 *,
.acc-27 *::before,
.acc-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-27 {
  --bg: #1a1d27;
  --gutter: #252937;
  --tok-kw: #c792ea;
  --tok-str: #c3e88d;
  --tok-fn: #82aaff;
  --tok-cm: #8b93ab;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #10121a;
  padding: 44px 24px;
}

.acc-27__win {
  width: min(640px,100%);
  background: var(--bg);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 30px 70px -30px rgba(0,0,0,.8);
  border: 1px solid #2c3040;
}

.acc-27__bar {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 16px;
  background: #151823;
  border-bottom: 1px solid #2c3040;
}

.acc-27__dots {
  display: flex;
  gap: 7px;
}

.acc-27__dots i {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: #3d4254;
}

.acc-27__dots i:first-child {
  background: #e5695e;
}

.acc-27__dots i:nth-child(2) {
  background: #e0b055;
}

.acc-27__dots i:last-child {
  background: #5fb96a;
}

.acc-27__tab {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: #aab2c8;
  background: var(--bg);
  padding: 5px 14px;
  border-radius: 7px 7px 0 0;
  translate: 0 6px;
  border: 1px solid #2c3040;
  border-bottom-color: var(--bg);
}

.acc-27__editor {
  padding: 16px 0 20px;
  counter-reset: acc-27-line;
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
}

.acc-27__sum {
  list-style: none;
  display: block;
  position: relative;
  padding: 6px 18px 6px 64px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--tok-cm);
  font-style: italic;
  cursor: pointer;
  counter-increment: acc-27-line;
  transition: background .15s,color .15s;
}

.acc-27__sum::-webkit-details-marker {
  display: none;
}

.acc-27__sum::marker {
  content: "";
}

.acc-27__sum:hover {
  background: #20242f;
  color: #b8c0d8;
}

.acc-27__sum::before {
  content: counter(acc-27-line);
  position: absolute;
  left: 0;
  width: 40px;
  text-align: right;
  color: #4a5065;
  font-style: normal;
  font-size: 12px;
}

.acc-27__sum::after {
  content: "";
  position: absolute;
  left: 48px;
  top: 50%;
  translate: 0 -50%;
  border-left: 5px solid #6d7590;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  transition: rotate .2s;
}

.acc-27__fold[open] > .acc-27__sum::after {
  rotate: 90deg;
}

.acc-27__fold[open] > .acc-27__sum {
  color: #b8c0d8;
}

.acc-27__code {
  overflow-x: auto;
}

.acc-27__code code {
  display: block;
}

.acc-27__ln {
  display: block;
  position: relative;
  padding: 0 18px 0 64px;
  font-size: 13.5px;
  line-height: 1.7;
  color: #d6dcee;
  counter-increment: acc-27-line;
  white-space: pre;
}

.acc-27__ln::before {
  content: counter(acc-27-line);
  position: absolute;
  left: 0;
  width: 40px;
  text-align: right;
  color: #3c4257;
  font-size: 12px;
}

.acc-27__kw {
  color: var(--tok-kw);
  font-weight: 400;
  font-style: italic;
}

.acc-27__str {
  color: var(--tok-str);
  font-style: normal;
}

.acc-27__fn {
  color: var(--tok-fn);
  font-style: normal;
}

.acc-27__cm {
  color: var(--tok-cm);
  text-decoration: none;
}

.acc-27__fold[open] .acc-27__code {
  animation: acc-27-in .25s ease-out;
}

@keyframes acc-27-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.acc-27__sum:focus-visible {
  outline: 2px solid var(--tok-fn);
  outline-offset: -2px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-27__fold[open] .acc-27__code {
    animation: none;
  }

  .acc-27__sum::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — summaries and code lines share one CSS counter, so line numbers renumber live as folds open, exactly like an editor; syntax colors are hand-spanned token classes. */
```

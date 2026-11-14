---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/ide-function-hover/"
title: "IDE Function Hover"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A typed-signature documentation popover for code editors."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: IDE Function Hover
Source: https://codefronts.com/snippets/css-tooltips/ide-function-hover/

A typed-signature documentation popover for code editors. Hover the underlined function call to reveal a stacked card — badge, namespace path, signature, prose description, parameter rows, and a docs-shortcut footer — the kind of tooltip every IDE wishes it shipped by default.
## HTML
```html
<div class="tp-03">
  <div class="tp-03__editor">
    <div class="tp-03__tabs">
      <span class="tp-03__dot"></span><span class="tp-03__dot"></span><span class="tp-03__dot"></span>
      <span class="tp-03__tab">orchestrator.ts</span>
    </div>
    <div class="tp-03__body">
      <div class="tp-03__gutter">
        <div>1</div><div>2</div><div>3</div><div>4</div><div>5</div>
        <div>6</div><div>7</div><div>8</div>
      </div>
      <div class="tp-03__code">
        <div class="tp-03__line"><span class="tp-03__cmt">// pipeline assembled at boot</span></div>
        <div class="tp-03__line"><span class="tp-03__kw">import</span> { <span class="tp-03__fn">createScheduler</span> } <span class="tp-03__kw">from</span> <span class="tp-03__str">"./scheduler"</span>;</div>
        <div class="tp-03__line">&nbsp;</div>
        <div class="tp-03__line"><span class="tp-03__kw">const</span> <span class="tp-03__var">queue</span> = <span class="tp-03__symbol"><span class="tp-03__fn">createScheduler</span><span class="tp-03__tip">
          <span class="tp-03__tip-head">
            <span class="tp-03__tip-badge">FUNCTION</span>
            <span class="tp-03__tip-path"><span>core</span><span class="tp-03__sep">›</span><span>scheduler</span><span class="tp-03__sep">›</span><span>createScheduler</span></span>
          </span>
          <span class="tp-03__tip-sig"><span class="tp-03__kw">function</span> <span class="tp-03__fn">createScheduler</span>&lt;<span class="tp-03__var">T</span>&gt;(<br>&nbsp;&nbsp;<span class="tp-03__param">opts</span>: <span class="tp-03__var">SchedulerOptions</span>&lt;<span class="tp-03__var">T</span>&gt;<br>): <span class="tp-03__var">Queue</span>&lt;<span class="tp-03__var">T</span>&gt;</span>
          <span class="tp-03__tip-desc">Creates a back-pressured task queue with concurrency control. Items are processed in <code class="tp-03__tip-code">FIFO</code> order; failing jobs surface to the dead-letter sink.</span>
          <span class="tp-03__tip-params">
            <span class="tp-03__tip-param-row"><span class="tp-03__pname">concurrency</span><span class="tp-03__pdesc">Max parallel jobs. Default <code class="tp-03__tip-code">4</code>.</span></span>
            <span class="tp-03__tip-param-row"><span class="tp-03__pname">retries</span><span class="tp-03__pdesc">Per-task retry budget. Default <code class="tp-03__tip-code">3</code>.</span></span>
            <span class="tp-03__tip-param-row"><span class="tp-03__pname">onDrain</span><span class="tp-03__pdesc">Fires once when the queue empties.</span></span>
          </span>
          <span class="tp-03__tip-foot">
            <span>scheduler.ts · L42</span>
            <span><span class="tp-03__kbd-key">⌘</span><span class="tp-03__kbd-key">K</span> for docs</span>
          </span>
        </span></span>({</div>
        <div class="tp-03__line">&nbsp;&nbsp;<span class="tp-03__param">concurrency</span>: <span class="tp-03__num">8</span>,</div>
        <div class="tp-03__line">&nbsp;&nbsp;<span class="tp-03__param">retries</span>: <span class="tp-03__num">3</span>,</div>
        <div class="tp-03__line">});</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
/* No @import here. Demos use Inter + JetBrains Mono (from
   BaseLayout) and Georgia / cursive system fallbacks for the rest.
   See top-of-file Fonts comment for the why. */

.tp-03 {
  width: 100%;
  min-height: 100vh;
  background: #0d1117;
  /* Top padding sized so the tooltip (~280px tall, pops up from the
       symbol) fully renders inside the gallery card. Without this the
       card's overflow:hidden clips the top of the tip. The bottom needs
       less room since the editor is anchored to flex-start. */
  padding: 300px 28px 48px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
}

.tp-03__editor {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 8px;
  width: 100%;
  max-width: 560px;
  box-shadow: 0 18px 50px -16px rgba(0, 0, 0, 0.7);
}

.tp-03__tabs {
  background: #0d1117;
  border-bottom: 1px solid #30363d;
  display: flex;
  align-items: center;
  padding: 0 14px;
  height: 32px;
  gap: 4px;
  border-radius: 8px 8px 0 0;
}

.tp-03__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #30363d;
}

.tp-03__dot:nth-child(1) {
  background: #ff5f57;
}

.tp-03__dot:nth-child(2) {
  background: #febc2e;
}

.tp-03__dot:nth-child(3) {
  background: #28c840;
}

.tp-03__tab {
  margin-left: 18px;
  padding: 5px 12px;
  background: #161b22;
  border-radius: 6px 6px 0 0;
  font-size: 11px;
  color: #c9d1d9;
  display: inline-flex;
  align-items: center;
  gap: 7px;
}

.tp-03__tab::before {
  content: '';
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: #58a6ff;
}

.tp-03__body {
  padding: 18px 0;
  font-size: 13px;
  /* Use a pixel line-height so the gutter and code columns advance at
       the same rate — em-based line-height (1.85) combined with two
       different font-sizes drifted them apart by ~2px per row and the
       gutter numbers no longer matched their code lines. */
  line-height: 22px;
  display: flex;
  color: #c9d1d9;
}

.tp-03__gutter {
  width: 44px;
  text-align: right;
  padding-right: 12px;
  color: #484f58;
  user-select: none;
  border-right: 1px solid #21262d;
  /* Same font-size as the code column so digits ride the 22px baseline
       in step with the code. */
  font-size: 13px;
}

.tp-03__code {
  padding: 0 16px;
  flex: 1;
  min-width: 0;
}
/* No white-space: pre on .tp-03__line. The line uses &nbsp; for visible
   indentation, which works under white-space: normal. Setting pre
   would honor the source newlines between sibling spans (especially
   inside the .tp-03__symbol that nests the multi-line tooltip markup),
   breaking each token onto its own visual row in the try-it iframe. */

.tp-03__line {
}

.tp-03__kw {
  color: #ff7b72;
}

.tp-03__fn {
  color: #d2a8ff;
}

.tp-03__str {
  color: #a5d6ff;
}

.tp-03__num {
  color: #79c0ff;
}

.tp-03__cmt {
  color: #8b949e;
  font-style: italic;
}

.tp-03__var {
  color: #79c0ff;
}

.tp-03__param {
  color: #ffa657;
}

.tp-03__symbol {
  position: relative;
  cursor: help;
  /* Visible-at-rest affordance: a dashed blue underline tells users
       "this token has a hover" without needing them to land on it first.
       The original (transparent until hover) was a discovery failure —
       users had no signal the demo had a hover tooltip at all. */
  border-bottom: 1px dashed rgba(88, 166, 255, 0.55);
  transition: border-color 0.2s, background 0.2s;
  border-radius: 2px;
  padding: 0 2px;
}

.tp-03__symbol::after {
  /* Small info dot to the right of the symbol — second discovery cue
       in case the underline gets lost in syntax highlighting. */
  content: 'ⓘ';
  display: inline-block;
  font-size: 9px;
  color: rgba(88, 166, 255, 0.6);
  vertical-align: middle;
  margin-left: 3px;
  transition: color 0.2s;
}

.tp-03__symbol:hover {
  border-color: #58a6ff;
  background: rgba(88, 166, 255, 0.08);
}

.tp-03__symbol:hover::after {
  color: #58a6ff;
}

.tp-03__tip {
  position: absolute;
  bottom: calc(100% + 14px);
  left: -20px;
  width: 380px;
  background: linear-gradient(180deg, #1c2128 0%, #161b22 100%);
  border: 1px solid #30363d;
  border-radius: 6px;
  box-shadow: 0 18px 50px -8px rgba(0, 0, 0, 0.75), 0 0 0 1px rgba(88, 166, 255, 0.06), inset 0 1px 0 rgba(255, 255, 255, 0.04);
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: opacity 0.22s ease, transform 0.22s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear 0.22s;
  z-index: 10;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  pointer-events: none;
  display: block;
  /* Reset two properties the tip inherits from the .tp-03__line ancestor:
       white-space: pre (which would render the source newlines between
       spans as visible whitespace inside the tip) and line-height: 1.85
       (the editor's loose line-height — fine for code, way too tall
       inside the tooltip's prose). */
  white-space: normal;
  line-height: 1.5;
  text-align: left;
}

.tp-03__symbol:hover .tp-03__tip {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
  transition-delay: 0s;
}

.tp-03__tip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 32px;
  width: 10px;
  height: 10px;
  background: #161b22;
  border-right: 1px solid #30363d;
  border-bottom: 1px solid #30363d;
  transform: translateY(-50%) rotate(45deg);
}

.tp-03__tip-head {
  padding: 10px 14px 9px;
  border-bottom: 1px solid #21262d;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 11px;
}

.tp-03__tip-badge {
  background: rgba(88, 166, 255, 0.15);
  color: #58a6ff;
  padding: 2px 7px;
  border-radius: 10px;
  font-size: 9.5px;
  font-weight: 600;
  letter-spacing: 0.05em;
}

.tp-03__tip-path {
  color: #8b949e;
  font-size: 11px;
}

.tp-03__sep {
  color: #484f58;
  margin: 0 4px;
}

.tp-03__tip-sig {
  padding: 12px 14px;
  font-size: 12px;
  line-height: 1.6;
  border-bottom: 1px solid #21262d;
  display: block;
  /* Re-enable pre here so the multi-line function signature keeps its
       indent. The outer .tp-03__tip reset this to normal so the prose
       blocks (description, params, footer) don't render the source-
       formatting whitespace between sibling spans. */
  white-space: pre;
}

.tp-03__tip-desc {
  padding: 12px 14px;
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 12px;
  line-height: 1.65;
  color: #c9d1d9;
  border-bottom: 1px solid #21262d;
  display: block;
}

.tp-03__tip-code {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  background: rgba(110, 118, 129, 0.2);
  color: #ffa657;
  padding: 1px 5px;
  border-radius: 3px;
  font-size: 11px;
}

.tp-03__tip-params {
  padding: 10px 14px;
  border-bottom: 1px solid #21262d;
  display: block;
}

.tp-03__tip-param-row {
  display: grid;
  grid-template-columns: 90px 1fr;
  gap: 10px;
  font-size: 11.5px;
  padding: 3px 0;
  line-height: 1.5;
}

.tp-03__pname {
  color: #ffa657;
}

.tp-03__pdesc {
  color: #8b949e;
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 11.5px;
}

.tp-03__tip-foot {
  padding: 9px 14px;
  font-size: 10px;
  color: #6e7681;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tp-03__kbd-key {
  background: #21262d;
  border: 1px solid #30363d;
  border-bottom-width: 2px;
  color: #c9d1d9;
  padding: 1px 6px;
  border-radius: 4px;
  font-size: 10px;
  margin: 0 2px;
  display: inline-block;
}
```

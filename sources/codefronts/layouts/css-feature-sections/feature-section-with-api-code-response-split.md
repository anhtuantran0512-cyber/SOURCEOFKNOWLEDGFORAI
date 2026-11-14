---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/feature-section-with-api-code-response-split/"
title: "Feature Section with API Code Response Split"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "The split every developer-first marketing page needs: the request on the left, the JSON it returns on the right, one headline spanning both."
has_js: "true"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section with API Code Response Split
Source: https://codefronts.com/layouts/css-feature-sections/feature-section-with-api-code-response-split/

The split every developer-first marketing page needs: the request on the left, the JSON it returns on the right, one headline spanning both. Syntax colour is hand-applied spans rather than a highlighter bundle, each pane has a copy button with a real unavailable state when the clipboard is blocked, and the whole thing scrolls inside its own panes instead of pushing the page sideways.
## HTML
```html
<section class="fs-10" aria-labelledby="fs-10-heading">
  <div class="fs-10__hero" aria-hidden="true">
    <span class="fs-10__wordmark">talon<i>/api</i></span>
    <span class="fs-10__heronav">v3 · reference · changelog</span>
  </div>

  <div class="fs-10__stage">
    <div class="fs-10__block">
      <div class="fs-10__head">
        <p class="fs-10__eyebrow">// one call, typed both ways</p>
        <h2 class="fs-10__heading" id="fs-10-heading">Send a payout. Get a typed result, or a typed error.</h2>
        <p class="fs-10__sub">Idempotent by default, so the retry your queue makes at 3am does not send twice.</p>
      </div>

      <div class="fs-10__panes">
        <div class="fs-10__pane">
          <div class="fs-10__panehead">
            <span class="fs-10__panelabel">Request</span>
            <button class="fs-10__copy" type="button" data-copy="req">Copy</button>
          </div>
          <pre class="fs-10__pre"><code class="fs-10__code" id="fs-10-req"><span class="fs-10__c">// POST https://api.talon.dev/v3/payouts</span>
<span class="fs-10__k">await</span> talon.payouts.<span class="fs-10__f">create</span>({
  <span class="fs-10__p">amount</span>: <span class="fs-10__n">48200</span>,
  <span class="fs-10__p">currency</span>: <span class="fs-10__s">"usd"</span>,
  <span class="fs-10__p">destination</span>: <span class="fs-10__s">"acct_1QmR8xKz"</span>,
  <span class="fs-10__p">idempotency_key</span>: <span class="fs-10__s">"payout_2026_08_20_a41"</span>,
  <span class="fs-10__p">metadata</span>: {
    <span class="fs-10__p">invoice</span>: <span class="fs-10__s">"INV-9931"</span>,
    <span class="fs-10__p">team</span>: <span class="fs-10__s">"platform"</span>
  }
});</code></pre>
        </div>

        <div class="fs-10__pane">
          <div class="fs-10__panehead">
            <span class="fs-10__panelabel">Response · 201</span>
            <button class="fs-10__copy" type="button" data-copy="res">Copy</button>
          </div>
          <pre class="fs-10__pre"><code class="fs-10__code" id="fs-10-res">{
  <span class="fs-10__p">"id"</span>: <span class="fs-10__s">"po_3Nk8QaLm"</span>,
  <span class="fs-10__p">"object"</span>: <span class="fs-10__s">"payout"</span>,
  <span class="fs-10__p">"status"</span>: <span class="fs-10__s">"pending"</span>,
  <span class="fs-10__p">"amount"</span>: <span class="fs-10__n">48200</span>,
  <span class="fs-10__p">"arrival_date"</span>: <span class="fs-10__s">"2026-08-22"</span>,
  <span class="fs-10__p">"idempotent_replay"</span>: <span class="fs-10__k">false</span>,
  <span class="fs-10__p">"fee"</span>: { <span class="fs-10__p">"amount"</span>: <span class="fs-10__n">125</span>, <span class="fs-10__p">"currency"</span>: <span class="fs-10__s">"usd"</span> }
}</code></pre>
        </div>
      </div>

      <ul class="fs-10__notes">
        <li><b>Idempotent</b> Replays return the original payout with a replay flag, never a duplicate.</li>
        <li><b>Typed errors</b> Every failure carries a machine code, a field pointer and a retry hint.</li>
        <li><b>Webhook parity</b> The event payload is the same shape as this response body.</li>
      </ul>
      <p class="fs-10__status" data-status hidden>Clipboard unavailable here — select the code and copy manually.</p>
    </div>
  </div>

  <div class="fs-10__below" aria-hidden="true">SDKs: node · python · go · ruby · php</div>
</section>
```
## CSS
```css
.fs-10 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --s0: #1a1310;
  --s0: oklch(0.22 0.017 45);
  --s1: #221a15;
  --s1: oklch(0.26 0.019 48);
  --s2: #2c221b;
  --s2: oklch(0.31 0.021 50);
  --ink: #f2e6d8;
  --ink: oklch(0.93 0.021 75);
  --muted: #a4907d;
  --muted: oklch(0.68 0.03 65);
  --rule: #3a2d24;
  --rule: oklch(0.35 0.02 50);
  --accent: #e8b64c;
  --accent: oklch(0.82 0.13 85);
  --tok-str: #a8c98a;
  --tok-num: #dba07a;
  --font-display: "JetBrains Mono", "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  background: var(--s0);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-10 *,
.fs-10 *::before,
.fs-10 *::after {
  box-sizing: border-box;
}

.fs-10__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 14px;
  justify-content: space-between;
  align-items: baseline;
  padding: 12px 16px;
  border-block-end: 1px solid var(--rule);
  font: 500 12px/1 var(--font-display);
  color: var(--muted);
}

.fs-10__wordmark {
  color: var(--ink);
}

.fs-10__wordmark i {
  color: var(--accent);
  font-style: normal;
}

.fs-10__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(22px, 4vw, 44px) 12px;
}

.fs-10__block {
  inline-size: 100%;
  max-inline-size: 74rem;
  min-inline-size: 0;
}

.fs-10__head {
  margin: 0 0 16px;
}

.fs-10__eyebrow {
  margin: 0 0 8px;
  font: 500 11.5px/1 var(--font-display);
  color: var(--accent);
}

.fs-10__heading {
  margin: 0 0 8px;
  font: 600 clamp(22px, 3.8vw, 33px)/1.15 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.fs-10__sub {
  margin: 0;
  max-inline-size: 60ch;
  font-size: 14px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-10__panes {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: 10px;
  margin: 0 0 12px;
}

.fs-10__pane {
  min-inline-size: 0;
  background: var(--s1);
  border: 1px solid var(--rule);
  border-radius: 6px;
  overflow: hidden;
}

.fs-10__panehead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 8px 10px;
  background: var(--s2);
  border-block-end: 1px solid var(--rule);
}

.fs-10__panelabel {
  font: 500 10.5px/1 var(--font-display);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.fs-10__copy {
  min-height: 30px;
  padding: 0 10px;
  font: 500 11px/1 var(--font-display);
  color: var(--accent);
  background: transparent;
  border: 1px solid color-mix(in oklab, var(--accent) 40%, var(--rule));
  border-radius: 4px;
  cursor: pointer;
}

.fs-10__copy:hover {
  background: color-mix(in oklab, var(--accent) 14%, transparent);
}

.fs-10__copy:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fs-10__copy[data-done] {
  color: var(--tok-str);
  border-color: var(--tok-str);
}

.fs-10__pre {
  margin: 0;
  padding: 12px;
  overflow-x: auto;
  tab-size: 2;
  background: var(--s1);
}

.fs-10__code {
  font: 400 12.5px/1.75 var(--font-display);
  color: var(--ink);
  white-space: pre;
}

.fs-10__k {
  color: var(--accent);
}

.fs-10__f {
  color: #7fc4d9;
}

.fs-10__p {
  color: #c9b8a5;
}

.fs-10__s {
  color: var(--tok-str);
}

.fs-10__n {
  color: var(--tok-num);
}

.fs-10__c {
  color: #7a6a5c;
  font-style: italic;
}

.fs-10__notes {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr));
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.fs-10__notes li {
  min-inline-size: 0;
  padding: 10px 12px;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--muted);
  background: var(--s1);
  border: 1px solid var(--rule);
  border-radius: 5px;
}

.fs-10__notes b {
  display: block;
  margin-block-end: 3px;
  font: 600 11px/1 var(--font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-10__status {
  margin: 10px 0 0;
  font: 500 12px/1.5 var(--font-display);
  color: var(--tok-num);
}

.fs-10__below {
  padding: 12px 16px;
  border-block-start: 1px solid var(--rule);
  font: 500 11.5px/1 var(--font-display);
  color: var(--muted);
}

@media (max-width: 820px) {
  .fs-10__panes {
    grid-template-columns: minmax(0, 1fr);
  }
}

@media (prefers-color-scheme: light) {
  .fs-10 {
    --s0: #f8f4ee;
    --s1: #ffffff;
    --s2: #f1e9df;
    --ink: #241a13;
    --muted: #6d5b4c;
    --rule: #e0d3c4;
    --accent: #96650a;
    --tok-str: #37662a;
    --tok-num: #9a4a1c;
  }

  .fs-10__f {
    color: #1c5f76;
  }

  .fs-10__p {
    color: #5c4a3a;
  }

  .fs-10__c {
    color: #8d7a68;
  }
}

[data-theme="dark"] .fs-10 {
  --s0: #1a1310;
  --s1: #221a15;
  --s2: #2c221b;
  --ink: #f2e6d8;
  --muted: #a4907d;
  --rule: #3a2d24;
  --accent: #e8b64c;
  --tok-str: #a8c98a;
  --tok-num: #dba07a;
}
```

## JavaScript
```js
const targets = { req: document.getElementById('fs-10-req'), res: document.getElementById('fs-10-res') };
const status = document.querySelector('.fs-10 [data-status]');
document.querySelectorAll('.fs-10__copy').forEach((btn) => {
  const fire = async () => {
    const src = targets[btn.dataset.copy];
    if (!src) return;
    try {
      if (!navigator.clipboard) throw new Error('unavailable');
      await navigator.clipboard.writeText(src.innerText);
      btn.textContent = 'Copied';
      btn.dataset.done = 'true';
      setTimeout(() => { btn.textContent = 'Copy'; delete btn.dataset.done; }, 1600);
    } catch {
      btn.textContent = 'Select code';
      if (status) status.hidden = false;
      getSelection()?.selectAllChildren(src);
    }
  };
  btn.addEventListener('click', fire);
  btn.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fire(); } });
});
```

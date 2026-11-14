---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/css-text-wrap-banner-with-long-strings/"
title: "Long Text Wrapping Banner"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "A live laboratory for the bug that breaks more banners than any other: one unbreakable string."
has_js: "false"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Long Text Wrapping Banner
Source: https://codefronts.com/snippets/css-banners-alerts/css-text-wrap-banner-with-long-strings/

A live laboratory for the bug that breaks more banners than any other: one unbreakable string. Switch between five wrapping strategies with the radio group and watch the same hostile content — a 96-character support URL, a German compound noun, a wallet address — behave completely differently. Everything is CSS: the radios drive :has(), and the expand animates height:auto via interpolate-size.
## HTML
```html
<div class="ba-20">
  <div class="ba-20__wrap">
    <fieldset class="ba-20__switch">
      <legend class="ba-20__legend">Wrapping strategy</legend>
      <label><input type="radio" name="ba-20-s" id="ba-20-default" checked><span>default</span></label>
      <label><input type="radio" name="ba-20-s" id="ba-20-anywhere"><span>overflow-wrap: anywhere</span></label>
      <label><input type="radio" name="ba-20-s" id="ba-20-hyphen"><span>hyphens: auto</span></label>
      <label><input type="radio" name="ba-20-s" id="ba-20-pretty"><span>text-wrap: pretty</span></label>
      <label><input type="radio" name="ba-20-s" id="ba-20-clamp"><span>line-clamp: 3</span></label>
    </fieldset>

    <div class="ba-20__banner" role="status">
      <span class="ba-20__icon" aria-hidden="true">
        <svg viewBox="0 0 20 20" fill="none" focusable="false"><circle cx="10" cy="10" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M10 9.2v4.4M10 6.5h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </span>

      <div class="ba-20__col">
        <p class="ba-20__title">Payout blocked by the reconciliation service</p>
        <p class="ba-20__prose">
          The transfer <code>0x7d4f9a1c8e2b6f05a3d94c17be08f2a6d5c39b71e4802fa6c1d7e93b58042ac6f</code> was rejected. Full trace at
          <a href="#ba-20-a">https://status.northline-payments.example.com/incidents/2026-08-10/reconciliation-timeout-eu-west-1-batch-4482197</a>
          and the German audit note reads <span lang="de">Zahlungsverkehrsüberwachungsverordnung</span>, which is one word, and it is not getting shorter.
        </p>
        <details class="ba-20__more">
          <summary>Full reconciliation trace</summary>
          <div class="ba-20__moreInner">
            <p><code>batch=4482197 attempt=3 window=2026-08-10T09:41:12Z/2026-08-10T09:46:12Z ledger=eu-west-1-primary shard=07 reconciler=v4.18.2-hotfix.1 cause=UpstreamTimeoutWaitingForSettlementConfirmation</code></p>
            <p>Retries are automatic for 24 hours. Nothing is double-spent: the ledger entry stays in <code>pending_reconciliation</code> until the settlement confirmation arrives or the window expires.</p>
          </div>
        </details>
      </div>

      <div class="ba-20__side">
        <p class="ba-20__meta">Case</p>
        <p class="ba-20__case">NL-4482197</p>
        <a class="ba-20__act" href="#ba-20-a">Contact support</a>
      </div>
    </div>

    <div class="ba-20__narrow">
      <p class="ba-20__narrowLabel" aria-hidden="true">18rem column</p>
      <div class="ba-20__banner ba-20__banner--narrow" role="status">
        <div class="ba-20__col">
          <p class="ba-20__title">Same content, hostile width</p>
          <p class="ba-20__prose">Trace: <a href="#ba-20-a">https://status.northline-payments.example.com/incidents/2026-08-10/reconciliation-timeout-eu-west-1-batch-4482197</a> · <span lang="de">Zahlungsverkehrsüberwachungsverordnung</span></p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

.ba-20 {
  --bg: #f5f6f8;
  --surface: #ffffff;
  --ink: #0f1216;
  --muted: #5f6773;
  --line: #e2e5ea;
  --acc: #d64545;
  --acc2: #2563eb;
  --sans: "Figtree",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  interpolate-size: allow-keywords;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  box-sizing: border-box;
  padding: clamp(1rem,4vw,3rem);
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-20 *,
.ba-20 *::before,
.ba-20 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-20 {
    --bg: oklch(97% .005 265);
    --surface: oklch(100% 0 0);
    --ink: oklch(19% .014 265);
    --muted: oklch(55% .016 265);
    --line: oklch(91% .01 265);
    --acc: oklch(58% .19 25);
    --acc2: oklch(55% .2 262);
  }
}

@media (prefers-color-scheme: dark) {
  .ba-20:not([data-theme="light"]) {
    --bg: #0b0d11;
    --surface: #14171d;
    --ink: #eef1f5;
    --muted: #98a0ac;
    --line: #232830;
  }
}

.ba-20[data-theme="dark"] {
  --bg: #0b0d11;
  --surface: #14171d;
  --ink: #eef1f5;
  --muted: #98a0ac;
  --line: #232830;
}

.ba-20__wrap {
  width: min(46rem,100%);
  min-width: 0;
  overflow-x: auto;
  display: grid;
  gap: 1rem;
}

.ba-20__switch {
  margin: 0;
  padding: .7rem .8rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
  align-items: center;
  background: var(--surface);
}

.ba-20__legend {
  padding: 0 .35rem;
  font-family: var(--mono);
  font-size: .625rem;
  font-weight: 500;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.ba-20__switch label {
  display: inline-flex;
}

.ba-20__switch input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
}

.ba-20__switch span {
  display: inline-flex;
  align-items: center;
  min-height: 2.25rem;
  padding: .4rem .7rem;
  cursor: pointer;
  border-radius: .6rem;
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: -.01em;
  color: var(--muted);
  border: 1px solid var(--line);
  transition: color .2s ease, background .2s ease, border-color .2s ease;
}

.ba-20__switch span:hover {
  color: var(--ink);
  border-color: var(--muted);
}

.ba-20__switch input:checked + span {
  color: var(--surface);
  background: var(--ink);
  border-color: var(--ink);
}

.ba-20__switch input:focus-visible + span {
  outline: 2px solid var(--acc2);
  outline-offset: 2px;
}

.ba-20__banner {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  gap: .9rem;
  align-items: start;
  padding: 1.1rem 1.15rem;
  border-radius: 1.15rem;
  background: color-mix(in oklab,var(--acc) 7%,var(--surface));
  border: 1px solid color-mix(in oklab,var(--acc) 26%,var(--line));
}

.ba-20__banner--narrow {
  grid-template-columns: minmax(0,1fr);
  padding: .85rem .9rem;
}

.ba-20__icon {
  display: grid;
  place-items: center;
  inline-size: 1.25rem;
  block-size: 1.25rem;
  color: var(--acc);
  margin-block-start: calc((1.5em - 1.25rem) / 2);
}

@supports (margin-block-start: calc((1lh - 1rem) / 2)) {
  .ba-20__icon {
    margin-block-start: calc((1lh - 1.25rem) / 2);
  }
}

.ba-20__icon svg {
  width: 100%;
  height: 100%;
}

.ba-20__col {
  min-width: 0;
  display: grid;
  gap: .35rem;
}

.ba-20__title {
  margin: 0;
  font-size: .9375rem;
  font-weight: 650;
  line-height: 1.45;
  letter-spacing: -.02em;
  color: color-mix(in oklab,var(--acc) 45%,var(--ink));
  text-wrap: balance;
}

.ba-20__prose {
  margin: 0;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 70ch;
  /* deliberately no wrapping aids by default — the radios add them */
}

.ba-20__prose code {
  font-family: var(--mono);
  font-size: .85em;
  padding: .08em .3em;
  border-radius: .25rem;
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.ba-20__prose a {
  color: var(--acc2);
  text-decoration: underline;
  text-underline-offset: 2px;
}
/* the five strategies, switched with :has() */

.ba-20:has(#ba-20-anywhere:checked) .ba-20__prose {
  overflow-wrap: anywhere;
}

.ba-20:has(#ba-20-hyphen:checked) .ba-20__prose {
  hyphens: auto;
  overflow-wrap: break-word;
  hyphenate-limit-chars: 8 4 4;
}

.ba-20:has(#ba-20-pretty:checked) .ba-20__prose {
  text-wrap: pretty;
  overflow-wrap: anywhere;
}

.ba-20:has(#ba-20-clamp:checked) .ba-20__prose {
  overflow-wrap: anywhere;
  overflow: hidden;
  line-clamp: 3;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
}

.ba-20__more {
  margin-block-start: .35rem;
}

.ba-20__more summary {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  min-height: 2.25rem;
  cursor: pointer;
  list-style: none;
  font-size: .75rem;
  font-weight: 600;
  color: var(--acc2);
}

.ba-20__more summary::-webkit-details-marker {
  display: none;
}

.ba-20__more summary::after {
  content: "+";
}

.ba-20__more[open] summary::after {
  content: "−";
}

.ba-20__more::details-content {
  block-size: 0;
  overflow: clip;
  opacity: 0;
  transition: block-size .4s cubic-bezier(.16,1,.3,1), opacity .3s ease, content-visibility .4s allow-discrete;
}

.ba-20__more[open]::details-content {
  block-size: auto;
  opacity: 1;
}

.ba-20__moreInner {
  display: grid;
  gap: .5rem;
  padding-block: .4rem 0;
}

.ba-20__moreInner p {
  margin: 0;
  font-size: .8125rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 70ch;
  text-wrap: pretty;
}

.ba-20__moreInner code {
  display: block;
  font-family: var(--mono);
  font-size: .75rem;
  line-height: 1.7;
  padding: .6rem .7rem;
  border-radius: .6rem;
  color: var(--ink);
  overflow-wrap: anywhere;
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.ba-20__side {
  display: grid;
  gap: .2rem;
  justify-items: end;
  text-align: end;
}

.ba-20__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .625rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.ba-20__case {
  margin: 0;
  font-family: var(--mono);
  font-size: .8125rem;
  font-weight: 500;
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}

.ba-20__act {
  margin-block-start: .4rem;
  display: inline-flex;
  align-items: center;
  min-height: 2.25rem;
  padding: .45rem .8rem;
  border-radius: .6rem;
  text-decoration: none;
  font-size: .75rem;
  font-weight: 600;
  color: var(--surface);
  background: var(--ink);
  white-space: nowrap;
}

.ba-20__act:hover {
  background: color-mix(in oklab,var(--ink) 85%,var(--acc));
}

.ba-20__narrow {
  display: grid;
  gap: .35rem;
  justify-items: start;
}

.ba-20__narrowLabel {
  margin: 0;
  font-family: var(--mono);
  font-size: .625rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.ba-20__narrow .ba-20__banner {
  inline-size: 18rem;
  max-inline-size: 100%;
}

.ba-20 :focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 2px;
}

@media (max-width: 34rem) {
  .ba-20__banner {
    grid-template-columns: auto minmax(0,1fr);
  }

  .ba-20__side {
    grid-column: 1 / -1;
    justify-items: start;
    text-align: start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-20 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-20__banner,
    .ba-20__switch {
    border: 1px solid CanvasText;
  }

  .ba-20__switch input:checked + span {
    background: Highlight;
    color: HighlightText;
  }
}
```

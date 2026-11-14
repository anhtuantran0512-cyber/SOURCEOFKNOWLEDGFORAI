---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-alert-box-success-error-styles/"
title: "CSS Alert Box Success Error Styles"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "The inline half of the status family: form-grade alert boxes (success confirmation, an error box that itemizes what failed and links each item to its field,…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Alert Box Success Error Styles
Source: https://codefronts.com/snippets/css-notifications/css-alert-box-success-error-styles/

The inline half of the status family: form-grade alert boxes (success confirmation, an error box that itemizes what failed and links each item to its field, a warning with body copy) derived from one --hue system — and a set of documentation callouts (Note, Tip, Warning, Danger) in the dark editorial style modern docs sites use, with monospace labels and quotable left-rail anatomy.
## HTML
```html
<div class="ntf-18-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-18a" aria-label="Inline form validation alert boxes">
  <div class="ntf-18a__col">
    <div class="ntf-18a__alert" style="--hue:152" role="status">
      <span class="ntf-18a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span>
      <div class="ntf-18a__body"><b>Application submitted</b><p>We emailed a copy to <a href="#" onclick="return false">[email protected]</a>. Expect a reply within 3 working days.</p></div>
    </div>
    <div class="ntf-18a__alert" style="--hue:26" role="alert">
      <span class="ntf-18a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></span>
      <div class="ntf-18a__body"><b>2 things need attention</b>
        <ul class="ntf-18a__list">
          <li><a href="#" onclick="return false">Card number</a> — must be 16 digits (you entered 15)</li>
          <li><a href="#" onclick="return false">Postcode</a> — doesn't match the card's billing address</li>
        </ul>
      </div>
    </div>
    <div class="ntf-18a__alert" style="--hue:82;--tx-l:0.4" role="status">
      <span class="ntf-18a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3L2 20h20L12 3zm0 8v4m0 3v.5"/></svg></span>
      <div class="ntf-18a__body"><b>Saved with warnings</b><p>Your logo is 4.2 MB — pages will load slower. <a href="#" onclick="return false">Compress it</a> for a faster storefront.</p></div>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..600&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
<section class="ntf-18b" aria-label="Documentation style callout boxes">
  <article class="ntf-18b__doc">
    <h2 class="ntf-18b__h">Rate limits</h2>
    <p class="ntf-18b__p">Every workspace gets 5,000 requests per hour, counted per API key.</p>
    <div class="ntf-18b__call" style="--hue:250"><i class="ntf-18b__rail" aria-hidden="true"></i><div><code class="ntf-18b__label">NOTE</code><p>Limits reset on a rolling window, not at the top of the hour.</p></div></div>
    <div class="ntf-18b__call" style="--hue:160"><i class="ntf-18b__rail" aria-hidden="true"></i><div><code class="ntf-18b__label">TIP</code><p>Batch endpoints count as one request per <em>call</em>, not per item — send 100 records in one call.</p></div></div>
    <div class="ntf-18b__call" style="--hue:82"><i class="ntf-18b__rail" aria-hidden="true"></i><div><code class="ntf-18b__label">WARNING</code><p>Keys created before 2026 use the legacy 1,000/hr limit until rotated.</p></div></div>
    <div class="ntf-18b__call" style="--hue:25"><i class="ntf-18b__rail" aria-hidden="true"></i><div><code class="ntf-18b__label">DANGER</code><p>Three 429 responses in a row triggers a 15-minute lockout. Back off exponentially.</p></div></div>
  </article>
</section>
</div>
```
## CSS
```css
.ntf-18-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-18-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-18a,
.ntf-18a *,
.ntf-18a *::before,
.ntf-18a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-18a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f7f9,#eceef2);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-18a__col {
  width: min(480px,100%);
  display: grid;
  gap: 14px;
}

.ntf-18a__alert {
  --tx-l: 0.32;
  --acc: oklch(0.58 0.14 var(--hue));
  --tx: oklch(var(--tx-l) 0.06 var(--hue));
  display: flex;
  gap: 13px;
  padding: 16px 17px;
  border-radius: 14px;
  background: color-mix(in oklch,var(--acc),white 93%);
  border: 1px solid color-mix(in oklch,var(--acc),white 60%);
  animation: ntf-18a-in .45s cubic-bezier(.22,1.2,.36,1) both;
}

.ntf-18a__alert:nth-child(2) {
  animation-delay: .08s;
}

.ntf-18a__alert:nth-child(3) {
  animation-delay: .16s;
}

.ntf-18a__ico {
  flex: none;
  width: 32px;
  height: 32px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  color: #fff;
  background: var(--acc);
}

.ntf-18a__ico svg {
  width: 16px;
  height: 16px;
}

.ntf-18a__body {
  min-width: 0;
  max-inline-size: 60ch;
}

.ntf-18a__body b {
  display: block;
  font-size: 14px;
  font-weight: 700;
  color: var(--tx);
}

.ntf-18a__body p {
  margin-top: 4px;
  font-size: 13px;
  line-height: 1.6;
  color: color-mix(in oklch,var(--tx),transparent 22%);
  text-wrap: pretty;
}

.ntf-18a__body a {
  color: var(--tx);
  font-weight: 600;
  text-underline-offset: 2px;
}

.ntf-18a__body a:hover {
  color: var(--acc);
}

.ntf-18a__list {
  margin-top: 6px;
  padding-inline-start: 18px;
  display: grid;
  gap: 5px;
}

.ntf-18a__list li {
  font-size: 13px;
  line-height: 1.55;
  color: color-mix(in oklch,var(--tx),transparent 18%);
}

@keyframes ntf-18a-in {
  from {
    opacity: 0;
    translate: 0 10px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-18a__alert {
    animation: ntf-18a-rm .2s ease both;
  }

  @keyframes ntf-18a-rm {
    from {
      opacity: 0;
    }
  }
}

.ntf-18b,
.ntf-18b *,
.ntf-18b *::before,
.ntf-18b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-18b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101216;
  font-family: 'Newsreader',Georgia,serif;
}

.ntf-18b__doc {
  width: min(520px,100%);
}

.ntf-18b__h {
  font-size: 30px;
  font-weight: 600;
  letter-spacing: -.01em;
  color: #eef1f7;
}

.ntf-18b__p {
  margin-top: 8px;
  font-size: 16px;
  line-height: 1.65;
  color: rgba(228,234,246,.65);
  max-inline-size: 62ch;
}

.ntf-18b__call {
  --acc: oklch(0.75 0.13 var(--hue));
  display: flex;
  gap: 14px;
  margin-top: 16px;
  padding: 14px 16px;
  border-radius: 12px;
  background: color-mix(in oklch,var(--acc),#101216 92%);
  border: 1px solid color-mix(in oklch,var(--acc),#101216 74%);
}

.ntf-18b__rail {
  flex: none;
  width: 2.5px;
  border-radius: 2px;
  background: var(--acc);
}

.ntf-18b__label {
  display: inline-block;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .16em;
  color: var(--acc);
}

.ntf-18b__call p {
  margin-top: 5px;
  font-size: 15px;
  line-height: 1.6;
  color: rgba(228,234,246,.78);
  max-inline-size: 58ch;
  text-wrap: pretty;
}

.ntf-18b__call em {
  color: #eef1f7;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-18b__call {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each box sets one --hue; surface, border, icon and text derive via color-mix(). The error box is a fix-it index: a count heading plus anchored items pointing at the fields to repair. */

/* No JavaScript — pure reading furniture: a 2.5px accent rail, an uppercase mono label, serif body at 1.6 line-height, all four types derived from a single --hue custom property. */
```

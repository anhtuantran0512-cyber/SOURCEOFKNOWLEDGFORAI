---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-success-error-warning-info-alert-toasts/"
title: "CSS Success Error Warning Info Alert Toasts"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "A complete status system, not four hand-tinted divs: one .toast class whose success/error/warning/info identities are a single --hue swap fed through oklch()…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Success Error Warning Info Alert Toasts
Source: https://codefronts.com/snippets/css-notifications/css-success-error-warning-info-alert-toasts/

A complete status system, not four hand-tinted divs: one .toast class whose success/error/warning/info identities are a single --hue swap fed through oklch() and color-mix() (surface, border, icon and text all derive automatically), plus a live morphing toast where a segmented control swaps data-type and the whole card cross-fades to the new state.
## HTML
```html
<div class="ntf-07-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-07a" aria-label="Success error warning info toast suite">
  <div class="ntf-07a__wrap">
    <h2 class="ntf-07a__title">Four states, one <code>--hue</code></h2>
    <div class="ntf-07a__list">
      <div class="ntf-07a__toast" data-type="success" role="status"><span class="ntf-07a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span><span class="ntf-07a__tx"><b>Payment received</b><small>Invoice #2041 marked as paid</small></span><button class="ntf-07a__x" type="button" aria-label="Dismiss">&#10005;</button></div>
      <div class="ntf-07a__toast" data-type="error" role="alert"><span class="ntf-07a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></span><span class="ntf-07a__tx"><b>Payment failed</b><small>Card declined — try another method</small></span><button class="ntf-07a__x" type="button" aria-label="Dismiss">&#10005;</button></div>
      <div class="ntf-07a__toast" data-type="warning" role="alert"><span class="ntf-07a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3L2 20h20L12 3zm0 8v4m0 3v.5"/></svg></span><span class="ntf-07a__tx"><b>Trial ends in 3 days</b><small>Add billing to keep your workspace</small></span><button class="ntf-07a__x" type="button" aria-label="Dismiss">&#10005;</button></div>
      <div class="ntf-07a__toast" data-type="info" role="status"><span class="ntf-07a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M12 11v6m0-10v.5"/><circle cx="12" cy="12" r="9.2"/></svg></span><span class="ntf-07a__tx"><b>Scheduled maintenance</b><small>Sunday 02:00–02:20 UTC</small></span><button class="ntf-07a__x" type="button" aria-label="Dismiss">&#10005;</button></div>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-07b" aria-label="One toast morphing between four states">
  <div class="ntf-07b__wrap">
    <div class="ntf-07b__seg" role="tablist" aria-label="Toast type">
      <button class="ntf-07b__segbtn is-on" data-ntf-07b="success" type="button">Success</button>
      <button class="ntf-07b__segbtn" data-ntf-07b="error" type="button">Error</button>
      <button class="ntf-07b__segbtn" data-ntf-07b="warning" type="button">Warning</button>
      <button class="ntf-07b__segbtn" data-ntf-07b="info" type="button">Info</button>
    </div>
    <div class="ntf-07b__toast" id="ntf-07b-toast" data-type="success" role="status">
      <span class="ntf-07b__ico" aria-hidden="true">
        <svg class="ntf-07b__g ntf-07b__g--success" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
        <svg class="ntf-07b__g ntf-07b__g--error" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
        <svg class="ntf-07b__g ntf-07b__g--warning" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3L2 20h20L12 3zm0 8v4m0 3v.5"/></svg>
        <svg class="ntf-07b__g ntf-07b__g--info" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M12 11v6m0-10v.5"/><circle cx="12" cy="12" r="9.2"/></svg>
      </span>
      <span class="ntf-07b__tx"><b id="ntf-07b-title">Changes saved</b><small id="ntf-07b-sub">Everything is up to date</small></span>
      <code class="ntf-07b__hue" id="ntf-07b-hue">--hue: 150</code>
    </div>
    <p class="ntf-07b__cap">Switching <b>data-type</b> swaps one custom property — the card cross-fades because its consumers transition.</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-07-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-07-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-07a,
.ntf-07a *,
.ntf-07a *::before,
.ntf-07a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-07a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f7f9,#eceef2);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-07a__wrap {
  width: min(440px,100%);
}

.ntf-07a__title {
  font-size: 23px;
  font-weight: 600;
  letter-spacing: -.01em;
  color: #20242d;
  text-align: center;
}

.ntf-07a__title code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .82em;
  background: rgba(32,36,45,.07);
  padding: 3px 8px;
  border-radius: 7px;
}

.ntf-07a__list {
  margin-top: 24px;
  display: grid;
  gap: 11px;
}

.ntf-07a__toast {
  --hue: 150;
  --acc: oklch(0.6 0.14 var(--hue));
  --bg: color-mix(in oklch,var(--acc),white 92%);
  --line: color-mix(in oklch,var(--acc),white 66%);
  --tx: oklch(0.33 0.06 var(--hue));
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 13px 14px;
  border-radius: 14px;
  background: var(--bg);
  border: 1px solid var(--line);
  animation: ntf-07a-in .5s cubic-bezier(.22,1.2,.36,1) both;
}

.ntf-07a__toast[data-type=error] {
  --hue: 25;
}

.ntf-07a__toast[data-type=warning] {
  --hue: 85;
  --tx: oklch(0.4 0.08 70);
}

.ntf-07a__toast[data-type=info] {
  --hue: 250;
}

.ntf-07a__toast:nth-child(2) {
  animation-delay: .07s;
}

.ntf-07a__toast:nth-child(3) {
  animation-delay: .14s;
}

.ntf-07a__toast:nth-child(4) {
  animation-delay: .21s;
}

.ntf-07a__ico {
  flex: none;
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  color: #fff;
  background: var(--acc);
}

.ntf-07a__ico svg {
  width: 17px;
  height: 17px;
}

.ntf-07a__tx {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ntf-07a__tx b {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--tx);
}

.ntf-07a__tx small {
  font-size: 11.5px;
  color: color-mix(in oklch,var(--tx),transparent 30%);
}

.ntf-07a__x {
  margin-left: auto;
  flex: none;
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 8px;
  font-size: 11px;
  color: var(--tx);
  background: transparent;
  cursor: pointer;
  opacity: .55;
  transition: opacity .15s,background .15s;
}

.ntf-07a__x:hover {
  opacity: 1;
  background: color-mix(in oklch,var(--acc),transparent 85%);
}

@keyframes ntf-07a-in {
  from {
    opacity: 0;
    translate: 0 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-07a__toast {
    animation: ntf-07a-rm .2s ease both;
  }

  @keyframes ntf-07a-rm {
    from {
      opacity: 0;
    }
  }
}

.ntf-07b,
.ntf-07b *,
.ntf-07b *::before,
.ntf-07b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-07b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#151922,#0b0e14);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-07b__wrap {
  width: min(460px,100%);
  display: grid;
  gap: 20px;
  justify-items: center;
}

.ntf-07b__seg {
  display: flex;
  gap: 4px;
  padding: 4px;
  border-radius: 12px;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(165,190,230,.16);
}

.ntf-07b__segbtn {
  padding: 9px 16px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 600;
  color: rgba(220,230,248,.6);
  background: transparent;
  border: 0;
  border-radius: 9px;
  cursor: pointer;
  transition: background .2s,color .2s;
}

.ntf-07b__segbtn:hover {
  color: #eef2fb;
}

.ntf-07b__segbtn.is-on {
  background: rgba(255,255,255,.12);
  color: #eef2fb;
}

.ntf-07b__toast {
  --hue: 150;
  --acc: oklch(0.76 0.15 var(--hue));
  width: 100%;
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 16px;
  border-radius: 16px;
  background: color-mix(in oklch,var(--acc),#12151d 88%);
  border: 1px solid color-mix(in oklch,var(--acc),transparent 60%);
  box-shadow: 0 24px 55px -28px color-mix(in oklch,var(--acc),transparent 40%);
  transition: background .45s,border-color .45s,box-shadow .45s;
}

.ntf-07b__toast[data-type=error] {
  --hue: 25;
}

.ntf-07b__toast[data-type=warning] {
  --hue: 85;
}

.ntf-07b__toast[data-type=info] {
  --hue: 250;
}

.ntf-07b__ico {
  flex: none;
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: var(--acc);
  color: #0b0e14;
  transition: background .45s;
}

.ntf-07b__g {
  position: absolute;
  inset: 0;
  margin: auto;
  width: 19px;
  height: 19px;
  opacity: 0;
  scale: .6;
  transition: opacity .3s,scale .35s cubic-bezier(.22,1.4,.36,1);
}

.ntf-07b__toast[data-type=success] .ntf-07b__g--success,
.ntf-07b__toast[data-type=error] .ntf-07b__g--error,
.ntf-07b__toast[data-type=warning] .ntf-07b__g--warning,
.ntf-07b__toast[data-type=info] .ntf-07b__g--info {
  opacity: 1;
  scale: 1;
}

.ntf-07b__tx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-07b__tx b {
  font-size: 14.5px;
  font-weight: 600;
  color: #eef2fb;
}

.ntf-07b__tx small {
  font-size: 12px;
  color: rgba(220,230,248,.55);
}

.ntf-07b__hue {
  margin-left: auto;
  flex: none;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10.5px;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc),transparent 88%);
  padding: 5px 9px;
  border-radius: 7px;
  transition: color .45s,background .45s;
}

.ntf-07b__cap {
  font-size: 12px;
  line-height: 1.6;
  color: rgba(220,230,248,.45);
  text-align: center;
  text-wrap: pretty;
}

.ntf-07b__cap b {
  color: rgba(238,242,251,.8);
}

@media (prefers-reduced-motion: reduce) {
  .ntf-07b__toast,
    .ntf-07b__ico,
    .ntf-07b__g,
    .ntf-07b__hue {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — each data-type sets ONE --hue; oklch() + color-mix() derive surface, border, icon chip and text from it, so all four states are automatically the same perceived weight. */

(function(){
  var toast=document.getElementById('ntf-07b-toast'); if(!toast) return;
  var COPY={success:['Changes saved','Everything is up to date',150],error:['Upload failed','File exceeds the 25 MB limit',25],warning:['Trial ends in 3 days','Add billing to keep your workspace',85],info:['New version available','Refresh to get v3.2',250]};
  var title=document.getElementById('ntf-07b-title'),sub=document.getElementById('ntf-07b-sub'),hue=document.getElementById('ntf-07b-hue');
  document.querySelectorAll('[data-ntf-07b]').forEach(function(btn){
    btn.addEventListener('click',function(){
      var type=btn.getAttribute('data-ntf-07b'),d=COPY[type];
      document.querySelectorAll('[data-ntf-07b]').forEach(function(b){ b.classList.toggle('is-on',b===btn); });
      toast.setAttribute('data-type',type);
      toast.setAttribute('role',type==='error'||type==='warning'?'alert':'status');
      title.textContent=d[0]; sub.textContent=d[1]; hue.textContent='--hue: '+d[2];
    });
  });
})();
```

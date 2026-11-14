---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/dark-mode-toast-notification-css/"
title: "Dark Mode Toast Notification CSS"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Dark-mode toasts done as a system, not a re-skin: a light-dark() token sheet where flipping one color-scheme declaration re-themes every toast with zero…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Toast Notification CSS
Source: https://codefronts.com/snippets/css-notifications/dark-mode-toast-notification-css/

Dark-mode toasts done as a system, not a re-skin: a light-dark() token sheet where flipping one color-scheme declaration re-themes every toast with zero duplicated selectors, and a true-black OLED suite built on high-contrast accent borders with the actual WCAG contrast ratios printed on each toast.
## HTML
```html
<div class="ntf-05-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-05a" aria-label="Toast theme flipped by light-dark tokens">
  <div class="ntf-05a__stage">
    <label class="ntf-05a__switch"><input type="checkbox" id="ntf-05a-dark"><span class="ntf-05a__track" aria-hidden="true"><i></i></span><span class="ntf-05a__mode"></span></label>
    <h2 class="ntf-05a__title">One token sheet, two themes</h2>
    <p class="ntf-05a__sub">Every color below is a single <b>light-dark()</b> declaration — the switch just flips <b>color-scheme</b>.</p>
    <div class="ntf-05a__toasts">
      <div class="ntf-05a__toast" role="status"><span class="ntf-05a__chip ntf-05a__chip--ok" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span><span class="ntf-05a__tx"><b>Backup complete</b><small>142 files · encrypted</small></span><button class="ntf-05a__x" type="button" aria-label="Dismiss">&#10005;</button></div>
      <div class="ntf-05a__toast" role="alert"><span class="ntf-05a__chip ntf-05a__chip--err" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M12 8v5m0 3.5v.5"/><circle cx="12" cy="12" r="9.2"/></svg></span><span class="ntf-05a__tx"><b>Payment failed</b><small>Card ending 4242 was declined</small></span><button class="ntf-05a__x" type="button" aria-label="Dismiss">&#10005;</button></div>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="ntf-05b" aria-label="True black toasts with printed contrast ratios">
  <div class="ntf-05b__stage">
    <p class="ntf-05b__eyebrow">TRUE BLACK · #000000</p>
    <h2 class="ntf-05b__title">Identity by border, not by tint</h2>
    <div class="ntf-05b__list">
      <div class="ntf-05b__toast" style="--acc:oklch(0.82 0.16 160)" role="status"><span class="ntf-05b__tx"><b>Deploy succeeded</b><small>edge · 34 regions</small></span><code class="ntf-05b__ratio">text 17.4:1 &nbsp;AAA</code></div>
      <div class="ntf-05b__toast" style="--acc:oklch(0.84 0.14 85)" role="status"><span class="ntf-05b__tx"><b>Rate limit near</b><small>4,812 / 5,000 requests</small></span><code class="ntf-05b__ratio">accent 13.9:1 &nbsp;AAA</code></div>
      <div class="ntf-05b__toast" style="--acc:oklch(0.76 0.16 22)" role="alert"><span class="ntf-05b__tx"><b>Job failed</b><small>ingest-7 · exit code 137</small></span><code class="ntf-05b__ratio">accent 9.2:1 &nbsp;AAA</code></div>
    </div>
    <p class="ntf-05b__note">On OLED black, tinted surfaces vanish — the 3px inline-start border and a bright accent carry the state. Text is #f2f5fa, not #fff, to avoid halation.</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-05-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-05-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-05a,
.ntf-05a *,
.ntf-05a *::before,
.ntf-05a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-05a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  color-scheme: light dark;
  --bg: light-dark(#f2f4f8,#0c0f15);
  --surface: light-dark(#ffffff,#171b23);
  --text: light-dark(#1d212b,#e9eef8);
  --mut: light-dark(rgb(29 33 43 / .55),rgb(215 226 245 / .55));
  --line: light-dark(rgb(29 33 43 / .12),rgb(160 180 220 / .2));
  --ok: light-dark(oklch(0.55 0.14 155),oklch(0.8 0.15 160));
  --err: light-dark(oklch(0.55 0.19 25),oklch(0.74 0.17 22));
  background: var(--bg);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
  transition: background .35s;
}

.ntf-05a:has(#ntf-05a-dark:checked) {
  color-scheme: dark;
}

.ntf-05a__stage {
  width: min(460px,100%);
  text-align: center;
}

.ntf-05a__switch {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}

.ntf-05a__switch input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ntf-05a__track {
  width: 46px;
  height: 26px;
  border-radius: 999px;
  background: var(--line);
  padding: 3px;
  transition: background .25s;
}

.ntf-05a__track i {
  display: block;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--surface);
  box-shadow: 0 1px 3px rgb(0 0 0 / .3);
  transition: translate .25s cubic-bezier(.22,1.2,.36,1);
}

.ntf-05a:has(#ntf-05a-dark:checked) .ntf-05a__track i {
  translate: 20px 0;
}

.ntf-05a__switch:has(input:focus-visible) .ntf-05a__track {
  outline: 2px solid var(--text);
  outline-offset: 2px;
}

.ntf-05a__mode {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--mut);
}

.ntf-05a__mode::after {
  content: "OS theme · click to force dark";
}

.ntf-05a:has(#ntf-05a-dark:checked) .ntf-05a__mode::after {
  content: "Forced dark via color-scheme";
}

.ntf-05a__title {
  margin-top: 22px;
  font-size: 24px;
  font-weight: 600;
  letter-spacing: -.01em;
  color: var(--text);
}

.ntf-05a__sub {
  margin-top: 8px;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--mut);
}

.ntf-05a__sub b {
  color: var(--text);
}

.ntf-05a__toasts {
  margin-top: 26px;
  display: grid;
  gap: 12px;
  text-align: left;
}

.ntf-05a__toast {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 15px;
  border-radius: 15px;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 16px 40px -22px rgb(0 0 0 / .45);
  transition: background .35s,border-color .35s;
}

.ntf-05a__chip {
  flex: none;
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 11px;
  color: light-dark(#fff,#0c0f15);
}

.ntf-05a__chip svg {
  width: 18px;
  height: 18px;
}

.ntf-05a__chip--ok {
  background: var(--ok);
}

.ntf-05a__chip--err {
  background: var(--err);
}

.ntf-05a__tx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-05a__tx b {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--text);
}

.ntf-05a__tx small {
  font-size: 11.5px;
  color: var(--mut);
}

.ntf-05a__x {
  margin-left: auto;
  flex: none;
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 8px;
  font-size: 12px;
  color: var(--mut);
  background: transparent;
  cursor: pointer;
  transition: background .15s,color .15s;
}

.ntf-05a__x:hover {
  background: var(--line);
  color: var(--text);
}

@media (prefers-reduced-motion: reduce) {
  .ntf-05a,
    .ntf-05a__toast,
    .ntf-05a__track i {
    transition-duration: .01s;
  }
}

.ntf-05b,
.ntf-05b *,
.ntf-05b *::before,
.ntf-05b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-05b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #000;
  font-family: 'Sora','Segoe UI',system-ui,sans-serif;
}

.ntf-05b__stage {
  width: min(440px,100%);
}

.ntf-05b__eyebrow {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10.5px;
  letter-spacing: .22em;
  color: rgba(242,245,250,.45);
  text-align: center;
}

.ntf-05b__title {
  margin-top: 10px;
  font-size: 23px;
  font-weight: 600;
  letter-spacing: -.01em;
  color: #f2f5fa;
  text-align: center;
}

.ntf-05b__list {
  margin-top: 26px;
  display: grid;
  gap: 12px;
}

.ntf-05b__toast {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 15px 16px;
  border-radius: 14px;
  background: #0a0c10;
  border: 1px solid rgba(242,245,250,.13);
  border-inline-start: 3px solid var(--acc);
  box-shadow: inset 0 1px 0 rgba(242,245,250,.05);
  animation: ntf-05b-in .5s cubic-bezier(.22,1.2,.36,1) both;
}

.ntf-05b__toast:nth-child(2) {
  animation-delay: .08s;
}

.ntf-05b__toast:nth-child(3) {
  animation-delay: .16s;
}

.ntf-05b__tx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-05b__tx b {
  font-size: 13.5px;
  font-weight: 600;
  color: #f2f5fa;
}

.ntf-05b__tx small {
  font-size: 11.5px;
  color: rgba(242,245,250,.55);
}

.ntf-05b__ratio {
  margin-left: auto;
  flex: none;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10px;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc),transparent 88%);
  border: 1px solid color-mix(in oklch,var(--acc),transparent 70%);
  padding: 4px 8px;
  border-radius: 7px;
}

.ntf-05b__note {
  margin-top: 22px;
  font-size: 12px;
  line-height: 1.65;
  color: rgba(242,245,250,.45);
  text-align: center;
  text-wrap: pretty;
}

@keyframes ntf-05b-in {
  from {
    opacity: 0;
    translate: 0 14px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-05b__toast {
    animation: ntf-05b-rm .2s ease both;
  }

  @keyframes ntf-05b-rm {
    from {
      opacity: 0;
    }
  }
}
```

## JavaScript
```js
(function(){
  /* Optional persistence — light-dark() handles all theming; JS only remembers the override. */
  var box=document.getElementById('ntf-05a-dark'); if(!box) return;
  box.addEventListener('change',function(){
    try{ localStorage.setItem('ntf-05a-theme',box.checked?'dark':'auto'); }catch(e){}
  });
  try{ if(localStorage.getItem('ntf-05a-theme')==='dark') box.checked=true; }catch(e){}
})();

/* No JavaScript — this is a design-token study: true-black stage, near-black #0a0c10 panels, identity carried by the accent border, and every contrast pairing audited to WCAG AAA (ratios printed on the toasts). */
```

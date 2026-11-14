---
source: "codefronts"
url: "https://codefronts.com/snippets/css-variable-dark-mode-system/anti-fouc-head-script/"
title: "Prevent Dark Mode Flash of Unstyled Content (FOUC) with a Blocking Inline Head Script"
section: "snippets"
category: "css-variable-dark-mode-system"
category_name: "CSS Variable Dark Mode Systems"
description: "The fix for the most-reported dark-mode bug: the split-second white flash on every reload before your theme JS runs."
has_js: "true"
---

Here's a working CSS Variable Dark Mode System from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Prevent Dark Mode Flash of Unstyled Content (FOUC) with a Blocking Inline Head Script
Source: https://codefronts.com/snippets/css-variable-dark-mode-system/anti-fouc-head-script/

The fix for the most-reported dark-mode bug: the split-second white flash on every reload before your theme JS runs. A tiny render-blocking script placed first in the <head> reads localStorage (falling back to the OS preference) and stamps data-theme onto <html> BEFORE the browser paints a single pixel — so the page loads already-dark, with zero flicker.
## HTML
```html
<section class="cdm-03" data-theme="light">
  <div class="cdm-03__card">
    <span class="cdm-03__pill">Loaded flicker-free</span>
    <h1>No flash of white on reload</h1>
    <p>The theme for this frame was set inside <code>&lt;head&gt;</code> before the first paint. Hit reload — it stays dark (or light) with no white blink in between.</p>
    <button class="cdm-03__btn" type="button" aria-pressed="false">Toggle &amp; reload to prove it</button>
    <small class="cdm-03__note">View the code tab to see the exact <code>&lt;head&gt;</code> snippet.</small>
  </div>
</section>
```
## CSS
```css
.cdm-03,
.cdm-03 *,
.cdm-03 *::before,
.cdm-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdm-03 {
  --bg: oklch(0.98 0.004 250);
  --surface: oklch(1 0 0);
  --text: oklch(0.24 0.02 265);
  --border: oklch(0.9 0.008 265);
  --accent: oklch(0.55 0.16 210);
  color-scheme: light;
  --muted: color-mix(in oklab,var(--text) 60%,var(--bg));
  --hover: color-mix(in oklab,var(--text) 8%,transparent);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 32px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--text);
  transition: background-color .3s ease,color .3s ease;
}

.cdm-03[data-theme="dark"] {
  --bg: oklch(0.15 0.02 240);
  --surface: oklch(0.2 0.02 240);
  --text: oklch(0.95 0.005 240);
  --border: oklch(0.31 0.02 240);
  --accent: oklch(0.72 0.14 210);
  color-scheme: dark;
}

.cdm-03__card {
  width: min(440px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 30px;
  border-radius: 18px;
  background: var(--surface);
  border: 1px solid var(--border);
}

.cdm-03__pill {
  align-self: flex-start;
  padding: 5px 11px;
  border-radius: 999px;
  font: 600 11px/1 system-ui,sans-serif;
  letter-spacing: .03em;
  text-transform: uppercase;
  color: #fff;
  background: var(--accent);
}

.cdm-03__card h1 {
  font: 700 clamp(22px,4vw,30px)/1.15 system-ui,sans-serif;
  letter-spacing: -.01em;
}

.cdm-03__card p {
  font: 400 14.5px/1.6 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.cdm-03 code {
  font: 600 12.5px/1 ui-monospace,Menlo,monospace;
  padding: 2px 5px;
  border-radius: 5px;
  background: var(--hover);
  color: var(--text);
}

.cdm-03__btn {
  align-self: flex-start;
  min-height: 44px;
  padding: 0 20px;
  border: 1px solid var(--border);
  border-radius: 11px;
  background: var(--bg);
  color: var(--text);
  font: 600 14px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: background-color .2s ease;
}

.cdm-03__btn:hover {
  background: var(--hover);
}

.cdm-03__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdm-03__note {
  font: 400 12px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .cdm-03 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* ════════════════════════════════════════════════════════════════════
   PART 1 — HEAD SCRIPT · place FIRST in your document head, before CSS
   ════════════════════════════════════════════════════════════════════
   Synchronous, blocking. Runs before first paint and sets data-theme
   on the html element, so the browser applies the correct CSS
   variables from the very first render. No FOUC, no flicker.

   The head-script body (embed inside a plain script tag as the very
   first thing in your document head, before any stylesheet link):

     (function () {
       try {
         var t = localStorage.getItem('cf-theme')
           || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
         document.documentElement.dataset.theme = t;
         document.documentElement.style.colorScheme = t;   // native UI too
       } catch (e) {}
     })();

   ════════════════════════════════════════════════════════════════════
   PART 2 — TOGGLE BUTTON · loaded normally at end of body
   ════════════════════════════════════════════════════════════════════
   Reuses the same 'cf-theme' localStorage key the head script reads,
   so reloads never flash.

   NOTE: in your real site the toggle writes to document.documentElement
   (the html element) so the theme applies globally and the head script
   picks it up on next reload. Here in the isolated demo card, we scope
   the toggle to the .cdm-03 wrapper so it doesn't accidentally theme
   the whole page around the demo. The pattern is identical — only the
   target element changes. */
(function () {
  var KEY = 'cf-theme';
  var root = document.querySelector('.cdm-03');
  if (!root) return;
  var btn = root.querySelector('.cdm-03__btn');
  function sync(){ btn.setAttribute('aria-pressed', String(root.dataset.theme === 'dark')); }
  sync();
  btn.addEventListener('click', function () {
    var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem(KEY, next); } catch (e) {}
    sync();
  });
})();
```

---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/speed-dial-radial-menu-fab-with-backdrop/"
title: "Speed Dial Radial Menu FAB with Backdrop"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "The speed dial: one FAB, four actions arranged on a quarter-circle, a scrim that dims the page so the choice feels modal, and labels that arrive a beat after…"
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Speed Dial Radial Menu FAB with Backdrop
Source: https://codefronts.com/components/css-floating-buttons/speed-dial-radial-menu-fab-with-backdrop/

The speed dial: one FAB, four actions arranged on a quarter-circle, a scrim that dims the page so the choice feels modal, and labels that arrive a beat after their icons. The arrangement is computed in CSS with cos() and sin() from a per-item index, so adding a fifth action is one line of HTML — no re-tuning of translate values.
## HTML
```html
<section class="fb-07" aria-label="Speed dial radial menu demo">
  <div class="fb-07__page">
    <p class="fb-07__eyebrow">cos() · sin() · staggered delay</p>
    <h2 class="fb-07__title">Four actions on a quarter-circle</h2>
    <p class="fb-07__sub">The arc is computed from an index, not hard-coded. Open it and the dial fans out in sequence; close it and the order reverses.</p>
    <p class="fb-07__chip">--i · --step:30deg · --r:132px</p>
  </div>
  <div class="fb-07__scrim" id="fb-07-scrim" hidden></div>
  <div class="fb-07__dial" id="fb-07-dial">
    <ul class="fb-07__acts" id="fb-07-acts">
      <li style="--fb-07-i:0"><button class="fb-07__act" type="button" tabindex="-1"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16v12H4z" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="13" r="3.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9 7l1.4-2h3.2L15 7" fill="none" stroke="currentColor" stroke-width="1.8"/></svg><span class="fb-07__lab">Photo</span></button></li>
      <li style="--fb-07-i:1"><button class="fb-07__act" type="button" tabindex="-1"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 4h9l4 4v12H6z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M15 4v5h4" fill="none" stroke="currentColor" stroke-width="1.8"/></svg><span class="fb-07__lab">Document</span></button></li>
      <li style="--fb-07-i:2"><button class="fb-07__act" type="button" tabindex="-1"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 15a3.2 3.2 0 0 0 3.2-3.2V7a3.2 3.2 0 1 0-6.4 0v4.8A3.2 3.2 0 0 0 12 15z" fill="currentColor"/><path d="M6.5 11.6a5.5 5.5 0 0 0 11 0M12 17.2V21" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span class="fb-07__lab">Voice note</span></button></li>
      <li style="--fb-07-i:3"><button class="fb-07__act" type="button" tabindex="-1"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="10" r="3" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 21s6-5.4 6-10a6 6 0 1 0-12 0c0 4.6 6 10 6 10z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg><span class="fb-07__lab">Location</span></button></li>
    </ul>
    <button class="fb-07__fab" id="fb-07-fab" type="button" aria-expanded="false" aria-controls="fb-07-acts" aria-label="Open quick actions">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-07-bg);
  --fb-07-bg: radial-gradient(110% 80% at 80% 90%,oklch(0.32 0.09 300),oklch(0.17 0.04 285) 70%);
  --fb-07-accent: oklch(0.72 0.19 330);
  --fb-07-ink: oklch(0.97 0.01 300);
  --fb-07-mut: oklch(0.78 0.02 300);
  --fb-07-r: clamp(104px,24vw,138px);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-07-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-07 *,
.fb-07 *::before,
.fb-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-07__page {
  width: min(100%,54ch);
  display: grid;
  gap: 12px;
  justify-items: center;
  text-align: center;
}

.fb-07__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-07-accent);
}

.fb-07__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-07__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-07-mut);
  text-wrap: pretty;
}

.fb-07__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-07-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.18);
  border-radius: 99px;
}

.fb-07__scrim {
  position: absolute;
  inset: 0;
  z-index: 4;
  background: oklch(0.14 0.03 290/.6);
  -webkit-backdrop-filter: blur(3px);
  backdrop-filter: blur(3px);
  animation: fb-07-fade .24s ease;
}

.fb-07__scrim[hidden] {
  display: none;
}

@keyframes fb-07-fade {
  from {
    opacity: 0;
  }
}

.fb-07__dial {
  position: absolute;
  right: clamp(26px,6vw,64px);
  bottom: calc(clamp(26px,6vw,64px) + env(safe-area-inset-bottom));
  z-index: 5;
  width: 62px;
  height: 62px;
}

.fb-07__acts {
  list-style: none;
  position: absolute;
  inset: 0;
}

.fb-07__acts li {
  position: absolute;
  inset: 0;
  --fb-07-a: calc(var(--fb-07-i) * 30deg);
}

.fb-07__act {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  margin: 5px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  color: oklch(0.28 0.05 300);
  background: oklch(0.98 0.01 300);
  box-shadow: 0 8px 22px -8px oklch(0.1 0.03 290/.9);
  opacity: 0;
  scale: .3;
  translate: 0 0;
  pointer-events: none;
  transition: translate .38s cubic-bezier(.2,1.15,.35,1),scale .34s cubic-bezier(.2,1.3,.35,1),opacity .24s ease;
  transition-delay: calc((3 - var(--fb-07-i)) * 45ms);
}

.fb-07__act svg {
  width: 23px;
  height: 23px;
}

.fb-07__lab {
  position: absolute;
  right: calc(100% + 12px);
  white-space: nowrap;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--fb-07-ink);
  background: oklch(0.18 0.03 290/.86);
  border: 1px solid oklch(1 0 0/.12);
  padding: 5px 11px;
  border-radius: 8px;
  opacity: 0;
  translate: 8px 0;
  transition: opacity .2s ease,translate .2s ease;
  transition-delay: calc(var(--fb-07-i) * 45ms + 120ms);
}

.fb-07__dial[data-open="true"] .fb-07__act {
  opacity: 1;
  scale: 1;
  pointer-events: auto;
  translate: calc(cos(var(--fb-07-a)) * var(--fb-07-r) * -1) calc(sin(var(--fb-07-a)) * var(--fb-07-r) * -1);
  transition-delay: calc(var(--fb-07-i) * 55ms);
}

.fb-07__dial[data-open="true"] .fb-07__lab {
  opacity: 1;
  translate: 0 0;
}

.fb-07__act:hover {
  background: var(--fb-07-accent);
  color: oklch(0.16 0.04 330);
}

.fb-07__act:focus-visible {
  outline: 3px solid var(--fb-07-accent);
  outline-offset: 3px;
}

.fb-07__act:active {
  scale: .92;
}

.fb-07__fab {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  width: 62px;
  height: 62px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  color: oklch(0.15 0.04 330);
  background: linear-gradient(150deg,oklch(0.82 0.17 90),var(--fb-07-accent));
  box-shadow: 0 14px 34px -10px oklch(0.72 0.19 330/.8),0 2px 6px oklch(0.1 0.03 290/.5);
  transition: transform .3s cubic-bezier(.2,1.3,.4,1),box-shadow .3s ease;
}

.fb-07__fab svg {
  width: 27px;
  height: 27px;
  transition: rotate .34s cubic-bezier(.3,1.35,.4,1);
}

.fb-07__fab:hover {
  transform: scale(1.05);
}

.fb-07__fab:active {
  transform: scale(.93);
}

.fb-07__fab:focus-visible {
  outline: 3px solid oklch(0.98 0.01 300);
  outline-offset: 4px;
}

.fb-07__fab[aria-expanded="true"] svg {
  rotate: 135deg;
}

@media (prefers-reduced-motion: reduce) {
  .fb-07 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const dial = document.getElementById('fb-07-dial');
  const fab = document.getElementById('fb-07-fab');
  const scrim = document.getElementById('fb-07-scrim');
  if (!dial || !fab || fab.dataset.fbWired) return;
  fab.dataset.fbWired = '1';
  const acts = [...dial.querySelectorAll('.fb-07__act')];
  const set = (open) => {
    dial.dataset.open = String(open);
    fab.setAttribute('aria-expanded', String(open));
    fab.setAttribute('aria-label', open ? 'Close quick actions' : 'Open quick actions');
    scrim.hidden = !open;
    acts.forEach((a) => { a.tabIndex = open ? 0 : -1; });
    if (open) setTimeout(() => acts[0].focus(), 120);
  };
  fab.addEventListener('click', () => set(dial.dataset.open !== 'true'));
  scrim.addEventListener('click', () => { set(false); fab.focus(); });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && dial.dataset.open === 'true') { set(false); fab.focus(); }
  });
  acts.forEach((a) => a.addEventListener('click', () => { set(false); fab.focus(); }));
})();
```

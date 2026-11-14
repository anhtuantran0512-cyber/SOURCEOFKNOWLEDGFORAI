---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/slide-in-ribbon-notification/"
title: "Slide-In Ribbon Notification"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "The announcement ribbon that drops from the top of the viewport — built on the platform's own popover API, so it lives in the top layer above everything…"
has_js: "true"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slide-In Ribbon Notification
Source: https://codefronts.com/snippets/css-ribbons/slide-in-ribbon-notification/

The announcement ribbon that drops from the top of the viewport — built on the platform's own popover API, so it lives in the top layer above everything without a z-index war. The entry animation uses @starting-style and transition-behavior: allow-discrete, the pair that finally makes it possible to animate an element in and out of display: none with pure CSS.
## HTML
```html
<section class="rib-18" aria-label="Slide in ribbon notification toast demo">
  <div class="rib-18__stage">
    <div class="rib-18__panel">
      <h2 class="rib-18__title">Ribbon notifications</h2>
      <p class="rib-18__sub">Three tones, one component. Each drops from the top layer with a <code>@starting-style</code> entry and an <code>allow-discrete</code> exit.</p>
      <div class="rib-18__buttons">
        <button class="rib-18__btn" type="button" popovertarget="rib-18-ok">Show success</button>
        <button class="rib-18__btn" type="button" popovertarget="rib-18-warn">Show warning</button>
        <button class="rib-18__btn" type="button" popovertarget="rib-18-err">Show error</button>
      </div>
      <p class="rib-18__note">Toasts pause their auto-dismiss while hovered or focused.</p>
    </div>

    <div class="rib-18__toast" id="rib-18-ok" popover="manual" data-tone="ok" role="status" data-timeout="4500">
      <span class="rib-18__ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="m9.6 16.4-4-4L4.2 13.8l5.4 5.4 10-10-1.4-1.4z"/></svg></span>
      <span class="rib-18__txt"><strong>Deployment complete.</strong> build 2481 is live in eu-west-1.</span>
      <button class="rib-18__x" type="button" popovertarget="rib-18-ok" popovertargetaction="hide" aria-label="Dismiss notification">✕</button>
    </div>
    <div class="rib-18__toast" id="rib-18-warn" popover="manual" data-tone="warn" role="status" data-timeout="6000">
      <span class="rib-18__ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M12 2 1 21h22L12 2Zm1 14h-2v2h2v-2Zm0-7h-2v5h2V9Z"/></svg></span>
      <span class="rib-18__txt"><strong>Certificate expires in 6 days.</strong> renew before 15 Aug to avoid downtime.</span>
      <button class="rib-18__x" type="button" popovertarget="rib-18-warn" popovertargetaction="hide" aria-label="Dismiss notification">✕</button>
    </div>
    <div class="rib-18__toast" id="rib-18-err" popover="manual" data-tone="err" role="alert" data-timeout="0">
      <span class="rib-18__ic" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm1 15h-2v-2h2v2Zm0-4h-2V7h2v6Z"/></svg></span>
      <span class="rib-18__txt"><strong>Payment method declined.</strong> update your card to keep the workspace active.</span>
      <button class="rib-18__x" type="button" popovertarget="rib-18-err" popovertargetaction="hide" aria-label="Dismiss notification">✕</button>
    </div>

    <p class="rib-18__chip" aria-hidden="true">popover=&quot;manual&quot; · @starting-style · transition-behavior: allow-discrete · overlay</p>
  </div>
</section>
```
## CSS
```css
.rib-18,
.rib-18 *,
.rib-18 *::before,
.rib-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-18-bg: #0e1014;
  --rib-18-bg: oklch(0.18 0.008 260);
  --rib-18-panel: #171a21;
  --rib-18-panel: oklch(0.23 0.01 260);
  --rib-18-ink: #eff1f6;
  --rib-18-ink: oklch(0.95 0.005 260);
  --rib-18-mut: #8a90a0;
  --rib-18-mut: oklch(0.65 0.014 260);
  --rib-18-ok: #2fbf71;
  --rib-18-ok: oklch(0.72 0.16 155);
  --rib-18-warn: #e8a83a;
  --rib-18-warn: oklch(0.78 0.15 78);
  --rib-18-err: #f2555f;
  --rib-18-err: oklch(0.66 0.21 18);
  background: var(--rib-18-bg);
  color: var(--rib-18-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,3vw,24px);
  padding: clamp(20px,5vw,56px);
}

.rib-18__panel {
  width: min(100%,540px);
  display: grid;
  gap: 12px;
  padding: clamp(24px,5vw,34px);
  border-radius: 22px;
  background: var(--rib-18-panel);
  border: 1px solid oklch(1 0 0/.09);
  box-shadow: 0 30px 66px -34px oklch(0 0 0/.85);
}

.rib-18__title {
  font-size: clamp(22px,4vw,30px);
  font-weight: 660;
  letter-spacing: -.032em;
}

.rib-18__sub {
  font-size: 14px;
  line-height: 1.6;
  color: var(--rib-18-mut);
  text-wrap: pretty;
}

.rib-18__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  padding: 2px 5px;
  border-radius: 5px;
  background: oklch(1 0 0/.08);
}

.rib-18__buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  margin-block-start: 6px;
}

.rib-18__btn {
  min-height: 46px;
  padding-inline: 18px;
  border: 1.5px solid oklch(1 0 0/.16);
  border-radius: 12px;
  background: oklch(1 0 0/.04);
  color: var(--rib-18-ink);
  font: inherit;
  font-size: 14px;
  font-weight: 620;
  cursor: pointer;
  transition: background .22s,border-color .22s,translate .18s;
}

.rib-18__btn:hover {
  background: oklch(1 0 0/.09);
  translate: 0 -1px;
}

.rib-18__btn:focus-visible {
  outline: 3px solid var(--rib-18-ok);
  outline-offset: 3px;
}

.rib-18__note {
  font-size: 12px;
  color: var(--rib-18-mut);
}

.rib-18__toast {
  position: fixed;
  inset-block-start: 22px;
  inset-inline: 0;
  margin-inline: auto;
  inline-size: min(calc(100% - 32px),520px);
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 14px 14px 14px 16px;
  border: 0;
  border-radius: 14px;
  color: oklch(0.16 0.01 260);
  background: var(--rib-18-tone,var(--rib-18-ok));
  box-shadow: 0 18px 44px -14px oklch(0 0 0/.7),inset 0 1px 0 oklch(1 0 0/.35);
  translate: 0 -140%;
  opacity: 0;
  transition: translate .5s cubic-bezier(.16,1,.3,1),opacity .32s ease,display .5s allow-discrete,overlay .5s allow-discrete;
}

.rib-18__toast[data-tone="ok"] {
  --rib-18-tone: var(--rib-18-ok);
}

.rib-18__toast[data-tone="warn"] {
  --rib-18-tone: var(--rib-18-warn);
}

.rib-18__toast[data-tone="err"] {
  --rib-18-tone: var(--rib-18-err);
}

.rib-18__toast:popover-open {
  translate: 0 0;
  opacity: 1;
}

@starting-style {
  .rib-18__toast:popover-open {
    translate: 0 -140%;
    opacity: 0;
  }
}

.rib-18__toast::backdrop {
  background: transparent;
}

.rib-18__ic {
  flex: none;
  inline-size: 30px;
  block-size: 30px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  background: oklch(0 0 0/.16);
}

.rib-18__txt {
  flex: 1;
  font-size: 13.5px;
  line-height: 1.42;
  text-wrap: pretty;
}

.rib-18__txt strong {
  font-weight: 750;
}

.rib-18__x {
  flex: none;
  inline-size: 34px;
  block-size: 34px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 9px;
  background: oklch(0 0 0/.1);
  color: inherit;
  font-size: 13px;
  cursor: pointer;
  transition: background .2s;
}

.rib-18__x:hover {
  background: oklch(0 0 0/.22);
}

.rib-18__x:focus-visible {
  outline: 2.5px solid oklch(0.16 0.01 260);
  outline-offset: 2px;
}

.rib-18__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-18-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-18__toast {
    transition: opacity .01ms,display .01ms allow-discrete,overlay .01ms allow-discrete;
    translate: 0 0;
  }

  @starting-style {
    .rib-18__toast:popover-open {
      translate: 0 0;
      opacity: 0;
    }
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.rib-18__stage').forEach((stage) => {
    if (stage.dataset.wired) return;
    stage.dataset.wired = '1';

    stage.querySelectorAll('.rib-18__toast').forEach((toast) => {
      const ms = +toast.dataset.timeout || 0;   // 0 = never auto-dismiss (errors)
      let timer = 0, remaining = ms, startedAt = 0;

      const start = () => {
        if (!remaining) return;
        startedAt = performance.now();
        timer = setTimeout(() => toast.hidePopover(), remaining);
      };
      const pause = () => {                      // WCAG 2.2.1: never yank it away mid-read
        if (!timer) return;
        clearTimeout(timer); timer = 0;
        remaining -= performance.now() - startedAt;
      };

      toast.addEventListener('toggle', (e) => {
        if (e.newState === 'open') { remaining = ms; start(); }
        else { clearTimeout(timer); timer = 0; }
      });
      toast.addEventListener('pointerenter', pause);
      toast.addEventListener('focusin', pause);
      toast.addEventListener('pointerleave', start);
      toast.addEventListener('focusout', (e) => { if (!toast.contains(e.relatedTarget)) start(); });
    });

    // Only one ribbon at a time — manual popovers do not close each other.
    stage.querySelectorAll('.rib-18__btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        stage.querySelectorAll('.rib-18__toast').forEach((t) => {
          if (t.id !== btn.getAttribute('popovertarget') && t.matches(':popover-open')) t.hidePopover();
        });
      });
    });
  });
})();
```

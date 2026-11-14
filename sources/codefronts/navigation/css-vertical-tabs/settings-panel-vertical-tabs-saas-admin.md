---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/settings-panel-vertical-tabs-saas-admin/"
title: "Settings Panel Vertical Tabs (SaaS Admin)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "The account-settings layout every SaaS product converges on: a grouped navigation rail, a wide form column with real controls, and a sticky save bar that…"
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Settings Panel Vertical Tabs (SaaS Admin)
Source: https://codefronts.com/navigation/css-vertical-tabs/settings-panel-vertical-tabs-saas-admin/

The account-settings layout every SaaS product converges on: a grouped navigation rail, a wide form column with real controls, and a sticky save bar that only matters once something changed. Built as a two-column CSS Grid with a scroll-contained panel, CSS-only toggle switches and segmented controls — a complete, credible admin surface, not a lorem-ipsum shell.
## HTML
```html
<section class="vt-09" aria-label="SaaS settings panel vertical tabs demo">
  <div class="vt-09__stage">
    <div class="vt-09__app" role="radiogroup" aria-label="Account settings sections">
      <aside class="vt-09__rail">
        <div class="vt-09__col">
          <p class="vt-09__brand">Acme Console</p>
          <p class="vt-09__group">Account</p>
          <input class="vt-09__radio" type="radio" name="vt-09" id="vt-09-t1" checked>
          <label class="vt-09__tab" for="vt-09-t1">Profile</label>
          <input class="vt-09__radio" type="radio" name="vt-09" id="vt-09-t2">
          <label class="vt-09__tab" for="vt-09-t2">Notifications</label>
          <p class="vt-09__group">Workspace</p>
          <input class="vt-09__radio" type="radio" name="vt-09" id="vt-09-t3">
          <label class="vt-09__tab" for="vt-09-t3">Members<span class="vt-09__count">12</span></label>
          <input class="vt-09__radio" type="radio" name="vt-09" id="vt-09-t4">
          <label class="vt-09__tab" for="vt-09-t4">API keys</label>
        </div>
        <div class="vt-09__panels">
          <div class="vt-09__panel" id="vt-09-p1"><header class="vt-09__ph"><h3>Profile</h3><p>How you appear across the workspace.</p></header>
            <div class="vt-09__row"><div><b>Display name</b><span>Shown on comments and mentions</span></div><span class="vt-09__field">Jordan Ellis</span></div>
            <div class="vt-09__row"><div><b>Time zone</b><span>Used for digests and scheduling</span></div><span class="vt-09__field">UTC−05:00 · New York</span></div>
            <div class="vt-09__row"><div><b>Profile visibility</b><span>Who can see your activity</span></div><label class="vt-09__switch"><input type="checkbox" checked><i></i><span class="vt-09__sr">Profile visibility</span></label></div></div>
          <div class="vt-09__panel" id="vt-09-p2"><header class="vt-09__ph"><h3>Notifications</h3><p>Every switch below is a real checkbox with <code>appearance:none</code>.</p></header>
            <div class="vt-09__row"><div><b>Product updates</b><span>Monthly changelog digest</span></div><label class="vt-09__switch"><input type="checkbox" checked><i></i><span class="vt-09__sr">Product updates</span></label></div>
            <div class="vt-09__row"><div><b>Mentions</b><span>When someone @mentions you</span></div><label class="vt-09__switch"><input type="checkbox" checked><i></i><span class="vt-09__sr">Mentions</span></label></div>
            <div class="vt-09__row"><div><b>Marketing email</b><span>Occasional launch news</span></div><label class="vt-09__switch"><input type="checkbox"><i></i><span class="vt-09__sr">Marketing email</span></label></div></div>
          <div class="vt-09__panel" id="vt-09-p3"><header class="vt-09__ph"><h3>Members</h3><p>Twelve seats, three roles, one sticky save bar.</p></header>
            <div class="vt-09__row"><div><b>Default role</b><span>Applied to every new invite</span></div><span class="vt-09__field">Editor</span></div>
            <div class="vt-09__row"><div><b>Domain capture</b><span>Auto-join for @acme.com addresses</span></div><label class="vt-09__switch"><input type="checkbox" checked><i></i><span class="vt-09__sr">Domain capture</span></label></div>
            <div class="vt-09__row"><div><b>Guest links</b><span>Share read-only views externally</span></div><label class="vt-09__switch"><input type="checkbox"><i></i><span class="vt-09__sr">Guest links</span></label></div></div>
          <div class="vt-09__panel" id="vt-09-p4"><header class="vt-09__ph"><h3>API keys</h3><p>Long unbreakable strings are exactly why the content column uses <code>minmax(0,1fr)</code>.</p></header>
            <div class="vt-09__row"><div><b>Live key</b><span>Created 14 Mar · last used 2h ago</span></div><span class="vt-09__field vt-09__field--mono">sk-demo-REDACTED</span></div>
            <div class="vt-09__row"><div><b>Rotate automatically</b><span>Every 90 days</span></div><label class="vt-09__switch"><input type="checkbox" checked><i></i><span class="vt-09__sr">Rotate automatically</span></label></div>
            <div class="vt-09__row"><div><b>Webhook endpoint</b><span>Receives signed events</span></div><span class="vt-09__field vt-09__field--mono">https://api.acme.com/v2/hooks/inbound</span></div>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-09-bg);
  --vt-09-bg: oklch(0.955 0.006 260);
  --vt-09-card: oklch(1 0 0);
  --vt-09-rail: oklch(0.978 0.005 260);
  --vt-09-ink: oklch(0.24 0.02 262);
  --vt-09-mut: oklch(0.56 0.018 262);
  --vt-09-acc: oklch(0.56 0.16 250);
  --vt-09-line: oklch(0.24 0.02 262/.1);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-09-ink);
}

.vt-09 *,
.vt-09 *::before,
.vt-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-09__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: clamp(16px,4vw,56px);
  background: radial-gradient(90% 60% at 50% 0%,oklch(0.98 0.02 250),transparent);
}

.vt-09__app {
  width: min(96vw,940px);
}

.vt-09__rail {
  display: grid;
  grid-template-columns: minmax(160px,232px) minmax(0,1fr);
  align-items: stretch;
  background: var(--vt-09-card);
  border: 1px solid var(--vt-09-line);
  border-radius: 18px;
  box-shadow: 0 24px 66px -32px oklch(0.24 0.02 262/.38);
  overflow: hidden;
}

.vt-09__col {
  display: flex;
  flex-direction: column;
  background: var(--vt-09-rail);
  padding: 0 14px 14px;
  border-right: 1px solid var(--vt-09-line);
}

.vt-09__brand {
  padding-block: 16px 10px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.vt-09__group {
  padding-block: 12px 5px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--vt-09-mut) 80%,transparent);
}

.vt-09__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-09__tab {
  display: flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  margin-inline: -4px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 14.2px;
  font-weight: 600;
  color: var(--vt-09-mut);
  cursor: pointer;
  transition: color .18s ease,background .18s ease;
}

.vt-09__count {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 99px;
  background: oklch(0.24 0.02 262/.07);
}

.vt-09__tab:hover {
  color: var(--vt-09-ink);
  background: oklch(0.24 0.02 262/.05);
}

.vt-09__radio:checked+.vt-09__tab {
  color: var(--vt-09-acc);
  background: color-mix(in oklch,var(--vt-09-acc) 12%,transparent);
}

.vt-09__radio:focus-visible+.vt-09__tab {
  outline: 2px solid var(--vt-09-acc);
  outline-offset: 1px;
}

.vt-09__panels {
  display: grid;
  min-height: clamp(300px,42vw,364px);
  max-height: 76svh;
  overflow: auto;
  overscroll-behavior: contain;
}

.vt-09__panel {
  grid-area: 1/1;
  align-content: start;
  display: none;
  gap: 0;
}

.vt-09__app:has(#vt-09-t1:checked) #vt-09-p1,
.vt-09__app:has(#vt-09-t2:checked) #vt-09-p2,
.vt-09__app:has(#vt-09-t3:checked) #vt-09-p3,
.vt-09__app:has(#vt-09-t4:checked) #vt-09-p4 {
  display: grid;
  animation: vt-09-in .3s cubic-bezier(.32,.72,.3,1) both;
}

@keyframes vt-09-in {
  from {
    opacity: 0;
    translate: 0 7px;
  }

  to {
    opacity: 1;
    translate: 0;
  }
}

.vt-09__ph {
  display: grid;
  gap: 5px;
  padding: clamp(18px,2.6vw,26px) clamp(18px,2.6vw,28px) 14px;
  border-bottom: 1px solid var(--vt-09-line);
}

.vt-09__ph h3 {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.vt-09__ph p {
  font-size: 13.4px;
  line-height: 1.55;
  color: var(--vt-09-mut);
  text-wrap: pretty;
}

.vt-09__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  min-height: 64px;
  padding: 12px clamp(18px,2.6vw,28px);
  border-bottom: 1px solid color-mix(in oklch,var(--vt-09-line) 60%,transparent);
}

.vt-09__row>div {
  display: grid;
  gap: 2px;
  min-inline-size: 0;
}

.vt-09__row b {
  font-size: 14px;
  font-weight: 650;
}

.vt-09__row span {
  font-size: 12.6px;
  line-height: 1.5;
  color: var(--vt-09-mut);
}

.vt-09__field {
  flex: none;
  max-inline-size: 52%;
  padding: 7px 12px;
  border: 1px solid var(--vt-09-line);
  border-radius: 9px;
  font-size: 13px !important;
  color: var(--vt-09-ink) !important;
  background: oklch(0.24 0.02 262/.03);
  overflow-wrap: anywhere;
}

.vt-09__field--mono {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.6px !important;
}

.vt-09__switch {
  flex: none;
  position: relative;
  display: inline-grid;
  place-items: center;
  inline-size: 52px;
  block-size: 44px;
  cursor: pointer;
}

.vt-09__switch input {
  appearance: none;
  -webkit-appearance: none;
  margin: 0;
  inline-size: 44px;
  block-size: 26px;
  border-radius: 99px;
  background: oklch(0.24 0.02 262/.16);
  cursor: pointer;
  transition: background .22s ease;
}

.vt-09__switch i {
  position: absolute;
  inset-inline-start: 8px;
  inline-size: 20px;
  block-size: 20px;
  border-radius: 99px;
  background: oklch(1 0 0);
  box-shadow: 0 1px 4px oklch(0.24 0.02 262/.35);
  pointer-events: none;
  transition: translate .26s cubic-bezier(.34,1.3,.5,1);
}

.vt-09__switch input:checked {
  background: var(--vt-09-acc);
}

.vt-09__switch input:checked+i {
  translate: 18px 0;
}

.vt-09__switch input:focus-visible {
  outline: 2px solid var(--vt-09-acc);
  outline-offset: 3px;
}

.vt-09__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.vt-09 code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .86em;
  background: oklch(0.24 0.02 262/.06);
  padding: 1px 5px;
  border-radius: 4px;
}

@media (forced-colors: active) {
  .vt-09__switch input {
    border: 1px solid CanvasText;
  }

  .vt-09__switch input:checked {
    background: Highlight;
  }
}

@media (max-width: 680px) {
  .vt-09__rail {
    grid-template-columns: 1fr;
  }

  .vt-09__col {
    border-right: 0;
    border-bottom: 1px solid var(--vt-09-line);
  }

  .vt-09__field {
    max-inline-size: 44%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-09 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

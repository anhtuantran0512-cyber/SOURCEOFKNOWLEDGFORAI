---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/bootstrap-5-vertical-tabs/"
title: "Bootstrap 5 Vertical Tabs"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "Bootstrap 5's official vertical tab recipe — .d-flex + .nav.flex-column.nav-pills + .tab-content — with the exact class names, data attributes and ARIA…"
has_js: "true"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bootstrap 5 Vertical Tabs
Source: https://codefronts.com/navigation/css-vertical-tabs/bootstrap-5-vertical-tabs/

Bootstrap 5's official vertical tab recipe — .d-flex + .nav.flex-column.nav-pills + .tab-content — with the exact class names, data attributes and ARIA wiring the framework expects, so it drops straight into a Bootstrap project. Ships a 24-line stand-in script and a scoped stylesheet so it also runs with no Bootstrap on the page at all.
## HTML
```html
<section class="vt-06" aria-label="Bootstrap 5 vertical tabs demo">
  <div class="vt-06__stage">
    <div class="vt-06__head">
      <p class="vt-06__eyebrow">Bootstrap 5.3 · nav-pills · flex-column</p>
      <h2 class="vt-06__title">Framework-authentic markup</h2>
    </div>
    <div class="vt-06__card">
      <div class="d-flex align-items-start">
        <div class="nav flex-column nav-pills me-3" id="vt-06-tablist" role="tablist" aria-orientation="vertical">
          <button class="nav-link active" id="vt-06-tab-home" data-bs-toggle="pill" data-bs-target="#vt-06-home" type="button" role="tab" aria-controls="vt-06-home" aria-selected="true">Home</button>
          <button class="nav-link" id="vt-06-tab-profile" data-bs-toggle="pill" data-bs-target="#vt-06-profile" type="button" role="tab" aria-controls="vt-06-profile" aria-selected="false" tabindex="-1">Profile</button>
          <button class="nav-link" id="vt-06-tab-messages" data-bs-toggle="pill" data-bs-target="#vt-06-messages" type="button" role="tab" aria-controls="vt-06-messages" aria-selected="false" tabindex="-1">Messages</button>
          <button class="nav-link" id="vt-06-tab-settings" data-bs-toggle="pill" data-bs-target="#vt-06-settings" type="button" role="tab" aria-controls="vt-06-settings" aria-selected="false" tabindex="-1">Settings</button>
        </div>
        <div class="tab-content" id="vt-06-content">
          <div class="tab-pane fade show active" id="vt-06-home" role="tabpanel" aria-labelledby="vt-06-tab-home" tabindex="0">
            <h3>Buttons, not anchors</h3><p>Bootstrap 5 documents tabs as <code>&lt;button type="button"&gt;</code>. A tab that navigates nowhere should never be a link, and an anchor would hijack the URL.</p><p class="vt-06__note">.nav.flex-column.nav-pills + aria-orientation="vertical"</p>
          </div>
          <div class="tab-pane fade" id="vt-06-profile" role="tabpanel" aria-labelledby="vt-06-tab-profile" tabindex="0">
            <h3>show <em>and</em> active</h3><p>A <code>.fade</code> pane needs both classes on load. <code>active</code> alone leaves it in the layout at opacity 0 — the classic blank-first-tab bug.</p><p class="vt-06__note">class="tab-pane fade show active"</p>
          </div>
          <div class="tab-pane fade" id="vt-06-messages" role="tabpanel" aria-labelledby="vt-06-tab-messages" tabindex="0">
            <h3>tabindex="0" on the pane</h3><p>Panels that can scroll must be focusable, or keyboard users can never reach their content. Bootstrap's own docs require it.</p><p class="vt-06__note">role="tabpanel" tabindex="0"</p>
          </div>
          <div class="tab-pane fade" id="vt-06-settings" role="tabpanel" aria-labelledby="vt-06-tab-settings" tabindex="0">
            <h3>Theme with CSS variables</h3><p>v5.3 exposes <code>--bs-nav-pills-link-active-bg</code>, so you can recolour pills without recompiling any Sass.</p><p class="vt-06__note">--bs-nav-pills-link-active-bg: #6610f2</p>
          </div>
        </div>
      </div>
    </div>
    <p class="vt-06__foot">Runs standalone here. In a real Bootstrap project delete the script — <code>bootstrap.bundle.min.js</code> already owns this behaviour.</p>
  </div>
</section>
```
## CSS
```css
.vt-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-06-bg);
  --vt-06-bg: oklch(0.965 0.008 285);
  --vt-06-card: oklch(1 0 0);
  --vt-06-ink: oklch(0.26 0.02 285);
  --vt-06-mut: oklch(0.55 0.02 285);
  --vt-06-acc: oklch(0.51 0.21 285);
  --vt-06-line: oklch(0.26 0.02 285/.12);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-06-ink);
}

.vt-06 *,
.vt-06 *::before,
.vt-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-06__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(16px,2.6vw,26px);
  padding: clamp(20px,5vw,64px);
  background: radial-gradient(85% 55% at 50% 0%,oklch(0.93 0.05 285/.7),transparent);
}

.vt-06__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
}

.vt-06__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--vt-06-acc);
}

.vt-06__title {
  font-size: clamp(24px,3.6vw,38px);
  line-height: 1.08;
  letter-spacing: -.028em;
  font-weight: 700;
  text-wrap: balance;
}

.vt-06__card {
  width: min(94vw,840px);
  padding: clamp(14px,2.4vw,22px);
  background: var(--vt-06-card);
  border: 1px solid var(--vt-06-line);
  border-radius: 16px;
  box-shadow: 0 22px 60px -30px oklch(0.26 0.02 285/.4);
}

.vt-06 .d-flex {
  display: flex;
}

.vt-06 .align-items-start {
  align-items: flex-start;
}

.vt-06 .flex-column {
  flex-direction: column;
}

.vt-06 .me-3 {
  margin-right: 1rem;
}

.vt-06 .nav {
  display: flex;
  gap: .25rem;
  flex: none;
  inline-size: clamp(140px,24%,190px);
}

.vt-06 .nav-link {
  display: block;
  width: 100%;
  min-height: 46px;
  padding: .6rem .9rem;
  text-align: left;
  font: inherit;
  font-size: 14.4px;
  font-weight: 600;
  color: var(--vt-06-mut);
  background: transparent;
  border: 0;
  border-radius: .5rem;
  cursor: pointer;
  transition: color .18s ease,background .18s ease;
}

.vt-06 .nav-link:hover {
  color: var(--vt-06-acc);
  background: color-mix(in oklch,var(--vt-06-acc) 8%,transparent);
}

.vt-06 .nav-link:focus-visible {
  outline: 2px solid var(--vt-06-acc);
  outline-offset: 2px;
}

.vt-06 .nav-pills .nav-link.active {
  color: oklch(1 0 0);
  background: var(--vt-06-acc);
  box-shadow: 0 6px 18px -8px color-mix(in oklch,var(--vt-06-acc) 85%,transparent);
}

.vt-06 .tab-content {
  flex: 1 1 auto;
  min-inline-size: 0;
  display: grid;
  min-height: clamp(210px,26vw,240px);
  padding: clamp(4px,1vw,10px) clamp(6px,1.4vw,14px);
  border-left: 1px solid var(--vt-06-line);
}

.vt-06 .tab-pane {
  grid-area: 1/1;
  align-content: center;
  display: none;
  gap: 11px;
  padding-inline-start: clamp(12px,2vw,22px);
}

.vt-06 .tab-pane.active {
  display: grid;
}

.vt-06 .tab-pane.fade {
  opacity: 0;
  transform: translateY(6px);
  transition: opacity .28s ease,transform .32s cubic-bezier(.32,.72,.3,1);
}

.vt-06 .tab-pane.fade.show {
  opacity: 1;
  transform: none;
}

.vt-06 .tab-pane:focus-visible {
  outline: 2px solid var(--vt-06-acc);
  outline-offset: 4px;
  border-radius: 10px;
}

.vt-06 .tab-pane h3 {
  font-size: clamp(18px,2.3vw,23px);
  line-height: 1.22;
  letter-spacing: -.02em;
  font-weight: 680;
  text-wrap: balance;
}

.vt-06 .tab-pane p {
  max-width: 46ch;
  font-size: 14.6px;
  line-height: 1.62;
  color: var(--vt-06-mut);
  text-wrap: pretty;
}

.vt-06 code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.26 0.02 285/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.vt-06__note {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px !important;
  color: var(--vt-06-acc) !important;
  padding: 7px 12px;
  border: 1px dashed color-mix(in oklch,var(--vt-06-acc) 40%,transparent);
  border-radius: 8px;
}

.vt-06__foot {
  max-width: 60ch;
  text-align: center;
  font-size: 12.6px;
  line-height: 1.6;
  color: var(--vt-06-mut);
}

@media (max-width: 640px) {
  .vt-06 .d-flex {
    flex-direction: column;
  }

  .vt-06 .nav {
    flex-direction: row;
    inline-size: 100%;
    overflow: auto;
  }

  .vt-06 .me-3 {
    margin: 0 0 1rem;
  }

  .vt-06 .tab-content {
    border-left: 0;
    border-top: 1px solid var(--vt-06-line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-06 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const list = document.getElementById('vt-06-tablist');
  if (!list || list.dataset.vtWired) return;
  list.dataset.vtWired = '1';
  const tabs = [...list.querySelectorAll('[data-bs-toggle="pill"]')];
  const show = (tab) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.classList.toggle('active', on);
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      const pane = document.querySelector(t.dataset.bsTarget);
      if (!pane) return;
      pane.classList.toggle('active', on);
      requestAnimationFrame(() => pane.classList.toggle('show', on));
    });
  };
  list.addEventListener('click', (e) => {
    const tab = e.target.closest('[data-bs-toggle="pill"]');
    if (tab) show(tab);
  });
  list.addEventListener('keydown', (e) => {
    const step = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
    if (!step) return;
    e.preventDefault();
    const next = tabs[(tabs.indexOf(document.activeElement) + step + tabs.length) % tabs.length];
    next.focus(); show(next);
  });
})();
```

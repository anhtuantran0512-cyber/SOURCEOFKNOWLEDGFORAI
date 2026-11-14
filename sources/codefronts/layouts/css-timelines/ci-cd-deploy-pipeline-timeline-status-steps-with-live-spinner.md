---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/ci-cd-deploy-pipeline-timeline-status-steps-with-live-spinner/"
title: "CI/CD Deploy Pipeline Timeline — Status Steps with Live Spinner"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A deployment pipeline strip in the dashboard idiom: Build → Test → Deploy steps joined by connector lines that fill with state, a conic-gradient spinner on…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CI/CD Deploy Pipeline Timeline — Status Steps with Live Spinner
Source: https://codefronts.com/layouts/css-timelines/ci-cd-deploy-pipeline-timeline-status-steps-with-live-spinner/

A deployment pipeline strip in the dashboard idiom: Build → Test → Deploy steps joined by connector lines that fill with state, a conic-gradient spinner on the running step, and success/pending/failed expressed with icons AND text — never color alone — so the pipeline reads correctly for color-blind engineers and screen readers alike.
## HTML
```html
<section class="tls-02" aria-label="Deploy pipeline timeline demo">
  <div class="tls-02__card">
    <header class="tls-02__head">
      <p class="tls-02__title">Deploy <code class="tls-02__sha">a1f9c02</code> → production</p>
      <time class="tls-02__time" datetime="2026-07-18T15:04">Started 15:04 UTC</time>
    </header>
    <ol class="tls-02__pipe" role="list">
      <li class="tls-02__step" data-state="done">
        <span class="tls-02__dot" aria-hidden="true"></span>
        <span class="tls-02__label">Build<span class="tls-02__sr"> — completed</span></span>
        <span class="tls-02__dur">42s</span>
      </li>
      <li class="tls-02__step" data-state="done">
        <span class="tls-02__dot" aria-hidden="true"></span>
        <span class="tls-02__label">Test<span class="tls-02__sr"> — completed</span></span>
        <span class="tls-02__dur">2m 18s</span>
      </li>
      <li class="tls-02__step" data-state="running" aria-current="step">
        <span class="tls-02__dot" aria-hidden="true"></span>
        <span class="tls-02__label">Deploy<span class="tls-02__sr"> — in progress</span></span>
        <span class="tls-02__dur">running…</span>
      </li>
      <li class="tls-02__step" data-state="queued">
        <span class="tls-02__dot" aria-hidden="true"></span>
        <span class="tls-02__label">Verify<span class="tls-02__sr"> — queued</span></span>
        <span class="tls-02__dur">—</span>
      </li>
    </ol>
    <p class="tls-02__foot">Preview: <a class="tls-02__url" href="#preview">feat-cq-layout.example.app</a></p>
  </div>
</section>
```
## CSS
```css
.tls-02,
.tls-02 *,
.tls-02 *::before,
.tls-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-02 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #6366f1;
  --tl-ok: #10b981;
  --tl-fail: #ef4444;
  --tl-line: #27272a;
  --tl-ink: #fafafa;
  --tl-mut: #a1a1aa;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #09090b;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-02__card {
  width: min(680px,100%);
  container-type: inline-size;
  background: #111113;
  border: 1px solid var(--tl-line);
  border-radius: 14px;
  padding: 22px 26px;
}

.tls-02__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.tls-02__title {
  font-size: 14px;
  font-weight: 600;
  color: var(--tl-ink);
}

.tls-02__sha {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: var(--tl-accent);
  background: #1c1c1f;
  border-radius: 5px;
  padding: 2px 7px;
}

.tls-02__time {
  font-size: 12px;
  color: var(--tl-mut);
}

.tls-02__pipe {
  list-style: none;
  display: flex;
  align-items: flex-start;
}

.tls-02__step {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  position: relative;
  text-align: center;
}

.tls-02__step::before {
  content: '';
  position: absolute;
  top: 11px;
  right: calc(50% + 18px);
  left: calc(-50% + 18px);
  height: 2px;
  background: var(--tl-line);
  border-radius: 1px;
}

.tls-02__step:first-child::before {
  display: none;
}

.tls-02__step[data-state="done"]::before {
  background: var(--tl-ok);
}

.tls-02__step[data-state="running"]::before {
  background: linear-gradient(90deg,var(--tl-ok),var(--tl-accent));
}

.tls-02__dot {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  position: relative;
  background: #1c1c1f;
  border: 2px solid var(--tl-line);
}

.tls-02__step[data-state="done"] .tls-02__dot {
  background: var(--tl-ok);
  border-color: var(--tl-ok);
}

.tls-02__step[data-state="done"] .tls-02__dot::after {
  content: '';
  position: absolute;
  left: 7px;
  top: 4px;
  width: 5px;
  height: 9px;
  border-right: 2.5px solid #09090b;
  border-bottom: 2.5px solid #09090b;
  rotate: 45deg;
}

.tls-02__step[data-state="running"] .tls-02__dot {
  border-color: transparent;
}

.tls-02__step[data-state="running"] .tls-02__dot::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 50%;
  background: conic-gradient(var(--tl-accent) 0 28%,#27272a 28% 100%);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(100% - 3px),#000 calc(100% - 2.5px));
  mask: radial-gradient(farthest-side,transparent calc(100% - 3px),#000 calc(100% - 2.5px));
  animation: tls-02-spin .9s linear infinite;
}

@keyframes tls-02-spin {
  to {
    transform: rotate(1turn);
  }
}

.tls-02__step[data-state="failed"] .tls-02__dot {
  background: var(--tl-fail);
  border-color: var(--tl-fail);
}

.tls-02__label {
  font-size: 13px;
  font-weight: 600;
  color: var(--tl-mut);
}

.tls-02__step[data-state="done"] .tls-02__label,
.tls-02__step[data-state="running"] .tls-02__label {
  color: var(--tl-ink);
}

.tls-02__dur {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  color: var(--tl-mut);
}

.tls-02__step[data-state="running"] .tls-02__dur {
  color: var(--tl-accent);
}

.tls-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.tls-02__foot {
  margin-top: 22px;
  padding-top: 16px;
  border-top: 1px solid var(--tl-line);
  font-size: 12.5px;
  color: var(--tl-mut);
}

.tls-02__url {
  color: var(--tl-accent);
  text-decoration: none;
}

.tls-02__url:hover {
  text-decoration: underline;
}

@container (max-width: 480px) {
  .tls-02__pipe {
    flex-direction: column;
    align-items: stretch;
    gap: 18px;
  }

  .tls-02__step {
    flex-direction: row;
    text-align: left;
    gap: 12px;
  }

  .tls-02__step::before {
    top: calc(-18px);
    left: 11px;
    right: auto;
    bottom: calc(100% + -6px);
    width: 2px;
    height: 18px;
  }

  .tls-02__dur {
    margin-left: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tls-02__step[data-state="running"] .tls-02__dot::before {
    animation: none;
    background: conic-gradient(var(--tl-accent) 0 100%);
  }
}
```

## JavaScript
```js
/* No JavaScript — state is a data-state attribute per step; the spinner is a conic-gradient ring masked with radial-gradient and rotated with transform. */
```

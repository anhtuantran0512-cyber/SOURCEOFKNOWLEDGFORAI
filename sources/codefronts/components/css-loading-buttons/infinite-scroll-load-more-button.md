---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/infinite-scroll-load-more-button/"
title: "Infinite Scroll Load More Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "A secondary outline button below a short list, with a dots pulse for the pending state, a retry path when the page fails to load, and an end-of-results state…"
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Infinite Scroll Load More Button
Source: https://codefronts.com/components/css-loading-buttons/infinite-scroll-load-more-button/

A secondary outline button below a short list, with a dots pulse for the pending state, a retry path when the page fails to load, and an end-of-results state that replaces the control entirely rather than leaving a dead button on the page. The list itself stays deliberately plain — the button is the subject.
## HTML
```html
<div class="lb-14">
  <div class="lb-14__stage">
    <section class="lb-14__wrap" aria-labelledby="lb-14-h">
      <h2 class="lb-14__h" id="lb-14-h">Comments</h2>

      <ul class="lb-14__list" id="lb-14-list">
        <li class="lb-14__item"><span class="lb-14__who">Priya Sharma</span><span class="lb-14__text">The rollback plan needs a dry run before Thursday.</span></li>
        <li class="lb-14__item"><span class="lb-14__who">Jordan Lee</span><span class="lb-14__text">Agreed. I can take the staging pass tomorrow morning.</span></li>
        <li class="lb-14__item"><span class="lb-14__who">Sam Rivera</span><span class="lb-14__text">Added the shard checklist to the runbook.</span></li>
      </ul>

      <div class="lb-14__foot" id="lb-14-foot">
        <button class="lb-14__more" type="button" id="lb-14-btn" data-state="idle" aria-busy="false">
          <span class="lb-14__faces">
            <span class="lb-14__face lb-14__face--idle">Load more comments</span>
            <span class="lb-14__face lb-14__face--pending">Loading<span class="lb-14__dots" aria-hidden="true"><i></i><i></i><i></i></span></span>
            <span class="lb-14__face lb-14__face--error">Retry loading</span>
          </span>
        </button>
        <p class="lb-14__count" id="lb-14-count">3 of 11 shown</p>
      </div>

      <p class="lb-14__live" id="lb-14-live" role="status" aria-live="polite"></p>
      <p class="lb-14__alert" id="lb-14-alert" role="alert"></p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-14 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #0f1c2e;
  --surface: #142438;
  --ink: #e7eef7;
  --muted: #8ba3bf;
  --rule: #22364e;
  --accent: #7fb2ff;
  --bad: #e97f6b;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-14 *,
.lb-14 *::before,
.lb-14 *::after {
  box-sizing: border-box;
}

.lb-14__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-14__wrap {
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
}

.lb-14__h {
  margin: 0 0 14px;
  font-size: 12px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 620;
}

.lb-14__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
  background: var(--rule);
  border: 1px solid var(--rule);
  border-radius: 8px;
  overflow: hidden;
}

.lb-14__item {
  background: var(--surface);
  padding: 13px 15px;
  display: grid;
  gap: 4px;
  min-inline-size: 0;
}

.lb-14__who {
  font-size: 12px;
  font-weight: 640;
  color: var(--accent);
  min-inline-size: 0;
}

.lb-14__text {
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--ink);
  min-inline-size: 0;
}

.lb-14__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  justify-content: space-between;
  margin: 16px 0 0;
  min-inline-size: 0;
}

.lb-14__more {
  appearance: none;
  border: 1px solid var(--accent);
  background: transparent;
  color: var(--accent);
  border-radius: 999px;
  font: inherit;
  font-size: 13px;
  font-weight: 600;
  padding: 0 20px;
  min-block-size: 44px;
  min-inline-size: 0;
  cursor: pointer;
  transition: background 160ms ease, color 160ms ease;
}

.lb-14__more:hover {
  background: rgba(127, 178, 255, .12);
}

.lb-14__more:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.lb-14__more[data-state="pending"] {
  cursor: progress;
}

.lb-14__more[data-state="error"] {
  border-color: var(--bad);
  color: var(--bad);
}

.lb-14__faces {
  display: grid;
  place-items: center;
}

.lb-14__face {
  grid-area: 1 / 1;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  white-space: nowrap;
  visibility: hidden;
}

.lb-14__more[data-state="idle"] .lb-14__face--idle,
.lb-14__more[data-state="pending"] .lb-14__face--pending,
.lb-14__more[data-state="error"] .lb-14__face--error {
  visibility: visible;
}

.lb-14__dots {
  display: inline-flex;
  gap: 3px;
}

.lb-14__dots i {
  inline-size: 4px;
  block-size: 4px;
  border-radius: 50%;
  background: currentColor;
  animation: lb-14-pulse 850ms ease-in-out infinite;
}

.lb-14__dots i:nth-child(2) {
  animation-delay: 140ms;
}

.lb-14__dots i:nth-child(3) {
  animation-delay: 280ms;
}

@keyframes lb-14-pulse {
  0%,
    100% {
    opacity: .3;
    transform: scale(.8);
  }

  50% {
    opacity: 1;
    transform: scale(1);
  }
}

.lb-14__count {
  margin: 0;
  font-size: 11.5px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  min-inline-size: 0;
}

.lb-14__end {
  margin: 0;
  font-size: 12.5px;
  color: var(--muted);
  border-block-start: 1px solid var(--rule);
  padding-block-start: 14px;
  inline-size: 100%;
}

.lb-14__live {
  margin: 12px 0 0;
  min-block-size: 17px;
  font-size: 12px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-14__alert {
  margin: 2px 0 0;
  min-block-size: 17px;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--bad);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-14__dots i {
    animation: none;
    opacity: .85;
  }

  .lb-14__more {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .lb-14 {
    --bg: #eef3fa;
    --surface: #ffffff;
    --ink: #12253a;
    --muted: #5a748f;
    --rule: #d7e2ef;
    --accent: #1f5fbf;
    --bad: #b4432c;
  }
}

[data-theme="light"] .lb-14 {
  --bg: #eef3fa;
  --surface: #ffffff;
  --ink: #12253a;
  --muted: #5a748f;
  --rule: #d7e2ef;
  --accent: #1f5fbf;
  --bad: #b4432c;
}
```

## JavaScript
```js
const btn = document.getElementById('lb-14-btn');
const list = document.getElementById('lb-14-list');
const count = document.getElementById('lb-14-count');
const foot = document.getElementById('lb-14-foot');
const live = document.getElementById('lb-14-live');
const alertBox = document.getElementById('lb-14-alert');
const pages = [
  [['Alex Chen', 'Dry run is booked for 09:00 with the on-call pair.'], ['Priya Sharma', 'Shard 4 was the one that stalled last time.'], ['Jordan Lee', 'I will keep the old writer warm for an hour after cutover.'], ['Sam Rivera', 'Runbook step 7 needs the new metric name.']],
  [['Alex Chen', 'Metric renamed. Dashboards updated.'], ['Jordan Lee', 'Rollback rehearsal passed on the second attempt.'], ['Priya Sharma', 'Sign-off from support is in the ticket.'], ['Sam Rivera', 'Closing this out — thanks all.']]
];
let page = 0;
let attempted = false;
let timer;

btn.addEventListener('click', () => {
  if (btn.dataset.state === 'pending') return;
  clearTimeout(timer);
  btn.dataset.state = 'pending';
  btn.setAttribute('aria-busy', 'true');
  alertBox.textContent = '';
  timer = setTimeout(() => {
    btn.setAttribute('aria-busy', 'false');
    if (page === 1 && !attempted) {
      attempted = true;
      btn.dataset.state = 'error';
      alertBox.textContent = 'That page failed to load. The comments already shown are untouched.';
      return;
    }
    pages[page].forEach(([who, text]) => {
      const li = document.createElement('li');
      li.className = 'lb-14__item';
      li.innerHTML = '<span class="lb-14__who"></span><span class="lb-14__text"></span>';
      li.firstChild.textContent = who;
      li.lastChild.textContent = text;
      list.append(li);
    });
    const shown = list.children.length;
    live.textContent = pages[page].length + ' more comments loaded, ' + shown + ' of 11 shown';
    page += 1;
    if (page >= pages.length) {
      foot.innerHTML = '<p class="lb-14__end">That is all 11 comments.</p>';
    } else {
      btn.dataset.state = 'idle';
      count.textContent = shown + ' of 11 shown';
    }
  }, 1200);
});
```

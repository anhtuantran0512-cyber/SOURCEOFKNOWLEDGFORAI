---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-rate-limit-button-retry-after-countdown/"
title: "Tailwind Rate Limit Button with Retry-After Countdown"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "What a 429 Too Many Requests should look like in a UI: the button enters a cooldown derived from the Retry-After header and an amber fill drains across its…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Rate Limit Button with Retry-After Countdown
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-rate-limit-button-retry-after-countdown/

What a 429 Too Many Requests should look like in a UI: the button enters a cooldown derived from the Retry-After header and an amber fill drains across its label as the seconds tick away, with the response headers beside it so the number is traceable. New: a five-pip quota meter, a scrolling request log and a status-coloured header table, all from data-* variants.
## HTML
```html
<section class="tcd-06 w-full min-h-svh grid place-items-center bg-tcd06-page bg-[radial-gradient(50%_40%_at_50%_30%,var(--color-tcd06-glow),transparent_70%)] px-3 py-12 font-tcd06-mono text-tcd06-ink" aria-labelledby="tcd-06-title">
  <div class="w-full max-w-[640px] overflow-hidden rounded-xl border border-tcd06-rule bg-tcd06-panel shadow-[0_40px_80px_-40px_rgb(0_0_0/0.9)]">
    <header class="flex min-w-0 items-center gap-2.5 border-b border-tcd06-rule px-4 py-3">
      <span aria-hidden="true" class="flex gap-1.5"><span class="size-2.5 rounded-full bg-tcd06-rule"></span><span class="size-2.5 rounded-full bg-tcd06-rule"></span><span class="size-2.5 rounded-full bg-tcd06-rule"></span></span>
      <h2 id="tcd-06-title" class="ml-1 min-w-0 flex-1 text-[12.5px] font-medium tracking-[-0.01em] [overflow-wrap:anywhere]"><span class="text-tcd06-acc">POST</span> /v2/exports</h2>
      <span class="flex-none text-[10.5px] text-tcd06-mut">talon-api · staging</span>
    </header>

    <div class="flex flex-wrap items-center gap-3 border-b border-tcd06-rule p-4">
      <button type="button" data-go class="min-h-11 min-w-[168px] cursor-pointer rounded-md border border-tcd06-rule bg-[linear-gradient(var(--color-tcd06-acc-a),var(--color-tcd06-acc-a))] bg-[length:var(--fill,0%)_100%] bg-no-repeat px-4 text-[12.5px] font-semibold tabular-nums transition-[background-size,border-color,color] duration-1000 ease-linear enabled:hover:border-tcd06-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd06-acc disabled:cursor-not-allowed disabled:border-tcd06-acc/45 disabled:text-tcd06-acc motion-reduce:transition-none"><span data-label>Run request</span></button>
      <div class="grid min-w-0 flex-[1_1_180px] gap-1.5">
        <p role="timer" data-state class="text-[11.5px] text-tcd06-mut data-limited:text-tcd06-acc">Ready · 5 requests per minute</p>
        <div aria-hidden="true" data-pips class="flex gap-1">
          <span class="h-1.5 flex-1 rounded-full bg-tcd06-ok transition-colors data-off:bg-tcd06-rule"></span>
          <span class="h-1.5 flex-1 rounded-full bg-tcd06-ok transition-colors data-off:bg-tcd06-rule"></span>
          <span class="h-1.5 flex-1 rounded-full bg-tcd06-ok transition-colors data-off:bg-tcd06-rule"></span>
          <span class="h-1.5 flex-1 rounded-full bg-tcd06-ok transition-colors data-off:bg-tcd06-rule"></span>
          <span class="h-1.5 flex-1 rounded-full bg-tcd06-ok transition-colors data-off:bg-tcd06-rule"></span>
        </div>
      </div>
    </div>

    <dl class="grid grid-cols-1 border-b border-tcd06-rule sm:grid-cols-2">
      <div class="flex justify-between gap-3 border-b border-tcd06-rule px-4 py-2.5 text-[11.5px] sm:border-r"><dt class="text-tcd06-mut">status</dt><dd data-status class="font-semibold data-[status=202]:text-tcd06-ok data-[status=429]:text-tcd06-danger">—</dd></div>
      <div class="flex justify-between gap-3 border-b border-tcd06-rule px-4 py-2.5 text-[11.5px]"><dt class="text-tcd06-mut">retry-after</dt><dd class="font-semibold"><time datetime="" data-retry>—</time></dd></div>
      <div class="flex justify-between gap-3 border-b border-tcd06-rule px-4 py-2.5 text-[11.5px] sm:border-r sm:border-b-0"><dt class="text-tcd06-mut">x-ratelimit-remaining</dt><dd data-left class="font-semibold">5</dd></div>
      <div class="flex justify-between gap-3 px-4 py-2.5 text-[11.5px]"><dt class="text-tcd06-mut">x-ratelimit-reset</dt><dd data-reset class="font-semibold">—</dd></div>
    </dl>

    <ol data-log aria-label="Request log" class="grid max-h-40 gap-1 overflow-auto bg-tcd06-page/60 px-4 py-3 text-[11.5px] leading-relaxed text-tcd06-mut">
      <li>$ waiting for first run</li>
    </ol>
    <output data-live aria-live="polite" class="sr-only"></output>
    <p class="border-t border-tcd06-rule px-4 py-3 text-[10.5px] leading-relaxed text-tcd06-mut text-pretty">Retry-After may arrive as delta-seconds or an HTTP-date. Both are parsed; a missing header falls back to a fixed 15s wait.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd06-page: #000000;
  --color-tcd06-page: oklch(0 0 0);
  --color-tcd06-glow: #14110a;
  --color-tcd06-glow: oklch(0.2 0.03 78);
  --color-tcd06-panel: #0c0c0e;
  --color-tcd06-panel: oklch(0.16 0.004 280);
  --color-tcd06-ink: #f4f4f5;
  --color-tcd06-ink: oklch(0.96 0.003 280);
  --color-tcd06-mut: #9a9aa3;
  --color-tcd06-mut: oklch(0.7 0.01 280);
  --color-tcd06-rule: #232328;
  --color-tcd06-rule: oklch(0.27 0.006 280);
  --color-tcd06-acc: #ffb224;
  --color-tcd06-acc: oklch(0.81 0.16 78);
  --color-tcd06-acc-a: rgb(255 178 36 / 0.22);
  --color-tcd06-danger: #ff5c5c;
  --color-tcd06-danger: oklch(0.69 0.19 25);
  --color-tcd06-ok: #4ade80;
  --color-tcd06-ok: oklch(0.82 0.17 148);
  --font-tcd06-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tcd-06 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-06');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const go = q('[data-go]'), label = q('[data-label]'), state = q('[data-state]'), log = q('[data-log]');
  const live = q('[data-live]'), pips = [...q('[data-pips]').children], status = q('[data-status]');
  const LIMIT = 5, FALLBACK = 15;
  let left = LIMIT, id = 0, total = 0, target = 0;
  const stamp = () => new Date().toLocaleTimeString([], { hour12: false });
  const line = (t, cls) => { const li = document.createElement('li'); li.textContent = stamp() + '  ' + t; if (cls) li.className = cls; log.prepend(li); };
  const paint = () => { q('[data-left]').textContent = left; pips.forEach((p, i) => p.toggleAttribute('data-off', i >= left)); };
  const parseRetry = (v) => Number.isFinite(+v) ? +v : Number.isFinite(Date.parse(v)) ? Math.ceil((Date.parse(v) - Date.now()) / 1000) : FALLBACK;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    label.textContent = 'Retry in ' + s + 's';
    go.style.setProperty('--fill', (ms / total * 100).toFixed(1) + '%');
    if (ms > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); return; }
    go.disabled = false; label.textContent = 'Run request'; left = LIMIT; paint();
    state.removeAttribute('data-limited'); state.textContent = 'Ready · window reset';
    line('window reset · ' + LIMIT + ' requests available', 'text-tcd06-ok');
    live.textContent = 'Rate limit window reset. You can run the request again.';
  };
  go.addEventListener('click', () => {
    if (go.disabled) return;
    if (left > 0) {
      left -= 1; paint(); status.textContent = '202'; status.dataset.status = '202';
      line('202 accepted · export queued · ' + left + ' left in window');
      return;
    }
    const header = '9';
    const secs = parseRetry(header); total = secs * 1000; target = Date.now() + total;
    status.textContent = '429'; status.dataset.status = '429';
    q('[data-retry]').textContent = header; q('[data-retry]').dateTime = 'PT' + secs + 'S';
    q('[data-reset]').textContent = new Date(target).toLocaleTimeString([], { hour12: false });
    state.setAttribute('data-limited', ''); state.textContent = 'Too Many Requests · cooling down';
    line('429 too many requests · retry-after: ' + header + ' → cooldown ' + secs + 's', 'text-tcd06-danger');
    go.disabled = true; go.style.setProperty('--fill', '100%');
    live.textContent = 'Rate limited. Retry available in ' + secs + ' seconds.';
    clearTimeout(id); requestAnimationFrame(tick);
  });
  root.cleanup = () => clearTimeout(id);
})();
```

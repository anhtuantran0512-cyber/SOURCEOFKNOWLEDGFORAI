---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-webhooks-settings-page/"
title: "Tailwind Webhooks Settings Page"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A complete webhook manager: an endpoint list with health dots, success rates and 24-hour delivery sparklines, a detail pane with the URL, an enable switch…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Webhooks Settings Page
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-webhooks-settings-page/

A complete webhook manager: an endpoint list with health dots, success rates and 24-hour delivery sparklines, a detail pane with the URL, an enable switch that marks the endpoint Paused, toggleable event chips, a signing secret you can reveal, copy and roll, a 'Send test event' that lands in the delivery log live, and expandable deliveries showing request and response.
## HTML
```html
<section data-tsp17 class="tsp-17 group/wh w-full min-h-svh bg-tsp17-bg px-4 py-10 font-tsp17-sans text-tsp17-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-17-h">
  <div class="mx-auto grid w-full max-w-6xl gap-6">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div><h1 id="tsp-17-h" class="text-3xl font-bold tracking-tight">Webhooks</h1><p class="mt-1 text-tsp17-mut">Get an HTTPS POST the moment something happens in Northwind.</p></div>
      <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp17-ink px-4 text-sm font-semibold text-white transition hover:bg-tsp17-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp17-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 5v14M5 12h14"/></svg>Add endpoint</button>
    </header>
    <div class="grid gap-6 lg:grid-cols-[21rem_minmax(0,1fr)]">
      <fieldset class="grid content-start gap-2">
        <legend class="sr-only">Endpoints</legend>
        <label data-ep data-url="https://api.northwind.co/hooks/billing" data-rate="99.8%" data-health="ok" class="group/ep grid cursor-pointer gap-3 rounded-2xl border border-transparent p-4 transition hover:bg-white/70 has-checked:border-tsp17-line has-checked:bg-white has-checked:shadow-[0_8px_24px_-16px_rgb(20_20_60/0.35)] has-focus-visible:outline-2 has-focus-visible:outline-tsp17-acc"><input type="radio" name="tsp-17-ep" class="sr-only" checked><span class="flex items-center gap-2"><span class="size-2 flex-none rounded-full bg-emerald-500"></span><span class="truncate font-tsp17-mono text-[13px] font-medium">api.northwind.co/hooks/billing</span></span><span class="flex items-end justify-between gap-3"><span class="text-xs text-tsp17-mut">4 events · <strong class="font-semibold text-emerald-700">99.8%</strong></span><span class="flex h-6 items-end gap-px" aria-hidden="true"><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-[70%] w-1 rounded-sm bg-rose-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i></span></span></label>
        <label data-ep data-url="https://hooks.zapier.com/hooks/catch/48213/bq7" data-rate="92.1%" data-health="warn" class="group/ep grid cursor-pointer gap-3 rounded-2xl border border-transparent p-4 transition hover:bg-white/70 has-checked:border-tsp17-line has-checked:bg-white has-checked:shadow-[0_8px_24px_-16px_rgb(20_20_60/0.35)] has-focus-visible:outline-2 has-focus-visible:outline-tsp17-acc"><input type="radio" name="tsp-17-ep" class="sr-only"><span class="flex items-center gap-2"><span class="size-2 flex-none rounded-full bg-amber-500"></span><span class="truncate font-tsp17-mono text-[13px] font-medium">hooks.zapier.com/hooks/catch/48213</span></span><span class="flex items-end justify-between gap-3"><span class="text-xs text-tsp17-mut">2 events · <strong class="font-semibold text-amber-700">92.1%</strong></span><span class="flex h-6 items-end gap-px" aria-hidden="true"><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-[60%] w-1 rounded-sm bg-rose-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-[60%] w-1 rounded-sm bg-rose-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-[60%] w-1 rounded-sm bg-rose-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i><i class="h-full w-1 rounded-sm bg-emerald-400"></i></span></span></label>
        <label data-ep data-url="https://legacy.internal.northwind.co/notify" data-rate="0%" data-health="fail" class="group/ep grid cursor-pointer gap-3 rounded-2xl border border-transparent p-4 transition hover:bg-white/70 has-checked:border-tsp17-line has-checked:bg-white has-checked:shadow-[0_8px_24px_-16px_rgb(20_20_60/0.35)] has-focus-visible:outline-2 has-focus-visible:outline-tsp17-acc"><input type="radio" name="tsp-17-ep" class="sr-only"><span class="flex items-center gap-2"><span class="size-2 flex-none rounded-full bg-rose-500"></span><span class="truncate font-tsp17-mono text-[13px] font-medium">legacy.internal.northwind.co/notify</span></span><span class="flex items-end justify-between gap-3"><span class="text-xs text-tsp17-mut">Auto-paused · <strong class="font-semibold text-rose-700">0%</strong></span><span class="flex h-6 items-end gap-px" aria-hidden="true"><i class="h-[60%] w-1 rounded-sm bg-rose-400"></i><i class="h-[60%] w-1 rounded-sm bg-rose-400"></i><i class="h-[60%] w-1 rounded-sm bg-rose-400"></i><i class="h-[60%] w-1 rounded-sm bg-rose-400"></i><i class="h-[60%] w-1 rounded-sm bg-rose-400"></i><i class="h-[60%] w-1 rounded-sm bg-rose-400"></i><i class="h-1 w-1 rounded-sm bg-tsp17-line"></i><i class="h-1 w-1 rounded-sm bg-tsp17-line"></i><i class="h-1 w-1 rounded-sm bg-tsp17-line"></i><i class="h-1 w-1 rounded-sm bg-tsp17-line"></i><i class="h-1 w-1 rounded-sm bg-tsp17-line"></i><i class="h-1 w-1 rounded-sm bg-tsp17-line"></i></span></span></label>
      </fieldset>

      <div class="grid min-w-0 content-start gap-6 rounded-3xl border border-tsp17-line bg-white p-5 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-7">
        <div class="flex flex-wrap items-start justify-between gap-4">
          <div class="grid min-w-0 gap-2">
            <p class="flex flex-wrap items-center gap-2 text-sm"><span data-health-badge class="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-semibold text-emerald-700 data-[health=warn]:bg-amber-50 data-[health=warn]:text-amber-800 data-[health=fail]:bg-rose-50 data-[health=fail]:text-rose-700" data-health="ok"><span class="size-1.5 rounded-full bg-current"></span><span data-health-text>Healthy</span></span><span class="text-tsp17-mut">Success rate <strong data-rate class="font-semibold text-tsp17-ink">99.8%</strong> · last 24h</span><span class="hidden items-center rounded-full bg-zinc-900 px-2.5 py-1 text-xs font-semibold text-white group-has-[#tsp-17-on:not(:checked)]/wh:inline-flex">Paused</span></p>
            <div class="flex min-w-0 items-center gap-2"><code data-url class="truncate rounded-lg bg-tsp17-bg px-3 py-2 font-tsp17-mono text-sm">https://api.northwind.co/hooks/billing</code><button type="button" data-copy-url class="group/cp grid size-11 flex-none place-items-center rounded-xl text-tsp17-mut transition hover:bg-tsp17-bg hover:text-tsp17-ink focus-visible:outline-2 focus-visible:outline-tsp17-acc data-copied:text-emerald-600" aria-label="Copy endpoint URL"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 group-data-copied/cp:hidden"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="hidden size-4 group-data-copied/cp:block"><path d="M20 6 9 17l-5-5"/></svg></button></div>
          </div>
          <label class="flex min-h-11 cursor-pointer items-center gap-3 text-sm font-semibold">Enabled<span class="relative"><input id="tsp-17-on" type="checkbox" role="switch" checked class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-zinc-300 transition peer-checked:bg-tsp17-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp17-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5"></span></span></label>
        </div>

        <fieldset class="grid gap-3 transition group-has-[#tsp-17-on:not(:checked)]/wh:opacity-50">
          <legend class="mb-3 text-sm font-bold">Events</legend>
          <div data-events class="flex flex-wrap gap-2">
            <label class="inline-flex min-h-10 cursor-pointer items-center gap-2 rounded-full border border-tsp17-line px-3.5 font-tsp17-mono text-[13px] text-tsp17-mut transition has-checked:border-tsp17-acc/40 has-checked:bg-tsp17-acc/8 has-checked:text-tsp17-acc has-focus-visible:outline-2 has-focus-visible:outline-tsp17-acc"><input type="checkbox" value="invoice.paid" checked class="sr-only">invoice.paid</label>
            <label class="inline-flex min-h-10 cursor-pointer items-center gap-2 rounded-full border border-tsp17-line px-3.5 font-tsp17-mono text-[13px] text-tsp17-mut transition has-checked:border-tsp17-acc/40 has-checked:bg-tsp17-acc/8 has-checked:text-tsp17-acc has-focus-visible:outline-2 has-focus-visible:outline-tsp17-acc"><input type="checkbox" value="invoice.failed" checked class="sr-only">invoice.failed</label>
            <label class="inline-flex min-h-10 cursor-pointer items-center gap-2 rounded-full border border-tsp17-line px-3.5 font-tsp17-mono text-[13px] text-tsp17-mut transition has-checked:border-tsp17-acc/40 has-checked:bg-tsp17-acc/8 has-checked:text-tsp17-acc has-focus-visible:outline-2 has-focus-visible:outline-tsp17-acc"><input type="checkbox" value="subscription.updated" checked class="sr-only">subscription.updated</label>
            <label class="inline-flex min-h-10 cursor-pointer items-center gap-2 rounded-full border border-tsp17-line px-3.5 font-tsp17-mono text-[13px] text-tsp17-mut transition has-checked:border-tsp17-acc/40 has-checked:bg-tsp17-acc/8 has-checked:text-tsp17-acc has-focus-visible:outline-2 has-focus-visible:outline-tsp17-acc"><input type="checkbox" value="member.added" checked class="sr-only">member.added</label>
            <label class="inline-flex min-h-10 cursor-pointer items-center gap-2 rounded-full border border-tsp17-line px-3.5 font-tsp17-mono text-[13px] text-tsp17-mut transition has-checked:border-tsp17-acc/40 has-checked:bg-tsp17-acc/8 has-checked:text-tsp17-acc has-focus-visible:outline-2 has-focus-visible:outline-tsp17-acc"><input type="checkbox" value="member.removed" class="sr-only">member.removed</label>
            <label class="inline-flex min-h-10 cursor-pointer items-center gap-2 rounded-full border border-tsp17-line px-3.5 font-tsp17-mono text-[13px] text-tsp17-mut transition has-checked:border-tsp17-acc/40 has-checked:bg-tsp17-acc/8 has-checked:text-tsp17-acc has-focus-visible:outline-2 has-focus-visible:outline-tsp17-acc"><input type="checkbox" value="project.archived" class="sr-only">project.archived</label>
          </div>
        </fieldset>

        <div class="grid gap-2">
          <p class="text-sm font-bold">Signing secret</p>
          <div class="flex flex-wrap items-center gap-2"><code data-secret class="min-w-0 flex-1 truncate rounded-lg bg-tsp17-bg px-3 py-2.5 font-tsp17-mono text-sm">whsec_••••••••••••••••••••••••</code><button type="button" data-reveal aria-pressed="false" class="min-h-11 rounded-xl border border-tsp17-line px-3.5 text-sm font-semibold transition hover:bg-tsp17-bg focus-visible:outline-2 focus-visible:outline-tsp17-acc aria-pressed:bg-tsp17-ink aria-pressed:text-white">Reveal</button><button type="button" data-copy-secret class="min-h-11 rounded-xl border border-tsp17-line px-3.5 text-sm font-semibold transition hover:bg-tsp17-bg focus-visible:outline-2 focus-visible:outline-tsp17-acc data-copied:text-emerald-700">Copy</button><button type="button" data-roll class="min-h-11 rounded-xl border border-tsp17-line px-3.5 text-sm font-semibold transition hover:bg-tsp17-bg focus-visible:outline-2 focus-visible:outline-tsp17-acc">Roll</button></div>
          <p data-secret-note role="status" aria-live="polite" class="text-xs text-tsp17-mut">Verify the <code class="font-tsp17-mono">Northwind-Signature</code> header with this secret.</p>
        </div>

        <div class="grid gap-3">
          <div class="flex flex-wrap items-center justify-between gap-3"><p class="text-sm font-bold">Recent deliveries</p><div class="flex gap-2"><select data-test-event aria-label="Event to send" class="min-h-11 rounded-xl border border-tsp17-line bg-white px-3 font-tsp17-mono text-[13px] outline-none focus:ring-4 focus:ring-tsp17-acc/15"></select><button type="button" data-test class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp17-acc px-4 text-sm font-semibold text-white transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp17-acc disabled:opacity-40 group-has-[#tsp-17-on:not(:checked)]/wh:pointer-events-none group-has-[#tsp-17-on:not(:checked)]/wh:opacity-40">Send test</button></div></div>
          <ul data-log class="divide-y divide-tsp17-line overflow-hidden rounded-2xl border border-tsp17-line">
            <li data-delivery data-state="ok" class="group/d"><details class="group/dd"><summary class="grid min-h-11 cursor-pointer list-none grid-cols-[4.5rem_minmax(0,1fr)_auto] items-center gap-3 px-4 py-3 text-sm transition hover:bg-tsp17-bg/60 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsp17-acc [&::-webkit-details-marker]:hidden"><span data-code class="w-fit rounded-md bg-emerald-50 px-2 py-0.5 font-tsp17-mono text-xs font-semibold text-emerald-700 group-data-[state=pending]/d:bg-zinc-100 group-data-[state=pending]/d:text-zinc-500 group-data-[state=fail]/d:bg-rose-50 group-data-[state=fail]/d:text-rose-700">200</span><span class="truncate font-tsp17-mono text-[13px]"><span data-ev>invoice.paid</span> <span class="text-tsp17-mut">evt_3Qk…a91</span></span><span class="flex items-center gap-3 font-tsp17-mono text-xs text-tsp17-mut"><span data-dur>184 ms</span><span data-when>2m ago</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-open/dd:rotate-180"><path d="m6 9 6 6 6-6"/></svg></span></summary><div class="grid gap-2 px-4 pb-4 sm:grid-cols-2"><pre class="overflow-x-auto rounded-xl bg-tsp17-ink p-3 font-tsp17-mono text-[12px] leading-relaxed text-white/75"><span class="text-white/45">// request</span>
{ "type": "<span data-ev>invoice.paid</span>",
  "data": { "amount": 28800 } }</pre><pre class="overflow-x-auto rounded-xl bg-tsp17-ink p-3 font-tsp17-mono text-[12px] leading-relaxed text-white/75"><span class="text-white/45">// response</span>
HTTP/1.1 <span data-code>200</span> OK
{ "received": true }</pre></div></details></li>
            <li data-delivery data-state="fail" class="group/d"><details class="group/dd"><summary class="grid min-h-11 cursor-pointer list-none grid-cols-[4.5rem_minmax(0,1fr)_auto] items-center gap-3 px-4 py-3 text-sm transition hover:bg-tsp17-bg/60 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsp17-acc [&::-webkit-details-marker]:hidden"><span class="w-fit rounded-md bg-emerald-50 px-2 py-0.5 font-tsp17-mono text-xs font-semibold text-emerald-700 group-data-[state=pending]/d:bg-zinc-100 group-data-[state=pending]/d:text-zinc-500 group-data-[state=fail]/d:bg-rose-50 group-data-[state=fail]/d:text-rose-700">503</span><span class="truncate font-tsp17-mono text-[13px]">subscription.updated <span class="text-tsp17-mut">evt_3Qj…7c2 · retry 2 of 5</span></span><span class="flex items-center gap-3 font-tsp17-mono text-xs text-tsp17-mut"><span>10.0 s</span><span>1h ago</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-open/dd:rotate-180"><path d="m6 9 6 6 6-6"/></svg></span></summary><div class="grid gap-2 px-4 pb-4 sm:grid-cols-2"><pre class="overflow-x-auto rounded-xl bg-tsp17-ink p-3 font-tsp17-mono text-[12px] leading-relaxed text-white/75"><span class="text-white/45">// request</span>
{ "type": "subscription.updated",
  "data": { "seats": 12 } }</pre><pre class="overflow-x-auto rounded-xl bg-tsp17-ink p-3 font-tsp17-mono text-[12px] leading-relaxed text-rose-300"><span class="text-white/45">// response</span>
HTTP/1.1 503 Service Unavailable
timeout after 10 s · next retry in 8 min</pre></div></details></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp17-bg: #f4f4f8;
  --color-tsp17-bg: oklch(0.97 0.006 285);
  --color-tsp17-ink: #15142a;
  --color-tsp17-ink: oklch(0.215 0.035 285);
  --color-tsp17-mut: #5f5d78;
  --color-tsp17-mut: oklch(0.5 0.04 285);
  --color-tsp17-line: #e4e3ee;
  --color-tsp17-line: oklch(0.923 0.012 285);
  --color-tsp17-acc: #5b4ff0;
  --color-tsp17-acc: oklch(0.53 0.23 278);
  --font-tsp17-sans: 'Schibsted Grotesk', system-ui, sans-serif;
  --font-tsp17-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsp-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp17]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const $ = (s) => root.querySelector(s);
  const LABEL = { ok: 'Healthy', warn: 'Degraded', fail: 'Failing' };
  const copy = async (text, btn) => {
    try { await navigator.clipboard.writeText(text); } catch (e) {}
    btn.dataset.copied = ''; setTimeout(() => delete btn.dataset.copied, 1400);
  };
  root.querySelectorAll('[data-ep]').forEach((ep) => ep.querySelector('input').addEventListener('change', () => {
    $('[data-url]').textContent = ep.dataset.url;
    $('[data-rate]').textContent = ep.dataset.rate;
    $('[data-health-badge]').dataset.health = ep.dataset.health;
    $('[data-health-text]').textContent = LABEL[ep.dataset.health];
    $('#tsp-17-on').checked = ep.dataset.health !== 'fail';
  }));
  $('[data-copy-url]').addEventListener('click', (e) => copy($('[data-url]').textContent, e.currentTarget));
  const ALPHA = 'abcdefghijklmnopqrstuvwxyz0123456789';
  const gen = () => 'whsec_' + Array.from(crypto.getRandomValues(new Uint8Array(24)), (b) => ALPHA[b % ALPHA.length]).join('');
  let secret = gen();
  const mask = 'whsec_••••••••••••••••••••••••';
  const reveal = $('[data-reveal]');
  const paint = () => { const on = reveal.getAttribute('aria-pressed') === 'true'; $('[data-secret]').textContent = on ? secret : mask; reveal.textContent = on ? 'Hide' : 'Reveal'; };
  reveal.addEventListener('click', () => { reveal.setAttribute('aria-pressed', String(reveal.getAttribute('aria-pressed') !== 'true')); paint(); });
  $('[data-copy-secret]').addEventListener('click', (e) => copy(secret, e.currentTarget));
  $('[data-roll]').addEventListener('click', () => { secret = gen(); paint(); $('[data-secret-note]').textContent = 'New secret generated. The previous one keeps working for 24 hours.'; });
  const sel = $('[data-test-event]');
  const fill = () => {
    const keep = sel.value;
    sel.replaceChildren(...[...root.querySelectorAll('[data-events] input:checked')].map((c) => new Option(c.value, c.value)));
    if (keep) sel.value = keep;
  };
  $('[data-events]').addEventListener('change', fill); fill();
  $('[data-test]').addEventListener('click', () => {
    const log = $('[data-log]');
    const li = log.querySelector('[data-delivery]').cloneNode(true);
    li.dataset.state = 'pending';
    li.querySelector('details').open = false;
    li.querySelectorAll('[data-ev]').forEach((n) => { n.textContent = sel.value || 'ping'; });
    li.querySelectorAll('[data-code]').forEach((n) => { n.textContent = '···'; });
    li.querySelector('[data-dur]').textContent = '—';
    li.querySelector('[data-when]').textContent = 'now';
    log.prepend(li);
    const ms = 120 + Math.round(Math.random() * 180);
    setTimeout(() => {
      li.dataset.state = 'ok';
      li.querySelectorAll('[data-code]').forEach((n) => { n.textContent = '200'; });
      li.querySelector('[data-dur]').textContent = ms + ' ms';
    }, 900);
  });
})();
```

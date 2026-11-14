---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-data-export-request-page/"
title: "Tailwind Data Export Request Page"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A GDPR-ready 'download your data' page: selectable data cards with size estimates, Select all, JSON / CSV / ZIP format, a date range, a live size and time…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Data Export Request Page
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-data-export-request-page/

A GDPR-ready 'download your data' page: selectable data cards with size estimates, Select all, JSON / CSV / ZIP format, a date range, a live size and time estimate, then a three-stage Queued → Preparing → Ready tracker with a real progress bar and a download that produces an actual file — plus a history of past exports and a plain-language rights panel.
## HTML
```html
<section data-tsp15 data-state="idle" class="tsp-15 group/ex w-full min-h-svh bg-tsp15-bg px-4 py-10 font-tsp15-sans text-tsp15-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-15-h">
  <div class="mx-auto grid w-full max-w-6xl gap-8 lg:grid-cols-[minmax(0,1fr)_20rem]">
    <div class="grid min-w-0 content-start gap-6">
      <header><h1 id="tsp-15-h" class="text-3xl font-bold tracking-tight">Export your data</h1><p class="mt-1 text-pretty text-tsp15-mut">Get a copy of everything you've created in Northwind. We'll email you when it's ready.</p></header>

      <form data-form class="grid gap-6 rounded-3xl border border-tsp15-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)] group-data-[state=preparing]/ex:pointer-events-none group-data-[state=preparing]/ex:opacity-50 group-data-[state=queued]/ex:pointer-events-none group-data-[state=queued]/ex:opacity-50 sm:p-7">
        <fieldset class="grid gap-3">
          <legend class="sr-only">What to include</legend>
          <div class="flex items-center justify-between gap-3"><p class="font-bold" aria-hidden="true">What to include</p><label class="flex min-h-11 cursor-pointer items-center gap-2 text-sm font-semibold text-tsp15-acc"><input type="checkbox" data-all class="size-4 accent-tsp15-acc">Select all</label></div>
          <div class="grid gap-3 sm:grid-cols-2">
            <label class="group/c flex cursor-pointer items-start gap-3 rounded-2xl border border-tsp15-line p-4 transition hover:border-tsp15-acc/40 has-checked:border-tsp15-acc has-checked:bg-tsp15-acc/5 has-checked:ring-2 has-checked:ring-tsp15-acc/15 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp15-acc"><input type="checkbox" data-pick data-size="0.4" checked class="mt-0.5 size-4 accent-tsp15-acc"><span class="min-w-0 flex-1"><span class="flex justify-between gap-2 font-semibold">Profile &amp; settings<span class="text-xs font-medium tabular-nums text-tsp15-mut">0.4 MB</span></span><span class="block text-sm text-tsp15-mut">Account details, preferences, notification rules</span></span></label>
            <label class="group/c flex cursor-pointer items-start gap-3 rounded-2xl border border-tsp15-line p-4 transition hover:border-tsp15-acc/40 has-checked:border-tsp15-acc has-checked:bg-tsp15-acc/5 has-checked:ring-2 has-checked:ring-tsp15-acc/15 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp15-acc"><input type="checkbox" data-pick data-size="184" checked class="mt-0.5 size-4 accent-tsp15-acc"><span class="min-w-0 flex-1"><span class="flex justify-between gap-2 font-semibold">Projects &amp; docs<span class="text-xs font-medium tabular-nums text-tsp15-mut">184 MB</span></span><span class="block text-sm text-tsp15-mut">14 projects, 236 documents, version history</span></span></label>
            <label class="group/c flex cursor-pointer items-start gap-3 rounded-2xl border border-tsp15-line p-4 transition hover:border-tsp15-acc/40 has-checked:border-tsp15-acc has-checked:bg-tsp15-acc/5 has-checked:ring-2 has-checked:ring-tsp15-acc/15 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp15-acc"><input type="checkbox" data-pick data-size="12" class="mt-0.5 size-4 accent-tsp15-acc"><span class="min-w-0 flex-1"><span class="flex justify-between gap-2 font-semibold">Comments<span class="text-xs font-medium tabular-nums text-tsp15-mut">12 MB</span></span><span class="block text-sm text-tsp15-mut">Threads, reactions and mentions</span></span></label>
            <label class="group/c flex cursor-pointer items-start gap-3 rounded-2xl border border-tsp15-line p-4 transition hover:border-tsp15-acc/40 has-checked:border-tsp15-acc has-checked:bg-tsp15-acc/5 has-checked:ring-2 has-checked:ring-tsp15-acc/15 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp15-acc"><input type="checkbox" data-pick data-size="2300" class="mt-0.5 size-4 accent-tsp15-acc"><span class="min-w-0 flex-1"><span class="flex justify-between gap-2 font-semibold">Files &amp; uploads<span class="text-xs font-medium tabular-nums text-amber-700">2.3 GB</span></span><span class="block text-sm text-tsp15-mut">Original images, PDFs and attachments</span></span></label>
            <label class="group/c flex cursor-pointer items-start gap-3 rounded-2xl border border-tsp15-line p-4 transition hover:border-tsp15-acc/40 has-checked:border-tsp15-acc has-checked:bg-tsp15-acc/5 has-checked:ring-2 has-checked:ring-tsp15-acc/15 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp15-acc"><input type="checkbox" data-pick data-size="1.2" class="mt-0.5 size-4 accent-tsp15-acc"><span class="min-w-0 flex-1"><span class="flex justify-between gap-2 font-semibold">Billing history<span class="text-xs font-medium tabular-nums text-tsp15-mut">1.2 MB</span></span><span class="block text-sm text-tsp15-mut">Invoices, receipts and plan changes</span></span></label>
            <label class="group/c flex cursor-pointer items-start gap-3 rounded-2xl border border-tsp15-line p-4 transition hover:border-tsp15-acc/40 has-checked:border-tsp15-acc has-checked:bg-tsp15-acc/5 has-checked:ring-2 has-checked:ring-tsp15-acc/15 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp15-acc"><input type="checkbox" data-pick data-size="36" class="mt-0.5 size-4 accent-tsp15-acc"><span class="min-w-0 flex-1"><span class="flex justify-between gap-2 font-semibold">Activity log<span class="text-xs font-medium tabular-nums text-tsp15-mut">36 MB</span></span><span class="block text-sm text-tsp15-mut">Sign-ins and changes for the last 12 months</span></span></label>
          </div>
        </fieldset>
        <div class="grid gap-5 sm:grid-cols-2">
          <fieldset class="grid gap-2"><legend class="mb-2 font-bold">Format</legend>
            <div class="grid grid-cols-3 gap-1 rounded-xl bg-tsp15-bg p-1 ring-1 ring-tsp15-line">
              <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-sm font-semibold text-tsp15-mut transition has-checked:bg-white has-checked:text-tsp15-ink has-checked:shadow-sm has-focus-visible:outline-2 has-focus-visible:outline-tsp15-acc"><input type="radio" name="format" value="json" class="sr-only" checked>JSON</label>
              <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-sm font-semibold text-tsp15-mut transition has-checked:bg-white has-checked:text-tsp15-ink has-checked:shadow-sm has-focus-visible:outline-2 has-focus-visible:outline-tsp15-acc"><input type="radio" name="format" value="csv" class="sr-only">CSV</label>
              <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-sm font-semibold text-tsp15-mut transition has-checked:bg-white has-checked:text-tsp15-ink has-checked:shadow-sm has-focus-visible:outline-2 has-focus-visible:outline-tsp15-acc"><input type="radio" name="format" value="zip" class="sr-only">Both · ZIP</label>
            </div>
          </fieldset>
          <label class="grid content-start gap-2"><span class="font-bold">Date range</span><select name="range" class="min-h-11 rounded-xl border border-tsp15-line bg-white px-3 text-sm outline-none focus:ring-4 focus:ring-tsp15-acc/15"><option value="1">All time</option><option value="0.6">Last 12 months</option><option value="0.15">Last 30 days</option></select></label>
        </div>
        <div class="flex flex-wrap items-center justify-between gap-4 border-t border-tsp15-line pt-5">
          <p data-estimate aria-live="polite" class="text-sm text-tsp15-mut"></p>
          <button type="submit" data-request class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp15-ink px-5 text-sm font-semibold text-white transition hover:bg-tsp15-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp15-acc disabled:cursor-not-allowed disabled:opacity-40">Request export</button>
        </div>
      </form>

      <div class="hidden gap-5 rounded-3xl border border-tsp15-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)] group-data-[state=queued]/ex:grid group-data-[state=preparing]/ex:grid group-data-[state=ready]/ex:grid sm:p-7" aria-live="polite">
        <ol class="grid grid-cols-3 gap-2 text-sm font-semibold">
          <li class="grid gap-2"><span class="h-1.5 rounded-full bg-tsp15-acc"></span><span class="text-tsp15-acc">Queued</span></li>
          <li class="grid gap-2"><span class="h-1.5 rounded-full bg-tsp15-line transition group-data-[state=preparing]/ex:bg-tsp15-acc group-data-[state=ready]/ex:bg-tsp15-acc"></span><span class="text-tsp15-mut group-data-[state=preparing]/ex:text-tsp15-acc group-data-[state=ready]/ex:text-tsp15-acc">Preparing</span></li>
          <li class="grid gap-2"><span class="h-1.5 rounded-full bg-tsp15-line transition group-data-[state=ready]/ex:bg-tsp15-acc"></span><span class="text-tsp15-mut group-data-[state=ready]/ex:text-tsp15-acc">Ready</span></li>
        </ol>
        <div class="grid gap-3 group-data-[state=ready]/ex:hidden">
          <p class="flex items-center gap-2 font-semibold"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" class="size-4 animate-spin text-tsp15-acc motion-reduce:animate-none"><path d="M12 3a9 9 0 1 0 9 9"/></svg><span data-stage>Waiting in the queue…</span></p>
          <progress data-progress max="100" value="0" class="h-2 w-full appearance-none overflow-hidden rounded-full bg-tsp15-line [&::-webkit-progress-bar]:bg-tsp15-line [&::-webkit-progress-value]:bg-tsp15-acc [&::-webkit-progress-value]:transition-all [&::-moz-progress-bar]:bg-tsp15-acc">0%</progress>
          <p class="text-sm text-tsp15-mut">You can leave this page — we'll email <strong class="font-semibold text-tsp15-ink">[email protected]</strong> when it's done.</p>
        </div>
        <div class="hidden flex-wrap items-center gap-4 rounded-2xl bg-tsp15-acc/8 p-4 ring-1 ring-tsp15-acc/20 group-data-[state=ready]/ex:flex">
          <span class="grid size-11 flex-none place-items-center rounded-xl bg-tsp15-acc text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M21 8v13H3V8M1 3h22v5H1zM10 12h4"/></svg></span>
          <div class="min-w-0 flex-1"><p data-file class="font-semibold">northwind-export.json</p><p class="text-sm text-tsp15-mut">Link expires in 7 days · also sent to your email</p></div>
          <button type="button" data-download class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp15-acc px-5 text-sm font-semibold text-white transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp15-acc">Download</button>
          <button type="button" data-new class="min-h-11 rounded-xl px-3 text-sm font-semibold text-tsp15-mut transition hover:text-tsp15-ink focus-visible:outline-2 focus-visible:outline-tsp15-acc">New export</button>
        </div>
      </div>

      <div class="overflow-x-auto rounded-3xl border border-tsp15-line bg-white">
        <table class="w-full min-w-[32rem] text-left text-sm">
          <caption class="px-5 pt-5 text-left font-bold">Previous exports</caption>
          <thead class="text-xs uppercase tracking-wide text-tsp15-mut"><tr><th scope="col" class="px-5 py-3 font-semibold">Requested</th><th scope="col" class="px-5 py-3 font-semibold">Format</th><th scope="col" class="px-5 py-3 font-semibold">Size</th><th scope="col" class="px-5 py-3 font-semibold">Status</th></tr></thead>
          <tbody data-history class="divide-y divide-tsp15-line border-t border-tsp15-line">
            <tr><td class="px-5 py-3">Sep 2, 2026</td><td class="px-5 py-3">ZIP</td><td class="px-5 py-3 tabular-nums">2.4 GB</td><td class="px-5 py-3"><span class="rounded-full bg-zinc-100 px-2 py-0.5 text-xs font-semibold text-zinc-600">Expired</span></td></tr>
            <tr><td class="px-5 py-3">Jun 14, 2026</td><td class="px-5 py-3">CSV</td><td class="px-5 py-3 tabular-nums">196 MB</td><td class="px-5 py-3"><span class="rounded-full bg-emerald-50 px-2 py-0.5 text-xs font-semibold text-emerald-700">Downloaded</span></td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <aside class="grid content-start gap-4">
      <div class="rounded-3xl bg-tsp15-ink p-6 text-white">
        <p class="text-xs font-semibold uppercase tracking-[0.14em] text-white/60">Your rights</p>
        <p class="mt-3 font-semibold">You can take your data anywhere.</p>
        <p class="mt-2 text-sm leading-relaxed text-white/70">Exports follow GDPR Article 20 and CCPA. Files use open formats any tool can read. We never include other people's private data.</p>
      </div>
      <div class="rounded-3xl border border-tsp15-line bg-white p-6 text-sm text-tsp15-mut"><p class="font-semibold text-tsp15-ink">Leaving Northwind?</p><p class="mt-1">Export first, then delete your account from the danger zone. Deleted data can't be exported.</p></div>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp15-bg: #f3f6f4;
  --color-tsp15-bg: oklch(0.971 0.006 160);
  --color-tsp15-ink: #102019;
  --color-tsp15-ink: oklch(0.225 0.025 162);
  --color-tsp15-mut: #586a61;
  --color-tsp15-mut: oklch(0.51 0.024 162);
  --color-tsp15-line: #e0e8e3;
  --color-tsp15-line: oklch(0.925 0.011 160);
  --color-tsp15-acc: #059669;
  --color-tsp15-acc: oklch(0.596 0.127 163);
  --font-tsp15-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tsp-15 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp15]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const MB_PER_MIN = 400;
  const form = root.querySelector('[data-form]');
  const picks = [...root.querySelectorAll('[data-pick]')];
  const all = root.querySelector('[data-all]');
  const est = root.querySelector('[data-estimate]');
  const btn = root.querySelector('[data-request]');
  const human = (mb) => (mb >= 1000 ? (mb / 1000).toFixed(1) + ' GB' : mb >= 10 ? Math.round(mb) + ' MB' : mb.toFixed(1) + ' MB');
  const total = () => picks.filter((p) => p.checked).reduce((s, p) => s + +p.dataset.size, 0) * +form.elements.range.value;
  const update = () => {
    const on = picks.filter((p) => p.checked).length;
    all.checked = on === picks.length; all.indeterminate = on > 0 && on < picks.length;
    btn.disabled = !on;
    if (!on) { est.textContent = 'Choose at least one type of data.'; return; }
    const mb = total(), mins = Math.max(1, Math.round(mb / MB_PER_MIN));
    est.innerHTML = 'About <strong class="font-semibold text-tsp15-ink">' + human(mb) + '</strong> · ready in ~' + (mins < 60 ? mins + ' min' : Math.round(mins / 60) + ' h');
  };
  all.addEventListener('change', () => { picks.forEach((p) => { p.checked = all.checked; }); update(); });
  form.addEventListener('change', update);
  const stage = root.querySelector('[data-stage]');
  const bar = root.querySelector('[data-progress]');
  let snapshot;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const fmt = form.elements.format.value;
    snapshot = { size: human(total()), fmt, file: 'northwind-export-2026-10-07.' + fmt, items: picks.filter((p) => p.checked).map((p) => p.closest('label').querySelector('.font-semibold').firstChild.textContent.trim()) };
    root.querySelector('[data-file]').textContent = snapshot.file;
    root.dataset.state = 'queued'; stage.textContent = 'Waiting in the queue…'; bar.value = 0;
    setTimeout(() => {
      root.dataset.state = 'preparing';
      let p = 0;
      const tick = setInterval(() => {
        p = Math.min(100, p + 4 + Math.random() * 9);
        bar.value = p; bar.textContent = Math.round(p) + '%';
        stage.textContent = 'Preparing ' + snapshot.items[Math.min(snapshot.items.length - 1, Math.floor((p / 100) * snapshot.items.length))].toLowerCase() + '… ' + Math.round(p) + '%';
        if (p >= 100) {
          clearInterval(tick);
          root.dataset.state = 'ready';
          const tr = document.createElement('tr');
          ['Today', snapshot.fmt.toUpperCase(), snapshot.size].forEach((v) => { const td = document.createElement('td'); td.className = 'px-5 py-3 tabular-nums'; td.textContent = v; tr.appendChild(td); });
          const st = document.createElement('td'); st.className = 'px-5 py-3'; st.innerHTML = '<span class="rounded-full bg-emerald-50 px-2 py-0.5 text-xs font-semibold text-emerald-700">Ready</span>'; tr.appendChild(st);
          root.querySelector('[data-history]').prepend(tr);
        }
      }, 220);
    }, 1200);
  });
  root.querySelector('[data-download]').addEventListener('click', () => {
    const manifest = { account: '[email protected]', generated: new Date().toISOString(), format: snapshot.fmt, includes: snapshot.items, estimatedSize: snapshot.size };
    const url = URL.createObjectURL(new Blob([JSON.stringify(manifest, null, 2)], { type: 'application/json' }));
    const a = document.createElement('a'); a.href = url; a.download = snapshot.file.replace(/[.](csv|zip)$/, '.json'); document.body.appendChild(a); a.click(); a.remove();
  });
  root.querySelector('[data-new]').addEventListener('click', () => { root.dataset.state = 'idle'; update(); });
  update();
})();
```

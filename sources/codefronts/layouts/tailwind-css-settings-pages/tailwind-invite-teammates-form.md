---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-invite-teammates-form/"
title: "Tailwind Invite Teammates Form"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A fast, forgiving invite flow: paste a whole list or type addresses one by one and they become chips — invalid and duplicate ones turn red and are skipped —…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Invite Teammates Form
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-invite-teammates-form/

A fast, forgiving invite flow: paste a whole list or type addresses one by one and they become chips — invalid and duplicate ones turn red and are skipped — then pick a role from descriptive cards, see the seat cost before you commit, and send with a button that counts for you. A side panel adds a copyable invite link and domain auto-join.
## HTML
```html
<section data-tsp07 class="tsp-07 group/inv w-full min-h-svh bg-tsp07-bg px-4 py-10 font-tsp07-sans text-tsp07-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-07-h">
  <div class="mx-auto grid w-full max-w-6xl gap-8">
    <header><h1 id="tsp-07-h" class="text-3xl font-extrabold tracking-tight">Invite teammates</h1><p class="mt-1 text-tsp07-mut">They'll get an email with a link to join <strong class="font-semibold text-tsp07-ink">Northwind</strong>.</p></header>
    <div class="grid gap-6 lg:grid-cols-[minmax(0,1.6fr)_minmax(0,1fr)]">
      <div class="rounded-3xl border border-tsp07-line bg-white shadow-[0_1px_2px_rgb(0_0_0/0.04)]">
        <form data-form class="grid gap-7 p-6 group-data-sent/inv:hidden sm:p-8" novalidate>
          <div class="grid gap-2">
            <label for="tsp-07-entry" class="text-sm font-bold">Email addresses</label>
            <div data-field class="flex min-h-14 cursor-text flex-wrap items-center gap-1.5 rounded-2xl border border-tsp07-line bg-white p-2 shadow-xs transition focus-within:border-tsp07-acc focus-within:ring-4 focus-within:ring-tsp07-acc/15">
              <span data-chip data-valid="true" class="inline-flex max-w-full items-center gap-1.5 rounded-full bg-tsp07-bg py-1 pl-1 pr-1 text-sm font-medium ring-1 ring-tsp07-line data-[valid=false]:bg-rose-50 data-[valid=false]:text-rose-700 data-[valid=false]:ring-rose-200"><span data-chip-av class="grid size-6 flex-none place-items-center rounded-full bg-tsp07-acc text-[11px] font-bold uppercase text-white">l</span><span data-chip-text class="truncate">[email protected]</span><button type="button" data-chip-x class="grid size-6 place-items-center rounded-full text-current/60 transition hover:bg-black/5 focus-visible:outline-2 focus-visible:outline-tsp07-acc" aria-label="Remove [email protected]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" class="size-3"><path d="M18 6 6 18M6 6l12 12"/></svg></button></span>
              <span data-chip data-valid="false" class="inline-flex max-w-full items-center gap-1.5 rounded-full bg-tsp07-bg py-1 pl-1 pr-1 text-sm font-medium ring-1 ring-tsp07-line data-[valid=false]:bg-rose-50 data-[valid=false]:text-rose-700 data-[valid=false]:ring-rose-200"><span data-chip-av class="grid size-6 flex-none place-items-center rounded-full bg-rose-500 text-[11px] font-bold uppercase text-white">!</span><span data-chip-text class="truncate">mia@northwind</span><button type="button" data-chip-x class="grid size-6 place-items-center rounded-full text-current/60 transition hover:bg-black/5 focus-visible:outline-2 focus-visible:outline-tsp07-acc" aria-label="Remove mia@northwind"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" class="size-3"><path d="M18 6 6 18M6 6l12 12"/></svg></button></span>
              <input id="tsp-07-entry" data-entry inputmode="email" autocomplete="off" placeholder="Add emails — paste a list or press Enter" aria-describedby="tsp-07-sum" class="min-h-9 min-w-48 flex-1 bg-transparent px-2 text-sm outline-none placeholder:text-tsp07-mut">
            </div>
            <p id="tsp-07-sum" data-summary aria-live="polite" class="text-sm text-tsp07-mut"></p>
          </div>

          <fieldset class="grid gap-3">
            <legend class="mb-3 text-sm font-bold">Role</legend>
            <div class="grid gap-3 sm:grid-cols-3">
              <label class="group/r grid cursor-pointer content-start gap-2 rounded-2xl border border-tsp07-line p-4 transition hover:border-tsp07-acc/40 has-checked:border-tsp07-acc has-checked:bg-tsp07-acc/5 has-checked:ring-2 has-checked:ring-tsp07-acc/20 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp07-acc"><input type="radio" name="role" value="admin" class="sr-only"><span class="flex items-center justify-between font-bold">Admin<span class="grid size-5 place-items-center rounded-full border-2 border-tsp07-line group-has-checked/r:border-tsp07-acc group-has-checked/r:bg-tsp07-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/r:opacity-100"></span></span></span><span class="text-sm text-tsp07-mut">Manage members, billing and every workspace setting.</span></label>
              <label class="group/r grid cursor-pointer content-start gap-2 rounded-2xl border border-tsp07-line p-4 transition hover:border-tsp07-acc/40 has-checked:border-tsp07-acc has-checked:bg-tsp07-acc/5 has-checked:ring-2 has-checked:ring-tsp07-acc/20 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp07-acc"><input type="radio" name="role" value="member" class="sr-only" checked><span class="flex items-center justify-between font-bold">Member<span class="grid size-5 place-items-center rounded-full border-2 border-tsp07-line group-has-checked/r:border-tsp07-acc group-has-checked/r:bg-tsp07-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/r:opacity-100"></span></span></span><span class="text-sm text-tsp07-mut">Create and edit projects. Can't change billing.</span></label>
              <label class="group/r grid cursor-pointer content-start gap-2 rounded-2xl border border-tsp07-line p-4 transition hover:border-tsp07-acc/40 has-checked:border-tsp07-acc has-checked:bg-tsp07-acc/5 has-checked:ring-2 has-checked:ring-tsp07-acc/20 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp07-acc"><input type="radio" name="role" value="viewer" class="sr-only"><span class="flex items-center justify-between font-bold"><span class="flex items-center gap-2">Viewer <span class="rounded-full bg-emerald-100 px-2 py-0.5 text-[11px] font-bold text-emerald-700">Free</span></span><span class="grid size-5 place-items-center rounded-full border-2 border-tsp07-line group-has-checked/r:border-tsp07-acc group-has-checked/r:bg-tsp07-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/r:opacity-100"></span></span></span><span class="text-sm text-tsp07-mut">View and comment. Doesn't use a paid seat.</span></label>
            </div>
          </fieldset>

          <details class="group/msg rounded-2xl border border-tsp07-line">
            <summary class="flex min-h-12 cursor-pointer list-none items-center justify-between gap-3 px-4 text-sm font-bold [&::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-tsp07-acc rounded-2xl">Add a personal note <span class="font-normal text-tsp07-mut">optional</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="ml-auto size-4 transition group-open/msg:rotate-180"><path d="m6 9 6 6 6-6"/></svg></summary>
            <div class="px-4 pb-4"><textarea name="note" rows="3" maxlength="280" placeholder="Hey! Join us on Northwind — the Q4 roadmap lives here." class="w-full rounded-xl border border-tsp07-line px-3.5 py-3 text-sm outline-none transition focus:border-tsp07-acc focus:ring-4 focus:ring-tsp07-acc/15" aria-label="Personal note"></textarea></div>
          </details>

          <div class="flex flex-wrap items-center justify-between gap-4 border-t border-tsp07-line pt-6">
            <p data-cost class="text-sm text-tsp07-mut"></p>
            <button type="submit" data-send class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp07-ink px-5 text-sm font-bold text-white shadow-sm transition hover:bg-tsp07-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp07-acc disabled:cursor-not-allowed disabled:opacity-40">Send invites</button>
          </div>
        </form>

        <div class="hidden justify-items-center gap-4 p-10 text-center group-data-sent/inv:grid sm:p-14" aria-live="polite">
          <span class="grid size-14 place-items-center rounded-full bg-emerald-100 text-emerald-600"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="size-7"><path d="M20 6 9 17l-5-5"/></svg></span>
          <h2 class="text-xl font-extrabold">Invites sent</h2>
          <p data-sent-msg class="max-w-sm text-pretty text-tsp07-mut"></p>
          <button type="button" data-again class="inline-flex min-h-11 items-center rounded-xl border border-tsp07-line bg-white px-5 text-sm font-bold shadow-xs transition hover:bg-tsp07-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp07-acc">Invite more people</button>
        </div>
      </div>

      <aside class="grid content-start gap-6">
        <div class="grid gap-4 rounded-3xl border border-tsp07-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)]">
          <div><h2 class="font-bold">Invite link</h2><p class="mt-1 text-sm text-tsp07-mut">Anyone with the link joins as a Member.</p></div>
          <div class="flex gap-2"><input data-link readonly value="https://northwind.app/join/7Kq2-mX9p" aria-label="Invite link" class="min-h-11 min-w-0 flex-1 rounded-xl border border-tsp07-line bg-tsp07-bg px-3 font-mono text-xs text-tsp07-mut outline-none focus:ring-4 focus:ring-tsp07-acc/15"><button type="button" data-copy class="group/cp inline-flex min-h-11 items-center gap-1.5 rounded-xl bg-tsp07-acc px-4 text-sm font-bold text-white transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp07-acc data-copied:bg-emerald-600"><span class="group-data-copied/cp:hidden">Copy</span><span class="hidden group-data-copied/cp:inline">Copied</span></button></div>
          <label class="grid gap-1.5 text-sm"><span class="font-semibold">Expires</span><select class="min-h-11 rounded-xl border border-tsp07-line bg-white px-3 text-sm outline-none focus:ring-4 focus:ring-tsp07-acc/15"><option>In 7 days</option><option>In 30 days</option><option>Never</option></select></label>
        </div>
        <label class="flex cursor-pointer items-start justify-between gap-4 rounded-3xl border border-tsp07-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)]"><span><span class="block font-bold">Domain auto-join</span><span class="mt-1 block text-sm text-tsp07-mut">Anyone who signs up with an <strong class="font-semibold text-tsp07-ink">@northwind.co</strong> email joins automatically as a Viewer.</span></span><span class="relative mt-1 flex-none"><input type="checkbox" role="switch" class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-zinc-300 transition peer-checked:bg-tsp07-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp07-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5"></span></span></label>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp07-bg: #f8f6f4;
  --color-tsp07-bg: oklch(0.975 0.004 60);
  --color-tsp07-ink: #1f1a17;
  --color-tsp07-ink: oklch(0.22 0.01 50);
  --color-tsp07-mut: #6b625b;
  --color-tsp07-mut: oklch(0.52 0.016 55);
  --color-tsp07-line: #ebe5df;
  --color-tsp07-line: oklch(0.925 0.01 60);
  --color-tsp07-acc: #e2531b;
  --color-tsp07-acc: oklch(0.63 0.19 40);
  --font-tsp07-sans: 'Figtree', system-ui, sans-serif;
}

.tsp-07 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp07]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const PRICE = { admin: 24, member: 24, viewer: 0 };
  const form = root.querySelector('[data-form]');
  const field = root.querySelector('[data-field]');
  const entry = root.querySelector('[data-entry]');
  const proto = { valid: field.querySelector('[data-valid=true]').cloneNode(true), invalid: field.querySelector('[data-valid=false]').cloneNode(true) };
  const isEmail = (v) => /^[^@ ,;]+@[^@ ,;]+[.][a-z]{2,}$/i.test(v);
  const chips = () => [...field.querySelectorAll('[data-chip]')];
  const emails = () => chips().map((c) => c.querySelector('[data-chip-text]').textContent);
  const addChip = (raw) => {
    const v = raw.trim().toLowerCase();
    if (!v) return;
    const dup = emails().includes(v);
    const ok = isEmail(v) && !dup;
    const c = (ok ? proto.valid : proto.invalid).cloneNode(true);
    c.querySelector('[data-chip-text]').textContent = v;
    c.querySelector('[data-chip-av]').textContent = ok ? v[0] : '!';
    c.querySelector('[data-chip-x]').setAttribute('aria-label', 'Remove ' + v);
    if (dup) c.title = 'Already in the list';
    field.insertBefore(c, entry);
  };
  const flush = () => { entry.value.split(/[\s,;]+/).forEach(addChip); entry.value = ''; update(); };
  const update = () => {
    const valid = chips().filter((c) => c.dataset.valid === 'true').length;
    const bad = chips().length - valid;
    const role = form.elements.role.value;
    root.querySelector('[data-summary]').textContent = chips().length ? valid + ' ready' + (bad ? ' · ' + bad + ' invalid or duplicate — will be skipped' : '') : 'Separate addresses with commas, spaces or new lines.';
    const cost = valid * PRICE[role];
    root.querySelector('[data-cost]').innerHTML = !valid ? 'Add at least one valid email.' : cost ? 'Adds <strong class="font-semibold text-tsp07-ink">' + valid + ' seat' + (valid > 1 ? 's' : '') + '</strong> · +$' + cost + '/mo on your next invoice' : 'Viewers don\'t use paid seats — <strong class="font-semibold text-tsp07-ink">no extra cost</strong>';
    const btn = root.querySelector('[data-send]');
    btn.disabled = !valid;
    btn.textContent = valid ? 'Send ' + valid + ' invite' + (valid > 1 ? 's' : '') : 'Send invites';
  };
  field.addEventListener('click', (e) => {
    const x = e.target.closest('[data-chip-x]');
    if (x) { x.closest('[data-chip]').remove(); update(); entry.focus(); return; }
    if (e.target === field) entry.focus();
  });
  entry.addEventListener('keydown', (e) => {
    if (['Enter', ',', ' ', ';'].includes(e.key)) { e.preventDefault(); flush(); }
    else if (e.key === 'Backspace' && !entry.value) { const last = chips().pop(); if (last) { last.remove(); update(); } }
  });
  entry.addEventListener('blur', flush);
  entry.addEventListener('paste', (e) => { e.preventDefault(); entry.value += (e.clipboardData || window.clipboardData).getData('text'); flush(); });
  form.addEventListener('change', update);
  form.addEventListener('submit', (e) => {
    e.preventDefault(); flush();
    const ok = chips().filter((c) => c.dataset.valid === 'true').map((c) => c.querySelector('[data-chip-text]').textContent);
    if (!ok.length) return;
    root.querySelector('[data-sent-msg]').textContent = ok.join(', ') + ' will receive an invite to join as ' + form.elements.role.value + '.';
    root.dataset.sent = '';
  });
  root.querySelector('[data-again]').addEventListener('click', () => { chips().forEach((c) => c.remove()); delete root.dataset.sent; update(); entry.focus(); });
  const copyBtn = root.querySelector('[data-copy]');
  copyBtn.addEventListener('click', async () => {
    const link = root.querySelector('[data-link]');
    try { await navigator.clipboard.writeText(link.value); } catch (err) { link.select(); document.execCommand('copy'); }
    copyBtn.dataset.copied = '';
    setTimeout(() => delete copyBtn.dataset.copied, 1600);
  });
  update();
})();
```

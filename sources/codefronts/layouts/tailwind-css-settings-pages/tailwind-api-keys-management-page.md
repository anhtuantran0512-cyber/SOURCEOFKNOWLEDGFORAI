---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-api-keys-management-page/"
title: "Tailwind API Keys Management Page"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A developer-grade API keys page in a dark theme: masked keys with copy, Live / Test badges, scopes, last-used and 24-hour request sparklines, a stale-key…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind API Keys Management Page
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-api-keys-management-page/

A developer-grade API keys page in a dark theme: masked keys with copy, Live / Test badges, scopes, last-used and 24-hour request sparklines, a stale-key warning, a two-step revoke that arms then confirms, and a native <dialog> that creates a scoped key with crypto.getRandomValues and reveals the secret exactly once.
## HTML
```html
<section data-tsp09 class="tsp-09 w-full min-h-svh bg-tsp09-bg bg-[radial-gradient(60%_40%_at_80%_0%,rgb(163_230_53/0.08),transparent_70%)] px-4 py-10 font-tsp09-sans text-white antialiased [color-scheme:dark] sm:px-8 sm:py-14" aria-labelledby="tsp-09-h">
  <div class="mx-auto grid w-full max-w-6xl gap-6">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div><h1 id="tsp-09-h" class="text-3xl font-semibold tracking-tight">API keys</h1><p class="mt-1 text-tsp09-mut">Authenticate requests to the Northwind API.</p></div>
      <button type="button" data-open class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp09-acc px-4 text-sm font-semibold text-tsp09-bg shadow-[0_0_0_1px_rgb(255_255_255/0.1),0_10px_30px_-10px_var(--color-tsp09-acc)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp09-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 5v14M5 12h14"/></svg>Create key</button>
    </header>

    <p class="flex items-start gap-3 rounded-2xl border border-amber-400/20 bg-amber-400/5 p-4 text-sm text-amber-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mt-0.5 size-4 flex-none text-amber-400"><path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/></svg><span>Secret keys can read and write your data. Keep them on the server — never in client code or public repositories.</span></p>

    <ul data-list class="grid gap-3" aria-label="API keys">
      <li data-key class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-gone:grid-rows-[0fr] data-gone:opacity-0"><div class="overflow-hidden"><div class="grid gap-4 rounded-2xl border border-white/10 bg-tsp09-card p-5 lg:grid-cols-[minmax(0,1.3fr)_minmax(0,1fr)_auto] lg:items-center">
        <div class="grid gap-2 min-w-0">
          <p class="flex flex-wrap items-center gap-2"><span data-k-name class="font-semibold">Production server</span><span data-k-env class="rounded-md bg-amber-400/10 px-1.5 py-0.5 font-tsp09-mono text-[11px] font-medium text-amber-300 ring-1 ring-amber-400/20">live</span></p>
          <div class="flex items-center gap-2"><code data-k-mask class="truncate rounded-lg bg-black/40 px-2.5 py-1.5 font-tsp09-mono text-[13px] text-white/80 ring-1 ring-white/10">sk_live_••••••••••••3f9a</code><button type="button" data-copy data-value="key_01J8ZQ3f9a" class="group/cp grid size-11 flex-none place-items-center rounded-xl text-tsp09-mut transition hover:bg-white/5 hover:text-white focus-visible:outline-2 focus-visible:outline-tsp09-acc data-copied:text-tsp09-acc" aria-label="Copy key ID"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 group-data-copied/cp:hidden"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="hidden size-4 group-data-copied/cp:block"><path d="M20 6 9 17l-5-5"/></svg></button></div>
          <p data-k-scopes class="flex flex-wrap gap-1.5"><span class="rounded-md bg-white/5 px-1.5 py-0.5 font-tsp09-mono text-[11px] text-white/70 ring-1 ring-white/10">read</span><span class="rounded-md bg-white/5 px-1.5 py-0.5 font-tsp09-mono text-[11px] text-white/70 ring-1 ring-white/10">write</span></p>
        </div>
        <div class="grid grid-cols-[1fr_auto] items-end gap-4 text-sm">
          <dl class="grid gap-1 text-tsp09-mut"><div class="flex gap-2"><dt>Created</dt><dd data-k-created class="text-white/80">Aug 12, 2026</dd></div><div class="flex gap-2"><dt>Last used</dt><dd data-k-used class="text-white/80">2 min ago</dd></div></dl>
          <div class="grid justify-items-end gap-1" aria-label="24.1k requests in 24 hours"><div class="flex h-8 items-end gap-0.5" aria-hidden="true"><i class="h-[40%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[55%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[35%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[70%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[60%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[85%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[75%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-full w-1 rounded-full bg-tsp09-acc"></i></div><span data-k-req class="font-tsp09-mono text-[11px] text-tsp09-mut">24.1k / 24h</span></div>
        </div>
        <button type="button" data-revoke class="inline-flex min-h-11 items-center justify-center rounded-xl border border-white/10 px-4 text-sm font-semibold text-white/80 transition hover:border-rose-400/40 hover:text-rose-300 focus-visible:outline-2 focus-visible:outline-tsp09-acc data-armed:border-transparent data-armed:bg-rose-600 data-armed:text-white">Revoke</button>
      </div></div></li>
      <li data-key class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-gone:grid-rows-[0fr] data-gone:opacity-0"><div class="overflow-hidden"><div class="grid gap-4 rounded-2xl border border-white/10 bg-tsp09-card p-5 lg:grid-cols-[minmax(0,1.3fr)_minmax(0,1fr)_auto] lg:items-center">
        <div class="grid gap-2 min-w-0">
          <p class="flex flex-wrap items-center gap-2"><span class="font-semibold">CI pipeline</span><span class="rounded-md bg-amber-400/10 px-1.5 py-0.5 font-tsp09-mono text-[11px] font-medium text-amber-300 ring-1 ring-amber-400/20">live</span></p>
          <div class="flex items-center gap-2"><code class="truncate rounded-lg bg-black/40 px-2.5 py-1.5 font-tsp09-mono text-[13px] text-white/80 ring-1 ring-white/10">sk_live_••••••••••••71bc</code><button type="button" data-copy data-value="key_01J7KM71bc" class="group/cp grid size-11 flex-none place-items-center rounded-xl text-tsp09-mut transition hover:bg-white/5 hover:text-white focus-visible:outline-2 focus-visible:outline-tsp09-acc data-copied:text-tsp09-acc" aria-label="Copy key ID"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 group-data-copied/cp:hidden"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="hidden size-4 group-data-copied/cp:block"><path d="M20 6 9 17l-5-5"/></svg></button></div>
          <p class="flex flex-wrap gap-1.5"><span class="rounded-md bg-white/5 px-1.5 py-0.5 font-tsp09-mono text-[11px] text-white/70 ring-1 ring-white/10">read</span></p>
        </div>
        <div class="grid grid-cols-[1fr_auto] items-end gap-4 text-sm">
          <dl class="grid gap-1 text-tsp09-mut"><div class="flex gap-2"><dt>Created</dt><dd class="text-white/80">Jul 3, 2026</dd></div><div class="flex gap-2"><dt>Last used</dt><dd class="text-white/80">3 hours ago</dd></div></dl>
          <div class="grid justify-items-end gap-1" aria-label="1.2k requests in 24 hours"><div class="flex h-8 items-end gap-0.5" aria-hidden="true"><i class="h-[10%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[60%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[10%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[10%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[80%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[10%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[50%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[20%] w-1 rounded-full bg-tsp09-acc"></i></div><span class="font-tsp09-mono text-[11px] text-tsp09-mut">1.2k / 24h</span></div>
        </div>
        <button type="button" data-revoke class="inline-flex min-h-11 items-center justify-center rounded-xl border border-white/10 px-4 text-sm font-semibold text-white/80 transition hover:border-rose-400/40 hover:text-rose-300 focus-visible:outline-2 focus-visible:outline-tsp09-acc data-armed:border-transparent data-armed:bg-rose-600 data-armed:text-white">Revoke</button>
      </div></div></li>
      <li data-key class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-gone:grid-rows-[0fr] data-gone:opacity-0"><div class="overflow-hidden"><div class="grid gap-4 rounded-2xl border border-white/10 bg-tsp09-card p-5 lg:grid-cols-[minmax(0,1.3fr)_minmax(0,1fr)_auto] lg:items-center">
        <div class="grid gap-2 min-w-0">
          <p class="flex flex-wrap items-center gap-2"><span class="font-semibold">Local dev — Ava</span><span class="rounded-md bg-sky-400/10 px-1.5 py-0.5 font-tsp09-mono text-[11px] font-medium text-sky-300 ring-1 ring-sky-400/20">test</span></p>
          <div class="flex items-center gap-2"><code class="truncate rounded-lg bg-black/40 px-2.5 py-1.5 font-tsp09-mono text-[13px] text-white/80 ring-1 ring-white/10">sk_test_••••••••••••a002</code><button type="button" data-copy data-value="key_01J9AAa002" class="group/cp grid size-11 flex-none place-items-center rounded-xl text-tsp09-mut transition hover:bg-white/5 hover:text-white focus-visible:outline-2 focus-visible:outline-tsp09-acc data-copied:text-tsp09-acc" aria-label="Copy key ID"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 group-data-copied/cp:hidden"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="hidden size-4 group-data-copied/cp:block"><path d="M20 6 9 17l-5-5"/></svg></button></div>
          <p class="flex flex-wrap gap-1.5"><span class="rounded-md bg-white/5 px-1.5 py-0.5 font-tsp09-mono text-[11px] text-white/70 ring-1 ring-white/10">read</span><span class="rounded-md bg-white/5 px-1.5 py-0.5 font-tsp09-mono text-[11px] text-white/70 ring-1 ring-white/10">write</span><span class="rounded-md bg-rose-400/10 px-1.5 py-0.5 font-tsp09-mono text-[11px] text-rose-300 ring-1 ring-rose-400/20">admin</span></p>
        </div>
        <div class="grid grid-cols-[1fr_auto] items-end gap-4 text-sm">
          <dl class="grid gap-1 text-tsp09-mut"><div class="flex gap-2"><dt>Created</dt><dd class="text-white/80">Sep 28, 2026</dd></div><div class="flex gap-2"><dt>Last used</dt><dd class="text-white/80">Yesterday</dd></div></dl>
          <div class="grid justify-items-end gap-1" aria-label="312 requests in 24 hours"><div class="flex h-8 items-end gap-0.5" aria-hidden="true"><i class="h-[30%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[45%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[20%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[10%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[10%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[10%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[10%] w-1 rounded-full bg-tsp09-acc/40"></i><i class="h-[10%] w-1 rounded-full bg-tsp09-acc"></i></div><span class="font-tsp09-mono text-[11px] text-tsp09-mut">312 / 24h</span></div>
        </div>
        <button type="button" data-revoke class="inline-flex min-h-11 items-center justify-center rounded-xl border border-white/10 px-4 text-sm font-semibold text-white/80 transition hover:border-rose-400/40 hover:text-rose-300 focus-visible:outline-2 focus-visible:outline-tsp09-acc data-armed:border-transparent data-armed:bg-rose-600 data-armed:text-white">Revoke</button>
      </div></div></li>
      <li data-key class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-gone:grid-rows-[0fr] data-gone:opacity-0"><div class="overflow-hidden"><div class="grid gap-4 rounded-2xl border border-amber-400/25 bg-tsp09-card p-5 lg:grid-cols-[minmax(0,1.3fr)_minmax(0,1fr)_auto] lg:items-center">
        <div class="grid gap-2 min-w-0">
          <p class="flex flex-wrap items-center gap-2"><span class="font-semibold">Old Zapier key</span><span class="rounded-md bg-amber-400/10 px-1.5 py-0.5 font-tsp09-mono text-[11px] font-medium text-amber-300 ring-1 ring-amber-400/20">live</span><span class="rounded-full bg-amber-400 px-2 py-0.5 text-[11px] font-semibold text-tsp09-bg">Unused 90+ days</span></p>
          <div class="flex items-center gap-2"><code class="truncate rounded-lg bg-black/40 px-2.5 py-1.5 font-tsp09-mono text-[13px] text-white/80 ring-1 ring-white/10">sk_live_••••••••••••9de1</code><button type="button" data-copy data-value="key_01HZ2X9de1" class="group/cp grid size-11 flex-none place-items-center rounded-xl text-tsp09-mut transition hover:bg-white/5 hover:text-white focus-visible:outline-2 focus-visible:outline-tsp09-acc data-copied:text-tsp09-acc" aria-label="Copy key ID"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 group-data-copied/cp:hidden"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="hidden size-4 group-data-copied/cp:block"><path d="M20 6 9 17l-5-5"/></svg></button></div>
          <p class="flex flex-wrap gap-1.5"><span class="rounded-md bg-white/5 px-1.5 py-0.5 font-tsp09-mono text-[11px] text-white/70 ring-1 ring-white/10">read</span></p>
        </div>
        <div class="grid grid-cols-[1fr_auto] items-end gap-4 text-sm">
          <dl class="grid gap-1 text-tsp09-mut"><div class="flex gap-2"><dt>Created</dt><dd class="text-white/80">Jan 9, 2026</dd></div><div class="flex gap-2"><dt>Last used</dt><dd class="text-amber-300">94 days ago</dd></div></dl>
          <div class="grid justify-items-end gap-1"><span class="font-tsp09-mono text-[11px] text-tsp09-mut">0 / 24h</span></div>
        </div>
        <button type="button" data-revoke class="inline-flex min-h-11 items-center justify-center rounded-xl border border-white/10 px-4 text-sm font-semibold text-white/80 transition hover:border-rose-400/40 hover:text-rose-300 focus-visible:outline-2 focus-visible:outline-tsp09-acc data-armed:border-transparent data-armed:bg-rose-600 data-armed:text-white">Revoke</button>
      </div></div></li>
    </ul>
    <p data-status role="status" aria-live="polite" class="text-sm text-tsp09-mut empty:hidden"></p>

    <div class="overflow-hidden rounded-2xl border border-white/10 bg-black/40">
      <p class="border-b border-white/10 px-4 py-2.5 font-tsp09-mono text-xs text-tsp09-mut">Quick start</p>
      <pre class="overflow-x-auto p-4 font-tsp09-mono text-[13px] leading-relaxed text-white/80"><code><span class="text-tsp09-acc">curl</span> https://api.northwind.dev/v1/projects \
  -H <span class="text-amber-300">"Authorization: Bearer sk_live_…"</span></code></pre>
    </div>
  </div>

  <dialog data-dialog data-step="form" aria-labelledby="tsp-09-dh" class="group/dlg m-auto w-[min(30rem,calc(100%-2rem))] rounded-3xl bg-tsp09-card p-0 text-white opacity-100 ring-1 ring-white/10 shadow-2xl transition-[opacity,scale,display,overlay] transition-discrete duration-200 backdrop:bg-black/70 backdrop:backdrop-blur-sm starting:open:scale-95 starting:open:opacity-0 motion-reduce:transition-none">
    <form data-create method="dialog" class="grid gap-5 p-6 group-data-[step=reveal]/dlg:hidden sm:p-7">
      <div><h2 id="tsp-09-dh" class="text-lg font-semibold">Create a secret key</h2><p class="mt-1 text-sm text-tsp09-mut">Scope it to the least access it needs.</p></div>
      <label class="grid gap-1.5"><span class="text-sm font-medium">Name</span><input name="name" required placeholder="e.g. Billing worker" class="min-h-11 rounded-xl border border-white/10 bg-black/30 px-3.5 text-sm outline-none transition placeholder:text-white/30 focus:border-tsp09-acc focus:ring-4 focus:ring-tsp09-acc/15"></label>
      <fieldset class="grid gap-2"><legend class="mb-2 text-sm font-medium">Environment</legend><div class="grid grid-cols-2 gap-1 rounded-xl bg-black/30 p-1 ring-1 ring-white/10"><label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-sm font-medium text-tsp09-mut transition has-checked:bg-white/10 has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp09-acc"><input type="radio" name="env" value="live" class="sr-only" checked>Live</label><label class="flex min-h-10 cursor-pointer items-center justify-center rounded-lg text-sm font-medium text-tsp09-mut transition has-checked:bg-white/10 has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp09-acc"><input type="radio" name="env" value="test" class="sr-only">Test</label></div></fieldset>
      <fieldset class="grid gap-2"><legend class="mb-2 text-sm font-medium">Scopes</legend>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-3 ring-1 ring-white/10 transition has-checked:bg-tsp09-acc/5 has-checked:ring-tsp09-acc/40"><input type="checkbox" name="scope" value="read" checked class="size-4 accent-tsp09-acc"><span class="font-tsp09-mono text-sm">read</span><span class="ml-auto text-xs text-tsp09-mut">List and fetch resources</span></label>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-3 ring-1 ring-white/10 transition has-checked:bg-tsp09-acc/5 has-checked:ring-tsp09-acc/40"><input type="checkbox" name="scope" value="write" class="size-4 accent-tsp09-acc"><span class="font-tsp09-mono text-sm">write</span><span class="ml-auto text-xs text-tsp09-mut">Create and update</span></label>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-xl px-3 ring-1 ring-white/10 transition has-checked:bg-rose-500/10 has-checked:ring-rose-400/40"><input type="checkbox" name="scope" value="admin" class="size-4 accent-rose-500"><span class="font-tsp09-mono text-sm">admin</span><span class="ml-auto text-xs text-rose-300">Manage members &amp; billing</span></label>
      </fieldset>
      <label class="grid gap-1.5"><span class="text-sm font-medium">Expires</span><select name="exp" class="min-h-11 rounded-xl border border-white/10 bg-black/30 px-3 text-sm outline-none focus:border-tsp09-acc"><option>In 30 days</option><option selected>In 90 days</option><option>Never</option></select></label>
      <div class="flex justify-end gap-2 pt-1"><button type="button" data-cancel class="min-h-11 rounded-xl px-4 text-sm font-semibold text-white/70 transition hover:text-white focus-visible:outline-2 focus-visible:outline-tsp09-acc">Cancel</button><button type="submit" value="create" class="min-h-11 rounded-xl bg-tsp09-acc px-5 text-sm font-semibold text-tsp09-bg transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp09-acc">Create key</button></div>
    </form>
    <div class="hidden gap-5 p-6 group-data-[step=reveal]/dlg:grid sm:p-7">
      <span class="grid size-11 place-items-center rounded-full bg-tsp09-acc/15 text-tsp09-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M2 18v3h3l7.4-7.4A5 5 0 1 0 9.4 10.6L2 18zM16 8h.01"/></svg></span>
      <div><h2 class="text-lg font-semibold">Save your key now</h2><p class="mt-1 text-sm text-tsp09-mut">For security we'll only show it once. Store it in your secrets manager.</p></div>
      <div class="flex items-center gap-2 rounded-xl bg-black/50 p-2 pl-3.5 ring-1 ring-tsp09-acc/30"><code data-secret class="min-w-0 flex-1 break-all font-tsp09-mono text-[13px] text-tsp09-acc"></code><button type="button" data-copy-secret class="group/cp inline-flex min-h-11 flex-none items-center rounded-lg bg-white/10 px-3 text-sm font-semibold transition hover:bg-white/15 focus-visible:outline-2 focus-visible:outline-tsp09-acc data-copied:text-tsp09-acc"><span class="group-data-copied/cp:hidden">Copy</span><span class="hidden group-data-copied/cp:inline">Copied ✓</span></button></div>
      <button type="button" data-done class="min-h-11 rounded-xl bg-white px-5 text-sm font-semibold text-tsp09-bg transition hover:bg-white/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp09-acc">I've saved it</button>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp09-bg: #09090b;
  --color-tsp09-bg: oklch(0.141 0.005 286);
  --color-tsp09-card: #131316;
  --color-tsp09-card: oklch(0.185 0.006 286);
  --color-tsp09-mut: #9b9ba6;
  --color-tsp09-mut: oklch(0.7 0.013 286);
  --color-tsp09-acc: #a3e635;
  --color-tsp09-acc: oklch(0.841 0.203 129);
  --font-tsp09-sans: 'Geist', system-ui, sans-serif;
  --font-tsp09-mono: 'Geist Mono', ui-monospace, monospace;
}

.tsp-09 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp09]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const ARM_MS = 3000;
  const list = root.querySelector('[data-list]');
  const status = root.querySelector('[data-status]');
  const dlg = root.querySelector('[data-dialog]');
  const form = root.querySelector('[data-create]');
  const copy = async (text, btn) => {
    try { await navigator.clipboard.writeText(text); } catch (e) { const t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select(); document.execCommand('copy'); t.remove(); }
    btn.dataset.copied = '';
    setTimeout(() => delete btn.dataset.copied, 1500);
  };
  const wire = (li) => {
    li.querySelector('[data-copy]').addEventListener('click', (e) => copy(e.currentTarget.dataset.value, e.currentTarget));
    const rv = li.querySelector('[data-revoke]');
    let t;
    rv.addEventListener('click', () => {
      if (rv.hasAttribute('data-armed')) {
        li.dataset.gone = '';
        status.textContent = 'Key revoked. Requests using it now return 401.';
        setTimeout(() => li.remove(), 320);
        return;
      }
      rv.dataset.armed = ''; rv.textContent = 'Click to confirm';
      clearTimeout(t);
      t = setTimeout(() => { delete rv.dataset.armed; rv.textContent = 'Revoke'; }, ARM_MS);
    });
  };
  list.querySelectorAll('[data-key]').forEach(wire);
  const ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  const rand = (n) => Array.from(crypto.getRandomValues(new Uint8Array(n)), (b) => ALPHA[b % ALPHA.length]).join('');
  let draft = null;
  root.querySelector('[data-open]').addEventListener('click', () => { form.reset(); dlg.dataset.step = 'form'; dlg.showModal(); });
  root.querySelector('[data-cancel]').addEventListener('click', () => dlg.close());
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    const env = form.elements.env.value;
    const secret = 'sk_' + env + '_' + rand(32);
    draft = { name: form.elements.name.value, env, secret, scopes: [...form.querySelectorAll('[name=scope]:checked')].map((c) => c.value) };
    root.querySelector('[data-secret]').textContent = secret;
    dlg.dataset.step = 'reveal';
  });
  root.querySelector('[data-copy-secret]').addEventListener('click', (e) => copy(draft.secret, e.currentTarget));
  root.querySelector('[data-done]').addEventListener('click', () => {
    dlg.close();
    if (!draft) return;
    const li = list.querySelector('[data-key]').cloneNode(true);
    li.querySelector('[data-k-name]').textContent = draft.name;
    const env = li.querySelector('[data-k-env]');
    env.textContent = draft.env;
    if (draft.env === 'test') env.className = env.className.replaceAll('amber', 'sky');
    li.querySelector('[data-k-mask]').textContent = 'sk_' + draft.env + '_••••••••••••' + draft.secret.slice(-4);
    li.querySelector('[data-copy]').dataset.value = 'key_' + draft.secret.slice(-10);
    const sc = li.querySelector('[data-k-scopes]');
    const chip = sc.firstElementChild;
    sc.replaceChildren(...draft.scopes.map((s) => { const c = chip.cloneNode(); c.textContent = s; return c; }));
    li.querySelector('[data-k-created]').textContent = 'Just now';
    li.querySelector('[data-k-used]').textContent = 'Never';
    li.querySelector('[data-k-req]').textContent = '0 / 24h';
    const rv = li.querySelector('[data-revoke]'); delete rv.dataset.armed; rv.textContent = 'Revoke';
    list.prepend(li); wire(li);
    status.textContent = 'Key "' + draft.name + '" created.';
    draft = null;
  });
})();
```

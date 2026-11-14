---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-api-feature-section-with-code/"
title: "Tailwind API Feature Section with Code"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "A developer-facing feature split: benefits on the left, a request/response pair on the right with cURL · Node · Python tabs and a one-click copy button."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind API Feature Section with Code
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-api-feature-section-with-code/

A developer-facing feature split: benefits on the left, a request/response pair on the right with cURL · Node · Python tabs and a one-click copy button. Tabs are a pure radio group; the only script copies whichever snippet is visible and flips a data-copied attribute the button reads.
## HTML
```html
<section class="tfs-10 w-full min-h-svh bg-tfs10-bg px-5 py-20 font-tfs10-sans text-tfs10-ink antialiased sm:py-28" aria-labelledby="tfs-10-h">
  <div class="mx-auto grid w-full max-w-6xl gap-12 lg:grid-cols-[1fr_1.25fr] lg:items-center lg:gap-16">
    <div class="grid gap-8">
      <div class="grid gap-4">
        <p class="font-tfs10-mono text-xs font-semibold uppercase tracking-[0.18em] text-tfs10-acc">Developer API</p>
        <h2 id="tfs-10-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">One request. A verified identity.</h2>
        <p class="text-pretty text-lg text-tfs10-mut">Sable's REST API returns a decision, a risk score and the evidence behind it — in under 100 ms.</p>
      </div>
      <ul class="grid gap-5">
        <li class="flex gap-4"><span class="grid size-9 flex-none place-items-center rounded-lg bg-tfs10-acc/10 text-tfs10-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg></span><div><h3 class="font-semibold">p95 under 100 ms</h3><p class="text-sm text-tfs10-mut">Served from 14 regions, auto-routed.</p></div></li>
        <li class="flex gap-4"><span class="grid size-9 flex-none place-items-center rounded-lg bg-tfs10-acc/10 text-tfs10-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/></svg></span><div><h3 class="font-semibold">Typed SDKs</h3><p class="text-sm text-tfs10-mut">Node, Python, Go and Ruby, generated from OpenAPI.</p></div></li>
        <li class="flex gap-4"><span class="grid size-9 flex-none place-items-center rounded-lg bg-tfs10-acc/10 text-tfs10-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 3v5h-5"/></svg></span><div><h3 class="font-semibold">Idempotent by default</h3><p class="text-sm text-tfs10-mut">Retries never double-charge or double-verify.</p></div></li>
      </ul>
    </div>
    <div class="group/api grid gap-4" data-tfs10>
      <div class="overflow-hidden rounded-2xl bg-tfs10-code shadow-[0_30px_80px_-30px_rgb(2_6_23/0.6)] ring-1 ring-white/10">
        <div class="flex items-center gap-2 border-b border-white/10 px-3 py-2">
          <fieldset class="flex gap-1"><legend class="sr-only">Language</legend>
            <label class="inline-flex min-h-9 cursor-pointer items-center rounded-lg px-3 font-tfs10-mono text-xs text-slate-400 transition hover:text-white has-checked:bg-white/10 has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tfs10-acc"><input type="radio" name="tfs-10-lang" id="tfs-10-curl" class="sr-only" checked>cURL</label><label class="inline-flex min-h-9 cursor-pointer items-center rounded-lg px-3 font-tfs10-mono text-xs text-slate-400 transition hover:text-white has-checked:bg-white/10 has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tfs10-acc"><input type="radio" name="tfs-10-lang" id="tfs-10-node" class="sr-only">Node</label><label class="inline-flex min-h-9 cursor-pointer items-center rounded-lg px-3 font-tfs10-mono text-xs text-slate-400 transition hover:text-white has-checked:bg-white/10 has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tfs10-acc"><input type="radio" name="tfs-10-lang" id="tfs-10-py" class="sr-only">Python</label>
          </fieldset>
          <button type="button" data-copy class="group/btn ml-auto inline-flex min-h-9 items-center gap-1.5 rounded-lg px-3 text-xs font-medium text-slate-300 ring-1 ring-white/10 transition hover:bg-white/10 hover:text-white focus-visible:outline-2 focus-visible:outline-tfs10-acc data-copied:text-emerald-300 data-copied:ring-emerald-400/40"><span class="group-data-copied/btn:hidden"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M8 8h12v12H8zM16 8V4H4v12h4"/></svg></span><span class="hidden group-data-copied/btn:block"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M20 6 9 17l-5-5"/></svg></span><span class="group-data-copied/btn:hidden">Copy</span><span class="hidden group-data-copied/btn:inline">Copied</span></button>
          <span role="status" class="sr-only"></span>
        </div>
        <pre tabindex="0" data-lang="curl" class="hidden overflow-x-auto p-5 font-tfs10-mono text-[13px] leading-6 text-slate-200 group-has-[#tfs-10-curl:checked]/api:block focus-visible:outline-2 focus-visible:outline-tfs10-acc"><code><span class="text-tfs10-key">curl</span> https://api.sable.dev/v1/verify \
  -H <span class="text-tfs10-str">"Authorization: Bearer $SABLE_KEY"</span> \
  -d <span class="text-tfs10-str">[email protected]</span> \
  -d <span class="text-tfs10-str">ip=81.2.69.142</span></code></pre>
        <pre tabindex="0" data-lang="node" class="hidden overflow-x-auto p-5 font-tfs10-mono text-[13px] leading-6 text-slate-200 group-has-[#tfs-10-node:checked]/api:block focus-visible:outline-2 focus-visible:outline-tfs10-acc"><code><span class="text-tfs10-key">import</span> Sable <span class="text-tfs10-key">from</span> <span class="text-tfs10-str">'@sable/node'</span>;
<span class="text-tfs10-key">const</span> sable = <span class="text-tfs10-key">new</span> Sable(process.env.SABLE_KEY);
<span class="text-tfs10-key">const</span> res = <span class="text-tfs10-key">await</span> sable.verify({
  email: <span class="text-tfs10-str">'[email protected]'</span>, ip: <span class="text-tfs10-str">'81.2.69.142'</span>
});</code></pre>
        <pre tabindex="0" data-lang="py" class="hidden overflow-x-auto p-5 font-tfs10-mono text-[13px] leading-6 text-slate-200 group-has-[#tfs-10-py:checked]/api:block focus-visible:outline-2 focus-visible:outline-tfs10-acc"><code><span class="text-tfs10-key">import</span> sable
client = sable.Client()
res = client.verify(
    email=<span class="text-tfs10-str">"[email protected]"</span>, ip=<span class="text-tfs10-str">"81.2.69.142"</span>
)</code></pre>
      </div>
      <div class="overflow-hidden rounded-2xl bg-tfs10-code2 ring-1 ring-white/10 lg:ml-10">
        <div class="flex items-center justify-between border-b border-white/10 px-5 py-3"><span class="font-tfs10-mono text-xs text-slate-400">Response</span><span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-400/10 px-2.5 py-0.5 font-tfs10-mono text-[11px] font-semibold text-emerald-300"><span class="size-1.5 rounded-full bg-emerald-400"></span>200 OK · 84 ms</span></div>
        <pre tabindex="0" class="overflow-x-auto p-5 font-tfs10-mono text-[13px] leading-6 text-slate-300 focus-visible:outline-2 focus-visible:outline-tfs10-acc"><code>{
  <span class="text-tfs10-prop">"decision"</span>: <span class="text-tfs10-str">"approve"</span>,
  <span class="text-tfs10-prop">"risk_score"</span>: <span class="text-tfs10-num">0.04</span>,
  <span class="text-tfs10-prop">"signals"</span>: [<span class="text-tfs10-str">"email_age_7y"</span>, <span class="text-tfs10-str">"ip_residential"</span>]
}</code></pre>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs10-bg: #f8fafc;
  --color-tfs10-bg: oklch(0.984 0.003 248);
  --color-tfs10-ink: #0f172a;
  --color-tfs10-ink: oklch(0.208 0.04 266);
  --color-tfs10-mut: #475569;
  --color-tfs10-mut: oklch(0.446 0.037 257);
  --color-tfs10-acc: #e11d48;
  --color-tfs10-acc: oklch(0.586 0.222 18);
  --color-tfs10-code: #0b1020;
  --color-tfs10-code: oklch(0.177 0.034 270);
  --color-tfs10-code2: #111729;
  --color-tfs10-code2: oklch(0.209 0.037 269);
  --color-tfs10-key: #f472b6;
  --color-tfs10-key: oklch(0.725 0.175 350);
  --color-tfs10-str: #86efac;
  --color-tfs10-str: oklch(0.871 0.136 154);
  --color-tfs10-prop: #93c5fd;
  --color-tfs10-prop: oklch(0.809 0.096 252);
  --color-tfs10-num: #fcd34d;
  --color-tfs10-num: oklch(0.879 0.153 92);
  --font-tfs10-sans: 'Geist', system-ui, sans-serif;
  --font-tfs10-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-10 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const copyText = async (text) => {
    try { await navigator.clipboard.writeText(text); return true; }
    catch {
      const ta = Object.assign(document.createElement('textarea'), { value: text });
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;opacity:0';
      document.body.append(ta); ta.select();
      const ok = document.execCommand('copy'); ta.remove(); return ok;
    }
  };
  document.querySelectorAll('[data-tfs10]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const btn = root.querySelector('[data-copy]');
    const status = root.querySelector('[role="status"]');
    let t = 0;
    btn.addEventListener('click', async () => {
      const lang = root.querySelector('input[name="tfs-10-lang"]:checked').id.replace('tfs-10-', '');
      const ok = await copyText(root.querySelector('pre[data-lang="' + lang + '"]').textContent);
      clearTimeout(t);
      if (ok) { btn.setAttribute('data-copied', ''); status.textContent = 'Code copied to clipboard'; }
      else status.textContent = 'Copy failed';
      t = setTimeout(() => { btn.removeAttribute('data-copied'); status.textContent = ''; }, 1800);
    });
  });
})();
```

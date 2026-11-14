---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-500-internal-server-error-page/"
title: "Tailwind CSS 500 Internal Server Error Page"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A 500 page that treats the user as a colleague: a plain-English cause, a retry that actually replays, a copyable incident reference and a live recovery log."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS 500 Internal Server Error Page
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-500-internal-server-error-page/

A 500 page that treats the user as a colleague: a plain-English cause, a retry that actually replays, a copyable incident reference and a live recovery log. The giant 500 is outlined text with [-webkit-text-stroke]; the retry button's three states are data-busy: and data-done: variants.
## HTML
```html
<div class="tes-08 w-full min-h-svh bg-tes08-bg bg-[radial-gradient(60%_50%_at_20%_0%,color-mix(in_oklab,var(--color-tes08-acc)_14%,transparent),transparent)] font-tes08-sans text-tes08-ink antialiased [color-scheme:dark]">
  <header class="flex flex-wrap items-center gap-x-4 gap-y-2 border-b border-tes08-line px-[clamp(1rem,4vw,3rem)] py-4">
    <span class="font-semibold tracking-tight">Tideline</span>
    <span class="rounded-full border border-tes08-line2 px-2.5 py-1 font-tes08-mono text-[11px] text-tes08-mut">production · eu-west-1</span>
    <a href="#" class="ml-auto inline-flex min-h-11 items-center gap-2 text-sm text-tes08-mut hover:text-tes08-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes08-acc"><i aria-hidden="true" class="size-2 rounded-full bg-tes08-warn"></i>Status page</a>
  </header>
  <main class="mx-auto grid w-full max-w-6xl items-center gap-10 px-[clamp(1rem,4vw,3rem)] py-[clamp(2rem,7vw,5rem)] lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)]">
    <section aria-labelledby="tes08-h" class="grid justify-items-start gap-5">
      <p aria-hidden="true" class="font-tes08-sans text-[clamp(5rem,16vw,9.5rem)] leading-[0.85] font-semibold tracking-[-0.06em] text-transparent [-webkit-text-stroke:1.5px_var(--color-tes08-line2)]">500</p>
      <h1 id="tes08-h" class="text-[clamp(1.6rem,3.4vw,2.4rem)] leading-tight font-semibold tracking-tight text-balance">The request did not make it back</h1>
      <p id="tes08-p" class="max-w-[48ch] text-[15px]/7 text-tes08-mut text-pretty">Our edge accepted it, the upstream service did not answer in time. Nothing you sent has been lost — retry when you are ready.</p>
      <div class="flex flex-wrap gap-2.5 pt-1">
        <button type="button" id="tes08-retry" class="group/btn inline-flex min-h-11 items-center gap-2 rounded-xl bg-tes08-ink px-5 text-sm font-medium text-tes08-bg transition hover:bg-white active:scale-[.98] data-busy:pointer-events-none data-busy:bg-tes08-panel2 data-busy:text-tes08-ink data-done:bg-tes08-ok data-done:text-tes08-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes08-acc"><span aria-hidden="true" class="hidden size-4 animate-spin rounded-full border-2 border-current border-r-transparent group-data-busy/btn:block motion-reduce:animate-none"></span><span id="tes08-rl">Retry request</span></button>
        <button type="button" id="tes08-copy" class="min-h-11 rounded-xl border border-tes08-line2 px-4 text-sm transition hover:bg-tes08-panel2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes08-acc">Copy incident reference</button>
      </div>
      <p id="tes08-said" role="status" class="min-h-5 text-xs text-tes08-ok"></p>
      <dl class="grid w-full max-w-lg grid-cols-3 gap-px overflow-hidden rounded-xl border border-tes08-line bg-tes08-line text-xs">
        <div class="grid gap-1 bg-tes08-panel p-3"><dt class="text-tes08-mut">Reference</dt><dd class="truncate font-tes08-mono">req_9f2c41ba8e</dd></div>
        <div class="grid gap-1 bg-tes08-panel p-3"><dt class="text-tes08-mut">Region</dt><dd class="font-tes08-mono">eu-west-1b</dd></div>
        <div class="grid gap-1 bg-tes08-panel p-3"><dt class="text-tes08-mut">Time</dt><dd id="tes08-time" class="font-tes08-mono">14:02:11 UTC</dd></div>
      </dl>
    </section>
    <aside aria-label="Recovery log" class="overflow-hidden rounded-2xl border border-tes08-line bg-tes08-panel shadow-[0_40px_80px_-40px_rgb(0_0_0/0.7)]">
      <div class="flex items-center gap-2 border-b border-tes08-line px-4 py-3">
        <span aria-hidden="true" class="flex gap-1.5"><i class="size-2.5 rounded-full bg-tes08-line2"></i><i class="size-2.5 rounded-full bg-tes08-line2"></i><i class="size-2.5 rounded-full bg-tes08-line2"></i></span>
        <span class="ml-2 font-tes08-mono text-xs text-tes08-mut">recovery log</span>
        <span id="tes08-state" class="ml-auto rounded-full bg-tes08-warn/15 px-2 py-0.5 font-tes08-mono text-[11px] text-tes08-warn">idle</span>
      </div>
      <div aria-hidden="true" class="relative h-0.5 overflow-hidden bg-tes08-line"><span id="tes08-prog" hidden class="absolute inset-y-0 w-1/3 animate-tes08-scan bg-tes08-acc motion-reduce:animate-none"></span></div>
      <ol id="tes08-lines" class="grid gap-2 p-4 font-tes08-mono text-[12.5px]/5 text-tes08-mut">
        <li class="flex gap-3"><span class="text-tes08-faint">14:02:09</span><span>POST /v2/ledger/settle → <b class="font-medium text-tes08-err">upstream timeout</b></span></li>
        <li class="flex gap-3"><span class="text-tes08-faint">14:02:10</span><span>circuit breaker opened for ledger-api</span></li>
        <li class="flex gap-3"><span class="text-tes08-faint">14:02:11</span><span>request queued for replay</span></li>
      </ol>
    </aside>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes08-bg: #0c0e12;
  --color-tes08-bg: oklch(0.15 0.01 255);
  --color-tes08-panel: #12151b;
  --color-tes08-panel: oklch(0.19 0.012 255);
  --color-tes08-panel2: #1a1e26;
  --color-tes08-panel2: oklch(0.23 0.014 255);
  --color-tes08-line: #232831;
  --color-tes08-line: oklch(0.275 0.014 255);
  --color-tes08-line2: #3a414e;
  --color-tes08-line2: oklch(0.37 0.018 255);
  --color-tes08-ink: #eef1f6;
  --color-tes08-ink: oklch(0.96 0.006 255);
  --color-tes08-mut: #a3abba;
  --color-tes08-mut: oklch(0.74 0.02 255);
  --color-tes08-faint: #7b8494;
  --color-tes08-faint: oklch(0.62 0.02 255);
  --color-tes08-acc: #64b5ff;
  --color-tes08-acc: oklch(0.75 0.13 245);
  --color-tes08-ok: #5ee0a0;
  --color-tes08-ok: oklch(0.83 0.15 160);
  --color-tes08-warn: #f2b45a;
  --color-tes08-warn: oklch(0.81 0.12 72);
  --color-tes08-err: #ff8a7a;
  --color-tes08-err: oklch(0.76 0.14 28);
  --font-tes08-sans: 'Geist', system-ui, sans-serif;
  --font-tes08-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tes08-scan: tes08-scan 1.1s cubic-bezier(0.4,0,0.2,1) infinite;

  @keyframes tes08-scan {
    from {
      translate: -100% 0;
    }

    to {
      translate: 300% 0;
    }
  }
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-08 {
  width: 100%;
  min-height: 100svh;
}

.tes-08 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-08');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const $ = (s) => root.querySelector(s);
  const retry = $('#tes08-retry'), lines = $('#tes08-lines'), state = $('#tes08-state');
  const stamp = () => new Date().toISOString().slice(11, 19);
  const line = (html) => {
    const li = document.createElement('li');
    li.className = 'flex gap-3 transition-[opacity,translate] duration-300 starting:-translate-x-1 starting:opacity-0';
    li.innerHTML = '<span class="text-tes08-faint">' + stamp() + '</span><span>' + html + '</span>';
    lines.appendChild(li);
  };
  $('#tes08-time').textContent = stamp() + ' UTC';
  retry.addEventListener('click', () => {
    if (retry.hasAttribute('data-busy') || retry.hasAttribute('data-done')) return;
    retry.setAttribute('data-busy', ''); $('#tes08-rl').textContent = 'Retrying';
    $('#tes08-prog').hidden = false; state.textContent = 'replaying';
    line('replaying req_9f2c41ba8e');
    setTimeout(() => line('ledger-api handshake ok'), 700);
    setTimeout(() => {
      line('<b class="font-medium text-tes08-ok">settled \u2014 200 OK</b>');
      $('#tes08-prog').hidden = true;
      state.textContent = 'recovered'; state.className = 'ml-auto rounded-full bg-tes08-ok/15 px-2 py-0.5 font-tes08-mono text-[11px] text-tes08-ok';
      retry.removeAttribute('data-busy'); retry.setAttribute('data-done', ''); $('#tes08-rl').textContent = 'Request completed';
      $('#tes08-h').textContent = 'It went through this time';
      $('#tes08-p').textContent = 'The replay settled against the ledger. You can carry on where you left off.';
    }, 1600);
  });
  $('#tes08-copy').addEventListener('click', () => {
    const ref = 'req_9f2c41ba8e';
    const said = $('#tes08-said');
    const fallback = () => {
      const t = document.createElement('textarea'); t.value = ref; document.body.appendChild(t); t.select();
      let ok = false; try { ok = document.execCommand('copy'); } catch (e) {}
      t.remove(); said.textContent = ok ? 'Reference copied.' : 'Copy blocked \u2014 the reference is ' + ref;
    };
    if (navigator.clipboard) navigator.clipboard.writeText(ref).then(() => { said.textContent = 'Reference copied.'; }, fallback);
    else fallback();
  });
})();
```

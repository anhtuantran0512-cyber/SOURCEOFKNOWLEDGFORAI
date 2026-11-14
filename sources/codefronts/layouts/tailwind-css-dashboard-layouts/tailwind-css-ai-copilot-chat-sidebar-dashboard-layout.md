---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-ai-copilot-chat-sidebar-dashboard-layout/"
title: "Tailwind CSS AI Copilot Chat Sidebar Dashboard Layout"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "Your data on the left, a resident AI copilot docked on the right."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS AI Copilot Chat Sidebar Dashboard Layout
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-ai-copilot-chat-sidebar-dashboard-layout/

Your data on the left, a resident AI copilot docked on the right. The panel folds by animating grid-cols-[minmax(0,1fr)_21.25rem] to group-data-closed/split:grid-cols-[minmax(0,1fr)_0rem], so the dashboard reflows in the same motion. New in the port: the copilot actually talks &mdash; the pending answer streams in word by word, suggestion chips and the composer send real messages, and Esc closes the panel.
## HTML
```html
<section class="tdl-13 @container/s w-full min-h-svh bg-tdl13-bg font-tdl13-sans text-tdl13-ink antialiased" aria-label="AI copilot split dashboard demo">
  <div data-split class="group/split grid h-svh min-h-[34rem] grid-cols-[minmax(0,1fr)_21.25rem] overflow-hidden transition-[grid-template-columns] duration-350 ease-[cubic-bezier(.2,.7,.2,1)] group-data-closed/split:grid-cols-[minmax(0,1fr)_0rem] @max-[44rem]/s:grid-cols-[minmax(0,1fr)_17.5rem]">
    <div class="flex min-w-0 flex-col">
      <header class="flex h-15 flex-none items-center justify-between gap-3 border-b border-tdl13-edge bg-tdl13-panel px-4">
        <strong class="flex min-w-0 items-center gap-2.5 truncate text-[15px] font-semibold"><span aria-hidden="true" class="size-5 flex-none rounded-md bg-[conic-gradient(from_210deg,var(--color-tdl13-ai),var(--color-tdl13-ai2),var(--color-tdl13-ai))]"></span>Margin — Q3 board</strong>
        <button data-ask type="button" aria-expanded="true" aria-controls="tdl13-panel" class="flex h-10 flex-none items-center gap-2 rounded-full border border-tdl13-ai/40 bg-linear-120 from-tdl13-ai/10 to-tdl13-ai2/10 px-4 text-[13px] font-semibold text-tdl13-aiink transition hover:-translate-y-px hover:shadow-[0_6px_18px_-8px_var(--color-tdl13-ai)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl13-ai"><i aria-hidden="true" class="size-3.5 rounded-full bg-[conic-gradient(from_var(--tdl13-spin),var(--color-tdl13-ai),var(--color-tdl13-ai2),var(--color-tdl13-ai))] animate-tdl13-spin"></i>Copilot<kbd class="rounded border border-tdl13-ai/30 px-1 font-sans text-[10px] text-tdl13-aiink/80 @max-[44rem]/s:hidden">⌘J</kbd></button>
      </header>
      <div class="grid min-h-0 flex-1 auto-rows-min grid-cols-[repeat(auto-fit,minmax(min(10.5rem,100%),1fr))] gap-3 overflow-y-auto overscroll-contain p-4 [&>article]:rounded-2xl [&>article]:border [&>article]:border-tdl13-edge [&>article]:bg-tdl13-panel [&>article]:px-4.5 [&>article]:py-4 [&_h3]:text-[10.5px] [&_h3]:font-bold [&_h3]:tracking-[0.1em] [&_h3]:text-tdl13-mut [&_h3]:uppercase">
        <article><h3>Gross margin</h3><p class="mt-1.5 mb-0.5 text-[24px] font-bold tabular-nums">61.4%</p><small class="text-[11.5px] font-semibold text-tdl13-good">▲ 2.1 pts QoQ</small></article>
        <article><h3>Burn multiple</h3><p class="mt-1.5 mb-0.5 text-[24px] font-bold tabular-nums">1.3×</p><small class="text-[11.5px] font-semibold text-tdl13-good">improving</small></article>
        <article><h3>Net revenue retention</h3><p class="mt-1.5 mb-0.5 text-[24px] font-bold tabular-nums">117%</p><small class="text-[11.5px] font-semibold text-tdl13-mut">flat QoQ</small></article>
        <article class="col-span-full"><h3 class="flex flex-wrap items-center justify-between gap-2">Revenue vs. cost<span class="flex gap-3 tracking-normal normal-case"><span class="flex items-center gap-1.5"><i aria-hidden="true" class="size-2.5 rounded-[3px] bg-tdl13-ai"></i>Revenue</span><span class="flex items-center gap-1.5"><i aria-hidden="true" class="size-2.5 rounded-[3px] bg-tdl13-ai2/55"></i>Cost</span></span></h3>
          <div aria-hidden="true" class="mt-3 flex h-28 items-end gap-2.25 *:relative *:h-full *:flex-1 *:before:absolute *:before:bottom-0 *:before:left-0 *:before:h-(--a) *:before:w-[52%] *:before:rounded-t-[3px] *:before:bg-tdl13-ai *:before:content-[''] *:after:absolute *:after:right-0 *:after:bottom-0 *:after:h-(--b) *:after:w-[34%] *:after:rounded-t-[3px] *:after:bg-tdl13-ai2/55 *:after:content-['']"><i style="--a:46%;--b:30%"></i><i style="--a:52%;--b:33%"></i><i style="--a:49%;--b:35%"></i><i style="--a:61%;--b:36%"></i><i style="--a:66%;--b:38%"></i><i style="--a:74%;--b:39%"></i><i style="--a:82%;--b:41%"></i><i style="--a:90%;--b:42%"></i></div>
        </article>
      </div>
    </div>
    <aside id="tdl13-panel" aria-label="AI copilot" class="min-w-0 overflow-hidden border-l border-tdl13-edge bg-tdl13-panel transition-[visibility] group-data-closed/split:invisible group-data-closed/split:delay-350">
      <div class="flex h-full w-85 flex-col @max-[44rem]/s:w-70">
        <header class="flex items-center gap-2.5 border-b border-tdl13-edge px-4 py-3.5"><span aria-hidden="true" class="size-8 rounded-full bg-[conic-gradient(from_var(--tdl13-spin),var(--color-tdl13-ai),var(--color-tdl13-ai2),var(--color-tdl13-ai3),var(--color-tdl13-ai))] shadow-[inset_0_0_0_3px_var(--color-tdl13-panel)] animate-tdl13-spin-slow"></span><div><b class="block text-sm">Copilot</b><small class="text-[11.5px] text-tdl13-mut">grounded in this board</small></div><button data-close type="button" aria-label="Close copilot" class="ml-auto grid size-9 place-items-center rounded-lg text-tdl13-mut transition-colors hover:bg-tdl13-bg hover:text-tdl13-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl13-ai"><svg viewBox="0 0 24 24" class="size-4 fill-none stroke-current stroke-2 [stroke-linecap:round]" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button></header>
        <div data-thread role="log" aria-live="polite" class="flex min-h-0 flex-1 flex-col gap-3 overflow-y-auto overscroll-contain p-4 text-[13px]/[1.5] [&_.q]:max-w-[85%] [&_.q]:self-end [&_.q]:rounded-[13px_13px_4px_13px] [&_.q]:bg-tdl13-q [&_.q]:px-3.25 [&_.q]:py-2.25 [&_.q]:starting:translate-y-1 [&_.q]:starting:opacity-0 [&_.q]:transition [&_.a]:max-w-[92%] [&_.a]:rounded-[4px_13px_13px_13px] [&_.a]:border-[1.5px] [&_.a]:border-transparent [&_.a]:bg-[linear-gradient(var(--color-tdl13-panel),var(--color-tdl13-panel))_padding-box,linear-gradient(130deg,var(--color-tdl13-ai),var(--color-tdl13-ai2))_border-box] [&_.a]:px-3.5 [&_.a]:py-2.75 [&_.a]:starting:translate-y-1 [&_.a]:starting:opacity-0 [&_.a]:transition [&_.a_b]:text-tdl13-aiink">
          <p class="q">Why did gross margin jump this quarter?</p>
          <div class="a"><p>Two drivers: hosting costs fell <b>9%</b> after the CDN renegotiation, and the Pro tier (72% margin) grew to <b>44%</b> of revenue mix — worth ~1.6 of the 2.1 point gain.</p></div>
          <p class="q">Draft a one-line summary for the board deck.</p>
          <div class="a" data-pending="Q3 gross margin rose 2.1 pts to 61.4%, driven by lower hosting costs and a richer Pro-tier mix."><span class="flex min-h-5 items-center gap-1.25 *:size-1.5 *:rounded-full *:bg-tdl13-ai *:animate-tdl13-think" aria-hidden="true"><i></i><i style="animation-delay:.15s"></i><i style="animation-delay:.3s"></i></span><span class="sr-only">Copilot is typing</span></div>
        </div>
        <div class="flex flex-wrap gap-2 px-4 pb-3 [&>button]:h-8.5 [&>button]:cursor-pointer [&>button]:rounded-full [&>button]:border [&>button]:border-tdl13-edge [&>button]:bg-tdl13-bg [&>button]:px-3 [&>button]:text-xs [&>button]:font-semibold [&>button]:text-tdl13-mut [&>button]:transition [&>button:hover]:border-tdl13-ai/50 [&>button:hover]:text-tdl13-aiink [&>button:focus-visible]:outline-2 [&>button:focus-visible]:outline-offset-2 [&>button:focus-visible]:outline-tdl13-ai">
          <button type="button" data-chip>Explain NRR risk</button><button type="button" data-chip>Forecast Q4 margin</button>
        </div>
        <form data-form class="mx-4 mb-4 flex items-end gap-2 rounded-xl border border-tdl13-edge bg-tdl13-bg p-1.75 pl-3.5 transition focus-within:border-tdl13-ai focus-within:ring-3 focus-within:ring-tdl13-ai/15"><label for="tdl13-in" class="sr-only">Ask about this board</label><textarea id="tdl13-in" rows="1" placeholder="Ask about this board…" class="field-sizing-content max-h-28 min-h-9 flex-1 resize-none bg-transparent py-2 text-[13px] outline-none placeholder:text-tdl13-mut"></textarea><button type="submit" aria-label="Send" class="grid size-9 flex-none place-items-center rounded-lg bg-linear-130 from-tdl13-ai to-tdl13-ai2 text-white transition hover:scale-105 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdl13-ai"><svg viewBox="0 0 24 24" class="size-4 fill-none stroke-current stroke-[2.4] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg></button></form>
      </div>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl13-bg: #f8f7fb;
  --color-tdl13-bg: oklch(0.975 0.005 300);
  --color-tdl13-panel: #ffffff;
  --color-tdl13-panel: oklch(1 0 0);
  --color-tdl13-q: #efedf4;
  --color-tdl13-q: oklch(0.945 0.01 300);
  --color-tdl13-edge: #e3e0ea;
  --color-tdl13-edge: oklch(0.905 0.012 300);
  --color-tdl13-ink: #29243a;
  --color-tdl13-ink: oklch(0.27 0.025 300);
  --color-tdl13-mut: #5f5a6d;
  --color-tdl13-mut: oklch(0.49 0.025 300);
  --color-tdl13-ai: #9a48e0;
  --color-tdl13-ai: oklch(0.58 0.2 305);
  --color-tdl13-aiink: #6a24a8;
  --color-tdl13-aiink: oklch(0.45 0.18 305);
  --color-tdl13-ai2: #3ea6dc;
  --color-tdl13-ai2: oklch(0.69 0.13 230);
  --color-tdl13-ai3: #ee8fb4;
  --color-tdl13-ai3: oklch(0.76 0.12 355);
  --color-tdl13-good: #17804a;
  --color-tdl13-good: oklch(0.52 0.13 155);
  --font-tdl13-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --animate-tdl13-spin: tdl13-spin 6s linear infinite;
  --animate-tdl13-spin-slow: tdl13-spin 9s linear infinite;
  --animate-tdl13-think: tdl13-think 1.2s infinite;

  @keyframes tdl13-spin {
    to {
      --tdl13-spin: 570deg;
    }
  }

  @keyframes tdl13-think {
    0%,
        60%,
        100% {
      translate: 0 0;
      opacity: .4;
    }

    30% {
      translate: 0 -4px;
      opacity: 1;
    }
  }
}
/* At-rule: an angle only animates once it is registered. */

@property --tdl13-spin {
  syntax: "<angle>";
  inherits: false;
  initial-value: 210deg;
}

.tdl-13 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-13 * {
    animation: none !important;
    transition-duration: 0.01s !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tdl-13 [data-split]').forEach((split) => {
    if (split.dataset.bound) return; split.dataset.bound = '1';
    const ask = split.querySelector('[data-ask]');
    const thread = split.querySelector('[data-thread]');
    const input = split.querySelector('textarea');
    const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const answers = {
      'explain nrr risk': 'NRR is flat at 117%, but two enterprise accounts (11% of ARR) renew in Q4 without expansion plans. Losing one would pull NRR to ~111%.',
      'forecast q4 margin': 'If the Pro mix holds at 44% and hosting stays flat, Q4 gross margin lands at <b>62.0–62.6%</b>.'
    };
    const set = (open) => { split.toggleAttribute('data-closed', !open); ask.setAttribute('aria-expanded', String(open)); if (open) setTimeout(() => input.focus(), 360); else ask.focus(); };
    const bottom = () => { thread.scrollTop = thread.scrollHeight; };
    const stream = (bubble, html) => {
      if (calm) { bubble.innerHTML = '<p>' + html + '</p>'; bottom(); return; }
      const words = html.split(' '); let i = 0; bubble.innerHTML = '<p></p>'; const p = bubble.firstChild;
      const t = setInterval(() => { p.innerHTML = words.slice(0, ++i).join(' '); bottom(); if (i >= words.length) clearInterval(t); }, 45);
    };
    const reply = (text) => {
      const a = document.createElement('div'); a.className = 'a';
      a.innerHTML = '<span class="flex min-h-5 items-center gap-1.25 *:size-1.5 *:rounded-full *:bg-tdl13-ai *:animate-tdl13-think" aria-hidden="true"><i></i><i style="animation-delay:.15s"></i><i style="animation-delay:.3s"></i></span>';
      thread.appendChild(a); bottom();
      setTimeout(() => stream(a, answers[text.toLowerCase()] || 'Good question — based on this board, I would start with the margin bridge: hosting savings and tier mix explain most of the movement.'), 900);
    };
    const send = (text) => {
      text = text.trim(); if (!text) return;
      const q = document.createElement('p'); q.className = 'q'; q.textContent = text; thread.appendChild(q);
      input.value = ''; bottom(); reply(text);
    };
    const pending = thread.querySelector('[data-pending]');
    if (pending) setTimeout(() => stream(pending, pending.dataset.pending), 1400);
    ask.addEventListener('click', () => set(split.hasAttribute('data-closed')));
    split.querySelector('[data-close]').addEventListener('click', () => set(false));
    split.querySelector('[data-form]').addEventListener('submit', (e) => { e.preventDefault(); send(input.value); });
    input.addEventListener('keydown', (e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(input.value); } });
    split.querySelectorAll('[data-chip]').forEach((c) => c.addEventListener('click', () => send(c.textContent)));
    split.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !split.hasAttribute('data-closed')) set(false); });
    document.addEventListener('keydown', (e) => { if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'j') { e.preventDefault(); set(split.hasAttribute('data-closed')); } });
  });
})();
```

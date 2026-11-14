---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-support-ticket-form-file-upload/"
title: "Tailwind Support Ticket Form with File Upload"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's help-desk ticket form, ported one-for-one to Tailwind v4: a focused dark developer-tool look, priority as a colour-coded segmented…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Support Ticket Form with File Upload
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-support-ticket-form-file-upload/

The CSS collection's help-desk ticket form, ported one-for-one to Tailwind v4: a focused dark developer-tool look, priority as a colour-coded segmented control (Urgent reveals an on-call warning), category, environment and subject fields, a description with markdown hints, and a drag-and-drop zone that is a real <input type="file" multiple> underneath — with per-file progress, image thumbnails, size and count limits, remove buttons and a ⌘↵ shortcut.
## HTML
```html
<div class="tf-06 relative block min-h-svh w-full [background:radial-gradient(70rem_36rem_at_50%_-15%,color-mix(in_oklab,var(--color-tf06-accent)_14%,transparent),transparent_70%),var(--color-tf06-bg)] pt-[72px] font-tf06-sans leading-[normal] text-tf06-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,5vw,4rem)]">
    <div class="grid w-full max-w-[42rem] gap-5 rounded-[1.25rem] border border-tf06-line bg-tf06-surface p-[clamp(1.25rem,5vw,2.25rem)] shadow-[inset_0_0_0_1px_rgba(255,255,255,.02),0_40px_80px_-40px_rgba(0,0,0,.8)]" role="form" aria-labelledby="tf-06-title">
      <header class="flex flex-wrap items-end justify-between gap-[.8rem] border-b border-tf06-line pb-[1.1rem]">
        <div><p class="mb-[.3rem] font-tf06-mono text-[.78rem] text-tf06-muted">Support / New ticket</p><h2 id="tf-06-title" class="text-[1.45rem] font-semibold tracking-[-.02em]">Open a support ticket</h2></div>
        <span class="inline-flex items-center gap-2 rounded-full border border-tf06-line px-[.65rem] py-[.35rem] font-tf06-mono text-[.78rem] text-tf06-muted"><i aria-hidden="true" class="size-2 animate-tf06-live rounded-full bg-tf06-ok shadow-[0_0_0_0_var(--color-tf06-ok)]"></i>Median first reply: 38 min</span>
      </header>
      <fieldset class="group/p grid gap-[.55rem]">
        <legend class="mb-[.55rem] text-[.82rem] font-medium text-tf06-ink">Priority</legend>
        <div class="grid grid-cols-4 gap-1 rounded-[.8rem] border border-tf06-line bg-tf06-raised p-1">
          <label style="--dot:#64748b" class="group/s relative text-[.82rem] font-medium text-tf06-ink"><input type="radio" name="tf-06-p" value="low" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="flex min-h-[2.6rem] items-center justify-center gap-[.45rem] rounded-[.6rem] text-[.88rem] text-tf06-muted [transition:background_.2s,color_.2s] before:size-2 before:rounded-full before:bg-[var(--dot)] before:opacity-60 before:content-[''] group-hover/s:text-tf06-ink peer-checked:bg-[color-mix(in_oklab,var(--dot)_18%,var(--color-tf06-surface))] peer-checked:text-tf06-ink peer-checked:shadow-[inset_0_0_0_1px_color-mix(in_oklab,var(--dot)_55%,transparent)] peer-checked:before:opacity-100 peer-checked:before:shadow-[0_0_10px_var(--dot)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-1 peer-focus-visible:outline-tf06-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Low</span></label>
          <label style="--dot:#38bdf8" class="group/s relative text-[.82rem] font-medium text-tf06-ink"><input type="radio" name="tf-06-p" value="normal" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="flex min-h-[2.6rem] items-center justify-center gap-[.45rem] rounded-[.6rem] text-[.88rem] text-tf06-muted [transition:background_.2s,color_.2s] before:size-2 before:rounded-full before:bg-[var(--dot)] before:opacity-60 before:content-[''] group-hover/s:text-tf06-ink peer-checked:bg-[color-mix(in_oklab,var(--dot)_18%,var(--color-tf06-surface))] peer-checked:text-tf06-ink peer-checked:shadow-[inset_0_0_0_1px_color-mix(in_oklab,var(--dot)_55%,transparent)] peer-checked:before:opacity-100 peer-checked:before:shadow-[0_0_10px_var(--dot)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-1 peer-focus-visible:outline-tf06-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Normal</span></label>
          <label style="--dot:#f59e0b" class="group/s relative text-[.82rem] font-medium text-tf06-ink"><input type="radio" name="tf-06-p" value="high" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="flex min-h-[2.6rem] items-center justify-center gap-[.45rem] rounded-[.6rem] text-[.88rem] text-tf06-muted [transition:background_.2s,color_.2s] before:size-2 before:rounded-full before:bg-[var(--dot)] before:opacity-60 before:content-[''] group-hover/s:text-tf06-ink peer-checked:bg-[color-mix(in_oklab,var(--dot)_18%,var(--color-tf06-surface))] peer-checked:text-tf06-ink peer-checked:shadow-[inset_0_0_0_1px_color-mix(in_oklab,var(--dot)_55%,transparent)] peer-checked:before:opacity-100 peer-checked:before:shadow-[0_0_10px_var(--dot)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-1 peer-focus-visible:outline-tf06-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">High</span></label>
          <label style="--dot:#f43f5e" class="group/s relative text-[.82rem] font-medium text-tf06-ink"><input type="radio" name="tf-06-p" value="urgent" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="flex min-h-[2.6rem] items-center justify-center gap-[.45rem] rounded-[.6rem] text-[.88rem] text-tf06-muted [transition:background_.2s,color_.2s] before:size-2 before:rounded-full before:bg-[var(--dot)] before:opacity-60 before:content-[''] group-hover/s:text-tf06-ink peer-checked:bg-[color-mix(in_oklab,var(--dot)_18%,var(--color-tf06-surface))] peer-checked:text-tf06-ink peer-checked:shadow-[inset_0_0_0_1px_color-mix(in_oklab,var(--dot)_55%,transparent)] peer-checked:before:opacity-100 peer-checked:before:shadow-[0_0_10px_var(--dot)] peer-focus-visible:outline-2 peer-focus-visible:outline-offset-1 peer-focus-visible:outline-tf06-accent forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Urgent</span></label>
        </div>
        <p class="hidden text-[.78rem] text-[#fda4af] in-data-[theme=light]:text-tf06-bad group-has-[[value=urgent]:checked]/p:block group-has-[[value=urgent]:checked]/p:animate-tf06-in">Urgent = production is down or data is at risk. We'll page the on-call engineer.</p>
      </fieldset>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] gap-4">
        <div class="grid gap-[.45rem]"><label for="tf-06-cat" class="text-[.82rem] font-medium text-tf06-ink">Category</label>
          <select id="tf-06-cat" class="min-h-[2.9rem] w-full rounded-[.65rem] border border-tf06-line bg-tf06-raised px-[.85rem] py-[.65rem] text-[.95rem] text-tf06-ink [transition:border-color_.2s,box-shadow_.2s] placeholder:text-tf06-muted/70 focus-visible:border-tf06-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf06-accent)_25%,transparent)] focus-visible:outline-none user-invalid:border-tf06-bad cursor-pointer appearance-none bg-[image:var(--tf06-chevron)] bg-[length:1.1rem] bg-[position:right_.7rem_center] bg-no-repeat pr-[2.4rem]"><option>Billing</option><option selected>Bug report</option><option>Integration / API</option><option>Account access</option><option>Feature request</option></select></div>
        <div class="grid gap-[.45rem]"><label for="tf-06-env" class="text-[.82rem] font-medium text-tf06-ink">Environment</label>
          <select id="tf-06-env" class="min-h-[2.9rem] w-full rounded-[.65rem] border border-tf06-line bg-tf06-raised px-[.85rem] py-[.65rem] text-[.95rem] text-tf06-ink [transition:border-color_.2s,box-shadow_.2s] placeholder:text-tf06-muted/70 focus-visible:border-tf06-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf06-accent)_25%,transparent)] focus-visible:outline-none user-invalid:border-tf06-bad cursor-pointer appearance-none bg-[image:var(--tf06-chevron)] bg-[length:1.1rem] bg-[position:right_.7rem_center] bg-no-repeat pr-[2.4rem]"><option>Production</option><option>Staging</option><option>Local</option></select></div>
      </div>
      <div class="grid gap-[.45rem]"><label for="tf-06-subj" class="text-[.82rem] font-medium text-tf06-ink">Subject</label><input id="tf-06-subj" type="text" required placeholder="Webhook retries failing with 502 after deploy" class="min-h-[2.9rem] w-full rounded-[.65rem] border border-tf06-line bg-tf06-raised px-[.85rem] py-[.65rem] text-[.95rem] text-tf06-ink [transition:border-color_.2s,box-shadow_.2s] placeholder:text-tf06-muted/70 focus-visible:border-tf06-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf06-accent)_25%,transparent)] focus-visible:outline-none user-invalid:border-tf06-bad"></div>
      <div class="grid gap-[.45rem]"><label for="tf-06-desc" class="text-[.82rem] font-medium text-tf06-ink">Description</label>
        <textarea id="tf-06-desc" required placeholder="Steps to reproduce, expected vs actual result, request IDs…" aria-describedby="tf-06-md" class="min-h-[2.9rem] w-full rounded-[.65rem] border border-tf06-line bg-tf06-raised px-[.85rem] py-[.65rem] text-[.95rem] text-tf06-ink [transition:border-color_.2s,box-shadow_.2s] placeholder:text-tf06-muted/70 focus-visible:border-tf06-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf06-accent)_25%,transparent)] focus-visible:outline-none user-invalid:border-tf06-bad max-h-[18rem] min-h-32! resize-y leading-[1.55] [field-sizing:content]"></textarea>
        <p class="text-[.78rem] text-tf06-muted [&_code]:rounded-[.3rem] [&_code]:border [&_code]:border-tf06-line [&_code]:bg-tf06-raised [&_code]:px-[.35rem] [&_code]:py-[.1rem] [&_code]:font-tf06-mono [&_code]:text-[.74rem]" id="tf-06-md">Markdown supported: <code>**bold**</code> <code>&#96;code&#96;</code> <code>- list</code></p></div>
      <div class="grid gap-[.45rem]">
        <span class="text-[.82rem] font-medium text-tf06-ink" id="tf-06-att-label">Attachments</span>
        <label class="tf-06__drop relative grid cursor-pointer justify-items-center gap-[.4rem] rounded-[.9rem] border-[1.5px] border-dashed border-tf06-muted/45 bg-tf06-raised px-4 py-[1.6rem] text-center [transition:border-color_.2s,background_.25s] focus-within:outline-2 focus-within:outline-offset-3 focus-within:outline-tf06-accent hover:border-tf06-muted forced-colors:border-[CanvasText] [&.is-over]:border-solid [&.is-over]:border-tf06-accent [&.is-over]:bg-[color-mix(in_oklab,var(--color-tf06-accent)_10%,var(--color-tf06-raised))] text-[.82rem] font-medium text-tf06-ink">
          <input type="file" multiple accept="image/*,.pdf,.txt,.log,.json,.har,.zip" aria-labelledby="tf-06-att-label" aria-describedby="tf-06-att-hint" class="absolute inset-0 w-full cursor-pointer opacity-0">
          <span class="grid size-11 place-items-center rounded-[.8rem] border border-tf06-line bg-tf06-surface [transition:translate_.35s_var(--ease-tf06)] in-[.is-over]:-translate-y-1" aria-hidden="true"><svg viewBox="0 0 24 24" class="size-[1.3rem] fill-none stroke-tf06-accent stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 15v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/></svg></span>
          <span class="text-[.95rem]"><b>Drop files here</b> or <u class="text-tf06-accent underline-offset-3">browse</u></span>
          <span class="text-[.78rem] text-tf06-muted" id="tf-06-att-hint">Screenshots, logs, HAR or PDF · up to 5 files · 10 MB each</span>
        </label>
        <ul class="tf-06__files grid list-none gap-[.45rem] *:grid *:animate-tf06-in *:grid-cols-[auto_minmax(0,1fr)_auto] *:items-center *:gap-3 *:rounded-[.75rem] *:border *:border-tf06-line *:bg-tf06-raised *:py-[.55rem] *:pr-[.6rem] *:pl-[.55rem] [&_.tf-06\_\_thumb]:grid [&_.tf-06\_\_thumb]:size-10 [&_.tf-06\_\_thumb]:place-items-center [&_.tf-06\_\_thumb]:rounded-[.5rem] [&_.tf-06\_\_thumb]:border [&_.tf-06\_\_thumb]:border-tf06-line [&_.tf-06\_\_thumb]:bg-tf06-surface [&_.tf-06\_\_thumb]:object-cover [&_.tf-06\_\_thumb]:font-tf06-mono [&_.tf-06\_\_thumb]:text-[.62rem] [&_.tf-06\_\_thumb]:font-medium [&_.tf-06\_\_thumb]:text-tf06-muted [&_.tf-06\_\_thumb]:uppercase [&_.tf-06\_\_meta]:grid [&_.tf-06\_\_meta]:min-w-0 [&_.tf-06\_\_meta]:gap-[.3rem] [&_b]:truncate [&_b]:text-[.88rem] [&_b]:font-medium [&_small]:font-tf06-mono [&_small]:text-[.72rem] [&_small]:text-tf06-muted [&_.tf-06\_\_track]:h-1 [&_.tf-06\_\_track]:overflow-hidden [&_.tf-06\_\_track]:rounded-full [&_.tf-06\_\_track]:bg-tf06-line [&_.tf-06\_\_bar]:block [&_.tf-06\_\_bar]:h-full [&_.tf-06\_\_bar]:origin-left [&_.tf-06\_\_bar]:bg-tf06-accent [&_.tf-06\_\_bar]:[scale:var(--p,0)_1] [&_.tf-06\_\_bar]:[transition:scale_.2s_linear] [&_.is-done_.tf-06\_\_bar]:bg-tf06-ok forced-colors:[&_.tf-06\_\_bar]:bg-[Highlight] [&_.tf-06\_\_rm]:grid [&_.tf-06\_\_rm]:size-9 [&_.tf-06\_\_rm]:cursor-pointer [&_.tf-06\_\_rm]:place-items-center [&_.tf-06\_\_rm]:rounded-[.55rem] [&_.tf-06\_\_rm]:border-0 [&_.tf-06\_\_rm]:bg-transparent [&_.tf-06\_\_rm]:text-tf06-muted [&_.tf-06\_\_rm:hover]:bg-tf06-bad/15 [&_.tf-06\_\_rm:hover]:text-tf06-bad [&_.tf-06\_\_rm:focus-visible]:outline-2 [&_.tf-06\_\_rm:focus-visible]:outline-tf06-accent [&_.tf-06\_\_rm_svg]:size-4 [&_.tf-06\_\_rm_svg]:fill-none [&_.tf-06\_\_rm_svg]:stroke-current [&_.tf-06\_\_rm_svg]:stroke-2 [&_.tf-06\_\_rm_svg]:[stroke-linecap:round]" aria-label="Attached files"></ul>
        <p class="sr-only" aria-live="polite" id="tf-06-live"></p>
      </div>
      <footer class="flex flex-wrap items-center justify-between gap-4 border-t border-tf06-line pt-[1.1rem]">
        <label class="flex min-h-11 cursor-pointer items-center gap-[.55rem] text-[.82rem] font-medium text-tf06-muted"><input type="checkbox" class="m-0 size-[1.05rem] accent-tf06-accent"><span>CC my team (ops@)</span></label>
        <button class="tf-06__submit inline-flex min-h-[2.9rem] cursor-pointer items-center gap-[.8rem] rounded-[.7rem] border-0 bg-tf06-accent pr-[.6rem] pl-[1.2rem] font-semibold text-[#04131c] [transition:filter_.2s,translate_.2s_var(--ease-tf06)] hover:-translate-y-px hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf06-ink" type="button"><span>Submit ticket</span><kbd class="rounded-[.4rem] bg-black/18 px-[.45rem] py-1 font-tf06-mono text-[.72rem] font-medium">⌘ ↵</kbd></button>
      </footer>
      <p class="tf-06__status -mt-2 font-tf06-mono text-[.82rem] text-tf06-ok empty:hidden data-[ok=false]:text-tf06-bad" role="status"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf06-bg: #0a0c10;
  --color-tf06-surface: #11141a;
  --color-tf06-raised: #171b23;
  --color-tf06-ink: #e6e9ef;
  --color-tf06-muted: #8b93a3;
  --color-tf06-line: #252a35;
  --color-tf06-accent: #38bdf8;
  --color-tf06-ok: #4ade80;
  --color-tf06-bad: #fb7185;
  --font-tf06-sans: "IBM Plex Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-tf06-mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
  --ease-tf06: cubic-bezier(0.16,1,0.3,1);
  --animate-tf06-live: tf06-live 2s infinite;
  --animate-tf06-in: tf06-in 0.35s cubic-bezier(0.16,1,0.3,1);

  @keyframes tf06-live {
    70% {
      box-shadow: 0 0 0 6px transparent;
    }
  }

  @keyframes tf06-in {
    from {
      opacity: 0;
      translate: 0 -4px;
    }
  }
}
/* Root rule: full-bleed contract. Dark-first like its CSS original: @theme holds the dark values,
   data-theme="light" overrides them. The select chevron is a data URI, so it lives here. */

.tf-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: dark;
  --tf06-chevron: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%238b93a3' stroke-width='2' stroke-linecap='round'%3E%3Cpath d='m7 10 5 5 5-5'/%3E%3C/svg%3E");
}

.tf-06[data-theme="light"] {
  color-scheme: light;
  --color-tf06-bg: #f3f5f8;
  --color-tf06-surface: #ffffff;
  --color-tf06-raised: #f6f8fb;
  --color-tf06-ink: #0f1720;
  --color-tf06-muted: #5b6474;
  --color-tf06-line: #e1e5ec;
  --color-tf06-accent: #0284c7;
  --color-tf06-ok: #15803d;
  --color-tf06-bad: #e11d48;
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-06').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : true);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.tf-06');
  if (!root) return;
  const MAX_FILES = 5, MAX_MB = 10;
  const drop = root.querySelector('.tf-06__drop'), input = drop.querySelector('input'), list = root.querySelector('.tf-06__files'), live = root.querySelector('#tf-06-live');
  const files = [];
  const size = (b) => b < 1024 ? b + ' B' : b < 1048576 ? (b / 1024).toFixed(0) + ' KB' : (b / 1048576).toFixed(1) + ' MB';
  const setProgress = (row, p) => row.style.setProperty('--p', p / 100);
  const add = (incoming) => {
    const rejected = [];
    [...incoming].forEach((f) => {
      if (files.length >= MAX_FILES) return rejected.push(f.name + ' (limit of ' + MAX_FILES + ' files)');
      if (f.size > MAX_MB * 1048576) return rejected.push(f.name + ' (over ' + MAX_MB + ' MB)');
      const ext = (f.name.split('.').pop() || '').slice(0, 4);
      const li = document.createElement('li');
      const isImg = f.type.startsWith('image/'), url = isImg ? URL.createObjectURL(f) : null;
      li.innerHTML = (isImg ? '<img class="tf-06__thumb" alt="">' : '<span class="tf-06__thumb" aria-hidden="true"></span>') +
        '<div class="tf-06__meta"><b></b><small></small><span class="tf-06__track"><span class="tf-06__bar"></span></span></div>' +
        '<button type="button" class="tf-06__rm"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button>';
      if (isImg) li.querySelector('img').src = url; else li.querySelector('.tf-06__thumb').textContent = ext;
      li.querySelector('b').textContent = f.name;
      const meta = li.querySelector('small'); meta.textContent = size(f.size) + ' · uploading…';
      li.querySelector('.tf-06__rm').setAttribute('aria-label', 'Remove ' + f.name);
      const entry = { f, li, url };
      files.push(entry); list.append(li);
      let p = 0;
      const t = setInterval(() => {
        p = Math.min(100, p + 8 + Math.random() * 18); setProgress(li, p);
        if (p >= 100) { clearInterval(t); li.classList.add('is-done'); meta.textContent = size(f.size) + ' · uploaded'; }
      }, 140);
      li.querySelector('.tf-06__rm').addEventListener('click', () => {
        clearInterval(t); if (url) URL.revokeObjectURL(url);
        files.splice(files.indexOf(entry), 1); li.remove(); live.textContent = f.name + ' removed.'; input.focus();
      });
    });
    live.textContent = rejected.length ? 'Not added: ' + rejected.join(', ') : incoming.length + ' file(s) attached.';
  };
  input.addEventListener('change', () => { add(input.files); input.value = ''; });
  let depth = 0;
  drop.addEventListener('dragenter', (e) => { e.preventDefault(); depth++; drop.classList.add('is-over'); });
  drop.addEventListener('dragover', (e) => e.preventDefault());
  drop.addEventListener('dragleave', () => { if (--depth <= 0) { depth = 0; drop.classList.remove('is-over'); } });
  drop.addEventListener('drop', (e) => { e.preventDefault(); depth = 0; drop.classList.remove('is-over'); add(e.dataTransfer.files); });
  const status = root.querySelector('.tf-06__status');
  const submit = () => {
    const bad = [...root.querySelectorAll('[required]')].find((f) => !f.value.trim());
    if (bad) { status.dataset.ok = 'false'; status.textContent = '✕ Subject and description are required.'; bad.focus(); return; }
    const p = root.querySelector('[name="tf-06-p"]:checked').value;
    status.dataset.ok = 'true';
    status.textContent = '✓ Ticket #' + (48000 + Math.floor(Math.random() * 999)) + ' created · priority ' + p + ' · ' + files.length + ' attachment(s)';
  };
  root.querySelector('.tf-06__submit').addEventListener('click', submit);
  root.addEventListener('keydown', (e) => { if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') submit(); });
})();
```

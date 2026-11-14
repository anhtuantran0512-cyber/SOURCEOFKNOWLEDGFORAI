---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/tailwind-css-chat-bubble/"
title: "Tailwind CSS Chat Bubble"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "A chat card written the way you would actually write it in a Tailwind project — utilities on every element, dark: variants for the full colour scheme,…"
has_js: "true"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Chat Bubble
Source: https://codefronts.com/snippets/css-chat-bubbles/tailwind-css-chat-bubble/

A chat card written the way you would actually write it in a Tailwind project — utilities on every element, dark: variants for the full colour scheme, group-hover: timestamps, peer state on the composer, and arbitrary-value utilities for the tail geometry. Ships with a scoped vanilla fallback so it renders identically here; delete that block in a real Tailwind app and the class names carry over untouched.
## HTML
```html
<div class="cb-04 min-h-screen w-full grid place-items-center p-4 sm:p-8 bg-slate-100 dark:bg-slate-950">
  <button class="cb-04__theme absolute top-4 end-4 z-10 grid size-11 place-items-center rounded-2xl border border-slate-200 bg-white text-slate-900 shadow-sm transition hover:-translate-y-0.5 dark:border-slate-800 dark:bg-slate-900 dark:text-slate-100" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cb-04__moon size-5" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-04__sun size-5" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>

  <section class="w-full max-w-lg overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-2xl dark:border-slate-800 dark:bg-slate-900" aria-label="Team chat">
    <header class="flex items-center gap-3 border-b border-slate-200 px-4 py-3 dark:border-slate-800">
      <img class="size-10 rounded-full object-cover" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=facearea&facepad=2.6&w=160&h=160&q=70" width="40" height="40" alt="Dorian Vale" loading="lazy" decoding="async">
      <div class="min-w-0">
        <p class="truncate text-sm font-semibold text-slate-900 dark:text-slate-100">Dorian Vale</p>
        <p class="flex items-center gap-1.5 text-xs text-slate-500 dark:text-slate-400"><span class="size-2 rounded-full bg-emerald-500"></span>Active now</p>
      </div>
      <button class="ms-auto grid size-11 place-items-center rounded-xl text-slate-500 transition hover:bg-slate-100 hover:text-slate-900 dark:hover:bg-slate-800 dark:hover:text-slate-100" type="button" aria-label="Conversation details">
        <svg class="size-5" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="5.5" r="1.6" fill="currentColor"/><circle cx="12" cy="12" r="1.6" fill="currentColor"/><circle cx="12" cy="18.5" r="1.6" fill="currentColor"/></svg>
      </button>
    </header>

    <ol class="cb-04__thread flex max-h-[26rem] flex-col gap-2.5 overflow-y-auto p-4" id="cb-04-thread" aria-label="Messages">
      <li class="group flex items-end justify-start gap-2">
        <p class="relative max-w-[22rem] rounded-2xl rounded-es-sm bg-slate-100 px-4 py-2.5 text-[0.95rem] leading-relaxed text-slate-900 after:absolute after:bottom-0 after:start-[-9px] after:border-y-[10px] after:border-y-transparent after:border-e-[11px] after:border-e-slate-100 after:content-[''] dark:bg-slate-800 dark:text-slate-100 dark:after:border-e-slate-800">Design tokens are merged. Want me to ship the dark palette tonight?</p>
        <time class="shrink-0 pb-1 text-[0.68rem] font-medium text-slate-400 opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-within:opacity-100" datetime="2027-02-11T16:41">16:41</time>
      </li>
      <li class="group flex items-end justify-end gap-2">
        <time class="shrink-0 pb-1 text-[0.68rem] font-medium text-slate-400 opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-within:opacity-100" datetime="2027-02-11T16:43">16:43</time>
        <p class="relative max-w-[22rem] rounded-2xl rounded-ee-sm bg-indigo-600 px-4 py-2.5 text-[0.95rem] leading-relaxed text-white after:absolute after:bottom-0 after:end-[-9px] after:border-y-[10px] after:border-y-transparent after:border-s-[11px] after:border-s-indigo-600 after:content-[''] dark:bg-indigo-500 dark:after:border-s-indigo-500">Ship it. I'll review the contrast pass in the morning.</p>
      </li>
      <li class="group flex items-end justify-start gap-2">
        <p class="relative max-w-[22rem] rounded-2xl rounded-es-sm bg-slate-100 px-4 py-2.5 text-[0.95rem] leading-relaxed text-slate-900 after:absolute after:bottom-0 after:start-[-9px] after:border-y-[10px] after:border-y-transparent after:border-e-[11px] after:border-e-slate-100 after:content-[''] dark:bg-slate-800 dark:text-slate-100 dark:after:border-e-slate-800">Every surface hits 4.6:1 or better. Screenshots in the PR.</p>
        <time class="shrink-0 pb-1 text-[0.68rem] font-medium text-slate-400 opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-within:opacity-100" datetime="2027-02-11T16:45">16:45</time>
      </li>
    </ol>

    <div class="flex flex-wrap gap-2 border-t border-slate-200 px-4 pt-3 dark:border-slate-800" role="group" aria-label="Quick replies">
      <button class="cb-04__quick min-h-9 rounded-full border border-slate-200 px-3 py-1.5 text-xs font-medium text-slate-600 transition hover:-translate-y-px hover:border-indigo-400 hover:text-slate-900 dark:border-slate-700 dark:text-slate-300 dark:hover:text-white" type="button">Looks good 👌</button>
      <button class="cb-04__quick min-h-9 rounded-full border border-slate-200 px-3 py-1.5 text-xs font-medium text-slate-600 transition hover:-translate-y-px hover:border-indigo-400 hover:text-slate-900 dark:border-slate-700 dark:text-slate-300 dark:hover:text-white" type="button">Send the PR link</button>
      <button class="cb-04__quick min-h-9 rounded-full border border-slate-200 px-3 py-1.5 text-xs font-medium text-slate-600 transition hover:-translate-y-px hover:border-indigo-400 hover:text-slate-900 dark:border-slate-700 dark:text-slate-300 dark:hover:text-white" type="button">Tomorrow works</button>
    </div>

    <div class="flex items-center gap-2 p-4">
      <input class="peer min-h-11 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 text-[0.95rem] text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-indigo-500 focus:bg-white dark:border-slate-700 dark:bg-slate-800 dark:text-slate-100 dark:focus:bg-slate-800" id="cb-04-input" type="text" placeholder="Write a message…" aria-label="Message">
      <button class="grid size-11 shrink-0 place-items-center rounded-2xl bg-indigo-600 text-white transition hover:scale-105 disabled:scale-100 disabled:opacity-30 peer-focus:ring-2 peer-focus:ring-indigo-500/40 dark:bg-indigo-500" id="cb-04-send" type="button" aria-label="Send message" disabled>
        <svg class="size-5" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12 20 5l-3.2 14.5-4.6-4.3-3 2.4z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
      </button>
    </div>
    <p class="sr-only" id="cb-04-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap');

.cb-04 {
  font-family: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}
/* ═════════════════════════════════════════════════════════════════
   VANILLA FALLBACK — scoped implementations of every Tailwind utility
   used above. DELETE THIS ENTIRE BLOCK inside a real Tailwind project.
   ═════════════════════════════════════════════════════════════════ */

.cb-04,
.cb-04 *,
.cb-04 *::before,
.cb-04 *::after {
  box-sizing: border-box;
}

.cb-04 .sr-only {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.cb-04.min-h-screen {
  min-height: 100vh;
  min-height: 100svh;
}

.cb-04.w-full {
  width: 100%;
}

.cb-04.grid {
  display: grid;
}

.cb-04.place-items-center {
  place-items: center;
}

.cb-04.p-4 {
  padding: 1rem;
}

@media (min-width: 640px) {
  .cb-04.sm\:p-8 {
    padding: 2rem;
  }
}

.cb-04.bg-slate-100 {
  background: #f1f5f9;
}

.cb-04 .absolute {
  position: absolute;
}

.cb-04 .relative {
  position: relative;
}

.cb-04 .top-4 {
  top: 1rem;
}

.cb-04 .end-4 {
  inset-inline-end: 1rem;
}

.cb-04 .z-10 {
  z-index: 10;
}

.cb-04 .size-2 {
  inline-size: .5rem;
  block-size: .5rem;
}

.cb-04 .size-5 {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.cb-04 .size-10 {
  inline-size: 2.5rem;
  block-size: 2.5rem;
}

.cb-04 .size-11 {
  inline-size: 2.75rem;
  block-size: 2.75rem;
}

.cb-04 .min-h-9 {
  min-block-size: 2.25rem;
}

.cb-04 .min-h-11 {
  min-block-size: 2.75rem;
}

.cb-04 .grid {
  display: grid;
}

.cb-04 .flex {
  display: flex;
}

.cb-04 .flex-col {
  flex-direction: column;
}

.cb-04 .flex-wrap {
  flex-wrap: wrap;
}

.cb-04 .items-center {
  align-items: center;
}

.cb-04 .items-end {
  align-items: flex-end;
}

.cb-04 .justify-start {
  justify-content: flex-start;
}

.cb-04 .justify-end {
  justify-content: flex-end;
}

.cb-04 .place-items-center {
  place-items: center;
}

.cb-04 .shrink-0 {
  flex-shrink: 0;
}

.cb-04 .min-w-0 {
  min-inline-size: 0;
}

.cb-04 .gap-1\.5 {
  gap: .375rem;
}

.cb-04 .gap-2 {
  gap: .5rem;
}

.cb-04 .gap-2\.5 {
  gap: .625rem;
}

.cb-04 .gap-3 {
  gap: .75rem;
}

.cb-04 .p-4 {
  padding: 1rem;
}

.cb-04 .px-3 {
  padding-inline: .75rem;
}

.cb-04 .px-4 {
  padding-inline: 1rem;
}

.cb-04 .py-1\.5 {
  padding-block: .375rem;
}

.cb-04 .py-2\.5 {
  padding-block: .625rem;
}

.cb-04 .py-3 {
  padding-block: .75rem;
}

.cb-04 .pt-3 {
  padding-block-start: .75rem;
}

.cb-04 .pb-1 {
  padding-block-end: .25rem;
}

.cb-04 .ms-auto {
  margin-inline-start: auto;
}

.cb-04 .w-full {
  inline-size: 100%;
}

.cb-04 .max-w-lg {
  max-inline-size: 32rem;
}

.cb-04 .max-w-\[22rem\] {
  max-inline-size: 22rem;
}

.cb-04 .max-h-\[26rem\] {
  max-block-size: 26rem;
}

.cb-04 .overflow-hidden {
  overflow: hidden;
}

.cb-04 .overflow-y-auto {
  overflow-y: auto;
  overflow-x: clip;
  scrollbar-width: thin;
}

.cb-04 .rounded-full {
  border-radius: 999px;
}

.cb-04 .rounded-xl {
  border-radius: .75rem;
}

.cb-04 .rounded-2xl {
  border-radius: 1rem;
}

.cb-04 .rounded-3xl {
  border-radius: 1.5rem;
}

.cb-04 .rounded-es-sm {
  border-end-start-radius: .25rem;
}

.cb-04 .rounded-ee-sm {
  border-end-end-radius: .25rem;
}

.cb-04 .border {
  border: 1px solid;
}

.cb-04 .border-b {
  border-block-end: 1px solid;
}

.cb-04 .border-t {
  border-block-start: 1px solid;
}

.cb-04 .border-slate-200 {
  border-color: #e2e8f0;
}

.cb-04 .bg-white {
  background: #fff;
}

.cb-04 .bg-slate-50 {
  background: #f8fafc;
}

.cb-04 .bg-slate-100 {
  background: #f1f5f9;
}

.cb-04 .bg-indigo-600 {
  background: #4f46e5;
}

.cb-04 .bg-emerald-500 {
  background: #10b981;
}

.cb-04 .text-white {
  color: #fff;
}

.cb-04 .text-slate-900 {
  color: #0f172a;
}

.cb-04 .text-slate-600 {
  color: #475569;
}

.cb-04 .text-slate-500 {
  color: #64748b;
}

.cb-04 .text-slate-400 {
  color: #94a3b8;
}

.cb-04 .text-xs {
  font-size: .75rem;
  line-height: 1.4;
}

.cb-04 .text-sm {
  font-size: .875rem;
  line-height: 1.45;
}

.cb-04 .text-\[0\.68rem\] {
  font-size: .68rem;
}

.cb-04 .text-\[0\.95rem\] {
  font-size: .95rem;
}

.cb-04 .font-medium {
  font-weight: 500;
}

.cb-04 .font-semibold {
  font-weight: 600;
}

.cb-04 .leading-relaxed {
  line-height: 1.55;
}

.cb-04 .truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.cb-04 .object-cover {
  object-fit: cover;
}

.cb-04 .outline-none {
  outline: 0;
}

.cb-04 .shadow-sm {
  box-shadow: 0 1px 3px rgba(15,23,42,.1);
}

.cb-04 .shadow-2xl {
  box-shadow: 0 40px 90px -55px rgba(15,23,42,.55);
}

.cb-04 .transition,
.cb-04 .transition-opacity {
  transition: all .22s cubic-bezier(.16,1,.3,1);
}

.cb-04 .duration-200 {
  transition-duration: .2s;
}

.cb-04 .opacity-0 {
  opacity: 0;
}

.cb-04 [class*="after:content"]::after {
  content: '';
}

.cb-04 .after\:absolute::after {
  position: absolute;
}

.cb-04 .after\:bottom-0::after {
  inset-block-end: 0;
}

.cb-04 .after\:start-\[-9px\]::after {
  inset-inline-start: -9px;
}

.cb-04 .after\:end-\[-9px\]::after {
  inset-inline-end: -9px;
}

.cb-04 .after\:border-y-\[10px\]::after {
  border-block: 10px solid;
}

.cb-04 .after\:border-y-transparent::after {
  border-block-color: transparent;
}

.cb-04 .after\:border-e-\[11px\]::after {
  border-inline-end: 11px solid;
}

.cb-04 .after\:border-s-\[11px\]::after {
  border-inline-start: 11px solid;
}

.cb-04 .after\:border-e-slate-100::after {
  border-inline-end-color: #f1f5f9;
}

.cb-04 .after\:border-s-indigo-600::after {
  border-inline-start-color: #4f46e5;
}

.cb-04 .hover\:-translate-y-0\.5:hover {
  transform: translateY(-2px);
}

.cb-04 .hover\:-translate-y-px:hover {
  transform: translateY(-1px);
}

.cb-04 .hover\:scale-105:hover {
  transform: scale(1.05);
}

.cb-04 .hover\:bg-slate-100:hover {
  background: #f1f5f9;
}

.cb-04 .hover\:text-slate-900:hover {
  color: #0f172a;
}

.cb-04 .hover\:border-indigo-400:hover {
  border-color: #818cf8;
}

.cb-04 .placeholder\:text-slate-400::placeholder {
  color: #94a3b8;
}

.cb-04 .focus\:border-indigo-500:focus {
  border-color: #6366f1;
}

.cb-04 .focus\:bg-white:focus {
  background: #fff;
}

.cb-04 .disabled\:opacity-30:disabled {
  opacity: .3;
}

.cb-04 .disabled\:scale-100:disabled {
  transform: none;
}

.cb-04 .peer:focus ~ .peer-focus\:ring-2 {
  box-shadow: 0 0 0 3px rgba(99,102,241,.4);
}

.cb-04 .group:hover .group-hover\:opacity-100,
.cb-04 .group:focus-within .group-focus-within\:opacity-100 {
  opacity: 1;
}

.cb-04 button,
.cb-04 input {
  font: inherit;
}

.cb-04 button {
  cursor: pointer;
  border-color: transparent;
  background: transparent;
}

.cb-04 button:disabled {
  cursor: not-allowed;
}

.cb-04 ol {
  list-style: none;
  margin: 0;
}

.cb-04 p,
.cb-04 time {
  margin: 0;
}

.cb-04 :focus-visible {
  outline: 2px solid #6366f1;
  outline-offset: 2px;
}
/* dark: variants — class strategy, so the in-demo toggle can override the OS */

.cb-04.dark.bg-slate-950,
.cb-04.dark .dark\:bg-slate-950 {
  background: #020618;
}

.cb-04.dark .dark\:bg-slate-900 {
  background: #0f172a;
}

.cb-04.dark .dark\:bg-slate-800 {
  background: #1e293b;
}

.cb-04.dark .dark\:bg-indigo-500 {
  background: #6366f1;
}

.cb-04.dark .dark\:border-slate-800 {
  border-color: #1e293b;
}

.cb-04.dark .dark\:border-slate-700 {
  border-color: #334255;
}

.cb-04.dark .dark\:text-slate-100 {
  color: #f1f5f9;
}

.cb-04.dark .dark\:text-slate-300 {
  color: #cbd5e1;
}

.cb-04.dark .dark\:text-slate-400 {
  color: #94a3b8;
}

.cb-04.dark .dark\:after\:border-e-slate-800::after {
  border-inline-end-color: #1e293b;
}

.cb-04.dark .dark\:after\:border-s-indigo-500::after {
  border-inline-start-color: #6366f1;
}

.cb-04.dark .dark\:hover\:bg-slate-800:hover {
  background: #1e293b;
}

.cb-04.dark .dark\:hover\:text-slate-100:hover {
  color: #f1f5f9;
}

.cb-04.dark .dark\:hover\:text-white:hover {
  color: #fff;
}

.cb-04 .cb-04__sun {
  display: none;
}

.cb-04.dark .cb-04__moon {
  display: none;
}

.cb-04.dark .cb-04__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cb-04 *,
    .cb-04 *::before,
    .cb-04 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-04 p[class*="bg-"] {
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.cb-04');
  if (!root) return;
  const thread = root.querySelector('#cb-04-thread');
  const input = root.querySelector('#cb-04-input');
  const send = root.querySelector('#cb-04-send');
  const status = root.querySelector('#cb-04-status');

  /* the exact utility string an outgoing bubble uses — keep it in one constant */
  const OUT = "relative max-w-[22rem] rounded-2xl rounded-ee-sm bg-indigo-600 px-4 py-2.5 text-[0.95rem] leading-relaxed text-white after:absolute after:bottom-0 after:end-[-9px] after:border-y-[10px] after:border-y-transparent after:border-s-[11px] after:border-s-indigo-600 after:content-[''] dark:bg-indigo-500 dark:after:border-s-indigo-500";
  const TIME = "shrink-0 pb-1 text-[0.68rem] font-medium text-slate-400 opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-within:opacity-100";

  const push = (text) => {
    const now = new Date();
    const hhmm = String(now.getHours()).padStart(2, '0') + ':' + String(now.getMinutes()).padStart(2, '0');
    const li = document.createElement('li');
    li.className = 'group flex items-end justify-end gap-2';
    const t = document.createElement('time');
    t.className = TIME; t.dateTime = now.toISOString(); t.textContent = hhmm;
    const p = document.createElement('p');
    p.className = OUT; p.textContent = text;
    li.append(t, p); thread.append(li);
    thread.scrollTop = thread.scrollHeight;
    status.textContent = 'Sent: ' + text;
  };

  input.addEventListener('input', () => { send.disabled = !input.value.trim(); });
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') send.click(); });
  send.addEventListener('click', () => {
    const text = input.value.trim();
    if (!text) return;
    push(text); input.value = ''; send.disabled = true; input.focus();
  });
  root.querySelectorAll('.cb-04__quick').forEach((b) => {
    b.addEventListener('click', () => push(b.textContent.trim()));
  });
})();

(() => {                                      // dark: class strategy toggle
  const root = document.querySelector('.cb-04');
  const btn = root && root.querySelector('.cb-04__theme');
  if (!btn) return;
  const set = (dark) => {
    root.classList.toggle('dark', dark);
    btn.setAttribute('aria-pressed', String(dark));
    btn.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
  };
  set(matchMedia('(prefers-color-scheme: dark)').matches);
  btn.addEventListener('click', () => set(!root.classList.contains('dark')));
})();
```

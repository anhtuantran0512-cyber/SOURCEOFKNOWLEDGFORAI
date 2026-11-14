---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-voice-search-input/"
title: "Tailwind Voice Search Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A search field with a mic that pulses while listening."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Voice Search Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-voice-search-input/

A search field with a mic that pulses while listening. The recording state is aria-pressed on a real button, and every visual — icon colour, halo, pulse — is a variant reading that attribute, so the accessible state and the visible state cannot disagree.
## HTML
```html
<div class="tif-20 grid min-h-svh w-full place-items-center bg-tif20-bg px-6 py-14 font-tif20-sans" aria-label="Voice search input demo">
  <form role="search" autocomplete="off" class="grid w-full max-w-80 gap-1.5">
    <label for="tif20-input" class="font-tif20-mono text-[10px] tracking-[0.12em] text-tif20-mut uppercase">Voice search</label>
    <span class="flex items-center gap-2 rounded-[10px] border border-white/12 bg-tif20-field py-1 pr-1 pl-3.5 transition-colors duration-200 focus-within:border-tif20-rec">
      <svg viewBox="0 0 24 24" aria-hidden="true" class="size-4 shrink-0 fill-none stroke-tif20-dim stroke-2 [stroke-linecap:round]"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input id="tif20-input" type="search" name="q" inputmode="search" placeholder="Speak or type to search…"
        class="min-w-0 flex-1 border-0 bg-transparent py-2 text-sm font-medium text-tif20-ink outline-none placeholder:text-tif20-mut">
      <button type="button" aria-label="Start voice input" aria-pressed="false" data-tif20-mic
        class="group relative grid size-11 shrink-0 cursor-pointer place-items-center rounded-lg border-0 bg-transparent transition-colors duration-200 hover:bg-tif20-rec/10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tif20-rec aria-pressed:bg-tif20-rec/10 aria-pressed:after:absolute aria-pressed:after:inset-2 aria-pressed:after:rounded-md aria-pressed:after:border-[1.5px] aria-pressed:after:border-tif20-rec aria-pressed:after:animate-tif20-pulse aria-pressed:after:content-[''] motion-reduce:aria-pressed:after:animate-none">
        <svg viewBox="0 0 24 24" aria-hidden="true" class="size-4 fill-none stroke-tif20-acc stroke-2 transition-colors [stroke-linecap:round] group-aria-pressed:stroke-tif20-rec"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>
      </button>
    </span>
  </form>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif20-bg: #12121a;
  --color-tif20-bg: oklch(0.19 0.015 285);
  --color-tif20-field: #1a1a22;
  --color-tif20-field: oklch(0.23 0.015 285);
  --color-tif20-ink: #f0eeff;
  --color-tif20-ink: oklch(0.95 0.02 290);
  --color-tif20-mut: #b8b6d4;
  --color-tif20-mut: oklch(0.77 0.03 290);
  --color-tif20-dim: #6b6987;
  --color-tif20-dim: oklch(0.55 0.03 290);
  --color-tif20-acc: #a78bfa;
  --color-tif20-acc: oklch(0.74 0.15 295);
  --color-tif20-rec: #ff6c8a;
  --color-tif20-rec: oklch(0.72 0.17 15);
  --font-tif20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tif20-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tif20-pulse: tif20-pulse 1.2s ease-out infinite;
}
/* The keyframes the @theme animation token points at — the one thing that cannot
   be a utility. */

@keyframes tif20-pulse {
  0% {
    transform: scale(0.8);
    opacity: 1;
  }

  100% {
    transform: scale(1.4);
    opacity: 0;
  }
}

.tif-20 {
  width: 100%;
}

.tif-20 ::selection {
  background: var(--color-tif20-rec);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tif-20').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    root.querySelectorAll('[data-tif20-mic]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var on = btn.getAttribute('aria-pressed') === 'true';
        btn.setAttribute('aria-pressed', on ? 'false' : 'true');
        btn.setAttribute('aria-label', on ? 'Start voice input' : 'Stop voice input');
        // Real recognition goes here:
        // var Rec = window.SpeechRecognition || window.webkitSpeechRecognition;
      });
    });
  });
})();
```

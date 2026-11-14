---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/copy-link-button-with-copied-feedback/"
title: "Copy Link Button with Copied Feedback"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "A share-this-page control: the URL sits in a monospace field, one button copies it, and the confirmation is driven by the result of the write rather than by…"
has_js: "true"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Copy Link Button with Copied Feedback
Source: https://codefronts.com/snippets/css-social-buttons/copy-link-button-with-copied-feedback/

A share-this-page control: the URL sits in a monospace field, one button copies it, and the confirmation is driven by the result of the write rather than by optimism. When the clipboard is unavailable — an insecure origin, a locked-down frame — the button says so and pre-selects the text instead of showing a confirmation that never happened.
## HTML
```html
<div class="soc-09">
  <div class="soc-09__stage">
    <div class="soc-09__card">
      <p class="soc-09__eyebrow">Share link</p>
      <h2 class="soc-09__title">Copy the page URL</h2>
      <div class="soc-09__row">
        <span class="soc-09__url" id="soc-09-url">https://example.com/blog/design-tokens</span>
        <button class="soc-09__btn" type="button" data-state="idle" aria-describedby="soc-09-url">
          <span class="soc-09__ico" aria-hidden="true">
            <svg class="soc-09__link" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.2 13.8a3.6 3.6 0 0 0 5.1 0l2.9-2.9a3.6 3.6 0 1 0-5.1-5.1L11.7 7.2"/><path d="M13.8 10.2a3.6 3.6 0 0 0-5.1 0l-2.9 2.9a3.6 3.6 0 1 0 5.1 5.1l1.4-1.4"/></svg>
            <svg class="soc-09__check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
          </span>
          <span class="soc-09__label">Copy link</span>
        </button>
      </div>
      <p class="soc-09__ok" role="status" aria-live="polite"></p>
      <p class="soc-09__err" role="alert"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.soc-09 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --ok: #0e8a55;
  --warn: #b3541e;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .soc-09 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
    --ok: oklch(56% .13 158);
    --warn: oklch(56% .13 55);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-09:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
    --ok: #3ecf8e;
    --warn: #f0a45c;
  }
}

.soc-09[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
  --ok: #3ecf8e;
  --warn: #f0a45c;
}

.soc-09,
.soc-09 *,
.soc-09 *::before,
.soc-09 *::after {
  box-sizing: border-box;
}

.soc-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-09__card {
  inline-size: min(34rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-09__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-09__title {
  margin: 0 0 1.35rem;
  font-size: clamp(1.1rem,1rem + .9vw,1.4rem);
  font-weight: 600;
  letter-spacing: -.02em;
}

.soc-09__row {
  display: flex;
  flex-wrap: wrap;
  gap: .55rem;
  align-items: stretch;
}

.soc-09__url {
  flex: 1 1 12rem;
  min-inline-size: 0;
  display: flex;
  align-items: center;
  padding: .7rem .85rem;
  border: 1px solid var(--line);
  border-radius: .85rem;
  background: color-mix(in oklab,var(--fg) 4%,var(--surface));
  font-family: var(--mono);
  font-size: .82rem;
  color: var(--muted);
  overflow-wrap: anywhere;
  user-select: all;
}

.soc-09__btn {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 2.875rem;
  padding: 0 1.05rem;
  border: 1px solid var(--fg);
  border-radius: .85rem;
  background: var(--fg);
  color: var(--surface);
  font: inherit;
  font-size: .9rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: translate .2s cubic-bezier(.16,1,.3,1), background-color .22s ease, border-color .22s ease, color .22s ease;
}

.soc-09__btn:hover {
  translate: 0 -2px;
}

.soc-09__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-09__ico {
  position: relative;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  display: grid;
  place-items: center;
}

.soc-09__ico svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  transition: opacity .2s ease, scale .2s cubic-bezier(.16,1,.3,1);
}

.soc-09__check {
  opacity: 0;
  scale: .6;
}

.soc-09__btn[data-state="copied"] {
  background: var(--ok);
  border-color: var(--ok);
  color: #fff;
}

.soc-09__btn[data-state="copied"] .soc-09__link {
  opacity: 0;
  scale: .6;
}

.soc-09__btn[data-state="copied"] .soc-09__check {
  opacity: 1;
  scale: 1;
}

.soc-09__btn[data-state="manual"] {
  background: var(--surface);
  color: var(--warn);
  border-color: var(--warn);
}

.soc-09__ok {
  margin: 1rem 0 0;
  min-block-size: 1.1rem;
  font-size: .82rem;
  font-weight: 550;
  color: var(--ok);
}

.soc-09__err {
  margin: .2rem 0 0;
  min-block-size: 1.1rem;
  font-size: .82rem;
  font-weight: 550;
  color: var(--warn);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .soc-09__btn,
    .soc-09__ico svg {
    transition-duration: 1ms;
  }

  .soc-09__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-09__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }

  .soc-09__btn[data-state="copied"] {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.soc-09');
  if (!root) return;
  const btn = root.querySelector('.soc-09__btn');
  const field = root.querySelector('.soc-09__url');
  const ok = root.querySelector('.soc-09__ok');
  const err = root.querySelector('.soc-09__err');
  let timer;
  const set = (state, text, okMsg, errMsg) => {
    btn.dataset.state = state;
    root.querySelector('.soc-09__label').textContent = text;
    ok.textContent = okMsg; err.textContent = errMsg;
    clearTimeout(timer);
    if (state !== 'idle') timer = setTimeout(() => set('idle', 'Copy link', '', ''), 2400);
  };
  btn.addEventListener('click', async () => {
    try {
      if (!navigator.clipboard) throw new Error('no-clipboard');
      await navigator.clipboard.writeText(field.textContent.trim());
      set('copied', 'Copied', 'Link copied to your clipboard.', '');
    } catch {
      const r = document.createRange(); r.selectNodeContents(field);
      const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
      set('manual', 'Select it', '', 'Clipboard unavailable here. The link is selected — press Ctrl/Cmd + C.');
    }
  });
})();
```

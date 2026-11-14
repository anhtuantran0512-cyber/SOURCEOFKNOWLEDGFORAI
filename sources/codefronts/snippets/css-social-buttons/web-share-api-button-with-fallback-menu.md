---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/web-share-api-button-with-fallback-menu/"
title: "Web Share API Button with Fallback Menu"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "One control, two behaviours: on a device that supports the native share sheet it calls navigator.share and hands off to the operating system; everywhere else…"
has_js: "true"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Web Share API Button with Fallback Menu
Source: https://codefronts.com/snippets/css-social-buttons/web-share-api-button-with-fallback-menu/

One control, two behaviours: on a device that supports the native share sheet it calls navigator.share and hands off to the operating system; everywhere else it opens a styled menu of channel buttons. The feature check runs before the call, the abort path is swallowed silently, and the fallback menu is the shipped baseline rather than an emergency patch.
## HTML
```html
<div class="soc-06">
  <div class="soc-06__stage">
    <div class="soc-06__card">
      <p class="soc-06__eyebrow">Article</p>
      <h2 class="soc-06__title">Container queries in production: a six-month review</h2>
      <p class="soc-06__meta">Sam Rivera · 9 min read</p>
      <div class="soc-06__wrap">
        <button class="soc-06__btn" type="button" aria-expanded="false" aria-controls="soc-06-menu" aria-haspopup="true">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="17.5" cy="5.5" r="2.6"/><circle cx="6.5" cy="12" r="2.6"/><circle cx="17.5" cy="18.5" r="2.6"/><path d="m8.9 10.7 6.2-3.6"/><path d="m8.9 13.3 6.2 3.6"/></svg>
          <span>Share this article</span>
        </button>
        <div class="soc-06__menu" id="soc-06-menu" role="menu" aria-label="Share options">
          <a class="soc-06__opt" style="--brand:#0f1419" role="menuitem" href="https://example.com/intent/post" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg><span>Post on X</span></a>
          <a class="soc-06__opt" style="--brand:#0a66c2" role="menuitem" href="https://example.com/intent/linkedin" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg><span>Share on LinkedIn</span></a>
          <a class="soc-06__opt" style="--brand:#25d366" role="menuitem" href="https://example.com/intent/whatsapp" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 11.6a8.4 8.4 0 0 1-12.4 7.3L3.5 20.4l1.6-4.5A8.4 8.4 0 1 1 20.5 11.6Z"/><path d="M9.2 9.4c.6 2.4 2.6 4.3 5 4.9"/></svg><span>Send on WhatsApp</span></a>
          <a class="soc-06__opt" style="--brand:#d4453b" role="menuitem" href="mailto:?subject=Container%20queries%20in%20production&amp;body=Thought%20you%27d%20like%20this%3A%20https%3A%2F%2Fexample.com%2Farticle">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.2" width="18" height="13.6" rx="3.4"/><path d="m4.4 8 6.7 4.7a1.6 1.6 0 0 0 1.8 0L19.6 8"/></svg><span>Email a link</span></a>
        </div>
      </div>
      <p class="soc-06__hint">No native sheet here? The menu is the shipped fallback.</p>
      <p class="soc-06__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-06 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --accent: #1c1c22;
  --on-accent: #ffffff;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
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
  .soc-06 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
    --accent: oklch(22% .015 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-06:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
    --accent: #f2f2f5;
    --on-accent: #101015;
  }
}

.soc-06[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
  --accent: #f2f2f5;
  --on-accent: #101015;
}

.soc-06,
.soc-06 *,
.soc-06 *::before,
.soc-06 *::after {
  box-sizing: border-box;
}

.soc-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-06__card {
  inline-size: min(34rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-06__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-06__title {
  margin: 0 0 .4rem;
  font-size: clamp(1.1rem,1rem + .9vw,1.4rem);
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.soc-06__meta {
  margin: 0 0 1.5rem;
  font-size: .85rem;
  color: var(--muted);
}

.soc-06__wrap {
  position: relative;
}

.soc-06__btn {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-block-size: 2.875rem;
  padding: 0 1.15rem;
  border: 0;
  border-radius: .85rem;
  background: var(--accent);
  color: var(--on-accent);
  font: inherit;
  font-size: .92rem;
  font-weight: 550;
  cursor: pointer;
  transition: translate .2s cubic-bezier(.16,1,.3,1), box-shadow .2s ease, opacity .2s ease;
  box-shadow: 0 10px 24px -16px rgb(9 9 20/.7);
}

.soc-06__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.soc-06__btn:hover {
  translate: 0 -2px;
}

.soc-06__btn:active {
  translate: 0 0;
  opacity: .9;
}

.soc-06__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-06__menu {
  display: none;
  opacity: 0;
  translate: 0 -6px;
  position: absolute;
  top: calc(100% + .6rem);
  inset-inline-start: 0;
  z-index: 10;
  inline-size: min(17.5rem,calc(100vw - 3rem));
  padding: .4rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
  box-shadow: 0 24px 50px -24px rgb(9 9 20/.45);
  transition: opacity .18s ease, translate .18s cubic-bezier(.16,1,.3,1), display .18s allow-discrete;
}

.soc-06__wrap[data-open="true"] .soc-06__menu {
  display: block;
  opacity: 1;
  translate: 0 0;
}

@starting-style {
  .soc-06__wrap[data-open="true"] .soc-06__menu {
    opacity: 0;
    translate: 0 -6px;
  }
}

.soc-06__opt {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 2.75rem;
  padding: 0 .7rem;
  border-radius: .7rem;
  color: var(--fg);
  text-decoration: none;
  font-size: .9rem;
  min-inline-size: 0;
  transition: background-color .16s ease, color .16s ease;
}

.soc-06__opt span {
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.soc-06__opt svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
  color: var(--muted);
  transition: color .16s ease;
}

.soc-06__opt:hover {
  background: color-mix(in oklab,var(--fg) 6%,var(--surface));
}

.soc-06__opt:hover svg {
  color: var(--brand);
}

.soc-06__opt:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: -2px;
}

.soc-06__hint {
  margin: 1.1rem 0 0;
  font-size: .78rem;
  color: var(--muted);
}

.soc-06__live {
  margin: .4rem 0 0;
  min-block-size: 1.2rem;
  font-size: .8rem;
  font-weight: 550;
  color: var(--fg);
}

@media (prefers-reduced-motion: reduce) {
  .soc-06__menu {
    transition: display .01s allow-discrete;
    translate: none;
  }

  .soc-06__btn {
    transition-duration: 1ms;
  }

  .soc-06__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-06__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .soc-06__menu {
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.soc-06');
  if (!root) return;
  const wrap = root.querySelector('.soc-06__wrap');
  const btn = root.querySelector('.soc-06__btn');
  const live = root.querySelector('.soc-06__live');
  const payload = { title: 'Container queries in production', text: 'A six-month review by Sam Rivera', url: 'https://example.com/article' };
  const setOpen = (on) => {
    wrap.dataset.open = String(on);
    btn.setAttribute('aria-expanded', String(on));
    live.textContent = on ? 'Share menu open. Four options.' : '';
  };
  btn.addEventListener('click', async () => {
    if (wrap.dataset.open === 'true') return setOpen(false);
    if (navigator.share) {
      try { await navigator.share(payload); live.textContent = 'Shared via your device.'; return; }
      catch (err) { if (err && err.name === 'AbortError') return; }
    }
    setOpen(true);
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setOpen(false); });
  document.addEventListener('click', (e) => { if (!wrap.contains(e.target)) setOpen(false); });
})();
```

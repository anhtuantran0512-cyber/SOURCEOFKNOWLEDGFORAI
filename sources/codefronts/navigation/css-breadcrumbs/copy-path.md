---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/copy-path/"
title: "Developer Docs Breadcrumb with One-Click Path Copy to Clipboard"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "Terminal-inspired breadcrumb for developer documentation sites (Stripe, Vercel, Cloudflare, Docker, MDN)."
has_js: "true"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Developer Docs Breadcrumb with One-Click Path Copy to Clipboard
Source: https://codefronts.com/navigation/css-breadcrumbs/copy-path/

Terminal-inspired breadcrumb for developer documentation sites (Stripe, Vercel, Cloudflare, Docker, MDN). Monospace typography with slash separators and a one-click copy button that pushes the full path to the clipboard so devs can drop it straight into Slack, Linear, or a PR.
## HTML
```html
<section class="bc-22" aria-label="Developer docs breadcrumb with path copy demo">
      <nav class="bc-22__nav" aria-label="Documentation breadcrumb">
        <ol class="bc-22__list">
          <li><a href="#">docs</a></li>
          <li><a href="#">api</a></li>
          <li><a href="#">authentication</a></li>
          <li><a aria-current="page" href="#">oauth2</a></li>
        </ol>
        <button type="button" class="bc-22__copy" aria-label="Copy path to clipboard" data-cf-track="copy_path_click">
          <svg class="bc-22__icon bc-22__icon--copy" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>
          <svg class="bc-22__icon bc-22__icon--check" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="m5 12 5 5L20 7"/></svg>
        </button>
        <span class="bc-22__sr" role="status" aria-live="polite" aria-atomic="true"></span>
      </nav>
    </section>
```
## CSS
```css
.bc-22 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 2rem 1.25rem;
  background: radial-gradient(1200px 600px at 50% -10%, oklch(0.28 0.05 265 / 0.55), transparent 60%), oklch(0.16 0.02 260);
  font-family: ui-monospace, "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
  color: oklch(0.82 0.02 260);
  --bc18-accent: oklch(0.78 0.17 300);
  --bc18-muted: oklch(0.58 0.02 260);
  --bc18-sep: oklch(0.42 0.02 260);
  --bc18-surface: oklch(0.21 0.02 260);
  --bc18-border: oklch(0.32 0.02 260 / 0.6);
}

.bc-22 *,
.bc-22 *::before,
.bc-22 *::after {
  box-sizing: border-box;
}

.bc-22__nav {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.5rem 0.5rem 1rem;
  background: var(--bc18-surface);
  border: 1px solid var(--bc18-border);
  border-radius: 12px;
  box-shadow: 0 1px 0 oklch(1 0 0 / 0.04) inset, 0 10px 30px -12px oklch(0 0 0 / 0.6);
  font-size: 0.9375rem;
  line-height: 1.2;
  max-width: 100%;
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--bc18-border) transparent;
}

.bc-22__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: inline-flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 0.25rem;
}

.bc-22__list li {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  white-space: nowrap;
}

.bc-22__list li + li::before {
  content: "/";
  color: var(--bc18-sep);
  padding: 0 0.25rem;
  user-select: none;
}

.bc-22__list a {
  color: var(--bc18-muted);
  text-decoration: none;
  padding: 0.375rem 0.5rem;
  border-radius: 6px;
  transition: color 160ms ease, background-color 160ms ease;
}

.bc-22__list a:hover {
  color: oklch(0.92 0.02 260);
  background: color-mix(in oklch, var(--bc18-accent) 8%, transparent);
}

.bc-22__list a[aria-current="page"] {
  color: var(--bc18-accent);
  background: color-mix(in oklch, var(--bc18-accent) 12%, transparent);
  font-weight: 600;
  cursor: default;
}

.bc-22__list a:focus-visible,
.bc-22__copy:focus-visible {
  outline: 2px solid var(--bc18-accent);
  outline-offset: 2px;
  border-radius: 6px;
}

.bc-22__copy {
  appearance: none;
  border: 1px solid var(--bc18-border);
  background: color-mix(in oklch, var(--bc18-surface) 70%, oklch(0.28 0.02 260));
  color: oklch(0.82 0.02 260);
  min-width: 44px;
  min-height: 44px;
  width: 44px;
  height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  cursor: pointer;
  position: relative;
  transition: background-color 160ms ease, color 160ms ease, border-color 160ms ease, transform 160ms ease;
  flex-shrink: 0;
}

.bc-22__copy:hover {
  color: oklch(0.95 0.02 260);
  border-color: color-mix(in oklch, var(--bc18-accent) 40%, var(--bc18-border));
  background: color-mix(in oklch, var(--bc18-accent) 10%, var(--bc18-surface));
}

.bc-22__copy:active {
  transform: scale(0.96);
}

.bc-22__icon {
  width: 18px;
  height: 18px;
  position: absolute;
  inset: 0;
  margin: auto;
  transition: opacity 180ms ease, transform 180ms ease;
}

.bc-22__icon--check {
  color: var(--bc18-accent);
  opacity: 0;
  transform: scale(0.6);
}

.bc-22__copy.is-copied .bc-22__icon--copy {
  opacity: 0;
  transform: scale(0.6);
}

.bc-22__copy.is-copied .bc-22__icon--check {
  opacity: 1;
  transform: scale(1);
}

.bc-22__copy.is-copied {
  border-color: color-mix(in oklch, var(--bc18-accent) 60%, var(--bc18-border));
  background: color-mix(in oklch, var(--bc18-accent) 15%, var(--bc18-surface));
}

.bc-22__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

@media (prefers-reduced-motion: reduce) {
  .bc-22__list a,
    .bc-22__copy,
    .bc-22__icon {
    transition: none;
  }

  .bc-22__copy:active {
    transform: none;
  }
}

@media (max-width: 480px) {
  .bc-22__nav {
    font-size: 0.8125rem;
    padding-left: 0.75rem;
  }
}
```

## JavaScript
```js
(() => {
      const btn = document.querySelector('.bc-22__copy');
      if (!btn) return;
      const live = document.querySelector('.bc-22 .bc-22__sr');
      const path = 'docs/api/authentication/oauth2';
      btn.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(path);
          btn.classList.add('is-copied');
          if (live) live.textContent = 'Path copied to clipboard';
          setTimeout(() => {
            btn.classList.remove('is-copied');
            if (live) live.textContent = '';
          }, 1200);
        } catch (err) {
          // Clipboard API can fail on http:// or if permission denied — fail silently in demo.
        }
      });
    })();
```

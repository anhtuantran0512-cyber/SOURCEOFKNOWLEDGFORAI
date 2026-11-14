---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/text-with-lines-on-sides-divider-css-or-divider/"
title: "Text with Lines on Sides Divider CSS (\"OR\" Divider)"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "The divider every auth screen and pricing card needs: a centred word flanked by rules that fill whatever space is left."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Text with Lines on Sides Divider CSS ("OR" Divider)
Source: https://codefronts.com/snippets/css-dividers/text-with-lines-on-sides-divider-css-or-divider/

The divider every auth screen and pricing card needs: a centred word flanked by rules that fill whatever space is left. Shown three ways — the flexbox pseudo-element classic, the two-line grid version that needs no pseudo-elements at all, and a border-image one-liner — inside a real sign-in card, with the accessibility answer for whether the word should be announced.
## HTML
```html
<section class="div-04" aria-label="Text with lines on sides OR divider demo">
  <div class="div-04__stage">
    <div class="div-04__card">
      <h2 class="div-04__title">Sign in to Codefronts</h2>
      <button class="div-04__oauth" type="button">
        <svg viewBox="0 0 18 18" width="17" height="17" aria-hidden="true"><path fill="#4285F4" d="M17.6 9.2c0-.6-.1-1.2-.2-1.8H9v3.5h4.8a4.1 4.1 0 0 1-1.8 2.7v2.2h2.9c1.7-1.6 2.7-3.9 2.7-6.6z"/><path fill="#34A853" d="M9 18c2.4 0 4.5-.8 6-2.2l-2.9-2.2c-.8.5-1.8.9-3.1.9-2.4 0-4.4-1.6-5.1-3.8H.9v2.3A9 9 0 0 0 9 18z"/><path fill="#FBBC05" d="M3.9 10.7a5.4 5.4 0 0 1 0-3.4V5H.9a9 9 0 0 0 0 8l3-2.3z"/><path fill="#EA4335" d="M9 3.6c1.3 0 2.5.5 3.4 1.3l2.6-2.6A9 9 0 0 0 .9 5l3 2.3C4.6 5.2 6.6 3.6 9 3.6z"/></svg>
        Continue with Google
      </button>
      <div class="div-04__or" role="separator" aria-label="or">or</div>
      <button class="div-04__email" type="button">Continue with email</button>
      <div class="div-04__variants">
        <div class="div-04__grid" role="separator" aria-label="grid variant"><span class="div-04__rule"></span><span class="div-04__word">grid 1fr auto 1fr</span><span class="div-04__rule"></span></div>
        <div class="div-04__bimg" role="separator" aria-label="border-image variant"><span>border-image</span></div>
      </div>
    </div>
    <p class="div-04__chip">flex:1 1 0 pseudo-rules · role="separator" · aria-label carries the word</p>
  </div>
</section>
```
## CSS
```css
.div-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-04-bg);
  --div-04-bg: oklch(0.965 0.006 250);
  --div-04-card: oklch(1 0 0);
  --div-04-ink: oklch(0.24 0.02 260);
  --div-04-mut: oklch(0.58 0.018 260);
  --div-04-line: oklch(0.24 0.02 260/.14);
  --div-04-acc: oklch(0.52 0.17 268);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-04-ink);
}

.div-04 *,
.div-04 *::before,
.div-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-04__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 22px;
  padding: clamp(24px,5vw,60px) clamp(20px,5vw,56px);
  background: radial-gradient(90% 70% at 50% 0%,oklch(1 0 0),transparent);
}

.div-04__card {
  width: min(92vw,392px);
  background: var(--div-04-card);
  border: 1px solid var(--div-04-line);
  border-radius: 18px;
  padding: clamp(24px,4vw,32px);
  box-shadow: 0 18px 44px oklch(0.24 0.02 260/.09);
  display: grid;
  gap: 16px;
}

.div-04__title {
  font-size: 21px;
  font-weight: 680;
  letter-spacing: -.02em;
  text-align: center;
  margin-bottom: 2px;
}

.div-04__oauth,
.div-04__email {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  min-height: 46px;
  width: 100%;
  border-radius: 11px;
  font-size: 14.5px;
  font-weight: 600;
  cursor: pointer;
  font-family: inherit;
  transition: background .18s ease,border-color .18s ease,transform .18s ease;
}

.div-04__oauth {
  background: var(--div-04-card);
  border: 1px solid var(--div-04-line);
  color: var(--div-04-ink);
}

.div-04__oauth:hover {
  background: oklch(0.97 0.004 260);
}

.div-04__email {
  background: var(--div-04-acc);
  border: 1px solid transparent;
  color: oklch(0.99 0.01 268);
}

.div-04__email:hover {
  background: oklch(0.46 0.17 268);
}

.div-04__oauth:active,
.div-04__email:active {
  transform: translateY(1px);
}

.div-04__oauth:focus-visible,
.div-04__email:focus-visible {
  outline: 2px solid var(--div-04-acc);
  outline-offset: 2px;
}

.div-04__or {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 11.5px;
  font-weight: 650;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--div-04-mut);
}

.div-04__or::before,
.div-04__or::after {
  content: '';
  flex: 1 1 0;
  height: 1px;
  background: var(--div-04-line);
}

.div-04__variants {
  display: grid;
  gap: 14px;
  margin-top: 6px;
  padding-top: 16px;
  border-top: 1px dashed var(--div-04-line);
}

.div-04__grid {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 12px;
}

.div-04__rule {
  height: 1px;
  background: linear-gradient(90deg,transparent,var(--div-04-line));
}

.div-04__grid .div-04__rule:last-child {
  background: linear-gradient(90deg,var(--div-04-line),transparent);
}

.div-04__word {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  color: var(--div-04-mut);
  letter-spacing: .04em;
}

.div-04__bimg {
  display: flex;
  justify-content: center;
  border-top: 1px solid transparent;
  border-image: linear-gradient(90deg,transparent,var(--div-04-acc),transparent) 1;
  padding-top: 12px;
}

.div-04__bimg span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  color: var(--div-04-mut);
}

.div-04__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-04-mut);
  padding: 8px 14px;
  border: 1px solid var(--div-04-line);
  border-radius: 99px;
  text-align: center;
  max-width: 92vw;
}

@media (prefers-reduced-motion: reduce) {
  .div-04 * {
    transition-duration: .01ms !important;
  }
}
```

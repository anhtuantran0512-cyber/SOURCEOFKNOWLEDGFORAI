---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/sign-in-with-google-apple-github-buttons/"
title: "Sign In with Google Apple GitHub Buttons"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "The provider button set on its own — no email field, no divider, no form wrapper."
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sign In with Google Apple GitHub Buttons
Source: https://codefronts.com/snippets/css-social-buttons/sign-in-with-google-apple-github-buttons/

The provider button set on its own — no email field, no divider, no form wrapper. Three full-width blocks with the mark pinned left and the label optically centred, each on the surface its provider expects: a bordered white block, a true black block, and a dark slate block. Sized as real auth targets at 3.25rem with focus rings that survive on every surface.
## HTML
```html
<div class="soc-11">
  <div class="soc-11__stage">
    <div class="soc-11__card">
      <h2 class="soc-11__title">Continue to your workspace</h2>
      <p class="soc-11__sub">Use the account you already have.</p>
      <div class="soc-11__set">
        <button class="soc-11__btn" type="button" style="--surface:#ffffff;--fg:#1f1f22;--edge:#dcdce2;--ring:#3d63ff">
          <span class="soc-11__mark" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke-width="2.6" stroke-linecap="round"><path d="M12 3.6a8.4 8.4 0 1 0 8.2 10.2" stroke="#4285f4"/><path d="M12 3.6a8.4 8.4 0 0 1 5.9 2.4" stroke="#ea4335"/><path d="M3.6 12a8.4 8.4 0 0 1 2.5-5.9" stroke="#fbbc05"/><path d="M6.1 17.9a8.4 8.4 0 0 0 11.8 0" stroke="#34a853"/><path d="M12.6 12h7.6" stroke="#4285f4"/></svg>
          </span>
          <span class="soc-11__label">Continue with Google</span>
        </button>
        <button class="soc-11__btn" type="button" style="--surface:#000000;--fg:#ffffff;--edge:#000000;--ring:#8ab4ff">
          <span class="soc-11__mark" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 6.3c-2.4 0-4.4 2.1-4.4 5.2 0 3.6 2.2 7.2 4.4 7.2s4.4-3.6 4.4-7.2c0-3.1-2-5.2-4.4-5.2Z"/><path d="M12.4 5.6c1.1-.2 2-1.2 2.1-2.4-1.1.1-2.2 1-2.4 2 0 .2 0 .3.3.4Z"/></svg>
          </span>
          <span class="soc-11__label">Continue with Apple</span>
        </button>
        <button class="soc-11__btn" type="button" style="--surface:#1c2128;--fg:#f0f3f6;--edge:#30363d;--ring:#8ab4ff">
          <span class="soc-11__mark" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.6"/><path d="m9.8 9.4-2.3 2.6 2.3 2.6"/><path d="m14.2 9.4 2.3 2.6-2.3 2.6"/></svg>
          </span>
          <span class="soc-11__label">Continue with GitHub</span>
        </button>
      </div>
      <p class="soc-11__foot">Buttons only — the surrounding form is yours to build.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-11 {
  --bg: #f4f4f6;
  --card: #ffffff;
  --ink: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --h: 3.25rem;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .soc-11 {
    --bg: oklch(96.4% .003 285);
    --card: oklch(100% 0 0);
    --ink: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-11:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --card: #131318;
    --ink: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
  }
}

.soc-11[data-theme="dark"] {
  --bg: #0a0a0d;
  --card: #131318;
  --ink: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
}

.soc-11,
.soc-11 *,
.soc-11 *::before,
.soc-11 *::after {
  box-sizing: border-box;
}

.soc-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-11__card {
  inline-size: min(24rem,100%);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.35rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 22px 48px -30px rgb(9 9 20/.45);
}

.soc-11__title {
  margin: 0 0 .35rem;
  font-size: 1.3rem;
  font-weight: 600;
  letter-spacing: -.025em;
}

.soc-11__sub {
  margin: 0 0 1.6rem;
  font-size: .88rem;
  color: var(--muted);
}

.soc-11__set {
  display: grid;
  gap: .65rem;
}

.soc-11__btn {
  display: grid;
  grid-template-columns: 1.35rem 1fr 1.35rem;
  align-items: center;
  gap: .75rem;
  min-block-size: var(--h);
  padding: 0 1rem;
  cursor: pointer;
  min-inline-size: 0;
  border: 1px solid var(--edge);
  border-radius: .9rem;
  background: var(--surface);
  color: var(--fg);
  font: inherit;
  font-size: .95rem;
  font-weight: 550;
  letter-spacing: -.01em;
  box-shadow: 0 1px 2px rgb(0 0 0/.05);
  transition: translate .18s cubic-bezier(.16,1,.3,1), filter .18s ease, box-shadow .18s ease;
}

.soc-11__mark {
  display: grid;
  place-items: center;
}

.soc-11__mark svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
}

.soc-11__label {
  min-inline-size: 0;
  overflow-wrap: anywhere;
  text-align: center;
}

.soc-11__btn:hover {
  translate: 0 -2px;
  filter: brightness(.97);
  box-shadow: 0 12px 26px -18px rgb(9 9 20/.6);
}

.soc-11__btn:active {
  translate: 0 1px;
  filter: brightness(.94);
}

.soc-11__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-11__foot {
  margin: 1.5rem 0 0;
  font-size: .75rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .soc-11__btn {
    transition-duration: 1ms;
  }

  .soc-11__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-11__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .soc-11__mark svg {
    stroke: ButtonText;
    fill: ButtonText;
  }
}
```

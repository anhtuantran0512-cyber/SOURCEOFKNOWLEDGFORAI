---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/biometric-prompt/"
title: "Biometric Prompt"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "A PWA-style face / touch-ID prompt: a large centred biometric glyph with soft concentric pulse ripples signalling the app is listening — the clean, minimal…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Biometric Prompt
Source: https://codefronts.com/components/css-login-forms/biometric-prompt/

A PWA-style face / touch-ID prompt: a large centred biometric glyph with soft concentric pulse ripples signalling the app is listening — the clean, minimal native-feel authentication moment.
## HTML
```html
<section class="lf-30">
  <div class="lf-30__card">
    <h1 class="lf-30__h">Confirm it's you</h1>
    <p class="lf-30__sub">Use Face ID or your fingerprint to sign in.</p>
    <button class="lf-30__target" type="button" aria-label="Authenticate with biometrics">
      <span class="lf-30__ripple" aria-hidden="true"></span>
      <span class="lf-30__ripple lf-30__ripple--2" aria-hidden="true"></span>
      <svg class="lf-30__glyph" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" d="M5 11a7 7 0 0 1 14 0M7.5 12.5a4.5 4.5 0 0 1 9 0v1.5M12 12v4M9.5 15v1.5M14.5 14.5V17M4.5 14v1"/></svg>
    </button>
    <p class="lf-30__status" role="status" aria-live="polite">Waiting for authentication…</p>
    <a class="lf-30__fallback" href="#">Use passcode instead</a>
  </div>
</section>
```
## CSS
```css
.lf-30,
.lf-30 *,
.lf-30 *::before,
.lf-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-30 {
  --accent: oklch(0.62 0.16 250);
  --radius: 14px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #0f1220;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-30__card {
  width: min(340px,100%);
  background: #171a2b;
  border: 1px solid #262b40;
  border-radius: 22px;
  padding: 38px 30px;
  text-align: center;
  box-shadow: 0 30px 70px -44px #000;
  color: #e9ecf7;
}

.lf-30__h {
  font-size: 22px;
  font-weight: 700;
}

.lf-30__sub {
  font-size: 13.5px;
  color: #9298b3;
  margin: 6px 0 30px;
  line-height: 1.5;
}

.lf-30__target {
  position: relative;
  width: 104px;
  height: 104px;
  margin: 0 auto 26px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  background: oklch(0.62 0.16 250/.14);
  color: var(--accent);
  transition: transform .14s,background .18s;
}

.lf-30__target:hover {
  background: oklch(0.62 0.16 250/.22);
}

.lf-30__target:active {
  transform: scale(.94);
}

.lf-30__target:focus-visible {
  outline: 3px solid oklch(0.62 0.16 250/.6);
  outline-offset: 4px;
}

.lf-30__ripple {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 2px solid var(--accent);
  opacity: 0;
  animation: lf-30-pulse 2.4s ease-out infinite;
}

.lf-30__ripple--2 {
  animation-delay: 1.2s;
}

.lf-30__glyph {
  position: relative;
  width: 52px;
  height: 52px;
}

.lf-30__status {
  font-size: 12.5px;
  color: #7f86a3;
  margin-bottom: 20px;
}

.lf-30__fallback {
  font-size: 13.5px;
  color: var(--accent);
  font-weight: 600;
  text-decoration: none;
}

.lf-30__fallback:hover {
  text-decoration: underline;
}

@keyframes lf-30-pulse {
  0% {
    transform: scale(.7);
    opacity: .7;
  }

  80%,
    100% {
    transform: scale(1.5);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-30__ripple {
    animation: none;
    opacity: .4;
    inset: -6px;
  }

  .lf-30__ripple--2 {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — concentric ripple rings pulse via a transform/opacity @keyframes; a passcode fallback is always offered. */
```

---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/vault-lock/"
title: "Vault Lock"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "An ironclad, industrial login for banking and secure-storage apps: flat metallic tones, geometric borders, a lock crest, and a crisp crimson error state that…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vault Lock
Source: https://codefronts.com/components/css-login-forms/vault-lock/

An ironclad, industrial login for banking and secure-storage apps: flat metallic tones, geometric borders, a lock crest, and a crisp crimson error state that flashes when a field is left invalid.
## HTML
```html
<section class="lf-22">
  <form class="lf-22__vault" novalidate>
    <div class="lf-22__crest" aria-hidden="true">🔒</div>
    <h1 class="lf-22__h">Secure Vault Access</h1>
    <p class="lf-22__sub">Authorised personnel only.</p>
    <div class="lf-22__field">
      <label class="lf-22__label" for="lf-22-acct">Account ID</label>
      <input id="lf-22-acct" type="text" inputmode="numeric" pattern="[0-9]{6,}" placeholder="000000" required>
      <span class="lf-22__err" role="alert">Enter a valid 6+ digit account ID.</span>
    </div>
    <div class="lf-22__field">
      <label class="lf-22__label" for="lf-22-pin">Passphrase</label>
      <input id="lf-22-pin" type="password" autocomplete="current-password" placeholder="••••••••" required minlength="8">
      <span class="lf-22__err" role="alert">Passphrase must be at least 8 characters.</span>
    </div>
    <button class="lf-22__submit" type="submit">Unlock</button>
  </form>
</section>
```
## CSS
```css
.lf-22,
.lf-22 *,
.lf-22 *::before,
.lf-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-22 {
  --steel: #1c222c;
  --line: #333c49;
  --accent: oklch(0.72 0.14 210);
  --danger: oklch(0.62 0.2 25);
  --radius: 6px;
  --field-h: 48px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #0d1015;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-22__vault {
  width: min(370px,100%);
  background: var(--steel);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 32px 30px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 30px 70px -40px #000,inset 0 1px 0 rgba(255,255,255,.05);
}

.lf-22__crest {
  width: 52px;
  height: 52px;
  display: grid;
  place-items: center;
  border: 2px solid var(--line);
  border-radius: 10px;
  font-size: 24px;
  background: #141922;
}

.lf-22__h {
  font-size: 20px;
  font-weight: 700;
  color: #e8edf3;
  letter-spacing: .01em;
}

.lf-22__sub {
  font-size: 12.5px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #6b7688;
  margin-top: -10px;
}

.lf-22__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
  animation-fill-mode: both;
}

.lf-22__label {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: #9aa6b8;
}

.lf-22__field input {
  height: var(--field-h);
  border: 1.5px solid var(--line);
  border-radius: var(--radius);
  padding: 0 14px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 15px;
  letter-spacing: .08em;
  color: #e8edf3;
  background: #12161e;
  transition: border-color .18s,box-shadow .18s;
}

.lf-22__field input::placeholder {
  color: #4d586a;
  letter-spacing: .15em;
}

.lf-22__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px oklch(0.72 0.14 210/.25);
}

.lf-22__err {
  font-size: 12px;
  color: var(--danger);
  font-weight: 600;
  opacity: 0;
  height: 0;
  overflow: hidden;
  transition: opacity .2s;
}

.lf-22__field input:not(:focus):invalid:not(:placeholder-shown) {
  border-color: var(--danger);
  box-shadow: 0 0 0 3px oklch(0.62 0.2 25/.22);
  animation: lf-22-shake .4s;
}

.lf-22__field input:not(:focus):invalid:not(:placeholder-shown) ~ .lf-22__err {
  opacity: 1;
  height: auto;
}

.lf-22__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 1px solid var(--accent);
  border-radius: var(--radius);
  cursor: pointer;
  background: oklch(0.72 0.14 210/.14);
  color: #dff2fb;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  transition: background .18s,transform .12s;
}

.lf-22__submit:hover {
  background: oklch(0.72 0.14 210/.24);
}

.lf-22__submit:active {
  transform: scale(.985);
}

.lf-22__submit:focus-visible {
  outline: 3px solid oklch(0.72 0.14 210/.55);
  outline-offset: 2px;
}

@keyframes lf-22-shake {
  0%,
    100% {
    transform: translateX(0);
  }

  20% {
    transform: translateX(-6px);
  }

  40% {
    transform: translateX(6px);
  }

  60% {
    transform: translateX(-4px);
  }

  80% {
    transform: translateX(4px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-22__field input:not(:focus):invalid:not(:placeholder-shown) {
    animation: none;
  }

  .lf-22 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — :invalid drives the crimson error state and a transform-only shake after blur. */
```

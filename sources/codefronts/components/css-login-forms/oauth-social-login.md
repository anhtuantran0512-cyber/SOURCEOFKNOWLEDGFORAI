---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/oauth-social-login/"
title: "OAuth Social Login"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "OAuth-first done right: prominent Google and GitHub buttons up top with crisp inline SVG logos, an \"or continue with email\" divider, and the email field…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: OAuth Social Login
Source: https://codefronts.com/components/css-login-forms/oauth-social-login/

OAuth-first done right: prominent Google and GitHub buttons up top with crisp inline SVG logos, an "or continue with email" divider, and the email field tucked neatly beneath for those who want it.
## HTML
```html
<section class="lf-06">
  <form class="lf-06__card" novalidate>
    <h1 class="lf-06__h">Log in to Orbit</h1>
    <button class="lf-06__soc" type="button">
      <svg class="lf-06__ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M23 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.2a5.3 5.3 0 0 1-2.3 3.5v2.9h3.7C21.8 19 23 15.9 23 12.3z"/><path fill="#34A853" d="M12 24c3.1 0 5.7-1 7.6-2.8l-3.7-2.9c-1 .7-2.4 1.1-3.9 1.1-3 0-5.5-2-6.4-4.7H1.7v3A12 12 0 0 0 12 24z"/><path fill="#FBBC05" d="M5.6 14.7a7.2 7.2 0 0 1 0-4.6v-3H1.7a12 12 0 0 0 0 10.6l3.9-3z"/><path fill="#EA4335" d="M12 4.8c1.7 0 3.2.6 4.4 1.7l3.3-3.3A12 12 0 0 0 1.7 6.4l3.9 3C6.5 6.8 9 4.8 12 4.8z"/></svg>
      Continue with Google
    </button>
    <button class="lf-06__soc" type="button">
      <svg class="lf-06__ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="#181717" d="M12 .5A12 12 0 0 0 8.2 23.9c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.6-1.4-1.3-1.8-1.3-1.8-1.1-.7 0-.7 0-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2 0-.4-.5-1.6.2-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.3 5 18.3 5.3 18.3 5.3c.7 1.6.2 2.8.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5z"/></svg>
      Continue with GitHub
    </button>
    <div class="lf-06__divider"><span>or continue with email</span></div>
    <label class="lf-06__field"><span class="lf-06__vh">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required></label>
    <label class="lf-06__field"><span class="lf-06__vh">Password</span>
      <input type="password" autocomplete="current-password" placeholder="Password" required></label>
    <button class="lf-06__submit" type="submit">Log in</button>
  </form>
</section>
```
## CSS
```css
.lf-06,
.lf-06 *,
.lf-06 *::before,
.lf-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-06 {
  --accent: oklch(0.5 0.16 265);
  --radius: 11px;
  --field-h: 48px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #f4f5f9;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-06__card {
  width: min(360px,100%);
  background: #fff;
  border: 1px solid #e6e8f0;
  border-radius: 16px;
  padding: 32px 28px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: 0 22px 50px -38px rgba(16,24,60,.5);
}

.lf-06__h {
  font-size: 22px;
  font-weight: 700;
  color: #161c2e;
  text-align: center;
  margin-bottom: 6px;
}

.lf-06__soc {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 11px;
  height: var(--field-h);
  border: 1.5px solid #dde1ec;
  border-radius: var(--radius);
  cursor: pointer;
  background: #fff;
  color: #232a40;
  font-size: 14.5px;
  font-weight: 600;
  transition: background .16s,transform .12s,border-color .16s;
}

.lf-06__soc:hover {
  background: #f7f8fc;
  border-color: #c6ccdd;
  transform: translateY(-1px);
}

.lf-06__soc:active {
  transform: translateY(0);
}

.lf-06__soc:focus-visible {
  outline: 3px solid oklch(0.5 0.16 265/.45);
  outline-offset: 2px;
}

.lf-06__ic {
  width: 19px;
  height: 19px;
  flex: none;
}

.lf-06__divider {
  display: flex;
  align-items: center;
  gap: 12px;
  color: #8a91a8;
  font-size: 12px;
  margin: 4px 0;
}

.lf-06__divider::before,
.lf-06__divider::after {
  content: "";
  flex: 1;
  height: 1px;
  background: #e6e8f0;
}

.lf-06__field input {
  width: 100%;
  height: var(--field-h);
  border: 1.5px solid #dde1ec;
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 14.5px;
  color: #161c2e;
  background: #fbfbfe;
  transition: border-color .18s,box-shadow .18s;
}

.lf-06__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.lf-06__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.5 0.16 265/.16);
}

.lf-06__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  transition: filter .18s,transform .12s;
}

.lf-06__submit:hover {
  filter: brightness(1.08);
}

.lf-06__submit:active {
  transform: scale(.985);
}

.lf-06__submit:focus-visible {
  outline: 3px solid oklch(0.5 0.16 265/.5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .lf-06 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — OAuth buttons carry inline brand SVGs; the divider uses flex pseudo-element lines. */
```

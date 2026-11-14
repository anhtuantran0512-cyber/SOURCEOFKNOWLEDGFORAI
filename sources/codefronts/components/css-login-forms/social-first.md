---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/social-first/"
title: "Social First"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "Consumer-mobile onboarding that leads with big, brand-compliant social sign-in blocks — Apple, Google, Facebook — stacked full-width for instant one-tap…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Social First
Source: https://codefronts.com/components/css-login-forms/social-first/

Consumer-mobile onboarding that leads with big, brand-compliant social sign-in blocks — Apple, Google, Facebook — stacked full-width for instant one-tap entry, with the email path pushed politely below.
## HTML
```html
<section class="lf-16">
  <div class="lf-16__card">
    <div class="lf-16__logo" aria-hidden="true">✳</div>
    <h1 class="lf-16__h">Join Frame</h1>
    <p class="lf-16__sub">Create your account in one tap.</p>
    <div class="lf-16__stack">
      <button class="lf-16__btn lf-16__btn--apple" type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.4 12.6c0-2.3 1.9-3.4 2-3.5-1.1-1.6-2.8-1.8-3.4-1.8-1.4-.1-2.8.9-3.5.9s-1.8-.8-3-.8c-1.5 0-3 .9-3.8 2.3-1.6 2.8-.4 7 1.2 9.3.8 1.1 1.7 2.4 2.9 2.3 1.2 0 1.6-.7 3-.7s1.8.7 3 .7 2-1 2.8-2.1c.9-1.3 1.2-2.5 1.3-2.6-.1 0-2.5-1-2.5-3.7zM14.2 5.6c.6-.8 1-1.9.9-3-.9 0-2 .6-2.7 1.4-.6.7-1.1 1.8-.9 2.9 1 0 2-.5 2.7-1.3z"/></svg>Continue with Apple</button>
      <button class="lf-16__btn lf-16__btn--google" type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M23 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.2a5.3 5.3 0 0 1-2.3 3.5v2.9h3.7C21.8 19 23 15.9 23 12.3z"/><path fill="#34A853" d="M12 24c3.1 0 5.7-1 7.6-2.8l-3.7-2.9c-1 .7-2.4 1.1-3.9 1.1-3 0-5.5-2-6.4-4.7H1.7v3A12 12 0 0 0 12 24z"/><path fill="#FBBC05" d="M5.6 14.7a7.2 7.2 0 0 1 0-4.6v-3H1.7a12 12 0 0 0 0 10.6l3.9-3z"/><path fill="#EA4335" d="M12 4.8c1.7 0 3.2.6 4.4 1.7l3.3-3.3A12 12 0 0 0 1.7 6.4l3.9 3C6.5 6.8 9 4.8 12 4.8z"/></svg>Continue with Google</button>
      <button class="lf-16__btn lf-16__btn--fb" type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7v-3.5h3.1V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9v2.2h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/></svg>Continue with Facebook</button>
    </div>
    <a class="lf-16__email" href="#">or sign up with email</a>
  </div>
</section>
```
## CSS
```css
.lf-16,
.lf-16 *,
.lf-16 *::before,
.lf-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-16 {
  --tap: 52px;
  --radius: 12px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #f4f4f7;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-16__card {
  width: min(360px,100%);
  background: #fff;
  border: 1px solid #eaeaef;
  border-radius: 20px;
  padding: 36px 28px;
  text-align: center;
  box-shadow: 0 22px 50px -38px rgba(20,20,40,.5);
}

.lf-16__logo {
  font-size: 34px;
  margin-bottom: 8px;
}

.lf-16__h {
  font-size: 24px;
  font-weight: 700;
  color: #16171f;
}

.lf-16__sub {
  font-size: 14px;
  color: #767889;
  margin: 5px 0 22px;
}

.lf-16__stack {
  display: flex;
  flex-direction: column;
  gap: 11px;
}

.lf-16__btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 11px;
  height: var(--tap);
  border-radius: var(--radius);
  cursor: pointer;
  font-size: 15px;
  font-weight: 600;
  border: 1px solid transparent;
  transition: filter .16s,transform .12s,background .16s;
}

.lf-16__btn svg {
  width: 20px;
  height: 20px;
  flex: none;
}

.lf-16__btn:active {
  transform: scale(.986);
}

.lf-16__btn--apple {
  background: #000;
  color: #fff;
}

.lf-16__btn--apple:hover {
  filter: brightness(1.15);
}

.lf-16__btn--google {
  background: #fff;
  color: #3c4043;
  border-color: #dadce0;
}

.lf-16__btn--google:hover {
  background: #f7f8fa;
}

.lf-16__btn--fb {
  background: #1877f2;
  color: #fff;
}

.lf-16__btn--fb:hover {
  filter: brightness(1.05);
}

.lf-16__btn:focus-visible {
  outline: 3px solid oklch(0.6 0.16 250/.6);
  outline-offset: 2px;
}

.lf-16__email {
  display: inline-block;
  margin-top: 20px;
  font-size: 13.5px;
  color: #767889;
  text-decoration: none;
  font-weight: 500;
}

.lf-16__email:hover {
  color: #16171f;
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .lf-16 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — brand-compliant social buttons in a gap-spaced flex stack with 52px tap targets. */
```

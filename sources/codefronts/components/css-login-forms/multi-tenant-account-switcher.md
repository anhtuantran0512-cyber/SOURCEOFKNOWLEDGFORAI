---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/multi-tenant-account-switcher/"
title: "Multi-Tenant Account Switcher"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The B2B enterprise entry screen (think Slack or AWS): a returning user picks which workspace / client org to enter from a stack of profile cards, each with…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Tenant Account Switcher
Source: https://codefronts.com/components/css-login-forms/multi-tenant-account-switcher/

The B2B enterprise entry screen (think Slack or AWS): a returning user picks which workspace / client org to enter from a stack of profile cards, each with an avatar and a role badge, plus a link to add another account.
## HTML
```html
<section class="lf-02">
  <div class="lf-02__card">
    <header class="lf-02__head">
      <h1 class="lf-02__h">Choose a workspace</h1>
      <p class="lf-02__sub">You're signed in as [email protected]</p>
    </header>
    <ul class="lf-02__list">
      <li class="lf-02__item" style="--tint:264">
        <a class="lf-02__row" href="#">
          <span class="lf-02__av" aria-hidden="true">LM</span>
          <span class="lf-02__meta"><span class="lf-02__name">Lumen Design</span><span class="lf-02__email">lumen.slack.com</span></span>
          <span class="lf-02__badge">Owner</span>
        </a>
      </li>
      <li class="lf-02__item" style="--tint:160">
        <a class="lf-02__row" href="#">
          <span class="lf-02__av" aria-hidden="true">AC</span>
          <span class="lf-02__meta"><span class="lf-02__name">Acme Corp</span><span class="lf-02__email">acme.slack.com</span></span>
          <span class="lf-02__badge lf-02__badge--admin">Admin</span>
        </a>
      </li>
      <li class="lf-02__item" style="--tint:30">
        <a class="lf-02__row" href="#">
          <span class="lf-02__av" aria-hidden="true">NW</span>
          <span class="lf-02__meta"><span class="lf-02__name">Northwind</span><span class="lf-02__email">northwind.slack.com</span></span>
          <span class="lf-02__badge lf-02__badge--member">Member</span>
        </a>
      </li>
    </ul>
    <a class="lf-02__add" href="#"><span aria-hidden="true">+</span> Add another account</a>
  </div>
</section>
```
## CSS
```css
.lf-02,
.lf-02 *,
.lf-02 *::before,
.lf-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-02 {
  --accent: oklch(0.58 0.19 264);
  --radius: 12px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #f4f5f9;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 20px;
}

.lf-02__card {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #e7e9f0;
  border-radius: 18px;
  padding: 26px 22px;
  box-shadow: 0 24px 56px -38px rgba(16,24,60,.55);
}

.lf-02__head {
  margin-bottom: 18px;
}

.lf-02__h {
  font-size: 20px;
  font-weight: 700;
  color: #161c2e;
  letter-spacing: -.01em;
}

.lf-02__sub {
  font-size: 13px;
  color: #767d97;
  margin-top: 4px;
}

.lf-02__list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.lf-02__row {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 11px 12px;
  border-radius: var(--radius);
  text-decoration: none;
  border: 1px solid transparent;
  transition: transform .16s,background .16s,border-color .16s;
}

.lf-02__row:hover {
  background: oklch(var(--tint,264) 100% 0% /0);
  background: color-mix(in oklch,oklch(0.58 0.16 var(--tint)) 8%,#fff);
  border-color: color-mix(in oklch,oklch(0.58 0.16 var(--tint)) 30%,#fff);
  transform: translateX(3px);
}

.lf-02__row:focus-visible {
  outline: 3px solid color-mix(in oklch,oklch(0.58 0.19 var(--tint)) 55%,#fff);
  outline-offset: 2px;
}

.lf-02__av {
  flex: none;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  background: oklch(0.58 0.16 var(--tint));
}

.lf-02__meta {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.lf-02__name {
  font-size: 15px;
  font-weight: 600;
  color: #1a2135;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.lf-02__email {
  font-size: 12.5px;
  color: #8a91aa;
}

.lf-02__badge {
  flex: none;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .02em;
  padding: 4px 9px;
  border-radius: 999px;
  color: oklch(0.45 0.16 var(--tint));
  background: color-mix(in oklch,oklch(0.58 0.16 var(--tint)) 16%,#fff);
}

.lf-02__badge--admin {
  --tint: 160;
}

.lf-02__badge--member {
  --tint: 30;
}

.lf-02__add {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  margin-top: 16px;
  padding: 11px;
  border-radius: var(--radius);
  border: 1.5px dashed #cfd4e2;
  color: #5a6180;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  transition: border-color .16s,color .16s;
}

.lf-02__add:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.lf-02__add:focus-visible {
  outline: 3px solid oklch(0.58 0.19 264/.5);
  outline-offset: 2px;
}

.lf-02__add span {
  font-size: 17px;
  line-height: 1;
}

@media (prefers-reduced-motion: reduce) {
  .lf-02 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — a semantic list of workspace links tinted per row via a --tint custom property. */
```

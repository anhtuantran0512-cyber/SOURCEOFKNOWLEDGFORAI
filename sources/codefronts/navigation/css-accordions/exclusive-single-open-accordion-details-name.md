---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/exclusive-single-open-accordion-details-name/"
title: "Exclusive Single-Open Accordion with the details name Attribute (Close Others Automatically)"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Opening one section automatically closes the rest — with ONE html attribute, zero JavaScript."
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Exclusive Single-Open Accordion with the details name Attribute (Close Others Automatically)
Source: https://codefronts.com/navigation/css-accordions/exclusive-single-open-accordion-details-name/

Opening one section automatically closes the rest — with ONE html attribute, zero JavaScript. The native name attribute on <details> gives radio-group behavior for settings pages and dashboards, demonstrated here as a billing settings panel with animated open state and an active-section indicator bar.
## HTML
```html
<section class="acc-06" aria-label="Exclusive single-open accordion demo">
  <div class="acc-06__wrap">
    <h3 class="acc-06__title">Workspace settings</h3>
    <p class="acc-06__sub">One section open at a time — the <code>name</code> attribute handles it natively.</p>
    <details class="acc-06__item" name="acc-06-settings" open>
      <summary class="acc-06__sum"><span class="acc-06__ic">💳</span><span class="acc-06__lab">Billing<small>Plan, invoices &amp; payment method</small></span><span class="acc-06__chev"></span></summary>
      <div class="acc-06__body"><p>You're on the <b>Team</b> plan, billed annually. Next invoice: <b>Aug 12, 2026</b> · $432. Payment method Visa •• 4242.</p><button type="button" class="acc-06__btn">Manage billing</button></div>
    </details>
    <details class="acc-06__item" name="acc-06-settings">
      <summary class="acc-06__sum"><span class="acc-06__ic">👥</span><span class="acc-06__lab">Members<small>Invites, roles &amp; permissions</small></span><span class="acc-06__chev"></span></summary>
      <div class="acc-06__body"><p>18 members · 3 pending invites. Default role for new members is <b>Editor</b>; guests can view shared projects only.</p><button type="button" class="acc-06__btn">Invite people</button></div>
    </details>
    <details class="acc-06__item" name="acc-06-settings">
      <summary class="acc-06__sum"><span class="acc-06__ic">🔒</span><span class="acc-06__lab">Security<small>SSO, 2FA &amp; session policy</small></span><span class="acc-06__chev"></span></summary>
      <div class="acc-06__body"><p>SAML SSO is <b>enabled</b> (Okta). Two-factor is required for admins. Sessions expire after 30 days of inactivity.</p><button type="button" class="acc-06__btn">Review policy</button></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-06,
.acc-06 *,
.acc-06 *::before,
.acc-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-06 {
  --accent: oklch(0.6 0.14 220);
  interpolate-size: allow-keywords;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eef3f6;
  padding: 40px 20px;
}

.acc-06__wrap {
  width: min(560px,100%);
  background: #fff;
  border-radius: 18px;
  padding: 34px 32px;
  box-shadow: 0 24px 60px -34px rgba(20,50,70,.35);
}

.acc-06__title {
  font-size: 24px;
  font-weight: 800;
  color: #152430;
  letter-spacing: -.02em;
}

.acc-06__sub {
  font-size: 13.5px;
  color: #5e7284;
  margin: 6px 0 18px;
}

.acc-06__sub code {
  font-family: ui-monospace,Menlo,monospace;
  background: #e8f0f5;
  padding: 1px 5px;
  border-radius: 4px;
  font-size: .9em;
}

.acc-06__item {
  position: relative;
  border: 1.5px solid #e2eaf0;
  border-radius: 14px;
  margin-bottom: 10px;
  overflow: clip;
  transition: border-color .25s;
}

.acc-06__item::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: var(--accent);
  transform: scaleY(0);
  transform-origin: top;
  transition: transform .3s;
}

.acc-06__item[open] {
  border-color: oklch(0.6 0.14 220 / .5);
}

.acc-06__item[open]::before {
  transform: scaleY(1);
}

.acc-06__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 64px;
  padding: 8px 18px;
  cursor: pointer;
}

.acc-06__sum::-webkit-details-marker {
  display: none;
}

.acc-06__sum::marker {
  content: "";
}

.acc-06__ic {
  font-size: 20px;
  flex: none;
}

.acc-06__lab {
  display: flex;
  flex-direction: column;
  gap: 2px;
  font-size: 15.5px;
  font-weight: 700;
  color: #152430;
}

.acc-06__lab small {
  font-size: 12.5px;
  font-weight: 500;
  color: #7189a0;
}

.acc-06__item[open] .acc-06__lab {
  color: var(--accent);
}

.acc-06__chev {
  margin-left: auto;
  width: 9px;
  height: 9px;
  border-right: 2.5px solid #93a9bd;
  border-bottom: 2.5px solid #93a9bd;
  transform: rotate(45deg) translateY(-2px);
  transition: transform .3s;
  flex: none;
}

.acc-06__item[open] .acc-06__chev {
  transform: rotate(225deg) translateY(-2px);
}

.acc-06__item::details-content {
  height: 0;
  overflow: clip;
  opacity: 0;
  transition: height .35s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .35s allow-discrete;
}

.acc-06__item[open]::details-content {
  height: auto;
  opacity: 1;
}

.acc-06__body {
  padding: 0 18px 18px 52px;
  font-size: 14.5px;
  line-height: 1.6;
  color: #43596d;
}

.acc-06__btn {
  margin-top: 12px;
  height: 40px;
  padding: 0 18px;
  border: 1.5px solid var(--accent);
  background: none;
  border-radius: 10px;
  color: var(--accent);
  font-size: 13.5px;
  font-weight: 700;
  cursor: pointer;
  transition: all .15s;
}

.acc-06__btn:hover {
  background: var(--accent);
  color: #fff;
}

.acc-06__sum:focus-visible,
.acc-06__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-06__item::details-content,
    .acc-06__chev,
    .acc-06__item::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the shared name="acc-06-settings" attribute makes the browser close the open panel whenever another opens, exactly like a radio group. Animation is the same ::details-content height transition as demo 05. */
```

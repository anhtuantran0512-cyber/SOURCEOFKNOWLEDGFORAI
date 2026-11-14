---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-expansion-panel-css/"
title: "Material Design Expansion Panel CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Standard accordion, icon-leading accordion with inline forms, and FAQ-style fully-rounded panels — interactive via the CSS checkbox-hack, zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Expansion Panel CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-expansion-panel-css/

Standard accordion, icon-leading accordion with inline forms, and FAQ-style fully-rounded panels — interactive via the CSS checkbox-hack, zero JavaScript.
## HTML
```html
<div class="md-11">

  <!-- Section 1: Standard accordion -->
  <h3>Standard Accordion</h3>
  <div class="accordion">

    <div class="acc-panel">
      <input class="acc-toggle" type="checkbox" id="a1">
      <label class="acc-header" for="a1">
        <span class="acc-title">Personal Information</span>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          <p>Manage your name, email address, phone number, and other personal details associated with your account.</p>
          <p>Changes to personal information may require verification before taking effect.</p>
        </div>
        <div class="acc-actions">
          <button class="acc-btn">Cancel</button>
          <button class="acc-btn acc-btn--filled">Save</button>
        </div>
      </div>
    </div>

    <div class="acc-panel">
      <input class="acc-toggle" type="checkbox" id="a2" checked>
      <label class="acc-header" for="a2">
        <span class="acc-title">Billing &amp; Payment</span>
        <span class="acc-meta">Visa ···4242</span>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          <p>Your current payment method is a Visa card ending in 4242, expiring 08/2027.</p>
          <p>You can add, remove, or update payment methods at any time. Changes will apply to all future charges.</p>
        </div>
        <div class="acc-actions">
          <button class="acc-btn">Add Method</button>
          <button class="acc-btn acc-btn--filled">Update</button>
        </div>
      </div>
    </div>

    <div class="acc-panel">
      <input class="acc-toggle" type="checkbox" id="a3">
      <label class="acc-header" for="a3">
        <span class="acc-title">Notifications</span>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          <p>Configure how and when you receive notifications — by email, push, or SMS. You can fine-tune per-category preferences.</p>
        </div>
      </div>
    </div>

    <div class="acc-panel">
      <input class="acc-toggle" type="checkbox" id="a4">
      <label class="acc-header" for="a4">
        <span class="acc-title">Privacy &amp; Security</span>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          <p>Review app permissions, manage connected accounts, set two-factor authentication, and download your data.</p>
        </div>
      </div>
    </div>

  </div>

  <!-- Section 2: With icons -->
  <h3>With Leading Icons</h3>
  <div class="accordion accordion--gap">

    <div class="acc-panel">
      <input class="acc-toggle" type="checkbox" id="b1">
      <label class="acc-header" for="b1">
        <span class="acc-icon-wrap">
          <svg viewBox="0 0 24 24"><path d="M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z"/></svg>
        </span>
        <div>
          <div class="acc-title">Account Settings</div>
          <div class="acc-subtitle">Profile, avatar, username</div>
        </div>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-form">
          <div class="field-row">
            <div class="field">
              <label>First name</label>
              <input type="text" value="Jordan">
            </div>
            <div class="field">
              <label>Last name</label>
              <input type="text" value="Smith">
            </div>
          </div>
          <div class="field">
            <label>Username</label>
            <input type="text" value="@jordan.smith">
          </div>
        </div>
        <div class="acc-actions">
          <button class="acc-btn acc-btn--filled">Update Profile</button>
        </div>
      </div>
    </div>

    <div class="acc-panel">
      <input class="acc-toggle" type="checkbox" id="b2">
      <label class="acc-header" for="b2">
        <span class="acc-icon-wrap">
          <svg viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>
        </span>
        <div>
          <div class="acc-title">Security</div>
          <div class="acc-subtitle">Password, 2FA, sessions</div>
        </div>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          <p>Last password change: 3 months ago. Two-factor authentication is currently <strong>disabled</strong>. We strongly recommend enabling it for your security.</p>
        </div>
        <div class="acc-actions">
          <button class="acc-btn">Change Password</button>
          <button class="acc-btn acc-btn--filled">Enable 2FA</button>
        </div>
      </div>
    </div>

    <div class="acc-panel">
      <input class="acc-toggle" type="checkbox" id="b3">
      <label class="acc-header" for="b3">
        <span class="acc-icon-wrap">
          <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </span>
        <div>
          <div class="acc-title">Notifications</div>
          <div class="acc-subtitle">Email, push, frequency</div>
        </div>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          <p>You're subscribed to weekly digests, product updates, and security alerts. Marketing emails are currently off.</p>
        </div>
        <div class="acc-actions">
          <button class="acc-btn acc-btn--filled">Manage</button>
        </div>
      </div>
    </div>

  </div>

  <!-- Section 3: FAQ style -->
  <h3>FAQ Style</h3>
  <div class="accordion accordion--gap">

    <div class="acc-panel acc-panel--rounded">
      <input class="acc-toggle" type="checkbox" id="c1">
      <label class="acc-header" for="c1">
        <span class="acc-title">How does billing work?</span>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          You are billed monthly on the date you subscribed. Upgrades are prorated and applied immediately; downgrades take effect at the next billing cycle.
        </div>
      </div>
    </div>

    <div class="acc-panel acc-panel--rounded">
      <input class="acc-toggle" type="checkbox" id="c2">
      <label class="acc-header" for="c2">
        <span class="acc-title">Can I cancel at any time?</span>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          Yes. You can cancel your subscription from the Account settings page. You'll retain access until the end of your current billing period — no partial refunds are issued.
        </div>
      </div>
    </div>

    <div class="acc-panel acc-panel--rounded">
      <input class="acc-toggle" type="checkbox" id="c3">
      <label class="acc-header" for="c3">
        <span class="acc-title">Is my data secure?</span>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          All data is encrypted at rest (AES-256) and in transit (TLS 1.3). We are SOC 2 Type II certified and undergo annual penetration testing.
        </div>
      </div>
    </div>

    <div class="acc-panel acc-panel--rounded">
      <input class="acc-toggle" type="checkbox" id="c4">
      <label class="acc-header" for="c4">
        <span class="acc-title">Do you offer a free trial?</span>
        <span class="acc-chevron"></span>
      </label>
      <div class="acc-body">
        <div class="acc-content">
          We offer a 14-day free trial on all paid plans. No credit card is required to start — you'll only be charged if you choose to continue after the trial ends.
        </div>
      </div>
    </div>

  </div>

</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

.md-11 {
  --primary: #5c6bc0;
  --primary-dark: #3949ab;
  --primary-light: #e8eaf6;
  --on-surface: #1c1b1f;
  --surface: #fffbfe;
  --surface-variant: #e7e0ec;
  --outline: #79747e;
  --outline-variant: #cac4d0;
  --error: #b3261e;
  all: unset;
  display: block;
  font-family: 'Roboto', sans-serif;
  background: #f3f3f7;
  padding: 32px 24px;
  box-sizing: border-box;
  color: var(--on-surface);
}

.md-11 *,
.md-11 *::before,
.md-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-11 h3 {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--outline);
  margin-bottom: 12px;
  margin-top: 32px;
}

.md-11 h3:first-child {
  margin-top: 0;
}
/* ── Accordion container ── */

.md-11 .accordion {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.md-11 .accordion--gap {
  gap: 8px;
}
/* Hide real checkbox */

.md-11 .acc-toggle {
  display: none;
}
/* Panel wrapper */

.md-11 .acc-panel {
  background: var(--surface);
  border: 1px solid var(--outline-variant);
  border-radius: 0;
  overflow: hidden;
  transition: box-shadow 200ms ease;
}

.md-11 .accordion .acc-panel:first-of-type {
  border-radius: 4px 4px 0 0;
}

.md-11 .accordion .acc-panel:last-of-type {
  border-radius: 0 0 4px 4px;
}

.md-11 .accordion .acc-panel:not(:first-of-type) {
  border-top: none;
}

.md-11 .accordion--gap .acc-panel {
  border-radius: 12px !important;
  border: 1px solid var(--outline-variant);
}
/* Expanded panel gets elevation */

.md-11 .acc-toggle:checked ~ .acc-panel,
.md-11 .acc-panel:has(.acc-toggle:checked) {
  box-shadow: 0 2px 8px rgba(0,0,0,.15);
  z-index: 1;
  position: relative;
}
/* Header / label */

.md-11 .acc-header {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 0 24px;
  min-height: 56px;
  cursor: pointer;
  user-select: none;
  position: relative;
  transition: background 150ms ease;
}

.md-11 .acc-header:hover {
  background: rgba(0,0,0,.04);
}

.md-11 .acc-header:active {
  background: rgba(0,0,0,.08);
}

.md-11 .acc-title {
  flex: 1;
  font-size: 15px;
  font-weight: 500;
  color: var(--on-surface);
  line-height: 1.4;
}

.md-11 .acc-subtitle {
  font-size: 12px;
  font-weight: 400;
  color: var(--outline);
  margin-top: 1px;
}

.md-11 .acc-meta {
  font-size: 13px;
  color: var(--outline);
  white-space: nowrap;
}

.md-11 .acc-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  fill: var(--primary);
}
/* Chevron arrow */

.md-11 .acc-chevron {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 250ms cubic-bezier(.4,0,.2,1);
  color: var(--outline);
}

.md-11 .acc-chevron::before {
  content: '';
  display: block;
  width: 10px;
  height: 10px;
  border-right: 2px solid currentColor;
  border-bottom: 2px solid currentColor;
  transform: rotate(45deg) translate(-2px,-2px);
  transition: transform 250ms cubic-bezier(.4,0,.2,1);
}
/* When checked: rotate chevron */

.md-11 .acc-toggle:checked + .acc-header .acc-chevron::before {
  transform: rotate(-135deg) translate(-2px,-2px);
}
/* For nested structure */

.md-11 .acc-panel:has(> .acc-toggle:checked) .acc-chevron::before {
  transform: rotate(-135deg) translate(-2px,-2px);
}
/* Collapsed content: height 0, no border */

.md-11 .acc-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 300ms cubic-bezier(.4,0,.2,1);
}

.md-11 .acc-toggle:checked ~ .acc-body,
.md-11 .acc-panel:has(> .acc-toggle:checked) > .acc-body {
  max-height: 600px;
}

.md-11 .acc-content {
  padding: 8px 24px 20px;
  border-top: 1px solid var(--outline-variant);
  font-size: 14px;
  line-height: 1.6;
  color: #49454f;
}

.md-11 .acc-content p {
  margin-bottom: 8px;
}

.md-11 .acc-content p:last-child {
  margin-bottom: 0;
}
/* Actions row inside panel */

.md-11 .acc-actions {
  display: flex;
  gap: 8px;
  padding: 12px 16px 4px;
  justify-content: flex-end;
}

.md-11 .acc-btn {
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: .3px;
  cursor: pointer;
  border: none;
  background: transparent;
  color: var(--primary);
  transition: background 150ms;
}

.md-11 .acc-btn:hover {
  background: var(--primary-light);
}

.md-11 .acc-btn--filled {
  background: var(--primary);
  color: #fff;
}

.md-11 .acc-btn--filled:hover {
  background: var(--primary-dark);
}
/* ── Variant: Filled / tonal ── */

.md-11 .acc-panel--tonal {
  background: var(--primary-light);
  border-color: transparent;
}

.md-11 .acc-panel--tonal .acc-content {
  background: #fff;
  border-top-color: var(--outline-variant);
}
/* ── Variant: Outlined rounded ── */

.md-11 .acc-panel--rounded {
  border-radius: 28px !important;
  overflow: hidden;
}

.md-11 .acc-panel--rounded .acc-header {
  padding: 0 20px;
  min-height: 52px;
}
/* ── Icon list variant ── */

.md-11 .acc-icon-wrap {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--primary-light);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.md-11 .acc-icon-wrap svg {
  width: 18px;
  height: 18px;
  fill: var(--primary);
}
/* ── Form inside panel ── */

.md-11 .acc-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 16px 24px 20px;
  border-top: 1px solid var(--outline-variant);
}

.md-11 .field {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.md-11 .field label {
  font-size: 12px;
  color: var(--outline);
  font-weight: 500;
}

.md-11 .field input,
.md-11 .field select {
  border: 1px solid var(--outline-variant);
  border-radius: 4px;
  padding: 10px 12px;
  font-size: 14px;
  font-family: inherit;
  outline: none;
  transition: border-color 150ms;
  background: var(--surface);
}

.md-11 .field input:focus,
.md-11 .field select:focus {
  border-color: var(--primary);
}

.md-11 .field-row {
  display: flex;
  gap: 12px;
}

.md-11 .field-row .field {
  flex: 1;
}

@media (prefers-reduced-motion: reduce) {
  .md-11 .acc-body,
    .md-11 .acc-chevron::before,
    .md-11 .acc-header,
    .md-11 .acc-btn {
    transition: none !important;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/jewelry-sign-in/"
title: "Jewelry Sign-in"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Jewelry boutique sign-in — champagne cream + obsidian black + rose gold."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Jewelry Sign-in
Source: https://codefronts.com/layouts/css-split-screen/jewelry-sign-in/

Jewelry boutique sign-in — champagne cream + obsidian black + rose gold. Brand on one side, sign-in form on the other. The kind of split-screen Tiffany would commission. Real <form> with proper labels and autocomplete tokens.
## HTML
```html
<section class="ss-jew" aria-label="Jewelry account sign-in">
  <aside class="ss-jew-brand">
    <span class="ss-jew-mark" aria-hidden="true"></span>
    <span class="ss-jew-since">EST. 1924</span>
    <h2><em>Maison</em><br />Aurelia.</h2>
    <p>Welcome back. Your private viewing room and saved pieces are one sign-in away.</p>
    <span class="ss-jew-divider" aria-hidden="true"></span>
    <span class="ss-jew-quote"><em>"Adorned with intent."</em></span>
  </aside>
  <article class="ss-jew-form-wrap">
    <header>
      <span class="ss-jew-eye">— Members only</span>
      <h3>Sign in to your account.</h3>
    </header>
    <form class="ss-jew-form">
      <label>
        <span class="ss-jew-lbl">Email</span>
        <input
          type="email"
          name="email"
          autocomplete="email"
          placeholder="[email protected]"
          required
        />
      </label>
      <label>
        <span class="ss-jew-lbl">Password</span>
        <input
          type="password"
          name="password"
          autocomplete="current-password"
          placeholder="••••••••••"
          required
        />
      </label>
      <div class="ss-jew-row">
        <label class="ss-jew-check"
          ><input type="checkbox" /> <span>Remember this device</span></label
        >
        <a href="#!">Forgot password</a>
      </div>
      <button type="submit" class="ss-jew-cta">Enter the salon</button>
      <p class="ss-jew-meta">Not a member? <a href="#!">Request an invitation</a></p>
    </form>
  </article>
</section>
```
## CSS
```css
.ss-jew {
  width: 100%;
  display: grid;
  grid-template-columns: 45% 55%;
  min-height: 100vh;
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  background: #fbf6e8;
  color: #1a1612;
  border-radius: 0;
  overflow: hidden;
}

.ss-jew-brand {
  background: radial-gradient(60% 80% at 50% 30%, #1a1612 0%, #0a0806 100%);
  color: #f5e6c8;
  padding: 44px 40px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: relative;
}

.ss-jew-mark {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg, #f3c0a4 0%, #b88a6a 100%);
  box-shadow: 0 0 0 1px rgba(255,255,255,0.18), 0 0 0 6px rgba(243,192,164,0.12);
  position: relative;
}

.ss-jew-mark::after {
  content: '';
  position: absolute;
  inset: 8px;
  border: 1px solid #1a1612;
  border-radius: 50%;
}

.ss-jew-since {
  font-family: 'Inter', sans-serif;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.32em;
  color: #b88a6a;
}

.ss-jew-brand h2 {
  margin: 4px 0 0;
  font-size: clamp(40px, 5.5vw, 64px);
  font-weight: 500;
  line-height: 0.92;
  letter-spacing: -0.02em;
  color: #f5e6c8;
}

.ss-jew-brand h2 em {
  font-style: italic;
  color: #f3c0a4;
}

.ss-jew-brand p {
  margin: 4px 0 0;
  font-size: 17px;
  line-height: 1.6;
  color: #c8b896;
  max-width: 380px;
  font-style: italic;
}

.ss-jew-divider {
  display: block;
  width: 60px;
  height: 1px;
  background: #b88a6a;
  margin-top: 16px;
}

.ss-jew-quote {
  margin-top: auto;
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
  font-style: italic;
  color: #b88a6a;
  letter-spacing: 0.04em;
}

.ss-jew-form-wrap {
  padding: 44px 48px;
  display: flex;
  flex-direction: column;
  gap: 22px;
  background: linear-gradient(180deg, #fff 0%, #fbf6e8 100%);
}

.ss-jew-eye {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: #b88a6a;
}

.ss-jew-form-wrap h3 {
  margin: 6px 0 0;
  font-size: clamp(26px, 3.5vw, 38px);
  font-weight: 500;
  letter-spacing: -0.01em;
  color: #1a1612;
  line-height: 1.05;
  font-style: italic;
}

.ss-jew-form {
  display: flex;
  flex-direction: column;
  gap: 14px;
  max-width: 400px;
}

.ss-jew-form label {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ss-jew-lbl {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #6a4a35;
}

.ss-jew-form input[type="email"],
.ss-jew-form input[type="password"] {
  padding: 12px 14px;
  background: #fff;
  border: 1px solid #c8b896;
  border-radius: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
  color: #1a1612;
  font-style: italic;
  transition: border-color 0.14s, box-shadow 0.14s;
}

.ss-jew-form input:focus {
  outline: 0;
  border-color: #b88a6a;
  box-shadow: 0 0 0 3px rgba(184,138,106,0.15);
}

.ss-jew-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  color: #4a3a2a;
}

.ss-jew-check {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.ss-jew-check input {
  accent-color: #b88a6a;
}

.ss-jew-row a {
  color: #b88a6a;
  text-decoration: none;
}

.ss-jew-row a:hover {
  text-decoration: underline;
}

.ss-jew-cta {
  padding: 14px 22px;
  background: #1a1612;
  color: #f5e6c8;
  border: 0;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.16s;
}

.ss-jew-cta:hover {
  background: #b88a6a;
  color: #1a1612;
}

.ss-jew-meta {
  margin: 6px 0 0;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  color: #6a4a35;
  text-align: center;
}

.ss-jew-meta a {
  color: #b88a6a;
  text-decoration: none;
}

.ss-jew-meta a:hover {
  text-decoration: underline;
}

@media (max-width: 720px) {
  .ss-jew {
    grid-template-columns: 1fr;
  }

  .ss-jew-brand {
    padding: 36px 28px;
  }
}
```

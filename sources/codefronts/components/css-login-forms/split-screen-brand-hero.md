---
source: "codefronts"
url: "https://codefronts.com/components/css-login-forms/split-screen-brand-hero/"
title: "Split-Screen Brand Hero"
section: "components"
category: "css-login-forms"
category_name: "CSS Login Forms"
description: "The high-conversion SaaS classic: a 50/50 desktop split with an isolated minimal form on one side and a branded panel — headline, testimonial, abstract…"
has_js: "false"
---

Here's a working CSS Login Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split-Screen Brand Hero
Source: https://codefronts.com/components/css-login-forms/split-screen-brand-hero/

The high-conversion SaaS classic: a 50/50 desktop split with an isolated minimal form on one side and a branded panel — headline, testimonial, abstract gradient mesh — on the other. Collapses to a single clean column on mobile.
## HTML
```html
<section class="lf-01">
  <div class="lf-01__shell">
    <aside class="lf-01__brand" aria-hidden="true">
      <div class="lf-01__mesh"></div>
      <div class="lf-01__brandbody">
        <div class="lf-01__logo">◆ Northwind</div>
        <p class="lf-01__pitch">The workspace where product, design and engineering finally share one source of truth.</p>
        <figure class="lf-01__quote">
          <blockquote>"We cut our release cycle in half the month we switched."</blockquote>
          <figcaption><span class="lf-01__av">AR</span> Ana Reyes · VP Eng, Lumen</figcaption>
        </figure>
      </div>
    </aside>
    <div class="lf-01__panel">
      <form class="lf-01__form" novalidate>
        <h1 class="lf-01__h">Welcome back</h1>
        <p class="lf-01__sub">Sign in to your Northwind workspace.</p>
        <label class="lf-01__field">
          <span class="lf-01__label">Work email</span>
          <input type="email" name="email" autocomplete="email" placeholder="[email protected]" required>
        </label>
        <label class="lf-01__field">
          <span class="lf-01__label">Password</span>
          <input type="password" name="password" autocomplete="current-password" placeholder="••••••••" required>
        </label>
        <button class="lf-01__submit" type="submit">Sign in</button>
        <p class="lf-01__foot">New here? <a href="#">Create an account</a></p>
      </form>
    </div>
  </div>
</section>
```
## CSS
```css
.lf-01,
.lf-01 *,
.lf-01 *::before,
.lf-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lf-01 {
  --accent: oklch(0.58 0.19 264);
  --brand-bg: #0e1330;
  --radius: 14px;
  --field-h: 48px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  background: #eef0f5;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.lf-01__shell {
  width: min(960px,100%);
  min-height: 560px;
  display: grid;
  grid-template-columns: 1.05fr 1fr;
  background: #fff;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 30px 70px -40px rgba(16,24,60,.5);
}

.lf-01__brand {
  position: relative;
  background: var(--brand-bg);
  color: #fff;
  overflow: hidden;
  display: flex;
}

.lf-01__mesh {
  position: absolute;
  inset: 0;
  background: radial-gradient(60% 55% at 20% 20%,oklch(0.6 0.2 264/.55),transparent 60%), radial-gradient(55% 50% at 85% 30%,oklch(0.62 0.18 200/.5),transparent 60%), radial-gradient(70% 60% at 60% 100%,oklch(0.6 0.2 330/.45),transparent 60%);
}

.lf-01__brandbody {
  position: relative;
  padding: 48px;
  display: flex;
  flex-direction: column;
  gap: 24px;
  justify-content: space-between;
}

.lf-01__logo {
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.lf-01__pitch {
  font-size: 26px;
  line-height: 1.28;
  font-weight: 600;
  letter-spacing: -.01em;
  text-wrap: balance;
}

.lf-01__quote blockquote {
  font-size: 15px;
  line-height: 1.5;
  color: #d7ddf5;
}

.lf-01__quote figcaption {
  margin-top: 14px;
  font-size: 13px;
  color: #aeb7dd;
  display: flex;
  align-items: center;
  gap: 10px;
}

.lf-01__av {
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
  font-size: 12px;
  font-weight: 700;
}

.lf-01__panel {
  display: grid;
  place-items: center;
  padding: 48px;
}

.lf-01__form {
  width: 100%;
  max-width: 340px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.lf-01__h {
  font-size: 28px;
  font-weight: 700;
  color: #141a2e;
  letter-spacing: -.02em;
}

.lf-01__sub {
  font-size: 14px;
  color: #69708a;
  margin-top: -8px;
  margin-bottom: 6px;
}

.lf-01__field {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.lf-01__label {
  font-size: 13px;
  font-weight: 600;
  color: #39405a;
}

.lf-01__field input {
  height: var(--field-h);
  border: 1.5px solid #d6dae6;
  border-radius: var(--radius);
  padding: 0 14px;
  font-size: 15px;
  color: #141a2e;
  background: #fbfbfe;
  transition: border-color .18s,box-shadow .18s;
}

.lf-01__field input::placeholder {
  color: #a3aac2;
}

.lf-01__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.58 0.19 264/.16);
}

.lf-01__submit {
  height: var(--field-h);
  margin-top: 4px;
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  transition: transform .12s,filter .18s;
}

.lf-01__submit:hover {
  filter: brightness(1.06);
}

.lf-01__submit:active {
  transform: scale(.985);
}

.lf-01__submit:focus-visible {
  outline: 3px solid oklch(0.58 0.19 264/.5);
  outline-offset: 3px;
}

.lf-01__foot {
  font-size: 13.5px;
  color: #69708a;
  text-align: center;
}

.lf-01__foot a {
  color: var(--accent);
  font-weight: 600;
  text-decoration: none;
}

.lf-01__foot a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .lf-01__shell {
    grid-template-columns: 1fr;
    min-height: 0;
  }

  .lf-01__brand {
    display: none;
  }

  .lf-01__panel {
    padding: 36px 26px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lf-01 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — a CSS Grid split that collapses to one column under 768px via @media. */
```

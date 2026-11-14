---
source: "codefronts"
url: "https://codefronts.com/layouts/css-two-column-layout/css-two-column-split-screen-layout/"
title: "CSS Two Column Split Screen Layout"
section: "layouts"
category: "css-two-column-layout"
category_name: "CSS Two-Column Layouts"
description: "A full-height split screen layout — brand panel left, sign-in form right — using min-height: 100dvh and grid-template-columns: 1.1fr 1fr. The modern SaaS…"
has_js: "false"
---

Here's a working CSS Two-Column Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Two Column Split Screen Layout
Source: https://codefronts.com/layouts/css-two-column-layout/css-two-column-split-screen-layout/

A full-height split screen layout — brand panel left, sign-in form right — using min-height: 100dvh and grid-template-columns: 1.1fr 1fr. The modern SaaS auth-page pattern, complete with a gradient-mesh brand side, a testimonial card, an accessible form and a mobile view where the brand panel becomes a compact banner.
## HTML
```html
<section class="tcl-08" aria-label="Split screen two column layout demo">
  <div class="tcl-08__screen">
    <div class="tcl-08__brand">
      <div class="tcl-08__brandinner">
        <div class="tcl-08__logo"><i></i>Fieldnote</div>
        <h2>Every great trip starts as a note.</h2>
        <p>Plan, map and share journeys with the people you travel with — all in one quiet place.</p>
        <figure class="tcl-08__quote">
          <blockquote>“We planned a three-week Japan trip in one evening. Fieldnote is the first planner that didn’t feel like a spreadsheet.”</blockquote>
          <figcaption><b>MK</b><span>Mara Kessler · Travel writer</span></figcaption>
        </figure>
      </div>
    </div>
    <div class="tcl-08__auth">
      <form class="tcl-08__form">
        <h1>Welcome back</h1>
        <p class="tcl-08__sub">Sign in to your workspace</p>
        <label class="tcl-08__field"><span>Email</span><input type="email" name="email" autocomplete="email" placeholder="[email protected]" required></label>
        <label class="tcl-08__field"><span>Password</span><input type="password" name="pw" autocomplete="current-password" placeholder="••••••••" required></label>
        <div class="tcl-08__row"><label class="tcl-08__remember"><input type="checkbox">Remember me</label><a class="tcl-08__forgot" href="#reset">Forgot password?</a></div>
        <button class="tcl-08__btn" type="submit">Sign in</button>
        <p class="tcl-08__alt">New here? <a href="#signup">Create an account</a></p>
      </form>
    </div>
  </div>
</section>
```
## CSS
```css
.tcl-08,
.tcl-08 *,
.tcl-08 *::before,
.tcl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tcl-08 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.6 0.16 230);
  --deep: oklch(0.24 0.05 245);
  --ink: oklch(0.25 0.02 245);
  background: var(--deep);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.tcl-08__screen {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  min-height: 100vh;
  min-height: 100dvh;
}

.tcl-08__brand {
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(28px,4vw,56px);
  color: #fff;
  background: radial-gradient(80% 60% at 20% 10%,oklch(0.5 0.14 230 / .8),transparent 60%),radial-gradient(70% 70% at 90% 30%,oklch(0.55 0.12 280 / .55),transparent 60%),radial-gradient(90% 80% at 50% 100%,oklch(0.4 0.1 200 / .6),transparent 65%),var(--deep);
  overflow: hidden;
}

.tcl-08__brand::after {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-conic-gradient(rgba(255,255,255,.015) 0 .8deg,transparent .8deg 1.6deg);
  pointer-events: none;
}

.tcl-08__brandinner {
  position: relative;
  display: grid;
  gap: 18px;
  max-width: 420px;
  z-index: 1;
}

.tcl-08__logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  font-size: 17px;
  letter-spacing: -.01em;
}

.tcl-08__logo i {
  width: 28px;
  height: 28px;
  border-radius: 9px;
  background: linear-gradient(135deg,oklch(0.8 0.12 200),var(--accent));
}

.tcl-08__brandinner h2 {
  font-size: clamp(26px,3.2vw,38px);
  line-height: 1.12;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.tcl-08__brandinner>p {
  font-size: 15px;
  line-height: 1.65;
  color: oklch(0.85 0.03 240);
  text-wrap: pretty;
}

.tcl-08__quote {
  margin-top: 10px;
  display: grid;
  gap: 12px;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.14);
  border-radius: 16px;
  padding: 18px;
  backdrop-filter: blur(8px);
}

.tcl-08__quote blockquote {
  font-size: 14px;
  line-height: 1.6;
  color: oklch(0.92 0.02 240);
  text-wrap: pretty;
}

.tcl-08__quote figcaption {
  display: flex;
  gap: 10px;
  align-items: center;
  font-size: 12.5px;
  color: oklch(0.8 0.03 240);
}

.tcl-08__quote b {
  display: grid;
  place-items: center;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
  font-size: 11.5px;
}

.tcl-08__auth {
  display: grid;
  place-items: center;
  padding: clamp(24px,4vw,56px);
  background: oklch(0.98 0.004 240);
}

.tcl-08__form {
  display: grid;
  gap: 14px;
  width: min(360px,100%);
}

.tcl-08__form h1 {
  font-size: clamp(22px,2.6vw,28px);
  letter-spacing: -.02em;
}

.tcl-08__sub {
  font-size: 14px;
  color: color-mix(in oklab,var(--ink) 58%,transparent);
  margin-top: -8px;
}

.tcl-08__field {
  display: grid;
  gap: 6px;
  font: 600 12.5px/1 inherit;
}

.tcl-08__field input {
  font: inherit;
  font-weight: 400;
  font-size: 16px;
  border: 1.5px solid oklch(0.88 0.01 240);
  border-radius: 10px;
  padding: 12px 14px;
  min-height: 46px;
  background: #fff;
  transition: border-color .15s,box-shadow .15s;
}

.tcl-08__field input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 18%,transparent);
}

.tcl-08__row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
}

.tcl-08__remember {
  display: flex;
  gap: 8px;
  align-items: center;
  cursor: pointer;
}

.tcl-08__remember input {
  width: 16px;
  height: 16px;
  accent-color: var(--accent);
}

.tcl-08__forgot {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
}

.tcl-08__forgot:hover,
.tcl-08__alt a:hover {
  text-decoration: underline;
}

.tcl-08__btn {
  font: 600 15px/1 inherit;
  color: #fff;
  background: var(--accent);
  border: none;
  border-radius: 11px;
  padding: 15px;
  min-height: 48px;
  cursor: pointer;
  transition: transform .15s,box-shadow .2s;
  margin-top: 4px;
}

.tcl-08__btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 24px -12px var(--accent);
}

.tcl-08__btn:focus-visible {
  outline: 3px solid var(--deep);
  outline-offset: 3px;
}

.tcl-08__alt {
  font-size: 13.5px;
  text-align: center;
  color: color-mix(in oklab,var(--ink) 60%,transparent);
}

.tcl-08__alt a {
  color: var(--accent);
  font-weight: 600;
  text-decoration: none;
}

.tcl-08__forgot:focus-visible,
.tcl-08__alt a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 4px;
}

@media (max-width: 780px) {
  .tcl-08__screen {
    grid-template-columns: 1fr;
    min-height: 0;
  }

  .tcl-08__brand {
    padding: 24px;
  }

  .tcl-08__quote {
    display: none;
  }

  .tcl-08__brandinner h2 {
    font-size: 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tcl-08__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a min-height:100dvh grid with 1.1fr/1fr tracks; each half centers its content with place-items, and the brand panel compresses to a banner on mobile. */
```

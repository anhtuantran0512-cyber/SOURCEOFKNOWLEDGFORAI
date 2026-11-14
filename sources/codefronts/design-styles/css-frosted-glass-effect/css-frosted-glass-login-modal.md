---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/css-frosted-glass-login-modal/"
title: "CSS Frosted Glass Login Modal"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A full-viewport login modal floating over a colorful photo backdrop with a real frosted-glass card — the canonical glassmorphism pattern Apple, Vercel, and…"
has_js: "false"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Frosted Glass Login Modal
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/css-frosted-glass-login-modal/

A full-viewport login modal floating over a colorful photo backdrop with a real frosted-glass card — the canonical glassmorphism pattern Apple, Vercel, and Linear ship on their auth screens. Real form with email, password, remember-me toggle, primary CTA, and social sign-in buttons (Google, Apple, GitHub). Backdrop uses `backdrop-filter: blur(24px) saturate(180%)` with an inset highlight stroke and a subtle gradient border.
## HTML
```html
<div class="fg-01">
  <div class="fg-01__stage">
    <div class="fg-01__card" role="dialog" aria-labelledby="fg-01-title">
      <div class="fg-01__logo" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 2l2.09 6.26L20 9.27l-4.55 4.44L16.54 20 12 16.77 7.46 20l1.09-6.29L4 9.27l5.91-1.01L12 2z"/>
        </svg>
      </div>
      <h1 class="fg-01__title" id="fg-01-title">Welcome back</h1>
      <p class="fg-01__sub">Sign in to continue to your account.</p>

      <form class="fg-01__form" onsubmit="event.preventDefault()">
        <label class="fg-01__field">
          <span class="fg-01__label">Email</span>
          <input type="email" id="fg-01-email" name="email" placeholder="[email protected]" autocomplete="email" required>
        </label>
        <label class="fg-01__field">
          <span class="fg-01__label">Password</span>
          <input type="password" id="fg-01-password" name="password" placeholder="••••••••" autocomplete="current-password" required>
        </label>

        <div class="fg-01__row">
          <label class="fg-01__check">
            <input type="checkbox" id="fg-01-remember" checked>
            <span class="fg-01__checkbox" aria-hidden="true"></span>
            <span>Keep me signed in</span>
          </label>
          <a href="#" class="fg-01__forgot">Forgot?</a>
        </div>

        <button type="submit" class="fg-01__submit">
          Sign in
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M5 12h14M13 5l7 7-7 7"/>
          </svg>
        </button>
      </form>

      <div class="fg-01__divider"><span>or continue with</span></div>

      <div class="fg-01__socials">
        <button type="button" class="fg-01__social" aria-label="Sign in with Google">
          <svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true">
            <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
            <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
            <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
            <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
          </svg>
          Google
        </button>
        <button type="button" class="fg-01__social" aria-label="Sign in with Apple">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83zM13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/>
          </svg>
          Apple
        </button>
        <button type="button" class="fg-01__social" aria-label="Sign in with GitHub">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M12 .5C5.65.5.5 5.65.5 12c0 5.09 3.29 9.4 7.86 10.93.58.11.79-.25.79-.56v-2.01c-3.2.7-3.88-1.37-3.88-1.37-.52-1.34-1.28-1.69-1.28-1.69-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.71 1.26 3.37.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.68 0-1.26.45-2.28 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11.1 11.1 0 015.79 0c2.21-1.49 3.18-1.18 3.18-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.83 1.19 3.09 0 4.41-2.69 5.38-5.25 5.67.41.35.78 1.05.78 2.12v3.14c0 .31.21.68.79.56A11.51 11.51 0 0023.5 12C23.5 5.65 18.35.5 12 .5z"/>
          </svg>
          GitHub
        </button>
      </div>

      <p class="fg-01__foot">
        New here? <a href="#">Create an account</a>
      </p>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-01,
.fg-01 *,
.fg-01 *::before,
.fg-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-01 ::selection {
  background: rgba(255,255,255,.28);
  color: #fff;
}

.fg-01 {
  --accent: #7c6cff;
  --ink: #0f172a;
  --paper: #ffffff;
  min-height: 100vh;
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",Roboto,sans-serif;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}
/* Backdrop stage — the colourful photo behind the glass. Multi-stop
   linear-gradient stands in for a real hero photo. The variety of hues
   is what gives the frosted panel its shifting colour through the blur. */

.fg-01__stage {
  position: relative;
  width: 100%;
  min-height: calc(100vh - 48px);
  border-radius: 24px;
  overflow: hidden;
  background: radial-gradient(circle at 15% 20%, #fbbf24 0%, transparent 42%), radial-gradient(circle at 85% 30%, #ec4899 0%, transparent 45%), radial-gradient(circle at 30% 85%, #7c6cff 0%, transparent 50%), radial-gradient(circle at 80% 80%, #22d3ee 0%, transparent 48%), linear-gradient(135deg,#1e1b4b 0%,#312e81 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(24px,4vw,64px);
}
/* Frosted glass card — the star of the show */

.fg-01__card {
  width: 100%;
  max-width: 420px;
  padding: clamp(28px,3.5vw,40px);
  border-radius: 22px;
  position: relative;
  background: rgba(255,255,255,0.12);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.22);
  box-shadow: 0 24px 48px -20px rgba(15,15,30,0.42), inset 0 1px 0 rgba(255,255,255,0.28);
}
/* Fallback for engines without backdrop-filter — dark semi-opaque
   panel that keeps the copy readable without the frosted effect. */

@supports not (backdrop-filter: blur(1px)) {
  .fg-01__card {
    background: rgba(15,20,25,0.85);
  }
}

.fg-01__logo {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  background: rgba(255,255,255,0.14);
  border: 1px solid rgba(255,255,255,0.22);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 22px;
}

.fg-01__title {
  font-size: clamp(1.5rem,2.6vw,1.9rem);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.1;
  margin-bottom: 6px;
}

.fg-01__sub {
  font-size: .92rem;
  color: rgba(255,255,255,0.72);
  margin-bottom: 24px;
  line-height: 1.5;
}

.fg-01__form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.fg-01__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.fg-01__label {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.68);
}

.fg-01__field input {
  padding: 12px 14px;
  border-radius: 10px;
  background: rgba(255,255,255,0.09);
  border: 1px solid rgba(255,255,255,0.18);
  color: #fff;
  font-size: .95rem;
  font-family: inherit;
  transition: border-color .2s,background .2s;
}

.fg-01__field input::placeholder {
  color: rgba(255,255,255,0.35);
}

.fg-01__field input:focus {
  outline: none;
  border-color: var(--accent);
  background: rgba(255,255,255,0.14);
}

.fg-01__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 4px;
}

.fg-01__check {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: .84rem;
  color: rgba(255,255,255,0.82);
  cursor: pointer;
}

.fg-01__check input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.fg-01__checkbox {
  width: 16px;
  height: 16px;
  border-radius: 4px;
  background: rgba(255,255,255,0.10);
  border: 1.5px solid rgba(255,255,255,0.35);
  position: relative;
  transition: background .2s,border-color .2s;
}

.fg-01__check input:checked + .fg-01__checkbox {
  background: var(--accent);
  border-color: var(--accent);
}

.fg-01__check input:checked + .fg-01__checkbox::after {
  content: "";
  position: absolute;
  left: 4px;
  top: 1px;
  width: 5px;
  height: 9px;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.fg-01__forgot {
  font-size: .84rem;
  color: rgba(255,255,255,0.72);
  text-decoration: none;
}

.fg-01__forgot:hover {
  color: #fff;
  text-decoration: underline;
}

.fg-01__submit {
  margin-top: 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 13px 20px;
  background: var(--accent);
  color: #fff;
  border: 0;
  border-radius: 10px;
  font-size: .95rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .2s,transform .1s;
}

.fg-01__submit:hover {
  background: #6d5cf0;
  transform: translateY(-1px);
}

.fg-01__submit:focus-visible {
  outline: 2px solid rgba(255,255,255,0.9);
  outline-offset: 2px;
}

.fg-01__divider {
  display: flex;
  align-items: center;
  gap: 14px;
  margin: 24px 0 18px;
  color: rgba(255,255,255,0.55);
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.fg-01__divider::before,
.fg-01__divider::after {
  content: "";
  flex: 1;
  height: 1px;
  background: rgba(255,255,255,0.15);
}

.fg-01__socials {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 8px;
}

.fg-01__social {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 10px 8px;
  background: rgba(255,255,255,0.09);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 9px;
  color: #fff;
  font-size: .82rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .2s,border-color .2s;
  font-family: inherit;
}

.fg-01__social:hover {
  background: rgba(255,255,255,0.16);
  border-color: rgba(255,255,255,0.32);
}

.fg-01__foot {
  margin-top: 22px;
  text-align: center;
  font-size: .86rem;
  color: rgba(255,255,255,0.68);
}

.fg-01__foot a {
  color: #fff;
  font-weight: 600;
  text-decoration: none;
}

.fg-01__foot a:hover {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .fg-01__socials {
    grid-template-columns: 1fr;
    gap: 6px;
  }

  .fg-01__stage {
    border-radius: 16px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fg-01__submit,
    .fg-01__field input,
    .fg-01__social,
    .fg-01__checkbox {
    transition: none;
  }
}
```

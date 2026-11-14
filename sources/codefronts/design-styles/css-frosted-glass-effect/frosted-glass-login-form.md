---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/frosted-glass-login-form/"
title: "Frosted Glass Login Form"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A premium glassmorphism login/signup card with four animated gradient orbs, a sliding tab pill, floating-label inputs, password strength meter, eye toggle,…"
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Login Form
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/frosted-glass-login-form/

A premium glassmorphism login/signup card with four animated gradient orbs, a sliding tab pill, floating-label inputs, password strength meter, eye toggle, custom checkbox, and a shimmer CTA button — all rendered on an animated cyber-grid background.
## HTML
```html
<div class="fg-06">
  <div class="fg-01__bg" aria-hidden="true">
    <div class="fg-01__orb fg-01__orb--1"></div>
    <div class="fg-01__orb fg-01__orb--2"></div>
    <div class="fg-01__orb fg-01__orb--3"></div>
    <div class="fg-01__orb fg-01__orb--4"></div>
    <div class="fg-01__grid"></div>
  </div>
  <div class="fg-01__card" role="main">
    <div class="fg-01__brand">
      <div class="fg-01__brand-icon" aria-hidden="true">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
      </div>
      <span class="fg-01__brand-name">Nexus</span>
      <span class="fg-01__brand-tag">Beta</span>
    </div>
    <div class="fg-01__tabs" role="tablist" aria-label="Authentication tabs">
      <button class="fg-01__tab is-active" role="tab" aria-selected="true" data-panel="fg-06-login">Log In</button>
      <button class="fg-01__tab" role="tab" aria-selected="false" data-panel="fg-06-signup">Sign Up</button>
      <div class="fg-01__tab-pill" aria-hidden="true"></div>
    </div>
    <div class="fg-01__panels">
      <div class="fg-01__panel is-active" id="fg-06-login" role="tabpanel">
        <div class="fg-01__field">
          <input class="fg-01__input" type="email" id="fg-06-li-email" placeholder=" " autocomplete="email">
          <label class="fg-01__label" for="fg-06-li-email">Email address</label>
        </div>
        <div class="fg-01__field fg-01__field--pass">
          <input class="fg-01__input" type="password" id="fg-06-li-pass" placeholder=" " autocomplete="current-password">
          <label class="fg-01__label" for="fg-06-li-pass">Password</label>
          <button type="button" class="fg-01__eye" aria-label="Toggle password">
            <svg class="fg-01__eye-open" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            <svg class="fg-01__eye-shut" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94"/><path d="M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19"/><line x1="1" y1="1" x2="23" y2="23"/></svg>
          </button>
        </div>
        <div class="fg-01__meta">
          <label class="fg-01__remember">
            <span class="fg-01__chk"><input type="checkbox" id="fg-06-remember"><span class="fg-01__chk-box"></span></span>
            <span>Remember me</span>
          </label>
          <a class="fg-01__forgot" href="#">Forgot password?</a>
        </div>
        <button type="button" class="fg-01__cta" data-label="Sign In">Sign In</button>
      </div>
      <div class="fg-01__panel" id="fg-06-signup" role="tabpanel">
        <div class="fg-01__row2">
          <div class="fg-01__field">
            <input class="fg-01__input" type="text" id="fg-06-su-fn" placeholder=" " autocomplete="given-name">
            <label class="fg-01__label" for="fg-06-su-fn">First name</label>
          </div>
          <div class="fg-01__field">
            <input class="fg-01__input" type="text" id="fg-06-su-ln" placeholder=" " autocomplete="family-name">
            <label class="fg-01__label" for="fg-06-su-ln">Last name</label>
          </div>
        </div>
        <div class="fg-01__field">
          <input class="fg-01__input" type="email" id="fg-06-su-email" placeholder=" " autocomplete="email">
          <label class="fg-01__label" for="fg-06-su-email">Email address</label>
        </div>
        <div class="fg-01__field fg-01__field--pass">
          <input class="fg-01__input" type="password" id="fg-06-su-pass" placeholder=" " autocomplete="new-password">
          <label class="fg-01__label" for="fg-06-su-pass">Create password</label>
          <button type="button" class="fg-01__eye" aria-label="Toggle password">
            <svg class="fg-01__eye-open" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            <svg class="fg-01__eye-shut" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94"/><path d="M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19"/><line x1="1" y1="1" x2="23" y2="23"/></svg>
          </button>
        </div>
        <div class="fg-01__strength" id="fg-06-strength">
          <div class="fg-01__strength-bars"><span></span><span></span><span></span><span></span></div>
          <span class="fg-01__strength-label">Password strength</span>
        </div>
        <button type="button" class="fg-01__cta" data-label="Create Account">Create Account</button>
      </div>
    </div>
    <div class="fg-01__divider" aria-hidden="true"><span>or continue with</span></div>
    <div class="fg-01__socials">
      <button type="button" class="fg-01__social" aria-label="Continue with Google">
        <svg width="18" height="18" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
        <span>Google</span>
      </button>
      <button type="button" class="fg-01__social" aria-label="Continue with GitHub">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
        <span>GitHub</span>
      </button>
      <button type="button" class="fg-01__social" aria-label="Continue with Apple">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
        <span>Apple</span>
      </button>
    </div>
    <div class="fg-01__success" id="fg-06-success" aria-live="polite">
      <div class="fg-01__success-ring"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div>
      <p class="fg-01__success-title">Welcome back!</p>
      <p class="fg-01__success-sub">Redirecting to your dashboard...</p>
      <div class="fg-01__success-dots" aria-hidden="true"><span></span><span></span><span></span></div>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-06,
.fg-06 *,
.fg-06 *::before,
.fg-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-06 ::selection {
  background: rgba(124,58,237,.5);
  color: #fff;
}

.fg-06 {
  --c-bg: #07071a;
  --c-o1: #7c3aed;
  --c-o2: #db2777;
  --c-o3: #0ea5e9;
  --c-o4: #4338ca;
  --c-glass: rgba(255,255,255,.065);
  --c-border: rgba(255,255,255,.12);
  --c-text: #eeeeff;
  --c-muted: rgba(238,238,255,.5);
  --c-accent: #7c3aed;
  --c-accent-lt: #a78bfa;
  --c-field: rgba(255,255,255,.05);
  --c-fborder: rgba(255,255,255,.1);
  --c-green: #10b981;
  --t-ui: .25s ease;
  --t-pill: .32s cubic-bezier(.4,0,.2,1);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--c-bg);
  position: relative;
  overflow: hidden;
  padding: 40px 20px;
}
/* ── animated background ── */

.fg-01__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fg-01__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(90px);
}

.fg-01__orb--1 {
  width: 440px;
  height: 440px;
  background: var(--c-o1);
  opacity: .3;
  top: -130px;
  left: -110px;
  animation: fg-06-o1 18s ease-in-out infinite alternate;
}

.fg-01__orb--2 {
  width: 380px;
  height: 380px;
  background: var(--c-o2);
  opacity: .25;
  bottom: -110px;
  right: -90px;
  animation: fg-06-o2 23s ease-in-out infinite alternate;
}

.fg-01__orb--3 {
  width: 310px;
  height: 310px;
  background: var(--c-o3);
  opacity: .2;
  top: 45%;
  left: 58%;
  animation: fg-06-o3 16s ease-in-out infinite alternate;
}

.fg-01__orb--4 {
  width: 270px;
  height: 270px;
  background: var(--c-o4);
  opacity: .28;
  bottom: 25%;
  left: 4%;
  animation: fg-06-o4 21s ease-in-out infinite alternate;
}

.fg-01__grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);
  background-size: 40px 40px;
}

@keyframes fg-06-o1 {
  to {
    transform: translate(70px,90px) scale(1.12);
  }
}

@keyframes fg-06-o2 {
  to {
    transform: translate(-65px,-75px) scale(1.18);
  }
}

@keyframes fg-06-o3 {
  to {
    transform: translate(-90px,65px) scale(.88);
  }
}

@keyframes fg-06-o4 {
  to {
    transform: translate(55px,-85px) scale(1.2);
  }
}
/* ── glass card ── */

.fg-01__card {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 424px;
  background: var(--c-glass);
  backdrop-filter: blur(26px) saturate(160%);
  -webkit-backdrop-filter: blur(26px) saturate(160%);
  border: 1px solid var(--c-border);
  border-radius: 24px;
  padding: 36px 32px 32px;
  box-shadow: 0 8px 48px rgba(0,0,0,.5),0 1px 0 rgba(255,255,255,.1) inset;
}
/* ── brand ── */

.fg-01__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 24px;
}

.fg-01__brand-icon {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  flex-shrink: 0;
  background: linear-gradient(135deg,var(--c-o1),var(--c-o3));
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 22px rgba(124,58,237,.45);
}

.fg-01__brand-name {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -.4px;
  background: linear-gradient(90deg,#fff 40%,rgba(255,255,255,.6));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.fg-01__brand-tag {
  margin-left: auto;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .7px;
  text-transform: uppercase;
  color: var(--c-accent-lt);
  padding: 3px 9px;
  border-radius: 20px;
  background: rgba(124,58,237,.14);
  border: 1px solid rgba(124,58,237,.28);
}
/* ── tabs ── */

.fg-01__tabs {
  display: flex;
  position: relative;
  background: rgba(255,255,255,.05);
  border: 1px solid var(--c-border);
  border-radius: 12px;
  padding: 4px;
  margin-bottom: 22px;
}

.fg-01__tab {
  flex: 1;
  border: none;
  background: transparent;
  color: var(--c-muted);
  font-size: 14px;
  font-weight: 600;
  padding: 9px 0;
  border-radius: 9px;
  cursor: pointer;
  position: relative;
  z-index: 1;
  transition: color var(--t-ui);
}

.fg-01__tab.is-active {
  color: var(--c-text);
}

.fg-01__tab-pill {
  position: absolute;
  top: 4px;
  bottom: 4px;
  left: 4px;
  width: calc(50% - 4px);
  background: linear-gradient(135deg,var(--c-o1),var(--c-o4));
  border-radius: 9px;
  box-shadow: 0 2px 14px rgba(124,58,237,.45);
  transition: transform var(--t-pill);
  pointer-events: none;
}

.fg-01__tab-pill.to-right {
  transform: translateX(100%);
}
/* ── panels ── */

.fg-01__panels {
  position: relative;
}

.fg-01__panel {
  display: none;
  animation: fg-06-panelin .28s ease both;
}

.fg-01__panel.is-active {
  display: block;
}

@keyframes fg-06-panelin {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
/* ── floating-label field ── */

.fg-01__field {
  position: relative;
  margin-bottom: 14px;
}

.fg-01__input {
  width: 100%;
  background: var(--c-field);
  border: 1px solid var(--c-fborder);
  border-radius: 12px;
  padding: 20px 16px 8px;
  color: var(--c-text);
  font-size: 15px;
  outline: none;
  transition: border-color var(--t-ui),box-shadow var(--t-ui);
}

.fg-01__input:focus {
  border-color: var(--c-accent);
  box-shadow: 0 0 0 3px rgba(124,58,237,.22);
}

.fg-01__label {
  position: absolute;
  top: 14px;
  left: 16px;
  color: var(--c-muted);
  font-size: 15px;
  pointer-events: none;
  transition: top .2s,font-size .2s,letter-spacing .2s,color .2s;
}

.fg-01__input:focus~.fg-01__label,
.fg-01__input:not(:placeholder-shown)~.fg-01__label {
  top: 6px;
  font-size: 11px;
  letter-spacing: .3px;
  color: var(--c-accent-lt);
}

.fg-01__field--pass .fg-01__input {
  padding-right: 48px;
}
/* ── eye toggle ── */

.fg-01__eye {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  cursor: pointer;
  color: var(--c-muted);
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color var(--t-ui);
}

.fg-01__eye:hover {
  color: var(--c-text);
}

.fg-01__eye-shut {
  display: none;
}
/* ── meta row ── */

.fg-01__meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 14px 0 20px;
  font-size: 13px;
}

.fg-01__remember {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  color: var(--c-muted);
  user-select: none;
}

.fg-01__chk {
  position: relative;
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.fg-01__chk input {
  position: absolute;
  opacity: 0;
  width: 100%;
  height: 100%;
  cursor: pointer;
  margin: 0;
}

.fg-01__chk-box {
  display: block;
  width: 16px;
  height: 16px;
  border: 1.5px solid var(--c-fborder);
  border-radius: 4px;
  background: var(--c-field);
  transition: background var(--t-ui),border-color var(--t-ui);
  position: relative;
}

.fg-01__chk-box::after {
  content: '';
  position: absolute;
  top: 1px;
  left: 4px;
  width: 5px;
  height: 9px;
  border: 2px solid #fff;
  border-top: none;
  border-left: none;
  transform: rotate(45deg) scale(0);
  transition: transform .15s;
}

.fg-01__chk input:checked~.fg-01__chk-box {
  background: var(--c-accent);
  border-color: var(--c-accent);
}

.fg-01__chk input:checked~.fg-01__chk-box::after {
  transform: rotate(45deg) scale(1);
}

.fg-01__forgot {
  color: var(--c-accent-lt);
  text-decoration: none;
  font-weight: 500;
  transition: opacity var(--t-ui);
}

.fg-01__forgot:hover {
  opacity: .75;
}
/* ── 2-col row ── */

.fg-01__row2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
/* ── password strength ── */

.fg-01__strength {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: -4px 0 14px;
}

.fg-01__strength-bars {
  display: flex;
  gap: 4px;
  flex: 1;
}

.fg-01__strength-bars span {
  flex: 1;
  height: 3px;
  border-radius: 2px;
  background: rgba(255,255,255,.1);
  transition: background .3s;
}

.fg-01__strength[data-level="1"] .fg-01__strength-bars span:nth-child(1) {
  background: #ef4444;
}

.fg-01__strength[data-level="2"] .fg-01__strength-bars span:nth-child(-n+2) {
  background: #f59e0b;
}

.fg-01__strength[data-level="3"] .fg-01__strength-bars span:nth-child(-n+3) {
  background: #84cc16;
}

.fg-01__strength[data-level="4"] .fg-01__strength-bars span {
  background: var(--c-green);
}

.fg-01__strength-label {
  font-size: 11px;
  color: var(--c-muted);
  white-space: nowrap;
}
/* ── cta button ── */

.fg-01__cta {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg,var(--c-o1) 0%,var(--c-o4) 100%);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .4px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 22px rgba(124,58,237,.45);
  transition: transform .15s,box-shadow .2s,opacity .2s;
}

.fg-01__cta::before {
  content: '';
  position: absolute;
  top: 0;
  left: -80%;
  width: 55%;
  height: 100%;
  background: linear-gradient(90deg,transparent,rgba(255,255,255,.22),transparent);
  animation: fg-06-shine 2.4s linear infinite;
}

@keyframes fg-06-shine {
  to {
    left: 160%;
  }
}

.fg-01__cta:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 6px 30px rgba(124,58,237,.6);
}

.fg-01__cta:active:not(:disabled) {
  transform: translateY(0);
}

.fg-01__cta:disabled {
  opacity: .6;
  cursor: not-allowed;
}
/* ── divider ── */

.fg-01__divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 22px 0 18px;
  color: var(--c-muted);
  font-size: 12px;
  letter-spacing: .4px;
}

.fg-01__divider::before,
.fg-01__divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--c-border);
}
/* ── socials ── */

.fg-01__socials {
  display: flex;
  gap: 8px;
}

.fg-01__social {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  padding: 10px;
  background: var(--c-field);
  border: 1px solid var(--c-border);
  border-radius: 10px;
  color: var(--c-text);
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: background var(--t-ui),border-color var(--t-ui),transform .15s;
}

.fg-01__social:hover {
  background: rgba(255,255,255,.1);
  border-color: rgba(255,255,255,.22);
  transform: translateY(-1px);
}
/* ── success state ── */

.fg-01__success {
  display: none;
  text-align: center;
  padding: 26px 0 8px;
}

.fg-01__success.is-visible {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  animation: fg-06-fadein .4s ease;
}

.fg-01__success-ring {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--c-green),#34d399);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 44px rgba(16,185,129,.5);
  animation: fg-06-pop .5s cubic-bezier(.175,.885,.32,1.275) both;
}

.fg-01__success-title {
  font-size: 22px;
  font-weight: 800;
  color: var(--c-text);
  letter-spacing: -.3px;
}

.fg-01__success-sub {
  font-size: 14px;
  color: var(--c-muted);
}

.fg-01__success-dots {
  display: flex;
  gap: 6px;
  margin-top: 2px;
}

.fg-01__success-dots span {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--c-muted);
  animation: fg-06-dot 1.4s ease infinite;
}

.fg-01__success-dots span:nth-child(2) {
  animation-delay: .2s;
}

.fg-01__success-dots span:nth-child(3) {
  animation-delay: .4s;
}

@keyframes fg-06-dot {
  0%,
    80%,
    100% {
    transform: scale(0);
    opacity: .4;
  }

  40% {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes fg-06-fadein {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fg-06-pop {
  from {
    transform: scale(0) rotate(-30deg);
  }

  to {
    transform: scale(1) rotate(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fg-01__orb,
    .fg-01__cta::before,
    .fg-01__success-dots span {
    animation: none;
  }

  .fg-01__tab-pill,
    .fg-01__input,
    .fg-01__label,
    .fg-01__social,
    .fg-01__chk-box,
    .fg-01__cta {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.fg-06');
  if(!root)return;

  /* tab switching */
  var tabBtns=root.querySelectorAll('.fg-01__tab');
  var pill=root.querySelector('.fg-01__tab-pill');
  var panels=root.querySelectorAll('.fg-01__panel');
  tabBtns.forEach(function(btn,i){
    btn.addEventListener('click',function(){
      tabBtns.forEach(function(b){b.classList.remove('is-active');b.setAttribute('aria-selected','false')});
      btn.classList.add('is-active');btn.setAttribute('aria-selected','true');
      pill.classList.toggle('to-right',i===1);
      panels.forEach(function(p,pi){p.classList.toggle('is-active',pi===i)});
    });
  });

  /* password eye toggles */
  root.querySelectorAll('.fg-01__eye').forEach(function(eye){
    eye.addEventListener('click',function(){
      var field=eye.closest('.fg-01__field');
      var inp=field.querySelector('.fg-01__input');
      var showing=inp.type==='text';
      inp.type=showing?'password':'text';
      eye.querySelector('.fg-01__eye-open').style.display=showing?'':'none';
      eye.querySelector('.fg-01__eye-shut').style.display=showing?'none':'';
    });
  });

  /* password strength meter (signup panel) */
  var suPass=root.querySelector('#fg-06-su-pass');
  var stEl=root.querySelector('#fg-06-strength');
  if(suPass&&stEl){
    var stLabels=['','Weak','Fair','Good','Strong'];
    suPass.addEventListener('input',function(){
      var v=suPass.value,s=0;
      if(v.length>=8)s++;
      if(/[A-Z]/.test(v))s++;
      if(/[0-9]/.test(v))s++;
      if(/[^A-Za-z0-9]/.test(v))s++;
      stEl.setAttribute('data-level',v.length?String(s):'');
      stEl.querySelector('.fg-01__strength-label').textContent=v.length?(stLabels[s]||'Weak'):'Password strength';
    });
  }

  /* submit — both CTAs trigger the success state */
  var successEl=root.querySelector('#fg-06-success');
  var hideable=[
    root.querySelector('.fg-01__panels'),
    root.querySelector('.fg-01__tabs'),
    root.querySelector('.fg-01__divider'),
    root.querySelector('.fg-01__socials')
  ];
  root.querySelectorAll('.fg-01__cta').forEach(function(cta){
    cta.addEventListener('click',function(){
      var orig=cta.dataset.label||cta.textContent.trim();
      cta.disabled=true;cta.textContent='Authenticating…';
      setTimeout(function(){
        hideable.forEach(function(el){if(el)el.style.display='none'});
        successEl.classList.add('is-visible');
        setTimeout(function(){
          successEl.classList.remove('is-visible');
          hideable.forEach(function(el){if(el)el.style.display=''});
          cta.disabled=false;cta.textContent=orig;
        },3000);
      },1100);
    });
  });
})();
```

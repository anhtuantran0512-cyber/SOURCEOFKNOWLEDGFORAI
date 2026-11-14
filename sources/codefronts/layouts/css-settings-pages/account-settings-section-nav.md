---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/account-settings-section-nav/"
title: "Account Settings Page with Section Nav"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A complete SaaS account settings page with a sticky sidebar section nav that highlights the section you're reading (scroll-spy), grouped Profile, Email &…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Account Settings Page with Section Nav
Source: https://codefronts.com/layouts/css-settings-pages/account-settings-section-nav/

A complete SaaS account settings page with a sticky sidebar section nav that highlights the section you're reading (scroll-spy), grouped Profile, Email & login, Preferences and Privacy cards, native :user-invalid validation, iOS-style switches built from real checkboxes, and a floating 'unsaved changes' bar that slides up the moment the form is edited. On narrow containers the sidebar collapses into a horizontal, swipeable tab strip via a container query.
## HTML
```html
<section class="csp-01">
  <div class="csp-01__shell">
    <aside class="csp-01__aside">
      <p class="csp-01__label">Settings</p>
      <nav class="csp-01__nav" data-nav aria-label="Account sections">
        <a href="#csp01-profile" aria-current="true"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>Profile</a>
        <a href="#csp01-login"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>Email &amp; login</a>
        <a href="#csp01-prefs"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>Preferences</a>
        <a href="#csp01-privacy"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/></svg>Privacy</a>
      </nav>
    </aside>
    <form class="csp-01__main" data-form novalidate>
      <header class="csp-01__head">
        <h1>Account</h1>
        <p>Manage how you appear to teammates and how you sign in.</p>
      </header>

      <section class="csp-01__sec" id="csp01-profile" data-section>
        <div class="csp-01__sechd"><h2>Profile</h2><p>Shown on comments, mentions and shared documents.</p></div>
        <div class="csp-01__fields">
          <div class="csp-01__avatarrow">
            <span class="csp-01__avatar" aria-hidden="true">AM</span>
            <div class="csp-01__stack"><button type="button" class="csp-01__btn">Upload photo</button><small class="csp-01__hint">PNG or JPG, square, up to 2&nbsp;MB</small></div>
          </div>
          <label class="csp-01__field"><span>Full name</span><input name="name" value="Ava Mitchell" autocomplete="name" required></label>
          <label class="csp-01__field"><span>Job title</span><input name="title" value="Product Designer" autocomplete="organization-title"></label>
          <label class="csp-01__field csp-01__field--full"><span>Bio</span><textarea name="bio" rows="3" maxlength="160">Designing calm, accessible tools for busy teams.</textarea><small class="csp-01__hint">Up to 160 characters.</small></label>
        </div>
      </section>

      <section class="csp-01__sec" id="csp01-login" data-section>
        <div class="csp-01__sechd"><h2>Email &amp; login</h2><p>Used to sign in and receive security alerts.</p></div>
        <div class="csp-01__fields">
          <label class="csp-01__field"><span>Email address</span><input type="email" name="email" value="[email protected]" autocomplete="email" required></label>
          <div class="csp-01__field"><span>Password</span><div class="csp-01__inline"><input type="password" value="placeholder-pass" aria-label="Current password" readonly><button type="button" class="csp-01__btn">Change</button></div></div>
          <div class="csp-01__row"><div><strong>Sign in with Google</strong><small class="csp-01__hint">Connected as [email protected]</small></div><input class="csp-01__switch" type="checkbox" role="switch" checked aria-label="Sign in with Google"></div>
        </div>
      </section>

      <section class="csp-01__sec" id="csp01-prefs" data-section>
        <div class="csp-01__sechd"><h2>Preferences</h2><p>Language and regional formats for dates, times and numbers.</p></div>
        <div class="csp-01__fields">
          <label class="csp-01__field"><span>Language</span><select name="lang"><option>English (United States)</option><option>English (United Kingdom)</option><option>English (Australia)</option><option>Deutsch</option><option>Français</option></select></label>
          <label class="csp-01__field"><span>Time zone</span><select name="tz"><option>(GMT−08:00) Pacific Time</option><option>(GMT−05:00) Eastern Time</option><option>(GMT+00:00) London</option><option>(GMT+10:00) Sydney</option></select></label>
          <label class="csp-01__field"><span>Date format</span><select name="date"><option>Oct 7, 2026</option><option>07/10/2026</option><option>2026-10-07</option></select></label>
          <label class="csp-01__field"><span>Start of week</span><select name="week"><option>Sunday</option><option>Monday</option></select></label>
        </div>
      </section>

      <section class="csp-01__sec" id="csp01-privacy" data-section>
        <div class="csp-01__sechd"><h2>Privacy</h2><p>Control what others in your workspace can see.</p></div>
        <div class="csp-01__fields">
          <div class="csp-01__row"><div><strong>Show my activity status</strong><small class="csp-01__hint">Teammates see when you're online.</small></div><input class="csp-01__switch" type="checkbox" role="switch" checked aria-label="Show my activity status"></div>
          <div class="csp-01__row"><div><strong>Searchable profile</strong><small class="csp-01__hint">Appear in member search across the organisation.</small></div><input class="csp-01__switch" type="checkbox" role="switch" checked aria-label="Searchable profile"></div>
          <div class="csp-01__row"><div><strong>Share usage analytics</strong><small class="csp-01__hint">Anonymous data that helps us improve the product.</small></div><input class="csp-01__switch" type="checkbox" role="switch" aria-label="Share usage analytics"></div>
        </div>
      </section>

      <div class="csp-01__bar" role="status" aria-live="polite">
        <span data-msg>You have unsaved changes</span>
        <button type="reset" class="csp-01__btn csp-01__btn--ghost">Discard</button>
        <button type="submit" class="csp-01__btn csp-01__btn--primary">Save changes</button>
      </div>
    </form>
  </div>
</section>
```
## CSS
```css
.csp-01,
.csp-01 *,
.csp-01 *::before,
.csp-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-01 {
  --bg: oklch(0.985 0.003 260);
  --surface: #fff;
  --ink: oklch(0.22 0.02 265);
  --muted: oklch(0.5 0.02 265);
  --line: oklch(0.92 0.006 265);
  --accent: oklch(0.55 0.2 268);
  --ring: oklch(0.55 0.2 268/.22);
  --danger: oklch(0.58 0.21 25);
  color-scheme: light;
  container-type: inline-size;
  min-height: 100vh;
  min-height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  accent-color: var(--accent);
  width: 100%;
}

.csp-01__shell {
  display: grid;
  grid-template-columns: 220px minmax(0,1fr);
  gap: 40px;
  max-width: 1040px;
  margin-inline: auto;
  padding: 40px 28px 140px;
}

.csp-01__aside {
  position: sticky;
  top: 40px;
  align-self: start;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.csp-01__label {
  font: 600 11px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
  padding-inline: 12px;
}

.csp-01__nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.csp-01__nav a {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 42px;
  padding: 0 12px;
  border-radius: 10px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--muted);
  text-decoration: none;
  white-space: nowrap;
  transition: background .15s,color .15s,box-shadow .15s;
}

.csp-01__nav a:hover {
  background: oklch(0.95 0.006 265);
  color: var(--ink);
}

.csp-01__nav a[aria-current] {
  background: var(--surface);
  color: var(--ink);
  box-shadow: 0 1px 2px oklch(0 0 0/.06),0 0 0 1px var(--line);
}

.csp-01__nav svg {
  width: 17px;
  height: 17px;
  flex: none;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.csp-01__nav a[aria-current] svg {
  color: var(--accent);
}

.csp-01__nav a:focus-visible,
.csp-01__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-01__main {
  display: flex;
  flex-direction: column;
  gap: 24px;
  min-width: 0;
}

.csp-01__head {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding-bottom: 4px;
}

.csp-01__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-01__head p {
  font: 400 15px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.csp-01__sec {
  scroll-margin-top: 32px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: 0 1px 2px oklch(0 0 0/.03),0 8px 24px -18px oklch(0.3 0.05 265/.25);
}

.csp-01__sechd {
  padding: 22px 24px 18px;
  border-bottom: 1px solid var(--line);
}

.csp-01__sechd h2 {
  font: 650 16px/1.2 system-ui,sans-serif;
  letter-spacing: -.01em;
}

.csp-01__sechd p {
  font: 400 13.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 4px;
  text-wrap: pretty;
}

.csp-01__fields {
  display: grid;
  grid-template-columns: repeat(2,minmax(0,1fr));
  gap: 18px 20px;
  padding: 22px 24px 24px;
}

.csp-01__field {
  display: flex;
  flex-direction: column;
  gap: 7px;
  font: 550 13px/1.2 system-ui,sans-serif;
  min-width: 0;
}

.csp-01__field--full {
  grid-column: 1/-1;
}

.csp-01__field input,
.csp-01__field select,
.csp-01__field textarea {
  width: 100%;
  font: 400 14.5px/1.4 system-ui,sans-serif;
  color: var(--ink);
  min-height: 44px;
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--surface);
  transition: border-color .15s,box-shadow .15s;
  resize: vertical;
}

.csp-01__field input:hover,
.csp-01__field select:hover,
.csp-01__field textarea:hover {
  border-color: oklch(0.85 0.01 265);
}

.csp-01__field input:focus,
.csp-01__field select:focus,
.csp-01__field textarea:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px var(--ring);
}

.csp-01__field :user-invalid {
  border-color: var(--danger);
  box-shadow: 0 0 0 4px oklch(0.58 0.21 25/.14);
}

.csp-01__inline {
  display: flex;
  gap: 8px;
}

.csp-01__hint {
  display: block;
  font: 400 12.5px/1.45 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 3px;
}

.csp-01__avatarrow {
  grid-column: 1/-1;
  display: flex;
  align-items: center;
  gap: 16px;
}

.csp-01__stack {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 4px;
}

.csp-01__avatar {
  display: grid;
  place-items: center;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  font: 650 19px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(140deg,var(--accent),oklch(0.72 0.14 200));
  box-shadow: 0 0 0 4px var(--surface),0 0 0 5px var(--line);
}

.csp-01__row {
  grid-column: 1/-1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  font: 550 14px/1.3 system-ui,sans-serif;
}

.csp-01__row+.csp-01__row {
  padding-top: 16px;
  border-top: 1px solid var(--line);
}

.csp-01__btn {
  flex: none;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--surface);
  font: 600 13.5px/1 system-ui,sans-serif;
  color: var(--ink);
  cursor: pointer;
  transition: background .15s,transform .1s;
}

.csp-01__btn:hover {
  background: oklch(0.97 0.004 265);
}

.csp-01__btn:active {
  transform: scale(.98);
}

.csp-01__btn--primary {
  background: var(--accent);
  color: #fff;
  border-color: transparent;
}

.csp-01__btn--primary:hover {
  background: oklch(0.5 0.2 268);
}

.csp-01__btn--ghost {
  background: transparent;
  color: #fff;
  border-color: oklch(1 0 0/.2);
}

.csp-01__btn--ghost:hover {
  background: oklch(1 0 0/.08);
}

.csp-01__switch {
  appearance: none;
  position: relative;
  flex: none;
  width: 44px;
  height: 26px;
  border-radius: 999px;
  background: oklch(0.88 0.01 265);
  cursor: pointer;
  transition: background .2s;
}

.csp-01__switch::before {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px oklch(0 0 0/.25);
  transition: translate .2s cubic-bezier(.3,.7,.4,1.3);
}

.csp-01__switch:checked {
  background: var(--accent);
}

.csp-01__switch:checked::before {
  translate: 18px 0;
}

.csp-01__switch:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.csp-01__bar {
  position: fixed;
  left: 50%;
  bottom: 22px;
  z-index: 20;
  width: min(540px,calc(100% - 32px));
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 8px 8px 18px;
  border-radius: 14px;
  background: oklch(0.2 0.02 265);
  color: #fff;
  box-shadow: 0 20px 44px -12px oklch(0 0 0/.45);
  translate: -50% 150%;
  opacity: 0;
  pointer-events: none;
  transition: translate .4s cubic-bezier(.2,.9,.3,1.15),opacity .2s,background .3s;
}

.csp-01__bar span {
  flex: 1;
  font: 500 13.5px/1.3 system-ui,sans-serif;
}

.csp-01.is-dirty .csp-01__bar {
  translate: -50% 0;
  opacity: 1;
  pointer-events: auto;
}

.csp-01.is-saved .csp-01__bar {
  background: oklch(0.48 0.13 155);
}

.csp-01.is-saved .csp-01__bar button {
  visibility: hidden;
}

@container (max-width: 760px) {
  .csp-01__shell {
    grid-template-columns: minmax(0,1fr);
    gap: 16px;
    padding: 0 16px 140px;
  }

  .csp-01__aside {
    top: 0;
    z-index: 10;
    margin-inline: -16px;
    padding: 10px 16px;
    background: color-mix(in oklab,var(--bg) 88%,transparent);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--line);
  }

  .csp-01__label {
    display: none;
  }

  .csp-01__nav {
    flex-direction: row;
    overflow-x: auto;
    scrollbar-width: none;
  }

  .csp-01__fields {
    grid-template-columns: minmax(0,1fr);
  }

  .csp-01__sec {
    scroll-margin-top: 76px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-01 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-01');
  var form = root.querySelector('[data-form]');
  var links = root.querySelectorAll('[data-nav] a');
  var msg = root.querySelector('[data-msg]');
  var reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;

  function setActive(id) {
    links.forEach(function (a) {
      if (a.getAttribute('href') === '#' + id) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
  }
  links.forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var target = root.querySelector(a.getAttribute('href'));
      var offset = parseFloat(getComputedStyle(target).scrollMarginTop) || 0;
      window.scrollTo({ top: target.getBoundingClientRect().top + scrollY - offset, behavior: reduce ? 'auto' : 'smooth' });
      setActive(target.id);
    });
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) setActive(en.target.id); });
  }, { rootMargin: '-30% 0px -60% 0px' });
  root.querySelectorAll('[data-section]').forEach(function (s) { io.observe(s); });

  form.addEventListener('input', function () { root.classList.add('is-dirty'); });
  form.addEventListener('change', function () { root.classList.add('is-dirty'); });
  form.addEventListener('reset', function () { root.classList.remove('is-dirty'); });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;
    msg.textContent = 'All changes saved';
    root.classList.add('is-saved');
    setTimeout(function () {
      root.classList.remove('is-dirty', 'is-saved');
      setTimeout(function () { msg.textContent = 'You have unsaved changes'; }, 400);
    }, 1400);
  });
})();
```

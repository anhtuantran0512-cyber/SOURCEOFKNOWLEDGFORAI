---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/profile-settings-form-with-avatar-upload/"
title: "Profile Settings Form with Avatar Upload"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "An account-settings panel that behaves like a modern app: an avatar you can replace (instant local preview via URL.createObjectURL), zoom with a range slider…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Profile Settings Form with Avatar Upload
Source: https://codefronts.com/components/css-forms/profile-settings-form-with-avatar-upload/

An account-settings panel that behaves like a modern app: an avatar you can replace (instant local preview via URL.createObjectURL), zoom with a range slider and remove; a username field with a fused @ prefix and a live availability check; a bio with counter; accessible role="switch" toggles; and a dirty-state save bar that slides up only when something actually changed — with Discard to restore the original values.
## HTML
```html
<div class="frm-09">
  <button type="button" class="frm-09__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-09__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-09__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-09__stage">
    <div class="frm-09__card" role="form" aria-labelledby="frm-09-title">
      <header class="frm-09__head">
        <h2 id="frm-09-title">Profile</h2>
        <p>This is how others will see you across the workspace.</p>
      </header>
      <section class="frm-09__avatarrow" aria-label="Profile photo">
        <div class="frm-09__avatar" style="--zoom:1">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=320&h=320&fit=crop&crop=faces&auto=format&q=75" width="160" height="160" alt="Your current profile photo" decoding="async">
          <span class="frm-09__initials" aria-hidden="true">MO</span>
        </div>
        <div class="frm-09__avctl">
          <div class="frm-09__avbtns">
            <label class="frm-09__btn frm-09__btn--solid"><input type="file" accept="image/png,image/jpeg,image/webp" class="frm-09__sr">Upload new</label>
            <button type="button" class="frm-09__btn frm-09__rm">Remove</button>
          </div>
          <label class="frm-09__zoom"><span>Zoom</span><input type="range" min="1" max="2" step="0.01" value="1" name="zoom" aria-label="Avatar zoom"></label>
          <p class="frm-09__hint">JPG, PNG or WebP. At least 400×400px.</p>
        </div>
      </section>
      <div class="frm-09__grid">
        <div class="frm-09__field"><label for="frm-09-name">Display name</label><input id="frm-09-name" name="name" value="Maya Okafor" autocomplete="name"></div>
        <div class="frm-09__field"><label for="frm-09-pr">Pronouns <span class="frm-09__opt">Optional</span></label>
          <select id="frm-09-pr" name="pronouns"><option value="">Prefer not to say</option><option selected>she/her</option><option>he/him</option><option>they/them</option></select></div>
      </div>
      <div class="frm-09__field">
        <label for="frm-09-user">Username</label>
        <div class="frm-09__prefix" data-state="idle"><span aria-hidden="true">app.loop.so/@</span><input id="frm-09-user" name="user" value="maya" autocomplete="username" spellcheck="false" aria-describedby="frm-09-user-msg"><i class="frm-09__spin" aria-hidden="true"></i></div>
        <p class="frm-09__hint" id="frm-09-user-msg" aria-live="polite">Letters, numbers and underscores.</p>
      </div>
      <div class="frm-09__field">
        <div class="frm-09__lr"><label for="frm-09-bio">Bio</label><span class="frm-09__count" aria-hidden="true">0/160</span></div>
        <textarea id="frm-09-bio" name="bio" rows="3" maxlength="160" aria-describedby="frm-09-bio-h">Design engineer. Building calm software in London. Tea &gt; coffee.</textarea>
        <p class="frm-09__hint" id="frm-09-bio-h">Brief description for your profile. URLs are hyperlinked.</p>
      </div>
      <div class="frm-09__field"><label for="frm-09-tz">Time zone</label>
        <select id="frm-09-tz" name="tz"><option>Pacific Time (US &amp; Canada)</option><option>Eastern Time (US &amp; Canada)</option><option selected>London (GMT/BST)</option><option>Sydney (AEST)</option><option>Auckland (NZST)</option></select></div>
      <fieldset class="frm-09__switches">
        <legend>Privacy &amp; notifications</legend>
        <label class="frm-09__row"><span><b>Show online status</b><small>Let teammates see when you're active.</small></span><span class="frm-09__switch"><input type="checkbox" role="switch" name="online" checked><i aria-hidden="true"></i></span></label>
        <label class="frm-09__row"><span><b>Weekly digest email</b><small>A Monday summary of mentions and tasks.</small></span><span class="frm-09__switch"><input type="checkbox" role="switch" name="digest"><i aria-hidden="true"></i></span></label>
        <label class="frm-09__row"><span><b>Searchable profile</b><small>Allow people outside your org to find you.</small></span><span class="frm-09__switch"><input type="checkbox" role="switch" name="search" checked><i aria-hidden="true"></i></span></label>
      </fieldset>
      <div class="frm-09__bar" role="region" aria-label="Unsaved changes">
        <span><i aria-hidden="true"></i>You have unsaved changes</span>
        <div><button type="button" class="frm-09__btn frm-09__discard">Discard</button><button type="button" class="frm-09__btn frm-09__btn--solid frm-09__save">Save changes</button></div>
      </div>
      <p class="frm-09__toast" role="status"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&display=swap');

.frm-09 {
  --bg: #f5f5f4;
  --card: #ffffff;
  --ink: #0c0a09;
  --muted: #78716c;
  --line: #e7e5e4;
  --soft: #fafaf9;
  --accent: #0c0a09;
  --on-accent: #fafaf9;
  --ok: #16a34a;
  --bad: #dc2626;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  --spring: cubic-bezier(.34,1.56,.64,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (transition-timing-function: linear(0, 1)) {
  .frm-09 {
    --spring: linear(0, .009, .035 2.1%, .141 4.4%, .723 12.9%, .938 16.7%, 1.017, 1.077, 1.121 26%, 1.149 28.4%, 1.159 31%, 1.15 33.7%, 1.123 37.1%, 1.017 46.2%, .991 50.9%, .977 55.5%, .975 60.4%, 1.003 79.4%, 1);
  }
}

@media (prefers-color-scheme: dark) {
  .frm-09:not([data-theme="light"]) {
    --bg: #0c0a09;
    --card: #161412;
    --ink: #fafaf9;
    --muted: #a8a29e;
    --line: #292524;
    --soft: #1c1917;
    --accent: #fafaf9;
    --on-accent: #0c0a09;
    --ok: #4ade80;
    --bad: #f87171;
  }
}

.frm-09[data-theme="dark"] {
  --bg: #0c0a09;
  --card: #161412;
  --ink: #fafaf9;
  --muted: #a8a29e;
  --line: #292524;
  --soft: #1c1917;
  --accent: #fafaf9;
  --on-accent: #0c0a09;
  --ok: #4ade80;
  --bad: #f87171;
}

.frm-09,
.frm-09 *,
.frm-09 *::before,
.frm-09 *::after {
  box-sizing: border-box;
}

.frm-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.frm-09__card {
  position: relative;
  overflow: hidden;
  width: 100%;
  max-width: 40rem;
  display: grid;
  gap: 1.4rem;
  padding: clamp(1.25rem,5vw,2.5rem) clamp(1.25rem,5vw,2.5rem) 5.5rem;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  box-shadow: 0 1px 2px rgba(0,0,0,.04), 0 24px 60px -30px rgba(0,0,0,.25);
}

.frm-09__head h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
  letter-spacing: -.025em;
}

.frm-09__head p {
  margin: .3rem 0 0;
  color: var(--muted);
  font-size: .93rem;
}

.frm-09__avatarrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1.4rem;
  padding: 1.25rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--soft);
}

.frm-09__avatar {
  position: relative;
  flex: none;
  width: 5.5rem;
  height: 5.5rem;
  border-radius: 50%;
  overflow: hidden;
  background: linear-gradient(135deg,#a8a29e,#57534e);
  box-shadow: 0 0 0 4px var(--card), 0 0 0 5px var(--line);
}

.frm-09__avatar img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  scale: var(--zoom);
  transition: scale .15s, opacity .3s;
}

.frm-09__avatar.is-empty img {
  opacity: 0;
}

.frm-09__initials {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  color: #fff;
  font-weight: 600;
  font-size: 1.6rem;
  opacity: 0;
  transition: opacity .3s;
}

.frm-09__avatar.is-empty .frm-09__initials {
  opacity: 1;
}

.frm-09__avatar.is-new {
  animation: frm-09-pop .6s var(--spring);
}

@keyframes frm-09-pop {
  from {
    scale: .85;
  }
}

.frm-09__avctl {
  flex: 1;
  min-width: 14rem;
  display: grid;
  gap: .7rem;
}

.frm-09__avbtns {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.frm-09__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.6rem;
  padding: 0 1rem;
  border-radius: .65rem;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font: inherit;
  font-size: .88rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .2s, translate .2s var(--ease);
}

.frm-09__btn:hover {
  background: var(--soft);
}

.frm-09__btn--solid {
  background: var(--accent);
  color: var(--on-accent);
  border-color: var(--accent);
}

.frm-09__btn--solid:hover {
  background: color-mix(in oklab,var(--accent) 85%,var(--card));
}

.frm-09__btn:focus-visible,
.frm-09__btn:focus-within {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.frm-09__zoom {
  display: flex;
  align-items: center;
  gap: .75rem;
  font-size: .8rem;
  font-weight: 600;
  color: var(--muted);
}

.frm-09__zoom input {
  flex: 1;
  max-width: 12rem;
  accent-color: var(--ink);
}

.frm-09__hint {
  margin: 0;
  font-size: .8rem;
  color: var(--muted);
}

.frm-09__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
}

.frm-09__field {
  display: grid;
  gap: .4rem;
}

.frm-09 label,
.frm-09 legend {
  font-size: .86rem;
  font-weight: 600;
}

.frm-09__opt {
  font-weight: 400;
  color: var(--muted);
}

.frm-09 input:not([type="range"]):not([type="checkbox"]):not([type="file"]),
.frm-09 select,
.frm-09 textarea {
  width: 100%;
  min-height: 2.9rem;
  padding: .65rem .9rem;
  border-radius: .7rem;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font: inherit;
  font-size: .95rem;
  transition: border-color .2s, box-shadow .2s;
}

.frm-09 textarea {
  resize: vertical;
  line-height: 1.5;
}

.frm-09 :is(input,select,textarea):focus-visible {
  outline: none;
  border-color: var(--ink);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--ink) 12%,transparent);
}

.frm-09__prefix {
  position: relative;
  display: flex;
  align-items: stretch;
  border: 1px solid var(--line);
  border-radius: .7rem;
  overflow: hidden;
  transition: border-color .2s, box-shadow .2s;
}

.frm-09__prefix:focus-within {
  border-color: var(--ink);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--ink) 12%,transparent);
}

.frm-09__prefix span {
  display: flex;
  align-items: center;
  padding: 0 .4rem 0 .9rem;
  background: var(--soft);
  color: var(--muted);
  font-size: .9rem;
  border-right: 1px solid var(--line);
  white-space: nowrap;
}

.frm-09__prefix input {
  border: 0 !important;
  box-shadow: none !important;
  border-radius: 0 !important;
  padding-right: 2.5rem !important;
}

.frm-09__spin {
  position: absolute;
  right: .85rem;
  top: 50%;
  width: 1rem;
  height: 1rem;
  margin-top: -.5rem;
  border-radius: 50%;
}

.frm-09__prefix[data-state="checking"] .frm-09__spin {
  border: 2px solid var(--line);
  border-top-color: var(--ink);
  animation: frm-09-spin .7s linear infinite;
}

.frm-09__prefix[data-state="ok"] .frm-09__spin {
  background: var(--ok);
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='m3.5 8.5 3 3 6-7' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E") center/contain no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='m3.5 8.5 3 3 6-7' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E") center/contain no-repeat;
}

.frm-09__prefix[data-state="taken"] {
  border-color: var(--bad);
}

.frm-09__field:has([data-state="taken"]) .frm-09__hint {
  color: var(--bad);
}

.frm-09__field:has([data-state="ok"]) .frm-09__hint {
  color: var(--ok);
}

@keyframes frm-09-spin {
  to {
    rotate: 1turn;
  }
}

.frm-09__lr {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.frm-09__count {
  font-size: .78rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.frm-09__switches {
  border: 0;
  margin: 0;
  padding: 0;
  display: grid;
  border-top: 1px solid var(--line);
}

.frm-09__switches legend {
  padding: 1.25rem 0 .4rem;
}

.frm-09__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .9rem 0;
  border-bottom: 1px solid var(--line);
  cursor: pointer;
  font-weight: 400 !important;
}

.frm-09__row b {
  display: block;
  font-weight: 600;
  font-size: .92rem;
}

.frm-09__row small {
  display: block;
  color: var(--muted);
  font-size: .82rem;
  margin-top: .15rem;
}

.frm-09__switch {
  position: relative;
  flex: none;
}

.frm-09__switch input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
  z-index: 1;
}

.frm-09__switch i {
  display: block;
  width: 2.75rem;
  height: 1.5rem;
  border-radius: 99px;
  background: var(--line);
  transition: background .25s;
}

.frm-09__switch i::after {
  content: '';
  display: block;
  width: 1.2rem;
  height: 1.2rem;
  margin: .15rem;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px rgba(0,0,0,.25);
  transition: translate .45s var(--spring);
}

.frm-09__switch input:checked + i {
  background: var(--ok);
}

.frm-09__switch input:checked + i::after {
  translate: 1.25rem 0;
}

.frm-09__switch input:focus-visible + i {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.frm-09__switch:active i::after {
  width: 1.45rem;
}

.frm-09__bar {
  position: absolute;
  left: .75rem;
  right: .75rem;
  bottom: .75rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
  padding: .6rem .6rem .6rem 1rem;
  border-radius: .9rem;
  background: var(--ink);
  color: var(--card);
  box-shadow: 0 18px 40px -16px rgba(0,0,0,.5);
  translate: 0 calc(100% + 1rem);
  visibility: hidden;
  transition: translate .55s var(--spring), visibility 0s .55s;
}

.frm-09[data-dirty] .frm-09__bar {
  translate: 0 0;
  visibility: visible;
  transition: translate .55s var(--spring), visibility 0s;
}

.frm-09__bar > span {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .88rem;
  font-weight: 500;
}

.frm-09__bar > span i {
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: #f59e0b;
}

.frm-09__bar div {
  display: flex;
  gap: .4rem;
}

.frm-09__bar .frm-09__btn {
  border-color: color-mix(in oklab,var(--card) 25%,transparent);
  background: transparent;
  color: var(--card);
}

.frm-09__bar .frm-09__btn--solid {
  background: var(--card);
  color: var(--ink);
}

.frm-09__bar .frm-09__btn:focus-visible {
  outline-color: var(--card);
}

.frm-09__toast {
  position: absolute;
  left: 50%;
  bottom: 1.4rem;
  translate: -50% 0;
  margin: 0;
  padding: .55rem 1rem;
  border-radius: 99px;
  background: var(--ok);
  color: #fff;
  font-size: .85rem;
  font-weight: 600;
  opacity: 0;
  pointer-events: none;
  transition: opacity .3s, translate .4s var(--spring);
  white-space: nowrap;
}

.frm-09__toast.is-on {
  opacity: 1;
  translate: -50% -.4rem;
}

.frm-09__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .frm-09 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-09__switch i {
    border: 1px solid CanvasText;
  }

  .frm-09__switch input:checked + i {
    background: Highlight;
  }

  .frm-09__bar {
    border: 1px solid CanvasText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-09 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-09__theme {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 20;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 22%, transparent);
  background: color-mix(in srgb, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .2s, transform .2s;
}

.frm-09__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-09__theme:active {
  transform: scale(.94);
}

.frm-09__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-09__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-09__theme .frm-09__sun,
.frm-09__theme[aria-pressed="true"] .frm-09__moon {
  display: none;
}

.frm-09__theme[aria-pressed="true"] .frm-09__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-09__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-09__theme {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.frm-09').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.frm-09');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const DEFAULT = $('.frm-09__avatar img').src, TAKEN = ['admin', 'support', 'alex', 'sam', 'loop'];
  const av = $('.frm-09__avatar'), img = av.querySelector('img'), file = $('input[type="file"]'), zoom = $('[name="zoom"]');
  const controls = [...root.querySelectorAll('[name]')];
  let objectUrl = null, avatarState = 'default';
  const snap = () => JSON.stringify([avatarState].concat(controls.map((c) => c.type === 'checkbox' ? c.checked : c.value)));
  let saved = snap(), savedValues = controls.map((c) => c.type === 'checkbox' ? c.checked : c.value), savedAvatar = { state: avatarState, src: DEFAULT };
  const dirty = () => root.toggleAttribute('data-dirty', snap() !== saved);
  root.addEventListener('input', dirty); root.addEventListener('change', dirty);
  zoom.addEventListener('input', () => av.style.setProperty('--zoom', zoom.value));
  file.addEventListener('change', () => {
    const f = file.files[0]; if (!f) return;
    if (objectUrl) URL.revokeObjectURL(objectUrl);
    objectUrl = URL.createObjectURL(f); img.src = objectUrl; av.classList.remove('is-empty');
    avatarState = 'new:' + f.name; av.classList.remove('is-new'); void av.offsetWidth; av.classList.add('is-new'); dirty();
  });
  $('.frm-09__rm').addEventListener('click', () => { av.classList.add('is-empty'); avatarState = 'removed'; dirty(); });
  const bio = $('#frm-09-bio'), count = $('.frm-09__count');
  const upd = () => { count.textContent = bio.value.length + '/160'; };
  bio.addEventListener('input', upd); upd();
  const user = $('#frm-09-user'), wrap = $('.frm-09__prefix'), msg = $('#frm-09-user-msg');
  let t;
  user.addEventListener('input', () => {
    clearTimeout(t);
    const v = user.value.trim().toLowerCase();
    if (!/^[a-z0-9_]{3,20}$/.test(v)) { wrap.dataset.state = 'taken'; msg.textContent = '3–20 letters, numbers or underscores.'; return; }
    wrap.dataset.state = 'checking'; msg.textContent = 'Checking availability…';
    t = setTimeout(() => {
      const taken = TAKEN.includes(v);
      wrap.dataset.state = taken ? 'taken' : 'ok';
      msg.textContent = taken ? '@' + v + ' is already taken.' : '@' + v + ' is available.';
    }, 450);
  });
  const toast = $('.frm-09__toast');
  $('.frm-09__save').addEventListener('click', () => {
    if (wrap.dataset.state === 'taken') { user.focus(); return; }
    saved = snap(); savedValues = controls.map((c) => c.type === 'checkbox' ? c.checked : c.value);
    savedAvatar = { state: avatarState, src: img.src, empty: av.classList.contains('is-empty') };
    root.removeAttribute('data-dirty');
    toast.textContent = 'Profile saved'; toast.classList.add('is-on'); setTimeout(() => toast.classList.remove('is-on'), 1800);
  });
  $('.frm-09__discard').addEventListener('click', () => {
    controls.forEach((c, i) => { if (c.type === 'checkbox') c.checked = savedValues[i]; else c.value = savedValues[i]; });
    avatarState = savedAvatar.state; img.src = savedAvatar.src; av.classList.toggle('is-empty', !!savedAvatar.empty);
    av.style.setProperty('--zoom', zoom.value); wrap.dataset.state = 'idle'; msg.textContent = 'Letters, numbers and underscores.';
    upd(); root.removeAttribute('data-dirty');
  });
})();
```

---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-profile-settings-form-avatar-upload/"
title: "Tailwind Profile Settings Form with Avatar Upload"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's account-settings panel, ported one-for-one to Tailwind v4: an avatar you can replace (instant local preview via URL.createObjectURL),…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Profile Settings Form with Avatar Upload
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-profile-settings-form-avatar-upload/

The CSS collection's account-settings panel, ported one-for-one to Tailwind v4: an avatar you can replace (instant local preview via URL.createObjectURL), zoom with a slider and remove; a username field with a fused app.loop.so/@ prefix and a live availability check; a bio counter; accessible role="switch" toggles on a linear() spring; and a dirty-state save bar that springs up from the card edge only when something has actually changed.
## HTML
```html
<div class="tf-09 relative block min-h-svh w-full bg-tf09-bg pt-[72px] font-tf09-sans leading-[normal] text-tf09-ink antialiased motion-reduce:**:animate-none! motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,5vw,4rem)]">
    <div class="relative grid w-full max-w-[40rem] gap-[1.4rem] overflow-hidden rounded-[1.25rem] border border-tf09-line bg-tf09-card px-[clamp(1.25rem,5vw,2.5rem)] pt-[clamp(1.25rem,5vw,2.5rem)] pb-[5.5rem] shadow-[0_1px_2px_rgba(0,0,0,.04),0_24px_60px_-30px_rgba(0,0,0,.25)]" role="form" aria-labelledby="tf-09-title">
      <header>
        <h2 id="tf-09-title" class="text-[1.5rem] font-semibold tracking-[-.025em]">Profile</h2>
        <p class="mt-[.3rem] text-[.93rem] text-tf09-muted">This is how others will see you across the workspace.</p>
      </header>
      <section class="flex flex-wrap items-center gap-[1.4rem] rounded-2xl border border-tf09-line bg-tf09-soft p-5" aria-label="Profile photo">
        <div class="tf-09__avatar relative size-[5.5rem] flex-none overflow-hidden rounded-full bg-[linear-gradient(135deg,#a8a29e,#57534e)] shadow-[0_0_0_4px_var(--color-tf09-card),0_0_0_5px_var(--color-tf09-line)] [&.is-new]:animate-tf09-pop" style="--zoom:1">
          <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=320&h=320&fit=crop&crop=faces&auto=format&q=75" width="160" height="160" alt="Your current profile photo" decoding="async" class="absolute inset-0 size-full object-cover [scale:var(--zoom)] [transition:scale_.15s,opacity_.3s] in-[.is-empty]:opacity-0">
          <span class="absolute inset-0 grid place-items-center text-[1.6rem] font-semibold text-white opacity-0 [transition:opacity_.3s] in-[.is-empty]:opacity-100" aria-hidden="true">MO</span>
        </div>
        <div class="grid min-w-56 flex-1 gap-[.7rem]">
          <div class="flex flex-wrap gap-2">
            <label class="inline-flex min-h-[2.6rem] cursor-pointer items-center justify-center rounded-[.65rem] border px-4 font-semibold [transition:background_.2s,translate_.2s_var(--ease-tf09)] focus-within:outline-2 focus-within:outline-offset-2 focus-within:outline-tf09-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf09-ink border-tf09-accent bg-tf09-accent text-tf09-on hover:bg-[color-mix(in_oklab,var(--color-tf09-accent)_85%,var(--color-tf09-card))] text-[.86rem]"><input type="file" accept="image/png,image/jpeg,image/webp" class="sr-only">Upload new</label>
            <button type="button" class="tf-09__rm inline-flex min-h-[2.6rem] cursor-pointer items-center justify-center rounded-[.65rem] border px-4 font-semibold [transition:background_.2s,translate_.2s_var(--ease-tf09)] focus-within:outline-2 focus-within:outline-offset-2 focus-within:outline-tf09-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf09-ink border-tf09-line bg-tf09-card text-tf09-ink hover:bg-tf09-soft text-[.88rem]">Remove</button>
          </div>
          <label class="flex items-center gap-3 text-[.8rem] font-semibold text-tf09-muted"><span>Zoom</span><input type="range" min="1" max="2" step="0.01" value="1" name="zoom" aria-label="Avatar zoom" class="max-w-48 flex-1 accent-tf09-ink"></label>
          <p class="text-[.8rem] text-tf09-muted">JPG, PNG or WebP. At least 400×400px.</p>
        </div>
      </section>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-4">
        <div class="grid gap-[.4rem]"><label for="tf-09-name" class="text-[.86rem] font-semibold">Display name</label><input id="tf-09-name" name="name" value="Maya Okafor" autocomplete="name" class="min-h-[2.9rem] w-full rounded-[.7rem] border border-tf09-line bg-tf09-card px-[.9rem] py-[.65rem] text-[.95rem] text-tf09-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf09-ink focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf09-ink)_12%,transparent)] focus-visible:outline-none"></div>
        <div class="grid gap-[.4rem]"><label for="tf-09-pr" class="text-[.86rem] font-semibold">Pronouns <span class="font-normal text-tf09-muted">Optional</span></label>
          <select id="tf-09-pr" name="pronouns" class="min-h-[2.9rem] w-full rounded-[.7rem] border border-tf09-line bg-tf09-card px-[.9rem] py-[.65rem] text-[.95rem] text-tf09-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf09-ink focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf09-ink)_12%,transparent)] focus-visible:outline-none"><option value="">Prefer not to say</option><option selected>she/her</option><option>he/him</option><option>they/them</option></select></div>
      </div>
      <div class="group/f grid gap-[.4rem]">
        <label for="tf-09-user" class="text-[.86rem] font-semibold">Username</label>
        <div class="tf-09__prefix group/px relative flex items-stretch overflow-hidden rounded-[.7rem] border border-tf09-line [transition:border-color_.2s,box-shadow_.2s] focus-within:border-tf09-ink focus-within:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf09-ink)_12%,transparent)] data-[state=taken]:border-tf09-bad" data-state="idle"><span aria-hidden="true" class="flex items-center border-r border-tf09-line bg-tf09-soft pr-[.4rem] pl-[.9rem] text-[.9rem] whitespace-nowrap text-tf09-muted">app.loop.so/@</span><input id="tf-09-user" name="user" value="maya" autocomplete="username" spellcheck="false" aria-describedby="tf-09-user-msg" class="min-h-[2.9rem] w-full border-0 bg-tf09-card py-[.65rem] pr-10 pl-[.9rem] text-[.95rem] text-tf09-ink outline-none"><i class="absolute top-1/2 right-[.85rem] -mt-2 size-4 rounded-full group-data-[state=checking]/px:animate-tf09-spin group-data-[state=checking]/px:border-2 group-data-[state=checking]/px:border-tf09-line group-data-[state=checking]/px:border-t-tf09-ink group-data-[state=ok]/px:bg-tf09-ok group-data-[state=ok]/px:[mask:var(--tf09-tick)_center/contain_no-repeat]" aria-hidden="true"></i></div>
        <p class="text-[.8rem] text-tf09-muted group-has-[[data-state=ok]]/f:text-tf09-ok group-has-[[data-state=taken]]/f:text-tf09-bad" id="tf-09-user-msg" aria-live="polite">Letters, numbers and underscores.</p>
      </div>
      <div class="grid gap-[.4rem]">
        <div class="flex items-baseline justify-between"><label for="tf-09-bio" class="text-[.86rem] font-semibold">Bio</label><span class="tf-09__count text-[.78rem] text-tf09-muted tabular-nums" aria-hidden="true">0/160</span></div>
        <textarea id="tf-09-bio" name="bio" rows="3" maxlength="160" aria-describedby="tf-09-bio-h" class="min-h-[2.9rem] w-full rounded-[.7rem] border border-tf09-line bg-tf09-card px-[.9rem] py-[.65rem] text-[.95rem] text-tf09-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf09-ink focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf09-ink)_12%,transparent)] focus-visible:outline-none resize-y leading-[1.5]">Design engineer. Building calm software in London. Tea &gt; coffee.</textarea>
        <p class="text-[.8rem] text-tf09-muted" id="tf-09-bio-h">Brief description for your profile. URLs are hyperlinked.</p>
      </div>
      <div class="grid gap-[.4rem]"><label for="tf-09-tz" class="text-[.86rem] font-semibold">Time zone</label>
        <select id="tf-09-tz" name="tz" class="min-h-[2.9rem] w-full rounded-[.7rem] border border-tf09-line bg-tf09-card px-[.9rem] py-[.65rem] text-[.95rem] text-tf09-ink [transition:border-color_.2s,box-shadow_.2s] focus-visible:border-tf09-ink focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf09-ink)_12%,transparent)] focus-visible:outline-none"><option>Pacific Time (US &amp; Canada)</option><option>Eastern Time (US &amp; Canada)</option><option selected>London (GMT/BST)</option><option>Sydney (AEST)</option><option>Auckland (NZST)</option></select></div>
      <fieldset class="grid border-t border-tf09-line">
        <legend class="pt-5 pb-[.4rem] text-[.86rem] font-semibold">Privacy &amp; notifications</legend>
        <label class="flex cursor-pointer items-center justify-between gap-4 border-b border-tf09-line py-[.9rem] text-[.86rem] font-normal"><span><b class="block text-[.92rem] font-semibold">Show online status</b><small class="mt-[.15rem] block text-[.82rem] text-tf09-muted">Let teammates see when you're active.</small></span><span class="group/sw relative flex-none"><input type="checkbox" role="switch" name="online" checked class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><i aria-hidden="true" class="block h-6 w-11 rounded-full bg-tf09-line [transition:background_.25s] after:m-[.15rem] after:block after:size-[1.2rem] after:rounded-full after:bg-white after:shadow-[0_1px_3px_rgba(0,0,0,.25)] after:[transition:translate_.45s_var(--tf09-spring)] after:content-[''] group-active/sw:after:w-[1.45rem] peer-checked:bg-tf09-ok peer-checked:after:translate-x-5 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf09-ink forced-colors:border forced-colors:border-[CanvasText] forced-colors:peer-checked:bg-[Highlight]"></i></span></label>
        <label class="flex cursor-pointer items-center justify-between gap-4 border-b border-tf09-line py-[.9rem] text-[.86rem] font-normal"><span><b class="block text-[.92rem] font-semibold">Weekly digest email</b><small class="mt-[.15rem] block text-[.82rem] text-tf09-muted">A Monday summary of mentions and tasks.</small></span><span class="group/sw relative flex-none"><input type="checkbox" role="switch" name="digest" class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><i aria-hidden="true" class="block h-6 w-11 rounded-full bg-tf09-line [transition:background_.25s] after:m-[.15rem] after:block after:size-[1.2rem] after:rounded-full after:bg-white after:shadow-[0_1px_3px_rgba(0,0,0,.25)] after:[transition:translate_.45s_var(--tf09-spring)] after:content-[''] group-active/sw:after:w-[1.45rem] peer-checked:bg-tf09-ok peer-checked:after:translate-x-5 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf09-ink forced-colors:border forced-colors:border-[CanvasText] forced-colors:peer-checked:bg-[Highlight]"></i></span></label>
        <label class="flex cursor-pointer items-center justify-between gap-4 border-b border-tf09-line py-[.9rem] text-[.86rem] font-normal"><span><b class="block text-[.92rem] font-semibold">Searchable profile</b><small class="mt-[.15rem] block text-[.82rem] text-tf09-muted">Allow people outside your org to find you.</small></span><span class="group/sw relative flex-none"><input type="checkbox" role="switch" name="search" checked class="peer absolute inset-0 z-1 m-0 cursor-pointer opacity-0"><i aria-hidden="true" class="block h-6 w-11 rounded-full bg-tf09-line [transition:background_.25s] after:m-[.15rem] after:block after:size-[1.2rem] after:rounded-full after:bg-white after:shadow-[0_1px_3px_rgba(0,0,0,.25)] after:[transition:translate_.45s_var(--tf09-spring)] after:content-[''] group-active/sw:after:w-[1.45rem] peer-checked:bg-tf09-ok peer-checked:after:translate-x-5 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf09-ink forced-colors:border forced-colors:border-[CanvasText] forced-colors:peer-checked:bg-[Highlight]"></i></span></label>
      </fieldset>
      <div class="invisible absolute right-3 bottom-3 left-3 flex translate-y-[calc(100%+1rem)] flex-wrap items-center justify-between gap-3 rounded-[.9rem] bg-tf09-ink py-[.6rem] pr-[.6rem] pl-4 text-tf09-card shadow-[0_18px_40px_-16px_rgba(0,0,0,.5)] [transition:translate_.55s_var(--tf09-spring),visibility_0s_.55s] in-data-dirty:visible in-data-dirty:translate-y-0 in-data-dirty:[transition:translate_.55s_var(--tf09-spring),visibility_0s] forced-colors:border forced-colors:border-[CanvasText]" role="region" aria-label="Unsaved changes">
        <span class="flex items-center gap-[.55rem] text-[.88rem] font-medium"><i aria-hidden="true" class="size-2 rounded-full bg-[#f59e0b]"></i>You have unsaved changes</span>
        <div class="flex gap-[.4rem]"><button type="button" class="tf-09__discard inline-flex min-h-[2.6rem] cursor-pointer items-center justify-center rounded-[.65rem] border px-4 font-semibold [transition:background_.2s,translate_.2s_var(--ease-tf09)] focus-within:outline-2 focus-within:outline-offset-2 focus-within:outline-tf09-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf09-ink border-tf09-card/25 bg-transparent text-[.88rem] text-tf09-card focus-visible:outline-tf09-card">Discard</button><button type="button" class="tf-09__save inline-flex min-h-[2.6rem] cursor-pointer items-center justify-center rounded-[.65rem] border px-4 font-semibold [transition:background_.2s,translate_.2s_var(--ease-tf09)] focus-within:outline-2 focus-within:outline-offset-2 focus-within:outline-tf09-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tf09-ink border-tf09-card bg-tf09-card text-[.88rem] text-tf09-ink focus-visible:outline-tf09-card">Save changes</button></div>
      </div>
      <p class="tf-09__toast pointer-events-none absolute bottom-[1.4rem] left-1/2 -translate-x-1/2 rounded-full bg-tf09-ok px-4 py-[.55rem] text-[.85rem] font-semibold whitespace-nowrap text-white opacity-0 [transition:opacity_.3s,translate_.4s_var(--tf09-spring)] [&.is-on]:-translate-y-[.4rem] [&.is-on]:opacity-100" role="status"></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf09-bg: #f5f5f4;
  --color-tf09-card: #ffffff;
  --color-tf09-ink: #0c0a09;
  --color-tf09-muted: #78716c;
  --color-tf09-line: #e7e5e4;
  --color-tf09-soft: #fafaf9;
  --color-tf09-accent: #0c0a09;
  --color-tf09-on: #fafaf9;
  --color-tf09-ok: #16a34a;
  --color-tf09-bad: #dc2626;
  --font-tf09-sans: "Instrument Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf09: cubic-bezier(0.16,1,0.3,1);
  --animate-tf09-pop: tf09-pop 0.6s var(--tf09-spring);
  --animate-tf09-spin: tf09-spin 0.7s linear infinite;

  @keyframes tf09-pop {
    from {
      scale: 0.85;
    }
  }

  @keyframes tf09-spin {
    to {
      rotate: 1turn;
    }
  }
}
/* Root rule: full-bleed contract + scheme switch, the spring easing (linear() with a fallback)
   and the tick mask data URI. Dark values override the @theme variables. */

.tf-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light;
  --tf09-spring: cubic-bezier(0.34,1.56,0.64,1);
  --tf09-tick: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='m3.5 8.5 3 3 6-7' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E");
}

@supports (transition-timing-function: linear(0, 1)) {
  .tf-09 {
    --tf09-spring: linear(0, 0.009, 0.035 2.1%, 0.141 4.4%, 0.723 12.9%, 0.938 16.7%, 1.017, 1.077, 1.121 26%, 1.149 28.4%, 1.159 31%, 1.15 33.7%, 1.123 37.1%, 1.017 46.2%, 0.991 50.9%, 0.977 55.5%, 0.975 60.4%, 1.003 79.4%, 1);
  }
}

.tf-09[data-theme="dark"] {
  color-scheme: dark;
  --color-tf09-bg: #0c0a09;
  --color-tf09-card: #161412;
  --color-tf09-ink: #fafaf9;
  --color-tf09-muted: #a8a29e;
  --color-tf09-line: #292524;
  --color-tf09-soft: #1c1917;
  --color-tf09-accent: #fafaf9;
  --color-tf09-on: #0c0a09;
  --color-tf09-ok: #4ade80;
  --color-tf09-bad: #f87171;
}

@media (prefers-color-scheme: dark) {
  .tf-09:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tf09-bg: #0c0a09;
    --color-tf09-card: #161412;
    --color-tf09-ink: #fafaf9;
    --color-tf09-muted: #a8a29e;
    --color-tf09-line: #292524;
    --color-tf09-soft: #1c1917;
    --color-tf09-accent: #fafaf9;
    --color-tf09-on: #0c0a09;
    --color-tf09-ok: #4ade80;
    --color-tf09-bad: #f87171;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-09').forEach((root) => {
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
  const root = document.querySelector('.tf-09');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const DEFAULT = $('.tf-09__avatar img').src, TAKEN = ['admin', 'support', 'alex', 'sam', 'loop'];
  const av = $('.tf-09__avatar'), img = av.querySelector('img'), file = $('input[type="file"]'), zoom = $('[name="zoom"]');
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
  $('.tf-09__rm').addEventListener('click', () => { av.classList.add('is-empty'); avatarState = 'removed'; dirty(); });
  const bio = $('#tf-09-bio'), count = $('.tf-09__count');
  const upd = () => { count.textContent = bio.value.length + '/160'; };
  bio.addEventListener('input', upd); upd();
  const user = $('#tf-09-user'), wrap = $('.tf-09__prefix'), msg = $('#tf-09-user-msg');
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
  const toast = $('.tf-09__toast');
  $('.tf-09__save').addEventListener('click', () => {
    if (wrap.dataset.state === 'taken') { user.focus(); return; }
    saved = snap(); savedValues = controls.map((c) => c.type === 'checkbox' ? c.checked : c.value);
    savedAvatar = { state: avatarState, src: img.src, empty: av.classList.contains('is-empty') };
    root.removeAttribute('data-dirty');
    toast.textContent = 'Profile saved'; toast.classList.add('is-on'); setTimeout(() => toast.classList.remove('is-on'), 1800);
  });
  $('.tf-09__discard').addEventListener('click', () => {
    controls.forEach((c, i) => { if (c.type === 'checkbox') c.checked = savedValues[i]; else c.value = savedValues[i]; });
    avatarState = savedAvatar.state; img.src = savedAvatar.src; av.classList.toggle('is-empty', !!savedAvatar.empty);
    av.style.setProperty('--zoom', zoom.value); wrap.dataset.state = 'idle'; msg.textContent = 'Letters, numbers and underscores.';
    upd(); root.removeAttribute('data-dirty');
  });
})();
```

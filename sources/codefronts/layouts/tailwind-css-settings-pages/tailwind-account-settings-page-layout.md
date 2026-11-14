---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-account-settings-page-layout/"
title: "Tailwind Account Settings Page Layout"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A complete SaaS account settings layout in Tailwind v4: a sticky section nav that tracks the card you are reading, Profile, Email & login, Preferences and…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Account Settings Page Layout
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-account-settings-page-layout/

A complete SaaS account settings layout in Tailwind v4: a sticky section nav that tracks the card you are reading, Profile, Email & login, Preferences and Privacy cards, whole-row switches built from real checkboxes, user-invalid: validation and a floating save bar that springs up on the first edit. Below lg the sidebar becomes a swipeable tab strip.
## HTML
```html
<section data-tsp01 class="tsp-01 group/page w-full min-h-svh bg-tsp01-bg font-tsp01-sans text-tsp01-ink antialiased" aria-labelledby="tsp-01-h">
  <div class="mx-auto grid w-full max-w-6xl gap-8 px-4 py-10 sm:px-8 lg:grid-cols-[15rem_minmax(0,1fr)] lg:gap-12 lg:py-14">
    <aside class="min-w-0 lg:sticky lg:top-10 lg:self-start">
      <p class="mb-3 hidden px-3 text-xs font-semibold uppercase tracking-[0.14em] text-tsp01-mut lg:block">Settings</p>
      <nav aria-label="Account sections" class="flex gap-1 overflow-x-auto rounded-2xl border border-tsp01-line bg-white/70 p-1.5 [scrollbar-width:none] lg:flex-col lg:overflow-visible lg:border-0 lg:bg-transparent lg:p-0">
        <a data-nav href="#tsp-01-profile" aria-current="true" class="flex min-h-11 flex-none items-center gap-3 rounded-xl px-3 text-sm font-medium text-tsp01-mut transition hover:bg-white hover:text-tsp01-ink focus-visible:outline-2 focus-visible:outline-tsp01-acc aria-[current=true]:bg-white aria-[current=true]:text-tsp01-ink aria-[current=true]:shadow-[0_1px_2px_rgb(0_0_0/0.06),0_0_0_1px_var(--color-tsp01-line)]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>Profile</a>
        <a data-nav href="#tsp-01-login" class="flex min-h-11 flex-none items-center gap-3 rounded-xl px-3 text-sm font-medium text-tsp01-mut transition hover:bg-white hover:text-tsp01-ink focus-visible:outline-2 focus-visible:outline-tsp01-acc aria-[current=true]:bg-white aria-[current=true]:text-tsp01-ink aria-[current=true]:shadow-[0_1px_2px_rgb(0_0_0/0.06),0_0_0_1px_var(--color-tsp01-line)]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>Email &amp; login</a>
        <a data-nav href="#tsp-01-prefs" class="flex min-h-11 flex-none items-center gap-3 rounded-xl px-3 text-sm font-medium text-tsp01-mut transition hover:bg-white hover:text-tsp01-ink focus-visible:outline-2 focus-visible:outline-tsp01-acc aria-[current=true]:bg-white aria-[current=true]:text-tsp01-ink aria-[current=true]:shadow-[0_1px_2px_rgb(0_0_0/0.06),0_0_0_1px_var(--color-tsp01-line)]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>Preferences</a>
        <a data-nav href="#tsp-01-privacy" class="flex min-h-11 flex-none items-center gap-3 rounded-xl px-3 text-sm font-medium text-tsp01-mut transition hover:bg-white hover:text-tsp01-ink focus-visible:outline-2 focus-visible:outline-tsp01-acc aria-[current=true]:bg-white aria-[current=true]:text-tsp01-ink aria-[current=true]:shadow-[0_1px_2px_rgb(0_0_0/0.06),0_0_0_1px_var(--color-tsp01-line)]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/></svg>Privacy</a>
      </nav>
      <div class="mt-6 hidden rounded-2xl border border-tsp01-line bg-white p-4 lg:block">
        <div class="flex items-center justify-between text-sm"><span class="font-semibold">Profile strength</span><span class="font-semibold tabular-nums text-tsp01-acc">80%</span></div>
        <div class="mt-3 h-1.5 rounded-full bg-tsp01-line"><div class="h-full w-4/5 rounded-full bg-linear-to-r from-tsp01-acc to-tsp01-acc2"></div></div>
        <p class="mt-3 text-xs leading-relaxed text-tsp01-mut">Add a profile photo to reach 100% — profiles with photos get 3× more mentions.</p>
      </div>
    </aside>

    <form data-form class="grid min-w-0 gap-6 pb-28" novalidate>
      <header>
        <h1 id="tsp-01-h" class="text-3xl font-semibold tracking-tight">Account</h1>
        <p class="mt-1 text-pretty text-tsp01-mut">Manage how you appear to teammates and how you sign in.</p>
      </header>

      <section id="tsp-01-profile" data-section class="grid scroll-mt-10 gap-6 rounded-3xl border border-tsp01-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-8 xl:grid-cols-[13rem_minmax(0,1fr)]" aria-labelledby="tsp-01-profile-h">
        <div><h2 id="tsp-01-profile-h" class="font-semibold">Profile</h2><p class="mt-1 text-sm text-tsp01-mut">Shown on comments, mentions and shared documents.</p></div>
        <div class="grid gap-5 sm:grid-cols-2">
          <div class="flex flex-wrap items-center gap-4 sm:col-span-2">
            <span class="relative grid size-16 place-items-center rounded-full bg-linear-135 from-tsp01-acc to-tsp01-acc2 text-lg font-semibold text-white shadow-[0_8px_24px_-8px_var(--color-tsp01-acc)]" aria-hidden="true">AM<span class="absolute bottom-0.5 right-0.5 size-3.5 rounded-full bg-emerald-500 ring-2 ring-white"></span></span>
            <div class="grid gap-1.5">
              <div class="flex flex-wrap gap-2"><button type="button" class="inline-flex min-h-11 items-center rounded-xl border border-tsp01-line bg-white px-4 text-sm font-semibold shadow-xs transition hover:bg-tsp01-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp01-acc">Upload photo</button><button type="button" class="inline-flex min-h-11 items-center rounded-xl px-3 text-sm font-semibold text-tsp01-mut transition hover:text-tsp01-ink focus-visible:outline-2 focus-visible:outline-tsp01-acc">Remove</button></div>
              <small class="text-xs text-tsp01-mut">PNG or JPG, square, up to 2&nbsp;MB</small>
            </div>
          </div>
          <label class="grid content-start gap-1.5"><span class="text-sm font-medium">Full name</span><input name="name" value="Ava Mitchell" autocomplete="name" required class="peer min-h-11 rounded-xl border border-tsp01-line bg-white px-3.5 text-sm shadow-xs outline-none transition focus:border-tsp01-acc focus:ring-4 focus:ring-tsp01-acc/15 user-invalid:border-rose-500 user-invalid:ring-4 user-invalid:ring-rose-500/15"><span class="hidden text-xs font-medium text-rose-600 peer-user-invalid:block">Your name is required.</span></label>
          <label class="grid content-start gap-1.5"><span class="text-sm font-medium">Job title</span><input name="title" value="Product Designer" autocomplete="organization-title" class="min-h-11 rounded-xl border border-tsp01-line bg-white px-3.5 text-sm shadow-xs outline-none transition focus:border-tsp01-acc focus:ring-4 focus:ring-tsp01-acc/15"></label>
          <label class="grid content-start gap-1.5 sm:col-span-2"><span class="text-sm font-medium">Username</span><span class="flex min-h-11 overflow-hidden rounded-xl border border-tsp01-line bg-white shadow-xs transition focus-within:border-tsp01-acc focus-within:ring-4 focus-within:ring-tsp01-acc/15"><span class="grid place-items-center border-r border-tsp01-line bg-tsp01-bg px-3 text-sm text-tsp01-mut">northwind.co/</span><input name="user" value="ava" pattern="[a-z0-9-]{2,24}" class="min-w-0 flex-1 px-3 text-sm outline-none"></span></label>
          <label class="grid gap-1.5 sm:col-span-2"><span class="flex justify-between text-sm font-medium">Bio <span data-count class="font-normal tabular-nums text-tsp01-mut">0 / 160</span></span><textarea name="bio" rows="3" maxlength="160" class="rounded-xl border border-tsp01-line bg-white px-3.5 py-3 text-sm shadow-xs outline-none transition [field-sizing:content] min-h-24 focus:border-tsp01-acc focus:ring-4 focus:ring-tsp01-acc/15">Designing calm, accessible tools for busy teams.</textarea></label>
        </div>
      </section>

      <section id="tsp-01-login" data-section class="grid scroll-mt-10 gap-6 rounded-3xl border border-tsp01-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-8 xl:grid-cols-[13rem_minmax(0,1fr)]" aria-labelledby="tsp-01-login-h">
        <div><h2 id="tsp-01-login-h" class="font-semibold">Email &amp; login</h2><p class="mt-1 text-sm text-tsp01-mut">Used to sign in and receive security alerts.</p></div>
        <div class="grid gap-5">
          <label class="grid gap-1.5"><span class="flex items-center gap-2 text-sm font-medium">Email address <span class="rounded-full bg-emerald-50 px-2 py-0.5 text-[11px] font-semibold text-emerald-700">Verified</span></span><input type="email" name="email" value="[email protected]" autocomplete="email" required class="peer min-h-11 rounded-xl border border-tsp01-line bg-white px-3.5 text-sm shadow-xs outline-none transition focus:border-tsp01-acc focus:ring-4 focus:ring-tsp01-acc/15 user-invalid:border-rose-500 user-invalid:ring-4 user-invalid:ring-rose-500/15"><span class="hidden text-xs font-medium text-rose-600 peer-user-invalid:block">Enter a valid email address.</span></label>
          <div class="flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-tsp01-line p-4"><div><p class="text-sm font-medium">Password</p><p class="text-sm text-tsp01-mut">Last changed 3 months ago</p></div><button type="button" class="inline-flex min-h-11 items-center rounded-xl border border-tsp01-line bg-white px-4 text-sm font-semibold shadow-xs transition hover:bg-tsp01-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp01-acc">Change password</button></div>
          <label class="flex min-h-11 cursor-pointer items-center justify-between gap-4 rounded-2xl border border-tsp01-line p-4 transition hover:bg-tsp01-bg/60"><span><span class="block text-sm font-medium">Sign in with Google</span><span class="block text-sm text-tsp01-mut">Connected as [email protected]</span></span><span class="relative flex-none"><input name="google" type="checkbox" role="switch" checked class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-zinc-300 transition peer-checked:bg-tsp01-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp01-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5 motion-reduce:transition-none"></span></span></label>
        </div>
      </section>

      <section id="tsp-01-prefs" data-section class="grid scroll-mt-10 gap-6 rounded-3xl border border-tsp01-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-8 xl:grid-cols-[13rem_minmax(0,1fr)]" aria-labelledby="tsp-01-prefs-h">
        <div><h2 id="tsp-01-prefs-h" class="font-semibold">Preferences</h2><p class="mt-1 text-sm text-tsp01-mut">Language and regional formats.</p></div>
        <div class="grid gap-5 sm:grid-cols-2">
          <label class="grid gap-1.5"><span class="text-sm font-medium">Language</span><select name="lang" class="min-h-11 rounded-xl border border-tsp01-line bg-white px-3 text-sm shadow-xs outline-none focus:border-tsp01-acc focus:ring-4 focus:ring-tsp01-acc/15"><option>English (United States)</option><option>English (United Kingdom)</option><option>English (Australia)</option><option>Deutsch</option><option>Français</option></select></label>
          <label class="grid gap-1.5"><span class="text-sm font-medium">Time zone</span><select name="tz" class="min-h-11 rounded-xl border border-tsp01-line bg-white px-3 text-sm shadow-xs outline-none focus:border-tsp01-acc focus:ring-4 focus:ring-tsp01-acc/15"><option>(GMT−08:00) Pacific Time</option><option>(GMT−05:00) Eastern Time</option><option>(GMT+00:00) London</option><option>(GMT+10:00) Sydney</option></select></label>
          <label class="grid gap-1.5"><span class="text-sm font-medium">Date format</span><select name="date" class="min-h-11 rounded-xl border border-tsp01-line bg-white px-3 text-sm shadow-xs outline-none focus:border-tsp01-acc focus:ring-4 focus:ring-tsp01-acc/15"><option>Oct 7, 2026</option><option>07/10/2026</option><option>2026-10-07</option></select></label>
          <label class="grid gap-1.5"><span class="text-sm font-medium">Start of week</span><select name="week" class="min-h-11 rounded-xl border border-tsp01-line bg-white px-3 text-sm shadow-xs outline-none focus:border-tsp01-acc focus:ring-4 focus:ring-tsp01-acc/15"><option>Sunday</option><option>Monday</option></select></label>
        </div>
      </section>

      <section id="tsp-01-privacy" data-section class="grid scroll-mt-10 gap-6 rounded-3xl border border-tsp01-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-8 xl:grid-cols-[13rem_minmax(0,1fr)]" aria-labelledby="tsp-01-privacy-h">
        <div><h2 id="tsp-01-privacy-h" class="font-semibold">Privacy</h2><p class="mt-1 text-sm text-tsp01-mut">Control what others in your workspace can see.</p></div>
        <div class="grid divide-y divide-tsp01-line rounded-2xl border border-tsp01-line">
          <label class="flex min-h-11 cursor-pointer items-center justify-between gap-4 p-4 transition hover:bg-tsp01-bg/60"><span><span class="block text-sm font-medium">Show my activity status</span><span class="block text-sm text-tsp01-mut">Teammates see when you're online.</span></span><span class="relative flex-none"><input name="status" type="checkbox" role="switch" checked class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-zinc-300 transition peer-checked:bg-tsp01-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp01-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5 motion-reduce:transition-none"></span></span></label>
          <label class="flex min-h-11 cursor-pointer items-center justify-between gap-4 p-4 transition hover:bg-tsp01-bg/60"><span><span class="block text-sm font-medium">Searchable profile</span><span class="block text-sm text-tsp01-mut">Appear in member search across the organisation.</span></span><span class="relative flex-none"><input name="search" type="checkbox" role="switch" checked class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-zinc-300 transition peer-checked:bg-tsp01-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp01-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5 motion-reduce:transition-none"></span></span></label>
          <label class="flex min-h-11 cursor-pointer items-center justify-between gap-4 p-4 transition hover:bg-tsp01-bg/60"><span><span class="block text-sm font-medium">Share usage analytics</span><span class="block text-sm text-tsp01-mut">Anonymous data that helps us improve the product.</span></span><span class="relative flex-none"><input name="analytics" type="checkbox" role="switch" class="peer sr-only"><span class="block h-6 w-11 rounded-full bg-zinc-300 transition peer-checked:bg-tsp01-acc peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tsp01-acc"></span><span class="pointer-events-none absolute left-0.5 top-0.5 size-5 rounded-full bg-white shadow-sm transition peer-checked:translate-x-5 motion-reduce:transition-none"></span></span></label>
        </div>
      </section>

      <div role="status" aria-live="polite" class="fixed inset-x-0 bottom-4 z-20 mx-auto flex w-[min(40rem,calc(100%-2rem))] translate-y-[160%] flex-wrap items-center justify-between gap-3 rounded-2xl bg-tsp01-ink py-2 pl-5 pr-2 text-sm text-white shadow-[0_20px_50px_-12px_rgb(0_0_0/0.45)] transition duration-500 ease-[cubic-bezier(.2,.9,.3,1.15)] group-data-dirty/page:translate-y-0 group-data-saved/page:translate-y-0 motion-reduce:transition-none">
        <span class="flex items-center gap-2.5"><span class="size-2 rounded-full bg-amber-400 group-data-saved/page:bg-emerald-400"></span><span data-msg>You have unsaved changes</span></span>
        <span class="flex gap-1.5 group-data-saved/page:invisible"><button type="reset" class="min-h-11 rounded-xl px-4 font-semibold text-white/70 transition hover:text-white focus-visible:outline-2 focus-visible:outline-white">Discard</button><button type="submit" class="min-h-11 rounded-xl bg-white px-4 font-semibold text-tsp01-ink transition hover:bg-white/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Save changes</button></span>
      </div>
    </form>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp01-bg: #f6f6f9;
  --color-tsp01-bg: oklch(0.975 0.004 286);
  --color-tsp01-ink: #18181f;
  --color-tsp01-ink: oklch(0.205 0.012 286);
  --color-tsp01-mut: #63636f;
  --color-tsp01-mut: oklch(0.51 0.017 286);
  --color-tsp01-line: #e6e6ec;
  --color-tsp01-line: oklch(0.921 0.007 286);
  --color-tsp01-acc: #5b5bf0;
  --color-tsp01-acc: oklch(0.55 0.215 277);
  --color-tsp01-acc2: #b45cf2;
  --color-tsp01-acc2: oklch(0.64 0.21 307);
  --font-tsp01-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated before the browser build compiles. */

.tsp-01 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp01]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const form = root.querySelector('[data-form]');
  const msg = root.querySelector('[data-msg]');
  const links = [...root.querySelectorAll('[data-nav]')];
  const setActive = (id) => links.forEach((a) => a.setAttribute('aria-current', a.hash === '#' + id ? 'true' : 'false'));
  const io = new IntersectionObserver((entries) => entries.forEach((e) => e.isIntersecting && setActive(e.target.id)), { rootMargin: '-25% 0px -65% 0px' });
  root.querySelectorAll('[data-section]').forEach((s) => io.observe(s));
  links.forEach((a) => a.addEventListener('click', (ev) => {
    ev.preventDefault();
    const target = root.querySelector(a.hash);
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 24, behavior: reduce ? 'auto' : 'smooth' });
    setActive(target.id);
  }));
  const bio = form.elements.bio;
  const count = root.querySelector('[data-count]');
  const updateCount = () => { count.textContent = bio.value.length + ' / 160'; };
  bio.addEventListener('input', updateCount);
  updateCount();
  let timer;
  form.addEventListener('input', () => {
    delete root.dataset.saved;
    root.dataset.dirty = '';
    msg.textContent = 'You have unsaved changes';
  });
  form.addEventListener('reset', () => { setTimeout(updateCount); delete root.dataset.dirty; });
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    delete root.dataset.dirty;
    root.dataset.saved = '';
    msg.textContent = 'All changes saved';
    clearTimeout(timer);
    timer = setTimeout(() => { delete root.dataset.saved; }, 2200);
  });
})();
```

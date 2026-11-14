---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-registration-form-password-strength-meter/"
title: "Tailwind Registration Form with Password Strength Meter"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's sign-up screen, ported one-for-one to Tailwind v4: a frosted card on a slow-drifting aurora, a four-segment strength meter keyed to one…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Registration Form with Password Strength Meter
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-registration-form-password-strength-meter/

The CSS collection's sign-up screen, ported one-for-one to Tailwind v4: a frosted card on a slow-drifting aurora, a four-segment strength meter keyed to one data-score attribute, a requirements checklist whose ticks draw themselves in, an aria-pressed show/hide toggle, live confirm-password matching and a length-first scorer in line with NIST SP 800-63B.
## HTML
```html
<div class="tf-02 relative isolate block min-h-svh w-full overflow-hidden bg-tf02-bg pt-[72px] font-tf02-sans leading-[normal] text-tf02-ink antialiased motion-reduce:**:transition-none!">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="absolute inset-0 -z-10 opacity-75 blur-[70px] saturate-120 forced-colors:hidden" aria-hidden="true"><i class="absolute -top-[18vmax] -left-[10vmax] size-[46vmax] animate-tf02-drift rounded-full bg-tf02-accent motion-reduce:animate-none"></i><i class="absolute -right-[12vmax] -bottom-[22vmax] size-[46vmax] animate-tf02-drift rounded-full bg-tf02-accent-2 opacity-70 [animation-delay:-6s] motion-reduce:animate-none"></i><i class="absolute top-[30%] left-[55%] size-[26vmax] animate-tf02-drift rounded-full bg-[#d946ef] opacity-45 [animation-delay:-11s] motion-reduce:animate-none"></i></div>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,5vw,4rem)]">
    <div class="grid w-full max-w-[27rem] gap-[1.05rem] rounded-[1.75rem] border border-tf02-line bg-tf02-card p-[clamp(1.5rem,5vw,2.5rem)] shadow-[inset_0_1px_0_rgba(255,255,255,.08),0_40px_80px_-30px_rgba(0,0,0,.6)] backdrop-blur-[24px] backdrop-saturate-140" role="form" aria-labelledby="tf-02-title">
      <div class="flex items-center gap-[.55rem] font-semibold tracking-[-.01em]" aria-hidden="true"><span class="size-[1.6rem] rounded-[.5rem] bg-[conic-gradient(from_200deg,var(--color-tf02-accent),var(--color-tf02-accent-2),var(--color-tf02-accent))] shadow-[0_0_20px_color-mix(in_oklab,var(--color-tf02-accent)_60%,transparent)]"></span>Northwind</div>
      <h2 id="tf-02-title" class="mt-[.6rem] text-[clamp(1.6rem,4vw,1.9rem)] font-semibold tracking-[-.03em]">Create your account</h2>
      <p class="-mt-[.6rem] mb-[.2rem] text-[.95rem] text-tf02-muted">Free for 14 days. No card required.</p>
      <button class="flex min-h-12 cursor-pointer items-center justify-center gap-[.6rem] rounded-[.9rem] border border-tf02-line bg-tf02-field font-medium text-tf02-ink [transition:background_.2s,border-color_.2s] hover:border-[color-mix(in_oklab,var(--color-tf02-line),white_15%)] hover:bg-[color-mix(in_oklab,var(--color-tf02-field),white_6%)]" type="button">
        <svg viewBox="0 0 24 24" aria-hidden="true" class="size-5 fill-none stroke-current stroke-[1.6] [stroke-linecap:round]"><circle cx="8" cy="9" r="4"/><path d="M2 20c.7-3.3 3-5 6-5 1.4 0 2.7.4 3.7 1.1"/><circle cx="17.5" cy="13.5" r="2.5"/><path d="M17.5 16v5l1.5-1.2M17.5 19l1.5-1"/></svg>
        Sign up with a passkey
      </button>
      <div class="flex items-center gap-[.8rem] text-[.8rem] text-tf02-muted before:h-px before:flex-1 before:bg-tf02-line before:content-[''] after:h-px after:flex-1 after:bg-tf02-line after:content-['']"><span>or with email</span></div>
      <div class="group/f grid gap-[.45rem]">
        <label for="tf-02-name" class="text-[.85rem] font-medium">Full name</label>
        <input id="tf-02-name" type="text" autocomplete="name" required placeholder="Jordan Avery" class="min-h-12 w-full rounded-[.9rem] border border-tf02-line bg-tf02-field px-4 py-3 text-[1rem] text-tf02-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf02)] placeholder:text-tf02-muted/70 focus-visible:border-tf02-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf02-accent)_28%,transparent)] focus-visible:outline-none user-invalid:border-tf02-weak">
      </div>
      <div class="group/f grid gap-[.45rem]">
        <label for="tf-02-email" class="text-[.85rem] font-medium">Email</label>
        <input id="tf-02-email" type="email" autocomplete="email" required placeholder="[email protected]" aria-describedby="tf-02-email-err" class="min-h-12 w-full rounded-[.9rem] border border-tf02-line bg-tf02-field px-4 py-3 text-[1rem] text-tf02-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf02)] placeholder:text-tf02-muted/70 focus-visible:border-tf02-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf02-accent)_28%,transparent)] focus-visible:outline-none user-invalid:border-tf02-weak">
        <p class="hidden text-[.8rem] text-tf02-weak group-has-[input:user-invalid]/f:block" id="tf-02-email-err">Enter a valid email address.</p>
      </div>
      <div class="grid gap-[.45rem]">
        <label for="tf-02-pw" class="text-[.85rem] font-medium">Password</label>
        <div class="relative">
          <input id="tf-02-pw" type="password" autocomplete="new-password" required minlength="8" placeholder="At least 8 characters" aria-describedby="tf-02-strength tf-02-rules" class="min-h-12 w-full rounded-[.9rem] border border-tf02-line bg-tf02-field px-4 py-3 text-[1rem] text-tf02-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf02)] placeholder:text-tf02-muted/70 focus-visible:border-tf02-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf02-accent)_28%,transparent)] focus-visible:outline-none user-invalid:border-tf02-weak pr-[3.4rem]">
          <button class="tf-02__eye group/eye absolute top-1/2 right-[.3rem] grid size-[2.6rem] -translate-y-1/2 cursor-pointer place-items-center rounded-[.7rem] border-0 bg-transparent text-tf02-muted hover:bg-tf02-field hover:text-tf02-ink focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-tf02-accent" type="button" aria-pressed="false" aria-controls="tf-02-pw">
            <span class="tf-02__sr sr-only">Show password</span>
            <svg viewBox="0 0 24 24" aria-hidden="true" class="size-5 fill-none stroke-current stroke-[1.7] [stroke-linecap:round]"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/><path class="[stroke-dasharray:23] [stroke-dashoffset:0] [transition:stroke-dashoffset_.3s_var(--ease-tf02)] group-aria-pressed/eye:[stroke-dashoffset:23]" d="M4 4l16 16"/></svg>
          </button>
        </div>
        <div class="tf-02__meter group/m mt-1 grid grid-cols-4 gap-[.35rem] data-[score=1]:[--seg:var(--color-tf02-weak)] data-[score=2]:[--seg:var(--color-tf02-fair)] data-[score=3]:[--seg:var(--color-tf02-good)] data-[score=4]:[--seg:var(--color-tf02-great)]" data-score="0" aria-hidden="true"><i class="relative h-[.32rem] overflow-hidden rounded-full bg-tf02-line after:absolute after:inset-0 after:origin-left after:scale-x-0 after:rounded-[inherit] after:bg-[var(--seg,transparent)] after:[transition:scale_.45s_var(--ease-tf02),background_.3s] after:content-[''] group-data-[score=4]/m:after:shadow-[0_0_12px_var(--color-tf02-great)] motion-reduce:after:transition-none forced-colors:after:bg-[Highlight] group-data-[score=1]/m:after:scale-x-100 group-data-[score=2]/m:after:scale-x-100 group-data-[score=3]/m:after:scale-x-100 group-data-[score=4]/m:after:scale-x-100"></i><i class="relative h-[.32rem] overflow-hidden rounded-full bg-tf02-line after:absolute after:inset-0 after:origin-left after:scale-x-0 after:rounded-[inherit] after:bg-[var(--seg,transparent)] after:[transition:scale_.45s_var(--ease-tf02),background_.3s] after:content-[''] group-data-[score=4]/m:after:shadow-[0_0_12px_var(--color-tf02-great)] motion-reduce:after:transition-none forced-colors:after:bg-[Highlight] after:delay-50 group-data-[score=2]/m:after:scale-x-100 group-data-[score=3]/m:after:scale-x-100 group-data-[score=4]/m:after:scale-x-100"></i><i class="relative h-[.32rem] overflow-hidden rounded-full bg-tf02-line after:absolute after:inset-0 after:origin-left after:scale-x-0 after:rounded-[inherit] after:bg-[var(--seg,transparent)] after:[transition:scale_.45s_var(--ease-tf02),background_.3s] after:content-[''] group-data-[score=4]/m:after:shadow-[0_0_12px_var(--color-tf02-great)] motion-reduce:after:transition-none forced-colors:after:bg-[Highlight] after:delay-100 group-data-[score=3]/m:after:scale-x-100 group-data-[score=4]/m:after:scale-x-100"></i><i class="relative h-[.32rem] overflow-hidden rounded-full bg-tf02-line after:absolute after:inset-0 after:origin-left after:scale-x-0 after:rounded-[inherit] after:bg-[var(--seg,transparent)] after:[transition:scale_.45s_var(--ease-tf02),background_.3s] after:content-[''] group-data-[score=4]/m:after:shadow-[0_0_12px_var(--color-tf02-great)] motion-reduce:after:transition-none forced-colors:after:bg-[Highlight] after:delay-150 group-data-[score=4]/m:after:scale-x-100"></i></div>
        <p class="tf-02__strength text-[.8rem] text-tf02-muted" id="tf-02-strength"><span>Strength:</span> <b class="font-semibold text-tf02-ink">Too short</b></p>
        <p class="sr-only" aria-live="polite" id="tf-02-live"></p>
        <ul class="tf-02__rules mt-[.15rem] grid list-none grid-cols-[repeat(auto-fit,minmax(10.5rem,1fr))] gap-x-[.8rem] gap-y-[.4rem] text-[.8rem] text-tf02-muted" id="tf-02-rules" aria-label="Password requirements">
          <li data-rule="len" class="group/r flex items-center gap-[.45rem] transition-colors duration-250 data-[met=true]:text-tf02-ink"><svg viewBox="0 0 16 16" aria-hidden="true" class="size-4 flex-none fill-none stroke-current stroke-[1.5] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="8" cy="8" r="7" class="opacity-35 [transition:fill_.25s,opacity_.25s] group-data-[met=true]/r:fill-[color-mix(in_oklab,var(--color-tf02-great)_25%,transparent)] group-data-[met=true]/r:stroke-tf02-great group-data-[met=true]/r:opacity-100"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6" class="[stroke-dasharray:10] [stroke-dashoffset:10] [transition:stroke-dashoffset_.35s_var(--ease-tf02)] group-data-[met=true]/r:stroke-tf02-great group-data-[met=true]/r:[stroke-dashoffset:0]"/></svg>8+ characters <small class="text-[length:inherit] opacity-70">(12+ is better)</small></li>
          <li data-rule="case" class="group/r flex items-center gap-[.45rem] transition-colors duration-250 data-[met=true]:text-tf02-ink"><svg viewBox="0 0 16 16" aria-hidden="true" class="size-4 flex-none fill-none stroke-current stroke-[1.5] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="8" cy="8" r="7" class="opacity-35 [transition:fill_.25s,opacity_.25s] group-data-[met=true]/r:fill-[color-mix(in_oklab,var(--color-tf02-great)_25%,transparent)] group-data-[met=true]/r:stroke-tf02-great group-data-[met=true]/r:opacity-100"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6" class="[stroke-dasharray:10] [stroke-dashoffset:10] [transition:stroke-dashoffset_.35s_var(--ease-tf02)] group-data-[met=true]/r:stroke-tf02-great group-data-[met=true]/r:[stroke-dashoffset:0]"/></svg>Upper &amp; lowercase</li>
          <li data-rule="num" class="group/r flex items-center gap-[.45rem] transition-colors duration-250 data-[met=true]:text-tf02-ink"><svg viewBox="0 0 16 16" aria-hidden="true" class="size-4 flex-none fill-none stroke-current stroke-[1.5] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="8" cy="8" r="7" class="opacity-35 [transition:fill_.25s,opacity_.25s] group-data-[met=true]/r:fill-[color-mix(in_oklab,var(--color-tf02-great)_25%,transparent)] group-data-[met=true]/r:stroke-tf02-great group-data-[met=true]/r:opacity-100"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6" class="[stroke-dasharray:10] [stroke-dashoffset:10] [transition:stroke-dashoffset_.35s_var(--ease-tf02)] group-data-[met=true]/r:stroke-tf02-great group-data-[met=true]/r:[stroke-dashoffset:0]"/></svg>A number</li>
          <li data-rule="sym" class="group/r flex items-center gap-[.45rem] transition-colors duration-250 data-[met=true]:text-tf02-ink"><svg viewBox="0 0 16 16" aria-hidden="true" class="size-4 flex-none fill-none stroke-current stroke-[1.5] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="8" cy="8" r="7" class="opacity-35 [transition:fill_.25s,opacity_.25s] group-data-[met=true]/r:fill-[color-mix(in_oklab,var(--color-tf02-great)_25%,transparent)] group-data-[met=true]/r:stroke-tf02-great group-data-[met=true]/r:opacity-100"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6" class="[stroke-dasharray:10] [stroke-dashoffset:10] [transition:stroke-dashoffset_.35s_var(--ease-tf02)] group-data-[met=true]/r:stroke-tf02-great group-data-[met=true]/r:[stroke-dashoffset:0]"/></svg>A symbol</li>
        </ul>
      </div>
      <div class="tf-02__confirm group/cm grid gap-[.45rem]" data-match="empty">
        <label for="tf-02-pw2" class="text-[.85rem] font-medium">Confirm password</label>
        <input id="tf-02-pw2" type="password" autocomplete="new-password" required placeholder="Re-enter password" aria-describedby="tf-02-match" class="min-h-12 w-full rounded-[.9rem] border border-tf02-line bg-tf02-field px-4 py-3 text-[1rem] text-tf02-ink [transition:border-color_.2s,box-shadow_.25s_var(--ease-tf02)] placeholder:text-tf02-muted/70 focus-visible:border-tf02-accent focus-visible:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tf02-accent)_28%,transparent)] focus-visible:outline-none user-invalid:border-tf02-weak group-data-[match=no]/cm:border-tf02-weak group-data-[match=yes]/cm:border-tf02-great">
        <p class="min-h-[1.1em] text-[.8rem] group-data-[match=no]/cm:text-tf02-weak group-data-[match=yes]/cm:text-tf02-great" id="tf-02-match" aria-live="polite"></p>
      </div>
      <label class="flex cursor-pointer items-start gap-[.65rem] text-[.85rem] leading-[1.45] font-normal text-tf02-muted"><input type="checkbox" required id="tf-02-terms" class="mt-[.1rem] size-[1.15rem] flex-none accent-tf02-accent"><span>I agree to the <a href="#terms" class="text-tf02-ink underline decoration-tf02-accent/70 underline-offset-3 hover:text-tf02-accent-2">Terms</a> and <a href="#privacy" class="text-tf02-ink underline decoration-tf02-accent/70 underline-offset-3 hover:text-tf02-accent-2">Privacy Policy</a>.</span></label>
      <button class="tf-02__submit relative min-h-[3.2rem] cursor-pointer overflow-hidden rounded-[.9rem] border-0 bg-[linear-gradient(110deg,var(--color-tf02-accent),var(--color-tf02-accent-2))] font-semibold text-[#0b0b1a] shadow-[0_14px_30px_-12px_color-mix(in_oklab,var(--color-tf02-accent)_80%,transparent)] [transition:translate_.2s_var(--ease-tf02),filter_.2s,opacity_.2s] in-[:not(:has(#tf-02-terms:checked))]:opacity-55 hover:-translate-y-0.5 hover:brightness-108 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf02-ink forced-colors:border forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace] forced-colors:text-[ButtonText]" type="button">Create account</button>
      <p class="tf-02__status -mt-[.4rem] text-center text-[.85rem] text-tf02-great empty:hidden" role="status"></p>
      <p class="text-center text-[.85rem] text-tf02-muted">Already have an account? <a href="#login" class="text-tf02-ink underline decoration-tf02-accent/70 underline-offset-3 hover:text-tf02-accent-2">Sign in</a></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf02-bg: #070814;
  --color-tf02-card: rgba(18,20,40,0.62);
  --color-tf02-ink: #eef0ff;
  --color-tf02-muted: #9aa0c3;
  --color-tf02-line: rgba(255,255,255,0.12);
  --color-tf02-field: rgba(255,255,255,0.05);
  --color-tf02-accent: oklch(68% 0.19 285);
  --color-tf02-accent-2: oklch(80% 0.13 180);
  --color-tf02-weak: oklch(63% 0.22 25);
  --color-tf02-fair: oklch(77% 0.16 70);
  --color-tf02-good: oklch(78% 0.19 130);
  --color-tf02-great: oklch(72% 0.19 150);
  --font-tf02-sans: "Sora", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf02: cubic-bezier(0.16,1,0.3,1);
  --animate-tf02-drift: tf02-drift 18s ease-in-out infinite alternate;

  @keyframes tf02-drift {
    to {
      translate: 8vmax 6vmax;
      scale: 1.15;
    }
  }
}
/* Root rule: full-bleed contract. This demo is dark-first, like its CSS original:
   @theme holds the dark values, and data-theme="light" overrides them. */

.tf-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: dark;
}

.tf-02[data-theme="light"] {
  color-scheme: light;
  --color-tf02-bg: #eef0fb;
  --color-tf02-card: rgba(255,255,255,0.72);
  --color-tf02-ink: #14162b;
  --color-tf02-muted: #5b6080;
  --color-tf02-line: rgba(20,22,43,0.12);
  --color-tf02-field: rgba(255,255,255,0.7);
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-02').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : true);
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
  const root = document.querySelector('.tf-02');
  if (!root) return;
  const pw = root.querySelector('#tf-02-pw'), pw2 = root.querySelector('#tf-02-pw2');
  const meter = root.querySelector('.tf-02__meter'), label = root.querySelector('.tf-02__strength b');
  const live = root.querySelector('#tf-02-live'), confirm = root.querySelector('.tf-02__confirm');
  const matchMsg = root.querySelector('#tf-02-match'), eye = root.querySelector('.tf-02__eye');
  const rules = {
    len: (v) => v.length >= 8, case: (v) => /[a-z]/.test(v) && /[A-Z]/.test(v),
    num: (v) => /\d/.test(v), sym: (v) => /[^A-Za-z0-9]/.test(v)
  };
  const names = ['Too short', 'Weak', 'Fair', 'Good', 'Strong'];
  const score = (v) => {
    if (v.length < 8) return v.length ? 1 : 0;
    let s = (v.length >= 12) + (v.length >= 16);
    s += [rules.case(v), rules.num(v), rules.sym(v)].filter(Boolean).length * 0.75;
    if (/^(.)\1+$/.test(v) || /password|qwerty|12345/i.test(v)) s = 0;
    return Math.max(1, Math.min(4, Math.round(s) + 1));
  };
  let last = 0;
  const checkMatch = () => {
    if (!pw2.value) { confirm.dataset.match = 'empty'; matchMsg.textContent = ''; return; }
    const ok = pw2.value === pw.value;
    confirm.dataset.match = ok ? 'yes' : 'no';
    matchMsg.textContent = ok ? 'Passwords match.' : 'Passwords don\'t match yet.';
    pw2.setCustomValidity(ok ? '' : 'Mismatch');
  };
  pw.addEventListener('input', () => {
    const v = pw.value, s = score(v);
    meter.dataset.score = s;
    label.textContent = v.length && v.length < 8 ? 'Too short' : names[s];
    root.querySelectorAll('.tf-02__rules li').forEach((li) => { li.dataset.met = rules[li.dataset.rule](v); });
    if (s !== last) { live.textContent = 'Password strength: ' + label.textContent; last = s; }
    checkMatch();
  });
  pw2.addEventListener('input', checkMatch);
  eye.addEventListener('click', () => {
    const show = eye.getAttribute('aria-pressed') !== 'true';
    eye.setAttribute('aria-pressed', show);
    [pw, pw2].forEach((i) => { i.type = show ? 'text' : 'password'; });
    eye.querySelector('.tf-02__sr').textContent = show ? 'Hide password' : 'Show password';
  });
  root.querySelector('.tf-02__submit').addEventListener('click', () => {
    const status = root.querySelector('.tf-02__status');
    const bad = [...root.querySelectorAll('input[required]')].find((i) => !i.checkValidity());
    if (bad) { bad.focus(); bad.reportValidity(); return; }
    status.textContent = 'Account created — check your inbox to verify your email.';
  });
})();
```

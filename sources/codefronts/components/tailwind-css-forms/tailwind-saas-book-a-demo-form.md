---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-forms/tailwind-saas-book-a-demo-form/"
title: "Tailwind SaaS Book a Demo Form"
section: "components"
category: "tailwind-css-forms"
category_name: "Tailwind CSS Forms"
description: "The CSS collection's B2B ‘Book a demo’, ported one-for-one to Tailwind v4: a dark mesh-gradient stage with a faint grid, a pitch column with a gradient…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SaaS Book a Demo Form
Source: https://codefronts.com/components/tailwind-css-forms/tailwind-saas-book-a-demo-form/

The CSS collection's B2B ‘Book a demo’, ported one-for-one to Tailwind v4: a dark mesh-gradient stage with a faint grid, a pitch column with a gradient headline, value points, a customer quote and logo row, and a frosted form card — work-email validation that nudges Gmail/Outlook users and auto-fills the company, a team-size segmented control, interest chips, and a scheduler for the next five business days in the visitor's own time zone.
## HTML
```html
<div class="tf-18 relative isolate block min-h-svh w-full overflow-hidden bg-tf18-bg pt-[72px] font-tf18-sans leading-[normal] text-tf18-ink antialiased after:pointer-events-none after:absolute after:inset-0 after:-z-1 after:[background:linear-gradient(rgba(255,255,255,.035)_1px,transparent_1px)_0_0/48px_48px,linear-gradient(90deg,rgba(255,255,255,.035)_1px,transparent_1px)_0_0/48px_48px] after:[mask:radial-gradient(circle_at_50%_40%,#000,transparent_75%)] after:content-[''] motion-reduce:**:animate-none! motion-reduce:**:transition-none! forced-colors:after:hidden">
  <button type="button" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode" class="group/tt absolute top-4 right-4 z-20 grid size-11 cursor-pointer place-items-center rounded-full border border-current/22 bg-current/8 backdrop-blur-sm transition-[background-color,scale] duration-200 hover:bg-current/14 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-current active:scale-94 forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace]"><svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] [stroke-linejoin:round] group-aria-pressed/tt:hidden" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg viewBox="0 0 24 24" class="hidden size-5 fill-none stroke-current stroke-2 [stroke-linecap:round] group-aria-pressed/tt:block" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="absolute inset-0 -z-1 opacity-60 blur-[80px] forced-colors:hidden" aria-hidden="true"><i class="absolute -top-[20vmax] -left-[15vmax] size-[50vmax] animate-tf18-drift rounded-full bg-tf18-accent"></i><i class="absolute top-[10%] -right-[20vmax] size-[50vmax] animate-tf18-drift rounded-full bg-tf18-accent-2 opacity-55 [animation-delay:-8s]"></i><i class="absolute -bottom-[30vmax] left-1/4 size-[50vmax] animate-tf18-drift rounded-full bg-tf18-warm opacity-40 [animation-delay:-14s]"></i></div>
  <div class="grid min-h-svh place-items-center p-[clamp(1rem,4vw,3.5rem)]">
    <div class="@container w-full max-w-[70rem]">
      <div class="grid items-center gap-[clamp(1.5rem,5cqi,4rem)] @[56rem]:grid-cols-[minmax(0,1fr)_minmax(0,27rem)]">
        <section class="grid gap-6">
          <p class="inline-flex items-center gap-[.55rem] justify-self-start rounded-full border border-tf18-line bg-tf18-field py-[.4rem] pr-[.8rem] pl-[.45rem] text-[.85rem] font-semibold"><span class="size-[1.4rem] animate-tf18-spin rounded-full bg-[conic-gradient(from_90deg,var(--color-tf18-accent),var(--color-tf18-accent-2),var(--color-tf18-warm),var(--color-tf18-accent))]"></span>Orbit Analytics</p>
          <h2 class="text-[clamp(2.1rem,6cqi,3.9rem)] leading-none font-extrabold tracking-[-.045em] text-balance">See your whole funnel in <em class="bg-[linear-gradient(100deg,var(--color-tf18-accent-2),var(--color-tf18-accent)_50%,var(--color-tf18-warm))] bg-clip-text text-transparent not-italic">one live view.</em></h2>
          <ul class="grid list-none gap-[.7rem] text-tf18-muted">
            <li class="flex items-baseline gap-[.7rem] leading-[1.45] before:size-2 before:flex-none before:-translate-y-[.1rem] before:rounded-full before:bg-tf18-accent-2 before:shadow-[0_0_12px_var(--color-tf18-accent-2)] before:content-['']"><b class="font-semibold text-tf18-ink">30-minute walkthrough</b> tailored to your stack</li>
            <li class="flex items-baseline gap-[.7rem] leading-[1.45] before:size-2 before:flex-none before:-translate-y-[.1rem] before:rounded-full before:bg-tf18-accent-2 before:shadow-[0_0_12px_var(--color-tf18-accent-2)] before:content-['']"><b class="font-semibold text-tf18-ink">Live Q&amp;A</b> with a solutions engineer, not an SDR</li>
            <li class="flex items-baseline gap-[.7rem] leading-[1.45] before:size-2 before:flex-none before:-translate-y-[.1rem] before:rounded-full before:bg-tf18-accent-2 before:shadow-[0_0_12px_var(--color-tf18-accent-2)] before:content-['']"><b class="font-semibold text-tf18-ink">Free 14-day pilot</b> on your own data afterwards</li>
          </ul>
          <figure class="rounded-2xl border border-tf18-line bg-tf18-field px-5 py-[1.1rem]">
            <blockquote class="mb-[.9rem] text-[1.02rem] leading-[1.5]">“We replaced four dashboards and a weekly spreadsheet ritual in the first month.”</blockquote>
            <figcaption class="flex items-center gap-[.7rem] text-[.82rem] text-tf18-muted"><img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=120&h=120&fit=crop&crop=faces&auto=format&q=70" width="44" height="44" alt="" loading="lazy" decoding="async" class="size-11 rounded-full bg-[#333] object-cover"><span><b class="block font-semibold text-tf18-ink">Priya Raman</b>VP Growth, Larkspur</span></figcaption>
          </figure>
          <p class="flex flex-wrap items-center gap-6 font-extrabold tracking-[.04em] text-tf18-muted opacity-75" aria-label="Trusted by teams at Northwind, Halcyon, Fernway and Quanta"><span>NORTHWIND</span><span class="text-[1.15rem] font-medium tracking-normal italic">halcyon</span><span class="font-semibold tracking-[-.02em]">Fernway</span><span class="text-[.85rem] tracking-[.3em]">QUANTA</span></p>
        </section>
        <div class="grid gap-4 rounded-3xl border border-tf18-line bg-tf18-card p-[clamp(1.25rem,4cqi,2rem)] shadow-[inset_0_1px_0_rgba(255,255,255,.07),0_40px_80px_-30px_rgba(0,0,0,.6)] backdrop-blur-[24px] backdrop-saturate-130" role="form" aria-labelledby="tf-18-title">
          <h3 id="tf-18-title" class="mb-[.2rem] text-[1.35rem] font-bold tracking-[-.02em]">Book your demo</h3>
          <div class="tf-18__email group/em grid gap-[.4rem]" data-state="idle">
            <label for="tf-18-e" class="text-[.82rem] font-semibold">Work email</label>
            <input id="tf-18-e" type="email" autocomplete="email" required placeholder="[email protected]" aria-describedby="tf-18-e-msg" class="min-h-[2.9rem] w-full rounded-[.75rem] border border-tf18-line bg-tf18-field px-[.9rem] py-[.6rem] text-[.97rem] text-tf18-ink [transition:border-color_.2s,box-shadow_.2s] placeholder:text-tf18-muted/70 focus-visible:border-tf18-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf18-accent)_35%,transparent)] focus-visible:outline-none user-invalid:border-[#fb7185] group-data-[state=work]/em:border-tf18-ok/60">
            <p class="text-[.78rem] empty:hidden group-data-[state=free]/em:text-tf18-warn group-data-[state=work]/em:text-tf18-ok" id="tf-18-e-msg" aria-live="polite"></p>
          </div>
          <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,10rem),1fr))] gap-4">
            <div class="grid gap-[.4rem]"><label for="tf-18-n" class="text-[.82rem] font-semibold">Full name</label><input id="tf-18-n" autocomplete="name" required class="min-h-[2.9rem] w-full rounded-[.75rem] border border-tf18-line bg-tf18-field px-[.9rem] py-[.6rem] text-[.97rem] text-tf18-ink [transition:border-color_.2s,box-shadow_.2s] placeholder:text-tf18-muted/70 focus-visible:border-tf18-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf18-accent)_35%,transparent)] focus-visible:outline-none user-invalid:border-[#fb7185]"></div>
            <div class="grid gap-[.4rem]"><label for="tf-18-c" class="text-[.82rem] font-semibold">Company</label><input id="tf-18-c" autocomplete="organization" required class="min-h-[2.9rem] w-full rounded-[.75rem] border border-tf18-line bg-tf18-field px-[.9rem] py-[.6rem] text-[.97rem] text-tf18-ink [transition:border-color_.2s,box-shadow_.2s] placeholder:text-tf18-muted/70 focus-visible:border-tf18-accent focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tf18-accent)_35%,transparent)] focus-visible:outline-none user-invalid:border-[#fb7185]"></div>
          </div>
          <fieldset class="grid min-w-0 grid-cols-5 gap-[.2rem] rounded-[.8rem] border border-tf18-line bg-tf18-field p-[.2rem]"><legend class="col-span-full mb-2 flex items-baseline gap-2 p-0 text-[.82rem] font-semibold">Team size</legend>
            <label class="relative text-[.82rem] font-semibold"><input type="radio" name="tf-18-s" value="1-10" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-10 place-items-center rounded-[.6rem] text-[.8rem] font-semibold text-tf18-muted transition-all duration-200 peer-checked:bg-tf18-ink peer-checked:text-tf18-bg peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">1–10</span></label><label class="relative text-[.82rem] font-semibold"><input type="radio" name="tf-18-s" value="11-50" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-10 place-items-center rounded-[.6rem] text-[.8rem] font-semibold text-tf18-muted transition-all duration-200 peer-checked:bg-tf18-ink peer-checked:text-tf18-bg peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">11–50</span></label><label class="relative text-[.82rem] font-semibold"><input type="radio" name="tf-18-s" value="51-200" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-10 place-items-center rounded-[.6rem] text-[.8rem] font-semibold text-tf18-muted transition-all duration-200 peer-checked:bg-tf18-ink peer-checked:text-tf18-bg peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">51–200</span></label><label class="relative text-[.82rem] font-semibold"><input type="radio" name="tf-18-s" value="201-1k" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-10 place-items-center rounded-[.6rem] text-[.8rem] font-semibold text-tf18-muted transition-all duration-200 peer-checked:bg-tf18-ink peer-checked:text-tf18-bg peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">201–1k</span></label><label class="relative text-[.82rem] font-semibold"><input type="radio" name="tf-18-s" value="1k+" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="grid min-h-10 place-items-center rounded-[.6rem] text-[.8rem] font-semibold text-tf18-muted transition-all duration-200 peer-checked:bg-tf18-ink peer-checked:text-tf18-bg peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">1k+</span></label>
          </fieldset>
          <fieldset class="flex min-w-0 flex-wrap gap-[.4rem]"><legend class="mb-2 w-full flex items-baseline gap-2 p-0 text-[.82rem] font-semibold">What do you want to see?</legend>
            <label class="group/c relative text-[.82rem] font-semibold"><input type="checkbox" checked class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.3rem] items-center rounded-full border border-tf18-line px-[.85rem] text-[.8rem] font-medium text-tf18-muted transition-all duration-200 group-hover/c:border-tf18-ink/30 peer-checked:border-tf18-accent/70 peer-checked:bg-tf18-accent/22 peer-checked:text-tf18-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Attribution</span></label><label class="group/c relative text-[.82rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.3rem] items-center rounded-full border border-tf18-line px-[.85rem] text-[.8rem] font-medium text-tf18-muted transition-all duration-200 group-hover/c:border-tf18-ink/30 peer-checked:border-tf18-accent/70 peer-checked:bg-tf18-accent/22 peer-checked:text-tf18-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Cohorts</span></label><label class="group/c relative text-[.82rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.3rem] items-center rounded-full border border-tf18-line px-[.85rem] text-[.8rem] font-medium text-tf18-muted transition-all duration-200 group-hover/c:border-tf18-ink/30 peer-checked:border-tf18-accent/70 peer-checked:bg-tf18-accent/22 peer-checked:text-tf18-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Revenue forecasting</span></label><label class="group/c relative text-[.82rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.3rem] items-center rounded-full border border-tf18-line px-[.85rem] text-[.8rem] font-medium text-tf18-muted transition-all duration-200 group-hover/c:border-tf18-ink/30 peer-checked:border-tf18-accent/70 peer-checked:bg-tf18-accent/22 peer-checked:text-tf18-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">Warehouse sync</span></label><label class="group/c relative text-[.82rem] font-semibold"><input type="checkbox" class="peer absolute inset-0 m-0 cursor-pointer opacity-0"><span class="inline-flex min-h-[2.3rem] items-center rounded-full border border-tf18-line px-[.85rem] text-[.8rem] font-medium text-tf18-muted transition-all duration-200 group-hover/c:border-tf18-ink/30 peer-checked:border-tf18-accent/70 peer-checked:bg-tf18-accent/22 peer-checked:text-tf18-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tf18-accent-2 forced-colors:peer-checked:bg-[Highlight] forced-colors:peer-checked:text-[HighlightText]">SSO &amp; security</span></label>
          </fieldset>
          <fieldset class="min-w-0"><legend class="mb-2 flex items-baseline gap-2 p-0 text-[.82rem] font-semibold">Pick a time <span class="tf-18__tz text-[.75rem] font-normal text-tf18-muted"></span></legend>
            <div class="tf-18__days mb-2 grid grid-cols-5 gap-[.35rem] *:relative *:text-[.82rem] *:font-semibold [&_input]:absolute [&_input]:inset-0 [&_input]:m-0 [&_input]:cursor-pointer [&_input]:opacity-0 [&_input:focus-visible+span]:outline-2 [&_input:focus-visible+span]:outline-offset-2 [&_input:focus-visible+span]:outline-tf18-accent-2 [&_label:hover_span]:border-tf18-ink/30 forced-colors:[&_input:checked+span]:bg-[Highlight] forced-colors:[&_input:checked+span]:text-[HighlightText] [&_span]:grid [&_span]:justify-items-center [&_span]:rounded-[.7rem] [&_span]:border [&_span]:border-tf18-line [&_span]:bg-tf18-field [&_span]:py-2 [&_span]:transition-all [&_span]:duration-200 [&_small]:text-[.66rem] [&_small]:tracking-[.08em] [&_small]:text-tf18-muted [&_small]:uppercase [&_b]:text-[1.05rem] [&_b]:font-bold [&_input:checked+span]:border-tf18-accent [&_input:checked+span]:bg-tf18-accent/25"></div>
            <div class="tf-18__slots grid grid-cols-[repeat(auto-fill,minmax(5.25rem,1fr))] gap-[.35rem] *:relative *:text-[.82rem] *:font-semibold [&_input]:absolute [&_input]:inset-0 [&_input]:m-0 [&_input]:cursor-pointer [&_input]:opacity-0 [&_input:focus-visible+span]:outline-2 [&_input:focus-visible+span]:outline-offset-2 [&_input:focus-visible+span]:outline-tf18-accent-2 [&_label:hover_span]:border-tf18-ink/30 forced-colors:[&_input:checked+span]:bg-[Highlight] forced-colors:[&_input:checked+span]:text-[HighlightText] [&_span]:grid [&_span]:min-h-10 [&_span]:animate-tf18-in [&_span]:place-items-center [&_span]:rounded-[.6rem] [&_span]:border [&_span]:border-tf18-line [&_span]:text-[.82rem] [&_span]:tabular-nums [&_span]:transition-all [&_span]:duration-200 [&_span]:[animation-delay:calc(var(--k)*30ms)] [&_input:checked+span]:border-transparent [&_input:checked+span]:bg-[linear-gradient(110deg,var(--color-tf18-accent),var(--color-tf18-accent-2))] [&_input:checked+span]:font-bold [&_input:checked+span]:text-[#06061a]"></div>
          </fieldset>
          <button type="button" class="tf-18__book group/b relative flex min-h-[3.2rem] cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-[.9rem] border-0 bg-[linear-gradient(110deg,var(--color-tf18-accent),var(--color-tf18-accent-2))] text-[1rem] font-bold text-[#06061a] shadow-[0_14px_30px_-12px_color-mix(in_oklab,var(--color-tf18-accent)_80%,transparent)] [transition:translate_.2s_var(--ease-tf18),filter_.2s] after:absolute after:inset-0 after:-translate-x-full after:bg-[linear-gradient(100deg,transparent_30%,rgba(255,255,255,.45)_50%,transparent_70%)] after:[transition:translate_.8s_var(--ease-tf18)] after:content-[''] hover:-translate-y-0.5 hover:after:translate-x-full focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tf18-ink forced-colors:border forced-colors:border-[ButtonText] forced-colors:bg-[ButtonFace] forced-colors:text-[ButtonText]"><span>Book demo</span><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[1.1rem] fill-none stroke-current stroke-[2.3] [stroke-linecap:round] [stroke-linejoin:round] [transition:translate_.3s_var(--ease-tf18)] group-hover/b:translate-x-[3px]"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
          <p class="-mt-[.3rem] text-center text-[.74rem] text-tf18-muted">By booking you agree to our <a href="#privacy" class="text-tf18-ink underline underline-offset-3 hover:text-tf18-accent-2">Privacy Policy</a>. We'll never share your data.</p>
          <p class="tf-18__status text-center text-[.88rem] font-semibold empty:hidden data-[ok=false]:text-[#fb7185] data-[ok=true]:text-tf18-ok" role="status"></p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tf18-bg: #05060d;
  --color-tf18-card: rgba(14,16,30,0.72);
  --color-tf18-ink: #f1f2fb;
  --color-tf18-muted: #9ca0bd;
  --color-tf18-line: rgba(255,255,255,0.1);
  --color-tf18-field: rgba(255,255,255,0.05);
  --color-tf18-accent: #7c5cff;
  --color-tf18-accent-2: #22d3ee;
  --color-tf18-warm: #f472b6;
  --color-tf18-ok: #34d399;
  --color-tf18-warn: #fbbf24;
  --font-tf18-sans: "Onest", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tf18: cubic-bezier(0.16,1,0.3,1);
  --animate-tf18-drift: tf18-drift 22s ease-in-out infinite alternate;
  --animate-tf18-spin: tf18-spin 8s linear infinite;
  --animate-tf18-in: tf18-in 0.35s cubic-bezier(0.16,1,0.3,1) both;

  @keyframes tf18-drift {
    to {
      translate: 6vmax -5vmax;
      scale: 1.12;
    }
  }

  @keyframes tf18-spin {
    to {
      rotate: 1turn;
    }
  }

  @keyframes tf18-in {
    from {
      opacity: 0;
      scale: 0.94;
    }
  }
}
/* Root rule: full-bleed contract. Dark-first like its CSS original: @theme holds the dark values,
   data-theme="light" overrides them. */

.tf-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: dark;
}

.tf-18[data-theme="light"] {
  color-scheme: light;
  --color-tf18-bg: #f3f3fb;
  --color-tf18-card: rgba(255,255,255,0.78);
  --color-tf18-ink: #11122a;
  --color-tf18-muted: #585c7d;
  --color-tf18-line: rgba(17,18,42,0.1);
  --color-tf18-field: rgba(255,255,255,0.75);
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.tf-18').forEach((root) => {
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
  const root = document.querySelector('.tf-18');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const FREE = new Set(['gmail.com', 'googlemail.com', 'outlook.com', 'hotmail.com', 'live.com', 'yahoo.com', 'yahoo.co.uk', 'icloud.com', 'me.com', 'aol.com', 'proton.me', 'protonmail.com']);
  const email = $('#tf-18-e'), field = $('.tf-18__email'), msg = $('#tf-18-e-msg'), company = $('#tf-18-c');
  let autoCo = false;
  email.addEventListener('blur', () => {
    const domain = (email.value.split('@')[1] || '').toLowerCase();
    if (!email.checkValidity() || !domain) { field.dataset.state = 'idle'; msg.textContent = ''; return; }
    if (FREE.has(domain)) { field.dataset.state = 'free'; msg.textContent = 'Looks like a personal address — a work email helps us prepare a tailored demo.'; return; }
    field.dataset.state = 'work'; msg.textContent = '✓ Work email';
    if (!company.value || autoCo) { const n = domain.split('.')[0]; company.value = n.charAt(0).toUpperCase() + n.slice(1); autoCo = true; }
  });
  company.addEventListener('input', () => { autoCo = false; });
  const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC';
  const tzShort = new Intl.DateTimeFormat('en-US', { timeZoneName: 'short' }).formatToParts(new Date()).find((p) => p.type === 'timeZoneName');
  $('.tf-18__tz').textContent = '· ' + (tzShort ? tzShort.value : tz);
  const days = []; const d = new Date(); d.setHours(0, 0, 0, 0);
  while (days.length < 5) { d.setDate(d.getDate() + 1); if (d.getDay() % 6) days.push(new Date(d)); }
  const wd = new Intl.DateTimeFormat('en-US', { weekday: 'short' }), full = new Intl.DateTimeFormat('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
  const tf = new Intl.DateTimeFormat('en-US', { hour: 'numeric', minute: '2-digit' });
  $('.tf-18__days').innerHTML = days.map((x, i) => '<label><input type="radio" name="tf-18-d" value="' + i + '"' + (i ? '' : ' checked') + ' aria-label="' + full.format(x) + '"><span aria-hidden="true"><small>' + wd.format(x) + '</small><b>' + x.getDate() + '</b></span></label>').join('');
  const slotsFor = (i) => { const base = days[i], out = []; [9, 10, 11, 13, 14, 15, 16].forEach((h, k) => { if ((i + k) % 3 !== 1) { const t = new Date(base); t.setHours(h, k % 2 ? 30 : 0); out.push(t); } }); return out; };
  const renderSlots = () => {
    const i = Number(root.querySelector('[name="tf-18-d"]:checked').value);
    $('.tf-18__slots').innerHTML = slotsFor(i).map((t, k) => '<label><input type="radio" name="tf-18-t" value="' + t.toISOString() + '" aria-label="' + tf.format(t) + '"><span style="--k:' + k + '" aria-hidden="true">' + tf.format(t) + '</span></label>').join('');
  };
  $('.tf-18__days').addEventListener('change', renderSlots); renderSlots();
  $('.tf-18__book').addEventListener('click', () => {
    const status = $('.tf-18__status');
    const bad = [...root.querySelectorAll('input[required]')].find((f) => !f.checkValidity());
    if (bad) { bad.reportValidity(); return; }
    const t = root.querySelector('[name="tf-18-t"]:checked');
    if (!t) { status.dataset.ok = 'false'; status.textContent = 'Choose a time slot to continue.'; root.querySelector('[name="tf-18-t"]').focus(); return; }
    const when = new Date(t.value);
    status.dataset.ok = 'true';
    status.textContent = 'Booked for ' + full.format(when) + ' at ' + tf.format(when) + '. Calendar invite sent to ' + email.value + '.';
    $('.tf-18__book span').textContent = 'Demo booked';
  });
})();
```

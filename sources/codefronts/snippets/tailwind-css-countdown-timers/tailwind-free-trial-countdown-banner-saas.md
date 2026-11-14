---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-free-trial-countdown-banner-saas/"
title: "Tailwind Free Trial Countdown Banner for SaaS Apps"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "An in-app trial banner that escalates as the window closes: a calm violet state with seven days left, a magenta critical state inside the last two days, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Free Trial Countdown Banner for SaaS Apps
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-free-trial-countdown-banner-saas/

An in-app trial banner that escalates as the window closes: a calm violet state with seven days left, a magenta critical state inside the last two days, a depleting bar in both. Dismissal costs no script &mdash; a checkbox and has-checked: &mdash; and the port now collapses smoothly with a grid-rows-[1fr] &rarr; [0fr] transition and leaves a one-click Show again link behind.
## HTML
```html
<section class="tcd-13 w-full min-h-svh bg-tcd13-page font-tcd13-sans text-tcd13-ink antialiased" aria-labelledby="tcd-13-title">
  <div class="mx-auto grid min-h-svh max-w-[880px] content-center gap-5 px-[clamp(16px,4vw,48px)] py-14">
    <h2 id="tcd-13-title" class="text-[clamp(18px,3vw,24px)] font-semibold tracking-[-0.02em]">Trial banner · two escalation states</h2>

    <div class="rounded-2xl border border-tcd13-rule bg-tcd13-app p-3 shadow-tcd13-app">
      <div aria-hidden="true" class="flex flex-wrap items-center gap-x-3 gap-y-1 border-b border-tcd13-rule px-2 pt-1 pb-3.5">
        <span class="grid size-7 place-items-center rounded-lg bg-tcd13-ink text-xs font-bold text-white">Q</span>
        <span class="text-sm font-bold">Quill</span>
        <em class="text-xs not-italic text-tcd13-mut">Nova workspace · Alex Chen</em>
      </div>

      <div class="group/w mt-3 grid grid-rows-[1fr] transition-[grid-template-rows] duration-300 ease-out has-checked:grid-rows-[0fr] motion-reduce:transition-none">
        <div class="min-h-0 overflow-hidden">
          <input type="checkbox" id="tcd-13-d1" class="peer sr-only">
          <div role="timer" data-state="calm" style="--left: 58%" class="relative grid grid-cols-[auto_minmax(0,1fr)_auto] sm:grid-cols-[auto_minmax(0,1fr)_auto_auto] items-center gap-x-3.5 gap-y-3 overflow-hidden rounded-xl border border-tcd13-acc/25 bg-tcd13-acc/6 py-3.5 pr-2 pl-4 transition-opacity group-has-checked/w:opacity-0 data-[state=critical]:border-tcd13-crit/30 data-[state=critical]:bg-tcd13-crit/8">
            <span aria-hidden="true" class="grid size-9 place-items-center rounded-lg bg-tcd13-acc text-white"><svg viewBox="0 0 20 20" width="17" height="17"><circle cx="10" cy="10" r="7.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 6v4.3l2.8 1.7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
            <p class="min-w-0 text-[14px] leading-snug text-pretty"><strong class="font-semibold"><time datetime="P7D">7 days left</time> in your trial.</strong> <span class="text-tcd13-mut">Keep unlimited documents and version history by adding a plan.</span></p>
            <label for="tcd-13-d1" class="col-start-3 row-start-1 grid size-11 cursor-pointer place-items-center rounded-lg text-tcd13-mut transition hover:bg-tcd13-ink/5 hover:text-tcd13-ink peer-focus-visible:outline-2 peer-focus-visible:outline-tcd13-acc sm:col-start-4"><span class="sr-only">Dismiss trial banner for this session</span><svg viewBox="0 0 14 14" width="13" height="13" aria-hidden="true"><path d="M2.5 2.5l9 9M11.5 2.5l-9 9" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></label>
            <button type="button" class="col-span-3 row-start-2 min-h-11 cursor-pointer rounded-lg bg-tcd13-acc px-4 text-sm font-semibold whitespace-nowrap text-white transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd13-ink sm:col-span-1 sm:col-start-3 sm:row-start-1">Choose a plan</button>
            <div aria-hidden="true" class="absolute inset-x-0 bottom-0 h-[3px] bg-tcd13-acc/15"><i class="block h-full w-(--left) rounded-r-full bg-tcd13-acc"></i></div>
          </div>
        </div>
        <label for="tcd-13-d1" class="hidden min-h-11 cursor-pointer items-center gap-2 px-2 text-[13px] font-semibold text-tcd13-acc underline-offset-4 hover:underline group-has-checked/w:flex">↺ Show the 7-day trial banner again</label>
      </div>

      <div class="group/w mt-2.5 grid grid-rows-[1fr] transition-[grid-template-rows] duration-300 ease-out has-checked:grid-rows-[0fr] motion-reduce:transition-none">
        <div class="min-h-0 overflow-hidden">
          <input type="checkbox" id="tcd-13-d2" class="peer sr-only">
          <div role="timer" data-state="critical" style="--left: 9%" class="relative grid grid-cols-[auto_minmax(0,1fr)_auto] sm:grid-cols-[auto_minmax(0,1fr)_auto_auto] items-center gap-x-3.5 gap-y-3 overflow-hidden rounded-xl border border-tcd13-acc/25 bg-tcd13-acc/6 py-3.5 pr-2 pl-4 transition-opacity group-has-checked/w:opacity-0 data-[state=critical]:border-tcd13-crit/30 data-[state=critical]:bg-tcd13-crit/8">
            <span aria-hidden="true" class="grid size-9 place-items-center rounded-lg bg-tcd13-crit text-white"><svg viewBox="0 0 20 20" width="17" height="17"><path d="M10 2.4 1.6 16.6h16.8L10 2.4Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M10 7.4v4.1M10 13.4v1" stroke="currentColor" stroke-width="1.6"/></svg></span>
            <p class="min-w-0 text-[14px] leading-snug text-pretty"><strong class="font-semibold text-tcd13-crit-ink"><time datetime="PT41H">41 hours left</time> — then editing locks.</strong> <span class="text-tcd13-mut">Your documents stay safe and read-only. No card on file yet.</span></p>
            <label for="tcd-13-d2" class="col-start-3 row-start-1 grid size-11 cursor-pointer place-items-center rounded-lg text-tcd13-mut transition hover:bg-tcd13-ink/5 hover:text-tcd13-ink peer-focus-visible:outline-2 peer-focus-visible:outline-tcd13-crit sm:col-start-4"><span class="sr-only">Dismiss trial banner for this session</span><svg viewBox="0 0 14 14" width="13" height="13" aria-hidden="true"><path d="M2.5 2.5l9 9M11.5 2.5l-9 9" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></label>
            <button type="button" class="col-span-3 row-start-2 min-h-11 cursor-pointer rounded-lg bg-tcd13-crit px-4 text-sm font-semibold whitespace-nowrap text-white transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd13-ink sm:col-span-1 sm:col-start-3 sm:row-start-1">Add payment method</button>
            <div aria-hidden="true" class="absolute inset-x-0 bottom-0 h-[3px] bg-tcd13-crit/15"><i class="block h-full w-(--left) rounded-r-full bg-tcd13-crit animate-pulse motion-reduce:animate-none"></i></div>
          </div>
        </div>
        <label for="tcd-13-d2" class="hidden min-h-11 cursor-pointer items-center gap-2 px-2 text-[13px] font-semibold text-tcd13-crit-ink underline-offset-4 hover:underline group-has-checked/w:flex">↺ Show the 41-hour trial banner again</label>
      </div>

      <div aria-hidden="true" class="mt-4 grid gap-2.5 px-2 pt-2 pb-3"><span class="h-4 w-[42%] rounded-md bg-tcd13-rule"></span><span class="h-2.5 rounded-md bg-tcd13-rule/70"></span><span class="h-2.5 rounded-md bg-tcd13-rule/70"></span><span class="h-2.5 w-[63%] rounded-md bg-tcd13-rule/70"></span></div>
    </div>

    <p class="text-[12.5px] leading-relaxed text-tcd13-mut text-pretty">An authenticated in-app surface scoped to one workspace, not a site-wide promo bar. Dismissal is a checkbox plus <code class="rounded bg-tcd13-rule px-1 py-0.5 text-[11.5px] text-tcd13-ink">has-checked:</code>, so it lasts for the session, animates closed and costs no script.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd13-page: #f7f5fd;
  --color-tcd13-page: oklch(0.97 0.014 300);
  --color-tcd13-app: #ffffff;
  --color-tcd13-app: oklch(1 0 0);
  --color-tcd13-ink: #191430;
  --color-tcd13-ink: oklch(0.23 0.06 300);
  --color-tcd13-mut: #5c537f;
  --color-tcd13-mut: oklch(0.46 0.06 300);
  --color-tcd13-rule: #e6e1f5;
  --color-tcd13-rule: oklch(0.92 0.02 300);
  --color-tcd13-acc: #6d3ce0;
  --color-tcd13-acc: oklch(0.52 0.22 295);
  --color-tcd13-crit: #d61f7a;
  --color-tcd13-crit: oklch(0.56 0.24 350);
  --color-tcd13-crit-ink: #a3135b;
  --color-tcd13-crit-ink: oklch(0.46 0.2 350);
  --font-tcd13-sans: 'Space Grotesk', system-ui, sans-serif;
  --shadow-tcd13-app: 0 20px 46px -30px rgb(109 60 224 / 0.5);
}

.tcd-13 {
  width: 100%;
  min-height: 100svh;
}
```

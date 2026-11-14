---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-fixed-header-dashboard-independent-scroll-panels/"
title: "Tailwind CSS Fixed Header Dashboard with Independent Scroll Panels"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "The app-shell scroll model in utilities: the frame never moves, the page scrollbar is dead, and the activity feed and deploy table scroll on their own with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Fixed Header Dashboard with Independent Scroll Panels
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-fixed-header-dashboard-independent-scroll-panels/

The app-shell scroll model in utilities: the frame never moves, the page scrollbar is dead, and the activity feed and deploy table scroll on their own with sticky, blurred section headers. It is still three load-bearing ideas &mdash; grid-rows-[3.5rem_minmax(0,1fr)], min-h-0 down the chain, overflow-y-auto overscroll-contain on the scroller &mdash; now each a class you can point at.
## HTML
```html
<section class="tdl-05 w-full min-h-svh bg-tdl05-bg font-tdl05-sans text-tdl05-ink antialiased" aria-label="Independent scroll panels demo">
  <div class="@container/frame grid h-svh min-h-[30rem] grid-rows-[3.5rem_minmax(0,1fr)] overflow-hidden">
    <header class="flex min-w-0 items-center gap-5 border-b border-tdl05-edge bg-tdl05-panel px-4">
      <strong class="flex flex-none items-center gap-2.5 text-[15px] font-semibold"><span aria-hidden="true" class="size-5 rounded-md bg-[conic-gradient(from_210deg,var(--color-tdl05-acc),var(--color-tdl05-acc2),var(--color-tdl05-acc))]"></span>Opsdeck</strong>
      <nav aria-label="Primary" class="flex min-w-0 gap-1 overflow-x-auto [scrollbar-width:none] [&>a]:flex [&>a]:h-10 [&>a]:items-center [&>a]:rounded-lg [&>a]:px-3.25 [&>a]:text-[13px] [&>a]:font-semibold [&>a]:whitespace-nowrap [&>a]:text-tdl05-mut [&>a]:no-underline [&>a]:transition-colors [&>a:hover]:bg-tdl05-hover [&>a:hover]:text-tdl05-ink [&>a:focus-visible]:outline-2 [&>a:focus-visible]:-outline-offset-2 [&>a:focus-visible]:outline-tdl05-acc [&>a[aria-current=page]]:bg-tdl05-acc/10 [&>a[aria-current=page]]:text-tdl05-acc">
        <a href="#activity" aria-current="page">Activity</a><a href="#deploys">Deploys</a><a href="#alerts">Alerts</a>
      </nav>
      <label class="ml-auto flex flex-none items-center gap-2 text-xs font-semibold text-tdl05-mut"><span class="@max-[30rem]/frame:sr-only">Env</span>
        <select class="h-9 cursor-pointer rounded-full border border-tdl05-edge bg-tdl05-bg pr-3 pl-3 text-xs font-semibold text-tdl05-ink outline-none focus-visible:border-tdl05-acc focus-visible:ring-3 focus-visible:ring-tdl05-acc/20"><option>production</option><option>staging</option><option>preview</option></select>
      </label>
    </header>
    <div class="grid min-h-0 grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)] gap-3.5 p-3.5 @max-[42rem]/frame:grid-cols-1 @max-[42rem]/frame:grid-rows-2">
      <section class="flex min-h-0 flex-col overflow-hidden rounded-2xl border border-tdl05-edge bg-tdl05-panel" aria-labelledby="tdl05-h1">
        <h2 id="tdl05-h1" class="flex items-center justify-between border-b border-tdl05-edge px-4 py-3.25 text-[13.5px] font-semibold">Activity<span class="rounded-full bg-tdl05-acc/9 px-2.25 py-0.75 text-[10.5px] font-bold tracking-[0.06em] text-tdl05-acc uppercase">12 events</span></h2>
        <div role="region" aria-label="Activity feed, scrollable" tabindex="0" class="min-h-0 flex-1 overflow-y-auto overscroll-contain [scrollbar-color:var(--color-tdl05-edge)_transparent] [scrollbar-gutter:stable] [scrollbar-width:thin] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdl05-acc [&>h3]:sticky [&>h3]:top-0 [&>h3]:z-10 [&>h3]:border-b [&>h3]:border-tdl05-edge/60 [&>h3]:bg-tdl05-panel/85 [&>h3]:px-4 [&>h3]:pt-2.5 [&>h3]:pb-2 [&>h3]:text-[10.5px] [&>h3]:font-bold [&>h3]:tracking-[0.12em] [&>h3]:text-tdl05-mut [&>h3]:uppercase [&>h3]:backdrop-blur-md [&>p]:flex [&>p]:items-center [&>p]:gap-2.5 [&>p]:border-b [&>p]:border-tdl05-edge/45 [&>p]:px-4 [&>p]:py-2.75 [&>p]:text-[13px] [&>p]:transition-colors [&>p:hover]:bg-tdl05-bg [&_time]:ml-auto [&_time]:font-tdl05-mono [&_time]:text-[11px] [&_time]:text-tdl05-mut [&_em]:rounded-md [&_em]:border [&_em]:border-tdl05-edge [&_em]:bg-tdl05-bg [&_em]:px-1.5 [&_em]:font-tdl05-mono [&_em]:text-xs [&_em]:not-italic">
          <h3>Today</h3>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-ok"></i><b>api-eu</b> autoscaled to 12 pods <time>09:41</time></p>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-ok"></i><b>maya</b> merged <em>fix/checkout-402</em> <time>09:20</time></p>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-warn"></i><b>queue-workers</b> latency above 400ms <time>08:57</time></p>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-ok"></i><b>cron</b> nightly backup verified <time>06:00</time></p>
          <h3>Yesterday</h3>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-bad"></i><b>payments</b> incident #221 opened <time>18:12</time></p>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-ok"></i><b>payments</b> incident #221 resolved <time>18:44</time></p>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-ok"></i><b>tom</b> rotated API keys <time>16:03</time></p>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-ok"></i><b>web</b> cache hit rate 97.2% <time>12:30</time></p>
          <h3>Mon, Sep 28</h3>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-warn"></i><b>db-01</b> slow query flagged <time>15:22</time></p>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-ok"></i><b>lena</b> invited 2 teammates <time>11:08</time></p>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-ok"></i><b>api-us</b> deployed <em>v2.41.0</em> <time>09:00</time></p>
          <p><i aria-hidden="true" class="size-2 flex-none rounded-full bg-tdl05-ok"></i><b>web</b> Lighthouse score 98 <time>08:14</time></p>
        </div>
      </section>
      <section class="flex min-h-0 flex-col overflow-hidden rounded-2xl border border-tdl05-edge bg-tdl05-panel" aria-labelledby="tdl05-h2">
        <h2 id="tdl05-h2" class="flex items-center justify-between border-b border-tdl05-edge px-4 py-3.25 text-[13.5px] font-semibold">Deploys<span class="rounded-full bg-tdl05-acc/9 px-2.25 py-0.75 text-[10.5px] font-bold tracking-[0.06em] text-tdl05-acc uppercase">9 this week</span></h2>
        <div role="region" aria-label="Recent deploys, scrollable" tabindex="0" class="min-h-0 flex-1 overflow-auto overscroll-contain [scrollbar-color:var(--color-tdl05-edge)_transparent] [scrollbar-gutter:stable] [scrollbar-width:thin] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdl05-acc">
          <table class="w-full border-collapse text-[13px] tabular-nums [&_td]:border-b [&_td]:border-tdl05-edge/45 [&_td]:px-4 [&_td]:py-2.75 [&_td]:whitespace-nowrap [&_th]:sticky [&_th]:top-0 [&_th]:z-10 [&_th]:border-b [&_th]:border-tdl05-edge [&_th]:bg-tdl05-panel/88 [&_th]:px-4 [&_th]:pt-2.75 [&_th]:pb-2.25 [&_th]:text-left [&_th]:text-[10.5px] [&_th]:font-bold [&_th]:tracking-[0.1em] [&_th]:text-tdl05-mut [&_th]:uppercase [&_th]:backdrop-blur-md [&_tbody_tr:hover]:bg-tdl05-bg [&_td:first-child]:font-tdl05-mono [&_td:first-child]:text-xs">
            <caption class="sr-only">Recent deploys with status and duration</caption>
            <thead><tr><th scope="col">Ref</th><th scope="col">Service</th><th scope="col">Status</th><th scope="col">Time</th></tr></thead>
            <tbody>
              <tr><td>v2.41.2</td><td>api-eu</td><td><span class="rounded-full bg-tdl05-ok/13 px-2.5 py-0.75 text-[11px] font-bold text-tdl05-okink">Live</span></td><td>2m 04s</td></tr>
              <tr><td>v2.41.1</td><td>web</td><td><span class="rounded-full bg-tdl05-ok/13 px-2.5 py-0.75 text-[11px] font-bold text-tdl05-okink">Live</span></td><td>1m 41s</td></tr>
              <tr><td>v2.41.0</td><td>api-us</td><td><span class="rounded-full bg-tdl05-ok/13 px-2.5 py-0.75 text-[11px] font-bold text-tdl05-okink">Live</span></td><td>2m 12s</td></tr>
              <tr><td>v2.40.9</td><td>workers</td><td><span class="rounded-full bg-tdl05-bad/11 px-2.5 py-0.75 text-[11px] font-bold text-tdl05-bad">Rolled back</span></td><td>0m 58s</td></tr>
              <tr><td>v2.40.8</td><td>web</td><td><span class="rounded-full bg-tdl05-ok/13 px-2.5 py-0.75 text-[11px] font-bold text-tdl05-okink">Live</span></td><td>1m 39s</td></tr>
              <tr><td>v2.40.7</td><td>api-eu</td><td><span class="rounded-full bg-tdl05-warn/20 px-2.5 py-0.75 text-[11px] font-bold text-tdl05-warnink">Canary</span></td><td>3m 20s</td></tr>
              <tr><td>v2.40.6</td><td>db-migrator</td><td><span class="rounded-full bg-tdl05-ok/13 px-2.5 py-0.75 text-[11px] font-bold text-tdl05-okink">Live</span></td><td>4m 02s</td></tr>
              <tr><td>v2.40.5</td><td>web</td><td><span class="rounded-full bg-tdl05-ok/13 px-2.5 py-0.75 text-[11px] font-bold text-tdl05-okink">Live</span></td><td>1m 47s</td></tr>
              <tr><td>v2.40.4</td><td>api-us</td><td><span class="rounded-full bg-tdl05-ok/13 px-2.5 py-0.75 text-[11px] font-bold text-tdl05-okink">Live</span></td><td>2m 30s</td></tr>
            </tbody>
          </table>
        </div>
      </section>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl05-bg: #f6f7fa;
  --color-tdl05-bg: oklch(0.975 0.005 255);
  --color-tdl05-hover: #eef0f5;
  --color-tdl05-hover: oklch(0.955 0.008 255);
  --color-tdl05-panel: #ffffff;
  --color-tdl05-panel: oklch(1 0 0);
  --color-tdl05-edge: #dfe2e9;
  --color-tdl05-edge: oklch(0.905 0.01 255);
  --color-tdl05-ink: #242a37;
  --color-tdl05-ink: oklch(0.27 0.02 255);
  --color-tdl05-mut: #5a6273;
  --color-tdl05-mut: oklch(0.49 0.02 255);
  --color-tdl05-acc: #2f5fd0;
  --color-tdl05-acc: oklch(0.52 0.17 260);
  --color-tdl05-acc2: #38a9c4;
  --color-tdl05-acc2: oklch(0.69 0.11 210);
  --color-tdl05-ok: #2aa766;
  --color-tdl05-ok: oklch(0.65 0.15 155);
  --color-tdl05-okink: #157a45;
  --color-tdl05-okink: oklch(0.5 0.12 155);
  --color-tdl05-warn: #e3a72c;
  --color-tdl05-warn: oklch(0.77 0.15 80);
  --color-tdl05-warnink: #8a5d00;
  --color-tdl05-warnink: oklch(0.48 0.1 75);
  --color-tdl05-bad: #c9372c;
  --color-tdl05-bad: oklch(0.56 0.19 27);
  --font-tdl05-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-tdl05-mono: 'IBM Plex Mono', ui-monospace, monospace;
}

.tdl-05 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-05 * {
    transition: none !important;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-exclusive-accordion-with-details-name-attribute/"
title: "Tailwind Exclusive Accordion with details name Attribute"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A five-lesson course module that is an exclusive accordion with zero JavaScript: every <details> shares name=\"tvt-15-lessons\", so the browser closes the open…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Exclusive Accordion with details name Attribute
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-exclusive-accordion-with-details-name-attribute/

A five-lesson course module that is an exclusive accordion with zero JavaScript: every <details> shares name="tvt-15-lessons", so the browser closes the open lesson when you open another. Tailwind v4's details-content: and open: variants plus one [interpolate-size:allow-keywords] on the root animate the panel from h-0 to h-auto, and the number badge, chevron and card all react through group-open/d:.
## HTML
```html
<section class="tvt-15 w-full min-h-svh grid place-items-center bg-tvt15-bg bg-[radial-gradient(65%_50%_at_50%_0%,var(--color-tvt15-glow),transparent_72%)] px-4 py-14 font-tvt15-sans text-tvt15-ink antialiased [interpolate-size:allow-keywords] sm:px-6" aria-label="Tailwind exclusive accordion with details name attribute demo">
  <div class="grid w-full max-w-[60rem] justify-items-center gap-8">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="inline-flex items-center gap-2 rounded-full bg-tvt15-card px-3 py-1.5 font-tvt15-mono text-[11.5px] text-tvt15-acc-ink ring-1 ring-tvt15-line"><span aria-hidden="true" class="size-1.5 rounded-full bg-tvt15-acc shadow-[0_0_0_3px] shadow-tvt15-acc/25"></span>&lt;details name&gt; · 0 KB JavaScript</p>
      <h2 class="font-tvt15-serif text-[clamp(32px,5vw,50px)] leading-[1.02] tracking-[-0.01em] text-balance">One open at a time, <span class="bg-linear-to-r from-tvt15-hl to-tvt15-hl2 bg-clip-text pe-1 text-transparent italic">natively</span></h2>
      <p class="max-w-[50ch] text-[15px] leading-relaxed text-tvt15-mut text-pretty">Five <code class="font-tvt15-mono text-[13px] text-tvt15-ink">&lt;details&gt;</code> share one <code class="font-tvt15-mono text-[13px] text-tvt15-ink">name</code>. Open a lesson and the browser closes the last one &mdash; and the height animates to <code class="font-tvt15-mono text-[13px] text-tvt15-ink">auto</code>.</p>
    </header>

    <div class="@container w-full">
    <div class="grid w-full grid-cols-[17rem_minmax(0,1fr)] items-start gap-5 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none @max-[46rem]:grid-cols-1">
      <aside class="overflow-hidden rounded-3xl bg-tvt15-card shadow-tvt15-card ring-1 ring-tvt15-line" aria-label="Course summary">
        <div class="relative h-32 overflow-hidden bg-linear-to-br from-tvt15-acc to-tvt15-acc2 @max-[46rem]:h-24">
          <svg aria-hidden="true" viewBox="0 0 280 130" preserveAspectRatio="xMidYMid slice" class="absolute inset-0 size-full" focusable="false"><g fill="none" stroke="#fff" stroke-opacity=".22" stroke-width="1.5"><circle cx="240" cy="20" r="30"/><circle cx="240" cy="20" r="58"/><circle cx="240" cy="20" r="86"/><circle cx="240" cy="20" r="114"/><circle cx="240" cy="20" r="142"/></g><circle cx="240" cy="20" r="12" fill="#fff" fill-opacity=".85"/><path d="M0 110 Q70 80 140 104 T280 96 V130 H0Z" fill="#fff" fill-opacity=".12"/></svg>
          <p class="absolute start-4 bottom-3 rounded-full bg-white/18 px-2.5 py-1 font-tvt15-mono text-[11px] font-medium text-white backdrop-blur-sm">Module 3 · Disclosure</p>
        </div>
        <div class="grid gap-4 p-5">
          <div>
            <h3 class="font-tvt15-serif text-[24px] leading-tight">Native HTML, no framework</h3>
            <p class="mt-1 text-[13.5px] text-tvt15-mut">Exclusive accordions with four attributes.</p>
          </div>
          <div class="flex items-center gap-4 rounded-2xl bg-tvt15-open p-3.5 ring-1 ring-tvt15-line">
            <svg viewBox="0 0 44 44" width="52" height="52" class="shrink-0 -rotate-90" role="img" aria-label="40 percent complete" focusable="false"><circle cx="22" cy="22" r="18" fill="none" stroke="currentColor" stroke-width="5" class="text-tvt15-line"/><circle cx="22" cy="22" r="18" fill="none" stroke="url(#tvt-15-ring)" stroke-width="5" stroke-linecap="round" pathLength="100" stroke-dasharray="40 100"/><defs><linearGradient id="tvt-15-ring"><stop offset="0" stop-color="var(--color-tvt15-acc)"/><stop offset="1" stop-color="var(--color-tvt15-acc2)"/></linearGradient></defs></svg>
            <div class="leading-tight"><p class="text-[22px] font-bold tracking-[-0.02em] tabular-nums">2<span class="text-[14px] font-semibold text-tvt15-mut"> / 5</span></p><p class="mt-0.5 text-[12.5px] text-tvt15-mut">lessons complete</p></div>
          </div>
          <dl class="grid grid-cols-3 gap-2 text-center">
            <div class="rounded-xl p-2 ring-1 ring-tvt15-line"><dt class="text-[11px] text-tvt15-mut">Length</dt><dd class="text-[14px] font-semibold tabular-nums">34m</dd></div>
            <div class="rounded-xl p-2 ring-1 ring-tvt15-line"><dt class="text-[11px] text-tvt15-mut">Level</dt><dd class="text-[14px] font-semibold">Mid</dd></div>
            <div class="rounded-xl p-2 ring-1 ring-tvt15-line"><dt class="text-[11px] text-tvt15-mut">Lessons</dt><dd class="text-[14px] font-semibold tabular-nums">5</dd></div>
          </dl>
          <p class="flex items-center gap-2.5 border-t border-tvt15-line pt-4 text-[13px]"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-linear-to-br from-[oklch(0.72_0.14_40)] to-[oklch(0.58_0.2_10)] text-[11px] font-bold text-white">EM</span><span class="leading-tight"><b class="block font-semibold">Elena Marsh</b><span class="text-[12px] text-tvt15-mut">Web platform educator</span></span></p>
        </div>
      </aside>

      <div class="grid gap-3">

        <details name="tvt-15-lessons" class="group/d rounded-2xl bg-tvt15-card ring-1 ring-tvt15-line transition-[box-shadow,background-color] duration-300 open:bg-tvt15-open open:shadow-tvt15-open open:ring-tvt15-acc/30 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:duration-[380ms] details-content:ease-[cubic-bezier(.32,.72,.3,1)] details-content:transition-discrete open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 select-none transition-colors duration-200 hover:bg-tvt15-acc/[0.05] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt15-ring sm:gap-4 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-full bg-tvt15-acc/10 font-tvt15-mono text-[12.5px] font-semibold text-tvt15-acc-ink ring-1 ring-tvt15-acc/20 transition-[background-color,color,box-shadow,scale] duration-300 group-open/d:scale-105 group-open/d:bg-linear-to-br group-open/d:from-tvt15-acc group-open/d:to-tvt15-acc2 group-open/d:text-white group-open/d:shadow-tvt15-badge group-open/d:ring-0 motion-reduce:transition-none">01</span>
            <span class="grid min-w-0 flex-1 leading-tight">
              <span class="text-[15.5px] font-semibold tracking-[-0.01em] text-pretty transition-colors group-open/d:text-tvt15-ink">The name attribute</span>
              <span class="mt-1 flex items-center gap-2 text-[12.5px] text-tvt15-mut tabular-nums">6 min<span class="inline-flex items-center gap-1 rounded-full bg-tvt15-ok/12 px-2 py-0.5 text-[11.5px] font-semibold text-tvt15-ok"><svg viewBox="0 0 20 20" width="12" height="12" aria-hidden="true" focusable="false"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>Done</span></span>
            </span>
            <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full text-tvt15-mut ring-1 ring-tvt15-line transition-[rotate,background-color,color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] group-open/d:rotate-180 group-open/d:bg-tvt15-acc/10 group-open/d:text-tvt15-acc-ink motion-reduce:transition-none"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="grid gap-3.5 px-4 pb-5 sm:ps-[4.75rem] sm:pe-6">
            <p class="max-w-[60ch] text-[14.5px] leading-[1.7] text-tvt15-mut text-pretty">Matching <code class="rounded-md bg-tvt15-acc/10 px-1.5 py-0.5 font-tvt15-mono text-[12.5px] text-tvt15-acc-ink">name</code> values make the group exclusive &mdash; opening one closes the rest. Unlike radios, clicking the open item closes it, so &ldquo;none open&rdquo; is a valid state. The members don't even need to be siblings.</p>
            <pre class="overflow-x-auto rounded-xl bg-tvt15-code px-4 py-3.5 font-tvt15-mono text-[12.5px] leading-[1.7] text-tvt15-c-ink shadow-inner ring-1 ring-black/10"><code><span class="text-tvt15-c-tag">&lt;details</span> <span class="text-tvt15-c-attr">name</span>=<span class="text-tvt15-c-str">"faq"</span> <span class="text-tvt15-c-attr">open</span><span class="text-tvt15-c-tag">&gt;</span>…<span class="text-tvt15-c-tag">&lt;/details&gt;</span>
<span class="text-tvt15-c-tag">&lt;details</span> <span class="text-tvt15-c-attr">name</span>=<span class="text-tvt15-c-str">"faq"</span><span class="text-tvt15-c-tag">&gt;</span>…<span class="text-tvt15-c-tag">&lt;/details&gt;</span>  <span class="text-tvt15-c-cm italic">&lt;!-- closes the first --&gt;</span></code></pre>
            <p class="flex items-center justify-between gap-3 text-[12.5px] text-tvt15-mut"><span>Lesson 1 of 5</span><span class="font-tvt15-mono text-[11.5px]">name=""</span></p>
          </div>
        </details>

        <details name="tvt-15-lessons" class="group/d rounded-2xl bg-tvt15-card ring-1 ring-tvt15-line transition-[box-shadow,background-color] duration-300 open:bg-tvt15-open open:shadow-tvt15-open open:ring-tvt15-acc/30 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:duration-[380ms] details-content:ease-[cubic-bezier(.32,.72,.3,1)] details-content:transition-discrete open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 select-none transition-colors duration-200 hover:bg-tvt15-acc/[0.05] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt15-ring sm:gap-4 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-full bg-tvt15-acc/10 font-tvt15-mono text-[12.5px] font-semibold text-tvt15-acc-ink ring-1 ring-tvt15-acc/20 transition-[background-color,color,box-shadow,scale] duration-300 group-open/d:scale-105 group-open/d:bg-linear-to-br group-open/d:from-tvt15-acc group-open/d:to-tvt15-acc2 group-open/d:text-white group-open/d:shadow-tvt15-badge group-open/d:ring-0 motion-reduce:transition-none">02</span>
            <span class="grid min-w-0 flex-1 leading-tight">
              <span class="text-[15.5px] font-semibold tracking-[-0.01em] text-pretty transition-colors group-open/d:text-tvt15-ink">Animating the impossible</span>
              <span class="mt-1 flex items-center gap-2 text-[12.5px] text-tvt15-mut tabular-nums">7 min<span class="inline-flex items-center gap-1 rounded-full bg-tvt15-ok/12 px-2 py-0.5 text-[11.5px] font-semibold text-tvt15-ok"><svg viewBox="0 0 20 20" width="12" height="12" aria-hidden="true" focusable="false"><path d="m5 10.5 3.2 3L15 6.5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>Done</span></span>
            </span>
            <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full text-tvt15-mut ring-1 ring-tvt15-line transition-[rotate,background-color,color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] group-open/d:rotate-180 group-open/d:bg-tvt15-acc/10 group-open/d:text-tvt15-acc-ink motion-reduce:transition-none"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="grid gap-3.5 px-4 pb-5 sm:ps-[4.75rem] sm:pe-6">
            <p class="max-w-[60ch] text-[14.5px] leading-[1.7] text-tvt15-mut text-pretty"><code class="rounded-md bg-tvt15-acc/10 px-1.5 py-0.5 font-tvt15-mono text-[12.5px] text-tvt15-acc-ink">::details-content</code> targets the wrapper the browser generates around everything after the summary &mdash; the box that never existed for CSS before. In Tailwind v4 it is a variant: <code class="rounded-md bg-tvt15-acc/10 px-1.5 py-0.5 font-tvt15-mono text-[12.5px] text-tvt15-acc-ink">details-content:h-0</code>.</p>
            <pre class="overflow-x-auto rounded-xl bg-tvt15-code px-4 py-3.5 font-tvt15-mono text-[12.5px] leading-[1.7] text-tvt15-c-ink shadow-inner ring-1 ring-black/10"><code><span class="text-tvt15-c-prop">details-content</span>:h-0 <span class="text-tvt15-c-prop">details-content</span>:opacity-0
<span class="text-tvt15-c-prop">open</span>:<span class="text-tvt15-c-prop">details-content</span>:h-auto <span class="text-tvt15-c-prop">open</span>:<span class="text-tvt15-c-prop">details-content</span>:opacity-100</code></pre>
            <p class="flex items-center justify-between gap-3 text-[12.5px] text-tvt15-mut"><span>Lesson 2 of 5</span><span class="font-tvt15-mono text-[11.5px]">::details-content</span></p>
          </div>
        </details>

        <details name="tvt-15-lessons" class="group/d rounded-2xl bg-tvt15-card ring-1 ring-tvt15-line transition-[box-shadow,background-color] duration-300 open:bg-tvt15-open open:shadow-tvt15-open open:ring-tvt15-acc/30 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:duration-[380ms] details-content:ease-[cubic-bezier(.32,.72,.3,1)] details-content:transition-discrete open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 select-none transition-colors duration-200 hover:bg-tvt15-acc/[0.05] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt15-ring sm:gap-4 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-full bg-tvt15-acc/10 font-tvt15-mono text-[12.5px] font-semibold text-tvt15-acc-ink ring-1 ring-tvt15-acc/20 transition-[background-color,color,box-shadow,scale] duration-300 group-open/d:scale-105 group-open/d:bg-linear-to-br group-open/d:from-tvt15-acc group-open/d:to-tvt15-acc2 group-open/d:text-white group-open/d:shadow-tvt15-badge group-open/d:ring-0 motion-reduce:transition-none">03</span>
            <span class="grid min-w-0 flex-1 leading-tight">
              <span class="text-[15.5px] font-semibold tracking-[-0.01em] text-pretty transition-colors group-open/d:text-tvt15-ink">height: auto, transitioned</span>
              <span class="mt-1 flex items-center gap-2 text-[12.5px] text-tvt15-mut tabular-nums">8 min</span>
            </span>
            <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full text-tvt15-mut ring-1 ring-tvt15-line transition-[rotate,background-color,color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] group-open/d:rotate-180 group-open/d:bg-tvt15-acc/10 group-open/d:text-tvt15-acc-ink motion-reduce:transition-none"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="grid gap-3.5 px-4 pb-5 sm:ps-[4.75rem] sm:pe-6">
            <p class="max-w-[60ch] text-[14.5px] leading-[1.7] text-tvt15-mut text-pretty"><code class="rounded-md bg-tvt15-acc/10 px-1.5 py-0.5 font-tvt15-mono text-[12.5px] text-tvt15-acc-ink">interpolate-size: allow-keywords</code> opts the subtree into interpolating intrinsic sizes, which finally makes <code class="rounded-md bg-tvt15-acc/10 px-1.5 py-0.5 font-tvt15-mono text-[12.5px] text-tvt15-acc-ink">height: auto</code> a legal transition endpoint. Set it once, on the root.</p>
            <pre class="overflow-x-auto rounded-xl bg-tvt15-code px-4 py-3.5 font-tvt15-mono text-[12.5px] leading-[1.7] text-tvt15-c-ink shadow-inner ring-1 ring-black/10"><code><span class="text-tvt15-c-tag">&lt;section</span> <span class="text-tvt15-c-attr">class</span>=<span class="text-tvt15-c-str">"[interpolate-size:allow-keywords]"</span><span class="text-tvt15-c-tag">&gt;</span>
<span class="text-tvt15-c-cm italic">/* → interpolate-size: allow-keywords; inherited by every details */</span></code></pre>
            <p class="flex items-center justify-between gap-3 text-[12.5px] text-tvt15-mut"><span>Lesson 3 of 5</span><span class="font-tvt15-mono text-[11.5px]">interpolate-size</span></p>
          </div>
        </details>

        <details name="tvt-15-lessons" class="group/d rounded-2xl bg-tvt15-card ring-1 ring-tvt15-line transition-[box-shadow,background-color] duration-300 open:bg-tvt15-open open:shadow-tvt15-open open:ring-tvt15-acc/30 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:duration-[380ms] details-content:ease-[cubic-bezier(.32,.72,.3,1)] details-content:transition-discrete open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 select-none transition-colors duration-200 hover:bg-tvt15-acc/[0.05] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt15-ring sm:gap-4 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-full bg-tvt15-acc/10 font-tvt15-mono text-[12.5px] font-semibold text-tvt15-acc-ink ring-1 ring-tvt15-acc/20 transition-[background-color,color,box-shadow,scale] duration-300 group-open/d:scale-105 group-open/d:bg-linear-to-br group-open/d:from-tvt15-acc group-open/d:to-tvt15-acc2 group-open/d:text-white group-open/d:shadow-tvt15-badge group-open/d:ring-0 motion-reduce:transition-none">04</span>
            <span class="grid min-w-0 flex-1 leading-tight">
              <span class="text-[15.5px] font-semibold tracking-[-0.01em] text-pretty transition-colors group-open/d:text-tvt15-ink">allow-discrete</span>
              <span class="mt-1 flex items-center gap-2 text-[12.5px] text-tvt15-mut tabular-nums">6 min</span>
            </span>
            <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full text-tvt15-mut ring-1 ring-tvt15-line transition-[rotate,background-color,color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] group-open/d:rotate-180 group-open/d:bg-tvt15-acc/10 group-open/d:text-tvt15-acc-ink motion-reduce:transition-none"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="grid gap-3.5 px-4 pb-5 sm:ps-[4.75rem] sm:pe-6">
            <p class="max-w-[60ch] text-[14.5px] leading-[1.7] text-tvt15-mut text-pretty">Without <code class="rounded-md bg-tvt15-acc/10 px-1.5 py-0.5 font-tvt15-mono text-[12.5px] text-tvt15-acc-ink">transition-discrete</code>, <code class="rounded-md bg-tvt15-acc/10 px-1.5 py-0.5 font-tvt15-mono text-[12.5px] text-tvt15-acc-ink">content-visibility</code> flips the instant the item closes and the content vanishes before the height has finished collapsing.</p>
            <pre class="overflow-x-auto rounded-xl bg-tvt15-code px-4 py-3.5 font-tvt15-mono text-[12.5px] leading-[1.7] text-tvt15-c-ink shadow-inner ring-1 ring-black/10"><code><span class="text-tvt15-c-prop">details-content</span>:transition-[height,opacity,content-visibility]
<span class="text-tvt15-c-prop">details-content</span>:transition-discrete  <span class="text-tvt15-c-cm italic">/* allow-discrete */</span></code></pre>
            <p class="flex items-center justify-between gap-3 text-[12.5px] text-tvt15-mut"><span>Lesson 4 of 5</span><span class="font-tvt15-mono text-[11.5px]">allow-discrete</span></p>
          </div>
        </details>

        <details name="tvt-15-lessons" class="group/d rounded-2xl bg-tvt15-card ring-1 ring-tvt15-line transition-[box-shadow,background-color] duration-300 open:bg-tvt15-open open:shadow-tvt15-open open:ring-tvt15-acc/30 details-content:h-0 details-content:overflow-clip details-content:opacity-0 details-content:transition-[height,opacity,content-visibility] details-content:duration-[380ms] details-content:ease-[cubic-bezier(.32,.72,.3,1)] details-content:transition-discrete open:details-content:h-auto open:details-content:opacity-100 motion-reduce:details-content:transition-none">
          <summary class="flex min-h-16 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 select-none transition-colors duration-200 hover:bg-tvt15-acc/[0.05] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt15-ring sm:gap-4 sm:px-5 [&::-webkit-details-marker]:hidden">
            <span aria-hidden="true" class="grid size-10 shrink-0 place-items-center rounded-full bg-tvt15-acc/10 font-tvt15-mono text-[12.5px] font-semibold text-tvt15-acc-ink ring-1 ring-tvt15-acc/20 transition-[background-color,color,box-shadow,scale] duration-300 group-open/d:scale-105 group-open/d:bg-linear-to-br group-open/d:from-tvt15-acc group-open/d:to-tvt15-acc2 group-open/d:text-white group-open/d:shadow-tvt15-badge group-open/d:ring-0 motion-reduce:transition-none">05</span>
            <span class="grid min-w-0 flex-1 leading-tight">
              <span class="text-[15.5px] font-semibold tracking-[-0.01em] text-pretty transition-colors group-open/d:text-tvt15-ink">Nothing to hydrate</span>
              <span class="mt-1 flex items-center gap-2 text-[12.5px] text-tvt15-mut tabular-nums">7 min</span>
            </span>
            <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full text-tvt15-mut ring-1 ring-tvt15-line transition-[rotate,background-color,color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] group-open/d:rotate-180 group-open/d:bg-tvt15-acc/10 group-open/d:text-tvt15-acc-ink motion-reduce:transition-none"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="m5.5 8 4.5 4.5L14.5 8" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </summary>
          <div class="grid gap-3.5 px-4 pb-5 sm:ps-[4.75rem] sm:pe-6">
            <p class="max-w-[60ch] text-[14.5px] leading-[1.7] text-tvt15-mut text-pretty">Strip every enhancement and four HTML attributes still give you a working, keyboard-operable, screen-reader-correct exclusive accordion. Every class here is decoration on top of that.</p>
            <pre class="overflow-x-auto rounded-xl bg-tvt15-code px-4 py-3.5 font-tvt15-mono text-[12.5px] leading-[1.7] text-tvt15-c-ink shadow-inner ring-1 ring-black/10"><code><span class="text-tvt15-c-cm italic">&lt;!-- no script tag, no hydration, no layout shift --&gt;</span>
<span class="text-tvt15-c-tag">&lt;details</span> <span class="text-tvt15-c-attr">name</span>=<span class="text-tvt15-c-str">"tvt-15-lessons"</span><span class="text-tvt15-c-tag">&gt;&lt;summary&gt;</span>…<span class="text-tvt15-c-tag">&lt;/summary&gt;</span>…<span class="text-tvt15-c-tag">&lt;/details&gt;</span></code></pre>
            <p class="flex items-center justify-between gap-3 text-[12.5px] text-tvt15-mut"><span>Lesson 5 of 5</span><span class="font-tvt15-mono text-[11.5px]">0 KB JS</span></p>
          </div>
        </details>
      </div>
    </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt15-card px-3.5 py-2 text-center font-tvt15-mono text-[11.5px] text-tvt15-mut ring-1 ring-tvt15-line">name="" · open: · details-content: · [interpolate-size:allow-keywords]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt15-bg: #fff0f1;
  --color-tvt15-bg: oklch(0.968 0.016 15);
  --color-tvt15-glow: #ffcbd2b3;
  --color-tvt15-glow: oklch(0.89 0.07 10 / 0.7);
  --color-tvt15-card: #fffefe;
  --color-tvt15-card: oklch(0.997 0.004 15);
  --color-tvt15-open: #fff8f9;
  --color-tvt15-open: oklch(0.985 0.012 12);
  --color-tvt15-ink: #311618;
  --color-tvt15-ink: oklch(0.24 0.045 15);
  --color-tvt15-mut: #755355;
  --color-tvt15-mut: oklch(0.48 0.045 15);
  --color-tvt15-line: #eed8d9;
  --color-tvt15-line: oklch(0.9 0.025 15);
  --color-tvt15-acc: #ce2854;
  --color-tvt15-acc: oklch(0.56 0.2 12);
  --color-tvt15-acc2: #af0f6f;
  --color-tvt15-acc2: oklch(0.5 0.2 352);
  --color-tvt15-acc-ink: #a70f3f;
  --color-tvt15-acc-ink: oklch(0.47 0.18 12);
  --color-tvt15-hl: #ce2854;
  --color-tvt15-hl: oklch(0.56 0.2 12);
  --color-tvt15-hl2: #ae007e;
  --color-tvt15-hl2: oklch(0.5 0.22 345);
  --color-tvt15-ring: #ca2352;
  --color-tvt15-ring: oklch(0.55 0.2 12);
  --color-tvt15-ok: #00764c;
  --color-tvt15-ok: oklch(0.5 0.12 160);
  --color-tvt15-code: #2a1216;
  --color-tvt15-code: oklch(0.22 0.04 10);
  --color-tvt15-c-ink: #eee1e1;
  --color-tvt15-c-ink: oklch(0.92 0.015 15);
  --color-tvt15-c-tag: #fe93a1;
  --color-tvt15-c-tag: oklch(0.78 0.13 12);
  --color-tvt15-c-attr: #f8c384;
  --color-tvt15-c-attr: oklch(0.85 0.1 70);
  --color-tvt15-c-str: #93e4a4;
  --color-tvt15-c-str: oklch(0.85 0.12 150);
  --color-tvt15-c-cm: #aa9192;
  --color-tvt15-c-cm: oklch(0.68 0.03 15);
  --color-tvt15-c-prop: #eea2d4;
  --color-tvt15-c-prop: oklch(0.8 0.11 340);
  --font-tvt15-sans: 'Figtree', system-ui, sans-serif;
  --font-tvt15-serif: 'DM Serif Display', Georgia, serif;
  --font-tvt15-mono: 'Fira Code', ui-monospace, monospace;
  --shadow-tvt15-card: 0 1px 2px oklch(0.3 0.08 15 / 0.06), 0 30px 64px -32px oklch(0.4 0.15 12 / 0.38);
  --shadow-tvt15-open: 0 1px 2px oklch(0.3 0.08 15 / 0.08), 0 22px 48px -26px oklch(0.45 0.18 12 / 0.45);
  --shadow-tvt15-badge: 0 8px 18px -8px oklch(0.5 0.2 10 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.25);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-15 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-15:not([data-theme="light"]) {
    --color-tvt15-bg: #19090b;
    --color-tvt15-bg: oklch(0.165 0.03 10);
    --color-tvt15-glow: #61132880;
    --color-tvt15-glow: oklch(0.33 0.11 10 / 0.5);
    --color-tvt15-card: #251013;
    --color-tvt15-card: oklch(0.205 0.035 10);
    --color-tvt15-open: #301419;
    --color-tvt15-open: oklch(0.235 0.045 10);
    --color-tvt15-ink: #faefef;
    --color-tvt15-ink: oklch(0.96 0.012 15);
    --color-tvt15-mut: #caacad;
    --color-tvt15-mut: oklch(0.77 0.035 15);
    --color-tvt15-line: #49282c;
    --color-tvt15-line: oklch(0.32 0.05 12);
    --color-tvt15-acc: #ce2854;
    --color-tvt15-acc: oklch(0.56 0.2 12);
    --color-tvt15-acc2: #b61b75;
    --color-tvt15-acc2: oklch(0.52 0.2 352);
    --color-tvt15-acc-ink: #ffa8b2;
    --color-tvt15-acc-ink: oklch(0.82 0.11 12);
    --color-tvt15-hl: #ff9ea6;
    --color-tvt15-hl: oklch(0.8 0.12 15);
    --color-tvt15-hl2: #f99bd1;
    --color-tvt15-hl2: oklch(0.8 0.13 345);
    --color-tvt15-ring: #fe93a1;
    --color-tvt15-ring: oklch(0.78 0.13 12);
    --color-tvt15-ok: #68d7a1;
    --color-tvt15-ok: oklch(0.8 0.13 160);
    --color-tvt15-code: #130407;
    --color-tvt15-code: oklch(0.14 0.03 10);
  }
}

.tvt-15[data-theme="dark"] {
  --color-tvt15-bg: #19090b;
  --color-tvt15-bg: oklch(0.165 0.03 10);
  --color-tvt15-glow: #61132880;
  --color-tvt15-glow: oklch(0.33 0.11 10 / 0.5);
  --color-tvt15-card: #251013;
  --color-tvt15-card: oklch(0.205 0.035 10);
  --color-tvt15-open: #301419;
  --color-tvt15-open: oklch(0.235 0.045 10);
  --color-tvt15-ink: #faefef;
  --color-tvt15-ink: oklch(0.96 0.012 15);
  --color-tvt15-mut: #caacad;
  --color-tvt15-mut: oklch(0.77 0.035 15);
  --color-tvt15-line: #49282c;
  --color-tvt15-line: oklch(0.32 0.05 12);
  --color-tvt15-acc: #ce2854;
  --color-tvt15-acc: oklch(0.56 0.2 12);
  --color-tvt15-acc2: #b61b75;
  --color-tvt15-acc2: oklch(0.52 0.2 352);
  --color-tvt15-acc-ink: #ffa8b2;
  --color-tvt15-acc-ink: oklch(0.82 0.11 12);
  --color-tvt15-hl: #ff9ea6;
  --color-tvt15-hl: oklch(0.8 0.12 15);
  --color-tvt15-hl2: #f99bd1;
  --color-tvt15-hl2: oklch(0.8 0.13 345);
  --color-tvt15-ring: #fe93a1;
  --color-tvt15-ring: oklch(0.78 0.13 12);
  --color-tvt15-ok: #68d7a1;
  --color-tvt15-ok: oklch(0.8 0.13 160);
  --color-tvt15-code: #130407;
  --color-tvt15-code: oklch(0.14 0.03 10);
}
```

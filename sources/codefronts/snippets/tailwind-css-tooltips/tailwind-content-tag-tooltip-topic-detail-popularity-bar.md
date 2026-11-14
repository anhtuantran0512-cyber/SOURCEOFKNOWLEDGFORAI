---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-content-tag-tooltip-topic-detail-popularity-bar/"
title: "Tailwind Content Tag Tooltip with Topic Detail and Popularity Bar"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "Coloured topic pills that lift on hover and open a topic card: monogram tile, article count, description, a popularity bar with trend, related tags and three…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Content Tag Tooltip with Topic Detail and Popularity Bar
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-content-tag-tooltip-topic-detail-popularity-bar/

Coloured topic pills that lift on hover and open a topic card: monogram tile, article count, description, a popularity bar with trend, related tags and three top articles. Eight pills in eight brand colours make the port's rule explicit &mdash; the per-topic palette is inline data, the card is one @apply shell.
## HTML
```html
<section class="ttp-12 w-full min-h-svh bg-white px-7 pt-[320px] pb-9 font-ttp12-sans">
  <div class="mx-auto max-w-[560px]">
    <div class="flex flex-wrap justify-center gap-2.25">

      <div class="group relative">
        <button type="button" aria-describedby="ttp12-t1" class="ttp12-pill bg-[#eff6ff] border-[#bfdbfe] text-[#1e40af]"><span class="ttp12-dot bg-[#3b82f6]"></span>Machine Learning</button>
        <div id="ttp12-t1" role="tooltip" class="ttp12-card">
          <div class="ttp12-head"><div class="ttp12-headrow"><div class="ttp12-icon bg-[#dbeafe] text-[#1e40af]">ML</div><div><div class="ttp12-name">Machine Learning</div><div class="ttp12-count">1,284 articles</div></div></div><p class="ttp12-desc">Algorithms that enable systems to learn from data without explicit programming. Covers supervised, unsupervised and reinforcement learning.</p></div>
          <div class="ttp12-sec"><div class="ttp12-label">Popularity this month</div><div class="ttp12-track"><div class="ttp12-fill w-[88%] bg-[#3b82f6]"></div></div><div class="ttp12-trend"><span><strong>↑ trending</strong></span><span>+14% vs last month</span></div></div>
          <div class="ttp12-sec"><div class="ttp12-label">Related</div><div class="flex flex-wrap gap-1.25"><span class="ttp12-rel">Deep Learning</span><span class="ttp12-rel">Neural Nets</span><span class="ttp12-rel">PyTorch</span></div></div>
          <div class="px-3.5 pt-2.5 pb-3"><div class="ttp12-label">Top articles</div><div class="ttp12-ex">Fine-tuning LLMs on custom datasets</div><div class="ttp12-ex">Understanding transformer attention</div><div class="ttp12-ex">Gradient descent, explained visually</div></div>
        </div>
      </div>

      <div class="group relative">
        <button type="button" aria-describedby="ttp12-t2" class="ttp12-pill bg-[#f0fdf4] border-[#bbf7d0] text-[#15803d]"><span class="ttp12-dot bg-[#22c55e]"></span>Open Source</button>
        <div id="ttp12-t2" role="tooltip" class="ttp12-card">
          <div class="ttp12-head"><div class="ttp12-headrow"><div class="ttp12-icon bg-[#dcfce7] text-[#15803d]">OS</div><div><div class="ttp12-name">Open Source</div><div class="ttp12-count">2,941 articles</div></div></div><p class="ttp12-desc">Software with source code available for anyone to use, inspect, modify and distribute. Covers licensing, contributing and ecosystem news.</p></div>
          <div class="ttp12-sec"><div class="ttp12-label">Popularity this month</div><div class="ttp12-track"><div class="ttp12-fill w-[94%] bg-[#22c55e]"></div></div><div class="ttp12-trend"><span><strong>↑ all-time high</strong></span><span>+22% vs last month</span></div></div>
          <div class="ttp12-sec"><div class="ttp12-label">Related</div><div class="flex flex-wrap gap-1.25"><span class="ttp12-rel">GitHub</span><span class="ttp12-rel">Linux</span><span class="ttp12-rel">Licensing</span></div></div>
          <div class="px-3.5 pt-2.5 pb-3"><div class="ttp12-label">Top articles</div><div class="ttp12-ex">How to write a great README</div><div class="ttp12-ex">OSS licensing: MIT vs Apache vs GPL</div><div class="ttp12-ex">First PR tips for new contributors</div></div>
        </div>
      </div>

      <div class="group relative">
        <button type="button" aria-describedby="ttp12-t3" class="ttp12-pill bg-[#fdf4ff] border-[#e9d5ff] text-[#7e22ce]"><span class="ttp12-dot bg-[#a855f7]"></span>System Design</button>
        <div id="ttp12-t3" role="tooltip" class="ttp12-card">
          <div class="ttp12-head"><div class="ttp12-headrow"><div class="ttp12-icon bg-[#f3e8ff] text-[#7e22ce]">SD</div><div><div class="ttp12-name">System Design</div><div class="ttp12-count">876 articles</div></div></div><p class="ttp12-desc">The process of defining the architecture, components and interfaces of a system to satisfy specified requirements at scale.</p></div>
          <div class="ttp12-sec"><div class="ttp12-label">Popularity this month</div><div class="ttp12-track"><div class="ttp12-fill w-[76%] bg-[#a855f7]"></div></div><div class="ttp12-trend"><span><strong>→ stable</strong></span><span>+3% vs last month</span></div></div>
          <div class="ttp12-sec"><div class="ttp12-label">Related</div><div class="flex flex-wrap gap-1.25"><span class="ttp12-rel">Distributed</span><span class="ttp12-rel">CAP Theorem</span><span class="ttp12-rel">Databases</span></div></div>
          <div class="px-3.5 pt-2.5 pb-3"><div class="ttp12-label">Top articles</div><div class="ttp12-ex">Designing a rate limiter from scratch</div><div class="ttp12-ex">When to use a message queue</div><div class="ttp12-ex">Read replicas and write-ahead logs</div></div>
        </div>
      </div>

      <div class="group relative">
        <button type="button" aria-describedby="ttp12-t4" class="ttp12-pill bg-[#fff7ed] border-[#fed7aa] text-[#c2410c]"><span class="ttp12-dot bg-[#f97316]"></span>Career</button>
        <div id="ttp12-t4" role="tooltip" class="ttp12-card">
          <div class="ttp12-head"><div class="ttp12-headrow"><div class="ttp12-icon bg-[#ffedd5] text-[#c2410c]">CR</div><div><div class="ttp12-name">Career</div><div class="ttp12-count">3,102 articles</div></div></div><p class="ttp12-desc">Advice on navigating tech careers — from first job to staff engineer, negotiation, interviews and switching roles.</p></div>
          <div class="ttp12-sec"><div class="ttp12-label">Popularity this month</div><div class="ttp12-track"><div class="ttp12-fill w-[82%] bg-[#f97316]"></div></div><div class="ttp12-trend"><span><strong>↑ trending</strong></span><span>+9% vs last month</span></div></div>
          <div class="ttp12-sec"><div class="ttp12-label">Related</div><div class="flex flex-wrap gap-1.25"><span class="ttp12-rel">Interviews</span><span class="ttp12-rel">Salary</span><span class="ttp12-rel">Remote work</span></div></div>
          <div class="px-3.5 pt-2.5 pb-3"><div class="ttp12-label">Top articles</div><div class="ttp12-ex">The staff engineer path, explained</div><div class="ttp12-ex">How to negotiate a competing offer</div><div class="ttp12-ex">Writing your first performance review</div></div>
        </div>
      </div>

      <div class="group relative">
        <button type="button" aria-describedby="ttp12-t5" class="ttp12-pill bg-[#fff1f2] border-[#fecdd3] text-[#be123c]"><span class="ttp12-dot bg-[#f43f5e]"></span>Security</button>
        <div id="ttp12-t5" role="tooltip" class="ttp12-card">
          <div class="ttp12-head"><div class="ttp12-headrow"><div class="ttp12-icon bg-[#ffe4e6] text-[#be123c]">SE</div><div><div class="ttp12-name">Security</div><div class="ttp12-count">1,540 articles</div></div></div><p class="ttp12-desc">Application security, cryptography, threat modelling, vulnerability research and secure development practices for engineers.</p></div>
          <div class="ttp12-sec"><div class="ttp12-label">Popularity this month</div><div class="ttp12-track"><div class="ttp12-fill w-[70%] bg-[#f43f5e]"></div></div><div class="ttp12-trend"><span><strong>↑ trending</strong></span><span>+18% vs last month</span></div></div>
          <div class="ttp12-sec"><div class="ttp12-label">Related</div><div class="flex flex-wrap gap-1.25"><span class="ttp12-rel">OWASP</span><span class="ttp12-rel">Auth</span><span class="ttp12-rel">CVE</span></div></div>
          <div class="px-3.5 pt-2.5 pb-3"><div class="ttp12-label">Top articles</div><div class="ttp12-ex">SQL injection prevention, 2026 edition</div><div class="ttp12-ex">JWT vs sessions: which to use</div><div class="ttp12-ex">Zero-trust architecture basics</div></div>
        </div>
      </div>

      <div class="group relative">
        <button type="button" aria-describedby="ttp12-t6" class="ttp12-pill bg-[#f0fdfa] border-[#99f6e4] text-[#0f766e]"><span class="ttp12-dot bg-[#14b8a6]"></span>DevOps</button>
        <div id="ttp12-t6" role="tooltip" class="ttp12-card">
          <div class="ttp12-head"><div class="ttp12-headrow"><div class="ttp12-icon bg-[#ccfbf1] text-[#0f766e]">DO</div><div><div class="ttp12-name">DevOps</div><div class="ttp12-count">1,188 articles</div></div></div><p class="ttp12-desc">Practices and tools that unify software development and IT operations — CI/CD, containerisation, infrastructure as code, monitoring.</p></div>
          <div class="ttp12-sec"><div class="ttp12-label">Popularity this month</div><div class="ttp12-track"><div class="ttp12-fill w-[66%] bg-[#14b8a6]"></div></div><div class="ttp12-trend"><span><strong>→ stable</strong></span><span>+2% vs last month</span></div></div>
          <div class="ttp12-sec"><div class="ttp12-label">Related</div><div class="flex flex-wrap gap-1.25"><span class="ttp12-rel">Docker</span><span class="ttp12-rel">Kubernetes</span><span class="ttp12-rel">Terraform</span></div></div>
          <div class="px-3.5 pt-2.5 pb-3"><div class="ttp12-label">Top articles</div><div class="ttp12-ex">Building zero-downtime deploys</div><div class="ttp12-ex">Helm charts for beginners</div><div class="ttp12-ex">Observability vs. monitoring</div></div>
        </div>
      </div>

      <div class="group relative">
        <button type="button" aria-describedby="ttp12-t7" class="ttp12-pill bg-[#fefce8] border-[#fef08a] text-[#854d0e]"><span class="ttp12-dot bg-[#eab308]"></span>Performance</button>
        <div id="ttp12-t7" role="tooltip" class="ttp12-card">
          <div class="ttp12-head"><div class="ttp12-headrow"><div class="ttp12-icon bg-[#fef9c3] text-[#854d0e]">PF</div><div><div class="ttp12-name">Performance</div><div class="ttp12-count">922 articles</div></div></div><p class="ttp12-desc">Techniques for optimising speed, throughput and resource efficiency — from query tuning to Core Web Vitals.</p></div>
          <div class="ttp12-sec"><div class="ttp12-label">Popularity this month</div><div class="ttp12-track"><div class="ttp12-fill w-[60%] bg-[#eab308]"></div></div><div class="ttp12-trend"><span><strong>→ stable</strong></span><span>+1% vs last month</span></div></div>
          <div class="ttp12-sec"><div class="ttp12-label">Related</div><div class="flex flex-wrap gap-1.25"><span class="ttp12-rel">Profiling</span><span class="ttp12-rel">Caching</span><span class="ttp12-rel">Web Vitals</span></div></div>
          <div class="px-3.5 pt-2.5 pb-3"><div class="ttp12-label">Top articles</div><div class="ttp12-ex">N+1 queries and how to fix them</div><div class="ttp12-ex">React re-renders: a visual guide</div><div class="ttp12-ex">Redis caching patterns in production</div></div>
        </div>
      </div>

      <div class="group relative">
        <button type="button" aria-describedby="ttp12-t8" class="ttp12-pill bg-[#f8fafc] border-[#e2e8f0] text-[#475569]"><span class="ttp12-dot bg-[#64748b]"></span>Architecture</button>
        <div id="ttp12-t8" role="tooltip" class="ttp12-card">
          <div class="ttp12-head"><div class="ttp12-headrow"><div class="ttp12-icon bg-[#f1f5f9] text-[#475569]">AR</div><div><div class="ttp12-name">Architecture</div><div class="ttp12-count">748 articles</div></div></div><p class="ttp12-desc">Software architecture patterns, trade-offs and design decisions — microservices, monoliths, event-driven, hexagonal and beyond.</p></div>
          <div class="ttp12-sec"><div class="ttp12-label">Popularity this month</div><div class="ttp12-track"><div class="ttp12-fill w-[54%] bg-[#64748b]"></div></div><div class="ttp12-trend"><span><strong>↓ slight dip</strong></span><span>−3% vs last month</span></div></div>
          <div class="ttp12-sec"><div class="ttp12-label">Related</div><div class="flex flex-wrap gap-1.25"><span class="ttp12-rel">DDD</span><span class="ttp12-rel">Microservices</span><span class="ttp12-rel">Clean Code</span></div></div>
          <div class="px-3.5 pt-2.5 pb-3"><div class="ttp12-label">Top articles</div><div class="ttp12-ex">Monolith first: the case for starting simple</div><div class="ttp12-ex">CQRS and event sourcing, explained</div><div class="ttp12-ex">When to break up a microservice</div></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp12-ink: #111111;
  --color-ttp12-ink: oklch(0.18 0 0);
  --color-ttp12-body: #5c5c5c;
  --color-ttp12-body: oklch(0.47 0 0);
  --color-ttp12-muted: #6f6f6f;
  --color-ttp12-muted: oklch(0.53 0 0);
  --color-ttp12-rule: #f0f0f0;
  --color-ttp12-rule: oklch(0.95 0 0);
  --color-ttp12-chip: #f4f4f6;
  --color-ttp12-chip: oklch(0.96 0.002 270);
  --font-ttp12-sans: 'Inter', system-ui, sans-serif;
}

.ttp-12 {
  width: 100%;
  min-height: 100svh;
}
/* Eight pills, eight identical cards, six repeated sections. The
   per-topic palette stays inline on the pill and the monogram tile,
   because that trio of colours IS the tag. */

.ttp-12 .ttp12-pill {
  @apply inline-flex cursor-help items-center gap-1.5 rounded-full border px-3 py-1.5 text-[12.5px] font-medium transition-[transform,box-shadow] duration-150 group-hover:-translate-y-0.5 group-hover:shadow-[0_6px_16px_rgba(0,0,0,0.1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp12-ink;
}

.ttp-12 .ttp12-dot {
  @apply h-1.5 w-1.5 shrink-0 rounded-full;
}

.ttp-12 .ttp12-card {
  @apply pointer-events-none invisible absolute bottom-[calc(100%+9px)] left-1/2 z-30 w-65 max-w-[calc(100vw-48px)] -translate-x-1/2 translate-y-1 overflow-hidden rounded-[11px] border border-black/7 bg-white text-left opacity-0 shadow-[0_12px_36px_rgba(0,0,0,0.11),0_2px_8px_rgba(0,0,0,0.05)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100;
}

.ttp-12 .ttp12-head {
  @apply border-b border-ttp12-rule px-3.5 pt-3.25 pb-2.75;
}

.ttp-12 .ttp12-headrow {
  @apply mb-2 flex items-center gap-2.5;
}

.ttp-12 .ttp12-icon {
  @apply flex h-7.5 w-7.5 shrink-0 items-center justify-center rounded-[7px] text-[11px] font-bold tracking-[0.04em];
}

.ttp-12 .ttp12-name {
  @apply text-sm font-bold leading-tight text-ttp12-ink;
}

.ttp-12 .ttp12-count {
  @apply mt-px text-[10.5px] text-ttp12-muted;
}

.ttp-12 .ttp12-desc {
  @apply m-0 text-[11.5px] leading-[1.55] text-ttp12-body;
}

.ttp-12 .ttp12-sec {
  @apply border-b border-ttp12-rule px-3.5 py-2.5;
}

.ttp-12 .ttp12-label {
  @apply mb-1.5 text-[8.5px] uppercase tracking-[0.1em] text-ttp12-muted;
}

.ttp-12 .ttp12-track {
  @apply mb-1.25 h-1.25 overflow-hidden rounded-[3px] bg-ttp12-rule;
}

.ttp-12 .ttp12-fill {
  @apply h-full rounded-[3px];
}

.ttp-12 .ttp12-trend {
  @apply flex justify-between text-[10.5px] text-ttp12-muted;
}

.ttp-12 .ttp12-trend strong {
  @apply font-semibold text-ttp12-body;
}

.ttp-12 .ttp12-rel {
  @apply rounded-[10px] border border-ttp12-rule bg-ttp12-chip px-1.75 py-0.5 text-[10px] text-ttp12-body;
}

.ttp-12 .ttp12-ex {
  @apply relative mb-1 pl-2.25 text-[10.5px] leading-[1.4] text-ttp12-body before:absolute before:left-0.5 before:text-ttp12-muted before:content-['·'];
}
```

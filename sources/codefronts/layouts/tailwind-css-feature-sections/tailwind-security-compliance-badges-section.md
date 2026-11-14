---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-security-compliance-badges-section/"
title: "Tailwind Security Compliance Badges Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "An enterprise trust block on deep navy: four certification seals (SOC 2 Type II, ISO 27001, GDPR, HIPAA) with audit dates, a live 'all systems operational'…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Security Compliance Badges Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-security-compliance-badges-section/

An enterprise trust block on deep navy: four certification seals (SOC 2 Type II, ISO 27001, GDPR, HIPAA) with audit dates, a live 'all systems operational' strip, and three security features with spec-sheet detail. Seals use a conic-gradient ring so they read as badges, not buttons.
## HTML
```html
<section class="tfs-09 relative w-full min-h-svh overflow-hidden bg-tfs09-bg px-5 py-20 font-tfs09-sans text-white antialiased sm:py-28" aria-labelledby="tfs-09-h">
  <div aria-hidden="true" class="absolute inset-0 bg-[radial-gradient(60%_50%_at_50%_0%,color-mix(in_oklab,var(--color-tfs09-acc)_22%,transparent),transparent)]"></div>
  <div class="relative mx-auto grid w-full max-w-6xl gap-14">
    <header class="grid gap-6 lg:grid-cols-[1.2fr_1fr] lg:items-end">
      <div class="grid gap-4">
        <p class="inline-flex w-fit items-center gap-2 rounded-full bg-white/5 px-3 py-1 text-xs font-semibold text-tfs09-acc ring-1 ring-white/10"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Security &amp; compliance</p>
        <h2 id="tfs-09-h" class="text-balance text-4xl font-extrabold tracking-tight sm:text-5xl">Enterprise-grade from day one</h2>
      </div>
      <a href="#tfs-09-h" class="flex min-h-11 items-center gap-3 rounded-2xl bg-white/5 px-4 py-3 text-sm ring-1 ring-white/10 transition hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-tfs09-acc lg:justify-self-end"><span class="relative flex size-2.5"><span class="absolute inset-0 animate-ping rounded-full bg-emerald-400/70 motion-reduce:hidden"></span><span class="relative size-2.5 rounded-full bg-emerald-400"></span></span>All systems operational<span class="text-tfs09-mut">· 99.99% 90d</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-tfs09-mut"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </header>
    <ul class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      <li class="group grid justify-items-center gap-4 rounded-3xl bg-tfs09-card p-7 text-center ring-1 ring-white/10 transition hover:-translate-y-1 hover:ring-tfs09-acc/50">
        <div class="relative grid size-24 place-items-center rounded-full bg-conic-[from_200deg,var(--color-tfs09-acc),var(--color-tfs09-acc2),var(--color-tfs09-acc)] p-0.5 shadow-[0_0_40px_-8px_var(--color-tfs09-acc)]"><div class="grid size-full place-items-center rounded-full bg-tfs09-card"><span class="grid justify-items-center gap-1 text-tfs09-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg><span class="font-tfs09-mono text-[11px] font-semibold tracking-wider text-white">SOC 2</span></span></div></div>
        <div><h3 class="font-bold">SOC 2 Type II</h3><p class="mt-1 text-sm text-tfs09-mut">Audited Jun 2026</p></div>
      </li>
      <li class="group grid justify-items-center gap-4 rounded-3xl bg-tfs09-card p-7 text-center ring-1 ring-white/10 transition hover:-translate-y-1 hover:ring-tfs09-acc/50">
        <div class="relative grid size-24 place-items-center rounded-full bg-conic-[from_200deg,var(--color-tfs09-acc),var(--color-tfs09-acc2),var(--color-tfs09-acc)] p-0.5 shadow-[0_0_40px_-8px_var(--color-tfs09-acc)]"><div class="grid size-full place-items-center rounded-full bg-tfs09-card"><span class="grid justify-items-center gap-1 text-tfs09-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg><span class="font-tfs09-mono text-[11px] font-semibold tracking-wider text-white">ISO</span></span></div></div>
        <div><h3 class="font-bold">ISO/IEC 27001</h3><p class="mt-1 text-sm text-tfs09-mut">Certified 2026–2029</p></div>
      </li>
      <li class="group grid justify-items-center gap-4 rounded-3xl bg-tfs09-card p-7 text-center ring-1 ring-white/10 transition hover:-translate-y-1 hover:ring-tfs09-acc/50">
        <div class="relative grid size-24 place-items-center rounded-full bg-conic-[from_200deg,var(--color-tfs09-acc),var(--color-tfs09-acc2),var(--color-tfs09-acc)] p-0.5 shadow-[0_0_40px_-8px_var(--color-tfs09-acc)]"><div class="grid size-full place-items-center rounded-full bg-tfs09-card"><span class="grid justify-items-center gap-1 text-tfs09-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M7 11V7a5 5 0 0 1 10 0v4M5 11h14v10H5z"/></svg><span class="font-tfs09-mono text-[11px] font-semibold tracking-wider text-white">GDPR</span></span></div></div>
        <div><h3 class="font-bold">GDPR &amp; UK GDPR</h3><p class="mt-1 text-sm text-tfs09-mut">DPA on request</p></div>
      </li>
      <li class="group grid justify-items-center gap-4 rounded-3xl bg-tfs09-card p-7 text-center ring-1 ring-white/10 transition hover:-translate-y-1 hover:ring-tfs09-acc/50">
        <div class="relative grid size-24 place-items-center rounded-full bg-conic-[from_200deg,var(--color-tfs09-acc),var(--color-tfs09-acc2),var(--color-tfs09-acc)] p-0.5 shadow-[0_0_40px_-8px_var(--color-tfs09-acc)]"><div class="grid size-full place-items-center rounded-full bg-tfs09-card"><span class="grid justify-items-center gap-1 text-tfs09-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6"><path d="M2 18v3h3l7.4-7.4A5 5 0 1 0 9.4 10.6L2 18zM16 8h.01"/></svg><span class="font-tfs09-mono text-[11px] font-semibold tracking-wider text-white">HIPAA</span></span></div></div>
        <div><h3 class="font-bold">HIPAA</h3><p class="mt-1 text-sm text-tfs09-mut">BAA available</p></div>
      </li>
    </ul>
    <div class="grid gap-4 md:grid-cols-3">
      <article class="grid gap-3 rounded-3xl border border-white/10 bg-white/[0.03] p-7"><span class="grid size-10 place-items-center rounded-xl bg-tfs09-acc/15 text-tfs09-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M7 11V7a5 5 0 0 1 10 0v4M5 11h14v10H5z"/></svg></span><h3 class="text-lg font-bold">Encrypted everywhere</h3><p class="text-pretty text-sm text-tfs09-mut">Data encrypted at rest and in transit, with customer-managed keys on Enterprise.</p><p class="mt-auto border-t border-white/10 pt-3 font-tfs09-mono text-xs text-tfs09-acc">AES-256 · TLS 1.3 · BYOK</p></article>
      <article class="grid gap-3 rounded-3xl border border-white/10 bg-white/[0.03] p-7"><span class="grid size-10 place-items-center rounded-xl bg-tfs09-acc/15 text-tfs09-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span><h3 class="text-lg font-bold">Access you control</h3><p class="text-pretty text-sm text-tfs09-mut">SAML SSO, SCIM and role-based permissions down to the field.</p><p class="mt-auto border-t border-white/10 pt-3 font-tfs09-mono text-xs text-tfs09-acc">SAML 2.0 · SCIM 2.0 · RBAC</p></article>
      <article class="grid gap-3 rounded-3xl border border-white/10 bg-white/[0.03] p-7"><span class="grid size-10 place-items-center rounded-xl bg-tfs09-acc/15 text-tfs09-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12zM12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/></svg></span><h3 class="text-lg font-bold">Audited continuously</h3><p class="text-pretty text-sm text-tfs09-mut">Annual third-party pen tests and a public bug bounty since 2022.</p><p class="mt-auto border-t border-white/10 pt-3 font-tfs09-mono text-xs text-tfs09-acc">Pen test Q2 · HackerOne</p></article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs09-bg: #060b1a;
  --color-tfs09-bg: oklch(0.153 0.033 267);
  --color-tfs09-card: #0c1428;
  --color-tfs09-card: oklch(0.195 0.042 266);
  --color-tfs09-mut: #a6b0c8;
  --color-tfs09-mut: oklch(0.757 0.036 268);
  --color-tfs09-acc: #5eead4;
  --color-tfs09-acc: oklch(0.855 0.125 181);
  --color-tfs09-acc2: #60a5fa;
  --color-tfs09-acc2: oklch(0.714 0.143 255);
  --font-tfs09-sans: 'Manrope', system-ui, sans-serif;
  --font-tfs09-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-09 {
  width: 100%;
  min-height: 100svh;
}
```

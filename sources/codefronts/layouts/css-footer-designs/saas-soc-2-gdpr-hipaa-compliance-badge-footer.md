---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/saas-soc-2-gdpr-hipaa-compliance-badge-footer/"
title: "SaaS SOC 2 / GDPR / HIPAA Compliance Badge Footer"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The footer an enterprise buyer's security reviewer actually reads: certification seals that each expose the audit period, the auditor and the report link,…"
has_js: "false"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS SOC 2 / GDPR / HIPAA Compliance Badge Footer
Source: https://codefronts.com/layouts/css-footer-designs/saas-soc-2-gdpr-hipaa-compliance-badge-footer/

The footer an enterprise buyer's security reviewer actually reads: certification seals that each expose the audit period, the auditor and the report link, plus the data-residency and DPA links procurement will ask for. Every badge is a real disclosure, not a sticker — which is the difference between building trust and triggering suspicion.
## HTML
```html
<section class="ft-10" aria-label="Compliance badge footer demo">
  <main class="ft-10__main">
    <p class="ft-10__eyebrow">:focus-within · audit metadata</p>
    <h1 class="ft-10__title">Badges that survive a security review</h1>
    <p class="ft-10__sub">Hover or tab into any seal below. Each one names the auditor, the period and the report — because a reviewer's first question is never “do you have SOC 2”, it is “which type, and when”.</p>
  </main>
  <footer class="ft-10__foot">
    <section class="ft-10__trust" aria-labelledby="ft-10-th">
      <div class="ft-10__thead">
        <h2 class="ft-10__h" id="ft-10-th">Security &amp; compliance</h2>
        <a class="ft-10__tc" href="#ft-10-a">Open the trust centre<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6"/></svg></a>
      </div>
      <ul class="ft-10__badges">
        <li class="ft-10__badge" style="--ft-10-seal:oklch(0.72 0.15 165)">
          <span class="ft-10__seal" aria-hidden="true"><svg viewBox="0 0 40 40" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.7" focusable="false"><path d="M20 3l14 5v11c0 8.5-5.8 14.8-14 18-8.2-3.2-14-9.5-14-18V8z"/><path d="M14 20l4.4 4.4L27 15.6" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          <span class="ft-10__blabel">SOC 2 Type II</span>
          <span class="ft-10__bmeta">Renewed Mar 2026</span>
          <div class="ft-10__detail">
            <dl class="ft-10__dl"><div><dt>Auditor</dt><dd>Prescient Assurance</dd></div><div><dt>Period</dt><dd><time datetime="2025-04-01">Apr 2025</time> – <time datetime="2026-03-31">Mar 2026</time></dd></div><div><dt>Scope</dt><dd>Security, Availability, Confidentiality</dd></div></dl>
            <a class="ft-10__dlink" href="#ft-10-a">Request the report (NDA)</a>
          </div>
        </li>
        <li class="ft-10__badge" style="--ft-10-seal:oklch(0.72 0.14 250)">
          <span class="ft-10__seal" aria-hidden="true"><svg viewBox="0 0 40 40" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.7" focusable="false"><circle cx="20" cy="20" r="15"/><path d="M20 5v30M5 20h30" opacity=".45"/><circle cx="20" cy="20" r="6.5" stroke-width="2.4"/></svg></span>
          <span class="ft-10__blabel">GDPR &amp; UK GDPR</span>
          <span class="ft-10__bmeta">EU + UK data residency</span>
          <div class="ft-10__detail">
            <dl class="ft-10__dl"><div><dt>DPA</dt><dd>Standard, countersigned at signup</dd></div><div><dt>Transfers</dt><dd>SCCs + UK addendum</dd></div><div><dt>DPO</dt><dd>[email protected]</dd></div></dl>
            <a class="ft-10__dlink" href="#ft-10-a">Read the DPA</a>
          </div>
        </li>
        <li class="ft-10__badge" style="--ft-10-seal:oklch(0.74 0.13 30)">
          <span class="ft-10__seal" aria-hidden="true"><svg viewBox="0 0 40 40" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.7" focusable="false"><rect x="6" y="12" width="28" height="22" rx="4"/><path d="M14 12V9a6 6 0 0 1 12 0v3"/><path d="M20 21v5" stroke-width="2.4" stroke-linecap="round"/></svg></span>
          <span class="ft-10__blabel">HIPAA</span>
          <span class="ft-10__bmeta">BAA available</span>
          <div class="ft-10__detail">
            <dl class="ft-10__dl"><div><dt>Assessment</dt><dd>Annual, independent</dd></div><div><dt>PHI handling</dt><dd>Encrypted at rest (AES-256) and in transit</dd></div><div><dt>BAA</dt><dd>Signed for Business &amp; Enterprise</dd></div></dl>
            <a class="ft-10__dlink" href="#ft-10-a">Request a BAA</a>
          </div>
        </li>
        <li class="ft-10__badge" style="--ft-10-seal:oklch(0.76 0.14 95)">
          <span class="ft-10__seal" aria-hidden="true"><svg viewBox="0 0 40 40" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.7" focusable="false"><circle cx="20" cy="17" r="11"/><path d="M14 33l6-4 6 4" stroke-linejoin="round"/><path d="M15 17l3.6 3.6L26 13" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          <span class="ft-10__blabel">ISO/IEC 27001</span>
          <span class="ft-10__bmeta">Cert. 2025-0441-IS</span>
          <div class="ft-10__detail">
            <dl class="ft-10__dl"><div><dt>Body</dt><dd>BSI</dd></div><div><dt>Valid to</dt><dd><time datetime="2028-06-30">30 June 2028</time></dd></div><div><dt>Statement</dt><dd>SoA v4.2 published</dd></div></dl>
            <a class="ft-10__dlink" href="#ft-10-a">Verify the certificate</a>
          </div>
        </li>
      </ul>
      <p class="ft-10__resid"><span class="ft-10__pulse" aria-hidden="true"></span>All systems operational · data resident in <strong>eu-west-1</strong> and <strong>us-east-2</strong> · <a class="ft-10__slink" href="#ft-10-a">security.txt</a> · <a class="ft-10__slink" href="#ft-10-a">Sub-processors (14)</a></p>
    </section>
    <div class="ft-10__cols">
      <div class="ft-10__brandcol">
        <div class="ft-10__brand"><span class="ft-10__mark" aria-hidden="true"></span>Arcvault</div>
        <p class="ft-10__blurb">Encrypted document infrastructure for regulated teams.</p>
      </div>
      <nav class="ft-10__col" aria-labelledby="ft-10-c1"><h2 class="ft-10__ch" id="ft-10-c1">Platform</h2><ul class="ft-10__list"><li><a class="ft-10__link" href="#ft-10-a">Vaults</a></li><li><a class="ft-10__link" href="#ft-10-a">Access control</a></li><li><a class="ft-10__link" href="#ft-10-a">Audit log</a></li><li><a class="ft-10__link" href="#ft-10-a">Retention</a></li></ul></nav>
      <nav class="ft-10__col" aria-labelledby="ft-10-c2"><h2 class="ft-10__ch" id="ft-10-c2">Legal</h2><ul class="ft-10__list"><li><a class="ft-10__link" href="#ft-10-a">Terms of service</a></li><li><a class="ft-10__link" href="#ft-10-a">Privacy notice</a></li><li><a class="ft-10__link" href="#ft-10-a">DPA</a></li><li><a class="ft-10__link" href="#ft-10-a">Acceptable use</a></li></ul></nav>
      <nav class="ft-10__col" aria-labelledby="ft-10-c3"><h2 class="ft-10__ch" id="ft-10-c3">Company</h2><ul class="ft-10__list"><li><a class="ft-10__link" href="#ft-10-a">About</a></li><li><a class="ft-10__link" href="#ft-10-a">Security</a></li><li><a class="ft-10__link" href="#ft-10-a">Careers</a></li><li><a class="ft-10__link" href="#ft-10-a">Contact</a></li></ul></nav>
    </div>
    <p class="ft-10__copy">© <time datetime="2026">2026</time> Arcvault Inc. · Delaware C-Corp · Report a vulnerability: <a class="ft-10__slink" href="#ft-10-a">[email protected]</a></p>
  </footer>
</section>
```
## CSS
```css
.ft-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-10-bg);
  --ft-10-bg: oklch(0.98 0.004 255);
  --ft-10-foot: oklch(0.17 0.02 260);
  --ft-10-ink: oklch(0.21 0.025 260);
  --ft-10-mut: oklch(0.53 0.02 260);
  --ft-10-fink: oklch(0.97 0.005 260);
  --ft-10-fmut: oklch(0.73 0.015 260);
  --ft-10-acc: oklch(0.72 0.15 165);
  --ft-10-fline: oklch(0.97 0.005 260/.14);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-10-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-10 *,
.ft-10 *::before,
.ft-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-10 ul {
  list-style: none;
}

.ft-10__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(40px,8vh,90px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1180px)/2));
}

.ft-10__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: oklch(0.5 0.13 165);
}

.ft-10__title {
  font-size: clamp(29px,5.2vw,56px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 16ch;
  text-wrap: balance;
}

.ft-10__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-10-mut);
  max-width: 60ch;
  text-wrap: pretty;
}

.ft-10__foot {
  background: var(--ft-10-foot);
  color: var(--ft-10-fink);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1180px)/2));
}

.ft-10__trust {
  display: grid;
  gap: 16px;
  padding-block: clamp(28px,4vw,44px);
}

.ft-10__thead {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 10px 20px;
}

.ft-10__h {
  font-size: clamp(17px,2vw,21px);
  font-weight: 690;
  letter-spacing: -.02em;
}

.ft-10__tc {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  margin-inline-start: auto;
  font-size: 13.5px;
  font-weight: 640;
  color: var(--ft-10-acc);
  text-decoration: none;
  padding: 8px 0;
}

.ft-10__tc:hover svg {
  translate: 3px 0;
}

.ft-10__tc svg {
  transition: translate .22s ease;
}

.ft-10__badges {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(13rem,100%),1fr));
  gap: 12px;
}

.ft-10__badge {
  position: relative;
  display: grid;
  justify-items: start;
  gap: 5px;
  padding: 16px;
  border-radius: 16px;
  background: oklch(0.97 0.005 260/.05);
  border: 1px solid var(--ft-10-fline);
  transition: border-color .25s ease,background .25s ease;
}

.ft-10__badge:hover,
.ft-10__badge:focus-within {
  border-color: color-mix(in oklch,var(--ft-10-seal) 55%,transparent);
  background: color-mix(in oklch,var(--ft-10-seal) 10%,transparent);
}

.ft-10__seal {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 13px;
  background: color-mix(in oklch,var(--ft-10-seal) 16%,transparent);
  color: var(--ft-10-seal);
  margin-block-end: 4px;
}

.ft-10__blabel {
  font-size: 14.5px;
  font-weight: 680;
  letter-spacing: -.01em;
}

.ft-10__bmeta {
  font-size: 12.3px;
  color: var(--ft-10-fmut);
  font-variant-numeric: tabular-nums;
}

.ft-10__detail {
  position: absolute;
  left: 8px;
  right: 8px;
  bottom: calc(100% + 8px);
  z-index: 5;
  display: grid;
  gap: 10px;
  padding: 14px;
  border-radius: 14px;
  background: oklch(0.23 0.022 260);
  border: 1px solid color-mix(in oklch,var(--ft-10-seal) 40%,transparent);
  box-shadow: 0 22px 48px -22px oklch(0 0 0/.85);
  opacity: 0;
  visibility: hidden;
  translate: 0 6px;
  transition: opacity .24s ease,translate .24s ease,visibility .24s;
}

.ft-10__badge:hover .ft-10__detail,
.ft-10__badge:focus-within .ft-10__detail {
  opacity: 1;
  visibility: visible;
  translate: 0 0;
}

.ft-10__dl {
  display: grid;
  gap: 7px;
}

.ft-10__dl>div {
  display: grid;
  grid-template-columns: 5.4rem 1fr;
  gap: 10px;
  font-size: 12.4px;
  line-height: 1.4;
}

.ft-10__dl dt {
  color: var(--ft-10-fmut);
}

.ft-10__dl dd {
  font-weight: 600;
  text-wrap: pretty;
}

.ft-10__dlink {
  font-size: 12.5px;
  font-weight: 650;
  color: var(--ft-10-seal);
  text-decoration: underline;
  text-underline-offset: .25em;
}

.ft-10__resid {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  font-size: 12.8px;
  color: var(--ft-10-fmut);
}

.ft-10__resid strong {
  color: var(--ft-10-fink);
  font-weight: 640;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .94em;
}

.ft-10__pulse {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--ft-10-acc);
  box-shadow: 0 0 0 0 color-mix(in oklch,var(--ft-10-acc) 70%,transparent);
  animation: ft-10-pulse 2.4s ease-out infinite;
}

@keyframes ft-10-pulse {
  0% {
    box-shadow: 0 0 0 0 color-mix(in oklch,var(--ft-10-acc) 60%,transparent);
  }

  70% {
    box-shadow: 0 0 0 9px transparent;
  }

  100% {
    box-shadow: 0 0 0 0 transparent;
  }
}

.ft-10__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: clamp(24px,3.2vw,38px) clamp(16px,2.2vw,30px);
  padding-block: clamp(26px,3.6vw,40px);
  border-top: 1px solid var(--ft-10-fline);
}

.ft-10__brandcol {
  display: grid;
  align-content: start;
  gap: 10px;
  min-width: 0;
}

.ft-10__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ft-10__mark {
  width: 23px;
  height: 23px;
  border-radius: 7px;
  background: linear-gradient(145deg,var(--ft-10-acc),oklch(0.66 0.14 250));
}

.ft-10__blurb {
  font-size: 14px;
  line-height: 1.55;
  color: var(--ft-10-fmut);
  max-width: 30ch;
}

.ft-10__col {
  display: grid;
  align-content: start;
  gap: 4px;
  min-width: 0;
}

.ft-10__ch {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  margin-block-end: 8px;
}

.ft-10__list {
  display: grid;
  gap: 1px;
}

.ft-10__link {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  font-size: 14px;
  color: var(--ft-10-fmut);
  text-decoration: none;
  width: fit-content;
  transition: color .18s ease;
}

.ft-10__link:hover {
  color: var(--ft-10-acc);
}

.ft-10__link:focus-visible,
.ft-10__slink:focus-visible,
.ft-10__dlink:focus-visible,
.ft-10__tc:focus-visible {
  outline: 2px solid var(--ft-10-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.ft-10__slink {
  color: var(--ft-10-fink);
  text-decoration: underline;
  text-underline-offset: .25em;
  text-decoration-color: color-mix(in oklch,currentColor 32%,transparent);
}

.ft-10__copy {
  padding-block: 18px;
  padding-bottom: calc(18px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-10-fline);
  font-size: 12.6px;
  line-height: 1.6;
  color: var(--ft-10-fmut);
}

@media (max-width: 560px) {
  .ft-10__tc {
    margin-inline-start: 0;
  }

  .ft-10__detail {
    position: static;
    opacity: 1;
    visibility: visible;
    translate: 0;
    box-shadow: none;
    margin-block-start: 8px;
    justify-self: stretch;
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-10 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

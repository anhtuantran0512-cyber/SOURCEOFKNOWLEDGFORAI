---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/categorized-faq-with-sticky-sidebar-menu/"
title: "Categorized FAQ with Sticky Sidebar Menu"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The help-center layout: FAQ questions grouped under category headings with a sticky sidebar menu that jumps between sections — the pattern every SaaS support…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Categorized FAQ with Sticky Sidebar Menu
Source: https://codefronts.com/snippets/css-faq-accordion/categorized-faq-with-sticky-sidebar-menu/

The help-center layout: FAQ questions grouped under category headings with a sticky sidebar menu that jumps between sections — the pattern every SaaS support page converges on once questions pass a dozen. All navigation is native anchors: position:sticky pins the menu, scroll-margin-top stops headings hiding under the sticky header, scroll-behavior:smooth makes jumps glide, and the whole stage is its own scroll container so the demo behaves identically in a playground iframe and a real page.
## HTML
```html
<section class="cfa-16" aria-label="Categorized FAQ with sticky sidebar">
  <div class="cfa-16__stage">
    <div class="cfa-16__cols">
      <nav class="cfa-16__side" aria-label="FAQ categories">
        <span class="cfa-16__sidehead">Help center</span>
        <a href="#cfa16-account"><b>Account</b><span>3</span></a>
        <a href="#cfa16-billing"><b>Billing</b><span>2</span></a>
        <a href="#cfa16-privacy"><b>Privacy</b><span>2</span></a>
        <p class="cfa-16__sidenote">Sticky via <code>position: sticky</code> — no JS scroll-spy needed for the jump pattern.</p>
      </nav>
      <div class="cfa-16__main">
        <section class="cfa-16__cat" id="cfa16-account">
          <h2>Account</h2>
          <details class="cfa-16__item" open>
            <summary class="cfa-16__q">How do I change my email address?<i aria-hidden="true"></i></summary>
            <div class="cfa-16__a"><p>Settings → Account → Email. We send a confirmation link to both the old and new address; the change applies when the new one is verified. Login sessions stay active.</p></div>
          </details>
          <details class="cfa-16__item">
            <summary class="cfa-16__q">Can I merge two accounts?<i aria-hidden="true"></i></summary>
            <div class="cfa-16__a"><p>Yes — from the older account, Settings → Advanced → Merge. Projects, history and integrations move over; the source account becomes an alias that still accepts logins for 90 days.</p></div>
          </details>
          <details class="cfa-16__item">
            <summary class="cfa-16__q">How do I delete my account?<i aria-hidden="true"></i></summary>
            <div class="cfa-16__a"><p>Settings → Advanced → Delete. There is a 14-day grace period during which logging back in cancels the deletion; after that everything is purged, including backups, within 30 days.</p></div>
          </details>
        </section>
        <section class="cfa-16__cat" id="cfa16-billing">
          <h2>Billing</h2>
          <details class="cfa-16__item">
            <summary class="cfa-16__q">Where do I find my invoices?<i aria-hidden="true"></i></summary>
            <div class="cfa-16__a"><p>Settings → Billing → History lists every invoice as PDF with your VAT/tax details. Accountants can be added as billing-only members who see nothing else.</p></div>
          </details>
          <details class="cfa-16__item">
            <summary class="cfa-16__q">Why was my card declined?<i aria-hidden="true"></i></summary>
            <div class="cfa-16__a"><p>Nine times out of ten it is a 3-D Secure prompt your bank never delivered. Retry from Billing → Payment method — we trigger a fresh authentication. Failing that, the decline code from your bank tells the real story.</p></div>
          </details>
        </section>
        <section class="cfa-16__cat" id="cfa16-privacy">
          <h2>Privacy</h2>
          <details class="cfa-16__item">
            <summary class="cfa-16__q">Can I export everything you hold on me?<i aria-hidden="true"></i></summary>
            <div class="cfa-16__a"><p>Settings → Privacy → Export builds a machine-readable archive (JSON + attachments) within 24 hours — the full GDPR/CCPA portability package, self-serve.</p></div>
          </details>
          <details class="cfa-16__item">
            <summary class="cfa-16__q">Do you sell or share my data?<i aria-hidden="true"></i></summary>
            <div class="cfa-16__a"><p>No, and the DPA says so contractually. Subprocessors are listed publicly with 30-day change notices; analytics run first-party and cookieless.</p></div>
          </details>
        </section>
        <p class="cfa-16__foot">Delete the stage's <code>overflow-y</code> line and this whole layout runs on document scroll. CodeFronts collection.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.cfa-16,
.cfa-16 *,
.cfa-16 *::before,
.cfa-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-16 {
  --bg: oklch(0.975 0.006 280);
  --panel: oklch(1 0 0);
  --ink: oklch(0.23 0.03 285);
  --mut: oklch(0.5 0.02 282);
  --line: oklch(0.9 0.01 280);
  --acc: oklch(0.55 0.19 295);
  --stick: 24px;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-16__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  scroll-behavior: smooth;
  background: var(--bg);
  container: cfa16/inline-size;
}

.cfa-16__cols {
  display: grid;
  grid-template-columns: 220px minmax(0,1fr);
  gap: clamp(20px,4cqi,48px);
  width: min(100%,900px);
  margin-inline: auto;
  padding: clamp(20px,4vw,48px);
}

.cfa-16__side {
  position: sticky;
  top: var(--stick);
  align-self: start;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.cfa-16__sidehead {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 6px;
}

.cfa-16__side a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 11px;
  font-size: 14px;
  font-weight: 600;
  color: var(--ink);
  text-decoration: none;
  transition: background .2s,color .2s;
}

.cfa-16__side a:hover,
.cfa-16__side a:focus-visible {
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  color: var(--acc);
}

.cfa-16__side a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cfa-16__side a span {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--mut);
  padding: 3px 8px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 99px;
}

.cfa-16__sidenote {
  margin-top: 12px;
  font-size: 11.5px;
  line-height: 1.55;
  color: var(--mut);
  padding: 10px 12px;
  border: 1px dashed var(--line);
  border-radius: 10px;
}

.cfa-16__sidenote code,
.cfa-16__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  color: var(--acc);
}

.cfa-16__cat {
  scroll-margin-top: var(--stick);
}

.cfa-16__cat + .cfa-16__cat {
  margin-top: 34px;
}

.cfa-16__cat h2 {
  font-size: 19px;
  font-weight: 800;
  letter-spacing: -.02em;
  padding-bottom: 10px;
  border-bottom: 2px solid var(--line);
}

.cfa-16__cat:target h2 {
  border-color: var(--acc);
  color: var(--acc);
}

.cfa-16__item {
  margin-top: 10px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 13px;
  interpolate-size: allow-keywords;
  transition: border-color .3s;
}

.cfa-16__item[open] {
  border-color: color-mix(in oklch,var(--acc) 35%,var(--line));
}

.cfa-16__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  min-height: 44px;
  padding: 14px 16px;
  cursor: pointer;
  font-size: 14.5px;
  font-weight: 650;
  list-style: none;
  transition: color .2s;
}

.cfa-16__q::-webkit-details-marker {
  display: none;
}

.cfa-16__q:hover {
  color: var(--acc);
}

.cfa-16__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 13px;
}

.cfa-16__q i {
  flex: none;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s;
}

.cfa-16__item[open] .cfa-16__q i {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-16__a p {
  padding: 0 16px 15px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-16__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .35s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .35s allow-discrete;
  }

  .cfa-16__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-16__foot {
  margin-top: 30px;
  font-size: 12.5px;
  color: var(--mut);
}

@container cfa16 (width < 760px) {
  .cfa-16__cols {
    grid-template-columns: 1fr;
    gap: 18px;
  }

  .cfa-16__side {
    position: sticky;
    top: 0;
    z-index: 5;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    background: color-mix(in oklch,var(--bg) 88%,transparent);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    padding: 10px 0;
    margin: -10px 0;
  }

  .cfa-16__sidehead {
    width: 100%;
    margin: 0 0 4px;
  }

  .cfa-16__sidenote {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cfa-16 *,
    .cfa-16 .cfa-16__item::details-content {
    transition-duration: .01ms !important;
  }

  .cfa-16__stage {
    scroll-behavior: auto;
  }
}
```

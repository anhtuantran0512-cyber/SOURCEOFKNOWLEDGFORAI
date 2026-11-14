---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/developer-portfolio-layout-html-css-single-page/"
title: "Developer Portfolio Layout HTML CSS Single Page"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "The complete single-page engineer portfolio — Hero, Stack, Projects, Contact — in one HTML file with zero dependencies and a weight budget a Lighthouse audit…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Developer Portfolio Layout HTML CSS Single Page
Source: https://codefronts.com/layouts/css-portfolio-layouts/developer-portfolio-layout-html-css-single-page/

The complete single-page engineer portfolio — Hero, Stack, Projects, Contact — in one HTML file with zero dependencies and a weight budget a Lighthouse audit would frame. Navigation is plain anchor links with CSS smooth scrolling and scroll-margin, the stack is a chip cloud, projects are honest cards with metric lines, and the sticky mini-nav shows a scroll-driven reading-progress hairline where supported.
## HTML
```html
<section class="cpl-09" aria-label="Single page developer portfolio demo">
  <div class="cpl-09__page">
    <header class="cpl-09__nav">
      <span class="cpl-09__logo">st<i>.</i></span>
      <nav aria-label="Sections">
        <a href="#cpl09-stack">Stack</a><a href="#cpl09-projects">Projects</a><a href="#cpl09-contact">Contact</a>
      </nav>
      <i class="cpl-09__progress" aria-hidden="true"></i>
    </header>
    <main class="cpl-09__scroll">
      <section class="cpl-09__hero" aria-label="Intro">
        <p class="cpl-09__hi">Hi, I'm</p>
        <h2>Sam Torres</h2>
        <p class="cpl-09__sub">Full-stack engineer. I ship small, fast, boring-in-the-good-way software — mostly TypeScript, mostly for developer tools.</p>
        <div class="cpl-09__cta">
          <a class="cpl-09__btn" href="#cpl09-projects">See projects</a>
          <a class="cpl-09__ghost" href="#resume">Résumé ↗</a>
        </div>
      </section>
      <section id="cpl09-stack" aria-labelledby="cpl09-stack-h">
        <h3 id="cpl09-stack-h"><i>01</i>Stack</h3>
        <ul class="cpl-09__chips">
          <li>TypeScript</li><li>Node</li><li>Rust</li><li>PostgreSQL</li><li>React</li><li>Vite</li><li>Playwright</li><li>Terraform</li><li>Grafana</li>
        </ul>
      </section>
      <section id="cpl09-projects" aria-labelledby="cpl09-proj-h">
        <h3 id="cpl09-proj-h"><i>02</i>Projects</h3>
        <div class="cpl-09__projects">
          <a class="cpl-09__proj" href="#quickdiff">
            <h4>quickdiff</h4>
            <p>Structural diffs for JSON APIs in CI. p95 review time on schema PRs down 60%.</p>
            <span><i>Rust</i><i>2.1k ★</i></span>
          </a>
          <a class="cpl-09__proj" href="#coldstart">
            <h4>coldstart.dev</h4>
            <p>Benchmark harness for serverless cold starts across 5 clouds — cited by two vendor docs.</p>
            <span><i>TypeScript</i><i>weekly cron</i></span>
          </a>
          <a class="cpl-09__proj" href="#shelf">
            <h4>shelf</h4>
            <p>Self-hosted read-later that renders everything to plain HTML. 14KB client, zero build step.</p>
            <span><i>Node</i><i>self-hosted</i></span>
          </a>
          <a class="cpl-09__proj" href="#atlasui">
            <h4>atlas-ui (day job)</h4>
            <p>Design-system infra at Atlas: token pipeline + 40 components. p95 render 210ms → 90ms.</p>
            <span><i>React</i><i>design systems</i></span>
          </a>
        </div>
      </section>
      <section id="cpl09-contact" aria-labelledby="cpl09-contact-h">
        <h3 id="cpl09-contact-h"><i>03</i>Contact</h3>
        <p class="cpl-09__mail">One inbox, answered daily: <a href="#email">[email protected]</a></p>
        <p class="cpl-09__fine">GitHub · Bluesky · RSS — no newsletters, no chatbots.</p>
      </section>
    </main>
  </div>
</section>
```
## CSS
```css
.cpl-09,
.cpl-09 *,
.cpl-09 *::before,
.cpl-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-09 {
  --bg: oklch(0.18 0.015 260);
  --card: oklch(0.23 0.018 260);
  --ink: oklch(0.94 0.008 250);
  --mut: oklch(0.64 0.015 260);
  --line: oklch(0.3 0.02 260);
  --acc: oklch(0.8 0.15 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-09__page {
  position: relative;
  width: 100%;
  height: 100vh;
  height: 100svh;
  background: var(--bg);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.cpl-09__nav {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  min-height: 56px;
  border-bottom: 1px solid var(--line);
  background: color-mix(in oklch,var(--bg) 88%,transparent);
  backdrop-filter: blur(8px);
}

.cpl-09__logo {
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.02em;
}

.cpl-09__logo i {
  font-style: normal;
  color: var(--acc);
}

.cpl-09__nav nav {
  display: flex;
  gap: 2px;
}

.cpl-09__nav nav a {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 12px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  color: var(--mut);
  transition: color .2s,background .2s;
}

.cpl-09__nav nav a:hover,
.cpl-09__nav nav a:focus-visible {
  color: var(--ink);
  background: oklch(1 0 0/.06);
}

.cpl-09__nav nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cpl-09__progress {
  position: absolute;
  left: 0;
  bottom: -1px;
  height: 2px;
  width: 100%;
  background: var(--acc);
  transform-origin: left;
  transform: scaleX(0);
  display: none;
}

.cpl-09__scroll {
  flex: 1;
  overflow-y: auto;
  scroll-behavior: smooth;
  padding: 0 clamp(20px,4cqi,34px) 34px;
  scroll-timeline: --cpl09 y;
}

@supports (animation-timeline: scroll()) {
  .cpl-09__progress {
    display: block;
    animation: cpl09-read linear both;
    animation-timeline: --cpl09;
  }

  @keyframes cpl09-read {
    from {
      transform: scaleX(0);
    }

    to {
      transform: scaleX(1);
    }
  }
}

.cpl-09__scroll section {
  scroll-margin-top: 16px;
  padding-top: 34px;
}

.cpl-09__hero {
  padding-top: 44px !important;
  min-height: 300px;
  display: grid;
  align-content: center;
  gap: 8px;
}

.cpl-09__hi {
  font-size: 14px;
  color: var(--acc);
  font-weight: 700;
}

.cpl-09__hero h2 {
  font-size: clamp(30px,6cqi,46px);
  letter-spacing: -.03em;
  line-height: 1.02;
}

.cpl-09__sub {
  font-size: 14.5px;
  line-height: 1.65;
  color: var(--mut);
  max-width: 46ch;
  margin-top: 6px;
}

.cpl-09__cta {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 16px;
}

.cpl-09__btn {
  display: inline-grid;
  place-items: center;
  min-height: 42px;
  padding: 0 18px;
  border-radius: 10px;
  font-size: 13.5px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.16 0.02 260);
  background: var(--acc);
  transition: background .2s,translate .2s;
}

.cpl-09__btn:hover,
.cpl-09__btn:focus-visible {
  background: oklch(0.86 0.15 155);
  translate: 0 -2px;
}

.cpl-09__ghost {
  display: inline-grid;
  place-items: center;
  min-height: 42px;
  padding: 0 16px;
  border-radius: 10px;
  font-size: 13.5px;
  font-weight: 600;
  text-decoration: none;
  color: var(--ink);
  border: 1px solid var(--line);
  transition: border-color .2s,background .2s;
}

.cpl-09__ghost:hover,
.cpl-09__ghost:focus-visible {
  border-color: var(--acc);
  background: oklch(1 0 0/.04);
}

.cpl-09__btn:focus-visible,
.cpl-09__ghost:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-09__scroll h3 {
  display: flex;
  align-items: baseline;
  gap: 10px;
  font-size: 19px;
  letter-spacing: -.015em;
  margin-bottom: 16px;
}

.cpl-09__scroll h3 i {
  font-style: normal;
  font-size: 12px;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
}

.cpl-09__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  list-style: none;
}

.cpl-09__chips li {
  padding: 8px 14px;
  border-radius: 99px;
  font-size: 12.5px;
  font-weight: 600;
  border: 1px solid var(--line);
  color: var(--mut);
  transition: color .2s,border-color .2s;
  cursor: default;
}

.cpl-09__chips li:hover {
  color: var(--ink);
  border-color: var(--acc);
}

.cpl-09__projects {
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fill,minmax(min(260px,100%),1fr));
}

.cpl-09__proj {
  display: grid;
  gap: 7px;
  align-content: start;
  padding: 18px;
  border-radius: 14px;
  background: var(--card);
  border: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
  transition: border-color .25s,translate .25s cubic-bezier(.2,.7,.2,1);
}

.cpl-09__proj:hover,
.cpl-09__proj:focus-visible {
  border-color: color-mix(in oklch,var(--acc) 50%,var(--line));
  translate: 0 -3px;
}

.cpl-09__proj:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-09__proj h4 {
  font-size: 15px;
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  letter-spacing: -.01em;
}

.cpl-09__proj p {
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--mut);
}

.cpl-09__proj span {
  display: flex;
  gap: 6px;
  margin-top: 4px;
}

.cpl-09__proj span i {
  font-style: normal;
  font-size: 10.5px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 99px;
  background: oklch(1 0 0/.06);
  color: var(--mut);
}

.cpl-09__mail {
  font-size: 15px;
}

.cpl-09__mail a {
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: 4px;
  font-weight: 700;
}

.cpl-09__mail a:hover,
.cpl-09__mail a:focus-visible {
  color: oklch(0.88 0.13 155);
}

.cpl-09__mail a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.cpl-09__fine {
  margin-top: 8px;
  font-size: 12px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cpl-09__scroll {
    scroll-behavior: auto;
  }

  .cpl-09 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

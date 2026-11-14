---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-section-headers-list/"
title: "CSS Sticky Section Headers List"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The iOS-contacts pattern: alphabetical group headers that pin to the top of the list, then get pushed out by the next arriving header — that satisfying shove…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Section Headers List
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-section-headers-list/

The iOS-contacts pattern: alphabetical group headers that pin to the top of the list, then get pushed out by the next arriving header — that satisfying shove is not an animation, it's the containing block doing its job. Each header is sticky inside its own <section>, so its leash ends exactly where the next group begins. A directory app shell with a letter rail, all CSS, zero scroll listeners.
## HTML
```html
<section class="cst-07" aria-label="Sticky section headers list demo">
  <div class="cst-07__stage">
    <header class="cst-07__bar">
      <h1>Directory</h1>
      <label class="cst-07__search"><span class="cst-07__vh">Search people</span><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="9" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="m13.5 13.5 4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><input type="search" placeholder="Search 23 people…"></label>
    </header>
    <div class="cst-07__body">
      <div class="cst-07__list" id="cst07-list" tabindex="0">
        <section class="cst-07__group" id="cst07-A"><h3>A</h3><ul>
          <li><i style="--h:280">AB</i><div><strong>Amara Bailey</strong><span>Product design · Sydney</span></div><a href="#cst07-A" aria-label="Call Amara Bailey">+61 2 5550 114</a></li>
          <li><i style="--h:180">AO</i><div><strong>Arthur Okonkwo</strong><span>Platform eng · London</span></div><a href="#cst07-A" aria-label="Call Arthur Okonkwo">+44 20 5550 883</a></li>
          <li><i style="--h:60">AS</i><div><strong>Astrid Solheim</strong><span>Research · remote</span></div><a href="#cst07-A" aria-label="Call Astrid Solheim">+1 604 555 0192</a></li>
        </ul></section>
        <section class="cst-07__group" id="cst07-B"><h3>B</h3><ul>
          <li><i style="--h:330">BC</i><div><strong>Bea Castellanos</strong><span>Brand · Austin</span></div><a href="#cst07-B" aria-label="Call Bea Castellanos">+1 512 555 0147</a></li>
          <li><i style="--h:220">BN</i><div><strong>Bodhi Ngata</strong><span>Mobile eng · Auckland</span></div><a href="#cst07-B" aria-label="Call Bodhi Ngata">+64 9 555 0173</a></li>
        </ul></section>
        <section class="cst-07__group" id="cst07-C"><h3>C</h3><ul>
          <li><i style="--h:120">CD</i><div><strong>Callum Doyle</strong><span>Support lead · Dublin</span></div><a href="#cst07-C" aria-label="Call Callum Doyle">+353 1 555 0128</a></li>
          <li><i style="--h:20">CF</i><div><strong>Cleo Fontaine</strong><span>Content · Montréal</span></div><a href="#cst07-C" aria-label="Call Cleo Fontaine">+1 514 555 0136</a></li>
          <li><i style="--h:260">CW</i><div><strong>Casey Wu</strong><span>Data science · Seattle</span></div><a href="#cst07-C" aria-label="Call Casey Wu">+1 206 555 0161</a></li>
        </ul></section>
        <section class="cst-07__group" id="cst07-H"><h3>H</h3><ul>
          <li><i style="--h:200">HK</i><div><strong>Hana Kobayashi</strong><span>Design systems · Vancouver</span></div><a href="#cst07-H" aria-label="Call Hana Kobayashi">+1 604 555 0175</a></li>
          <li><i style="--h:300">HP</i><div><strong>Hugh Prescott</strong><span>Finance · Edinburgh</span></div><a href="#cst07-H" aria-label="Call Hugh Prescott">+44 131 555 0119</a></li>
        </ul></section>
        <section class="cst-07__group" id="cst07-J"><h3>J</h3><ul>
          <li><i style="--h:90">JM</i><div><strong>Jonas Meyer</strong><span>Security · Berlin</span></div><a href="#cst07-J" aria-label="Call Jonas Meyer">+49 30 5550 0142</a></li>
          <li><i style="--h:350">JT</i><div><strong>Jaya Thakur</strong><span>PM, payments · Toronto</span></div><a href="#cst07-J" aria-label="Call Jaya Thakur">+1 416 555 0187</a></li>
          <li><i style="--h:150">JW</i><div><strong>Jesse Whitehorse</strong><span>QA · Phoenix</span></div><a href="#cst07-J" aria-label="Call Jesse Whitehorse">+1 602 555 0158</a></li>
        </ul></section>
        <section class="cst-07__group" id="cst07-M"><h3>M</h3><ul>
          <li><i style="--h:240">MA</i><div><strong>Miriam Abebe</strong><span>Engineering manager · NYC</span></div><a href="#cst07-M" aria-label="Call Miriam Abebe">+1 212 555 0139</a></li>
          <li><i style="--h:40">MF</i><div><strong>Marco Ferrari</strong><span>iOS · Melbourne</span></div><a href="#cst07-M" aria-label="Call Marco Ferrari">+61 3 5550 168</a></li>
        </ul></section>
        <section class="cst-07__group" id="cst07-R"><h3>R</h3><ul>
          <li><i style="--h:310">RC</i><div><strong>Rhiannon Carey</strong><span>Legal · Cardiff</span></div><a href="#cst07-R" aria-label="Call Rhiannon Carey">+44 29 5550 122</a></li>
          <li><i style="--h:170">RS</i><div><strong>Rafael Santos</strong><span>SRE · Lisbon</span></div><a href="#cst07-R" aria-label="Call Rafael Santos">+351 21 555 0176</a></li>
          <li><i style="--h:70">RV</i><div><strong>Ruby Vance</strong><span>Marketing · Chicago</span></div><a href="#cst07-R" aria-label="Call Ruby Vance">+1 312 555 0114</a></li>
        </ul></section>
        <section class="cst-07__group" id="cst07-S"><h3>S</h3><ul>
          <li><i style="--h:130">SB</i><div><strong>Saoirse Byrne</strong><span>Customer research · Galway</span></div><a href="#cst07-S" aria-label="Call Saoirse Byrne">+353 91 555 0151</a></li>
          <li><i style="--h:290">SO</i><div><strong>Sam Osei</strong><span>Growth · London</span></div><a href="#cst07-S" aria-label="Call Sam Osei">+44 20 5550 199</a></li>
        </ul></section>
        <section class="cst-07__group" id="cst07-T"><h3>T</h3><ul>
          <li><i style="--h:210">TH</i><div><strong>Tove Hansen</strong><span>Ops · Copenhagen</span></div><a href="#cst07-T" aria-label="Call Tove Hansen">+45 33 555 0184</a></li>
          <li><i style="--h:10">TN</i><div><strong>Tāne Ngata</strong><span>Partnerships · Wellington</span></div><a href="#cst07-T" aria-label="Call Tāne Ngata">+64 4 555 0129</a></li>
        </ul></section>
        <section class="cst-07__group" id="cst07-W"><h3>W</h3><ul>
          <li><i style="--h:100">WF</i><div><strong>Willa Fitzgerald</strong><span>People · Denver</span></div><a href="#cst07-W" aria-label="Call Willa Fitzgerald">+1 303 555 0146</a></li>
          <li><i style="--h:250">WT</i><div><strong>Wes Tanaka</strong><span>Video · Los Angeles</span></div><a href="#cst07-W" aria-label="Call Wes Tanaka">+1 213 555 0171</a></li>
        </ul></section>
        <p class="cst-07__end">23 people · headers above are <code>position: sticky; top: 0</code>, each caged by its own section</p>
      </div>
      <nav class="cst-07__rail" aria-label="Jump to letter">
        <a href="#cst07-A">A</a><a href="#cst07-B">B</a><a href="#cst07-C">C</a><a href="#cst07-H">H</a><a href="#cst07-J">J</a><a href="#cst07-M">M</a><a href="#cst07-R">R</a><a href="#cst07-S">S</a><a href="#cst07-T">T</a><a href="#cst07-W">W</a>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.cst-07,
.cst-07 *,
.cst-07 *::before,
.cst-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-07 {
  --bg: oklch(0.97 0.005 260);
  --pane: oklch(1 0 0);
  --ink: oklch(0.23 0.015 260);
  --mut: oklch(0.53 0.012 260);
  --line: oklch(0.915 0.006 260);
  --acc: oklch(0.58 0.17 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-07__stage {
  width: 100%;
  container: cst07/inline-size;
  height: 100vh;
  height: 100svh;
  display: flex;
  flex-direction: column;
  background: var(--bg);
}

.cst-07__bar {
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 16px clamp(16px,3.5cqi,32px) 14px;
}

.cst-07__bar h1 {
  font-size: clamp(22px,3.4cqi,30px);
  letter-spacing: -.03em;
  font-weight: 800;
}

.cst-07__search {
  display: flex;
  align-items: center;
  gap: 9px;
  flex: 0 1 340px;
  margin-left: auto;
  min-height: 42px;
  padding: 0 14px;
  border-radius: 12px;
  background: var(--pane);
  border: 1.5px solid var(--line);
  color: var(--mut);
  transition: border-color .2s,box-shadow .2s;
}

.cst-07__search:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 3px oklch(0.58 0.17 260/.15);
  color: var(--ink);
}

.cst-07__search input {
  flex: 1;
  min-width: 0;
  border: none;
  background: none;
  font: inherit;
  font-size: 13.5px;
  color: var(--ink);
  outline: none;
}

.cst-07__search input::placeholder {
  color: oklch(0.66 0.01 260);
}

.cst-07__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.cst-07__body {
  flex: 1;
  min-height: 0;
  display: flex;
  gap: 4px;
  padding: 0 clamp(10px,2.5cqi,26px) clamp(12px,2.5cqi,22px);
}

.cst-07__list {
  flex: 1;
  min-width: 0;
  overflow-y: auto;
  border-radius: 18px;
  background: var(--pane);
  border: 1px solid var(--line);
  scrollbar-width: thin;
  scroll-behavior: smooth;
}

.cst-07__list:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cst-07__group h3 {
  position: sticky;
  top: -1px;
  z-index: 2;
  display: flex;
  align-items: center;
  min-height: 34px;
  padding: 1px 18px 0;
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: .1em;
  color: var(--acc);
  background: color-mix(in oklch,var(--pane) 82%,transparent);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--line);
}

.cst-07__group {
  scroll-margin-top: 0;
}

.cst-07__group ul {
  list-style: none;
}

.cst-07__group li {
  display: flex;
  align-items: center;
  gap: 13px;
  min-height: 60px;
  padding: 8px 18px;
  border-bottom: 1px solid color-mix(in oklch,var(--line) 55%,transparent);
  transition: background .15s;
}

.cst-07__group li:hover {
  background: oklch(0.975 0.005 260);
}

.cst-07__group li:last-child {
  border-bottom: none;
}

.cst-07__group i {
  flex: none;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-style: normal;
  font-size: 12.5px;
  font-weight: 800;
  color: oklch(0.99 0 0);
  background: linear-gradient(140deg,oklch(0.68 0.14 var(--h,260)),oklch(0.5 0.15 calc(var(--h,260) + 40)));
}

.cst-07__group strong {
  display: block;
  font-size: 14.5px;
  letter-spacing: -.005em;
}

.cst-07__group span {
  font-size: 12px;
  color: var(--mut);
}

.cst-07__group li a {
  margin-left: auto;
  flex: none;
  display: grid;
  place-items: center;
  min-height: 36px;
  padding: 0 12px;
  border-radius: 9px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.cst-07__group li a:hover,
.cst-07__group li a:focus-visible {
  color: var(--acc);
  background: oklch(0.93 0.02 260/.6);
}

.cst-07__group li a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-07__end {
  padding: 18px;
  font-size: 12px;
  color: var(--mut);
  text-align: center;
}

.cst-07__end code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .92em;
  background: oklch(0.94 0.008 260);
  padding: 1px 5px;
  border-radius: 4px;
}

.cst-07__rail {
  flex: none;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 1px;
  padding: 6px 2px;
}

.cst-07__rail a {
  display: grid;
  place-items: center;
  width: 26px;
  min-height: 26px;
  border-radius: 7px;
  font-size: 10.5px;
  font-weight: 800;
  color: var(--mut);
  text-decoration: none;
  transition: color .15s,background .15s,scale .15s;
}

.cst-07__rail a:hover,
.cst-07__rail a:focus-visible {
  color: oklch(0.99 0 0);
  background: var(--acc);
  scale: 1.15;
}

.cst-07__rail a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@container cst07 (width < 480px) {
  .cst-07__bar {
    flex-wrap: wrap;
    gap: 10px;
  }

  .cst-07__search {
    flex-basis: 100%;
  }

  .cst-07__group li a {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-07__list {
    scroll-behavior: auto;
  }

  .cst-07 * {
    transition-duration: .01ms !important;
    scale: none !important;
  }
}
```

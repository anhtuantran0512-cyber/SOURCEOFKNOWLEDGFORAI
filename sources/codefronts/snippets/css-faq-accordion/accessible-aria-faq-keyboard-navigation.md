---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/accessible-aria-faq-keyboard-navigation/"
title: "Accessible ARIA FAQ Keyboard Navigation"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "The WAI-ARIA Authoring Practices accordion, implemented exactly: real heading elements wrapping real buttons with aria-expanded and aria-controls, labelled…"
has_js: "true"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible ARIA FAQ Keyboard Navigation
Source: https://codefronts.com/snippets/css-faq-accordion/accessible-aria-faq-keyboard-navigation/

The WAI-ARIA Authoring Practices accordion, implemented exactly: real heading elements wrapping real buttons with aria-expanded and aria-controls, labelled regions for the panels, and the full keyboard layer — Arrow Up/Down cycles between headers, Home/End jump to first/last, Enter/Space toggle. This is the pattern for when you need button semantics and heading structure rather than details/summary (which covers simpler cases natively) — with the tutorial explaining exactly when each is the right call, and a visible keymap in the demo itself.
## HTML
```html
<section class="cfa-21" aria-label="Accessible ARIA FAQ accordion">
  <div class="cfa-21__wrap">
    <header class="cfa-21__head">
      <h1>Accessibility statement FAQ</h1>
      <p>The WAI-ARIA accordion pattern, to the letter. Put focus in the list and drive it from the keyboard:</p>
      <ul class="cfa-21__keys" aria-label="Keyboard commands">
        <li><kbd>↑</kbd><kbd>↓</kbd> move between questions</li>
        <li><kbd>Home</kbd><kbd>End</kbd> first / last</li>
        <li><kbd>Enter</kbd><kbd>Space</kbd> toggle</li>
      </ul>
    </header>
    <div class="cfa-21__list" id="cfa21-list">
      <div class="cfa-21__item">
        <h3 class="cfa-21__h"><button type="button" class="cfa-21__q" id="cfa21-h1" aria-expanded="true" aria-controls="cfa21-p1">Why buttons inside headings?<span class="cfa-21__chev" aria-hidden="true"></span></button></h3>
        <div class="cfa-21__a" role="region" id="cfa21-p1" aria-labelledby="cfa21-h1"><div><p>Screen-reader users navigate by headings more than any other structure — the h3 puts each question in the document outline. The button inside it carries the interaction and announces “collapsed” or “expanded” from its <code>aria-expanded</code> attribute, which this CSS also styles from, so what is announced and what is shown can never disagree.</p></div></div>
      </div>
      <div class="cfa-21__item">
        <h3 class="cfa-21__h"><button type="button" class="cfa-21__q" id="cfa21-h2" aria-expanded="false" aria-controls="cfa21-p2">When is details/summary enough?<span class="cfa-21__chev" aria-hidden="true"></span></button></h3>
        <div class="cfa-21__a" role="region" id="cfa21-p2" aria-labelledby="cfa21-h2"><div><p>Most of the time. A marketing FAQ with a handful of questions is perfectly served by native disclosure — it is keyboard-operable and announced correctly with zero script. Reach for this ARIA pattern when audits require heading navigation, aria-controls relationships, or APG-spec arrow-key traversal.</p></div></div>
      </div>
      <div class="cfa-21__item">
        <h3 class="cfa-21__h"><button type="button" class="cfa-21__q" id="cfa21-h3" aria-expanded="false" aria-controls="cfa21-p3">Why don't arrow keys open panels?<span class="cfa-21__chev" aria-hidden="true"></span></button></h3>
        <div class="cfa-21__a" role="region" id="cfa21-p3" aria-labelledby="cfa21-h3"><div><p>Browsing and activating are separate acts. Arrow keys let a screen-reader user survey all questions quickly; Enter or Space commits to one. A widget that opens panels while you are merely looking around announces a wall of content you never asked for.</p></div></div>
      </div>
      <div class="cfa-21__item">
        <h3 class="cfa-21__h"><button type="button" class="cfa-21__q" id="cfa21-h4" aria-expanded="false" aria-controls="cfa21-p4">What does role="region" add?<span class="cfa-21__chev" aria-hidden="true"></span></button></h3>
        <div class="cfa-21__a" role="region" id="cfa21-p4" aria-labelledby="cfa21-h4"><div><p>A labelled landmark: from deep inside a long answer, AT users can query their location and hear the question it belongs to. Use it judiciously — past six or so panels, keep <code>aria-labelledby</code> but drop the role to avoid flooding the landmark rotor.</p></div></div>
      </div>
    </div>
    <p class="cfa-21__foot">Markup: h3 &gt; button[aria-expanded][aria-controls] + region[aria-labelledby]. The audit-grade accordion. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-21,
.cfa-21 *,
.cfa-21 *::before,
.cfa-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-21 {
  --bg: oklch(0.15 0.015 265);
  --panel: oklch(0.2 0.02 265);
  --ink: oklch(0.96 0.005 260);
  --mut: oklch(0.7 0.015 262);
  --line: oklch(0.31 0.025 264);
  --acc: oklch(0.82 0.16 95);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-21__wrap {
  width: min(100%,680px);
}

.cfa-21__head h1 {
  font-size: clamp(26px,4.5cqi,38px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-21__head p {
  margin-top: 8px;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--mut);
}

.cfa-21__keys {
  margin-top: 14px;
  display: flex;
  flex-wrap: wrap;
  gap: 8px 20px;
  list-style: none;
}

.cfa-21__keys li {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12.5px;
  color: var(--mut);
}

.cfa-21__keys kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  font-weight: 700;
  min-width: 24px;
  text-align: center;
  padding: 3px 7px;
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 6px;
  background: var(--panel);
  color: var(--acc);
}

.cfa-21__list {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.cfa-21__item {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--panel);
  overflow: hidden;
  transition: border-color .3s;
}

.cfa-21__item:has([aria-expanded="true"]) {
  border-color: color-mix(in oklch,var(--acc) 45%,var(--line));
}

.cfa-21__h {
  font-size: inherit;
  font-weight: inherit;
}

.cfa-21__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  width: 100%;
  min-height: 48px;
  padding: 16px 18px;
  background: none;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: 15.5px;
  font-weight: 650;
  letter-spacing: -.01em;
  color: var(--ink);
  text-align: left;
  transition: color .2s;
}

.cfa-21__q:hover {
  color: var(--acc);
}

.cfa-21__q:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: -3px;
  border-radius: 14px;
}

.cfa-21__chev {
  flex: none;
  width: 9px;
  height: 9px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s cubic-bezier(.4,0,.2,1);
}

.cfa-21__q[aria-expanded="true"] .cfa-21__chev {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-21__a {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .4s cubic-bezier(.4,0,.2,1);
}

.cfa-21__a>div {
  overflow: hidden;
  min-height: 0;
}

.cfa-21__a p {
  padding: 0 18px 17px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 62ch;
}

.cfa-21__a code,
.cfa-21__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: oklch(0.27 0.022 264);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.cfa-21__item:has([aria-expanded="true"]) .cfa-21__a {
  grid-template-rows: 1fr;
}

.cfa-21__foot {
  margin-top: 22px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-21 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.cfa-21');if(!root||root.dataset.cfa21)return;root.dataset.cfa21='1';
  var btns=[].slice.call(root.querySelectorAll('.cfa-21__q'));
  btns.forEach(function(btn,i){
    btn.addEventListener('click',function(){
      btn.setAttribute('aria-expanded',btn.getAttribute('aria-expanded')!=='true');
    });
    btn.addEventListener('keydown',function(e){
      var next=null;
      if(e.key==='ArrowDown')next=(i+1)%btns.length;
      else if(e.key==='ArrowUp')next=(i-1+btns.length)%btns.length;
      else if(e.key==='Home')next=0;
      else if(e.key==='End')next=btns.length-1;
      if(next!==null){e.preventDefault();btns[next].focus();}
    });
  });
})();
```

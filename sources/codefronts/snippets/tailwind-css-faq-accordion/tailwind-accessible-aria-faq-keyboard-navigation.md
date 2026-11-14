---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-accessible-aria-faq-keyboard-navigation/"
title: "Tailwind Accessible ARIA FAQ Accordion with Keyboard Navigation"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "The WAI-ARIA Authoring Practices accordion, implemented exactly: real headings wrapping real buttons with aria-expanded and aria-controls, labelled regions…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accessible ARIA FAQ Accordion with Keyboard Navigation
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-accessible-aria-faq-keyboard-navigation/

The WAI-ARIA Authoring Practices accordion, implemented exactly: real headings wrapping real buttons with aria-expanded and aria-controls, labelled regions for the panels, and the full keyboard layer — arrows cycle between headers, Home/End jump to the ends, Enter/Space toggle. The port's best property is that every visual state keys off the accessibility attribute, so what is announced and what is shown cannot drift apart.
## HTML
```html
<section class="tfa-21 w-full min-h-svh grid place-items-center bg-tfa21-bg font-tfa21-sans text-tfa21-ink px-5 py-12">
  <div class="w-[min(700px,100%)]">
    <header>
      <h1 class="text-[clamp(28px,5vw,40px)] font-extrabold leading-[1.08] tracking-[-0.025em]">Accessibility statement FAQ</h1>
      <p class="mt-3 max-w-[56ch] text-[15px] leading-relaxed text-tfa21-mut">The WAI-ARIA accordion pattern, to the letter. Put focus in the list and drive it from the keyboard:</p>
      <ul aria-label="Keyboard commands" class="mt-4 flex list-none flex-wrap gap-x-5 gap-y-2">
        <li class="flex items-center gap-1.5 text-[12.5px] text-tfa21-mut"><kbd class="min-w-6 rounded-md border border-b-2 border-tfa21-edge bg-tfa21-panel px-1.5 py-0.5 text-center font-tfa21-mono text-[11px] font-bold text-tfa21-acc">↑</kbd><kbd class="min-w-6 rounded-md border border-b-2 border-tfa21-edge bg-tfa21-panel px-1.5 py-0.5 text-center font-tfa21-mono text-[11px] font-bold text-tfa21-acc">↓</kbd>move between questions</li>
        <li class="flex items-center gap-1.5 text-[12.5px] text-tfa21-mut"><kbd class="rounded-md border border-b-2 border-tfa21-edge bg-tfa21-panel px-1.5 py-0.5 font-tfa21-mono text-[11px] font-bold text-tfa21-acc">Home</kbd><kbd class="rounded-md border border-b-2 border-tfa21-edge bg-tfa21-panel px-1.5 py-0.5 font-tfa21-mono text-[11px] font-bold text-tfa21-acc">End</kbd>first / last</li>
        <li class="flex items-center gap-1.5 text-[12.5px] text-tfa21-mut"><kbd class="rounded-md border border-b-2 border-tfa21-edge bg-tfa21-panel px-1.5 py-0.5 font-tfa21-mono text-[11px] font-bold text-tfa21-acc">Enter</kbd><kbd class="rounded-md border border-b-2 border-tfa21-edge bg-tfa21-panel px-1.5 py-0.5 font-tfa21-mono text-[11px] font-bold text-tfa21-acc">Space</kbd>toggle</li>
      </ul>
    </header>

    <div id="tfa21-list" class="mt-7 flex flex-col gap-2.5">
      <div class="rounded-2xl border border-tfa21-edge bg-tfa21-panel overflow-hidden transition-[border-color,box-shadow] duration-300 has-[[aria-expanded=true]]:border-tfa21-accedge has-[[aria-expanded=true]]:shadow-[0_16px_38px_-24px_oklch(0.82_0.16_95/0.4)]">
        <h3 class="text-base font-normal">
          <button type="button" id="tfa21-h1" aria-expanded="true" aria-controls="tfa21-p1" class="group flex min-h-12 w-full cursor-pointer items-center justify-between gap-4 border-0 bg-transparent px-5 py-4 text-left font-tfa21-sans text-[15.5px] font-semibold tracking-[-0.01em] text-tfa21-ink transition-colors duration-200 hover:text-tfa21-acc focus-visible:rounded-2xl focus-visible:outline-3 focus-visible:-outline-offset-[3px] focus-visible:outline-tfa21-acc">Why buttons inside headings?
            <span aria-hidden="true" class="size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa21-acc transition-[rotate,translate] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-aria-expanded:translate-y-0.5 group-aria-expanded:rotate-[225deg] motion-reduce:transition-none"></span>
          </button>
        </h3>
        <div role="region" id="tfa21-p1" aria-labelledby="tfa21-h1" class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[62ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa21-mut">Screen-reader users navigate by headings more than any other structure — the heading puts each question in the document outline. The button inside it carries the interaction and announces collapsed or expanded from its <code class="rounded bg-tfa21-tint px-1.5 py-0.5 font-tfa21-mono text-[0.88em] text-tfa21-acc">aria-expanded</code> attribute, which these utilities also style from, so what is announced and what is shown can never disagree.</p></div>
        </div>
      </div>
      <div class="rounded-2xl border border-tfa21-edge bg-tfa21-panel overflow-hidden transition-[border-color,box-shadow] duration-300 has-[[aria-expanded=true]]:border-tfa21-accedge has-[[aria-expanded=true]]:shadow-[0_16px_38px_-24px_oklch(0.82_0.16_95/0.4)]">
        <h3 class="text-base font-normal">
          <button type="button" id="tfa21-h2" aria-expanded="false" aria-controls="tfa21-p2" class="group flex min-h-12 w-full cursor-pointer items-center justify-between gap-4 border-0 bg-transparent px-5 py-4 text-left font-tfa21-sans text-[15.5px] font-semibold tracking-[-0.01em] text-tfa21-ink transition-colors duration-200 hover:text-tfa21-acc focus-visible:rounded-2xl focus-visible:outline-3 focus-visible:-outline-offset-[3px] focus-visible:outline-tfa21-acc">When is details/summary enough?
            <span aria-hidden="true" class="size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa21-acc transition-[rotate,translate] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-aria-expanded:translate-y-0.5 group-aria-expanded:rotate-[225deg] motion-reduce:transition-none"></span>
          </button>
        </h3>
        <div role="region" id="tfa21-p2" aria-labelledby="tfa21-h2" class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[62ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa21-mut">Most of the time. A marketing FAQ with a handful of questions is perfectly served by native disclosure — keyboard-operable and announced correctly with zero script. Reach for this ARIA pattern when audits require heading navigation, <code class="rounded bg-tfa21-tint px-1.5 py-0.5 font-tfa21-mono text-[0.88em] text-tfa21-acc">aria-controls</code> relationships, or spec arrow-key traversal.</p></div>
        </div>
      </div>
      <div class="rounded-2xl border border-tfa21-edge bg-tfa21-panel overflow-hidden transition-[border-color,box-shadow] duration-300 has-[[aria-expanded=true]]:border-tfa21-accedge has-[[aria-expanded=true]]:shadow-[0_16px_38px_-24px_oklch(0.82_0.16_95/0.4)]">
        <h3 class="text-base font-normal">
          <button type="button" id="tfa21-h3" aria-expanded="false" aria-controls="tfa21-p3" class="group flex min-h-12 w-full cursor-pointer items-center justify-between gap-4 border-0 bg-transparent px-5 py-4 text-left font-tfa21-sans text-[15.5px] font-semibold tracking-[-0.01em] text-tfa21-ink transition-colors duration-200 hover:text-tfa21-acc focus-visible:rounded-2xl focus-visible:outline-3 focus-visible:-outline-offset-[3px] focus-visible:outline-tfa21-acc">Why do arrow keys not open panels?
            <span aria-hidden="true" class="size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa21-acc transition-[rotate,translate] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-aria-expanded:translate-y-0.5 group-aria-expanded:rotate-[225deg] motion-reduce:transition-none"></span>
          </button>
        </h3>
        <div role="region" id="tfa21-p3" aria-labelledby="tfa21-h3" class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[62ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa21-mut">Browsing and activating are separate acts. Arrow keys let a screen-reader user survey all questions quickly; Enter or Space commits to one. A widget that opens panels while you are merely looking around announces a wall of content you never asked for.</p></div>
        </div>
      </div>
      <div class="rounded-2xl border border-tfa21-edge bg-tfa21-panel overflow-hidden transition-[border-color,box-shadow] duration-300 has-[[aria-expanded=true]]:border-tfa21-accedge has-[[aria-expanded=true]]:shadow-[0_16px_38px_-24px_oklch(0.82_0.16_95/0.4)]">
        <h3 class="text-base font-normal">
          <button type="button" id="tfa21-h4" aria-expanded="false" aria-controls="tfa21-p4" class="group flex min-h-12 w-full cursor-pointer items-center justify-between gap-4 border-0 bg-transparent px-5 py-4 text-left font-tfa21-sans text-[15.5px] font-semibold tracking-[-0.01em] text-tfa21-ink transition-colors duration-200 hover:text-tfa21-acc focus-visible:rounded-2xl focus-visible:outline-3 focus-visible:-outline-offset-[3px] focus-visible:outline-tfa21-acc">What does role=region add?
            <span aria-hidden="true" class="size-2.5 shrink-0 -translate-y-0.5 rotate-45 border-b-2 border-r-2 border-tfa21-acc transition-[rotate,translate] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] group-aria-expanded:translate-y-0.5 group-aria-expanded:rotate-[225deg] motion-reduce:transition-none"></span>
          </button>
        </h3>
        <div role="region" id="tfa21-p4" aria-labelledby="tfa21-h4" class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="max-w-[62ch] px-5 pb-4 text-[14px] leading-[1.7] text-tfa21-mut">A labelled landmark: from deep inside a long answer, AT users can query their location and hear the question it belongs to. Use it judiciously — past six or so panels, keep <code class="rounded bg-tfa21-tint px-1.5 py-0.5 font-tfa21-mono text-[0.88em] text-tfa21-acc">aria-labelledby</code> but drop the role to avoid flooding the landmark rotor.</p></div>
        </div>
      </div>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa21-mut">Markup: heading &gt; button[aria-expanded][aria-controls] plus region[aria-labelledby]. The audit-grade accordion.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa21-bg: #1a1c22;
  --color-tfa21-bg: oklch(0.2 0.015 265);
  --color-tfa21-panel: #23262e;
  --color-tfa21-panel: oklch(0.24 0.02 265);
  --color-tfa21-ink: #f3f4f7;
  --color-tfa21-ink: oklch(0.96 0.005 260);
  --color-tfa21-mut: #b8bcc6;
  --color-tfa21-mut: oklch(0.8 0.013 262);
  --color-tfa21-edge: #383c46;
  --color-tfa21-edge: oklch(0.34 0.025 264);
  --color-tfa21-accedge: #8f8552;
  --color-tfa21-accedge: oklch(0.6 0.09 95);
  --color-tfa21-tint: #3a3520;
  --color-tfa21-tint: oklch(0.3 0.05 95);
  --color-tfa21-acc: #e8cd5f;
  --color-tfa21-acc: oklch(0.86 0.15 95);
  --font-tfa21-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tfa21-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfa-21 {
  width: 100%;
  min-height: 100svh;
}
/* One selector utilities cannot express: the panel's open state is driven by its BUTTON's
   aria-expanded, which lives on a previous sibling's descendant. */

.tfa-21 h3:has([aria-expanded="true"]) + [role="region"] {
  grid-template-rows: 1fr;
}
```

## JavaScript
```js
(function(){
  var root=document.querySelector('.tfa-21');if(!root||root.dataset.tfa21)return;root.dataset.tfa21='1';
  var btns=[].slice.call(root.querySelectorAll('#tfa21-list button[aria-expanded]'));
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

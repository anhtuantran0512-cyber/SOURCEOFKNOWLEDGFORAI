---
source: "lucianlabs"
id: "048"
title: "Swipe-linked underline tabs"
category: "Menus & Tabs"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#048"
tags: ["tabs", "swipe", "underline", "scroll-linked", "overflow"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Swipe-linked underline tabs (048, Menus & Tabs)
[What it does] Swipe the articles sideways and the underline stretches along with your finger to the next tab. The chosen tab scrolls to the center, and both ends of the tab row fade to hint there is more.
[How to use it] Drag or swipe the article card sideways, or press the tabs above. With a keyboard, use the left and right arrows on the tabs

Please add the UI element below to my project.

[Check first]
1. Find out the project’s framework (React, Next, Vue, Svelte, plain HTML, etc.), styling approach (CSS modules, Tailwind, global CSS) and existing theming approach (data-theme, a dark class, CSS variables).
2. Locate the file and any existing element at the insertion point first, and report where that element is used.

[How to apply]
3. Add it as a new component at the insertion point. If there is a replacement target, replace that element with the one below.
4. Keep existing data, props, event handlers, form values and accessibility attributes (labels, aria, keyboard support) as they are.
5. Port the structure, shapes and motion values (durations, curves, delays) of the code below as they are. Convert it into components and state for the framework, but do not guess a new design.
6. Map the --ux-* color tokens below to the project’s existing theme variables. Keep both the light and dark values and check both themes.
7. Keep styles inside this element’s class (.uNNN) and do not change global CSS or global scripts. Make sure the class names do not clash with existing ones.
8. Replace the sample copy and sample data with the project’s real data. Do not bring over gallery-only screens or demo code. Keep the one-line license comment at the top of the new component file.
9. Check that the feature and its final states still work with prefers-reduced-motion turned on.

[Report when done]
10. List the files you changed, behavior that differs from the old element, what you checked (both themes, mobile width, keyboard) and anything you could not check.

[Insertion point] Write the page or component name here
[Replacement target] Write the file path or component name of the existing element, or "none"

--- Code start (this whole code is the working original) ---
<!-- Lucian UX/UI Prompt #048 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#048 -->
<style>
/* lucianLabs UI 요소 — 공통 테마 토큰 (라이트 / 다크)
   라이트 기본값 → 시스템이 다크면 다크 → data-theme으로 명시하면 그 값을 우선합니다.
   요소 CSS는 --ux-* 토큰만 참조하므로, 프로젝트 테마 변수에 이 값을 매핑하면 됩니다. */
:root{
  color-scheme:light;
  --ux-page:#F4F2EE;
  --ux-surface:#FFFFFF;
  --ux-surface-2:#F5F3EF;
  --ux-surface-3:#EAE7E1;
  --ux-ink:#16151B;
  --ux-ink-2:#57535F;
  --ux-ink-3:#8E8A97;
  --ux-line:rgba(22,21,27,.09);
  --ux-line-2:rgba(22,21,27,.17);
  --ux-accent:#6A57F2;
  --ux-accent-2:#2F8FE0;
  --ux-accent-soft:rgba(106,87,242,.12);
  --ux-accent-ink:#FFFFFF;
  --ux-mint:#119C72;
  --ux-warn:#D6731E;
  --ux-danger:#D93A55;
  --ux-glass:rgba(255,255,255,.58);
  --ux-glass-line:rgba(255,255,255,.85);
  --ux-shadow:rgba(40,30,80,.14);
  --ux-shadow-strong:rgba(40,30,80,.3);
  --ux-grad:linear-gradient(120deg,#7B61FF,#3D8BFF 55%,#1FB89A);
  --ux-ease:cubic-bezier(.2,.8,.2,1);
  --ux-spring:cubic-bezier(.34,1.45,.64,1);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    color-scheme:dark;
    --ux-page:#07080D;
    --ux-surface:#13141C;
    --ux-surface-2:#1A1B25;
    --ux-surface-3:#252632;
    --ux-ink:#F4F0E8;
    --ux-ink-2:rgba(244,240,232,.68);
    --ux-ink-3:rgba(244,240,232,.42);
    --ux-line:rgba(255,255,255,.08);
    --ux-line-2:rgba(255,255,255,.16);
    --ux-accent:#B7A4FF;
    --ux-accent-2:#7DB4FF;
    --ux-accent-soft:rgba(183,164,255,.15);
    --ux-accent-ink:#0B0C12;
    --ux-mint:#7EE8C0;
    --ux-warn:#FFB26B;
    --ux-danger:#FF7D8C;
    --ux-glass:rgba(255,255,255,.07);
    --ux-glass-line:rgba(255,255,255,.18);
    --ux-shadow:rgba(0,0,0,.45);
    --ux-shadow-strong:rgba(0,0,0,.72);
    --ux-grad:linear-gradient(120deg,#B7A4FF,#7DB4FF 55%,#A5F2D3);
  }
}
:root[data-theme="dark"]{
  color-scheme:dark;
  --ux-page:#07080D;
  --ux-surface:#13141C;
  --ux-surface-2:#1A1B25;
  --ux-surface-3:#252632;
  --ux-ink:#F4F0E8;
  --ux-ink-2:rgba(244,240,232,.68);
  --ux-ink-3:rgba(244,240,232,.42);
  --ux-line:rgba(255,255,255,.08);
  --ux-line-2:rgba(255,255,255,.16);
  --ux-accent:#B7A4FF;
  --ux-accent-2:#7DB4FF;
  --ux-accent-soft:rgba(183,164,255,.15);
  --ux-accent-ink:#0B0C12;
  --ux-mint:#7EE8C0;
  --ux-warn:#FFB26B;
  --ux-danger:#FF7D8C;
  --ux-glass:rgba(255,255,255,.07);
  --ux-glass-line:rgba(255,255,255,.18);
  --ux-shadow:rgba(0,0,0,.45);
  --ux-shadow-strong:rgba(0,0,0,.72);
  --ux-grad:linear-gradient(120deg,#B7A4FF,#7DB4FF 55%,#A5F2D3);
}
/* 요소 공통 베이스 — 루트에 .ux 클래스를 붙입니다 */
.ux,.ux *,.ux *::before,.ux *::after{box-sizing:border-box}
.ux{
  font-family:"Pretendard Variable",Pretendard,-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Segoe UI",Roboto,"Noto Sans KR",sans-serif;
  color:var(--ux-ink);-webkit-font-smoothing:antialiased;letter-spacing:-.01em;
  -webkit-tap-highlight-color:transparent;
  word-break:keep-all;overflow-wrap:break-word;
}
/* :where()로 명시도를 0으로 둬서, 요소 클래스가 버튼·입력의 색과 글꼴을 덮어쓸 수 있게 합니다 */
:where(.ux) :is(button,input,textarea,select){font:inherit;color:inherit}
:where(.ux) button{cursor:pointer}
.ux :focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
.ux [hidden]{display:none!important}
/* 모션 줄이기: 전환은 즉시 끝나고, 무한 반복은 한 번으로 줄여 최종 상태가 보이게 합니다 */
@media (prefers-reduced-motion:reduce){
  .ux,.ux *,.ux *::before,.ux *::after{
    animation-duration:.001ms!important;animation-iteration-count:1!important;
    transition-duration:.001ms!important;scroll-behavior:auto!important;
  }
}
</style>

<style>
.u048{position:relative;width:350px;height:420px;display:flex;flex-direction:column;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -38px var(--ux-shadow-strong);overflow:hidden}
.u048-top{display:flex;align-items:center;justify-content:space-between;padding:18px 20px 6px}
.u048-top b{font-size:21px;font-weight:800;letter-spacing:-.04em}
.u048-top small{font-size:12px;font-weight:700;color:var(--ux-ink-3)}
.u048-tw{position:relative;border-bottom:1px solid var(--ux-line)}
.u048-tw::before,.u048-tw::after{content:"";position:absolute;top:0;bottom:0;width:36px;z-index:1;pointer-events:none;transition:opacity .3s}
.u048-tw::before{left:0;background:linear-gradient(90deg,var(--ux-surface),transparent);opacity:var(--fl,0)}
.u048-tw::after{right:0;background:linear-gradient(-90deg,var(--ux-surface),transparent);opacity:var(--fr,1)}
.u048-tabs{position:relative;display:flex;gap:4px;padding:0 14px;overflow-x:auto;scrollbar-width:none}
.u048-tabs::-webkit-scrollbar{display:none}
.u048-tab{position:relative;flex:none;height:46px;padding:0 10px;border:0;background:none;font-size:15px;font-weight:700;letter-spacing:-.02em;color:var(--ux-ink-3);white-space:nowrap;transition:color .3s}
.u048-tab:hover{color:var(--ux-ink-2)}
.u048-tab[aria-selected="true"]{color:var(--ux-ink)}
.u048-tab:focus-visible{outline:2px solid var(--ux-accent);outline-offset:-6px;border-radius:12px}
.u048-line{position:absolute;left:0;bottom:0;width:40px;height:3px;border-radius:3px 3px 0 0;background:var(--ux-grad);pointer-events:none}
.u048-pages{flex:1;display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;overscroll-behavior-x:contain;cursor:grab;touch-action:pan-x pan-y}
.u048-pages::-webkit-scrollbar{display:none}
.u048-pages.drag{cursor:grabbing;scroll-snap-type:none;user-select:none}
.u048-pg{flex:none;width:100%;padding:14px 16px 16px;scroll-snap-align:start;display:flex;flex-direction:column;gap:10px}
.u048-hero{position:relative;flex:none;height:170px;border-radius:20px;overflow:hidden;background:var(--g);padding:16px;display:flex;flex-direction:column;justify-content:flex-end;color:#fff}
.u048-hero::before{content:"";position:absolute;width:180px;height:180px;right:-50px;top:-70px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.5),transparent 65%)}
.u048-hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(10,8,25,.45))}
.u048-hero small{position:relative;z-index:1;font-size:11px;font-weight:800;letter-spacing:.08em;opacity:.85}
.u048-hero b{position:relative;z-index:1;margin-top:4px;font-size:18px;line-height:1.3;font-weight:800;letter-spacing:-.035em}
.u048-it{display:flex;align-items:center;gap:12px}
.u048-it i{width:48px;height:48px;flex:none;border-radius:13px;background:var(--g);opacity:.85}
.u048-it span{font-size:14px;font-weight:650;line-height:1.35;letter-spacing:-.02em}
.u048-it small{display:block;margin-top:2px;font-size:11.5px;font-weight:600;color:var(--ux-ink-3)}
</style>
<div class="ux u048">
  <div class="u048-top"><b>Today’s reads</b><small>October 10</small></div>
  <div class="u048-tw"><div class="u048-tabs" role="tablist" aria-label="Topics"><span class="u048-line" aria-hidden="true"></span></div></div>
  <div class="u048-pages" tabindex="-1"></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var bar = root.querySelector('.u048-tabs'), line = root.querySelector('.u048-line'), pages = root.querySelector('.u048-pages');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var D = [
    ['For you', 'linear-gradient(140deg,#7B61FF,#3D8BFF)', 'Why slower teams go further', ['Teams that dropped morning meetings', 'How to protect focus time']],
    ['Economy', 'linear-gradient(140deg,#22C3A6,#0E7490)', 'Rates are on hold. What’s the next signal?', ['Grocery shopping on a weak won', 'Three things to do on payday']],
    ['Tech', 'linear-gradient(140deg,#3D8BFF,#B04FD0)', 'Why screenless devices are rising', ['Why voice assistants are back', 'Settings that save battery']],
    ['Design', 'linear-gradient(140deg,#FF6B8B,#FFB547)', 'Roomier screens read faster', ['A brand in three colors', 'What makes a good button']],
    ['Travel', 'linear-gradient(140deg,#0EA5E9,#22C3A6)', 'Five islands for autumn walks', ['Solo train journeys', 'How to pack half as much']],
    ['Food', 'linear-gradient(140deg,#FF7A45,#E5484D)', 'Why the corner bakery opens at 4 a.m.', ['Soup with in-season radish', 'Foolproof pot rice']],
    ['Culture', 'linear-gradient(140deg,#8B6CFF,#FF6B8B)', 'Six small shows this weekend', ['Classic novels, reread', 'Films worth a theater trip']]
  ];
  var uid = 'u048-' + Math.random().toString(36).slice(2, 7);
  D.forEach(function (d, i) {
    var t = document.createElement('button');
    t.className = 'u048-tab'; t.type = 'button'; t.setAttribute('role', 'tab');
    t.id = uid + '-t' + i; t.setAttribute('aria-controls', uid + '-p' + i);
    t.textContent = d[0];
    bar.insertBefore(t, line);
    var p = document.createElement('section');
    p.className = 'u048-pg'; p.id = uid + '-p' + i; p.setAttribute('role', 'tabpanel'); p.setAttribute('aria-labelledby', t.id);
    p.style.setProperty('--g', d[1]);
    p.innerHTML = '<div class="u048-hero"><small>' + d[0] + ' · 5 min</small><b>' + d[2] + '</b></div>' + d[3].map(function (x, k) { return '<div class="u048-it"><i aria-hidden="true" style="filter:hue-rotate(' + (k * 25 + 15) + 'deg)"></i><span>' + x + '<small>' + (k + 3) + ' min read</small></span></div>'; }).join('');
    pages.appendChild(p);
  });
  var tabs = Array.prototype.slice.call(bar.querySelectorAll('.u048-tab'));
  var panels = Array.prototype.slice.call(pages.children);
  var act = -1;
  function sync() {
    var w = pages.clientWidth || 1, f = Math.max(0, Math.min(tabs.length - 1, pages.scrollLeft / w));
    var i = Math.floor(f), t = f - i, a = tabs[i], b = tabs[Math.min(i + 1, tabs.length - 1)];
    var l = a.offsetLeft + (b.offsetLeft - a.offsetLeft) * t + 10;
    var wd = (a.offsetWidth + (b.offsetWidth - a.offsetWidth) * t) - 20 + Math.sin(t * Math.PI) * 26;
    line.style.transform = 'translateX(' + (l - Math.sin(t * Math.PI) * 6).toFixed(1) + 'px)';
    line.style.width = wd.toFixed(1) + 'px';
    var n = Math.round(f);
    if (n !== act) select(n);
  }
  function select(n) {
    act = n;
    tabs.forEach(function (t, k) { t.setAttribute('aria-selected', String(k === n)); t.tabIndex = k === n ? 0 : -1; });
    panels.forEach(function (p, k) { p.inert = k !== n; });
    var t = tabs[n];
    bar.scrollTo({ left: t.offsetLeft - (bar.clientWidth - t.offsetWidth) / 2, behavior: rm ? 'auto' : 'smooth' });
  }
  function edges() {
    var max = bar.scrollWidth - bar.clientWidth;
    bar.parentNode.style.setProperty('--fl', bar.scrollLeft > 4 ? '1' : '0');
    bar.parentNode.style.setProperty('--fr', bar.scrollLeft < max - 4 ? '1' : '0');
  }
  function goTo(i, focus) {
    i = Math.max(0, Math.min(tabs.length - 1, i));
    if (focus) tabs[i].focus({ preventScroll: true });
    pages.scrollTo({ left: i * pages.clientWidth, behavior: rm ? 'auto' : 'smooth' });
  }
  pages.addEventListener('scroll', sync, { passive: true });
  bar.addEventListener('scroll', edges, { passive: true });
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { goTo(i); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (e.key === 'Home') d = -i; else if (e.key === 'End') d = tabs.length - 1 - i;
      if (d) { e.preventDefault(); goTo(i + d, true); }
    });
  });
  var sx = 0, sl = 0, v = 0, lx = 0, dragging = false;
  pages.addEventListener('pointerdown', function (e) {
    if (e.pointerType !== 'mouse' || e.button !== 0) return;
    dragging = true; sx = lx = e.clientX; sl = pages.scrollLeft; v = 0;
    pages.classList.add('drag');
    pages.setPointerCapture(e.pointerId);
  });
  pages.addEventListener('pointermove', function (e) {
    if (!dragging) return;
    v = e.clientX - lx; lx = e.clientX;
    pages.scrollLeft = sl - (e.clientX - sx);
  });
  function end() {
    if (!dragging) return;
    dragging = false;
    var w = pages.clientWidth, f = pages.scrollLeft / w;
    var n = Math.abs(v) > 4 ? (v < 0 ? Math.ceil(f) : Math.floor(f)) : Math.round(f);
    goTo(n);
    var done = function () { pages.removeEventListener('scrollend', done); clearTimeout(tm); if (!dragging) pages.classList.remove('drag'); };
    var tm = setTimeout(done, 700);
    pages.addEventListener('scrollend', done);
  }
  pages.addEventListener('pointerup', end);
  pages.addEventListener('pointercancel', end);
  sync(); edges();
  if (window.ResizeObserver) new ResizeObserver(function () { pages.scrollLeft = act * pages.clientWidth; sync(); edges(); }).observe(pages);
})();
</script>
--- Code end ---

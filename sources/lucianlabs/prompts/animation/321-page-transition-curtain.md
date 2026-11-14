---
source: "lucianlabs"
id: "321"
title: "Curtain page transition"
category: "Navigation"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#321"
tags: ["page-transition", "navigation", "curtain", "route", "website"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Curtain page transition (321, Navigation)
[What it does] Press another page in the site's top menu and a colored curtain rises from the bottom to cover the screen, the destination page's name briefly appears on it, then the curtain lifts away to reveal the new page. The new page's title and image rise one after another as the curtain clears, and the menu's current-location marker slides over too.
[How to use it] Press a different page in the top menu

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
<!-- Lucian UX/UI Prompt #321 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#321 -->
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
.u321{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:#FBF7F2;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:#22201C}
.u321-nv{position:absolute;left:18px;right:18px;top:16px;z-index:4;display:flex;align-items:center}
.u321-nv b{margin-right:auto;font-size:13px;font-weight:900;letter-spacing:-.02em}
.u321-ls{position:relative;display:flex;gap:2px;padding:3px;border-radius:999px;background:rgba(34,32,28,.06)}
.u321-mk{position:absolute;top:3px;bottom:3px;border-radius:999px;background:#22201C;transition:left .45s cubic-bezier(.3,1.3,.5,1),width .45s cubic-bezier(.3,1.3,.5,1)}
.u321-ln{position:relative;border:0;padding:5px 11px;border-radius:999px;background:none;color:#5E5850;font:inherit;font-size:11px;font-weight:800;cursor:pointer;transition:color .3s}
.u321-ln.is-on{color:#FBF7F2}
.u321-ln:focus-visible{outline:2px solid #E2725B;outline-offset:2px}
.u321-pg{position:absolute;inset:0;padding:66px 18px 18px}
.u321-pg small{font-size:10px;font-weight:850;letter-spacing:.08em;color:#E2725B}
.u321-pg h3{margin:6px 0 0;font-size:26px;line-height:1.14;font-weight:900;letter-spacing:-.045em}
.u321-im{position:absolute;left:18px;right:18px;bottom:18px;height:118px;border-radius:16px}
.u321-pg [data-s]{transition:opacity .5s,transform .7s cubic-bezier(.2,.8,.2,1);transition-delay:var(--d)}
.u321.is-hide .u321-pg [data-s]{opacity:0;transform:translateY(18px);transition:none}
.u321-cu{position:absolute;inset:0;z-index:3;background:#E2725B;transform:translateY(101%);display:grid;place-items:center;color:#FBF7F2;font-size:30px;font-weight:900;letter-spacing:-.04em;pointer-events:none}
.u321-cu span{opacity:0;transform:translateY(10px);transition:opacity .3s,transform .4s}
.u321.is-cover .u321-cu{transform:none;transition:transform .5s cubic-bezier(.7,0,.2,1)}
.u321.is-cover .u321-cu span{opacity:1;transform:none;transition-delay:.25s}
.u321.is-lift .u321-cu{transform:translateY(-101%);transition:transform .55s cubic-bezier(.7,0,.2,1)}
@media (prefers-reduced-motion: reduce){.u321-cu{display:none}.u321-pg [data-s]{transition:none}}
</style>
<div class="ux u321">
  <div class="u321-nv"><b>Maison</b><div class="u321-ls" role="navigation" aria-label="Site menu"><span class="u321-mk" aria-hidden="true"></span></div></div>
  <div class="u321-pg" aria-live="polite"><small data-s style="--d:.05s"></small><h3 data-s style="--d:.12s"></h3><div class="u321-im" data-s style="--d:.22s" aria-hidden="true"></div></div>
  <div class="u321-cu" aria-hidden="true"><span></span></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ls = root.querySelector('.u321-ls'), mk = root.querySelector('.u321-mk'), sm = root.querySelector('.u321-pg small'), h = root.querySelector('.u321-pg h3'), im = root.querySelector('.u321-im'), cu = root.querySelector('.u321-cu span');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var PG = [['Home', 'How to use good<br>things for longer', 'Living magazine'], ['Work', 'Twelve things<br>we made this year', 'Portfolio'], ['About', 'A small team<br>making slowly', 'About the studio']];
  var IMG = ['linear-gradient(135deg,#F1D3B3,#C98F6A)', 'linear-gradient(135deg,#B9D4C8,#4F7F6B)', 'linear-gradient(135deg,#D6D0F0,#7C6FB8)'];
  var cur = -1, busy = false, L = [];
  PG.forEach(function (p, i) { var b = document.createElement('button'); b.type = 'button'; b.className = 'u321-ln'; b.textContent = p[0]; b.addEventListener('click', function () { go(i); }); ls.appendChild(b); L.push(b); });
  function mark(i) { L.forEach(function (b, k) { b.classList.toggle('is-on', k === i); if (k === i) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current'); }); mk.style.left = L[i].offsetLeft + 'px'; mk.style.width = L[i].offsetWidth + 'px'; }
  function show(i) { sm.textContent = PG[i][2]; h.innerHTML = PG[i][1]; im.style.background = IMG[i]; }
  function go(i) {
    if (i === cur || busy) return;
    mark(i); cur = i;
    if (rm) { show(i); return; }
    busy = true; cu.textContent = PG[i][0];
    root.classList.remove('is-lift'); root.classList.add('is-cover');
    setTimeout(function () {
      show(i); root.classList.add('is-hide');
      setTimeout(function () {
        root.classList.remove('is-cover'); root.classList.add('is-lift');
        requestAnimationFrame(function () { root.classList.remove('is-hide'); });
        setTimeout(function () { root.classList.remove('is-lift'); busy = false; }, 600);
      }, 380);
    }, 520);
  }
  mark(0); cur = 0; show(0);
})();
</script>
--- Code end ---

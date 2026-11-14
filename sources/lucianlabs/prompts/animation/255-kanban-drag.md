---
source: "lucianlabs"
id: "255"
title: "Drag-to-move kanban cards"
category: "App Screens"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#255"
tags: ["kanban", "drag-and-drop", "board", "tasks", "productivity"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Drag-to-move kanban cards (255, App Screens)
[What it does] A task board with To do, In progress and Done columns. Pick up a card and it tilts slightly and lifts; drag it over another column and a gap opens where it will land as the cards below shift down. Drop it and the card settles into the gap while each column's count updates, and cards dropped in Done get a check and a line through their title.
[How to use it] Pick up a card and drop it in another column

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
<!-- Lucian UX/UI Prompt #255 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#255 -->
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
.u255{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface-2);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink);touch-action:none;user-select:none}
.u255-bd{position:absolute;inset:14px;display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.u255-col{position:relative;padding:8px 6px;border-radius:16px;background:color-mix(in srgb,var(--ux-surface) 55%,transparent);box-shadow:inset 0 0 0 1px var(--ux-line);transition:background .2s,box-shadow .2s}
.u255-col.is-over{background:color-mix(in srgb,var(--ux-accent) 9%,var(--ux-surface));box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--ux-accent) 45%,transparent)}
.u255-ch{display:flex;align-items:center;gap:5px;padding:2px 4px 8px;font-size:10.5px;font-weight:850;color:var(--ux-ink-2)}
.u255-ch i{width:7px;height:7px;border-radius:50%}
.u255-ch b{margin-left:auto;min-width:16px;height:16px;padding:0 4px;border-radius:8px;background:var(--ux-surface);font-size:9.5px;font-weight:850;line-height:16px;text-align:center;font-variant-numeric:tabular-nums;box-sizing:border-box}
.u255-ch b.is-pop{animation:u255-pop .4s cubic-bezier(.3,1.7,.5,1)}
@keyframes u255-pop{40%{transform:scale(1.35)}}
.u255-cd{position:relative;margin-bottom:6px;padding:8px;border-radius:11px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 2px 4px -2px var(--ux-shadow-strong);cursor:grab;transition:box-shadow .2s,transform .2s}
.u255-cd:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u255-cd b{display:block;font-size:10.5px;line-height:1.35;font-weight:800;text-decoration-thickness:1.5px;text-decoration-color:var(--ux-ink-3)}
.u255-cd span{display:inline-block;margin-top:6px;padding:1px 6px;border-radius:999px;font-size:8.5px;font-weight:850;color:#fff}
.u255-cd em{position:absolute;right:7px;bottom:7px;width:16px;height:16px;border-radius:50%;background:#10B981;transform:scale(0);transition:transform .35s cubic-bezier(.3,1.7,.5,1)}
.u255-cd em::after{content:"";position:absolute;left:5.5px;top:3px;width:3.5px;height:7px;border:solid #fff;border-width:0 1.6px 1.6px 0;transform:rotate(45deg)}
.u255-col[data-c="2"] .u255-cd b{text-decoration-line:line-through;color:var(--ux-ink-3)}
.u255-col[data-c="2"] .u255-cd em{transform:none}
.u255-cd.is-lift{position:absolute;z-index:10;margin:0;cursor:grabbing;transform:rotate(3deg) scale(1.04);box-shadow:0 0 0 1px var(--ux-line),0 18px 30px -12px var(--ux-shadow-strong);transition:transform .2s,box-shadow .2s}
.u255-cd.is-land{position:absolute;z-index:10;margin:0;transition:left .28s cubic-bezier(.3,1.2,.5,1),top .28s cubic-bezier(.3,1.2,.5,1),transform .28s}
.u255-ph{margin-bottom:6px;border-radius:11px;border:1.5px dashed color-mix(in srgb,var(--ux-accent) 50%,transparent);background:color-mix(in srgb,var(--ux-accent) 6%,transparent);transition:height .2s cubic-bezier(.3,1.2,.5,1)}
@media (prefers-reduced-motion: reduce){.u255-cd,.u255-cd.is-land,.u255-ph,.u255-cd em{transition:none}.u255-ch b.is-pop{animation:none}}
</style>
<div class="ux u255"><div class="u255-bd"></div></div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var bd = root.querySelector('.u255-bd');
  var COL = ['To do', 'In progress', 'Done'], CC = ['#94A3B8', '#6366F1', '#10B981'];
  var CD = [[0, 'Pricing page draft', 'Design', '#EC4899'], [0, 'Onboarding email copy', 'Marketing', '#F59E0B'], [0, 'Checkout error logs', 'Dev', '#0EA5E9'], [1, 'Landing hero', 'Design', '#EC4899'], [1, 'Speed up the API', 'Dev', '#0EA5E9'], [2, 'Connect domain', 'Dev', '#0EA5E9']];
  var cols = COL.map(function (n, i) {
    var c = document.createElement('div'); c.className = 'u255-col'; c.dataset.c = i; c.setAttribute('role', 'list'); c.setAttribute('aria-label', n);
    c.innerHTML = '<div class="u255-ch"><i style="background:' + CC[i] + '"></i><span></span><b></b></div>'; c.querySelector('span').textContent = n;
    bd.appendChild(c); return c;
  });
  function counts(pop) { cols.forEach(function (c, i) { var b = c.querySelector('b'), n = c.querySelectorAll('.u255-cd:not(.is-lift):not(.is-land)').length + (c.querySelector('.u255-ph') ? 1 : 0); if (b.textContent != n && pop && pop.indexOf(i) >= 0) { b.classList.remove('is-pop'); void b.offsetWidth; b.classList.add('is-pop'); } b.textContent = n; }); }
  CD.forEach(function (d) {
    var e = document.createElement('div'); e.className = 'u255-cd'; e.tabIndex = 0; e.setAttribute('role', 'listitem');
    e.innerHTML = '<b></b><span style="background:' + d[3] + '"></span><em aria-hidden="true"></em>'; e.querySelector('b').textContent = d[1]; e.querySelector('span').textContent = d[2];
    cols[d[0]].appendChild(e); bind(e);
  });
  counts();
  function k() { return root.offsetWidth / (root.getBoundingClientRect().width || 1); }
  function local(x, y) { var r = root.getBoundingClientRect(), s = k(); return { x: (x - r.left) * s, y: (y - r.top) * s }; }
  var drag = null;
  function bind(e) {
    e.addEventListener('pointerdown', function (ev) {
      if (drag) return;
      var s = k(), r = e.getBoundingClientRect(), p = local(ev.clientX, ev.clientY), at = local(r.left, r.top);
      var ph = document.createElement('div'); ph.className = 'u255-ph'; ph.style.height = (r.height * s) + 'px';
      e.parentNode.insertBefore(ph, e);
      drag = { e: e, ph: ph, dx: p.x - at.x, dy: p.y - at.y, from: +e.parentNode.dataset.c, w: r.width * s };
      e.style.width = drag.w + 'px'; e.style.left = at.x + 'px'; e.style.top = at.y + 'px'; e.classList.add('is-lift'); root.appendChild(e);
      try { e.setPointerCapture(ev.pointerId); } catch (er) {}
      ev.preventDefault();
    });
    e.addEventListener('pointermove', function (ev) {
      if (!drag || drag.e !== e) return;
      var p = local(ev.clientX, ev.clientY);
      e.style.left = (p.x - drag.dx) + 'px'; e.style.top = (p.y - drag.dy) + 'px';
      var col = null; cols.forEach(function (c) { var r = c.getBoundingClientRect(); if (ev.clientX >= r.left && ev.clientX <= r.right) col = c; });
      cols.forEach(function (c) { c.classList.toggle('is-over', c === col && +c.dataset.c !== drag.from); });
      if (!col) return;
      var list = Array.prototype.filter.call(col.querySelectorAll('.u255-cd'), function (c) { return c !== e; }), before = null;
      for (var i = 0; i < list.length; i++) { var r = list[i].getBoundingClientRect(); if (ev.clientY < r.top + r.height / 2) { before = list[i]; break; } }
      if (before) { if (drag.ph.nextSibling !== before) col.insertBefore(drag.ph, before); } else if (drag.ph.parentNode !== col || drag.ph.nextSibling) col.appendChild(drag.ph);
      counts();
    });
    function up() {
      if (!drag || drag.e !== e) return;
      var d = drag; drag = null;
      var s = k(), r = d.ph.getBoundingClientRect(), at = local(r.left, r.top);
      e.classList.remove('is-lift'); e.classList.add('is-land'); e.style.left = at.x + 'px'; e.style.top = at.y + 'px';
      cols.forEach(function (c) { c.classList.remove('is-over'); });
      setTimeout(function () { d.ph.parentNode.insertBefore(e, d.ph); d.ph.remove(); e.classList.remove('is-land'); e.style.cssText = ''; counts([d.from, +e.parentNode.dataset.c]); }, 290);
    }
    e.addEventListener('pointerup', up); e.addEventListener('pointercancel', up);
    e.addEventListener('keydown', function (ev) {
      var dir = ev.key === 'ArrowRight' ? 1 : ev.key === 'ArrowLeft' ? -1 : 0, c = +e.parentNode.dataset.c, to = c + dir;
      if (!dir || to < 0 || to > 2) return;
      ev.preventDefault(); var h = cols[to].querySelector('.u255-ch'); cols[to].insertBefore(e, h.nextSibling); e.focus(); counts([c, to]);
    });
  }
})();
</script>
--- Code end ---

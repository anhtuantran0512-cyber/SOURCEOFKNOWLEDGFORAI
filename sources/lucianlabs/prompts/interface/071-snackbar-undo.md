---
source: "lucianlabs"
id: "071"
title: "Swipe-to-delete with undo"
category: "Alerts & Feedback"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#071"
tags: ["snackbar", "undo", "swipe-to-delete", "countdown", "list"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Swipe-to-delete with undo (071, Alerts & Feedback)
[What it does] Swipe an email left to reveal the red layer behind it as the trash icon grows; swipe far enough and the row folds away. A snackbar rises with a ring counting down, and Undo unfolds the deleted rows back into place.
[How to use it] Drag a row left to delete it, or hover a row and press the trash icon. Delete a few, then press Undo to bring them all back. With a keyboard, press Delete on a row

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
<!-- Lucian UX/UI Prompt #071 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#071 -->
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
.u071{position:relative;width:340px;height:470px;border-radius:30px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u071-head{display:flex;align-items:baseline;justify-content:space-between;padding:20px 20px 8px}
.u071-head b{font-size:21px;font-weight:850;letter-spacing:-.045em}
.u071-head small{font-size:12.5px;font-weight:700;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u071-list{margin:0;padding:0 10px;list-style:none}
.u071-it{display:grid;grid-template-rows:1fr;transition:grid-template-rows .4s var(--ux-ease),opacity .3s}
.u071-it.gone{grid-template-rows:0fr;opacity:0}
.u071-it>div{position:relative;min-height:0;overflow:hidden;border-radius:16px}
.u071-bg{position:absolute;inset:6px 4px;border-radius:12px;background:var(--ux-danger);display:flex;align-items:center;justify-content:flex-end;padding-right:22px;color:#fff}
.u071-bg svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;transform:scale(var(--k,.6));transition:transform .2s}
.u071-row{position:relative;display:flex;align-items:center;gap:12px;height:76px;padding:0 10px;border-radius:16px;background:var(--ux-surface);outline:none;transform:translateX(var(--x,0px));transition:transform .45s var(--ux-spring),background-color .2s;touch-action:pan-y;user-select:none;-webkit-user-select:none}
.u071-row.drag{transition:none}
.u071-row:hover{background:var(--ux-surface-2)}
.u071-row:focus-visible{box-shadow:inset 0 0 0 2px var(--ux-accent)}
.u071-av{width:42px;height:42px;flex:none;border-radius:50%;display:grid;place-items:center;background:var(--g);color:#fff;font-size:15px;font-weight:800}
.u071-tx{flex:1;min-width:0}
.u071-tx b{display:flex;justify-content:space-between;font-size:14.5px;font-weight:780;letter-spacing:-.02em}
.u071-tx b small{font-size:11.5px;font-weight:650;color:var(--ux-ink-3)}
.u071-tx span{display:block;margin-top:3px;font-size:12.5px;font-weight:600;color:var(--ux-ink-3);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.u071-tx b small{transition:opacity .2s}
.u071-row:hover .u071-tx b small,.u071-row:focus-within .u071-tx b small{opacity:0}
.u071-del{position:absolute;right:10px;top:50%;width:36px;height:36px;margin-top:-18px;border:0;padding:0;border-radius:11px;display:grid;place-items:center;background:var(--ux-surface);color:var(--ux-danger);box-shadow:0 0 0 1px var(--ux-line);opacity:0;transform:scale(.8);transition:opacity .2s,transform .3s var(--ux-spring)}
.u071-row:hover .u071-del,.u071-row:focus-within .u071-del{opacity:1;transform:none}
.u071-del:focus-visible{outline:2px solid var(--ux-accent);outline-offset:1px;opacity:1}
.u071-del svg{width:17px;height:17px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
@media (hover:none){.u071-del{display:none}}
.u071-empty{padding:40px 0;text-align:center;font-size:13.5px;font-weight:650;color:var(--ux-ink-3);display:none}
.u071.is-empty .u071-empty{display:block}
.u071-snack{position:absolute;left:12px;right:12px;bottom:12px;display:flex;align-items:center;gap:10px;height:58px;padding:0 8px 0 16px;border-radius:18px;background:var(--ux-ink);color:var(--ux-page);box-shadow:0 18px 30px -16px var(--ux-shadow-strong);transform:translateY(130%);transition:transform .5s var(--ux-spring)}
.u071.is-snack .u071-snack{transform:none}
.u071-snack p{flex:1;margin:0;font-size:13.5px;font-weight:700}
.u071-snack p b{display:inline-block;min-width:1ch;font-variant-numeric:tabular-nums}
.u071-undo{height:40px;padding:0 10px 0 6px;border:0;border-radius:12px;display:inline-flex;align-items:center;gap:8px;background:none;color:var(--ux-accent-2);font-size:14px;font-weight:800}
.u071-undo:hover{background:color-mix(in srgb,var(--ux-page) 12%,transparent)}
.u071-undo:focus-visible{outline:2px solid var(--ux-accent-2);outline-offset:1px}
.u071-undo svg{width:22px;height:22px;transform:rotate(-90deg)}
.u071-undo circle{fill:none;stroke-width:2.6}
.u071-undo .t{stroke:color-mix(in srgb,var(--ux-page) 20%,transparent)}
.u071-undo .p{stroke:currentColor;stroke-dasharray:100;stroke-dashoffset:calc(100 - var(--left,1) * 100);stroke-linecap:round}
</style>
<div class="ux u071">
  <div class="u071-head"><b>Inbox</b><small class="u071-count"></small></div>
  <ul class="u071-list"></ul>
  <p class="u071-empty">Inbox zero</p>
  <div class="u071-snack" role="status" aria-live="polite"><p></p><button class="u071-undo" type="button" tabindex="-1"><svg viewBox="0 0 22 22" aria-hidden="true"><circle class="t" cx="11" cy="11" r="8.5"/><circle class="p" cx="11" cy="11" r="8.5" pathLength="100"/></svg>Undo</button></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ul = root.querySelector('.u071-list'), snack = root.querySelector('.u071-snack'), msg = snack.querySelector('p'), undo = root.querySelector('.u071-undo'), count = root.querySelector('.u071-count');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var D = [
    ['D', 'Doyun Han', '9:41 AM', 'Mockup feedback, all in one place', 'linear-gradient(140deg,#8B6CFF,#5B8CFF)'],
    ['H', 'Harin Yoon', '8:15 AM', 'Friday’s meetup has a new venue', 'linear-gradient(140deg,#22C3A6,#0EA5E9)'],
    ['L', 'Lumen Billing', 'Yesterday', 'Your October receipt is here', 'linear-gradient(140deg,#FFB547,#FF7A45)'],
    ['M', 'Mina Jung', 'Yesterday', 'Sharing QA checklist v3', 'linear-gradient(140deg,#FF7A93,#B04FD0)']
  ];
  var TRASH = '<svg viewBox="0 0 22 22"><path d="M4 6.5h14M9 6.5V4.5h4v2M6 6.5l1 11a1.5 1.5 0 0 0 1.5 1.4h5a1.5 1.5 0 0 0 1.5-1.4l1-11"/></svg>';
  var items = D.map(function (d) {
    var li = document.createElement('li');
    li.className = 'u071-it';
    li.innerHTML = '<div><span class="u071-bg" aria-hidden="true">' + TRASH + '</span><div class="u071-row" tabindex="0" aria-label="' + d[1] + ', ' + d[3] + '. Press Delete to remove"><span class="u071-av" style="--g:' + d[4] + '" aria-hidden="true">' + d[0] + '</span><span class="u071-tx"><b>' + d[1] + '<small>' + d[2] + '</small></b><span>' + d[3] + '</span></span><button class="u071-del" type="button" aria-label="Delete email from ' + d[1] + '">' + TRASH + '</button></div></div>';
    ul.appendChild(li);
    return li;
  });
  var batch = [], left = 0, raf = 0, paused = false, last = 0, DUR = 5000;
  function refresh() {
    var n = items.filter(function (li) { return !li.classList.contains('gone'); }).length;
    count.textContent = n + ' unread';
    root.classList.toggle('is-empty', n === 0);
  }
  function hideSnack() { root.classList.remove('is-snack'); undo.tabIndex = -1; batch = []; cancelAnimationFrame(raf); }
  function tick(now) {
    if (!root.isConnected) return;
    if (!paused) left -= now - last;
    last = now;
    undo.style.setProperty('--left', Math.max(0, left / DUR).toFixed(3));
    if (left <= 0) { hideSnack(); return; }
    raf = requestAnimationFrame(tick);
  }
  function del(li) {
    if (li.classList.contains('gone')) return;
    var row = li.querySelector('.u071-row');
    row.style.setProperty('--x', '-110%');
    setTimeout(function () { li.classList.add('gone'); li.inert = true; refresh(); }, rm ? 0 : 160);
    batch.push(li);
    msg.innerHTML = batch.length > 1 ? '<b>' + batch.length + '</b> emails deleted' : 'Email deleted';
    if (!rm && batch.length > 1) msg.querySelector('b').animate([{ transform: 'scale(1.5)' }, { transform: 'none' }], { duration: 350, easing: 'cubic-bezier(.34,1.5,.64,1)' });
    root.classList.add('is-snack'); undo.tabIndex = 0;
    left = DUR; last = performance.now();
    cancelAnimationFrame(raf); raf = requestAnimationFrame(tick);
    var next = items.filter(function (x) { return !x.classList.contains('gone') && x !== li; })[0];
    if (next && li.contains(document.activeElement)) next.querySelector('.u071-row').focus({ preventScroll: true });
  }
  undo.addEventListener('click', function () {
    batch.forEach(function (li, i) {
      var row = li.querySelector('.u071-row');
      li.inert = false;
      setTimeout(function () { li.classList.remove('gone'); }, i * 60);
      setTimeout(function () { row.style.setProperty('--x', '0px'); li.querySelector('.u071-bg').style.setProperty('--k', .6); }, rm ? 0 : 260 + i * 60);
    });
    var first = batch[0];
    hideSnack(); refresh();
    if (first) setTimeout(function () { if (root.isConnected) first.querySelector('.u071-row').focus({ preventScroll: true }); }, 300);
  });
  snack.addEventListener('pointerenter', function () { paused = true; });
  snack.addEventListener('pointerleave', function () { paused = false; });
  snack.addEventListener('focusin', function () { paused = true; });
  snack.addEventListener('focusout', function () { paused = false; });
  items.forEach(function (li) {
    var row = li.querySelector('.u071-row'), bg = li.querySelector('.u071-bg');
    var sx = 0, dx = 0, down = false;
    row.addEventListener('pointerdown', function (e) { if (e.target.closest('button') || e.button !== 0) return; down = true; sx = e.clientX; dx = 0; row.setPointerCapture(e.pointerId); row.classList.add('drag'); });
    row.addEventListener('pointermove', function (e) {
      if (!down) return;
      dx = Math.min(0, e.clientX - sx);
      row.style.setProperty('--x', (dx < -100 ? -100 + (dx + 100) * 0.6 : dx) + 'px');
      bg.style.setProperty('--k', Math.min(1.25, 0.6 + -dx / 160).toFixed(2));
    });
    var end = function (e) { if (!down) return; down = false; dx = Math.min(0, e.clientX - sx); row.classList.remove('drag'); if (dx < -100) del(li); else { row.style.setProperty('--x', '0px'); bg.style.setProperty('--k', .6); } };
    row.addEventListener('pointerup', end); row.addEventListener('pointercancel', end);
    row.addEventListener('keydown', function (e) { if (e.key === 'Delete' || e.key === 'Backspace') { e.preventDefault(); del(li); } });
    li.querySelector('.u071-del').addEventListener('click', function () { del(li); });
  });
  refresh();
})();
</script>
--- Code end ---

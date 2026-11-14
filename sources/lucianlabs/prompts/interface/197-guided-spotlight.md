---
source: "lucianlabs"
id: "197"
title: "Guided spotlight tour"
category: "Workflow & Systems"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#197"
tags: ["onboarding", "spotlight", "tour", "coachmark", "overlay"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Guided spotlight tour (197, Workflow & Systems)
[What it does] A tour that highlights the key controls of a real app screen one by one. Press Take the tour and the screen dims while only the first target shows through a rounded hole; each Next glides the hole to the size and position of the next target. The explanation bubble follows with a tail pointing at the target, and a glowing ring pulses around the hole.
[How to use it] Press ‘Take the tour’ and follow ‘Next’. Esc ends it any time

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
<!-- Lucian UX/UI Prompt #197 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#197 -->
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
.u197{position:relative;width:340px;height:352px;padding:16px;box-sizing:border-box;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink);overflow:hidden}
.u197-app{height:252px;border-radius:16px;background:var(--ux-surface-2);overflow:hidden}
.u197-bar{display:flex;align-items:center;gap:6px;height:48px;padding:0 10px 0 14px;background:var(--ux-surface);border-bottom:1px solid var(--ux-line)}
.u197-bar b{flex:1;font:italic 800 17px/1 Georgia,serif;letter-spacing:-.02em}
.u197-ib{width:32px;height:32px;border:0;padding:0;border-radius:10px;background:var(--ux-surface-2);color:var(--ux-ink);display:grid;place-items:center}
.u197-ib svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round}
.u197-add{background:var(--ux-ink);color:var(--ux-surface)}
.u197-me{width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#FFC078,#E8590C);margin-left:2px}
.u197-bd{padding:12px 14px}
.u197-bd h5{margin:0 0 8px;font-size:11.5px;font-weight:800;color:var(--ux-ink-3)}
.u197-gd{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
.u197-dc{height:132px;border-radius:12px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line);padding:10px 9px;display:flex;flex-direction:column;gap:5px}
.u197-dc i{height:5px;border-radius:3px;background:var(--ux-line-2)}.u197-dc i:nth-of-type(2){width:70%}.u197-dc i:nth-of-type(3){width:85%}
.u197-dc b{margin-top:auto;font-size:11.5px;font-weight:800}
.u197-dc small{font-size:10px;color:var(--ux-ink-3)}
.u197-dc:first-child{background:linear-gradient(160deg,color-mix(in srgb,#c09045 16%,var(--ux-surface)),var(--ux-surface) 60%)}
.u197-start{display:block;margin:14px auto 0;height:40px;padding:0 20px;border:0;border-radius:999px;background:#c09045;color:#fff;font-size:13px;font-weight:800;box-shadow:0 10px 18px -10px #c09045}
.u197-start:focus-visible,.u197-tip button:focus-visible,.u197-ib:focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
.u197-ov{position:absolute;inset:0;width:100%;height:100%;opacity:0;pointer-events:none;transition:opacity .35s}
.u197-ov path{fill:rgba(10,12,22,.66);pointer-events:none}
.u197.is-tour .u197-ov{opacity:1}
.u197.is-tour .u197-ov path{pointer-events:visiblePainted}
.u197-ring{position:absolute;left:0;top:0;border-radius:14px;box-shadow:0 0 0 2px #FFD8A8;pointer-events:none;opacity:0;transition:opacity .3s}
.u197.is-tour .u197-ring{opacity:1}
.u197-ring::after{content:"";position:absolute;inset:-2px;border-radius:inherit;box-shadow:0 0 0 2px #FFD8A8;animation:u197-pulse 1.5s ease-out infinite}
@keyframes u197-pulse{0%{opacity:.9;transform:scale(1)}100%{opacity:0;transform:scale(1.25)}}
.u197-tip{position:absolute;left:0;top:0;width:224px;padding:12px 13px 11px;border-radius:14px;background:var(--ux-surface);box-shadow:0 14px 30px -10px rgba(0,0,0,.45);opacity:0;visibility:hidden;transform:translateY(6px) scale(.97);transition:left .45s cubic-bezier(.3,1.15,.4,1),top .45s cubic-bezier(.3,1.15,.4,1),opacity .25s,transform .35s var(--ux-spring),visibility 0s .3s}
.u197.is-tour .u197-tip{opacity:1;visibility:visible;transform:none;transition:left .45s cubic-bezier(.3,1.15,.4,1),top .45s cubic-bezier(.3,1.15,.4,1),opacity .25s,transform .35s var(--ux-spring)}
.u197-tip::before{content:"";position:absolute;left:var(--ax,30px);width:12px;height:12px;margin-left:-6px;background:inherit;transform:rotate(45deg);transition:left .45s cubic-bezier(.3,1.15,.4,1)}
.u197-tip.dn::before{top:-5px}.u197-tip.up::before{bottom:-5px}
.u197-tip.rt::before{left:-5px;top:var(--ay,30px);margin:-6px 0 0}
.u197-tip small{font-size:10.5px;font-weight:800;color:#c09045}
.u197-tip b{display:block;margin-top:3px;font-size:14px;font-weight:850}
.u197-tip p{margin:3px 0 10px;font-size:12px;line-height:1.45;color:var(--ux-ink-2)}
.u197-tip .ct{animation:u197-fade .35s ease}
@keyframes u197-fade{from{opacity:0;transform:translateY(4px)}}
.u197-tf{display:flex;align-items:center;gap:6px}
.u197-dots{display:flex;gap:4px;margin-right:auto}
.u197-dots i{width:6px;height:6px;border-radius:3px;background:var(--ux-line-2);transition:width .3s var(--ux-spring),background-color .3s}
.u197-dots i.on{width:16px;background:#c09045}
.u197-tf button{height:28px;padding:0 10px;border:0;border-radius:8px;background:var(--ux-surface-2);color:var(--ux-ink-2);font-size:11.5px;font-weight:800}
.u197-tf .u197-nx{background:var(--ux-ink);color:var(--ux-surface)}
.u197-x{position:absolute;right:8px;top:8px;height:22px;padding:0 7px;border:0;border-radius:7px;background:none;color:var(--ux-ink-3);font-size:10.5px;font-weight:800}
</style>
<div class="ux u197">
  <div class="u197-app">
    <div class="u197-bar"><b>Notes</b><button class="u197-ib u197-find" type="button" aria-label="Search"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5 14 14"/></svg></button><button class="u197-ib u197-share" type="button" aria-label="Share"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 10V2M5 5l3-3 3 3M3 9v4h10V9"/></svg></button><button class="u197-ib u197-add" type="button" aria-label="New document"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 3v10M3 8h10"/></svg></button><span class="u197-me" aria-hidden="true"></span></div>
    <div class="u197-bd"><h5>My documents</h5><div class="u197-gd"><div class="u197-dc u197-doc"><i></i><i></i><i></i><b>Meeting notes</b><small>Edited today</small></div><div class="u197-dc"><i></i><i></i><i></i><b>Trip plan</b><small>Yesterday</small></div><div class="u197-dc"><i></i><i></i><i></i><b>Groceries</b><small>3 days ago</small></div></div></div>
  </div>
  <button class="u197-start" type="button"></button>
  <svg class="u197-ov" viewBox="0 0 340 352" aria-hidden="true"><path fill-rule="evenodd"/></svg>
  <i class="u197-ring" aria-hidden="true"></i>
  <div class="u197-tip" role="dialog" aria-label="Screen tour"><button class="u197-x" type="button">Skip</button><div class="ct"><small></small><b></b><p></p></div><div class="u197-tf"><span class="u197-dots" aria-hidden="true"></span><button class="u197-pv" type="button">Back</button><button class="u197-nx" type="button"></button></div></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ov = root.querySelector('.u197-ov path'), ring = root.querySelector('.u197-ring'), tip = root.querySelector('.u197-tip'), start = root.querySelector('.u197-start');
  var nx = root.querySelector('.u197-nx'), pv = root.querySelector('.u197-pv'), dots = root.querySelector('.u197-dots'), ct = tip.querySelector('.ct');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var STEPS = [['.u197-add', 'New document', 'Start a blank document right here.'], ['.u197-find', 'Quick search', 'Search titles and content at once.'], ['.u197-doc', 'Recent documents', 'The last one you opened comes first.'], ['.u197-share', 'Write together', 'Invite people with a link to edit together.']];
  var W = 340, H = 352, PAD = 6, cur = -1, hole = null, anim = 0;
  STEPS.forEach(function () { dots.appendChild(document.createElement('i')); });
  start.textContent = 'Take the tour';
  function rect(el) {
    var r = el.getBoundingClientRect(), rr = root.getBoundingClientRect(), k = root.offsetWidth / (rr.width || 1);
    return { x: (r.left - rr.left) * k - PAD, y: (r.top - rr.top) * k - PAD, w: r.width * k + PAD * 2, h: r.height * k + PAD * 2 };
  }
  function shape(h) {
    var r = Math.min(14, h.h / 2, h.w / 2), x = h.x, y = h.y, w = h.w, hh = h.h;
    return 'M0 0H' + W + 'V' + H + 'H0Z M' + (x + r) + ' ' + y + 'H' + (x + w - r) + 'Q' + (x + w) + ' ' + y + ' ' + (x + w) + ' ' + (y + r) + 'V' + (y + hh - r) + 'Q' + (x + w) + ' ' + (y + hh) + ' ' + (x + w - r) + ' ' + (y + hh) + 'H' + (x + r) + 'Q' + x + ' ' + (y + hh) + ' ' + x + ' ' + (y + hh - r) + 'V' + (y + r) + 'Q' + x + ' ' + y + ' ' + (x + r) + ' ' + y + 'Z';
  }
  function paint(h) {
    ov.setAttribute('d', shape(h));
    ring.style.transform = 'translate(' + h.x.toFixed(1) + 'px,' + h.y.toFixed(1) + 'px)';
    ring.style.width = h.w.toFixed(1) + 'px'; ring.style.height = h.h.toFixed(1) + 'px';
    ring.style.borderRadius = Math.min(14, h.h / 2) + 'px';
  }
  function moveHole(to) {
    cancelAnimationFrame(anim);
    var from = hole || { x: to.x + to.w / 2, y: to.y + to.h / 2, w: 0, h: 0 }, t0 = performance.now();
    (function f(now) {
      var k = rm ? 1 : Math.max(0, Math.min(1, (now - t0) / 520)), c = 1.4, e = 1 + (c + 1) * Math.pow(k - 1, 3) + c * Math.pow(k - 1, 2);
      hole = { x: from.x + (to.x - from.x) * e, y: from.y + (to.y - from.y) * e, w: Math.max(0, from.w + (to.w - from.w) * e), h: Math.max(0, from.h + (to.h - from.h) * e) };
      paint(hole);
      if (k < 1) anim = requestAnimationFrame(f);
    })(t0);
  }
  function placeTip(t) {
    tip.style.width = '224px';
    var th = tip.offsetHeight, side = '', left, top;
    if (t.y + t.h + 12 + th <= H - 8) side = 'dn';
    else if (t.y - 12 - th >= 8) side = 'up';
    else side = 'rt';
    tip.classList.remove('dn', 'up', 'rt'); tip.classList.add(side);
    if (side === 'rt') {
      var tw = Math.min(224, W - (t.x + t.w + 12) - 10);
      tip.style.width = tw + 'px'; th = tip.offsetHeight;
      left = t.x + t.w + 12;
      top = Math.max(8, Math.min(H - th - 8, t.y + t.h / 2 - th / 2));
      tip.style.setProperty('--ay', Math.max(16, Math.min(th - 16, t.y + t.h / 2 - top)) + 'px');
    } else {
      left = Math.max(10, Math.min(W - 224 - 10, t.x + t.w / 2 - 112));
      top = side === 'dn' ? t.y + t.h + 12 : t.y - 12 - th;
      tip.style.setProperty('--ax', Math.max(18, Math.min(206, t.x + t.w / 2 - left)) + 'px');
    }
    tip.style.left = left + 'px'; tip.style.top = top + 'px';
  }
  function go(i) {
    cur = i;
    var s = STEPS[i], t = rect(root.querySelector(s[0]));
    ct.querySelector('small').textContent = (i + 1) + ' / ' + STEPS.length;
    ct.querySelector('b').textContent = s[1];
    ct.querySelector('p').textContent = s[2];
    ct.style.animation = 'none'; void ct.offsetWidth; ct.style.animation = '';
    nx.textContent = i === STEPS.length - 1 ? 'Done' : 'Next';
    pv.hidden = i === 0;
    Array.prototype.forEach.call(dots.children, function (d, k) { d.classList.toggle('on', k === i); });
    moveHole(t); placeTip(t);
    nx.focus({ preventScroll: true });
  }
  function begin() { root.classList.add('is-tour'); hole = null; go(0); }
  function end() {
    root.classList.remove('is-tour'); cur = -1;
    start.textContent = 'Tour again';
    start.focus({ preventScroll: true });
  }
  start.addEventListener('click', begin);
  nx.addEventListener('click', function () { if (cur < STEPS.length - 1) go(cur + 1); else end(); });
  pv.addEventListener('click', function () { if (cur > 0) go(cur - 1); });
  root.querySelector('.u197-x').addEventListener('click', end);
  root.addEventListener('keydown', function (e) {
    if (cur < 0) return;
    if (e.key === 'Escape') { e.preventDefault(); end(); }
    if (e.key === 'ArrowRight') { e.preventDefault(); nx.click(); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); pv.click(); }
  });
})();
</script>
--- Code end ---

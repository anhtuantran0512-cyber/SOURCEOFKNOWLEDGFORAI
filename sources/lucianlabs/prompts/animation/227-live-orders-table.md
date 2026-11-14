---
source: "lucianlabs"
id: "227"
title: "Live table with incoming orders"
category: "Data Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#227"
tags: ["data-table", "realtime", "sorting", "dashboard", "orders"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Live table with incoming orders (227, Data Motion)
[What it does] Every few seconds a new order slides in at the top of an order table and glows briefly as the rows below glide down. Press the Amount or Time header and the rows slide past each other into the new order while the sort arrow spins. Press Pause at the top and new orders just pile up; resume and “N new orders” come in all at once.
[How to use it] Press the Amount header to sort, and pause the stream

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
<!-- Lucian UX/UI Prompt #227 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#227 -->
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
.u227{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u227-hd{position:absolute;left:18px;right:14px;top:16px;display:flex;align-items:center;gap:8px}
.u227-hd b{margin-right:auto;display:flex;align-items:center;gap:7px;font-size:14.5px;font-weight:900}
.u227-hd b i{width:8px;height:8px;border-radius:50%;background:#E11D48;box-shadow:0 0 0 3px color-mix(in srgb,#E11D48 25%,transparent);animation:u227-lv 1.4s ease-in-out infinite}
.u227.is-pause .u227-hd b i{animation:none;background:var(--ux-ink-3);box-shadow:none}
@keyframes u227-lv{50%{opacity:.35}}
.u227-pz{display:inline-flex;align-items:center;gap:5px;height:28px;padding:0 10px;border:0;border-radius:999px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink-2);font:inherit;font-size:10.5px;font-weight:800;cursor:pointer}
.u227-pz em{font-style:normal;padding:1px 6px;border-radius:999px;background:var(--ux-accent);color:#fff;font-size:9.5px;font-weight:900}
.u227-pz em:empty{display:none}
.u227-tb{position:absolute;left:10px;right:10px;top:56px;bottom:10px;border-radius:16px;background:var(--ux-surface-2);overflow:hidden}
.u227-hr,.u227-r{display:grid;grid-template-columns:1.25fr .9fr 1fr;align-items:center;padding:0 12px}
.u227-hr{height:32px;border-bottom:1px solid var(--ux-line);font-size:10px;font-weight:850;color:var(--ux-ink-3)}
.u227-hr>span:first-child{font-size:10px}
.u227-th{display:inline-flex;align-items:center;gap:3px;padding:0;border:0;background:none;color:inherit;font:inherit;cursor:pointer}
.u227-th[aria-sort="ascending"],.u227-th[aria-sort="descending"]{color:var(--ux-ink)}
.u227-th svg{width:9px;height:9px;opacity:.35;transition:transform .35s cubic-bezier(.3,1.6,.5,1),opacity .2s}
.u227-th[aria-sort="ascending"] svg{opacity:1;transform:rotate(180deg)}
.u227-th[aria-sort="descending"] svg{opacity:1}
.u227-th:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px;border-radius:4px}
.u227-bd{position:relative}
.u227-r{position:absolute;left:0;right:0;height:42px;border-bottom:1px solid var(--ux-line);transition:transform .45s cubic-bezier(.3,1.1,.4,1),opacity .35s;font-size:11px;font-weight:700}
.u227-r.is-new{animation:u227-gl 1.4s ease}
@keyframes u227-gl{0%{background:color-mix(in srgb,var(--ux-accent) 22%,transparent)}100%{background:transparent}}
.u227-r .nm{display:flex;flex-direction:column;min-width:0}
.u227-r .nm b{font-size:11.5px;font-weight:850;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.u227-r .nm small{font-size:9.5px;font-weight:700;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u227-r .am{font-weight:900;font-variant-numeric:tabular-nums}
.u227-r .st{display:inline-flex;align-items:center;gap:5px;font-size:10px;font-weight:800;color:var(--c)}
.u227-r .st::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--c)}
@media (prefers-reduced-motion: reduce){.u227-r{transition:none}.u227-r.is-new,.u227-hd b i{animation:none}}
</style>
<div class="ux u227">
  <div class="u227-hd"><b><i aria-hidden="true"></i>Live orders</b><button type="button" class="u227-pz"><span></span><em></em></button></div>
  <div class="u227-tb" role="table"><div class="u227-hr" role="row"></div><div class="u227-bd" role="rowgroup"></div></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var hr = root.querySelector('.u227-hr'), bd = root.querySelector('.u227-bd'), pz = root.querySelector('.u227-pz'), pzl = pz.querySelector('span'), pzn = pz.querySelector('em');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var TH = ['Time', 'Amount', 'Status'], NM = ['Seoyeon K.', 'Junho L.', 'Haeun P.', 'Minjun C.', 'Yuna J.', 'Jiho H.', 'Jia Y.', 'Taemin O.'];
  var ST = [['Paid', '#10B981'], ['Packing', '#0EA5E9'], ['Reviewing', '#F59E0B']];
  var UNIT = 1, RH = 42, MAX = 6, seq = 0, now0 = Date.now();
  var rows = [], sort = { k: 0, d: -1 }, paused = false, queue = [], vis = true;
  var H = TH.map(function (t, i) {
    if (i === 2) { var s = document.createElement('span'); s.textContent = t; s.setAttribute('role', 'columnheader'); hr.appendChild(s); return null; }
    var b = document.createElement('button'); b.type = 'button'; b.className = 'u227-th'; b.setAttribute('role', 'columnheader'); b.innerHTML = '<span></span><svg viewBox="0 0 9 9" aria-hidden="true"><path d="M2 3.5l2.5 2.5L7 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'; b.firstChild.textContent = t;
    b.addEventListener('click', function () { sort = { k: i, d: sort.k === i ? -sort.d : -1 }; head(); place(); });
    hr.appendChild(b); return b;
  });
  function head() { H.forEach(function (b, i) { if (b) b.setAttribute('aria-sort', sort.k === i ? (sort.d > 0 ? 'ascending' : 'descending') : 'none'); }); }
  function make() {
    seq++; var a = Math.round((12 + Math.random() * 230)) * UNIT, o = { id: seq, t: Date.now(), a: a, n: NM[seq % NM.length], s: ST[Math.floor(Math.random() * 3)] };
    var r = document.createElement('div'); r.className = 'u227-r'; r.setAttribute('role', 'row'); r.style.setProperty('--c', o.s[1]);
    r.innerHTML = '<span class="nm" role="cell"><b></b><small></small></span><span class="am" role="cell"></span><span class="st" role="cell"></span>';
    r.querySelector('b').textContent = o.n; r.querySelector('.am').textContent = '$' + a.toLocaleString('en-US'); r.querySelector('.st').textContent = o.s[0];
    o.el = r; o.ago = r.querySelector('small'); return o;
  }
  function ago(o) { var s = Math.round((Date.now() - o.t) / 1000); return s < 3 ? 'now' : s + 's ago'; }
  function place() {
    rows.sort(function (x, y) { var v = sort.k === 1 ? x.a - y.a : x.t - y.t; return v * sort.d || y.id - x.id; });
    rows.forEach(function (o, i) { o.el.style.transform = 'translateY(' + (i * RH) + 'px)'; o.el.style.opacity = i < MAX ? 1 : 0; o.ago.textContent = ago(o); });
    while (rows.length > MAX + 2) { var g = rows.pop(); (function (el) { setTimeout(function () { el.remove(); }, 450); })(g.el); }
  }
  function push(o, glow) {
    o.el.style.transition = 'none'; o.el.style.transform = 'translateY(' + (sort.k === 0 && sort.d < 0 ? -RH : MAX * RH) + 'px)'; o.el.style.opacity = 0;
    bd.appendChild(o.el); void o.el.offsetWidth; o.el.style.transition = '';
    if (glow && !rm) { o.el.classList.remove('is-new'); void o.el.offsetWidth; o.el.classList.add('is-new'); }
    rows.push(o); place();
  }
  function label() { pzl.textContent = paused ? 'Resume' : 'Pause'; pzn.textContent = paused && queue.length ? 'New orders: ' + queue.length + '' : ''; root.classList.toggle('is-pause', paused); }
  pz.addEventListener('click', function () {
    paused = !paused;
    if (!paused) queue.splice(0).forEach(function (o, i) { setTimeout(function () { push(o, true); }, rm ? 0 : i * 90); });
    label();
  });
  for (var i = 0; i < 5; i++) { var o = make(); o.t = now0 - (5 - i) * 7000; push(o, false); }
  head(); label();
  (function loop() {
    if (!root.isConnected) return;
    if (vis) { var o = make(); if (paused) { queue.push(o); label(); } else push(o, true); }
    setTimeout(loop, rm ? 5000 : 2300);
  })();
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; }).observe(root);
})();
</script>
--- Code end ---

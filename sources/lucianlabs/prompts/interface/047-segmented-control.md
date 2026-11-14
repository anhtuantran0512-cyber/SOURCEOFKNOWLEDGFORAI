---
source: "lucianlabs"
id: "047"
title: "Period segmented control"
category: "Menus & Tabs"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#047"
tags: ["segmented", "control", "period", "count-up", "chart-morph"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Period segmented control (047, Menus & Tabs)
[What it does] Switch the period and the knob stretches as it moves, the big number counts from the old value to the new one, and the chart line bends into its new shape.
[How to use it] Press Day, Week, Month or Year — the number and the chart change together. With a keyboard, use the left and right arrow keys

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
<!-- Lucian UX/UI Prompt #047 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#047 -->
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
.u047{position:relative;width:350px;height:330px;display:flex;flex-direction:column;padding:16px 16px 0;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -38px var(--ux-shadow-strong);overflow:hidden}
.u047-seg{position:relative;display:grid;grid-template-columns:repeat(4,1fr);padding:4px;border-radius:16px;background:var(--ux-surface-2)}
.u047-knob{position:absolute;top:4px;bottom:4px;left:var(--l,4px);right:var(--r,4px);border-radius:12px;background:var(--ux-surface);box-shadow:0 4px 12px -6px var(--ux-shadow-strong),0 0 0 1px var(--ux-line)}
.u047-seg.go-r .u047-knob{transition:right .3s var(--ux-ease),left .5s var(--ux-spring) .07s}
.u047-seg.go-l .u047-knob{transition:left .3s var(--ux-ease),right .5s var(--ux-spring) .07s}
.u047-opt{position:relative;height:38px;border:0;padding:0;border-radius:12px;background:none;font-size:14px;font-weight:680;color:var(--ux-ink-3);transition:color .3s,transform .3s var(--ux-spring)}
.u047-opt:hover{color:var(--ux-ink-2)}
.u047-opt:active{transform:scale(.94)}
.u047-opt[aria-checked="true"]{color:var(--ux-ink)}
.u047-opt:focus-visible{outline:2px solid var(--ux-accent);outline-offset:1px}
.u047-lab{margin:18px 4px 0;font-size:13px;font-weight:650;color:var(--ux-ink-3)}
.u047-row{display:flex;align-items:center;gap:10px;margin:2px 4px 0}
.u047-num{font-size:40px;font-weight:800;letter-spacing:-.055em;line-height:1.1;font-variant-numeric:tabular-nums}
.u047-chg{display:inline-flex;align-items:center;gap:4px;height:26px;padding:0 9px;border-radius:999px;font-size:12.5px;font-weight:750;background:color-mix(in srgb,var(--ux-mint) 15%,transparent);color:var(--ux-mint);font-variant-numeric:tabular-nums;transition:background-color .4s,color .4s}
.u047-chg.down{background:color-mix(in srgb,var(--ux-danger) 13%,transparent);color:var(--ux-danger)}
.u047-chg svg{width:11px;height:11px;fill:none;stroke:currentColor;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;transition:transform .45s var(--ux-spring)}
.u047-chg.down svg{transform:rotate(180deg)}
.u047-chart{position:relative;flex:1;margin:8px -16px 0}
.u047-chart svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.u047-line{fill:none;stroke:var(--ux-accent);stroke-width:2.6;stroke-linejoin:round;stroke-linecap:round}
.u047-grid line{stroke:var(--ux-line);stroke-dasharray:3 5}
.u047-dot{fill:var(--ux-surface);stroke:var(--ux-accent);stroke-width:3}
.u047-halo{fill:var(--ux-accent);opacity:.18;transform-box:fill-box;transform-origin:center;animation:u047-p 2s ease-out infinite}
@keyframes u047-p{0%{transform:scale(.6);opacity:.35}100%{transform:scale(2.2);opacity:0}}
</style>
<div class="ux u047">
  <div class="u047-seg" role="radiogroup" aria-label="Period">
    <span class="u047-knob" aria-hidden="true"></span>
    <button class="u047-opt" type="button" role="radio" aria-checked="false">Day</button>
    <button class="u047-opt" type="button" role="radio" aria-checked="false">Week</button>
    <button class="u047-opt" type="button" role="radio" aria-checked="true">Month</button>
    <button class="u047-opt" type="button" role="radio" aria-checked="false">Year</button>
  </div>
  <div class="u047-lab">Revenue, last 30 days</div>
  <div class="u047-row" aria-live="polite"><span class="u047-num">$0</span><span class="u047-chg"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 7.5L6 4l3.5 3.5"/></svg><span>0%</span></span></div>
  <div class="u047-chart" aria-hidden="true">
    <svg viewBox="0 0 350 150" preserveAspectRatio="xMidYMax meet">
      <defs><linearGradient id="u047-fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" style="stop-color:var(--ux-accent);stop-opacity:.28"/><stop offset="1" style="stop-color:var(--ux-accent);stop-opacity:0"/></linearGradient></defs>
      <g class="u047-grid"><line x1="0" x2="350" y1="40" y2="40"/><line x1="0" x2="350" y1="85" y2="85"/></g>
      <path class="u047-area"/>
      <path class="u047-line"/>
      <circle class="u047-halo" r="9"/>
      <circle class="u047-dot" r="5.5"/>
    </svg>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var seg = root.querySelector('.u047-seg'), knob = root.querySelector('.u047-knob');
  var opts = Array.prototype.slice.call(root.querySelectorAll('.u047-opt'));
  var num = root.querySelector('.u047-num'), lab = root.querySelector('.u047-lab');
  var chg = root.querySelector('.u047-chg'), pct = chg.querySelector('span');
  var area = root.querySelector('.u047-area'), line = root.querySelector('.u047-line');
  var dot = root.querySelector('.u047-dot'), halo = root.querySelector('.u047-halo');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var gid = 'u047-f' + Math.random().toString(36).slice(2, 7);
  root.querySelector('linearGradient').id = gid;
  area.setAttribute('fill', 'url(#' + gid + ')');
  function wave(seed, rise) {
    var a = [];
    for (var i = 0; i < 14; i++) a.push(0.5 + Math.sin(i * 0.9 + seed) * 0.16 + Math.sin(i * 2.3 + seed * 2) * 0.08 + (i / 13 - 0.5) * rise);
    return a;
  }
  var DATA = [
    { l: 'Revenue today', v: 1840000, p: -2.1, pts: wave(1.2, -0.2) },
    { l: 'Revenue, last 7 days', v: 12680000, p: 6.8, pts: wave(2.6, 0.25) },
    { l: 'Revenue, last 30 days', v: 54200000, p: 12.4, pts: wave(4.1, 0.45) },
    { l: 'Revenue this year', v: 486500000, p: 31.9, pts: wave(0.3, 0.7) }
  ];
  var cur = 2, shown = { v: 0, p: 0, pts: DATA[2].pts.map(function () { return 0.15; }) }, raf = 0;
  function xy(pts) {
    return pts.map(function (v, i) { return [i * 350 / (pts.length - 1), 140 - Math.max(0.05, Math.min(0.98, v)) * 120]; });
  }
  function path(p) {
    var d = 'M' + p[0][0] + ',' + p[0][1];
    for (var i = 0; i < p.length - 1; i++) {
      var a = p[i - 1] || p[i], b = p[i], c = p[i + 1], e = p[i + 2] || c;
      d += 'C' + (b[0] + (c[0] - a[0]) / 6).toFixed(1) + ',' + (b[1] + (c[1] - a[1]) / 6).toFixed(1) + ' ' + (c[0] - (e[0] - b[0]) / 6).toFixed(1) + ',' + (c[1] - (e[1] - b[1]) / 6).toFixed(1) + ' ' + c[0].toFixed(1) + ',' + c[1].toFixed(1);
    }
    return d;
  }
  function won(v) { return '$' + Math.round(v / 1380).toLocaleString('en-US'); }
  function paint() {
    var p = xy(shown.pts), d = path(p), last = p[p.length - 1];
    line.setAttribute('d', d);
    area.setAttribute('d', d + 'L350,150L0,150Z');
    dot.setAttribute('cx', last[0]); dot.setAttribute('cy', last[1]);
    halo.setAttribute('cx', last[0]); halo.setAttribute('cy', last[1]);
    num.textContent = won(shown.v);
    pct.textContent = Math.abs(shown.p).toFixed(1) + '%';
  }
  function tween(to) {
    cancelAnimationFrame(raf);
    var from = { v: shown.v, p: shown.p, pts: shown.pts.slice() }, t0 = 0, dur = 750;
    if (rm) { shown = { v: to.v, p: to.p, pts: to.pts.slice() }; paint(); return; }
    function step(now) {
      if (!root.isConnected) return;
      if (!t0) t0 = now;
      var k = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - k, 4);
      shown.v = from.v + (to.v - from.v) * e;
      shown.p = from.p + (to.p - from.p) * e;
      shown.pts = from.pts.map(function (v, i) { return v + (to.pts[i] - v) * e; });
      paint();
      if (k < 1) raf = requestAnimationFrame(step);
    }
    raf = requestAnimationFrame(step);
  }
  function place(dir) {
    var o = opts[cur];
    seg.classList.toggle('go-r', dir > 0);
    seg.classList.toggle('go-l', dir < 0);
    knob.style.setProperty('--l', o.offsetLeft + 'px');
    knob.style.setProperty('--r', (seg.clientWidth - o.offsetLeft - o.offsetWidth) + 'px');
  }
  function select(i, focus, first) {
    if (i === cur && !first) return;
    var dir = first ? 0 : i > cur ? 1 : -1;
    cur = i;
    opts.forEach(function (o, k) { o.setAttribute('aria-checked', String(k === i)); o.tabIndex = k === i ? 0 : -1; });
    if (focus) opts[i].focus();
    place(dir);
    var d = DATA[i];
    lab.textContent = d.l;
    chg.classList.toggle('down', d.p < 0);
    chg.setAttribute('aria-label', (d.p < 0 ? 'Down ' : 'Up ') + Math.abs(d.p) + '% from the previous period');
    tween(d);
  }
  opts.forEach(function (o, i) {
    o.addEventListener('click', function () { select(i); });
    o.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1 : e.key === 'ArrowLeft' || e.key === 'ArrowUp' ? -1 : 0;
      if (d) { e.preventDefault(); select((i + d + 4) % 4, true); }
    });
  });
  select(2, false, true);
})();
</script>
--- Code end ---

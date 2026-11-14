---
source: "lucianlabs"
id: "095"
title: "Bar chart that changes shape"
category: "Widgets & Charts"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#095"
tags: ["chart", "bar", "morph", "tooltip", "scrub"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Bar chart that changes shape (095, Widgets & Charts)
[What it does] Switch between week, month and year and the bars don’t regrow; their count, width and height carry over into the new shape while the axis numbers and average line move along. Sweep across the bars and only the one under you darkens while the big number and tooltip switch to its value and change from the previous one.
[How to use it] Move the mouse or sweep a finger across the bars. Click a bar to pin it, and switch the period with W·M·Y in the top right. On a keyboard, use ←/→ on the bars

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
<!-- Lucian UX/UI Prompt #095 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#095 -->
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
.u095{position:relative;width:340px;height:410px;display:flex;flex-direction:column;padding:20px 18px 14px;border-radius:30px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u095-h{display:flex;align-items:flex-start;justify-content:space-between}
.u095-h small{display:block;font-size:12.5px;font-weight:700;color:var(--ux-ink-3)}
.u095-v{margin-top:2px}
.u095-v b{font-size:29px;font-weight:850;letter-spacing:-.05em;font-variant-numeric:tabular-nums}
.u095-top{display:flex;align-items:baseline;gap:6px}
.u095-dl{font-size:12px;font-weight:800;color:var(--ux-mint);white-space:nowrap}
.u095-dl.dn{color:var(--ux-danger)}
.u095-seg{position:relative;display:flex;padding:3px;border-radius:12px;background:var(--ux-surface-2)}
.u095-seg::before{content:"";position:absolute;top:3px;bottom:3px;left:3px;width:36px;border-radius:9px;background:var(--ux-surface);box-shadow:0 1px 4px -1px var(--ux-shadow-strong);transform:translateX(calc(var(--k,0) * 36px));transition:transform .45s var(--ux-spring)}
.u095-seg button{position:relative;width:36px;height:30px;border:0;padding:0;background:transparent;font-size:12.5px;font-weight:800;color:var(--ux-ink-3);transition:color .2s}
.u095-seg button[aria-pressed="true"]{color:var(--ux-ink)}
.u095-ch{position:relative;flex:1;margin-top:18px;padding-right:44px}
.u095-grid{position:absolute;inset:0 0 26px 0}
.u095-gl{position:absolute;left:0;right:0;height:0;border-top:1px dashed var(--ux-line-2)}
.u095-gl span{position:absolute;right:0;top:-7px;transition:opacity .3s;font-size:10.5px;font-weight:700;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u095-gl:first-child{border-top-style:solid}
.u095-avg{position:absolute;left:0;right:40px;bottom:calc(26px + var(--a,0) * (100% - 26px));height:0;border-top:1.5px dashed var(--ux-accent);transition:bottom .6s var(--ux-spring);z-index:2;pointer-events:none}
.u095-avg span{position:absolute;right:-44px;top:-10px;height:20px;padding:0 6px;border-radius:6px;display:grid;place-items:center;background:var(--ux-accent);color:var(--ux-accent-ink);font-size:10px;font-weight:800}
.u095-bars{position:absolute;left:0;right:44px;top:0;bottom:0;display:flex;align-items:stretch}
.u095-b{position:relative;flex:var(--on,1) 1 0;min-width:0;padding:0 var(--pad,4px);border:0;background:transparent;display:flex;flex-direction:column;justify-content:flex-end;transition:flex-grow .55s var(--ux-ease),padding .55s var(--ux-ease),opacity .3s}
.u095-b.off{--on:0;padding:0;opacity:0;pointer-events:none}
.u095-b i{display:block;height:calc(var(--h,0) * (100% - 26px));margin-bottom:26px;border-radius:8px 8px 4px 4px;background:var(--ux-surface-3);transition:height .65s var(--ux-spring),background-color .25s,opacity .25s;transition-delay:calc(var(--d,0) * 28ms),0s,0s}
.u095-b.last i{background:var(--ux-grad)}
.u095-b em{position:absolute;left:-6px;right:-6px;bottom:4px;font-style:normal;text-align:center;font-size:11px;font-weight:700;color:var(--ux-ink-3);white-space:nowrap;transition:color .2s}
.u095.has .u095-b:not(.on) i{opacity:.5}
.u095-b.on i{background:var(--ux-accent);opacity:1}
.u095-b.on em{color:var(--ux-ink)}
.u095-b.pin i{box-shadow:0 0 0 2px var(--ux-surface),0 0 0 4px var(--ux-accent)}
.u095-b:focus-visible{outline:none}
.u095-b:focus-visible i{box-shadow:0 0 0 2px var(--ux-surface),0 0 0 4px var(--ux-accent)}
.u095-tip{position:absolute;left:0;top:0;z-index:3;height:28px;padding:0 10px;border-radius:9px;display:flex;align-items:center;gap:6px;background:var(--ux-ink);color:var(--ux-page);font-size:12px;font-weight:800;white-space:nowrap;pointer-events:none;transform:translate(var(--tx),var(--ty));opacity:0;transition:opacity .2s,transform .3s var(--ux-ease)}
.u095.has .u095-tip{opacity:1}
.u095-tip small{font-size:11px;font-weight:800;color:var(--ux-mint)}
.u095-tip small.dn{color:#FF8F92}
.u095-seg button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:1px;border-radius:9px}
</style>
<div class="ux u095">
  <div class="u095-h">
    <div><div class="u095-top"><small class="u095-lab">This week</small><span class="u095-dl"></span></div><div class="u095-v"><b>₩0K</b></div></div>
    <div class="u095-seg" role="group" aria-label="Period"><button type="button" aria-pressed="true">W</button><button type="button" aria-pressed="false">M</button><button type="button" aria-pressed="false">Y</button></div>
  </div>
  <div class="u095-ch">
    <div class="u095-grid" aria-hidden="true"></div>
    <div class="u095-bars" role="group" aria-label="Sales bars"></div>
    <div class="u095-avg" aria-hidden="true"><span></span></div>
    <div class="u095-tip" aria-hidden="true"><span></span><small></small></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var lab = root.querySelector('.u095-lab'), big = root.querySelector('.u095-v b'), dl = root.querySelector('.u095-dl'), segs = root.querySelectorAll('.u095-seg button');
  var grid = root.querySelector('.u095-grid'), bars = root.querySelector('.u095-bars'), avg = root.querySelector('.u095-avg'), tip = root.querySelector('.u095-tip'), ch = root.querySelector('.u095-ch');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var D = [
    { t: 'This week', p: 'vs last week', d: 0.12, l: ['M', 'T', 'W', 'T', 'F', 'S', 'S'], f: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Today'], v: [32, 45, 38, 52, 61, 74, 58] },
    { t: 'October', p: 'vs last month', d: 0.08, l: ['W1', 'W2', 'W3', 'W4', 'W5'], f: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'This week'], v: [210, 245, 198, 276, 302] },
    { t: 'This year', p: 'vs last year', d: -0.04, l: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], f: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], v: [1200, 1420, 1080, 1610, 1830, 1700, 2120, 2380, 2210, 2640, 2290, 3100] }
  ];
  var B = [];
  for (var i = 0; i < 12; i++) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'u095-b off'; b.tabIndex = -1;
    b.innerHTML = '<i></i><em></em>';
    bars.appendChild(b); B.push(b);
  }
  var G = [0, 1, 2, 3].map(function (k) { var g = document.createElement('div'); g.className = 'u095-gl'; g.style.bottom = (k / 3 * 100).toFixed(3) + '%'; g.innerHTML = '<span></span>'; grid.appendChild(g); return g; });
  var set = 0, act = -1, pin = -1, shown = 0, tw = 0;
  function fmt(v) { return v < 100 ? '₩' + Math.round(v * 10) + 'K' : '₩' + (v / 100).toFixed(v < 1000 ? 2 : 1) + 'M'; }
  function axis(v) { return !v ? '0' : v < 100 ? Math.round(v * 10) + 'K' : +(v / 100).toFixed(1) + 'M'; }
  function nice(m) { var p = Math.pow(10, Math.floor(Math.log10(m / 3))), s = [1, 2, 2.5, 5, 10].map(function (k) { return k * p; }).filter(function (k) { return k * 3 >= m; })[0]; return s * 3; }
  function roll(to) {
    cancelAnimationFrame(tw);
    var from = shown, t0 = performance.now(), dur = rm ? 1 : 420;
    (function f(n) {
      if (!root.isConnected) return;
      var k = Math.min(1, (n - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      shown = from + (to - from) * e; big.textContent = fmt(shown);
      if (k < 1) tw = requestAnimationFrame(f);
    })(t0);
  }
  function pct(a, b) { var r = (a - b) / b; return (r >= 0 ? '+' : '−') + Math.abs(Math.round(r * 100)) + '%'; }
  function header() {
    var d = D[set], idx = act >= 0 ? act : pin;
    if (idx >= 0) {
      lab.textContent = d.f[idx];
      roll(d.v[idx]);
      dl.textContent = idx ? pct(d.v[idx], d.v[idx - 1]) + ' vs previous' : '';
      dl.classList.toggle('dn', idx > 0 && d.v[idx] < d.v[idx - 1]);
    } else {
      var sum = d.v.reduce(function (a, b) { return a + b; }, 0);
      lab.textContent = d.t; roll(sum);
      dl.textContent = (d.d >= 0 ? '+' : '−') + Math.abs(Math.round(d.d * 100)) + '% ' + d.p;
      dl.classList.toggle('dn', d.d < 0);
    }
  }
  function draw(k, first) {
    set = k; act = -1; pin = -1;
    var d = D[k], n = d.v.length, max = nice(Math.max.apply(null, d.v)), mean = d.v.reduce(function (a, b) { return a + b; }, 0) / n;
    segs.forEach(function (s, j) { s.setAttribute('aria-pressed', String(j === k)); });
    root.querySelector('.u095-seg').style.setProperty('--k', k);
    B.forEach(function (b, j) {
      var on = j < n;
      b.classList.toggle('off', !on); b.classList.remove('on', 'pin');
      b.classList.toggle('last', j === n - 1);
      b.style.setProperty('--d', j);
      b.style.setProperty('--pad', n > 8 ? '2.5px' : '5px');
      if (on) {
        b.querySelector('em').textContent = d.l[j];
        b.setAttribute('aria-label', d.f[j] + ' ' + fmt(d.v[j]));
        b.style.setProperty('--h', first ? 0 : (d.v[j] / max).toFixed(3));
      } else b.style.setProperty('--h', 0);
      b.tabIndex = on && j === n - 1 ? 0 : -1;
    });
    if (first) requestAnimationFrame(function () { requestAnimationFrame(function () { B.forEach(function (b, j) { if (j < n) b.style.setProperty('--h', (d.v[j] / max).toFixed(3)); }); }); });
    G.forEach(function (g, j) { g.firstChild.textContent = axis(max * j / 3); g.firstChild.style.opacity = Math.abs(j / 3 - mean / max) < 0.07 ? 0 : 1; });
    avg.style.setProperty('--a', (mean / max).toFixed(3));
    avg.firstChild.textContent = 'Avg';
    root.classList.remove('has');
    header();
  }
  function show(j) {
    act = j;
    B.forEach(function (b, k) { b.classList.toggle('on', k === j || (j < 0 && k === pin)); });
    var idx = j >= 0 ? j : pin;
    root.classList.toggle('has', idx >= 0);
    if (idx >= 0) {
      var d = D[set], b = B[idx], i = b.querySelector('i');
      tip.firstChild.textContent = fmt(d.v[idx]);
      var sm = tip.querySelector('small');
      sm.textContent = idx ? pct(d.v[idx], d.v[idx - 1]) : '';
      sm.classList.toggle('dn', idx > 0 && d.v[idx] < d.v[idx - 1]);
      var cw = ch.clientWidth, tw2 = tip.offsetWidth, cx = b.offsetLeft + b.offsetWidth / 2;
      var hh = parseFloat(b.style.getPropertyValue('--h')) * (ch.clientHeight - 26);
      tip.style.setProperty('--tx', Math.max(0, Math.min(cw - tw2, cx - tw2 / 2)).toFixed(1) + 'px');
      tip.style.setProperty('--ty', Math.max(-6, ch.clientHeight - 26 - hh - 36).toFixed(1) + 'px');
    }
    header();
  }
  function idxAt(x) {
    var n = D[set].v.length, best = 0;
    for (var j = 0; j < n; j++) { var r = B[j].getBoundingClientRect(); if (x >= r.left) best = j; }
    return best;
  }
  bars.addEventListener('pointermove', function (e) { show(idxAt(e.clientX)); });
  bars.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse') { bars.setPointerCapture(e.pointerId); show(idxAt(e.clientX)); } });
  bars.addEventListener('pointerleave', function () { show(-1); });
  bars.addEventListener('click', function (e) {
    var b = e.target.closest('.u095-b'); if (!b) return;
    var j = B.indexOf(b);
    pin = pin === j ? -1 : j;
    B.forEach(function (x, k) { x.classList.toggle('pin', k === pin); });
    show(j);
  });
  bars.addEventListener('keydown', function (e) {
    var n = D[set].v.length, j = B.indexOf(document.activeElement);
    var to = e.key === 'ArrowRight' ? j + 1 : e.key === 'ArrowLeft' ? j - 1 : e.key === 'Home' ? 0 : e.key === 'End' ? n - 1 : null;
    if (to === null) return;
    e.preventDefault();
    to = Math.max(0, Math.min(n - 1, to));
    B.forEach(function (b, k) { b.tabIndex = k === to ? 0 : -1; });
    B[to].focus(); show(to);
  });
  bars.addEventListener('focusin', function (e) { var j = B.indexOf(e.target); if (j >= 0) show(j); });
  bars.addEventListener('focusout', function (e) { if (!bars.contains(e.relatedTarget)) show(-1); });
  segs.forEach(function (s, k) { s.addEventListener('click', function () { if (k !== set) draw(k); }); });
  draw(0, !rm);
})();
</script>
--- Code end ---

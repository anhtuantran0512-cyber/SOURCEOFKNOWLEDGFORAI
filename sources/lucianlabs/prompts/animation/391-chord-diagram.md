---
source: "lucianlabs"
id: "391"
title: "Month-switching chord diagram"
category: "Data Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#391"
tags: ["chord-diagram", "flow", "network", "transition", "data"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Month-switching chord diagram (391, Data Motion)
[What it does] A chord diagram shows the messages six teams sent each other as arcs around a circle joined by ribbons, with the arcs growing around the rim and the ribbons weaving in when it first appears. Switch between last month and this month above and the arc lengths and ribbon widths stretch and shrink continuously; hover a team's arc to keep only its ribbons with sent and received counts below, or hover a ribbon to see the traffic both ways.
[How to use it] Hover a team arc or a ribbon, then switch months above

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
<!-- Lucian UX/UI Prompt #391 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#391 -->
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
.u391{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);color:var(--ux-ink);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong)}
.u391-hd{position:absolute;left:20px;right:16px;top:16px;display:flex;justify-content:space-between;align-items:center;z-index:1}
.u391-hd b{font-size:13.5px;font-weight:900;white-space:nowrap}
.u391-sg{display:flex;padding:3px;border-radius:999px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line)}
.u391-mo{border:0;padding:4px 10px;white-space:nowrap;border-radius:999px;background:none;color:var(--ux-ink-2);font:inherit;font-size:11px;font-weight:800;cursor:pointer;transition:background .2s,color .2s}
.u391-mo.is-on{background:var(--ux-ink);color:var(--ux-surface)}
.u391-mo:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u391-sv{position:absolute;left:0;top:0;width:340px;height:340px}
.u391-rb{fill-opacity:.55;stroke:var(--ux-surface);stroke-width:.6;cursor:pointer;transition:fill-opacity .25s}
.u391-ar{cursor:pointer;transition:opacity .25s}
.u391-tx{font-size:10.5px;font-weight:850;fill:var(--ux-ink);pointer-events:none}
.u391.is-f .u391-rb{fill-opacity:.07}
.u391.is-f .u391-rb.is-hl{fill-opacity:.8}
.u391.is-f .u391-ar{opacity:.35}
.u391.is-f .u391-ar.is-hl{opacity:1}
.u391-in{position:absolute;left:50%;bottom:12px;transform:translateX(-50%);padding:6px 12px;border-radius:999px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line);font-size:10.5px;font-weight:800;white-space:nowrap;font-variant-numeric:tabular-nums}
</style>
<div class="ux u391">
  <div class="u391-hd"><b>Team messages</b><div class="u391-sg" role="group" aria-label="Period"><button type="button" class="u391-mo" aria-pressed="false">Last mo.</button><button type="button" class="u391-mo is-on" aria-pressed="true">This mo.</button></div></div>
  <svg class="u391-sv" viewBox="0 0 340 340"><g class="u391-rbs"></g><g class="u391-ars"></g><g class="u391-txs" aria-hidden="true"></g></svg>
  <div class="u391-in" aria-live="polite"></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var rbs = root.querySelector('.u391-rbs'), ars = root.querySelector('.u391-ars'), txs = root.querySelector('.u391-txs'), info = root.querySelector('.u391-in'), mos = root.querySelectorAll('.u391-mo');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NAME = ['Eng', 'Design', 'Product', 'Mktg', 'Sales', 'Ops'], COL = ['#6366F1', '#EC4899', '#F59E0B', '#10B981', '#0EA5E9', '#8B5CF6'];
  var M = [
    [[0, 60, 70, 15, 10, 80], [55, 0, 60, 40, 8, 10], [80, 50, 0, 45, 50, 25], [20, 45, 50, 0, 140, 25], [12, 10, 40, 130, 0, 85], [70, 12, 30, 20, 75, 0]],
    [[0, 120, 90, 20, 15, 60], [110, 0, 80, 70, 10, 15], [95, 85, 0, 60, 40, 30], [25, 75, 55, 0, 90, 20], [10, 12, 45, 95, 0, 70], [55, 18, 25, 22, 65, 0]]
  ];
  var n = 6, CX = 170, CY = 173, R0 = 91, R1 = 102, PAD = 0.06, cur = M[1].map(function (r) { return r.slice(); }), grow = rm ? 1 : 0, hov = null;
  var AR = [], RB = [], TX = [], PAIRS = [];
  function el(tag, cls, parent) { var e = document.createElementNS('http://www.w3.org/2000/svg', tag); e.setAttribute('class', cls); parent.appendChild(e); return e; }
  for (var i = 0; i < n; i++) for (var j = i + 1; j < n; j++) PAIRS.push([i, j]);
  PAIRS.forEach(function (p, k) { var r = el('path', 'u391-rb', rbs); r.setAttribute('fill', COL[p[0]]); r.addEventListener('pointerenter', function () { setHov({ r: k }); }); r.addEventListener('pointerleave', function () { setHov(null); }); RB.push(r); });
  NAME.forEach(function (nm, i) { var a = el('path', 'u391-ar', ars); a.setAttribute('fill', COL[i]); a.addEventListener('pointerenter', function () { setHov({ g: i }); }); a.addEventListener('pointerleave', function () { setHov(null); }); AR.push(a); var t = el('text', 'u391-tx', txs); t.textContent = nm; TX.push(t); });
  function pt(a, r) { return (CX + r * Math.sin(a)).toFixed(2) + ' ' + (CY - r * Math.cos(a)).toFixed(2); }
  function layout() {
    var tot = 0; cur.forEach(function (r) { r.forEach(function (v) { tot += v; }); });
    var k = (2 * Math.PI - n * PAD) / tot * grow, a = 0, G = [], S = [];
    for (var i = 0; i < n; i++) {
      var g0 = a; S[i] = [];
      for (var t = 1; t <= n - 1; t++) { var j = (i + t) % n, w = cur[i][j] * k; S[i][j] = [a, a + w]; a += w; }
      G.push([g0, a]); a += PAD * grow;
    }
    return { G: G, S: S };
  }
  function paint() {
    var L = layout();
    L.G.forEach(function (g, i) {
      var big = g[1] - g[0] > Math.PI ? 1 : 0;
      AR[i].setAttribute('d', 'M' + pt(g[0], R1) + ' A' + R1 + ' ' + R1 + ' 0 ' + big + ' 1 ' + pt(g[1], R1) + ' L' + pt(g[1], R0) + ' A' + R0 + ' ' + R0 + ' 0 ' + big + ' 0 ' + pt(g[0], R0) + ' Z');
      var m = (g[0] + g[1]) / 2, x = CX + (R1 + 10) * Math.sin(m), y = CY - (R1 + 10) * Math.cos(m);
      TX[i].setAttribute('x', x.toFixed(1)); TX[i].setAttribute('y', (y + 3.5 + (Math.cos(m) < -0.6 ? 6 : Math.cos(m) > 0.6 ? -2 : 0)).toFixed(1));
      TX[i].setAttribute('text-anchor', Math.sin(m) > 0.25 ? 'start' : Math.sin(m) < -0.25 ? 'end' : 'middle');
      TX[i].style.opacity = grow;
    });
    PAIRS.forEach(function (p, k) {
      var s = L.S[p[0]][p[1]], t = L.S[p[1]][p[0]];
      RB[k].setAttribute('d', 'M' + pt(s[0], R0) + ' A' + R0 + ' ' + R0 + ' 0 0 1 ' + pt(s[1], R0) + ' Q' + CX + ' ' + CY + ' ' + pt(t[0], R0) + ' A' + R0 + ' ' + R0 + ' 0 0 1 ' + pt(t[1], R0) + ' Q' + CX + ' ' + CY + ' ' + pt(s[0], R0) + ' Z');
      RB[k].setAttribute('fill', COL[cur[p[0]][p[1]] >= cur[p[1]][p[0]] ? p[0] : p[1]]);
    });
    if (hov) setHov(hov, true);
  }
  function setHov(h, quiet) {
    hov = h; root.classList.toggle('is-f', !!h);
    AR.forEach(function (a, i) { a.classList.toggle('is-hl', !!h && (h.g === i || (h.r != null && PAIRS[h.r].indexOf(i) >= 0))); });
    RB.forEach(function (r, k) { r.classList.toggle('is-hl', !!h && (h.r === k || (h.g != null && PAIRS[k].indexOf(h.g) >= 0))); });
    if (!h) { info.textContent = 'Hover an arc or a ribbon'; return; }
    if (h.g != null) { var sent = 0, got = 0; for (var j = 0; j < n; j++) { sent += cur[h.g][j]; got += cur[j][h.g]; } info.textContent = NAME[h.g] + ' · sent ' + Math.round(sent) + ' · received ' + Math.round(got); }
    else { var p = PAIRS[h.r]; info.textContent = NAME[p[0]] + ' → ' + NAME[p[1]] + ' ' + Math.round(cur[p[0]][p[1]]) + '  ·  ' + NAME[p[1]] + ' → ' + NAME[p[0]] + ' ' + Math.round(cur[p[1]][p[0]]); }
  }
  var tw = 0;
  function morph(to) {
    var from = cur.map(function (r) { return r.slice(); }), t0 = performance.now();
    cancelAnimationFrame(tw);
    (function f(now) {
      var k = rm ? 1 : Math.min(1, (now - t0) / 800), e = k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
      cur = from.map(function (r, i) { return r.map(function (v, j) { return v + (M[to][i][j] - v) * e; }); });
      paint(); if (k < 1) tw = requestAnimationFrame(f);
    })(t0);
  }
  mos.forEach(function (b, i) { b.addEventListener('click', function () { mos.forEach(function (x, j) { x.classList.toggle('is-on', j === i); x.setAttribute('aria-pressed', j === i); }); morph(i); }); });
  if (!rm && 'IntersectionObserver' in window) {
    var done = false, io = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting || done) return; done = true; io.disconnect();
      var t0 = performance.now();
      (function f(now) { var k = Math.min(1, (now - t0) / 1100); grow = 1 - Math.pow(1 - k, 3); paint(); if (k < 1) requestAnimationFrame(f); })(t0);
    });
    io.observe(root);
  } else grow = 1;
  paint(); setHov(null);
})();
</script>
--- Code end ---

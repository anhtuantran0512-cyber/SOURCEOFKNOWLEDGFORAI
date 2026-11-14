---
source: "lucianlabs"
id: "336"
title: "Bottom sheet with three detents"
category: "App Screens"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#336"
tags: ["bottom-sheet", "detents", "spring", "velocity", "mobile"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Bottom sheet with three detents (336, App Screens)
[What it does] Drag the bottom sheet over the map and it tracks your finger, then carries the release velocity into the nearest of three heights — collapsed, half or full — overshooting slightly like a spring before settling. Drag past the ends and it resists like a rubber band; open it fully and the map behind shrinks a little and dims.
[How to use it] Drag or fling the top of the sheet. Tap the handle to step through heights

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
<!-- Lucian UX/UI Prompt #336 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#336 -->
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
.u336{position:relative;width:300px;height:500px;border-radius:36px;background:#0B0C10;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden;--p:0}
.u336-map{position:absolute;inset:0;border-radius:36px;overflow:hidden;background:color-mix(in srgb,var(--ux-surface-2) 82%,#8CE99A);transform:scale(calc(1 - .07 * var(--p)));transform-origin:50% 0}
.u336-map svg{position:absolute;inset:0;width:100%;height:100%}
.u336-pin{position:absolute;width:26px;height:26px;margin:-26px 0 0 -13px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:var(--ux-accent);box-shadow:0 4px 8px -2px rgba(0,0,0,.35)}
.u336-pin::after{content:"";position:absolute;inset:8px;border-radius:50%;background:#fff}
.u336-pin.on{background:#F03E3E;animation:u336-b .7s cubic-bezier(.3,1.6,.5,1)}
@keyframes u336-b{0%{translate:0 0}35%{translate:0 -16px}100%{translate:0 0}}
.u336-dim{position:absolute;inset:0;background:#000;opacity:calc(.4 * var(--p));pointer-events:none}
.u336-sh{position:absolute;left:0;right:0;top:0;height:500px;border-radius:26px 26px 0 0;background:var(--ux-surface);box-shadow:0 -8px 30px -10px rgba(0,0,0,.35);will-change:transform}
.u336-hd{position:relative;padding:22px 20px 10px;display:flex;align-items:baseline;gap:8px;touch-action:none;cursor:grab;user-select:none}
.u336-hd b{font-size:19px;font-weight:880;letter-spacing:-.03em;color:var(--ux-ink)}
.u336-hd span{font-size:12.5px;font-weight:700;color:var(--ux-ink-3)}
.u336-gr{position:absolute;left:50%;top:4px;width:60px;height:18px;margin-left:-30px;border:0;padding:0;background:none;border-radius:9px}
.u336-gr::before{content:"";position:absolute;left:12px;right:12px;top:7px;height:5px;border-radius:3px;background:var(--ux-line-2)}
.u336-gr:focus-visible{outline:2px solid var(--ux-accent)}
.u336-sr{margin:0 16px;height:40px;display:flex;align-items:center;gap:8px;padding:0 14px;border-radius:12px;background:var(--ux-surface-2);color:var(--ux-ink-3);font-size:13.5px;font-weight:600}
.u336-sr svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round}
.u336-ls{list-style:none;margin:10px 0 0;padding:0 8px}
.u336-it{width:100%;display:flex;align-items:center;gap:12px;padding:9px 10px;border:0;border-radius:14px;background:none;text-align:left;color:var(--ux-ink)}
.u336-it:hover{background:var(--ux-surface-2)}
.u336-it i{flex:none;width:42px;height:42px;border-radius:12px;background:var(--c)}
.u336-it b{display:block;font-size:14px;font-weight:780}
.u336-it small{display:block;margin-top:2px;font-size:12px;color:var(--ux-ink-3)}
.u336-it em{margin-left:auto;font-style:normal;font-size:12.5px;font-weight:800;color:#E8590C}
</style>
<div class="ux u336">
  <div class="u336-map" aria-hidden="true">
    <svg viewBox="0 0 300 500" preserveAspectRatio="none"><path d="M-10 120 Q80 100 150 150 T310 170" stroke="var(--ux-surface)" stroke-width="16" fill="none"/><path d="M90 -10 L120 510" stroke="var(--ux-surface)" stroke-width="12" fill="none"/><path d="M-10 330 L310 280" stroke="var(--ux-surface)" stroke-width="10" fill="none"/><path d="M220 -10 Q200 250 250 510" stroke="var(--ux-surface)" stroke-width="8" fill="none"/><path d="M0 420 Q120 380 300 460 L300 500 L0 500Z" fill="color-mix(in srgb,var(--ux-surface-2) 40%,#74C0FC)"/><rect x="140" y="190" width="60" height="60" rx="14" fill="color-mix(in srgb,var(--ux-surface-2) 50%,#51CF66)"/></svg>
  </div>
  <div class="u336-dim"></div>
  <section class="u336-sh" aria-label="Cafés nearby">
    <div class="u336-hd"><button class="u336-gr" type="button"></button><b>Cafés nearby</b><span>8 places</span></div>
    <div class="u336-sr"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="5"/><path d="M11 11l3 3"/></svg>Search by name or menu</div>
    <ul class="u336-ls"></ul>
  </section>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sh = root.querySelector('.u336-sh'), hd = root.querySelector('.u336-hd'), gr = root.querySelector('.u336-gr'), ls = root.querySelector('.u336-ls'), map = root.querySelector('.u336-map');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NAMES = ['collapsed', 'half', 'full'];
  var CAFE = [['Corner Roastery', '3 min walk', '4.8'], ['Green Garden Café', '5 min walk', '4.6'], ['Dawn Bakery', '6 min walk', '4.9'], ['Slow Afternoon', '8 min walk', '4.5'], ['Bookshop Coffee', '9 min walk', '4.7'], ['Hilltop Tea House', '12 min walk', '4.4'], ['Ocean Latte', '14 min walk', '4.3'], ['Little Station', '15 min walk', '4.6']];
  var COL = ['#FFA94D', '#69DB7C', '#FFD43B', '#B197FC', '#74C0FC', '#F783AC', '#63E6BE', '#FF8787'];
  var PIN = [[70, 150], [180, 110], [130, 260], [240, 220], [60, 340]];
  var DET = [384, 250, 56];
  var y = DET[0], vy = 0, target = DET[0], det = 0, raf = 0, last = 0;
  var pins = PIN.map(function (p) { var i = document.createElement('i'); i.className = 'u336-pin'; i.style.left = p[0] + 'px'; i.style.top = p[1] + 'px'; map.appendChild(i); return i; });
  CAFE.forEach(function (c, i) {
    var li = document.createElement('li'), b = document.createElement('button');
    b.type = 'button'; b.className = 'u336-it';
    b.innerHTML = '<i style="--c:' + COL[i] + '"></i><span><b></b><small></small></span><em></em>';
    b.querySelector('b').textContent = c[0]; b.querySelector('small').textContent = c[1]; b.querySelector('em').textContent = '★ ' + c[2];
    b.addEventListener('click', function () {
      pins.forEach(function (p, k) { p.classList.remove('on'); if (k === i % pins.length) { void p.offsetWidth; p.classList.add('on'); } });
      snap(1);
    });
    li.appendChild(b); ls.appendChild(li);
  });
  function paint() {
    sh.style.transform = 'translateY(' + y.toFixed(1) + 'px)';
    root.style.setProperty('--p', Math.max(0, Math.min(1, (DET[1] - y) / (DET[1] - DET[2]))).toFixed(3));
  }
  function label() { gr.setAttribute('aria-label', 'Change sheet height, now ' + NAMES[det]); }
  function step(now) {
    raf = 0;
    if (!root.isConnected) return;
    var dt = Math.min(0.032, Math.max(0, (now - last) / 1000)); last = now;
    vy += (-320 * (y - target) - 25 * vy) * dt;
    y += vy * dt;
    if (Math.abs(y - target) < 0.3 && Math.abs(vy) < 6) { y = target; vy = 0; paint(); return; }
    paint();
    raf = requestAnimationFrame(step);
  }
  function run() { if (rm) { y = target; vy = 0; paint(); return; } if (!raf) { last = performance.now(); raf = requestAnimationFrame(step); } }
  function snap(d) { det = Math.max(0, Math.min(2, d)); target = DET[det]; label(); run(); }
  var on = false, sy = 0, y0 = 0, k = 1, moved = false, hist = [], dragEnd = 0;
  function band(v) { if (v < DET[2]) return DET[2] - (DET[2] - v) * 0.25; if (v > DET[0]) return DET[0] + (v - DET[0]) * 0.25; return v; }
  hd.addEventListener('pointerdown', function (e) {
    on = true; moved = false; var r = root.getBoundingClientRect(); k = root.offsetHeight / (r.height || 1);
    sy = e.clientY; y0 = y; vy = 0; hist = [[performance.now(), y]];
    if (raf) { cancelAnimationFrame(raf); raf = 0; }
    try { hd.setPointerCapture(e.pointerId); } catch (er) {  }
  });
  hd.addEventListener('pointermove', function (e) {
    if (!on) return;
    var raw = y0 + (e.clientY - sy) * k;
    if (Math.abs(raw - y0) > 4) moved = true;
    y = band(raw); paint();
    hist.push([performance.now(), y]); if (hist.length > 6) hist.shift();
  });
  function up() {
    if (!on) return;
    on = false;
    if (!moved) { target = DET[det]; run(); return; }
    dragEnd = performance.now();
    var a = hist[0], b = hist[hist.length - 1], dt = (b[0] - a[0]) / 1000;
    vy = dt > 0.001 ? (b[1] - a[1]) / dt : 0;
    var proj = y + vy * 0.2, best = 0;
    DET.forEach(function (d, i) { if (Math.abs(d - proj) < Math.abs(DET[best] - proj)) best = i; });
    snap(best);
  }
  hd.addEventListener('pointerup', up);
  hd.addEventListener('pointercancel', up);
  gr.addEventListener('click', function () { if (performance.now() - dragEnd < 350) return; snap(det === 2 ? 0 : det + 1); });
  gr.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowUp') { e.preventDefault(); snap(det + 1); }
    if (e.key === 'ArrowDown') { e.preventDefault(); snap(det - 1); }
  });
  label(); paint();
})();
</script>
--- Code end ---

---
source: "lucianlabs"
id: "345"
title: "Spin-and-open soda can"
category: "Commerce & Pricing"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#345"
tags: ["can", "cylinder", "3d", "canvas", "product"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Spin-and-open soda can (345, Commerce & Pricing)
[What it does] A label wrapped around a round can bends along the cylinder as it turns, narrowing and darkening toward the edges for a sense of volume. Drag sideways and it spins with your hand, coasting to a stop when you let go. Change the flavor with the chips below to swap the label colors and fruit, and press Open to lift the tab as fizzy bubbles rise.
[How to use it] Drag the can sideways to spin it, then change the flavor or open it

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
<!-- Lucian UX/UI Prompt #345 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#345 -->
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
.u345{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--bg,#FFF9DB);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);transition:background .5s}
.u345-cv{position:absolute;inset:0;width:100%;height:100%;touch-action:none;cursor:grab}
.u345-cv:active{cursor:grabbing}
.u345-ui{position:absolute;left:0;right:0;bottom:14px;display:flex;justify-content:center;gap:6px}
.u345-ch,.u345-op{border:0;padding:6px 12px;border-radius:999px;background:rgba(255,255,255,.75);color:#343A40;font:inherit;font-size:11.5px;font-weight:750;cursor:pointer;box-shadow:0 0 0 1px rgba(0,0,0,.06);transition:background .2s,color .2s}
.u345-ch[aria-pressed="true"]{background:#343A40;color:#fff}
.u345-op{background:#fff;margin-left:8px}
.u345-ch:focus-visible,.u345-op:focus-visible{outline:2px solid #343A40;outline-offset:2px}
</style>
<div class="ux u345">
  <canvas class="u345-cv" role="img" aria-label="Soda can, drag sideways to spin"></canvas>
  <div class="u345-ui"><div role="group" aria-label="Choose a flavor" style="display:flex;gap:4px" class="u345-chs"></div><button type="button" class="u345-op">Open</button></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var cv = root.querySelector('.u345-cv'), cx = cv.getContext('2d'), chs = root.querySelector('.u345-chs'), opb = root.querySelector('.u345-op');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var W = 340, H = 340, dpr = Math.min(2, window.devicePixelRatio || 1), CXp = 170, R = 62, TOP = 62, BOT = 268;
  cv.width = W * dpr; cv.height = H * dpr; cx.scale(dpr, dpr);
  var FL = [['Lemon', 'LEMON'], ['Cherry', 'CHERRY'], ['Mint', 'MINT']];
  var TH = [{ a: '#FFD43B', b: '#F59F00', c: '#2B8A3E', bg: '#FFF9DB' }, { a: '#FA5252', b: '#C92A2A', c: '#2B8A3E', bg: '#FFF0F6' }, { a: '#63E6BE', b: '#0CA678', c: '#087F5B', bg: '#E6FCF5' }];
  var LW = Math.round(2 * Math.PI * R), LH = BOT - TOP, fi = 0, lab = null;
  function label() {
    var c = document.createElement('canvas'); c.width = LW * dpr; c.height = LH * dpr; var g = c.getContext('2d'); g.scale(dpr, dpr);
    var th = TH[fi];
    var bg = g.createLinearGradient(0, 0, 0, LH); bg.addColorStop(0, th.a); bg.addColorStop(1, th.b); g.fillStyle = bg; g.fillRect(0, 0, LW, LH);
    g.fillStyle = 'rgba(255,255,255,.22)'; for (var k = 0; k < 40; k++) { g.beginPath(); g.arc((k * 97) % LW, (k * 53) % LH, 2 + (k % 5), 0, 6.2832); g.fill(); }
    g.fillStyle = '#fff'; g.fillRect(0, 60, LW, 46);
    g.save(); g.fillStyle = th.b; g.font = '900 30px system-ui,-apple-system,sans-serif'; g.textBaseline = 'middle';
    [0, LW / 2].forEach(function (x0) { g.textAlign = 'left'; g.fillText('LUCIAN', x0 + 18, 84); });
    g.restore();
    g.fillStyle = '#fff'; g.font = '800 15px system-ui,-apple-system,sans-serif'; g.textAlign = 'center';
    [LW * 0.27, LW * 0.77].forEach(function (x) { g.fillText(FL[fi][1] + ' SODA', x, 132); });
    [LW * 0.27, LW * 0.77].forEach(function (x) {
      if (fi === 0) { g.fillStyle = '#FFF3BF'; g.beginPath(); g.ellipse(x, 168, 20, 15, 0.3, 0, 6.2832); g.fill(); g.strokeStyle = th.b; g.lineWidth = 2; g.stroke(); g.fillStyle = th.c; g.beginPath(); g.ellipse(x + 14, 150, 8, 4, -0.6, 0, 6.2832); g.fill(); }
      else if (fi === 1) { g.strokeStyle = '#2B8A3E'; g.lineWidth = 2; g.beginPath(); g.moveTo(x - 10, 162); g.quadraticCurveTo(x, 140, x + 4, 146); g.moveTo(x + 12, 164); g.quadraticCurveTo(x + 6, 144, x + 4, 146); g.stroke(); g.fillStyle = '#fff'; [[-10, 170], [12, 172]].forEach(function (p) { g.beginPath(); g.arc(x + p[0], p[1], 11, 0, 6.2832); g.fill(); }); g.fillStyle = '#E03131'; [[-10, 170], [12, 172]].forEach(function (p) { g.beginPath(); g.arc(x + p[0], p[1], 9, 0, 6.2832); g.fill(); }); }
      else { g.fillStyle = '#fff'; [[-12, 166, -0.6], [0, 160, 0], [12, 166, 0.6]].forEach(function (p) { g.save(); g.translate(x + p[0], p[1]); g.rotate(p[2]); g.beginPath(); g.ellipse(0, 0, 7, 15, 0, 0, 6.2832); g.fill(); g.restore(); }); }
    });
    g.fillStyle = 'rgba(255,255,255,.75)'; g.font = '700 8px system-ui,-apple-system,sans-serif'; g.textAlign = 'left';
    g.fillText('355 ml · 0 kcal', LW * 0.52, 196);
    lab = c;
  }
  var rot = 0.4, vel = 0.5, tab = 0, tabT = 0, bub = [], t = 0;
  function draw() {
    cx.clearRect(0, 0, W, H);
    cx.fillStyle = 'rgba(0,0,0,.13)'; cx.beginPath(); cx.ellipse(CXp, BOT + 16, R + 14, 12, 0, 0, 6.2832); cx.fill();
    for (var x = -R; x < R; x += 1.5) {
      var th = Math.asin(Math.max(-1, Math.min(1, (x + 0.75) / R))), u = ((th + rot) / (2 * Math.PI) % 1 + 1) % 1 * LW;
      cx.drawImage(lab, u * dpr, 0, 1.5 * dpr, LH * dpr, CXp + x, TOP, 1.6, LH);
    }
    var sh = cx.createLinearGradient(CXp - R, 0, CXp + R, 0);
    sh.addColorStop(0, 'rgba(0,0,0,.42)'); sh.addColorStop(0.18, 'rgba(0,0,0,.05)'); sh.addColorStop(0.32, 'rgba(255,255,255,.38)'); sh.addColorStop(0.42, 'rgba(255,255,255,.04)'); sh.addColorStop(0.8, 'rgba(0,0,0,.12)'); sh.addColorStop(1, 'rgba(0,0,0,.5)');
    cx.fillStyle = sh; cx.fillRect(CXp - R, TOP, R * 2, LH);
    function rim(y, h, top) {
      var mg = cx.createLinearGradient(CXp - R, 0, CXp + R, 0); mg.addColorStop(0, '#6C757D'); mg.addColorStop(0.3, '#F1F3F5'); mg.addColorStop(0.55, '#ADB5BD'); mg.addColorStop(1, '#495057');
      cx.fillStyle = mg; cx.beginPath(); cx.moveTo(CXp - R, y); cx.lineTo(CXp - R + (top ? 6 : 8), y + (top ? -h : h)); cx.lineTo(CXp + R - (top ? 6 : 8), y + (top ? -h : h)); cx.lineTo(CXp + R, y); cx.closePath(); cx.fill();
    }
    rim(TOP, 12, true); rim(BOT, 10, false);
    cx.fillStyle = '#ADB5BD'; cx.beginPath(); cx.ellipse(CXp, BOT + 10, R - 8, 6, 0, 0, Math.PI); cx.fill();
    var ty = TOP - 12;
    cx.fillStyle = '#DEE2E6'; cx.beginPath(); cx.ellipse(CXp, ty, R - 6, 13, 0, 0, 6.2832); cx.fill();
    cx.strokeStyle = '#ADB5BD'; cx.lineWidth = 2; cx.beginPath(); cx.ellipse(CXp, ty, R - 9, 11, 0, 0, 6.2832); cx.stroke();
    cx.fillStyle = tab > 0.5 ? '#212529' : '#CED4DA'; cx.beginPath(); cx.ellipse(CXp + 14, ty - 1, 12, 5, 0, 0, 6.2832); cx.fill();
    cx.save(); cx.translate(CXp - 2, ty); cx.scale(1, 1 - tab * 0.0); cx.rotate(-tab * 0.5);
    cx.fillStyle = '#E9ECEF'; cx.strokeStyle = '#868E96'; cx.lineWidth = 1.2;
    cx.beginPath(); cx.ellipse(-8, -tab * 10, 14, 6 + tab * 4, 0, 0, 6.2832); cx.fill(); cx.stroke();
    cx.fillStyle = '#ADB5BD'; cx.beginPath(); cx.ellipse(-10, -tab * 10, 6, 2.4 + tab * 1.6, 0, 0, 6.2832); cx.fill();
    cx.restore();
    bub.forEach(function (b) { cx.strokeStyle = 'rgba(255,255,255,' + (b.a * 0.9).toFixed(2) + ')'; cx.fillStyle = 'rgba(255,255,255,' + (b.a * 0.25).toFixed(2) + ')'; cx.lineWidth = 1.2; cx.beginPath(); cx.arc(b.x, b.y, b.r, 0, 6.2832); cx.fill(); cx.stroke(); });
  }
  var vis = true, raf = 0, last = 0, drag = null;
  function frame(now) {
    raf = 0;
    if (!root.isConnected || !vis) return;
    var dt = Math.min(0.05, Math.max(0, (now - last) / 1000)); last = now; t += dt;
    if (!drag) { vel += (0.5 - vel) * Math.min(1, dt * 0.8); rot += vel * dt; }
    tab += (tabT - tab) * Math.min(1, dt * 9);
    if (tabT && Math.random() < dt * 30) bub.push({ x: CXp + 14 + (Math.random() - 0.5) * 16, y: TOP - 14, r: 2 + Math.random() * 4, vy: -60 - Math.random() * 90, vx: (Math.random() - 0.5) * 40, a: 1 });
    bub.forEach(function (b) { b.y += b.vy * dt; b.x += b.vx * dt + Math.sin(t * 8 + b.r) * 0.3; b.a -= dt * 0.7; });
    bub = bub.filter(function (b) { return b.a > 0; });
    draw();
    raf = requestAnimationFrame(frame);
  }
  function run() { if (rm) { tab = tabT; draw(); return; } if (!raf && vis) { last = performance.now(); raf = requestAnimationFrame(frame); } }
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; run(); }).observe(root);
  FL.forEach(function (f, i) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'u345-ch'; b.textContent = f[0]; b.setAttribute('aria-pressed', i === 0 ? 'true' : 'false');
    b.addEventListener('click', function () { fi = i; label(); root.style.setProperty('--bg', TH[i].bg); [].forEach.call(chs.children, function (c, j) { c.setAttribute('aria-pressed', j === i ? 'true' : 'false'); }); vel += 3; run(); });
    chs.appendChild(b);
  });
  opb.addEventListener('click', function () { tabT = tabT ? 0 : 1; opb.textContent = tabT ? 'Reseal' : 'Open'; run(); });
  function loc(e) { var r = cv.getBoundingClientRect(), k = cv.offsetWidth / (r.width || 1); return (e.clientX - r.left) * k; }
  cv.addEventListener('pointerdown', function (e) { var x = loc(e); drag = { x: x, r: rot, lx: x, lt: performance.now() }; try { cv.setPointerCapture(e.pointerId); } catch (_) {} });
  cv.addEventListener('pointermove', function (e) {
    if (!drag) return;
    var x = loc(e), nt = performance.now();
    rot = drag.r - (x - drag.x) / R; vel = -(x - drag.lx) / R / Math.max(0.008, (nt - drag.lt) / 1000); drag.lx = x; drag.lt = nt;
    if (rm) draw();
  });
  function end() { if (!drag) return; drag = null; vel = Math.max(-12, Math.min(12, vel)); }
  cv.addEventListener('pointerup', end); cv.addEventListener('pointercancel', end);
  label(); draw(); run();
})();
</script>
--- Code end ---

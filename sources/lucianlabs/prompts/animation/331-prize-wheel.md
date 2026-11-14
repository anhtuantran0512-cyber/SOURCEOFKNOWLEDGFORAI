---
source: "lucianlabs"
id: "331"
title: "Flick-to-spin prize wheel"
category: "Promos & Rewards"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#331"
tags: ["wheel", "spin", "flick", "game", "prize"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Flick-to-spin prize wheel (331, Promos & Rewards)
[What it does] Flick the eight-slice prize wheel with your hand or press Spin and it whirls fast before friction gradually slows it down. The pointer at the top clicks back each time a slice boundary passes, and when it stops the winning slice glows as the result rises. The harder you flick, the longer it spins.
[How to use it] Drag to flick the wheel, or press the Spin button

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
<!-- Lucian UX/UI Prompt #331 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#331 -->
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
.u331{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:radial-gradient(90% 80% at 50% 35%,#5F3DC4,#2B1A6B 75%);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:#fff}
.u331-wh{position:absolute;left:50%;top:40px;width:240px;height:240px;margin-left:-120px;border-radius:50%;cursor:grab;touch-action:none;filter:drop-shadow(0 14px 20px rgba(0,0,0,.45))}
.u331-wh:active{cursor:grabbing}
.u331-wh svg{width:100%;height:100%;display:block}
.u331-pt{position:absolute;left:50%;top:26px;width:26px;height:36px;margin-left:-13px;transform-origin:50% 8px;pointer-events:none;filter:drop-shadow(0 3px 3px rgba(0,0,0,.4))}
.u331-ft{position:absolute;left:0;right:0;bottom:16px;display:flex;align-items:center;justify-content:center;gap:12px}
.u331-go{border:0;padding:9px 20px;border-radius:999px;background:#FCC419;color:#2B1A6B;font:inherit;font-size:13px;font-weight:900;cursor:pointer;box-shadow:0 6px 0 #E67700}
.u331-go:active{transform:translateY(3px);box-shadow:0 3px 0 #E67700}
.u331-go:focus-visible{outline:2px solid #fff;outline-offset:3px}
.u331-rs{min-width:96px;font-size:13px;font-weight:800;opacity:0;transform:translateY(6px);transition:opacity .3s,transform .4s cubic-bezier(.3,1.6,.5,1)}
.u331-rs.is-on{opacity:1;transform:none}
</style>
<div class="ux u331">
  <div class="u331-wh" role="img" aria-label="Prize wheel, drag to flick"><svg viewBox="-120 -120 240 240" aria-hidden="true"><g class="u331-rot"></g></svg></div>
  <svg class="u331-pt" viewBox="0 0 26 36" aria-hidden="true"><circle cx="13" cy="8" r="7" fill="#F8F9FA"/><path d="M5 10 L13 34 L21 10 Z" fill="#F8F9FA"/><circle cx="13" cy="8" r="3" fill="#FA5252"/></svg>
  <div class="u331-ft"><button type="button" class="u331-go">Spin</button><div class="u331-rs" aria-live="polite"></div></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var wh = root.querySelector('.u331-wh'), g = wh.querySelector('.u331-rot'), pt = root.querySelector('.u331-pt'), go = root.querySelector('.u331-go'), rs = root.querySelector('.u331-rs');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var SEG = ['Coffee', 'Miss', 'Cookie', 'Sticker', 'Miss', '10%', 'Cake', 'Again'];
  var COL = ['#FF6B6B', '#495057', '#FCC419', '#51CF66', '#868E96', '#4DABF7', '#F783AC', '#9775FA'], N = 8, R = 112;
  var h = '';
  SEG.forEach(function (s, i) {
    var a0 = (i / N) * 2 * Math.PI - Math.PI / 2, a1 = ((i + 1) / N) * 2 * Math.PI - Math.PI / 2, am = (a0 + a1) / 2;
    h += '<path class="u331-s" d="M0 0 L' + (Math.cos(a0) * R).toFixed(2) + ' ' + (Math.sin(a0) * R).toFixed(2) + ' A' + R + ' ' + R + ' 0 0 1 ' + (Math.cos(a1) * R).toFixed(2) + ' ' + (Math.sin(a1) * R).toFixed(2) + ' Z" fill="' + COL[i] + '" stroke="#fff" stroke-width="2"/>';
    h += '<text transform="rotate(' + (am * 180 / Math.PI + 90).toFixed(2) + ') translate(0 -74)" text-anchor="middle" font-size="13" font-weight="900" fill="#fff" font-family="system-ui,-apple-system,sans-serif">' + s + '</text>';
  });
  for (var k = 0; k < N; k++) { var a = (k / N) * 2 * Math.PI - Math.PI / 2; h += '<circle cx="' + (Math.cos(a) * (R - 6)).toFixed(2) + '" cy="' + (Math.sin(a) * (R - 6)).toFixed(2) + '" r="3" fill="#FFF3BF"/>'; }
  h += '<circle r="' + (R + 4) + '" fill="none" stroke="#FFD43B" stroke-width="8"/><circle r="22" fill="#fff"/><circle r="12" fill="#FCC419"/>';
  g.innerHTML = h;
  var segs = g.querySelectorAll('.u331-s');
  var ang = 0, vel = 0, flap = 0, raf = 0, last = 0, spinning = false, lastSeg = 0;
  function apply() { g.setAttribute('transform', 'rotate(' + ang.toFixed(2) + ')'); pt.style.transform = 'rotate(' + flap.toFixed(1) + 'deg)'; }
  function under() { var a = ((-ang % 360) + 360) % 360; return Math.floor(a / (360 / N)) % N; }
  function frame(now) {
    raf = 0;
    if (!root.isConnected) return;
    var dt = Math.min(0.033, Math.max(0, (now - last) / 1000)); last = now;
    if (!drag) {
      vel *= Math.pow(0.42, dt); if (Math.abs(vel) < 260) vel -= Math.sign(vel) * 60 * dt;
      ang += vel * dt;
    }
    var seg = Math.floor(ang / (360 / N));
    if (seg !== lastSeg) { flap = Math.max(-28, Math.min(28, -Math.sign(vel || 1) * Math.min(28, 8 + Math.abs(vel) / 40))); lastSeg = seg; }
    flap *= Math.pow(0.0005, dt);
    apply();
    if (!drag && spinning && Math.abs(vel) < 6) { spinning = false; vel = 0; finish(); }
    if (drag || spinning || Math.abs(flap) > 0.3) raf = requestAnimationFrame(frame);
  }
  function kick() { if (!raf) { last = performance.now(); raf = requestAnimationFrame(frame); } }
  function finish() {
    var i = under();
    [].forEach.call(segs, function (s, j) { s.style.filter = j === i ? 'brightness(1.25) drop-shadow(0 0 6px #fff)' : 'brightness(.75)'; });
    rs.textContent = 'Result: ' + SEG[i]; rs.classList.add('is-on');
  }
  function start(v) {
    [].forEach.call(segs, function (s) { s.style.filter = ''; }); rs.classList.remove('is-on');
    if (rm) { ang += Math.sign(v) * (720 + Math.random() * 360); apply(); finish(); return; }
    vel = v; spinning = true; kick();
  }
  go.addEventListener('click', function () { if (spinning) return; start(900 + Math.random() * 500); });
  var drag = null;
  function angAt(e) { var r = wh.getBoundingClientRect(); return Math.atan2(e.clientY - (r.top + r.height / 2), e.clientX - (r.left + r.width / 2)) * 180 / Math.PI; }
  wh.addEventListener('pointerdown', function (e) { drag = { la: angAt(e), hist: [[performance.now(), ang]] }; spinning = false; vel = 0; rs.classList.remove('is-on'); [].forEach.call(segs, function (s) { s.style.filter = ''; }); try { wh.setPointerCapture(e.pointerId); } catch (_) {} kick(); });
  wh.addEventListener('pointermove', function (e) {
    if (!drag) return;
    var a = angAt(e), d = a - drag.la; if (d > 180) d -= 360; if (d < -180) d += 360;
    drag.la = a; ang += d; drag.hist.push([performance.now(), ang]); if (drag.hist.length > 40) drag.hist.shift(); if (rm) apply();
  });
  function end() {
    if (!drag) return;
    var h2 = drag.hist, now = performance.now(), j = h2.length - 1; while (j > 0 && now - h2[j][0] < 120) j--;
    var v = (ang - h2[j][1]) / Math.max(0.05, (now - h2[j][0]) / 1000); drag = null;
    if (Math.abs(v) > 120) start(Math.max(-1800, Math.min(1800, v * 1.3))); else kick();
  }
  wh.addEventListener('pointerup', end); wh.addEventListener('pointercancel', end);
  apply();
})();
</script>
--- Code end ---

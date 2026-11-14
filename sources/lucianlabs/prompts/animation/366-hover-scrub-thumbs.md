---
source: "lucianlabs"
id: "366"
title: "Hover-scrub video previews"
category: "Cursor & Hover"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#366"
tags: ["video", "scrub", "thumbnail", "hover", "preview"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Hover-scrub video previews (366, Cursor & Hover)
[What it does] Move the cursor left and right over a thumbnail in a video list and the scene inside steps back and forth with your position, letting you skim a sunrise, a bike ride and a blooming flower. A progress bar fills beneath the thumbnail and the scene's timestamp floats above the cursor; when the cursor leaves, it returns to the cover frame.
[How to use it] Move the cursor slowly side to side over a thumbnail

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
<!-- Lucian UX/UI Prompt #366 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#366 -->
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
.u366{position:relative;width:300px;height:480px;border-radius:32px;overflow:hidden;background:#F8F9FB;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:#1B1E28;padding:18px 16px}
.u366-hd{font-size:16px;font-weight:850;letter-spacing:-.02em;margin:2px 4px 12px}
.u366-ls{display:flex;flex-direction:column;gap:12px}
.u366-it{display:flex;gap:10px;align-items:flex-start}
.u366-th{position:relative;width:146px;height:92px;flex:none;border-radius:12px;overflow:hidden;background:#000;cursor:ew-resize;touch-action:pan-y;outline:none}
.u366-th:focus-visible{box-shadow:0 0 0 3px #4C6EF5}
.u366-th canvas{width:100%;height:100%;display:block}
.u366-du{position:absolute;right:6px;bottom:8px;padding:1px 5px;border-radius:4px;background:rgba(0,0,0,.7);color:#fff;font:700 9.5px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;transition:opacity .2s}
.u366-bar{position:absolute;left:0;right:0;bottom:0;height:3px;background:rgba(255,255,255,.3);opacity:0;transition:opacity .2s}
.u366-bar i{display:block;height:100%;width:0;background:#FA5252}
.u366-tip{position:absolute;top:6px;left:0;padding:2px 6px;border-radius:5px;background:rgba(0,0,0,.75);color:#fff;font:700 9.5px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;transform:translateX(-50%);opacity:0;transition:opacity .15s;pointer-events:none}
.u366-th.is-on .u366-bar,.u366-th.is-on .u366-tip{opacity:1}
.u366-th.is-on .u366-du{opacity:0}
.u366-tx b{display:block;font-size:13px;font-weight:800;line-height:1.3;word-break:keep-all}
.u366-tx span{display:block;margin-top:3px;font-size:10.5px;font-weight:600;color:#7A7F92;word-break:keep-all}
</style>
<div class="ux u366"><div class="u366-hd">Recommended</div><div class="u366-ls"></div></div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ls = root.querySelector('.u366-ls');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var VID = [['Sunrise time-lapse', '3 minutes of sun rising over the sea', 192], ['Bike commute', 'A morning ride along the river', 254], ['The moment it blooms', 'Six hours in one minute', 61]];
  var dpr = Math.min(2, window.devicePixelRatio || 1), W = 146, H = 92;
  function mix(a, b, t) { return 'rgb(' + a.map(function (v, i) { return Math.round(v + (b[i] - v) * t); }).join(',') + ')'; }
  var SCENES = [
    function (g, t) {
      var sk = g.createLinearGradient(0, 0, 0, H); sk.addColorStop(0, mix([20, 24, 60], [120, 190, 255], t)); sk.addColorStop(1, mix([90, 50, 90], [255, 214, 165], t));
      g.fillStyle = sk; g.fillRect(0, 0, W, H);
      var sy = 70 - t * 52; g.fillStyle = mix([255, 120, 80], [255, 240, 200], t); g.beginPath(); g.arc(W / 2, sy, 11 + t * 2, 0, 6.2832); g.fill();
      g.fillStyle = mix([20, 30, 70], [40, 110, 190], t); g.fillRect(0, 64, W, H - 64);
      g.fillStyle = 'rgba(255,230,180,' + (0.3 + t * 0.4).toFixed(2) + ')'; for (var k = 0; k < 5; k++) g.fillRect(W / 2 - 18 + k * 2, 68 + k * 5, 36 - k * 4, 1.6);
    },
    function (g, t) {
      g.fillStyle = '#BDE0FE'; g.fillRect(0, 0, W, H);
      var off = t * 260;
      g.fillStyle = '#95D5B2'; for (var k = -1; k < 6; k++) { var x = ((k * 46 - off * 0.4) % 276 + 276) % 276 - 40; g.beginPath(); g.arc(x, 56, 26, Math.PI, 0); g.fill(); }
      g.fillStyle = '#4DABF7'; g.fillRect(0, 62, W, 10);
      g.fillStyle = '#ADB5BD'; g.fillRect(0, 72, W, 20);
      g.fillStyle = '#F8F9FA'; for (var j = -1; j < 8; j++) { var lx = ((j * 24 - off) % 192 + 192) % 192 - 24; g.fillRect(lx, 81, 12, 2); }
      var bx = 18 + t * 104, by = 70, wr = 7, rot = t * 40;
      g.strokeStyle = '#212529'; g.lineWidth = 1.6;
      [bx - 10, bx + 10].forEach(function (cx0) { g.beginPath(); g.arc(cx0, by, wr, 0, 6.2832); g.stroke(); g.beginPath(); g.moveTo(cx0 + Math.cos(rot) * wr, by + Math.sin(rot) * wr); g.lineTo(cx0 - Math.cos(rot) * wr, by - Math.sin(rot) * wr); g.stroke(); });
      g.beginPath(); g.moveTo(bx - 10, by); g.lineTo(bx - 2, by - 10); g.lineTo(bx + 10, by); g.lineTo(bx - 2, by); g.closePath(); g.moveTo(bx - 2, by - 10); g.lineTo(bx + 6, by - 12); g.stroke();
      g.fillStyle = '#FA5252'; g.beginPath(); g.ellipse(bx - 1, by - 20, 4, 7, 0.3, 0, 6.2832); g.fill();
      g.fillStyle = '#FFD8A8'; g.beginPath(); g.arc(bx + 1, by - 30, 4, 0, 6.2832); g.fill();
    },
    function (g, t) {
      var bg = g.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, '#2B2D42'); bg.addColorStop(1, '#141522'); g.fillStyle = bg; g.fillRect(0, 0, W, H);
      g.strokeStyle = '#51CF66'; g.lineWidth = 3; g.beginPath(); g.moveTo(W / 2, H); g.quadraticCurveTo(W / 2 - 4, 70, W / 2, 46); g.stroke();
      g.fillStyle = '#40C057'; g.beginPath(); g.ellipse(W / 2 - 12, 74, 11, 4, -0.5, 0, 6.2832); g.fill();
      var open = t * t * (3 - 2 * t), n = 7;
      for (var k = 0; k < n; k++) {
        var a = k / n * Math.PI * 2 - Math.PI / 2, len = 6 + open * 16, wd = 3 + open * 5;
        g.save(); g.translate(W / 2, 40); g.rotate(a * open + (1 - open) * (-Math.PI / 2 + (k - 3) * 0.08));
        g.fillStyle = 'hsl(' + (330 + k * 4) + ',80%,' + (55 + open * 15) + '%)'; g.beginPath(); g.ellipse(len * 0.6, 0, len * 0.6, wd, 0, 0, 6.2832); g.fill(); g.restore();
      }
      g.fillStyle = '#FFD43B'; g.beginPath(); g.arc(W / 2, 40, 2 + open * 4, 0, 6.2832); g.fill();
    }
  ];
  function fmt(s) { s = Math.round(s); return Math.floor(s / 60) + ':' + ('0' + s % 60).slice(-2); }
  VID.forEach(function (v, i) {
    var it = document.createElement('div'); it.className = 'u366-it';
    it.innerHTML = '<div class="u366-th" tabindex="0" role="slider" aria-valuemin="0" aria-valuemax="' + v[2] + '" aria-valuenow="0"><canvas></canvas><span class="u366-du">' + fmt(v[2]) + '</span><span class="u366-bar"><i></i></span><span class="u366-tip"></span></div><div class="u366-tx"><b>' + v[0] + '</b><span>' + v[1] + '</span></div>';
    ls.appendChild(it);
    var th = it.querySelector('.u366-th'), c = th.querySelector('canvas'), g = c.getContext('2d'), bar = th.querySelector('.u366-bar i'), tip = th.querySelector('.u366-tip');
    th.setAttribute('aria-label', v[0] + ' preview, skim side to side');
    c.width = W * dpr; c.height = H * dpr; g.scale(dpr, dpr);
    var COVER = [0.85, 0.45, 0.95][i], cur = COVER, want = COVER, raf = 0;
    function paint(t) { SCENES[i](g, t); }
    function frame() { raf = 0; cur += (want - cur) * (rm ? 1 : 0.35); if (Math.abs(want - cur) < 0.002) cur = want; paint(cur); if (cur !== want) raf = requestAnimationFrame(frame); }
    function to(t, on) {
      want = t; th.classList.toggle('is-on', on);
      if (on) { bar.style.width = (t * 100).toFixed(1) + '%'; tip.textContent = fmt(t * v[2]); tip.style.left = Math.max(18, Math.min(W - 18, t * W)) + 'px'; th.setAttribute('aria-valuenow', Math.round(t * v[2])); }
      if (!raf) raf = requestAnimationFrame(frame);
    }
    th.addEventListener('pointermove', function (e) { var r = th.getBoundingClientRect(); to(Math.max(0, Math.min(1, (e.clientX - r.left) / r.width)), true); });
    th.addEventListener('pointerleave', function () { to(COVER, false); });
    th.addEventListener('keydown', function (e) { var d = { ArrowRight: 0.1, ArrowLeft: -0.1 }[e.key]; if (d === undefined) return; e.preventDefault(); to(Math.max(0, Math.min(1, (th.classList.contains('is-on') ? want : 0) + d)), true); });
    th.addEventListener('blur', function () { to(COVER, false); });
    paint(COVER);
  });
})();
</script>
--- Code end ---

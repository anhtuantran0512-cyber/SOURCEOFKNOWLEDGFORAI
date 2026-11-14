---
source: "lucianlabs"
id: "191"
title: "Event replay tape"
category: "Workflow & Systems"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#191"
tags: ["event-replay", "session-replay", "timeline", "scrub", "debugging"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Event replay tape (191, Workflow & Systems)
[What it does] A player that replays recorded user input on a tiny sign-up screen. Press play and the cursor glides exactly as recorded, pressing fields and typing one character at a time, with a ripple wherever it clicks. The tape below color-codes moves, clicks and typing; drag the playhead to scrub back and forth, or press → to skip to the next event.
[How to use it] Press play, or drag along the tape to jump to any moment

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
<!-- Lucian UX/UI Prompt #191 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#191 -->
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
.u191{position:relative;width:340px;height:372px;padding:16px;box-sizing:border-box;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink);font-variant-numeric:tabular-nums}
.u191-ap{position:relative;height:184px;border-radius:14px;background:#fff;box-shadow:0 0 0 1px var(--ux-line-2),0 10px 20px -14px rgba(0,0,0,.35);overflow:hidden;color:#212529}
.u191-cr{display:flex;align-items:center;gap:5px;height:24px;padding:0 10px;background:#F1F3F5;border-bottom:1px solid #E9ECEF}
.u191-cr i{width:7px;height:7px;border-radius:50%;background:#FA5252}.u191-cr i:nth-child(2){background:#FCC419}.u191-cr i:nth-child(3){background:#51CF66}
.u191-cr span{margin-left:8px;flex:1;height:14px;border-radius:7px;background:#fff;font:600 9px/14px ui-monospace,SFMono-Regular,Menlo,monospace;color:#868E96;padding-left:8px}
.u191-ap h4{position:absolute;left:16px;top:32px;margin:0;font-size:13px;font-weight:850}
.u191-f{position:absolute;left:16px;width:276px;height:26px;border-radius:7px;box-shadow:inset 0 0 0 1.5px #DEE2E6;display:flex;align-items:center;padding:0 9px;font-size:11.5px;transition:box-shadow .2s}
.u191-f small{width:40px;flex:none;color:#868E96;font-weight:700}
.u191-f b{font-weight:600}
.u191-f.on{box-shadow:inset 0 0 0 2px #E8590C}
.u191-f.on b::after{content:"";display:inline-block;width:1.5px;height:12px;margin-left:1px;vertical-align:-2px;background:#E8590C;animation:u191-blink 1s steps(1) infinite}
@keyframes u191-blink{50%{opacity:0}}
.u191-ck{position:absolute;left:16px;top:130px;display:flex;align-items:center;gap:7px;font-size:11.5px;font-weight:650}
.u191-ck i{width:15px;height:15px;border-radius:4px;box-shadow:inset 0 0 0 1.5px #ADB5BD;display:grid;place-items:center;transition:background-color .2s,box-shadow .2s}
.u191-ck.on i{background:#E8590C;box-shadow:none}
.u191-ck i::after{content:"";width:7px;height:4px;border:solid #fff;border-width:0 0 2px 2px;transform:rotate(-45deg) translate(1px,-1px) scale(0);transition:transform .25s var(--ux-spring)}
.u191-ck.on i::after{transform:rotate(-45deg) translate(1px,-1px) scale(1)}
.u191-go{position:absolute;right:16px;top:124px;width:92px;height:28px;border-radius:8px;background:#212529;color:#fff;font-size:11.5px;font-weight:800;display:grid;place-items:center;transition:transform .15s}
.u191-go.press{transform:scale(.93)}
.u191-ok{position:absolute;left:50%;bottom:10px;transform:translate(-50%,20px);padding:6px 12px;border-radius:999px;background:#2B8A3E;color:#fff;font-size:11px;font-weight:800;opacity:0;transition:opacity .3s,transform .4s var(--ux-spring)}
.u191-ok.on{opacity:1;transform:translate(-50%,0)}
.u191-rp{position:absolute;width:34px;height:34px;margin:-17px 0 0 -17px;border-radius:50%;background:rgba(232,89,12,.35);pointer-events:none;opacity:0}
.u191-cu{position:absolute;left:0;top:0;width:16px;height:20px;pointer-events:none;filter:drop-shadow(0 2px 2px rgba(0,0,0,.3))}
.u191-tp{position:relative;height:46px;margin-top:12px;border-radius:12px;background:var(--ux-surface-2);touch-action:none;cursor:ew-resize}
.u191-tp:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u191-tp svg{position:absolute;left:12px;right:12px;top:0;width:calc(100% - 24px);height:30px;overflow:visible}
.u191-ph{position:absolute;top:4px;bottom:4px;width:2px;margin-left:-1px;background:var(--ux-ink);border-radius:1px;pointer-events:none}
.u191-ph::before{content:"";position:absolute;left:50%;top:-3px;width:10px;height:10px;margin-left:-5px;border-radius:50%;background:var(--ux-ink)}
.u191-lg{position:absolute;left:12px;bottom:5px;display:flex;gap:10px;font-size:9.5px;font-weight:750;color:var(--ux-ink-3)}
.u191-lg span::before{content:"";display:inline-block;width:8px;height:4px;margin-right:4px;border-radius:2px;vertical-align:1px;background:var(--c)}
.u191-ct{display:flex;align-items:center;gap:6px;margin-top:10px}
.u191-ct button{height:34px;min-width:34px;padding:0 8px;border:0;border-radius:10px;background:var(--ux-surface-2);color:var(--ux-ink);font-size:13px;font-weight:800;display:grid;place-items:center;transition:transform .25s var(--ux-spring)}
.u191-ct button:active{transform:scale(.92)}
.u191-ct .u191-pl{min-width:46px;background:var(--ux-ink);color:var(--ux-surface)}
.u191-ct button svg{width:14px;height:14px;fill:currentColor}
.u191-ct output{margin-left:auto;font:700 12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--ux-ink-2)}
.u191-ct button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
</style>
<div class="ux u191">
  <div class="u191-ap" role="img" aria-label="Recorded screen">
    <div class="u191-cr" aria-hidden="true"><i></i><i></i><i></i><span>lucian.app/signup</span></div>
    <h4>Create account</h4>
    <div class="u191-f" style="top:56px"><small>Name</small><b></b></div>
    <div class="u191-f" style="top:90px"><small>Email</small><b></b></div>
    <div class="u191-ck"><i></i>I agree to the terms</div>
    <div class="u191-go">Sign up</div>
    <div class="u191-ok">Signed up!</div>
    <i class="u191-rp"></i>
    <svg class="u191-cu" viewBox="0 0 16 20" aria-hidden="true"><path d="M1 1v15.5l4.2-4 2.7 6.3 2.6-1.1-2.7-6.2H14Z" fill="#212529" stroke="#fff" stroke-width="1.3" stroke-linejoin="round"/></svg>
  </div>
  <div class="u191-tp" role="slider" tabindex="0" aria-label="Playback position" aria-valuemin="0" aria-valuemax="7"><svg aria-hidden="true"></svg><i class="u191-ph"></i><div class="u191-lg" aria-hidden="true"><span style="--c:var(--ux-ink-3)">Move</span><span style="--c:#E8590C">Click</span><span style="--c:#3D8BFF">Type</span></div></div>
  <div class="u191-ct"><button class="u191-rs" type="button" aria-label="Restart"><svg viewBox="0 0 14 14"><path d="M2 2h2v10H2zM12 2v10L5 7z"/></svg></button><button class="u191-pl" type="button"></button><button class="u191-nx" type="button" aria-label="Next event"><svg viewBox="0 0 14 14"><path d="M2 2v10l7-5zM10 2h2v10h-2z"/></svg></button><button class="u191-sp" type="button" aria-label="Playback speed">1×</button><output></output></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var fields = Array.prototype.slice.call(root.querySelectorAll('.u191-f')), ck = root.querySelector('.u191-ck'), go = root.querySelector('.u191-go'), ok = root.querySelector('.u191-ok');
  var cu = root.querySelector('.u191-cu'), rp = root.querySelector('.u191-rp'), tp = root.querySelector('.u191-tp'), tsvg = tp.querySelector('svg'), ph = root.querySelector('.u191-ph');
  var pl = root.querySelector('.u191-pl'), nx = root.querySelector('.u191-nx'), spb = root.querySelector('.u191-sp'), out = root.querySelector('.u191-ct output');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NAME = 'Minji Kim', MAIL = 'minji@lucian.app', T = 7000, NS = 'http://www.w3.org/2000/svg';
  var EV = [
    ['move', 300, 1000, [70, 70]], ['click', 1080, 1080, [70, 70]], ['type', 1200, 1800, [0, NAME]],
    ['move', 1900, 2450, [80, 104]], ['click', 2520, 2520, [80, 104]], ['type', 2650, 4200, [1, MAIL]],
    ['move', 4300, 4900, [24, 138]], ['click', 4980, 4980, [24, 138]],
    ['move', 5100, 5700, [244, 139]], ['click', 5780, 5780, [244, 139]]
  ];
  var t = 0, playing = false, speed = 1, raf = 0, last = 0;
  function ease(k) { return k < 0.5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; }
  function stateAt(t) {
    var s = { cx: 250, cy: 160, text: ['', ''], focus: -1, check: false, done: false, ripple: null, press: false };
    EV.forEach(function (e) {
      if (t < e[1]) return;
      var k = e[2] > e[1] ? Math.min(1, (t - e[1]) / (e[2] - e[1])) : 1;
      if (e[0] === 'move') { var sx = s.cx, sy = s.cy, q = ease(k); s.cx = sx + (e[3][0] - sx) * q; s.cy = sy + (e[3][1] - sy) * q; }
      if (e[0] === 'click') {
        s.cx = e[3][0]; s.cy = e[3][1];
        if (t - e[1] < 450) s.ripple = [e[3][0], e[3][1], (t - e[1]) / 450];
        if (e[3][1] < 90) s.focus = 0; else if (e[3][1] < 120) s.focus = 1; else s.focus = -1;
        if (e[3][0] < 60 && e[3][1] > 120) s.check = !s.check;
        if (e[3][0] > 180) { s.done = true; s.press = t - e[1] < 150; }
      }
      if (e[0] === 'type') s.text[e[3][0]] = e[3][1].slice(0, Math.round(k * e[3][1].length));
    });
    return s;
  }
  function render() {
    var s = stateAt(t);
    cu.style.transform = 'translate(' + (s.cx - 1).toFixed(1) + 'px,' + (s.cy - 1).toFixed(1) + 'px)';
    fields.forEach(function (f, i) { f.querySelector('b').textContent = s.text[i]; f.classList.toggle('on', s.focus === i); });
    ck.classList.toggle('on', s.check);
    go.classList.toggle('press', s.press);
    ok.classList.toggle('on', s.done);
    if (s.ripple && !rm) { rp.style.left = s.ripple[0] + 'px'; rp.style.top = s.ripple[1] + 'px'; rp.style.opacity = (1 - s.ripple[2]).toFixed(2); rp.style.transform = 'scale(' + (0.3 + s.ripple[2]).toFixed(2) + ')'; }
    else rp.style.opacity = '0';
    ph.style.left = (12 + t / T * (tp.offsetWidth - 24 || 284)).toFixed(1) + 'px';
    out.value = (t / 1000).toFixed(1) + ' / ' + (T / 1000).toFixed(1) + 's';
    tp.setAttribute('aria-valuenow', (t / 1000).toFixed(1));
    pl.innerHTML = playing ? '<svg viewBox="0 0 14 14"><path d="M3 2h3v10H3zM8 2h3v10H8z"/></svg>' : '<svg viewBox="0 0 14 14"><path d="M3 1.5v11l9-5.5z"/></svg>';
    pl.setAttribute('aria-label', playing ? 'Pause' : 'Play');
  }
  (function tape() {
    var W = 284;
    EV.forEach(function (e) {
      var x0 = e[1] / T * W, x1 = e[2] / T * W, el;
      if (e[0] === 'move') { el = document.createElementNS(NS, 'line'); el.setAttribute('x1', x0); el.setAttribute('x2', x1); el.setAttribute('y1', 15); el.setAttribute('y2', 15); el.setAttribute('stroke', 'var(--ux-ink-3)'); el.setAttribute('stroke-width', 2); el.setAttribute('stroke-dasharray', '2 3'); }
      if (e[0] === 'type') { el = document.createElementNS(NS, 'rect'); el.setAttribute('x', x0); el.setAttribute('width', Math.max(3, x1 - x0)); el.setAttribute('y', 11); el.setAttribute('height', 8); el.setAttribute('rx', 4); el.setAttribute('fill', '#3D8BFF'); }
      if (e[0] === 'click') { el = document.createElementNS(NS, 'circle'); el.setAttribute('cx', x0); el.setAttribute('cy', 15); el.setAttribute('r', 4.5); el.setAttribute('fill', '#E8590C'); el.setAttribute('stroke', 'var(--ux-surface-2)'); el.setAttribute('stroke-width', 2); }
      tsvg.appendChild(el);
    });
    tsvg.setAttribute('viewBox', '0 0 ' + W + ' 30');
  })();
  function step(now) {
    raf = 0;
    if (!root.isConnected || !playing) return;
    var dt = Math.max(0, Math.min(60, now - last)); last = now;
    t = Math.min(T, t + dt * speed);
    if (t >= T) playing = false;
    render();
    if (playing) raf = requestAnimationFrame(step);
  }
  function play(v) {
    playing = v;
    if (playing && t >= T) t = 0;
    if (playing && rm) { t = T; playing = false; }
    render();
    if (playing && !raf) { last = performance.now(); raf = requestAnimationFrame(step); }
  }
  pl.addEventListener('click', function () { play(!playing); });
  root.querySelector('.u191-rs').addEventListener('click', function () { t = 0; play(true); });
  nx.addEventListener('click', function () {
    playing = false;
    var n = EV.filter(function (e) { return e[0] !== 'move' && e[2] > t + 1; })[0];
    t = n ? n[2] + (n[0] === 'click' ? 200 : 0) : T;
    render();
  });
  spb.addEventListener('click', function () { speed = speed === 1 ? 2 : 1; spb.textContent = speed + '×'; });
  var on = false;
  function seek(e) { var r = tp.getBoundingClientRect(), k = tp.offsetWidth / (r.width || 1); t = Math.max(0, Math.min(T, ((e.clientX - r.left) * k - 12) / (tp.offsetWidth - 24) * T)); render(); }
  tp.addEventListener('pointerdown', function (e) { on = true; playing = false; seek(e); try { tp.setPointerCapture(e.pointerId); } catch (er) {  } });
  tp.addEventListener('pointermove', function (e) { if (on) seek(e); });
  tp.addEventListener('pointerup', function () { on = false; });
  tp.addEventListener('pointercancel', function () { on = false; });
  tp.addEventListener('keydown', function (e) {
    var d = e.key === 'ArrowRight' ? 250 : e.key === 'ArrowLeft' ? -250 : 0;
    if (e.key === ' ') { e.preventDefault(); play(!playing); return; }
    if (!d) return;
    e.preventDefault(); playing = false; t = Math.max(0, Math.min(T, t + d)); render();
  });
  render();
})();
</script>
--- Code end ---

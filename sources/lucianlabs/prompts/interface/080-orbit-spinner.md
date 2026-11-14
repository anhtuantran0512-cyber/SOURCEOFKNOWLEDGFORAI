---
source: "lucianlabs"
id: "080"
title: "Orbit sync spinner"
category: "Loading & Progress"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#080"
tags: ["spinner", "orbit", "sync", "loading", "success"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Orbit sync spinner (080, Loading & Progress)
[What it does] Planets circle three tilted orbits at different speeds while the core glows like it is breathing. The step text and counter change, and at the end the orbits are drawn into the core, which turns into a check as a ripple spreads.
[How to use it] Watch the sync finish. Repeat it with “Sync again”, and stop it with “Cancel” while it spins

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
<!-- Lucian UX/UI Prompt #080 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#080 -->
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
.u080{position:relative;width:340px;height:390px;display:flex;flex-direction:column;align-items:center;padding:26px 24px 22px;border-radius:30px;background:radial-gradient(80% 60% at 50% 35%,color-mix(in srgb,var(--ux-accent) 14%,transparent),transparent 70%),var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u080-sys{position:relative;width:230px;height:200px;flex:none}
.u080-o{position:absolute;left:50%;top:50%;width:var(--d);height:var(--d);margin:calc(var(--d) / -2) 0 0 calc(var(--d) / -2);transform:rotate(var(--t)) scaleY(.38);transition:transform .7s var(--ux-ease),opacity .5s}
.u080-o::before{content:"";position:absolute;inset:0;border-radius:50%;border:1.5px solid color-mix(in srgb,var(--ux-ink) 14%,transparent)}
.u080-p{position:absolute;left:0;top:0;width:var(--s);height:var(--s);margin:calc(var(--s) / -2) 0 0 calc(var(--s) / -2);border-radius:50%;background:var(--c);box-shadow:0 0 12px var(--c);transition:opacity .4s}
.u080.is-done .u080-p{opacity:0}
.u080-core{position:absolute;z-index:1;left:50%;top:50%;width:56px;height:56px;margin:-28px 0 0 -28px;border-radius:50%;background:radial-gradient(circle at 38% 32%,#fff,#B7A4FF 40%,#5B3FD9);box-shadow:0 0 30px color-mix(in srgb,var(--ux-accent) 60%,transparent);animation:u080-breath 2.2s ease-in-out infinite;display:grid;place-items:center;transition:background .5s,width .6s var(--ux-spring),height .6s var(--ux-spring),margin .6s var(--ux-spring)}
@keyframes u080-breath{50%{transform:scale(1.08);box-shadow:0 0 44px color-mix(in srgb,var(--ux-accent) 70%,transparent)}}
.u080-core svg{width:34px;height:34px;fill:none;stroke:#fff;stroke-width:3.2;stroke-linecap:round;stroke-linejoin:round}
.u080-core path{stroke-dasharray:30;stroke-dashoffset:30;transition:stroke-dashoffset .5s var(--ux-ease) .35s}
.u080-wave{position:absolute;left:50%;top:50%;width:84px;height:84px;margin:-42px 0 0 -42px;border-radius:50%;border:2px solid var(--ux-mint);opacity:0}
.u080.is-done .u080-o{transform:rotate(var(--t)) scaleY(.38) scale(0);opacity:0}
.u080.is-done .u080-core{width:84px;height:84px;margin:-42px 0 0 -42px;background:var(--ux-mint);box-shadow:0 0 0 0 transparent;animation:none}
.u080.is-done .u080-core path{stroke-dashoffset:0}
.u080.is-done .u080-wave{animation:u080-wave 1.1s var(--ux-ease) .3s 2}
@keyframes u080-wave{from{transform:scale(1);opacity:.7}to{transform:scale(2.4);opacity:0}}
.u080.is-paused .u080-core{animation-play-state:paused}
.u080-msg{width:100%;text-align:center}
.u080-t{position:relative;height:26px;width:100%;margin-top:14px;text-align:center}
.u080-t b{position:absolute;left:0;right:0;font-size:18px;font-weight:850;letter-spacing:-.04em;transition:opacity .3s,transform .45s var(--ux-spring)}
.u080-t b.out{opacity:0;transform:translateY(-10px)}
.u080-t b.in{opacity:0;transform:translateY(10px)}
.u080-sub{margin:4px 0 0;font-size:13px;font-weight:650;color:var(--ux-ink-3);font-variant-numeric:tabular-nums}
.u080-b{margin-top:auto;height:46px;padding:0 20px;border:0;border-radius:999px;background:var(--ux-surface-2);color:var(--ux-ink);font-size:14px;font-weight:750;transition:transform .3s var(--ux-spring),background-color .3s,color .3s}
.u080-b:active{transform:scale(.95)}
.u080-b:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u080.is-done .u080-b{background:var(--ux-ink);color:var(--ux-page)}
</style>
<div class="ux u080">
  <div class="u080-sys" aria-hidden="true">
    <div class="u080-o" style="--d:210px;--t:-18deg"></div>
    <div class="u080-o" style="--d:150px;--t:24deg"></div>
    <div class="u080-o" style="--d:100px;--t:-58deg"></div>
    <span class="u080-wave"></span>
    <span class="u080-core"><svg viewBox="0 0 34 34"><path d="M9 17.5l5.5 5.5L25.5 12"/></svg></span>
  </div>
  <div class="u080-msg" role="status" aria-live="polite"><div class="u080-t"><b>Connecting to server</b></div><p class="u080-sub">Hang on a moment</p></div>
  <button class="u080-b" type="button">Cancel</button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var tWrap = root.querySelector('.u080-t'), sub = root.querySelector('.u080-sub'), btn = root.querySelector('.u080-b');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var raf = 0, t0 = 0, acc = 0, state = 'run', step = -1;
  var sys = root.querySelector('.u080-sys'), core = root.querySelector('.u080-core');
  var O = [[105, -18, 5.5, '#22C3A6', 12], [75, 24, 3.6, '#FF6B8B', 10], [50, -58, 2.2, '#FFB547', 9]];
  var planets = [];
  O.forEach(function (o, i) {
    [0, Math.PI].forEach(function (ph, k) {
      var p = document.createElement('i');
      p.className = 'u080-p';
      p.style.setProperty('--c', o[3]); p.style.setProperty('--s', (k ? o[4] - 4 : o[4]) + 'px');
      if (k) p.style.opacity = '.7';
      sys.insertBefore(p, core);
      planets.push({ el: p, o: o, ph: ph + i });
    });
  });
  var orbitT = 0, lastF = performance.now();
  function orbit(now) {
    if (!root.isConnected) return;
    if (state === 'run' && !rm) orbitT += (now - lastF) / 1000;
    lastF = now;
    planets.forEach(function (p) {
      var o = p.o, a = p.ph + orbitT * Math.PI * 2 / o[2], tl = o[1] * Math.PI / 180;
      var x = Math.cos(a) * o[0], y = Math.sin(a) * o[0] * 0.38;
      var rx = x * Math.cos(tl) - y * Math.sin(tl), ry = x * Math.sin(tl) + y * Math.cos(tl);
      p.el.style.transform = 'translate(' + (115 + rx).toFixed(1) + 'px,' + (100 + ry).toFixed(1) + 'px)';
      p.el.style.zIndex = Math.sin(a) < 0 ? 0 : 2;
    });
    if (state !== 'done') requestAnimationFrame(orbit);
  }
  var STEPS = [[0, 'Connecting to server'], [0.18, 'Syncing files'], [0.86, 'Almost there']], DUR = 5200, TOTAL = 340;
  function title(txt) {
    var old = tWrap.querySelector('b:not(.out)'), b = document.createElement('b');
    b.textContent = txt; b.className = 'in';
    tWrap.appendChild(b); void b.offsetWidth; b.className = '';
    if (old) { old.className = 'out'; setTimeout(function () { old.remove(); }, 450); }
  }
  function tick(now) {
    if (!root.isConnected || state !== 'run') return;
    var p = Math.min(1, (acc + now - t0) / (rm ? 1200 : DUR)), s = 0;
    STEPS.forEach(function (x, i) { if (p >= x[0]) s = i; });
    if (s !== step) { step = s; title(STEPS[s][1]); }
    sub.textContent = s === 0 ? 'Hang on a moment' : 'Files ' + Math.round(Math.min(1, (p - 0.18) / 0.8) * TOTAL) + ' / ' + TOTAL;
    if (p >= 1) { done(); return; }
    raf = requestAnimationFrame(tick);
  }
  function done() {
    state = 'done';
    root.classList.add('is-done');
    title('Sync complete');
    sub.textContent = TOTAL + ' files · just now';
    btn.textContent = 'Sync again';
  }
  function start() {
    cancelAnimationFrame(raf);
    root.classList.remove('is-done', 'is-paused');
    state = 'run'; step = -1; acc = 0; t0 = performance.now();
    btn.textContent = 'Cancel';
    raf = requestAnimationFrame(tick);
    lastF = performance.now(); requestAnimationFrame(orbit);
  }
  btn.addEventListener('click', function () {
    if (state === 'run') {
      state = 'stop'; cancelAnimationFrame(raf);
      root.classList.add('is-paused');
      title('Sync stopped'); sub.textContent = 'You can restart anytime';
      btn.textContent = 'Sync again';
    } else start();
  });
  start();
})();
</script>
--- Code end ---

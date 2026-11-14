---
source: "lucianlabs"
id: "224"
title: "AI answer with traceable sources"
category: "App Screens"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#224"
tags: ["ai", "citations", "sources", "answer", "search"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] AI answer with traceable sources (224, App Screens)
[What it does] Each sentence in an AI answer ends with a small numbered badge. Rest the pointer on a number and that sentence gets underlined while a source preview card floats above, highlighting the quoted part of the original, and the matching card in the source list below lifts up too. Rest the pointer on a source card and every sentence that used it is marked at once.
[How to use it] Rest the pointer on a sentence number or a source card below

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
<!-- Lucian UX/UI Prompt #224 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#224 -->
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
.u224{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u224-q{position:absolute;right:16px;top:16px;max-width:240px;padding:8px 12px;border-radius:14px 14px 4px 14px;background:var(--ux-ink);color:var(--ux-surface);font-size:11.5px;font-weight:750}
.u224-an{position:absolute;left:16px;right:16px;top:58px;font-size:12px;line-height:1.75;font-weight:600;color:var(--ux-ink-2)}
.u224-an>span{transition:color .2s,background-size .3s;background:linear-gradient(transparent 88%,color-mix(in srgb,var(--ux-accent) 70%,transparent) 88%) no-repeat 0 0/0 100%}
.u224-an>span.is-hl{color:var(--ux-ink);background-size:100% 100%}
.u224-ct{display:inline-grid;place-items:center;min-width:15px;height:15px;margin:0 1px;padding:0 3px;border:0;border-radius:5px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink-2);font:inherit;font-size:9px;font-weight:900;line-height:1;vertical-align:1px;cursor:pointer;transition:background .15s,color .15s}
.u224-ct.is-on{background:var(--ux-accent);color:#fff;box-shadow:none}
.u224-ct:focus-visible{outline:2px solid var(--ux-accent);outline-offset:1px}
.u224-pv{position:absolute;z-index:3;width:218px;padding:10px 11px;border-radius:13px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 18px 34px -12px var(--ux-shadow-strong);transform:translate(-50%,calc(-100% - 6px)) scale(.94);transform-origin:50% 100%;opacity:0;pointer-events:none;transition:opacity .15s,transform .22s cubic-bezier(.3,1.5,.5,1)}
.u224-pv.is-on{opacity:1;transform:translate(-50%,calc(-100% - 6px))}
.u224-pv.is-below{transform:translate(-50%,24px) scale(.94);transform-origin:50% 0}
.u224-pv.is-below.is-on{transform:translate(-50%,24px)}
.u224-pv header{display:flex;align-items:center;gap:6px;font-size:9.5px;font-weight:800;color:var(--ux-ink-3)}
.u224-pv header i{width:16px;height:16px;border-radius:5px;display:grid;place-items:center;color:#fff;font-style:normal;font-size:9px;font-weight:900}
.u224-pv b{display:block;margin-top:5px;font-size:11px;font-weight:850}
.u224-pv p{margin:4px 0 0;font-size:10px;line-height:1.5;font-weight:600;color:var(--ux-ink-2)}
.u224-pv mark{background:color-mix(in srgb,#FACC15 50%,transparent);color:var(--ux-ink);border-radius:3px;padding:0 1px}
.u224-sr{position:absolute;left:16px;right:16px;bottom:16px}
.u224-sr>small{font-size:10px;font-weight:850;color:var(--ux-ink-3)}
.u224-sl{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:6px}
.u224-sc{padding:8px;border-radius:12px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line);cursor:pointer;transition:transform .25s cubic-bezier(.3,1.5,.5,1),box-shadow .2s,background .2s}
.u224-sc.is-on{transform:translateY(-4px);background:var(--ux-surface);box-shadow:0 0 0 1.5px var(--ux-accent),0 10px 20px -12px var(--ux-shadow-strong)}
.u224-sc header{display:flex;align-items:center;gap:5px}
.u224-sc header i{flex:none;width:16px;height:16px;border-radius:5px;display:grid;place-items:center;color:#fff;font-style:normal;font-size:9px;font-weight:900}
.u224-sc header em{font-style:normal;font-size:9px;font-weight:900;color:var(--ux-ink-3)}
.u224-sc b{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;margin-top:5px;font-size:10px;line-height:1.35;font-weight:800}
.u224-sc small{display:block;margin-top:3px;font-size:8.5px;font-weight:700;color:var(--ux-ink-3);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.u224-sc:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u224-an>span,.u224-pv,.u224-sc{transition:none}}
</style>
<div class="ux u224">
  <div class="u224-q">How do I raise landing page conversion?</div>
  <p class="u224-an" aria-live="off"></p>
  <div class="u224-sr"><small>Sources</small><div class="u224-sl"></div></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var an = root.querySelector('.u224-an'), sl = root.querySelector('.u224-sl');
  var A = [['Your first screen should say what you do in one sentence.', [1]], ['Button copy that promises an outcome beats a plain “Get started.”', [2]], ['Fewer sign-up fields is better; asking for just an email had the highest completion.', [2, 3]], ['Put real customer quotes and numbers close to the button.', [1]]];
  var SRC = [['L', 'lucianlabs.dev', 'Five habits of great landing pages', 'Visitors stay only if within 3 seconds they know ', 'what the product does', '.'], ['C', 'cro-weekly.com', '120 button copy tests', 'Copy that ', 'promised an outcome', ' got 31% more clicks than “Start free.”'], ['F', 'formlab.io', 'Sign-up form length report', 'Asking only for email ', 'had the highest completion', '.']];
  var COL = ['#6366F1', '#F59E0B', '#10B981'];
  var pv = document.createElement('div'); pv.className = 'u224-pv'; pv.setAttribute('role', 'tooltip'); pv.innerHTML = '<header><i></i><span></span></header><b></b><p></p>'; root.appendChild(pv);
  var SEN = [], CT = [];
  A.forEach(function (a, i) {
    var s = document.createElement('span'); s.textContent = a[0]; an.appendChild(s); SEN.push(s);
    a[1].forEach(function (n) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'u224-ct'; b.textContent = n; b.setAttribute('aria-label', SRC[n - 1][1] + ' — view source');
      b.addEventListener('pointerenter', function () { cite(b, i, n); }); b.addEventListener('focus', function () { cite(b, i, n); });
      b.addEventListener('pointerleave', clear); b.addEventListener('blur', clear);
      an.appendChild(b); CT.push(b);
    });
    an.appendChild(document.createTextNode(' '));
  });
  var SC = SRC.map(function (s, k) {
    var c = document.createElement('div'); c.className = 'u224-sc'; c.tabIndex = 0;
    c.innerHTML = '<header><i style="background:' + COL[k] + '">' + s[0] + '</i><em>' + (k + 1) + '</em></header><b></b><small></small>'; c.querySelector('b').textContent = s[2]; c.querySelector('small').textContent = s[1];
    function on() { clear(); c.classList.add('is-on'); A.forEach(function (a, i) { if (a[1].indexOf(k + 1) >= 0) SEN[i].classList.add('is-hl'); }); CT.forEach(function (b) { b.classList.toggle('is-on', +b.textContent === k + 1); }); }
    c.addEventListener('pointerenter', on); c.addEventListener('focus', on); c.addEventListener('pointerleave', clear); c.addEventListener('blur', clear);
    sl.appendChild(c); return c;
  });
  function clear() { pv.classList.remove('is-on'); SEN.forEach(function (s) { s.classList.remove('is-hl'); }); CT.forEach(function (b) { b.classList.remove('is-on'); }); SC.forEach(function (c) { c.classList.remove('is-on'); }); }
  function cite(b, i, n) {
    clear(); var s = SRC[n - 1];
    SEN[i].classList.add('is-hl'); b.classList.add('is-on'); SC[n - 1].classList.add('is-on');
    pv.querySelector('i').textContent = s[0]; pv.querySelector('i').style.background = COL[n - 1]; pv.querySelector('header span').textContent = s[1]; pv.querySelector('b').textContent = s[2];
    var p = pv.querySelector('p'); p.innerHTML = ''; p.appendChild(document.createTextNode(s[3])); var m = document.createElement('mark'); m.textContent = s[4]; p.appendChild(m); p.appendChild(document.createTextNode(s[5]));
    var rr = root.getBoundingClientRect(), k = 340 / (rr.width || 340), br = b.getBoundingClientRect();
    var top = (br.top - rr.top) * k; pv.style.left = Math.max(125, Math.min(215, (br.left + br.width / 2 - rr.left) * k)) + 'px'; pv.style.top = top + 'px';
    pv.classList.toggle('is-below', top < 150);
    pv.classList.add('is-on');
  }
})();
</script>
--- Code end ---

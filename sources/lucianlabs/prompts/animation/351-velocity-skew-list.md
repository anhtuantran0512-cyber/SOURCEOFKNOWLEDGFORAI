---
source: "lucianlabs"
id: "351"
title: "List that leans with velocity"
category: "Scroll Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#351"
tags: ["scroll", "velocity", "skew", "physics", "list"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] List that leans with velocity (351, Scroll Motion)
[What it does] The faster you scroll the list, the more its cards lean in that direction and stretch slightly, then spring upright the moment you stop. Scrolling slowly barely tilts them so reading is undisturbed, and the gauge at the top shows the current speed.
[How to use it] Scroll inside the card fast, then slowly

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
<!-- Lucian UX/UI Prompt #351 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#351 -->
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
.u351{position:relative;width:340px;height:340px;display:flex;flex-direction:column;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden}
.u351-hd{display:flex;align-items:center;justify-content:space-between;padding:16px 18px 10px}
.u351-hd b{font-size:17px;font-weight:850}
.u351-g{display:flex;align-items:center;gap:8px;font-size:11px;font-weight:750;color:var(--ux-ink-3)}
.u351-g svg{width:44px;height:26px;overflow:visible}
.u351-g path{fill:none;stroke:var(--ux-line-2);stroke-width:4;stroke-linecap:round}
.u351-g line{stroke:var(--ux-danger);stroke-width:2.5;stroke-linecap:round;transform-box:view-box;transform-origin:22px 24px}
.u351-sc{flex:1;overflow-y:auto;padding:4px 16px 16px;scrollbar-width:none;outline:none}
.u351-sc::-webkit-scrollbar{display:none}
.u351-ls{margin:0;padding:0;list-style:none;display:grid;gap:10px;transform-origin:50% 50%;will-change:transform}
.u351-it{display:flex;align-items:center;gap:12px;height:68px;padding:0 14px;border-radius:18px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line)}
.u351-it i{flex:none;width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--a),var(--b))}
.u351-it b{display:block;font-size:14.5px;font-weight:780}
.u351-it span{font-size:12px;font-weight:650;color:var(--ux-ink-3)}
</style>
<div class="ux u351">
  <div class="u351-hd"><b>Weekend plans</b><span class="u351-g" aria-hidden="true">Scroll speed<svg viewBox="0 0 44 26"><path d="M4 24a18 18 0 0 1 36 0"/><line x1="22" y1="24" x2="22" y2="9"/></svg></span></div>
  <div class="u351-sc" tabindex="0" aria-label="Weekend plans"><ul class="u351-ls"></ul></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sc = root.querySelector('.u351-sc'), ls = root.querySelector('.u351-ls'), needle = root.querySelector('.u351-g line');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ITEMS = ['Seoul Forest walk', 'Euljiro film lab', 'Mangwon market tteokbokki', 'Seongsu studio visit', 'Han River sunset ride', 'Tea in Ikseon-dong', 'Bukchon alley photos', 'Yeonnam park picnic', 'Seochon bookshop tour', 'Namsan night walk'];
  var C = [['#FF8787', '#FFD43B'], ['#74C0FC', '#B197FC'], ['#63E6BE', '#4DABF7'], ['#FFA94D', '#F783AC'], ['#A9E34B', '#38D9A9']];
  ITEMS.forEach(function (t, i) {
    var li = document.createElement('li');
    li.className = 'u351-it';
    li.innerHTML = '<i style="--a:' + C[i % 5][0] + ';--b:' + C[i % 5][1] + '"></i><div><b></b><span>' + (1 + (i * 7) % 5) + '.' + (i * 3 % 10) + ' km · ' + (30 + i * 15) + ' min</span></div>';
    li.querySelector('b').textContent = t;
    ls.appendChild(li);
  });
  var lastY = 0, lastT = 0, vel = 0, skew = 0, sv = 0, raf = 0;
  sc.addEventListener('scroll', function () {
    var now = performance.now(), dt = Math.max(8, now - (lastT || now - 16));
    var v = (sc.scrollTop - lastY) / dt;
    lastY = sc.scrollTop; lastT = now;
    vel = vel * 0.6 + v * 0.4;
    if (!raf) raf = requestAnimationFrame(tick);
  }, { passive: true });
  function tick() {
    raf = 0;
    if (!root.isConnected) return;
    if (performance.now() - lastT > 60) vel *= 0.6;
    var target = rm ? 0 : Math.max(-10, Math.min(10, -vel * 3.2));
    sv += (target - skew) * 0.2; sv *= 0.72; skew += sv;
    ls.style.transform = 'skewY(' + skew.toFixed(2) + 'deg) scaleY(' + (1 + Math.min(0.06, Math.abs(skew) * 0.006)).toFixed(3) + ')';
    needle.style.transform = 'rotate(' + Math.max(-80, Math.min(80, -88 + Math.min(1, Math.abs(vel) / 3) * 176)).toFixed(1) + 'deg)';
    if (Math.abs(skew) > 0.02 || Math.abs(sv) > 0.02 || Math.abs(vel) > 0.01) raf = requestAnimationFrame(tick);
    else { ls.style.transform = ''; needle.style.transform = 'rotate(-88deg)'; }
  }
  needle.style.transform = 'rotate(-88deg)';
})();
</script>
--- Code end ---

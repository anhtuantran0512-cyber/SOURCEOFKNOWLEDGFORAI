---
source: "lucianlabs"
id: "306"
title: "Orbiting integrations"
category: "Sections & Content"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#306"
tags: ["integrations", "orbit", "logos", "hover", "landing"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Orbiting integrations (306, Sections & Content)
[What it does] In the middle of an integrations section sits the product logo, while tool icons such as mail, calendar and payments slowly circle it on an inner and an outer orbit, turning in opposite directions. The icons stay upright as they go, and resting the pointer on one stops the orbits, draws a line of flowing data between it and the center logo, and changes the caption above to that tool.
[How to use it] Rest the pointer on one of the orbiting icons

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
<!-- Lucian UX/UI Prompt #306 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#306 -->
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
.u306{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:radial-gradient(60% 50% at 50% 62%,var(--ux-accent-soft),transparent 75%),var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u306-hd{position:absolute;left:0;right:0;top:22px;z-index:3;text-align:center}
.u306-hd small{font-size:10px;font-weight:850;letter-spacing:.08em;color:var(--ux-accent)}
.u306-hd h3{margin:4px 0 0;font-size:19px;font-weight:900;letter-spacing:-.035em}
.u306-cp{display:block;height:16px;margin-top:6px;font-size:11px;font-weight:700;color:var(--ux-ink-2);transition:opacity .2s}
.u306-cp b{color:var(--ux-ink);font-weight:850}
.u306-st{position:absolute;left:50%;top:212px;width:0;height:0}
.u306-rg{position:absolute;left:0;top:0;width:0;height:0;animation:u306-r var(--t) linear infinite;animation-direction:var(--dir)}
.u306-rg::before{content:"";position:absolute;left:calc(var(--r) * -1);top:calc(var(--r) * -1);width:calc(var(--r) * 2);height:calc(var(--r) * 2);border-radius:50%;border:1px dashed color-mix(in srgb,var(--ux-ink) 16%,transparent)}
.u306.is-hold .u306-rg,.u306.is-hold .u306-up{animation-play-state:paused}
@keyframes u306-r{to{transform:rotate(360deg)}}
.u306-sl{position:absolute;left:0;top:0}
.u306-up{position:absolute;left:-19px;top:-19px;animation:u306-r var(--t) linear infinite;animation-direction:var(--rdir)}
.u306-ic{display:grid;place-items:center;width:38px;height:38px;padding:0;border:0;border-radius:12px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 8px 16px -8px var(--ux-shadow-strong);color:var(--c);cursor:pointer;transition:transform .3s cubic-bezier(.3,1.6,.5,1),box-shadow .3s}
.u306-ic svg{width:18px;height:18px}
.u306-ic.is-on{transform:scale(1.22);box-shadow:0 0 0 2px var(--c),0 10px 22px -8px var(--c)}
.u306-ic:focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
.u306-hb{position:absolute;left:-30px;top:-30px;width:60px;height:60px;border-radius:19px;background:var(--ux-grad);display:grid;place-items:center;box-shadow:0 14px 30px -10px color-mix(in srgb,var(--ux-accent) 70%,transparent);z-index:2}
.u306-hb::before{content:"";position:absolute;inset:-10px;border-radius:26px;border:2px solid color-mix(in srgb,var(--ux-accent) 40%,transparent);animation:u306-p 2.6s ease-out infinite}
@keyframes u306-p{from{transform:scale(.85);opacity:1}to{transform:scale(1.35);opacity:0}}
.u306-hb svg{width:28px;height:28px}
.u306-ln{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.u306-ln path{fill:none;stroke-width:2;stroke-linecap:round;stroke-dasharray:3 7;opacity:0;transition:opacity .25s}
.u306-ln path.is-on{opacity:1;animation:u306-fl .6s linear infinite}
@keyframes u306-fl{to{stroke-dashoffset:-10}}
@media (prefers-reduced-motion: reduce){.u306-rg,.u306-up,.u306-hb::before,.u306-ln path.is-on{animation:none}}
</style>
<div class="ux u306">
  <div class="u306-hd"><small>Integrations</small><h3>Connect the tools you use</h3><span class="u306-cp" aria-live="polite"></span></div>
  <svg class="u306-ln" viewBox="0 0 340 340" aria-hidden="true"><path d=""/></svg>
  <div class="u306-st"><div class="u306-hb" aria-hidden="true"><svg viewBox="0 0 28 28"><path d="M8 18.5c0-5 2.8-9 6-9s6 4 6 9" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/><circle cx="14" cy="9.5" r="3" fill="#fff"/></svg></div></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var st = root.querySelector('.u306-st'), cp = root.querySelector('.u306-cp'), ln = root.querySelector('.u306-ln path');
  var DEF = 'Connects to 40+ tools in a single click';
  var I = [['Mail', 'Turn inquiries into tasks', '#EF4444'], ['Calendar', 'Events stay in sync both ways', '#3B82F6'], ['Payments', 'Payments flow into revenue', '#8B5CF6'], ['Chat', 'Updates land in team channels', '#10B981'], ['Drive', 'Import whole folders of files', '#F59E0B'], ['Code repo', 'Link deploys to issues', '#334155'], ['Spreadsheets', 'Two-way table sync', '#16A34A'], ['Video calls', 'Meeting notes saved for you', '#0EA5E9'], ['Forms', 'Responses go to your contacts', '#EC4899'], ['Webhooks', 'Send events anywhere', '#F97316']];
  var ICO = [
    '<rect x="2.5" y="4.5" width="13" height="9.5" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 5.5l6 4.5 6-4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
    '<rect x="2.5" y="3.5" width="13" height="12" rx="2.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M2.5 7.5h13M6 2v3M12 2v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><rect x="5.5" y="10" width="3" height="2.6" rx=".6" fill="currentColor"/>',
    '<rect x="2" y="4" width="14" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M2 7.5h14" stroke="currentColor" stroke-width="2.2"/><path d="M4.5 11h3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
    '<path d="M3 4.5h12v8H8l-3.5 2.5V12.5H3z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M6 8.5h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
    '<path d="M6.5 3h5l4 7-2.5 4.5h-8L2.5 10z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M6.5 3l4 7h5M2.5 10l4-7" fill="none" stroke="currentColor" stroke-width="1.3"/>',
    '<path d="M6.5 5.5L3 9l3.5 3.5M11.5 5.5L15 9l-3.5 3.5M10 4l-2 10" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>',
    '<rect x="3" y="2.5" width="12" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 7h12M3 11h12M8 7v8.5" stroke="currentColor" stroke-width="1.4"/>',
    '<rect x="2" y="5" width="10" height="8" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 8l4-2.2v6.4L12 10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
    '<rect x="3.5" y="2.5" width="11" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M6 6.5h6M6 9.5h6M6 12.5h3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
    '<circle cx="9" cy="5" r="2.2" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="4.5" cy="13" r="2.2" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="13.5" cy="13" r="2.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 7l-2.5 4M10 7l2.5 4M6.7 13h4.6" stroke="currentColor" stroke-width="1.5"/>'
  ];
  var RINGS = [{ r: 62, t: 36, dir: 'normal', n: [0, 1, 2, 3], a0: 20 }, { r: 112, t: 56, dir: 'reverse', n: [4, 5, 6, 7, 8, 9], a0: 0 }];
  var B = [];
  RINGS.forEach(function (R) {
    var rg = document.createElement('div'); rg.className = 'u306-rg';
    rg.style.cssText = '--r:' + R.r + 'px;--t:' + R.t + 's;--dir:' + R.dir + ';--rdir:' + (R.dir === 'normal' ? 'reverse' : 'normal');
    R.n.forEach(function (n, k) {
      var a = R.a0 + k * 360 / R.n.length, sl = document.createElement('div'); sl.className = 'u306-sl';
      sl.style.transform = 'rotate(' + a + 'deg) translateX(' + R.r + 'px) rotate(' + -a + 'deg)';
      sl.innerHTML = '<div class="u306-up"><button type="button" class="u306-ic" style="--c:' + I[n][2] + '"><svg viewBox="0 0 18 18" aria-hidden="true">' + ICO[n] + '</svg></button></div>';
      var b = sl.querySelector('button'); b.setAttribute('aria-label', I[n][0]); b._n = n; B[n] = b;
      rg.appendChild(sl);
    });
    st.insertBefore(rg, st.firstChild);
  });
  cp.textContent = DEF;
  var on = null;
  function show(b) {
    if (on === b) return;
    if (on) on.classList.remove('is-on');
    on = b; root.classList.toggle('is-hold', !!b);
    if (!b) { ln.classList.remove('is-on'); cp.textContent = DEF; return; }
    b.classList.add('is-on');
    cp.innerHTML = '<b></b> · <span></span>'; cp.firstChild.textContent = I[b._n][0]; cp.lastChild.textContent = I[b._n][1];
    var rr = root.getBoundingClientRect(), k = 340 / (rr.width || 340), br = b.getBoundingClientRect();
    var x = (br.left + br.width / 2 - rr.left) * k, y = (br.top + br.height / 2 - rr.top) * k, cx = 170, cy = 212, mx = (x + cx) / 2 + (y - cy) * .18, my = (y + cy) / 2 - (x - cx) * .18;
    ln.setAttribute('d', 'M' + x.toFixed(1) + ' ' + y.toFixed(1) + ' Q' + mx.toFixed(1) + ' ' + my.toFixed(1) + ' ' + cx + ' ' + cy);
    ln.style.stroke = I[b._n][2]; ln.classList.add('is-on');
  }
  B.forEach(function (b) {
    b.addEventListener('pointerenter', function () { show(b); });
    b.addEventListener('pointerleave', function () { if (on === b) show(null); });
    b.addEventListener('focus', function () { show(b); });
    b.addEventListener('blur', function () { if (on === b) show(null); });
    b.addEventListener('click', function () { show(on === b ? null : b); });
  });
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { Array.prototype.forEach.call(root.querySelectorAll('.u306-rg,.u306-up'), function (el) { el.style.animationPlayState = es[0].isIntersecting ? '' : 'paused'; }); }).observe(root);
})();
</script>
--- Code end ---

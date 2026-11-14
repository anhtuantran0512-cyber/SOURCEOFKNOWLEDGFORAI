---
source: "lucianlabs"
id: "356"
title: "Watch under the loupe"
category: "Commerce & Pricing"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#356"
tags: ["magnifier", "loupe", "zoom", "product", "hover"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Watch under the loupe (356, Commerce & Pricing)
[What it does] Hover over a wristwatch photo and a round loupe follows the cursor, magnifying that spot so the dial's tiny lettering, tick marks and even the tip of the second hand come into sharp view. Each press switches between 2.5× and 4×, with the current power shown on the loupe's rim. The hands move with the real time.
[How to use it] Move the cursor over the watch, and press to change the magnification

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
<!-- Lucian UX/UI Prompt #356 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#356 -->
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
.u356{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:radial-gradient(90% 80% at 50% 40%,#F8F5EF,#E6DFD2);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong)}
.u356-st{position:absolute;inset:0;cursor:none;touch-action:none}
.u356-st>svg{position:absolute;inset:0;width:100%;height:100%}
.u356-lp{position:absolute;left:0;top:0;width:128px;height:128px;margin:-64px 0 0 -64px;border-radius:50%;overflow:hidden;pointer-events:none;opacity:0;transform:scale(.6);transition:opacity .2s,transform .3s cubic-bezier(.3,1.5,.5,1);box-shadow:0 0 0 5px #2C2C30,0 0 0 7px #8E8E96,0 18px 30px -8px rgba(0,0,0,.55);background:#F3EEE5}
.u356-lp.is-on{opacity:1;transform:scale(1)}
.u356-lp svg{position:absolute;left:0;top:0;width:340px;height:340px;transform-origin:0 0}
.u356-lp::after{content:"";position:absolute;inset:0;border-radius:50%;background:radial-gradient(circle at 30% 25%,rgba(255,255,255,.35),transparent 40%);box-shadow:inset 0 0 18px rgba(0,0,0,.35)}
.u356-zm{position:absolute;left:0;top:0;padding:2px 6px;border-radius:999px;background:#2C2C30;color:#F3EEE5;font:800 10px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;pointer-events:none;opacity:0;transform:translate(-50%,0);transition:opacity .2s}
.u356-zm.is-on{opacity:1}
</style>
<div class="ux u356">
  <div class="u356-st" role="img" aria-label="Wristwatch, magnify with the loupe">
    <svg viewBox="0 0 340 340" class="u356-w" aria-hidden="true">
      <defs>
        <radialGradient id="u356-dial" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#1E3A5F"/><stop offset="1" stop-color="#0B1626"/></radialGradient>
        <linearGradient id="u356-case" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F1F3F5"/><stop offset=".5" stop-color="#ADB5BD"/><stop offset="1" stop-color="#E9ECEF"/></linearGradient>
      </defs>
      <path d="M128 20 h84 l-6 70 h-72z M134 250 h72 l6 70 h-84z" fill="#6B4226"/>
      <path d="M140 30 v52 M200 30 v52 M140 258 v52 M200 258 v52" stroke="#4A2C17" stroke-width="1.2" stroke-dasharray="3 3"/>
      <circle cx="170" cy="170" r="92" fill="url(#u356-case)"/>
      <rect x="258" y="160" width="14" height="20" rx="3" fill="#ADB5BD"/>
      <circle cx="170" cy="170" r="80" fill="url(#u356-dial)"/>
      <g class="u356-ticks"></g>
      <text x="170" y="128" text-anchor="middle" font-family="Georgia,serif" font-size="9" font-weight="700" fill="#F1F3F5" letter-spacing="1.5">LUCIAN</text>
      <text x="170" y="136" text-anchor="middle" font-family="system-ui,sans-serif" font-size="3.2" fill="#ADB5BD" letter-spacing=".6">AUTOMATIC · GENÈVE</text>
      <text x="170" y="214" text-anchor="middle" font-family="system-ui,sans-serif" font-size="2.6" fill="#ADB5BD" letter-spacing=".5">25 JEWELS · 100M · SWISS MADE</text>
      <text x="170" y="219" text-anchor="middle" font-family="system-ui,sans-serif" font-size="1.8" fill="#868E96" letter-spacing=".3">N° 0400 / 2026 — made with care in Seoul</text>
      <rect x="214" y="164" width="16" height="12" rx="1.5" fill="#F8F9FA"/><text class="u356-dt" x="222" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="8" font-weight="700" fill="#212529">15</text>
      <g class="u356-hh"><path d="M168 172 L170 126 L172 172 Z" fill="#E9ECEF"/></g>
      <g class="u356-mh"><path d="M169 174 L170 104 L171 174 Z" fill="#F8F9FA"/></g>
      <g class="u356-sh"><path d="M169.6 186 L170 98 L170.4 186 Z" fill="#FF6B6B"/><circle cx="170" cy="98.5" r="1.2" fill="#FF6B6B"/></g>
      <circle cx="170" cy="170" r="3.4" fill="#ADB5BD"/><circle cx="170" cy="170" r="1.4" fill="#FF6B6B"/>
    </svg>
  </div>
  <div class="u356-lp" aria-hidden="true"></div>
  <div class="u356-zm" aria-hidden="true"></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var st = root.querySelector('.u356-st'), art = st.querySelector('svg'), lp = root.querySelector('.u356-lp'), zm = root.querySelector('.u356-zm');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var tk = art.querySelector('.u356-ticks'), h = '';
  for (var i = 0; i < 60; i++) {
    var a = i * 6 * Math.PI / 180, big = i % 5 === 0, r0 = big ? 66 : 72, r1 = 77;
    h += '<line x1="' + (170 + Math.sin(a) * r0).toFixed(2) + '" y1="' + (170 - Math.cos(a) * r0).toFixed(2) + '" x2="' + (170 + Math.sin(a) * r1).toFixed(2) + '" y2="' + (170 - Math.cos(a) * r1).toFixed(2) + '" stroke="#F1F3F5" stroke-width="' + (big ? 2 : 0.5) + '"/>';
    if (big) h += '<text x="' + (170 + Math.sin(a) * 58).toFixed(2) + '" y="' + (171.2 - Math.cos(a) * 58).toFixed(2) + '" text-anchor="middle" font-family="system-ui,sans-serif" font-size="3.2" fill="#ADB5BD">' + (i === 0 ? 60 : i) + '</text>';
  }
  tk.innerHTML = h;
  var uid = Math.random().toString(36).slice(2, 7);
  art.querySelectorAll('[id]').forEach(function (n) { var old = n.id; n.id = old + uid; art.querySelectorAll('[fill="url(#' + old + ')"]').forEach(function (m) { m.setAttribute('fill', 'url(#' + old + uid + ')'); }); });
  var big = art.cloneNode(true); big.removeAttribute('class');
  big.querySelectorAll('[id]').forEach(function (n) { var old = n.id; n.id = old + 'z'; big.querySelectorAll('[fill="url(#' + old + ')"]').forEach(function (m) { m.setAttribute('fill', 'url(#' + old + 'z)'); }); });
  lp.appendChild(big);
  var Z = [2.5, 4], zi = 0, pos = null;
  function hands() {
    var d = new Date(), s = d.getSeconds() + (rm ? 0 : d.getMilliseconds() / 1000), m = d.getMinutes() + s / 60, hr = (d.getHours() % 12) + m / 60;
    [art, big].forEach(function (g) {
      g.querySelector('.u356-sh').setAttribute('transform', 'rotate(' + (s * 6).toFixed(2) + ' 170 170)');
      g.querySelector('.u356-mh').setAttribute('transform', 'rotate(' + (m * 6).toFixed(2) + ' 170 170)');
      g.querySelector('.u356-hh').setAttribute('transform', 'rotate(' + (hr * 30).toFixed(2) + ' 170 170)');
      g.querySelector('.u356-dt').textContent = d.getDate();
    });
  }
  function place() {
    if (!pos) { lp.classList.remove('is-on'); zm.classList.remove('is-on'); return; }
    var z = Z[zi];
    lp.style.left = pos.x + 'px'; lp.style.top = pos.y + 'px';
    big.style.transform = 'translate(' + (64 - pos.x * z).toFixed(1) + 'px,' + (64 - pos.y * z).toFixed(1) + 'px) scale(' + z + ')';
    zm.textContent = z + '×'; zm.style.left = pos.x + 'px'; zm.style.top = (pos.y + 70) + 'px';
    lp.classList.add('is-on'); zm.classList.add('is-on');
  }
  var vis = true, raf = 0;
  function frame() { raf = 0; if (!root.isConnected || !vis) return; hands(); raf = requestAnimationFrame(frame); }
  function run() { if (rm) { hands(); return; } if (!raf && vis) raf = requestAnimationFrame(frame); }
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; run(); }).observe(root);
  function loc(e) { var r = st.getBoundingClientRect(), k = st.offsetWidth / (r.width || 1); return { x: (e.clientX - r.left) * k, y: (e.clientY - r.top) * k }; }
  st.addEventListener('pointermove', function (e) { pos = loc(e); place(); });
  st.addEventListener('pointerleave', function () { pos = null; place(); });
  st.addEventListener('click', function (e) { zi = (zi + 1) % Z.length; if (!pos) pos = loc(e); place(); });
  if (rm) setInterval(function () { if (root.isConnected) hands(); }, 1000);
  hands(); run();
})();
</script>
--- Code end ---

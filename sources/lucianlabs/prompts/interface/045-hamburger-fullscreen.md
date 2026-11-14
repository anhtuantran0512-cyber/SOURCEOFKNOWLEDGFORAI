---
source: "lucianlabs"
id: "045"
title: "Full-screen menu from the button"
category: "Menus & Tabs"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#045"
tags: ["hamburger", "menu", "fullscreen", "clip-path", "stagger", "focus-trap"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Full-screen menu from the button (045, Menus & Tabs)
[What it does] While the hamburger’s three lines fold into an ×, the menu screen spreads out as a circle from the button and covers the screen. The page behind steps back slightly, and the big menu words rise line by line.
[How to use it] Open and close the menu with the button in the top right. Esc closes it too, and while it is open Tab stays inside the menu

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
<!-- Lucian UX/UI Prompt #045 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#045 -->
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
.u045{position:relative;width:340px;height:520px;border-radius:34px;overflow:hidden;isolation:isolate;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong)}
.u045-page{position:absolute;inset:0;padding:78px 20px 20px;transform-origin:50% 0;transition:transform .7s var(--ux-ease),filter .7s var(--ux-ease)}
.u045.is-open .u045-page{transform:scale(.92) translateY(14px);filter:blur(3px)}
.u045-hero{position:relative;height:200px;border-radius:24px;overflow:hidden;background:linear-gradient(150deg,#FFB547,#FF6B8B 45%,#7B61FF)}
.u045-hero::before{content:"";position:absolute;width:190px;height:190px;right:-40px;top:-50px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.6),transparent 65%)}
.u045-hero::after{content:"";position:absolute;left:-30px;right:-30px;bottom:-60px;height:130px;border-radius:50%;background:rgba(20,10,40,.28);filter:blur(10px)}
.u045-hero b{position:absolute;left:18px;bottom:16px;z-index:1;font-size:12px;font-weight:800;letter-spacing:.08em;color:#fff}
.u045-page h3{margin:18px 0 6px;font-size:25px;line-height:1.18;font-weight:800;letter-spacing:-.045em}
.u045-page p{margin:0;font-size:13.5px;line-height:1.55;color:var(--ux-ink-3)}
.u045-row{display:flex;gap:8px;margin-top:16px}
.u045-row i{flex:1;height:64px;border-radius:16px;background:var(--ux-surface-2)}
.u045-top{position:absolute;left:0;right:0;top:0;height:68px;display:flex;align-items:center;justify-content:space-between;padding:0 14px 0 22px;z-index:3;color:var(--ux-ink);transition:color .4s}
.u045.is-open .u045-top{color:#F4F0E8}
.u045-logo{display:flex;align-items:center;gap:8px;font-size:16px;font-weight:800;letter-spacing:-.03em}
.u045-logo i{width:20px;height:20px;border-radius:7px;background:var(--ux-grad)}
.u045-ham{position:relative;width:46px;height:46px;border:0;padding:0;border-radius:50%;background:var(--ux-surface-2);color:inherit;transition:transform .4s var(--ux-spring),background-color .4s}
.u045.is-open .u045-ham{background:rgba(255,255,255,.12)}
.u045-ham:hover{transform:scale(1.06)}
.u045-ham:active{transform:scale(.9)}
.u045-ham:focus-visible{outline:2px solid var(--ux-accent);outline-offset:3px}
.u045-ham i{position:absolute;left:50%;top:50%;width:18px;height:2px;margin:-1px 0 0 -9px;border-radius:2px;background:currentColor;transition:transform .55s var(--ux-spring),opacity .25s,width .4s var(--ux-ease)}
.u045-ham i:nth-child(1){transform:translateY(-6px)}
.u045-ham i:nth-child(2){width:12px;margin-left:-3px}
.u045-ham i:nth-child(3){transform:translateY(6px)}
.u045.is-open .u045-ham i:nth-child(1){transform:rotate(45deg)}
.u045.is-open .u045-ham i:nth-child(2){opacity:0;transform:translateX(8px)}
.u045.is-open .u045-ham i:nth-child(3){transform:rotate(-45deg)}
.u045-sheet{position:absolute;inset:0;z-index:2;padding:96px 26px 26px;display:flex;flex-direction:column;background:radial-gradient(120% 70% at 100% 0%,#3A2A8C,transparent 60%),radial-gradient(90% 60% at 0% 100%,#0E5E63,transparent 65%),#0E0D16;color:#F4F0E8;clip-path:circle(0 at var(--cx,300px) var(--cy,34px));visibility:hidden;transition:clip-path .7s var(--ux-ease),visibility 0s .7s}
.u045.is-open .u045-sheet{clip-path:circle(640px at var(--cx,300px) var(--cy,34px));visibility:visible;transition:clip-path .8s var(--ux-ease),visibility 0s}
.u045-sheet small{font-size:11.5px;font-weight:700;letter-spacing:.14em;color:rgba(244,240,232,.45)}
.u045-nav{margin:12px 0 0;padding:0;list-style:none}
.u045-ln{display:flex;align-items:baseline;gap:12px;padding:7px 0;font-size:34px;font-weight:800;letter-spacing:-.05em;color:inherit;text-decoration:none;opacity:0;transform:translateY(26px);transition:opacity .25s,transform .3s var(--ux-ease)}
.u045-ln em{font-style:normal;font-size:12px;font-weight:700;letter-spacing:0;color:rgba(244,240,232,.4);font-variant-numeric:tabular-nums}
.u045-ln span{background:linear-gradient(90deg,#B7A4FF,#7DB4FF 55%,#A5F2D3) no-repeat 0 100%/0 3px;padding-bottom:2px;transition:background-size .45s var(--ux-ease)}
.u045-ln:hover span,.u045-ln:focus-visible span{background-size:100% 3px}
.u045-ln:focus-visible{outline:none}
.u045-ln[aria-current="page"] em{color:#A5F2D3}
.u045.is-open .u045-ln{opacity:1;transform:none;transition:opacity .4s var(--ux-ease) calc(.22s + var(--i) * 60ms),transform .7s var(--ux-spring) calc(.22s + var(--i) * 60ms)}
.u045-foot{margin-top:auto;display:flex;align-items:center;gap:8px;opacity:0;transform:translateY(14px);transition:opacity .25s,transform .3s}
.u045.is-open .u045-foot{opacity:1;transform:none;transition:opacity .4s .5s,transform .6s var(--ux-spring) .5s}
.u045-foot a{height:44px;padding:0 16px;border-radius:999px;display:inline-flex;align-items:center;font-size:13.5px;font-weight:700;color:inherit;text-decoration:none;box-shadow:inset 0 0 0 1px rgba(255,255,255,.2);transition:background-color .3s}
.u045-foot a:hover{background:rgba(255,255,255,.08)}
.u045-foot a.go{margin-left:auto;background:#F4F0E8;color:#0E0D16;box-shadow:none}
.u045-foot a:focus-visible{outline:2px solid #B7A4FF;outline-offset:2px}
</style>
<div class="ux u045">
  <div class="u045-page">
    <div class="u045-hero"><b>SPRING ISSUE · 04</b></div>
    <h3>Twelve studios<br>full of light</h3>
    <p>We visited the spaces of people who work quietly</p>
    <div class="u045-row" aria-hidden="true"><i></i><i></i><i></i></div>
  </div>
  <div class="u045-sheet" role="dialog" aria-modal="true" aria-label="Full menu" aria-hidden="true">
    <small>MENU</small>
    <ul class="u045-nav">
      <li><a class="u045-ln" href="#" style="--i:0" aria-current="page"><em>01</em><span>Magazine</span></a></li>
      <li><a class="u045-ln" href="#" style="--i:1"><em>02</em><span>Spaces</span></a></li>
      <li><a class="u045-ln" href="#" style="--i:2"><em>03</em><span>People</span></a></li>
      <li><a class="u045-ln" href="#" style="--i:3"><em>04</em><span>Subscribe</span></a></li>
    </ul>
    <div class="u045-foot"><a href="#">Instagram</a><a class="go" href="#">Sign in</a></div>
  </div>
  <div class="u045-top">
    <span class="u045-logo"><i aria-hidden="true"></i>Atelier</span>
    <button class="u045-ham" type="button" aria-expanded="false" aria-label="Open menu"><i></i><i></i><i></i></button>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ham = root.querySelector('.u045-ham');
  var sheet = root.querySelector('.u045-sheet');
  var page = root.querySelector('.u045-page');
  var focusables = Array.prototype.slice.call(sheet.querySelectorAll('a'));
  var open = false;
  function origin() {
    sheet.style.setProperty('--cx', (ham.offsetLeft + ham.parentNode.offsetLeft + ham.offsetWidth / 2) + 'px');
    sheet.style.setProperty('--cy', (ham.offsetTop + ham.parentNode.offsetTop + ham.offsetHeight / 2) + 'px');
  }
  function set(v) {
    open = v;
    origin();
    root.classList.toggle('is-open', v);
    ham.setAttribute('aria-expanded', String(v));
    ham.setAttribute('aria-label', v ? 'Close menu' : 'Open menu');
    sheet.setAttribute('aria-hidden', String(!v));
    page.inert = v;
    focusables.forEach(function (a) { a.tabIndex = v ? 0 : -1; });
  }
  ham.addEventListener('click', function () { set(!open); });
  focusables.forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      if (a.classList.contains('u045-ln')) {
        root.querySelectorAll('.u045-ln').forEach(function (x) { x.removeAttribute('aria-current'); });
        a.setAttribute('aria-current', 'page');
      }
      set(false); ham.focus();
    });
  });
  root.addEventListener('keydown', function (e) {
    if (!open) return;
    if (e.key === 'Escape') { e.preventDefault(); set(false); ham.focus(); return; }
    if (e.key !== 'Tab') return;
    var list = [ham].concat(focusables), i = list.indexOf(document.activeElement);
    if (i < 0) return;
    e.preventDefault();
    list[(i + (e.shiftKey ? -1 : 1) + list.length) % list.length].focus();
  });
  set(false);
})();
</script>
--- Code end ---

---
source: "lucianlabs"
id: "225"
title: "Cookie consent with a bite"
category: "Forms & Input"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#225"
tags: ["cookie", "consent", "banner", "privacy", "gdpr"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Cookie consent with a bite (225, Forms & Input)
[What it does] A cookie consent banner rises from the bottom of a website. Press Settings and the banner grows upward to show Essential, Analytics and Marketing switches, with Essential always on and locked. Press Accept all or Save choices and a bite mark appears in the cookie as crumbs fall, then the banner slides away, leaving a small cookie button in the bottom left to reopen the settings any time.
[How to use it] Open Settings, flip a switch and save, then reopen with the leftover cookie button

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
<!-- Lucian UX/UI Prompt #225 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#225 -->
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
.u225{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u225-pg{position:absolute;inset:0;padding:22px 20px}
.u225-pg i{display:block;border-radius:8px;background:var(--ux-surface-2);margin-bottom:9px}
.u225-bn{position:absolute;left:12px;right:12px;bottom:12px;padding:14px;border-radius:20px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 20px 40px -14px var(--ux-shadow-strong);transform:translateY(130%);transition:transform .5s cubic-bezier(.3,1.25,.5,1)}
.u225.is-on .u225-bn{transform:none}
.u225.is-done .u225-bn{transform:translateY(130%);transition:transform .45s cubic-bezier(.5,0,.75,0) .55s}
.u225-tp{display:flex;gap:11px;align-items:center}
.u225-ck{position:relative;flex:none;width:44px;height:44px}
.u225-ck svg{width:44px;height:44px;overflow:visible}
.u225-bt circle.b{transform-box:fill-box;transform-origin:center;transform:scale(0);transition:transform .25s cubic-bezier(.3,1.6,.5,1)}
.u225.is-bite .u225-bt circle.b{transform:none}
.u225-cr{position:absolute;right:2px;top:4px;width:4px;height:4px;border-radius:1px;background:#B45309;opacity:0}
.u225.is-bite .u225-cr{animation:u225-cr .7s ease-in forwards}
.u225-cr:nth-of-type(2){right:8px;width:3px;height:3px;animation-delay:.05s!important}
.u225-cr:nth-of-type(3){right:-2px;top:9px;width:3px;height:3px;animation-delay:.1s!important}
@keyframes u225-cr{0%{opacity:1;transform:translate(0,0) rotate(0)}100%{opacity:0;transform:translate(6px,34px) rotate(160deg)}}
.u225-tx b{display:block;font-size:13px;font-weight:900}
.u225-tx span{display:block;margin-top:2px;font-size:10.5px;line-height:1.4;font-weight:650;color:var(--ux-ink-3)}
.u225-ex{display:grid;grid-template-rows:0fr;transition:grid-template-rows .45s cubic-bezier(.3,1,.4,1)}
.u225-ex>div{min-height:0;overflow:hidden}
.u225.is-x .u225-ex{grid-template-rows:1fr}
.u225-rw{display:flex;align-items:center;gap:10px;padding:9px 2px;border-bottom:1px solid var(--ux-line)}
.u225-rw:first-child{margin-top:10px}
.u225-rw div{flex:1;min-width:0}
.u225-rw b{display:block;font-size:11.5px;font-weight:850}
.u225-rw small{display:block;font-size:9.5px;font-weight:650;color:var(--ux-ink-3)}
.u225-rw em{font-style:normal;font-size:9.5px;font-weight:800;color:var(--ux-ink-3)}
.u225-sw{position:relative;flex:none;width:36px;height:22px;border:0;border-radius:11px;background:var(--ux-surface-3);cursor:pointer;transition:background .2s}
.u225-sw::after{content:"";position:absolute;left:3px;top:3px;width:16px;height:16px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.25);transition:transform .25s cubic-bezier(.3,1.5,.5,1)}
.u225-sw[aria-checked="true"]{background:#10B981}
.u225-sw[aria-checked="true"]::after{transform:translateX(14px)}
.u225-sw:disabled{opacity:.55;cursor:not-allowed}
.u225-bs{display:flex;gap:6px;margin-top:12px}
.u225-bs button{flex:1;height:38px;border:0;border-radius:11px;font:inherit;font-size:12px;font-weight:850;cursor:pointer}
.u225-set,.u225-sv{background:var(--ux-surface-2);color:var(--ux-ink);box-shadow:inset 0 0 0 1px var(--ux-line)}
.u225-all{background:var(--ux-ink);color:var(--ux-surface)}
.u225-sv{display:none}
.u225.is-x .u225-set{display:none}
.u225.is-x .u225-sv{display:block}
.u225-fab{position:absolute;left:14px;bottom:14px;width:44px;height:44px;border:0;border-radius:50%;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 10px 20px -10px var(--ux-shadow-strong);display:grid;place-items:center;cursor:pointer;transform:scale(0);transition:transform .4s cubic-bezier(.3,1.7,.5,1)}
.u225.is-fab .u225-fab{transform:none}
.u225-fab svg{width:26px;height:26px}
.u225 button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u225-bn,.u225.is-done .u225-bn,.u225-ex,.u225-fab,.u225-bt circle.b{transition:none}.u225.is-bite .u225-cr{animation:none}}
</style>
<div class="ux u225">
  <div class="u225-pg" aria-hidden="true"><i style="height:22px;width:40%"></i><i style="height:120px"></i><i style="height:12px;width:90%"></i><i style="height:12px;width:76%"></i><i style="height:12px;width:84%"></i></div>
  <div class="u225-bn" role="dialog" aria-label="Cookie consent">
    <div class="u225-tp"><span class="u225-ck" aria-hidden="true"></span><div class="u225-tx"><b>Can we use cookies?</b><span>Only to make the site easier to use.</span></div></div>
    <div class="u225-ex"><div class="u225-ls"></div></div>
    <div class="u225-bs"><button type="button" class="u225-set">Settings</button><button type="button" class="u225-sv">Save choices</button><button type="button" class="u225-all">Accept all</button></div>
  </div>
  <button type="button" class="u225-fab" aria-label="Reopen cookie settings" tabindex="-1"></button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var bn = root.querySelector('.u225-bn'), ck = root.querySelector('.u225-ck'), ls = root.querySelector('.u225-ls'), set = root.querySelector('.u225-set'), sv = root.querySelector('.u225-sv'), all = root.querySelector('.u225-all'), fab = root.querySelector('.u225-fab');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var uid = 'u225' + Math.random().toString(36).slice(2, 7);
  function cookie(id, bite) {
    return '<svg viewBox="0 0 44 44"><defs><mask id="' + id + '" class="u225-bt"><rect width="44" height="44" fill="#fff"/>' + (bite ? '<circle class="b" cx="38" cy="7" r="9" fill="#000"/><circle class="b" cx="42" cy="17" r="6" fill="#000"/><circle class="b" cx="30" cy="2" r="6" fill="#000"/>' : '') + '</mask></defs><g mask="url(#' + id + ')"><circle cx="22" cy="22" r="19" fill="#F2B866"/><circle cx="22" cy="22" r="19" fill="none" stroke="#D97706" stroke-width="2"/><circle cx="15" cy="16" r="3" fill="#78350F"/><circle cx="26" cy="27" r="3.2" fill="#78350F"/><circle cx="14" cy="29" r="2.2" fill="#78350F"/><circle cx="29" cy="15" r="2" fill="#78350F"/></g></svg>';
  }
  ck.innerHTML = cookie(uid + 'a', true) + '<i class="u225-cr"></i><i class="u225-cr"></i><i class="u225-cr"></i>';
  fab.innerHTML = cookie(uid + 'b', false).replace('<svg ', '<svg aria-hidden="true" ');
  var CK = [['Essential', 'Keeps you signed in and your cart', 1], ['Analytics', 'Shows which pages help', 0], ['Marketing', 'Shows news you may like', 0]];
  var on = CK.map(function (c) { return !!c[2]; });
  var S = CK.map(function (c, i) {
    var r = document.createElement('div'); r.className = 'u225-rw';
    r.innerHTML = '<div><b></b><small></small></div>' + (c[2] ? '<em></em>' : '') + '<button type="button" class="u225-sw" role="switch"></button>';
    r.querySelector('b').textContent = c[0]; r.querySelector('small').textContent = c[1]; if (c[2]) r.querySelector('em').textContent = 'Always on';
    var b = r.querySelector('button'); b.setAttribute('aria-label', c[0]); if (c[2]) b.disabled = true;
    b.addEventListener('click', function () { on[i] = !on[i]; sync(); });
    ls.appendChild(r); return b;
  });
  function sync() { S.forEach(function (b, i) { b.setAttribute('aria-checked', on[i]); }); }
  function expand(v) { root.classList.toggle('is-x', v); }
  function done() {
    root.classList.remove('is-bite'); void root.offsetWidth; root.classList.add('is-bite', 'is-done');
    setTimeout(function () { root.classList.remove('is-on', 'is-done', 'is-x'); root.classList.add('is-fab'); fab.tabIndex = 0; fab.focus({ preventScroll: true }); }, rm ? 0 : 1050);
  }
  set.addEventListener('click', function () { expand(true); S[1].focus({ preventScroll: true }); });
  sv.addEventListener('click', done);
  all.addEventListener('click', function () { on = on.map(function () { return true; }); sync(); done(); });
  fab.addEventListener('click', function () { root.classList.remove('is-fab', 'is-bite'); fab.tabIndex = -1; root.classList.add('is-on'); expand(true); setTimeout(function () { S[1].focus({ preventScroll: true }); }, 300); });
  sync();
  setTimeout(function () { root.classList.add('is-on'); }, rm ? 0 : 600);
})();
</script>
--- Code end ---

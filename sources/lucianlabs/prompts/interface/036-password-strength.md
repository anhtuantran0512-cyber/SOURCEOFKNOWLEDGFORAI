---
source: "lucianlabs"
id: "036"
title: "Password strength meter"
category: "Inputs & Search"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#036"
tags: ["password", "strength", "meter", "validation", "form"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Password strength meter (036, Inputs & Search)
[What it does] With every keystroke the four-part bar fills and shifts from red to green, and each rule you satisfy pops its circle into a check. Press the eye icon and its lid opens to reveal the password.
[How to use it] Add or remove symbols in the password field. The eye icon toggles visibility

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
<!-- Lucian UX/UI Prompt #036 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#036 -->
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
.u036{--lv:var(--ux-line-2);position:relative;width:340px;height:262px;display:flex;flex-direction:column;justify-content:center}
.u036-lab{display:block;margin:0 4px 8px;font-size:13px;font-weight:700;color:var(--ux-ink-3)}
.u036-box{position:relative;display:flex;align-items:center;height:60px;padding:0 8px 0 18px;border-radius:18px;background:var(--ux-surface);box-shadow:0 0 0 1.5px var(--ux-line-2);transition:box-shadow .25s}
.u036-box:focus-within{box-shadow:0 0 0 2px var(--lv),0 0 0 6px color-mix(in srgb,var(--lv) 18%,transparent)}
.u036-in{flex:1;min-width:0;height:100%;border:0;outline:0;background:none;font-size:18px;font-weight:650;letter-spacing:.04em;color:var(--ux-ink)}
.u036-in:focus-visible{outline:none}
.u036-eye{width:44px;height:44px;flex:none;border:0;padding:0;border-radius:13px;background:none;color:var(--ux-ink-2);display:grid;place-items:center;transition:background-color .2s}
.u036-eye:hover{background:var(--ux-surface-2)}
.u036-eye:focus-visible{outline:2px solid var(--ux-accent);outline-offset:1px}
.u036-eye svg{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round;overflow:visible}
.u036-lid{transform-origin:12px 12px;transition:transform .4s var(--ux-spring)}
.u036-pupil{transform-origin:12px 12px;transition:transform .35s var(--ux-spring) .05s}
.u036-slash{stroke-dasharray:24;stroke-dashoffset:0;transition:stroke-dashoffset .35s var(--ux-ease)}
.u036.is-show .u036-slash{stroke-dashoffset:24}
.u036:not(.is-show) .u036-pupil{transform:scale(0)}
.u036:not(.is-show) .u036-lid{transform:scaleY(.15)}
.u036-meter{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:16px 4px 0}
.u036-meter i{height:7px;border-radius:4px;background:var(--ux-surface-3);overflow:hidden;position:relative}
.u036-meter i::after{content:"";position:absolute;inset:0;background:var(--lv);transform:scaleX(0);transform-origin:0 50%;transition:transform .45s var(--ux-ease),background-color .4s}
.u036-meter i.on::after{transform:none}
.u036-meter i:nth-child(2)::after{transition-delay:.05s}
.u036-meter i:nth-child(3)::after{transition-delay:.1s}
.u036-meter i:nth-child(4)::after{transition-delay:.15s}
.u036-lv{display:flex;justify-content:space-between;margin:9px 4px 0;font-size:13px;font-weight:650;color:var(--ux-ink-3)}
.u036-lv b{color:var(--lv);transition:color .4s}
.u036-rules{margin:18px 0 0;padding:16px;list-style:none;border-radius:18px;background:var(--ux-surface-2);display:grid;grid-template-columns:1fr 1fr;gap:12px 10px}
.u036-r{display:flex;align-items:center;gap:9px;font-size:13.5px;font-weight:600;color:var(--ux-ink-3);transition:color .3s}
.u036-r i{position:relative;width:20px;height:20px;flex:none;border-radius:50%;box-shadow:inset 0 0 0 1.8px var(--ux-line-2);transition:box-shadow .3s,background-color .3s}
.u036-r svg{position:absolute;inset:0;width:100%;height:100%;fill:none;stroke:var(--ux-accent-ink);stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
.u036-r path{stroke-dasharray:14;stroke-dashoffset:14;transition:stroke-dashoffset .3s var(--ux-ease) .1s}
.u036-r.ok{color:var(--ux-ink)}
.u036-r.ok i{background:var(--ux-mint);box-shadow:none;animation:u036-pop .4s var(--ux-spring)}
.u036-r.ok path{stroke-dashoffset:0}
@keyframes u036-pop{from{transform:scale(.4)}}
</style>
<div class="ux u036">
  <label class="u036-lab">New password</label>
  <div class="u036-box">
    <input class="u036-in" type="password" value="Lucian2026" autocomplete="new-password">
    <button class="u036-eye" type="button" aria-label="Show password" aria-pressed="false">
      <svg viewBox="0 0 24 24" aria-hidden="true"><g class="u036-lid"><path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/></g><circle class="u036-pupil" cx="12" cy="12" r="3"/><path class="u036-slash" d="M4 4l16 16"/></svg>
    </button>
  </div>
  <div class="u036-meter" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
  <p class="u036-lv"><span>Strength</span><b class="u036-word" aria-live="polite"></b></p>
  <ul class="u036-rules">
    <li class="u036-r" data-r="len"><i aria-hidden="true"><svg viewBox="0 0 20 20"><path d="M5.5 10.5l3 3 6-6.5"/></svg></i>10+ characters</li>
    <li class="u036-r" data-r="up"><i aria-hidden="true"><svg viewBox="0 0 20 20"><path d="M5.5 10.5l3 3 6-6.5"/></svg></i>An uppercase letter</li>
    <li class="u036-r" data-r="num"><i aria-hidden="true"><svg viewBox="0 0 20 20"><path d="M5.5 10.5l3 3 6-6.5"/></svg></i>A number</li>
    <li class="u036-r" data-r="sym"><i aria-hidden="true"><svg viewBox="0 0 20 20"><path d="M5.5 10.5l3 3 6-6.5"/></svg></i>A symbol</li>
  </ul>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var input = root.querySelector('.u036-in');
  var eye = root.querySelector('.u036-eye');
  var segs = root.querySelectorAll('.u036-meter i');
  var word = root.querySelector('.u036-word');
  var rules = Array.prototype.slice.call(root.querySelectorAll('.u036-r'));
  var lab = root.querySelector('.u036-lab');
  var uid = 'u036-' + Math.random().toString(36).slice(2, 7);
  input.id = uid; lab.htmlFor = uid;
  root.querySelector('.u036-rules').id = uid + '-r';
  input.setAttribute('aria-describedby', uid + '-r');
  var TEST = { len: function (v) { return v.length >= 10; }, up: function (v) { return /[A-Z]/.test(v); }, num: function (v) { return /\d/.test(v); }, sym: function (v) { return /[^A-Za-z0-9]/.test(v); } };
  var LV = [['Type a password', 'var(--ux-line-2)'], ['Weak', '#E5484D'], ['Fair', '#F07A3E'], ['Good', '#E8B417'], ['Strong', 'var(--ux-mint)']];
  function update() {
    var v = input.value, n = 0;
    rules.forEach(function (r) { var ok = TEST[r.dataset.r](v); r.classList.toggle('ok', ok); if (ok) n++; });
    var lv = v ? Math.max(1, n) : 0;
    root.style.setProperty('--lv', LV[lv][1]);
    Array.prototype.forEach.call(segs, function (s, i) { s.classList.toggle('on', i < lv); });
    word.textContent = LV[lv][0];
  }
  input.addEventListener('input', update);
  eye.addEventListener('click', function () {
    var show = input.type === 'password';
    input.type = show ? 'text' : 'password';
    root.classList.toggle('is-show', show);
    eye.setAttribute('aria-pressed', String(show));
    eye.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
  });
  update();
})();
</script>
--- Code end ---

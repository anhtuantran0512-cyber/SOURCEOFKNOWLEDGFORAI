---
source: "lucianlabs"
id: "026"
title: "6-digit code input"
category: "Inputs & Search"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#026"
tags: ["otp", "code", "verification", "input", "paste"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] 6-digit code input (026, Inputs & Search)
[What it does] Each digit pops up from below as you fill a box, and the cursor moves on to the next. With all six filled the boxes ripple while checking — green if it matches, or a shake and an empty row if it does not.
[How to use it] Type 482915 for success; any other code shows the failure flow. Paste and Backspace work too

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
<!-- Lucian UX/UI Prompt #026 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#026 -->
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
.u026{position:relative;width:350px;height:250px;display:flex;flex-direction:column;align-items:center;justify-content:center}
.u026-ic{width:56px;height:56px;border-radius:18px;display:grid;place-items:center;color:#fff;background:linear-gradient(140deg,#5B8CFF,#8B6CFF);box-shadow:0 14px 26px -14px rgba(91,108,255,.8);transition:background .5s var(--ux-ease)}
.u026-ic svg{width:26px;height:26px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.u026.is-ok .u026-ic{background:linear-gradient(140deg,#2FD8A8,#119C72)}
.u026-t{margin:16px 0 0;font-size:18px;font-weight:760;letter-spacing:-.03em}
.u026-s{margin:6px 0 20px;font-size:13.5px;color:var(--ux-ink-3)}
.u026-s b{color:var(--ux-ink-2);font-weight:650}
.u026-row{position:relative;display:flex;gap:8px}
.u026-row i.sep{width:10px;align-self:center;height:2px;border-radius:2px;background:var(--ux-line-2)}
.u026-c{position:relative;width:46px;height:58px;border-radius:14px;background:var(--ux-surface);box-shadow:inset 0 0 0 1.5px var(--ux-line-2);display:grid;place-items:center;overflow:hidden;
  font-size:26px;font-weight:760;font-variant-numeric:tabular-nums;transition:box-shadow .25s var(--ux-ease),background-color .4s var(--ux-ease),color .4s,transform .45s var(--ux-spring)}
.u026-c span{display:block;animation:u026-in .4s var(--ux-spring)}
@keyframes u026-in{from{transform:translateY(70%);opacity:0}}
.u026-c.cur{box-shadow:inset 0 0 0 2px var(--ux-accent),0 0 0 4px var(--ux-accent-soft)}
.u026-c.cur::after{content:"";position:absolute;left:50%;top:16px;bottom:16px;width:2px;margin-left:-1px;border-radius:1px;background:var(--ux-accent);animation:u026-blink 1s steps(1) infinite}
.u026-c.cur.has::after{display:none}
@keyframes u026-blink{50%{opacity:0}}
.u026.is-check .u026-c{animation:u026-wave .5s var(--ux-ease);animation-delay:calc(var(--i) * 60ms)}
@keyframes u026-wave{40%{transform:translateY(-8px)}}
.u026.is-ok .u026-c{background:color-mix(in srgb,var(--ux-mint) 14%,var(--ux-surface));box-shadow:inset 0 0 0 2px var(--ux-mint);color:var(--ux-mint);transition-delay:calc(var(--i) * 50ms)}
.u026.is-bad .u026-row{animation:u026-shake .45s var(--ux-ease)}
.u026.is-bad .u026-c{box-shadow:inset 0 0 0 2px var(--ux-danger);color:var(--ux-danger)}
@keyframes u026-shake{20%{transform:translateX(-8px)}40%{transform:translateX(7px)}60%{transform:translateX(-4px)}80%{transform:translateX(2px)}}
.u026-real{position:absolute;inset:0;width:100%;height:100%;opacity:0;border:0;padding:0;font-size:16px;cursor:text;caret-color:transparent;color:transparent;background:transparent}
.u026-msg{height:20px;margin:16px 0 0;font-size:13.5px;font-weight:650;color:var(--ux-ink-3);transition:color .3s var(--ux-ease)}
.u026.is-ok .u026-msg{color:var(--ux-mint)}
.u026.is-bad .u026-msg{color:var(--ux-danger)}
.u026-live{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.u026-real:focus-visible{outline:none}
</style>
<div class="ux u026">
  <span class="u026-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="6" y="2.5" width="12" height="19" rx="3"/><path d="M10.5 18.5h3"/></svg></span>
  <p class="u026-t">Enter the verification code</p>
  <p class="u026-s">The 6-digit code sent to <b>•••• 2981</b></p>
  <div class="u026-row">
    <span class="u026-c" style="--i:0"></span><span class="u026-c" style="--i:1"></span><span class="u026-c" style="--i:2"></span>
    <i class="sep" aria-hidden="true"></i>
    <span class="u026-c" style="--i:3"></span><span class="u026-c" style="--i:4"></span><span class="u026-c" style="--i:5"></span>
    <input class="u026-real" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" aria-label="6-digit verification code">
  </div>
  <p class="u026-msg">Resend code in 2:59</p>
  <span class="u026-live" aria-live="polite"></span>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var input = root.querySelector('.u026-real');
  var cells = Array.prototype.slice.call(root.querySelectorAll('.u026-c'));
  var msg = root.querySelector('.u026-msg');
  var live = root.querySelector('.u026-live');
  function say(t) { msg.textContent = t; live.textContent = t; }
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var CODE = '482915', prev = '', timers = [], left = 179, tick = 0;
  function later(fn, ms) { timers.push(setTimeout(function () { if (root.isConnected) fn(); }, ms)); }
  function paint() {
    var v = input.value;
    cells.forEach(function (c, i) {
      var ch = v[i] || '';
      if (ch !== (prev[i] || '')) c.innerHTML = ch ? '<span>' + ch + '</span>' : '';
      c.classList.toggle('has', !!ch);
      c.classList.toggle('cur', document.activeElement === input && (i === Math.min(v.length, 5)));
    });
    prev = v;
  }
  function verify() {
    root.classList.add('is-check');
    say('Checking');
    later(function () {
      root.classList.remove('is-check');
      if (input.value === CODE) {
        root.classList.add('is-ok');
        say('Verified');
        input.blur();
        clearInterval(tick);
      } else {
        root.classList.add('is-bad');
        say('That code doesn’t match. Try again');
        later(function () { root.classList.remove('is-bad'); input.value = ''; paint(); input.focus(); }, rm ? 600 : 900);
      }
    }, rm ? 60 : 640);
  }
  input.addEventListener('input', function () {
    input.value = input.value.replace(/\D/g, '').slice(0, 6);
    if (root.classList.contains('is-ok')) root.classList.remove('is-ok');
    paint();
    if (input.value.length === 6) verify();
  });
  input.addEventListener('focus', paint);
  input.addEventListener('blur', paint);
  tick = setInterval(function () {
    if (!root.isConnected) { clearInterval(tick); return; }
    if (root.classList.contains('is-bad') || root.classList.contains('is-check') || root.classList.contains('is-ok')) return;
    left = Math.max(0, left - 1);
    msg.textContent = left ? 'Resend code in ' + Math.floor(left / 60) + ':' + String(left % 60).padStart(2, '0') : 'You can resend the code now';
  }, 1000);
  paint();
})();
</script>
--- Code end ---

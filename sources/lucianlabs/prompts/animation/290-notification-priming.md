---
source: "lucianlabs"
id: "290"
title: "Ask-first notification permission"
category: "App Screens"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#290"
tags: ["notifications", "permission", "priming", "onboarding", "web-push"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Ask-first notification permission (290, App Screens)
[What it does] Instead of firing the browser's notification prompt right away, a card with a wiggling bell first asks, “Want a heads-up when someone replies?” Press Turn on and the browser's permission box drops in at the top with an arrow pointing at Allow; allow it and the bell turns into a check as a first notification slides in from the top right. Press Later and the card folds into a small bell button.
[How to use it] Press Turn on, then Allow in the box that appears above

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
<!-- Lucian UX/UI Prompt #290 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#290 -->
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
.u290{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface-2);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u290-cd{position:absolute;left:20px;right:20px;top:90px;padding:22px 20px 18px;border-radius:22px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 20px 40px -24px var(--ux-shadow-strong);text-align:center;transform-origin:calc(100% - 26px) calc(100% + 60px);transition:transform .5s cubic-bezier(.6,0,.3,1),opacity .35s}
.u290.is-later .u290-cd{transform:scale(.1);opacity:0;pointer-events:none}
.u290-bl{position:relative;width:56px;height:56px;margin:0 auto;border-radius:18px;background:color-mix(in srgb,#F59E0B 16%,transparent);display:grid;place-items:center;color:#D97706}
.u290-bl svg{width:28px;height:28px;transform-origin:50% 15%;animation:u290-ring 2.4s ease-in-out infinite}
@keyframes u290-ring{0%,60%,100%{transform:none}64%{transform:rotate(16deg)}70%{transform:rotate(-14deg)}76%{transform:rotate(10deg)}82%{transform:rotate(-6deg)}88%{transform:rotate(2deg)}}
.u290.is-on .u290-bl{background:color-mix(in srgb,#10B981 16%,transparent);color:#059669}
.u290.is-on .u290-bl svg{animation:none}
.u290-cd h4{margin:14px 0 0;font-size:16px;font-weight:900;letter-spacing:-.025em}
.u290-cd p{margin:6px 0 0;font-size:11px;line-height:1.5;font-weight:650;color:var(--ux-ink-3)}
.u290-bs{display:flex;gap:6px;margin-top:16px}
.u290-bs button{flex:1;height:40px;border:0;border-radius:12px;font:inherit;font-size:12px;font-weight:850;cursor:pointer}
.u290-lt{background:var(--ux-surface-2);color:var(--ux-ink-2)}
.u290-ok{background:var(--ux-ink);color:var(--ux-surface)}
.u290.is-on .u290-bs{display:none}
.u290-dn{display:none;margin-top:16px;height:40px;align-items:center;justify-content:center;font-size:12px;font-weight:850;color:#059669}
.u290.is-on .u290-dn{display:flex}
.u290-bw{position:absolute;left:12px;top:12px;width:236px;padding:12px;border-radius:12px;background:#FFF;color:#1F2937;box-shadow:0 0 0 1px rgba(0,0,0,.08),0 16px 32px -10px rgba(0,0,0,.35);font-size:11px;font-weight:650;transform:translateY(-130%);transition:transform .45s cubic-bezier(.3,1.25,.5,1)}
.u290.is-ask .u290-bw{transform:none}
.u290-bw p{margin:0;display:flex;align-items:center;gap:7px}
.u290-bw p i{flex:none;width:16px;height:16px;border-radius:4px;background:#E5E7EB;display:grid;place-items:center}
.u290-bw p i::after{content:"";width:6px;height:6px;border-radius:50%;background:#6B7280}
.u290-bw div{display:flex;justify-content:flex-end;gap:6px;margin-top:10px}
.u290-bw button{height:26px;padding:0 12px;border:0;border-radius:6px;font:inherit;font-size:11px;font-weight:750;cursor:pointer}
.u290-bk{background:#F3F4F6;color:#374151}
.u290-al{background:#2563EB;color:#fff}
.u290-ar{position:absolute;left:220px;top:104px;width:34px;height:40px;color:var(--ux-accent);opacity:0;transition:opacity .3s .3s}
.u290.is-ask .u290-ar{opacity:1}
.u290-ar svg{width:34px;height:40px;animation:u290-pt .8s ease-in-out infinite alternate}
@keyframes u290-pt{to{transform:translate(-3px,-5px)}}
.u290-nt{position:absolute;right:12px;top:12px;width:224px;display:flex;gap:9px;padding:11px;border-radius:14px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 18px 34px -12px var(--ux-shadow-strong);transform:translateX(120%);transition:transform .5s cubic-bezier(.3,1.3,.5,1)}
.u290-nt.is-on{transform:none}
.u290-nt i{flex:none;width:30px;height:30px;border-radius:9px;background:var(--ux-grad)}
.u290-nt b{display:block;font-size:11.5px;font-weight:850}
.u290-nt span{display:block;margin-top:2px;font-size:10.5px;font-weight:650;color:var(--ux-ink-2)}
.u290-fb{position:absolute;right:16px;bottom:16px;width:48px;height:48px;border:0;border-radius:50%;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 12px 24px -12px var(--ux-shadow-strong);color:#D97706;display:grid;place-items:center;cursor:pointer;transform:scale(0);transition:transform .4s cubic-bezier(.3,1.7,.5,1)}
.u290.is-later .u290-fb{transform:none;transition-delay:.35s}
.u290-fb svg{width:22px;height:22px}
.u290-fb::after{content:"";position:absolute;right:11px;top:11px;width:8px;height:8px;border-radius:50%;background:#EF4444;box-shadow:0 0 0 2px var(--ux-surface)}
.u290 button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u290-bl svg,.u290-ar svg{animation:none}.u290-cd,.u290-bw,.u290-nt,.u290-fb{transition:none}}
</style>
<div class="ux u290">
  <div class="u290-cd">
    <div class="u290-bl" aria-hidden="true"><svg viewBox="0 0 28 28"><path class="u290-bi" d="M7 19v-7a7 7 0 0 1 14 0v7l2 2.5H5zM11.5 24a2.6 2.6 0 0 0 5 0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/></svg></div>
    <h4>Want a heads-up when someone replies?</h4><p>Only the important stuff. Turn it off anytime in settings.</p>
    <div class="u290-bs"><button type="button" class="u290-lt">Later</button><button type="button" class="u290-ok">Turn on</button></div>
    <div class="u290-dn" role="status">Notifications are on</div>
  </div>
  <div class="u290-bw" role="dialog" aria-hidden="true"><p><i aria-hidden="true"></i>example.com wants to show notifications</p><div><button type="button" class="u290-bk" tabindex="-1">Block</button><button type="button" class="u290-al" tabindex="-1">Allow</button></div></div>
  <div class="u290-ar" aria-hidden="true"><svg viewBox="0 0 34 40"><path d="M26 36C14 34 8 24 10 8M4 14l6-7 6 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
  <div class="u290-nt" role="status"><i aria-hidden="true"></i><div><b>Junho replied</b><span>“Sounds good, I’ll ship it today!”</span></div></div>
  <button type="button" class="u290-fb" aria-label="Open notification settings" tabindex="-1"><svg viewBox="0 0 28 28" aria-hidden="true"><path d="M7 19v-7a7 7 0 0 1 14 0v7l2 2.5H5zM11.5 24a2.6 2.6 0 0 0 5 0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/></svg></button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ok = root.querySelector('.u290-ok'), lt = root.querySelector('.u290-lt'), bw = root.querySelector('.u290-bw'), al = root.querySelector('.u290-al'), bk = root.querySelector('.u290-bk'), nt = root.querySelector('.u290-nt'), fb = root.querySelector('.u290-fb'), bi = root.querySelector('.u290-bi');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function ask(v) { root.classList.toggle('is-ask', v); bw.setAttribute('aria-hidden', !v); al.tabIndex = bk.tabIndex = v ? 0 : -1; if (v) setTimeout(function () { al.focus({ preventScroll: true }); }, rm ? 0 : 400); }
  ok.addEventListener('click', function () { ask(true); });
  al.addEventListener('click', function () {
    ask(false); root.classList.add('is-on');
    bi.setAttribute('d', 'M6 14.5l5 5L22 8.5');
    setTimeout(function () { nt.classList.add('is-on'); setTimeout(function () { nt.classList.remove('is-on'); }, 2600); }, rm ? 0 : 600);
  });
  bk.addEventListener('click', function () { ask(false); root.classList.add('is-later'); fb.tabIndex = 0; });
  lt.addEventListener('click', function () { root.classList.add('is-later'); fb.tabIndex = 0; fb.focus({ preventScroll: true }); });
  fb.addEventListener('click', function () { root.classList.remove('is-later'); fb.tabIndex = -1; ok.focus({ preventScroll: true }); });
})();
</script>
--- Code end ---

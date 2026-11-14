---
source: "lucianlabs"
id: "215"
title: "Support chat from a launcher bubble"
category: "App Screens"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#215"
tags: ["chat-widget", "support", "launcher", "chatbot", "help"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Support chat from a launcher bubble (215, App Screens)
[What it does] Press the chat bubble in the bottom right of a website and the support window grows out from where the button was, showing the team's faces and “We usually reply in 3 minutes.” Press a quick question chip and your bubble rises, three dots bounce, and an answer arrives with a help article card. Choose Talk to a person and a line announces an agent has joined before their first hello arrives.
[How to use it] Press the chat bubble in the bottom right and pick a quick question

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
<!-- Lucian UX/UI Prompt #215 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#215 -->
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
.u215{position:relative;width:300px;height:480px;border-radius:32px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u215-pg{position:absolute;inset:0;padding:22px 18px}
.u215-pg nav{display:flex;gap:12px;font-size:11.5px;font-weight:800;color:var(--ux-ink-2)}
.u215-pg nav b{margin-right:auto;color:var(--ux-ink);font-weight:900}
.u215-pg i{display:block;margin-top:14px;height:120px;border-radius:16px;background:var(--ux-surface-2)}
.u215-pg i+i{height:70px}
.u215-ln{position:absolute;right:16px;bottom:16px;z-index:3;width:54px;height:54px;border:0;border-radius:50%;background:var(--ux-accent);color:#fff;display:grid;place-items:center;cursor:pointer;box-shadow:0 14px 28px -10px var(--ux-accent);transition:transform .3s cubic-bezier(.3,1.6,.5,1)}
.u215-ln svg{position:absolute;width:24px;height:24px;transition:transform .35s cubic-bezier(.3,1.5,.5,1),opacity .2s}
.u215-ln .x{transform:rotate(-90deg) scale(.5);opacity:0}
.u215.is-open .u215-ln .c{transform:rotate(90deg) scale(.5);opacity:0}
.u215.is-open .u215-ln .x{transform:none;opacity:1}
.u215-ln:active{transform:scale(.92)}
.u215-wg{position:absolute;right:12px;bottom:80px;left:12px;top:14px;z-index:2;display:flex;flex-direction:column;border-radius:22px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 50px -20px rgba(0,0,0,.4);overflow:hidden;transform-origin:calc(100% - 31px) calc(100% + 39px);transform:scale(.1);opacity:0;pointer-events:none;transition:transform .45s cubic-bezier(.3,1.15,.4,1),opacity .25s}
.u215.is-open .u215-wg{transform:none;opacity:1;pointer-events:auto}
.u215-wh{padding:16px 16px 14px;background:var(--ux-grad);color:#fff}
.u215-fs{display:flex}
.u215-fs i{width:26px;height:26px;margin-right:-7px;border-radius:50%;box-shadow:0 0 0 2px rgba(255,255,255,.9);display:grid;place-items:center;font-style:normal;font-size:10px;font-weight:850}
.u215-wh b{display:block;margin-top:10px;font-size:15px;font-weight:900}
.u215-wh small{display:flex;align-items:center;gap:5px;margin-top:2px;font-size:10px;font-weight:700;opacity:.9}
.u215-wh small::before{content:"";width:6px;height:6px;border-radius:50%;background:#4ADE80}
.u215-ms{flex:1;overflow-y:auto;scrollbar-width:none;padding:12px 12px 4px;display:flex;flex-direction:column;gap:7px}
.u215-ms::-webkit-scrollbar{display:none}
.u215-b{max-width:82%;padding:8px 11px;border-radius:14px;font-size:11px;line-height:1.45;font-weight:650;animation:u215-in .35s cubic-bezier(.3,1.4,.5,1) backwards}
@keyframes u215-in{from{opacity:0;transform:translateY(8px) scale(.96)}}
.u215-b.bt{align-self:flex-start;background:var(--ux-surface-2);border-bottom-left-radius:5px}
.u215-b.me{align-self:flex-end;background:var(--ux-accent);color:#fff;border-bottom-right-radius:5px}
.u215-b.ag{align-self:flex-start;background:color-mix(in srgb,#EC4899 12%,var(--ux-surface));border-bottom-left-radius:5px}
.u215-ty{align-self:flex-start;display:flex;gap:3px;padding:10px 12px;border-radius:14px;border-bottom-left-radius:5px;background:var(--ux-surface-2)}
.u215-ty i{width:6px;height:6px;border-radius:50%;background:var(--ux-ink-3);animation:u215-dt 1s ease-in-out infinite}
.u215-ty i:nth-child(2){animation-delay:.15s}.u215-ty i:nth-child(3){animation-delay:.3s}
@keyframes u215-dt{30%{transform:translateY(-4px);opacity:.6}}
.u215-ar{display:flex;align-items:center;gap:8px;margin-top:6px;padding:7px;border-radius:10px;background:var(--ux-surface);box-shadow:inset 0 0 0 1px var(--ux-line)}
.u215-ar i{flex:none;width:28px;height:28px;border-radius:7px;background:linear-gradient(135deg,#A5B4FC,#F0ABFC)}
.u215-ar b{display:block;font-size:10.5px;font-weight:850}
.u215-ar small{display:block;font-size:9px;font-weight:700;color:var(--ux-ink-3)}
.u215-sy{align-self:center;padding:3px 9px;border-radius:999px;background:var(--ux-surface-2);font-size:9.5px;font-weight:800;color:var(--ux-ink-3);animation:u215-in .35s backwards}
.u215-qs{display:flex;flex-wrap:wrap;gap:5px;padding:4px 12px 8px;justify-content:flex-end}
.u215-qk{height:28px;padding:0 10px;border:0;border-radius:999px;background:var(--ux-surface);box-shadow:inset 0 0 0 1.5px color-mix(in srgb,var(--ux-accent) 50%,transparent);color:var(--ux-accent);font:inherit;font-size:10.5px;font-weight:800;cursor:pointer;transition:opacity .2s}
.u215-qk:disabled{opacity:.35;cursor:default}
.u215-ip{display:flex;gap:6px;padding:8px 10px 10px;border-top:1px solid var(--ux-line)}
.u215-ip input{flex:1;min-width:0;height:34px;padding:0 11px;border:0;border-radius:10px;background:var(--ux-surface-2);color:var(--ux-ink);font:inherit;font-size:11px;font-weight:650;outline:none}
.u215 button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u215-wg,.u215-ln svg{transition:none}.u215-b,.u215-sy{animation:none}.u215-ty i{animation:none}}
</style>
<div class="ux u215">
  <div class="u215-pg" aria-hidden="true"><nav><b>Nimbus</b><span>Pricing</span><span>Docs</span><span>Blog</span></nav><i></i><i></i></div>
  <div class="u215-wg" role="dialog" aria-hidden="true">
    <div class="u215-wh"><div class="u215-fs" aria-hidden="true"><i style="background:#F9A8D4">M</i><i style="background:#A5B4FC">J</i><i style="background:#FDE68A">H</i></div><b>How can we help?</b><small>We usually reply in 3 minutes</small></div>
    <div class="u215-ms" aria-live="polite"><div class="u215-b bt">Hi there! Pick what you need 👋</div></div>
    <div class="u215-qs"></div>
    <div class="u215-ip"><input placeholder="Type a message" aria-label="Message" tabindex="-1"></div>
  </div>
  <button type="button" class="u215-ln" aria-label="Open chat" aria-expanded="false"><svg class="c" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5h16v10.5H10l-5 3.5V16H4z" fill="currentColor"/></svg><svg class="x" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ln = root.querySelector('.u215-ln'), wg = root.querySelector('.u215-wg'), ms = root.querySelector('.u215-ms'), qs = root.querySelector('.u215-qs'), ip = root.querySelector('.u215-ip input');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var QK = ['I want to change plans', 'Where do I get receipts?', 'Talk to a person'];
  var AN = [['You can switch anytime in Settings › Billing. Unused time is prorated.', 'Changing your plan'], ['You can download them monthly from your billing history.', 'How to get receipts']];
  var busy = false;
  var Q = QK.map(function (q, i) { var b = document.createElement('button'); b.type = 'button'; b.className = 'u215-qk'; b.textContent = q; b.tabIndex = -1; b.addEventListener('click', function () { ask(i); }); qs.appendChild(b); return b; });
  function add(el) { ms.appendChild(el); ms.scrollTop = ms.scrollHeight; return el; }
  function bub(cls, txt) { var d = document.createElement('div'); d.className = 'u215-b ' + cls; d.textContent = txt; return add(d); }
  function ask(i) {
    if (busy) return; busy = true; Q[i].disabled = true;
    bub('me', QK[i]);
    var ty = document.createElement('div'); ty.className = 'u215-ty'; ty.innerHTML = '<i></i><i></i><i></i>';
    setTimeout(function () { add(ty); }, rm ? 0 : 300);
    setTimeout(function () {
      ty.remove();
      if (i < 2) {
        var d = bub('bt', AN[i][0]), ar = document.createElement('div'); ar.className = 'u215-ar'; ar.innerHTML = '<i aria-hidden="true"></i><div><b></b><small></small></div>'; ar.querySelector('b').textContent = AN[i][1]; ar.querySelector('small').textContent = 'Help article · 2 min read'; d.appendChild(ar); ms.scrollTop = ms.scrollHeight;
      } else {
        var s = document.createElement('div'); s.className = 'u215-sy'; s.textContent = 'Minji joined the chat'; add(s);
        setTimeout(function () { bub('ag', 'Hi, I’m Minji. What can I help with?'); }, rm ? 0 : 600);
      }
      busy = false;
    }, rm ? 0 : 1300);
  }
  function setOpen(v) {
    root.classList.toggle('is-open', v); wg.setAttribute('aria-hidden', !v); ln.setAttribute('aria-expanded', v); ln.setAttribute('aria-label', v ? 'Close chat' : 'Open chat');
    Q.forEach(function (b) { b.tabIndex = v ? 0 : -1; }); ip.tabIndex = v ? 0 : -1;
    if (v) setTimeout(function () { Q[0].focus({ preventScroll: true }); }, rm ? 0 : 350);
  }
  ln.addEventListener('click', function () { setOpen(!root.classList.contains('is-open')); });
  root.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('is-open')) { setOpen(false); ln.focus(); } });
})();
</script>
--- Code end ---

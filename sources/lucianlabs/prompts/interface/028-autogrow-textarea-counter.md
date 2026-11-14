---
source: "lucianlabs"
id: "028"
title: "Auto-growing reply box"
category: "Inputs & Search"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#028"
tags: ["textarea", "autogrow", "counter", "ring", "composer"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Auto-growing reply box (028, Inputs & Search)
[What it does] The box grows smoothly as you write, and the ring in the bottom-right fills as you use up characters. Near the limit the ring turns orange, past it red, and it shows how many are left as a number.
[How to use it] Write a long reply. Past 140 characters the Post button is blocked

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
<!-- Lucian UX/UI Prompt #028 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#028 -->
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
.u028{position:relative;width:350px;height:300px;display:flex;flex-direction:column;justify-content:center}
.u028-thread{display:flex;gap:10px;margin-bottom:14px}
.u028-av{width:34px;height:34px;flex:none;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFD3A8,#FF7A93 60%,#8B6CFF)}
.u028-bub{margin:0;padding:10px 14px;border-radius:4px 16px 16px 16px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line);font-size:14px;line-height:1.5;color:var(--ux-ink-2)}
.u028-bub b{display:block;font-size:12.5px;color:var(--ux-ink);margin-bottom:2px}
.u028-box{position:relative;padding:14px 14px 12px 16px;border-radius:22px;background:var(--ux-surface);box-shadow:0 0 0 1.5px var(--ux-line-2),0 20px 40px -28px var(--ux-shadow-strong);transition:box-shadow .3s var(--ux-ease)}
.u028-box:focus-within{box-shadow:0 0 0 2px var(--ux-accent),0 0 0 6px var(--ux-accent-soft),0 20px 40px -28px var(--ux-shadow-strong)}
.u028-ta{display:block;width:100%;height:24px;min-height:24px;max-height:144px;padding:0;border:0;outline:0;resize:none;background:none;font:inherit;font-size:15.5px;line-height:24px;color:var(--ux-ink);overflow:hidden;transition:height .25s var(--ux-ease)}
.u028-ta::placeholder{color:var(--ux-ink-3)}
.u028-foot{display:flex;align-items:center;gap:10px;margin-top:12px}
.u028-tool{width:34px;height:34px;border:0;padding:0;border-radius:10px;background:none;color:var(--ux-ink-3);display:grid;place-items:center;transition:background-color .2s,color .2s}
.u028-tool:hover{background:var(--ux-surface-2);color:var(--ux-ink)}
.u028-tool:focus-visible{outline:2px solid var(--ux-accent);outline-offset:1px}
.u028-tool svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.u028-ring{position:relative;width:30px;height:30px;margin-left:auto;transition:transform .45s var(--ux-spring)}
.u028-ring svg{width:100%;height:100%;transform:rotate(-90deg)}
.u028-ring circle{fill:none;stroke-width:3}
.u028-ring .bg{stroke:var(--ux-surface-3)}
.u028-ring .fg{stroke:var(--ux-accent);stroke-linecap:round;stroke-dasharray:75.4;stroke-dashoffset:calc(75.4 * (1 - var(--p,0)));transition:stroke-dashoffset .3s var(--ux-ease),stroke .3s var(--ux-ease)}
.u028-left{position:absolute;inset:0;display:grid;place-items:center;font-size:10.5px;font-weight:800;font-variant-numeric:tabular-nums;opacity:0;transition:opacity .2s}
.u028.is-near .u028-ring{transform:scale(1.25)}
.u028.is-near .u028-ring .fg{stroke:var(--ux-warn)}
.u028.is-near .u028-left{opacity:1;color:var(--ux-warn)}
.u028.is-over .u028-ring .fg{stroke:var(--ux-danger)}
.u028.is-over .u028-left{color:var(--ux-danger)}
.u028-send{height:38px;padding:0 16px;border:0;border-radius:12px;background:var(--ux-ink);color:var(--ux-page);font-size:14px;font-weight:700;transition:opacity .25s var(--ux-ease),transform .4s var(--ux-spring)}
.u028-send:active{transform:scale(.94)}
.u028-send:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u028-send[aria-disabled="true"]{opacity:.3;cursor:not-allowed}
.u028-sep{width:1px;height:20px;background:var(--ux-line-2)}
.u028-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.u028-ta:focus-visible{outline:none}
</style>
<div class="ux u028">
  <div class="u028-thread">
    <span class="u028-av" aria-hidden="true"></span>
    <p class="u028-bub"><b>Seojun Yoon</b>The transition in concept 3 feels a little fast. Any thoughts?</p>
  </div>
  <div class="u028-box">
    <textarea class="u028-ta" rows="1" placeholder="Write a reply" aria-label="Reply">Sounds good! I’ll set it to 200ms.</textarea>
    <div class="u028-foot">
      <button class="u028-tool" type="button" aria-label="Attach image"><svg viewBox="0 0 24 24"><rect x="4" y="5" width="16" height="14" rx="3"/><circle cx="9.5" cy="10" r="1.6"/><path d="M5 17l4.5-4.5 3 3 2.5-2.5L19.5 17"/></svg></button>
      <button class="u028-tool" type="button" aria-label="Mention"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.5"/><path d="M15.5 12v1.3a2.2 2.2 0 0 0 4.4 0V12a8 8 0 1 0-3 6.2"/></svg></button>
      <span class="u028-ring" aria-hidden="true"><svg viewBox="0 0 30 30"><circle class="bg" cx="15" cy="15" r="12"/><circle class="fg" cx="15" cy="15" r="12"/></svg><span class="u028-left"></span></span>
      <span class="u028-sep" aria-hidden="true"></span>
      <button class="u028-send" type="button">Post</button>
    </div>
  </div>
  <span class="u028-sr" aria-live="polite"></span>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var ta = root.querySelector('.u028-ta');
  var left = root.querySelector('.u028-left');
  var send = root.querySelector('.u028-send');
  var sr = root.querySelector('.u028-sr');
  var MAX = 140;
  function grow() {
    var h = ta.style.height;
    ta.style.transition = 'none';
    ta.style.height = '24px';
    var need = Math.min(144, ta.scrollHeight);
    ta.style.height = h || '24px';
    void ta.offsetHeight;
    ta.style.transition = '';
    ta.style.height = need + 'px';
    ta.style.overflowY = ta.scrollHeight > 144 ? 'auto' : 'hidden';
  }
  function count() {
    var n = Array.from(ta.value).length;
    var rest = MAX - n;
    root.style.setProperty('--p', Math.min(1, n / MAX).toFixed(3));
    root.classList.toggle('is-near', rest <= 20);
    root.classList.toggle('is-over', rest < 0);
    left.textContent = rest;
    var bad = n === 0 || rest < 0;
    send.setAttribute('aria-disabled', String(bad));
    if (rest === 20 || rest === 0 || rest === -1) sr.textContent = rest >= 0 ? rest + ' characters left' : 'Over the character limit';
  }
  ta.addEventListener('input', function () { grow(); count(); });
  send.addEventListener('click', function () {
    if (send.getAttribute('aria-disabled') === 'true') { ta.focus(); return; }
    ta.value = '';
    grow(); count();
    sr.textContent = 'Reply posted';
    send.textContent = 'Posted';
    setTimeout(function () { if (root.isConnected) send.textContent = 'Post'; }, 1400);
  });
  grow(); count();
})();
</script>
--- Code end ---

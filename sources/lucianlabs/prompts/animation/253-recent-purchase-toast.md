---
source: "lucianlabs"
id: "253"
title: "Recent purchase notification"
category: "Social Proof"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#253"
tags: ["social-proof", "toast", "fomo", "ecommerce", "notification"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Recent purchase notification (253, Social Proof)
[What it does] In the bottom left of a store page, a notice like “Kim from Busan just bought a linen shirt” pops up with a product photo, and once the bar beneath it runs out it fades away and another purchase shows up a little later. Rest the pointer on it to stop the bar, and press close to fold it away, after which a brief “Stop showing these” confirmation appears.
[How to use it] When a notice appears, rest the pointer on it to pause it, then try the close button

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
<!-- Lucian UX/UI Prompt #253 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#253 -->
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
.u253{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u253-pg{position:absolute;inset:0;padding:20px 18px}
.u253-pg h3{margin:0 0 12px;font-size:16px;font-weight:900;letter-spacing:-.03em}
.u253-gd{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.u253-gd div i{display:block;height:128px;border-radius:14px}
.u253-gd b{display:block;margin-top:7px;font-size:11.5px;font-weight:800}
.u253-gd span{font-size:11px;font-weight:850;color:var(--ux-ink-2)}
.u253-tt{position:absolute;left:12px;bottom:12px;width:268px;display:flex;align-items:center;gap:10px;padding:10px 30px 13px 10px;border-radius:16px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 18px 36px -14px var(--ux-shadow-strong);transform-origin:20% 100%;transform:translateY(130%) scale(.9);opacity:0;transition:transform .5s cubic-bezier(.3,1.4,.5,1),opacity .3s;overflow:hidden}
.u253-tt.is-on{transform:none;opacity:1}
.u253-tt.is-shut{transform:translateY(20px) scale(.85);opacity:0;transition:transform .35s cubic-bezier(.5,0,.75,0),opacity .3s}
.u253-th{position:relative;flex:none;width:44px;height:44px;border-radius:11px}
.u253-th::after{content:"";position:absolute;inset:9px 11px;border-radius:6px 6px 3px 3px;background:rgba(255,255,255,.65)}
.u253-tx{min-width:0;font-size:11px;line-height:1.4;font-weight:650;color:var(--ux-ink-2)}
.u253-tx b{color:var(--ux-ink);font-weight:850}
.u253-tx small{display:flex;align-items:center;gap:4px;margin-top:2px;font-size:9.5px;font-weight:750;color:var(--ux-ink-3)}
.u253-tx small::before{content:"";width:10px;height:10px;border-radius:50%;background:#10B981 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 10 10'%3E%3Cpath d='M2.8 5.2l1.5 1.5 3-3.2' fill='none' stroke='white' stroke-width='1.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/100%}
.u253-x{position:absolute;right:6px;top:6px;width:22px;height:22px;border:0;border-radius:50%;background:none;color:var(--ux-ink-3);display:grid;place-items:center;cursor:pointer}
.u253-x:hover,.u253-x.g-hov{background:var(--ux-surface-2);color:var(--ux-ink)}
.u253-x svg{width:10px;height:10px}
.u253-x:focus-visible,.u253-un:focus-visible{outline:2px solid var(--ux-accent);outline-offset:1px}
.u253-tm{position:absolute;left:0;bottom:0;height:3px;width:100%;background:var(--ux-accent);transform-origin:0 50%;opacity:.7}
.u253-ok{position:absolute;left:12px;bottom:12px;display:flex;align-items:center;gap:10px;height:40px;padding:0 6px 0 14px;border-radius:999px;background:var(--ux-ink);color:var(--ux-surface);font-size:11px;font-weight:750;transform:translateY(140%);transition:transform .45s cubic-bezier(.3,1.4,.5,1)}
.u253-ok.is-on{transform:none}
.u253-un{height:28px;padding:0 11px;border:0;border-radius:999px;background:color-mix(in srgb,var(--ux-surface) 18%,transparent);color:var(--ux-surface);font:inherit;font-size:10.5px;font-weight:850;cursor:pointer}
@media (prefers-reduced-motion: reduce){.u253-tt,.u253-tt.is-shut,.u253-ok{transition:opacity .2s}}
</style>
<div class="ux u253">
  <div class="u253-pg" aria-hidden="true"><h3>Summer arrivals</h3><div class="u253-gd"><div><i style="background:linear-gradient(160deg,#F5F5F4,#D6D3D1)"></i><b>Linen shirt</b><span>$39</span></div><div><i style="background:linear-gradient(160deg,#DBEAFE,#93C5FD)"></i><b>Half pants</b><span>$32</span></div></div></div>
  <div class="u253-tt" role="status"><span class="u253-th"></span><div class="u253-tx"></div><button type="button" class="u253-x" aria-label="Close notice"><svg viewBox="0 0 10 10" aria-hidden="true"><path d="M2 2l6 6M8 2L2 8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button><i class="u253-tm" aria-hidden="true"></i></div>
  <div class="u253-ok" role="status"><span>Purchase notices off</span><button type="button" class="u253-un" tabindex="-1">Undo</button></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var tt = root.querySelector('.u253-tt'), th = root.querySelector('.u253-th'), tx = root.querySelector('.u253-tx'), tm = root.querySelector('.u253-tm'), x = root.querySelector('.u253-x'), ok = root.querySelector('.u253-ok'), un = root.querySelector('.u253-un');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var B = [['Busan', 'Kim', 'a linen shirt', 2, '#E7E5E4', ''], ['Seoul', 'Lee', 'half pants', 5, '#BFDBFE', ''], ['Daegu', 'Park', 'a canvas tote', 1, '#FDE68A', ''], ['Gwangju', 'Choi', 'a bucket hat', 8, '#BBF7D0', '']];
  var WHO = '%n from %c just bought ';
  var SHOW = 4200, GAP = 1300, k = 0, left = 0, last = 0, hold = false, off = false, state = 'wait', wait = 900, vis = true, raf = 0;
  function fill(b) {
    th.style.background = 'linear-gradient(150deg,' + b[4] + ',color-mix(in srgb,' + b[4] + ' 70%,#000))';
    tx.innerHTML = '<span></span><small></small>';
    var s = tx.firstChild; s.appendChild(document.createTextNode(WHO.replace('%c', b[0]).replace('%n', b[1]))); var bb = document.createElement('b'); bb.textContent = b[2]; s.appendChild(bb); s.appendChild(document.createTextNode(b[5] + (b[5] ? '' : '')));
    tx.lastChild.textContent = b[3] + ' min ago · Verified';
  }
  function tick(now) {
    raf = 0; if (!root.isConnected) return;
    var dt = Math.min(64, now - last); last = now;
    if (vis && !off && !hold) {
      if (state === 'wait') { wait -= dt; if (wait <= 0) { fill(B[k]); k = (k + 1) % B.length; tt.classList.remove('is-shut'); tt.classList.add('is-on'); state = 'show'; left = SHOW; } }
      else if (state === 'show') { left -= dt; if (left <= 0) { tt.classList.remove('is-on'); state = 'wait'; wait = GAP; } }
    }
    tm.style.transform = 'scaleX(' + (state === 'show' ? Math.max(0, left / SHOW) : 0).toFixed(3) + ')';
    raf = requestAnimationFrame(tick);
  }
  tt.addEventListener('pointerenter', function () { hold = true; });
  tt.addEventListener('pointerleave', function () { hold = false; });
  tt.addEventListener('focusin', function () { hold = true; });
  tt.addEventListener('focusout', function () { hold = false; });
  x.addEventListener('click', function () {
    off = true; hold = false; state = 'wait'; tt.classList.remove('is-on'); tt.classList.add('is-shut');
    setTimeout(function () { ok.classList.add('is-on'); un.tabIndex = 0; un.focus({ preventScroll: true }); }, rm ? 0 : 280);
  });
  un.addEventListener('click', function () { ok.classList.remove('is-on'); un.tabIndex = -1; off = false; wait = 700; });
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; }).observe(root);
  last = performance.now(); raf = requestAnimationFrame(tick);
})();
</script>
--- Code end ---

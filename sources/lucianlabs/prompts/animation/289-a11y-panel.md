---
source: "lucianlabs"
id: "289"
title: "Live display settings panel"
category: "Navigation"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#289"
tags: ["accessibility", "settings", "font-size", "contrast", "a11y"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Live display settings panel (289, Navigation)
[What it does] Press the person-shaped button in the corner of a website and a display settings panel unfolds. Raise the text size and the page text behind grows smoothly; turn on high contrast and the background and text get bolder; turn on link highlighting and every link gains an underline and outline. You can widen line spacing too, and Reset brings every setting back together.
[How to use it] Press the button in the bottom right and change text size, contrast and link highlighting

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
<!-- Lucian UX/UI Prompt #289 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#289 -->
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
.u289{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink);--fs:1;--lh:1.6}
.u289-pg{position:absolute;inset:0;padding:22px 20px;background:var(--bg,transparent);color:var(--fg,var(--ux-ink));transition:background .3s,color .3s}
.u289.is-hc .u289-pg{--bg:#000;--fg:#fff}
.u289-pg h3{margin:0;font-size:calc(20px * var(--fs));font-weight:900;letter-spacing:-.03em;transition:font-size .3s}
.u289-pg p{margin:10px 0 0;font-size:calc(12px * var(--fs));line-height:var(--lh);font-weight:600;color:var(--pc,var(--ux-ink-2));transition:font-size .3s,line-height .3s}
.u289.is-hc .u289-pg p{--pc:#fff}
.u289-pg nav{display:flex;gap:14px;margin-top:12px}
.u289-pg a{font-size:calc(12px * var(--fs));font-weight:800;color:var(--ux-accent);text-decoration:none;border-radius:4px;transition:font-size .3s,box-shadow .2s}
.u289.is-hc .u289-pg a{color:#FDE047}
.u289.is-ln .u289-pg a{text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:3px;box-shadow:0 0 0 2px currentColor;padding:1px 4px}
.u289-fb{position:absolute;right:14px;bottom:14px;z-index:3;width:46px;height:46px;border:0;border-radius:50%;background:#2563EB;color:#fff;display:grid;place-items:center;cursor:pointer;box-shadow:0 10px 22px -10px #2563EB}
.u289-fb svg{width:24px;height:24px}
.u289-pn{position:absolute;right:14px;bottom:70px;z-index:3;width:212px;padding:12px;border-radius:18px;background:var(--ux-surface);color:var(--ux-ink);box-shadow:0 0 0 1px var(--ux-line),0 22px 44px -16px rgba(0,0,0,.4);transform-origin:calc(100% - 23px) calc(100% + 34px);transform:scale(.5);opacity:0;pointer-events:none;transition:transform .35s cubic-bezier(.3,1.4,.5,1),opacity .2s}
.u289.is-open .u289-pn{transform:none;opacity:1;pointer-events:auto}
.u289-pn b{display:block;font-size:12.5px;font-weight:900}
.u289-fs{display:flex;align-items:center;gap:6px;margin-top:10px;padding:6px;border-radius:11px;background:var(--ux-surface-2)}
.u289-fs span{flex:1;font-size:11px;font-weight:800}
.u289-fs em{font-style:normal;font-size:10.5px;font-weight:850;color:var(--ux-ink-3);font-variant-numeric:tabular-nums;min-width:34px;text-align:center}
.u289-fs button{width:28px;height:28px;border:0;border-radius:8px;background:var(--ux-surface);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink);font:inherit;font-weight:900;cursor:pointer}
.u289-fs button:disabled{opacity:.35;cursor:default}
.u289-dn{font-size:10px}.u289-up{font-size:14px}
.u289-rw{display:flex;align-items:center;justify-content:space-between;margin-top:6px;padding:6px 6px 6px 8px;font-size:11px;font-weight:800}
.u289-sw{position:relative;width:34px;height:20px;border:0;border-radius:10px;background:var(--ux-surface-3);cursor:pointer;transition:background .2s}
.u289-sw::after{content:"";position:absolute;left:2px;top:2px;width:16px;height:16px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.25);transition:transform .25s cubic-bezier(.3,1.5,.5,1)}
.u289-sw[aria-checked="true"]{background:#2563EB}
.u289-sw[aria-checked="true"]::after{transform:translateX(14px)}
.u289-rs{width:100%;height:30px;margin-top:6px;border:0;border-radius:9px;background:none;color:var(--ux-ink-3);font:inherit;font-size:10.5px;font-weight:800;cursor:pointer}
.u289 button:focus-visible{outline:2px solid #2563EB;outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u289-pn,.u289-pg,.u289-pg h3,.u289-pg p,.u289-pg a{transition:none}}
</style>
<div class="ux u289">
  <div class="u289-pg"><h3>Spring garden care</h3><p>Once it warms up, check the soil first. Loosening soil packed down over winter lets the roots breathe.</p><nav><a href="#">Watering guide</a><a href="#">Seeds we love</a></nav></div>
  <div class="u289-pn" role="dialog" aria-hidden="true"><b>Display settings</b>
    <div class="u289-fs"><span>Text size</span><button type="button" class="u289-dn" aria-label="Smaller text">A</button><em class="u289-fv"></em><button type="button" class="u289-up" aria-label="Larger text">A</button></div>
    <div class="u289-sws"></div>
    <button type="button" class="u289-rs">Reset</button>
  </div>
  <button type="button" class="u289-fb" aria-label="Open display settings" aria-expanded="false"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="4.5" r="2.2" fill="currentColor"/><path d="M4.5 8.5l7.5 1.5 7.5-1.5M12 10v5m0 0l-3.5 6.5M12 15l3.5 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var fb = root.querySelector('.u289-fb'), pn = root.querySelector('.u289-pn'), dn = root.querySelector('.u289-dn'), up = root.querySelector('.u289-up'), fv = root.querySelector('.u289-fv'), sws = root.querySelector('.u289-sws'), rs = root.querySelector('.u289-rs');
  var SW = ['High contrast', 'Highlight links', 'Wider line spacing'], CLS = ['is-hc', 'is-ln', 'is-lh'];
  var STEPS = [0.9, 1, 1.15, 1.3], k = 1, on = [false, false, false];
  Array.prototype.forEach.call(root.querySelectorAll('.u289-pg a'), function (a) { a.addEventListener('click', function (e) { e.preventDefault(); }); });
  var B = SW.map(function (t, i) {
    var r = document.createElement('div'); r.className = 'u289-rw'; r.innerHTML = '<span></span><button type="button" class="u289-sw" role="switch" aria-checked="false"></button>';
    r.firstChild.textContent = t; var b = r.lastChild; b.setAttribute('aria-label', t);
    b.addEventListener('click', function () { on[i] = !on[i]; sync(); });
    sws.appendChild(r); return b;
  });
  function sync() {
    root.style.setProperty('--fs', STEPS[k]); root.style.setProperty('--lh', on[2] ? 2 : 1.6);
    fv.textContent = Math.round(STEPS[k] * 100) + '%'; dn.disabled = k === 0; up.disabled = k === STEPS.length - 1;
    B.forEach(function (b, i) { b.setAttribute('aria-checked', on[i]); root.classList.toggle(CLS[i], on[i]); });
  }
  dn.addEventListener('click', function () { if (k > 0) { k--; sync(); } });
  up.addEventListener('click', function () { if (k < STEPS.length - 1) { k++; sync(); } });
  rs.addEventListener('click', function () { k = 1; on = [false, false, false]; sync(); });
  function open(v) { root.classList.toggle('is-open', v); pn.setAttribute('aria-hidden', !v); fb.setAttribute('aria-expanded', v); if (v) setTimeout(function () { up.focus({ preventScroll: true }); }, 200); }
  fb.addEventListener('click', function () { open(!root.classList.contains('is-open')); });
  root.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('is-open')) { open(false); fb.focus(); } });
  sync();
})();
</script>
--- Code end ---

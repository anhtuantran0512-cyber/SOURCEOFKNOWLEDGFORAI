---
source: "lucianlabs"
id: "314"
title: "Target-shaped morphing cursor"
category: "Cursor & Hover"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#314"
tags: ["cursor", "morph", "hover", "pointer", "spring"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Target-shaped morphing cursor (314, Cursor & Hover)
[What it does] A small round cursor follows across the screen like a spring, stretching to wrap a button's shape over buttons and thinning into a vertical bar over text. Over a photo it swells into a large circle that says View, and over a link it becomes a dot holding an arrow. While wrapping a button it is pulled slightly toward your fingertip so it feels stuck to your hand.
[How to use it] Move the cursor over the buttons, text, photo and link

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
<!-- Lucian UX/UI Prompt #314 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#314 -->
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
.u314{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:#F7F5F0;box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:#22201C;cursor:none;padding:22px;display:flex;flex-direction:column;gap:16px}
.u314 *{cursor:none}
.u314-tb{display:flex;gap:8px;align-items:center}
.u314-ib{width:42px;height:42px;border:0;border-radius:14px;background:#fff;box-shadow:0 0 0 1px rgba(34,32,28,.08);display:grid;place-items:center;color:#22201C;padding:0}
.u314-ib svg{width:18px;height:18px}
.u314-fb{margin-left:auto;height:38px;padding:0 18px;border:0;border-radius:999px;background:#22201C;color:#F7F5F0;font:inherit;font-size:13px;font-weight:750}
.u314-tx{margin:0;font-size:14px;line-height:1.6;font-weight:550;color:#3B3832;word-break:keep-all}
.u314-row{display:flex;gap:14px;align-items:flex-end;margin-top:auto}
.u314-ph{width:150px;height:104px;border-radius:16px;background:linear-gradient(140deg,#FFB86B,#F06595 60%,#845EF7)}
.u314-ln{font-size:14px;font-weight:800;color:#22201C;text-decoration:underline;text-underline-offset:4px;padding:6px 0}
.u314-ib:focus-visible,.u314-fb:focus-visible,.u314-ln:focus-visible{outline:2px solid #845EF7;outline-offset:3px}
.u314-cur{position:absolute;left:0;top:0;width:16px;height:16px;margin:0;border-radius:999px;background:rgba(34,32,28,.85);pointer-events:none;z-index:5;display:grid;place-items:center;color:#fff;font-size:12px;font-weight:800;opacity:0;transition:width .28s cubic-bezier(.3,1.4,.5,1),height .28s cubic-bezier(.3,1.4,.5,1),border-radius .28s,background .2s,opacity .2s;mix-blend-mode:normal}
.u314-cur.is-on{opacity:1}
.u314-cur.is-btn{background:rgba(34,32,28,.1)}
.u314-cur.is-text{background:#845EF7}
.u314-cur.is-img{background:rgba(255,255,255,.92);color:#22201C;box-shadow:0 10px 24px -8px rgba(0,0,0,.4)}
.u314-cur.is-link{background:#845EF7}
.u314-cur span{opacity:0;transition:opacity .2s;white-space:nowrap}
.u314-cur.is-img span,.u314-cur.is-link span{opacity:1}
@media (prefers-reduced-motion: reduce){.u314-cur{transition:opacity .2s}}
</style>
<div class="ux u314">
  <div class="u314-tb">
    <button type="button" class="u314-ib" data-k="btn" aria-label="Like"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg></button>
    <button type="button" class="u314-ib" data-k="btn" aria-label="Share"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 15V4M7 9l5-5 5 5M5 14v5h14v-5"/></svg></button>
    <button type="button" class="u314-ib" data-k="btn" aria-label="Save"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 4h12v16l-6-4-6 4z"/></svg></button>
    <button type="button" class="u314-fb" data-k="btn">Follow</button>
  </div>
  <p class="u314-tx" data-k="text">Motion adds story to a screen. When the cursor takes on the shape of what it points at, your fingertip knows what it can do before you click.</p>
  <div class="u314-row"><div class="u314-ph" data-k="img" aria-hidden="true"></div><a class="u314-ln" href="#" data-k="link">Learn more</a></div>
  <div class="u314-cur" aria-hidden="true"><span class="u314-cl"></span></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var cur = root.querySelector('.u314-cur'), cl = root.querySelector('.u314-cl');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var pos = { x: 170, y: 300 }, sp = { x: 170, y: 300 }, vel = { x: 0, y: 0 }, mode = '', box = null, raf = 0, last = 0;
  root.querySelector('.u314-ln').addEventListener('click', function (e) { e.preventDefault(); });
  function rel(e) { var r = root.getBoundingClientRect(), k = root.offsetWidth / (r.width || 1); return { x: (e.clientX - r.left) * k, y: (e.clientY - r.top) * k, k: k, r: r }; }
  function set(m, el, p) {
    mode = m; cur.className = 'u314-cur is-on' + (m ? ' is-' + m : '');
    box = null;
    if (m === 'btn') { var b = el.getBoundingClientRect(); box = { x: (b.left - p.r.left) * p.k, y: (b.top - p.r.top) * p.k, w: b.width * p.k, h: b.height * p.k, rad: getComputedStyle(el).borderRadius }; }
    cl.textContent = m === 'img' ? 'View' : m === 'link' ? '→' : '';
  }
  function target() {
    if (mode === 'btn' && box) { var cxp = box.x + box.w / 2, cyp = box.y + box.h / 2; return { x: cxp + (pos.x - cxp) * 0.15, y: cyp + (pos.y - cyp) * 0.15, w: box.w + 8, h: box.h + 8, r: box.rad }; }
    if (mode === 'text') return { x: pos.x, y: pos.y, w: 3, h: 24, r: '2px' };
    if (mode === 'img') return { x: pos.x, y: pos.y, w: 64, h: 64, r: '999px' };
    if (mode === 'link') return { x: pos.x, y: pos.y, w: 30, h: 30, r: '999px' };
    return { x: pos.x, y: pos.y, w: 16, h: 16, r: '999px' };
  }
  function frame(now) {
    raf = 0;
    if (!root.isConnected) return;
    var dt = Math.min(0.033, Math.max(0, (now - last) / 1000)); last = now;
    var t = target();
    if (rm) { sp.x = t.x; sp.y = t.y; }
    else { vel.x += ((t.x - sp.x) * 420 - vel.x * 30) * dt; vel.y += ((t.y - sp.y) * 420 - vel.y * 30) * dt; sp.x += vel.x * dt; sp.y += vel.y * dt; }
    cur.style.width = t.w + 'px'; cur.style.height = t.h + 'px'; cur.style.borderRadius = t.r;
    cur.style.transform = 'translate(' + (sp.x - t.w / 2).toFixed(1) + 'px,' + (sp.y - t.h / 2).toFixed(1) + 'px)';
    if (Math.abs(t.x - sp.x) + Math.abs(t.y - sp.y) > 0.2 || Math.abs(vel.x) + Math.abs(vel.y) > 1) raf = requestAnimationFrame(frame);
  }
  function kick() { if (!raf) { last = performance.now(); raf = requestAnimationFrame(frame); } }
  root.addEventListener('pointermove', function (e) {
    var p = rel(e); pos.x = p.x; pos.y = p.y;
    var hitEl = document.elementFromPoint(e.clientX, e.clientY) || e.target, el = hitEl.closest && hitEl.closest('[data-k]');
    var m = el && root.contains(el) ? el.getAttribute('data-k') : '';
    if (m !== mode || (m === 'btn' && (!box || el !== set.last))) { set(m, el, p); set.last = el; }
    if (!cur.classList.contains('is-on')) { sp.x = p.x; sp.y = p.y; cur.classList.add('is-on'); }
    kick();
  });
  root.addEventListener('pointerleave', function () { cur.classList.remove('is-on'); mode = ''; set.last = null; });
})();
</script>
--- Code end ---

---
source: "lucianlabs"
id: "113"
title: "Pixel icon workbench"
category: "Layout, Schedule & Design"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#113"
tags: ["pixel-editor", "native", "spatial"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Pixel icon workbench (113, Layout, Schedule & Design)
[What it does] A workbench for drawing a small icon on an 8×8 grid. Press an empty cell to fill it or a filled one to erase it; drag to change every cell you pass over.
[How to use it] Press or drag across cells to paint. Esc restores the original drawing

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
<!-- Lucian UX/UI Prompt #113 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#113 -->
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
.u113{width:100%;max-width:400px;min-width:0;font-size:13px}.u113 button{font:inherit;color:inherit;cursor:pointer}.u113 input[type=range]{min-width:0;width:100%;accent-color:var(--ux-accent)}.u113 .sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}.u113{max-width:264px;padding:4px}.u113 .pixels{display:grid;grid-template-columns:repeat(8,1fr);gap:2px;aspect-ratio:1;padding:2px;background:var(--ux-line-2);border:5px solid var(--ux-surface);box-shadow:0 5px 18px var(--ux-shadow)}.u113 .pixel{border:0;border-radius:0;padding:0;min-height:0;aspect-ratio:1;background:var(--ux-surface);touch-action:none}.u113 .pixel[aria-pressed=true]{background:var(--ux-accent)}
</style>
<div class="ux u113"><div class="pixels" aria-label="8 × 8 pixel icon"></div></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling,q=s=>root.querySelector(s),qa=s=>[...root.querySelectorAll(s)];const initial=[10,11,12,13,17,22,25,30,33,38,41,46,50,51,52,53];let pixels=new Set(initial),drag=false,draw=true;q('.pixels').innerHTML=Array.from({length:64},(_,i)=>`<button class="pixel" data-i="${i}" aria-label="row ${Math.floor(i/8)+1}, column ${i%8+1}" aria-pressed="false"></button>`).join('');function paint(){qa('.pixel').forEach(b=>b.setAttribute('aria-pressed',pixels.has(+b.dataset.i)))}function dot(b){if(!b)return;draw?pixels.add(+b.dataset.i):pixels.delete(+b.dataset.i);paint()}qa('.pixel').forEach(b=>{b.onpointerdown=e=>{draw=!pixels.has(+b.dataset.i);drag=true;b.setPointerCapture(e.pointerId);dot(b)};b.onpointermove=e=>{if(drag&&b.hasPointerCapture(e.pointerId)){const el=document.elementFromPoint(e.clientX,e.clientY);if(el?.classList.contains('pixel'))dot(el)}};b.onpointerup=()=>drag=false;b.onpointercancel=()=>drag=false;b.onclick=e=>{if(e.detail===0){draw=!pixels.has(+b.dataset.i);dot(b)}}});root.onkeydown=e=>{if(e.key==='Escape'){pixels=new Set(initial);paint()}};paint();})();
</script>
--- Code end ---

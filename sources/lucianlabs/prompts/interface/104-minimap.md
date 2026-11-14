---
source: "lucianlabs"
id: "104"
title: "Canvas minimap"
category: "Layout, Schedule & Design"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#104"
tags: ["minimap", "native", "spatial"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Canvas minimap (104, Layout, Schedule & Design)
[What it does] A view onto part of a large artboard, with a minimap of the whole. Move the purple frame in the minimap and the view follows to that spot.
[How to use it] Drag the frame in the minimap. With it focused, the arrow keys move it too, and Esc returns it

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
<!-- Lucian UX/UI Prompt #104 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#104 -->
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
.u104{width:100%;max-width:400px;min-width:0;font-size:13px}.u104 button{font:inherit;color:inherit;cursor:pointer}.u104 input[type=range]{min-width:0;width:100%;accent-color:var(--ux-accent)}.u104 .sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}.u104{position:relative}.u104 .canvas{height:245px;overflow:hidden;position:relative;border:1px solid var(--ux-line-2);border-radius:7px;background:var(--ux-surface-2)}.u104 .artboard{position:absolute;width:600px;height:400px;transform:translate(var(--x,-100px),var(--y,-70px));transition:transform .3s;display:grid;grid-template-columns:repeat(3,150px);gap:35px;padding:30px}.u104 .art{height:150px;border:12px solid var(--ux-surface);background:linear-gradient(155deg,#dca778,#a26068);box-shadow:0 3px 12px var(--ux-shadow)}.u104 .art:nth-child(2n){background:linear-gradient(135deg,#7390be,#3f4b69)}.u104 .mini{width:136px;height:94px;position:absolute;bottom:11px;right:11px;border:3px solid var(--ux-surface);padding:0;border-radius:4px;box-shadow:0 3px 14px var(--ux-shadow-strong);touch-action:none;cursor:crosshair}.u104 .mini svg{width:100%;height:100%;display:block;pointer-events:none}.u104 .viewport{position:absolute;left:25px;top:18px;border:2px solid var(--ux-accent);background:#fff3;pointer-events:none}
</style>
<div class="ux u104"><div class="canvas" aria-label="Large artboard"><div class="artboard"><div class="art"></div><div class="art"></div><div class="art"></div><div class="art"></div><div class="art"></div><div class="art"></div></div></div><button class="mini" aria-label="Minimap position, move with arrow keys"><svg viewBox="0 0 600 400" aria-hidden="true"><rect width="600" height="400" fill="#c9cfda"/><g fill="#bf765f"><rect x="30" y="30" width="150" height="150"/><rect x="400" y="30" width="150" height="150"/><rect x="215" y="215" width="150" height="150"/></g><g fill="#5879ad"><rect x="215" y="30" width="150" height="150"/><rect x="30" y="215" width="150" height="150"/><rect x="400" y="215" width="150" height="150"/></g></svg><span class="viewport"></span></button><output class="sr" aria-live="polite"></output></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling,q=s=>root.querySelector(s),qa=s=>[...root.querySelectorAll(s)];let x=100,y=70;function paint(){x=Math.max(0,Math.min(600-q(".canvas").clientWidth,x));y=Math.max(0,Math.min(400-q(".canvas").clientHeight,y));root.style.setProperty("--x",-x+"px");root.style.setProperty("--y",-y+"px");const m=q(".mini"),v=q(".viewport");v.style.left=x/600*m.clientWidth+"px";v.style.top=y/400*m.clientHeight+"px";v.style.width=q(".canvas").clientWidth/600*m.clientWidth+"px";v.style.height=q(".canvas").clientHeight/400*m.clientHeight+"px";q("output").textContent="Position "+x+", "+y}function point(e){const r=q(".mini").getBoundingClientRect();x=Math.round((e.clientX-r.left)/r.width*600-q(".canvas").clientWidth/2);y=Math.round((e.clientY-r.top)/r.height*400-q(".canvas").clientHeight/2);paint()}q(".mini").onpointerdown=e=>{e.currentTarget.setPointerCapture(e.pointerId);point(e)};q(".mini").onpointermove=e=>{if(e.currentTarget.hasPointerCapture(e.pointerId))point(e)};q(".mini").onkeydown=e=>{const d={ArrowLeft:[-40,0],ArrowRight:[40,0],ArrowUp:[0,-40],ArrowDown:[0,40]}[e.key];if(d){e.preventDefault();x+=d[0];y+=d[1];paint()}if(e.key==="Escape"||e.key==="Home"){e.preventDefault();x=100;y=70;paint()}};new ResizeObserver(paint).observe(q(".canvas"));paint();})();
</script>
--- Code end ---

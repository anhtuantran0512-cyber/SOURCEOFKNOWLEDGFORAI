---
source: "lucianlabs"
id: "111"
title: "Task duration editor"
category: "Layout, Schedule & Design"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#111"
tags: ["gantt", "native", "spatial"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Task duration editor (111, Layout, Schedule & Design)
[What it does] A Gantt editor for changing a task’s start day and length on a weekly chart. Drag the bar to move its start or the end handle to change its length, and the summary follows.
[How to use it] Drag the purple bar or its end handle. The arrow keys work too

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
<!-- Lucian UX/UI Prompt #111 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#111 -->
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
.u111{width:100%;max-width:400px;min-width:0;font-size:13px}.u111 button{font:inherit;color:inherit;cursor:pointer}.u111 input[type=range]{min-width:0;width:100%;accent-color:var(--ux-accent)}.u111 .sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}.u111{padding:24px 4px}.u111 .schedule{display:grid;grid-template-columns:64px minmax(0,1fr);gap:17px 10px}.u111 .days{display:flex;justify-content:space-around;font-size:12px;color:var(--ux-ink-2);padding-bottom:4px}.u111 .lane{height:58px;position:relative;background:repeating-linear-gradient(90deg,var(--ux-surface-2) 0 calc(14.285% - 1px),var(--ux-line) calc(14.285% - 1px) 14.285%);border-radius:4px}.u111 .task{position:absolute;left:var(--start,14.285%);width:var(--duration,42.855%);height:38px;top:10px;border-radius:5px;background:var(--ux-accent);color:var(--ux-accent-ink);font-size:13px;padding:0 12px;border:0;text-align:left;white-space:nowrap;touch-action:none;cursor:grab}.u111 .other{left:0;width:28.57%;background:var(--ux-surface-3);color:var(--ux-ink-2);padding:10px}.u111 .rowname{align-self:center;font-size:13px}.u111 .duration{position:absolute;top:8px;left:calc(var(--start,14.285%) + var(--duration,42.855%) - 11px);height:42px;width:22px;background:transparent;border:0;padding:0;color:var(--ux-accent-ink);cursor:ew-resize;touch-action:none}.u111 .duration:after{content:"";display:block;height:17px;width:3px;margin:auto;background:currentColor;border-radius:2px}
</style>
<div class="ux u111"><div class="schedule"><span></span><div class="days"><span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span></div><span class="rowname">Research</span><div class="lane"><span class="task other">2 days</span></div><span class="rowname">Design</span><div class="lane editable"><button class="task selected" aria-label="Design start day, move with arrow keys">3 days</button><button class="duration" aria-label="Design duration" role="slider" aria-valuemin="1" aria-valuemax="6" aria-valuenow="3"></button></div></div><output class="sr" aria-live="polite"></output></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling,q=s=>root.querySelector(s),qa=s=>[...root.querySelectorAll(s)];let s=2,d=3;const days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];function paint(){s=Math.max(1,Math.min(7,s));d=Math.max(1,Math.min(8-s,d));root.style.setProperty('--start',(s-1)/7*100+'%');root.style.setProperty('--duration',d/7*100+'%');q('.selected').textContent=d+(d>1?' days':' day');q('.duration').setAttribute('aria-valuenow',d);q('.duration').setAttribute('aria-valuemax',8-s);q('.selected').setAttribute('aria-label','Design starts '+days[s-1]+', move with arrow keys');q('output').textContent=days[s-1]+'–'+days[s+d-2]+' · '+d+(d>1?' days':' day')}function reset(){s=2;d=3;paint()}qa('.selected,.duration').forEach(b=>{b.onkeydown=e=>{if(['ArrowLeft','ArrowRight','Home','End','Escape'].includes(e.key)){e.preventDefault();if(e.key==='Escape'){reset();return}let delta=e.key==='ArrowRight'?1:-1;if(b.matches('.duration'))d=e.key==='Home'?1:e.key==='End'?8-s:d+delta;else s=e.key==='Home'?1:e.key==='End'?7:s+delta;paint()}};b.onpointerdown=e=>b.setPointerCapture(e.pointerId);b.onpointermove=e=>{if(b.hasPointerCapture(e.pointerId)){const r=q('.editable').getBoundingClientRect(),day=Math.round((e.clientX-r.left)/r.width*7);if(b.matches('.duration'))d=day-s+1;else s=day+1;paint()}}});paint();})();
</script>
--- Code end ---

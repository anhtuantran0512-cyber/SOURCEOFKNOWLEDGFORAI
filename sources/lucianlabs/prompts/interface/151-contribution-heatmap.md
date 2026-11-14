---
source: "lucianlabs"
id: "151"
title: "Weekly contribution grid"
category: "Analytics & Data"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#151"
tags: ["contribution-heatmap", "analytics"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Weekly contribution grid (151, Analytics & Data)
[What it does] A heatmap of 84 days of contributions laid out week by week. Move the date slider and that day’s cell is marked, with its date and count shown below.
[How to use it] Move the date slider below

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
<!-- Lucian UX/UI Prompt #151 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#151 -->
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

<style>.u151{width:100%;max-width:390px;padding:16px;position:relative;font-size:13px;line-height:1.45}.u151 button{border:1px solid var(--ux-line-2);background:var(--ux-surface);padding:8px 12px;border-radius:10px;min-height:44px;font-size:12px;transition:background .2s,transform .3s var(--ux-ease)}.u151 button[aria-pressed="true"]{background:var(--ux-accent-soft);border-color:var(--ux-accent)}.u151 button:active{transform:scale(.97)}.u151 small{color:var(--ux-ink-2);font-size:12px}.u151 .status{margin-top:10px;color:var(--ux-ink-2);font-size:12px;line-height:1.5}.u151 .status b{color:var(--ux-ink)}.u151 .controls{display:flex;gap:6px;flex-wrap:wrap;margin-top:12px}.u151 svg{display:block;width:100%;overflow:visible}.u151 svg text{font-family:inherit;fill:var(--ux-ink-2);font-size:11px}.u151 .gridline{stroke:var(--ux-line-2);fill:none}.u151 input[type="range"]{width:100%;height:44px;accent-color:var(--ux-accent);margin:0}.u151 .inline{display:flex;align-items:center;justify-content:space-between;gap:12px}.u151 .month{display:flex;justify-content:space-between;color:var(--ux-ink-2);font-size:12px}.u151 .heat{display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:repeat(7,20px);grid-auto-flow:column;gap:4px;margin:12px 0 0}.u151 .heat i{border-radius:4px;background:color-mix(in srgb,var(--ux-mint) calc(var(--v)*20%),var(--ux-surface-3));transition:background .25s,transform .25s}.u151 .heat i.chosen{outline:2px solid var(--ux-ink);outline-offset:1px;transform:translateY(-2px)}.u151 .date{font-size:12px;color:var(--ux-ink-2)}.u151 .count{font-weight:750;color:var(--ux-mint);font-size:18px}.u151{min-height:0;box-shadow:none}.u151 .status{background:transparent;border:0;padding:0;min-height:0;height:auto}.u151 .inline{margin-bottom:8px}</style>
<div class="ux u151"><div class="month"><span>Jul</span><span>Aug</span><span>Sep</span></div><div class="heat" aria-hidden="true"></div><input class="range" type="range" min="0" max="83" step="1" value="0" aria-label="Contribution date"><div class="inline"><time class="date"></time><output class="count" aria-live="polite"></output></div></div>

<script>
(()=>{const root=document.currentScript.previousElementSibling,q=s=>root.querySelector(s),data=Array.from({length:84},(_,i)=>(i*7+i%6)%5);q('.heat').innerHTML=data.map((v,i)=>`<i data-i="${i}" style="--v:${v}"></i>`).join('');function draw(){let i=+q('.range').value;root.querySelectorAll('.heat i').forEach((t,n)=>t.classList.toggle('chosen',n===i));let date=`${['Jul','Aug','Sep'][Math.floor(i/28)]} ${i%28+1}`;q('.date').textContent=date;q('.count').textContent=data[i]*3+' contributions';q('.range').setAttribute('aria-valuetext',date+', '+data[i]*3+' contributions');root.dataset.state=String(i)}q('.range').oninput=draw;q('.heat').onpointerdown=e=>{let t=e.target.closest('[data-i]');if(t){q('.range').value=t.dataset.i;draw()}};draw()})();
</script>
--- Code end ---

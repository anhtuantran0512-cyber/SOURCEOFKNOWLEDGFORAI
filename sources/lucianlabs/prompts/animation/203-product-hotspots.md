---
source: "lucianlabs"
id: "203"
title: "Leader-lined product hotspots"
category: "Commerce & Pricing"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#203"
tags: ["hotspot", "annotation", "product", "color-swatch", "headphones"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Leader-lined product hotspots (203, Commerce & Pricing)
[What it does] A front view of premium headphones: a slim stainless steel frame runs straight down into both arms, a knit-mesh canopy hangs from its ends like a hammock, and the arms hold aluminum ear cups with mesh cushions on the inside. Hover a softly pulsing pin and a dotted line draws from it down to a note card that slides up, while that part brightens and the rest dims. On the crown pin the dial's ridges turn, and on the mic pin sound waves ripple out and get cancelled. Press a color dot below and the cups, canopy and cushions blend to the new finish as the color name rolls over.
[How to use it] Hover the pins on the headphones, then try the color dots below

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
<!-- Lucian UX/UI Prompt #203 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#203 -->
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
.u203{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:radial-gradient(70% 55% at 50% 40%,#FFFFFF,transparent 75%),linear-gradient(165deg,#F4F6F8,#E6E9ED);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:#1D1D1F;--c1:#CFE0EA;--c2:#97B5C7;--cn:#DFEAF0;--cu:#B3CAD7}
.u203-sv{position:absolute;left:0;top:0;width:340px;height:262px;overflow:visible}
.u203-sv stop{transition:stop-color .6s ease}
.u203-part{transition:opacity .3s,filter .3s}
.u203.is-act .u203-part{opacity:.45}
.u203.is-act .u203-part.is-on{filter:drop-shadow(0 0 7px rgba(0,113,227,.5))}
.u203-ln{fill:none;stroke:#0071E3;stroke-width:1.6;stroke-dasharray:3 3}
.u203-dot{fill:#0071E3}

.u203-kn{transition:none}
.u203.is-a3 .u203-kn{animation:u203-kn .5s linear infinite}
@keyframes u203-kn{to{transform:translateX(-2.5px)}}

.u203-wv path{fill:none;stroke:#0071E3;stroke-width:1.6;stroke-linecap:round;opacity:0}
.u203.is-a1 .u203-wv path{animation:u203-wv 1.4s ease-out infinite}
.u203.is-a1 .u203-wv path:nth-child(2){animation-delay:.35s}
.u203.is-a1 .u203-wv path:nth-child(3){animation-delay:.7s}
@keyframes u203-wv{0%{opacity:0;transform:translateX(6px)}25%{opacity:.9}100%{opacity:0;transform:translateX(-10px)}}
.u203.is-a2 .u203-cs{animation:u203-cs 1.2s ease-in-out infinite}
@keyframes u203-cs{50%{filter:brightness(1.12)}}
.u203-pin{position:absolute;left:0;top:0;width:26px;height:26px;margin:-13px 0 0 -13px;padding:0;border:0;border-radius:50%;background:rgba(0,113,227,.18);cursor:pointer;z-index:2;transition:opacity .25s,transform .25s cubic-bezier(.3,1.6,.5,1)}
.u203-pin::before{content:"";position:absolute;inset:7px;border-radius:50%;background:#fff;box-shadow:0 0 0 3px #0071E3}
.u203-pin::after{content:"";position:absolute;inset:0;border-radius:50%;border:2px solid #0071E3;animation:u203-p 2.2s infinite}
@keyframes u203-p{from{transform:scale(.6);opacity:1}to{transform:scale(1.7);opacity:0}}
.u203.is-act .u203-pin{opacity:.35}
.u203.is-act .u203-pin.is-on{opacity:1;transform:scale(1.15)}
.u203-pin:focus-visible{outline:2px solid #1D1D1F;outline-offset:3px}
.u203-ft{position:absolute;left:16px;right:16px;top:266px;height:58px}
.u203-sws{position:absolute;inset:0;display:flex;align-items:center;gap:10px;padding:0 6px;transition:opacity .25s,transform .35s cubic-bezier(.3,1.2,.5,1)}
.u203.is-act .u203-sws{opacity:0;transform:translateY(8px);pointer-events:none}
.u203-cl{flex:1;min-width:0}
.u203-cl small{display:block;font-size:10px;font-weight:800;color:#86868B}
.u203-nw{position:relative;display:block;height:18px;margin-top:2px;overflow:hidden}
.u203-nw b{position:absolute;left:0;top:0;white-space:nowrap;font-size:13.5px;font-weight:850;letter-spacing:-.02em;transition:transform .4s cubic-bezier(.3,1.2,.5,1),opacity .3s}
.u203-nw b.is-in{transform:translateY(100%);opacity:0;transition:none}
.u203-nw b.is-out{transform:translateY(-100%);opacity:0}
.u203-sw{position:relative;width:22px;height:22px;padding:0;border:0;border-radius:50%;background:linear-gradient(145deg,var(--a),var(--b));box-shadow:inset 0 0 0 1px rgba(0,0,0,.12);cursor:pointer;transition:transform .25s cubic-bezier(.3,1.6,.5,1)}
.u203-sw::after{content:"";position:absolute;inset:-4px;border-radius:50%;box-shadow:0 0 0 1.5px #0071E3;opacity:0;transform:scale(.8);transition:opacity .2s,transform .3s cubic-bezier(.3,1.6,.5,1)}
.u203-sw[aria-checked="true"]::after{opacity:1;transform:none}
.u203-sw:hover,.u203-sw.g-hov{transform:scale(1.1)}
.u203-sw:focus-visible{outline:2px solid #1D1D1F;outline-offset:5px}
.u203-cd{position:absolute;inset:0;padding:10px 14px;border-radius:16px;background:#fff;box-shadow:0 14px 30px -14px rgba(29,29,31,.35),0 0 0 1px rgba(29,29,31,.06);opacity:0;transform:translateY(10px);transition:opacity .25s,transform .35s cubic-bezier(.3,1.3,.5,1);pointer-events:none;box-sizing:border-box}
.u203.is-act .u203-cd{opacity:1;transform:none}
.u203-cd b{display:block;font-size:12.5px;font-weight:850;color:#0071E3}
.u203-cd span{display:block;margin-top:3px;font-size:11px;font-weight:600;line-height:1.45;color:#424245;word-break:keep-all}
@media (prefers-reduced-motion: reduce){.u203-pin::after,.u203.is-a3 .u203-kn,.u203.is-a1 .u203-wv path,.u203.is-a2 .u203-cs{animation:none}.u203-sws,.u203-cd,.u203-nw b{transition:none}}
</style>
<div class="ux u203">
  <svg class="u203-sv" viewBox="0 0 340 262" role="img" aria-label="Headphone product view with annotation pins">
    <defs>
      <linearGradient class="g-cupl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" style="stop-color:var(--c1)"/><stop offset=".55" style="stop-color:var(--c1)"/><stop offset="1" style="stop-color:var(--c2)"/></linearGradient>
      <linearGradient class="g-cupr" x1="1" y1="0" x2="0" y2="0"><stop offset="0" style="stop-color:var(--c2)"/><stop offset=".45" style="stop-color:var(--c1)"/><stop offset="1" style="stop-color:var(--c2)"/></linearGradient>
      <linearGradient class="g-shade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset=".35" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".10"/></linearGradient>
      <linearGradient class="g-stv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EEF0F3"/><stop offset=".5" stop-color="#A3AAB3"/><stop offset="1" stop-color="#D3D7DC"/></linearGradient>
      <linearGradient class="g-sth" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9FA5AD"/><stop offset=".45" stop-color="#F6F7F9"/><stop offset="1" stop-color="#A9AFB7"/></linearGradient>
      <linearGradient class="g-cushl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".16"/><stop offset=".35" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".06"/></linearGradient>
      <linearGradient class="g-cushr" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".16"/><stop offset=".35" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".06"/></linearGradient>
      <pattern class="p-mesh" width="3.4" height="3.4" patternUnits="userSpaceOnUse"><rect width="3.4" height="3.4" style="fill:var(--cn)"/><path d="M0 3.4L3.4 0" stroke="rgba(0,0,0,.09)" stroke-width=".5"/></pattern>
      <pattern class="p-cush" width="2.6" height="2.6" patternUnits="userSpaceOnUse"><rect width="2.6" height="2.6" style="fill:var(--cu)"/><circle cx="1.3" cy="1.3" r=".45" fill="rgba(0,0,0,.14)"/></pattern>
      <clipPath class="c-kn"><rect x="263" y="127" width="10" height="10" rx="2.5"/></clipPath>
    </defs>
    <ellipse cx="170" cy="252" rx="102" ry="7" fill="rgba(29,29,31,.10)"/>
    
    <path d="M86 132 V118 C86 -10 254 -10 254 118 V132" fill="none" stroke="rgba(29,29,31,.18)" stroke-width="5.4" stroke-linecap="round"/>
    <path class="u203-fr" d="M86 132 V118 C86 -10 254 -10 254 118 V132" fill="none" stroke-width="4" stroke-linecap="round"/>
    <path d="M87.2 112 C88 0 252 0 252.8 112" fill="none" stroke="#fff" stroke-width=".9" opacity=".95"/>
    
    <g class="u203-part" data-i="0">
      <path class="u203-mb" d="M94 96 C98 40 242 40 246 96 C238 58 102 58 94 96 Z"/>
      <path d="M94 96 C98 40 242 40 246 96 C238 58 102 58 94 96 Z" fill="rgba(29,29,31,.05)" stroke="rgba(29,29,31,.16)" stroke-width=".9"/>
      <path d="M97 90 C102 46 238 46 243 90" fill="none" stroke="#fff" stroke-width=".8" opacity=".7"/>
    </g>
    <rect class="u203-sth" x="87" y="90" width="12" height="9" rx="3"/><rect class="u203-sth" x="241" y="90" width="12" height="9" rx="3"/>
    
    <rect class="u203-sth" x="83" y="104" width="6" height="18" rx="3"/><rect class="u203-sth" x="251" y="104" width="6" height="18" rx="3"/>
    
    <g class="u203-part" data-i="2">
      <rect class="u203-cs" x="98" y="146" width="20" height="90" rx="8"/><rect class="u203-csl" x="98" y="146" width="20" height="90" rx="8"/>
      <rect class="u203-cs" x="222" y="146" width="20" height="90" rx="8"/><rect class="u203-csr" x="222" y="146" width="20" height="90" rx="8"/>
    </g>
    
    <rect class="u203-cupl" x="68" y="134" width="36" height="114" rx="13"/><rect class="u203-shd" x="68" y="134" width="36" height="114" rx="13"/><rect x="68.5" y="134.5" width="35" height="113" rx="12.5" fill="none" stroke="rgba(29,29,31,.10)"/>
    <rect class="u203-cupr" x="236" y="134" width="36" height="114" rx="13"/><rect class="u203-shd" x="236" y="134" width="36" height="114" rx="13"/><rect x="236.5" y="134.5" width="35" height="113" rx="12.5" fill="none" stroke="rgba(29,29,31,.10)"/>
    <path d="M74 150 V232" stroke="#fff" stroke-width="1.8" stroke-linecap="round" opacity=".45"/><path d="M266 150 V232" stroke="#fff" stroke-width="1.8" stroke-linecap="round" opacity=".3"/>
    
    <rect class="u203-sth" x="78" y="126" width="16" height="11" rx="5.5"/><rect class="u203-sth" x="246" y="126" width="16" height="11" rx="5.5"/>
    
    <rect class="u203-stv2" x="237" y="131" width="7" height="4" rx="2"/>
    <g class="u203-part" data-i="3"><rect class="u203-sth" x="263" y="127" width="10" height="10" rx="2.5"/><g class="c-kng"><g class="u203-kn"><path d="M262 128v8M264.5 128v8M267 128v8M269.5 128v8M272 128v8M274.5 128v8" stroke="rgba(29,29,31,.3)" stroke-width=".7"/></g></g></g>
    
    <g class="u203-part" data-i="1"><rect x="70" y="158" width="2.4" height="16" rx="1.2" fill="rgba(29,29,31,.4)"/></g>
    <g class="u203-wv"><path d="M60 157 Q54 166 60 175"/><path d="M53 153 Q45 166 53 179"/><path d="M46 149 Q36 166 46 183"/></g>
    <path class="u203-ln" d=""/><circle class="u203-dot" r="3" cx="-10" cy="-10"/>
  </svg>
  <div class="u203-ft">
    <div class="u203-sws"><div class="u203-cl"><small>Color</small><span class="u203-nw"></span></div><div class="u203-swr" role="radiogroup" aria-label="Choose a color" style="display:flex;gap:10px"></div></div>
    <div class="u203-cd" aria-live="polite"><b></b><span></span></div>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var sv = root.querySelector('.u203-sv'), ln = sv.querySelector('.u203-ln'), dot = sv.querySelector('.u203-dot'), cd = root.querySelector('.u203-cd'), nw = root.querySelector('.u203-nw'), swr = root.querySelector('.u203-swr');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var INFO = [['Knit-mesh canopy', 'Spreads the weight on your head for all-day comfort'], ['Noise cancelling', 'Outer mics hear the noise around you and erase it'], ['Mesh ear cushions', 'Memory foam presses to the shape of your ears'], ['Crown dial', 'Turn for volume, press to play or pause']];
  var COL = [['Space Gray', '#8E9196', '#5B5E63', '#6E7176', '#4A4D52'], ['Silver', '#F1F2F4', '#C6CAD0', '#F4F5F6', '#D5D8DD'], ['Sky Blue', '#CFE0EA', '#97B5C7', '#DFEAF0', '#B3CAD7'], ['Green', '#DCE7CF', '#A9BE94', '#E6EEDC', '#C0D1AE'], ['Pink', '#F4D8D1', '#D9A497', '#F8E6E1', '#E6C0B6']];
  var uid = 'u203' + Math.random().toString(36).slice(2, 7);
  function ref(sel, kind, attrs) { var el = sv.querySelector(sel); el.id = uid + kind; attrs.forEach(function (a) { Array.prototype.forEach.call(sv.querySelectorAll(a[0]), function (t) { t.setAttribute(a[1], 'url(#' + uid + kind + ')'); }); }); }
  ref('.g-cupl', 'cl', [['.u203-cupl', 'fill']]);
  ref('.g-cupr', 'cr', [['.u203-cupr', 'fill']]);
  ref('.g-shade', 'sd', [['.u203-shd', 'fill']]);
  ref('.g-stv', 'stv', [['.u203-fr', 'stroke'], ['.u203-stv2', 'fill']]);
  ref('.g-sth', 'sth', [['.u203-sth', 'fill']]);
  ref('.g-cushl', 'ql', [['.u203-csl', 'fill']]);
  ref('.g-cushr', 'qr', [['.u203-csr', 'fill']]);
  ref('.p-mesh', 'mesh', [['.u203-mb', 'fill']]);
  ref('.p-cush', 'cush', [['.u203-cs', 'fill']]);
  ref('.c-kn', 'kn', [['.c-kng', 'clip-path']]);
  var PIN = [[170, 60], [71, 166], [111, 191], [268, 132]], cur = -1, P = [], hideT = 0;
  var parts = sv.querySelectorAll('.u203-part');
  PIN.forEach(function (p, i) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'u203-pin'; b.style.left = p[0] + 'px'; b.style.top = p[1] + 'px'; b.setAttribute('aria-label', INFO[i][0] + ', show note');
    b.addEventListener('pointerenter', function () { show(i); });
    b.addEventListener('pointerleave', function () { clearTimeout(hideT); hideT = setTimeout(function () { show(-1); }, 160); });
    b.addEventListener('focus', function () { show(i); });
    b.addEventListener('blur', function () { show(-1); });
    b.addEventListener('click', function () { show(i); });
    root.appendChild(b); P.push(b);
  });
  function show(i) {
    clearTimeout(hideT);
    if (i === cur) return;
    cur = i; root.classList.toggle('is-act', i >= 0);
    [0, 1, 2, 3].forEach(function (k) { root.classList.toggle('is-a' + k, k === i); });
    P.forEach(function (b, j) { b.classList.toggle('is-on', j === i); });
    Array.prototype.forEach.call(parts, function (g) { g.classList.toggle('is-on', +g.dataset.i === i); });
    if (i < 0) { ln.setAttribute('d', ''); dot.setAttribute('cx', -10); return; }
    cd.querySelector('b').textContent = INFO[i][0]; cd.querySelector('span').textContent = INFO[i][1];
    var p = PIN[i], ey = 266, d = 'M' + p[0] + ' ' + (p[1] + 10) + ' L' + p[0] + ' ' + ey;
    ln.setAttribute('d', d); dot.setAttribute('cx', p[0]); dot.setAttribute('cy', ey);
    if (!rm && ln.animate) { var L = ln.getTotalLength(); ln.style.strokeDasharray = L + ' ' + L; ln.animate([{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: 360, easing: 'cubic-bezier(.3,.8,.3,1)' }).onfinish = function () { ln.style.strokeDasharray = ''; }; }
  }
  var sel = -1, S = COL.map(function (c, i) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'u203-sw'; b.setAttribute('role', 'radio'); b.setAttribute('aria-label', c[0] + ' color'); b.style.setProperty('--a', c[1]); b.style.setProperty('--b', c[2]);
    b.addEventListener('click', function () { pick(i); });
    swr.appendChild(b); return b;
  });
  function pick(i, first) {
    if (i === sel) return; sel = i; show(-1);
    var c = COL[i]; root.style.setProperty('--c1', c[1]); root.style.setProperty('--c2', c[2]); root.style.setProperty('--cn', c[3]); root.style.setProperty('--cu', c[4]);
    S.forEach(function (b, k) { b.setAttribute('aria-checked', k === i); b.tabIndex = k === i ? 0 : -1; });
    var olds = Array.prototype.slice.call(nw.children), t = document.createElement('b'); t.textContent = c[0];
    if (first || rm) { nw.innerHTML = ''; nw.appendChild(t); return; }
    t.className = 'is-in'; nw.appendChild(t); void t.offsetWidth; t.className = '';
    olds.forEach(function (o) { o.className = 'is-out'; setTimeout(function () { o.remove(); }, 420); });
  }
  swr.addEventListener('keydown', function (e) { var d = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key]; if (d) { e.preventDefault(); var n = (sel + d + COL.length) % COL.length; pick(n); S[n].focus(); } });
  root.addEventListener('pointerleave', function () { show(-1); });
  pick(2, true);
})();
</script>
--- Code end ---

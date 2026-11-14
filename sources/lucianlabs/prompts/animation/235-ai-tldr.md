---
source: "lucianlabs"
id: "235"
title: "AI TL;DR that folds long text"
category: "App Screens"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#235"
tags: ["ai", "summary", "tldr", "highlight", "productivity"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] AI TL;DR that folds long text (235, App Screens)
[What it does] Press Summarize above a long meeting note and a glowing line sweeps down the text, highlighting the key sentences one by one. Once it's read through, the body folds away and a three-line summary card unfolds in its place, its items writing out line by line as the reading time changes from 4 minutes to 20 seconds. Press Show original to unfold the text again, highlights included.
[How to use it] Press Summarize, then switch to Show original

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
<!-- Lucian UX/UI Prompt #235 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#235 -->
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
.u235{position:relative;width:340px;height:340px;border-radius:30px;overflow:hidden;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);color:var(--ux-ink)}
.u235-hd{position:absolute;left:18px;right:16px;top:18px;display:flex;align-items:flex-start;gap:8px}
.u235-hd div{flex:1;min-width:0}
.u235-hd b{display:block;font-size:15px;font-weight:900;letter-spacing:-.02em}
.u235-hd small{display:flex;gap:6px;margin-top:2px;font-size:10px;font-weight:700;color:var(--ux-ink-3)}
.u235-rt{padding:0 6px;border-radius:5px;background:var(--ux-surface-2);font-variant-numeric:tabular-nums;transition:background .3s,color .3s}
.u235.is-sum .u235-rt{background:color-mix(in srgb,#10B981 15%,transparent);color:#047857}
.u235-go{display:inline-flex;align-items:center;gap:5px;height:30px;padding:0 12px;border:0;border-radius:999px;background:linear-gradient(135deg,#8B5CF6,#EC4899);color:#fff;font:inherit;font-size:11.5px;font-weight:850;cursor:pointer;transition:opacity .2s}
.u235-go:disabled{opacity:.45}
.u235-go svg{width:12px;height:12px}
.u235-tg{height:30px;padding:0 11px;border:0;border-radius:999px;background:var(--ux-surface-2);box-shadow:inset 0 0 0 1px var(--ux-line);color:var(--ux-ink-2);font:inherit;font-size:11px;font-weight:800;cursor:pointer;display:none}
.u235.is-done .u235-go{display:none}
.u235.is-done .u235-tg{display:inline-block}
.u235-bx{position:absolute;left:14px;right:14px;top:66px;bottom:14px}
.u235-tx{position:absolute;inset:0;overflow:hidden;padding:4px 4px 0;font-size:11.5px;line-height:1.65;font-weight:600;color:var(--ux-ink-2);transition:clip-path .55s cubic-bezier(.6,0,.3,1),opacity .3s;clip-path:inset(0 0 0 0 round 14px)}
.u235.is-sum .u235-tx{clip-path:inset(0 0 100% 0 round 14px);opacity:0;pointer-events:none}
.u235-tx span{transition:background-size .5s ease,color .3s;background:linear-gradient(transparent 52%,color-mix(in srgb,#FACC15 55%,transparent) 52%) no-repeat 0 0/0 100%}
.u235-tx span.is-hl{background-size:100% 100%;color:var(--ux-ink)}
.u235-sw{position:absolute;left:0;right:0;top:0;height:46px;margin-top:-46px;background:linear-gradient(transparent,color-mix(in srgb,#A855F7 22%,transparent));border-bottom:2px solid #A855F7;box-shadow:0 6px 14px -4px #A855F7;opacity:0;pointer-events:none}
.u235-sm{position:absolute;left:0;right:0;top:0;padding:14px 14px 6px;border-radius:16px;background:linear-gradient(var(--ux-surface),var(--ux-surface)) padding-box,linear-gradient(135deg,#8B5CF6,#EC4899) border-box;border:1.5px solid transparent;opacity:0;transform:translateY(-10px) scale(.97);transition:opacity .35s,transform .45s cubic-bezier(.3,1.3,.5,1);pointer-events:none}
.u235.is-sum .u235-sm{opacity:1;transform:none;pointer-events:auto;transition-delay:.35s}
.u235-sm small{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:850;color:#A855F7}
.u235-sm small svg{width:12px;height:12px}
.u235-sm ol{margin:10px 0 0;padding:0;list-style:none;counter-reset:n}
.u235-sm li{position:relative;padding:8px 0 8px 26px;border-bottom:1px solid var(--ux-line);font-size:12px;line-height:1.45;font-weight:750;color:var(--ux-ink);min-height:18px}
.u235-sm li:last-child{border-bottom:0}
.u235-sm li::before{counter-increment:n;content:counter(n);position:absolute;left:0;top:8px;width:18px;height:18px;border-radius:6px;background:color-mix(in srgb,#A855F7 14%,transparent);color:#9333EA;font-size:10px;font-weight:900;text-align:center;line-height:18px}
.u235-cu::after{content:"";display:inline-block;width:2px;height:12px;margin-left:1px;vertical-align:-2px;background:#A855F7;animation:u235-bl .8s steps(1) infinite}
@keyframes u235-bl{50%{opacity:0}}
.u235 button:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
@media (prefers-reduced-motion: reduce){.u235-tx,.u235-sm,.u235-tx span{transition:none}.u235-cu::after{animation:none}}
</style>
<div class="ux u235">
  <div class="u235-hd"><div><b>Weekly product meeting</b><small>Oct 14 · 6 attendees<span class="u235-rt"></span></small></div><button type="button" class="u235-go"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M6 1l1.2 3.3L10.5 5.5 7.2 6.7 6 10 4.8 6.7 1.5 5.5l3.3-1.2z" fill="currentColor"/></svg>Summarize</button><button type="button" class="u235-tg"></button></div>
  <div class="u235-bx"><div class="u235-tx"><div class="u235-sw" aria-hidden="true"></div></div><div class="u235-sm" aria-live="polite"><small><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M6 1l1.2 3.3L10.5 5.5 7.2 6.7 6 10 4.8 6.7 1.5 5.5l3.3-1.2z" fill="currentColor"/></svg><span class="u235-sl"></span></small><ol></ol></div></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var go = root.querySelector('.u235-go'), tg = root.querySelector('.u235-tg'), tx = root.querySelector('.u235-tx'), sw = root.querySelector('.u235-sw'), ol = root.querySelector('.u235-sm ol'), rt = root.querySelector('.u235-rt'), sl = root.querySelector('.u235-sl');
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var P = [['Last week we had 1,284 sign-ups, up 18% from the week before.', 1], ['Ad spend stayed flat, and most of the new sign-ups came from the new landing page.', 0], ['However, drop-off at checkout was high at 42%.', 1], ['The card field getting cut off on mobile looks like the cause.', 0], ['Design will cut checkout down to a single step this week.', 1], ['Engineering ships the fix by Friday and shares results at the next meeting.', 0], ['The next meeting is Oct 21 at 10 AM.', 0]];
  var S = ['1,284 sign-ups, up 18% (new landing page)', '42% checkout drop-off · mobile card field cut off', 'Checkout down to one step this week, ship Friday'];
  sl.textContent = '3 key points'; rt.textContent = '4 min read';
  var SP = P.map(function (p) { var s = document.createElement('span'); s.textContent = p[0] + ' '; tx.appendChild(s); return s; });
  var gen = 0;
  function later(g, ms, fn) { setTimeout(function () { if (g === gen && root.isConnected) fn(); }, rm ? 0 : ms); }
  function write(g) {
    ol.innerHTML = '';
    var L = S.map(function () { var li = document.createElement('li'); ol.appendChild(li); return li; }), i = 0, k = 0;
    if (rm) { L.forEach(function (li, n) { li.textContent = S[n]; }); return; }
    (function step() {
      if (g !== gen) return;
      if (i >= S.length) { L.forEach(function (li) { li.classList.remove('u235-cu'); }); return; }
      L.forEach(function (li, n) { li.classList.toggle('u235-cu', n === i); });
      k++; L[i].textContent = S[i].slice(0, k);
      if (k >= S[i].length) { i++; k = 0; setTimeout(step, 160); } else setTimeout(step, 22);
    })();
  }
  go.addEventListener('click', function () {
    var g = ++gen; go.disabled = true;
    var H = tx.offsetHeight, ms = 1700, t0 = performance.now();
    if (!rm) {
      sw.style.opacity = 1;
      (function f(now) { if (g !== gen) return; var q = Math.min(1, (now - t0) / ms); sw.style.transform = 'translateY(' + (q * (H + 46)).toFixed(1) + 'px)'; SP.forEach(function (s, i) { if (P[i][1] && s.offsetTop + 8 < q * H) s.classList.add('is-hl'); }); if (q < 1) requestAnimationFrame(f); else sw.style.opacity = 0; })(t0);
    } else SP.forEach(function (s, i) { if (P[i][1]) s.classList.add('is-hl'); });
    later(g, ms + 250, function () { root.classList.add('is-sum', 'is-done'); rt.textContent = '20 sec read'; tg.textContent = 'Show original'; go.disabled = false; });
    later(g, ms + 650, function () { write(g); });
  });
  tg.addEventListener('click', function () { var sum = !root.classList.contains('is-sum'); root.classList.toggle('is-sum', sum); tg.textContent = sum ? 'Show original' : 'Show summary'; rt.textContent = sum ? '20 sec read' : '4 min read'; });
})();
</script>
--- Code end ---

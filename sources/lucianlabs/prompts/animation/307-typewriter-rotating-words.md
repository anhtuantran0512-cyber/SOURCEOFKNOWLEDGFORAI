---
source: "lucianlabs"
id: "307"
title: "Typewriter rotating keyword"
category: "Text Motion"
collection: "animation"
url: "https://lucianlabs.dev/en/uxui-prompt/#307"
tags: ["text", "typewriter", "rotate", "hero", "caret"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Typewriter rotating keyword (307, Text Motion)
[What it does] Only the key word at the end of the sentence is deleted and retyped like a typewriter. Korean is typed jamo by jamo the way an IME composes it, and the underline color changes with each word. The caret blinks while idle and holds still while typing.
[How to use it] Press a chip below to rewrite the word right away. Hover the sentence to pause the rotation

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
<!-- Lucian UX/UI Prompt #307 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#307 -->
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
.u307{position:relative;width:340px;height:272px;display:flex;flex-direction:column;padding:24px 22px 18px;border-radius:28px;background:var(--ux-surface);box-shadow:0 0 0 1px var(--ux-line),0 30px 60px -36px var(--ux-shadow-strong);overflow:hidden;--c:var(--ux-accent)}
.u307::after{content:"";position:absolute;right:-60px;top:-70px;width:200px;height:200px;border-radius:50%;background:radial-gradient(circle,color-mix(in srgb,var(--c) 26%,transparent),transparent 70%);transition:background .6s var(--ux-ease);pointer-events:none}
.u307-k{position:relative;margin:0;font:600 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.14em;color:var(--ux-ink-3)}
.u307-line{position:relative;margin:16px 0 0;min-height:100px;font-size:31px;line-height:1.24;font-weight:820;letter-spacing:-.045em}
.u307-a{display:block;color:var(--ux-ink-2)}
.u307-b{display:inline;white-space:nowrap}
.u307-w{position:relative;color:var(--ux-ink);background:linear-gradient(var(--c),var(--c)) 0 100%/100% .14em no-repeat;padding-bottom:.04em;transition:background-size .3s var(--ux-ease)}
.u307-w:empty{padding:0}
.u307-caret{display:inline-block;width:3px;height:.95em;margin:0 2px 0 3px;vertical-align:-.1em;border-radius:2px;background:var(--c);animation:u307-blink 1s steps(1) infinite;transition:background-color .4s}
.u307.is-typing .u307-caret{animation:none}
@keyframes u307-blink{50%{opacity:0}}
.u307-tail{color:var(--ux-ink)}
.u307-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.u307-chips{position:relative;margin-top:auto;display:flex;flex-wrap:wrap;gap:6px}
.u307-chip{height:34px;padding:0 13px;border:0;border-radius:999px;background:var(--ux-surface-2);font-size:13px;font-weight:700;color:var(--ux-ink-2);box-shadow:inset 0 0 0 1px var(--ux-line);transition:background-color .3s,color .3s,box-shadow .3s,transform .35s var(--ux-spring)}
.u307-chip:hover{color:var(--ux-ink)}
.u307-chip:active{transform:scale(.93)}
.u307-chip[aria-pressed="true"]{background:var(--k);color:#fff;box-shadow:none}
</style>
<div class="ux u307">
  <p class="u307-k">LUCIANLABS · STUDIO</p>
  <p class="u307-line"><span class="u307-a">What we build together is</span> <span class="u307-sr"></span><span class="u307-b"><span class="u307-w" aria-hidden="true"></span><span class="u307-caret" aria-hidden="true"></span><span class="u307-tail">.</span></span></p>
  <div class="u307-chips" role="group" aria-label="Change the word">
    <button class="u307-chip" type="button" aria-pressed="true" style="--k:var(--ux-accent)">products</button>
    <button class="u307-chip" type="button" aria-pressed="false" style="--k:var(--ux-mint)">experiences</button>
    <button class="u307-chip" type="button" aria-pressed="false" style="--k:var(--ux-warn)">brands</button>
    <button class="u307-chip" type="button" aria-pressed="false" style="--k:var(--ux-accent-2)">tomorrow</button>
  </div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var line = root.querySelector('.u307-line'), wEl = root.querySelector('.u307-w'), sr = root.querySelector('.u307-sr');
  var chips = Array.prototype.slice.call(root.querySelectorAll('.u307-chip'));
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var WORDS = ['products', 'experiences', 'brands', 'tomorrow'];
  var COLORS = ['var(--ux-accent)', 'var(--ux-mint)', 'var(--ux-warn)', 'var(--ux-accent-2)'];
  var CHO = [0x3131, 0x3132, 0x3134, 0x3137, 0x3138, 0x3139, 0x3141, 0x3142, 0x3143, 0x3145, 0x3146, 0x3147, 0x3148, 0x3149, 0x314A, 0x314B, 0x314C, 0x314D, 0x314E];
  var cur = 0, timer = 0, hold = false, busy = false;
  function frames(word) {
    var out = [], pre = '';
    Array.from(word).forEach(function (ch) {
      var c = ch.charCodeAt(0) - 0xAC00;
      if (c >= 0 && c < 11172) {
        var jong = c % 28, base = ch.charCodeAt(0) - jong;
        out.push(pre + String.fromCharCode(CHO[Math.floor(c / 588)]));
        out.push(pre + String.fromCharCode(base));
        if (jong) out.push(pre + ch);
      } else out.push(pre + ch);
      pre += ch;
    });
    return out;
  }
  function wait(ms, fn) { clearTimeout(timer); timer = setTimeout(function () { if (root.isConnected) fn(); }, ms); }
  function go(i, manual) {
    if (busy && !manual) return;
    busy = true;
    cur = i;
    chips.forEach(function (c, k) { c.setAttribute('aria-pressed', String(k === i)); });
    var target = WORDS[i], seq = frames(target);
    root.classList.add('is-typing');
    if (rm) { wEl.textContent = target; done(); return; }
    (function del() {
      var s = wEl.textContent;
      if (s.length) { wEl.textContent = s.slice(0, -1); wait(55, del); return; }
      root.style.setProperty('--c', COLORS[i]);
      var k = 0;
      wait(220, function type() {
        wEl.textContent = seq[k++];
        if (k < seq.length) wait(70 + Math.random() * 70, type); else done();
      });
    })();
  }
  function done() {
    root.classList.remove('is-typing');
    root.style.setProperty('--c', COLORS[cur]);
    sr.textContent = WORDS[cur];
    busy = false;
    next();
  }
  function next() { wait(2300, function () { if (hold) { next(); return; } go((cur + 1) % WORDS.length); }); }
  chips.forEach(function (c, i) { c.addEventListener('click', function () { if (i !== cur || busy) go(i, true); }); });
  line.addEventListener('pointerenter', function () { hold = true; });
  line.addEventListener('pointerleave', function () { hold = false; });
  wEl.textContent = '';
  go(0, true);
})();
</script>
--- Code end ---

---
source: "lucianlabs"
id: "029"
title: "Colored tag input"
category: "Inputs & Search"
collection: "interface"
url: "https://lucianlabs.dev/en/uxui-prompt/#029"
tags: ["tags", "chips", "input", "keyboard", "suggestions"]
license: "MIT (c) 2026 Seokwoooo"
---

[Element] Colored tag input (029, Inputs & Search)
[What it does] Press Enter and the text pops out as a colored tag; press a suggestion chip and it jumps into the field. In an empty field, Backspace once highlights the last tag for removal and a second press removes it.
[How to use it] Type a word in the field and press Enter. Try the suggestion chips below too

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
<!-- Lucian UX/UI Prompt #029 · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#029 -->
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
.u029{position:relative;width:350px}
.u029-head{display:flex;align-items:baseline;justify-content:space-between;margin:0 4px 10px}
.u029-head b{font-size:16px;font-weight:720;letter-spacing:-.02em}
.u029-n{font-size:13px;font-weight:700;color:var(--ux-ink-3);font-variant-numeric:tabular-nums;transition:color .3s}
.u029-n.full{color:var(--ux-warn)}
.u029-field{display:flex;flex-wrap:wrap;align-content:flex-start;gap:7px;height:142px;padding:12px;border-radius:20px;background:var(--ux-surface);box-shadow:0 0 0 1.5px var(--ux-line-2);cursor:text;transition:box-shadow .3s var(--ux-ease)}
.u029-field:focus-within{box-shadow:0 0 0 2px var(--ux-accent),0 0 0 6px var(--ux-accent-soft)}
.u029-field.shake{animation:u029-shake .42s var(--ux-ease)}
@keyframes u029-shake{20%{transform:translateX(-6px)}40%{transform:translateX(5px)}60%{transform:translateX(-3px)}}
.u029-tag{display:inline-flex;align-items:center;gap:4px;height:34px;padding:0 6px 0 12px;border-radius:11px;background:color-mix(in srgb,var(--c) 16%,transparent);color:color-mix(in srgb,var(--c) 72%,var(--ux-ink));font-size:14px;font-weight:700;
  animation:u029-pop .45s var(--ux-spring);transition:transform .3s var(--ux-ease),opacity .3s var(--ux-ease),box-shadow .2s}
@keyframes u029-pop{from{transform:scale(.4);opacity:0}}
.u029-tag.out{transform:scale(.4);opacity:0}
.u029-tag.armed{box-shadow:0 0 0 2px var(--c);animation:u029-arm .3s var(--ux-ease)}
@keyframes u029-arm{50%{transform:scale(1.08)}}
.u029-x{width:22px;height:22px;border:0;padding:0;border-radius:7px;background:none;color:inherit;display:grid;place-items:center;opacity:.7}
.u029-x:hover{opacity:1;background:color-mix(in srgb,currentColor 15%,transparent)}
.u029-x:focus-visible{outline:2px solid currentColor;outline-offset:1px}
.u029-x svg{width:10px;height:10px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round}
.u029-in{flex:1;min-width:90px;height:34px;border:0;outline:0;background:none;font-size:14.5px;color:var(--ux-ink)}
.u029-in::placeholder{color:var(--ux-ink-3)}
.u029-msg{height:18px;margin:8px 4px 10px;font-size:12.5px;color:var(--ux-ink-3);transition:color .3s}
.u029-msg.warn{color:var(--ux-danger)}
.u029-sg-row{display:flex;flex-wrap:wrap;gap:6px}
.u029-sg{display:inline-flex;align-items:center;gap:5px;height:32px;padding:0 12px 0 9px;border:0;border-radius:999px;background:none;box-shadow:inset 0 0 0 1px var(--ux-line-2);font-size:13px;font-weight:620;color:var(--ux-ink-2);transition:transform .35s var(--ux-spring),opacity .3s,box-shadow .2s}
.u029-sg:hover{box-shadow:inset 0 0 0 1px var(--ux-ink-3);color:var(--ux-ink)}
.u029-sg:active{transform:scale(.92)}
.u029-sg:focus-visible{outline:2px solid var(--ux-accent);outline-offset:2px}
.u029-sg svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round}
.u029-sg.used{opacity:.3;pointer-events:none}
.u029-in:focus-visible{outline:none}
</style>
<div class="ux u029">
  <div class="u029-head"><b>Project tags</b><span class="u029-n">3 / 6</span></div>
  <div class="u029-field">
    <input class="u029-in" type="text" placeholder="Type a tag, press Enter" aria-label="Add tag" autocomplete="off">
  </div>
  <p class="u029-msg" aria-live="polite"></p>
  <div class="u029-sg-row" role="group" aria-label="Suggested tags"></div>
</div>

<script>
(function () {
  var root = document.currentScript.previousElementSibling;
  var field = root.querySelector('.u029-field');
  var input = root.querySelector('.u029-in');
  var count = root.querySelector('.u029-n');
  var msg = root.querySelector('.u029-msg');
  var sgRow = root.querySelector('.u029-sg-row');
  var MAX = 6, t = 0;
  var PALETTE = ['#7B61FF', '#E0457B', '#0E9F8E', '#D6731E', '#2F7FE0', '#B04FD0'];
  function colorOf(s) { var h = 0; for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0; return PALETTE[h % PALETTE.length]; }
  function tags() { return Array.prototype.slice.call(field.querySelectorAll('.u029-tag:not(.out)')); }
  function say(text, warn) {
    msg.textContent = text;
    msg.classList.toggle('warn', !!warn);
    clearTimeout(t);
    t = setTimeout(function () { if (root.isConnected) { msg.textContent = ''; msg.classList.remove('warn'); } }, 1800);
  }
  function refresh() {
    var n = tags().length;
    count.textContent = n + ' / ' + MAX;
    count.classList.toggle('full', n >= MAX);
    var have = tags().map(function (x) { return x.dataset.v; });
    Array.prototype.forEach.call(sgRow.children, function (b) { b.classList.toggle('used', have.indexOf(b.dataset.v) >= 0); });
  }
  function make(v) {
    var tag = document.createElement('span');
    tag.className = 'u029-tag';
    tag.dataset.v = v;
    tag.style.setProperty('--c', colorOf(v));
    var s = document.createElement('span');
    s.textContent = '#' + v;
    var x = document.createElement('button');
    x.type = 'button';
    x.className = 'u029-x';
    x.setAttribute('aria-label', 'Remove tag ' + v);
    x.innerHTML = '<svg viewBox="0 0 10 10" aria-hidden="true"><path d="M2 2l6 6M8 2L2 8"/></svg>';
    x.addEventListener('click', function () { remove(tag); input.focus(); });
    tag.appendChild(s); tag.appendChild(x);
    return tag;
  }
  function add(raw) {
    var v = raw.trim().replace(/^#/, '');
    if (!v) return false;
    if (tags().length >= MAX) {
      say('You can add up to six tags', true);
      field.classList.remove('shake'); void field.offsetWidth; field.classList.add('shake');
      return false;
    }
    if (tags().some(function (x) { return x.dataset.v === v; })) { say('That tag already exists', true); return false; }
    disarm();
    field.insertBefore(make(v), input);
    refresh();
    say('Added #' + v);
    return true;
  }
  function remove(tag) {
    if (tag.classList.contains('out')) return;
    tag.classList.add('out');
    say('Removed #' + tag.dataset.v);
    setTimeout(function () { if (root.isConnected) { tag.remove(); refresh(); } }, 280);
  }
  function disarm() { tags().forEach(function (x) { x.classList.remove('armed'); }); }
  input.addEventListener('keydown', function (e) {
    if (e.isComposing || e.keyCode === 229) return;
    if (e.key === 'Enter' || e.key === ',') { e.preventDefault(); if (add(input.value)) input.value = ''; }
    else if (e.key === 'Backspace' && !input.value) {
      var all = tags(), last = all[all.length - 1];
      if (!last) return;
      if (last.classList.contains('armed')) remove(last); else { disarm(); last.classList.add('armed'); }
    } else disarm();
  });
  input.addEventListener('blur', disarm);
  field.addEventListener('click', function (e) { if (e.target === field) input.focus(); });
  ['designsystem', 'motion', 'darkmode'].forEach(function (v) { field.insertBefore(make(v), input); });
  ['a11y', 'onboarding', 'microinteraction', 'dashboard'].forEach(function (v) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'u029-sg';
    b.dataset.v = v;
    b.innerHTML = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M6 2v8M2 6h8"/></svg>';
    b.appendChild(document.createTextNode(v));
    b.setAttribute('aria-label', 'Add tag ' + v);
    b.addEventListener('click', function () { add(v); });
    sgRow.appendChild(b);
  });
  refresh();
})();
</script>
--- Code end ---

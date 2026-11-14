---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/team-members-roles/"
title: "Team Members Page with Roles"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A team management page that scales from 5 to 500 people: seat usage at a glance, instant search across names and emails, a role filter, colour-coded role…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Team Members Page with Roles
Source: https://codefronts.com/layouts/css-settings-pages/team-members-roles/

A team management page that scales from 5 to 500 people: seat usage at a glance, instant search across names and emails, a role filter, colour-coded role selects per member (Owner is locked), pending-invite rows with resend, and a remove action that collapses the row smoothly with an undo toast. The list reflows to a compact stacked layout via container queries.
## HTML
```html
<section class="csp-06">
  <div class="csp-06__wrap">
    <header class="csp-06__head">
      <div><h1>Members</h1><p>Manage who has access to the Northwind workspace.</p></div>
      <a class="csp-06__btn" href="#">Invite people</a>
    </header>

    <div class="csp-06__seats">
      <div class="csp-06__seatbar"><i style="width:80%"></i></div>
      <p><b>8 of 10</b> seats used · 2 available on your Pro plan</p>
    </div>

    <div class="csp-06__tools">
      <label class="csp-06__search"><span class="csp-06__sr">Search members</span><input type="search" placeholder="Search by name or email" data-q></label>
      <label><span class="csp-06__sr">Filter by role</span><select data-rf><option value="">All roles</option><option value="owner">Owner</option><option value="admin">Admin</option><option value="member">Member</option><option value="viewer">Viewer</option></select></label>
    </div>
    <p class="csp-06__count" data-count aria-live="polite"></p>

    <ul class="csp-06__list" data-list>
      <li class="csp-06__row" data-name="Ava Mitchell" data-email="[email protected]" data-role="owner"><div class="csp-06__inner">
        <span class="csp-06__av" style="--h:265">AM</span><span class="csp-06__who"><b>Ava Mitchell <em>You</em></b><small>[email protected]</small></span><span class="csp-06__seen">Active now</span>
        <select class="csp-06__role" disabled aria-label="Role for Ava Mitchell" title="Transfer ownership from the Danger zone"><option value="owner">Owner</option></select><span class="csp-06__more"></span></div></li>
      <li class="csp-06__row" data-name="Jordan Lee" data-email="[email protected]" data-role="admin"><div class="csp-06__inner">
        <span class="csp-06__av" style="--h:200">JL</span><span class="csp-06__who"><b>Jordan Lee</b><small>[email protected]</small></span><span class="csp-06__seen">2 hours ago</span>
        <select class="csp-06__role" aria-label="Role for Jordan Lee"><option value="admin" selected>Admin</option><option value="member">Member</option><option value="viewer">Viewer</option></select><button class="csp-06__rm" type="button" aria-label="Remove Jordan Lee">Remove</button></div></li>
      <li class="csp-06__row" data-name="Priya Raman" data-email="[email protected]" data-role="member"><div class="csp-06__inner">
        <span class="csp-06__av" style="--h:330">PR</span><span class="csp-06__who"><b>Priya Raman</b><small>[email protected]</small></span><span class="csp-06__seen">Yesterday</span>
        <select class="csp-06__role" aria-label="Role for Priya Raman"><option value="admin">Admin</option><option value="member" selected>Member</option><option value="viewer">Viewer</option></select><button class="csp-06__rm" type="button" aria-label="Remove Priya Raman">Remove</button></div></li>
      <li class="csp-06__row" data-name="Liam O'Connor" data-email="[email protected]" data-role="member"><div class="csp-06__inner">
        <span class="csp-06__av" style="--h:150">LO</span><span class="csp-06__who"><b>Liam O'Connor</b><small>[email protected]</small></span><span class="csp-06__seen">3 days ago</span>
        <select class="csp-06__role" aria-label="Role for Liam O'Connor"><option value="admin">Admin</option><option value="member" selected>Member</option><option value="viewer">Viewer</option></select><button class="csp-06__rm" type="button" aria-label="Remove Liam O'Connor">Remove</button></div></li>
      <li class="csp-06__row" data-name="Sofia Rossi" data-email="[email protected]" data-role="member"><div class="csp-06__inner">
        <span class="csp-06__av" style="--h:40">SR</span><span class="csp-06__who"><b>Sofia Rossi</b><small>[email protected]</small></span><span class="csp-06__seen">Last week</span>
        <select class="csp-06__role" aria-label="Role for Sofia Rossi"><option value="admin">Admin</option><option value="member" selected>Member</option><option value="viewer">Viewer</option></select><button class="csp-06__rm" type="button" aria-label="Remove Sofia Rossi">Remove</button></div></li>
      <li class="csp-06__row" data-name="Noah Williams" data-email="[email protected]" data-role="viewer"><div class="csp-06__inner">
        <span class="csp-06__av" style="--h:90">NW</span><span class="csp-06__who"><b>Noah Williams <em class="csp-06__guest">Guest</em></b><small>[email protected]</small></span><span class="csp-06__seen">2 weeks ago</span>
        <select class="csp-06__role" aria-label="Role for Noah Williams"><option value="admin">Admin</option><option value="member">Member</option><option value="viewer" selected>Viewer</option></select><button class="csp-06__rm" type="button" aria-label="Remove Noah Williams">Remove</button></div></li>
      <li class="csp-06__row is-pending" data-name="Emma Clarke" data-email="[email protected]" data-role="member"><div class="csp-06__inner">
        <span class="csp-06__av csp-06__av--pending">EC</span><span class="csp-06__who"><b>[email protected]</b><small>Invited 2 days ago · <button type="button" class="csp-06__link" data-resend>Resend invite</button></small></span><span class="csp-06__seen"><span class="csp-06__pend">Pending</span></span>
        <select class="csp-06__role" aria-label="Role for [email protected]"><option value="admin">Admin</option><option value="member" selected>Member</option><option value="viewer">Viewer</option></select><button class="csp-06__rm" type="button" aria-label="Revoke invite for [email protected]">Revoke</button></div></li>
    </ul>
    <p class="csp-06__empty" hidden data-empty>No members match your search.</p>
  </div>
  <div class="csp-06__toast" role="status" data-toast><span data-tmsg></span><button type="button" data-undo>Undo</button></div>
</section>
```
## CSS
```css
.csp-06,
.csp-06 *,
.csp-06 *::before,
.csp-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-06 {
  --bg: oklch(0.985 0.004 190);
  --surface: #fff;
  --ink: oklch(0.22 0.02 220);
  --muted: oklch(0.5 0.02 220);
  --line: oklch(0.92 0.007 210);
  --accent: oklch(0.55 0.12 190);
  color-scheme: light;
  container-type: inline-size;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 24px 100px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  accent-color: var(--accent);
  width: 100%;
}

.csp-06__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.csp-06__wrap {
  max-width: 900px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.csp-06__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
}

.csp-06__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-06__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-06__btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 11px;
  font: 650 14px/1 system-ui,sans-serif;
  text-decoration: none;
  color: #fff;
  background: var(--accent);
  box-shadow: 0 1px 0 oklch(1 0 0/.2) inset,0 6px 16px -8px var(--accent);
}

.csp-06__btn::before {
  content: "+";
  font: 500 18px/1 system-ui,sans-serif;
}

.csp-06__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.csp-06__seats {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 18px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
}

.csp-06__seatbar {
  flex: 0 0 140px;
  height: 8px;
  border-radius: 999px;
  background: oklch(0.94 0.006 210);
  overflow: hidden;
}

.csp-06__seatbar i {
  display: block;
  height: 100%;
  border-radius: inherit;
  background: var(--accent);
}

.csp-06__seats p {
  font: 400 13.5px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-06__seats b {
  color: var(--ink);
  font-weight: 650;
}

.csp-06__tools {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.csp-06__search {
  flex: 1 1 260px;
}

.csp-06__tools input,
.csp-06__tools select {
  width: 100%;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: var(--surface);
  font: 400 14.5px/1 system-ui,sans-serif;
  color: var(--ink);
}

.csp-06__search input {
  padding-left: 40px;
  background: var(--surface) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Ccircle cx='9' cy='9' r='5.5' fill='none' stroke='%23889' stroke-width='1.6'/%3E%3Cpath d='m13 13 3.5 3.5' stroke='%23889' stroke-width='1.6' stroke-linecap='round'/%3E%3C/svg%3E") 14px center/18px no-repeat;
}

.csp-06__tools input:focus,
.csp-06__tools select:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.55 0.12 190/.18);
}

.csp-06__count {
  font: 500 12.5px/1 system-ui,sans-serif;
  color: var(--muted);
  min-height: 12px;
}

.csp-06__list {
  list-style: none;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  overflow: hidden;
}

.csp-06__row {
  display: grid;
  grid-template-rows: 1fr;
  transition: grid-template-rows .35s cubic-bezier(.3,.7,.3,1),opacity .25s;
}

.csp-06__row+.csp-06__row .csp-06__inner {
  border-top: 1px solid var(--line);
}

.csp-06__row.is-removing {
  grid-template-rows: 0fr;
  opacity: 0;
}

.csp-06__inner {
  overflow: hidden;
  min-height: 0;
  display: grid;
  grid-template-columns: auto minmax(0,1fr) 110px 120px 84px;
  align-items: center;
  gap: 14px;
  padding: 12px 18px;
  transition: background .15s;
}

.csp-06__row:hover .csp-06__inner {
  background: oklch(0.985 0.004 200);
}

.csp-06__av {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font: 650 13.5px/1 system-ui,sans-serif;
  color: oklch(0.35 0.1 var(--h));
  background: oklch(0.92 0.06 var(--h));
}

.csp-06__av--pending {
  color: var(--muted);
  background: transparent;
  border: 1.5px dashed oklch(0.82 0.01 210);
}

.csp-06__who {
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-width: 0;
}

.csp-06__who b {
  display: flex;
  align-items: center;
  gap: 6px;
  font: 600 14px/1.2 system-ui,sans-serif;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.csp-06__who em {
  font: 600 10.5px/1 system-ui,sans-serif;
  font-style: normal;
  padding: 3px 6px;
  border-radius: 5px;
  color: var(--muted);
  background: oklch(0.95 0.005 210);
}

.csp-06__who em.csp-06__guest {
  color: oklch(0.5 0.13 60);
  background: oklch(0.96 0.05 85);
}

.csp-06__who small {
  font: 400 12.5px/1.3 system-ui,sans-serif;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.csp-06__seen {
  font: 400 13px/1 system-ui,sans-serif;
  color: var(--muted);
}

.csp-06__pend {
  padding: 4px 9px;
  border-radius: 999px;
  font: 600 11.5px/1 system-ui,sans-serif;
  color: oklch(0.5 0.13 65);
  background: oklch(0.96 0.05 85);
}

.csp-06__role {
  --rc: var(--muted);
  min-height: 36px;
  padding: 0 30px 0 12px;
  border: 1px solid color-mix(in oklab,var(--rc) 30%,transparent);
  border-radius: 9px;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--rc);
  background: color-mix(in oklab,var(--rc) 8%,var(--surface)) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='m3 4.5 3 3 3-3' fill='none' stroke='%23778' stroke-width='1.4' stroke-linecap='round'/%3E%3C/svg%3E") right 10px center/12px no-repeat;
  appearance: none;
  cursor: pointer;
}

.csp-06__role:disabled {
  cursor: not-allowed;
  background-image: none;
  padding-right: 12px;
}

[data-role="owner"] .csp-06__role {
  --rc: oklch(0.5 0.17 290);
}

[data-role="admin"] .csp-06__role {
  --rc: oklch(0.5 0.13 190);
}

[data-role="member"] .csp-06__role {
  --rc: oklch(0.45 0.03 240);
}

[data-role="viewer"] .csp-06__role {
  --rc: oklch(0.55 0.02 240);
}

.csp-06__role:focus-visible,
.csp-06__rm:focus-visible,
.csp-06__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-06__rm {
  justify-self: end;
  min-height: 36px;
  padding: 0 12px;
  border: 0;
  border-radius: 9px;
  background: transparent;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
  transition: color .15s,background .15s;
}

.csp-06__rm:hover {
  color: oklch(0.55 0.2 25);
  background: oklch(0.97 0.02 25);
}

.csp-06__link {
  border: 0;
  background: none;
  font: inherit;
  color: var(--accent);
  font-weight: 600;
  cursor: pointer;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.csp-06__empty {
  padding: 32px;
  text-align: center;
  font: 500 14px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-06__toast {
  position: fixed;
  left: 50%;
  bottom: 22px;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 8px 8px 8px 18px;
  border-radius: 12px;
  background: var(--ink);
  color: #fff;
  font: 500 13.5px/1.3 system-ui,sans-serif;
  box-shadow: 0 18px 40px -14px oklch(0 0 0/.5);
  translate: -50% 160%;
  transition: translate .35s cubic-bezier(.2,.9,.3,1.15);
}

.csp-06__toast.is-on {
  translate: -50% 0;
}

.csp-06__toast button {
  min-height: 36px;
  padding: 0 14px;
  border: 0;
  border-radius: 8px;
  font: 650 13px/1 system-ui,sans-serif;
  color: var(--ink);
  background: #fff;
  cursor: pointer;
}

@container (max-width: 680px) {
  .csp-06__inner {
    grid-template-columns: auto minmax(0,1fr) auto;
    grid-template-areas: "av who rm" "av role role";
  }

  .csp-06__av {
    grid-area: av;
    align-self: start;
  }

  .csp-06__who {
    grid-area: who;
  }

  .csp-06__rm,
    .csp-06__more {
    grid-area: rm;
  }

  .csp-06__role {
    grid-area: role;
    justify-self: start;
  }

  .csp-06__seen {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-06 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-06');
  var q = root.querySelector('[data-q]'), rf = root.querySelector('[data-rf]');
  var count = root.querySelector('[data-count]'), empty = root.querySelector('[data-empty]');
  var toast = root.querySelector('[data-toast]'), tmsg = root.querySelector('[data-tmsg]');
  var pending = null, timer = 0;
  var rows = function () { return root.querySelectorAll('.csp-06__row:not(.is-gone)'); };

  function apply() {
    var term = q.value.trim().toLowerCase(), role = rf.value, shown = 0, all = rows();
    all.forEach(function (r) {
      var hit = (!term || (r.dataset.name + ' ' + r.dataset.email).toLowerCase().indexOf(term) > -1) && (!role || r.dataset.role === role);
      r.hidden = !hit; if (hit) shown++;
    });
    count.textContent = 'Showing ' + shown + ' of ' + all.length + ' members';
    empty.hidden = shown > 0;
  }
  q.addEventListener('input', apply);
  rf.addEventListener('change', apply);

  root.addEventListener('change', function (e) {
    if (!e.target.classList.contains('csp-06__role')) return;
    var row = e.target.closest('.csp-06__row');
    row.dataset.role = e.target.value;
    show(row.dataset.name + ' is now ' + e.target.options[e.target.selectedIndex].text, false);
  });

  function commit() { if (pending) { pending.classList.add('is-gone'); pending.hidden = true; pending = null; apply(); } }
  function show(text, undo) {
    tmsg.textContent = text;
    toast.querySelector('[data-undo]').hidden = !undo;
    toast.classList.add('is-on');
    clearTimeout(timer);
    timer = setTimeout(function () { toast.classList.remove('is-on'); commit(); }, undo ? 5000 : 2200);
  }
  root.addEventListener('click', function (e) {
    var rm = e.target.closest('.csp-06__rm');
    if (rm) { commit(); pending = rm.closest('.csp-06__row'); pending.classList.add('is-removing'); show(pending.dataset.name + ' removed', true); }
    if (e.target.closest('[data-resend]')) { e.target.textContent = 'Invite sent ✓'; }
    if (e.target.closest('[data-undo]') && pending) { pending.classList.remove('is-removing'); pending = null; toast.classList.remove('is-on'); clearTimeout(timer); }
  });
  apply();
})();
```

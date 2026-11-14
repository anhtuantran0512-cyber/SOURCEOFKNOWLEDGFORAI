---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-team-members-page-with-roles/"
title: "Tailwind Team Members Page with Roles"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A team page that scales from 5 to 500 people: a seat meter, instant search across names and emails, a segmented role filter with a live result count,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Team Members Page with Roles
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-team-members-page-with-roles/

A team page that scales from 5 to 500 people: a seat meter, instant search across names and emails, a segmented role filter with a live result count, colour-coded role selects that recolour the moment you change them, a locked Owner, 2FA status per person, a pending-invite row with Resend, and removal that collapses the row smoothly with a five-second Undo toast.
## HTML
```html
<section data-tsp06 class="tsp-06 w-full min-h-svh bg-tsp06-bg px-4 py-10 font-tsp06-sans text-tsp06-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-06-h">
  <div class="mx-auto grid w-full max-w-5xl gap-6">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div><h1 id="tsp-06-h" class="text-3xl font-semibold tracking-tight">Team</h1><p class="mt-1 text-tsp06-mut">Manage who has access to the Northwind workspace.</p></div>
      <div class="flex flex-wrap items-center gap-4">
        <div class="grid w-44 gap-1.5"><p class="flex justify-between text-sm"><span class="text-tsp06-mut">Seats</span><span class="font-semibold tabular-nums"><span data-seats>9</span> of 12</span></p><div class="h-1.5 rounded-full bg-tsp06-line"><div data-seat-bar class="h-full w-[75%] rounded-full bg-tsp06-acc transition-[width] duration-500"></div></div></div>
        <a href="#tsp-06-h" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp06-ink px-4 text-sm font-semibold text-white shadow-sm transition hover:bg-tsp06-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp06-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 5v14M5 12h14"/></svg>Invite people</a>
      </div>
    </header>

    <div class="flex flex-wrap items-center gap-3">
      <label class="relative min-w-60 flex-1"><span class="sr-only">Search members</span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none absolute left-3.5 top-1/2 size-4 -translate-y-1/2 text-tsp06-mut"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input data-search type="search" placeholder="Search by name or email" class="min-h-11 w-full rounded-xl border border-tsp06-line bg-white pl-10 pr-3.5 text-sm shadow-xs outline-none transition placeholder:text-tsp06-mut focus:border-tsp06-acc focus:ring-4 focus:ring-tsp06-acc/15"></label>
      <fieldset class="flex rounded-xl border border-tsp06-line bg-white p-1 shadow-xs">
        <legend class="sr-only">Filter by role</legend>
        <label class="flex min-h-9 cursor-pointer items-center rounded-lg px-3 text-sm font-medium text-tsp06-mut transition has-checked:bg-tsp06-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp06-acc"><input type="radio" name="tsp-06-role" value="all" class="sr-only" checked>All</label>
        <label class="flex min-h-9 cursor-pointer items-center rounded-lg px-3 text-sm font-medium text-tsp06-mut transition has-checked:bg-tsp06-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp06-acc"><input type="radio" name="tsp-06-role" value="admin" class="sr-only">Admins</label>
        <label class="flex min-h-9 cursor-pointer items-center rounded-lg px-3 text-sm font-medium text-tsp06-mut transition has-checked:bg-tsp06-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp06-acc"><input type="radio" name="tsp-06-role" value="member" class="sr-only">Members</label>
        <label class="flex min-h-9 cursor-pointer items-center rounded-lg px-3 text-sm font-medium text-tsp06-mut transition has-checked:bg-tsp06-ink has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tsp06-acc"><input type="radio" name="tsp-06-role" value="viewer" class="sr-only">Viewers</label>
      </fieldset>
      <p data-result class="ml-auto text-sm text-tsp06-mut" aria-live="polite">9 members</p>
    </div>

    <ul data-list class="divide-y divide-tsp06-line overflow-hidden rounded-3xl border border-tsp06-line bg-white shadow-[0_1px_2px_rgb(0_0_0/0.04)]">
      <li data-member data-name="ava mitchell" data-email="[email protected]" data-role="owner" class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-hidden:hidden data-removing:grid-rows-[0fr] data-removing:opacity-0"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-x-4 gap-y-3 px-5 py-4">
        <span class="grid size-10 flex-none place-items-center rounded-full bg-linear-135 from-teal-400 to-emerald-600 text-sm font-semibold text-white">AM</span>
        <div class="min-w-0 flex-1"><p class="flex items-center gap-2 font-medium">Ava Mitchell <span class="rounded-full bg-tsp06-bg px-2 py-0.5 text-[11px] font-semibold text-tsp06-mut">You</span></p><p class="truncate text-sm text-tsp06-mut">[email protected]</p></div>
        <span class="hidden items-center gap-1 text-xs font-medium text-emerald-700 sm:flex"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>2FA</span>
        <span class="hidden w-24 text-sm text-tsp06-mut md:block">Active now</span>
        <span class="inline-flex min-h-11 w-32 items-center gap-1.5 rounded-xl bg-amber-50 px-3 text-sm font-semibold text-amber-800 ring-1 ring-inset ring-amber-200" title="Transfer ownership from the danger zone"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M7 11V7a5 5 0 0 1 10 0v4M5 11h14v10H5z"/></svg>Owner</span>
        <span class="size-11"></span>
      </div></div></li>
      <li data-member data-name="noah patel" data-email="[email protected]" data-role="admin" class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-hidden:hidden data-removing:grid-rows-[0fr] data-removing:opacity-0"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-x-4 gap-y-3 px-5 py-4">
        <span class="grid size-10 flex-none place-items-center rounded-full bg-violet-100 text-sm font-semibold text-violet-700">NP</span>
        <div class="min-w-0 flex-1"><p class="font-medium">Noah Patel</p><p class="truncate text-sm text-tsp06-mut">[email protected]</p></div>
        <span class="hidden items-center gap-1 text-xs font-medium text-emerald-700 sm:flex"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>2FA</span>
        <span class="hidden w-24 text-sm text-tsp06-mut md:block">2 hours ago</span>
        <span class="relative w-32"><select data-role-select data-role="admin" aria-label="Role for Noah Patel" class="min-h-11 w-full cursor-pointer appearance-none rounded-xl border-0 pl-3 pr-8 text-sm font-semibold ring-1 ring-inset outline-none transition focus-visible:ring-2 focus-visible:ring-tsp06-acc data-[role=admin]:bg-violet-50 data-[role=admin]:text-violet-700 data-[role=admin]:ring-violet-200 data-[role=member]:bg-sky-50 data-[role=member]:text-sky-700 data-[role=member]:ring-sky-200 data-[role=viewer]:bg-zinc-100 data-[role=viewer]:text-zinc-700 data-[role=viewer]:ring-zinc-200"><option value="admin" selected>Admin</option><option value="member">Member</option><option value="viewer">Viewer</option></select><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none absolute right-2.5 top-1/2 size-4 -translate-y-1/2 opacity-60"><path d="m6 9 6 6 6-6"/></svg></span>
        <button type="button" data-remove class="grid size-11 place-items-center rounded-xl text-tsp06-mut transition hover:bg-rose-50 hover:text-rose-600 focus-visible:outline-2 focus-visible:outline-tsp06-acc" aria-label="Remove Noah Patel"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg></button>
      </div></div></li>
      <li data-member data-name="priya shah" data-email="[email protected]" data-role="admin" class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-hidden:hidden data-removing:grid-rows-[0fr] data-removing:opacity-0"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-x-4 gap-y-3 px-5 py-4">
        <span class="grid size-10 flex-none place-items-center rounded-full bg-amber-100 text-sm font-semibold text-amber-700">PS</span>
        <div class="min-w-0 flex-1"><p class="font-medium">Priya Shah</p><p class="truncate text-sm text-tsp06-mut">[email protected]</p></div>
        <span class="hidden items-center gap-1 text-xs font-medium text-emerald-700 sm:flex"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>2FA</span>
        <span class="hidden w-24 text-sm text-tsp06-mut md:block">Yesterday</span>
        <span class="relative w-32"><select data-role-select data-role="admin" aria-label="Role for Priya Shah" class="min-h-11 w-full cursor-pointer appearance-none rounded-xl border-0 pl-3 pr-8 text-sm font-semibold ring-1 ring-inset outline-none transition focus-visible:ring-2 focus-visible:ring-tsp06-acc data-[role=admin]:bg-violet-50 data-[role=admin]:text-violet-700 data-[role=admin]:ring-violet-200 data-[role=member]:bg-sky-50 data-[role=member]:text-sky-700 data-[role=member]:ring-sky-200 data-[role=viewer]:bg-zinc-100 data-[role=viewer]:text-zinc-700 data-[role=viewer]:ring-zinc-200"><option value="admin" selected>Admin</option><option value="member">Member</option><option value="viewer">Viewer</option></select><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none absolute right-2.5 top-1/2 size-4 -translate-y-1/2 opacity-60"><path d="m6 9 6 6 6-6"/></svg></span>
        <button type="button" data-remove class="grid size-11 place-items-center rounded-xl text-tsp06-mut transition hover:bg-rose-50 hover:text-rose-600 focus-visible:outline-2 focus-visible:outline-tsp06-acc" aria-label="Remove Priya Shah"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg></button>
      </div></div></li>
      <li data-member data-name="leo martins" data-email="[email protected]" data-role="member" class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-hidden:hidden data-removing:grid-rows-[0fr] data-removing:opacity-0"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-x-4 gap-y-3 px-5 py-4">
        <span class="grid size-10 flex-none place-items-center rounded-full bg-sky-100 text-sm font-semibold text-sky-700">LM</span>
        <div class="min-w-0 flex-1"><p class="font-medium">Leo Martins</p><p class="truncate text-sm text-tsp06-mut">[email protected]</p></div>
        <span class="hidden items-center gap-1 text-xs font-medium text-amber-700 sm:flex"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="M12 9v3M12 15h.01"/></svg>No 2FA</span>
        <span class="hidden w-24 text-sm text-tsp06-mut md:block">3 days ago</span>
        <span class="relative w-32"><select data-role-select data-role="member" aria-label="Role for Leo Martins" class="min-h-11 w-full cursor-pointer appearance-none rounded-xl border-0 pl-3 pr-8 text-sm font-semibold ring-1 ring-inset outline-none transition focus-visible:ring-2 focus-visible:ring-tsp06-acc data-[role=admin]:bg-violet-50 data-[role=admin]:text-violet-700 data-[role=admin]:ring-violet-200 data-[role=member]:bg-sky-50 data-[role=member]:text-sky-700 data-[role=member]:ring-sky-200 data-[role=viewer]:bg-zinc-100 data-[role=viewer]:text-zinc-700 data-[role=viewer]:ring-zinc-200"><option value="admin">Admin</option><option value="member" selected>Member</option><option value="viewer">Viewer</option></select><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none absolute right-2.5 top-1/2 size-4 -translate-y-1/2 opacity-60"><path d="m6 9 6 6 6-6"/></svg></span>
        <button type="button" data-remove class="grid size-11 place-items-center rounded-xl text-tsp06-mut transition hover:bg-rose-50 hover:text-rose-600 focus-visible:outline-2 focus-visible:outline-tsp06-acc" aria-label="Remove Leo Martins"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg></button>
      </div></div></li>
      <li data-member data-name="mia chen" data-email="[email protected]" data-role="member" class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-hidden:hidden data-removing:grid-rows-[0fr] data-removing:opacity-0"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-x-4 gap-y-3 px-5 py-4">
        <span class="grid size-10 flex-none place-items-center rounded-full bg-rose-100 text-sm font-semibold text-rose-700">MC</span>
        <div class="min-w-0 flex-1"><p class="font-medium">Mia Chen</p><p class="truncate text-sm text-tsp06-mut">[email protected]</p></div>
        <span class="hidden items-center gap-1 text-xs font-medium text-emerald-700 sm:flex"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>2FA</span>
        <span class="hidden w-24 text-sm text-tsp06-mut md:block">Active now</span>
        <span class="relative w-32"><select data-role-select data-role="member" aria-label="Role for Mia Chen" class="min-h-11 w-full cursor-pointer appearance-none rounded-xl border-0 pl-3 pr-8 text-sm font-semibold ring-1 ring-inset outline-none transition focus-visible:ring-2 focus-visible:ring-tsp06-acc data-[role=admin]:bg-violet-50 data-[role=admin]:text-violet-700 data-[role=admin]:ring-violet-200 data-[role=member]:bg-sky-50 data-[role=member]:text-sky-700 data-[role=member]:ring-sky-200 data-[role=viewer]:bg-zinc-100 data-[role=viewer]:text-zinc-700 data-[role=viewer]:ring-zinc-200"><option value="admin">Admin</option><option value="member" selected>Member</option><option value="viewer">Viewer</option></select><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none absolute right-2.5 top-1/2 size-4 -translate-y-1/2 opacity-60"><path d="m6 9 6 6 6-6"/></svg></span>
        <button type="button" data-remove class="grid size-11 place-items-center rounded-xl text-tsp06-mut transition hover:bg-rose-50 hover:text-rose-600 focus-visible:outline-2 focus-visible:outline-tsp06-acc" aria-label="Remove Mia Chen"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg></button>
      </div></div></li>
      <li data-member data-name="jonas weber" data-email="[email protected]" data-role="member" class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-hidden:hidden data-removing:grid-rows-[0fr] data-removing:opacity-0"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-x-4 gap-y-3 px-5 py-4">
        <span class="grid size-10 flex-none place-items-center rounded-full bg-emerald-100 text-sm font-semibold text-emerald-700">JW</span>
        <div class="min-w-0 flex-1"><p class="font-medium">Jonas Weber</p><p class="truncate text-sm text-tsp06-mut">[email protected]</p></div>
        <span class="hidden items-center gap-1 text-xs font-medium text-emerald-700 sm:flex"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>2FA</span>
        <span class="hidden w-24 text-sm text-tsp06-mut md:block">Last week</span>
        <span class="relative w-32"><select data-role-select data-role="member" aria-label="Role for Jonas Weber" class="min-h-11 w-full cursor-pointer appearance-none rounded-xl border-0 pl-3 pr-8 text-sm font-semibold ring-1 ring-inset outline-none transition focus-visible:ring-2 focus-visible:ring-tsp06-acc data-[role=admin]:bg-violet-50 data-[role=admin]:text-violet-700 data-[role=admin]:ring-violet-200 data-[role=member]:bg-sky-50 data-[role=member]:text-sky-700 data-[role=member]:ring-sky-200 data-[role=viewer]:bg-zinc-100 data-[role=viewer]:text-zinc-700 data-[role=viewer]:ring-zinc-200"><option value="admin">Admin</option><option value="member" selected>Member</option><option value="viewer">Viewer</option></select><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none absolute right-2.5 top-1/2 size-4 -translate-y-1/2 opacity-60"><path d="m6 9 6 6 6-6"/></svg></span>
        <button type="button" data-remove class="grid size-11 place-items-center rounded-xl text-tsp06-mut transition hover:bg-rose-50 hover:text-rose-600 focus-visible:outline-2 focus-visible:outline-tsp06-acc" aria-label="Remove Jonas Weber"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg></button>
      </div></div></li>
      <li data-member data-name="sara kim" data-email="[email protected]" data-role="viewer" class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-hidden:hidden data-removing:grid-rows-[0fr] data-removing:opacity-0"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-x-4 gap-y-3 px-5 py-4">
        <span class="grid size-10 flex-none place-items-center rounded-full bg-zinc-200 text-sm font-semibold text-zinc-700">SK</span>
        <div class="min-w-0 flex-1"><p class="flex items-center gap-2 font-medium">Sara Kim <span class="rounded-full bg-orange-50 px-2 py-0.5 text-[11px] font-semibold text-orange-700">External</span></p><p class="truncate text-sm text-tsp06-mut">[email protected]</p></div>
        <span class="hidden items-center gap-1 text-xs font-medium text-amber-700 sm:flex"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="M12 9v3M12 15h.01"/></svg>No 2FA</span>
        <span class="hidden w-24 text-sm text-tsp06-mut md:block">2 weeks ago</span>
        <span class="relative w-32"><select data-role-select data-role="viewer" aria-label="Role for Sara Kim" class="min-h-11 w-full cursor-pointer appearance-none rounded-xl border-0 pl-3 pr-8 text-sm font-semibold ring-1 ring-inset outline-none transition focus-visible:ring-2 focus-visible:ring-tsp06-acc data-[role=admin]:bg-violet-50 data-[role=admin]:text-violet-700 data-[role=admin]:ring-violet-200 data-[role=member]:bg-sky-50 data-[role=member]:text-sky-700 data-[role=member]:ring-sky-200 data-[role=viewer]:bg-zinc-100 data-[role=viewer]:text-zinc-700 data-[role=viewer]:ring-zinc-200"><option value="admin">Admin</option><option value="member">Member</option><option value="viewer" selected>Viewer</option></select><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none absolute right-2.5 top-1/2 size-4 -translate-y-1/2 opacity-60"><path d="m6 9 6 6 6-6"/></svg></span>
        <button type="button" data-remove class="grid size-11 place-items-center rounded-xl text-tsp06-mut transition hover:bg-rose-50 hover:text-rose-600 focus-visible:outline-2 focus-visible:outline-tsp06-acc" aria-label="Remove Sara Kim"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg></button>
      </div></div></li>
      <li data-member data-name="omar haddad" data-email="[email protected]" data-role="viewer" class="grid grid-rows-[1fr] transition-[grid-template-rows,opacity] duration-300 data-hidden:hidden data-removing:grid-rows-[0fr] data-removing:opacity-0"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-x-4 gap-y-3 px-5 py-4">
        <span class="grid size-10 flex-none place-items-center rounded-full bg-indigo-100 text-sm font-semibold text-indigo-700">OH</span>
        <div class="min-w-0 flex-1"><p class="font-medium">Omar Haddad</p><p class="truncate text-sm text-tsp06-mut">[email protected]</p></div>
        <span class="hidden items-center gap-1 text-xs font-medium text-emerald-700 sm:flex"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3.5"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>2FA</span>
        <span class="hidden w-24 text-sm text-tsp06-mut md:block">Last month</span>
        <span class="relative w-32"><select data-role-select data-role="viewer" aria-label="Role for Omar Haddad" class="min-h-11 w-full cursor-pointer appearance-none rounded-xl border-0 pl-3 pr-8 text-sm font-semibold ring-1 ring-inset outline-none transition focus-visible:ring-2 focus-visible:ring-tsp06-acc data-[role=admin]:bg-violet-50 data-[role=admin]:text-violet-700 data-[role=admin]:ring-violet-200 data-[role=member]:bg-sky-50 data-[role=member]:text-sky-700 data-[role=member]:ring-sky-200 data-[role=viewer]:bg-zinc-100 data-[role=viewer]:text-zinc-700 data-[role=viewer]:ring-zinc-200"><option value="admin">Admin</option><option value="member">Member</option><option value="viewer" selected>Viewer</option></select><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none absolute right-2.5 top-1/2 size-4 -translate-y-1/2 opacity-60"><path d="m6 9 6 6 6-6"/></svg></span>
        <button type="button" data-remove class="grid size-11 place-items-center rounded-xl text-tsp06-mut transition hover:bg-rose-50 hover:text-rose-600 focus-visible:outline-2 focus-visible:outline-tsp06-acc" aria-label="Remove Omar Haddad"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/></svg></button>
      </div></div></li>
      <li data-member data-name="dana" data-email="[email protected]" data-role="member" class="grid grid-rows-[1fr] bg-tsp06-bg/50 transition-[grid-template-rows,opacity] duration-300 data-hidden:hidden data-removing:grid-rows-[0fr] data-removing:opacity-0"><div class="overflow-hidden"><div class="flex flex-wrap items-center gap-x-4 gap-y-3 px-5 py-4">
        <span class="grid size-10 flex-none place-items-center rounded-full border-2 border-dashed border-tsp06-line text-tsp06-mut"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span>
        <div class="min-w-0 flex-1"><p class="flex items-center gap-2 font-medium">[email protected] <span class="rounded-full bg-amber-100 px-2 py-0.5 text-[11px] font-semibold text-amber-800">Invite pending</span></p><p class="truncate text-sm text-tsp06-mut">Invited by Noah Patel · expires in 5 days</p></div>
        <button type="button" data-resend class="inline-flex min-h-11 w-32 items-center justify-center rounded-xl border border-tsp06-line bg-white text-sm font-semibold shadow-xs transition hover:bg-tsp06-bg focus-visible:outline-2 focus-visible:outline-tsp06-acc data-sent:text-emerald-700">Resend</button>
        <button type="button" data-remove class="grid size-11 place-items-center rounded-xl text-tsp06-mut transition hover:bg-rose-50 hover:text-rose-600 focus-visible:outline-2 focus-visible:outline-tsp06-acc" aria-label="Revoke invite for [email protected]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
      </div></div></li>
      <li data-empty hidden class="grid justify-items-center gap-1 px-5 py-12 text-center"><p class="font-medium">No one matches that search</p><p class="text-sm text-tsp06-mut">Try a different name, email or role.</p></li>
    </ul>
  </div>
  <div data-toast role="status" aria-live="polite" class="group/toast pointer-events-none fixed inset-x-0 bottom-5 z-20 flex justify-center px-4">
    <div class="pointer-events-auto flex translate-y-[180%] items-center gap-4 rounded-2xl bg-tsp06-ink py-2 pl-5 pr-2 text-sm text-white shadow-2xl transition duration-300 group-data-show/toast:translate-y-0 motion-reduce:transition-none"><span data-toast-msg>Member removed</span><button type="button" data-undo class="min-h-11 rounded-xl px-4 font-semibold text-tsp06-acc2 transition hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-white">Undo</button></div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp06-bg: #f4f7f6;
  --color-tsp06-bg: oklch(0.975 0.004 175);
  --color-tsp06-ink: #11201d;
  --color-tsp06-ink: oklch(0.225 0.02 178);
  --color-tsp06-mut: #5a6b67;
  --color-tsp06-mut: oklch(0.52 0.02 178);
  --color-tsp06-line: #e1e8e6;
  --color-tsp06-line: oklch(0.93 0.008 178);
  --color-tsp06-acc: #0d9488;
  --color-tsp06-acc: oklch(0.6 0.104 185);
  --color-tsp06-acc2: #5eead4;
  --color-tsp06-acc2: oklch(0.855 0.13 181);
  --font-tsp06-sans: 'Outfit', system-ui, sans-serif;
}

.tsp-06 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp06]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const UNDO_MS = 5000;
  const search = root.querySelector('[data-search]');
  const result = root.querySelector('[data-result]');
  const empty = root.querySelector('[data-empty]');
  const toast = root.querySelector('[data-toast]');
  const members = () => [...root.querySelectorAll('[data-member]:not([data-removing])')];
  const apply = () => {
    const q = search.value.trim().toLowerCase();
    const role = root.querySelector('[name=tsp-06-role]:checked').value;
    let shown = 0;
    members().forEach((li) => {
      const hit = (!q || li.dataset.name.includes(q) || li.dataset.email.includes(q)) && (role === 'all' || li.dataset.role === role);
      li.toggleAttribute('data-hidden', !hit);
      if (hit) shown++;
    });
    const total = members().length;
    result.textContent = shown === total ? total + ' members' : shown + ' of ' + total + ' members';
    empty.hidden = shown > 0;
  };
  const seats = () => {
    const n = members().length;
    root.querySelector('[data-seats]').textContent = n;
    root.querySelector('[data-seat-bar]').style.width = (n / 12) * 100 + '%';
  };
  search.addEventListener('input', apply);
  root.querySelectorAll('[name=tsp-06-role]').forEach((r) => r.addEventListener('change', apply));
  root.querySelectorAll('[data-role-select]').forEach((s) => s.addEventListener('change', () => {
    s.dataset.role = s.value;
    s.closest('[data-member]').dataset.role = s.value;
    apply();
  }));
  root.querySelectorAll('[data-resend]').forEach((b) => b.addEventListener('click', () => { b.dataset.sent = ''; b.textContent = 'Sent ✓'; }));
  let pending = null, timer;
  const commit = () => { if (pending) pending.remove(); pending = null; delete toast.dataset.show; };
  root.querySelectorAll('[data-remove]').forEach((b) => b.addEventListener('click', () => {
    commit();
    const li = b.closest('[data-member]');
    pending = li;
    li.dataset.removing = '';
    root.querySelector('[data-toast-msg]').textContent = (li.querySelector('.font-medium').firstChild.textContent.trim()) + ' removed';
    toast.dataset.show = '';
    seats(); apply();
    clearTimeout(timer);
    timer = setTimeout(commit, UNDO_MS);
  }));
  root.querySelector('[data-undo]').addEventListener('click', () => {
    if (!pending) return;
    delete pending.dataset.removing;
    pending = null;
    clearTimeout(timer);
    delete toast.dataset.show;
    seats(); apply();
  });
})();
```

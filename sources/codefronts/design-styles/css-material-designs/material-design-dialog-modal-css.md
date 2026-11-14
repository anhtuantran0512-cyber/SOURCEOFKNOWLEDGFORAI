---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-dialog-modal-css/"
title: "Material Design Dialog Modal CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Alert dialog, full-featured share dialog, bottom sheet, and snackbar — all toggled with the CSS checkbox-hack, no JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Dialog Modal CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-dialog-modal-css/

Alert dialog, full-featured share dialog, bottom sheet, and snackbar — all toggled with the CSS checkbox-hack, no JavaScript.
## HTML
```html
<div class="md-05">
  <!-- Modals (outside flow via fixed positioning, controlled by hidden checkboxes) -->

  <!-- Alert Dialog -->
  <input class="md-05__modal-trigger" type="checkbox" id="md05-alert">
  <div class="md-05__backdrop">
    <div class="md-05__dialog">
      <div class="md-05__dialog-icon">🗑</div>
      <div class="md-05__dialog-head md-05__dialog-head--center">Delete project?</div>
      <div class="md-05__dialog-body md-05__dialog-body--center">This will permanently delete "Aurora Dashboard" and all of its contents. This action cannot be undone.</div>
      <div class="md-05__dialog-actions" style="justify-content:center">
        <label class="md-05__dialog-btn md-05__dialog-btn--text md-05__close-label" for="md05-alert">Cancel</label>
        <label class="md-05__dialog-btn md-05__dialog-btn--err md-05__close-label" for="md05-alert">Delete</label>
      </div>
    </div>
  </div>

  <!-- Full Dialog -->
  <input class="md-05__modal-trigger" type="checkbox" id="md05-full">
  <div class="md-05__backdrop">
    <div class="md-05__dialog" style="position:relative">
      <label class="md-05__dialog-btn--close md-05__close-label" for="md05-full">✕</label>
      <div class="md-05__dialog-head">Share with people</div>
      <div class="md-05__dialog-body">
        <div style="display:flex;flex-direction:column;gap:12px">
          <div style="background:#f5f5f5;border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px">
            <span style="font-size:1.3rem">🔗</span>
            <div style="flex:1;font-size:.85rem;color:#616161;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">https://aurora.design/shared/abc123</div>
            <button style="background:none;border:none;color:#4527a0;font-size:.8rem;font-weight:500;cursor:pointer">Copy</button>
          </div>
          <div style="font-size:.82rem;color:#9e9e9e">Anyone with the link can view this project</div>
          <div style="height:1px;background:#e0e0e0;margin:4px 0"></div>
          <div style="font-size:.9rem;font-weight:500">People with access</div>
          <div style="display:flex;align-items:center;gap:12px">
            <div style="width:36px;height:36px;border-radius:50%;background:#4527a0;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.9rem;font-weight:700">A</div>
            <div style="flex:1"><div style="font-size:.88rem;font-weight:500">Alex Thompson</div><div style="font-size:.78rem;color:#9e9e9e">[email protected] · Owner</div></div>
          </div>
          <div style="display:flex;align-items:center;gap:12px">
            <div style="width:36px;height:36px;border-radius:50%;background:#e91e63;color:#fff;display:flex;align-items:center;justify-content:center;font-size:.9rem;font-weight:700">M</div>
            <div style="flex:1"><div style="font-size:.88rem;font-weight:500">Maria Chen</div><div style="font-size:.78rem;color:#9e9e9e">[email protected] · Editor</div></div>
          </div>
        </div>
      </div>
      <div class="md-05__dialog-actions">
        <label class="md-05__dialog-btn md-05__dialog-btn--text md-05__close-label" for="md05-full">Close</label>
        <label class="md-05__dialog-btn md-05__dialog-btn--filled md-05__close-label" for="md05-full">Done</label>
      </div>
    </div>
  </div>

  <!-- Bottom Sheet -->
  <input class="md-05__sheet-trigger" type="checkbox" id="md05-sheet">
  <div class="md-05__sheet-backdrop">
    <div class="md-05__sheet">
      <div class="md-05__sheet-handle"></div>
      <div class="md-05__sheet-title">Export file as</div>
      <label class="md-05__sheet-option md-05__close-label" for="md05-sheet"><span class="md-05__sheet-option-icon">📄</span>PDF Document</label>
      <label class="md-05__sheet-option md-05__close-label" for="md05-sheet"><span class="md-05__sheet-option-icon">🖼</span>PNG Image</label>
      <label class="md-05__sheet-option md-05__close-label" for="md05-sheet"><span class="md-05__sheet-option-icon">⚡</span>SVG Vector</label>
      <label class="md-05__sheet-option md-05__close-label" for="md05-sheet"><span class="md-05__sheet-option-icon">📊</span>CSV Data</label>
      <label class="md-05__sheet-option md-05__close-label" for="md05-sheet"><span class="md-05__sheet-option-icon">💾</span>JSON Format</label>
    </div>
  </div>

  <!-- Snackbar -->
  <input class="md-05__snack-trigger" type="checkbox" id="md05-snack">
  <div class="md-05__snackbar">
    <span style="flex:1">✅ Changes saved to cloud</span>
    <label class="md-05__snack-action md-05__close-label" for="md05-snack">Undo</label>
    <label class="md-05__close-label" for="md05-snack" style="cursor:pointer;color:#aaa;font-size:1rem;padding:0 4px">✕</label>
  </div>

  <div class="md-05__wrap">
    <div class="md-05__page-title">Material Design Dialogs &amp; Modals</div>
    <div class="md-05__page-sub">Alert dialogs, full dialogs, bottom sheets and snackbars — CSS-only with checkbox-hack</div>

    <div class="md-05__btn-grid">
      <label class="md-05__trigger-btn" for="md05-alert" style="display:inline-flex;align-items:center;cursor:pointer;height:40px;padding:0 20px;font-size:.875rem;letter-spacing:.089em;text-transform:uppercase;font-weight:500">🗑 Alert Dialog</label>
      <label class="md-05__trigger-btn" for="md05-full" style="display:inline-flex;align-items:center;cursor:pointer;height:40px;padding:0 20px;font-size:.875rem;letter-spacing:.089em;text-transform:uppercase;font-weight:500;background:#7e57c2">↗ Share Dialog</label>
      <label class="md-05__trigger-btn" for="md05-sheet" style="display:inline-flex;align-items:center;cursor:pointer;height:40px;padding:0 20px;font-size:.875rem;letter-spacing:.089em;text-transform:uppercase;font-weight:500;background:#ff7043">⬆ Bottom Sheet</label>
      <label class="md-05__trigger-btn" for="md05-snack" style="display:inline-flex;align-items:center;cursor:pointer;height:40px;padding:0 20px;font-size:.875rem;letter-spacing:.089em;text-transform:uppercase;font-weight:500;background:#00897b">💾 Snackbar</label>
    </div>

    <div class="md-05__preview">
      <div class="md-05__preview-card">
        <div class="md-05__preview-label">Alert Dialog</div>
        <div style="background:#fff;border-radius:16px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,.1)">
          <div style="text-align:center;font-size:1.6rem;margin-bottom:8px">⚠</div>
          <div style="font-size:.95rem;font-weight:700;text-align:center;margin-bottom:6px;color:var(--ink)">Discard changes?</div>
          <div style="font-size:.8rem;color:var(--ink2);text-align:center;margin-bottom:16px">Changes will be lost if you leave this page</div>
          <div style="display:flex;gap:8px;justify-content:center">
            <div style="padding:8px 16px;border-radius:16px;font-size:.78rem;font-weight:500;color:var(--primary);text-transform:uppercase;letter-spacing:.05em">Keep</div>
            <div style="padding:8px 16px;border-radius:16px;font-size:.78rem;font-weight:500;background:var(--primary);color:#fff;text-transform:uppercase;letter-spacing:.05em">Discard</div>
          </div>
        </div>
      </div>

      <div class="md-05__preview-card">
        <div class="md-05__preview-label">Confirmation Dialog</div>
        <div style="background:#fff;border-radius:16px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,.1)">
          <div style="font-size:.95rem;font-weight:700;margin-bottom:6px;color:var(--ink)">Phone ringtone</div>
          <div style="display:flex;flex-direction:column;gap:2px">
            <div style="display:flex;align-items:center;gap:10px;padding:8px;border-radius:8px;background:rgba(69,39,160,.08)"><div style="width:16px;height:16px;border-radius:50%;background:var(--primary);display:flex;align-items:center;justify-content:center"><div style="width:6px;height:6px;border-radius:50%;background:#fff"></div></div><span style="font-size:.85rem;color:var(--primary);font-weight:500">Callisto</span></div>
            <div style="display:flex;align-items:center;gap:10px;padding:8px"><div style="width:16px;height:16px;border-radius:50%;border:2px solid #bdbdbd"></div><span style="font-size:.85rem;color:var(--ink)">Ganymede</span></div>
            <div style="display:flex;align-items:center;gap:10px;padding:8px"><div style="width:16px;height:16px;border-radius:50%;border:2px solid #bdbdbd"></div><span style="font-size:.85rem;color:var(--ink)">Luna</span></div>
          </div>
          <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:12px">
            <div style="padding:8px 16px;border-radius:16px;font-size:.78rem;font-weight:500;color:var(--primary);text-transform:uppercase;letter-spacing:.05em">Cancel</div>
            <div style="padding:8px 16px;border-radius:16px;font-size:.78rem;font-weight:500;background:var(--primary);color:#fff;text-transform:uppercase;letter-spacing:.05em">OK</div>
          </div>
        </div>
      </div>

      <div class="md-05__preview-card">
        <div class="md-05__preview-label">Snackbar Variants</div>
        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="background:#323232;color:#fff;border-radius:4px;padding:12px 16px;font-size:.85rem">Message sent</div>
          <div style="background:#323232;color:#fff;border-radius:4px;padding:12px 16px;font-size:.85rem;display:flex;justify-content:space-between;align-items:center"><span>Connection lost</span><span style="color:#bb86fc;font-size:.8rem;font-weight:500">Retry</span></div>
          <div style="background:#1b5e20;color:#fff;border-radius:4px;padding:12px 16px;font-size:.85rem;display:flex;gap:10px;align-items:center"><span>✓</span><span>Profile updated</span></div>
          <div style="background:#b71c1c;color:#fff;border-radius:4px;padding:12px 16px;font-size:.85rem;display:flex;gap:10px;align-items:center"><span>⚠</span><span>Upload failed</span></div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-05,
.md-05 *,
.md-05 *::before,
.md-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-05 ::selection {
  background: #4527a0;
  color: #fff;
}

.md-05 {
  --primary: #4527a0;
  --primary-l: #7e57c2;
  --secondary: #ff7043;
  --error: #b00020;
  --surface: #fff;
  --surface2: #f3f0fa;
  --bg: #ede7f6;
  --ink: #212121;
  --ink2: #616161;
  --ink3: #9e9e9e;
  --divider: #d1c4e9;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 48px 24px 80px;
  color: var(--ink);
}

.md-05__wrap {
  max-width: 900px;
  margin: 0 auto;
}

.md-05__page-title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  margin-bottom: 4px;
}

.md-05__page-sub {
  font-size: .9rem;
  color: var(--ink2);
  margin-bottom: 40px;
}
/* Trigger buttons */

.md-05__btn-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 56px;
}

.md-05__trigger-btn {
  height: 40px;
  padding: 0 20px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  background: var(--primary);
  color: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,.2);
  transition: box-shadow .2s;
}

.md-05__trigger-btn:hover {
  box-shadow: 0 4px 10px rgba(0,0,0,.25);
}
/* ── DIALOG BACKDROP / MODAL ── */

.md-05__backdrop {
  position: fixed;
  inset: 0;
  z-index: 100;
  background: rgba(0,0,0,0);
  pointer-events: none;
  transition: background .25s;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.md-05__modal-trigger {
  display: none;
}

.md-05__modal-trigger:checked ~ .md-05__backdrop {
  background: rgba(0,0,0,.5);
  pointer-events: auto;
}

.md-05__dialog {
  background: var(--surface);
  border-radius: 28px;
  min-width: 280px;
  max-width: 560px;
  width: 100%;
  box-shadow: 0 24px 38px rgba(0,0,0,.14),0 9px 46px rgba(0,0,0,.12),0 11px 15px rgba(0,0,0,.2);
  transform: scale(.9) translateY(20px);
  opacity: 0;
  transition: transform .3s cubic-bezier(.34,1.56,.64,1),opacity .25s;
  max-height: 80vh;
  overflow-y: auto;
}

.md-05__modal-trigger:checked ~ .md-05__backdrop .md-05__dialog {
  transform: scale(1) translateY(0);
  opacity: 1;
}

.md-05__dialog-icon {
  text-align: center;
  padding-top: 28px;
  font-size: 2rem;
}

.md-05__dialog-head {
  padding: 24px 24px 12px;
  font-size: 1.375rem;
  font-weight: 700;
  color: var(--ink);
}

.md-05__dialog-head--center {
  text-align: center;
}

.md-05__dialog-body {
  padding: 0 24px 20px;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--ink2);
}

.md-05__dialog-body--center {
  text-align: center;
}

.md-05__dialog-actions {
  display: flex;
  gap: 8px;
  justify-content: flex-end;
  padding: 8px 24px 24px;
}

.md-05__dialog-btn {
  height: 40px;
  padding: 0 24px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  transition: background .15s;
}

.md-05__dialog-btn--text {
  background: transparent;
  color: var(--primary);
}

.md-05__dialog-btn--text:hover {
  background: rgba(69,39,160,.08);
}

.md-05__dialog-btn--filled {
  background: var(--primary);
  color: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,.2);
}

.md-05__dialog-btn--filled:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,.25);
}

.md-05__dialog-btn--err {
  background: var(--error);
  color: #fff;
}

.md-05__dialog-btn--close {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background: transparent;
  cursor: pointer;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ink2);
}

.md-05__dialog-btn--close:hover {
  background: rgba(0,0,0,.06);
}
/* close via label targeting the same checkbox */

.md-05__close-label {
  cursor: pointer;
}
/* ── BOTTOM SHEET ── */

.md-05__sheet-trigger {
  display: none;
}

.md-05__sheet-backdrop {
  position: fixed;
  inset: 0;
  z-index: 100;
  background: rgba(0,0,0,0);
  pointer-events: none;
  transition: background .25s;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}

.md-05__sheet-trigger:checked ~ .md-05__sheet-backdrop {
  background: rgba(0,0,0,.5);
  pointer-events: auto;
}

.md-05__sheet {
  background: var(--surface);
  border-radius: 28px 28px 0 0;
  width: 100%;
  max-width: 640px;
  padding: 0 0 40px;
  transform: translateY(100%);
  transition: transform .35s cubic-bezier(.4,0,.2,1);
  box-shadow: 0 -8px 24px rgba(0,0,0,.12);
}

.md-05__sheet-trigger:checked ~ .md-05__sheet-backdrop .md-05__sheet {
  transform: translateY(0);
}

.md-05__sheet-handle {
  width: 40px;
  height: 4px;
  background: var(--divider);
  border-radius: 2px;
  margin: 12px auto 20px;
}

.md-05__sheet-title {
  font-size: 1.1rem;
  font-weight: 700;
  padding: 0 24px 16px;
  color: var(--ink);
}

.md-05__sheet-option {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 24px;
  cursor: pointer;
  font-size: .9rem;
  color: var(--ink);
  transition: background .15s;
}

.md-05__sheet-option:hover {
  background: rgba(0,0,0,.04);
}

.md-05__sheet-option-icon {
  font-size: 1.3rem;
  width: 32px;
  text-align: center;
}
/* ── SNACKBAR ── */

.md-05__snack-trigger {
  display: none;
}

.md-05__snackbar {
  position: fixed;
  bottom: 32px;
  left: 50%;
  transform: translateX(-50%) translateY(120px);
  background: #323232;
  color: #fff;
  border-radius: 4px;
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 24px;
  box-shadow: 0 3px 10px rgba(0,0,0,.3);
  font-size: .875rem;
  min-width: 300px;
  max-width: 560px;
  transition: transform .35s cubic-bezier(.4,0,.2,1);
  z-index: 200;
  pointer-events: none;
}

.md-05__snack-trigger:checked ~ .md-05__snackbar {
  transform: translateX(-50%) translateY(0);
  pointer-events: auto;
}

.md-05__snack-action {
  background: transparent;
  border: none;
  color: #bb86fc;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  cursor: pointer;
  white-space: nowrap;
  padding: 0;
}
/* ── PREVIEW PANEL ── */

.md-05__preview {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(260px,1fr));
  gap: 20px;
  margin-top: 40px;
}

.md-05__preview-card {
  background: var(--surface2);
  border-radius: 20px;
  padding: 24px;
  border: 1px solid var(--divider);
}

.md-05__preview-label {
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--primary-l);
  margin-bottom: 12px;
}

.md-05__dialog--inline {
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0,0,0,.12);
  transform: none;
  opacity: 1;
  max-height: none;
  position: static;
  pointer-events: none;
}

@media (prefers-reduced-motion: reduce) {
  .md-05 * {
    transition: none!important;
  }
}
```

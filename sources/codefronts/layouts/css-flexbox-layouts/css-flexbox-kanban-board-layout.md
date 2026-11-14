---
source: "codefronts"
url: "https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-kanban-board-layout/"
title: "CSS Flexbox Kanban Board Layout"
section: "layouts"
category: "css-flexbox-layouts"
category_name: "CSS Flexbox Layouts"
description: "A dark-themed Kanban board with five status columns, draggable task cards, color-coded priority badges, avatar assignments, and a progress bar — built with a…"
has_js: "true"
---

Here's a working CSS Flexbox Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Kanban Board Layout
Source: https://codefronts.com/layouts/css-flexbox-layouts/css-flexbox-kanban-board-layout/

A dark-themed Kanban board with five status columns, draggable task cards, color-coded priority badges, avatar assignments, and a progress bar — built with a horizontal flex shell.
## HTML
```html
<div class="fl-15">

  <!-- Top Bar -->
  <div class="fl-15__topbar">
    <div class="fl-15__logo">
      <div class="fl-15__logo-icon">
        <svg viewBox="0 0 16 16"><rect x="1" y="1" width="6" height="8" rx="1.5"/><rect x="9" y="1" width="6" height="5" rx="1.5"/><rect x="9" y="8" width="6" height="7" rx="1.5"/><rect x="1" y="11" width="6" height="4" rx="1.5"/></svg>
      </div>
      <span class="fl-15__logo-name">Flex<span>Board</span></span>
    </div>
    <span class="fl-15__project">Sprint 14 · Q3 2025</span>
    <div class="fl-15__topbar-actions">
      <div class="fl-15__avatar fl-15__avatar--a">AJ</div>
      <div class="fl-15__avatar fl-15__avatar--b">SK</div>
      <div class="fl-15__avatar fl-15__avatar--c">MR</div>
      <button class="fl-15__btn fl-15__btn--ghost">Filter</button>
      <button class="fl-15__btn fl-15__btn--primary">+ Add Task</button>
    </div>
  </div>

  <!-- Board -->
  <div class="fl-15__board" id="fl-15-board">

    <!-- Backlog -->
    <div class="fl-15__col fl-15__col--backlog">
      <div class="fl-15__col-head">
        <div class="fl-15__col-label">
          <span class="fl-15__col-dot"></span> Backlog
        </div>
        <span class="fl-15__col-count">3</span>
      </div>
      <div class="fl-15__cards">
        <div class="fl-15__card" draggable="true">
          <span class="fl-15__card-tag fl-15__card-tag--ux">UX</span>
          <div class="fl-15__card-title">Redesign onboarding flow for new users</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-108</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--low">● Low</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--c">MR</div>
            </div>
          </div>
        </div>
        <div class="fl-15__card">
          <span class="fl-15__card-tag fl-15__card-tag--be">Backend</span>
          <div class="fl-15__card-title">Add Redis caching for API responses</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-109</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--medium">● Med</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--b">SK</div>
            </div>
          </div>
        </div>
        <div class="fl-15__card">
          <span class="fl-15__card-tag fl-15__card-tag--fe">Frontend</span>
          <div class="fl-15__card-title">Implement dark mode toggle</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-110</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--low">● Low</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--a">AJ</div>
            </div>
          </div>
        </div>
      </div>
      <div class="fl-15__col-add">
        <div class="fl-15__col-add-icon">+</div>
        Add card
      </div>
    </div>

    <!-- To Do -->
    <div class="fl-15__col fl-15__col--todo">
      <div class="fl-15__col-head">
        <div class="fl-15__col-label">
          <span class="fl-15__col-dot"></span> To Do
        </div>
        <span class="fl-15__col-count">3</span>
      </div>
      <div class="fl-15__cards">
        <div class="fl-15__card fl-15__card--highlighted">
          <span class="fl-15__card-tag fl-15__card-tag--fe">Frontend</span>
          <div class="fl-15__card-title">Build flexbox grid component library</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-101</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--high">● High</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--a">AJ</div>
            </div>
          </div>
        </div>
        <div class="fl-15__card">
          <span class="fl-15__card-tag fl-15__card-tag--be">Backend</span>
          <div class="fl-15__card-title">Migrate auth service to JWT tokens</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-102</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--high">● High</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--b">SK</div>
            </div>
          </div>
        </div>
        <div class="fl-15__card">
          <span class="fl-15__card-tag fl-15__card-tag--qa">QA</span>
          <div class="fl-15__card-title">Write E2E tests for checkout flow</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-103</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--medium">● Med</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--c">MR</div>
            </div>
          </div>
        </div>
      </div>
      <div class="fl-15__col-add">
        <div class="fl-15__col-add-icon">+</div>
        Add card
      </div>
    </div>

    <!-- In Progress -->
    <div class="fl-15__col fl-15__col--doing">
      <div class="fl-15__col-head">
        <div class="fl-15__col-label">
          <span class="fl-15__col-dot"></span> In Progress
        </div>
        <span class="fl-15__col-count">3</span>
      </div>
      <div class="fl-15__cards">
        <div class="fl-15__card">
          <span class="fl-15__card-tag fl-15__card-tag--fe">Frontend</span>
          <div class="fl-15__card-title">Implement responsive nav with flex</div>
          <div class="fl-15__card-progress">
            <div class="fl-15__card-progress-fill" style="width: 65%"></div>
          </div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-104</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--high">● High</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--a">AJ</div>
            </div>
          </div>
        </div>
        <div class="fl-15__card">
          <span class="fl-15__card-tag fl-15__card-tag--be">Backend</span>
          <div class="fl-15__card-title">Set up CI/CD pipeline for staging</div>
          <div class="fl-15__card-progress">
            <div class="fl-15__card-progress-fill" style="width: 30%"></div>
          </div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-105</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--medium">● Med</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--b">SK</div>
            </div>
          </div>
        </div>
        <div class="fl-15__card">
          <span class="fl-15__card-tag fl-15__card-tag--bug">Bug</span>
          <div class="fl-15__card-title">Fix overflow scroll on mobile sidebar</div>
          <div class="fl-15__card-progress">
            <div class="fl-15__card-progress-fill" style="width: 80%"></div>
          </div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-106</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--high">● High</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--c">MR</div>
            </div>
          </div>
        </div>
      </div>
      <div class="fl-15__col-add">
        <div class="fl-15__col-add-icon">+</div>
        Add card
      </div>
    </div>

    <!-- Review -->
    <div class="fl-15__col fl-15__col--review">
      <div class="fl-15__col-head">
        <div class="fl-15__col-label">
          <span class="fl-15__col-dot"></span> Review
        </div>
        <span class="fl-15__col-count">2</span>
      </div>
      <div class="fl-15__cards">
        <div class="fl-15__card">
          <span class="fl-15__card-tag fl-15__card-tag--fe">Frontend</span>
          <div class="fl-15__card-title">Pricing table with flex equal heights</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-097</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--medium">● Med</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--a">AJ</div>
            </div>
          </div>
        </div>
        <div class="fl-15__card">
          <span class="fl-15__card-tag fl-15__card-tag--qa">QA</span>
          <div class="fl-15__card-title">Cross-browser accessibility audit</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-098</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--low">● Low</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--b">SK</div>
            </div>
          </div>
        </div>
      </div>
      <div class="fl-15__col-add">
        <div class="fl-15__col-add-icon">+</div>
        Add card
      </div>
    </div>

    <!-- Done -->
    <div class="fl-15__col fl-15__col--done">
      <div class="fl-15__col-head">
        <div class="fl-15__col-label">
          <span class="fl-15__col-dot"></span> Done
        </div>
        <span class="fl-15__col-count">2</span>
      </div>
      <div class="fl-15__cards">
        <div class="fl-15__card" style="opacity:0.6">
          <span class="fl-15__card-tag fl-15__card-tag--fe">Frontend</span>
          <div class="fl-15__card-title">Holy grail layout with flex columns</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-090</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--low">✓ Done</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--c">MR</div>
            </div>
          </div>
        </div>
        <div class="fl-15__card" style="opacity:0.6">
          <span class="fl-15__card-tag fl-15__card-tag--be">Backend</span>
          <div class="fl-15__card-title">Database schema migrations v2.1</div>
          <div class="fl-15__card-meta">
            <span class="fl-15__card-id">#FL-091</span>
            <div class="fl-15__card-foot">
              <span class="fl-15__card-prio fl-15__card-prio--low">✓ Done</span>
              <div class="fl-15__card-avatar fl-15__card-avatar--a">AJ</div>
            </div>
          </div>
        </div>
      </div>
      <div class="fl-15__col-add">
        <div class="fl-15__col-add-icon">+</div>
        Add card
      </div>
    </div>

    <!-- Add Column -->
    <div class="fl-15__col fl-15__col--add">
      <div class="fl-15__col-add-label">
        <span>+</span>
        Add column
      </div>
    </div>

  </div>
</div>

<script>
(function() {
  const board = document.getElementById('fl-15-board');
  if (!board) return;

  let dragCard = null;
  let dragSource = null;

  board.querySelectorAll('.fl-15__card[draggable]').forEach(card => {
    // Enable drag on all cards
    card.setAttribute('draggable', 'true');
  });
  // Enable drag on ALL cards
  board.querySelectorAll('.fl-15__card').forEach(card => {
    card.setAttribute('draggable', 'true');

    card.addEventListener('dragstart', e => {
      dragCard = card;
      dragSource = card.closest('.fl-15__cards');
      setTimeout(() => card.classList.add('is-dragging'), 0);
      e.dataTransfer.effectAllowed = 'move';
    });
    card.addEventListener('dragend', () => {
      card.classList.remove('is-dragging');
      board.querySelectorAll('.fl-15__cards').forEach(z => z.classList.remove('fl-15__drop-zone'));
      dragCard = null;
    });
  });

  board.querySelectorAll('.fl-15__cards').forEach(zone => {
    zone.addEventListener('dragover', e => {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
    });
    zone.addEventListener('drop', e => {
      e.preventDefault();
      if (dragCard && zone !== dragSource) {
        zone.appendChild(dragCard);
        // Update counts
        updateCounts();
      }
    });
  });

  function updateCounts() {
    board.querySelectorAll('.fl-15__col').forEach(col => {
      const count = col.querySelectorAll('.fl-15__card').length;
      const badge = col.querySelector('.fl-15__col-count');
      if (badge) badge.textContent = count;
    });
  }

  // Add card buttons — append a placeholder card
  board.querySelectorAll('.fl-15__col-add').forEach(btn => {
    btn.addEventListener('click', () => {
      const col = btn.closest('.fl-15__col');
      const cardsZone = col.querySelector('.fl-15__cards');
      if (!cardsZone) return;
      const card = document.createElement('div');
      card.className = 'fl-15__card';
      card.setAttribute('draggable', 'true');
      card.innerHTML = `
        <span class="fl-15__card-tag fl-15__card-tag--fe">Frontend</span>
        <div class="fl-15__card-title" contenteditable="true" style="outline:none;border-bottom:1px dashed #6b6b80">New task…</div>
        <div class="fl-15__card-meta">
          <span class="fl-15__card-id">#FL-NEW</span>
        </div>`;
      cardsZone.appendChild(card);
      card.querySelector('[contenteditable]').focus();
      updateCounts();
      // Re-attach drag events
      card.addEventListener('dragstart', e => {
        dragCard = card;
        dragSource = card.closest('.fl-15__cards');
        setTimeout(() => card.classList.add('is-dragging'), 0);
        e.dataTransfer.effectAllowed = 'move';
      });
      card.addEventListener('dragend', () => {
        card.classList.remove('is-dragging');
        dragCard = null;
      });
    });
  });
})();
</script>
```
## CSS
```css
.fl-15,
.fl-15 *,
.fl-15 *::before,
.fl-15 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.fl-15 ::selection {
  background: #7c3aed;
  color: #fff;
}

.fl-15 {
  --bg: #0f0f13;
  --panel: #1a1a24;
  --col: #1e1e2a;
  --col-hover: #252533;
  --border: #2e2e40;
  --accent: #7c3aed;
  --accent2: #06b6d4;
  --accent3: #f59e0b;
  --accent4: #10b981;
  --danger: #ef4444;
  --ink: #e8e8f0;
  --muted: #6b6b80;
  --card-bg: #252535;
  --card-hover: #2d2d40;
  font-family: 'DM Sans', sans-serif;
  background: var(--bg);
  min-height: 520px;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--border);
  display: flex;
  flex-direction: column;
}
/* ── Top Bar ── */

.fl-15__topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  background: var(--panel);
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
  gap: 12px;
}

.fl-15__logo {
  display: flex;
  align-items: center;
  gap: 8px;
}

.fl-15__logo-icon {
  width: 28px;
  height: 28px;
  background: var(--accent);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fl-15__logo-icon svg {
  width: 16px;
  height: 16px;
  fill: #fff;
}

.fl-15__logo-name {
  font-family: 'Space Mono', monospace;
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--ink);
  letter-spacing: -0.02em;
}

.fl-15__logo-name span {
  color: var(--accent);
}

.fl-15__project {
  font-size: 0.75rem;
  color: var(--muted);
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.fl-15__topbar-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: auto;
}

.fl-15__avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  font-size: 0.65rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  flex-shrink: 0;
}

.fl-15__avatar--a {
  background: #7c3aed;
}

.fl-15__avatar--b {
  background: #06b6d4;
}

.fl-15__avatar--c {
  background: #f59e0b;
}

.fl-15__btn {
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  font-family: 'DM Sans', sans-serif;
  transition: opacity 0.2s;
}

.fl-15__btn:hover {
  opacity: 0.85;
}

.fl-15__btn--primary {
  background: var(--accent);
  color: #fff;
}

.fl-15__btn--ghost {
  background: transparent;
  color: var(--muted);
  border: 1px solid var(--border);
}
/* ── Board ── */

.fl-15__board {
  display: flex;
  flex: 1;
  gap: 10px;
  padding: 14px;
  overflow-x: auto;
  align-items: flex-start;
  min-height: 0;
  position: relative;
}

.fl-15__board::-webkit-scrollbar {
  height: 6px;
}

.fl-15__board::-webkit-scrollbar-track {
  background: transparent;
}

.fl-15__board::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 3px;
}

.fl-15__board::-webkit-scrollbar-thumb:hover {
  background: var(--accent);
}
/* ── Column ── */

.fl-15__col {
  display: flex;
  flex-direction: column;
  flex: 0 0 192px;
  min-width: 0;
  background: var(--col);
  border-radius: 10px;
  border: 1px solid var(--border);
  overflow: hidden;
}

.fl-15__col-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 12px;
  flex-shrink: 0;
  border-bottom: 2px solid transparent;
}

.fl-15__col--backlog .fl-15__col-head {
  border-color: var(--muted);
}

.fl-15__col--todo .fl-15__col-head {
  border-color: var(--accent2);
}

.fl-15__col--doing .fl-15__col-head {
  border-color: var(--accent);
}

.fl-15__col--review .fl-15__col-head {
  border-color: var(--accent3);
}

.fl-15__col--done .fl-15__col-head {
  border-color: var(--accent4);
}

.fl-15__col-label {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.fl-15__col--backlog .fl-15__col-label {
  color: var(--muted);
}

.fl-15__col--todo .fl-15__col-label {
  color: var(--accent2);
}

.fl-15__col--doing .fl-15__col-label {
  color: var(--accent);
}

.fl-15__col--review .fl-15__col-label {
  color: var(--accent3);
}

.fl-15__col--done .fl-15__col-label {
  color: var(--accent4);
}

.fl-15__col-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.fl-15__col--backlog .fl-15__col-dot {
  background: var(--muted);
}

.fl-15__col--todo .fl-15__col-dot {
  background: var(--accent2);
}

.fl-15__col--doing .fl-15__col-dot {
  background: var(--accent);
}

.fl-15__col--review .fl-15__col-dot {
  background: var(--accent3);
}

.fl-15__col--done .fl-15__col-dot {
  background: var(--accent4);
}

.fl-15__col-count {
  font-size: 0.68rem;
  background: var(--border);
  color: var(--muted);
  border-radius: 20px;
  padding: 1px 7px;
  font-weight: 700;
}
/* ── Cards area ── */

.fl-15__cards {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 10px;
  flex: 1;
  overflow-y: auto;
  min-height: 80px;
  max-height: 360px;
}

.fl-15__cards::-webkit-scrollbar {
  width: 3px;
}

.fl-15__cards::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 2px;
}
/* ── Card ── */

.fl-15__card {
  background: var(--card-bg);
  border-radius: 7px;
  border: 1px solid var(--border);
  padding: 10px;
  cursor: pointer;
  transition: background 0.15s, border-color 0.15s, transform 0.15s;
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.fl-15__card:hover {
  background: var(--card-hover);
  border-color: #3a3a50;
  transform: translateY(-1px);
}

.fl-15__card--highlighted {
  border-color: var(--accent);
}

.fl-15__card-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.62rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 2px 7px;
  border-radius: 4px;
  align-self: flex-start;
}

.fl-15__card-tag--fe {
  background: rgba(124,58,237,0.2);
  color: #a78bfa;
}

.fl-15__card-tag--be {
  background: rgba(6,182,212,0.2);
  color: #67e8f9;
}

.fl-15__card-tag--bug {
  background: rgba(239,68,68,0.2);
  color: #fca5a5;
}

.fl-15__card-tag--ux {
  background: rgba(245,158,11,0.2);
  color: #fcd34d;
}

.fl-15__card-tag--qa {
  background: rgba(16,185,129,0.2);
  color: #6ee7b7;
}

.fl-15__card-title {
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--ink);
  line-height: 1.4;
}

.fl-15__card-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.fl-15__card-id {
  font-family: 'Space Mono', monospace;
  font-size: 0.6rem;
  color: var(--muted);
}

.fl-15__card-foot {
  display: flex;
  align-items: center;
  gap: 5px;
}

.fl-15__card-prio {
  font-size: 0.6rem;
  font-weight: 600;
}

.fl-15__card-prio--high {
  color: var(--danger);
}

.fl-15__card-prio--medium {
  color: var(--accent3);
}

.fl-15__card-prio--low {
  color: var(--accent4);
}

.fl-15__card-avatar {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  font-size: 0.5rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  margin-left: auto;
}

.fl-15__card-avatar--a {
  background: #7c3aed;
}

.fl-15__card-avatar--b {
  background: #06b6d4;
}

.fl-15__card-avatar--c {
  background: #f59e0b;
}
/* ── Progress bar on doing cards ── */

.fl-15__card-progress {
  height: 3px;
  background: var(--border);
  border-radius: 2px;
  overflow: hidden;
}

.fl-15__card-progress-fill {
  height: 100%;
  border-radius: 2px;
  background: var(--accent);
  animation: fl-15-pulse 2.5s ease-in-out infinite;
}

@keyframes fl-15-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.6;
  }
}
/* ── Add card button ── */

.fl-15__col-add {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  font-size: 0.72rem;
  color: var(--muted);
  cursor: pointer;
  border-top: 1px solid var(--border);
  flex-shrink: 0;
  transition: color 0.15s, background 0.15s;
}

.fl-15__col-add:hover {
  color: var(--ink);
  background: var(--col-hover);
}

.fl-15__col-add-icon {
  width: 16px;
  height: 16px;
  border: 1.5px solid currentColor;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  line-height: 1;
}
/* ── Add column ── */

.fl-15__col--add {
  flex: 0 0 140px;
  border: 1.5px dashed var(--border);
  background: transparent;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: border-color 0.15s, background 0.15s;
  align-self: stretch;
  min-height: 120px;
}

.fl-15__col--add:hover {
  border-color: var(--accent);
  background: rgba(124,58,237,0.05);
}

.fl-15__col-add-label {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  color: var(--muted);
  font-size: 0.72rem;
  font-weight: 500;
}

.fl-15__col-add-label span {
  font-size: 1.2rem;
  line-height: 1;
}
/* ── Drag ghost (visual only) ── */

.fl-15__card.is-dragging {
  opacity: 0.4;
  transform: rotate(2deg) scale(0.97);
}
/* ── Responsive: narrow viewports ── */

@media (max-width: 520px) {
  .fl-15__project {
    display: none;
  }

  .fl-15__topbar {
    padding: 10px 14px;
    gap: 8px;
  }

  .fl-15__topbar-actions {
    gap: 6px;
  }

  .fl-15__btn--ghost {
    display: none;
  }

  .fl-15__avatar {
    width: 24px;
    height: 24px;
    font-size: 0.6rem;
  }
}

@media (max-width: 380px) {
  .fl-15__avatar {
    display: none;
  }

  .fl-15__avatar:last-of-type {
    display: flex;
  }
}
/* ── Reduced motion ── */

@media (prefers-reduced-motion: reduce) {
  .fl-15__card {
    transition: none;
  }

  .fl-15__card-progress-fill {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const board = document.getElementById('fl-15-board');
  if (!board) return;

  let dragCard = null;
  let dragSource = null;

  board.querySelectorAll('.fl-15__card[draggable]').forEach(card => {
    // Enable drag on all cards
    card.setAttribute('draggable', 'true');
  });
  // Enable drag on ALL cards
  board.querySelectorAll('.fl-15__card').forEach(card => {
    card.setAttribute('draggable', 'true');

    card.addEventListener('dragstart', e => {
      dragCard = card;
      dragSource = card.closest('.fl-15__cards');
      setTimeout(() => card.classList.add('is-dragging'), 0);
      e.dataTransfer.effectAllowed = 'move';
    });
    card.addEventListener('dragend', () => {
      card.classList.remove('is-dragging');
      board.querySelectorAll('.fl-15__cards').forEach(z => z.classList.remove('fl-15__drop-zone'));
      dragCard = null;
    });
  });

  board.querySelectorAll('.fl-15__cards').forEach(zone => {
    zone.addEventListener('dragover', e => {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
    });
    zone.addEventListener('drop', e => {
      e.preventDefault();
      if (dragCard && zone !== dragSource) {
        zone.appendChild(dragCard);
        // Update counts
        updateCounts();
      }
    });
  });

  function updateCounts() {
    board.querySelectorAll('.fl-15__col').forEach(col => {
      const count = col.querySelectorAll('.fl-15__card').length;
      const badge = col.querySelector('.fl-15__col-count');
      if (badge) badge.textContent = count;
    });
  }

  // Add card buttons — append a placeholder card
  board.querySelectorAll('.fl-15__col-add').forEach(btn => {
    btn.addEventListener('click', () => {
      const col = btn.closest('.fl-15__col');
      const cardsZone = col.querySelector('.fl-15__cards');
      if (!cardsZone) return;
      const card = document.createElement('div');
      card.className = 'fl-15__card';
      card.setAttribute('draggable', 'true');
      card.innerHTML = `
        <span class="fl-15__card-tag fl-15__card-tag--fe">Frontend</span>
        <div class="fl-15__card-title" contenteditable="true" style="outline:none;border-bottom:1px dashed #6b6b80">New task…</div>
        <div class="fl-15__card-meta">
          <span class="fl-15__card-id">#FL-NEW</span>
        </div>`;
      cardsZone.appendChild(card);
      card.querySelector('[contenteditable]').focus();
      updateCounts();
      // Re-attach drag events
      card.addEventListener('dragstart', e => {
        dragCard = card;
        dragSource = card.closest('.fl-15__cards');
        setTimeout(() => card.classList.add('is-dragging'), 0);
        e.dataTransfer.effectAllowed = 'move';
      });
      card.addEventListener('dragend', () => {
        card.classList.remove('is-dragging');
        dragCard = null;
      });
    });
  });
})();
```

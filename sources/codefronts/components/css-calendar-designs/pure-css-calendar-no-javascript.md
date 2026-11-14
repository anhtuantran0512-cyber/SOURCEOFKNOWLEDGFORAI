---
source: "codefronts"
url: "https://codefronts.com/components/css-calendar-designs/pure-css-calendar-no-javascript/"
title: "Pure CSS Calendar (No JavaScript)"
section: "components"
category: "css-calendar-designs"
category_name: "CSS Calendars"
description: "A Japandi/wabi-sabi calendar driven entirely by the checkbox/radio hack."
has_js: "false"
---

Here's a working CSS Calendar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Calendar (No JavaScript)
Source: https://codefronts.com/components/css-calendar-designs/pure-css-calendar-no-javascript/

A Japandi/wabi-sabi calendar driven entirely by the checkbox/radio hack. Hidden radio inputs switch months and select dates via :checked sibling rules with zero JavaScript. Cormorant + Noto Serif JP, kanji month marks, gold/red event dots on warm parchment.
## HTML
```html
<!-- ALL radio inputs must live OUTSIDE .cal04__frame so :checked siblings can target inside -->
<div class="cal04">

  <!-- Month selector radios (outside frame so ~ combinator works) -->
  <input type="radio" class="cal04__radio" name="cal04-month" id="cal04-m1" checked>
  <input type="radio" class="cal04__radio" name="cal04-month" id="cal04-m2">
  <input type="radio" class="cal04__radio" name="cal04-month" id="cal04-m3">

  <!-- Date selection radios for June -->
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d8">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d9">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d10">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d11">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d12">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d13">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d14">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d15">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d16">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d17">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d18">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d19">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d20">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d21">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d22">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d23">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d24">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d25">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d26">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d27">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d28">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d29">
  <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d30">

  <div class="cal04__frame">

    <!-- Month tabs -->
    <div class="cal04__header">
      <div class="cal04__tab-labels">
        <label class="cal04__tab-label" for="cal04-m1">June</label>
        <label class="cal04__tab-label" for="cal04-m2">July</label>
        <label class="cal04__tab-label" for="cal04-m3">August</label>
      </div>
    </div>

    <!-- Month panels -->
    <div class="cal04__months">

      <!-- ── June ── -->
      <div class="cal04__month cal04__month--1">
        <div class="cal04__month-head">
          <div class="cal04__month-name">June</div>
          <div class="cal04__month-year">2026</div>
          <div class="cal04__month-kanji">六月</div>
        </div>

        <div class="cal04__dow">
          <div class="cal04__dow-cell">日 Sun</div>
          <div class="cal04__dow-cell">月 Mon</div>
          <div class="cal04__dow-cell">火 Tue</div>
          <div class="cal04__dow-cell">水 Wed</div>
          <div class="cal04__dow-cell">木 Thu</div>
          <div class="cal04__dow-cell">金 Fri</div>
          <div class="cal04__dow-cell">土 Sat</div>
        </div>

        <div class="cal04__grid">
          <!-- May overflow -->
          <label class="cal04__date-label other sun"><span class="cal04__date-num">25</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">26</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">27</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">28</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">29</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">30</span></label>
          <label class="cal04__date-label other sat"><span class="cal04__date-num">31</span></label>
          <!-- June 1–7 -->
          <label class="cal04__date-label sun" for="cal04-d8"><span class="cal04__date-num">1</span></label>
          <label class="cal04__date-label" for="cal04-d9"><span class="cal04__date-num">2</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--red"></span></div></label>
          <label class="cal04__date-label" for="cal04-d10"><span class="cal04__date-num">3</span></label>
          <label class="cal04__date-label" for="cal04-d11"><span class="cal04__date-num">4</span></label>
          <label class="cal04__date-label" for="cal04-d12"><span class="cal04__date-num">5</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--gold"></span></div></label>
          <label class="cal04__date-label" for="cal04-d13"><span class="cal04__date-num">6</span></label>
          <label class="cal04__date-label sat" for="cal04-d14"><span class="cal04__date-num">7</span></label>
          <!-- June 8–14: today = 8 -->
          <input type="radio" class="cal04__date-radio" name="cal04-date" id="cal04-d8" checked>
          <label class="cal04__date-label today sun" for="cal04-d8"><span class="cal04__date-num">8</span></label>
          <label class="cal04__date-label" for="cal04-d9"><span class="cal04__date-num">9</span></label>
          <label class="cal04__date-label" for="cal04-d10"><span class="cal04__date-num">10</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--red"></span><span class="cal04__dot"></span></div></label>
          <label class="cal04__date-label" for="cal04-d11"><span class="cal04__date-num">11</span></label>
          <label class="cal04__date-label" for="cal04-d12"><span class="cal04__date-num">12</span></label>
          <label class="cal04__date-label" for="cal04-d13"><span class="cal04__date-num">13</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--gold"></span></div></label>
          <label class="cal04__date-label sat" for="cal04-d14"><span class="cal04__date-num">14</span></label>
          <!-- June 15–21 -->
          <label class="cal04__date-label sun" for="cal04-d15"><span class="cal04__date-num">15</span></label>
          <label class="cal04__date-label" for="cal04-d16"><span class="cal04__date-num">16</span></label>
          <label class="cal04__date-label" for="cal04-d17"><span class="cal04__date-num">17</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--red"></span><span class="cal04__dot cal04__dot--red"></span></div></label>
          <label class="cal04__date-label" for="cal04-d18"><span class="cal04__date-num">18</span></label>
          <label class="cal04__date-label" for="cal04-d19"><span class="cal04__date-num">19</span></label>
          <label class="cal04__date-label" for="cal04-d20"><span class="cal04__date-num">20</span></label>
          <label class="cal04__date-label sat" for="cal04-d21"><span class="cal04__date-num">21</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--gold"></span></div></label>
          <!-- June 22–28 -->
          <label class="cal04__date-label sun" for="cal04-d22"><span class="cal04__date-num">22</span></label>
          <label class="cal04__date-label" for="cal04-d23"><span class="cal04__date-num">23</span></label>
          <label class="cal04__date-label" for="cal04-d24"><span class="cal04__date-num">24</span><div class="cal04__dots"><span class="cal04__dot"></span></div></label>
          <label class="cal04__date-label" for="cal04-d25"><span class="cal04__date-num">25</span></label>
          <label class="cal04__date-label" for="cal04-d26"><span class="cal04__date-num">26</span></label>
          <label class="cal04__date-label" for="cal04-d27"><span class="cal04__date-num">27</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--red"></span></div></label>
          <label class="cal04__date-label sat" for="cal04-d28"><span class="cal04__date-num">28</span></label>
          <!-- June 29–30 + July overflow -->
          <label class="cal04__date-label sun" for="cal04-d29"><span class="cal04__date-num">29</span></label>
          <label class="cal04__date-label" for="cal04-d30"><span class="cal04__date-num">30</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">1</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">2</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">3</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">4</span></label>
          <label class="cal04__date-label other sat"><span class="cal04__date-num">5</span></label>
        </div>
      </div>

      <!-- ── July ── -->
      <div class="cal04__month cal04__month--2">
        <div class="cal04__month-head">
          <div class="cal04__month-name">July</div>
          <div class="cal04__month-year">2026</div>
          <div class="cal04__month-kanji">七月</div>
        </div>
        <div class="cal04__dow">
          <div class="cal04__dow-cell">日</div><div class="cal04__dow-cell">月</div><div class="cal04__dow-cell">火</div>
          <div class="cal04__dow-cell">水</div><div class="cal04__dow-cell">木</div><div class="cal04__dow-cell">金</div><div class="cal04__dow-cell">土</div>
        </div>
        <div class="cal04__grid">
          <label class="cal04__date-label other sun"><span class="cal04__date-num">29</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">30</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">1</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">2</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">3</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--gold"></span></div></label>
          <label class="cal04__date-label"><span class="cal04__date-num">4</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--red"></span></div></label>
          <label class="cal04__date-label sat"><span class="cal04__date-num">5</span></label>
          <label class="cal04__date-label sun"><span class="cal04__date-num">6</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">7</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">8</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">9</span><div class="cal04__dots"><span class="cal04__dot"></span></div></label>
          <label class="cal04__date-label"><span class="cal04__date-num">10</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">11</span></label>
          <label class="cal04__date-label sat"><span class="cal04__date-num">12</span></label>
          <label class="cal04__date-label sun"><span class="cal04__date-num">13</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">14</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">15</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--red"></span><span class="cal04__dot cal04__dot--gold"></span></div></label>
          <label class="cal04__date-label"><span class="cal04__date-num">16</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">17</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">18</span></label>
          <label class="cal04__date-label sat"><span class="cal04__date-num">19</span></label>
          <label class="cal04__date-label sun"><span class="cal04__date-num">20</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">21</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">22</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">23</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">24</span><div class="cal04__dots"><span class="cal04__dot"></span></div></label>
          <label class="cal04__date-label"><span class="cal04__date-num">25</span></label>
          <label class="cal04__date-label sat"><span class="cal04__date-num">26</span></label>
          <label class="cal04__date-label sun"><span class="cal04__date-num">27</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">28</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">29</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">30</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">31</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">1</span></label>
          <label class="cal04__date-label other sat"><span class="cal04__date-num">2</span></label>
        </div>
      </div>

      <!-- ── August ── -->
      <div class="cal04__month cal04__month--3">
        <div class="cal04__month-head">
          <div class="cal04__month-name">August</div>
          <div class="cal04__month-year">2026</div>
          <div class="cal04__month-kanji">八月</div>
        </div>
        <div class="cal04__dow">
          <div class="cal04__dow-cell">日</div><div class="cal04__dow-cell">月</div><div class="cal04__dow-cell">火</div>
          <div class="cal04__dow-cell">水</div><div class="cal04__dow-cell">木</div><div class="cal04__dow-cell">金</div><div class="cal04__dow-cell">土</div>
        </div>
        <div class="cal04__grid">
          <label class="cal04__date-label other sun"><span class="cal04__date-num">27</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">28</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">29</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">30</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">31</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">1</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--red"></span></div></label>
          <label class="cal04__date-label sat"><span class="cal04__date-num">2</span></label>
          <label class="cal04__date-label sun"><span class="cal04__date-num">3</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">4</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">5</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">6</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--gold"></span></div></label>
          <label class="cal04__date-label"><span class="cal04__date-num">7</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">8</span></label>
          <label class="cal04__date-label sat"><span class="cal04__date-num">9</span></label>
          <label class="cal04__date-label sun"><span class="cal04__date-num">10</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">11</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">12</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">13</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">14</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">15</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--red"></span><span class="cal04__dot"></span></div></label>
          <label class="cal04__date-label sat"><span class="cal04__date-num">16</span></label>
          <label class="cal04__date-label sun"><span class="cal04__date-num">17</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">18</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">19</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">20</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">21</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">22</span></label>
          <label class="cal04__date-label sat"><span class="cal04__date-num">23</span></label>
          <label class="cal04__date-label sun"><span class="cal04__date-num">24</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">25</span><div class="cal04__dots"><span class="cal04__dot cal04__dot--gold"></span><span class="cal04__dot cal04__dot--red"></span></div></label>
          <label class="cal04__date-label"><span class="cal04__date-num">26</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">27</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">28</span></label>
          <label class="cal04__date-label"><span class="cal04__date-num">29</span></label>
          <label class="cal04__date-label sat"><span class="cal04__date-num">30</span></label>
          <label class="cal04__date-label sun"><span class="cal04__date-num">31</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">1</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">2</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">3</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">4</span></label>
          <label class="cal04__date-label other sat"><span class="cal04__date-num">5</span></label>
          <label class="cal04__date-label other sun"><span class="cal04__date-num">6</span></label>
          <label class="cal04__date-label other"><span class="cal04__date-num">7</span></label>
        </div>
      </div>

    </div><!-- /months -->

    <!-- Footer -->
    <div class="cal04__footer">
      <div class="cal04__footer-note">純CSS · No JavaScript · 2026</div>
      <div class="cal04__legend">
        <div class="cal04__legend-item">
          <span class="cal04__legend-dot" style="background:#b5413a"></span> Event
        </div>
        <div class="cal04__legend-item">
          <span class="cal04__legend-dot" style="background:#c9954a"></span> Holiday
        </div>
      </div>
    </div>

  </div><!-- /frame -->
</div><!-- /cal04 -->
```
## CSS
```css
/* ── Reset scoped ── */

.cal04,
.cal04 *,
.cal04 *::before,
.cal04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cal04 ::selection {
  background: #b5a99a;
  color: #fff;
}
/* ── CSS-only toggle mechanism: hidden radio inputs ── */

.cal04__radio {
  display: none;
}
/* ── Root variables ── */

.cal04 {
  --paper: #f7f3ed;
  --warm: #ede7dc;
  --ink: #2c2520;
  --ink2: #6b5f56;
  --ink3: #a89e95;
  --red: #b5413a;
  --gold: #c9954a;
  --line: rgba(44,37,32,0.1);
  --sel: rgba(181,65,58,0.08);
  --sel-bdr: rgba(181,65,58,0.4);
  font-family: 'Cormorant Garamond', serif;
  background: var(--paper);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  color: var(--ink);
  background-image: radial-gradient(ellipse 80% 50% at 50% 0%, rgba(201,149,74,0.06) 0%, transparent 70%);
}
/* ── Outer frame ── */

.cal04__frame {
  width: 100%;
  max-width: 640px;
  border: 1px solid rgba(44,37,32,0.14);
  background: #faf7f2;
  box-shadow: 0 2px 0 rgba(44,37,32,0.04), 0 12px 48px rgba(44,37,32,0.08);
}
/* ── Header: month navigation using :checked ── */

.cal04__header {
  display: flex;
  align-items: stretch;
  border-bottom: 1px solid var(--line);
}
/* Month tabs — driven by radio inputs */

.cal04__tab-labels {
  display: flex;
  flex: 1;
  overflow: hidden;
}

.cal04__tab-label {
  flex: 1;
  padding: 18px 6px 16px;
  text-align: center;
  cursor: pointer;
  font-size: 12px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--ink3);
  border-right: 1px solid var(--line);
  transition: background 0.25s, color 0.25s;
  user-select: none;
  position: relative;
}

.cal04__tab-label:last-child {
  border-right: none;
}

.cal04__tab-label:hover {
  background: var(--warm);
  color: var(--ink2);
}
/* Active tab: when corresponding radio is checked */

#cal04-m1:checked ~ .cal04__frame .cal04__tab-label[for="cal04-m1"],
#cal04-m2:checked ~ .cal04__frame .cal04__tab-label[for="cal04-m2"],
#cal04-m3:checked ~ .cal04__frame .cal04__tab-label[for="cal04-m3"] {
  color: var(--red);
  background: var(--sel);
  font-weight: 600;
}

#cal04-m1:checked ~ .cal04__frame .cal04__tab-label[for="cal04-m1"]::after,
#cal04-m2:checked ~ .cal04__frame .cal04__tab-label[for="cal04-m2"]::after,
#cal04-m3:checked ~ .cal04__frame .cal04__tab-label[for="cal04-m3"]::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--red);
}
/* ── Month panels: show/hide via :checked ── */

.cal04__months {
  position: relative;
}

.cal04__month {
  display: none;
  flex-direction: column;
}

#cal04-m1:checked ~ .cal04__frame .cal04__month--1,
#cal04-m2:checked ~ .cal04__frame .cal04__month--2,
#cal04-m3:checked ~ .cal04__frame .cal04__month--3 {
  display: flex;
  animation: cal04-reveal 0.35s cubic-bezier(0.22,1,0.36,1);
}

@keyframes cal04-reveal {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
/* ── Month title ── */

.cal04__month-head {
  padding: 32px 36px 20px;
  display: flex;
  align-items: baseline;
  gap: 14px;
  border-bottom: 1px solid var(--line);
}

.cal04__month-name {
  font-size: 52px;
  font-weight: 300;
  font-style: italic;
  line-height: 1;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.cal04__month-year {
  font-size: 14px;
  letter-spacing: 0.2em;
  color: var(--ink3);
  font-family: 'Noto Serif JP', serif;
  font-weight: 300;
}

.cal04__month-kanji {
  margin-left: auto;
  font-family: 'Noto Serif JP', serif;
  font-size: 32px;
  font-weight: 300;
  color: var(--gold);
  opacity: 0.7;
}
/* ── Day-of-week labels ── */

.cal04__dow {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  padding: 12px 20px 0;
}

.cal04__dow-cell {
  text-align: center;
  font-family: 'Noto Serif JP', serif;
  font-size: 10px;
  font-weight: 400;
  letter-spacing: 0.14em;
  color: var(--ink3);
  padding-bottom: 10px;
}

.cal04__dow-cell:first-child {
  color: var(--red);
  opacity: 0.7;
}

.cal04__dow-cell:last-child {
  color: var(--gold);
  opacity: 0.7;
}
/* ── Date grid — pure CSS, checkbox-hack date selection ── */

.cal04__grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  padding: 4px 20px 28px;
  gap: 2px;
}
/* Hidden radio inputs for date selection */

.cal04__date-radio {
  display: none;
}

.cal04__date-label {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 10px 4px 8px;
  min-height: 56px;
  cursor: pointer;
  border-radius: 6px;
  transition: background 0.18s;
  position: relative;
}

.cal04__date-label:hover {
  background: var(--warm);
}

.cal04__date-num {
  font-size: 16px;
  font-weight: 400;
  color: var(--ink);
  line-height: 1;
  transition: color 0.18s;
}

.cal04__date-label.other {
  opacity: 0.22;
  pointer-events: none;
}

.cal04__date-label.sun .cal04__date-num {
  color: var(--red);
}

.cal04__date-label.sat .cal04__date-num {
  color: var(--gold);
}
/* Today ring */

.cal04__date-label.today .cal04__date-num {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1.5px solid var(--red);
  border-radius: 50%;
  color: var(--red);
  font-weight: 600;
}
/* Selected state — :checked sibling targets label */

.cal04__date-radio:checked + .cal04__date-label {
  background: var(--sel);
  border: 1px solid var(--sel-bdr);
}

.cal04__date-radio:checked + .cal04__date-label .cal04__date-num {
  color: var(--red);
  font-weight: 600;
}
/* Event dots (pure CSS, decorative) */

.cal04__dots {
  display: flex;
  gap: 3px;
  margin-top: 5px;
}

.cal04__dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--ink3);
  opacity: 0.5;
}

.cal04__dot--red {
  background: var(--red);
  opacity: 0.8;
}

.cal04__dot--gold {
  background: var(--gold);
  opacity: 0.8;
}
/* ── Footer: selected date readout (CSS :checked trick) ── */

.cal04__footer {
  border-top: 1px solid var(--line);
  padding: 16px 36px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--warm);
}

.cal04__footer-note {
  font-family: 'Noto Serif JP', serif;
  font-size: 11px;
  letter-spacing: 0.15em;
  color: var(--ink3);
}

.cal04__legend {
  display: flex;
  gap: 14px;
}

.cal04__legend-item {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  color: var(--ink3);
  letter-spacing: 0.06em;
}

.cal04__legend-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
}
/* ── Decorative vertical rule ── */

.cal04__rule {
  width: 1px;
  background: linear-gradient(to bottom, transparent, var(--line) 30%, var(--line) 70%, transparent);
  align-self: stretch;
}
/* ── Ink brush decoration ── */

.cal04__brush {
  position: absolute;
  top: -8px;
  right: 24px;
  font-family: 'Noto Serif JP', serif;
  font-size: 11px;
  letter-spacing: 0.3em;
  color: var(--ink3);
  opacity: 0.4;
  writing-mode: vertical-rl;
}

@media (max-width: 480px) {
  .cal04__month-head {
    padding: 20px 16px 14px;
  }

  .cal04__month-name {
    font-size: 36px;
  }

  .cal04__grid {
    padding: 4px 8px 20px;
    gap: 1px;
  }

  .cal04__footer {
    padding: 12px 16px;
    flex-direction: column;
    gap: 10px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cal04 * {
    animation: none !important;
    transition: none !important;
  }
}
```

---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/interview-q-and-a-transcript-layout/"
title: "Interview Q and A Transcript Layout"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A transcript that actually reads like one: questions in a condensed sans, answers in a serif at reading size, speaker avatars that stick beside their turn,…"
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interview Q and A Transcript Layout
Source: https://codefronts.com/layouts/css-blog-layouts/interview-q-and-a-transcript-layout/

A transcript that actually reads like one: questions in a condensed sans, answers in a serif at reading size, speaker avatars that stick beside their turn, and timestamps in the margin. Built on a <dl> — the semantically correct element for Q&A — with attribute-driven speakers so a three-way panel needs no new classes.
## HTML
```html
<article class="bl-11">
  <header class="bl-11__head">
    <p class="bl-11__rubric">Interview · 34 min read</p>
    <h1>“We stopped shipping features for a year. Revenue went up.”</h1>
    <p class="bl-11__standfirst">Mira Solberg spent 2025 deleting things. The CTO of a 60-person infrastructure company explains the year her team wrote almost no new product code — and why the board eventually thanked her for it.</p>
    <div class="bl-11__people">
      <div class="bl-11__person" data-who="host">
        <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=120&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="120" height="120" loading="lazy" decoding="async">
        <p><strong>Dev Patel</strong><span>Interviewer</span></p>
      </div>
      <div class="bl-11__person" data-who="guest">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="120" height="120" loading="lazy" decoding="async">
        <p><strong>Mira Solberg</strong><span>CTO, Ferrous</span></p>
      </div>
    </div>
    <p class="bl-11__note">Recorded 12 July 2026 in Oslo. Edited for length; <a href="#">full audio and transcript</a>.</p>
  </header>

  <dl class="bl-11__qa">
    <dt class="bl-11__turn" data-who="host">
      <div class="bl-11__gutter"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&amp;q=70&amp;auto=format&amp;fit=crop" alt="Dev Patel" width="80" height="80" loading="lazy" decoding="async"><time datetime="PT0M42S">00:42</time></div>
      <div class="bl-11__said"><p class="bl-11__who">Dev Patel</p><p class="bl-11__q">Let's start with the decision itself. Whose idea was the freeze, and how did you sell it?</p></div>
    </dt>
    <dd class="bl-11__turn" data-who="guest">
      <div class="bl-11__gutter"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&amp;q=70&amp;auto=format&amp;fit=crop" alt="Mira Solberg" width="80" height="80" loading="lazy" decoding="async"><time datetime="PT0M55S">00:55</time></div>
      <div class="bl-11__said">
        <p class="bl-11__who">Mira Solberg</p>
        <p>It wasn't sold, it was conceded. We had a quarter where four of five committed features slipped, and the postmortems all pointed at the same three subsystems. At some point the argument stops being strategic and becomes arithmetic.</p>
        <p>I brought the board a single slide: the cost of the next four features, and the cost of the four we had already shipped that were still consuming engineering time. The second number was bigger. That was the whole pitch.</p>
      </div>
    </dd>

    <dt class="bl-11__turn" data-who="host">
      <div class="bl-11__gutter"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&amp;q=70&amp;auto=format&amp;fit=crop" alt="Dev Patel" width="80" height="80" loading="lazy" decoding="async"><time datetime="PT4M10S">04:10</time></div>
      <div class="bl-11__said"><p class="bl-11__who">Dev Patel</p><p class="bl-11__q">A year is a long time to tell a sales team there is nothing new.</p></div>
    </dt>
    <dd class="bl-11__turn" data-who="guest">
      <div class="bl-11__gutter"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&amp;q=70&amp;auto=format&amp;fit=crop" alt="Mira Solberg" width="80" height="80" loading="lazy" decoding="async"><time datetime="PT4M22S">04:22</time></div>
      <div class="bl-11__said">
        <p class="bl-11__who">Mira Solberg</p>
        <p>That's the part I'd do differently. We framed it internally as a freeze, which sounds like absence. Our sales lead reframed it about six weeks in as “the reliability year”, and suddenly there was something to talk about on calls. <em>[laughs]</em> Same work, completely different reception.</p>
        <div class="bl-11__pullout"><p>“A freeze sounds like absence. Call it the reliability year and it becomes a roadmap.”</p></div>
        <p>By March we were publishing an uptime and latency report every month. Customers who had never asked about either started citing it in renewals.</p>
      </div>
    </dd>

    <dt class="bl-11__turn" data-who="host">
      <div class="bl-11__gutter"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&amp;q=70&amp;auto=format&amp;fit=crop" alt="Dev Patel" width="80" height="80" loading="lazy" decoding="async"><time datetime="PT11M08S">11:08</time></div>
      <div class="bl-11__said"><p class="bl-11__who">Dev Patel</p><p class="bl-11__q">What did you actually delete?</p></div>
    </dt>
    <dd class="bl-11__turn" data-who="guest">
      <div class="bl-11__gutter"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&amp;q=70&amp;auto=format&amp;fit=crop" alt="Mira Solberg" width="80" height="80" loading="lazy" decoding="async"><time datetime="PT11M14S">11:14</time></div>
      <div class="bl-11__said">
        <p class="bl-11__who">Mira Solberg</p>
        <p>Two entire integrations with fewer than nine users each, a custom job scheduler that predated a perfectly good open-source one, and about forty percent of our feature flags — most of which had been permanent for two years and were, functionally, dead branches nobody dared remove.</p>
        <p>The scheduler was the emotional one. Someone had written it in a week in 2019 and it worked. It also had no tests and one person who understood it. <em>[pause]</em> That's not a system, that's a hostage situation.</p>
      </div>
    </dd>

    <dt class="bl-11__turn" data-who="host">
      <div class="bl-11__gutter"><img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&amp;q=70&amp;auto=format&amp;fit=crop" alt="Dev Patel" width="80" height="80" loading="lazy" decoding="async"><time datetime="PT26M31S">26:31</time></div>
      <div class="bl-11__said"><p class="bl-11__who">Dev Patel</p><p class="bl-11__q">Would you do it again?</p></div>
    </dt>
    <dd class="bl-11__turn" data-who="guest">
      <div class="bl-11__gutter"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&amp;q=70&amp;auto=format&amp;fit=crop" alt="Mira Solberg" width="80" height="80" loading="lazy" decoding="async"><time datetime="PT26M35S">26:35</time></div>
      <div class="bl-11__said">
        <p class="bl-11__who">Mira Solberg</p>
        <p>I'd do it earlier and shorter. Nine months, not twelve, and I'd keep one small team shipping so the muscle doesn't atrophy. But the principle holds: you cannot build on a floor you are afraid to stand on.</p>
      </div>
    </dd>
  </dl>

  <footer class="bl-11__footer">
    <p>This interview has been condensed. <a href="#">Read the unedited transcript</a> or <a href="#">listen to the episode</a>.</p>
  </footer>
</article>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,300;0,400;0,600;1,400&family=DM+Sans:opsz,[email protected],400;9..40,500;9..40,700&display=swap');

.bl-11 {
  --bg: #faf9f7;
  --surface: #ffffff;
  --text: #171614;
  --muted: #6e6a63;
  --line: #e5e2db;
  --acc: #1d4ed8;
  --acc-2: #a21caf;
  --q-size: 1.0625rem;
  --q-weight: 700;
  --serif: "Spectral",ui-serif,Georgia,serif;
  --sans: "DM Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-11 {
    --bg: oklch(98% .004 80);
    --surface: oklch(100% 0 0);
    --text: oklch(17% .008 70);
    --muted: oklch(50% .012 72);
    --line: oklch(90% .008 80);
    --acc: oklch(48% .19 265);
    --acc-2: oklch(50% .21 330);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-11:not([data-theme="light"]) {
    --bg: #100f0e;
    --text: #f2f0ec;
    --surface: #191817;
    --muted: #a09b93;
    --line: #2a2825;
    --acc: #93b4ff;
    --acc-2: #f0abfc;
  }
}

.bl-11[data-theme="dark"] {
  --bg: #100f0e;
  --text: #f2f0ec;
  --surface: #191817;
  --muted: #a09b93;
  --line: #2a2825;
  --acc: #93b4ff;
  --acc-2: #f0abfc;
}

.bl-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--serif);
  -webkit-font-smoothing: antialiased;
}

.bl-11,
.bl-11 *,
.bl-11 *::before,
.bl-11 *::after {
  box-sizing: border-box;
}

.bl-11 a {
  color: inherit;
}

.bl-11 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.bl-11 img {
  display: block;
  object-fit: cover;
  background: var(--line);
}

.bl-11__head {
  max-width: 50rem;
  margin-inline: auto;
  padding: clamp(2.5rem,7vw,5rem) clamp(1.25rem,5vw,2rem) clamp(1.5rem,3vw,2.5rem);
  display: grid;
  gap: 1.15rem;
}

.bl-11__rubric {
  margin: 0;
  font-family: var(--sans);
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--acc-2);
}

.bl-11__head h1 {
  margin: 0;
  font-weight: 600;
  font-size: clamp(1.875rem,5vw,3.25rem);
  line-height: 1.06;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.bl-11__standfirst {
  margin: 0;
  font-size: clamp(1.0625rem,1.9vw,1.3125rem);
  line-height: 1.6;
  color: var(--muted);
  max-width: 56ch;
  text-wrap: pretty;
}

.bl-11__people {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-top: .5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
}

.bl-11__person {
  display: flex;
  align-items: center;
  gap: .7rem;
}

.bl-11__person img {
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  outline: 2px solid var(--voice,var(--acc));
  outline-offset: 2px;
}

.bl-11__person[data-who="host"] {
  --voice: var(--acc);
}

.bl-11__person[data-who="guest"] {
  --voice: var(--acc-2);
}

.bl-11__person p {
  margin: 0;
  display: grid;
  font-family: var(--sans);
  font-size: .875rem;
}

.bl-11__person strong {
  font-weight: 700;
}

.bl-11__person span {
  font-size: .75rem;
  color: var(--muted);
}

.bl-11__note {
  margin: 0;
  font-family: var(--sans);
  font-size: .8125rem;
  color: var(--muted);
}

.bl-11__note a {
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: .2em;
}

.bl-11__qa {
  display: grid;
  grid-template-columns: 4.5rem minmax(0,1fr);
  column-gap: clamp(.75rem,2vw,1.5rem);
  max-width: 50rem;
  margin: 0 auto;
  padding: 0 clamp(1.25rem,5vw,2rem);
}

.bl-11__turn {
  grid-column: 1/-1;
  display: grid;
  grid-template-columns: 4.5rem minmax(0,1fr);
  column-gap: clamp(.75rem,2vw,1.5rem);
  margin: 0;
  padding-block: clamp(1.25rem,2.5vw,1.75rem);
  border-top: 1px solid var(--line);
}

@supports (grid-template-columns: subgrid) {
  .bl-11__turn {
    grid-template-columns: subgrid;
  }
}

.bl-11__turn[data-who="host"] {
  --voice: var(--acc);
}

.bl-11__turn[data-who="guest"] {
  --voice: var(--acc-2);
}

.bl-11__gutter {
  display: grid;
  gap: .5rem;
  justify-items: center;
  position: sticky;
  top: 1.5rem;
  align-self: start;
  height: max-content;
}

.bl-11__gutter img {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  outline: 2px solid var(--voice);
  outline-offset: 2px;
}

.bl-11__gutter time {
  font-family: var(--sans);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  letter-spacing: .02em;
}

.bl-11__said {
  display: grid;
  gap: .85rem;
  min-width: 0;
}

.bl-11__who {
  margin: 0;
  font-family: var(--sans);
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--voice);
}

.bl-11__said p {
  margin: 0;
  font-size: 1.125rem;
  line-height: 1.72;
  text-wrap: pretty;
  max-width: 64ch;
}

.bl-11__said em {
  font-style: italic;
  color: var(--muted);
  font-size: .92em;
}

.bl-11__q {
  font-family: var(--sans) !important;
  font-size: var(--q-size) !important;
  font-weight: var(--q-weight);
  line-height: 1.45 !important;
  letter-spacing: -.015em;
  color: var(--text);
}

.bl-11__turn[data-who="host"] {
  background: linear-gradient(90deg,color-mix(in oklab,var(--acc) 5%,transparent),transparent 60%);
}

.bl-11__pullout {
  margin: .35rem 0;
  padding: 1rem 1.25rem;
  border-radius: .75rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-inline-start: 3px solid var(--voice);
}

.bl-11__pullout p {
  margin: 0;
  font-size: clamp(1.1875rem,2.4vw,1.5rem) !important;
  line-height: 1.32 !important;
  font-weight: 600;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.bl-11__footer {
  max-width: 50rem;
  margin-inline: auto;
  padding: clamp(2rem,4vw,3rem) clamp(1.25rem,5vw,2rem) clamp(3.5rem,8vw,6rem);
  border-top: 1px solid var(--line);
  font-family: var(--sans);
  font-size: .875rem;
  color: var(--muted);
}

.bl-11__footer p {
  margin: 0;
}

.bl-11__footer a {
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: .2em;
}

@media (max-width: 34rem) {
  .bl-11__qa,
    .bl-11__turn {
    grid-template-columns: 2.5rem minmax(0,1fr);
  }

  .bl-11__gutter img {
    width: 2rem;
    height: 2rem;
  }

  .bl-11__gutter time {
    font-size: .5625rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-11 * {
    transition: none !important;
    animation: none !important;
  }
}
```

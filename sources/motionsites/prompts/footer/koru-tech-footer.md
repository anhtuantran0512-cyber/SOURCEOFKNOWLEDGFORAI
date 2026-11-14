---
source: "motionsites"
id: "koru-tech-footer"
title: "Koru Tech Footer"
category: "Footer"
type: "footer"
types: []
license: "Free prompt published by MotionSites AI — see NOTICE.md"
url: "https://motionsites.ai/sections#koru-tech-footer"
---

# Prompt: Koru Tech footer

Build a single-file **website footer section** (header bar plus full footer, one screen) for a fictional IT services company, **Koru Tech**. Use plain HTML, CSS and vanilla JS, with no framework and no build step. The look is dark and techy: a near-black green page and a glass nav. At the bottom, a glowing emerald horizon over a perspective grid floor, with a giant outlined "KORU TECH" wordmark standing on the horizon line. Emerald accents throughout.

## Media

- **Still:** `https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/139344bb-585a-4867-9a31-94cbfad8f6d9.jpg` (1920×1280, 3:2). A dark green-black sky, a bright emerald horizon light low in the frame (horizon at 78.6% height), and a faint emerald perspective grid floor below.
- **Motion:** a muted 4s loop of the same scene, `https://d2ol7oe51mr4n9.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/17d62c8c-c7a4-491d-82ff-b0cbd3387820.mp4` (1600×1064).
  - The camera glides forward over the grid; the grid lines stream towards the viewer and the horizon glow breathes brighter and dimmer.
  - The horizon was stabilised so it never moves, and the last second crossfades into the first, so it loops without a jump and never plays in reverse.
  - Fade it in (0.9s) once its first frame is ready.
- **Rule:** nothing in the scene is drawn or animated in code. Only the UI animates.

## Scale

- **Units:** a 1536-wide reference frame, `--u = min(100vw/1536, 100vh/930)`, centred. The page is a flex column at least one screen tall.
- **Rows:** a 100u header row at the top and an 805u footer row pinned to the bottom. Only the empty band between them stretches.
- **Scene box:** pinned to the page bottom, centred, `width: max(100%, 1536u)`, `aspect-ratio: 3/2`, holding the still (cover, bottom-centre), the video (cover, object-position 50% 100%) and the wordmark.

## Type and colour

- **Font:** **Albert Sans** 400/600.
- **Colours:**
  - page `#030D0B`
  - accent emerald `#0BE3AE`, deeper emerald `#02C78A`
  - text `#F8F8F8`, muted `#BBBCC2`
- **Glass:** an emerald-tinted fill (4.5% → 7%) with an emerald hairline border that is brighter at the top.

## Header (1536 frame)

- **Logo:** at (251, 43). A 45u emerald gradient rounded tile (`#14E6B0` → `#01B987`, radius 10) holding a bold white geometric "K", then "KORU TECH" (600, 17u, tracking .06em).
- **Nav:** a glass pill 452×58u at (543, 33) with "Home · Services · Projects · About · Contact" at 15.2u. Home is the current page, in emerald.
- **Button:** a white "Book a Call" pill (158×51u at 1131.5, 37) with an emerald arrow.

## Footer

- **Left column** (from x 134):
  - the logo again
  - the tagline "Maximize your digital infrastructure and / enhance organizational efficiency." (16u)
  - "QUICK CONTACT" (tracking .05em)
  - four 51u round emerald-ring buttons: professional network (emerald glyph), Instagram, X and YouTube (white glyphs)
- **Link columns** (headings 600 at 17.4u, links 16.6u):
  - **Quick Links** at x 723: Home, About Us, Services, Projects, Contact Us
  - **Support** at x 921: FAQs, Support Center
  - **Get in Touch With Us** at x 1148, each row with a small emerald icon:
    - phone: "Phone: +64 9 555 0142"
    - mail: "Email: info@korutech.example"
    - mail: "Email: sales@korutech.example"
    - pin: "Address: Wellington, New Zealand"
- **Wordmark:** an inline SVG spanning the scene width (viewBox 1440×200, 21% of the box tall, bottom 21.4%, so it stands on the horizon). It's "KORU TECH" as outlined text (Albert Sans 600, textLength 1478, so the "H" runs off the right edge) with a 1.6px stroke. The stroke fades up from bright mint `#35FFC8` at the horizon to emerald at 42% opacity at the top.

## Motion (UI)

- **Entrance:** one Web Animations sequence, about 1.7s, behind an `entrance-pending` class with a fallback.
  - The header logo, nav and button rise 8u.
  - The footer logo rises, then the tagline wipes up.
  - Then the Quick Contact title, the socials and the three columns, staggered.
- **Hover:** links brighten; social rings fill faintly emerald and lift 2px; the button gets an emerald halo.
- **Reduced motion:** no entrance and no video.

## Tablet and phone (below 1180px)

- **One screen:** the page is locked to one screen, and a small script scales the content (`--k`) so it never scrolls.
- **Header:** the nav and button collapse into a glass menu button with a dropdown.
- **Columns:** the footer reflows. Tablets show the brand, then three columns; phones show two columns, then contact full width.
- **Scene:** the scene box is at least 640px wide, and a band is reserved so the wordmark never sits under text. On short landscape phones the wordmark hides.

## Acceptance check (1440×960)

- The emerald horizon glows low on the screen with the grid streaming towards you, and the giant outlined KORU TECH stands exactly on the horizon line.
- The footer columns sit above it with even margins, and the loop never jumps.
- **Content:** no real brands; contact details are fictional.

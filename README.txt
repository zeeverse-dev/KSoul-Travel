K-SOUL TRAVEL — website (8 pages)
=================================
HOW TO VIEW
  Unzip, then double-click index.html to open it in Chrome / Edge.
  (Do not preview it inside a chat window: those previews block photos and 3D.)
  Internet is needed: fonts, the animation libraries (GSAP, Lenis, Three.js) and
  inner-page photos load from the web (photos come from ksoultravel.com).

PAGES
  index.html            Home: 3D glass Mugunghwa (hibiscus) from the logo, bloom-on-scroll
  about.html            About Audrey, stats, journey Morocco -> Seoul
  design-your-trip.html Questions, how it works, benefits
  digital-guides.html   Guides + 4 categories
  travel-with-me.html   3 available trips + 6 coming soon
  book-a-call.html      Calendly inline booking (k-s-consultation-45min)
  contact.html          Channels, CTAs, contact form
  blog.html             11 destinations

FILES
  assets/css/style.css       all styles (brand colours at the top in :root)
  assets/js/main.js          smooth scroll, page transitions, scroll animations, flight path
  assets/js/hibiscus.module.js  the 3D flower (also inlined in index.html)
  assets/img/                logo + Audrey's photos used on the home page

PUBLISHING ON GITHUB PAGES
  Live site: https://zeeverse-dev.github.io/KSoul-Travel/
  The Pages workflow deploys automatically whenever changes are pushed to main.
  In repository Settings > Pages, keep the source set to GitHub Actions.

BEFORE GOING LIVE
  - "Design my trip" buttons link to the live questionnaire: https://ksoultravel.com/questionaire/
  - Contact form + newsletter are front-end only: connect them to your form / newsletter plugin.
  - Blog cards link to /blog/; replace with each country's category URL.
  - Footer IT / ES links go to the live TranslatePress versions.
  - edit text: pages.py + build.py generate the HTML (python3 pages.py) — or edit the .html files directly.

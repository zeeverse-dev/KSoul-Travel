# Builds the K-SOUL static site: shared head/nav/footer + page bodies.
import pathlib
OUT = pathlib.Path(__file__).parent
U = 'https://ksoultravel.com/wp-content/uploads/'
LIVE = 'https://ksoultravel.com'
Q = LIVE + '/questionaire/'          # live "Design my trip" questionnaire
CAL = 'https://calendly.com/ksoultravel/k-s-consultation-45min'

PAGES = [('home', 'index.html', 'Home'), ('about', 'about.html', 'About'), ('design', 'design-your-trip.html', 'Design Your Trip'),
         ('guides', 'digital-guides.html', 'Digital Guides'), ('travel', 'travel-with-me.html', 'Travel With Me'),
         ('book', 'book-a-call.html', 'Book A Call'), ('contact', 'contact.html', 'Contact'), ('blog', 'blog.html', 'Blog')]
HREF = {k: f for k, f, _ in PAGES}

FLOWER_SVG = '''<svg viewBox="-50 -50 100 100"><g>''' + ''.join(
    f'<path transform="rotate({i*72})" d="M0 -4 C 14 -10 22 -30 12 -44 C 6 -50 -6 -50 -12 -44 C -22 -30 -14 -10 0 -4Z" fill="#F4A7B9" stroke="#E7CC8A" stroke-width=".8" opacity=".95"/>' for i in range(5)
) + '<circle r="7" fill="#B8174E"/><circle r="3" fill="#E7CC8A"/></g></svg>'

def head(title, desc, extra=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0E4535">
<link rel="icon" href="{U}2026/05/cropped-WhatsApp_Image_2026-05-14_at_10.58.57_PM-removebg-preview-32x32.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{extra}
</head>
<body>
<div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="grain" aria-hidden="true"></div>
<div class="curtain" aria-hidden="true"><div class="panel"></div><div class="flower">{FLOWER_SVG}</div><div class="word">K-SOUL TRAVEL</div></div>
<div class="cursor" aria-hidden="true"><b>VIEW</b></div><div class="cursor-dot" aria-hidden="true"></div>
<div id="progress" aria-hidden="true"></div>
'''

def nav(active):
    act = lambda k: ' class="active"' if k == active else ''
    items = ''.join(f'<li><a href="{f}"{act(k)}>{n}</a></li>' for k, f, n in PAGES[1:])
    mitems = ''.join(f'<a href="{f}"{act(k)}>{n}</a>' for k, f, n in PAGES)
    return f'''
<header class="nav glass">
  <a href="index.html" class="logo" aria-label="K-SOUL Travel home"><img src="assets/img/logo.webp" alt="K-SOUL Travel Personalized Travel Planning &amp; Experiences"></a>
  <ul>{items}</ul>
  <div class="lang"><a class="on" href="#">EN</a><a href="{LIVE}/it/">IT</a><a href="{LIVE}/es/">ES</a></div>
  <a href="{Q}" class="btn btn-gold" data-magnetic><span>Design my trip</span></a>
  <button class="burger" aria-label="Menu"><i></i><i></i></button>
</header>
<nav class="mmenu">{mitems}<a href="{Q}" class="btn btn-gold"><span>Design my trip</span></a></nav>
'''

def footer():
    return f'''
<footer class="footer glass">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img class="flogo" src="assets/img/logo.webp" alt="K-SOUL Travel">
        <p class="tag">Your dream trip,<br>designed with soul ✦</p>
        <p style="margin-top:22px;color:var(--text);max-width:380px">Join the K-SOUL list: travel inspiration, hidden gems, future group trips and <b style="color:var(--green);font-weight:500">10% off</b> all digital travel guides.</p>
        <form class="news glass" data-demo><input type="email" placeholder="Your email" required aria-label="Email"><button class="btn btn-gold" type="submit"><span>Subscribe</span></button></form>
        <p class="form-msg" style="margin-top:12px">Thank you ✦ — please connect this form to your newsletter tool.</p>
      </div>
      <div><h4>Explore</h4><ul>
        <li><a href="about.html">About</a></li><li><a href="design-your-trip.html">Design Your Trip</a></li>
        <li><a href="digital-guides.html">Digital Guides</a></li><li><a href="travel-with-me.html">Travel With Me</a></li><li><a href="blog.html">Blog</a></li></ul></div>
      <div><h4>Support</h4><ul>
        <li><a href="book-a-call.html">Book A Call</a></li><li><a href="contact.html">Contact</a></li><li><a href="{LIVE}/faq/">FAQ</a></li>
        <li><a href="mailto:info.ksoultravel@gmail.com">info.ksoultravel@gmail.com</a></li></ul></div>
      <div><h4>Follow</h4><ul>
        <li><a href="https://www.instagram.com/ksoultravel" target="_blank" rel="noopener">Instagram</a></li>
        <li><a href="https://www.instagram.com/iamaudreymartin" target="_blank" rel="noopener">Personal Instagram</a></li>
        <li><a href="https://youtube.com/@audreymartin" target="_blank" rel="noopener">YouTube</a></li>
        <li><a href="https://www.tiktok.com/@iamaudreymartin" target="_blank" rel="noopener">TikTok</a></li></ul></div>
    </div>
    <div class="big">K-SOUL</div>
    <div class="footer-bottom">
      <span>© <span data-year></span> K-SOUL Travel. All rights reserved.</span>
      <div><a href="{LIVE}/privacy-policy/">Privacy Policy</a><a href="{LIVE}/cookie-policy/">Cookie Policy</a><a href="{LIVE}/terms-conditions/">Terms &amp; Conditions</a><a href="{LIVE}/cookie-preferences/">Cookie Preferences</a></div>
    </div>
  </div>
</footer>
'''

LIBS = '''<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>
'''

def page(key, title, desc, body, extra_head='', before_main='', after_main=''):
    html = head(title, desc, extra_head) + nav(key) + '<main>' + body + '</main>' + footer() + LIBS + before_main + '<script src="assets/js/main.js"></script>\n' + after_main + '</body>\n</html>\n'
    (OUT / HREF[key]).write_text(html, encoding='utf-8')

def phero(img, crumb, eyebrow, title, text='', btns=''):
    return f'''
<section class="phero" data-cursor="">
  <img class="bg" src="{img}" alt="">
  <canvas data-petals></canvas>
  <div class="crumbs glass-dark"><a href="index.html">Home</a> &nbsp;✦&nbsp; {crumb}</div>
  <div class="phero-card glass-dark">
    <span class="eyebrow">{eyebrow}</span>
    <h1 class="display" style="margin-top:14px">{title}</h1>
    {f"<p>{text}</p>" if text else ""}
    {f'<div class="btns">{btns}</div>' if btns else ""}
  </div>
</section>'''

def cta(img, eyebrow, title, text, btns):
    return f'''
<section class="cta" data-circle>
  <div class="cta-media"><img src="{img}" alt=""></div>
  <div class="cta-inner"><div class="cta-box glass-dark">
    <span class="eyebrow">{eyebrow}</span>
    <h2 class="h2" style="margin-top:16px">{title}</h2>
    <p>{text}</p>
    <div class="btns" style="justify-content:center">{btns}</div>
  </div></div>
</section>'''

BTN_DESIGN = f'<a href="{Q}" class="btn btn-gold" data-magnetic><span>Design my trip <i class="arr">→</i></span></a>'
BTN_CALL = '<a href="book-a-call.html" class="btn btn-glass on-dark" data-magnetic><span>Book a call</span></a>'
BTN_CALL_L = '<a href="book-a-call.html" class="btn btn-glass" data-magnetic><span>Book a call</span></a>'

REVIEWS = [
  ('7 Days · Maldives Proposal Trip', 'She took care of every single detail and designed a proposal that felt elegant, intimate and emotional instead of overly flashy or cliché. She even managed to find a violinist last minute… and thankfully, she said yes.', 'Michael A.', 'United Kingdom'),
  ('21 Days · Patagonia & Antarctica Honeymoon', 'Audrey made the entire experience feel seamless from beginning to end and we genuinely felt treated like VIP clients the whole time. We received two unexpected upgrades, and it truly became the honeymoon trip of our dreams.', 'Daniel & Olivia', 'Australia'),
  ('8 Days · Kazakhstan', 'Audrey organized for us to spend three nights inside traditional yurts with local families she personally knew, which allowed us to experience a completely different side of the country.', 'Lucas M.', 'Spain'),
  ('25 Days · Japan Solo Trip', 'She personally booked restaurants for me, made sure every place was halal-friendly and helped me discover local spots I would’ve never found on my own.', 'Omar', 'United Arab Emirates'),
  ('2 Months · South America', 'Audrey organized everything carefully for us, choosing safe neighborhoods, trusted hotels and even reliable local guides. Despite how long the journey was, everything flowed perfectly from beginning to end.', 'Giulia & Martina', 'Italy'),
  ('9 Days · South Korea', 'As someone obsessed with K-pop, skincare and K-dramas, this trip honestly felt like a dream. Audrey sent me the best skincare clinics, local beauty spots and amazing local restaurants that only someone living in Korea would know.', 'Camila G.', 'Mexico'),
  ('14 Days · Italy Family Trip', 'Traveling with 3 small children honestly scared us a lot at first…but everything was perfect. Every detail was carefully organized and all the activities were very family and child-friendly.', 'Sarah W.', 'United States'),
  ('17 Days · South Korea', 'I specifically wanted my South Korea trip to be organized by someone who had actually lived there, and Audrey did an incredible job. I also had the chance to visit Jeju Island and experience a side of Korea that felt much more real.', 'Emily R.', 'United States'),
]
def review_html(r):
    return f'<article class="review glass"><span class="trip-l">{r[0]}</span><blockquote>“{r[1]}”</blockquote><footer><div><b>{r[2]}</b><br><span>{r[3]}</span></div><span class="stars">★★★★★</span></footer></article>'
def reviews_section():
    a = ''.join(review_html(r) for r in REVIEWS[:4]) * 2
    b = ''.join(review_html(r) for r in REVIEWS[4:]) * 2
    return f'''
<section class="section" style="padding-bottom:60px">
  <div class="container center">
    <span class="eyebrow" data-reveal>Testimonials</span>
    <h2 class="h2 mt-s" data-split>Clients experiences<br>with <em>K-SOUL</em></h2>
  </div>
  <div class="fade-x mt-l" data-cursor="READ"><div class="marquee">{a}</div><div class="marquee rev">{b}</div></div>
</section>'''

SERVICES = ['Complete Personalized Travel Planning', '48h Express Planning', 'Itinerary Review', 'Couples, Honeymoons & Proposals', 'Solo Women Travel', 'Muslim-Friendly Travel', 'Adventure & Extreme Experiences', 'Family & Kids Travel', 'Friends & Group Trips', 'Relocation & Visa Support', 'Healing & Reconnection Trips', 'Luxury & VIP Experiences', 'Content Creator & Photography Trips', 'Korea Specialist Experiences', 'Off-The-Beaten-Path Destinations']

STEPS = [
  ('Share Your Vision', 'Fill out the questionnaire and tell me about your dream trip, travel style, preferences, expectations, special requests, and every detail that matters to you.', 'assets/img/karst.jpg'),
  ('Travel Review', "I carefully review your request to fully understand what you're looking for and create a personalized proposal tailored to your vision.", 'assets/img/k5.jpg'),
  ('Your Approval', "Review the proposal and let me know if you'd like any adjustments. Once you're happy with every detail, we'll move forward with the final planning process.", 'assets/img/k1.jpg'),
  ('Planning', 'Once approved, I take care of the complete organization of your trip from A to Z, carefully managing every detail to create an experience designed entirely around you.', 'assets/img/k7.jpg'),
  ('Enjoy Your Journey', 'From the planning stage until your return home, I remain available throughout your journey to provide support whenever needed, so you can simply relax and enjoy the experience.', 'assets/img/beach.jpg'),
]
def steps_section(title='Five steps to your<br><em>dream journey</em>'):
    imgs = ''.join(f'<img src="{s[2]}" alt="">' for s in STEPS)
    bars = ''.join('<i><b></b></i>' for _ in STEPS)
    lst = ''.join(f'<div class="step"><span class="num">STEP {i+1:02d}</span><h3 class="h3">{s[0]}</h3><p class="lead">{s[1]}</p></div>' for i, s in enumerate(STEPS))
    return f'''
<section class="section" id="how">
  <div class="container">
    <div class="center"><span class="eyebrow" data-reveal>How it works</span><h2 class="h2 mt-s" data-split>{title}</h2></div>
    <div class="steps-wrap" data-steps>
      <div class="steps-visual" data-cursor="VIEW">{imgs}<div class="steps-bar">{bars}</div><div class="glass-dark"><span class="big">01</span><span class="lbl">Share Your Vision</span></div></div>
      <div class="steps-list">{lst}</div>
    </div>
  </div>
</section>'''

ICON = {
 'detail': '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3M8 11h6M11 8v6"/></svg>',
 'time': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 'support': '<svg viewBox="0 0 24 24"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
 'star': '<svg viewBox="0 0 24 24"><path d="M12 2l2.6 7.4L22 12l-7.4 2.6L12 22l-2.6-7.4L2 12l7.4-2.6z"/></svg>',
 'mail': '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 'ig': '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".5"/></svg>',
 'yt': '<svg viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="4"/><path d="m10 9 5 3-5 3z"/></svg>',
 'tt': '<svg viewBox="0 0 24 24"><path d="M14 3v11a4 4 0 1 1-4-4"/><path d="M14 3c.5 3 2.5 5 6 5"/></svg>',
}

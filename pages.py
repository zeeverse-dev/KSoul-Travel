from build import *

# ============================== HOME ==============================
HIB = (OUT / 'assets/js/hibiscus.module.js').read_text(encoding='utf-8')
home_head = '''<script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"}}</script>
<script>window.KSHero={bloom:0,p:0,mx:0,my:0};</script>'''

trips_cards = ''.join(f'''<a class="trip" href="travel-with-me.html" data-cursor="TRIP">
  <img src="{U}{img}" alt="{name}"><span class="tag glass">Available</span>
  <div class="info glass-dark"><span class="when">{when}</span><h3>{name}</h3><ul><li>{days}</li><li>{dates}</li><li>{mx}</li></ul></div></a>''' for img, name, when, days, dates, mx in [
  ('2026/09/fadhil-abhimantra-u_Uwt5DVMCo-unsplash-1-909x1024.jpg', 'Kazakhstan: The Road to the Stars', 'June 2028', '11 Days / 10 Nights', 'June 17–27, 2028', 'Max 8 Travelers'),
  ('2026/09/WhatsApp-Image-2026-09-27-at-5.54.30-PM-988x1024.jpeg', 'Japan: From Cherry Blossoms to the Sea', 'March – April 2028', '15 Days / 14 Nights', 'March 27 – April 10, 2028', 'Max 9 Travelers'),
  ('2026/09/patagonia-antarctica-3-921x1024.jpg', 'Patagonia &amp; Antarctica', 'December 2028', '18 Days / 17 Nights', 'December 3–20, 2028', 'Max 7 Travelers')])

home = f'''
<section id="hero3d" data-cursor="">
  <canvas id="flowerCanvas" aria-label="3D glass hibiscus flower, the K-SOUL emblem"></canvas>
  <div class="hero-ui">
    <div class="hero-copy">
      <span class="eyebrow hero-in">Personalized travel planning</span>
      <h1 class="display mt-s"><span class="hl"><span>Your dream trip,</span></span><br><span class="hl"><span>designed with <em>soul</em></span></span></h1>
      <p class="lead hero-in">Custom itineraries for honeymoons, solo travel, families and Korea lovers — crafted around you, from the first idea to your return home.</p>
      <div class="btns hero-in">{BTN_DESIGN}<a href="#how" class="btn btn-glass" data-magnetic><span>How it works</span></a></div>
      <div class="hero-chips hero-in"><span class="chip glass">💍 Honeymoons</span><span class="chip glass">🧳 Solo women</span><span class="chip glass">🇰🇷 Korea specialist</span><span class="chip glass">🕌 Halal-friendly</span></div>
    </div>
    <aside class="hero-card glass glass-sheen hero-in">
      <div class="row"><img src="assets/img/k5.jpg" alt="Audrey in Kyoto"><div><b>Hi, I’m Audrey</b><br><small>Founder of K-SOUL · based in South Korea</small></div></div>
      <small>6 years on the road, 50+ countries across 5 continents — now designing yours.</small>
      <span class="stars">★★★★★ <small style="color:var(--text);letter-spacing:0">loved by travelers worldwide</small></span>
    </aside>
  </div>
  <div class="hero-bottom hero-in"><span>HONEYMOONS · SOLO · FAMILIES · KOREA LOVERS</span><span class="scroll-ind"><i></i>SCROLL</span></div>
  <div class="hero-veil"></div>
</section>

<div data-flight data-flight-start="120" style="position:relative">

<section class="section center">
  <div class="container">
    <span class="eyebrow" data-reveal>The K-SOUL way</span>
    <p class="statement" data-words="ideas,inspirations,dream,reality,uniquely,you.">K-SOUL transforms your ideas, inspirations and dream destinations into reality — with personalized trips designed uniquely around you.</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <span class="eyebrow" data-reveal>Why choose K-SOUL</span>
    <h2 class="h2 mt-s" data-split>Travel planned<br>with <em>heart</em> &amp; care</h2>
    <div class="bento" data-stagger>
      <article class="tile tall photo" data-tilt="6" data-cursor="VIEW"><img class="bg" src="assets/img/k5.jpg" alt="Audrey in a kimono at Kinkaku-ji, Kyoto" data-parallax="5"><span class="n">01</span>
        <div class="glass-cap glass-dark"><h3>From Dream To Reality</h3><p>K-SOUL transforms your ideas, inspirations and dream destinations into reality with personalized trips designed uniquely around you.</p></div></article>
      <article class="tile glass" data-tilt="8"><span class="n">02</span><div class="ico"><img src="assets/img/compass.png" alt=""></div>
        <h3>Completely Stress-Free</h3><p>I take care of you from the first planning stages and accompany you throughout your entire journey until your return home.</p></article>
      <article class="tile glass" data-tilt="8"><span class="n">03</span><div class="ico"><img src="assets/img/worldwide.png" alt=""></div>
        <h3>A Journey For Everyone</h3><p>Honeymoons, proposals, family trips, solo adventures, healing escapes, relocating abroad or trips with friends.</p></article>
      <article class="tile wide photo" data-tilt="5" data-cursor="VIEW"><img class="bg" src="assets/img/karst.jpg" alt="Audrey among karst mountains" data-parallax="5"><span class="n">04</span>
        <div class="glass-cap glass-dark" style="max-width:560px"><h3>My Experience</h3><p>Through my personal experience, the locals I work with and trusted partnerships: hidden gems, no tourist traps, selected upgrades and unique opportunities.</p></div></article>
    </div>
  </div>
</section>

{steps_section()}

</div>

<section class="hs" data-hscroll>
  <div class="hs-pin">
    <div class="hs-head">
      <div><span class="eyebrow">Travel with me</span><h2 class="h2 mt-s">Small group trips,<br><em>with soul</em></h2></div>
      <p class="lead">Come as a traveler. Leave with a story. Join Audrey on hand-crafted group journeys.</p>
    </div>
    <div class="hs-track">{trips_cards}
      <a class="trip glass" href="travel-with-me.html" style="display:grid;place-items:center;text-align:center;padding:40px" data-cursor="ALL">
        <div><span class="eyebrow">Coming soon</span><h3 class="h3 mt-s">Italy · Jeju · Kyrgyzstan<br>France · China · Amazon</h3><span class="btn btn-gold mt-m"><span>All trips <i class="arr">→</i></span></span></div></a>
    </div>
  </div>
</section>

{reviews_section()}

<section class="section center">
  <div class="container">
    <span class="eyebrow" data-reveal>Signature experiences</span>
    <h2 class="h2 mt-s" data-split>Special travel &amp; tour<br>services <em>for you</em></h2>
    <div class="pills" data-stagger>{''.join(f'<span class="pill glass"><i>✦</i>{s}</span>' for s in SERVICES)}</div>
  </div>
</section>

{cta('assets/img/hero.jpg', 'Your next chapter', 'You’re <em>ready</em><br>to start?', 'Tell me about the trip you’ve been dreaming of — I’ll take care of everything else.', BTN_DESIGN + BTN_CALL)}
'''

home_module = '<script type="module">\n' + HIB + '\n</script>\n'
home_before = '''<script>
window.KS = window.KS || {};
/* Home: hero intro + scroll scene driving the 3D hibiscus */
(function(){
  const S = window.KSHero;
  document.querySelectorAll('.hero-copy .hl').forEach(h => { h.style.display='inline-block'; h.style.overflow='hidden'; h.style.paddingBottom='.06em'; h.firstElementChild.style.display='inline-block'; });
  addEventListener('mousemove', e => { S.mx = e.clientX / innerWidth - .5; S.my = e.clientY / innerHeight - .5; });
  KS.beforeScenes = function(){
    gsap.timeline({ scrollTrigger:{ trigger:'#hero3d', start:'top top', end:'+=140%', scrub:1, pin:true } })
      .to(S, { p:1, ease:'none', duration:1 }, 0)
      .to('.hero-copy', { y:-120, opacity:0, ease:'power1.in', duration:.35 }, 0)
      .to('.hero-card', { y:-80, opacity:0, duration:.3 }, 0)
      .to('.hero-bottom', { opacity:0, duration:.15 }, 0)
      .to('.hero-veil', { opacity:1, duration:.18, ease:'none' }, .82);
  };
  KS.onStart = function(){
    gsap.to(S, { bloom:1.08, duration:3.2, ease:'power2.out', delay:.6 });
    gsap.from('.hero-copy .hl > span', { yPercent:115, rotate:4, duration:1.5, stagger:.12, ease:'expo.out', delay:.7 });
    gsap.from('.hero-in', { y:40, opacity:0, duration:1.2, stagger:.1, ease:'expo.out', delay:1 });
    gsap.from('.nav', { y:-100, opacity:0, duration:1.2, ease:'expo.out', delay:.9, clearProps:'transform' });
  };
})();
</script>
'''
page('home', 'K-SOUL Travel | Personalized Travel Planning & Itineraries',
     'K-SOUL Travel creates personalized trips and custom itineraries for honeymoons, solo travel, families and Korea lovers.',
     home, extra_head=home_head, before_main=home_before, after_main=home_module)

# ============================== ABOUT ==============================
stops = [('🇲🇦', 'Morocco', 'Born', 'Where my story began.'), ('🇮🇹', 'Italy', 'Raised', 'Where I spent most of my life before starting my journey around the world.'),
         ('🇵🇹', 'Portugal', 'Over 2 years', 'Living abroad for the first time.'), ('🇪🇸', 'Spain', '6 months', 'A different culture and lifestyle.'),
         ('🇯🇵', 'Japan', '4 months', 'Part of almost a year traveling across Asia.'), ('🇹🇭', 'Thailand', '3 months', 'Exploring Southeast Asia.'),
         ('🇮🇩', 'Indonesia', '3 months', 'Islands, temples and connection.'), ('🇰🇷', 'South Korea', 'Now · 2+ years', 'Where I am based today.')]
about = phero(U + '2026/09/IMG_2280-819x1024.jpg', 'About', 'About me', 'Hi, I’m <em>Audrey</em>', 'The founder of K-SOUL.') + f'''
<div data-flight data-flight-start="80" style="position:relative">
<section class="section">
  <div class="container split2">
    <div class="photo-stack" data-reveal="left">
      <img src="{U}2026/09/F67835A1-7ED5-429C-BF4A-A964CD4DBC9D-819x1024.jpeg" alt="Back of an embroidered royal hanbok at a Seoul palace" data-tilt="5">
      <img src="{U}2026/09/BCFE276B-6CF7-47CE-9AA2-6779DB62EA40-819x1024.jpeg" alt="Woman wearing a red and navy hanbok at a palace in Seoul" data-tilt="5">
      <div class="badge glass"><b><span data-count="50">0</span>+</b><span>countries explored</span></div>
    </div>
    <div class="prose" data-reveal="right">
      <span class="eyebrow">About me</span>
      <p>Hi, I’m Audrey — the founder of K-SOUL. I was born in Morocco, raised in Italy, and spent most of my life there before starting my journey around the world.</p>
      <p>Over the years, I’ve lived in different countries and experienced completely different cultures and lifestyles. I lived in Portugal for over 2 years, Spain for 6 months, spent almost 1 year traveling across Asia (4 months in Japan, 3 months in Thailand, and 3 months in Indonesia), and I now live in South Korea, where I’ve been based for more than 2 years.</p>
      <p>I’ve been traveling for the past 6 years and have explored more than 50 countries across 5 continents, mostly as a solo traveler.</p>
      <p>Traveling alone taught me how to adapt anywhere in the world, step outside my comfort zone, connect with people from completely different cultures, and experience destinations beyond the surface.</p>
    </div>
  </div>
  <div class="container stats" data-stagger>
    <div class="stat glass"><b><span data-count="6">0</span><small> yrs</small></b><span>traveling the world</span></div>
    <div class="stat glass"><b><span data-count="50">0</span><small>+</small></b><span>countries explored</span></div>
    <div class="stat glass"><b><span data-count="5">0</span></b><span>continents</span></div>
    <div class="stat glass"><b><span data-count="2">0</span><small>+ yrs</small></b><span>living in South Korea</span></div>
  </div>
</section>
</div>

<section class="hs" data-hscroll>
  <div class="hs-pin">
    <div class="hs-head"><div><span class="eyebrow">My journey</span><h2 class="h2 mt-s">From Morocco<br>to <em>Seoul</em></h2></div><p class="lead">Every place I’ve called home shaped the way I design journeys today.</p></div>
    <div class="journey">{''.join(f'<div class="stop glass{" now" if i == len(stops)-1 else ""}"><span class="flag">{f}</span><h4>{n}</h4><span class="dur">{d}</span><p>{t}</p></div>' for i, (f, n, d, t) in enumerate(stops))}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="big-quote glass" data-reveal="scale">
      <span class="eyebrow">Why K-SOUL</span>
      <p class="mt-m">K-SOUL was created to turn your dream journeys into reality: transforming your ideas, fantasies and travel desires into something <em>personal and unforgettable</em>.</p>
      <small>It’s about creating emotions, memories and experiences that stay with you forever, while making the entire process stress-free.</small>
    </div>
    <div class="split2 mt-l">
      <div class="prose" data-reveal="left"><span class="eyebrow">The story behind it</span>
        <p>The first time I used a traditional travel agency was also my last time.</p>
        <p>I realized something very quickly: expensive packages, generic itineraries, crowded tourist spots and experiences that felt completely disconnected from my passions and desires. Everything felt rushed, copy-paste and without soul.</p>
      </div>
      <div class="laptop" data-reveal="right" style="height:clamp(320px,52vh,520px);position:relative" data-cursor="VIEW"><img src="{U}2026/09/2nd-1024x663.jpeg" alt="Woman in a traditional Korean hanbok at a royal palace in Seoul" style="position:absolute;inset:-8% 0;width:100%;height:116%;object-fit:cover" data-parallax="6"></div>
    </div>
  </div>
</section>
''' + cta(U + '2026/09/happysurd-photography-0J9tKVIQ6Xc-unsplash-683x1024.jpg', 'Your journey', 'Ready to <em>plan</em><br>your trip?', 'Let’s turn your vision into a journey designed entirely around you.', BTN_DESIGN + BTN_CALL)
page('about', 'About Audrey | K-SOUL Travel', 'Meet Audrey, the founder of K-SOUL Travel: 6 years of travel, 50+ countries, now based in South Korea.', about)

# ============================== DESIGN YOUR TRIP ==============================
qs = [('2026/09/haotian-zheng-QQ74Efz14y4-unsplash-683x1024.jpg', 'Planning your honeymoon, a proposal, or a romantic surprise?'),
      ('2026/09/fadhil-abhimantra-XtgZ_TcjYOg-unsplash-819x1024.jpg', 'Traveling solo and looking for a safe, personalized experience?'),
      ('2026/09/ubeyonroad-HpPKRrWaT_Q-unsplash-683x1024.jpg', 'Planning a trip with friends or family and want everything organized perfectly?'),
      ('2026/09/dan-ma-qSzBVbkGGEw-unsplash-1024x630.jpg', 'Looking for a halal-friendly trip tailored to your needs?')]
bens = [('detail', 'Attention to Details', 'I take care of every little detail.'), ('time', 'Save Time & Stress', 'You enjoy the journey, I handle the rest.'),
        ('support', 'Support Every Step', 'I’m with you from start to finish.'), ('star', 'Exclusive Advantages', 'Thanks to my partnerships, you get more.')]
design = phero(U + '2026/09/dan-ma-qSzBVbkGGEw-unsplash-1024x630.jpg', 'Design Your Trip', 'Your dream trip, designed with soul', 'Design <em>your trip</em>',
               'A personalized travel experience designed around you.', f'<a href="{Q}" class="btn btn-gold" data-magnetic><span>Start here <i class="arr">→</i></span></a>') + f'''
<section class="section">
  <div class="container">
    <div class="center"><span class="eyebrow" data-reveal>Is this you?</span><h2 class="h2 mt-s" data-split>Every journey starts<br>with a <em>question</em></h2></div>
    <div class="qgrid" data-stagger>{''.join(f'<a class="qcard" href="{Q}" data-tilt="7" data-cursor="START"><img src="{U}{i}" alt=""><span class="q glass">?</span><div class="glass-dark">{t}</div></a>' for i, t in qs)}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="big-quote glass" data-reveal="scale">
      <img src="assets/img/worldwide.png" alt="" style="width:60px;margin:0 auto 20px">
      <span class="eyebrow">Whatever your dream trip looks like</span>
      <p class="mt-m">If you want someone to design and organize everything for you, from A to Z — from flights, transfers and hotels, to restaurants, experiences and every detail in between — I’m here to turn your vision into reality, <em>completely stress-free</em>.</p>
      <small>With access to trusted partners and exclusive advantages you wouldn’t get on your own.</small>
      <div class="btns mt-m" style="justify-content:center"><a href="{Q}" class="btn btn-gold" data-magnetic><span>Let’s start, design my trip <i class="arr">→</i></span></a></div>
    </div>
  </div>
</section>

{steps_section()}

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="benefits" data-stagger>{''.join(f'<div class="benefit glass glass-sheen" data-tilt="8"><div class="i">{ICON[i]}</div><h4>{h}</h4><p>{p}</p></div>' for i, h, p in bens)}</div>
  </div>
</section>
''' + reviews_section() + cta(U + '2026/09/haotian-zheng-QQ74Efz14y4-unsplash-683x1024.jpg', 'Start here', 'Your dream trip<br>is <em>one form</em> away', 'Tell me about your dream trip, travel style and every detail that matters to you.', BTN_DESIGN + BTN_CALL)
page('design', 'Design Your Trip | K-SOUL Travel', 'A personalized travel experience designed around you: honeymoons, solo travel, families, halal-friendly trips.', design)

# ============================== DIGITAL GUIDES ==============================
cats = [('2026/09/stephan-valentin-wepDTOWs4d0-unsplash-660x1024.jpg', 'Korea', 'After years living in Korea, I created the ultimate collection of guides I wish I had before moving here. Covering itineraries, hidden gems, local favorites, cafés, restaurants, nightlife, shopping, culture, and practical resources that make Korea feel less overwhelming and more authentic.'),
        ('2026/09/wei-jiaheng-O0iAZhikjj4-unsplash-631x1024.jpg', 'Rest of Asia', 'Carefully curated guides to help you explore Asia through unforgettable destinations, authentic experiences, hidden gems, local recommendations, and practical travel advice.'),
        ('2026/09/buddy-an-1wxNINIjJZw-unsplash-683x1024.jpg', 'Women', 'Travel guides for women, created by a woman — designed to help you travel safer, with more confidence, comfort, and peace of mind.'),
        ('2026/08/640AF64F-7E06-4EC7-96D1-0356BAE49558-1024x1013.webp', 'Travel like a pro', 'Smart travel resources designed to help you travel easier, cheaper, and with less stress — from airport hacks and packing guides to volunteering, work exchange, digital nomad life, and long-term travel tips.')]
guides = phero(U + '2026/09/stephan-valentin-wepDTOWs4d0-unsplash-660x1024.jpg', 'Digital Guides', 'Designed with soul', 'Digital <em>guides</em>',
               'Curated travel guides from real experience — 50+ guides to help you travel smarter.', '<a href="#categories" class="btn btn-gold" data-magnetic><span>Explore all guides <i class="arr">↓</i></span></a>') + f'''
<section class="section">
  <div class="container split2">
    <div class="laptop glass" data-reveal="left" style="padding:12px;border-radius:36px" data-tilt="5"><img src="{U}2026/09/454C3F6D-74DE-4103-83C8-8F5780C5808E-1024x576.png" alt="Reading a K-SOUL digital travel guide on a laptop" style="border-radius:26px"></div>
    <div class="prose" data-reveal="right"><span class="eyebrow">What are these guides?</span>
      <p>Carefully curated digital travel guides created from my real travel experience.</p>
      <p>Built from detailed research, local recommendations, and expert-approved resources — designed to help you save time, travel smarter, and plan with less stress. They combine trusted local favorites, hidden gems, curated itineraries, and practical travel resources that are often difficult to find online.</p>
      <p>With <b style="color:var(--green);font-weight:500"><span data-count="50">0</span>+ guides</b> available, you can unlock the ones that best match your destination, travel style, and personal needs.</p>
    </div>
  </div>
  <div class="container pillars" data-stagger>
    <div class="pillar glass" data-tilt="7"><span class="k">✦ Real experience</span><h4>Six years on the road</h4><p>Created from over six years of travel experience, careful research, local recommendations, and firsthand discoveries — expert-approved, local favorites and hidden gems for a more authentic trip.</p></div>
    <div class="pillar glass" data-tilt="7"><span class="k">✦ Save time</span><h4>Everything in one place</h4><p>Plan with less stress, spend less time researching, and travel like a pro.</p></div>
    <div class="pillar glass" data-tilt="7"><span class="k">✦ Made for you</span><h4>Every style &amp; goal</h4><p>Guides for every destination, travel style, budget, and personal goal — short getaways, long-term adventures, solo trips, or moving abroad.</p></div>
  </div>
</section>
<section class="section" id="categories" style="padding-top:0">
  <div class="container">
    <div class="center"><span class="eyebrow" data-reveal>Browse by category</span><h2 class="h2 mt-s" data-split>Find your<br><em>perfect guide</em></h2></div>
    <div class="cats" data-stagger>{''.join(f'<a class="cat" href="{LIVE}/digital-travel-guides/" data-tilt="5" data-cursor="OPEN"><img src="{U}{i}" alt="{n}"><div class="glass-dark"><h3>{n}</h3><p>{t}</p><span class="go">EXPLORE GUIDES →</span></div></a>' for i, n, t in cats)}</div>
  </div>
</section>
''' + cta(U + '2026/09/wei-jiaheng-O0iAZhikjj4-unsplash-631x1024.jpg', 'Need more?', 'Didn’t find <em>exactly</em><br>what you need?', 'Whether you need a fully personalized itinerary, help planning your trip, or simply have travel questions — I’m here to help.', BTN_DESIGN + BTN_CALL)
page('guides', 'Digital Travel Guides | K-SOUL Travel', '50+ curated digital travel guides for Korea, Asia, women travelers and travel like a pro.', guides)

# ============================== TRAVEL WITH ME ==============================
soon = [('2026/09/martinophuc-italy-9505446_1920-681x1024.jpg', 'Italy'), ('2026/09/korea-jeju-7-820x1024.jpg', 'Korea / Jeju Island'), ('2026/09/kirghizistan-7-820x1024.jpg', 'Kyrgyzstan'),
        ('2026/05/daniel-bounliane-3CSx4HNRy4A-unsplash-1-722x1024.webp', 'France'), ('2026/09/china-7-820x1024.jpg', 'China'), ('2026/09/amazon-rainforest-7-820x1024.jpg', 'Amazon Rainforest')]
travel = phero(U + '2026/09/WhatsApp-Image-2026-09-27-at-5.54.30-PM-988x1024.jpeg', 'Travel With Me', 'Small group journeys', 'Travel <em>with me</em>', 'Come as a traveler. Leave with a story.', '<a href="#trips" class="btn btn-gold" data-magnetic><span>Available trips <i class="arr">↓</i></span></a>') + f'''
<section class="section" id="trips">
  <div class="container">
    <div class="center"><span class="eyebrow" data-reveal>Available trips</span><h2 class="h2 mt-s" data-split>Join the next<br><em>adventure</em></h2></div>
    <div class="trips3" data-stagger>{trips_cards.replace('href="travel-with-me.html"', f'href="{LIVE}/travel-with-me-2/"').replace('class="trip"', 'class="trip" data-tilt="6"')}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="container">
    <div class="center"><span class="eyebrow" data-reveal>Coming soon</span><h2 class="h2 mt-s" data-split>Where we’re<br><em>going next</em></h2></div>
    <div class="soon" data-stagger>{''.join(f'<a href="#" data-cursor="SOON"><img src="{U}{i}" alt="{n}"><span class="cs glass">COMING SOON</span><span class="glass-dark">{n.upper()}</span></a>' for i, n in soon)}</div>
  </div>
</section>
<section class="section" style="padding-top:0"><div class="container"><div class="big-quote glass" data-reveal="scale"><p>Let’s explore the world <em>together</em> ♡</p></div></div></section>
''' + reviews_section() + cta(U + '2026/09/patagonia-antarctica-3-921x1024.jpg', 'Travel together', 'Come as a traveler.<br>Leave with a <em>story</em>.', 'Have questions about a group trip? Let’s talk.', BTN_CALL + BTN_DESIGN)
page('travel', 'Travel With Me | K-SOUL Travel', 'Small group trips with Audrey: Kazakhstan, Japan, Patagonia & Antarctica and more.', travel)

# ============================== BOOK A CALL ==============================
flow = ['Tell me what you need help with and provide your basic information.', 'Choose your preferred consultation length and book your call through Calendly.',
        'During our consultation, we will discuss your travel plans, goals, questions, challenges, ideas in detail or anything you need help with.',
        'After the call, you will receive a personalized follow-up email summarizing everything we discussed, including recommendations, next steps and useful resources.']
book = phero('assets/img/korea.jpg', 'Book A Call', 'Not sure where to start?', 'Book your <em>travel consultation</em>', 'Every situation is different, and sometimes it’s simply easier to talk.', '<a href="#calendar" class="btn btn-gold" data-magnetic><span>Choose a time <i class="arr">↓</i></span></a>') + f'''
<section class="section">
  <div class="container split2">
    <div class="prose" data-reveal="left"><span class="eyebrow">Private video consultation</span>
      <p>If you prefer discussing your plans face-to-face, or if you have questions or doubts, you’re welcome to book a private video consultation with me.</p>
      <p>Whether you want help planning a trip, need guidance with a visa application, are thinking about relocating to another country, would like to discuss your itinerary in person, or simply want my advice and recommendations, we’ll go through everything together.</p>
      <p>During our call, I will answer all your questions and help you find the best solution for your situation. Simply choose a date and time on the calendar to get started. See you soon! ✨</p>
    </div>
    <div class="photo-stack" data-reveal="right">
      <img src="assets/img/k5.jpg" alt="Audrey in Kyoto" data-tilt="5"><img src="assets/img/k3.jpg" alt="Friends at a Korean sauna" data-tilt="5">
      <div class="badge glass"><b>1:1</b><span>video call with Audrey</span></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="container">
    <div class="center"><span class="eyebrow" data-reveal>How it works</span><h2 class="h2 mt-s" data-split>Four simple<br><em>steps</em></h2></div>
    <div class="flow4" data-stagger>{''.join(f'<div class="f glass" data-tilt="7"><b>{i+1:02d}</b><p>{t}</p></div>' for i, t in enumerate(flow))}</div>
  </div>
</section>
<section class="section" id="calendar" style="padding-top:0">
  <div class="container">
    <div class="center"><span class="eyebrow" data-reveal>Choose a date</span><h2 class="h2 mt-s" data-split>Book your<br><em>call</em></h2></div>
    <div class="cal-wrap glass" data-reveal="scale"><div class="calendly-inline-widget" data-url="{CAL}?hide_gdpr_banner=1&primary_color=c59a32"></div></div>
    <p class="note glass">When you proceed with your Calendly booking, you will find two additional mandatory questions where you can provide more details about your situation, travel plans, goals, or the assistance you need before our consultation.</p>
  </div>
</section>
'''
page('book', 'Book a Travel Consultation | K-SOUL Travel', 'Book a private video consultation with Audrey for trip planning, visas, relocation or itinerary advice.', book,
     after_main='<script src="https://assets.calendly.com/assets/external/widget.js" async></script>\n')

# ============================== CONTACT ==============================
chans = [('mail', 'Email', 'info.ksoultravel@gmail.com', 'mailto:info.ksoultravel@gmail.com'), ('ig', 'K-SOUL Instagram', '@ksoultravel', 'https://www.instagram.com/ksoultravel'),
         ('ig', 'Personal Instagram', '@iamaudreymartin', 'https://www.instagram.com/iamaudreymartin'), ('yt', 'YouTube', 'youtube.com/@audreymartin', 'https://youtube.com/@audreymartin'),
         ('tt', 'TikTok', '@iamaudreymartin', 'https://www.tiktok.com/@iamaudreymartin')]
contact = phero(U + '2026/08/8AB1390A-6BCC-406B-8289-98928E8B2807-1536x1229-1-1024x819.webp', 'Contact', 'Get in touch', 'Let’s plan your <em>next adventure</em> together',
                'Whether you’re dreaming about Korea, Japan, a luxury honeymoon, a solo adventure or a once-in-a-lifetime journey… I’m here to help you create a trip that truly feels like you.') + f'''
<section class="section">
  <div class="container">
    <span class="eyebrow" data-reveal>General questions &amp; business partnerships</span>
    <div class="channels" data-stagger>{''.join(f'<a class="ch glass glass-sheen" href="{h}"{"" if h.startswith("mailto") else " target=\"_blank\" rel=\"noopener\""}><span class="i">{ICON[i]}</span><small>{l}</small><b>{v}</b></a>' for i, l, v, h in chans)}</div>
    <div class="two">
      <div class="box glass" data-reveal="left"><span class="eyebrow">Have questions?</span><h3 class="h3 mt-s">Let’s talk one-on-one</h3><p>Want to talk face-to-face, ask for advice, or simply understand where to start? No matter what your question is, we can talk one-on-one and plan everything together.</p><div class="btns mt-m">{BTN_CALL_L}</div></div>
      <div class="box dark glass" data-reveal="right"><span class="eyebrow" style="color:var(--gold-soft)">Ready to start planning?</span><h3 class="h3 mt-s">Send your travel request</h3><p>Fill out the travel questionnaire and send your request. I’ll personally reply by email with:</p>
        <ul><li>a first itinerary draft</li><li>estimated costs</li><li>timing</li><li>ideas &amp; recommendations</li><li>everything you need to get started</li></ul>{BTN_DESIGN}</div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="container split2" style="align-items:start">
    <div data-reveal="left"><span class="eyebrow">Send your request</span><h2 class="h2 mt-s">Write to <em>me</em></h2>
      <p class="lead mt-m">For collaborations, partnerships, media inquiries or general questions, feel free to contact me here. If your question is not already answered in the <a href="{LIVE}/faq/" style="color:var(--gold-2);text-decoration:underline">FAQ</a>, you can briefly send it through this form.</p>
      <p class="note glass">For personalized itinerary requests, destination planning, travel organization or detailed trip assistance, please fill out the <a href="{Q}" style="color:var(--gold-2);text-decoration:underline">Design My Trip questionnaire</a> instead.</p></div>
    <form class="form glass" data-demo data-reveal="right">
      <div class="field"><input id="n" type="text" placeholder=" " required><label for="n">Name</label></div>
      <div class="field"><input id="e" type="email" placeholder=" " required><label for="e">Email</label></div>
      <div class="field"><textarea id="m" placeholder=" " required></textarea><label for="m">Message</label></div>
      <button class="btn btn-gold" type="submit" style="justify-self:start" data-magnetic><span>Send request <i class="arr">→</i></span></button>
      <p class="form-msg">Thank you ✦ This demo form must be connected to your WordPress form plugin before going live.</p>
    </form>
  </div>
</section>
'''
page('contact', 'Contact | K-SOUL Travel', 'Contact K-SOUL Travel for questions, partnerships or to start planning your trip.', contact)

# ============================== BLOG ==============================
countries = [('🇩🇴', 'Dominican Republic', 'assets/img/beach.jpg'), ('🇫🇷', 'France', U + '2026/05/daniel-bounliane-3CSx4HNRy4A-unsplash-1-722x1024.webp'),
             ('🇮🇹', 'Italy', U + '2026/09/martinophuc-italy-9505446_1920-681x1024.jpg'), ('🇯🇵', 'Japan', U + '2026/09/wei-jiaheng-O0iAZhikjj4-unsplash-631x1024.jpg'),
             ('🇲🇽', 'Mexico', ''), ('🇲🇦', 'Morocco', ''), ('🇰🇷', 'South Korea', 'assets/img/korea.jpg'), ('🇪🇸', 'Spain', ''),
             ('🇹🇭', 'Thailand', ''), ('🇹🇷', 'Turkey', ''), ('🇦🇪', 'UAE', '')]
grads = ['linear-gradient(160deg,#0E4535,#2F7A5A)', 'linear-gradient(160deg,#B8174E,#F4A7B9)', 'linear-gradient(160deg,#B88A2A,#E7CC8A)', 'linear-gradient(160deg,#022A23,#0E4535 60%,#C59A32)']
def ccard(i, f, n, img):
    bg = f'<img src="{img}" alt="{n}">' if img else f'<div class="grad" style="background:{grads[i % len(grads)]}"></div><div style="position:absolute;inset:0;display:grid;place-items:center;font-size:7rem;opacity:.9">{f}</div>'
    return f'<a class="country" href="{LIVE}/blog/" data-tilt="7" data-cursor="READ">{bg}{"<span class=\"flag\">" + f + "</span>" if img else ""}<div class="glass-dark"><h3>{n}</h3><span class="arrow">→</span></div></a>'
blog = phero(U + '2026/09/happysurd-photography-0J9tKVIQ6Xc-unsplash-683x1024.jpg', 'Blog', 'Travel blogs', 'Travel blogs &amp; <em>practical tips</em>',
             'I’ve personally written these articles to help you get to know each country before you go.') + f'''
<section class="section">
  <div class="container">
    <div class="big-quote glass" data-reveal="scale"><p>Inside, you’ll find my own <em>travel experiences</em>, interesting facts, practical advice, activities to try, scams to watch out for and important things to remember before you leave.</p>
      <small>Choose a destination below to explore the articles and find inspiration for your next trip.</small></div>
    <div class="countries" data-stagger>{''.join(ccard(i, *c) for i, c in enumerate(countries))}</div>
  </div>
</section>
''' + cta('assets/img/k7.jpg', 'Inspired?', 'Turn reading into<br><em>travelling</em>', 'Let me design a trip around the places you love.', BTN_DESIGN + BTN_CALL)
page('blog', 'Travel Blogs & Practical Tips | K-SOUL Travel', 'Travel blogs and practical tips by Audrey for Korea, Japan, Italy, France and more.', blog)
print('built', [f for _, f, _ in PAGES])

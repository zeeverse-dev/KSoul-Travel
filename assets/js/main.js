/* =====================================================================
   K-SOUL TRAVEL — shared interactions
   Needs: gsap, ScrollTrigger, Lenis (loaded before this file)
   ===================================================================== */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const isTouch = matchMedia('(hover:none)').matches;
  const reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;
  gsap.registerPlugin(ScrollTrigger);
  window.KS = window.KS || {};

  /* ---------- smooth scroll ---------- */
  const lenis = new Lenis({ lerp: .085, smoothWheel: true });
  KS.lenis = lenis;
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add(t => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);

  /* ---------- year ---------- */
  $$('[data-year]').forEach(e => e.textContent = new Date().getFullYear());

  /* ---------- page transition curtain ---------- */
  const curtain = $('.curtain');
  const panel = curtain && $('.panel', curtain), cflower = curtain && $('.flower', curtain), cword = curtain && $('.word', curtain);
  function enter() {
    if (!curtain) return;
    const tl = gsap.timeline();
    tl.to(cflower, { scale: .6, opacity: 0, rotate: 60, duration: .6, ease: 'power3.in' })
      .to(cword, { opacity: 0, duration: .3 }, 0)
      .to(panel, { yPercent: -100, duration: 1, ease: 'expo.inOut' }, .2)
      .set(curtain, { display: 'none' });
    return tl;
  }
  function leave(href) {
    if (!curtain) { location.href = href; return; }
    gsap.set(curtain, { display: 'grid' });
    gsap.timeline({ onComplete: () => location.href = href })
      .fromTo(panel, { yPercent: 100 }, { yPercent: 0, duration: .8, ease: 'expo.inOut' })
      .fromTo(cflower, { scale: .4, opacity: 0, rotate: -60 }, { scale: 1, opacity: 1, rotate: 0, duration: .6, ease: 'expo.out' }, .45)
      .to(cword, { opacity: 1, duration: .3 }, .5);
  }
  $$('a[href]').forEach(a => {
    const h = a.getAttribute('href');
    if (!h || h.startsWith('#') || h.startsWith('mailto:') || h.startsWith('tel:') || a.target === '_blank' || /^https?:/.test(h)) return;
    a.addEventListener('click', e => { if (e.metaKey || e.ctrlKey) return; e.preventDefault(); leave(a.href); });
  });
  addEventListener('pageshow', e => { if (e.persisted && curtain) gsap.set(curtain, { display: 'none' }); });
  $$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
    const t = $(a.getAttribute('href')); if (t) { e.preventDefault(); lenis.scrollTo(t, { offset: -30, duration: 1.6 }); }
  }));

  /* ---------- nav ---------- */
  const nav = $('.nav'), burger = $('.burger'), mmenu = $('.mmenu');
  if (burger) burger.addEventListener('click', () => {
    burger.classList.toggle('open'); mmenu.classList.toggle('open');
    mmenu.classList.contains('open') ? lenis.stop() : lenis.start();
    if (mmenu.classList.contains('open')) gsap.from($$('a', mmenu), { y: 40, opacity: 0, stagger: .05, duration: .8, ease: 'expo.out', delay: .2 });
  });
  let lastY = 0;
  lenis.on('scroll', ({ scroll }) => {
    if (nav && !(mmenu && mmenu.classList.contains('open'))) nav.classList.toggle('hide', scroll > lastY && scroll > 260);
    lastY = scroll;
  });
  gsap.to('#progress', { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: .3 } });

  /* ---------- cursor ---------- */
  if (!isTouch) {
    const cur = $('.cursor'), dot = $('.cursor-dot');
    if (cur) {
      const lbl = $('b', cur);
      const cx = gsap.quickTo(cur, 'x', { duration: .45, ease: 'power3' }), cy = gsap.quickTo(cur, 'y', { duration: .45, ease: 'power3' });
      const dx = gsap.quickTo(dot, 'x', { duration: .08 }), dy = gsap.quickTo(dot, 'y', { duration: .08 });
      addEventListener('mousemove', e => { cx(e.clientX); cy(e.clientY); dx(e.clientX); dy(e.clientY); });
      $$('[data-cursor]').forEach(el => {
        el.addEventListener('mouseenter', () => { cur.classList.add('big'); lbl.textContent = el.dataset.cursor; });
        el.addEventListener('mouseleave', () => cur.classList.remove('big'));
      });
      $$('a,button,input,textarea').forEach(el => {
        el.addEventListener('mouseenter', () => { if (!cur.classList.contains('big')) gsap.to(cur, { scale: 1.45, duration: .3 }); });
        el.addEventListener('mouseleave', () => gsap.to(cur, { scale: 1, duration: .3 }));
      });
    }
  }

  /* ---------- text helpers ---------- */
  $$('[data-split]').forEach(el => {
    el.innerHTML = el.innerHTML.split(/<br\s*\/?>/i).map(l => `<span class="ln"><span>${l}</span></span>`).join('');
  });
  $$('[data-words]').forEach(el => {
    const g = (el.dataset.words || '').split(',').map(s => s.trim().toLowerCase()).filter(Boolean);
    el.innerHTML = el.textContent.trim().split(/\s+/).map(w => {
      const k = w.toLowerCase().replace(/[^a-zÀ-ɏ-]/g, '');
      return `<span class="w${g.includes(k) ? ' g' : ''}">${w}</span>`;
    }).join(' ');
  });

  /* ---------- 3D tilt + glare ---------- */
  if (!isTouch) $$('[data-tilt]').forEach(c => {
    const amt = +c.dataset.tilt || 10;
    if (!$('.glare', c)) { const g = document.createElement('span'); g.className = 'glare'; c.appendChild(g); }
    const rx = gsap.quickTo(c, 'rotateX', { duration: .7, ease: 'power3' }), ry = gsap.quickTo(c, 'rotateY', { duration: .7, ease: 'power3' });
    c.addEventListener('mousemove', e => {
      const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
      ry((x - .5) * amt * 2); rx((.5 - y) * amt * 2);
      c.style.setProperty('--mx', x * 100 + '%'); c.style.setProperty('--my', y * 100 + '%');
    });
    c.addEventListener('mouseleave', () => { rx(0); ry(0); });
  });

  /* ---------- magnetic ---------- */
  if (!isTouch) $$('[data-magnetic]').forEach(b => {
    const mx = gsap.quickTo(b, 'x', { duration: .6, ease: 'elastic.out(1,.4)' }), my = gsap.quickTo(b, 'y', { duration: .6, ease: 'elastic.out(1,.4)' });
    b.addEventListener('mousemove', e => { const r = b.getBoundingClientRect(); mx((e.clientX - r.left - r.width / 2) * .3); my((e.clientY - r.top - r.height / 2) * .4); });
    b.addEventListener('mouseleave', () => { mx(0); my(0); });
  });

  /* ---------- falling hibiscus petals (2D, inner heroes) ---------- */
  $$('canvas[data-petals]').forEach(cv => {
    const ctx = cv.getContext('2d'); let W, H, P = [];
    const cols = ['#F4A7B9', '#F8D3DD', '#E88AA3', '#FFFFFF', '#E7CC8A'];
    const fit = () => { const d = Math.min(devicePixelRatio, 2); W = cv.clientWidth; H = cv.clientHeight; cv.width = W * d; cv.height = H * d; ctx.setTransform(d, 0, 0, d, 0, 0); };
    fit(); addEventListener('resize', fit);
    const N = innerWidth < 700 ? 22 : 46;
    for (let i = 0; i < N; i++) P.push({ x: Math.random() * W, y: Math.random() * H, s: 6 + Math.random() * 10, vy: .3 + Math.random() * .7, vx: .2 + Math.random() * .5, r: Math.random() * 6, vr: (Math.random() - .5) * .04, f: Math.random() * 6, c: cols[i % cols.length], o: .55 + Math.random() * .4 });
    let vis = true; new IntersectionObserver(([e]) => vis = e.isIntersecting).observe(cv);
    (function loop() {
      requestAnimationFrame(loop); if (!vis) return;
      ctx.clearRect(0, 0, W, H);
      P.forEach(p => {
        p.y += p.vy; p.x += p.vx + Math.sin(p.f += .02) * .4; p.r += p.vr;
        if (p.y > H + 20) { p.y = -20; p.x = Math.random() * W; } if (p.x > W + 20) p.x = -20;
        ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.r); ctx.scale(1, Math.abs(Math.sin(p.f)) * .6 + .4);
        ctx.globalAlpha = p.o; ctx.fillStyle = p.c; ctx.beginPath();
        ctx.moveTo(0, -p.s); ctx.bezierCurveTo(p.s * .9, -p.s * .7, p.s * .7, p.s * .6, 0, p.s); ctx.bezierCurveTo(-p.s * .7, p.s * .6, -p.s * .9, -p.s * .7, 0, -p.s);
        ctx.fill(); ctx.restore();
      });
    })();
  });

  /* ---------- flight path: the logo's golden swoosh flies through the page ---------- */
  function buildFlight() {
    const host = $('[data-flight]'); if (!host) return;
    const old = $('.flight', host); if (old) old.remove();
    const W = host.clientWidth, H = host.scrollHeight;
    const ns = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(ns, 'svg'); svg.setAttribute('class', 'flight'); svg.setAttribute('width', W); svg.setAttribute('height', H); svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
    const startY = +(host.dataset.flightStart || innerHeight * .9);
    const seg = 820; let d = `M ${W * .1} ${startY}`; let side = 1, y = startY;
    while (y < H - 300) { const ny = Math.min(y + seg, H - 200); const x = side > 0 ? W * .92 : W * .08; d += ` C ${side > 0 ? W * .1 : W * .9} ${y + seg * .55}, ${side > 0 ? W * .95 : W * .05} ${ny - seg * .6}, ${x} ${ny}`; y = ny; side *= -1; }
    const defs = document.createElementNS(ns, 'defs'), mask = document.createElementNS(ns, 'mask'); mask.id = 'flightMask';
    const mr = document.createElementNS(ns, 'rect'); mr.setAttribute('width', W); mr.setAttribute('height', H); mr.setAttribute('fill', '#000');
    const mp = document.createElementNS(ns, 'path'); mp.setAttribute('d', d); mp.setAttribute('class', 'mask'); mp.setAttribute('stroke', '#fff');
    mask.append(mr, mp); defs.append(mask); svg.append(defs);
    const trail = document.createElementNS(ns, 'path'); trail.setAttribute('d', d); trail.setAttribute('class', 'trail'); trail.setAttribute('mask', 'url(#flightMask)'); svg.append(trail);
    const plane = document.createElementNS(ns, 'g'); plane.innerHTML = '<path class="plane" d="M2 11.5 9 10l4.5-8h2.2L13.4 10H19l2-3h1.6l-1.1 5 1.1 5H21l-2-3h-5.6l2.3 8h-2.2L9 14l-7-1.5z" transform="translate(-12 -12) scale(1.3)"/>';
    svg.append(plane); host.prepend(svg);
    const L = mp.getTotalLength(); mp.style.strokeDasharray = L; mp.style.strokeDashoffset = L;
    const st = { p: 0 };
    const draw = () => { const l = L * st.p; mp.style.strokeDashoffset = L - l; const a = mp.getPointAtLength(Math.max(l, .1)), b = mp.getPointAtLength(Math.min(l + 2, L)); const ang = Math.atan2(b.y - a.y, b.x - a.x) * 180 / Math.PI; plane.setAttribute('transform', `translate(${a.x} ${a.y}) rotate(${ang})`); };
    draw();
    if (KS.flightST) KS.flightST.kill();
    KS.flightST = ScrollTrigger.create({ trigger: host, start: 'top top', end: 'bottom bottom', scrub: 1, onUpdate: s => { st.p = s.progress; draw(); } });
  }

  /* ---------- reveals & scroll scenes ---------- */
  function scenes() {
    $$('[data-split]').forEach(el => gsap.from($$('.ln>span', el), { yPercent: 112, rotate: 3, duration: 1.4, stagger: .1, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 86%' } }));
    $$('[data-reveal]').forEach(el => {
      const kind = el.dataset.reveal;
      const from = kind === 'scale' ? { scale: .86, opacity: 0 } : kind === 'flip' ? { rotateX: -35, y: 120, opacity: 0, transformOrigin: '50% 100%' } : kind === 'left' ? { x: -80, opacity: 0 } : kind === 'right' ? { x: 80, opacity: 0 } : { y: 60, opacity: 0 };
      gsap.from(el, { ...from, duration: 1.4, ease: 'expo.out', delay: +(el.dataset.delay || 0), scrollTrigger: { trigger: el, start: 'top 88%' } });
    });
    $$('[data-stagger]').forEach(g => gsap.from(g.children, { y: 90, rotateX: -25, opacity: 0, transformOrigin: '50% 100%', duration: 1.4, stagger: .09, ease: 'expo.out', scrollTrigger: { trigger: g, start: 'top 85%' } }));
    $$('[data-words]').forEach(el => {
      gsap.to($$('.w', el), { opacity: 1, stagger: .06, ease: 'none', scrollTrigger: { trigger: el, start: 'top 82%', end: 'bottom 45%', scrub: true } });
    });
    $$('[data-parallax]').forEach(img => {
      const a = +(img.dataset.parallax || 10);
      gsap.fromTo(img, { yPercent: -a }, { yPercent: a, ease: 'none', scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true } });
    });
    $$('[data-count]').forEach(el => {
      const to = +el.dataset.count; const o = { v: 0 };
      gsap.to(o, { v: to, duration: 2, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 90%' }, onUpdate: () => el.textContent = Math.round(o.v) });
    });

    /* inner page hero: image settles, glass card lifts */
    const ph = $('.phero');
    if (ph) {
      gsap.to($('.bg', ph), { scale: 1, duration: 2.4, ease: 'expo.out', delay: .3 });
      gsap.from($$('.phero-card > *', ph), { y: 50, opacity: 0, duration: 1.3, stagger: .1, ease: 'expo.out', delay: .5 });
      gsap.from('.phero-card', { y: 80, scale: .94, opacity: 0, duration: 1.5, ease: 'expo.out', delay: .35 });
      gsap.to($('.bg', ph), { yPercent: 18, ease: 'none', scrollTrigger: { trigger: ph, start: 'top top', end: 'bottom top', scrub: true } });
      gsap.to('.phero-card', { y: -90, ease: 'none', scrollTrigger: { trigger: ph, start: 'top top', end: 'bottom top', scrub: true } });
    }

    /* Apple-style sticky steps */
    $$('[data-steps]').forEach(w => {
      const steps = $$('.step', w), imgs = $$('.steps-visual img', w), bars = $$('.steps-bar b', w), big = $('.steps-visual .big', w), lbl = $('.steps-visual .lbl', w);
      const set = i => {
        steps.forEach((s, k) => s.classList.toggle('on', k === i));
        imgs.forEach((im, k) => im.classList.toggle('on', k === i));
        if (big) big.textContent = String(i + 1).padStart(2, '0');
        if (lbl) lbl.textContent = $('h3', steps[i]).textContent;
      };
      steps.forEach((s, i) => ScrollTrigger.create({ trigger: s, start: 'top 60%', end: 'bottom 60%', onToggle: e => e.isActive && set(i),
        onUpdate: e => { bars.forEach((b, k) => b.style.width = k < i ? '100%' : k === i ? e.progress * 100 + '%' : '0%'); } }));
      set(0);
    });

    /* horizontal pinned tracks */
    $$('[data-hscroll]').forEach(sec => {
      const track = $('.hs-track', sec) || $('.journey', sec); if (!track) return;
      const dist = () => Math.max(0, track.scrollWidth - innerWidth);
      const tw = gsap.to(track, { x: () => -dist(), ease: 'none', scrollTrigger: { trigger: sec, start: 'top top', end: () => '+=' + dist(), scrub: 1, pin: true, invalidateOnRefresh: true } });
      $$(':scope > *', track).forEach(c => gsap.fromTo(c, { rotateY: -28, z: -160, opacity: .35 }, { rotateY: 0, z: 0, opacity: 1, ease: 'none', scrollTrigger: { trigger: c, containerAnimation: tw, start: 'left 100%', end: 'left 60%', scrub: true } }));
    });

    /* CTA circle reveal */
    $$('[data-circle]').forEach(sec => {
      gsap.timeline({ scrollTrigger: { trigger: sec, start: 'top top', end: '+=110%', scrub: 1, pin: true } })
        .to($('.cta-media', sec), { clipPath: 'circle(80% at 50% 50%)', ease: 'none' }, 0)
        .to($('.cta-media img', sec), { scale: 1, ease: 'none' }, 0)
        .from($('.cta-box', sec), { y: 120, scale: .9, opacity: 0, ease: 'power2.out', duration: .5 }, .35);
    });

    /* footer big word */
    gsap.from('.footer .big', { yPercent: 50, opacity: 0, ease: 'none', scrollTrigger: { trigger: '.footer', start: 'top bottom', end: 'bottom bottom', scrub: true } });

    buildFlight();
    let rt; addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(buildFlight, 300); });
  }

  /* ---------- forms (front-end only) ---------- */
  $$('form[data-demo]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const m = $('.form-msg', f) || f.nextElementSibling; if (m) { m.style.display = 'block'; }
    f.reset();
  }));

  /* ---------- start ---------- */
  function start() {
    enter();
    if (KS.beforeScenes) KS.beforeScenes();
    if (!reduce) scenes(); else buildFlight();
    if (KS.onStart) KS.onStart();
    ScrollTrigger.sort();
    setTimeout(() => { ScrollTrigger.sort(); ScrollTrigger.refresh(); }, 600);
  }
  start();
  addEventListener('load', () => { ScrollTrigger.refresh(); buildFlight(); });
})();

/* =====================================================================
   K-SOUL — 3D glass Mugunghwa (hibiscus) from the logo
   Three.js r160 · MeshPhysicalMaterial transmission ("glass")
   Reads shared state from window.KSHero = {bloom, p, mx, my}
   ===================================================================== */
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const canvas = document.getElementById('flowerCanvas');
if (canvas) {
  const S = window.KSHero || (window.KSHero = { bloom: 0, p: 0, mx: 0, my: 0 });
  const mobile = innerWidth < 980;
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(devicePixelRatio, mobile ? 1.5 : 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;
  renderer.outputColorSpace = THREE.SRGBColorSpace;

  const scene = new THREE.Scene();
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(renderer), .04).texture;

  const camera = new THREE.PerspectiveCamera(30, 1, .1, 100);
  camera.position.set(0, 0, 10);

  /* ---- living aurora backdrop (also what the glass refracts) ---- */
  const bgMat = new THREE.ShaderMaterial({
    uniforms: { t: { value: 0 }, c: { value: new THREE.Vector2(.68, .5) }, asp: { value: 1 } },
    vertexShader: `varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position.xy, .9999, 1.); }`,
    fragmentShader: `
      uniform float t; uniform vec2 c; uniform float asp; varying vec2 vUv;
      float blob(vec2 uv, vec2 p, float r){ vec2 d = uv - p; d.x *= asp; return smoothstep(r, 0., length(d)); }
      void main(){
        vec2 uv = vUv;
        vec3 col = vec3(.984,.972,.953);
        col = mix(col, vec3(.976,.80,.85), .70*blob(uv, c + vec2(.10+.05*sin(t*.21), .12+.05*cos(t*.17)), .55));
        col = mix(col, vec3(.80,.89,.85),  .65*blob(uv, vec2(.18+.06*cos(t*.19), .22+.07*sin(t*.23)), .60));
        col = mix(col, vec3(.96,.88,.68),  .55*blob(uv, vec2(.92+.04*cos(t*.13), .86+.05*sin(t*.2)), .45));
        col = mix(col, vec3(.06,.30,.23),  .55*blob(uv, c + vec2(-.06+.03*sin(t*.3), -.08), .26));
        col = mix(col, vec3(.85,.34,.50),  .45*blob(uv, c + vec2(.08, .10+.03*cos(t*.27)), .18));
        float g = fract(sin(dot(uv*900., vec2(12.9898,78.233)))*43758.5453);
        col += (g-.5)*.018;
        gl_FragColor = vec4(col, 1.);
      }`,
    depthWrite: false, depthTest: false, toneMapped: false
  });
  const bg = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), bgMat);
  bg.frustumCulled = false; bg.renderOrder = -10; scene.add(bg);

  /* ---- petal: parametric ruffled cup ---- */
  const heart = new THREE.Color('#B8174E'), pink = new THREE.Color('#F49AB4'), edge = new THREE.Color('#FFE4EC');
  function petalGeometry(len = 1.9) {
    const g = new THREE.PlaneGeometry(1, 1, 30, 40);
    const p = g.attributes.position, cols = [];
    const c = new THREE.Color();
    for (let i = 0; i < p.count; i++) {
      const u = p.getX(i) + .5, v = p.getY(i) + .5, xn = (u - .5) * 2;
      const w = .07 + (v < .56 ? 1.02 * Math.pow(Math.sin(Math.PI / 2 * v / .56), .85) : 1.02 * Math.sqrt(Math.max(0, 1 - Math.pow((v - .56) / .46, 2))));
      const x = xn * w;
      const y = v * len;
      const z = -(.62 * v * v) + .30 * xn * xn * v
        + .07 * Math.sin(xn * 6.5 + v * 5) * Math.pow(v, 2.4)
        + .045 * Math.sin(xn * 15 + 1.3) * Math.pow(v, 4);
      p.setXYZ(i, x, y, z);
      c.copy(heart).lerp(pink, THREE.MathUtils.smoothstep(v, .02, .36));
      c.lerp(edge, THREE.MathUtils.smoothstep(v, .72, 1.0) * .7);
      // veins
      const vein = Math.pow(Math.abs(Math.sin(xn * 9)), 18) * (1 - v) * .25;
      c.lerp(heart, vein);
      cols.push(c.r, c.g, c.b);
    }
    g.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3));
    g.computeVertexNormals();
    return g;
  }
  const glass = new THREE.MeshPhysicalMaterial({
    vertexColors: true, transmission: .9, roughness: .14, thickness: .9, ior: 1.42,
    iridescence: .55, iridescenceIOR: 1.25, clearcoat: 1, clearcoatRoughness: .08,
    sheen: .5, sheenColor: new THREE.Color('#ffd6e2'), sheenRoughness: .4,
    attenuationColor: new THREE.Color('#f39ab5'), attenuationDistance: 2.2,
    side: THREE.DoubleSide, envMapIntensity: 1.25, transparent: false
  });

  const flower = new THREE.Group(); scene.add(flower);
  const petals = [];
  const pg = petalGeometry();
  for (let i = 0; i < 5; i++) {
    const pivot = new THREE.Group();
    pivot.rotation.y = i * Math.PI * 2 / 5 + (i % 2 ? .05 : -.04);
    const m = new THREE.Mesh(pg, glass);
    m.rotation.z = .22;                      // pinwheel overlap like a real hibiscus
    pivot.add(m); flower.add(pivot);
    petals.push({ pivot, m, d: i * .08 });
  }

  /* ---- staminal column + anthers + stigma ---- */
  const curve = new THREE.CatmullRomCurve3([new THREE.Vector3(0, 0, 0), new THREE.Vector3(.04, .5, .02), new THREE.Vector3(.12, 1.05, .06), new THREE.Vector3(.26, 1.55, .1)]);
  const column = new THREE.Mesh(new THREE.TubeGeometry(curve, 40, .04, 10, false),
    new THREE.MeshPhysicalMaterial({ color: '#E04C7E', roughness: .3, clearcoat: 1, transmission: .3, thickness: .3 }));
  flower.add(column);
  const anther = new THREE.MeshPhysicalMaterial({ color: '#F2C14E', roughness: .35, metalness: .2, clearcoat: .6 });
  const sG = new THREE.SphereGeometry(.035, 10, 10);
  for (let i = 0; i < 46; i++) {
    const t = .55 + Math.random() * .38, pt = curve.getPoint(t);
    const a = Math.random() * Math.PI * 2, r = .07 + Math.random() * .07;
    const s = new THREE.Mesh(sG, anther); s.position.set(pt.x + Math.cos(a) * r, pt.y + (Math.random() - .5) * .05, pt.z + Math.sin(a) * r);
    s.scale.setScalar(.7 + Math.random() * .6); flower.add(s);
  }
  const stig = new THREE.MeshPhysicalMaterial({ color: '#A3123F', roughness: .25, clearcoat: 1 });
  const top = curve.getPoint(1);
  for (let i = 0; i < 5; i++) {
    const a = i / 5 * Math.PI * 2; const s = new THREE.Mesh(new THREE.SphereGeometry(.055, 14, 14), stig);
    s.position.set(top.x + Math.cos(a) * .09, top.y + .05, top.z + Math.sin(a) * .09); flower.add(s);
  }

  /* ---- two glass leaves ---- */
  function leafGeometry() {
    const g = new THREE.PlaneGeometry(1, 1, 16, 30); const p = g.attributes.position;
    for (let i = 0; i < p.count; i++) {
      const u = p.getX(i) + .5, v = p.getY(i) + .5, xn = (u - .5) * 2;
      const w = .42 * Math.sin(Math.PI * Math.pow(v, .9));
      p.setXYZ(i, xn * w, v * 2.1, -.18 * xn * xn + .1 * Math.sin(v * 3) + .03 * Math.sin(xn * 20) * w);
    }
    g.computeVertexNormals(); return g;
  }
  const leafMat = new THREE.MeshPhysicalMaterial({ color: '#2F7A5A', transmission: .75, roughness: .2, thickness: .6, ior: 1.4, clearcoat: 1, attenuationColor: new THREE.Color('#0E4535'), attenuationDistance: 1.4, side: THREE.DoubleSide, envMapIntensity: 1.1 });
  const lg = leafGeometry();
  [[2.6, 1.42, 1.5], [4.3, 1.38, 1.35]].forEach(([ry, rx, sc]) => {
    const piv = new THREE.Group(); piv.rotation.y = ry; const l = new THREE.Mesh(lg, leafMat);
    l.rotation.x = rx; l.scale.setScalar(sc * .6); l.position.y = -.12; piv.add(l); flower.add(piv);
  });

  /* ---- gold sparkles ✦ (logo star) ---- */
  const starShape = new THREE.Shape();
  for (let i = 0; i < 8; i++) { const a = i / 8 * Math.PI * 2 - Math.PI / 2, r = i % 2 ? .28 : 1; i ? starShape.lineTo(Math.cos(a) * r, Math.sin(a) * r) : starShape.moveTo(Math.cos(a) * r, Math.sin(a) * r); }
  const starGeo = new THREE.ExtrudeGeometry(starShape, { depth: .12, bevelEnabled: true, bevelThickness: .06, bevelSize: .05, bevelSegments: 2 });
  starGeo.center();
  const goldMat = new THREE.MeshPhysicalMaterial({ color: '#D7A93E', metalness: 1, roughness: .18, clearcoat: 1 });
  const stars = [];
  for (let i = 0; i < (mobile ? 10 : 18); i++) {
    const s = new THREE.Mesh(starGeo, goldMat);
    const a = Math.random() * Math.PI * 2, r = 2.2 + Math.random() * 2.4;
    s.position.set(Math.cos(a) * r, Math.sin(a) * r * .7, -1.5 + Math.random() * 2.5);
    s.scale.setScalar(.05 + Math.random() * .09); s.userData = { sp: .3 + Math.random() * .8, ph: Math.random() * 6, base: s.scale.x };
    scene.add(s); stars.push(s);
  }

  /* ---- layout ---- */
  const base = { x: 0, y: 0, s: 1 };
  function resize() {
    const w = canvas.clientWidth, h = canvas.clientHeight;
    renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix();
    bgMat.uniforms.asp.value = w / h;
    if (w < 980) { base.x = 0; base.y = 1.05; base.s = .72; bgMat.uniforms.c.value.set(.5, .66); }
    else { base.x = 1.85; base.y = .12; base.s = .95; bgMat.uniforms.c.value.set(.7, .5); }
  }
  addEventListener('resize', resize); resize();

  /* ---- loop ---- */
  const clock = new THREE.Clock(); let vis = true;
  new IntersectionObserver(([e]) => vis = e.isIntersecting).observe(canvas);
  const sm = { mx: 0, my: 0 };
  function frame() {
    requestAnimationFrame(frame);
    if (!vis) return;
    const t = clock.getElapsedTime(), p = S.p || 0;
    bgMat.uniforms.t.value = t;
    sm.mx += ((S.mx || 0) - sm.mx) * .05; sm.my += ((S.my || 0) - sm.my) * .05;

    // bloom: bud → open, with per-petal stagger; scroll opens it further
    const b = Math.min(Math.max(S.bloom || 0, 0), 1.2);
    petals.forEach((pt, i) => {
      const local = THREE.MathUtils.clamp((b - pt.d) / (1 - .32), 0, 1.15);
      const ease = 1 - Math.pow(1 - Math.min(local, 1), 3) + Math.max(local - 1, 0) * .4;
      pt.m.rotation.x = .12 + ease * 1.12 + p * .35 + Math.sin(t * 1.2 + i) * .015;
    });
    column.scale.setScalar(.4 + Math.min(b, 1) * .6);

    const zoom = THREE.MathUtils.smoothstep(p, .45, 1);
    flower.position.x = THREE.MathUtils.lerp(base.x, 0, THREE.MathUtils.smoothstep(p, 0, .5)) + sm.mx * .25;
    flower.position.y = base.y - .55 + Math.sin(t * .8) * .06 + THREE.MathUtils.lerp(0, .25, zoom);
    flower.scale.setScalar(base.s * (1 + p * .25));
    flower.rotation.x = .62 + sm.my * .25 - zoom * .45;
    flower.rotation.y = t * .12 + p * Math.PI * 1.2 + sm.mx * .5;
    flower.rotation.z = -.12;

    camera.position.z = 10 - zoom * 7.6;
    camera.position.x = sm.mx * .3; camera.position.y = -sm.my * .2 + zoom * .4;
    camera.lookAt(flower.position.x * zoom, base.y * (1 - zoom) * .0 + zoom * (flower.position.y + .9), 0);

    stars.forEach(s => { s.rotation.z += .01 * s.userData.sp; s.rotation.y = Math.sin(t * s.userData.sp + s.userData.ph) * .6; s.scale.setScalar(s.userData.base * (.75 + .35 * Math.sin(t * 2 * s.userData.sp + s.userData.ph))); });
    renderer.render(scene, camera);
  }
  frame();
  window.dispatchEvent(new Event('ks-flower-ready'));
}

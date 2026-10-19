/* Emblema 3D de NullGhost para video: mismo modelo, materiales y luces que
   landing/v2/emblem.js del sitio, pero cada cuadro se dibuja según el tiempo
   del timeline (evento hf-seek de HyperFrames), sin requestAnimationFrame. */
(() => {
  const canvas = document.getElementById('g3d');
  if (!canvas || !window.THREE) return;
  const T = window.THREE;
  const T0 = +(canvas.dataset.start || 0);
  const SIZE = +(canvas.dataset.size || 520);
  const renderer = new T.WebGLRenderer({canvas, alpha: true, antialias: true, preserveDrawingBuffer: true});
  renderer.setPixelRatio(2);
  renderer.setSize(SIZE, SIZE, false);
  renderer.outputColorSpace = T.SRGBColorSpace;
  renderer.toneMapping = T.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.3;
  const scene = new T.Scene();
  const camera = new T.PerspectiveCamera(36, 1, .1, 100);
  camera.position.set(0, .1, 6.9);
  const environment = document.createElement('canvas');
  environment.width = 1024; environment.height = 512;
  const ctx = environment.getContext('2d');
  ctx.fillStyle = '#111925'; ctx.fillRect(0, 0, 1024, 512);
  [[80,100,160,290,'#f3fbff'],[520,40,60,420,'#1557A6'],[780,100,120,250,'#849EC1']].forEach(([x,y,w,h,color]) => {
    const g = ctx.createLinearGradient(x, 0, x + w, 0);
    g.addColorStop(0, '#111925'); g.addColorStop(.5, color); g.addColorStop(1, '#111925');
    ctx.fillStyle = g; ctx.fillRect(x, y, w, h);
  });
  const texture = new T.CanvasTexture(environment);
  texture.mapping = T.EquirectangularReflectionMapping; texture.colorSpace = T.SRGBColorSpace;
  const pmrem = new T.PMREMGenerator(renderer);
  scene.environment = pmrem.fromEquirectangular(texture).texture;
  texture.dispose(); pmrem.dispose();
  scene.add(new T.AmbientLight(0x829bb8, 1.4));
  [[0xe6f5ff,28,3,4,4],[0x1557a6,24,-3,1,2],[0x64a3ff,20,2,-2,-2]].forEach(([c,p,x,y,z]) => {
    const l = new T.PointLight(c, p, 15); l.position.set(x, y, z); scene.add(l);
  });
  const assembly = new T.Group(); scene.add(assembly);
  const bodyMaterial = new T.MeshStandardMaterial({color:0x1557a6,metalness:.22,roughness:.3,envMapIntensity:.6});
  const darkMaterial = new T.MeshStandardMaterial({color:0x080e19,metalness:.88,roughness:.24,envMapIntensity:1.2});
  const coreMaterial = new T.MeshStandardMaterial({color:0x1557a6,emissive:0x1557a6,emissiveIntensity:1.2,metalness:.45,roughness:.24});
  const silhouette = [["M",20,144],["C",20,70,66,20,130,20],["C",176,20,202,39,238,65],["L",309,116],["C",337,136,348,153,348,186],["L",348,237],["C",348,273,360,294,387,307],["C",400,313,397,329,385,329],["C",365,329,350,317,337,307],["C",317,292,301,292,283,308],["C",264,326,248,333,226,333],["L",88,333],["C",47,333,20,306,20,265],["Z"]];
  function profile(commands, depth, bevel) {
    const shape = new T.Shape();
    const m = {M:'moveTo',L:'lineTo',C:'bezierCurveTo',Q:'quadraticCurveTo'};
    commands.forEach(([c, ...v]) => {
      if (c === 'Z') { shape.closePath(); return; }
      shape[m[c]](...v.map((n, i) => i % 2 ? (180 - n) / 135 : (n - 208) / 135));
    });
    return new T.ExtrudeGeometry(shape, {depth, bevelEnabled:true, bevelThickness:bevel, bevelSize:bevel, bevelSegments:4, curveSegments:20});
  }
  const shell = new T.Mesh(profile(silhouette, .19, .028), bodyMaterial); assembly.add(shell);
  const core = new T.Mesh(profile(silhouette, .085, .015), coreMaterial); core.position.z = -.095; assembly.add(core);
  const back = new T.Mesh(profile(silhouette, .10, .022), darkMaterial); assembly.add(back);
  const glyph = new T.Group(); assembly.add(glyph);
  const eyeMaterial = new T.MeshStandardMaterial({color:0xffffff,roughness:.2,metalness:.1,emissive:0xe9f1ff,emissiveIntensity:.18});
  [73, 187].forEach(x => {
    const y = 166, w = 67, h = 27, r = 13.5, a = 3 * Math.PI / 180;
    let eye = [['M',x+r,y],['L',x+w-r,y],['Q',x+w,y,x+w,y+r],['Q',x+w,y+h,x+w-r,y+h],['L',x+r,y+h],['Q',x,y+h,x,y+r],['Q',x,y,x+r,y],['Z']];
    eye = eye.map(([c, ...v]) => { const o = []; for (let i = 0; i < v.length; i += 2) { const dx = v[i]-200, dy = v[i+1]-188; o.push(200+dx*Math.cos(a)-dy*Math.sin(a), 188+dx*Math.sin(a)+dy*Math.cos(a)); } return [c, ...o]; });
    glyph.add(new T.Mesh(profile(eye, .025, .004), eyeMaterial));
  });
  shell.add(new T.LineSegments(new T.EdgesGeometry(shell.geometry, 35), new T.LineBasicMaterial({color:0x9cc3ff,transparent:true,opacity:.2})));
  const orbitMaterial = new T.MeshBasicMaterial({color:0x64a3ff,transparent:true,opacity:.23});
  const rings = [];
  const orbital = new T.Group(); scene.add(orbital);
  [1.64, 1.91].forEach((radius, i) => {
    const g = new T.Group(); g.rotation.set(i ? .95 : 1.32, i ? .6 : -.28, i ? -.45 : .25);
    g.add(new T.Mesh(new T.TorusGeometry(radius, .005, 5, 140), orbitMaterial));
    const pulse = new T.Mesh(new T.SphereGeometry(.028, 10, 10), coreMaterial); g.add(pulse);
    orbital.add(g); rings.push({pulse, radius});
  });

  const clamp = x => Math.max(0, Math.min(1, x));
  const smooth = x => x * x * (3 - 2 * x);
  const backOut = x => { const c = 1.70158; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
  // Despliegue del núcleo: abre al conectar las dos normas y vuelve a cerrar.
  const SPLIT = (canvas.dataset.split || '2.45,3.0,3.5,3.95').split(',').map(Number);
  function renderAt(t) {
    const lt = Math.max(0, t - T0), time = lt;
    const s = lt <= 0 ? .001 : backOut(clamp(lt / .7));
    assembly.scale.setScalar(Math.max(.001, s));
    orbital.scale.setScalar(Math.max(.001, smooth(clamp((lt - .3) / .8))));
    const spin = (1 - smooth(clamp(lt / 1.3))) * -2.6;
    assembly.rotation.set(-.13 + Math.sin(time * .6) * .035, -.32 + spin + Math.sin(time * .42) * .28, -.09 + Math.sin(time * .5) * .04);
    assembly.position.y = Math.sin(time * .8) * .065;
    const split = lt < SPLIT[1] ? smooth(clamp((lt - SPLIT[0]) / (SPLIT[1] - SPLIT[0])))
                : 1 - smooth(clamp((lt - SPLIT[2]) / (SPLIT[3] - SPLIT[2])));
    shell.position.z = .06 + split * .35; glyph.position.z = .284 + split * .67; back.position.z = -.23 - split * .38;
    rings.forEach(({pulse, radius}, i) => { const a = time * (i ? -.38 : .46) * 2.2 + i * 2; pulse.position.set(Math.cos(a) * radius, Math.sin(a) * radius, 0); });
    coreMaterial.emissiveIntensity = 1.1 + Math.sin(time * 1.5) * .2 + split * .9;
    renderer.render(scene, camera);
  }
  window.addEventListener('hf-seek', e => renderAt(+e.detail.time || 0));
  renderAt(window.__hfThreeTime || 0);
})();

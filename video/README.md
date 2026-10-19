# Video de la guía y el manual de IA de NullGhost

Dos versiones de 56 segundos, 1920 × 1080, 30 fps, H.264 y sin audio. Identidad oficial de NullGhost; portadas españolas v0.4 en ambas versiones.

- [Español](iso-ai-es.mp4)
- [English](iso-ai-en.mp4)

Ocho escenas: las dos normas y la pregunta que responde cada una; anillo de las cláusulas 4 a 10 de ISO/IEC 42001 con la evaluación de impacto (6.1.4); Anexo A (38 controles, 9 objetivos, según fuentes secundarias); amenazas de ISO/IEC 27090 apiladas por fase del ciclo de vida, con su correspondencia aproximada en OWASP y MITRE ATLAS; camino de cuatro semanas con la utilidad de técnicas de estudio de Dunlosky et al. (2013); estados de evidencia; cierre con las portadas. Todo el texto viene de `../content.py`; no hay cifras propias.

Fuente: `build_video.py` genera `index.html` (ES) y `compositions/en.html` (EN). HyperFrames 0.8.174, GSAP 3.14.2, Node.js 22.

```sh
python3 build_video.py
npx hyperframes render -o renders/iso-ai-es.mp4 .
npx hyperframes render -c compositions/en.html -o renders/iso-ai-en.mp4 .
```

Las portadas (`assets/guide.png`, `assets/manual.png`) salen de la primera página de cada PDF; el listón (`assets/ribbon.jpg`) viene de `../assets/premium/`. Inter incluye su licencia OFL; GSAP conserva su licencia de terceros. Marca NullGhost excluida de la licencia de contenido.

## Reel para Instagram

`iso-ai-reel-es.mp4`: 1080 × 1920, 33 s, con música. Fuente en `build_reel_pro.py` → `compositions/reel-pro-es.html`. El fantasma del hub es el emblema 3D del sitio (`assets/ghost3d.js`, mismo modelo que `landing/v2/emblem.js`, con Three.js r160 de `assets/vendor/three.min.js`, licencia MIT) dibujado cuadro por cuadro con el evento `hf-seek` de HyperFrames. La música se mezcla después del render con ffmpeg; procedencia y licencia en `MUSIC-LICENSE.txt`.

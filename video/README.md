# Video de las guías de IA de NullGhost

Dos versiones de 30 segundos, 1920 × 1080, 30 fps, H.264 y sin audio. Identidad oficial de NullGhost; portadas españolas v0.2 en ambas versiones.

- [Español](iso-ai-es.mp4)
- [English](iso-ai-en.mp4)

Fuente: `build_video.py`, `index.html` y `compositions/en.html`. HyperFrames 0.8.174, GSAP 3.14.2, Node.js 22. `npm ci` instala las dependencias. `python3 build_video.py` reconstruye el HTML; `npx hyperframes render --quality delivery` exporta ES y `npx hyperframes render -c compositions/en.html --quality delivery` exporta EN. Revisar BRIEF.md y STORYBOARD.md antes de editar.

Los SVG originales provienen de los activos oficiales del sitio. Las portadas provienen de los PDF v0.2 de este repositorio. Inter incluye su licencia OFL; GSAP conserva su licencia de terceros. Marca NullGhost excluida de la licencia de contenido.

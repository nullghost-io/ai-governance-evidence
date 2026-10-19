# Guía de investigación y manual de buenas prácticas de IA

**NullGhost · versión de trabajo v0.2 · 19 de octubre de 2026.**

Dos materiales prácticos para estudiar y documentar la gestión y seguridad de IA a partir del alcance público de ISO/IEC 42001:2023 e ISO/IEC 27090:2026. Se publican como guía y manual, con la identidad oficial de NullGhost. Son documentos distintos de la serie de papers académicos de la organización.

## Documentos

| Tipo | PDF (español) | Fuente editable |
|---|---|---|
| Guía de investigación, 10 páginas | [Gestión y seguridad de IA](guides/es/Guia_de_Investigacion_IA.pdf) | [Markdown](guides/es/Guia_de_Investigacion_IA.md) |
| Manual de buenas prácticas, 9 páginas | [Prácticas de IA](manuals/es/Manual_de_Buenas_Practicas_IA.pdf) | [Markdown](manuals/es/Manual_de_Buenas_Practicas_IA.md) |

[Ver en NullGhost](https://nullghost.io/ia-normas.html) · [Release v0.2](https://github.com/nullghost-io/ai-governance-evidence/releases/tag/v0.2)

![Guía de investigación](assets/research-guide-cover.png)

## Video y publicación web

[Video español](video/iso-ai-es.mp4) · [English video](video/iso-ai-en.mp4). Dos versiones de 30 segundos con la marca oficial. Integrados en Inicio, Investigaciones y la página de las guías; referencias ISO en Servicios. Los documentos conservan su versión v0.2.

## Research guide and good-practice manual

The Spanish PDFs contain research questions, an evidence workflow and practical templates. ES/EN summaries are available on the website. These are working guides and manuals, not entries in NullGhost's academic paper series. Version 0.2 replaces the earlier document classification and uses the official brand assets.

## Alcance y revisión pendiente

- Fichas oficiales contrastadas para identidad, edición y alcance general. No se han revisado íntegramente las normas ISO ni se redistribuyen.
- NIST AI 100-2e2025 consultado selectivamente, incluidas secciones 3.4 y 3.5. La página de AI RMF sirve como contexto, no como cruce normativo completo.
- Las prácticas, los estados de evidencia y los criterios son propuestas de NullGhost. No se presenta una campaña experimental ni resultados de eficacia.
- Ejemplos sintéticos; sin datos de clientes. Revisión técnica humana, contraste normativo y validación del protocolo pendientes.
- Elaboración asistida por IA; sin certificación o conformidad demostrada.

## Plantillas

[Inventario](templates/inventario.csv) · [Riesgos](templates/riesgos.csv) · [Pruebas](templates/pruebas.csv) · [Matriz de aplicación](templates/matriz_aplicacion.csv).

Contienen cabeceras, sin datos inventados. Las referencias de cláusula se completan solo después de verificarlas.

## Reconstruir

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 build_pdf.py
```

Contenido canónico: `content.py`. El generador produce PDF y Markdown en `guides/es/` y `manuals/es/`. Inserta los SVG originales de `assets/brand/`, sin reconstruir el fantasma ni componer el logo con texto. Usa Arial instalada en macOS o Helvetica como alternativa portable; revisar el render al cambiar de entorno.

## Versiones y fuentes

[Historial](CHANGELOG.md) · [Fuentes](sources.json) · [Huellas](SHA256SUMS.txt).

La v0.1 fue una primera publicación mal clasificada como paper y con una marca reconstruida. Está sustituida por v0.2 y se conserva solo como historial; utilizar las rutas actuales.

## Licencias

Código original: MIT. Texto y gráficos originales: CC BY 4.0. Las marcas y logotipos de NullGhost, normas y materiales de terceros conservan sus derechos y quedan excluidos de esa licencia. Ver LICENSE y LICENSE-CONTENT.md.

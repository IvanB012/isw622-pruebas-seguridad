# Creación de Pruebas de Seguridad de Software — ISW-622

Tarea en equipo: **Iván Barboza Blanco** (Fase A y Fase F) y **Ian Angulo Matamoros** (Fases B, C, D y E).
Unidad IV, Pruebas de Software (UTN). 100 puntos.

## Estructura del repositorio

```
.
├── informe_seguridad.pdf           # Informe final (se agrega al cierre, Fase F)
├── laboratorio_seguridad/          # Código base del profesor + correcciones del equipo
│   ├── README.md
│   ├── servidor.py
│   ├── src/
│   │   ├── __init__.py
│   │   └── lab.py
│   └── tests/
│       └── test_laboratorio.py
├── documentacion/
│   └── Fase_A_Requisitos_Amenazas_Trazabilidad.docx
├── evidencias/                     # Capturas rojo-verde-refactor y pruebas manuales (Ian, Fase C)
├── matriz_trazabilidad.csv         # SEC - Riesgo - TC - evidencia esperada
└── hallazgos.csv                   # Bitácora de hallazgos (se llena en Fase F)
```

## Cómo ejecutar el laboratorio

Desde `laboratorio_seguridad/`:

```bash
python -m unittest discover -s tests -v
python servidor.py   # en otra terminal
curl http://127.0.0.1:8765/health
```

Ver `laboratorio_seguridad/README.md` para detalles de tokens, roles y peticiones de ejemplo.

## Flujo de trabajo

- Rama `main`: estado integrado y entregable.
- Rama `ivan`: documentación y análisis (Fase A y Fase F).
- Rama `ian`: código, pruebas TDD y correcciones (Fases B, C, D, E).
- Los cambios se integran a `main` por Pull Request, que sirve también como evidencia de la inspección cruzada (Fase D).

## Avance

- [x] Fase A — Requisitos, amenazas y trazabilidad (Iván)
- [ ] Fase B/C — Diseño de casos, TDD y ejecución (Ian)
- [ ] Fase D/E — Revisión e inspección, usabilidad (Ian + Iván)
- [ ] Fase F — Resultados y dictamen (Iván)
# Creación de Pruebas de Seguridad de Software — ISW-622

Guía de relevo para Iván. La Fase A define requisitos SEC-01 a SEC-07 y amenazas T1 a T6; Ian ejecutó el trabajo técnico de Fases B y C.

## Lectura rápida

- **12 casos de prueba de seguridad:** TC-01 a TC-12; 3 positivos, 6 negativos y 3 de frontera.
- **14 pruebas automatizadas:** 12 unitarias, una por cada caso, más 2 pruebas de integración HTTP que vuelven a validar TC-03 y TC-05 a través de la API.
- **Resultado final:** 14 pruebas aprobadas, sin fallos.
- **Pruebas manuales:** cuatro escenarios API con cinco solicitudes Postman: TC-03, TC-05, TC-04 (dos pasos) y PM-01.

## Trazabilidad Fase A

| SEC | Amenaza | Casos |
|---|---|---|
| SEC-01 | T1 acceso horizontal | TC-01, TC-02 |
| SEC-02 | T2 modificación entre sedes | TC-03, TC-09, TC-10 |
| SEC-03 | T3 sesión inválida | TC-04, TC-06 |
| SEC-04 y SEC-05 | T4 validación e integridad | TC-05, TC-11, TC-12, PM-01 |
| SEC-06 | T5 auditoría | TC-07 |
| SEC-07 | autorización por rol | TC-08 |
| Riesgo residual | T6 fuerza bruta | Fuera de alcance; transferir a Fase F |

Los 12 casos están aprobados. PM-01 significa **Prueba Manual 01**: usa una nota no numérica y no se llama TC-11 porque TC-11 valida el valor numérico `0`.

## Dónde está el código

| Archivo | Contenido |
|---|---|
| `laboratorio_seguridad/src/lab.py` | Reglas de autenticación, sesiones, autorización por rol/sede, validación de nota y auditoría. |
| `laboratorio_seguridad/tests/test_laboratorio.py` | Las **12 pruebas unitarias**, una por cada TC. |
| `laboratorio_seguridad/tests/test_api.py` | Las **2 pruebas de integración HTTP** para TC-03 y TC-05. |
| `laboratorio_seguridad/servidor.py` | API local utilizada por integración y Postman. |

## Ejecución reproducible

Desde la raíz del repositorio:

```powershell
Set-Location ".\laboratorio_seguridad"
$env:PYTHONPATH = "."
python --version
python -m unittest discover -s tests -v
Remove-Item Env:PYTHONPATH
```

La ejecución final usa Python 3.14.6 y debe mostrar `Ran 14 tests` seguido de `OK`.

Para API manual:

```powershell
$env:PYTHONPATH = "."
python servidor.py
```

La API queda en `http://127.0.0.1:8765`. Detener con `Ctrl+C`.

## Estructura de evidencias

Cada carpeta se nombra por el caso y, cuando corresponde, por el tipo de evidencia. Varios archivos para un mismo caso son normales: pueden corresponder a rojo, verde, refactor, salida textual, captura terminal o captura Postman.

| Carpeta | Contenido |
|---|---|
| `tc-02-acceso-horizontal-tdd/` | Ciclo rojo-verde-refactor de TC-02. |
| `tc-03-modificacion-entre-sedes-tdd/` | Ciclo TDD de TC-03. |
| `tc-04-sesion-revocada-tdd/` | Ciclo TDD de TC-04. |
| `tc-05-nota-fuera-rango/` | Evidencia de frontera TC-05. |
| `tc-06-sesion-expirada/` | Ejecución de TC-06. |
| `tc-07-auditoria-segura-tdd/` | Hallazgo SEC-06, corrección, verde y regresión. |
| `tc-08-administrador-sin-modificacion/` | Ejecución de TC-08. |
| `tc-09-docente-misma-sede/` | Salida y captura de TC-09. |
| `tc-11-limite-inferior-valido/` | Salida y captura de TC-11. |
| `tc-12-limite-superior-invalido/` | Salida y captura de TC-12. |
| `integracion-api/` | Pruebas de integración HTTP de TC-03 y TC-05. |
| `manual-api-postman/` | Capturas Postman de TC-03, TC-05, TC-04 y PM-01. |
| `regresion-suite-final/` | Salida de regresión completa; agregar aquí la captura que muestre las 14 pruebas. |

TC-01 y TC-10 se evidencian dentro de la regresión global y en las pruebas unitarias; no se creó una carpeta individual para cada uno.

## Continuidad

Para Fase D/E, Iván debe inspeccionar una política de acceso y dos casos, y ejecutar la suite usando solo este README. Para Fase F, conservar la trazabilidad SEC–amenaza–caso–evidencia; distinguir defectos corregidos de T6, que permanece como riesgo residual.

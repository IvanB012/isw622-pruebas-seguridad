# Registro de Fases D y E

Este registro debe completarse con resultados observados. Ninguna observación, hallazgo o resultado se considera ejecutado hasta que el revisor o ejecutor independiente lo consigne.

## Fase D: revisión cruzada e inspección

**Revisor independiente:** Iván Barboza Blanco  
**Autor del código y pruebas revisados:** Ian Angulo Matamoros  
**Fecha de revisión:** Pendiente  

### Alcance propuesto

| Elemento | Ubicación | Motivo de selección |
|---|---|---|
| Política de acceso | `laboratorio_seguridad/src/lab.py` — `actualizar_nota()` | Aplica autorización por rol y sede, e integridad de la nota. |
| Caso de prueba 1 | TC-03 — modificación entre sedes | Traza SEC-02, SEC-05 y amenaza T2. |
| Caso de prueba 2 | TC-04 — sesión revocada | Traza SEC-03 y amenaza T3. |

### Procedimiento de inspección

1. El revisor lee la política seleccionada, los dos casos, sus pruebas automatizadas y las evidencias asociadas.
2. Confirma que cada oráculo comprueba tanto el código HTTP como la ausencia de cambio indebido en los datos cuando corresponde.
3. Registra al menos tres observaciones verificables o oportunidades de mejora. No se deben declarar vulnerabilidades sin evidencia reproducible.
4. Ian implementa únicamente las acciones aceptadas y ejecuta la regresión posterior.
5. Al menos una observación se valida mediante una prueba independiente que comprueba el efecto sobre los datos, no depende de otra prueba y falla cuando el control deja de cumplirse.

### Observaciones del revisor

| ID | Objeto revisado | Observación verificable u oportunidad de mejora | Evidencia | Severidad | Acción acordada | Estado |
|---|---|---|---|---|---|---|
| D-OBS-01 | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| D-OBS-02 | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| D-OBS-03 | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |

### Prueba independiente de una observación

| Campo | Registro |
|---|---|
| Observación seleccionada | Pendiente |
| Prueba creada o ejecutada | Pendiente |
| Datos antes de ejecutar la prueba | Pendiente |
| Condición de control evaluada | Pendiente |
| Efecto controlado sobre datos | Pendiente |
| Condición que debe hacer fallar la prueba | Pendiente |
| Resultado esperado | Pendiente |
| Resultado obtenido | Pendiente |
| Evidencia | Pendiente |

## Fase E: usabilidad y reproducibilidad

**Ejecutor independiente:** Iván Barboza Blanco  
**Fecha de ejecución:** Pendiente  
**Fuente única de instrucciones:** `README.md` de la raíz del repositorio.  

### Ejecución independiente

El ejecutor debe seguir únicamente el apartado **Ejecución reproducible** del README. Ian no debe indicarle comandos adicionales durante esta comprobación.

| Dato requerido | Registro |
|---|---|
| Versión de Python observada | Pendiente |
| Comandos ejecutados | Pendiente |
| Resultado de la suite | Pendiente |
| ¿El README fue suficiente? | Pendiente |
| Dificultades, ambigüedades o pasos faltantes | Pendiente |
| Evidencia de ejecución | Pendiente |

### Escenarios de usabilidad del control

| Escenario | Resultado que debe valorar el ejecutor | Resultado observado | ¿Expone datos sensibles? | Mejora propuesta |
|---|---|---|---|---|
| Sesión inválida o revocada | El mensaje debe indicar que la solicitud no está autenticada sin revelar expediente, nota, sede ni token. | Pendiente | Pendiente | Pendiente |
| Acceso denegado | El mensaje debe comunicar la denegación sin revelar datos del expediente ajeno ni detalles internos de autorización. | Pendiente | Pendiente | Pendiente |

### Ajustes para mantenimiento y diagnóstico

La rúbrica exige ajustar **nombres, datos o mensajes de error de al menos dos pruebas** para facilitar el mantenimiento y el diagnóstico. Los ajustes deben ser reales, trazables a la ejecución independiente o al análisis de usabilidad y verificarse por regresión.

| ID | Prueba afectada | Tipo de ajuste: nombre, dato o mensaje | Situación anterior | Ajuste aplicado por Ian | Motivo y vínculo con D/E | Prueba de regresión | Estado |
|---|---|---|---|---|---|---|---|
| E-AJ-01 | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |
| E-AJ-02 | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |

## Criterio de cierre

La Fase D se cierra cuando existen tres observaciones verificables, su clasificación, la acción correspondiente y una prueba independiente documentada. La Fase E se cierra cuando un compañero ejecuta la suite usando únicamente el README, valora los dos escenarios de usabilidad sin divulgar información privada y se documentan dos ajustes reales en pruebas. Después de ambos cierres, se actualiza la Fase F con los resultados finales.

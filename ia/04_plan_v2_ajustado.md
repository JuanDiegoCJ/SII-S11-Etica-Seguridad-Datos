# Plan de Contingencia de TI (versión 2, ajustada)

## Objetivo
Mantener o restablecer, dentro de tiempos definidos, los servicios tecnológicos críticos ante incidentes disruptivos, protegiendo los datos personales de la comunidad educativa y reduciendo el impacto ambiental de la infraestructura, en coherencia con ISO 22301, ISO/IEC 27001:2022, la Ley N.° 29733 y los ODS 4, 7, 9, 12, 13 y 16.

## Organización
- **Comité de Crisis:** dirección general, jefatura de TI, oficial de datos personales, comunicaciones, seguridad física.
- **Equipo de Respuesta Técnica:** servidores, redes, seguridad de la información.
- **Equipo de Apoyo:** mantenimiento, proveedores, atención a usuarios.
- Cada rol con titular y suplente.

## Análisis de impacto (BIA)
| Servicio | Criticidad | RTO | RPO | Estrategia |
|---|---|---|---|---|
| Plataforma académica | Crítica | 4 h | 1 h | Réplica en nube y conmutación por error |
| Identidad y autenticación (MFA) | Crítica | 2 h | 15 min | Controlador secundario en nube |
| Correo y colaboración | Alta | 8 h | 4 h | Continuidad del proveedor nube |
| Sistemas administrativos | Alta | 24 h | 4 h | Restauración desde copia inmutable |
| Portal web | Media | 24 h | 24 h | Versión estática en CDN |

## Matriz de riesgos
Ver `salidas/matriz_riesgos.md` y `salidas/mapa_calor.png` (generados por `src/matriz_riesgos.py`).

## Estrategias por escenario
| Escenario | Prevención | Respuesta y recuperación | Sostenibilidad / responsabilidad social |
|---|---|---|---|
| E1 Energía | UPS 30 min; mantenimiento trimestral del generador; medición por rack | Apagado ordenado; conmutación a nube si supera 2 h | Hoja de ruta solar + baterías; registro de emisiones (ODS 7, 13) |
| E2 Inundación | Piso técnico elevado; sensores de agua; revisión de drenajes | Desenergizar; sitio alterno en nube | Coordinación con defensa civil (ODS 11, 13) |
| E3 Ransomware | Parches, EDR, segmentación, MFA, copias 3-2-1-1-0 | Aislar; restaurar desde copia limpia; denuncia a Divindat | No pagar rescates; transparencia (ODS 16) |
| E5 Fuga de datos | Cifrado, DLP (A.8.12), mínimo privilegio | Contener; notificar a la ANPD en 48 h; informar a titulares | Prioridad a menores y vulnerables (ODS 16.10, ISO 26000) |
| E4 Climatización | N+1; pasillo frío; alarmas | Ventilación de emergencia; mover cargas a nube | PUE ≤ 1,6; free cooling; refrigerantes de bajo PCA |
| E7 Sismo | Anclaje de racks; copias geográficas | Evacuación; recuperación desde nube | Simulacros integrados (ODS 11.5) |
| E6 Nube/enlace | Dos ISP; cláusulas de continuidad y portabilidad | Enlace alterno; modo degradado | Proveedores con metas renovables e ISO/IEC 27701 |
| E8 Personal | Suplentes; procedimientos; capacitación cruzada | Activar suplentes y SLA de proveedor | Turnos razonables (ODS 8) |

## Fin de vida de equipos
Borrado seguro con acta (A.7.14, A.8.10) → reutilización o donación → operador RAEE autorizado (D. S. 009-2019-MINAM).

## Comunicación
Dos canales independientes; servicio afectado, tiempo estimado y alternativa; ampliación de plazos académicos; lenguaje claro y formatos accesibles.

## Pruebas e indicadores
| Ejercicio / indicador | Frecuencia | Meta |
|---|---|---|
| Restauración de copias | Mensual | Dentro del RPO, 0 errores |
| Ejercicio de mesa | Semestral | Decisiones clave < 30 min |
| Conmutación a nube | Anual | Plataforma en ≤ 4 h |
| Simulacro de fuga de datos | Anual | Notificación lista < 48 h |
| PUE | Mensual | ≤ 1,6 a dos años |
| Energía renovable | Anual | 30 % a cinco años |
| RAEE con operador autorizado | Anual | 100 % |
| Revisión del plan | Anual o tras incidente mayor | Aprobado por la dirección |

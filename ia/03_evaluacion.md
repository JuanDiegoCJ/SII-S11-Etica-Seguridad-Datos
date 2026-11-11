# Evaluación de la versión 1 frente a los ODS y normas internacionales

| N.° | Hallazgo en la versión 1 | Referencia incumplida | Ajuste aplicado en la versión 2 |
|---|---|---|---|
| 1 | Cita el «dominio A.17» de ISO/IEC 27001 (numeración de 2013). | ISO/IEC 27001:2022, A.5.29, A.5.30, A.8.13, A.8.14 | Referencias actualizadas a la edición 2022. |
| 2 | Sin análisis de impacto ni RTO/RPO. | ISO 22301:2019 cl. 8.2.2; ISO/IEC 27031 | BIA con RTO y RPO por servicio. |
| 3 | Omite lluvias por El Niño costero y sismo. | ISO/IEC 27001 Amd 1:2024; ODS 13.1; ODS 11.5 | Escenarios E2 y E7. |
| 4 | Riesgos sin priorizar. | ISO/IEC 27001 cl. 6.1.2; ISO 31000 | Matriz P × I calculada con `src/matriz_riesgos.py`. |
| 5 | Grupo electrógeno diésel sin criterio energético. | ODS 7.2, 7.3; ODS 13; ISO 50001 | Medición de consumo y hoja de ruta solar + baterías. |
| 6 | «Reciclar equipos» genérico; ignora datos almacenados. | ODS 12.5; D. S. 009-2019-MINAM; ISO/IEC 27001 A.7.14, A.8.10 | Borrado seguro y operador RAEE autorizado. |
| 7 | Restaurar desde copias no protege contra ransomware. | ISO/IEC 27001 A.8.13; ISO/IEC 27035 | Respaldo 3-2-1-1-0 con copia inmutable. |
| 8 | No contempla fuga de datos ni notificación a la ANPD. | Ley 29733; D. S. 016-2024-JUS (48 h); ISO/IEC 27701; ODS 16.10 | Escenario E5 con protocolo de notificación. |
| 9 | Responsabilidad social limitada a comunicar. | ISO 26000; ODS 4.1; ODS 10 | Continuidad académica y canales accesibles. |
| 10 | Sin indicadores ambientales. | ISO/IEC 30134-2 (PUE); ISO 14001 | PUE, % renovable, RAEE gestionados. |
| 11 | Pruebas sin tipo ni criterio; omite proveedores nube. | ISO 22301 cl. 8.5; ISO/IEC 27001 A.5.23, A.5.30 | Programa de ejercicios y cláusulas con proveedores. |

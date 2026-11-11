# SII-S11-Etica-Seguridad-Datos

**ÉTICA_SEGURIDAD DE DATOS_S11**

**Curso:** Sistemas de Información Integrados (NRC 12054 – 12055)
**Docente:** Dr. Mendoza Corpus Carlos Alfredo
**Estudiante:** Carranza Jacinto Juan Diego (ID 000257022)
**Universidad Privada Antenor Orrego – Escuela de Ingeniería de Sistemas e Inteligencia Artificial, 2026**

Material de soporte de la Parte IV del informe: plan de contingencia para una infraestructura tecnológica generado con IA, evaluado y ajustado según los ODS y normas internacionales.

## Estructura

```
ia/
  01_prompt_inicial.md          prompt enviado a la IA
  02_plan_v1_generado_por_ia.md salida original de la IA, sin modificaciones
  03_evaluacion.md              evaluación frente a ODS y normas
  04_plan_v2_ajustado.md        plan final ajustado
datos/
  escenarios.csv                escenarios con probabilidad, impacto, RTO, RPO, ODS y normas
src/
  matriz_riesgos.py             cálculo y priorización de riesgos, mapa de calor
salidas/
  matriz_riesgos.md             tabla priorizada
  mapa_calor.png                mapa de calor probabilidad × impacto
  salida_consola.txt            resultado de la ejecución
informe/
  ETICA_SEGURIDAD_DE_DATOS_S11.pdf
```

## Ejecución

Requisitos: Python 3.10 o superior y matplotlib.

```bash
pip install matplotlib
python src/matriz_riesgos.py
```

El programa calcula el nivel de riesgo (probabilidad × impacto), lo clasifica (crítico ≥ 15, alto 10–14, medio 5–9, bajo < 5), ordena los escenarios y verifica que cada estrategia esté vinculada al menos a un ODS y a una norma.

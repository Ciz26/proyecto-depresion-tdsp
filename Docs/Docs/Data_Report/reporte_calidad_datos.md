<p>
<a href="https://github.com/Ciz26/proyecto-depresion-tdsp"><img src="../../assets/nav_inicio.svg" width="24.4%" alt="Inicio"></a>
<a href="https://github.com/Ciz26/proyecto-depresion-tdsp/tree/main/Code"><img src="../../assets/nav_code.svg" width="24.4%" alt="Code"></a>
<a href="https://github.com/Ciz26/proyecto-depresion-tdsp/tree/main/Docs"><img src="../../assets/nav_docs_on.svg" width="24.4%" alt="Docs"></a>
<a href="https://github.com/Ciz26/proyecto-depresion-tdsp/tree/main/Sample_Data"><img src="../../assets/nav_sample_data.svg" width="24.4%" alt="Sample_Data"></a>
</p>

# Reporte de calidad de los datos

## Fuente

Evaluación Cognitiva de la ENASEM 2021 (ECENASEM 2021), INEGI. La base contiene 3,575 registros.

## Variables seleccionadas

Doce variables, una de respuesta y once predictoras. La selección se hizo con criterio teórico, a partir de los factores que la literatura asocia con la depresión en adultos mayores.

## Datos faltantes

| Variable | Faltantes |
|---|---|
| Edad | 0 |
| Sexo | 0 |
| Dificultad para preparar comidas | 142 |
| Dificultad para ir de compras | 140 |
| Dificultad para tomar medicinas | 140 |
| Dificultad para manejar dinero | 141 |
| Comparación de la memoria | 145 |
| Se siente aislado | 145 |
| Se siente ignorado | 144 |
| Le falta compañía | 142 |
| Estrés por la pandemia | 143 |
| Síntomas depresivos CES-D | 140 |

Los faltantes se concentran en las mismas personas, que no contestaron el bloque de preguntas. Se eliminaron los casos incompletos.

| | Registros |
|---|---|
| Originales | 3,575 |
| Completos | 3,418 |
| Eliminados | 157 (4.39%) |

## Variable respuesta

| Síntomas depresivos | Casos | Porcentaje |
|---|---|---|
| No | 2,090 | 61.15% |
| Sí | 1,328 | 38.85% |

## Limitaciones

- No es posible comprobar que los faltantes sean completamente aleatorios (MCAR).
- La variable de estrés mide el estrés con relación a la pandemia de COVID-19.

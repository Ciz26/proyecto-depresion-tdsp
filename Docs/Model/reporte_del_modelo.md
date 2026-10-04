<p>
<a href="https://github.com/Ciz26/proyecto-depresion-tdsp"><img src="../../assets/nav_inicio.svg" width="24.4%" alt="Inicio"></a>
<a href="https://github.com/Ciz26/proyecto-depresion-tdsp/tree/main/Code"><img src="../../assets/nav_code.svg" width="24.4%" alt="Code"></a>
<a href="https://github.com/Ciz26/proyecto-depresion-tdsp/tree/main/Docs"><img src="../../assets/nav_docs_on.svg" width="24.4%" alt="Docs"></a>
<a href="https://github.com/Ciz26/proyecto-depresion-tdsp/tree/main/Sample_Data"><img src="../../assets/nav_sample_data.svg" width="24.4%" alt="Sample_Data"></a>
</p>

# Reporte del modelo

## Especificación

Modelo lineal generalizado con distribución binomial y enlace logit. Partición estratificada en 70% de entrenamiento (2,392 casos) y 30% de prueba (1,026 casos).

## Razones de momios más altas

| Variable | Razón de momios | IC 95% |
|---|---|---|
| Le falta compañía, con mucha frecuencia | 7.45 | 4.54 a 12.23 |
| Estrés por la pandemia, mucho | 3.02 | 2.24 a 4.07 |
| Se siente ignorado, con mucha frecuencia | 2.66 | 1.26 a 5.60 |
| Le falta compañía, algunas veces | 2.64 | 1.96 a 3.54 |

## Diagnóstico

| Diagnóstico | Valor |
|---|---|
| Hosmer-Lemeshow | Estadístico 10.72, p = 0.2182 |
| VIF máximo | 8.67 |
| Distancia de Cook máxima | 0.0106 (umbral de referencia 4/n: 0.0017) |

## Desempeño en el conjunto de prueba

Área bajo la curva ROC: 0.8329. Punto de corte por índice de Youden: 0.4165.

| Medida | Corte de 0.5 | Corte de 0.4165 |
|---|---|---|
| Exactitud | 76.41% | 76.12% |
| Precisión | 76.08% | 68.78% |
| Sensibilidad | 57.39% | 70.68% |
| Especificidad | 88.52% | 79.59% |

## Matrices de confusión

| Corte de 0.5 | Predicho No | Predicho Sí |
|---|---|---|
| Real No | 555 | 72 |
| Real Sí | 170 | 229 |

| Corte de 0.4165 | Predicho No | Predicho Sí |
|---|---|---|
| Real No | 499 | 128 |
| Real Sí | 117 | 282 |

Con el cambio de corte el modelo cumple los dos criterios de éxito del acta del proyecto.

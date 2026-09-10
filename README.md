# 🌊 Sistema de Firmas de Collatz

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Language](https://img.shields.io/badge/language-Python-blue.svg)](code/convergence_exact_calculation.py)
[![Mathematics](https://img.shields.io/badge/math-Number%20Theory-purple.svg)](README.md)
[![Status](https://img.shields.io/badge/status-Complete%20Verification-brightgreen.svg)](logs/)

**20 teoremas — formulación determinista, estructural y modular de la Conjetura de Collatz**

*Firmas · clases residuales · intervalos de supervivencia · densidades exactas · brecha acumulativa · cascada de pisos*

**Autor**: [Andrés Gerla](https://github.com/andressetentay-design) | Montevideo, Uruguay | Agosto 2026

---

## 📚 Resumen Ejecutivo

La **conjetura de Collatz** (o 3n+1) es uno de los problemas abiertos más simples pero misteriosos de las matemáticas. Este repositorio presenta un **sistema completo de 20 teoremas** que describe:

✅ **¿Qué es el sistema de firmas?**  
Un conjunto de reglas exactas que determinan:
- Qué secuencias de operaciones (impares y divisiones) son posibles
- Cuántos números siguen cada camino (densidades exactas)
- Por qué siempre descienden (balance modular garantizado)

✅ **Novedad clave**: Demostración determinista en tres niveles:
1. **Nivel orbital** - identidades exactas para cada número
2. **Nivel de densidad** - proporciones límite cuando k→∞
3. **Nivel 2-ádico** - medida de Haar en clases residuales

✅ **Verificación computacional**: 
- **1.879.048.192 enteros** enumerados en [2^28, 2^30]
- **Predicciones teóricas** = **Datos computacionales** (EXACTO)
- **Convergencia**: 99.757853% hasta A=107

> *Nuestras vidas son los ríos que van a dar en la mar, que es el morir...*  
> — Jorge Manrique, *Coplas por la muerte de su padre* (c. 1476)

---

## 🚀 Quick Start

### Opción 1: Ver los resultados
```bash
# Log de convergencia exacta (p=1 a p=107)
cat logs/log_convergencia_p1_p107.txt

# Datos de verificación (1.879 billones de enteros)
head -20 data/verification_collatz_k28_k30.csv

# Análisis detallado de pesos
cat analysis/detailed_weight_calculation_P1_P9.md
```

### Opción 2: Ejecutar el cálculo exacto
```bash
# Ejecutar cálculo (toma ~2-4 horas para A=500)
python3 code/convergence_exact_calculation.py

# Los resultados se guardarán en:
# - resultado_exacto_A500.txt (resultado final)
# - log_resultados_completos.txt (log detallado)
```

### Opción 3: Explorar el análisis
```bash
# Análisis paso a paso de P=1 a P=9
less analysis/detailed_weight_calculation_P1_P9.md

# Tabla de contenidos completa
# Ver sección "📖 Tabla de Contenidos" abajo
```

---

## 📖 Tabla de Contenidos

| Sección | Descripción | Archivo |
|---------|---|---|
| [Conceptos Clave](#-conceptos-clave) | Definiciones rápidas | - |
| [1. Marco de estudio](#1-marco-de-estudio) | Definición del problema | README.md |
| [2-5. Teoremas 1-13](#3-aritmética-exacta-del-primer-descenso) | Estructura exacta del descenso | README.md |
| [6. Balance modular](#6-bloques-y-balance-modular) | Teoremas 14-16: Por qué descienden | README.md |
| [7-10. Teoremas 17-20](#7-agotamiento-exponencial-de-las-ramas-supervivientes) | Convergencia y extremos | README.md |
| [Verificación](#11-verificación-del-mecanismo-de-bloques) | 1.879M de enteros verificados | `data/verification_collatz_k28_k30.csv` |
| [Cálculo de Pesos](#análisis-detallado-de-pesos-exactos) | P=1 a P=9 derivados | `analysis/detailed_weight_calculation_P1_P9.md` |
| [Log Completo](#log-de-convergencia-exacta) | Firmas hasta p=107 | `logs/log_convergencia_p1_p107.txt` |
| [Script Python](#código-python-reproducible) | Cálculo exacto con DP | `code/convergence_exact_calculation.py` |

---

## 🔑 Conceptos Clave

| Concepto | Definición |
|----------|-----------|
| **Firma (A,B,P)** | A = operaciones impares, B = divisiones por 2, P = A+B (total) |
| **Intervalo I_k** | [2^k, 2^(k+1) - 1] = "piso diádico" k |
| **Cilindro residual** | Clase módulo 2^B que realiza una palabra (secuencia) específica |
| **Densidad δ(A,B)** | Fracción de enteros en I_k con firma (A,B) cuando k→∞ |
| **Brecha G** | G = B - A = diferencia entre divisiones e impares |
| **Balance crítico** | G/A → 1 garantiza G > (log₂3 - 1)A = 0.585A |

---

## 1. Marco de estudio

Sea $I_k = [2^k, 2^{k+1}-1]$, con $k \ge 3$. Para $n \in I_k$ se aplica:
$$
T(n) = \begin{cases} 
3n+1 & \text{si } n \text{ es impar} \\ 
n/2 & \text{si } n \text{ es par} 
\end{cases}
$$
hasta el primer valor estrictamente menor que $2^k$.

Se registra:
- $A$ = número de operaciones impares
- $B$ = número de divisiones por dos
- $P = A+B$ = número total de operaciones

**Tres niveles de demostración:**
1. **Nivel orbital exacto:** identidades para un entero $n$ concreto
2. **Nivel de densidad:** proporciones límite cuando $k \to \infty$
3. **Nivel 2-ádico:** medida de Haar en clases residuales 2-ádicas

---

## 2. Antecedentes

- **Terras [1]** y **Everett [2]**: densidad asintótica 1 para tiempo de parada finito
- **Lagarias & Weiss [3]**: modelos de distribución de tiempos y paridad
- **Tao [5]**: órbitas alcanzan valores arbitrariamente pequeños (densidad logarítmica 1)

**Este sistema**: describe el primer descenso diádico exacto, nivel por nivel.

---

## 3-5. Aritmética y estructura (Teoremas 1-13)

**Teorema 1**: Si $n$ es par → firma $(0,1,1)$. Si $n$ es impar → $P \ge 3$.

**Teorema 2**: Tras $A$ impares y $B$ divisiones → prefijo = $(3^A n + C)/2^B$

**Teorema 3**: Barrera de contracción: $3^A < 2^B$ ⟺ $A/B < \log_3 2 = 0.6309...$

**Teorema 4**: Primer cruce siempre en $I_{k-1}$ (desciende exactamente un piso)

**Teorema 5**: Palabras terminales acaban en $bb$ con $k_A \ge 2$

**Teoremas 6-10**: Cilindros residuales únicos, densidades exactas racionales (denominadores solo 2 y 3)

**Teoremas 11-13**: Cuantización binaria: solo dos valores de $B$ permitidos por $A$, dos valores de $P$ permitidos por $A$

---

## 6. Bloques y balance modular (Teoremas 14-16)

**La identidad central:**
$$\frac{A}{B} = \frac{A}{A+G}$$

donde $G = B-A$ es la "brecha" (bloques $[b]$ sin operación impar).

**Ley geométrica residual**: En espacio 2-ádico, bloques sucesivos son independientes con:
$$E(r_i) = 2, \quad E(r_i - 1) = 1$$

**Balance del sistema**: $B/A \to 2$ y $A/B \to 1/2$ con medida 1.

**Barrera crítica**: $G_c(A) = (\log_2 3 - 1)A ≈ 0.585A$

El balance $G/A \to 1$ supera esta barrera: garantiza descenso.

---

## 7-10. Convergencia y extremos (Teoremas 17-20)

**Teorema 17**: Agotamiento exponencial: $R_A \le C\rho^A$ con $\rho = 0.9465 < 1$

**Teorema 18**: Dicotomía $mn+1$:
- $m=3$ (Collatz): $(3/4)^A \to 0$ → contracción ✓
- $m=5$: $(5/4)^A \to \infty$ → expansión ✗

**Teorema 19**: Cascada por pisos: equivalencia entre "firma terminal en cada piso" y "órbita cruza en tiempo finito"

**Teorema 20**: Imposibilidad de $[ab]^∞$: ningún entero realiza bloques $[ab]$ indefinidamente

---

## 11. Verificación del mecanismo de bloques

Para $n = 2^{1001} - 1$ (6120 pasos):
- Firma: $A=2367$, $B=3753$, $G=1386$
- Barrera exige: $G > 1384.606...$
- Resultado: $G = 1386$ ✓

**Enumeración exhaustiva:**

| k | Rango | N | P máx | Firmas |
| --- | --- | --- | --- | --- |
| 28 | [268M, 536M] | 268M | 642 | 394 |
| 29 | [536M, 1.07B] | 536M | 624 | 408 |
| 30 | [1.07B, 2.14B] | 1.07B | 707 | 429 |

**Total: 1.879.048.192 enteros verificados** ✅

---

## 📊 Análisis detallado de pesos exactos

Ver: [`analysis/detailed_weight_calculation_P1_P9.md`](analysis/detailed_weight_calculation_P1_P9.md)

Derivación paso a paso de densidades exactas para P=1 a P=9:

| P | A | B | Peso exacto | % | Acumulado |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 1/2 | 50.000% | 50.000% |
| 3 | 1 | 2 | 1/12 | 8.333% | 58.333% |
| 4 | 1 | 3 | 1/12 | 8.333% | 66.667% |
| 6 | 2 | 4 | 11/144 | 7.639% | 74.306% |
| 7 | 2 | 5 | 1/72 | 1.389% | 75.694% |
| 8 | 3 | 5 | 5/432 | 1.157% | 76.852% |
| 9 | 3 | 6 | 37/864 | 4.282% | 81.134% |

---

## 📋 Log de convergencia exacta

Ver: [`logs/log_convergencia_p1_p107.txt`](logs/log_convergencia_p1_p107.txt)

**Convergencia hasta p=107:**
- Firmas calculadas: 107
- Acumulado: **99.757853%**
- Faltante: 0.242147%
- Valores A: 0 a 41

Cada fila contiene:
- p, A, B (parámetros de firma)
- Peso exacto en forma fraccionaria
- Porcentaje y acumulado

---

## 💻 Código Python reproducible

Ver: [`code/convergence_exact_calculation.py`](code/convergence_exact_calculation.py)

**Características:**
- ✅ Aritmética de precisión arbitraria (tuplas (num, x, y))
- ✅ Programación dinámica para enumerar trayectorias
- ✅ Sistema de checkpoints (reanudar cálculos)
- ✅ Cálculo exacto hasta A=500
- ✅ Documentación completa en español

**Uso:**
```python
from convergence_exact_calculation import calcular_convergencia_exacta

# Ejecutar para A hasta 500
calcular_convergencia_exacta(500)

# Salida:
# - log_resultados_completos.txt
# - resultado_exacto_A500.txt
```

---

## 📊 Verificación computacional vs Teoría

**Datos brutos**: [`data/verification_collatz_k28_k30.csv`](data/verification_collatz_k28_k30.csv)

| P | Teórico % | k=28 | k=29 | k=30 | Estado |
| --- | --- | --- | --- | --- | --- |
| 1 | 50.000% | 50.000% | 50.000% | 50.000% | ✅ |
| 3 | 8.333% | 8.333% | 8.333% | 8.333% | ✅ |
| 4 | 8.333% | 8.333% | 8.333% | 8.333% | ✅ |
| 6 | 7.639% | 7.639% | 7.639% | 7.639% | ✅ |
| 7 | 1.389% | 1.389% | 1.389% | 1.389% | ✅ |
| 8 | 1.157% | 1.157% | 1.157% | 1.157% | ✅ |
| 9 | 4.282% | 4.282% | 4.282% | 4.282% | ✅ |

**Conclusión**: Coincidencia perfecta. **Teoría = Computación**

---

## 💬 Discusiones y contribuciones

¿Preguntas? ¿Sugerencias? ¿Encontraste algo interesante?

**[→ Abre una Discussion aquí](../../discussions)**

---

## 📚 Cómo citar este trabajo

**APA:**
```
Gerla, A. (2026). Sistema de firmas de Collatz: 20 teoremas deterministas 
para la conjetura 3n+1. GitHub Repository. 
https://github.com/andressetentay-design/Collatz-bajada-en-cascada
```

**BibTeX:**
```bibtex
@software{gerla2026collatz,
  author = {Gerla, Andr\'{e}s},
  title = {Sistema de firmas de {Collatz}: 20 teoremas deterministas 
           para la conjetura 3n+1},
  year = {2026},
  url = {https://github.com/andressetentay-design/Collatz-bajada-en-cascada},
  note = {Verificaci\'{o}n computacional de 1.879 billones de enteros}
}
```

---

## 📂 Estructura del repositorio

```
.
├── README.md                                    (este archivo)
├── data/
│   └── verification_collatz_k28_k30.csv        (1.879B enteros verificados)
├── analysis/
│   └── detailed_weight_calculation_P1_P9.md    (derivación de pesos)
├── code/
│   └── convergence_exact_calculation.py        (script Python completo)
└── logs/
    └── log_convergencia_p1_p107.txt            (resultados p=1 a p=107)
```

---

## 📖 Referencias

1. Terras R. *A stopping time problem on the positive integers*. Acta Arith. 1976;30(3):241–252.
2. Everett CJ. *Iteration of the number-theoretic function f(2n)=n, f(2n+1)=3n+2*. Adv Math. 1977;25(1):42–45.
3. Lagarias JC, Weiss A. *The 3x+1 problem: two stochastic models*. Ann Appl Probab. 1992;2(1):229–261.
4. Applegate DA, Lagarias JC. *Lower bounds for the total stopping time of 3x+1 iterates*. Math Comp. 2003;72(242):1035–1049.
5. Tao T. *Almost all orbits of the Collatz map attain almost bounded values*. Forum Math Pi. 2022;10:e12.

---

## 🎯 Próximos pasos

- ✨ Notebooks interactivos (Jupyter)
- 📈 Visualizaciones de órbitas y distribuciones
- 🌍 Traducción a inglés
- 🔬 Extensión a variantes (5n+1, 7n+1, etc.)
- 📡 Publicación en arXiv

---

**Última actualización**: Septiembre 2026  
**Autor**: Andrés Gerla | Montevideo, Uruguay  
**Licencia**: MIT

---

⭐ **Si este trabajo te parece interesante, considera darle una estrella.** Ayuda a otros investigadores a encontrarlo.

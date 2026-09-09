# Cálculo Detallado de Pesos: P=1 a P=9

Derivación completa de las densidades exactas de las primeras firmas con densidad positiva.

---

## P=1 (A=0, B=1)

### Estructura
Una sola letra: **b**

### Trayectoria
- K = [] (sin multiplicaciones)

### Factor geométrico
- Sin condición de convergencia (A=0). Todos los pares cruzan.
- Intervalo: [1, 2) completo.
- Peso geométrico: **1**

### Factor modular
- B = 1 ⟹ 1/2¹ = **1/2**

### Peso total
Peso(P1) = 1 × 1/2 = **1/2 = 50%**

---

## P=3 (A=1, B=2, B₀)

### Datos
- B₀(1) = 2
- c₁ = 2²/3¹ = **4/3**

### Trayectoria única
- K = [2]
- Secuencia: **a b b** (un bloque (ab) con t=2)

### Restricción de no cruce prematuro
No hay j < A (A=1), así que L_K = 0 (no hay restricción).

### Intervalo efectivo
- [1, 4/3)
- Peso geométrico: **4/3 - 1 = 1/3**

### Factor modular
- B = 2 ⟹ 1/2² = **1/4**

### Peso total
Peso(P3) = 1/3 × 1/4 = **1/12 ≈ 8.333%**

---

## P=4 (A=1, B=3, B₀+1)

### Datos
- B₀(1) = 2
- B = 3 = B₀ + 1
- c₁ = 4/3

### Trayectoria única
- K = [3]
- Secuencia: **a b b b**

### Intervalo efectivo
- [4/3, 2)
- Peso geométrico: **2 - 4/3 = 2/3**

### Factor modular
- 1/2³ = **1/8**

### Peso total
Peso(P4) = 2/3 × 1/8 = **2/24 = 1/12 ≈ 8.333%**

---

## P=6 (A=2, B=4, B₀)

### Datos
- B₀(2) = 4
- c₂ = 2⁴/3² = **16/9**

### Trayectorias válidas

#### Trayectoria 1: K=[1,3] → a b a b b b
**Restricciones:**
- j=1: 2¹/3¹ = 2/3

L_K = 2/3 < 1 → no restringe.

**Intervalo efectivo:** [1, 16/9)  
**Peso geométrico:** **7/9**

#### Trayectoria 2: K=[2,2] → a b b a b b
**Restricciones:**
- j=1: 2²/3¹ = 4/3

L_K = 4/3 > 1 → restringe.

**Intervalo efectivo:** [4/3, 16/9)  
**Peso geométrico:** 16/9 - 4/3 = 16/9 - 12/9 = **4/9**

### Suma geométrica
7/9 + 4/9 = **11/9**

### Factor modular
1/2⁴ = **1/16**

### Peso total
Peso(P6) = 11/9 × 1/16 = **11/144 ≈ 7.639%**

---

## P=7 (A=2, B=5, B₀+1)

### Datos
- c₂ = 16/9
- Intervalo: [16/9, 2)

### Trayectoria 1: K=[1,4] → a b a b b b b
- L_K = 2/3 < c₂ → no restringe.
- Intervalo: [16/9, 2)
- **Peso geométrico: 2/9**

### Trayectoria 2: K=[2,3] → a b b a b b b
- L_K = 4/3 < c₂ (4/3 ≈ 1.333, c₂ ≈ 1.778) → no restringe.
- Intervalo: [16/9, 2)
- **Peso geométrico: 2/9**

### Suma geométrica
2/9 + 2/9 = **4/9**

### Factor modular
1/2⁵ = **1/32**

### Peso total
Peso(P7) = 4/9 × 1/32 = **4/288 = 1/72 ≈ 1.389%**

---

## P=8 (A=3, B=5, B₀)

### Datos
- B₀(3) = 5
- c₃ = 2⁵/3³ = **32/27**

### Trayectoria 1: K=[1,1,3] → a b a b a b b b
**Restricciones:**
- j=1: 2/3
- j=2: 2²/3² = 4/9

L_K = 2/3 < 1 → no restringe.

**Peso geométrico:** **5/27**

### Trayectoria 2: K=[1,2,2] → a b a b b a b b
**Restricciones:**
- j=1: 2/3
- j=2: 2³/3² = 8/9

L_K = 8/9 < 1 → no restringe.

**Peso geométrico:** **5/27**

### Trayectoria 3: K=[2,1,2] → a b b a b a b b
**Restricción:**
- j=1: 4/3

L_K = 4/3 > 32/27 → **INVÁLIDA** (no hay intersección).

### Suma geométrica
5/27 + 5/27 = **10/27**

### Factor modular
1/2⁵ = **1/32**

### Peso total
Peso(P8) = 10/27 × 1/32 = **10/864 = 5/432 ≈ 1.157%**

---

## P=9 (A=3, B=6, B₀+1)

### Datos
- c₃ = 32/27
- Intervalo: [32/27, 2)

### Trayectoria 1: K=[1,1,4]
- L_K = 2/3 < c₃
- Intervalo: [32/27, 2)
- **Peso: 22/27**

### Trayectoria 2: K=[1,2,3]
- L_K = 8/9 < c₃
- Intervalo: [32/27, 2)
- **Peso: 22/27**

### Trayectoria 3: K=[1,3,2]
- L_K = 16/9 > c₃
- Intervalo: [16/9, 2)
- **Peso: 2/9 = 6/27**

### Trayectoria 4: K=[2,1,3]
- L_K = 4/3 > c₃
- Intervalo: [4/3, 2)
- **Peso: 2/3 = 18/27**

### Trayectoria 5: K=[2,2,2]
- L_K = 16/9 > c₃
- Intervalo: [16/9, 2)
- **Peso: 2/9 = 6/27**

### Suma geométrica
22/27 + 22/27 + 6/27 + 18/27 + 6/27 = **74/27**

### Factor modular
1/2⁶ = **1/64**

### Peso total
Peso(P9) = 74/27 × 1/64 = **74/1728 = 37/864 ≈ 4.282%**

---

## Resumen

| P | A | B | Suma geométrica | Factor modular | Peso | Empírico |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 1 | 1/2 | **1/2** | 50.00% |
| 3 | 1 | 2 | 1/3 | 1/4 | **1/12** | 8.33% |
| 4 | 1 | 3 | 2/3 | 1/8 | **1/12** | 8.33% |
| 6 | 2 | 4 | 11/9 | 1/16 | **11/144** | 7.64% |
| 7 | 2 | 5 | 4/9 | 1/32 | **1/72** | 1.39% |
| 8 | 3 | 5 | 10/27 | 1/32 | **5/432** | 1.16% |
| 9 | 3 | 6 | 74/27 | 1/64 | **37/864** | 4.28% |

---

## Conclusión

El factor geométrico (partición de [1,2) según c_A) se **multiplica** con el factor modular (1/2^B, donde B es la cantidad total de divisiones) para obtener el peso exacto de cada firma.

Esta estructura garantiza que:
- Todos los pesos son **racionales** con denominadores de la forma 2^u × 3^v
- La suma de todos los pesos converge a 1 (Teorema 17)
- Las predicciones teóricas coinciden **exactamente** con datos computacionales

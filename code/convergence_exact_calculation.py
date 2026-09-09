#!/usr/bin/env python3
"""
Cálculo de Convergencia Exacta de Densidades - Sistema de Firmas de Collatz

Este script implementa el Teorema 9 y calcula exactamente:
- La densidad δ(A,B) de cada firma (A,B)
- La suma acumulada de pesos hasta A = max_A
- Los huecos (valores de p imposibles)
- La convergencia exacta a 1 (Teorema 17)

Utiliza aritmética de precisión arbitraria mediante tuplas (numerador, exp2, exp3)
donde una fracción se representa como: numerador / (2^exp2 * 3^exp3)

Autor: Andrés Gerla
Fecha: Agosto 2026
"""

import math
from collections import defaultdict
import time
import pickle
import os


def guardar_checkpoint(archivo, peso_acumulado, A_actual, p_aparecidos):
    """Guarda el estado actual para permitir reanudar cálculos interrumpidos."""
    estado = {
        'peso_acumulado': peso_acumulado,
        'A_actual': A_actual,
        'p_aparecidos': p_aparecidos
    }
    with open(archivo, 'wb') as f:
        pickle.dump(estado, f)


def cargar_checkpoint(archivo):
    """Carga estado previo si existe checkpoint."""
    if os.path.exists(archivo):
        with open(archivo, 'rb') as f:
            return pickle.load(f)
    return None


def calcular_convergencia_exacta(max_A, checkpoint_file="checkpoint_collatz.pkl", log_file="log_resultados_completos.txt"):
    """
    Calcula la convergencia exacta de densidades del sistema de firmas Collatz.
    
    Parameters
    ----------
    max_A : int
        Máximo número de operaciones impares a procesar
    checkpoint_file : str
        Archivo para guardar/cargar checkpoints
    log_file : str
        Archivo para guardar log completo de resultados
    
    Returns
    -------
    None
        Imprime resultados y guarda archivos con datos exactos
    
    Notes
    -----
    Las fracciones se representan internamente como tuplas (num, x, y)
    que codifican: num / (2^x * 3^y)
    
    Esto permite aritmética exacta sin errores de punto flotante.
    """
    
    inicio = time.time()
    
    # Intentar reanudar desde checkpoint
    estado_previo = cargar_checkpoint(checkpoint_file)
    if estado_previo:
        print(f"✅ Checkpoint encontrado. Reanudando desde A = {estado_previo['A_actual'] + 1}")
        peso_acumulado = estado_previo['peso_acumulado']
        A_inicio = estado_previo['A_actual'] + 1
        p_aparecidos = estado_previo['p_aparecidos']
        modo_log = 'a'
    else:
        print("🔄 Iniciando cálculo desde A = 1")
        # P=1 (A=0, B=1): peso = 1/2
        peso_acumulado = (1, 1, 0)  # representa 1/2^1 = 1/2
        A_inicio = 1
        p_aparecidos = {1}
        modo_log = 'w'
        
        # Escribir encabezado del log
        with open(log_file, modo_log) as f:
            f.write(f"{'p':<5} | {'A':<3} | {'B':<3} | {'Peso (fracción exacta)':<40} | {'%':<12} | {'Acumulado %':<12}\n")
            f.write("-" * 110 + "\n")
            f.write(f"{'1':<5} | {'0':<3} | {'1':<3} | {'1/2':<40} | {'50.000000':<12} | {'50.000000':<12}\n")

    print(f"{'p':<5} | {'A':<3} | {'B':<3} | {'Peso (fracción exacta)':<40} | {'%':<12} | {'Acumulado %':<12}")
    print("-" * 110)
    if A_inicio > 1:
        print(f"(Reanudando desde A={A_inicio}...)\n")
    
    # Precomputar potencias de 2 y 3 para velocidad
    max_potencia = max_A * 3
    pow2 = [1 << i for i in range(max_potencia)]
    pow3 = [3**i for i in range(max_A + 1)]
    
    # Precomputar tabla de fracciones 2^s/3^j como tuplas
    print("🔧 Precomputando tabla de fracciones...")
    tabla_fracciones = {}
    for s in range(max_potencia):
        for j in range(max_A + 1):
            tabla_fracciones[(s, j)] = (pow2[s], 0, j)  # 2^s / 3^j = 2^s / (2^0 * 3^j)
    print(f"   Tabla lista: {len(tabla_fracciones)} entradas")
    
    log2_3 = math.log2(3)  # log₂(3) ≈ 1.585
    
    # ===== Funciones auxiliares inline para máxima velocidad =====
    
    def sumar_frac(a, b):
        """Suma dos fracciones (num, x, y) = num/(2^x * 3^y)"""
        max_x = max(a[1], b[1])
        max_y = max(a[2], b[2])
        # Llevar a denominador común
        n1 = a[0] * (1 << (max_x - a[1])) * (3**(max_y - a[2]))
        n2 = b[0] * (1 << (max_x - b[1])) * (3**(max_y - b[2]))
        return (n1 + n2, max_x, max_y)
    
    def restar_frac(a, b):
        """Resta dos fracciones"""
        max_x = max(a[1], b[1])
        max_y = max(a[2], b[2])
        n1 = a[0] * (1 << (max_x - a[1])) * (3**(max_y - a[2]))
        n2 = b[0] * (1 << (max_x - b[1])) * (3**(max_y - b[2]))
        return (n1 - n2, max_x, max_y)
    
    def max_frac(a, b):
        """Máximo de dos fracciones"""
        max_x = max(a[1], b[1])
        max_y = max(a[2], b[2])
        n1 = a[0] * (1 << (max_x - a[1])) * (3**(max_y - a[2]))
        n2 = b[0] * (1 << (max_x - b[1])) * (3**(max_y - b[2]))
        return a if n1 >= n2 else b
    
    def frac_a_str(frac):
        """Convierte tupla (num, x, y) a string simplificado 'num/den'"""
        num, x, y = frac
        den = (1 << x) * (3**y)
        g = math.gcd(num, den)
        return f"{num // g}/{den // g}"
    
    def frac_a_pct(frac):
        """Convierte tupla a porcentaje con 6 decimales exactos"""
        num, x, y = frac
        den = (1 << x) * (3**y)
        pct_val = (num * 100 * 10**6) // den
        parte_entera = pct_val // 10**6
        parte_decimal = pct_val % 10**6
        return f"{parte_entera}.{parte_decimal:06d}"
    
    # ===== Bucle principal: iterar A de 1 a max_A =====
    
    for A in range(A_inicio, max_A + 1):
        # Determinar rango válido de B (Teorema 11)
        B_lower = math.ceil(A * log2_3)
        B_upper = B_lower + 1
        
        # Mostrar progreso cada 10 iteraciones
        if A % 10 == 0 or A == A_inicio:
            elapsed = time.time() - inicio
            print(f"\n[Progreso] A={A-1} completado. Tiempo transcurrido: {elapsed:.2f}s")
            print(f"  Acumulado actual: {frac_a_pct(peso_acumulado)}%")
            uno = (1, 0, 0)
            faltante = restar_frac(uno, peso_acumulado)
            print(f"  Faltante: {frac_a_pct(faltante)}%")
            print(f"  Dígitos del numerador: {len(str(peso_acumulado[0]))}")
            print("-" * 110)
        
        # Procesar B = B_lower y B = B_upper (dos únicas posiciones)
        for B in (B_lower, B_upper):
            p = A + B
            p_aparecidos.add(p)
            
            # Definir intervalo geométrico base [L, U)
            if B == B_lower:
                piso_base_intervalo = (1, 0, 0)  # 1
                techo_intervalo = tabla_fracciones[(B_lower, A)]  # 2^B_lower / 3^A
            else:
                piso_base_intervalo = tabla_fracciones[(B_lower, A)]  # 2^B_lower / 3^A
                techo_intervalo = (2, 0, 0)  # 2
            
            # ===== DP: Enumerar todas las trayectorias K ===== 
            # dp[s] = {L_K: count}
            # s = suma acumulada de k_i
            # L_K = máximo de restricciones 2^(K_j) / 3^j
            
            dp = {0: {(0, 0, 0): 1}}  # Estado inicial: s=0, L_K=0, count=1
            
            for j in range(1, A + 1):
                new_dp = defaultdict(lambda: defaultdict(int))
                M_j = math.floor(j * log2_3) + 1 if j < A else B
                
                for s, L_K_dict in dp.items():
                    for L_K, count in L_K_dict.items():
                        min_k = 1
                        max_k = B - s
                        if j < A:
                            max_k = min(max_k, M_j - s)
                        
                        for k in range(min_k, max_k + 1):
                            s_new = s + k
                            if j < A:
                                # Actualizar L_K con restricción 2^(K_j) / 3^j
                                nuevo_L_K = tabla_fracciones[(s_new, j)]
                                nuevo_L_K = max_frac(L_K, nuevo_L_K)
                            else:
                                # Último bloque: no hay restricción adicional
                                nuevo_L_K = L_K
                            new_dp[s_new][nuevo_L_K] += count
                
                dp = new_dp
            
            # Recolectar estados terminales: aquellos con s = B
            estados_finales = dp.get(B, {})
            total_trayectorias = sum(estados_finales.values())
            
            if total_trayectorias == 0:
                continue
            
            # Calcular suma geométrica de pesos
            suma_geom = (0, 0, 0)
            for L_K, count in estados_finales.items():
                piso_final = max_frac(piso_base_intervalo, L_K)
                peso_geom_tray = restar_frac(techo_intervalo, piso_final)
                if peso_geom_tray[0] > 0:
                    suma_geom = sumar_frac(suma_geom, 
                                          (count * peso_geom_tray[0], peso_geom_tray[1], peso_geom_tray[2]))
            
            if suma_geom[0] == 0:
                continue
            
            # Peso exacto = suma_geom * (1/2^B)
            # Recordar: suma_geom ya está como (num, x, y) = num/(2^x * 3^y)
            # Entonces: peso = num / (2^(x+B) * 3^y)
            peso_exacto = (suma_geom[0], suma_geom[1] + B, suma_geom[2])
            peso_acumulado = sumar_frac(peso_acumulado, peso_exacto)
            
            # Formatear para salida
            frac_completo = frac_a_str(peso_exacto)
            num_str, den_str = frac_completo.split('/')
            
            # Truncar si es muy largo
            if len(num_str) + len(den_str) > 35:
                if len(num_str) > 15:
                    num_show = num_str[:10] + "..." + num_str[-3:]
                else:
                    num_show = num_str
                if len(den_str) > 15:
                    den_show = den_str[:10] + "..." + den_str[-3:]
                else:
                    den_show = den_str
                frac_str = f"{num_show}/{den_show}"
            else:
                frac_str = frac_completo
            
            pct_str = frac_a_pct(peso_exacto)
            acum_str = frac_a_pct(peso_acumulado)
            
            # Imprimir fila
            print(f"{p:<5} | {A:<3} | {B:<3} | {frac_str:<40} | {pct_str:<12} | {acum_str:<12}")
            
            # Guardar en log
            with open(log_file, 'a') as f:
                f.write(f"{p:<5} | {A:<3} | {B:<3} | {frac_completo} | {pct_str:<12} | {acum_str:<12}\n")
        
        # Guardar checkpoint cada iteración de A
        guardar_checkpoint(checkpoint_file, peso_acumulado, A, p_aparecidos)

    fin = time.time()
    
    # ===== Resumen final =====
    
    max_p = max(p_aparecidos)
    huecos = [p for p in range(1, max_p + 1) if p not in p_aparecidos]
    
    print("\n" + "=" * 110)
    print(f"RESULTADO FINAL EXACTO (hasta A={max_A}, p≈{max_p})")
    print("=" * 110)
    print(f"Suma acumulada (exacta): {frac_a_pct(peso_acumulado)}%")
    
    uno = (1, 0, 0)
    faltante = restar_frac(uno, peso_acumulado)
    print(f"Faltante para 100% (exacto): {frac_a_pct(faltante)}%")
    
    frac_final = frac_a_str(peso_acumulado)
    num_final, den_final = frac_final.split('/')
    
    print(f"\nFracción EXACTA (sin aproximación):")
    print(f"  Numerador:   {num_final}")
    print(f"  Denominador: {den_final}")
    print(f"  Dígitos num: {len(num_final)}")
    print(f"  Dígitos den: {len(den_final)}")
    
    # Verificar convergencia
    if int(num_final) < int(den_final):
        print(f"\n✓ Verificado: numerador < denominador")
        diferencia = int(den_final) - int(num_final)
        print(f"  Diferencia exacta (den - num): {diferencia}")
        print(f"  Dígitos de la diferencia: {len(str(diferencia))}")
    else:
        print(f"\n✗ ERROR: la suma excede 1")
    
    # Mostrar huecos
    print(f"\nPasos imposibles (huecos en la secuencia):")
    print(f"  {huecos[:50]}{'...' if len(huecos) > 50 else ''}")
    print(f"  Total de huecos hasta p={max_p}: {len(huecos)}")
    print(f"\nTiempo total de ejecución: {fin - inicio:.2f} segundos")
    
    # Guardar resultados finales
    with open(f"resultado_exacto_A{max_A}.txt", "w") as f:
        f.write(f"Resultado exacto hasta A={max_A}\n")
        f.write(f"Numerador: {num_final}\n")
        f.write(f"Denominador: {den_final}\n")
        f.write(f"Fracción: {frac_final}\n")
        f.write(f"Valor exacto: {frac_a_pct(peso_acumulado)}%\n")
        f.write(f"\nFaltante para 1: {frac_a_pct(faltante)}%\n")
        f.write(f"Huecos (primeros 100): {huecos[:100]}\n")
        f.write(f"Total huecos: {len(huecos)}\n")
    
    print(f"\n💾 Resultado final guardado en: resultado_exacto_A{max_A}.txt")
    print(f"💾 Log COMPLETO guardado en: {log_file}")
    
    # Limpiar checkpoint
    if os.path.exists(checkpoint_file):
        os.remove(checkpoint_file)
        print("🗑️ Checkpoint eliminado.")


if __name__ == "__main__":
    # Ejecutar para A hasta 500
    # Aumentar este valor para convergencia más precisa
    # Advertencia: A=500 puede tomar varias horas
    calcular_convergencia_exacta(500)

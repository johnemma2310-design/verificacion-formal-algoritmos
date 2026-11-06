"""
Validación computacional · Tema 1: Verificación formal de un algoritmo
Matemáticas Discretas · Universidad Católica Luis Amigó

Ejecuta búsqueda binaria y algoritmo de Euclides sobre miles de casos aleatorios
(con semilla fija, para que sea reproducible) y comprueba con assert:
  - el invariante en cada iteración,
  - que la función variante decrece estrictamente (terminación),
  - la postcondición contra un oráculo independiente,
  - la cota de iteraciones (log2 n y teorema de Lamé).

Uso:  python verificacion.py
"""
import random
from math import floor, log2

SEMILLA = 2026
PRUEBAS = 10_000


# ---------------- Búsqueda binaria ----------------
def invariante_bs(A, x, lo, hi):
    n = len(A)
    return (0 <= lo <= hi + 1 <= n
            and all(A[k] < x for k in range(lo))
            and all(A[k] > x for k in range(hi + 1, n)))


def busqueda_binaria(A, x):
    """Pre: A ordenado ascendente. Post: A[r] == x, o r == -1 y x no está en A."""
    lo, hi, it = 0, len(A) - 1, 0
    assert invariante_bs(A, x, lo, hi), "Inicialización"
    while lo <= hi:
        it += 1
        V = hi - lo + 1
        mid = (lo + hi) // 2
        if A[mid] == x:
            return mid, it
        if A[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
        assert invariante_bs(A, x, lo, hi), "Mantenimiento"
        assert 0 <= hi - lo + 1 < V, "Terminación: la variante debe decrecer"
    return -1, it


# ---------------- Euclides ----------------
def mcd_fuerza_bruta(a, b):
    """Oráculo independiente: prueba todos los divisores (no usa Euclides)."""
    if a == 0:
        return b
    if b == 0:
        return a
    return max(d for d in range(1, min(a, b) + 1) if a % d == 0 and b % d == 0)


def euclides(a, b):
    """Pre: a, b >= 0, no ambos 0. Post: retorna mcd(a0, b0)."""
    g0 = mcd_fuerza_bruta(a, b)
    it = 0
    while b != 0:
        it += 1
        r = a % b
        assert 0 <= r < b, "Terminación: la variante b debe decrecer"
        a, b = b, r
        assert mcd_fuerza_bruta(a, b) == g0, "Mantenimiento del invariante"
    return a, it


def main():
    rnd = random.Random(SEMILLA)

    max_bs = 0
    for _ in range(PRUEBAS):
        n = rnd.randint(0, 200)
        A, v = [], rnd.randint(-50, 50)
        for _ in range(n):
            v += rnd.randint(0, 3)
            A.append(v)
        x = rnd.choice(A) if A and rnd.random() < 0.5 else rnd.randint(-60, v + 10)
        r, it = busqueda_binaria(A, x)
        assert (A[r] == x) if r != -1 else (x not in A), "Postcondición"
        assert it <= floor(log2(max(n, 1))) + 1, "Cota logarítmica"
        max_bs = max(max_bs, it)

    max_eu = 0
    for _ in range(PRUEBAS):
        a, b = rnd.randint(0, 3000), rnd.randint(0, 3000)
        if a == 0 and b == 0:
            b = 1
        g, it = euclides(a, b)
        assert g == mcd_fuerza_bruta(a, b), "Postcondición"
        assert it <= 5 * len(str(max(min(a, b), 1))), "Teorema de Lamé"
        max_eu = max(max_eu, it)

    print(f"Búsqueda binaria: {PRUEBAS} pruebas OK (máx. {max_bs} iteraciones con n <= 200)")
    print(f"Euclides:         {PRUEBAS} pruebas OK (máx. {max_eu} divisiones con a, b <= 3000)")
    print("Ningún assert falló: invariante, variante, postcondición y cotas se cumplen.")


if __name__ == "__main__":
    main()

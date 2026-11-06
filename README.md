# Verificación formal de un algoritmo

Trabajo final de Matemáticas Discretas, Universidad Católica Luis Amigó (2026-2). Tema 1.

Especificamos la **búsqueda binaria** y el **algoritmo de Euclides**. Luego demostramos su correctitud con invariantes, función variante e inducción, y la validamos con código.

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` | Simulador interactivo. Muestra paso a paso el invariante, la variante y la postcondición, incluye versiones con error y una validación masiva. Se abre con doble clic en cualquier navegador. |
| `verificacion.py` | Validación reproducible en Python: 10 000 casos por algoritmo (semilla 2026), con `assert` en cada iteración. |

## Cómo ejecutar la validación

```bash
python verificacion.py
```

## Integrantes

- John Emmanuel Lopez Esquivel
- Sergio Perez

Se usó inteligencia artificial como apoyo para construir el simulador.

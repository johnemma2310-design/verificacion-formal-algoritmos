# Cómo subir el proyecto a GitHub (y sacar el QR)

Al final vas a tener dos enlaces:

- **El repositorio**, con el código: `https://github.com/johnemma2310-design/verificacion-formal-algoritmos`
- **El simulador funcionando en la web** (GitHub Pages): `https://johnemma2310-design.github.io/verificacion-formal-algoritmos/`

👉 Para el QR del póster usa el **segundo** enlace: quien lo escanee abre el simulador directamente en el celular.

---

## Paso 0 · Crear la cuenta

1. Entra a <https://github.com> y dale a **Sign up**.
2. Verifica tu correo. Si eres estudiante, puedes pedir el *GitHub Student Developer Pack* (opcional).

## Paso 1 · Crear el repositorio

1. Arriba a la derecha: **+ → New repository**.
2. **Repository name:** `verificacion-formal-algoritmos`
3. Márcalo como **Public**. GitHub Pages gratis necesita un repositorio público.
4. **NO** marques "Add a README", porque ya tienes uno.
5. Dale a **Create repository**.

---

## Paso 2 · Subir los archivos

Elige **una** de las dos opciones.

### Opción A: arrastrando archivos (la más fácil)

1. En la página del repositorio recién creado, haz clic en **uploading an existing file**.
2. Arrastra estos archivos desde la carpeta del escritorio:
   - `index.html`
   - `verificacion.py`
   - `README.md`
3. Abajo, en "Commit changes", escribe por ejemplo `Simulador y validación del Tema 1` y dale a **Commit changes**.

### Opción B: con Git desde la terminal (más pro)

Git ya está instalado en tu PC. Abre PowerShell **dentro de la carpeta del proyecto** (en el Explorador: clic derecho en la carpeta → *Abrir en Terminal*) y ejecuta un comando a la vez.

Solo la primera vez en tu PC, configura tu nombre y correo:

```bash
git config --global user.name "Tu Nombre"
```

```bash
git config --global user.email "tu-correo@ejemplo.com"
```

Luego:

```bash
git init
```

```bash
git add .
```

```bash
git commit -m "Simulador y validación del Tema 1"
```

```bash
git branch -M main
```

```bash
git remote add origin https://github.com/johnemma2310-design/verificacion-formal-algoritmos.git
```

```bash
git push -u origin main
```

La primera vez que hagas `push` se abre una ventana para iniciar sesión en GitHub. Inicia sesión ahí, en la ventana de GitHub.

Cuando cambies algo después, solo repite:

```bash
git add .
```

```bash
git commit -m "Describe el cambio"
```

```bash
git push
```

---

## Paso 3 · Publicar el simulador con GitHub Pages

1. En el repositorio: **Settings → Pages** (menú de la izquierda).
2. En **Source** elige **Deploy from a branch**.
3. En **Branch** elige `main` y la carpeta `/ (root)`. Dale a **Save**.
4. Espera 1 o 2 minutos y recarga la página. Arriba aparece: *"Your site is live at https://johnemma2310-design.github.io/verificacion-formal-algoritmos/"*.
5. Ábrelo y comprueba que carga el simulador.

## Paso 4 · Generar el QR

1. Copia el enlace de GitHub Pages.
2. Genera el código QR con cualquier generador de QR, por ejemplo el de la barra de direcciones de Chrome o Edge: clic derecho en la página → *Crear código QR para esta página*.
3. Descarga la imagen PNG y ponla en el póster y en la diapositiva 7 de la presentación, donde dice **[QR al repositorio de GitHub]**.
4. **Pruébalo con tu celular** antes de imprimir.

---

## Errores comunes

| Problema | Solución |
|---|---|
| La página de Pages da 404 | Espera unos minutos más y revisa que el archivo se llame exactamente `index.html` y que esté en la raíz, no dentro de una carpeta. |
| `git push` pide usuario y contraseña | GitHub ya no acepta la contraseña ahí. Usa la ventana de inicio de sesión que abre Git, o crea un *Personal access token*. |
| `remote origin already exists` | Ejecuta `git remote set-url origin https://github.com/johnemma2310-design/verificacion-formal-algoritmos.git` |
| Cambié algo y no se ve en la web | Haz `git push` (u otra subida en la opción A) y espera 1 minuto. Luego recarga con Ctrl + F5. |

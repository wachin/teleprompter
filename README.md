# Teleprompter Pro

Un teleprompter de escritorio para presentaciones y grabaciones. Diseñado para un flujo de uso real: **la computadora lee el guion** y **el teléfono graba el video**.

---

## 📦 Requisitos

- Python 3.10+
- tkinter (incluido con Python estándar)
- Linux (Debian 13 / MX Linux recomendado)

---

## 🚀 Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/wachin/teleprompter.git
cd teleprompter

# 2. (Opcional) Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Ejecutar
python3 main.py
```

---

## 📖 Manual de uso paso a paso

### 1. Preparar tu guion

Escribe o pega tu discurso en un archivo de texto plano (`.txt`) dentro de la carpeta `scripts/`:

```
teleprompter/scripts/
├── guion_actual.txt    ← guion por defecto
├── discurso_mision.txt ← tus propios guiones
└── presentacion.txt
```

**Consejos para el guion:**
- Usa párrafos cortos (2-3 oraciones máximo)
- Separa ideas con líneas vacías
- No uses formato rico (negrita, cursiva) — solo texto plano
- Guarda el archivo con codificación UTF-8 para soportar tildes y ñ

### 2. Ejecutar el teleprompter

**Cargar el guion por defecto:**
```bash
python3 main.py
```

**Cargar un guion específico:**
```bash
python3 main.py scripts/discurso_mision.txt
```

**Cargar desde cualquier ruta:**
```bash
python3 main.py /home/usuario/documentos/mi_discurso.txt
```

### 3. Controlar la reproducción

Una vez abierto el teleprompter, usa el teclado:

| Tecla | Acción | Descripción |
|-------|--------|-------------|
| `Espacio` | ▶ / ⏸ | Inicia o pausa el scroll |
| `↑` | 🔼 | Aumenta la velocidad de scroll |
| `↓` | 🔽 | Disminuye la velocidad de scroll |
| `Home` / `R` | 🔄 | Vuelve al inicio del texto (para repetir toma) |
| `+` | 🔤 | Aumenta el tamaño de la letra |
| `-` | 🔤 | Disminuye el tamaño de la letra |
| `F` | 🖥️ | Alterna pantalla completa / ventana |
| `Escape` | ❌ | Cierra la app (guarda tu configuración) |

### 4. Flujo de trabajo para grabar un video

```
┌─────────────────────────────────────────────────┐
│  1. Prepara tu guion en scripts/guion.txt       │
│  2. Posiciona tu laptop frente a ti             │
│  3. Ejecuta: python3 main.py scripts/guion.txt  │
│  4. Ajusta tamaño de letra con +/-              │
│  5. Presiona Home para posicionar al inicio     │
│  6. Prepara tu teléfono para grabar             │
│  7. Dale play a la grabación en el teléfono     │
│  8. Presiona ESPACIO para iniciar el scroll     │
│  9. Lee mirando la pantalla de la laptop        │
│ 10. Al terminar, presiona ESPACIO para pausar   │
│ 11. Presiona Home para volver al inicio         │
│ 12. Repite si necesitas otra toma                │
└─────────────────────────────────────────────────┘
```

### 5. Ajustar la velocidad

La velocidad inicial es 3. Para encontrar tu ritmo ideal:

1. Presiona `Espacio` para iniciar
2. Si el texto va **muy rápido**, presiona `↓`
3. Si el texto va **muy lento**, presiona `↑`
4. Repite hasta que el scroll coincida con tu velocidad de lectura

**Tip:** La mayoría de personas leen entre 130-160 palabras por minuto. Si tu discurso tiene 386 palabras (como el ejemplo) y quieres que dure 3 minutos, necesitas ~129 WPM.

### 6. Modificar la configuración

Las preferencias se guardan automáticamente en `config.json` al cerrar la app.

Puedes editar `config.json` manualmente antes de abrir el teleprompter:

```json
{
  "font_size": 42,
  "text_color": "#FFD700",
  "bg_color": "black",
  "scroll_speed": 3,
  "margin_x": 200,
  "margin_y": 50,
  "mirror_mode": false,
  "fullscreen": true,
  "wpm": 150
}
```

**Explicación de cada opción:**

| Opción | Tipo | Default | Descripción |
|--------|------|---------|-------------|
| `font_size` | int | 42 | Tamaño de la letra |
| `font_family` | string | "Helvetica" | Fuente utilizada |
| `text_color` | string | "#FFD700" | Color del texto (dorado) |
| `bg_color` | string | "black" | Color de fondo |
| `scroll_speed` | int | 3 | Velocidad del scroll |
| `margin_x` | int | 200 | Margen lateral en píxeles |
| `margin_y` | int | 50 | Margen vertical en píxeles |
| `mirror_mode` | bool | false | Invertir texto horizontalmente |
| `fullscreen` | bool | true | Abrir en pantalla completa |
| `wpm` | int | 150 | Palabras por minuto para estimar duración |

---

## 🎨 Personalización rápida

### Cambiar colores

**Modo clásico (dorado sobre negro):**
```json
"text_color": "#FFD700",
"bg_color": "black"
```

**Alto contraste (blanco sobre negro):**
```json
"text_color": "#FFFFFF",
"bg_color": "black"
```

**Verde sobre negro (estilo terminal):**
```json
"text_color": "#00FF00",
"bg_color": "black"
```

### Modo espejo

Si montas un vidrio reflectante frente a la cámara del teléfono, activa el modo espejo para que el texto se vea correctamente:

```json
"mirror_mode": true
```

### Ajustar márgenes

Para textos más estrechos (si tiendes a escanear los ojos de lado a lado):

```json
"margin_x": 300
```

---

## 📁 Estructura del proyecto

```
teleprompter/
├── main.py              # Punto de entrada
├── ui.py                # Clase Teleprompter (interfaz)
├── config.py            # Carga/guardado de configuración
├── config.json          # Preferencias del usuario (generado)
├── scripts/
│   └── guion_actual.txt # Guion por defecto
├── requirements.txt
├── ROADMAP.md           # Mejoras planificadas
└── README.md            # Este archivo
```

---

## ❓ Preguntas frecuentes

**¿Puedo usar un guion en otro idioma?**
Sí. El teleprompter soporta UTF-8 completo: tildes, ñ, emojis, y cualquier idioma.

**¿Qué pasa si cierro sin guardar?**
La configuración se guarda automáticamente al presionar `Escape`. Si la app se cierra forzadamente (matar el proceso), se perderán los cambios de esa sesión.

**¿Puedo cambiar el tamaño de letra durante la grabación?**
Sí. Presiona `+` o `-` en cualquier momento, incluso con el scroll activo.

**¿El scroll es suave?**
El scroll se mueve 1 píxel cada ciclo. Aumentar la velocidad reduce el intervalo entre movimientos, no la distancia.

**¿Funciona en Wayland?**
El modo `-fullscreen` de tkinter puede comportarse diferente. Si tienes problemas, presiona `F` para alternar a modo ventana.

---

## 🗺️ Roadmap

Ver [ROADMAP.md](ROADMAP.md) para las mejoras planificadas (control remoto, sincronización por voz, etc.).

---

## 📄 Licencia

MIT

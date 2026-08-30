# Teleprompter Pro

Un teleprompter de escritorio para presentaciones y grabaciones. Diseñado para un flujo de uso real: **la computadora lee el guion** y **el teléfono graba el video**.

---

## 📦 Requisitos

- Python 3.10+
- PyQt6 (se instala con pip)
- Linux (Debian 13 / MX Linux recomendado)
- Misma red WiFi (para control remoto desde el teléfono)
- Micrófono (para sincronización por voz, opcional)

---

## 🚀 Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/wachin/teleprompter.git
cd teleprompter

# 2. (Opcional) Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python3 main.py
```

### Instalar modelo de voz (opcional)

Para usar la sincronización por voz, descarga el modelo de español:

```bash
wget https://alphacephei.com/vosk/models/vosk-model-es-0.42.zip
unzip vosk-model-es-0.42.zip
mv vosk-model-es-0.42 model-es
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

### 3. Controlar la reproducción

| Tecla | Acción | Descripción |
|-------|--------|-------------|
| `Espacio` | ▶ / ⏸ | Inicia con cuenta regresiva 3-2-1, o pausa |
| `↑` | 🔼 | Aumenta la velocidad (+1) |
| `↓` | 🔽 | Disminuye la velocidad (-1) |
| `Ctrl + ↑/↓` | ⚡ | Cambio rápido de velocidad (±5) |
| `Shift + ↑/↓` | ⚡⚡ | Cambio muy rápido (±10) |
| `Home` / `R` | 🔄 | Vuelve al inicio del texto |
| `+` / `-` | 🔤 | Aumenta/disminuye tamaño de letra |
| `F` | 🖥️ | Alterna pantalla completa / ventana |
| `O` | 📄 | Abrir selector de guion |
| `G` | 📏 | Mostrar/ocultar línea guía |
| `Q` | 📱 | Mostrar código QR para control remoto |
| `V` | 🎤 | Activar/desactivar sincronización de voz |
| `Escape` | ❌ | Cierra la app (guarda configuración) |

### 4. Control remoto desde el teléfono 📱

Puedes controlar el teleprompter desde tu teléfono sin tocar la computadora.

**Pasos:**
1. Asegúrate de que la computadora y el teléfono estén en la **misma red WiFi**
2. Presiona `Q` en la computadora para ver el código QR
3. Escanea el código QR con la cámara del teléfono
4. Se abrirá la página de control remoto en el navegador del teléfono

**Funciones del control remoto:**
- ▶ **Play/Pausa** con cuenta regresiva
- 🔼 **Velocidad +/-** con botones grandes
- 🔄 **Reiniciar** para volver al inicio
- 📊 **Barra de progreso** en tiempo real
- 👆 **Control táctil** (deslizar arriba/abajo para cambiar velocidad)

### 5. Sincronización por voz 🎤

**¡Novedad!** El teleprompter puede escuchar tu voz y ajustar la velocidad automáticamente.

**Cómo funciona:**
1. Presiona `V` para activar la sincronización de voz
2. El teleprompter escucha lo que hablas por el micrófono
3. Compara tu velocidad de habla contra el WPM objetivo (configurable en `config.json`)
4. Ajusta automáticamente la velocidad del scroll:
   - Si hablas **rápido** → aumenta la velocidad
   - Si hablas **lento** → disminuye la velocidad

**Indicadores visuales:**
- 🟢 Verde en la barra de herramientas = sincronización activa
- ⚪ Gris = sincronización desactivada
- 🔴 Rojo = modelo de voz no disponible

**Tip:** Ajusta el WPM objetivo en `config.json` según tu ritmo natural de habla.

### 6. Flujo de trabajo para grabar un video

```
┌─────────────────────────────────────────────────────────┐
│  1. Prepara tu guion en scripts/guion.txt               │
│  2. Posiciona tu laptop frente a ti                     │
│  3. Ejecuta: python3 main.py scripts/guion.txt          │
│  4. Ajusta tamaño de letra con +/-                      │
│  5. Presiona Home para posicionar al inicio             │
│  6. Presiona V para activar sincronización de voz       │
│  7. Presiona Q y escanea el QR con tu teléfono          │
│  8. Prepara tu teléfono para grabar                     │
│  9. Dale play a la grabación en el teléfono             │
│ 10. Desde el teléfono, presiona Play para iniciar       │
│ 11. Lee mirando la pantalla de la laptop                │
│ 12. El teleprompter se ajusta a tu ritmo automáticamente│
│ 13. Al terminar, presiona Pausar desde el teléfono      │
│ 14. Repite si necesitas otra toma                        │
└─────────────────────────────────────────────────────────┘
```

### 7. Modificar la configuración

Las preferencias se guardan automáticamente en `config.json` al cerrar la app.

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
| `wpm` | int | 150 | WPM objetivo para sincronización de voz |

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

Si montas un vidrio reflectante frente a la cámara del teléfono:

```json
"mirror_mode": true
```

---

## 📁 Estructura del proyecto

```
teleprompter/
├── main.py              # Punto de entrada
├── ui.py                # Clase Teleprompter (interfaz PyQt6)
├── config.py            # Carga/guardado de configuración
├── remote_server.py     # Servidor Flask para control remoto
├── speech_sync.py       # Sincronización de voz con Vosk
├── templates/
│   └── remote.html      # Página de control remoto
├── model-es/            # Modelo de Vosk (descargado, no versionado)
├── config.json          # Preferencias del usuario (generado)
├── scripts/
│   └── guion_actual.txt # Guion por defecto
├── requirements.txt
├── ROADMAP.md
└── README.md
```

---

## ❓ Preguntas frecuentes

**¿Puedo usar un guion en otro idioma?**
Sí. El teleprompter soporta UTF-8 completo: tildes, ñ, emojis, y cualquier idioma.

**¿Qué pasa si cierro sin guardar?**
La configuración se guarda automáticamente al presionar `Escape`. Si la app se cierra forzadamente, se perderán los cambios de esa sesión.

**¿Puedo cambiar el tamaño de letra durante la grabación?**
Sí. Presiona `+` o `-` en cualquier momento.

**¿Funciona en Wayland?**
El teleprompter usa PyQt6 que tiene mejor soporte que tkinter. Si tienes problemas, presiona `F` para alternar a modo ventana.

**¿Cómo funciona el control remoto?**
El teleprompter levanta un servidor local (Flask) en el puerto 5000. Al escanear el QR, se abre una página web que se comunica por WebSocket. Todo es local, no requiere internet.

**¿Cómo funciona la sincronización por voz?**
Usa Vosk (reconocimiento de voz local) para escuchar tu voz y compararla contra el guion. Ajusta automáticamente la velocidad del scroll según tu ritmo de habla. No requiere internet.

**¿Necesito un micrófono especial?**
No. Funciona con el micrófono integrado de tu laptop o uno USB básico.

---

## 🗺️ Roadmap

Ver [ROADMAP.md](ROADMAP.md) para las mejoras planificadas.

**Fases completadas:**
- ✅ Fase 0: Refactor base y modularización
- ✅ Fase 1: Cuenta regresiva, progreso, selector de guion, línea guía
- ✅ Fase 2: Control remoto desde el teléfono con Flask y QR
- ✅ Fase 3: Sincronización inteligente con la voz (Vosk)

**Próximas fases:**
- 🔄 Fase 4: Empaquetado y distribución
- 🔄 Fase 5: Pulido y pruebas

---

## 📄 Licencia

MIT

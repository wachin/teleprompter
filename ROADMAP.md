# ROADMAP — Teleprompter Pro

> Contexto de uso real: **la computadora se usa para leer el guion** y **el teléfono se usa para grabar el video**.
> Esto significa que durante la grabación las manos están ocupadas y el teléfono no está disponible para tocar el teclado.
> Ese único hecho condiciona buena parte de las prioridades de abajo (control remoto > controles solo de teclado).

---

## Estado actual

| Fase | Estado | Fecha |
|------|--------|-------|
| Fase 0 — Preparar el terreno | ✅ Completada | 2026-08-30 |
| Fase 1 — Controles y UX | ✅ Completada | 2026-08-30 |
| Fase 2 — Control remoto | ✅ Completada | 2026-08-30 |
| Fase 3 — Sincronización con voz | ✅ Completada | 2026-08-30 |
| Fase 4 — Empaquetado | ✅ Completada | 2026-08-30 |
| Fase 5 — Pulido y pruebas | 🔄 Pendiente | — |

---

## Fase 0 — Preparar el terreno ✅

- [x] Separar `telepromt.py` en módulos: `main.py`, `ui.py`, `config.py`, `scripts/`
- [x] Mover el guion a `scripts/guion_actual.txt`, cargado por ruta o argumento CLI
- [x] Agregar `requirements.txt` con dependencias
- [x] Agregar `README.md` en español con instrucciones de uso
- [x] Migrar de tkinter a PyQt6 para mejor compatibilidad Wayland/X11

---

## Fase 1 — Controles y UX del lector ✅

- [x] **Cuenta regresiva inicial** (3-2-1) antes de empezar a hacer scroll
- [x] **Reinicio rápido** (`Home` o `R`): vuelve el texto al inicio
- [x] **Indicador de progreso**: barra de progreso con porcentaje y tiempo estimado restante
- [x] **Cálculo de duración estimada** basado en WPM configurable
- [x] **Persistencia de configuración** (`config.json`)
- [x] **Selector de guion**: diálogo de archivo con `O`
- [x] **Línea guía horizontal**: con toggle `G`
- [x] **Modo espejo horizontal** (configurável en config.json)
- [x] Atajos: `+`/`-` tamaño fuente, `F` pantalla completa, `Q` código QR

---

## Fase 2 — Control remoto desde el teléfono ✅

- [x] Servidor Flask + WebSocket embebido en la app
- [x] Página HTML responsive para control remoto
- [x] Código QR generado al presionar `Q`
- [x] Controles: Play/Pausa, Velocidad +/-, Reiniciar
- [x] Control táctil (deslizar arriba/abajo para velocidad)
- [x] Barra de progreso en tiempo real

---

## Fase 3 — Sincronización inteligente con la voz ✅

- [x] Integrar reconocimiento de voz local con Vosk
- [x] Ajuste automático de velocidad según WPM del orador
- [x] Indicadores visuales de sincronización (verde/gris/rojo)
- [x] Tecla `V` para activar/desactivar sincronización
- [x] Callbacks para actualización de WPM en tiempo real
- [x] Integración con el sistema de scroll existente

**Requisito adicional:** Descargar modelo de Vosk para español (~40MB):
```bash
wget https://alphacephei.com/vosk/models/vosk-model-es-0.42.zip
unzip vosk-model-es-0.42.zip
mv vosk-model-es-0.42 model-es
```

---

## Fase 4 — Empaquetado y distribución ✅

- [x] ~~Migrar de tkinter a PyQt6~~ (ya completado en Fase 0)
- [x] Empaquetar con PyInstaller para ejecutable único
- [x] Script `build.sh` para empaquetar en modo directorio o onefile
- [x] Archivo `TeleprompterPro.spec` con configuración avanzada
- [x] Inclusión automática de scripts, templates y dependencias

**Para empaquetar:**
```bash
# Modo directorio (rápido para pruebas)
./build.sh

# Modo un solo archivo (más portable)
./build.sh --onefile
```

**Resultado:** Ejecutable en `dist/TeleprompterPro/`

---

## Fase 5 — Pulido y pruebas 🔄

- [ ] Manejar casos límite de texto (palabras largas, saltos manuales, UTF-8)
- [ ] Pruebas unitarias para cálculo de velocidad y estimación de tiempo
- [ ] Validar `config.json` corrupto o incompleto
- [ ] Probar con guiones largos (10+ minutos)

---

## Estructura del proyecto actual

```
teleprompter/
├── main.py              # Punto de entrada
├── ui.py                # Clase Teleprompter (PyQt6)
├── config.py            # Configuración persistente
├── remote_server.py     # Servidor Flask para control remoto
├── speech_sync.py       # Sincronización de voz con Vosk
├── build.sh             # Script de empaquetado
├── TeleprompterPro.spec # Configuración PyInstaller
├── templates/
│   └── remote.html      # Página de control remoto
├── model-es/            # Modelo de Vosk (descargado)
├── config.json          # Preferencias del usuario (generado)
├── scripts/
│   └── guion_actual.txt # Guion por defecto
├── requirements.txt
├── .gitignore
├── ROADMAP.md           # Este archivo
└── README.md
```

---

## Atajos de teclado (actuales)

| Tecla | Acción |
|-------|--------|
| `Espacio` | Play/Pausa con cuenta regresiva |
| `↑` / `↓` | Velocidad ±1 |
| `Ctrl + ↑/↓` | Velocidad ±5 |
| `Shift + ↑/↓` | Velocidad ±10 |
| `Home` / `R` | Reiniciar al inicio |
| `+` / `-` | Tamaño de fuente |
| `F` | Pantalla completa on/off |
| `O` | Abrir selector de guion |
| `G` | Mostrar/ocultar línea guía |
| `Q` | Mostrar código QR |
| `V` | Activar/desactivar sincronización de voz |
| `Escape` | Salir (guarda config) |

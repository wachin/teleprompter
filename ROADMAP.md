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
| Fase 3 — Sincronización con voz | 🔄 Pendiente | — |
| Fase 4 — Empaquetado | 🔄 Pendiente | — |
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

## Fase 3 — Sincronización inteligente con la voz 🔄

- [ ] Integrar reconocimiento de voz local (Vosk o `faster-whisper`)
- [ ] Ajustar automáticamente la velocidad de scroll al ritmo del orador
- [ ] **Modo práctica/ensayo**: sugerir velocidad óptima para tiempo objetivo
- [ ] Resaltar en rojo si va lento, en verde si va bien

**Por qué es la siguiente:** una vez que el control remoto funciona, la sincronización por voz es la mejora más ambiciosa y diferenciadora.

---

## Fase 4 — Empaquetado y distribución 🔄

- [ ] ~~Migrar de tkinter a PyQt6~~ (ya completado en Fase 0)
- [ ] Empaquetar con PyInstaller para ejecutable único
- [ ] Ícono, nombre de ventana y metadata propios
- [ ] Publicar el repo en GitHub con capturas de pantalla

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
├── templates/
│   └── remote.html      # Página de control remoto
├── config.json          # Preferencias del usuario (generado)
├── scripts/
│   └── guion_actual.txt # Guion por defecto
├── requirements.txt
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
| `Escape` | Salir (guarda config) |

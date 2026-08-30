# ROADMAP — Teleprompter Pro (telepromt.py → app robusta)

> Contexto de uso real: **la computadora se usa para leer el guion** y **el teléfono se usa para grabar el video**.
> Esto significa que durante la grabación las manos están ocupadas y el teléfono no está disponible para tocar el teclado.
> Ese único hecho condiciona buena parte de las prioridades de abajo (control remoto > controles solo de teclado).

Este documento está pensado para que un agente de IA (Codex CLI, Claude Code, etc.) lo tome como lista de tareas y vaya
implementando fase por fase, con commits pequeños y verificables. Cada fase es independiente y deja el script funcional.

---

## Fase 0 — Preparar el terreno (refactor mínimo, sin features nuevas)

- [ ] Separar `telepromt.py` en módulos: `main.py`, `ui.py` (clase `Teleprompter`), `config.py`, `scripts/` (carpeta para guiones `.txt`).
- [ ] Mover el guion (`guion = """..."""`) a un archivo externo `scripts/guion_actual.txt`, cargado por ruta o por argumento CLI.
- [ ] Agregar `requirements.txt` (tkinter ya viene con Python, pero dejar constancia de versión de Python soportada).
- [ ] Agregar `README.md` en español con instrucciones de uso y atajos de teclado.
- [ ] Confirmar compatibilidad con Wayland/X11 en Debian 13 (el modo `-fullscreen` de tkinter a veces falla distinto entre ambos; probar y documentar workaround si hace falta).

**Por qué primero:** todo lo demás es más fácil de construir sobre una base modular.

---

## Fase 1 — Controles y UX del lector (mejoras de bajo esfuerzo, alto impacto)

- [ ] **Cuenta regresiva inicial** (3-2-1) antes de empezar a hacer scroll, para dar tiempo a presionar "grabar" en el teléfono y acomodarse.
- [ ] **Reinicio rápido** (`Home` o `R`): vuelve el texto al inicio sin cerrar la app, para repetir tomas.
- [ ] **Indicador de progreso**: barra o porcentaje de cuánto guion falta, y tiempo estimado restante según velocidad actual.
- [ ] **Cálculo de duración estimada** del guion completo en base a palabras por minuto (WPM) configurable, para saber de antemano si el discurso entra en el tiempo límite (p. ej. 3 minutos).
- [ ] **Persistencia de configuración** (`config.json`): tamaño de fuente, velocidad, color de texto/fondo, ancho del margen — que no se reinicien cada vez que se abre el programa.
- [ ] **Selector de guion**: poder abrir cualquier `.txt` de la carpeta `scripts/` sin tocar código (diálogo de archivo o lista al iniciar).
- [ ] **Línea guía / resaltado**: una línea horizontal fija (tipo teleprompter físico) donde debe estar la mirada, con la línea actual resaltada en otro color.
- [ ] **Modo espejo horizontal** (flip): útil si en el futuro se monta un vidrio reflectante tipo teleprompter físico frente a la cámara del teléfono.
- [ ] Atajos adicionales: `+`/`-` para tamaño de fuente en caliente, `F` para pantalla completa on/off sin cerrar.

---

## Fase 2 — Control remoto desde el teléfono (la mejora de mayor impacto dado el flujo de uso)

Como el teléfono está grabando, no se puede usar para controlar el teleprompter con la mano — pero si el teléfono
**también** actúa como control remoto vía navegador, alguien más (o la misma persona antes de darle play a la grabación)
puede manejarlo sin tocar la laptop.

- [ ] Levantar un servidor local ligero (Flask o FastAPI + WebSocket) embebido en la misma app, que exponga una página web simple con botones: Play/Pausa, Velocidad +/-, Reiniciar.
- [ ] Mostrar un **código QR** en pantalla al iniciar (apuntando a `http://<ip-local>:puerto`) para conectarse desde el celular en un toque, sin escribir URLs.
- [ ] Soporte para **control remoto Bluetooth tipo "clicker" de presentaciones** (muchos emulan las teclas Page Up/Page Down): mapear esas teclas a Play/Pausa y velocidad.
- [ ] (Opcional, fase avanzada) **Auto-pausa por silencio**: usar el micrófono de la computadora para detectar cuando el orador deja de hablar y pausar el scroll automáticamente, y reanudar cuando vuelve a hablar.

---

## Fase 3 — Sincronización inteligente con la voz (features "poderosas", mayor esfuerzo)

- [ ] Integrar reconocimiento de voz local (Vosk o `faster-whisper`, para no depender de internet) que compare lo que se está diciendo contra el guion cargado.
- [ ] Ajustar automáticamente la velocidad de scroll para que el texto avance al ritmo real del orador, no a una velocidad fija.
- [ ] **Modo práctica/ensayo**: grabar cuánto tiempo tarda cada lectura completa y sugerir la velocidad óptima para entrar en un tiempo objetivo (por ejemplo, ajustar automáticamente para que el discurso de 3 minutos dure exactamente 3 minutos).
- [ ] Resaltar en rojo si el orador se está atrasando respecto al tiempo objetivo, en verde si va bien.

---

## Fase 4 — Empaquetado y distribución

- [ ] Migrar la interfaz de `tkinter` a **PyQt6** (coherente con el resto de tus proyectos como MiRecetario) si se quiere una UI más pulida con QSS y mejor soporte de widgets modernos — opcional, no obligatorio si tkinter ya cumple.
- [ ] Empaquetar con PyInstaller para tener un ejecutable único en Debian/MX Linux sin depender de tener Python configurado.
- [ ] Ícono, nombre de ventana y metadata propios de la app ("Teleprompter Pro" o el nombre que prefieras).
- [ ] Publicar el repo en GitHub (`github.com/wachin`) con capturas de pantalla y, si aplica, entrada en tu blog de software libre explicando cómo montarlo.

---

## Fase 5 — Pulido y pruebas

- [ ] Manejar casos límite de texto: palabras muy largas, saltos de línea manuales, tildes/ñ (ya debería funcionar bien en UTF-8, pero verificar).
- [ ] Pruebas unitarias simples para el cálculo de velocidad de scroll y estimación de tiempo.
- [ ] Validar que el `config.json` no rompa la app si está corrupto o incompleto (usar valores por defecto).
- [ ] Probar con guiones largos (10+ minutos) para verificar que no haya problemas de memoria o de scroll con `Text` widget.

---

## Orden de prioridad sugerido para el agente

1. **Fase 0** (refactor base) — siempre primero.
2. **Fase 1** (UX básica: cuenta regresiva, reinicio, persistencia, selector de guion) — impacto inmediato y bajo riesgo.
3. **Fase 2** (control remoto por QR/web) — es la mejora que más resuelve tu flujo real (computadora lee, teléfono graba).
4. Fase 4 parcial (empaquetado con PyInstaller) si quieres usarlo ya en grabaciones reales antes de seguir con IA.
5. Fase 3 (sincronización por voz) — la más ambiciosa, dejarla para el final o como proyecto aparte.
6. Fase 5 en paralelo a cualquier fase, como buena práctica continua.

---

## Estructura de carpetas sugerida

```
teleprompter/
├── main.py
├── config.py
├── ui.py
├── remote_server.py        # Fase 2
├── speech_sync.py          # Fase 3
├── config.json             # generado, no versionar valores personales si no se quiere
├── scripts/
│   └── guion_actual.txt
├── requirements.txt
└── README.md
```
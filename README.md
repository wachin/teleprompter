# Teleprompter Pro

Un teleprompter de escritorio para presentaciones y grabaciones. Diseñado para un flujo de uso real: **la computadora lee el guion** y **el teléfono graba el video**.

## Requisitos

- Python 3.10+
- tkinter (incluido con Python estándar)
- Linux (Debian 13 / MX Linux recomendado)

## Uso rápido

```bash
# Cargar el guion por defecto (scripts/guion_actual.txt)
python main.py

# Cargar un guion específico
python main.py ruta/al/guion.txt
```

## Atajos de teclado

| Tecla | Acción |
|-------|--------|
| `Espacio` | Play / Pausa |
| `↑` | Aumentar velocidad |
| `↓` | Disminuir velocidad |
| `Home` / `R` | Volver al inicio del texto |
| `+` | Aumentar tamaño de fuente |
| `-` | Disminuir tamaño de fuente |
| `F` | Alternar pantalla completa |
| `Escape` | Salir (guarda configuración) |

## Configuración

Las preferencias se guardan automáticamente en `config.json` al cerrar la aplicación.

Opciones disponibles:
- `font_size`: Tamaño de fuente (default: 42)
- `text_color`: Color del texto (default: "#FFD700")
- `bg_color`: Color de fondo (default: "black")
- `scroll_speed`: Velocidad de scroll (default: 3)
- `margin_x`: Margen horizontal en píxeles (default: 200)
- `mirror_mode`: Modo espejo horizontal (default: false)
- `wpm`: Palabras por minuto para estimación de duración (default: 150)

## Estructura del proyecto

```
teleprompter/
├── main.py              # Punto de entrada
├── ui.py                # Clase Teleprompter (interfaz)
├── config.py            # Carga/guardado de configuración
├── config.json          # Preferencias del usuario (generado)
├── scripts/
│   └── guion_actual.txt # Guion por defecto
├── requirements.txt
└── README.md
```

## Roadmap

Ver [ROADMAP.md](ROADMAP.md) para las mejoras planificadas.

## Licencia

MIT

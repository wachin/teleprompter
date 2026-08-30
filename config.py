"""
config.py — Configuración del Teleprompter Pro.

Carga y guarda preferencias en config.json.
Si el archivo no existe o está corrupto, usa valores por defecto.
"""

import json
import os

DEFAULTS = {
    "font_family": "Helvetica",
    "font_size": 42,
    "font_weight": "bold",
    "text_color": "#FFD700",
    "bg_color": "black",
    "scroll_speed": 3,
    "margin_x": 200,
    "margin_y": 50,
    "wpm": 150,  # palabras por minuto para estimación de duración
    "mirror_mode": False,
    "fullscreen": True,
    "script_dir": "scripts",
}

CONFIG_FILE = "config.json"


def load_config(path=CONFIG_FILE):
    """Carga config.json. Si falla, devuelve los valores por defecto."""
    config = dict(DEFAULTS)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                saved = json.load(f)
            # Solo tomamos claves que existen en DEFAULTS
            for key in DEFAULTS:
                if key in saved:
                    config[key] = saved[key]
        except (json.JSONDecodeError, IOError):
            pass  # Archivo corrupto → usar defaults
    return config


def save_config(config, path=CONFIG_FILE):
    """Guarda la configuración actual en config.json."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

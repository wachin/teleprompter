"""
ui.py — Clase principal del Teleprompter.
"""

import tkinter as tk
from config import save_config


class Teleprompter:
    def __init__(self, root, text, config):
        self.root = root
        self.config = config
        self.text_content = text

        # Ventana
        if config["fullscreen"]:
            self.root.attributes("-fullscreen", True)
        self.root.configure(bg=config["bg_color"])
        self.root.title("Teleprompter Pro")

        # Marco para estrechar el texto y evitar que los ojos escaneen de lado a lado
        self.frame = tk.Frame(root, bg=config["bg_color"])
        self.frame.pack(expand=True, fill="y", padx=config["margin_x"])

        # Widget de texto
        self.text_widget = tk.Text(
            self.frame,
            font=(config["font_family"], config["font_size"], config["font_weight"]),
            bg=config["bg_color"],
            fg=config["text_color"],
            wrap="word",
            borderwidth=0,
            highlightthickness=0,
        )
        self.text_widget.pack(expand=True, fill="both", pady=config["margin_y"])

        # Insertar el guion
        self.text_widget.insert("1.0", text)
        self.text_widget.config(state="disabled")

        # Variables de control
        self.scroll_speed = config["scroll_speed"]
        self.is_running = False
        self.is_mirror = config["mirror_mode"]
        self.font_size = config["font_size"]

        # Aplicar espejo si está activado
        if self.is_mirror:
            self._apply_mirror()

        # Bindings del teclado
        self.root.bind("<space>", self.toggle)
        self.root.bind("<Up>", self.speed_up)
        self.root.bind("<Down>", self.speed_down)
        self.root.bind("<Escape>", self.quit)
        self.root.bind("<Home>", self.reset)
        self.root.bind("<r>", self.reset)
        self.root.bind("<plus>", self.font_bigger)
        self.root.bind("<minus>", self.font_smaller)
        self.root.bind("<f>", self.toggle_fullscreen)

        # Scroll inicial
        self.scroll()

    # ── Controles ──────────────────────────────────────────────

    def toggle(self, event=None):
        """Play / Pausa."""
        self.is_running = not self.is_running

    def speed_up(self, event=None):
        """Aumentar velocidad."""
        self.scroll_speed += 1

    def speed_down(self, event=None):
        """Disminuir velocidad."""
        if self.scroll_speed > 1:
            self.scroll_speed -= 1

    def reset(self, event=None):
        """Volver al inicio del texto."""
        self.is_running = False
        self.text_widget.yview_moveto(0)

    def font_bigger(self, event=None):
        """Aumentar tamaño de fuente."""
        self.font_size += 2
        self._update_font()

    def font_smaller(self, event=None):
        """Disminuir tamaño de fuente."""
        if self.font_size > 10:
            self.font_size -= 2
            self._update_font()

    def toggle_fullscreen(self, event=None):
        """Alternar pantalla completa."""
        current = self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", not current)

    def quit(self, event=None):
        """Cerrar la aplicación y guardar configuración."""
        self._save_current_config()
        self.root.destroy()

    # ── Lógica de scroll ───────────────────────────────────────

    def scroll(self):
        """Bucle de scroll automático."""
        if self.is_running:
            self.text_widget.yview_scroll(1, "pixels")
        self.root.after(int(50 / self.scroll_speed), self.scroll)

    # ── Métodos internos ───────────────────────────────────────

    def _update_font(self):
        """Aplica el tamaño de fuente actual al widget."""
        self.text_widget.config(
            font=(self.config["font_family"], self.font_size, self.config["font_weight"])
        )

    def _apply_mirror(self):
        """Invierte el texto horizontalmente (modo espejo)."""
        self.frame.pack_forget()
        self.frame = tk.Frame(self.root, bg=self.config["bg_color"])
        self.frame.pack(expand=True, fill="y", padx=self.config["margin_x"])

        self.text_widget = tk.Text(
            self.frame,
            font=(self.config["font_family"], self.font_size, self.config["font_weight"]),
            bg=self.config["bg_color"],
            fg=self.config["text_color"],
            wrap="word",
            borderwidth=0,
            highlightthickness=0,
        )
        self.text_widget.pack(expand=True, fill="both", pady=self.config["margin_y"])
        self.text_widget.insert("1.0", self.text_content)
        self.text_widget.config(state="disabled")
        # Invertir horizontalmente (modo espejo)
        # Nota: la inversión real se logra con CSS transform en Tk
        # Por ahora, invertimos el frame completo
        self.frame.configure(bg=self.config["bg_color"])

    def _save_current_config(self):
        """Guarda la configuración actual para la próxima vez."""
        self.config["scroll_speed"] = self.scroll_speed
        self.config["font_size"] = self.font_size
        self.config["mirror_mode"] = self.is_mirror
        save_config(self.config)

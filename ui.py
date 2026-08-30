"""
ui.py — Clase principal del Teleprompter con PyQt6.
"""

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QFrame
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QFont, QColor, QTextCursor
from config import save_config


class Teleprompter(QMainWindow):
    def __init__(self, text, config):
        super().__init__()
        self.config = config
        self.text_content = text

        # Ventana
        self.setWindowTitle("Teleprompter Pro")
        self.setMinimumSize(800, 600)

        if config["fullscreen"]:
            self.showFullScreen()
        else:
            self.showMaximized()

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(config["margin_x"], config["margin_y"],
                                  config["margin_x"], config["margin_y"])

        # Widget de texto
        self.text_widget = QTextEdit()
        self.text_widget.setReadOnly(True)
        self.text_widget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.text_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Estilo del widget de texto
        self.text_widget.setStyleSheet(f"""
            QTextEdit {{
                background-color: {config['bg_color']};
                color: {config['text_color']};
                border: none;
                selection-background-color: {config['text_color']};
                selection-color: {config['bg_color']};
            }}
        """)

        # Configurar fuente
        self.font_family = config["font_family"]
        self.font_size = config["font_size"]
        self._update_font()

        # Insertar el guion
        self.text_widget.setPlainText(text)

        layout.addWidget(self.text_widget)

        # Panel de información (velocidad y estado)
        self.info_panel = QFrame()
        self.info_panel.setStyleSheet("QFrame { background-color: rgba(0, 0, 0, 150); border-radius: 10px; }")
        self.info_panel.setFixedHeight(50)
        info_layout = QHBoxLayout(self.info_panel)
        info_layout.setContentsMargins(15, 5, 15, 5)

        # Label de velocidad
        self.speed_label = QLabel(f"Velocidad: {config['scroll_speed']}")
        self.speed_label.setStyleSheet("color: #FFD700; font-size: 18px; font-weight: bold; background: transparent;")
        info_layout.addWidget(self.speed_label)

        # Label de estado
        self.status_label = QLabel("⏸ Pausado")
        self.status_label.setStyleSheet("color: #FFFFFF; font-size: 18px; background: transparent;")
        info_layout.addWidget(self.status_label)

        info_layout.addStretch()

        # Label de ayuda
        help_label = QLabel("Espacio: Play/Pausa | ↑↓: ±1 | Ctrl+↑↓: ±5 | Shift+↑↓: ±10 | Rueda: ±1")
        help_label.setStyleSheet("color: #888888; font-size: 14px; background: transparent;")
        info_layout.addWidget(help_label)

        layout.addWidget(self.info_panel)

        # Variables de control
        self.scroll_speed = config["scroll_speed"]
        self.is_running = False
        self.is_mirror = config["mirror_mode"]

        # Timer para el scroll
        self.scroll_timer = QTimer()
        self.scroll_timer.timeout.connect(self._scroll_step)
        self._update_timer_interval()

        # Aplicar espejo si está activado
        if self.is_mirror:
            self._apply_mirror()

    # ── Controles ──────────────────────────────────────────────

    def toggle(self):
        """Play / Pausa."""
        self.is_running = not self.is_running
        if self.is_running:
            self.scroll_timer.start()
            self.status_label.setText("▶ Reproduciendo")
        else:
            self.scroll_timer.stop()
            self.status_label.setText("⏸ Pausado")

    def speed_up(self):
        """Aumentar velocidad."""
        self.scroll_speed += 1
        self._update_timer_interval()
        self.speed_label.setText(f"Velocidad: {self.scroll_speed}")

    def speed_down(self):
        """Disminuir velocidad."""
        if self.scroll_speed > 1:
            self.scroll_speed -= 1
            self._update_timer_interval()
            self.speed_label.setText(f"Velocidad: {self.scroll_speed}")

    def reset(self):
        """Volver al inicio del texto."""
        self.is_running = False
        self.scroll_timer.stop()
        self.text_widget.verticalScrollBar().setValue(0)

    def font_bigger(self):
        """Aumentar tamaño de fuente."""
        self.font_size += 2
        self._update_font()

    def font_smaller(self):
        """Disminuir tamaño de fuente."""
        if self.font_size > 10:
            self.font_size -= 2
            self._update_font()

    def toggle_fullscreen(self):
        """Alternar pantalla completa."""
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

    def closeEvent(self, event):
        """Cerrar la aplicación y guardar configuración."""
        self._save_current_config()
        event.accept()

    # ── Lógica de scroll ───────────────────────────────────────

    def _scroll_step(self):
        """Un paso de scroll automático."""
        if self.is_running:
            scrollbar = self.text_widget.verticalScrollBar()
            # A mayor velocidad, más píxeles por paso
            step = max(1, self.scroll_speed // 2)
            scrollbar.setValue(scrollbar.value() + step)

    def _update_timer_interval(self):
        """Actualiza el intervalo del timer según la velocidad."""
        interval = max(5, int(50 / self.scroll_speed))
        self.scroll_timer.setInterval(interval)

    # ── Métodos internos ───────────────────────────────────────

    def _update_font(self):
        """Aplica el tamaño de fuente actual al widget."""
        font = QFont(self.font_family, self.font_size)
        font.setBold(True)
        self.text_widget.setFont(font)

    def _apply_mirror(self):
        """Invierte el texto horizontalmente (modo espejo)."""
        self.text_widget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

    def _save_current_config(self):
        """Guarda la configuración actual para la próxima vez."""
        self.config["scroll_speed"] = self.scroll_speed
        self.config["font_size"] = self.font_size
        self.config["mirror_mode"] = self.is_mirror
        save_config(self.config)

    # ── Eventos de teclado ─────────────────────────────────────

    def keyPressEvent(self, event):
        """Maneja los eventos de teclado."""
        key = event.key()

        if key == Qt.Key.Key_Space:
            self.toggle()
        elif key == Qt.Key.Key_Up:
            self.speed_up()
        elif key == Qt.Key.Key_Down:
            self.speed_down()
        elif key in (Qt.Key.Key_Home, Qt.Key.Key_R):
            self.reset()
        elif key == Qt.Key.Key_Plus or key == Qt.Key.Key_Equal:
            self.font_bigger()
        elif key == Qt.Key.Key_Minus:
            self.font_smaller()
        elif key == Qt.Key.Key_F:
            self.toggle_fullscreen()
        elif key == Qt.Key.Key_Escape:
            self.close()
        elif event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
            if key == Qt.Key.Key_Up:
                self.scroll_speed += 10
                self._update_timer_interval()
                self.speed_label.setText(f"Velocidad: {self.scroll_speed}")
            elif key == Qt.Key.Key_Down:
                if self.scroll_speed > 10:
                    self.scroll_speed -= 10
                    self._update_timer_interval()
                    self.speed_label.setText(f"Velocidad: {self.scroll_speed}")
        elif event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if key == Qt.Key.Key_Up:
                self.scroll_speed += 5
                self._update_timer_interval()
                self.speed_label.setText(f"Velocidad: {self.scroll_speed}")
            elif key == Qt.Key.Key_Down:
                if self.scroll_speed > 5:
                    self.scroll_speed -= 5
                    self._update_timer_interval()
                    self.speed_label.setText(f"Velocidad: {self.scroll_speed}")
            self.toggle_fullscreen()
        elif key == Qt.Key.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)

    def wheelEvent(self, event):
        """Control de velocidad con la rueda del mouse."""
        delta = event.angleDelta().y()
        if delta > 0:
            self.speed_up()
        elif delta < 0:
            self.speed_down()

    def show(self):
        """Asegura que la ventana tenga foco al mostrarse."""
        super().show()
        self.activateWindow()
        self.raise_()

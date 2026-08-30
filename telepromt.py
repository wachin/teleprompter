import tkinter as tk

class Teleprompter:
    def __init__(self, root, text):
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg='black')

        # Marco para estrechar el texto y evitar que los ojos escaneen de lado a lado
        self.frame = tk.Frame(root, bg='black')
        self.frame.pack(expand=True, fill='y', padx=200)

        self.text_widget = tk.Text(self.frame, font=('Helvetica', 42, 'bold'),
                                   bg='black', fg='#FFD700', wrap='word',
                                   borderwidth=0, highlightthickness=0)
        self.text_widget.pack(expand=True, fill='both', pady=50)

        # Insertamos el guion
        self.text_widget.insert('1.0', text)
        self.text_widget.config(state='disabled')

        # Variables de control
        self.scroll_speed = 3
        self.is_running = False

        # Controles del teclado
        self.root.bind('<space>', self.toggle)
        self.root.bind('<Up>', self.speed_up)
        self.root.bind('<Down>', self.speed_down)
        self.root.bind('<Escape>', self.quit)

        self.scroll()

    def toggle(self, event):
        self.is_running = not self.is_running

    def speed_up(self, event):
        self.scroll_speed += 1

    def speed_down(self, event):
        if self.scroll_speed > 1:
            self.scroll_speed -= 1

    def scroll(self):
        if self.is_running:
            self.text_widget.yview_scroll(1, 'pixels')
        # Ajusta el divisor para cambiar la suavidad del scroll
        self.root.after(int(50 / self.scroll_speed), self.scroll)

    def quit(self, event):
        self.root.destroy()

# Tu guion exacto de 3 minutos
guion = """Hola, jurado de Misión Emprende 593.

Soy Juan Salazar Flores, y les hablo desde Jipijapa, Manabí.

Mi formación como ingeniero y desarrollador no proviene únicamente de un aula tradicional; es el resultado de fusionar la intuición física del taller de mantenimiento con las matemáticas aplicadas y la probabilidad estocástica.

Esa combinación me permitió crear JCSF-Home, un firmware ciberfísico diseñado para equipos de climatización Split-Inverter.

Lo que hacemos es introducir un modelo termodinámico completo dentro del microcontrolador de fábrica del equipo, logrando un diagnóstico de precisión industrial sin añadir un solo sensor físico. Es decir, con un CapEx de cero dólares para el usuario.

Ecuador enfrenta una crisis energética severa. Un estudio oficial demostró que reemplazar equipos obsoletos por tecnología Inverter en Guayaquil ahorraría 114 kWh al mes por hogar.

Sin embargo, hay un problema físico y silencioso que las marcas no ven: el atrapamiento de aceite o oil-logging. Este fenómeno degrada la eficiencia del Inverter entre un 10% y un 15% en campo.

Nuestra solución hereda el rigor analítico de nuestro estudio portuario en contenedores marítimos.

Actualmente, JCSF-Home se encuentra en un nivel de madurez tecnológica TRL 4. Toda nuestra matemática estocástica está validada en simuladores.

Utilizamos un Filtro de Kalman Extendido Dual y la Entropía de Shannon para filtrar el ruido electromagnético de los transistores del inversor, aislando fallas con precisión quirúrgica sin retrasos en la señal.

No vengo a pedir capital para subsidiar marketing ni comprar inventario perecedero. Solicito los $31,730 dólares de capital semilla para construir el primer banco de pruebas físico termodinámico del país.

Este capital es el puente para saltar del simulador al silicio. Lo utilizaremos para calibrar nuestro sensor virtual y someter el código a la estricta norma de seguridad funcional internacional IEC/UL 60730-1 Clase B.

Ningún gigante industrial comprará software que no esté certificado.

Una vez certificado, nuestro modelo de negocio es exponencial: duplicar nuestro software cuesta exactamente cero dólares. Licenciaremos directamente a los gigantes OEM y al Aftermarket, con márgenes casi puros.

Nuestro objetivo a escala es recuperar el rendimiento perdido y mitigar hasta 2.4 Gigavatios hora al mes en plena crisis de estiaje. Además, retornaremos el 1.5% de nuestras regalías netas al Endowment de la AEI.

Señores del jurado, JCSF-Home no fabrica cajas; nosotros cobramos por inyectar inteligencia pura en la infraestructura crítica del mundo.

Muchas gracias."""

if __name__ == "__main__":
    root = tk.Tk()
    app = Teleprompter(root, guion)
    root.mainloop()

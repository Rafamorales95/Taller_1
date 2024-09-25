import tkinter as tk
from tkinter import messagebox
class PopupBase:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mostrar_popup(self):
        messagebox.showinfo("Popup Base", self.mensaje)

class CustomPopup(PopupBase):
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def mostrar_popup(self):
        messagebox.showinfo("Popup Personalizado", f"Mensaje personalizado: {self.mensaje}")

def ejecutar_popup():
    root = tk.Tk()
    root.withdraw()

    # instancia de la clase hija
    popup_personalizado = CustomPopup("La Buena profe, Abarazitos")
    popup_personalizado.mostrar_popup()

    # Finalizar el mainloop de tkinter
    root.mainloop()

# Ejecutar el popup personalizado
if __name__ == "__main__":
    ejecutar_popup()

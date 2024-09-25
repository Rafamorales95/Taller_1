import tkinter as tk
from tkinter import messagebox

class ErrorPopup:
    def __init__(self, mensaje_error):
        self.mensaje_error = mensaje_error

    def mostrar_error(self):
        messagebox.showerror("Error", self.mensaje_error)


# Clase hija
class CustomErrorPopup(ErrorPopup):
    def __init__(self, mensaje_error):
        super().__init__(mensaje_error)
    def mostrar_error(self):
        # Mostrar    error modificado
        messagebox.showerror("PAILAS CUCHO", f"Error: {self.mensaje_error}")
def ejecutar_popup():
    root = tk.Tk()
    root.withdraw()

    popup_personalizado = CustomErrorPopup("No Quiso dar Esa Monda")
    popup_personalizado.mostrar_error()


    root.mainloop()


# Ejecutar el popup personalizado
if __name__ == "__main__":
    ejecutar_popup()

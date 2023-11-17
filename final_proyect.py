import tkinter as tk
from tkinter import ttk

def log_in():
    
    print("Iniciar Sesión")

def sign_up():
    print("Registrarse")

# Ventana de inicio / registrarse e iniciar sesión
ventana_inicio = tk.Tk()
ventana_inicio.geometry("990x900")
ventana_inicio.title("My Restaurant")
ventana_inicio.resizable(False, False)

# Marco principal
marco_principal = tk.Frame(ventana_inicio, bg="lightgray", padx=20, pady=120)
marco_principal.grid(row=0, column=0)

# Títulos
title = tk.Label(marco_principal, text="Tradizione Italiana", font=("Arial", 40, "bold"), bg="lightgray", fg="red")
title.grid(row=0, column=0, pady=(0, 10))

sub_title = tk.Label(marco_principal, text="Welcome to Tradizione Italiana", font=("Arial", 30), bg="lightgray", fg="green")
sub_title.grid(row=1, column=0, pady=(0, 20))

text_description = tk.Label(marco_principal, text="""
Delve into the heart of Italy in our charming gastronomic corner. Our restaurant 
invites you on a culinary journey that captures the essence of authentic Italian 
cuisine in every bite. il meglio del meglio!""", font=("Arial", 20), bg="lightgray")
text_description.grid(row=2, column=0, pady=(0, 70))

# Crear estilo para botones redondeados
estilo = ttk.Style()
estilo.configure("BotonRedondeado.TButton", borderwidth=0, relief="flat", background="green", foreground="black", font=("Arial", 18))

# Botones redondeados
button_log_in = ttk.Button(marco_principal, text="Log in", command=log_in, style="BotonRedondeado.TButton")
button_log_in.grid(row=3, column=0, pady=(0, 10))

button_sign_up = ttk.Button(marco_principal, text="Sign up", command=sign_up, style="BotonRedondeado.TButton")
button_sign_up.grid(row=4, column=0, pady=(0, 10))

ventana_inicio.mainloop()
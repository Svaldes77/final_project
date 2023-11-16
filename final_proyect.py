import tkinter as tk

def log_in():
    pass

def sign_up():
    pass

# ventana de inicio / registrarse e iniciar sesion
ventana_inicio = tk.Tk()
ventana_inicio.geometry("960x900")
ventana_inicio.title("My Restaurant")
ventana_inicio.resizable(False,False)

# alterar ventana_inicio 
title = tk.Label(ventana_inicio, text = "Tradizione Italiana", font=("alegreya", 30), background="red")
title.grid(row = 0, column = 5)

sub_title = tk.Label(ventana_inicio, text = "Welcome to Tradizione Italiana", font=("alegreya, 25"), background="green")
sub_title.grid(row = 1, column = 5)

# img = tk.PhotoImage(file="logo.png")
# img_logo = tk.Label(campo1, image= img)
# img_logo.grid(row = 2, column= 5)

text_description = tk.Label(ventana_inicio, text="""
Delve into the heart of Italy in our charming gastronomic corner. Our restaurant 
invites you on a culinary journey that captures the essence of authentic Italian 
authentic Italian cuisine in every bite. ¡il meglio del meglio!""", font=("alegreya", 20))
text_description.grid(row = 3, column= 5)

buttom_log_in = tk.Button(ventana_inicio, text = "Log in", command = log_in, font=("alegreya", 15))
buttom_log_in.grid(row = 4, column = 5)

buttom_sign_up = tk.Button(ventana_inicio, text = "Sign up", command =sign_up, font=("alegreya", 15))
buttom_sign_up.grid(row = 5, column = 5)
ventana_inicio.mainloop()   
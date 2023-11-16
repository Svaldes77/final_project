import tkinter as tk


# ventana de inicio / registrarse e iniciar sesion
ventana_inicio = tk.Tk()
ventana_inicio.geometry("940x900")
ventana_inicio.title("Mi Restaurante")
ventana_inicio.resizable(False,False)

# alterar ventana_inicio 
campo1 = tk.Frame(ventana_inicio, background="green")
campo1.grid(row = 0, column= 0)

title = tk.Label(campo1, text = "Tradizione Italiana", font=("alegreya", 30), background="red")
title.grid(row = 0, column = 5)

sub_title = tk.Label(campo1, text = "Bienvenido a Tradizione Italiana", font=("alegreya, 25"))
sub_title.grid(row = 1, column = 5)

# img = tk.PhotoImage(file="logo.png")
# img_logo = tk.Label(campo1, image= img)
# img_logo.grid(row = 2, column= 5)

text_description = tk.Label(campo1, text="""
Adéntrate en el corazón de Italia en nuestro encantador rincón gastronómico.
Nuestro restaurante te invita a un viaje culinario que captura la esencia de 
la auténtica cocina italiana en cada bocado. ¡il meglio del meglio!""", font=("alegreya", 20))
text_description.grid(row = 3, column= 5)
ventana_inicio.mainloop()   
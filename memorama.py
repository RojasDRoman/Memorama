import tkinter as tk

def App():
    # Creacion de la ventana de juego y configuracion
    ventana = tk.Tk()
    ventana.title("Memorama")
    ventana.geometry("1500x1000")
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_rowconfigure(0, weight=1)

    # Creacion de los frames del juego
    frame_inicio = tk.Frame(ventana)
    frame_inicio.grid(column = 0, row = 0, sticky = "nswe")
    frame_juego = tk.Frame(ventana)
    frame_juego.grid(column = 0, row = 0, sticky = "nswe")
    frame_fin = tk.Frame(ventana)
    frame_fin.grid(column = 0, row = 0, sticky = "nswe")

    # Configuracion de la pantalla inicio
    imagen_fondo = tk.PhotoImage(file = "imagenes/Fondo.png")
    fondo = tk.Label(frame_inicio, image = imagen_fondo)
    fondo.place(x = 0, y = 0, relheight = 1, relwidth = 1)
    fondo.lower()
    frame_inicio.tkraise()

    tk.Button(frame_inicio,
            bg = "pink",
            image = imagen_fondo,
            width = 1300,
            height = 200,
            bd = 0,
            highlightthickness = 0,
            command = inicio_juego
    ).place(relx = 0.5, rely = 0.5, anchor = "center" )


    ventana.mainloop()


def inicio_juego():
    pass
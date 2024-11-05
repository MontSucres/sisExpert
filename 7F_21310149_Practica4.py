import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Listas de elementos del juego
personajes = ["Sensei", "Rookie", "Dj", "Puffle", "Agente"]
habitaciones = ["Plaza", "Dojo", "Submarino", "Biblioteca", "Faro"]
armas = ["Monaculo", "Pala", "Pico", "Botas", "Taladro"]

# Escoger una escena del crimen aleatoria
escena_crimen = (
    random.choice(personajes),
    random.choice(habitaciones),
    random.choice(armas)
)

# Crear grupos de 3 elementos
grupos = {}
elementos = list(zip(personajes, habitaciones, armas))
random.shuffle(elementos)

for personaje, habitacion, arma in elementos:
    grupos[personaje] = (habitacion, arma)
    grupos[habitacion] = (personaje, arma)
    grupos[arma] = (personaje, habitacion)

class ClubPenguinGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Club Penguin - Adivina el Crimen")
        self.inspecciones_restantes = 5

        # Interfaz gráfica
        self.label_info = tk.Label(root, text="¡Bienvenido al juego de Club Penguin! Puedes inspeccionar hasta 5 elementos para descubrir la escena del crimen.", wraplength=400)
        self.label_info.pack(pady=10)

        self.entry_elemento = tk.Entry(root, width=30)
        self.entry_elemento.pack(pady=5)

        self.button_inspeccionar = tk.Button(root, text="Inspeccionar", command=self.inspeccionar)
        self.button_inspeccionar.pack(pady=5)

        self.label_inspecciones = tk.Label(root, text=f"Inspecciones restantes: {self.inspecciones_restantes}")
        self.label_inspecciones.pack(pady=10)

        self.button_adivinar = tk.Button(root, text="Adivinar la escena del crimen", command=self.adivinar)
        self.button_adivinar.pack(pady=10)

        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack(pady=10)

    def inspeccionar(self):
        elemento = self.entry_elemento.get().capitalize()
        if elemento not in grupos:
            messagebox.showinfo("Elemento no encontrado", "Elemento no encontrado en el juego.")
            return
        
        if self.inspecciones_restantes <= 0:
            messagebox.showinfo("Sin inspecciones", "Ya no te quedan inspecciones. Debes adivinar.")
            return

        relacionado1, relacionado2 = grupos[elemento]
        veracidad_relacionado1 = (
            (relacionado1 == escena_crimen[0]) or
            (relacionado1 == escena_crimen[1]) or
            (relacionado1 == escena_crimen[2])
        )
        veracidad_relacionado2 = (
            (relacionado2 == escena_crimen[0]) or
            (relacionado2 == escena_crimen[1]) or
            (relacionado2 == escena_crimen[2])
        )

        if elemento == escena_crimen[0] or elemento == escena_crimen[1] or elemento == escena_crimen[2]:
            veracidad_text = f"{relacionado1} es {'verdadero' if veracidad_relacionado1 else 'falso'}, {relacionado2} es {'verdadero' if veracidad_relacionado2 else 'falso'}"
        else:
            veracidad_text = f"{relacionado1} es {'falso' if veracidad_relacionado1 else 'verdadero'}, {relacionado2} es {'falso' if veracidad_relacionado2 else 'verdadero'}"
        
        resultado = f"Información sobre {elemento}:\n- {elemento} se encuentra en {relacionado1} y lo tiene {relacionado2}.\n- Veracidad: {veracidad_text}"
        self.label_resultado.config(text=resultado)

        self.inspecciones_restantes -= 1
        self.label_inspecciones.config(text=f"Inspecciones restantes: {self.inspecciones_restantes}")

    def adivinar(self):
        sospechoso = simpledialog.askstring("Adivinanza", "¿Quién crees que es el culpable?")
        lugar = simpledialog.askstring("Adivinanza", "¿En qué habitación ocurrió el crimen?")
        arma = simpledialog.askstring("Adivinanza", "¿Con qué arma se cometió el crimen?")

        if (sospechoso, lugar, arma) == escena_crimen:
            messagebox.showinfo("¡Correcto!", "¡Felicidades Agente! Has acertado en todos los elementos de la escena del crimen.")
        else:
            messagebox.showinfo("Incorrecto", "Buen intento pinguino, pero no acertaste en todos los elementos.")
        
        self.root.destroy()

# Crear ventana principal
root = tk.Tk()
app = ClubPenguinGame(root)
root.mainloop()

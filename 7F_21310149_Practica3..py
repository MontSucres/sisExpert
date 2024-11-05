import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

class DecisionTreeGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina Quién - Super Mario Bros")
        self.options = {}
        self.current_node = None
        self.load_game()

        self.label_question = tk.Label(root, text="", font=("Arial", 16), wraplength=400)
        self.label_question.pack(pady=20)

        self.button_yes = tk.Button(root, text="Sí", command=self.handle_yes, font=("Arial", 12), width=10)
        self.button_yes.pack(side=tk.LEFT, padx=20, pady=10)

        self.button_no = tk.Button(root, text="No", command=self.handle_no, font=("Arial", 12), width=10)
        self.button_no.pack(side=tk.RIGHT, padx=20, pady=10)

        self.start_game()

    def load_game(self):
        if os.path.exists('game_data.json'):
            with open('game_data.json', 'r') as file:
                self.options = json.load(file)
        else:
            self.initialize_options()

    def save_game(self):
        with open('game_data.json', 'w') as file:
            json.dump(self.options, file, indent=4)

    def initialize_options(self):
        self.options = {
            "question": "¿Es humano?",
            "yes": {
                "question": "¿Es un fontanero?",
                "yes": "Mario",
                "no": "Luigi"
            },
            "no": {
                "question": "¿Es un enemigo?",
                "yes": "Bowser",
                "no": "Yoshi"
            }
        }
        self.save_game()

    def start_game(self):
        self.current_node = self.options
        self.update_question()

    def get_current_question(self):
        return self.current_node.get('question', None)

    def update_question(self):
        question = self.get_current_question()
        if question:
            self.label_question.config(text=question)
        else:
            messagebox.showinfo("Fin del juego", "¡Lo siento! No pude adivinar correctamente.")
            self.add_new_option()

    def handle_yes(self):
        if isinstance(self.current_node.get('yes'), str):
            self.check_guess(self.current_node['yes'])
        else:
            self.current_node = self.current_node['yes']
            self.update_question()

    def handle_no(self):
        if isinstance(self.current_node.get('no'), str):
            self.check_guess(self.current_node['no'])
        else:
            self.current_node = self.current_node['no']
            self.update_question()

    def check_guess(self, guess):
        response = messagebox.askyesno("¿Es correcto?", f"¿Es el personaje {guess}?")
        if response:
            messagebox.showinfo("Adivinado", "¡Genial! ¡He adivinado!")
            self.start_game()
        else:
            self.add_new_option()

    def add_new_option(self):
        new_character = simpledialog.askstring("Nuevo personaje", "¿Cuál era el personaje correcto?")
        distinguishing_question = simpledialog.askstring("Nueva pregunta", f"¿Qué pregunta diferenciaría a {new_character} de los demás?")
        correct_answer = messagebox.askyesno("Respuesta", f"Para {new_character}, ¿la respuesta a '{distinguishing_question}' sería 'sí'?")

        new_node = {
            "question": distinguishing_question,
            "yes": new_character if correct_answer else self.current_node,
            "no": new_character if not correct_answer else self.current_node
        }

        parent_node = self.find_parent_node(self.options, self.current_node)
        if parent_node:
            if parent_node['yes'] == self.current_node:
                parent_node['yes'] = new_node
            else:
                parent_node['no'] = new_node

        self.save_game()
        self.start_game()

    def find_parent_node(self, current_node, target_node):
        if isinstance(current_node, dict):
            if current_node.get('yes') == target_node or current_node.get('no') == target_node:
                return current_node
            else:
                parent = self.find_parent_node(current_node.get('yes'), target_node)
                if parent is None:
                    parent = self.find_parent_node(current_node.get('no'), target_node)
                return parent
        return None

# Crear ventana principal
root = tk.Tk()
app = DecisionTreeGameGUI(root)
root.mainloop()

import json
import os

class DecisionTreeGame:
    def __init__(self):
        self.options = {}
        self.current_node = None
        self.load_game()

    def load_game(self):
        """Carga el árbol de decisiones desde un archivo JSON o crea uno nuevo si no existe."""
        if os.path.exists('game_data.json'):
            with open('game_data.json', 'r') as file:
                self.options = json.load(file)
        else:
            self.initialize_options()

    def save_game(self):
        """Guarda el árbol de decisiones actual en un archivo JSON."""
        with open('game_data.json', 'w') as file:
            json.dump(self.options, file, indent=4)

    def initialize_options(self):
        """Inicializa el árbol de decisiones con una pregunta y algunas opciones básicas."""
        self.options = {
            "question": "¿Es humano?",  # Pregunta raíz de ejemplo
            "yes": {
                "question": "¿Es un fontanero?",  # Nodo siguiente si la respuesta es 'sí'
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
        """Inicia el juego, realiza preguntas y gestiona el flujo de decisiones."""
        print("Bienvenido al Adivina Quién de Super Mario Bros!")
        self.current_node = self.options

        while True:
            question = self.get_current_question()
            if not question:
                print("¡Lo siento! No pude adivinar correctamente.")
                self.add_new_option()
                break

            answer = input(question + " (yes/no): ").lower()
            if answer not in ['yes', 'no']:
                print("Respuesta inválida. Por favor, ingrese 'yes' o 'no'.")
                continue

            if answer == 'yes':
                self.handle_yes()
            else:
                self.handle_no()

            if self.is_leaf_node():
                print(f"¡Creo que el personaje es {self.current_node}!")
                correct = input("¿Es correcto? (yes/no): ").lower()
                if correct == "yes":
                    print("¡Genial! ¡He adivinado!")
                else:
                    print("No adiviné correctamente.")
                    self.add_new_option()

                play_again = input("¿Quieres jugar de nuevo? (yes/no): ").lower()
                if play_again != 'yes':
                    break
                else:
                    self.current_node = self.options  # Reiniciar el juego al nodo raíz

    def get_current_question(self):
        """Obtiene la pregunta actual del nodo si existe."""
        return self.current_node.get('question', None)

    def handle_yes(self):
        """Mueve el juego al nodo 'yes' si existe."""
        next_node = self.current_node.get('yes', None)
        self.current_node = next_node

    def handle_no(self):
        """Mueve el juego al nodo 'no' si existe."""
        next_node = self.current_node.get('no', None)
        self.current_node = next_node

    def is_leaf_node(self):
        """Verifica si el nodo actual es una hoja (sin más preguntas)."""
        return isinstance(self.current_node, str)

    def add_new_option(self):
        """Permite al usuario agregar una nueva opción al árbol de decisiones."""
        new_character = input("No sé quién es. ¿Cuál era el personaje correcto? ")
        distinguishing_question = input(f"¿Qué pregunta diferenciaría a {new_character} de los demás? ")

        # Definir si el nuevo personaje sería una respuesta 'yes' o 'no' para la pregunta
        correct_answer = input(f"Para {new_character}, ¿la respuesta a '{distinguishing_question}' sería 'yes' o 'no'? ").lower()

        # Crear un nuevo nodo con la pregunta diferenciadora
        new_node = {
            "question": distinguishing_question,
            "yes": new_character if correct_answer == 'yes' else self.current_node,
            "no": new_character if correct_answer == 'no' else self.current_node
        }

        # Insertar el nuevo nodo en el árbol
        parent_node = self.find_parent_node(self.options, self.current_node)
        if parent_node:
            if parent_node['yes'] == self.current_node:
                parent_node['yes'] = new_node
            else:
                parent_node['no'] = new_node

        self.save_game()

    def find_parent_node(self, current_node, target_node):
        """Busca el nodo padre de un nodo dado en el árbol de decisiones."""
        if isinstance(current_node, dict):
            if current_node.get('yes') == target_node or current_node.get('no') == target_node:
                return current_node
            else:
                parent = self.find_parent_node(current_node.get('yes'), target_node)
                if parent is None:
                    parent = self.find_parent_node(current_node.get('no'), target_node)
                return parent
        return None

# Ejecución del juego
game = DecisionTreeGame()
game.start_game()

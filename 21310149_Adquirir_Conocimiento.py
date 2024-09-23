class ChatBot:
    def __init__(self):
        # Línea de conversación precargada
        self.conocimientos = {
            "Hola": "¡Hola! ¿Cómo estás?",
            "¿Cómo estás?": "Estoy aquí para ayudarte. ¿De qué te gustaría hablar?",
            "¿De qué te gustaría hablar?": "Puedes preguntarme cualquier cosa.",
        }

    def obtener_respuesta(self, pregunta):
        # Verificar si la pregunta está en la base de datos
        if pregunta in self.conocimientos:
            return self.conocimientos[pregunta]
        else:
            return "No tengo respuesta para eso. ¿Te gustaría agregar un nuevo conocimiento? (sí/no)"

    def agregar_conocimiento(self, pregunta, respuesta):
        # Agregar nuevo conocimiento a la base de datos
        self.conocimientos[pregunta] = respuesta
        return "Conocimiento agregado exitosamente."

def main():
    chatbot = ChatBot()
    print("Bienvenido al ChatBot. Escribe 'salir' para terminar.")

    while True:
        entrada = input("Tú: ")
        if entrada.lower() == 'salir':
            print("ChatBot: ¡Hasta luego!")
            break

        respuesta = chatbot.obtener_respuesta(entrada)
        print(f"ChatBot: {respuesta}")

        if "¿Te gustaría agregar un nuevo conocimiento?" in respuesta:
            agregar = input("Tú: ")
            if agregar.lower() == 'sí':
                nueva_pregunta = input("Introduce la nueva pregunta: ")
                nueva_respuesta = input("Introduce la respuesta para la nueva pregunta: ")
                print(chatbot.agregar_conocimiento(nueva_pregunta, nueva_respuesta))

if __name__ == "__main__":
    main()

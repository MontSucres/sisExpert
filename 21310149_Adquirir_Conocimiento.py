import sqlite3

class ChatBot:
    def __init__(self):
        # Conectar a la base de datos (se creará si no existe)
        self.conn = sqlite3.connect("conocimientos.db")
        self.cursor = self.conn.cursor()
        # Crear la tabla si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS conocimientos (
                pregunta TEXT PRIMARY KEY,
                respuesta TEXT
            )
        ''')
        self.conn.commit()
        
        # Precargar conocimientos si no existen
        self.precargar_conocimientos()

    def precargar_conocimientos(self):
        conocimientos_iniciales = [
            ("Hola", "¡Hola! ¿Cómo estás?"),
            ("¿como estás?", "Estoy aquí para ayudarte. ¿De qué te gustaría hablar?"),
            ("¿De qué te gustaría hablar?", "Puedes preguntarme cualquier cosa."),
            ("¿Qué color te gusta?", "Me gustan todos los colores, pero el azul es agradable."),
        ]
        
        for pregunta, respuesta in conocimientos_iniciales:
            try:
                self.cursor.execute("INSERT INTO conocimientos (pregunta, respuesta) VALUES (?, ?)", (pregunta, respuesta))
            except sqlite3.IntegrityError:
                # La pregunta ya existe, no es necesario insertarla
                pass
        self.conn.commit()

    def obtener_respuesta(self, pregunta):
        # Buscar la respuesta en la base de datos
        self.cursor.execute("SELECT respuesta FROM conocimientos WHERE pregunta = ?", (pregunta,))
        resultado = self.cursor.fetchone()
        
        if resultado:
            return resultado[0]
        else:
            return "No tengo respuesta para eso. ¿Te gustaría agregar un nuevo conocimiento? (si/no)"

    def agregar_conocimiento(self, pregunta, respuesta):
        # Agregar nuevo conocimiento a la base de datos
        try:
            self.cursor.execute("INSERT INTO conocimientos (pregunta, respuesta) VALUES (?, ?)", (pregunta, respuesta))
            self.conn.commit()
            return "Conocimiento agregado exitosamente."
        except sqlite3.IntegrityError:
            return "La pregunta ya existe en la base de datos."

    def __del__(self):
        # Cerrar la conexión a la base de datos cuando se destruya el objeto
        self.conn.close()

def main():
    chatbot = ChatBot()
    print("Bienvenido al ChatBot. Escribe 'bye bye' para terminar.")

    while True:
        entrada = input("Tú: ")
        if entrada.lower() == 'bye bye':
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

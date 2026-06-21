import random

# =====================================================================
# 1. MODELO (Gestión de Vidas y Palabras Random que se Utilizan en el Juego) 
# =====================================================================

class AhorcadoModel:
    def __init__(self):
        # 7 palabras para este avance del proyecto
        self.lista_palabras = ["SOFTWARE", "LOGICA", "PROGRAMACION", "UIDE", "CODIGO", "INGENIERIA", "VARIABLE, SISTEMAS"]
        self.palabra_secreta = random.choice(self.lista_palabras)
        self.vidas_restantes = 7
        self.letras_adivinadas = []
        self.letras_intentadas = []

    def verificar_letra(self, letra):
        if letra not in self.letras_intentadas:
            self.letras_intentadas.append(letra)
        
        if letra in self.palabra_secreta:
            if letra not in self.letras_adivinadas:
                self.letras_adivinadas.append(letra)
            return True
        else:
            self.vidas_restantes -= 1
            return False

    def ha_ganado(self):
        return all(letra in self.letras_adivinadas for letra in self.palabra_secreta)

    def ha_perdido(self):
        return self.vidas_restantes <= 0


# =====================================================================
# 2. VISTA (Muestra el Estado Actual del Juego, Solicita la Letra al Usuario y Contiene los Mensajes de Victoria o Derrota)
# =====================================================================

class AhorcadoView:
    def mostrar_estado_actual(self, palabra_secreta, letras_adivinadas, vidas, intentadas):
        print("\n" + "="*40)
        progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print(f"Palabra a adivinar: {' '.join(progreso)}")
        print(f"Vidas restantes: {vidas}")
        print(f"Letras intentadas: {', '.join(intentadas) if intentadas else 'Ninguna'}")
        print("="*40)

    def mostrar_mensaje_victoria(self, palabra):
        print(f"\n¡FELICITACIONES! Has ganado. La palabra era: {palabra}")

    def mostrar_mensaje_derrota(self, palabra):
        print(f"\n¡PERDISTE! Te has quedado sin vidas. La palabra era: {palabra}")

    def solicitar_letra(self):
        return input("Ingresa una letra: ").strip().upper()

    def mostrar_error_repetida(self):
        print("!Ya intentaste esa letra antes!. Elige otra.")

    def mostrar_error_invalido(self):
        print("!Entrada inválida!. Ingresa solo una letra del alfabeto.")


# =====================================================================
# 3. CONTROLADOR (Da la Bienvenida, Solicita la Letra, Verifica el Estado del Juego y Muestra los Mensajes de Victoria o Derrota)
# =====================================================================
class AhorcadoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def iniciar_juego(self):
        print("¡Bienvenido al Juego del Ahorcado!")
        
        while not self.model.ha_ganado() and not self.model.ha_perdido():
            self.view.mostrar_estado_actual(
                self.model.palabra_secreta, 
                self.model.letras_adivinadas, 
                self.model.vidas_restantes,
                self.model.letras_intentadas
            )
            
            letra = self.view.solicitar_letra()
            
            if len(letra) != 1 or not letra.isalpha():
                self.view.mostrar_error_invalido()
                continue
                
            if letra in self.model.letras_intentadas:
                self.view.mostrar_error_repetida()
                continue
            
            self.model.verificar_letra(letra)

        if self.model.ha_ganado():
            self.view.mostrar_mensaje_victoria(self.model.palabra_secreta)
        else:
            self.view.mostrar_mensaje_derrota(self.model.palabra_secreta)


if __name__ == "__main__":
    modelo_juego = AhorcadoModel()
    vista_juego = AhorcadoView()
    controlador_juego = AhorcadoController(modelo_juego, vista_juego)
    controlador_juego.iniciar_juego()

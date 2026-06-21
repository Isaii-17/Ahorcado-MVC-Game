# Documentación del Diseño y Arquitectura - Juego del Ahorcado

Este módulo contiene la planificación gráfica y estructural del proyecto previa a la codificación, asegurando.

## 1. Diagrama de Flujo 
* **Propósito:** Mostrar el ciclo de vida de una partida estándar del juego y los flujos de decisión del algoritmo.
* **Funcionamiento:**
  * El sistema inicializa el entorno seleccionando una palabra e iniciando con un total de 7 vidas.
  * Se procesa un ciclo iterativo (bucle) por cada letra ingresada por el usuario.
  * Cuenta con bifurcaciones lógicas que validan si la letra es repetida, correcta o incorrecta.
  * El juego finaliza bajo dos condiciones de quiebre estrictas: Victoria (**Palabra Completa**) o Derrota (**Vidas == 0**).

## 2. Diagrama de Arquitectura con el Diseño MVC
* **Propósito:** Separar las responsabilidades del software en tres capas independientes para garantizar un código limpio, mantenible y escalable.
* **Características del Modelo-Vista-Controlador:**
  * **Modelo:** Maneja la lógica y los datos puros. No sabe cómo se ve la interfaz; solo gestiona las vidas, palabras y validaciones.
  * **Vista:** Capa de interacción con el usuario. Recibe los datos del Modelo y los renderiza en la terminal.
  * **Controlador:** Intercepta las acciones del usuario, ejecuta las órdenes de control y comunica los cambios entre el Modelo y la Vista.

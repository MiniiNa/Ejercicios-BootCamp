Crear un juego donde el programa piensa un número aleatorio entre 1 y 100, y el usuario debe adivinarlo recibiendo pistas.

Pasos a seguir:
1. Generar un numero aleatorio o Random (0-100)
2. Pedir al usuario que ingrese un número
3. Comparar el numero generado por el ordenador con el número escrito por el usuario
4. Aportar pista: <()>
5. En caso de acierto, generar mensajes de congratulación
6. Contador intentos hasta el éxito
7. Volver empezar??


**Lista de tareas**

1. Generar un número en el rango numerico del 0 al 100 numero=(1,100)
2. Guardar el numero generado
3. Solicitar al usuario un número en el mismo rango en bucle:
    3.1- Validar que el usuario introduce valores numéricos en el rango establecido
    3.2- Comparar el numero generado por el ordenador
    3.3- Si el número no es el mismo, aportar pista
    3.4- Contabilizar intentos hasta acertar
4. Imprimir número de intentos    
5. Permitir múltiples partidas

**Extructuras**

1. Bucles
    1.1- Intentos del usuario -> while True 
    1.2- Multiples partidas -> while seguir=="s"

2. Condicionales
    2.1- Validar número: try / except
    2.2- Intento correcto: if elif else

**Que variables se necesitan**

1. numero_random -> entero int()
2. numero_usuario -> entero int()
3. contador -> entero int()
4. seguir_jugando -> string input("s/n")
5. best_score -> entero int()

**Pseudo Codigo**

1. Generar numero_random entre 1 y 100 y guardarlo
2. Crear un contador de intentosle damos un valor inicial = 0
3. Bienvenida al usuario
4. Crear un bucle, mientras que se encuentra el numero correcto
   4.1- Solicitar al usuario un numero entre 1 y 100 input()
   4.2- Condicionamos el resultado (if, else, elif):
     4.2.1. si el usuario no escribe un numero valido, se despliega un mensaje de error y se vuelve a pedir un numero
     4.2.2. SI intento < numero_random:
                     Decir "Más alto"
                  SI NO, SI intento > numero_random:
                     Decir "Más bajo"
                  SI NO:
                     Decir "¡OLE, has acertado!"
                     SALIR del bucle
 

 **Pseudo codigo 2**

 INICIO DEL PROGRAMA

Generar numero_secreto aleatorio entre 1 y 100
Inicializar intentos = 0
Bienvenida 🤩

MIENTRAS no haya adivinado:4.1. Pedir un número al usuario4.2. SI el usuario no escribe un número válido:
        Mostrar error y volver a pedir
     SINO:4.2.1. Incrementar intentos en 14.2.2. SI intento < numero_secreto:
                  Decir "Más alto"
               SI NO, SI intento > numero_secreto:
                  Decir "Más bajo"
               SI NO:
                  Decir "¡OLE, has acertado!"
                  SALIR del bucle

Mostrar cuántos intentos necesitamos

FIN DEL PROGRAMA


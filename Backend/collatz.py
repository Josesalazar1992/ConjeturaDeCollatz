
import time

# La Conjetura de Collatz es un problema matemático no resuelto que consiste en la siguiente secuencia:

# 1. Comienza con un número entero positivo n.
# 2. Si n es par, divídelo entre 2 → n = n / 2.
# 3. Si n es impar, multiplícalo por 3 y súmale 1 → n = 3 * n + 1.
# 4. Repite el proceso hasta que n sea 1.

print("Hola, bienvenido a la Conjetura De Collatz")


number = int(input("Ingresa un numero : "))

while number != 1:
    original_number = number
    print(f"resultado: {number}")
    time.sleep(1)
    if number % 2 == 0:
        print(f"{number} / 2")
        time.sleep(1)
        number = number // 2    
    else:
        print(f"{number} * 3 + 1")
        time.sleep(1)
        number = number * 3 + 1
        

print (f"Resultado : {number}")


import time

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

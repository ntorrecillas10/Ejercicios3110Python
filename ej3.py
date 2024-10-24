operacion = input("Introduce una de estas opreciones: +, *, /, -")
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if operacion == '+':
    resultado = num1 + num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '/':
    if num2 != 0:
        resultado = num1/num2
    else:
        print("error")
else:
    print("introduce una operacion valida")
print(f"el resultado es : {resultado}")
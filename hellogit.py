print("Hello Git")
##Calculadora##

A=int(input("Cual es su primer numero?"))
B=int(input("Cual es su segundo numero?"))


suma=A+B
print(suma)

M= input("Quieres que se multipliquen los mismos datos? ")

if M.lower() == "si":
    print("La multiplicacion es: ",A*B)
else:
    print("No se realizara la multiplicacion")


D=input("Usted desea que se dividan los dos digitos ? ")
if D.lower() == "si":
    print("El resultado de la division es: ",A/B)
else:
    print("No existe division")


print("Hola como estas?")
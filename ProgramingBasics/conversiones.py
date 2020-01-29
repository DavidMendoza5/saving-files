
base = int(input("Ingrese la base del sistema: "))
numero = int(input("Ingresa el número que deseas convertir: "))

# Falta validar los números negativos
def conversion_binario(base, numero):
    residuos = []
    if(base == 2):
        cociente = numero // base 
        print(cociente)
        residuos.append(numero % base) 
        while(cociente != 0):
            numero = cociente 
            cociente = numero // base 
            print(cociente)
            residuos.append(numero % base)
        residuos.reverse() 
        print(residuos)

conversion_binario(base, numero)

#Buena práctica de programación: Siempre dejar dos líneas antes de codificar
def my_function(str1, str2): #Buena práctica: De esta manera se deben delcarar las funciones en python
    print(str1)
    print(str2)

my_function("This is argument 1", "This is the second argument")
my_function("Hello ", "world")

def print_something(name, age):
    print("My name is " + name + "and my age is " + str(age))
    print("Second example, my name is", name, "and my age is", age) #Se pueden usar las comas para evitar convertir los valores de los parámetros

print_something("David", 20)

def print_something2(name2 = "Someone", age2 = "Unknown"): #Parámetros puestos por default
    print("Hello", name2, "your age is", age2)

print_something2("David")
print_something2(age2 = 25, name2 = "David") #De esta forma se pueden pasar parámetros en diferente orden

def print_people(*people): #El asterisco indica que se la va a pasar un arreglo y va a tomar todos los datos que contenga
    for person in people:
        print("This person is", person) #Imprime la cadena con un nombre diferente (el que se le haya pasado al llamar la función)

print_people("David", "Daniel", "Layda", "Miguel", "Chente")

def do_math(num1, num2):
    return num1 + num2

math1 = do_math(5, 7)
math2 = do_math(11, 4)

print("First sum is", math1, "and the second sum is" , math2) #Devuelve la suma de los valores que se le hayan dado

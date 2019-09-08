import re

print("Calculator")
print("Type 'quit' to exit\n")

previus = 0 #Esta variable va a matener el resultado de las operaciones para poder seguir usando el valor con otras operaciones
run = True

def perform_math():
    global run      #Me permite tener acceso a las variables locales y poder cambiar/modificar su valor
    global previus
    equation = ""
    if previus == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previus))


    if (equation == 'quit'):
        run = False
    else:
        equation = re.sub('[a-zA-Z,;:()" "]', '', equation)
        if (previus == 0):
            previus = eval(equation)
        else:
            previus = eval(str(previus) + equation)

while run:
    perform_math()
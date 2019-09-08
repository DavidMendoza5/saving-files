import re

something = "I AM NOT YELLING, shes is the one that is yelling at me and I don't know why..."
variable = re.sub('[.,\'A-Z + " "]', '', something) #Con los primeros parámetros borramos puntos, comas, mayúsculas y espacios
print(something)
print(variable)

something2 = something + "123456789"
variable2 = re.sub('[^0-9]', '', something2) #Sólo deja los números de la cadena
print(variable2)

print("Hello world") #Hello world
print("Don't do that") #Don't do that
print('She said "I want this"') #She said "I want this"
print("She said 'I want this'") #She said 'I want this'
print('She said "Don\'t do that"') #She said "Don't do that"
print("Hello, " + "David") #Hello, David
print("This costs " + str(6) + " bucks") #This costs 6 bucks
print("This costs " + str(6+5) + " dollars") #This costs 11 dollars
print("Hello:David".split(":")) #['Hello', 'David']     Divide la palabra dependiendo del caracter que se le indicó
print("My name is " + "Hello:David".split(":")[1]) #My name is David       El número en los corchetes indica la posición del caracter que va a concatenar
print(5 is 5) #True
print(5 is 4) #False
print(5 is not 5) #False
print("This" is "This") #True
print("This" is "Hello") #False
print("This" is "That") #False
print(["Movies", "Games", "Series"][1]) #Games
number = 2
print("I want " + ["Games", str(number)][1] + " hamburguers") #I want 2 hamburguers
#               Dictionaries
print({"Name":"David", "Age":"20", "Hobby":"Biking"}["Name"]) #David
greeting = "Hello world"
print(greeting) #Hello world
greeting2 = greeting.split(" ")[0]
print(greeting2) #Hello
print(len("Hello")) #5
print(len(["Hello", 5, 7, 4])) #4
print(sorted([29, 3, 430, 5, 900, 901, 56])) #La función sorted() muestra los números del areglo ordenados
print(sorted(["F", "Z", "A", "a", "c", "B", "r", "3"])) #3, A, B, F, Z, a ,c, r





check = True

if check == True:
    print("It is true") #En este ejemplo esta condicional es la que se va a ejecutar

elif check == "Hamburguer":
    print("I like hamburguers")

elif check == "Something":
    print("It is something")

else:
    print("It is false")

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

run = True
current = 1

while run:
    if (current == 10):
        run = False
    else:
        print(current)
        current += 1
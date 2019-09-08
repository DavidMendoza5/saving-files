from Classes.Game import Person, Bcolors

magic = [{"Name": "Fire", "Cost": 12, "Dmg": 175},
        {"Name": "Thunder", "Cost": 15, "Dmg": 200},
        {"Name": "Blizzard", "Cost": 10, "Dmg": 140},]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(Bcolors.fail + Bcolors.bold + "An enemy attacks!" + Bcolors.endc)

while running:
    print("==================================")
    
    player.choose_action()
    choice = input("Choose an action: ")
    index = int(choice) - 1

    if(index == 0):
        Dmg = player.generate_damage()
        enemy.take_damage(Dmg)
        print("You attacked for", Dmg, "points of damage. Enemy hp:", enemy.get_hp())

    elif(index == 1):
        player.choose_magic()        
        magic_choice = int(input("Choose a spell: ")) - 1        
        magic_dmg = player.generate_spell_damage(magic_choice)        
        spell = player.get_spell_name(magic_choice)        
        cost = player.get_spell_cost(magic_choice)        
        current_mp = player.get_mp()

        if(cost > current_mp):
            print(Bcolors.fail + "Not enough magic points" + Bcolors.endc)
            continue

        player.reduce_mp(cost)        
        enemy.take_damage(magic_dmg)
        print(Bcolors.okblue + "\n" + spell + "deals", str(magic_dmg), "points of damage" + Bcolors.endc)
        print("Enemy hp:", enemy.get_hp())
        print(Bcolors.okblue + "Your MP:", str(player.get_mp()) + Bcolors.endc)

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Enemy attacks for", enemy_damage, "point of damage. Player HP:", player.get_hp())

    if(enemy.get_hp() == 0):
        print(Bcolors.okgreen + "You have won!" + Bcolors.endc)
        running = False

    elif(player.get_hp() == 0):
        print(Bcolors.fail + "You have died!" + Bcolors.endc)
        running = False

   

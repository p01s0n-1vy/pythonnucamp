character = ""
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
dragon = "Dragon"

my_hp = 0
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 175
dragon_hp = 300

my_damage = 0
wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 175
dragon_damage = 50

while True:
    print("1)   Wizard")
    print("2)   Elf")
    print("3)   Human")
    print("4)   Orc")
    character = input("Choose your character:")

    if (character == "1" or character == "Wizard" or character == "wizard" or character == "WIZARD"):
        character = wizard
        my_damage = wizard_damage
        my_hp = wizard_hp
        print("You've chosen the Wizard " "\n" "Health:" + str(wizard_hp) + "\n" "Damage:" + str(wizard_damage))
        break

    if (character == "2" or character == "Elf" or character == "elf" or character == "ELF"):
        character = elf
        my_damage = elf_damage
        my_hp = elf_hp
        print("You've chosen the Elf " "\n" "Health:" + str(elf_hp) + "\n" "Damage:" + str(elf_damage))
        break

    if (character == "3" or character == "Human" or character == "human" or character == "HUMAN"):
        character = human
        my_damage = human_damage
        my_hp = human_hp
        print("You've chosen the Human " "\n" "Health:" + str(human_hp) + "\n" "Damage:" + str(human_damage))
        break

    if (character == "4" or character == "Orc" or character == "orc" or character == "ORC"):
        character = orc
        my_damage = orc_damage
        my_hp = orc_hp
        print("You've chosen the Orc " "\n" "Health:" + str(orc_hp) + "\n" "Damage:" + str(orc_damage))
        break

    print ("unknown character")

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp, "\n")
    if dragon_hp <= 0:
        print ("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at", character)
    print("The", character + "'s hitpoints are now: ", my_hp)
    if my_hp <= 0:
        print ("The", character, "has lost the battle!")
        break

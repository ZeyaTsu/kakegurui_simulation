import magic_dice

print("KAKEGURUI SIMULATION")
print("1 - Magic Dice Game")

user_choice = int(input("> "))
match user_choice:
    case 1:
        n = int(input("Repeat for n = "))
        magic_dice.game(n)
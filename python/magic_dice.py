import random
def game(n:int):

    lost = 0
    win = 0

    black_dice = [3, 3, 4, 4, 8, 8]
    white_dice = [1, 1, 5, 5, 9, 9]
    red_dice = [2, 2, 6, 6, 7, 7]

    print(f"DICE\nBLACK DICE {black_dice}\nWHITE DICE {white_dice}\nRED DICE {red_dice}")
    dice_chosen = str(input("Choose a color (red,white,black) > "))
    for i in range(n):
        if dice_chosen == "red":
            host_face = random.choice(black_dice)
            guest_face = random.choice(red_dice)
        if dice_chosen == "white":
            host_face = random.choice(red_dice)
            guest_face = random.choice(white_dice)
        if dice_chosen == "black":
            host_face = random.choice(white_dice)
            guest_face = random.choice(black_dice)
        
        if host_face > guest_face:
            print(f"You lost. HOST {host_face} > {guest_face} GUEST")
            lost += 1
        else:
            print(f"You won. HOST {host_face} < {guest_face} GUEST")
            win += 1

    pourcentage_win = win / (win + lost) 
    pourcentage_lost = lost / (win + lost) 

    print(f"WINRATE: {pourcentage_win*100}% / LOSERATE: {pourcentage_lost*100}")
    print("The chance of winning if you're the host (second player) is 5/9. The chance of winning if you're the guest (first player) is 4/9.")


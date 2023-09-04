import random

def spin():
    result = random.randint(1, 100)

    if result <= 10:
        print("Congratulations! You won the rare item!")
    elif result <= 30:
        print("Congratulations! You won the uncommon item!")
    else:
        print("You won the common item. Better luck next time!")

spin()

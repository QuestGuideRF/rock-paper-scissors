import random

CHOICES = {
    "rock": "камень",
    "paper": "бумага",
    "scissors": "ножницы",
}
WINNING_MOVES = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def main():
    try:
        player = input("Введите вариант выбора (камень, бумага, ножницы): ").strip().casefold()
    except EOFError:
        return

    player = {label: move for move, label in CHOICES.items()}.get(player, player)
    if player not in CHOICES:
        print("Выберите камень, бумагу или ножницы.")
        return

    computer_choice = random.choice(tuple(CHOICES))
    print(f"Компьютер выбрал: {CHOICES[computer_choice]}.")
    if player == computer_choice:
        print("Ничья!")
    elif WINNING_MOVES[player] == computer_choice:
        print("Вы победили!")
    else:
        print("Компьютер победил!")


if __name__ == "__main__":
    main()

import random

cards = []


# creating cards and filling them in
def create_cards():
    global cards
    i = 0
    # quantity of cards is no more than 3
    while i < 3:
        rus_word = input("Введите слово по-русски: ")
        eng_word = input("Введите перевод на английский язык: ")
        card = [rus_word, eng_word]
        cards.append(card)
        i += 1
    return cards


# printing all words and their translations given in the cards
def print_cards_set():
    i = 0
    while i < 3:
        card = cards[i]
        print("Вы создали следующие карточки:\n")
        print("Карточка", i + 1, "\n по-русски:\t ", card[0], "\n english:\t ", card[1])
        i = i + 1


# choosing a random card from the set of all cards
def random_card_choosing(cards):
    random_card = random.choice(cards)
    print(random_card[0])
    while True:
        answer = input("Перевод слова: ")
        # if the answer is wrong, a user can try again or interrupt testing mode
        if answer != random_card[1]:
            print("Неверный ответ")
            answer2 = input('Для повторной попытки нажмите "1", для выхода - "2": ')
            if answer2 == "1":
                continue
            if answer2 == "2":
                break
        else:
            print("Правильный ответ")
            break


# choosing a mode necessary for working with cards: 1. filling in, 2. training or 3. exit
def choose_mode():
    global cards
    while True:
        print("Добро пожаловть!")
        print("Выберите режим:")
        print("1. Заполнение")
        print("2. Обучение")
        print("3. Выход")
        mode_choice = input("Номер режима: ")
        # when 1 is chosen, the cards are created and printed
        if mode_choice == "1":
            print("Вы вошли в режим заполнения")
            create_cards()  #
            print_cards_set()
        # when 2 is put in, a random card is chosen
        elif mode_choice == "2":
            print("Вы вошли в режим обучения")
            random_card_choosing(cards)
        # if the user chooses 3, the program will exit
        elif mode_choice == "3":
            print("До свидания")
            break
        # if a user enters a wrong number, the program will inform about an invalid input
        else:
            print("Введено неверное значение")


# the program starts here
choose_mode()

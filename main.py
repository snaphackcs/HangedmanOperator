import random
import time

total_time = 140


def print_word(orstr, upstr, char, stime):
    if time.time() - stime > total_time:
        return False
    stat = True
    for i in range(0, len(upstr)):
        if not upstr[i].isalpha():
            print(orstr[i], end='')
        if char[ord(upstr[i]) - ord('A')] == 0:
            print('_', end='')
            stat = False
        else:
            print(orstr[i], end='')
    return stat


def play_hanged_man(play_round):
    guessed_char = [0] * 26
    guessed_wrong = []
    win = False

    f = open('TOEFLvocab.txt', encoding='utf-8')
    data = f.readlines()
    line = random.randint(0, len(data))
    original_str = data[line].split(" ")[0]
    # print(original_str)
    # original_str = "funny"
    # original_str = input("Please enter the word: ")
    up_str = original_str.upper()
    guess_time = int(len(original_str) * (1.1 - 0.2 * play_round)) + 1
    start_time = time.time()

    while guess_time > 0 and not win and time.time() - start_time < total_time:
        print("Time left: " + str(total_time - time.time() + start_time) + " second(s)")
        print("Current state: ", end='')
        win = print_word(original_str, up_str, guessed_char, start_time)
        print()
        if win:
            break

        print("Letter guessed wrong: ", end='')
        for i in guessed_wrong:
            print(i, end=' ')
        print()
        print("----------------------------")
        print("There are " + str(guess_time) + " chance left. ")
        curchar = input("Please enter your guess: ")
        curchar = curchar.upper()
        if curchar in up_str:
            guessed_char[ord(curchar) - ord('A')] = 1
        else:
            guessed_wrong.append(curchar)
            guess_time -= 1

    print("============================")
    print("Final state: ", end='')
    print_word(original_str, up_str, guessed_char, start_time)
    print()
    print("Letter guessed wrong: ", end='')
    for i in guessed_wrong:
        print(i, end=' ')
    print()

    if win:
        print("You win! The word is: " + data[line] + "Well done! ")
        return True
    else:
        print("Time used: " + str(time.time() - start_time) + "second(s)")
        print("You lose... The word is: " + data[line] + "Better luck next time! ")
        return False


people = int(input("Players: "))
times = 0
while people > 1:
    print("Current round: " + str(times + 1))
    print("Players left: " + str(people))
    for i in range(people):
        if not play_hanged_man(times):
            people -= 1
        print()
        print("============================")
        print()
    times += 1

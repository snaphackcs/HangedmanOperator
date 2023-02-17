def print_word(orstr, upstr):
    stat = True
    for i in range(0, len(upstr)):
        if not upstr[i].isalpha():
            print(orstr[i], end='')
        if guessed_char[ord(upstr[i]) - ord('A')] == 0:
            print('_', end='')
            stat = False
        else:
            print(orstr[i], end='')
    return stat


guessed_char = [0] * 26
guessed_wrong = []
is_success = False

original_str = "funny"
# original_str = input("Please enter the word: ")
up_str = original_str.upper()
guess_time = len(original_str) + 1
win = False

while guess_time > 0 and not win:
    print("Current state: ", end='')
    win = print_word(original_str, up_str)
    print()
    if win:
        break

    print("Letter guessed: ", end='')
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

print("===========================")
print("Final state: ", end='')
print_word(original_str, up_str)
print()
print("Letter guessed wrong: ", end='')
for i in guessed_wrong:
    print(i, end=' ')
print()

if win:
    print("You win!")
else:
    print("You lose... The word is " + original_str + ". Better luck next time! ")

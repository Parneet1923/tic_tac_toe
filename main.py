from logo import logo
import random

print(logo)
print("Instructions:\n 1: Top Left of the board \n 2: Top right of the board \n 3: Top Middle of the board\n"
      " 4: Left of the board\n 5: Middle of the board\n 6: Right of the board\n 7: Bottom Left of the board\n "
      "8: Bottom Middle of the board\n 9: Bottom Right of the board")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

user_symbol = input("Do you want 'X' or '0' ? Please type X for 'X' or 0 for '0': ")
computer_symbol = ''
if user_symbol == "X":
    computer_symbol = "0"
elif user_symbol == "0":
    computer_symbol = "X"
else:
    print("Error! Type valid input")



def show():
    game_board = f' {l[0]} | {l[1]} | {l[2]} \n' \
             f'-----------\n' \
             f' {l[3]} | {l[4]} | {l[5]} \n' \
             f'-----------\n' \
             f' {l[6]} | {l[7]} | {l[8]} \n'
    print(game_board)


n1 = []
user_n = []
n2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if user_symbol == 'X' or user_symbol == '0':
    for n in range(1, 10):
        if n % 2 != 0:
            user_input = int(input("Play your turn: "))
            if user_input in n1:
                print("You lose! by overwriting the 'X' or '0'.")
                break
            else:
                l[user_input-1] = user_symbol
                user_n.append(user_input)
                n1.append(user_input)
                n2.remove(user_input)
                show()
        if l[0] == l[1] == l[2] or l[3] == l[4] == l[5] or l[6] == l[7] == l[8]:
            if 1 and 2 and 3 in user_n or 4 and 5 and 6 in user_n or 7 and 8 and 9 in user_n:
                print("Congratulations 🥳🥳. You Win 😁😁.")
                break
            else:
                print("You lose 😭😭.")
                break
        if l[0] == l[3] == l[6] or l[1] == l[4] == l[7] or l[2] == l[5] == l[8]:
            if 1 and 4 and 7 in user_n or 2 and 5 and 8 in user_n or 3 and 6 and 9 in user_n:
                print("Congratulations 🥳🥳. You Win 😁😁.")
                break
            else:
                print("You lose 😭😭.")
                break
        if l[0] == l[4] == l[8] or l[2] == l[4] == l[6]:
            if 1 and 5 and 9 in user_n or 3 and 5 and 7 in user_n:
                print("Congratulations 🥳🥳. You Win 😁😁.")
                break
            else:
                print("You lose 😭😭.")
                break
        elif n % 2 == 0:
            computer_choice = random.choice(n2)
            n1.append(computer_choice)
            l[computer_choice-1] = computer_symbol
            print("Computer's Turn: ")
            show()
        elif n == 9:
            print("It's a draw.")





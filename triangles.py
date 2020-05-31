'''  1
    ##
   333
  ####
 55555   '''

userInput = float(input("Enter a number between 1 and 10: "))

assert userInput.is_integer() and 1 <= userInput <= 10, "Invalid number."

intNumber = int(userInput)

spaces = intNumber

for row in range(intNumber):
    spaces -= 1
    for column in range(spaces): print(" ", end="")
    for column in range(intNumber - spaces):
        if (row + 1) % 2 == 1:
            print(row + 1, end="")
        else:
            print("#", end="")
    print("")

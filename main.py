#Exercise script for english training.

#Random guessing number.
import random
print("="*50)
print("Welcome to number guesser!")
print("="*50)
print("In this game, you need to guess a number between a range you select.")
print("="*50)
print("Let's start!")
print("="*50)

exit_menu = 0
while exit_menu == 0:
    option = int(input("Please select an option:\n1.New game\n2.Exit\n--- "))
    if option == 1:

        verify_num1 = 0
        while verify_num1 == 0:
            try:
                num1 =int(input("\nPlease enter the start of the range: "))
            except ValueError:
                print("\nPlease enter a number...")
            verify_num1 += 1

        verify_num2 = 0
        while verify_num2 == 0:
            try:
                num2 = int(input("\nPlease enter the end of the range: "))+1
            except ValueError:
                print("\nPlease enter a number...")
            verify_num2 += 1

        difference = num2 - num1
        print("\nRandomizing...")
        randnum = random.randint(num1, num2)
        tries = 1
        exit_loop = 0
        number_chosen = []
        while exit_loop == 0:
            answer = input("\nEnter your guess (press X to exit): ")
            
            if answer == "x":
                exit_loop += 1
            else:
                answer = int(answer)
                number_chosen.append(answer)
                if answer == randnum:
                    print("Congratulations, you are spot on!!!!")
                    print(f"Guessed the number in {tries} attempt(s)")
                    print(f"Chances were 1/{difference}!")
                    exit_loop += 1
                elif not answer == randnum:
                    print("Wrong, please try again!")
                    print(f"You have guessed these numbers: {number_chosen}")
                    tries += 1
    elif option == 2:
        print("Goodbye!")
        exit_menu += 1
    else:
        print("Please enter a valid option...")

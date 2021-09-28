print('Welcome to the Flarsheim Guesser!')

choice = 'Y'
# continuation of the loop
while choice != 'N' and choice == 'Y':
    num_chosen = int(input('Please think of a number between and including 1 and 100\n'))
    if num_chosen < 1:
        print('That number is not in the range')
        num_chosen = int(input('Please think of a number between and including 1 and 100\n'))
    elif num_chosen > 100:
        print('That number is not in the range')
        num_chosen = int(input('Please think of a number between and including 1 and 100\n'))
    else:
        div_3 = int(input('What is the remainder when your number is divided by 3?\n'))

    # For num_chosen divided by 3
    while num_chosen >= 1 and num_chosen <= 100:

        if div_3 < 0:
            print('The value you entered must be 0 or greater')
            div_3 = int(input('What is the remainder when your number is divided by 3?\n'))
        elif div_3 >= 3:
            print('The value entered must be less than 3')
            div_3 = int(input('What is the remainder when your number is divided by 3?\n'))
        else:
            div_5 = int(input('What is the remainder when your number is divided by 5?\n'))

        # for remainder divided by 5
        while num_chosen >= 1 and num_chosen <= 100:
            if div_5 < 0:
                print('The value you entered must be 0 or greater')
                div_5 = int(input('What is the remainder when your number is divided by 5?\n'))
            elif div_5 >= 5:
                print('The value entered must be less than 5')
                div_5 = int(input('What is the remainder when your number is divided by 5?\n'))
            else:
                div_7 = int(input('What is the remainder when your number is divided by 7?\n'))

            # num_chosen divided by 7:
            while num_chosen >= 1 and num_chosen <= 100:
                if div_7 < 0:
                    print('The value you entered must be 0 or greater')
                    div_7 = int(input('What is the remainder when your number is divided by 7?\n'))
                elif div_7 >= 7:
                    print('The value entered must be less than 7')
                    div_7 = int(input('What is the remainder when your number is divided by 7?\n'))
                else:
                    if div_3 >= 0 and div_3 < 3 and div_5 >= 0 and div_5 < 5 and div_7 >= 0 and div_7 < 7:  # Calculates the guess number by checking remainders from 1 to 100
                        for i in range(1, 101):
                            if i % 3 == div_3 and i % 5 == div_5 and i % 7 == div_7:
                                print('Your number was {}'.format(i))
                                print('How amazing is that?')
                    break
                break
            break
        break
    while num_chosen >= 1 and num_chosen <= 100:
        choice = input('do you want to play again(Y or N)\n')
        if choice != 'Y' and choice != 'N':
            print('That is not an option')
            choice = input('do you want to play again(Y or N)\n')
        elif choice == 'Y':
            break
        elif choice == 'N':
            break
        break
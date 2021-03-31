import random


def get_input_yn(message):
    """
    Gets a yes or no input from the user

    :param message: Message to be displayed before input
    :return: True or False from yes or no answer respectively
    """
    while True:
        ans = input(message).lower()

        if ans == 'yes':
            return True
        elif ans == 'no':
            return False
        else:
            print('\nInvalid input! Please enter yes or no.')


# Main loop
while True:
    # Resets the choices
    choices = ''

    # Lowercase choice
    if get_input_yn('\nInclude lowercase characters? (e.g. abcde) \n(yes/no): '):
        choices = choices + 'abcdefghijklmnopqrstuvwxyz'

    # Uppercase choice
    if get_input_yn('\nInclude uppercase characters? (e.g. ABCDE) \n(yes/no): '):
        choices = choices + 'abcdefghijklmnopqrstuvwxyz'.upper()

    # Numbers choice
    if get_input_yn('\nInclude numbers? (e.g. 12345) \n(yes/no): '):
        choices = choices + '1122334455667889900'

    # Symbols choice
    if get_input_yn('\nInclude symbols? (e.g. #$%&) \n(yes/no): '):
        choices = choices + '!@#$%&?'

    # Ambiguous characters
    if get_input_yn('\nInclude ambiguous characters? (e.g. (){}[]/\,;:<>) \n(yes/no): '):
        choices = choices + "(){}[]/\,;:<>\'\""

    # Input number of characters
    while True:
        try:
            chars = int(input("\nHow many characters in the password? \n(Min:5, Max:200): "))
            if chars < 5 or chars > 200:
                raise ValueError
            break
        except ValueError:
            print('\nPlease enter an integer between 5 and 200.')

    # Generates a password based on previous choices
    password = ''
    if choices != '':
        for i in range(chars):
            password = password + random.choice(choices)

        # Print the password
        print(f'\nYour password is: {password}')
    else:
        print('\nYou need to select at least one option to generate a password.')

    # User chooses to generate another password or not
    if not get_input_yn('\nWould you like to generate another password? \n(yes/no): '):
        break
    print('Values are reset. Please enter desired information.')

print('Thanks for using the password generator!')

original_number = '548'  # original number as string
while True:
    output = []
    guess_number = input('Enter a Number: ')

    # Check if the guessed number has the correct length
    if len(guess_number) != len(original_number):
        print(f'Enter {len(original_number)} digit number')
        continue  # Skip the rest of the loop and ask for input again

    # Check for duplicate digits in the guessed number
    if len(guess_number) != len(set(guess_number)):
        print('Duplicate Number')
        continue

    # Check if the guess is correct
    if int(guess_number) == int(original_number):
        print('Fermi' * len(original_number))
        print('\nYou Won!!')
        break

    # Compare each digit for "Fermi" and "Pico"
    for i in range(len(original_number)):
        for j in range(len(guess_number)):
            if original_number[i] == guess_number[j]:
                if i == j:
                    output.append('Fermi')
                    break  # Match in both value and position
                else:
                    output.append('Pico')
                    break  # Value matches but position does not

    # If there were no matches, output "Bagels"
    if len(output) == 0:
        print('Bagels')
    else:
        output_string = ' '.join(output)
        print(output_string)
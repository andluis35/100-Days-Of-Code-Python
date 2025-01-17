PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_filename = "letter_for_" + stripped_name + ".txt"
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        with open("./Output/ReadyToSend/" + new_filename, "w") as custom_letter:
            custom_letter.write(new_letter)

PLACEHOLDER = "[name]"
invited_names = []


def read_starting_letter():
    with open("Input/starting_letter.txt", mode="r") as letter_file:
        return letter_file.read()


def read_all_name(name_list):
    with open("Input/invited_names.txt", mode="r") as names_file:
        contents = names_file.readlines()

        for content in contents:
            name_list.append(content.strip("\n"))

    return name_list


def make_letter():
    name_list = read_all_name(invited_names)

    for name in name_list:
        letter = read_starting_letter()
        with open(f"Output/letter_for_{name.lower()}.txt", mode="w") as create_file:
            letter = letter.replace(PLACEHOLDER, name)
            create_file.write(f"{letter}")


make_letter()

# Keeps looping until magic words are spoken
# Gets input from user


def speak_to_auntie():
    user_name = input("What's your name?\n")
    while True:
        user_input = input("Speak to aunty: \n")

        if user_input == "I love you aunty, I have to go now":
            print("ok. Goodbye\n")
            print(f"{user_name}, where are you?")
            input("Speak to auntie: \n")
            input("Speak to auntie: \n")
            print("ok. Goodbye\n")
            return False

        if user_input.islower():
            print("WHAT? SPEAK UP! \n")

        elif user_input.isupper():
            print("YOU ARE VERY RUDE! \n")

        else:
            print("SHOW SOME RESPECT! \n")


speak_to_auntie()

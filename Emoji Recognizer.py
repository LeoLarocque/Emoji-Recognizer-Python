#Telling the user the purpose of the program.
print('Hello this is Friday. This program recognizes a variety of text emojis. If you would like to exit the program type "EXIT".')
newEmoji = ""
#Making a while statement that will keep going through the indented code until user exits program.
while 0 == 0:
    #Assigning what the user inputs to a variable.
    emoji = input("Type in a face. Example: :)\n")
    #If emoji is recognized in the program then print a string recognizing the emoji.
    if emoji == ":)" or emoji == "=)":
        print("Smiley face. " + emoji)
    elif emoji == ":(":
        print("Sad face. " + emoji)
    elif emoji == ";)":
        print("Winky face. " + emoji)
    elif emoji == ":|":
        print("Nuetral face. " + emoji)
    elif emoji == "-_-":
        print("Straight face. " + emoji)
    elif emoji == ":S" or emoji == ":s":
        print("Hesitant face. " + emoji)
    elif emoji == ":D":
        print("Laughing face. " + emoji)
    elif emoji == "XD" or emoji == "xD":
        print("LAUGHING face. " + emoji)
    elif emoji == ":p" or emoji == ":P":
        print("Tongue sticking out face. " + emoji)
    elif emoji == ":O" or emoji == ":o" or emoji == ":0":
        print("Surprised face. " + emoji)
    elif emoji == ":V" or emoji == ":v":
        print("Talking face. " + emoji)
    elif emoji == ">_<":
        print("Angry face. " + emoji)
    elif emoji == "8)" or emoji =="8|":
        print("Googly eyes face. " + emoji)
    elif emoji == "*_*" or emoji == "+_+":
        print("Dead face. " + emoji)
    elif emoji == ":*":
        print("Kissing face. " + emoji)
    elif emoji == "@_@":
        print("Googly eyes face. " + emoji)
    elif emoji == "B)" or emoji == "BD" or emoji == "B|":
        print("Cool sun-glasses face. " + emoji)
    elif emoji == "exit" or emoji == "EXIT" or emoji == "Exit":
        #Pausing the loop if the user wants to make a new emoji.
        break
    elif emoji == "n":
        #Asking user to input new emoji and other information.
        q1 = input("Would you like to make a new emoji? ")
        if q1 == "yes":
            username = input("Enter your name: ")
            emojiName = input("Enter your emoji name: ")
            newEmoji = input("Enter the new emoji: ")
        if q1 != "yes":
            print("Ok bye!")
    elif emoji == newEmoji:
        print(emojiName + " " + newEmoji + " This program originally did not know this emoji but " + username + " added it to the database! ")
    #If the emoji does not = any of the emoji's in the program then ask if you would like to add a new emoji.
    else:
        print('This is not a known emoji if you would like to add it to the database type in "n"')

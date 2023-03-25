user_list = {}  # Imports an empty dictionary.
messages = {}
print("Welcome, admin. Please select a password:")
admin_password = input()
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

while 1 == 1:   # Creates a recursive loop. Probably a better way to do this.

    print(  #Greeting message.
        "\n"
        "Press 1 to create a new account."
        "\nPress 2 for a current list of users. (Only usable by admin)"
        "\nPress 3 to send and receive messages."
        "\nPress 4 for help."
        "\nPlease enter your choice:\n"
        )

    user_input = input()    # Dictates which menu option to execute.

    if user_input == '1':
        print("\nPlease enter your preferred name:")
        attempted_name = input().lower()    # Disregards case.
        if attempted_name in user_list:     # Checks if name exists
            print("That name is already taken. Please choose again.")
        else:   # If name is unique, adds it to database.
            user_list.update({attempted_name.lower(): 'password'}) # Default password is "password" temporarily.
            print("Welcome to the site, "
                  + attempted_name +
                  "! Please choose a password:"
                  )
            user_list[attempted_name] = input()     # User defines new password.
            messages[attempted_name] = "DEFAULT MESSAGE"

    elif user_input == '2':     # Displays all current users and their passwords.
        print("Please enter admin password:")
        if input() == admin_password:
            print('\n' + str(user_list))
        else:
            print('\nPassword incorrect. Please try again.')

    elif user_input == '3':     # messaging other users, checking messages
        login_name = input("Please enter your user name: ").lower()     # User login
        if login_name in user_list:
            login_password = input("Please enter password for " + login_name + ": ")
            if login_password == user_list[login_name]:
                print("\nCorrect password entered.\nPress 1 to write a message.\nPress 2 to read your message.\n")
                user_option = input()
                if user_option == '1':
                    messaged_user = input("Please enter the name of the person you'd like to message:").lower()
                    if messages[messaged_user] != "DEFAULT MESSAGE":    # If user's message is "Default message", inbox
                        print("User's inbox is full.")                  #   is marked as full
                    else:
                        message = input("Please type your message:")
                        messages[messaged_user] = message
                elif user_option == '2':
                    print('\n' + messages[login_name])
                    mark_read = input("Mark message as read? y/n:")
                    if mark_read == "y":
                        print ("\nMessage marked as 'read'.")
                        messages[login_name] = "DEFAULT MESSAGE"    # If user marks message as read, it returns to
                    elif mark_read == "n":                          #   default, which opens up the inbox for more
                        print ("\nMessage not marked as 'read'.")   #   messages.
                    else:
                        print("\nInvalid option.")
                else:
                    print("\n That is not a valid option.")
            else:
                print("\nPassword not valid.")
        else:
            print("\nInvalid username.")


    else:   # Help message.
        print(
            "This is a simple messaging database. "
            "When creating a username,\nit must be unique, "
            "but the system will automatically\nformat your unique "
            "username to be in all lowercase.\n"
            "Passwords, however, are case-sensitive.")
            
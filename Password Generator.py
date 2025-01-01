#Password Generator
import random

#This below will have list of all lower letters, upper letters, numbers, and special characters
list_of_lower_letter = [ "a", "b", "c", #List containing lower letters
                         "d","e","f",
                         "g","h","i",
                         "j","k","l",
                         "m","n","o",
                         "p","q","r",
                         "s","t","u",
                         "v","w","x",
                            "y","z"]

list_of_upper_letter = [ "A", "B", "C", #List containing all upper letters
                         "D","E","F",
                         "G","H","I",
                         "J","K","L",
                         "M","N","O",
                         "P","Q","R",
                         "S","T","U",
                         "V","W","X",
                            "Y","Z"]

list_of_numbers = [ "1", "2","3", #List of all numbers
                    "4","5","6",
                    "7","8","9",
                        "0"]
list_of_special_characters = [ "!", "@" , #List of all special character
                               "#","$","%",
                               "^","&","*",
                                "(",")"]

#Now will start the password generator code

password=[] #Will add the password based on user input
running = True

while running:
    #Will ask user how many lower case they want
    lower_case_input = int(input("Enter in how many lower case you want: "))
    if lower_case_input <10: #Only works if the lower case is less than 10
        #Will pick random lower case letters based on user's  input
        lower_case_random = random.sample(list_of_lower_letter, lower_case_input)
        lower_case = "".join(lower_case_random) #Will store the lower case in the variable lower_case
    else: #Will print out error and end code if it is too long
        print("Your password is too long! Ending...")
        exit()

    #print(lower_case) #Debugging

    #Will ask user how many upper case they want
    upper_case_input = int(input("Enter in how many upper case you want: "))
    if upper_case_input <10: #Only works if the upper case is less than 10
        #Will pick random upper case letters based on user's  input
        upper_case_random = random.sample(list_of_upper_letter, upper_case_input)
        upper_case = "".join(upper_case_random) #Will store the upper case in the variable lower_case
    else: #Will print out error and end code if it is too long
        print("Your password is too long! Ending...")
        exit()

    #print(upper_case) #Debugging

    #Will ask user how many numbers  they want
    numbers_input = int(input("Enter in how many numbers you want: "))
    if numbers_input <10: #Only works if the special character is less than 10
        #Will pick random special character based on user's  input
        numbers_random = random.sample(list_of_numbers, numbers_input)
        numbers = "".join(numbers_random) #Will store the special character in the variable lower_case
    else: #Will print out error and end code if it is too long
        print("Your password is too long! Ending...")
        exit()

    #print(numbers) #Debugging

    #Will ask user how many special characters  they want
    special_characters_input = int(input("Enter in how many special characters you want: "))
    if special_characters_input <10: #Only works if the special character is less than 10
        #Will pick random special character based on user's  input
        special_characters_random = random.sample(list_of_special_characters, special_characters_input)
        special_characters = "".join(special_characters_random) #Will store the special character in the variable lower_case
    else: #Will print out error and end code if it is too long
        print("Your password is too long! Ending...")
        exit()

    #print(special_characters) #Debugging

    #Will now print out the full password
    password =list(lower_case+upper_case+numbers+special_characters)#Will store all of it in one variable called password
    random.shuffle(password)
    output_password = ''.join(password)
    print(output_password) #Debugging

    if len(password) >12: #Will print out if it is a strong password or weak
        print("Strong password!")
    elif len(password)== 12:
        print("This is a good password")
    else: #Will show that it is a weak password
        print("Weak password")

    #Will now ask the user to play again or exist
    do_it_again = input("Play again by pressing y or any other key: ").lower()
    if do_it_again != "y":
        running = False

print("Existing the program.....")


#To do: shuffle the password up ✅
#To do: Show the strength of the password ✅
"""Koosta programm telefoniraamatu loomiseks.



1.       Peab saama sisestada nime ja telefoni numbrit
2.       Samal nimel võib olla ainult üks telefoni number
3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime
    a.       Kui vastet pole, siis peab võimaldama lisamist
4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)
5.       Lisa funktsioon terve raamatu kuvamiseks"""

fileName = "telefoniraamat.txt"
def load_data():
    """
    Loads data from file, if there is a file.
    Data is a dictionary that contains a list which includes a name and a number (they are a pair)
    It returns data (dictionary)
    :return:
    """
    data = {}
    try:
        with open(fileName, "r", encoding="utf-8") as f:
            for row in f:
                name, number = row.strip().split("-")
                data[name] = number
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    """
    Open the file and writes a name and number from dictionary to the txt file.
    :param data:
    :return:
    """
    with open(fileName, "w") as f:
        for name, number in data.items():
            f.write(name + "-" + number + "\n")

def find_number_with_name(data):
    """
    Searches number when inserting a name. If name is found in the dictionary it prints the number for that name.
    If name is not found, we will ask if user wants to save a contact. If they choose "yes" we will check if phone number
    is in correct form and save it with given name.
    :param data:
    :return:
    """
    name = input("Enter contact name to search: ")

    if name in data:
        print("Number: ", data[name])
    else:
        print("Name not found")
        lisa = input("Do you want to add new contact (yes/no)?")
        if lisa.lower() == "yes":
            print("Enter a phone number: ")
            number = check_number()
            data[name] = number
            save_data(data)

def find_name_with_number(data):
    """
    Find the person's name with phone number, checks if the number is in correct form. If it is, it checks from dictioonary if this
    number already exists. If it does it prints out the name. If not it will ask if you want to add it. If answer is yes it will ask name for number and check if the name already exists
    in dictionary. If its not then it saves the number.
    :param data:
    :return:
    """
    print("Write phone number to search.")
    number = check_number()
    for name, nr in data.items():
        if nr == number:
            print("Number belongs to: ", name)
            return

    print("Number not found.")
    add = input("Do you want to add this number (yes/no) ")
    if add.lower() == "yes":
        name = input("Enter a name: ")
        if name in data:
            print("Number already has a person.")
        else:
            data[name] = number
            save_data(data)
            print("Number added")

def check_number():
    """
    We checking if number is in right form. If it is we return the number.
    :return:
    """
    while True:
        number = input("Enter phone number: ")
        if number.isdigit() and len(number) == 8 and number.startswith("5"):
            return number
        else:
            print("Error! Number needs to be 8 characters long and start with 5.")

def add_contact(data):
    """
    Asking for a name to add to contacts (dictionary). If the name alreadys exists it will say so. Otherwise it will ask for number and check it and save the contact.
    :param data:
    :return:
    """
    name = str(input("Enter a name: "))

    if name in data:
        print("Name already exists")
        return
    number = check_number()
    data[name] = number
    save_data(data)
    print("Contact added")

def view_book(data):
    """
    If there is data in dictionary it will display contacts, otherwise it lets you know it's empty.
    :param data:
    :return:
    """
    if data:
        print("Contacts")
        for name, number in data.items():
            print(f"{name} - {number}")
    else:
        print("No contacts to view")

def main():
    """
    We load dictionary and have a menu. You have multiple options to go to.
    :return:
    """
    data = load_data()

    while True:
        print("""\n Main Menu
        1. Add contact
        2. Search contact by name
        3. Search contact by phone
        4. Open contacts
        5. Exit""")
        answer = input("Enter a number, to choose from menu.")
        if answer == "1":
            add_contact(data)
        elif answer == "2":
            find_number_with_name(data)
        elif answer == "3":
            find_name_with_number(data)
        elif answer == "4":
            view_book(data)
        elif answer == "5":
            print("Program exiting...")
            break
        else:
            print("Choose the right number.")



if __name__ == "__main__":
    main()

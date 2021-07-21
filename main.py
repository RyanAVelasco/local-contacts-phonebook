import os
import time
import re

address_book = 'address_book.txt'

## creates address book if one does not exist
if not address_book in os.listdir():
    file = open(address_book, 'w')
    file.write('[FORMAT] Name;Address;Email;Phone Number\n\n')
    file.close()
else: print(address_book)

## creates contact information
def create_contact(name, address, email, phone_number):
    file = open(address_book, 'r')

    ## save contact information to address book
    contacts = file.readlines()
    print(contacts)
    if name + ';' + address + ';' + email + ';' + phone_number + '\n' in contacts : print('already exists')
    else: 
        file.close()
        file = open(address_book, 'a')
        file.write(name + ';' + address + ';' + email + ';' + phone_number + '\n')

    ## assures the file is closed once done
    file.close()

def check_exists(info):

    ## checks for contact name in address book
    file = open(address_book, 'r')
    lines = file.readlines()
    for line in lines:
        if info in line:
            print('\nSorry, contact already exists!' + '\n>> ' + line.replace(';', ' -- '))
            return True
        else : continue

    ## assures the file is closed once done
    file.close()
    
while True:
    options = input('''
    Please choose from the list of options below:
    1) Add contact
    2) Delete contact
    3) Lookup contact
    4) Lookup all contacts
    5) Exit program
    \nPlease choose: ''').lower().strip()
    
    if options == '1' or options == 'add contact':
        while True:
            ## if contact name is already in address book then return to main menu
            name = input('\nFirst Name: ').title().strip()
            if check_exists(name) == True : break

            address = input('\nHome Address: ').title().strip()
            email = input('\nEmail: ').strip()
            phone_number = input('\nPhone number: ').strip()

            create_contact(name, address, email, phone_number)
            break
        
        # elif options == '2' or options == 'add contact':
        #     pass
        # elif options == '3' or options == 'add contact':
        #     pass
        # elif options == '4' or options == 'add contact':
        #     pass

    if options == '5' or options == 'exit' or options == 'exit program':
        exit = input('\nThanks for using address book\nShould I show you your address book before exitting? (Y/N): ').strip()
        if exit.lower() == 'yes' or exit.lower() =='y':
            print('\nHere you go')
            time.sleep(2)
            file = open(address_book, 'r')
            lines = file.readlines()
            for line in lines:
                print(line.replace(';', ' -- '))
            quit()
        else : quit()
        

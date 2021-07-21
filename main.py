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

def open_address_book():
    file = open(address_book, 'r')
    contacts = file.readlines()
    ## assures the file is closed once done
    file.close()
    return contacts

## creates contact information
def create_contact(name, address, email, phone_number):
    if name + ';' + address + ';' + email + ';' + phone_number + '\n' in open_address_book() : print('already exists')
    else: 
        file = open(address_book, 'a')
        file.write(name + ';' + address + ';' + email + ';' + phone_number + '\n')

    ## assures the file is closed once done
    file.close()

def check_exists(info):
    ## checks for contact name in address book
    for contact in open_address_book():
        if info in contact.split(';'):
            return True
        else : continue

def search_contacts(full_list, contact_name):
    file = open(address_book, 'r')
    contacts = file.readlines()

    if full_list == True:
        for contact in contacts:
            print('>>', contact.replace(';', ', ').replace('\n', ''))
    elif full_list == False:
        for contact in contacts:
            if contact_name in contact.split(';'):
                print('>>', contact.replace(';', ', ').replace('\n', ''))
            continue
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
            first_name = input('First Name: ').title().lstrip()  
            last_name = input('Last name: ').title().rstrip()  
            name = first_name + ' ' + last_name

            if check_exists(name) == True : 
                print('>> Contact', name, 'exists')
                break

            address = input('Home Address: ').title().strip()
            email = input('Email: ').strip()
            phone_number = input('Phone number: ').strip()

            create_contact(name, address, email, phone_number)
            print('\n[ADDED]', '\nName:', name, '\nAddress:', address, '\nEmail:', email, '\nPhone Number:', phone_number)
            break
    
    elif options == '2' or options == 'Delete contact':
        pass

    elif options == '3' or options == 'lookup contact':
        contact_name = input('Please enter name: ').title().strip()
        search_contacts(False, contact_name)

    elif options == '4' or options == 'lookup all contacts':
        search_contacts(True, None)

    elif options == '5' or options == 'exit' or options == 'exit program':
        exit = input('\nThanks for using address book\nShould I show you your address book before exitting? (Y/N): ').strip()
        if exit.lower() == 'yes' or exit.lower() =='y':
            print('\nHere you go')
            search_contacts(True, None)
            quit()
        else : quit()
        
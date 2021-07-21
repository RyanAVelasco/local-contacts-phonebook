import os
import time
import re

address_book = 'address_book.txt'

## creates address book if one does not exist
if not address_book in os.listdir():
    file = open(address_book, 'w')
    file.write('FORMAT >> Name;Address;Email;Phone Number\n\n')
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
        file.write('>>' + name + ';' + address + ';' + email + ';' + phone_number + '\n')

    ## assures the file is closed once done
    file.close()
    
while True:
    name = input('\nFirst Name: ').title().strip()
    address = input('\nHome Address: ').title().strip()
    email = input('\nEmail: ').strip()
    phone_number = input('\nPhone number: ').strip()

    create_contact(name, address, email, phone_number)
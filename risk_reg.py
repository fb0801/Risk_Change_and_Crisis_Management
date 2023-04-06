#application modules
import pathlib
import os.path
from pathlib import Path


risk_key= {
    "ID":" ",
    "Risk name":" ",
    "Impact Level":"",
    "Risk Response":"",
    "Risk Owner":"",
    "Priority":"",
    "Risk Status":""

}

text = 'Risk Register' #text to put into the database
text2= 'ID' #puts the text in the file as a header
text3= 'Risk Name' #puts the text in the file as a header
text4 = 'Impact Level' #puts the text in the file as a header
text5 = 'Risk Response' #puts the text in the file as a header
text6 = 'Risk Owner' #puts the text in the file as a header
text7 = "Priority"# put txt in file as header
text8 = 'risk status' #puts the text in the file as a header

def file_check():
    path_to_file = 'risk_reg.csv'
    path = Path(path_to_file)

    if path.is_file():
        print('File exists')
        file = open('risk_reg.csv', 'r+')
        menu()

    else:
        print('The file does not exist making file')
        file = open('risk_reg.csv', 'w+')
        menu()


def add():
    #adding to the applicationn 
    pass

def remove():
    pass
def edit():
    pass

def search():
    pass


def menu():
    while True: #a loop that will keep running
        print('\t\t\tMenu') #prints in the console
        #options for user to pick from
        option = input('Select a option:\n\n1.Add risk\n2.Remove risk\n3.Edit details\n4.Search for risk\n5.Quit\n')
        if option == "1":
            add() # take the user to add risk
        elif option =="2":
            remove() # take the user to remove risk
        elif option == "3":
            edit() # take the user to edit an employee details
        elif option == "4":
            search() # takes the user to search for an employee
        elif option == "5":
            quit() # exit the application
        else:
            print("Not valid") # if option by user does not match


if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    menu()
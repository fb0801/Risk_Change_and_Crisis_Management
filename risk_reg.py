import pathlib
import os.path

risk_key= {
    "ID":" ",
    "Risk name":" ",
}
def file_check():
    path_to_file = 'risk_reg.csv'
    path = Path(path_to_file)

    if path.is_file():
        print('File exists')

    else:
        print('The file does not exist making file')


file = open('risk_reg.csv', 'w+')
if file 

def add():
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
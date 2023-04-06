import random #import random module


#random game names for the user
random_game_names =['Jimmy', 'Levi','Princess James','Lady Bailey','Eren','Lord uncool',
                    'Prince Fluffy', 'Princess Jigsaw', 'Alisha', 'David', 'Elon', 'Doge Musk']

banned_game_names =['Slender man', 'gingerbread man', 'name',69, 'Mr T', 'max'
                    ,'min', 'range', 'yield', 'while', 'return', 'pass', 'none'
                    ,'and', 'break', 'true', 'false', 'global', 'pygame', 'pycharm',
                    1,2,3,4,5,6,7,8,9,0, 'yes', 'no',]


# game classes for user to choose from
character_class_list ={
"A":"Project Manager",
"C":"Risk Manager",
"L":"Consultant",
"AA":"Assassin",

"X":"Random character"
    }

health = 10
budget = 10000
total = 0

def game_name_change():
    '''Game name changer function'''
    user_choice=str(input("Would you like us to give you a name?: ")).lower()
    if user_choice == "yes":
        random_name = random.randint(0,7) #assign random a range
        game_name_pick= random_game_names[random_name] #access the list we have created
        print('Your new name is', game_name_pick, '\n')
       
        
    elif user_choice =="no":
        user_new_name=str(input('Enter your new name, we promise not to judge: '))
        name_checker =isinstance(user_new_name, str)
        if name_checker == True and user_new_name not in banned_game_names:
            print(f'We could have given you a better name {user_new_name}')
        else:
            game_name_change()

    else:
        print('Sorry I dont understand')
        game_name_change()





def quiz_end():
    #function for ending the game
    print("\n This is the end \n Beautiful friend \n This is the end \n My only friend, the end")



def quiz_start(name):
    
    #function for the quiz game to begin
    print(f'You will have {health} health points')
    print("Before your journey", name ,'can continue select your type class by entering the class letter')
    print (character_class_list)
    
    
    user_class_type=input('Choose your adventure Class from the list above with the corresponding letter: ').upper()
    if user_class_type in character_class_list:
        if user_class_type == "X":
            user_class_type= random.choice(list(character_class_list.keys()))
        
        print(character_class_list.get(user_class_type),'is your chosen character')
    else:
        print('not valid character class')
        quiz_start(name)




def welcome_screen():
    print ("Welcome to the game!") #print statement
    name = input("What is your name? ") #input statement
    print ('Are you sure', name ,' is your name? ') #prints the name in the sentenace
    user_name_confirm=str(input())
    
        
    if user_name_confirm =="yes" or user_name_confirm=="Yes":
        for b_g_n in banned_game_names:
            if name in banned_game_names:
                print('Sorry you cant use that name \n')
                welcome_screen()                
            else:
                print("Lets continue ",name)
                quiz_start(name)


    elif user_name_confirm =="No" or user_name_confirm=="no":
        print("Would you like to change your name? ")
        user_choice_2 =str(input())
        if user_choice_2 == 'yes' or user_choice_2 == 'Yes':
            game_name_change()
        else:
            print('Sorry I dont understand')
            welcome_screen()

    else:
        print('Sorry I dont understand')
        welcome_screen()
        


#runs the first function we have made above
if __name__=='__main__':
    welcome_screen()
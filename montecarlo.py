#module to use
import random


prob=int(input('Enter interation range: ')) #takes user input
run = True

while run:
    #while running will ask for the risk name and display different probabilites
    issue_name = str(input('Enter risk name: '))
    if issue_name == 'QUIT':
        run = False
    


    for num in range(1, prob):
        #depending on user input will determine how many results are shown
        predict=random.randint(1,100)#get random value between 1-100
        print("Trial",num,' for issue',issue_name,':',str(predict) + '%',"chance of happening")

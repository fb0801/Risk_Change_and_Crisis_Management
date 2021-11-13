#module to use
import random


prob=input('Enter probability: ')
issue_name = str(input('Enter risk name: '))

while issue_name !='QUIT':


    for num in range(1, prob):

        print("Trial",num,':',random(),"% chance of happening")

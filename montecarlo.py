#module to use
import random


#prob=int(input('Enter probability: '))
issue_name = str(input('Enter risk name: '))

while issue_name !='QUIT':


    for num in range(1, 100):
        predict=random.randint(1,100)
        print("Trial",num,' for issue',issue_name,':',predict,"% chance of happening")

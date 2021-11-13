#module to use
import random


prob=int(input('Enter interation range: '))
run = True

while run:
    issue_name = str(input('Enter risk name: '))
    if issue_name == 'QUIT':
        run = False
    


    for num in range(1, prob):
        predict=random.randint(1,100)
        print("Trial",num,' for issue',issue_name,':',predict,"% chance of happening")

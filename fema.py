'''
FEMA
'''
def display_results(risk_name, risk_sev, risk_hid, risk_lik, result):
    print()


def calculate_results(risk_name, risk_sev, risk_hid, risk_lik):

    result = risk,sev * risk_hid * risk_lik
    
    display_results(risk_name, risk_sev, risk_hid, risk_lik, result)
    



def user_risks():
    run = True

    while run:
        #while running will ask for the risk name and other factors
        risk_name=str(input('Enter name: ')) #takes user input
        risk_sev = int(input('Enter severity : '))
        risk_hid = int(input('Enter hideability : '))
        risk_lik = int(input('Enter likelyhood : '))
        
        if issue_name == 'QUIT':
            run = False

        if risk_sev, risk_hid, risk_lik not in range(0,10):
            print('out of range')
        else:
            calculate_results(risk_name, risk_sev, risk_hid, risk_lik):


def main_menu():
    print('Welcome to the FEMA application')
    user_risks()

'''
FEMA

likely = prob
severity = impact
hide = risk of us not seeing it
'''
def display_results(risk_name, risk_sev, risk_hid, risk_lik, result):
    print(risk_name, risk_sev, risk_hid, risk_lik, result)


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
        
        if risk_name == 'QUIT':
            run = False

        if risk_sev or risk_hid or risk_lik not in range(0,10):
            print('out of range')
            user_risks()
        elif type(risk_sev) or type(risk_hid) or type(risk_lik) != int:
            
        else:
            calculate_results(risk_name, risk_sev, risk_hid, risk_lik)


def main_menu():
    print('Welcome to the FEMA application')
    user_risks()



if __name__ =='__main__':
    main_menu()

'''
FEMA

likely = prob
severity = impact
hide = risk of us not seeing it
'''
fema_results = []
def store_risks(risk_name, risk_sev, risk_hid, risk_lik, result):
    #function to store results
    
    fema_results.append(risk_name, risk_sev, risk_hid, risk_lik, result)
    

def display_results(risk_name, risk_sev, risk_hid, risk_lik, result):
    #function to display results
    
    for results in fema_results:
        print(results)
'''
def display_results(risk_name, risk_sev, risk_hid, risk_lik, result):
    print('risk name | risk sev | risk hid | risk lik | result')
    print(risk_name, risk_sev, risk_hid, risk_lik, result)
'''

def calculate_results(risk_name, risk_sev, risk_hid, risk_lik):
    #function to calculate

    result = risk_sev * risk_hid * risk_lik
    
    store_risks(risk_name, risk_sev, risk_hid, risk_lik, result)
    #display_results(risk_name, risk_sev, risk_hid, risk_lik, result)
    



def user_risks():
    run = True

    while run:
        #while running will ask for the risk name and other factors
        risk_name=str(input('Enter name: ')) #takes user input
        risk_sev = int(input('Enter severity : '))
        risk_hid = int(input('Enter hideability : '))
        risk_lik = int(input('Enter likelyhood : '))
        
        if risk_name == 'QUIT' or 'show':
            run = False
            display_results(risk_name, risk_sev, risk_hid, risk_lik, result)
        break

        if risk_sev and risk_hid and risk_lik in range(1,10):
            calculate_results(risk_name, risk_sev, risk_hid, risk_lik)
            
            user_risks()
        elif risk_sev or risk_hid or risk_lik != int:
            print('not valid')
        elif risk_name == show:
            display_results()
        else:
            print('out of range')


def main_menu():
    print('Welcome to the FEMA application')
    user_risks()



if __name__ =='__main__':
    main_menu()

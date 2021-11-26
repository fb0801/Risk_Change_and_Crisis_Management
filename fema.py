'''
FEMA Qualitative analysis prgram by Farhan
Please dont forget to reference this if you do use it


likely = prob
severity = impact
hide = risk of us not seeing it
'''
global risk_name

fema_result_name = []
fema_risk_sev = []
fema_risk_hid = []
fema_risk_lik = []
fema_result = []

fema_results_dict = {
"risk name":"name",
"risk sev":'',
"risk hid":'',
"risk lik":'',
"result": '',
    }

def store_risks(risk_name, risk_sev, risk_hid, risk_lik, result):
    #function to store results
    
    '''fema_results.append(risk_name)
    fema_risk_sev.append(risk_sev)
    fema_risk_hid.append(risk_hid)
    fema_risk_lik.append(risk_lik)
    fema_result.append(result)
    '''
    fema_results_dict["risk_name"]= risk_name
    fema_results_dict['risk_sev'] = risk_sev
    fema_results_dict['risk_hid'] = risk_hid
    fema_results_dict['risk_lik'] = risk_lik
    fema_results_dict['result']= result

def display_results(risk_name, risk_sev, risk_hid, risk_lik):
    #function to display results
    for key, value in fema_results_dict.items():
        print('{}: {}'.format(key, value))
    #print(fema_results_dict)
    '''for results in fema_results_dict.values():
        print(results)'''
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
        menu_input = str(input('would you like to\nshow: display results\nQUIT: to quit app \nrun: use application\noption: '))
        if menu_input == 'show':
            run = False
            display_results(risk_name, risk_sev, risk_hid, risk_lik)
        elif menu_input =="run":
            risk_name=str(input('Enter name: ')) #takes user input
            risk_sev = int(input('Enter severity between 1-10: '))
            risk_hid = int(input('Enter hideability between 1-10: '))
            risk_lik = int(input('Enter likelyhood between 1-10 : '))
            #screen_options()
        

            if risk_sev and risk_hid and risk_lik in range(1,10):
                calculate_results(risk_name, risk_sev, risk_hid, risk_lik)
                menu_input = str(input('would you like to\nshow: display results\nQUIT: to quit app \nrun: use application\noption: '))
                if menu_input == 'show':
                    run = False
                    display_results(risk_name, risk_sev, risk_hid, risk_lik)
                elif menu_input =="run":
                    risk_name=str(input('Enter name: ')) #takes user input
                    risk_sev = int(input('Enter severity between 1-10: '))
                    risk_hid = int(input('Enter hideability between 1-10: '))
                    risk_lik = int(input('Enter likelyhood between 1-10 : '))
                else:
                    print('Sorry i dont understand')
                    #screen_options()
                
                #user_risks()
            elif risk_sev or risk_hid or risk_lik != int:
                print('not valid')
            elif risk_name == 'show':
                display_results()
            else:
                print('out of range')
        elif menu_input =="QUIT":
            quit
        else:
            print('Sorry i dont understand')
            screen_options()
        
       

def screen_options():
    menu_input = str(input('would you like to\nshow: display results\nQUIT: to quit app \nrun: use application\noption: '))
    if menu_input == 'show':
            run = False
            display_results(risk_name, risk_sev, risk_hid, risk_lik)
    elif menu_input =="run":
        user_risks()
    elif menu_input =="QUIT":
        quit
    else:
        print('Sorry i dont understand')
        screen_options()
    

def main_menu():
    print('Welcome to the FEMA application!')
    # screen_options()
    user_risks()


if __name__ =='__main__':
    main_menu()

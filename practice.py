#Banking system
while True:
    try:
        staff_login = eval(input('1 Staff Login \n2 Close App\n'))
    except NameError:
        print('invalid response, respond with 1 or 2')
        continue
    if staff_login == 1:
        user_login_name = input('Username: ')
        user_login_password = input('password: ')
        d = {}
        with open('staff.txt', 'r') as file:
            for line in file:
                (key, val) = line.split()
                d[str(key)] =  val
        if (user_login_name == d['username1'] and user_login_password == d['password1']) or (user_login_name == d['username2'] and user_login_password == d['password2']):
             print('Login successful')
        else:
            print('Login not successful, try again')
            continue
        
        user_session = open('user_session.txt', 'w')
        user_session.write(f'''username: {user_login_name}
password: {user_login_password}''')
        user_session.close()
        while True:
            try:
                customer_action = eval(input('1 Create New Bank Account \n2 Check Account Details \n3 Logout\n'))
            except NameError:
                print('invalid response, respond with 1, 2, or 3')
                continue
            if customer_action == 1:
                account_name = input('Account Name:\n')
                opening_balance = eval(input('Opening Balance(NGN):\n'))
                account_type = input('Account Type(savings, current, Fixed Deposit):\n')
                account_email = input('E_mail address:\n')
                account_number ='0'
                from random import randint
                for i in range(9):
                    digits = randint(0, 9)
                    account_number += str(digits)
                print(f'Your account number is {account_number}')
                customer_details = open('customer.txt', 'w')
                customer_details.write(f'''Account Name: {account_name}
Opening Balance: {opening_balance}
Account Type: {account_type}
Account E_mail: {account_email}
Account Number: {account_number}''')
                customer_details.close()
            elif customer_action == 2:
                acct_number = input('Enter account number:\n')
                customer_details = open('customer.txt', 'r')
                customer = customer_details.read()
                if acct_number in customer:
                    print(customer)
                else:
                    print('please enter correct acct details')
            elif customer_action == 3:
                break
    elif staff_login == 2:
        break

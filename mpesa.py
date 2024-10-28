mpeso = input('Dial')

print('1 Send Money \n'
      '2 Withdrow Cash \n'
      '3 Buy Airtime \n'
      '4 Loans and Saving \n'
      '5 Financial Service \n'
      '6 Lipa na MPESA \n'
      '7 My Account \n'
      '8 Pochi la Biashara \n'
      '9 M-PESA Ratiba \n'
      '98 MORE \n')



print('waiting....')

myaccount = input()

if myaccount == '7':
    print('My Account \n'
          '1 UNLOCK M-PESA PIN \n'
          '2 MPESA PIN Manager \n'
          '3 M-PESA Statment \n'
          '4 Manage Junior Account \n'
          '5 check Balance \n'
          '6 Tariff Query \n'
          '00 Home'
          )
    
else:
    print(' error : Invalid option. Please select a valid option.')



checkbalance = input()

if checkbalance == '5':
    print(input('Enter M-pesa PIN : '))
    print('You request is processed . Please wait for the confirmation short message')

else:
    print(' error , Try it again')
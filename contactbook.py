# mini contact book 

# list aan ku kaydin doono lambarada iyo magac yadooda .

contacts = []

print(

    ' ----- CONTACT BOOK MENU ----- \n'
    '1. Kudar contact \n'
    '2. Arag contact oo dhan \n'
    '3. Raadi magac gaar ah \n'
    '4. Exit \n'
    '5. delete contact \n')
    
    
choice = input('Door (1-4): ')
    
if choice == '1':
    name = str(input('Magaca : '))
    number = int(input('lambarka : '))
        
    print('saving ....')
        
        
contact = {'name': name , 'number': number}
contacts.append(contact)


    
        

        
        
        
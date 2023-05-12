from threading import Thread, Lock
from time import sleep
from random import random

bal = 1000

lock = Lock()

def Pasa(lock, identifier, amount):
    global bal
    with lock:
        bal -= amount
        print(f'{identifier} has been successfully loaded with {amount}.')
def topUp():
    mobile = input('Input the number you wish to top-up: ')   
    if len(mobile) == 10:
        return mobile;
        
    else:
        print('That is not a valid number')
        topUp()
            
while True: 
    print('\n~~~~~Pasaload~~~~~~~')
    print(f'Your curent balance is: {bal} ')

    choice = int(input('''Choose amount to send:
    20
    50
    100 \n
'''))
    mobile = topUp()

    if choice <= bal:
        sleep(random())
    if choice == 20:
      Thread(target=Pasa, args=(lock, mobile, choice)).start()
    elif choice == 50:
      Thread(target=Pasa, args=(lock, mobile, choice)).start()
    elif choice == 100:
      Thread(target=Pasa, args=(lock, mobile, choice)).start()
    else: 
        print('Cannot Process Your Request.')
else: 
    print('Warning! Your balance too low!')
from threading import Thread, Lock
from time import sleep
from random import random

bal = 1000

lock = Lock()

def Pasa(lock, identifier, amount):
    global bal
    with lock:
        bal -= amount
        print(f'{identifier} has been successfully loaded with {amount}.')
def topUp():
    mobile = input('Input the number you wish to top-up: ')   
    if len(mobile) == 10:
        return mobile;
        
    else:
        print('That is not a valid number')
        topUp()
            
while True: 
    print('\n~~~~~Pasaload~~~~~~~')
    print(f'Your curent balance is: {bal} ')

    choice = int(input('''Choose amount to send:
    20
    50
    100 \n
'''))
    mobile = topUp()

    if choice <= bal:
        sleep(random())
    if choice == 20:
      Thread(target=Pasa, args=(lock, mobile, choice)).start()
    elif choice == 50:
      Thread(target=Pasa, args=(lock, mobile, choice)).start()
    elif choice == 100:
      Thread(target=Pasa, args=(lock, mobile, choice)).start()
    else: 
        print('Cannot Process Your Request.')
else: 
    print('Warning! Your balance is too low!')

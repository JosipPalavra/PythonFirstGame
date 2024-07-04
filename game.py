import time
from colorama import Fore, Back,  Style
import os   
import random 

loopin = 0
tries = 0
nazad ='Ananas'
timer = 1
full_loop_home = 0
onodrugo = 0
balance = 0
difficulty = 1

os.system('cls')
while loopin == 0:
    print('')
    age = int(input(f'{Style.BRIGHT}How old are you? '))
    dodatno = '0'
    if age >= 60:
        print(f'{Style.BRIGHT}You are too old for the game')
        break
    elif age < 60:
        dodatno = input(f'{Style.BRIGHT}Are you really ' + str(age) + f'{Style.BRIGHT} years old? ')
        if dodatno == 'YES' or dodatno== 'Yes' or dodatno == 'yes':
            print('')
            print(f'{Fore.GREEN}{Style.BRIGHT}Age Noted.{Fore.WHITE}{Style.NORMAL}', end='\r')
            time.sleep(2)
            loopin = 2       
        elif dodatno == 'NO' or dodatno== 'No' or dodatno == 'no':
            tries += 1
            if tries == 1:
                print('You have',3-tries,'tries left!')
                continue
            elif tries == 2:
                print('You have',3-tries,'try left!')
            elif tries >=3:
                print("You're kicked from the game!")
                time.sleep(1)
                break
              
if loopin == 2:
    loopin = 3
    full_loop_home = 1
    timer = 1
    
while full_loop_home == 1:
    if loopin == 3:    
        os.system('cls')
        loopin = 8
        
    if loopin == 8:    
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}------\n HOME\n------\n{Fore.WHITE}{Style.NORMAL}')
        print(f'{Style.BRIGHT}To START the game, type "Start"')
        if timer == 1:
            time.sleep(2)
        elif timer == 2:
            time.sleep(0)
        print(f'{Style.BRIGHT}To go to the SETTINGS page, type "Settings"')
        if timer == 1:
            time.sleep(2)
        elif timer == 2:
            time.sleep(0)
        print(f'{Style.BRIGHT}To go to the HELP page, type "Help"')
        if timer == 1:
            time.sleep(2)
        elif timer == 2:
            time.sleep(0)
        print(f'{Style.BRIGHT}To check your BALANCE, type "Balance"')
        print('')
        if timer == 1:
            time.sleep(2)
        elif timer == 2:
            time.sleep(0)
        print(f'{Style.BRIGHT}To CLOSE the program, type "Close"')
        print('')
        if timer == 1:
            time.sleep(2)
        elif timer == 2:
            time.sleep(0)
        oce = input('What do you want? ')
        if oce == 'SETTINGS' or oce == 'Settings' or oce == 'settings':
            if difficulty == 1:
                loopin = 4
            elif difficulty == 2:
                loopin = 10
            elif difficulty == 3:
                loopin = 11
            elif difficulty == 4:
                loopin = 12
        elif oce == 'HELP' or oce == 'Help' or oce == 'help':   
            loopin = 5
        elif oce == 'CLOSE' or oce == 'Close' or oce == 'close':
            loopin = 6
        elif oce == 'START' or oce == 'Start' or oce == 'start':
            loopin = 7
        elif oce == 'BALANCE' or oce == 'Balance' or oce == 'balance':
            loopin = 9
        
    if loopin == 4:        
        os.system('cls')
        difficulty = 1
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}----------\n SETTINGS\n----------\n{Fore.WHITE}{Style.BRIGHT}') 
        print(f'Select Difficulty: {Back.MAGENTA}{Style.BRIGHT}Easy{Fore.WHITE}{Back.BLACK}{Style.BRIGHT}    Medium    Hard    Very Hard')   
        print('')
        print('To select the difficulty, type in the name of the difficulty.')
        print('To go back to the home page, type "Back"')        
        print('')
        nazad = input('')
        if nazad == "BACK" or nazad == "Back" or nazad == "back":
            timer = 2
            loopin = 3
        elif nazad == "MEDIUM" or nazad == "Medium" or nazad == "medium":
            loopin = 10
        elif nazad == "HARD" or nazad == "Hard" or nazad == "hard":
            loopin = 11
        elif nazad == "VERY HARD" or nazad == "Very Hard" or nazad == "very hard":
            loopin = 12
       
    if loopin == 5:   
        os.system('cls')
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}------\n HELP\n------\n{Fore.WHITE}{Style.NORMAL}')                                            
        print(f'{Style.BRIGHT}1. The computer will think of a random number depending on which setting you selected.')
        print('')
        print(f'{Style.BRIGHT}2. You enter the number you think the computer is thinking of.')
        print('')
        print(f'{Style.BRIGHT}3. If you guess the number correctly, coins will be added to your balance, depending on the difficulty.')
        print('')
        print(f"{Style.BRIGHT}4. If you don't guess the number correctly, coins will be removed from your balance, depending on the difficulty.")
        print('')
        print('To go back to the home page, type "Back"')        
        print('')
        nazad = input('')
        if nazad == "BACK" or nazad == "Back" or nazad == "back":
            timer = 2
            loopin = 3

    if loopin == 6:
        print('')
        for i in range(3):
            print(f'{Fore.GREEN}{Style.BRIGHT}Closing Program.   ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Closing Program..  ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Closing Program... {Fore.WHITE}{Style.NORMAL}', end='\r')
            time.sleep(0.5)
        exit(1)
        
    if loopin == 9:
        os.system('cls')
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}---------\n BALANCE\n---------\n{Fore.WHITE}{Style.BRIGHT}')
        print(f'{Style.BRIGHT}Your balance is currently',balance,'coins!') 
        print('')
        print('To go back to the home page, type "Back"')        
        print('')
        nazad = input('')
        if nazad == "BACK" or nazad == "Back" or nazad == "back":
            timer = 2
            loopin = 3
            
    if loopin == 10:
        os.system('cls')
        difficulty = 2
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}----------\n SETTINGS\n----------\n{Fore.WHITE}{Style.BRIGHT}') 
        print(f'Select Difficulty: Easy    {Back.MAGENTA}{Style.BRIGHT}Medium{Fore.WHITE}{Back.BLACK}{Style.BRIGHT}    Hard    Very Hard')   
        print('')
        print('To select the difficulty, type in the name of the difficulty.')
        print('To go back to the home page, type "Back"')        
        print('')
        nazad = input('')
        if nazad == "BACK" or nazad == "Back" or nazad == "back":
            timer = 2
            loopin = 3
        elif nazad == "EASY" or nazad == "Easy" or nazad == "easy":
            loopin = 4
        elif nazad == "HARD" or nazad == "Hard" or nazad == "hard":
            loopin = 11
        elif nazad == "VERY HARD" or nazad == "Very Hard" or nazad == "very hard":
            loopin = 12

        
    if loopin == 11:
        os.system('cls')
        difficulty = 3
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}----------\n SETTINGS\n----------\n{Fore.WHITE}{Style.BRIGHT}') 
        print(f'Select Difficulty: Easy    Medium    {Back.MAGENTA}{Style.BRIGHT}Hard{Fore.WHITE}{Back.BLACK}{Style.BRIGHT}    Very Hard')   
        print('')
        print('To select the difficulty, type in the name of the difficulty.')
        print('To go back to the home page, type "Back"')        
        print('')
        nazad = input('')
        if nazad == "BACK" or nazad == "Back" or nazad == "back":
            timer = 2
            loopin = 3
        elif nazad == "EASY" or nazad == "Easy" or nazad == "easy":
            loopin = 4
        elif nazad == "MEDIUM" or nazad == "Medium" or nazad == "medium":
            loopin = 10
        elif nazad == "VERY HARD" or nazad == "Very Hard" or nazad == "very hard":
            loopin = 12
        
    if loopin == 12:
        os.system('cls')
        difficulty = 4
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}----------\n SETTINGS\n----------\n{Fore.WHITE}{Style.BRIGHT}') 
        print(f'Select Difficulty: Easy    Medium    Hard    {Back.MAGENTA}{Style.BRIGHT}Very Hard{Fore.WHITE}{Back.BLACK}{Style.BRIGHT}')   
        print('')
        print('To select the difficulty, type in the name of the difficulty.')
        print('To go back to the home page, type "Back"')        
        print('')
        nazad = input('')
        if nazad == "BACK" or nazad == "Back" or nazad == "back":
            timer = 2
            loopin = 3
        elif nazad == "EASY" or nazad == "Easy" or nazad == "easy":
            loopin = 4
        elif nazad == "MEDIUM" or nazad == "Medium" or nazad == "medium":
            loopin = 10
        elif nazad == "HARD" or nazad == "Hard" or nazad == "hard":
            loopin = 11
    
    if loopin == 7 and difficulty == 1:
        os.system('cls')
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}------\n GAME\n------\n{Fore.WHITE}{Style.NORMAL}')
        print(f'{Style.BRIGHT}I am thinking of a number between 1 and 3.')
        broj = random.randint(1,3)
        print('')
        print('What number am I thinking of?')
        print('')
        guess = int(input(''))
        if guess == broj:
            print('')
            print('Congratulations! You guessed the number! You get 5 coins!')
            balance += 5 
        elif guess != broj:
            print('')
            print("Oh no! You didn't guess the number! You lose 2 coins!")
            balance += -2
        print('')
        for i in range(3):
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page.   ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page..  ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page... {Fore.WHITE}{Style.NORMAL}', end='\r')
            time.sleep(0.5)  
        timer = 2
        loopin = 3
        
    if loopin == 7 and difficulty == 2:
        os.system('cls')
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}------\n GAME\n------\n{Fore.WHITE}{Style.NORMAL}')
        print(f'{Style.BRIGHT}I am thinking of a number between 1 and 5.')
        broj = random.randint(1,5)
        print('')
        print('What number am I thinking of?')
        print('')
        guess = int(input(''))
        if guess == broj:
            print('')
            print('Congratulations! You guessed the number! You get 5 coins!')
            balance += 5 
        elif guess != broj:
            print('')
            print("Oh no! You didn't guess the number! You lose 2 coins!")
            balance += -2
        print('')
        for i in range(3):
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page.   ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page..  ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page... {Fore.WHITE}{Style.NORMAL}', end='\r')
            time.sleep(0.5)  
        timer = 2
        loopin = 3
        
    if loopin == 7 and difficulty == 3:
        os.system('cls')
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}------\n GAME\n------\n{Fore.WHITE}{Style.NORMAL}')
        print(f'{Style.BRIGHT}I am thinking of a number between 1 and 10.')
        broj = random.randint(1,10)
        print('')
        print('What number am I thinking of?')
        print('')
        guess = int(input(''))
        if guess == broj:
            print('')
            print('Congratulations! You guessed the number! You get 5 coins!')
            balance += 5 
        elif guess != broj:
            print('')
            print("Oh no! You didn't guess the number! You lose 2 coins!")
            balance += -2
        print('')
        for i in range(3):
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page.   ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page..  ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page... {Fore.WHITE}{Style.NORMAL}', end='\r')
            time.sleep(0.5)  
        timer = 2
        loopin = 3
        
    if loopin == 7 and difficulty == 4:
        os.system('cls')
        print('')
        print(f'{Fore.CYAN}{Style.BRIGHT}------\n GAME\n------\n{Fore.WHITE}{Style.NORMAL}')
        print(f'{Style.BRIGHT}You are {age} years old, right?')
        time.sleep(2)
        print(f'{Style.BRIGHT}Well in that case, I am thinking of a number between 1 and {age}.')
        broj = random.randint(1,age)
        print('')
        print('What number am I thinking of?')
        print('')
        guess = int(input(''))
        if guess == broj:
            print('')
            print('Congratulations! You guessed the number! You get 5 coins!')
            balance += 5 
        elif guess != broj:
            print('')
            print("Oh no! You didn't guess the number! You lose 2 coins!")
            balance += -2
        print('')
        for i in range(3):
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page.   ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page..  ', end='\r')
            time.sleep(0.5)
            print(f'{Fore.GREEN}{Style.BRIGHT}Going back to Home page... {Fore.WHITE}{Style.NORMAL}', end='\r')
            time.sleep(0.5)  
        timer = 2
        loopin = 3
    

    
       
    
    

    
    



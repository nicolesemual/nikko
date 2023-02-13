print("""


 ▄▄▄       ██ ▄█▀▄▄▄       ███▄ ▄███▓▓█████      ▄████  ▄▄▄          ██ ▄█▀ ██▓ ██▓     ██▓    
▒████▄     ██▄█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀     ██▒ ▀█▒▒████▄        ██▄█▒ ▓██▒▓██▒    ▓██▒    
▒██  ▀█▄  ▓███▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░▄▄▄░▒██  ▀█▄     ▓███▄░ ▒██▒▒██░    ▒██░    
░██▄▄▄▄██ ▓██ █▄░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ░▓█  ██▓░██▄▄▄▄██    ▓██ █▄ ░██░▒██░    ▒██░    
 ▓█   ▓██▒▒██▒ █▄▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░▒▓███▀▒ ▓█   ▓██▒   ▒██▒ █▄░██░░██████▒░██████▒
 ▒▒   ▓▒█░▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░    ░▒   ▒  ▒▒   ▓▒█░   ▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░
  ▒   ▒▒ ░░ ░▒ ▒░ ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░   ░   ▒   ▒▒ ░   ░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░
  ░   ▒   ░ ░░ ░  ░   ▒   ░      ░      ░      ░ ░   ░   ░   ▒      ░ ░░ ░  ▒ ░  ░ ░     ░ ░   
      ░  ░░  ░        ░  ░       ░      ░  ░         ░       ░  ░   ░  ░    ░      ░  ░    ░  ░
                                                                                               


""")                                  
print("Welcome To Akame Ga Kill")              
player_name = input('What is your name, adventurer\n') 
 
health = 100 
damage = 20 
 
print('\nwelcome, ' + player_name + ' !you have ' + str(health) + ' health and can do damage ' + str(damage)) 
print('You came acress a pyscho!! what you will do??')

print('1. Fight')
print('2. Run')

choice = int(input('Enter either 1 or 2: ')) 
if choice == 1: 
    print("You attack the dragon and do " + str(damage) + ' damage') 
    print('the akame back off, spit some acid and does 10 damage') 
    health -= 10 
    print('Your current health is ' + str(health)) 
elif choice == 2: 
    print('You run away from the akame') 
    print('live today for tomorrow') 
    print('The Dragon manage to throw rocks at you deals with twice the damage you inflict')

    health==(10*2)
    print('Your current health is = ' + str (health))
else: 
    print('\nInvalid choice, the akame get to kill you alive!!!') 
print("Thanks for playing!")
# Rock-paper-scissors-lizard-Spock 
import random

def name_to_number(name):
    if name=='rock':
        return 0
    elif name=='Spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    else:
        return 4

def number_to_name(number):
    if number==0:
        return 'rock'
    elif number==1:
        return 'Spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    else:
        return 'scissors'

def rpsls(player_choice):
    
    print 
    
    print 'Player chooses',player_choice
    
    player_value=name_to_number(player_choice)

    comp_value=random.randrange(0,4)

    number_to_name(comp_value)
    result=(player_value-comp_value)%5

    print 'Computer chooses',number_to_name(comp_value)
    
    if ((result%5)==1) or ((result%5)==2):
        print 'Player wins!'
    elif ((result%5)==3) or ((result%5)==4):
        print 'Computer wins!'
    else:
        print 'Player and computer tie!'

    
#Test!!!
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

from random import randint
n = input ("Enter dice side:")
player1_name = input ("player1_name:")
player2_name = input ("player2_name:")
n = int (n) 
dice1_roll= randint(1,n)
dice2_roll = randint (1,n)
print (player1_name + " rolled:"+ str (dice1_roll))
print(player2_name + " rolled:"+str(dice2_roll))
if dice1_roll==dice2_roll:
    print ("Tie!")
elif dice1_roll>dice2_roll:
    print ("The winner is"+ player1_name)
else:
    print ("The winner is" + player2_name)
    

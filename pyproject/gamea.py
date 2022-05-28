import random
print("rock")
print("paper")
print("scissors")
p_1=input("player-1,make your move").lower()
randp_2=random.randint(0,2)
if randp_2==0:
    p_2="rock"
elif randp_2==1:
    p_2="paper"
else :
    p_2="scissors"
print("player-1,make your move"+ p_2)
if p_1=="rock" and p_2=="paper":
    print("player-2 wins!...")
elif p_1=="rock" and p_2=="scissors":
    print("player-1 wins!...")
elif p_1=="paper" and p_2=="rock":
    print("player-1 wins!...")
elif p_1=="paper" and p_2=="scissors":
    print("player-2 wins!...")
elif p_1=="scissors" and p_2=="paper":
    print("player-1 wins!...")
elif p_1=="scissors" and p_2=="rock":
    print("player-2 wins!...")
elif p_1==p_2:
    print("thats a tie...")
else:
    peint("something went wrong...")








from card_dict import *
from action import *

players=[]

for i  in range(5):
    players.append(player(i))
    players[i].blood_m(5)
    players[i].print_status()
print(Check_Range_No_Weapon(1,players))





from card_dict import *
from action import *

players=[]

for i  in range(8):
    players.append(player(i))
    players[i].blood_m(5)
    players[i].print_status()
x=0
#players[x].equip_m(1,65)
players[1].equip_m(1,66)
print(Check_Range_No_Weapon(x,players))





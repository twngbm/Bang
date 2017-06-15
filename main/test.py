from card_dict import *
from action import *

players=[]

for i  in range(8):
    players.append(player(i))
    players[i].blood_m(5)
    players[i].setid(i)
    players[i].print_status()
players[0].blood_m(-10)
players[2].blood_m(-10)
players[3].blood_m(-10)

print(Gameover_Check(players))




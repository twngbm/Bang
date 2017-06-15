import math
import os
import random
import sys
from game_init import *
from action import *


#card_dict={id:["card name",type(0~3),color(0~51),"card effect"]}
#char_dict={id:[player ability,blood]} 
#1=thief win 2=traitor win 3=traitor1 win 4=traitor2 win 5=police win 0= no one win yet


#Main Function


#Game_Init
    
person=Player_numbers()                         #Enter players number
identity_dict=identity_make_up(person)          #Init card,identity,char,players,wasted_card list and shuffle

random.shuffle(identity_list)
random.shuffle(character_list)
random.shuffle(card_list)

for i in range(person):
    players.append(player(i))

Set_identity(person,players,identity_list)      #Set Player Identity

#Set_character(person,players,character_list)    #Set Player Character

Set_blood(person,players)                       #Set Player Blood

Set_card(person,players,card_list)              #Spare Card

#Game_Init End
print("player number, id, char, (max_life,life),card,equip,status")



#Print Player init status
for i in range(person):
    players[i].print_status()

#test section-------------------------
    
for i in range(person):
    players[i].setchar(i)
    players[i].card_m(1,0)
    players[i].card_m(1,25)
    players[i].card_m(1,37)
    players[i].card_m(1,38)
    players[i].card_m(1,68)
players[0].equip_m(1,63)
players[1].equip_m(1,63)
    
for i in range(person):
    players[i].print_status()

#test section-------------------------
#Main Loop

while True: 
    for i in range(person):  
        #Init player status at every start
        for j in range(len(players)):
            players[j].print_status
        gameover=0
        card_list=Card_Reuse(card_list,wasted_card_list)
        
        #Live Status Check Stage
        if players[i].blood<=0:
            continue
        #Live Status Check Stage Finish
        
        #Buff Check Stage
        x=Buff_Check(i,person,players,card_list,wasted_card_list)
        if x==1:
            gameover=1
            break
        if x==2:
            continue
        #Buff Check Stage Finish
        
        #Draw Card Stage
        
        Darw_Card(i,players,card_list,wasted_card_list)
        #Draw Card Stage Finish

        #CARD_USE_STAGE


        #Use_Card(i,players,card_list,wasted_card_list)
        gameover=Use_Card(i,players,card_list,wasted_card_list)

        #CARD_USE_STAGE_FINISH
        if gameover==1:
            break
    
        
        #Discard Stage
        Discard(i,players,wasted_card_list,1) #0=online_mode,1=test_mode
        #Discard Stage Finish
        #players[i].print_status()
    if gameover==1:
        break
    
#Gameover


print(Gameover_Check(players))
print("final_status:\n")
for i in range(person):
    players[i].print_status() 

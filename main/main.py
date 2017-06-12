import math
import os
import random
import sys
from card_dict import *
from game_init import *
from action import *
from character_function import *
from card_function import *


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


#Main Loop

while True: #Game Loop
    for i in range(person):    
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
        players[i].blood_m(-1)
        players[i].card_m(1,40)
        players[i].card_m(1,44)
        players[i].card_m(1,48)
        players[i].card_m(1,49)
        players[i].card_m(1,50)
        players[i].card_m(1,51)
        players[i].card_m(1,57)
        players[i].card_m(1,59)
        Darw_Card(i,players,card_list,wasted_card_list)
        players[i].print_status()
        #Draw Card Stage Finish

        #CARD_USE_STAGE


        #Use_Card(i,players,card_list,wasted_card_list)
        while True:
            print("Player",i+1,"you have",len(players[i].card),"cards now")
            if len(players[i].card)==0:
                print("You have no more card,Force end turn.")
                break
            for j in players[i].card:
                print(j,card_dict[j])
            print("input card ID to select a card to use it.")
            print("Or input 999 to end the turn")
            selected=int(input(":"))
            if selected==999:
                print("You chose to end the turn.")
                break


            if card_dict[selected][1]==0:
                pass
            elif card_dict[selected][1]==1:
                Set_Function_Card(i,players,selected,card_list,wasted_card_list)
            elif card_dict[selected][1]==2:
                Set_Equipment(i,players,selected)
            elif card_dict[selected][1]==3:
                Set_Buff(i,players,selected)


        #CARD_USE_STAGE_FINISH

        
        #Discard Stage
        Discard(i,players,wasted_card_list,1) #0=online_mode,1=test_mode
        #Discard Stage Finish
        #players[i].print_status()
    if gameover==1:
        break

#Gameover

win=Gameover_Check(players)
print(win)
print("final_status:\n")
for i in range(person):
    players[i].print_status() 

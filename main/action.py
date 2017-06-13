'''card_dict={id:["card effect",type(0~3),color(0~51)]}'''  
'''char_dict={id:[player ability,blood]} '''    
''' 1=thief win 2=traitor win 3=traitor1 win 4=traitor2 win 5=police win 0= no one win yet'''
from character_function import *
from card_function import *
from card_dict import *
import random

def Darw_Card(i,players,card_list,wasted_card_list):
    
    if players[i].char==1: #Black Jack character ability.
        print(Black_Jack(i,players,card_list))
    elif players[i].char==4:#Jesse Jones character ability.
        Jesse_Jones(i,players,card_list)
        Suzy_Lafayette(i,players,card_list)        
    elif players[i].char==6:#Kit Carlson character ability
        Kit_Carlson(i,players,card_list)
    elif players[i].char==9:#Pedro Ramirex character ability
        Pedro_Ramirex(i,players,card_list,wasted_card_list)
    else:
        for j in range(2):
            players[i].card_m(1,card_list.pop())
    
def Bomb(x,person,players,card_list,wasted_card_list):
    if len(set([1,2,3,4,5,6,7,8]) & set(Judge(x,players,card_list,wasted_card_list)))>0: #Judge fail, bomb exploid
        players[x].blood_m(-3)                       #Damage
        players[x].buff_m(0,71)                      #Remove card from player
        wasted_card_list.append(71)                  #add card to the wasted_card_list
        print("Bomb exploid , do 3 damage to player",x+1)
        return 1
    else:                                            #Judge success
        players[x].buff_m(0,71)                      #Remove card from player
        while True:
            if players[(x+1)%person].blood>0:
                players[(x+1)%person].buff_m(1,71)          #Pass The card to the next player
                break
            else:
                x=x+1
        print("Bomb didn't exploid,pass the bomb to player",(x+1)%person+1)
        return 0

def Jail(i,players,card_list,wasted_card_list):
    if len(set([13,14,15,16,17,18,19,20,21,22,23,24,25])&set(Judge(i,players,card_list,wasted_card_list)))==0:  #Judge Fail, You sleep
        card=int(players[i].buff.pop())
        wasted_card_list.append(card)   
        print("Player",i+1,"fail to escape from Jail")                         
        return 1                                                             
    else:
        card=int(players[i].buff.pop())
        wasted_card_list.append(card)                            #add Jail card to the wasted_card_list
        print("Player",i+1,"escape successful.")
        return 0

def Buff_Check(i,person,players,card_list,wasted_card_list):
    while len(players[i].buff)!=0:              #Check Jail or bomb exist
        if 71 in players[i].buff:
            if Bomb(i,person,players,card_list,wasted_card_list)==1:
                win=Gameover_Check(players)
                if type(win)!=int:                               #Whenever there is a damage,we must make a judge if the game is over
                    return 1
                if players[i].blood<=0:
                    return 2
        if 68 in players[i].buff or 69 in players[i].buff or 70 in players[i].buff: 
            if Jail(i,players,card_list,wasted_card_list)==1:
                return 2

def Card_Reuse(card_list,wasted_card_list):
        if len(card_list)<5:
            temp_list=[]
            temp_list.append(wasted_card_list.pop())
            random.shuffle(wasted_card_list)
            card_list=wasted_card_list+card_list
            wasted_card_list.clear()
            wasted_card_list.append(temp_list.pop())
        return card_list

def Discard(i,players,wasted_card_list,test_code):
    if test_code==1:
        if len(players[i].card)>players[i].blood:
            n=len(players[i].card)-players[i].blood
            for j in range(n):
                card=players[i].card[0]
                players[i].card_m(0,card)
                wasted_card_list.append(card)
    elif test_code==0:
        if len(players[i].card)>players[i].blood:
            n=len(players[i].card)-players[i].blood
            print("You must discard",n,"card")
            for j in range(n):
                print("You have",players[i].card,"Now")
                print("Enter card ID to diacard")
                players[i].card_m(0,int(input(":")))
                
def Set_Buff(i,players,selected):
    if card_dict[selected][4]==71:
        Set_Bomb_Buff(i,players)
    if card_dict[selected][4]==11:
        Set_Jail_Buff(i,players,selected)

def Set_Equipment(i,players,selected):
    if equip_card[card_dict[selected][4]][0]==0:
        Equipment_Check_Same(i,players,selected)
    elif equip_card[card_dict[selected][4]][0]==1:
        Weapon_Check_Same(i,players,selected)

def Set_Function_Card(i,players,selected,card_list,wasted_card_list):
    if card_dict[selected][4]==1:
        print("You are not under attack, You don't need to play Miss")
        print("You are not Calamity Janet either, you can't use this card now")
        status=-1
    elif card_dict[selected][4]==3:
        status=Panic(i,players)
    elif card_dict[selected][4]==4:
        status=Cat_Balou(i,players,wasted_card_list)
    elif card_dict[selected][4]==5:
        status=Stagecoach(i,players,card_list)
    elif card_dict[selected][4]==6:
        status=General_Store(i,players,card_list)
    elif card_dict[selected][4]==7:
        status=Beer(i,players,wasted_card_list)
    elif card_dict[selected][4]==50:
        status=Wells(i,players,card_list)
    elif card_dict[selected][4]==59:
        status=Saloon(players)
    if status!=-1:
        players[i].card_m(0,selected)
        wasted_card_list.append(selected)

    Suzy_Lafayette(status,players,card_list)
    
def Set_Attack_Card(i,players,selected,card_list,wasted_card_list):
    if card_dict[selected][4]==0:
        pass
    elif card_dict[selected][4]==1:
        pass
    elif card_dict[selected][4]==2:
        pass
    elif card_dict[selected][4]==8:
        pass
    elif card_dict[selected][4]==37:
        pass
    
    if status!=-1:
        players[i].card_m(0,selected)
        wasted_card_list.append(selected)

    if type(Gameover_Check(players))!=int:
        return 1





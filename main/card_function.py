from card_dict import *

def Set_Bomb_Buff(i,players):
    players[i].card_m(0,71)
    players[i].buff_m(1,71)
    print("Player",i+1,"You have set up a bomb")

def Set_Jail_Buff(i,players,selected):
    while True:
        target=int(input("Select a Target:"))
        if players[target-1].blood<=0:
            print("Player",target,"is already dead")
        elif players[target-1].identity==0:
            print("You can not put sheriff in Jail.")
        elif 68 in players[target-1].buff or 69 in players[target-1].buff or 70 in players[target-1].buff:
            print("Player",target,"is already in jail")
        else:
            break
    players[i].card_m(0,selected)
    players[target-1].buff_m(1,selected)
    print("Player",i+1,"have put",target,"in jail")

def Equipment_Check_Same(i,players,selected):
    temp_list=[]
    for j in range(len(players[i].equip)):
        temp_list.append(card_dict[players[i].equip[j]][4])
    if card_dict[selected][4] in temp_list:
        print("Player",i+1,",you already have same equipment.")
        print("Enter 1 to cancel the action")
        print("Enter 2 to replace your equipment with new card")
        c=int(input(":"))
        if c==2:
            print("You have successful equip",card_dict[selected][0])
            players[i].card_m(0,selected)
            players[i].equip_m(1,selected)
    else:
         print("You have successful equip",card_dict[selected][0])
         players[i].card_m(0,selected)
         players[i].equip_m(1,selected)

def Weapon_Check_Same(i,players,selected):
    if len(players[i].weapon)!=0:
        print("Player",i+1,"You already have one weapon")
        print("Enter 1 to cancel the action")
        print("Enter 2 to replace your weapon with new one")
        c=int(input(":"))
        if c==2:
            print("You have new weapon",card_dict[selected][0])
            players[i].card_m(0,selected)
            players[i].weapon_m(1,selected)
    else:
        print("You have new weapon",card_dict[selected][0])
        players[i].card_m(0,selected)
        players[i].weapon_m(1,selected)
from character_function import *

def Hurt_Action(i,target,players,card_list,wasted_card_list):
    Bart_Cassidy(target,players,card_list)
    El_Gringo(i,target,players)
    if players[target].blood<=0:
        Beer(target,players,wasted_card_list)
        Dead_Action(i,target,players,card_list,wasted_card_list)


def Dead_Action(i,target,players,card_list,wasted_card_list):
    if players[target].blood>0:
        return 0
    identity_list=identity_make_up(len(players))
    print("Player",target+1,"is dead!")
    print("Player",target+1,"'s identity is",identity_list[players[target].identity])
    player_i_ID=identity_list[players[i].identity]
    player_target_ID=identity_list[players[target].identity]
    if player_i_ID=="police" and player_target_ID=="sheriff":
        print("Too bad, Sherriff have kill the police")
        print("He must discard all his card and equipment")
        for j in players[i].card:
            wasted_card_list.append(j)
            players[i].card_m(0,j)
        for j in players[i].equip:
            wasted_card_list.append(j)
            players[i].equip_m(0,j)
        for j in players[i].weapon:
            wasted_card_list.append(j)
            players[i].weapon_m(0,j)
    if player_target_ID=="thief":
        print("Congratulation,player",i+1,"you have elimate a thief")
        print("You can draw three card as your reward")
        players[i].card_m(1,card_list.pop())
        players[i].card_m(1,card_list.pop())
        players[i].card_m(1,card_list.pop())
    x=0
    for j in range(len(players)):
        if players[j].char==14:
            x=1
            break
    if x==1:
        if j==target:
            return 0
        print("Player",j+1,"can stole all the card and equipment from",target+1)
        for k in players[target].card:
            players[j].card_m(1,k)
            players[target].card_m(0,k)
        for k in players[target].equip:
            players[j].equip_m(1,k)
            players[target].equip_m(0,k)
        for k in players[target].weapon:
            players[j].weapon_m(1,k)
            players[target].weapon_m(0,k)
    return 0

    
    

def Damage_Judge(players,target,barrel_used):
    temp_card_list=[]
    barrel=Jourdonnais(target,players)
    if 63 in players[target].equip or 64 in players[target].equip:
        barrel=barrel+1
    else:
        barrel=barrel+0
    print("Player",target+1,"You have",barrel,"Barrel now")
    if barrel_used==1:
        print("You have already use a barrel.")
    if players[target].char==2:
        print("Player",target+1,"Can use Bang as miss.")
        for j in players[target].card:
            if card_dict[j][4]==0 or card_dict[j][4]==1:
                temp_card_list.append(j)
    else:
        for j in players[target].card:
            if card_dict[j][4]==1:
                temp_card_list.append(j)
    print("Player",target+1,"You have ",len(temp_card_list),"Miss! card now.")
    if len(temp_card_list)==0 and barrel_used==1:
        print("So bad,You don't have any method to defend this attack.")
        return -1
    if barrel>0 and (barrel_used!=1 or barrel==2):
        judge_card=Judge(target,players,card_list,wasted_card_list)
        if len(set([13,14,15,16,17,18,19,20,21,22,23,24,25])&set(judge_card))>0:
            print("Doge successful")
            return 999
        else:
            print("Doge falid")
    if len(temp_card_list)>0:
        print("You can play MISS to defence this attack or 999 to loose one blood")
        print("Input a card ID from",temp_card_list)
        choose=int(input(":"))
        if choose ==999:
            print("Player",target+1,"You choose to loose one blood")
            return -1
        players[target].card_m(0,choose)
        temp_card_list.remove(choose)
        print("You have defen successful")
        return 998
    else:
        print("You can't hide from his bullet")
        return -1


    

def Set_Bomb_Buff(i,players):
    players[i].card_m(0,71)
    players[i].buff_m(1,71)
    print("Player",i+1,"You have set up a bomb")

def Set_Jail_Buff(i,players,selected):
    temp_player_list=Alive_Player(players)
    for j in range(len(temp_player_list)):
        if players[j].identity==0 or 68 in players[j].buff or 69 in players[j].buff or 70 in players[j].buff:
            temp_player_list.remove(j)    
    for j in temp_player_list:
        x=temp_player_list.pop()
        x=x+1
        temp_player_list.insert(0,x)
    print("Select a target from",temp_player_list)
    target=int(input(":"))-1        
    players[i].card_m(0,selected)
    players[target].buff_m(1,selected)
    print("Player",i+1,"have put player",target+1,"in jail")

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

def Panic(i,players):
    target=Check_Range_No_Weapon(i,players)
    if len(players[target].card)==0 and len(players[target].equip)==0 and len(players[target].weapon)==0:
        print("Player",target+1,"has no more card")
        return -1
    temp_equip_list=[]
    temp_weapon_list=[]
    for j in players[target].equip:
        temp_equip_list.append(card_dict[j][0])
    for j in players[target].weapon:
        temp_weapon_list.append(card_dict[j][0])
    print("Player",target+1,"have",len(players[target].card),"cards and " ,temp_equip_list,"equipments and",temp_weapon_list,"weapon")
    print("Enter 1 to darw a card or 2 to take a equipment or 3 to take a weapon")
    choose=int(input(":"))
    if choose ==1:
        if len(players[target].card)==0:
            print("players",target+1,"has no more card")
            return -1
        print("Enter 1~",len(players[target].card),"to draw one card.")
        choosed_card=players[target].card[int(input(":"))-1]
        players[target].card_m(0,choosed_card)
        players[i].card_m(1,choosed_card)
        print("You have get",card_dict[choosed_card][0])
        
        return target
    if choose==2:
         if len(players[target].equip)==0:
             print("players",target+1,"has no more equipment")
             return -1
         print("Enter a card ID from",players[target].equip,"to choose a card")
         choosed_card=int(input(":"))
         players[target].equip_m(0,choosed_card)
         players[i].card_m(1,choosed_card)
         print("You have get",card_dict[choosed_card][0])
         return target
    if choose==3:
        if len(players[target].weapon)==0:
            print("players",target+1,"has no more weapon")
            return -1
        print("Enter a card ID from",players[target].weapon,"to choose a card")
        choosed_card=int(input(":"))
        players[target].weapon_m(0,choosed_card)
        players[i].weapon_m(1,choosed_card)
        print("You have get",card_dict[choosed_card][0])
        return target

def Cat_Balou(i,players,wasted_card_list):#ban card
    temp_player_list=Alive_Player(players)
    temp_player_list.remove(i)
    for j in temp_player_list:
        x=temp_player_list.pop()
        x=x+1
        temp_player_list.insert(0,x)
    print("You can pick a target from ",temp_player_list)
    target=int(input(":"))-1

    if len(players[target].card)==0 and len(players[target].equip)==0 and len(players[target].weapon)==0:
        print("Player",target+1,"has no more card")
        return -1
    temp_equip_list=[]
    temp_weapon_list=[]
    for j in players[target].equip:
        temp_equip_list.append(card_dict[j][0])
    for j in players[target].weapon:
        temp_weapon_list.append(card_dict[j][0])
    print("Player",target+1,"have",len(players[target].card),"cards and " ,temp_equip_list,"equipments and",temp_weapon_list,"weapon")
    print("Enter 1 to darw a card or 2 to take a equipment or 3 to take a weapon")
    choose=int(input(":"))
    if choose ==1:
        if len(players[target].card)==0:
            print("players",target+1,"has no more card")
            return -1
        print("Enter 1~",len(players[target].card),"to draw one card.")
        choosed_card=players[target].card[int(input(":"))-1]
        print(card_dict[choosed_card],"Has been ban")
        players[target].card_m(0,choosed_card)
        wasted_card_list.append(choosed_card)
        
        return target
    if choose==2:
         if len(players[target].equip)==0:
             print("players",target+1,"has no more equipment")
             return -1
         print("Enter a card ID from",players[target].equip,"to choose a card")
         choosed_card=int(input(":"))
         players[target].equip_m(0,choosed_card)
         wasted_card_list.append(choosed_card)
         return 0
    if choose==3:
        if len(players[target].weapon)==0:
            print("players",target+1,"has no more weapon")
            return -1
        print("Enter a card ID from",players[target].weapon,"to choose a card")
        choosed_card=int(input(":"))
        players[target].weapon_m(0,choosed_card)
        wasted_card_list.append(choosed_card)
        return 0

def Stagecoach(i,players,card_list):
    print("You can darw two more card")
    players[i].card_m(1,card_list.pop())
    players[i].card_m(1,card_list.pop())
    return 0

def Wells(i,players,card_list):
    print("You can darw three more card")
    players[i].card_m(1,card_list.pop())
    players[i].card_m(1,card_list.pop())
    players[i].card_m(1,card_list.pop())
    return 0
    
def Beer(i,players,wasted_card_list):
    if players[i].blood>0:
        x=players[i].blood+1
        if x>players[i].max_blood:
            print("You had already reach your upper limit")
            return -1
        else:
            print("You have gain 1 blood,your blood is",x,"now")
            players[i].setblood(x)
            return 0
    elif players[i].blood<=0:
        remain_beer=[]
        for j in players[i].card:
            if card_dict[j][4]==7:
                remain_beer.append(j)
        while True:
            print("Player",i+1,"You have already dead now,you have",len(remain_beer),"beer now")
            if players[i].blood>0:
                print("Player",i+1,"You are alive now.")
                print("Player",i+1,"You still have",len(remain_beer),"beer now.")
                return 0
            elif len(remain_beer)==0:
                print("So sad,player",i+1,"you have no more beer,You are sure to be dead.")
                return -1
            elif len(remain_beer)+players[i].blood<=0:
                print("So bad,player",i+1," you don't have enough beer to recovery your life.You are sure to be dead")
                return -1
            else:
                print("Enter a beer card ID from",remain_beer)
                choosed=int(input(":"))
                players[i].blood_m(1)
                remain_beer.remove(choosed)
                players[i].card_m(0,choosed)
                wasted_card_list.append(choosed)
                print("Player",i+1,"You have recover 1 blood,you now have",players[i].blood,"blood now.")

def Saloon(players):
    for j in range(len(players)):
        if players[j].blood<=0:
            print("Player",j+1,"is already dead")
            continue
        elif players[j].blood==players[j].max_blood:
            print("Player",j+1,"'s blood is already full")
            continue
        else:
            players[j].blood_m(1)
            print("Player",j+1,"have",players[j].blood,"blood now")
    return 0

def General_Store(i,players,card_list):
    temp_players_list=Alive_Player(players)
    temp_card_list=[]
    
    for j in temp_players_list:
        temp_card_list.append(card_list.pop())
    for j in range(len(players)):
        print("Now have",len(temp_card_list),"cards to choose.")
        for k in temp_card_list:
            print(k,card_dict[k])
        x=i+j
        if x>=len(temp_players_list):
            x=x-len(temp_players_list)
        print("Player",x+1,"You can pick one card from above")
        choose=int(input(":"))
        temp_card_list.remove(choose)
        print("Player",x+1,"You have get",card_dict[choose])
        players[x].card_m(1,choose)
    return 0

def Miss(i,players):
    #This Miss function used only char is Calamity Janet
    #And it use to act like BANG
    if players[i].bang==1:
        print("You have already use Bang in this round,choose another card")
        return -1
    players[i].setbang(1)
    if 72 in players[i].weapon or 73 in players[i].weapon:
        players[i].setbang(0)
    target=Check_Range_Weapon(i,players)
    print("Player",target+1,"You have been choose as a target.")
    x=Slab_the_Killer(i,players)
    barrel_used=0
    while x>0:
        output=Damage_Judge(players,target,barrel_used)
        if ouptup==999:
            barrel_used=1
        x=x-1
    if output==-1:
        players[target].blood_m(-1)
        Hurt_Action(i,target,players,card_list,wasted_card_list)
        return 0

def Bang(i,players,card_list,wast_card_list):
    if players[i].bang==1:
        print("You have already use Bang in this round,choose another card")
        return -1
    players[i].setbang(1)
    if players[i].char==15 or 72 in players[i].weapon or 73 in players[i].weapon:
        players[i].setbang(0)
    target=Check_Range_Weapon(i,players)
    print("Player",target+1,"You have been choose as a target.")
    x=Slab_the_Killer(i,players)
    barrel_used=0
    while x>0:
        output=Damage_Judge(players,target,barrel_used)
        if output==999:
            barrel_used=1
        x=x-1
    if output==-1:
        players[target].blood_m(-1)
        Hurt_Action(i,target,players,card_list,wasted_card_list)
        return 0
    return 0

def Indians(i,players,card_list,wasted_card_list):
    temp_players=Alive_Player(players)
    for j in temp_players:
        get_hurt=0
        temp_card_list=[]
        if i == j:
            continue
        print("Player",j+1,"you have to play a BANG! card or loose one blood")
        for k in players[j].card:
            if card_dict[k][4]==0:
                temp_card_list.append(k)
        if players[j].char==2:
            for k in players[j].card:
                if card_dict[k][4]==0 or card_dict[k][4]==1:
                    temp_card_list.append(k)
        print("Player",j+1,"You now have",len(temp_card_list),"BANG! card")
        if len(temp_card_list)==0:
            print("To Bad ,you must loose one point of blood")
            players[j].blood_m(-1)
            get_hurt=1
        else:
            print("Player",j+1,"you can enter 1 to play one BANG! or 2 to choose to loose one blood")
            choose=int(input(":"))
            if choose==1:
                print("You choose to play one bang ,enter a ID from",temp_card_list)
                x=int(input(":"))
                players[j].card_m(0,x)
                continue
            elif choose==2:
                print("You choose to loose one blood")
                players[j].blood_m(-1)
                get_hurt=1
        if get_hurt==1:
            Hurt_Action(i,j,players,card_list,wasted_card_list)
    return 0
            
def Gatling(i,players,card_list,wasted_card_list):
    temp_players=Alive_Player(players)
    for j in temp_players:
        get_hurt=0
        temp_card_list=[]
        if i == j:
            continue
        print("Player",j+1,"you have to play a MISS! card or loose one blood")
        if 63 in players[j].equip or 64 in players[j].equip:
            print("Player",j+1,"you can judge first because you have a barrel")
            if len(set([13,14,15,16,17,18,19,20,21,22,23,24,25])&set(Judge(j,players,card_list,wasted_card_list)))>0:
                print("Doge successful")
                continue
            else:
                print("Doge faild")

        for k in players[j].card:
            if card_dict[k][4]==1:
                temp_card_list.append(k)
        if players[j].char==2:
            for k in players[j].card:
                if card_dict[k][4]==0 or card_dict[k][4]==1:
                    temp_card_list.append(k)
        print("Player",j+1,"You now have",len(temp_card_list),"MISS! card")
        if len(temp_card_list)==0:
            print("To Bad ,you must loose one point of blood")
            players[j].blood_m(-1)
            get_hurt=1
        else:
            print("Player",j+1,"you can enter 1 to play one MISS! or 2 to choose to loose one blood")
            choose=int(input(":"))
            if choose==1:
                print("You choose to play one bang ,enter a ID from",temp_card_list)
                x=int(input(":"))
                players[j].card_m(0,x)
                continue
            elif choose==2:
                print("You choose to loose one blood")
                players[j].blood_m(-1)
                get_hurt=1
        if get_hurt==1:
            Hurt_Action(i,j,players,card_list,wasted_card_list)
    return 0

def Duel(i,players,card_list,wasted_card_list):
    temp_players=Alive_Player(players)
    temp_players.remove(i)
    for j in temp_players:
        x=temp_players.pop()
        x=x+1
        temp_players.insert(0,x)
    print("Player",i+1,"You can pick a target to duel from",temp_players)
    target=int(input(":"))-1
    player_i_card=[]
    player_target_card=[]
    for j in players[i].card:
        if players[i].char==2:
            if card_dict[j][4]==0 or card_dict[j][4]==1:
                player_i_card.append(j)
        else:
            if card_dict[j][4]==0:
                player_i_card.append(j)
    for j in players[target].card:
        if players[target].char==2:
            if card_dict[j][4]==0 or card_dict[j][4]==1:
                player_target_card.append(j)
        else:
            if card_dict[j][4]==0:
                player_target_card.append(j)
    temp_dict={i:player_i_card,target:player_target_card}
    print("Player",i+1,"You have ",len(player_i_card),"Bang!")
    print("Player",target+1,"You have ",len(player_target_card),"Bang!")
    print("Begin from player",i+1,"enter 1 to playe one bang card or 999 to loose one blood")
    print("Then turn to player",target+1,"enter 1 to playe one bang card or 999 to loose one blood")
    print("Until one can't play any BANG or stop the duel by his own mind.")
    print("The first one stop the duel loose one blood.")
    while True:
        loser=-1
        for j in [i,target]:
            if len(temp_dict[j])==0:
                print("Player",j+1,"You have no more card.You loose the duel,you must lost one blood.")
                loser=j
                break
            else:
                print("Player",j+1,"You can enter 1 to playe one bang card or 999 to loose one blood")
                choose=int(input(":"))
                if choose==1:
                    print("You choose to play a bang!")
                    x=temp_dict[j].pop()
                    players[j].card_m(0,x)
                    print("Player",j+1,"You have ",len(temp_dict[j]),"BANG! now.")
                else:
                    print("You choose to quick the duel,you will loose one blood")
                    loser=j
                    break
        if loser!=-1:
            break
    print("Player",loser+1,"You have loose the duel,you loose one blood.")
    players[loser].blood_m(-1)
    Hurt_Action(i,loser,players,card_list,wasted_card_list)
    return 0
    
from card_dict import *
def Black_Jack(i,players,card_list):
    players[i].card_m(1,card_list.pop())
    second_card=card_list.pop()
    if card_dict[second_card][2] in [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]:
        players[i].card_m(1,card_list.pop())
    players[i].card_m(1,second_card)
    return card_dict[second_card]

def Jesse_Jones(i,players,card_list):
    print("Player",i+1,"You can draw your first card from ether top of the card stack or from other player's card.")
    print("Input 1 to draw card from top of the card stack.")
    print("Input 2 to draw card from other player's card.")
    mode=int(input(":"))
    if mode==1:
        players[i].card_m(1,card_list.pop())
    elif mode==2:
        print("Pick a player to draw a card.")
        for j in range(len(players)):
            if i==j:
                continue
            print("Player" ,j+1,"have",len(players[j].card),"cards")
        while True:
            target=int(input(":"))
            if players[target-1].vid==0:
                print("Player",target,"is already dead,choose again.")
                continue
            elif len(players[target-1].card)==0:
                print("Player",target,"has no more card,you have to pick another player.")
                continue
            else:
                print("Player" ,target,"have",len(players[target-1].card),"cards,Enter 1 to",len(players[target-1].card),"to pick a card")
                target_card=int(input(":"))
                card_id=players[target-1].card[target_card-1]
                players[target-1].card_m(0,card_id)
                players[i].card_m(1,card_id)
                print("You have get card",card_dict[card_id])
                break
    players[i].card_m(1,card_list.pop())

def Suzy_Lafayette(i,players,card_list):
    for i in range(len(players)):
        if players[i].char==13:
            break
    if len(players[i].card)==0:
        players[i].card_m(1,card_list.pop())

def Kit_Carlson(i,players,card_list):
    card_temp=[]
    card_temp.append(card_list.pop())
    card_temp.append(card_list.pop())
    card_temp.append(card_list.pop())
    print("You can choose two card from",card_dict[card_temp[0]],
          "and",card_dict[card_temp[1]],"and",card_dict[card_temp[2]],
          "Enter 1~3 to put card back to the card_stack.")
    card_back_id=card_temp[int(input(":"))-1]
    card_temp.remove(card_back_id)
    card_list.append(card_back_id)
    players[i].card_m(1,card_temp.pop())
    players[i].card_m(1,card_temp.pop())

def Pedro_Ramirex(i,players,card_list,wasted_card_list):
    print("You can draw your first card from ether top of the card stack or from the wasted_card_stack.")
    print("Input 1 to draw card from top of the card stack.")
    print("Input 2 to draw card from the wasted_card_stack.")
    mode=int(input(":"))
    if mode==1:
        players[i].card_m(1,card_list.pop())
    elif mode==2:
        if len(wasted_card_list)>0:
            players[i].card_m(1,wasted_card_list.pop())
        else:
            print("Wasted_card_Stack is empty.Draw from Card_stack.")
            players[i].card_m(1,card_list.pop())
    players[i].card_m(1,card_list.pop())
# darw card


def Suzy_Lafayette(i,players,card_list):
    if players[i].identity==13:
        if len(players[i].card)==0:
            print("Players ",i,"You have no more card. Basic on Your character ,you can draw one card")
            players[i].card_m(1,card_list.pop())

def Calamity_Janet(i,players,selected):
    if players[i].identity==2 and card_dict[selested][4]==1:
        return 1
    return 0

def Slab_the_Killer(i,players):
    if players[i].identity==12:
        return 2
    return 1

def Jourdonnais(i,players):
    if players[i].identity==5:
        return 1
    return 0
"""
def Paul Regret
def Rose Doolan
"""



from card_dict import *


def Player_numbers():
    while True:
        try:
            person=int(input("input players number,from 4~8:"))
        except:
            print("Please enter number")
            continue
        if person <= 8 and person >= 4:
            print("Players number are",person)
            identity_list.extend(list(range(person)))
            return person
        else:
            print("number not accept")
    

def Set_identity(person,players,identity_list):
    identity_dict=identity_make_up(person)
    for i in range(person):
        players[i].setid(identity_list.pop())
        print("Player",i+1,"'s identity is",identity_dict[players[i].identity])

def Set_character(person,players,character_list):        
    for i in range(person):
        c1=character_list.pop()
        c2=character_list.pop()
    
        print("Player",i+1,"You have to choose one character from",c1,char_dict[c1][0],"and",c2,char_dict[c2][0])
        print(char_dict[c1][0],"'s abality is",char_dict[c1][1]," Life is",char_dict[c1][2])
        print(char_dict[c2][0],"'s abality is",char_dict[c2][1]," Life is",char_dict[c2][2])
        while True:
            x=int(input(":"))
            if x==c1 or x==c2:
                print("You have choses",char_dict[x][0]," for your character.")
                players[i].setchar(x)
                break
            else:
                print("You must choses from",char_dict[c1][0],"and",char_dict[c2][0])
                continue

    for i in range(person):
        print("Player",i+1,"'s character is",char_dict[players[i].char][0])
        print("The ability is.......",char_dict[players[i].char][1])

def Set_blood(person,players):

    for i in range(person):
        x=0
        if players[i].identity==0:
            x=1
        x=x+char_dict[players[i].char][2]
        players[i].setmax_blood(x)
        players[i].setblood(x)
        print("Player",i+1,",you have",x,"/",x,"points of blood at the begin")

def Set_card(person,players,card_list):
    for i in range(person):
        for j in range(players[i].blood):
            players[i].card_m(1,card_list.pop())
    
        print("Player",i+1,"you have",players[i].card,"cards")


"""
0:attack
1:function
2:equip
3:buff
            0,1,2,3,4,5,6,7,8,9,10,11,12
0~12:Spades[A,2,3,4,5,6,7,8,9,10,J,Q,K]

            13141516171819202122 232425
13~25:Heart[A,2,3,4,5,6,7,8,9,10,J,Q,K]

              26272829303132333435 363738
26~38:dimanod[A,2,3,4,5,6,7,8,9,10,J,Q,K]

           39404142434445464748 495051
39~51:club[A,2,3,4,5,6,7,8,9,10,J,Q,K]
"""

#Global Used Function

def Gameover_Check(players):
    while True:
        flag_t=0
        win=0
        if len(players)<8:
            for i in range(len(players)):
                if players[i].identity==len(players)-1 and players[i].blood<=0:
                    flag_t=1
                if players[i].identity!=len(players)-1 and players[i].blood>0:
                    flag_t=1
            if flag_t==0:
                win=2 
                break
        else:
            for i in range(8):
                if players[i].identity<6 and players[i].blood>0:
                    flag_t=1
                if flag_t==0: 
                    if players[i].identity==6 and players[i].blood>0:
                        for j in range(8):
                            if players[j].identity==7 and players[j].blood<=0:
                                flag_t=6
                    if players[i].identity==7 and players[i].blood>0:
                        for j in range(8):
                            if players[j].identity==6 and players[j].blood<=0:
                                flag_t=7
            if flag_t==6:
                win=3
                break
            if flag_t==7:
                win=4
                break
        for i in range(len(players)):
            if players[i].identity==0 and players[i].blood<=0:
                win=1    
                break
        if win==1:
            break  
        flag_p=0    
        if len(players)==4:
            for i in range(len(players)):
                if players[i].identity>0 and players[i].blood>0:
                    flag_p=1         
        elif len(players)<7:
            for i in range(len(players)):
                if players[i].identity>1 and players[i].blood>0:
                    flag_p=1 
        else:            
            for i in range(len(players)):   
                if players[i].identity>2 and players[i].blood>0:
                    flag_p=1 
        if flag_p==0:
            win=5
            break
        if win!=0:
            break
    
    if win==1:
        return "Game over, thief win"
    elif win==2:
        return "Game over, traitor win"
    elif win==3:
        return "Game over, traitor1 win"  
    elif win==4:
        return "Game over, traitor2 win"
    elif win==5:         
        return "Game over, police win"
    else:
        return 0

def Judge(x,players,card_list,wasted_card_list):
    if players[x].char==7:
        wasted_card_list.append(card_list.pop())
        wasted_card_list.append(card_list.pop())
        return [wasted_card_list[-1],wasted_card_list[-2]]
    else:
        wasted_card_list.append(card_list.pop())
        return [wasted_card_list[-1]]

def Alive_Player(players):
    temp_player_list=[]
    for i in range(len(players)):
        if players[i].blood>0:
            temp_player_list.append(i)
    return temp_player_list

def Check_Range_No_Weapon(i,players):  
    temp_players_list=Alive_Player(players)
    temp_list=[]
    
    for j in temp_players_list:
        if i ==j:
            continue
        x=min(abs(temp_players_list.index(i)-temp_players_list.index(j)),len(temp_players_list)-abs(temp_players_list.index(i)-temp_players_list.index(j)))
        
        if 65 in players[i].equip:
            x=x-1
        if 66 in players[j].equip or 67 in players[j].equip:
            x=x+1
        if players[i].identity==10:
            x=x-1
        if players[j].identity==8:
            x=x+1
        if x<=1:
            temp_list.append(j)
    if len(temp_list)==0:
        print("Everyone is out of your range, play another card or force end the round")
        return -1
    t_temp_list=[]
    for k in temp_list:
        t_temp_list.append(k+1)
    print("Pick a Target from",t_temp_list)
    x=int(input(":"))
    if x in t_temp_list:
        print("You have choose player",x,"as your target.")
        return x-1

def Check_Range_Weapon(i,players):  
    temp_players_list=Alive_Player(players)
    temp_list=[]
    
    for j in temp_players_list:
        if i ==j:
            continue
        x=min(abs(temp_players_list.index(i)-temp_players_list.index(j)),abs(len(temp_players_list)-(temp_players_list.index(i)-temp_players_list.index(j))))
        
        if 65 in players[i].equip:
            x=x-1
        if 66 in players[j].equip or 67 in players[j].equip:
            x=x+1
        if players[i].identity==10:
            x=x-1
        if players[j].identity==8:
            x=x+1
        if len(players[i].weapon)==0:
            x=x-1
        elif card_dict[players[i].weapon[0]][4]==13:
            x=x-2
        elif card_dict[players[i].weapon[0]][4]==77:
            x=x-3
        elif card_dict[players[i].weapon[0]][4]==78:
            x=x-4
        elif card_dict[players[i].weapon[0]][4]==79:
            x=x-5
        
        
        if x<=0:
            temp_list.append(j)
    if len(temp_list)==0:
        print("Everyone is out of your range, play another card or force end the round")
        return -1
    for j in temp_list:
        t_temp_list.append(j+1)
    print("Pick a Target from",t_temp_list)
    x=int(input(":"))
    if x in t_temp_list:
        print("You have choose player",x,"as your target.")
        return x-1



class player():
    def __init__(self,pid):
        self.pid=pid
        self.identity=-1
        self.char=-1
        self.max_blood=-1
        self.blood=-1
        self.card=[]
        self.equip=[]
        self.weapon=[]
        self.buff=[]
        self.vid=1
        self.bang=0
    def setbang(self,x):
        self.bang=x
    def setid(self,id):
        self.identity=id
    def setchar(self,char):
        self.char=char
    def setmax_blood(self,max_blood):
        self.max_blood=max_blood
    def setblood(self,blood):
        self.blood=blood
    def blood_m(self,x):
        self.blood=self.blood+x
    def card_m(self,mode,id):
        if mode==1:
            self.card.append(id)
        else :
            self.card.remove(id)
            return
    def equip_m(self,mode,id):
        if mode==1:
            self.equip.append(id)
        else :
            self.equip.remove(id)
    def weapon_m(self,mode,id):
        if mode==1:
            self.weapon.append(id)
        else :
            self.weapon.remove(id)        
    def buff_m(self,mode,id):
        if mode==1:
            self.buff.append(id)
        else :
            self.buff.remove(id)
    def vid_m(self):
        if self.blood<=0:
            self.vid=0
    def print_status(self):
        print(self.pid,self.identity,self.char,self.max_blood,self.blood,self.card,self.equip,self.buff)        

person=int()

identity_list=[]
character_list=list(range(16))
card_list=list(range(80))
wasted_card_list=[]
players=[]


card_dict={0:["Bang!,Range=1",0,0,"attack a player",0],
           1:["Bang!,Range=1",0,13,"attack a player",0],
           2:["Bang!,Range=1",0,24,"attack a player",0],
           3:["Bang!,Range=1",0,25,"attack a player",0],
           4:["Bang!,Range=1",0,26,"attack a player",0],
           5:["Bang!,Range=1",0,27,"attack a player",0],
           6:["Bang!,Range=1",0,28,"attack a player",0],
           7:["Bang!,Range=1",0,29,"attack a player",0],
           8:["Bang!,Range=1",0,30,"attack a player",0],
           9:["Bang!,Range=1",0,31,"attack a player",0],
           10:["Bang!,Range=1",0,32,"attack a player",0],
           11:["Bang!,Range=1",0,33,"attack a player",0],
           12:["Bang!,Range=1",0,34,"attack a player",0],
           13:["Bang!,Range=1",0,35,"attack a player",0],
           14:["Bang!,Range=1",0,36,"attack a player",0],
           15:["Bang!,Range=1",0,37,"attack a player",0],
           16:["Bang!,Range=1",0,38,"attack a player",0],
           17:["Bang!,Range=1",0,40,"attack a player",0],
           18:["Bang!,Range=1",0,41,"attack a player",0],
           19:["Bang!,Range=1",0,42,"attack a player",0],
           20:["Bang!,Range=1",0,43,"attack a player",0],
           21:["Bang!,Range=1",0,44,"attack a player",0],
           22:["Bang!,Range=1",0,45,"attack a player",0],
           23:["Bang!,Range=1",0,46,"attack a player",0],
           24:["Bang!,Range=1",0,47,"attack a player",0],
           25:["MISS!",1,1,"counter a Bang!",1],
           26:["MISS!",1,2,"counter a Bang!",1],
           27:["MISS!",1,3,"counter a Bang!",1],
           28:["MISS!",1,4,"counter a Bang!",1],
           29:["MISS!",1,5,"counter a Bang!",1],
           30:["MISS!",1,6,"counter a Bang!",1],
           31:["MISS!",1,7,"counter a Bang!",1],
           32:["MISS!",1,39,"counter a Bang!",1],
           33:["MISS!",1,48,"counter a Bang!",1],
           34:["MISS!",1,49,"counter a Bang!",1],
           35:["MISS!",1,50,"counter a Bang!",1],
           36:["MISS!",1,51,"counter a Bang!",1],
           37:["Gatling",0,22,"attack other players",37],
           38:["Indians!",0,26,"call the Indians to attack other players,they can use a Bang! to defeat Indians or lose one health",2],
           39:["Indians!",0,38,"call the Indians to attack other players,they can use a Bang! to defeat Indians or lose one health",2],
           40:["Panic!",1,23,"pick a card from a player at range 1",3],
           41:["Panic!",1,24,"pick a card from a player at range 1",3],
           42:["Panic!",1,18,"pick a card from a player at range 1",3],
           43:["Panic!",1,33,"pick a card from a player at range 1",3],
           44:["Ban card",1,25,"let a player discard a card",4],
           45:["Ban card",1,34,"let a player discard a card",4],
           46:["Ban card",1,35,"let a player discard a card",4],
           47:["Ban card",1,36,"let a player discard a card",4],
           48:["Two more",1,8,"draw 2 cards",5],
           49:["Two more",1,8,"draw 2 cards",5],
           50:["Three more",1,15,"draw 3 cards",50],
           51:["Store",1,11," reveal as many cards from the deck face up as the players still playing.Starting with you and proceeding clockwise, each player chooses one of those cards and puts it in his hand.",6],
           52:["Store",1,47," reveal as many cards from the deck face up as the players still playing.Starting with you and proceeding clockwise, each player chooses one of those cards and puts it in his hand.",6],
           53:["Beer",1,18,"restore 1 health",7],
           54:["Beer",1,19,"restore 1 health",7],
           55:["Beer",1,20,"restore 1 health",7],
           56:["Beer",1,21,"restore 1 health",7],
           57:["Beer",1,22,"restore 1 health",7],
           58:["Beer",1,23,"restore 1 health",7],
           59:["all health +1",1,17,"restore 1 health to every players",59],
           60:["Duel",0,10,"you can choose a player to duel with you,he can use a Bang! to fight back,until one of them can't use the Bang! and lose one health.",8],
           61:["Duel",0,37,"you can choose a player to duel with you,he can use a Bang! to fight back,until one of them can't use the Bang! and lose one health.",8],
           62:["Duel",0,46,"you can choose a player to duel with you,he can use a Bang! to fight back,until one of them can't use the Bang! and lose one health.",8],
           63:["Barrel",2,11,"Draw when you are attacked by Bang!. If it is a heart, then the attack misses",9],
           64:["Barrel",2,12,"Draw when you are attacked by Bang!. If it is a heart, then the attack misses",9],
           65:["attack range -1",2,0,"You see others range -1",65],
           66:["def range +1",2,20,"others see you range -1",10],
           67:["def range +1",2,21,"others see you range -1",10],
           68:["Jail",3,9,"Draw! at the beginning of your turn. If it is a heart,you are free",11],
           69:["Jail",3,10,"Draw! at the beginning of your turn. If it is a heart,you are free",11],
           70:["Jail",3,16,"Draw! at the beginning of your turn. If it is a heart,you are free",11],
           71:["BOMB!",3,14,"Draw! at the beginning of your turn. If the drawn card is a 2-9 of spades,you lose three health,else, you give the bomb to the next player",71],
           72:["Multi-Bang!",2,9,"you can use several Bang! cards in one turn if you want",12],
           73:["Multi-Bang!",2,48,"you can use several Bang! cards in one turn if you want",12],
           74:["range+2",2,12,"your attack range become 2",13],
           75:["range+2",2,49,"your attack range become 2",13],
           76:["range+2",2,50,"your attack range become 2",13],
           77:["range+3",2,51,"your attack range become 3",77],
           78:["range+4",2,39,"your attack range become 4",78],
           79:["range+5",2,7,"your attack range become 5",79]
           }
attack_card={-1:["Damage=int","Range 0=self,999=all","target=int,999=all","Function","Character effect"],
             0:[1,1,"input","Bang function",[0,2,3,5,7,8,10,12,15]],
             8:[1,999,"input","Duel function",[0,2,3,12]],
             37:[1,999,999,"Galting function",[0,2,5,7]],
             2:[1,999,999,"Indian function",[0,2]]
             }

function_card={-1:["Range0=self,999=all","target,0=self,999=all","function"],
               1:[999,999,"defect bang!"],
               7:[0,0,"Beer Function"],
               4:[999,"input","Dis-others-card Function"],
               3:[1,"input","Darw-others-card Function"],
               5:[0,0,"Darw-two more card"],
               50:[0,0,"Darw-two more card"],
               59:[999,999,"all life +1"],
               6:[999,999,"all card+1"]
               }
equip_card={-1:["only=0or1","attack range[0,-1]","defense range[0,1]","weapon range","function"],
            9:[0,0,0,0,"barrel function"],
            65:[0,-1,0,0,"n/a"],
            10:[0,0,1,0,"n/a"],
            12:[1,0,0,0,"multi-bang function"],
            13:[1,0,0,2,"n/a"],
            77:[1,0,0,3,"n/a"],
            78:[1,0,0,4,"n/a"],
            79:[1,0,0,5,"n/a"]
            }
buff_card={-1:["target check function"],
           11:["Jail buff on function"],
           71:["bomb buff on function"]
           }

char_dict={0:["Bart Cassidy","you can draw one card each time you lose one blood",4],
           1:["Black Jack","You must show your second_draw card ,if the color is red,you can darw another card",4],
           2:["Calamity Janet","Bang!=Miss",4],
           3:["El Gringo","You can darw one card from the attacker each time you lose one point of blood",3],
           4:["Jesse Jones","The first card you darw, You can reather darw from the card_stack or any player.",4],
           5:["Jourdonnais","Self-barrel",4],
           6:["Kit Carlson","Draw three,return one",4],
           7:["Lucky Duke","Draw two and pick one as your judge",4],
           8:["Paul Regret","def range +1",3],
           9:["Pedro Ramirex","The first card you darw, You can reather darw from the card_stack or wasted card stack.",4],
           10:["Rose Doolan","attack range -1",4],
           11:["Sid Ketchum","You can discard two card and return one blood at any time.",4],
           12:["Slab the Killer","Target need to wasted two MISS! to defend his Bang!",4],
           13:["Suzy Lafayette","Draw one card if you don't have any card when you are not in action",4],
           14:["Vulture Sam","Stole every card and equip when player dead.",4],
           15:["Willy The Kid","Multi-Bang!",4],
           -1:["Test","Test",2]
            }
sheriff="sheriff"
police="police"
thief="thief"
traitor="traitor"
def identity_make_up(person):
    if person==4:
        return {0:sheriff,1:thief,2:thief,3:traitor}
    elif person==5:
        return {0:sheriff,1:police,2:thief,3:thief,4:traitor}
    elif person==6:
        return {0:sheriff,1:police,2:thief,3:thief,4:thief,5:traitor}
    elif person==7:
        return {0:sheriff,1:police,2:police,3:thief,4:thief,5:thief,6:traitor}
    elif person==8:
        return {0:sheriff,1:police,2:police,3:thief,4:thief,5:thief,6:traitor,7:traitor}

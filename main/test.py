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

def Gameover_Check(players):
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
        if flag_t==7:
            win=4
    for i in range(len(players)):
        if players[i].identity==0 and players[i].blood<=0:
            win=1      
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






players=[]
for i in range(4):
    players.append(player(i))
players[0].setid(0)
players[1].setid(1)
players[2].setid(2)
players[3].setid(3)

players[0].setblood(0)
players[1].setblood(0)
players[2].setblood(0)
players[3].setblood(1)



print(Gameover_Check(players))

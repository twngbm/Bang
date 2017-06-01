import tkinter as tk
from PIL import Image, ImageTk,ImageDraw,ImageFont
from card_dict import *
import action,game_init
def generate_scene():
    master=tk.Tk()
    master.minsize(1080, 720)
    master.maxsize(1080, 720)
    master.title("BANG!")
    return master
class guide_scene:
    def __init__(self,master):
        self.master=master
        back=Image.open("bg_ex.jpg")
        draw=ImageDraw.Draw(back)
        draw.text((390,50),"View Cards",font=(ImageFont.truetype("arial.ttf", 35)))
        bg=ImageTk.PhotoImage(back)
        self.bg_panel=tk.Label(self.master,image=bg)
        self.bg_panel.image=bg
        self.bg_panel.place(x=0,y=0)
        self.back=tk.Button(self.master,text="BACK",command=self.callback_back,width=10,height=4)
        self.back.place(x=700,y=600)
    def callback_back(self):
        intro_scene(self.master)    
class victory_scene:
    def __init__(self,master):
        self.master=master 
        back=Image.open("bg_ex.jpg")
        draw=ImageDraw.Draw(back)
        win_str=action.Gameover_Check(players)
        draw.text((180,50),win_str,font=(ImageFont.truetype("arial.ttf", 35)))
        bg=ImageTk.PhotoImage(back)
        self.bg_panel=tk.Label(self.master,image=bg)
        self.bg_panel.image=bg  
        self.bg_panel.place(x=0,y=0)
        self.back=tk.Button(self.master,text="BACK",command=self.callback_back,width=10,height=4)
        self.back.place(x=700,y=600)
    def callback_back(self):
        intro_scene(self.master)    
class setting_scene:
    def __init__(self,master):
        self.master=master
        # bg = ImageTk.PhotoImage(Image.open("bg_ex.jpg"))
        back=Image.open("bg_ex.jpg")
        draw=ImageDraw.Draw(back)
        draw.text((390,50),"How many players?",font=(ImageFont.truetype("arial.ttf", 35)))
        bg=ImageTk.PhotoImage(back)
        self.bg_panel=tk.Label(self.master,image=bg)
        self.bg_panel.image=bg
        self.bg_panel.place(x=0,y=0)
        #T=tk.Label(self.master,text="How many players?",font=(None,30),bg="white")
        #T.place(x=390,y=50)
        self.b1=tk.Button(self.master,text="4",command=self.callback_b1,width=10,height=4)
        self.b2=tk.Button(self.master,text="5",command=self.callback_b2,width=10,height=4)
        self.b3=tk.Button(self.master,text="6",command=self.callback_b3,width=10,height=4)
        self.b4=tk.Button(self.master,text="7",command=self.callback_b4,width=10,height=4)
        self.b5=tk.Button(self.master,text="8",command=self.callback_b5,width=10,height=4)
        self.back=tk.Button(self.master,text="BACK",command=self.callback_back,width=10,height=4)
        self.b5.place(x=500,y=600)
        self.b4.place(x=500,y=550)
        self.b3.place(x=500,y=500)
        self.b2.place(x=500,y=450)
        self.b1.place(x=500,y=400)
        self.back.place(x=700,y=600)
    def callback_b1(self):
        person=4
        for j in range(person):
            players.append(player(j))
        identity_list.extend(list(range(person)))
        random.shuffle(identity_list)
        self.gotoidchar()
    def callback_b2(self):
        person=5
        for j in range(person):
            players.append(player(j))
        identity_list.extend(list(range(person)))
        random.shuffle(identity_list)
        self.gotoidchar()
    def callback_b3(self):
        person=6
        for j in range(person):
            players.append(player(j))
        identity_list.extend(list(range(person)))
        random.shuffle(identity_list)
        self.gotoidchar()
    def callback_b4(self):
        person=7
        for j in range(person):
            players.append(player(j))
        identity_list.extend(list(range(person)))
        random.shuffle(identity_list)
        self.gotoidchar()
    def callback_b5(self):
        person=8
        for j in range(person):
            players.append(player(j))
        identity_list.extend(list(range(person)))
        random.shuffle(identity_list)
        self.gotoidchar()   
    def callback_back(self):
        intro_scene(self.master)
    def gotoidchar(self):
        idchar_scene(self.master,0)
class game_scene: 
    def __init__(self,master):     
        self.master=master 
        back=Image.open("bg_ex.jpg")
        draw=ImageDraw.Draw(back)
        draw.text((180,50),"during GAME",font=(ImageFont.truetype("arial.ttf", 35)))
        bg=ImageTk.PhotoImage(back)
        self.bg_panel=tk.Label(self.master,image=bg)
        self.bg_panel.image=bg  
        self.bg_panel.place(x=0,y=0)
        game_init.Set_blood(len(players),players)
        game_init.Set_card(len(players),players,card_list)
        for j in range(len(players)):
            players[j].print_status()
class idchar_scene:
    def __init__(self,master,playerid):
        self.i=playerid
        self.master=master
        self.person=len(players)
        players[self.i].setid(identity_list.pop())
        back=Image.open("bg_ex.jpg")
        identity_dict=identity_make_up(len(players))
        draw=ImageDraw.Draw(back)
        draw.text((180,50),"Player "+str(self.i+1)+" Check your identity and select your character!",font=(ImageFont.truetype("arial.ttf", 35)))
        bg=ImageTk.PhotoImage(back)
        self.bg_panel=tk.Label(self.master,image=bg)
        self.bg_panel.image=bg
        self.bg_panel.place(x=0,y=0)
        self.c1=character_list.pop()
        self.c2=character_list.pop()
        T=tk.Label(self.master,text="Your identity is "+identity_dict[players[self.i].identity],font=(None,30),bg="white")
        T.place(x=200,y=300)
        id_card = ImageTk.PhotoImage(Image.open("card_ex.jpg"))
        self.idcardp=tk.Label(self.master,image=id_card)
        self.idcardp.image=id_card
        self.idcardp.place(x=700,y=200)
        self.choice1=tk.Button(self.master,text=str(char_dict[self.c1][0]+"\n"+char_dict[self.c1][1]),command=lambda: self.choose1(self.i)) 
        self.choice2=tk.Button(self.master,text=str(char_dict[self.c2][0]+"\n"+char_dict[self.c2][1]),command=lambda: self.choose2(self.i))
        self.choice1.place(x=50,y=500)  
        self.choice2.place(x=50,y=600)
        char_card1 = ImageTk.PhotoImage(Image.open("card_ex.jpg"))
        self.card1=tk.Label(self.master,image=id_card)
        self.card1.image=id_card
        self.card1.place(x=700,y=380)
        char_card2 = ImageTk.PhotoImage(Image.open("card_ex.jpg"))
        self.card2=tk.Label(self.master,image=id_card)
        self.card2.image=id_card
        self.card2.place(x=700,y=550) 
    def choose1(self,i):
        players[i].setchar(self.c1)
        if i==self.person-1:
            game_scene(self.master)
        else:
            idchar_scene(self.master,i+1)     
    def choose2(self,i):
        players[i].setchar(self.c2)
        if i==self.person-1:
            game_scene(self.master)
        else:
            idchar_scene(self.master,i+1)     
                            
class intro_scene:   
    def __init__(self,master):
        self.master= master
        #bg = ImageTk.PhotoImage(Image.open("bg_ex.jpg"))
        #logo = ImageTk.PhotoImage(Image.open("logo_ex.png"))
        back=Image.open("bg_ex.jpg")
        front=Image.open("logo_ex.png")
        back.paste(front, (90, 130), front)
        bg=ImageTk.PhotoImage(back)
        self.bg_panel=tk.Label(self.master,image=bg)
        self.bg_panel.image=bg
        self.bg_panel.place(x=0,y=0)
        self.start=tk.Button(self.master,text="GUIDE",command=self.goguide,width=10,height=4)
        self.start.place(x=350,y=550)
        self.start=tk.Button(self.master,text="START",command=self.gotosetting,width=10,height=4)
        self.start.place(x=450,y=550)
        self.q=tk.Button(self.master,text="QUIT",command=self.close,width=10,height=4)
        self.q.place(x=550,y=550)
        
    def close(self):
        self.master.destroy()
    def goguide(self):
        guide_scene(self.master)        
    def gotosetting(self):
        setting_scene(self.master)            
root=generate_scene()
intro_scene(root)
root.mainloop()
from tkinter import *
from tkinter import ttk
import socket
import time
import math

root=Tk()
root.geometry('700x600')
root.title('mount etna')

main_frame=Frame(root)
main_frame.place(x=10, y=30)

my_canvas=Canvas(main_frame)
my_canvas.place(x=10, y=30)

c=socket.socket()
percentage_of_exploding=10
modes=["safe mode", "danger mode", "warning mode"]
mode_chooser=0
changer=0
changer2=0
changer3=0
changer4=0
integer=0
percentage_text=["one", "two"]
mode=["oneone", "twotwo"]
news_names=["uno", "dos", "tres", "quatro", "sinco", "seis", "siete", "ocho"]
position_news=75
deleter=0
deleter2=0
destroy_label=0
destroy_label1=0
bad_label=0
logged_account=False
buisniss_names_list=[]

def main():
    global changer3
    global changer4
    global changer2
    def changer3l():
        global changer3
        global changer
        changer3=0
        changer=1
    def statistics():
        def statisitcs_destroyer():
            global changer
            global percentage_text
            global integer
            back1.destroy()
            percentage_text[integer-1].destroy()
            mode[integer-1].destroy()
            main()
            changer=0
        global changer
        global modes
        global mode_chooser
        global changer2
        global changer3
        global changer4
        global integer
        global percentage_text
        global mode
        if changer3!=1:
            changer3=1
            changer=1
        if changer==1:            
            c.send(bytes("rqst_sts", 'utf-8'))
            percentage_of_exploding=int(c.recv(3).decode())
            if percentage_of_exploding<30:
                mode_chooser=0
            if percentage_of_exploding>30 and percentage_of_exploding>60:
                mode_chooser=2
            if percentage_of_exploding>60:
                mode_chooser=1
            percentage_text[integer]=Label(root, font=("Arial",40), text="percentage of exploding: " + str(percentage_of_exploding) + "%")
            percentage_text[integer].place(x=10, y=70)
            mode[integer]=Label(root, font=("Arial",40), text="level of danger: " + modes[mode_chooser])
            mode[integer].place(x=10, y=120)
            mountain_statistics.destroy()
            mountan_accouts.destroy()
            mountain_news.destroy()
            mountain_buisnesses.destroy()
            back1 = Button(root, text='back', width=15, height=3, bd='10', command=statisitcs_destroyer)
            back1.place(x=10,y=10)
            if integer==1:
                integer=-1
            if changer2==1:
                changer2=0
                back1.destroy()
                percentage_text[integer-1].destroy()
                mode[integer-1].destroy()
            root.after(1000, statistics)
            changer4=1
            changer2=1
            integer=integer+1
    def news():
        def news_destroyer():
            for i in range(news_getter):
                news_names[i].destroy()
            back2.destroy()
            main()
        global news_names
        global position_news
        c.send(bytes("rqst_nws", 'utf-8'))
        news_getter=int(c.recv(1).decode())
        mountain_news.destroy()
        mountain_statistics.destroy()
        mountain_buisnesses.destroy()
        mountan_accouts.destroy()
        position_news=75
        for i in range(news_getter):
            len_len_news=int(c.recv(1).decode())
            len_news=int(c.recv(len_len_news).decode())
            news_getter1=str(c.recv(len_news).decode())
            news_names[i]=Label(root, font=("Arial",20), text=news_getter1)
            news_names[i].place(x=10, y=position_news)
            position_news=position_news+30
        back2=Button(root, text='Back', width=15, height=3, bd='10', command=news_destroyer)
        back2.place(x=10, y=10)
    def buisnesses():
        def buisniss_delete2():
            for i in range(18):
                buisniss_names_list[i].destroy()
            return
        def buisniss_printout():
            c.send(bytes("rqst_bna", "utf-8"))
            buisniss_names_list.clear()
            for repeater in range(18): #####################################
                len_len_name=c.recv(1).decode()
                len_len_name=int(len_len_name)
                len_name=int(c.recv(len_len_name).decode())
                name=c.recv(len_name).decode()
                if name!="":
                    buisniss_names_list.append(name)
                else:
                    buisniss_names_list.append(" ")
            bx=10
            by=80
            for printing in range(18):
                buisniss_names_list[printing]=Label(root, font=("Arial",30), text=str(buisniss_names_list[printing]))
                buisniss_names_list[printing].place(x=bx, y=by)
                by=by+40
                if printing==8:
                    bx=260
                    by=80
            return
        def buisniss_next():
            c.send(bytes("next", "utf-8"))
            buisniss_delete2()
            buisniss_printout()
            return
        def buisniss_delete():
            back4.destroy()
            next_button.destroy()
            for i in range(18):
                buisniss_names_list[i].destroy()
            main()
        global buisniss_names_list
        mountain_news.destroy()
        mountain_statistics.destroy()
        mountain_buisnesses.destroy()
        mountan_accouts.destroy()
        back4=Button(root, text='Back', width=15, height=3, bd='10', command=buisniss_delete)
        back4.place(x=10, y=10)
        next_button = Button(root, text='next', width=15, height=3, bd='10', command=buisniss_next)
        next_button.place(x=190,y=10)
        buisniss_printout()
    def accounts():
        global deleter
        def accounts_destroyer():
            global deleter
            back.destroy()
            email_label.destroy()
            email_entry.destroy()
            password_entry.destroy()
            password_label.destroy()
            new_account1.destroy()
            new_account2.destroy()
            enter.destroy()
            main()
        def new_account():
            def account_destroyer():
                enteremail.destroy()
                enteremail_entry.destroy()
                enterpassword1.destroy()
                enterpassword2.destroy()
                enterpassword2_entry.destroy()
                enterpassword1_entry.destroy()
                enterbuisnissname.destroy()
                enterbuisnissname_entry.destroy()
                back3.destroy()
                enter2.destroy()
                main()
            def new_account_considaration():
                npassword1=enterpassword1_entry.get()
                len_len_npassword=len(npassword1)
                len_npassword=len(str(len_len_npassword))
                npassword2=enterpassword2_entry.get()
                nemail=enteremail_entry.get()
                nenterbuisnissname=enterbuisnissname_entry.get()
                len_nenterbuisnissname=len(nenterbuisnissname)
                len_len_nenterbuissnisname=len(str(len_nenterbuisnissname))
                if npassword1==npassword2 and npassword2!="" and nenterbuisnissname!="":
                    len_nemail=len(nemail)
                    c.send(bytes("rqstnacu", "utf8"))
                    c.send(bytes(str(len_nemail), "utf-8"))
                    c.send(bytes(str(nemail), "utf8"))
                    #####
                    c.send(bytes(str(len_len_nenterbuissnisname), "utf-8"))
                    c.send(bytes(str(len_nenterbuisnissname), "utf-8"))
                    c.send(bytes(str(nenterbuisnissname), "utf-8"))
                    ###
                    c.send(bytes(str(len_npassword), "utf-8"))
                    print("now:", len_len_npassword)
                    c.send(bytes(str(len_len_npassword), "utf-8"))
                    print("1len", len_npassword)
                    c.send(bytes(str(npassword1), "utf-8"))
            global bad_label
            global deleter
            email_label.destroy()
            email_entry.destroy()
            password_entry.destroy()
            password_label.destroy()
            new_account1.destroy()
            new_account2.destroy()
            back.destroy()
            enter.destroy()
            enteremail=Label(root, font=("Arial",15), text="Enter email:")
            enteremail.place(x=15, y=80)
            enteremail_entry=Entry(root)
            enteremail_entry.place(x=135, y=80)
            enterpassword1=Label(root, font=("Arial",15), text=" Enter password:")
            enterpassword1.place(x=10, y=160)
            enterpassword1_entry=Entry(root)
            enterpassword1_entry.place(x=150, y=160)
            enterpassword2=Label(root, font=("Arial",15), text=" Enter password:")
            enterpassword2.place(x=10, y=200)
            enterpassword2_entry=Entry(root)
            enterpassword2_entry.place(x=150, y=200)
            enterbuisnissname=Label(root, font=("Arial",15), text=" Enter buisness name:")
            enterbuisnissname.place(x=10, y=120)
            enterbuisnissname_entry=Entry(root)
            enterbuisnissname_entry.place(x=180, y=120)
            back3=Button(root, text='Back', width=18, height=3, bd='10', command=account_destroyer)
            back3.place(x=1, y=1)
            enter2=Button(root, text='Enter', width=10, height=2, bd='10', bg='white', command=new_account_considaration)
            enter2.place(x=10, y=240)
        def log_in():
            def logged_in():
                global logged_account
                logged_account=True
                accounts_destroyer()
            def bad():
                global deleter
                global destroy_label
                global bad_label
                global destroy_label1
                if deleter==0:
                    deleter=1
                    bad_label=Label(root, font=("Arial",20), text="Incorrect password or email", bg='red')
                    bad_label.place(x=120, y=160)
            def good():
                global deleter
                global destroy_label
                global bad_label
                destroy_label=0
                if deleter==1:
                    bad_label.destroy()
                    logged_in()
            c.send(bytes("rqst_acu", 'utf-8'))
            email=email_entry.get()
            email_len1=len(email)
            password=password_entry.get()
            password_len=len(password)
            if email_len1>9:
                c.send(bytes("2", 'utf-8'))
            else:
                c.send(bytes("1", 'utf-8'))
            c.send(bytes(str(email_len1), 'utf-8'))
            c.send(bytes(str(email), 'utf-8'))
            if password_len>9:
                c.send(bytes("2", 'utf-8'))
            else:
                c.send(bytes("1", 'utf-8'))
            c.send(bytes(str(password_len), 'utf-8'))
            c.send(bytes(str(password), 'utf-8'))
            email_confirm=str(c.recv(10).decode())
            if email_confirm=="password_c":
                good()
            if email_confirm=="password_b":
                bad()
        if logged_account==False:
            mountain_buisnesses.destroy()
            mountain_news.destroy()
            mountain_statistics.destroy()
            mountan_accouts.destroy()
            back=Button(root, text='Back', width=18, height=3, bd='10', command=accounts_destroyer)
            back.place(x=10, y=10)
            email_entry=Entry(root)
            email_entry.place(x=100, y=80)
            email_label=Label(root, font=("Arial",15), text="Email:")
            email_label.place(x=10, y=81)
            password_entry=Entry(root)
            password_entry.place(x=90, y=120)
            password_label=Label(root, font=("Arial",15), text="Password:")
            password_label.place(x=10, y=120)
            enter=Button(root, text='Enter', width=10, height=2, bd='10', bg='white', command=log_in)
            enter.place(x=10, y=160)
            new_account1=Label(root, font=("Arial",15), text="Don't have a account? To make a new one")
            new_account1.place(x=10, y=200)
            new_account2=Button(root, text='Click here!', width=10, height=2, bd='10', bg='white', command=new_account)
            new_account2.place(x=300, y=199)
        if logged_account==True:
            pass
    changer=0
    changer2=0
    if changer4==1:
        root.after(1001, changer3l)
        changer4=0
    integer=0
    global deleter
    global logged_account
    deleter=0
    if logged_account==False:
        types="Log/sing in"
    if logged_account==True:
        types="Log out"
    mountain_statistics = Button(root, text='Statistics', width=14, height=3, bd='10', command=statistics)
    mountain_statistics.place(x=10,y=10)
    mountain_news = Button(root, text='News', width=14, height=3, bd='10', command=news)
    mountain_news.place(x=180,y=10)
    mountain_buisnesses=Button(root, text='Buisnesses', width=14, height=3, bd='10', command=buisnesses)
    mountain_buisnesses.place(x=350, y=10)
    mountan_accouts=Button(root, text=types, width=14, height=3, bd='10', command=accounts)
    mountan_accouts.place(x=520, y=10)
#    img1=PhotoImage(file='Picture1.png')
 #   picture1=Label(root, image=img1)
  #  picture1.place(x=20, y=35)


def main_animation1():
    def main_animation1_destroyer():
        def main_animation2():
            def main_animation2_destroyer():
                animation2.destroy()
                main()
            animation2=Label(root, font=("Arial",50), text="Mount Etna inhabitant app")
            animation2.place(x=10, y=70)
            root.after(1500, main_animation2_destroyer)
        main_animation2()
        animation1.destroy()
    animation1=Label(root, font=("Arial",90), text="Created by ADJ")
    animation1.place(x=10, y=70)
    main_animation1_destroyer()
    c.connect(('localhost', 1119))
main_animation1()

root.mainloop()
c.send(bytes("levesver", 'utf-8'))
c.close()
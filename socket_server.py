import socket
import time
import threading
from _thread import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

ip_adress='localhost'
s.bind((ip_adress, 1119))
s.listen(3)

looking=""
counter=0

def clinet(c):
    global looking
    global counter
    print(addr, "in lobby")
    while True:
        recieved_msg=str(c.recv(8).decode())
        counter=0
        if recieved_msg=="rqst_bna":
            print("opening buisnissnames.txt")
            def read():
                reader=open("buisnissnames.txt", "r")
                for repeater in range(18):
                    name=reader.readline().strip()
                    len_name=len(str(name))
                    len_len_name=len(str(len_name))
                    c.send(bytes(str(len_len_name), "utf-8"))
                    c.send(bytes(str(len_name), "utf-8"))
                    c.send(bytes(str(name), "utf-8"))
                return
            read()
            leveorstay=str(c.recv(4).decode())
            if leveorstay=="leve":
                reader.close()
            else:
                read()
        if recieved_msg=="levesver":
            break
        if recieved_msg=="rqstnacu":
            len_nemail=int(c.recv(2).decode())
            nemail=str(c.recv(len_nemail).decode())
            emails=open("email.txt", "a")
            emails.write(nemail)
            emails.write("\n")
            emails.close()
            len_len_nenterbuisnissname=int(c.recv(1).decode())
            len_nenterbuisnissname=int(c.recv(len_len_nenterbuisnissname).decode())
            nenterbuisnissname=str(c.recv(len_nenterbuisnissname).decode())
            fbuisnissname=open("buisnissnames.txt", "a")
            fbuisnissname.write(nenterbuisnissname)
            fbuisnissname.write("\n")
            fbuisnissname.close()
            len_len_npassword=int(c.recv(1).decode())
            len_npassword=int(c.recv(len_len_npassword).decode())
            npassword=str(c.recv(len_npassword).decode())
            fnpasswords=open("passwords.txt", "a")
            fnpasswords.write(npassword)
            fnpasswords.write("\n")
            fnpasswords.close()
        if recieved_msg=="rqst_acu":
            print(addr[0], "requested account system")
            capacity1=int(c.recv(1).decode())
            capacity2=int(c.recv(capacity1).decode())
            email=str(c.recv(capacity2).decode())
            capacity3=int(c.recv(1).decode())
            capacity4=int(c.recv(capacity3).decode())
            password=str(c.recv(capacity4).decode())
            counter=0
            f=open("email.txt")
            line=f.readline()
            confirment=False
            while line!="" or line==email:
                line=str(f.readline().strip())
                counter=counter+1
                if email==line:
                    #c.send(bytes("password_c", 'utf-8'))
                    confirment=True
                    break
            if confirment==True:
                f.close()
                f=open("passwords.txt")
                for i in range(counter):
                    line=str(f.readline().strip())
                f.close()
            if line==password and confirment==True:
                c.send(bytes("password_c", 'utf8'))
            else:
                c.send(bytes("password_b", 'utf8'))
        if recieved_msg=="rqst_sts":
            looking="stats"
            f=open("percentage_of_exploding.txt")
            percentage_of_exploding=str(f.readline())
            len_percentage=len(percentage_of_exploding)
            if len_percentage==2:
                percentage_of_exploding="0" + percentage_of_exploding
            if len_percentage==1:
                percentage_of_exploding="00" + percentage_of_exploding
            c.send(bytes(str(percentage_of_exploding), 'utf-8'))
            f.close()
        if recieved_msg=="rqst_nws":
            print(addr, "reqested news")
            f=open("news.txt")
            news=0
            while news!="":
                news=f.readline().strip()
                counter=counter+1
            f.close()
            c.send(bytes(str(counter), 'utf-8'))
            f=open("news.txt")
            for i in range(counter):
                news=f.readline().strip()
                len_news=len(news)
                print("len_len:  ", len_news)
                len_len_news=len(str(len_news))
                print(len_len_news)
                c.send(bytes(str(len_len_news), "utf-8"))
                c.send(bytes(str(len_news), "utf-8"))
                c.send(bytes(str(news), 'utf-8'))
            f.close()
    c.close()

print("waiting for connections, ip: ", ip_adress)

while True:
    c, addr = s.accept()
    print(addr[1], "has connected to the server!")
    print(c, addr)
    start_new_thread(clinet, (c,))

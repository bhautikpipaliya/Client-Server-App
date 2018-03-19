from socket import *
import math

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("localhost",8888))
print clientSocket.recv(1024)
clientSocket.send("HELLO pipaliya.b\n")

while True:
           s = clientSocket.recv(2048)
           print(s)
           if s[0] == "D" and s[1] == "O" :
              break

           stringsplit = s.split(" ")
	 
	   
           x = int(stringsplit[1])
           y = int(stringsplit[3])
	
           

           if s[7] == "*" or s[9] == "*" or s[8] == "*":
              answer = x * y
              clientSocket.send("ANSWER" +" "+ str(answer) + "\n")

           if s[7] == "+" or s[9] == "+" or s[8] == "+":
              answer = x + y
              clientSocket.send("ANSWER" +" "+ str(answer) + "\n")

           if s[7] == "-" or s[9] == "-" or s[8] == "-":
              answer = x - y
              clientSocket.send("ANSWER" +" "+ str(answer) + "\n")

           if s[7] == "/" or s[9] == "/" or s[8] == "/":
              answer = x / y
              clientSocket.send("ANSWER" +" "+ str(answer) + "\n")



                   


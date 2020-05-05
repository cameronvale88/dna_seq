#!/usr/bin/python3

#Version 2 is a bit more refined that version 1 and will not store the results to a file.


import random
import os
import time

def purpose():
    print("This program is designed to generate a random sequence of DNA based on your specifications.")
    time.sleep(2)
    print("")
    print("You will be asked a series of questions that will determine the size of the sequence and")
    time.sleep(2)
    print("")
    print("the pattern it will be displayed.")
    print("")
    time.sleep(3)

def bases():
  num = input("How many base pairs would you like? ")
  return num

def break_l():
  breakpoint = input("How many sequences wide would you like before I start a new line? ")
  return breakpoint

def line():
  line_break = input("How many rows would you like before clearing the screen? ")
  return line_break


purpose()

num = bases()
breakpoint=break_l()
line_break=line()


list = []

if str(num.isdigit()) == "False" or str(breakpoint.isdigit()) == "False" or str(line_break.isdigit()) == "False":
    while str(num.isdigit()) == "False" or str(breakpoint.isdigit()) == "False" or str(line_break.isdigit()) == "False":
        print("Please try again.")
        print("This program can only accept integers.")
        num = input("how long? ")
        os.system('clear')
        os.system('clear')
        breakpoint = input("where should I start a new line? ")
        os.system('clear')
        os.system('clear')
        line_break=input("how many before clearing the screen? ")
        if str(num.isdigit()) == "True" and str(breakpoint.isdigit()) == "True" and str(line_break.isdigit()) == "True":
            break

num2=int(num)
breakpoint2=int(breakpoint)
line_break2=int(line_break)



for x in range(num2):
    x=random.randrange(1,5)
    list.append(x)
    if len(list) == num2:
        s=str(list).replace(" ","").replace(",","").replace("[","").replace("]","").replace("1","a").replace("2","t").replace("3","g").replace("4","c")

n=int(0)
p=int(breakpoint2)
lines=int(0)
value = len(s)/breakpoint2
sequence = []
clear=int(0)



while lines < value:
    print(s[n:p])
    if clear == (line_break2 - 1):
        os.system("clear")
#        os.system("cls")
        clear=int(0)
    else:
        clear=clear+1
    write=s[n:p]
    sequence.append(write)
    n=int(n+breakpoint2)
    p=int(p+breakpoint2)
    lines=lines+1

lastline=int(num2-(len(s)%breakpoint2))
print(s[lastline:])

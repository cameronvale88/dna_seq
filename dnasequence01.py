#!/usr/bin/python
#!/usr/bin/python

import random

num = input("How many base pairs would you like? ")

breakpoint = input("where should I start a new line? ")

line_break=input("how many rows before clearing the screen? ")

list = []

if str(num.isdigit()) == "False" or str(breakpoint.isdigit()) == "False" or str(line_break.isdigit()) == "False":
    while str(num.isdigit()) == "False" or str(breakpoint.isdigit()) == "False" or str(line_break.isdigit()) == "False":
        print("Please try again.")
        print("This program can only accept integers.")
        num = input("How many base pairs would you like? ")

        breakpoint = input("where should I start a new line? ")

        line_break=input("how many before clearing the screen? ")
        if str(num.isdigit()) == "True" and str(breakpoint.isdigit()) == "True" and str(line_break.isdigit()) == "True":
            break
num2=int(num)
breakpoint2=int(breakpoint)
line_break2=int(line_break)
print("processing")


for x in range(num2):
    x=random.randrange(1,5)
    list.append(x)
    if len(list) == num2:
        s=str(list).replace(" ","").replace(",","").replace("[","").replace("]","").replace("1","a").replace("2","t").replace("3","g").replace("4","c")

n=int(0)
p=int(breakpoint2)
lines=int(0)
value = len(s)/breakpoint2
file = open("sequences", 'a')
clear=int(0)

while lines < value:
    print(s[n:p])
    if clear == line_break2-1:
        os.system("clear")
        clear=int(0)
    else:
        clear=clear+1
    write=s[n:p]
    file.write(write)
    file.write("\n")
    n=int(n+breakpoint2)
    p=int(p+breakpoint2)
    lines=lines+1

lastline=int(num2-(len(s)%breakpoint2))
print(s[lastline:])
finalwrite=s[lastline:]
file.write(finalwrite)
file.write("\n")
file.close()

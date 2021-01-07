#My first Advent of Code

f = open("/home/anouxis/TrySomethingElse/AdventOfCode/E01/input.txt")
mylist = f.readlines()
f.close()

for i in mylist:
    for j in mylist:
        if int(i)+ int(j) == 2020:
            print (int(i)*int(j))

#%%


f = open("/home/anouxis/TrySomethingElse/AdventOfCode/E01/input.txt")
mylist = f.readlines()
f.close()

for i in mylist:
    for j in mylist:
        for k in mylist:
            if int(i)+ int(j) + int(k) == 2020:
                print (int(i)*int(j)*int(k))

p = open("file.txt", "r")
l = p.readlines()
print(l)
sum = 0
for i in l:
    r = i.count(" ") + 1
    sum = sum + r
print("Number of char is sum:",sum)
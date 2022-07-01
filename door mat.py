#still a work in progress

n = int(input())
m = (n*3)

if (n%2) == 1 :
    x = int((n-1)/2) #number of top/bottom rows

    y = int(((m-7)/2)) #number of '-'s in one part of the middle row
    c = "-"
    d = ".|."

    #top part
    for i in range(x+1):
        print(i*d)

    #middle part
    print (f"{(y*c)}WELCOME{y*c}")

    #bottom part
    for i in range(x+1):
        print(i*d)



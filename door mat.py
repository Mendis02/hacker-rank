n, m = input().split()
n = int(n)
m = int(m)


if (n%2) == 1 :
    x = int((n-1)/2) #number of top/bottom rows

    y = int(((m-7)/2)) #number of '-'s in one part of the middle row
    c = "-"
    d = ".|."

    #top part
    for i in range(1,x+1):
        print(int((m-(6*i-3))/2)*c +(2*i-1)*d+int((m-(6*i-3))/2)*c )

    #middle part
    print (f"{(y*c)}WELCOME{y*c}")

    #bottom part
    for i in range(1,x+1):
        print((3*i)*c+int((m-6*i)/3)*d+(3*i)*c)



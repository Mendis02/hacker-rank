import re

if __name__ == '__main__':
    s = input()
    

    #checking alphanumerics
    y = re.findall("\w", s)

    #checking digits
    x = re.findall("\d", s)

    #if all the characters are digits
    z = s.isdigit()


    # alphanumerics
    if y:
        print("True")
    else:
        print("False")


    #alphabetics
    if y:
        if z is False:
            print("True")
        else:
            print("False")
    else:
        print('False')


    #digits
    if x:
        print('True')
    else:
        print('False')


    #lower case
    l1 = []

    for c in s:
        if c.islower():
            l1.append(c)
    if len(l1) > 0:
        print("True")
    else:
        print("False")

    #upper case
    l2 = []

    for d in s:
        if d.isupper():
            l2.append(d)
    if len(l2)>0:
        print("True")
    else:
        print("False")


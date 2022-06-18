if __name__ == '__main__':
    n = int(input('how many commands? '))
    i = 1
    the_list = []
    while i <= n:
    # used a 'while' loop , can also use a 'for' loop (which might be easier)

        operation = input('command: ')
        backstage = operation.split()
    #inserting the input into a list

        if backstage[0] == "print" :
            print(the_list)
            i = i+1    #have repeated the same code
        else:
            if backstage[0] == "append":
                the_list.append(backstage[1])
                i = i + 1
            else:
                if backstage[0] == "sort":
                    the_list.sort()
                    i = i + 1
                else:
                    if backstage[0] == "pop":
                        the_list.pop()
                        i = i + 1
                    else:
                        if backstage[0] == "reverse":
                            the_list.reverse()
                            i = i + 1
                        else:
                            if backstage[0] == "remove":
                                the_list.remove(backstage[1])
                                i = i + 1
                            else:
                                if backstage[0] == "insert":
                                    the_list.insert(backstage[2] , backstage[1]) 
                                    #this is not working
                                    i = i + 1
                                    break


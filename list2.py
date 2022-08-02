if __name__ == '__main__':
    n = int(input(''))
    i = 1
    the_list = []
    while i <= n:
        # used a 'while' loop , can also use a 'for' loop (which might be easier)

        operation = input('')
        backstage = operation.split()
        # inserting the input into a list

        if backstage[0] == "print":
            print(the_list)
            i = i + 1
        else:
            if backstage[0] == "append":
                the_list.append(backstage[1])
                i = i + 1
            else:
                if backstage[0] == "sort":     #sorting is not working correctly

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
                                if backstage[1] in the_list:
                                    the_list.remove(backstage[1])
                                    i = i + 1
                                else:
                                    i = i + 1
                            else:
                                if backstage[0] == "insert":
                                    position = backstage[1]
                                    the_list.insert(int(position), backstage[2])
                                    i = i + 1

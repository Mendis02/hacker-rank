def count_substring(string, sub_string):
    l = list(string)
    main_count = 0
    for i in l:
        if i == sub_string[0]:
            s = ''.join(l)
            count = s.count(sub_string)
            l = list(s)

            if count >= 1:
                main_count = main_count + 1

            if len(l) > len(sub_string):
                for x in range(len(sub_string) ):
                    l.pop(0)
    return main_count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
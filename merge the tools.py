def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        l = string[i:i + k]
        uniques = set()

        for i in l :
            if i not in uniques:
                print(i, end='')
                uniques.add(i)
        print()



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

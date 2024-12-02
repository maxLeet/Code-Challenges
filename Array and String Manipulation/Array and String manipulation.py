## Write a function to find the first non-repeating character in a string.

def first_non_repeating(str):
    print(str)
    iter = 0
    char_list = {}
    while iter < len(str):
        if string1[iter] not in char_list:
            char_list[str[iter]] = 1
        else:
            char_list[str[iter]] += 1
        iter+=1

    for x in char_list:
        if char_list[x] == 1:
            print(x)
            return
    print(char_list)

string1 = 'a list of not repeating characters' ##should return 'l'
first_non_repeating(string1)

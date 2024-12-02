# Given two strings, determine if one is a permutation of the other.
class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
def two_of_a_kind(s1, s2):
    #print("Length of array - ", len(s2))
    for v in range(0, len(s2)):
        #print("current index: ", v)
        if s2[v] in s1:
            #print("Replacing: ", s2[v])
            s1 = s1.replace(s2[v], '')
    if s1 != '':
        return False
    else:
        return True

def assertion(bool):
    if bool == True:
        return "Enumeration "+Colors.GREEN+"matched"+Colors.END
    else:
        return "Enumeration "+Colors.RED+"did not"+Colors.END+" matched"
if __name__ == '__main__':
    file = 'wordlist.txt'
    wordlist = open(file, 'r')
    newlist = []

    for x in wordlist:
        newlist.append(x.strip().split(' '))
    for x in newlist:
        #print(two_of_a_kind(x[0], x[1]))
        print(assertion(two_of_a_kind(x[0].lower(), x[1].lower())), x[0]," : ",x[1])
    #print( two_of_a_kind(str1.lower(), str2.lower()) )

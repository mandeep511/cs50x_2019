from cs50 import get_int

def main():
    print_p(get_num())

def get_num():
    while True:
        n = get_int("Enter a number between 1 and 8 here: ")
        # range() 2nd argument is like x < 2nd argument 
        # meaning range will be 1 to 7 if we say range(1, 8)
        if n in range(1, 9):
            break
    return n

def print_p(n):
    i = 0
    while i <= n:
        k = n
        while k > i:
            # Python print function ends with \n if we want to change that we add another argument end
            # print in python is powerfull 
            print(" ", end="")
            k -= 1
        j = 0
        while j < i:
            # Python print function ends with \n if we want to change that we add another argument end
            # print in python is powerfull 
            print("#", end="")
            j += 1
        print("")
        i += 1
main()
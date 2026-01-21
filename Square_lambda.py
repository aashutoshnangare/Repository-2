sqr = lambda No : (No * No)

def main():

    print("Enter the number :")
    value = int(input())

    Ret = sqr(value)
    print("The Square of number is",Ret)

if __name__ == "__main__":
    main()
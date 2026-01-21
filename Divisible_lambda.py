Divisble = lambda No : (No % 5 == 0)

def main():

    print("Enter the Number")
    value = int(input())

    Ret = Divisble(value)

    if Ret == True:
        print("The Number",value,"divisble by 5")
    
    else:
        print("The Number",value,"is not divisble by 5")

if __name__ == "__main__":
    main()
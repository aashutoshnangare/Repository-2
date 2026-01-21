Maximum = lambda No1,No2 : (No1 if No1 > No2 else No2)

def main():

    value1 = int(input("Enter the number 1 :"))
    value2 = int(input("Enter the number 2 :"))

    Ret =  Maximum(value1,value2)

    print("The maximum number is :",Ret)

if __name__ == "__main__":
    main()
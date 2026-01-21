Minimum = lambda No1,No2 : (No1 if No1 > No2 else No2)

def main():

    value1 = int(input("Enter the number 1 :"))
    value2 = int(input("Enter the number 2 :"))

    Ret =  Minimum(value1,value2)

    print("The Minimum value is :",Ret)

    
if __name__ == "__main__":
    main()
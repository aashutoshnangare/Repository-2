Largest = lambda No1, No2, No3: No1 if (No1 >= No2 and No1 >= No3) else (No2 if No2 >= No3 else No3)

def main():

    Value1 = int(input("Enter The Number 1 :"))
    Value2 = int(input("Enter The Number 2 :"))
    Value3 = int(input("Enter The Number 3 :"))

    Ret = Largest(Value1,Value2,Value3)
    print("The Largest Number is",Ret)

if __name__ == "__main__":
    main()
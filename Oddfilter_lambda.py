ChkOdd = lambda No : (No % 2 == 1 )

def main():
    Datax = [2,3,4,5,6,7,8,9,10]
    print("Actual data is :",Datax)

    Fdata = list(filter(ChkOdd,Datax))
    print("Data after Filtering is:",Fdata)

if __name__ == "__main__":
    main()
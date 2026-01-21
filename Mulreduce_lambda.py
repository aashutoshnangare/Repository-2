from functools import reduce

Mul = lambda No1 , No2 : (No1 * No2)

def main():
    Datax = [2,3,4,5,6,7,8,9,10]
    print("Actual data is :",Datax)

    Rdata = reduce(Mul,Datax)
    print("Data after Filtering is:",Rdata)

if __name__ == "__main__":
    main()
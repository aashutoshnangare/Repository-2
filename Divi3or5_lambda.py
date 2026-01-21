
DivisibleBy3And5 = lambda data:  data % 3 == 0 and data % 5 == 0 

def main():
    
    Datax =  [3, 5, 7, 10, 15]

    print("Actual data is :",Datax)

    Fdata = list(filter(DivisibleBy3And5,Datax))
    print("Data after Filtering is:",Fdata)


if __name__ == "__main__":
    main()

Accept_list = lambda No : (No * No)

def main():

    Datax = [2,3,4,5,6,7,8,9,10]
    print("Actual data is :",Datax)

    Mdata = list(map(Accept_list,Datax))
    print("Data after mapping is:",Mdata)

if __name__ == "__main__":
    main()
Count = lambda Data : Data if len(Data) > 5 else 0

def main():

    Datax = ["Hi","Python","Cricket","And","Football","Bye"]
    print("Actual data is :",Datax)

    Fdata = list(filter(Count,Datax))
    print("Data after Filtering is:",Fdata)

if __name__ == "__main__":
    main()

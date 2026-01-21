

even = lambda No : (No % 2 == 0)
   
def main():

    print("Enter the  number : ")
    value = int(input())

    ret = even(value)

    if ret == True:
        print("It is even")
    else:
        print("It is odd")
  
     
if __name__ == "__main__":
    main()
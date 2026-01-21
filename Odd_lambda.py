

odd = lambda No : (No % 2 == 1)
   
def main():
    value = 0
    ret = False

    print("Enter the  number : ")
    value = int(input())

    ret = odd(value)

    if (ret == True):
        print("It is odd")
    else:
        print("It is even")
  
     
if __name__ == "__main__":
    main()
import time,sys
def collatz(number):
    try:
        isEven = number % 2 == 0
        isOdd = number % 2 != 0
        if isEven:
            o = number // 2
            print(o)
            return o
        elif isOdd:
            o = 3 * number + 1
            print(o)
            return o
    except TypeError:
        print("error...")
        sys.exit()
        
print("Enter a number")
user = input('>')
try:
    user = int(user)  
except ValueError:
    print("Error...")
    sys.exit()
try:  
    while True:
        p = collatz(user)
        time.sleep(.1)
        user = p
        if p == 1:
            break
except KeyboardInterrupt:
    sys.exit()
    

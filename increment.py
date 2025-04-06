class Number():
    def __init__(self, arr):
        self.left = arr[0]
        self.right = arr[1]
        self.resetLeft = arr[0]
        self.resetRight = arr[1]
    def increment(self):
        self.left += 1
        self.right -= 1          
        return [self.left,self.right]
    
myNumber = Number([1,3])
print([myNumber.left,myNumber.right])

iterations = 0
while myNumber.left <= myNumber.right:
    iterations += 1
    myNumber.increment()
print(f"{[myNumber.left,myNumber.right]} in {iterations} steps from {[myNumber.resetLeft,myNumber.resetRight]}")
        

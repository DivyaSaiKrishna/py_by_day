class adder:
    def __init__(self, a, b):
        self.a = a 
        self.b = b
    
    def add(self) -> int:
        sum = lambda : self.a + self.b
        print(sum())
        result = sum()
        print(result)
        return result

if __name__ == "__main__":
    addCheck = adder(4,5)
    print(addCheck.add()) 
    addTwo = lambda num : num + num
    print(addTwo(3))
    checkNum = lambda checkN : "High" if checkN > 50 else "Low"
    print(checkNum(7))
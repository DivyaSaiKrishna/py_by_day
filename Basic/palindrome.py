import re

def checkPalindrome (data):
    for i in data:

        checkStr = re.sub(r'[^A-Za-z0-9]','',i).lower();

        print(checkStr)

        
        if(checkStr == checkStr[::-1]):
            print("palindrome")
        else:
            print("not palindrome")


if __name__ == "__main__":
    data = ["car", "data", "vikatakavi", "John", "eye", "A Man, A Plan, A Canal – Panama!"]
    checkPalindrome(data)
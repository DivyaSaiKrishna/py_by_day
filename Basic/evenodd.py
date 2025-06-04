def checkEvenOdd(data):
    for i in data:
        if i%2 == 0:
            print(f" {i} is even")
        else:
            print(f" {i} is odd")



if __name__ == "__main__":
    data = [12, 35, 1, 10, 34, 1]
    checkEvenOdd(data)
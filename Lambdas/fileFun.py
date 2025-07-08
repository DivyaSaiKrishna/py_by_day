def add(n1, n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2 if n1 > n2 else n2-n1

def multiply(n1,n2):
    return n1 * n2

def calculations(operation, n1, n2):
    return operation(n1,n2)

print(calculations(multiply,6,5))

print(calculations(sub,6,13))

print(calculations(add,6,5))

num_list = [30, -2, 15, 17, -9, 100]
greater_than_10 = list(filter(lambda n: n > 10 , num_list))

print(num_list)
print(greater_than_10)
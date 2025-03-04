def second(data):
    largest = -1;
    second = -1;
    for rec in data:
        if rec > largest :
            second = largest;
            largest = rec;

        elif rec < largest and rec > second:
            second = rec;
    print(second);

if __name__ == "__main__":
    data = [12, 35, 1, 10, 34, 1]
    second(data)
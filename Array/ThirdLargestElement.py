def third(data):
    largest = -1;
    second = -1;
    third = -1;
    for rec in data:
        if rec > largest :
            third = second;
            second = largest;
            largest = rec;

        elif rec < largest and rec > second:
            third = second
            second = rec;

        elif rec < second and rec > third:
            third = rec;

        
        
    print(third);

if __name__ == "__main__":
    data = [12, 35, 1, 10, 34, 1]
    third(data)
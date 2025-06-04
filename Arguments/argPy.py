def average_of_numbers(*args):
    if not args :
        return 0
    return sum(args) / len(args)

def print_student_info(**kwargs):
    if not kwargs :
        return "nothing"

    print("student ")
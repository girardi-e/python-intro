grade = input("Enter grade(A,B,C,D,F): ")

match(grade):
    case("A"):
        print("Excellent job!")
    case("B"):
        print("Well done!")
    case("C"):
        print("Good job!")
    case("D"):
        print("You've got work to do.")
    case("F"):
        print("You've failed")
    case _:
        print("You hopeless!")

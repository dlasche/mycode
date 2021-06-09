with open("students.txt", "r") as x:
    for line in x:
        print(line.strip("\n"))
print("thanks to a unindent, this file is now automatically closed!")


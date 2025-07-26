with open("output.txt", "w") as file:
    n = str(input("Enter text to write to the file: "))
    file.write(n)
    print("Data successfully written to output.txt\n")

with open("output.txt", "a") as file:
    x = str(input("Enter additonal text to append: "))
    file.write(f"\n{x}")
    print("Data successfully appended to output.txt\n")

with open("output.txt", "r") as file:
    print("Final content of output.txt:\n")
    print(file.read())
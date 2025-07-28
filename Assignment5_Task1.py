Student = {
    "Mandeep" : 98,
    "Mandy" : 99,
    "Alice" : 89,
    "Anuj" : 97
}
n = str(input("Enter the student name: "))
marks = Student.get(n)

if marks:
    print(f"{n} marks: {marks}")
else:
    print("Student not found")
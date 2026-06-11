name = input("Enter Student Name: ")

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n========== MARKSHEET ==========")
print("Student Name :", name)
print("Subject 1  :", sub1)
print("Subject 2  :", sub2)
print("Subject 3  :", sub3)
print("Subject 4  :", sub4)
print("Subject 5  :", sub5)

print("Total Marks :", total, "/ 500")
print("Percentage  :", percentage, "%")
print("Grade       :", grade)
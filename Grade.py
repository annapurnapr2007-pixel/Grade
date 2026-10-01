n = int(input("Enter number of subjects: "))

passed = True

for i in range(1, n + 1):
    marks = float(input(f"Enter marks for subject {i}: "))

    if marks < 35:
        passed = False

if passed:
    print("Result: PASS")
else:
    print("Result: FAIL")
    marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")
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
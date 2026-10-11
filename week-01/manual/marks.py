marks = input("Enter marks: ").split(",")
valid = []

for mark in marks:
    try:
        number = float(mark.strip())
        if 0 <= number <= 100:
            valid.append(number)
    except ValueError:
        continue

if not valid:
    print("No valid marks")
else:
    passed = sum(mark >= 50 for mark in valid)

    print(f"Valid marks: {len(valid)}")
    print(f"Average: {sum(valid) / len(valid):.2f}")
    print(f"Highest: {max(valid):g}")
    print(f"Lowest: {min(valid):g}")
    print(f"Pass rate: {passed / len(valid) * 100:.1f}%")
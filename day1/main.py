f = open("input.txt", "r")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    first_digit = None
    second_digit = None
    for digit in line:
        if digit.isnumeric():
            if first_digit is None:
                first_digit = digit
            second_digit = digit
    total += int(first_digit + second_digit)
print(total)

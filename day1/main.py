f = open("input.txt", "r")
lines = f.readlines()
f.close()

name_to_string = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

total = 0
for line in lines:
    first_digit = None
    second_digit = None

    for i in range(len(line)):      
        word = line[i:i+5]
        if word in name_to_string:
            line = line.replace(word, name_to_string[word])
            i += 5
        else:
            word = line[i:i+4]
            if word in name_to_string:
                line = line.replace(word, name_to_string[word])
                i += 4
            else:
                word = line[i:i+3]
                if word in name_to_string:
                    line = line.replace(word, name_to_string[word])
                    i += 3
                else:
                    word = line[i:i+2]
                    if word in name_to_string:
                        line = line.replace(word, name_to_string[word])
                        i += 2
                    else:
                        word = line[i:i+1]
                        if word in name_to_string:
                            line = line.replace(word, name_to_string[word])
                            i += 1

    for digit in line:
        if digit.isnumeric():
            if first_digit is None:
                first_digit = digit
            second_digit = digit
    total += int(first_digit + second_digit)
print(total)

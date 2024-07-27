nice_words_counter = 0

with open("input1.txt") as file:
    for line in file:
        vowel_counter = 0
        double_letter = 0
        disallowed_string = 0
        prev_letter = ""
        if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
            disallowed_string = 1
            print(line)
        for letter in line:
            if prev_letter == letter:
                double_letter += 1
            if letter in "aeiou":
                vowel_counter += 1
            prev_letter = letter
        if disallowed_string == 0 and double_letter > 0 and vowel_counter > 2:
            nice_words_counter += 1

print(nice_words_counter)

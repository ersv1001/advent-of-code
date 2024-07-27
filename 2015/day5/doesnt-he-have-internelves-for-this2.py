nice_words_counter = 0

with open("input1.txt") as file:
    for line in file:
        repeat_sandwich = 0
        prev_letter = "1"
        prev_prev_letter = "1"
        letter_counter = 0
        double_pair = 0
        for letter in line:
            if prev_prev_letter == letter:
                repeat_sandwich += 1
            if prev_letter + letter in line[letter_counter + 1 :]:
                double_pair += 1
            letter_counter += 1
            prev_prev_letter = prev_letter
            prev_letter = letter

        if repeat_sandwich > 0 and double_pair > 0:
            nice_words_counter += 1

print(nice_words_counter)

import hashlib

md5 = hashlib.md5
input_file = open("input1.txt", "r")
input = input_file.read()

counter = 0


def check_hash(hash_input):
    result = md5(hash_input.encode())
    result_hex = result.hexdigest()
    if result_hex[:6] == "000000":
        return True
    return False


while check_hash(input + str(counter)) is False:
    counter += 1

print(counter)

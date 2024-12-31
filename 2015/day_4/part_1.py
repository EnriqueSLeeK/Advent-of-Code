
import hashlib

string_key_base = 'yzbqklnj'

i = 0
while True:
    hash = hashlib.md5((f"{string_key_base}{i}").encode())

    # Part 2
    # if str(hash.hexdigest()[:6]) == '000000':

    # Part 1
    if str(hash.hexdigest()[:6]) == '00000':
        print(i)
        print(hash.hexdigest())
        break
    i += 1

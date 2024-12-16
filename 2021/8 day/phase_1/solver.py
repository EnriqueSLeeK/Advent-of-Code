with open("input", "r") as f:
    codes = [[sequence for sequence in code.split('|')[1].split()] for code in f]

count = 0
for seq_list in codes:
    for seq in seq_list:
        len_seq = len(seq)
        if (len_seq == 2 or
            len_seq == 4 or
            len_seq == 3 or
            len_seq == 7):
            count += 1
print(count)

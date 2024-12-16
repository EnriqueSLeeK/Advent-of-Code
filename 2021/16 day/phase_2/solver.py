from math import prod

with open("input", "r") as f:
    transmission = f.readline().strip()

def hex_to_bin(digit):
    binary = bin( int(digit, 16) )[2:]
    return ("0" * (4 - len(binary)) + binary)

transmission_bin = ""

for k in range(len(transmission)):
    transmission_bin += hex_to_bin( transmission[k] )

pivot = 0

def operation(op, elem_list):
    if (op == 0):
        return (sum(elem_list))
    elif (op == 1):
        return (prod(elem_list))
    elif (op == 2):
        return (min(elem_list))
    elif (op == 3):
        return (max(elem_list))
    elif (op == 5):
        return (int(elem_list[0] >  elem_list[1]))
    elif (op == 6):
        return (int(elem_list[0] <  elem_list[1]))
    elif (op == 7):
        return (int(elem_list[0] == elem_list[1]))

def get_literal_val():
    global pivot
    literal_val = ""
    while (True):
        segment = transmission_bin[pivot: pivot + 5]
        pivot += 5
        literal_val += segment[1: len(segment)]
        if (segment[0] == '0'):
            break
    return(int(literal_val, 2))

def i_zero(total_len, ref, op):
    global pivot
    numbers = []
    while (pivot - ref < total_len):
        numbers.append(packet_parsing(get_header()))
    return (operation(op, numbers))

def i_one(total_quant, op):
    numbers = []
    for k in range(total_quant):
        numbers.append(packet_parsing(get_header()))
    return (operation(op, numbers))

def packet_parsing(header):
    global pivot
    version, mode = header
    if (mode == 4):
        return (get_literal_val())
    else:
        len_id = int(transmission_bin[pivot: pivot + 1], 2)
        pivot += 1

        if (len_id == 0):
            subpacket_total_len = int(
                    transmission_bin[pivot: pivot + 15], 2)
            pivot += 15
            return (i_zero(subpacket_total_len, pivot, mode))

        elif (len_id == 1):
            subpacket_total_quant = int(
                    transmission_bin[pivot: pivot + 11], 2) 
            pivot += 11
            return (i_one(subpacket_total_quant, mode))

def get_header():
    global pivot, version_sum
    version = int(transmission_bin[pivot: pivot + 3], 2)
    pivot += 3
    id = int(transmission_bin[pivot: pivot + 3], 2)
    pivot += 3
    return (version, id)

print(packet_parsing(get_header()))
